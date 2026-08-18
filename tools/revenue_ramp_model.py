"""
GTT Center Perth -- Revenue Ramp Model (deterministic calculation module).

Rebuilds the Month 1-5+ revenue ramp for Table 1 (18-client) and Table 2
(12-client) using the CANONICAL revenue methodology adopted 2026-08-09
(docs/architecture/CANONICAL-REVENUE-METHODOLOGY.md), not the inherited
historical figures. Full investigation and rationale:
docs/architecture/REVENUE-RAMP-METHODOLOGY.md.

This module contains NO unexplained hard-coded financial values. Every input
(client volume, AM/PM price, PM session capacity, operating days) is read
directly from data/canonical/*.yml by id. The one genuine modelling choice
made here -- reusing the historical 43/64/79/93/100% ramp-percentage shape --
is isolated in RAMP_CURVE below with a full citation and status, so it can be
inspected, challenged, or replaced without touching the calculation engine
itself (per the coordinator's explicit "allow the ramp curve to be changed
without rewriting the engine" requirement).

Usage:
    python tools/revenue_ramp_model.py            # print both scenarios' ramp tables
    python tools/revenue_ramp_model.py --scenario scenario_table_1
"""

import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml is required (pip install pyyaml).")
    sys.exit(2)

REPO_ROOT = Path(__file__).resolve().parent.parent
CANON_DIR = REPO_ROOT / "data" / "canonical"

# ---------------------------------------------------------------------------
# THE ONE MODELLING CHOICE THIS MODULE MAKES -- isolated, cited, changeable.
#
# Reuses the 43%/64%/79%/93%/100% ramp-percentage shape already established
# and applied identically across docs/cash-flow.md's 18-Month Monthly Ramp,
# docs/profit-loss-tables.md's Year 1 Monthly Ramp, and
# docs/investor-memorandum.md's AM GTT Revenue Monthly Ramp -- the ONLY ramp
# curve this repo has ever used, applied identically to AM and PM revenue in
# every one of those three documents (confirmed by direct arithmetic in
# docs/architecture/REVENUE-RAMP-METHODOLOGY.md §3).
#
# STATUS: MODELLED, not VERIFIED -- this is a reused planning convention, not
# an independently re-derived or externally benchmarked ramp shape. Applying
# it to the NEW canonical revenue bases (Table 1/Table 2, including PM
# Saturday, which the historical ramp tables never modelled at all) is a
# genuine, disclosed extension, not a re-verification of the historical
# figures themselves -- see docs/architecture/REVENUE-RAMP-METHODOLOGY.md §4.
#
# A competing, MUTUALLY INCONSISTENT interpretation of the PM ramp exists in
# docs/pm-staffing-roster.md (4/8/12/15/16 sessions/day = 25/50/75/93.75/100%
# of the 16-session steady-state capacity) -- this module does NOT use that
# curve for revenue (see docs/architecture/REVENUE-RAMP-METHODOLOGY.md §5 for
# the full conflict and why the blanket curve was chosen for REVENUE
# specifically, not a staffing/hours ramp, which is a separate, un-modelled
# question this phase does not resolve).
# ---------------------------------------------------------------------------
RAMP_CURVE = [
    ("M1", 43),
    ("M2", 64),
    ("M3", 79),
    ("M4", 93),
    ("M5plus", 100),
]
RAMP_CURVE_SOURCE = {
    "status": "MODELLED",
    "basis": "Reused historical ramp-percentage shape, applied identically to AM and PM revenue.",
    "sources": [
        {"file": "docs/cash-flow.md", "section": "18-Month Monthly Ramp (Rebuilt to Current Model)"},
        {"file": "docs/profit-loss-tables.md", "section": "Year 1 Monthly Ramp"},
        {"file": "docs/investor-memorandum.md", "section": "3. Financial Projections, AM GTT Revenue -- Monthly Ramp"},
    ],
}


def load_yaml(filename):
    path = CANON_DIR / filename
    with path.open(encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def find_record(records, record_id):
    for rec in records:
        if rec.get("id") == record_id:
            return rec
    raise KeyError(f"No record with id={record_id!r} found")


class CanonicalRevenueInputs:
    """Every input the canonical revenue formula (and therefore the ramp) needs,
    read by id from data/canonical/*.yml -- mirrors
    docs/architecture/CANONICAL-REVENUE-METHODOLOGY.md §3 and
    tests/test_revenue_methodology.py's CanonicalInputs."""

    def __init__(self):
        client_assumptions = load_yaml("client_assumptions.yml")
        scenarios = load_yaml("scenarios.yml")
        pricing = load_yaml("pricing.yml")
        revenue_assumptions = load_yaml("revenue_assumptions.yml")

        universal = client_assumptions["universal"]
        self.operating_days_weekday = find_record(universal, "operating_days_per_month_weekday")["value"]
        self.operating_saturdays = find_record(universal, "operating_saturdays_per_month")["value"]

        scenario_records = scenarios["records"]
        self.client_volume = {
            "scenario_table_1": find_record(scenario_records, "scenario_table_1")["client_volume"]["value"],
            "scenario_table_2": find_record(scenario_records, "scenario_table_2")["client_volume"]["value"],
        }

        pricing_records = pricing["records"]
        self.am_price = find_record(pricing_records, "am_price_used_for_revenue")["price"]
        self.pm_price = find_record(pricing_records, "pm_alacarte_average")["price"]

        rev_records = revenue_assumptions["records"]
        # CORRECTED 2026-08-18 (PM capacity/transaction reconciliation, Priority 1) --
        # PM revenue must be driven by CLIENT-TRANSACTION capacity, not raw
        # STAFF-SESSION capacity (client_assumptions.yml#pm_steady_state_capacity,
        # still correctly used for labour-hours costing in
        # tools/cost_ramp_model.py, UNCHANGED). A package transaction consumes
        # more than one staff-session, so multiplying the raw session count by
        # the average transaction price overstated PM revenue. See
        # docs/architecture/PM-CAPACITY-RECONCILIATION.md for the full
        # investigation and derivation of these two new records.
        self.pm_weekday_sessions = find_record(rev_records, "rev_pm_weekday_transactions")["value"]
        self.pm_saturday_sessions = find_record(rev_records, "rev_pm_saturday_transactions")["value"]
        self.ancillary_monthly = find_record(rev_records, "rev_ancillary_excluded_from_baseline")["value"]


def steady_state_revenue(client_volume, inputs: CanonicalRevenueInputs):
    """The canonical Month 5+ (100%) revenue -- identical formula to
    docs/architecture/CANONICAL-REVENUE-METHODOLOGY.md §4 /
    tests/test_revenue_methodology.py's compute_monthly_revenue, decomposed
    into AM/PM components so the ramp can scale each separately."""
    am_weekday = client_volume * inputs.am_price * inputs.operating_days_weekday
    am_saturday = client_volume * inputs.am_price * inputs.operating_saturdays
    pm_weekday = inputs.pm_weekday_sessions * inputs.pm_price * inputs.operating_days_weekday
    pm_saturday = inputs.pm_saturday_sessions * inputs.pm_price * inputs.operating_saturdays
    am_total = am_weekday + am_saturday
    pm_total = pm_weekday + pm_saturday
    return am_total, pm_total, am_total + pm_total


def compute_ramp(scenario_id, inputs: CanonicalRevenueInputs, ramp_curve=RAMP_CURVE):
    """Returns a list of month dicts for the given scenario, applying
    `ramp_curve`'s percentages identically to the AM and PM steady-state
    components (see RAMP_CURVE's own docstring for why AM==PM==Total under
    this specific curve, a mathematical consequence of scaling every additive
    component by the same factor, not a coincidence)."""
    client_volume = inputs.client_volume[scenario_id]
    am_ss, pm_ss, total_ss = steady_state_revenue(client_volume, inputs)
    months = []
    for month_label, pct in ramp_curve:
        am_month = am_ss * pct / 100
        pm_month = pm_ss * pct / 100
        ancillary_month = inputs.ancillary_monthly  # currently 0, does not ramp (excluded from baseline entirely)
        total_month = am_month + pm_month + ancillary_month
        months.append(
            {
                "scenario_id": scenario_id,
                "month": month_label,
                "ramp_pct": pct,
                "implied_client_volume": round(client_volume * pct / 100, 2),
                "implied_pm_sessions_weekday": round(inputs.pm_weekday_sessions * pct / 100, 2),
                "am_revenue": round(am_month, 2),
                "pm_revenue": round(pm_month, 2),
                "ancillary_revenue": round(ancillary_month, 2),
                "total_revenue": round(total_month, 2),
                "steady_state_total_revenue": round(total_ss, 2),
                "pct_of_steady_state": round(total_month / total_ss * 100, 4) if total_ss else None,
            }
        )
    return months


def compute_all():
    inputs = CanonicalRevenueInputs()
    return {
        "scenario_table_1": compute_ramp("scenario_table_1", inputs),
        "scenario_table_2": compute_ramp("scenario_table_2", inputs),
    }


def _print_table(scenario_id, months):
    print(f"\n{scenario_id}")
    print(f"{'Month':<8}{'Ramp%':>8}{'AM Rev':>14}{'PM Rev':>14}{'Ancillary':>12}{'Total':>14}{'% of SS':>10}")
    for m in months:
        print(
            f"{m['month']:<8}{m['ramp_pct']:>7}%{m['am_revenue']:>14,.2f}{m['pm_revenue']:>14,.2f}"
            f"{m['ancillary_revenue']:>12,.2f}{m['total_revenue']:>14,.2f}{m['pct_of_steady_state']:>9.2f}%"
        )


def main(argv):
    all_results = compute_all()
    if "--scenario" in argv:
        idx = argv.index("--scenario")
        target = argv[idx + 1]
        _print_table(target, all_results[target])
    else:
        for scenario_id, months in all_results.items():
            _print_table(scenario_id, months)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
