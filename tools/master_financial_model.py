"""
GTT Center Perth -- Master Financial Model (deterministic calculation engine).

Combines the canonical revenue methodology, revenue_ramp.yml, and
cost_ramp.yml into a 24-month P&L, basic cash flow, break-even, scenario
comparison, and sensitivity analysis. This is the first phase that
calculates a P&L -- still NOT investor PDFs, Excel, Word docs, dashboards,
or a funding proposal (presentation is a later, separately-authorised
phase).

Priority order, per the coordinator's explicit instruction: correctness >
traceability > reproducibility > transparency > scenario separation >
auditability > presentation (presentation is out of scope this phase).

This module contains NO hard-coded financial OUTPUTS. Every revenue and cost
figure is read directly from data/canonical/revenue_ramp.yml and
data/canonical/cost_ramp.yml by id -- both already-validated, already-tested
canonical data products of prior phases. The only NEW calculations this
module performs are: (a) extending Month 5+ flat through Month 24 (an
explicit, disclosed, cited assumption -- no growth is invented past Month 5,
per the coordinator's explicit instruction), (b) superannuation (12% of OTE,
data/canonical/wages.yml#wage_superannuation_rate, a genuinely new line not
present in cost_ramp.yml's own payroll total -- disclosed as a supplementary,
non-primary figure, not silently folded into the authoritative total), (c)
Gross Contribution / Operating Expenses / Net Operating Profit-or-Loss (this
model's own defined P&L structure, per the coordinator's explicit line-item
instruction), (d) a basic cash-flow view (cumulative net operating result,
explicitly NOT a true cash-basis forecast -- no debtor/creditor timing data
exists anywhere in this repo), and (e) a break-even calculation, clearly
scoped to what the underlying cost classification actually supports (see
docs/architecture/MASTER-FINANCIAL-MODEL-METHODOLOGY.md §9 for the full
disclosed reasoning).

Does NOT calculate: EBITDA, EBIT (undefined terms in this repo -- not used),
opening funding requirement (startup-cost reconciliation stays unresolved,
per docs/architecture/STARTUP-COST-RECONCILIATION.md), NPV, IRR, or investor
return.

Usage:
    python tools/master_financial_model.py                    # print both scenarios' 24-month summary
    python tools/master_financial_model.py --scenario scenario_table_1
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
MODELS_DIR = REPO_ROOT / "data" / "models"

RAMP_MONTHS = ["M1", "M2", "M3", "M4", "M5plus"]  # the 5 canonical ramp months
FORECAST_MONTHS = list(range(1, 25))  # Months 1-24, explicit

# ---------------------------------------------------------------------------
# THE ONE MODELLING CHOICE THIS MODULE MAKES FOR THE 24-MONTH EXTENSION --
# isolated, cited, changeable, per the same pattern established in
# tools/revenue_ramp_model.py's RAMP_CURVE and tools/cost_ramp_model.py's
# payroll constants.
#
# STATUS: DECIDED, per the coordinator's explicit instruction for this phase
# ("Do NOT invent growth after Month 5 -- if there's no documented growth
# assumption past Month 5, keep revenue flat at canonical steady-state
# through Month 24"). This is not a claim that the venture will not grow --
# it is a disclosed, deliberate absence of an invented growth curve, because
# no canonical or historical document in this repo states one.
# ---------------------------------------------------------------------------
def ramp_month_for_forecast_month(forecast_month: int) -> str:
    """Maps forecast Month 1-24 to one of the 5 canonical ramp months.
    Months 1-4 map 1:1. Months 5-24 all map to M5plus (steady state, held
    flat -- no growth invented past Month 5)."""
    if forecast_month <= 4:
        return RAMP_MONTHS[forecast_month - 1]
    return "M5plus"


# Superannuation rate -- data/canonical/wages.yml#wage_superannuation_rate,
# MODELLED, 12% of Ordinary Time Earnings. NOT currently included anywhere in
# cost_ramp.yml's own payroll_costs total -- see
# docs/architecture/MASTER-FINANCIAL-MODEL-METHODOLOGY.md §6 and the new
# tracker item this phase adds. Applied here to direct_labor_and_opening_total
# (the wage-earning base) only, NOT to Workers Comp (an employer on-cost, not
# itself OTE).
SUPERANNUATION_RATE_PCT = 12.0


def load_yaml(filename, directory=CANON_DIR):
    path = directory / filename
    with path.open(encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def find_record(records, record_id):
    for rec in records:
        if rec.get("id") == record_id:
            return rec
    raise KeyError(f"No record with id={record_id!r} found")


class CanonicalModelInputs:
    """Loads revenue_ramp.yml and cost_ramp.yml records, indexed by
    (scenario_id, month) -- the ONLY source of revenue/cost figures this
    module uses. No revenue or cost figure is computed independently here."""

    def __init__(self):
        revenue_ramp = load_yaml("revenue_ramp.yml")
        cost_ramp = load_yaml("cost_ramp.yml")
        scenarios = load_yaml("scenarios.yml")
        wages = load_yaml("wages.yml")

        self.revenue_records = {}
        for rec in revenue_ramp["records"]:
            self.revenue_records[(rec["scenario_id"], rec["month"])] = rec

        self.cost_records = {}
        for rec in cost_ramp["records"]:
            self.cost_records[(rec["scenario_id"], rec["month"])] = rec

        self.scenario_records = {r["id"]: r for r in scenarios["records"]}
        self.superannuation_rate = find_record(wages["records"], "wage_superannuation_rate")["value_pct"]
        assert self.superannuation_rate == SUPERANNUATION_RATE_PCT, (
            "wages.yml#wage_superannuation_rate has changed -- update SUPERANNUATION_RATE_PCT "
            "or re-derive it from this record directly rather than silently diverging"
        )

    def revenue(self, scenario_id, ramp_month):
        return self.revenue_records[(scenario_id, ramp_month)]

    def cost(self, scenario_id, ramp_month):
        return self.cost_records[(scenario_id, ramp_month)]


def compute_month_pnl(scenario_id, forecast_month, inputs: CanonicalModelInputs):
    """Returns one month's full P&L line-up, per the coordinator's explicit
    line-item instruction: Revenue, Payroll, Gross Contribution, Operating
    Expenses, Total Operating Costs, Net Operating Profit/(Loss) -- plus the
    supplementary, disclosed Superannuation line (not part of the primary
    Total Operating Costs / Net Operating Result, see module docstring)."""
    ramp_month = ramp_month_for_forecast_month(forecast_month)
    rev = inputs.revenue(scenario_id, ramp_month)
    cost = inputs.cost(scenario_id, ramp_month)

    revenue_total = rev["total_revenue"]
    am_revenue = rev["am_revenue"]
    pm_revenue = rev["pm_revenue"]
    ancillary_revenue = rev["ancillary_revenue"]

    payroll = cost["payroll_costs"]
    fixed_costs = cost["fixed_costs"]
    variable_costs = cost["variable_costs"]
    operating_expenses = round(fixed_costs + variable_costs, 2)
    total_operating_costs = cost["total_operating_costs"]

    gross_contribution = round(revenue_total - payroll, 2)
    net_operating_result = round(revenue_total - total_operating_costs, 2)

    payroll_breakdown = cost.get("payroll_breakdown", {})
    direct_labor_and_opening = payroll_breakdown.get("direct_labor_and_opening_total")
    superannuation = round(direct_labor_and_opening * inputs.superannuation_rate / 100, 2) if direct_labor_and_opening else None
    net_operating_result_incl_super = (
        round(net_operating_result - superannuation, 2) if superannuation is not None else None
    )

    return {
        "scenario_id": scenario_id,
        "forecast_month": forecast_month,
        "ramp_month": ramp_month,
        "is_extended_flat": forecast_month > 5,  # Months 6-24: held flat at M5plus, no growth invented
        "revenue": {
            "am_revenue": am_revenue,
            "pm_revenue": pm_revenue,
            "ancillary_revenue": ancillary_revenue,
            "total_revenue": revenue_total,
        },
        "payroll": payroll,
        "payroll_breakdown": payroll_breakdown,
        "gross_contribution": gross_contribution,
        "operating_expenses": operating_expenses,
        "operating_expenses_breakdown": {"fixed_costs": fixed_costs, "variable_costs": variable_costs},
        "total_operating_costs": total_operating_costs,
        "net_operating_result": net_operating_result,
        "superannuation_supplementary": superannuation,
        "net_operating_result_incl_super_supplementary": net_operating_result_incl_super,
    }


def compute_24_month_pnl(scenario_id, inputs: CanonicalModelInputs):
    return [compute_month_pnl(scenario_id, m, inputs) for m in FORECAST_MONTHS]


def compute_24_month_totals(scenario_id, inputs: CanonicalModelInputs):
    months = compute_24_month_pnl(scenario_id, inputs)
    return {
        "total_revenue_24mo": round(sum(m["revenue"]["total_revenue"] for m in months), 2),
        "total_operating_costs_24mo": round(sum(m["total_operating_costs"] for m in months), 2),
        "total_net_operating_result_24mo": round(sum(m["net_operating_result"] for m in months), 2),
        "annualised_revenue_steady_state": round(months[4]["revenue"]["total_revenue"] * 12, 2),  # M5's rate x12
        "annualised_operating_costs_steady_state": round(months[4]["total_operating_costs"] * 12, 2),
        "annualised_net_operating_result_steady_state": round(months[4]["net_operating_result"] * 12, 2),
    }


def compute_cash_flow(scenario_id, inputs: CanonicalModelInputs, opening_cash=None):
    """Basic 24-month cash flow. opening_cash is an EXPLICIT, un-invented
    input -- if None (the default, since no canonical source states an
    opening cash figure), closing_cash is not computed, only the cumulative
    net operating result (a proxy for cumulative cash need/generation on an
    ACCRUAL basis -- explicitly NOT a true cash-basis forecast, since no
    debtor/creditor timing data exists anywhere in this repo). Startup
    expenditure and capex timing are NOT included here -- no canonical
    per-month timing schedule exists for either (see
    docs/architecture/MASTER-FINANCIAL-MODEL-METHODOLOGY.md §11)."""
    months = compute_24_month_pnl(scenario_id, inputs)
    rows = []
    cumulative = opening_cash if opening_cash is not None else 0.0
    for m in months:
        operating_cash_flow = m["net_operating_result"]  # accrual proxy, disclosed simplification
        cumulative = round(cumulative + operating_cash_flow, 2)
        rows.append(
            {
                "forecast_month": m["forecast_month"],
                "operating_cash_flow": operating_cash_flow,
                "startup_expenditure": None,  # no canonical per-month timing schedule exists
                "capex": None,  # no canonical per-month timing schedule exists
                "net_monthly_cash_movement": operating_cash_flow,
                "cumulative_position": cumulative,
                "closing_cash": cumulative if opening_cash is not None else None,
            }
        )
    trough = min(rows, key=lambda r: r["cumulative_position"])
    return {
        "opening_cash_assumption": opening_cash,
        "opening_cash_status": "PLACEHOLDER -- no canonical source states an opening cash figure" if opening_cash is None else "explicit input, provided by caller",
        "rows": rows,
        "trough_month": trough["forecast_month"],
        "trough_cumulative_position": trough["cumulative_position"],
    }


def compute_breakeven(scenario_id, inputs: CanonicalModelInputs):
    """Steady-state (Month 5+) AM client-volume break-even -- the ONE
    break-even calculation this module treats as defensible, and only under
    an explicitly disclosed simplification: PM revenue, payroll, and opex
    are all held at their Month 5+ steady-state levels (none of them are a
    function of AM client volume in this repo's canonical data except AM
    revenue itself, which is linear: clients x price x operating_days).
    A true contribution-margin break-even (fixed vs variable cost split) is
    NOT computed -- see the disclosed reason in `defensibility_note` below.
    """
    m5 = compute_month_pnl(scenario_id, 5, inputs)
    pricing = load_yaml("pricing.yml")
    client_assumptions = load_yaml("client_assumptions.yml")
    am_price = find_record(pricing["records"], "am_price_used_for_revenue")["price"]
    universal = client_assumptions["universal"]
    operating_days_weekday = find_record(universal, "operating_days_per_month_weekday")["value"]
    operating_saturdays = find_record(universal, "operating_saturdays_per_month")["value"]
    am_revenue_per_client_per_month = am_price * (operating_days_weekday + operating_saturdays)

    pm_and_ancillary_revenue = m5["revenue"]["pm_revenue"] + m5["revenue"]["ancillary_revenue"]
    total_operating_costs = m5["total_operating_costs"]

    breakeven_am_client_volume = round(
        (total_operating_costs - pm_and_ancillary_revenue) / am_revenue_per_client_per_month, 3
    )
    breakeven_monthly_revenue = round(
        breakeven_am_client_volume * am_revenue_per_client_per_month + pm_and_ancillary_revenue, 2
    )
    committed_client_volume = inputs.scenario_records[scenario_id]["client_volume"]["value"]

    return {
        "scenario_id": scenario_id,
        "breakeven_am_client_volume_per_day": breakeven_am_client_volume,
        "breakeven_monthly_revenue": breakeven_monthly_revenue,
        "committed_client_volume_per_day": committed_client_volume,
        "margin_of_safety_clients_per_day": round(committed_client_volume - breakeven_am_client_volume, 3),
        "basis": "Month 5+ (steady state) costs and PM/ancillary revenue held fixed; AM revenue treated as the only volume-linear component -- see defensibility_note",
        "defensibility_note": (
            "A traditional contribution-margin break-even (fixed costs / contribution margin %) is NOT "
            "computed, because this repo's own cost classification does not support one reliably: nearly "
            "every cost in cost_ramp.yml is classified FIXED (including AM/PM payroll, which do not vary "
            "with actual booking volume in this model's current ramp treatment -- see "
            "conflict_am_labor_ramp_unmodelled), and the one disputed classification "
            "(GTT supplies/consumables/laundry, conflict_variable_vs_fixed_classification) remains "
            "unresolved. The client-volume break-even above is defensible because AM revenue specifically "
            "is a known, linear function of client volume (price x operating days) -- it does not require "
            "resolving the disputed cost classification to compute."
        ),
    }


def compute_sensitivity_client_volume(scenario_id, inputs: CanonicalModelInputs):
    """Client volume at 50/75/100/125% of the scenario's committed level,
    holding price/PM/opex/payroll at their Month 5+ steady-state values
    (payroll does NOT flex with client volume in this model's current
    treatment -- see conflict_am_labor_ramp_unmodelled; this sensitivity
    deliberately does not invent a payroll-flex assumption either, matching
    the base case's own disclosed conservatism)."""
    m5 = compute_month_pnl(scenario_id, 5, inputs)
    pricing = load_yaml("pricing.yml")
    client_assumptions = load_yaml("client_assumptions.yml")
    am_price = find_record(pricing["records"], "am_price_used_for_revenue")["price"]
    universal = client_assumptions["universal"]
    operating_days_weekday = find_record(universal, "operating_days_per_month_weekday")["value"]
    operating_saturdays = find_record(universal, "operating_saturdays_per_month")["value"]
    committed_volume = inputs.scenario_records[scenario_id]["client_volume"]["value"]

    results = []
    for pct in (50, 75, 100, 125):
        volume = committed_volume * pct / 100
        am_revenue = round(volume * am_price * (operating_days_weekday + operating_saturdays), 2)
        total_revenue = round(am_revenue + m5["revenue"]["pm_revenue"] + m5["revenue"]["ancillary_revenue"], 2)
        net_result = round(total_revenue - m5["total_operating_costs"], 2)
        results.append(
            {
                "pct_of_committed": pct,
                "client_volume_per_day": round(volume, 2),
                "am_revenue": am_revenue,
                "total_revenue": total_revenue,
                "net_operating_result": net_result,
                "note": "payroll and opex held at Month 5+ steady-state levels -- NOT flexed with client volume, per conflict_am_labor_ramp_unmodelled",
            }
        )
    return results


def compute_sensitivity_insurance(scenario_id, inputs: CanonicalModelInputs):
    """Insurance sensitivity -- data/canonical/opex.yml's own disclosed
    conflict_insurance_estimate: modelled A$400/month vs. the itemised
    A$11,700-19,000/year (A$975-1,583/month) range. Neither is chosen as
    correct -- both are shown as alternative Total Operating Costs/Net
    Operating Result outcomes."""
    opex = load_yaml("opex.yml")
    modelled = find_record(opex["records"], "opex_insurance_modelled")["monthly_equivalent"]
    itemised_low = find_record(opex["records"], "opex_insurance_public_liability")["monthly_equivalent"]["low"] + \
        find_record(opex["records"], "opex_insurance_professional_indemnity")["monthly_equivalent"]["low"] + \
        find_record(opex["records"], "opex_insurance_property_contents")["monthly_equivalent"]["low"]
    itemised_high = find_record(opex["records"], "opex_insurance_public_liability")["monthly_equivalent"]["high"] + \
        find_record(opex["records"], "opex_insurance_professional_indemnity")["monthly_equivalent"]["high"] + \
        find_record(opex["records"], "opex_insurance_property_contents")["monthly_equivalent"]["high"]
    # Business interruption explicitly OPTIONAL per opex.yml -- excluded from this range, per that record's own status_detail.

    m5 = compute_month_pnl(scenario_id, 5, inputs)
    base_total_costs = m5["total_operating_costs"]
    base_net = m5["net_operating_result"]

    results = []
    for label, monthly_insurance in (
        ("modelled (current)", modelled),
        ("itemised low (mandatory policies only)", round(itemised_low, 2)),
        ("itemised high (mandatory policies only)", round(itemised_high, 2)),
    ):
        delta = round(monthly_insurance - modelled, 2)
        adjusted_total_costs = round(base_total_costs + delta, 2)
        adjusted_net = round(base_net - delta, 2)
        results.append(
            {
                "scenario": label,
                "monthly_insurance": round(monthly_insurance, 2),
                "delta_vs_modelled": delta,
                "adjusted_total_operating_costs": adjusted_total_costs,
                "adjusted_net_operating_result": adjusted_net,
            }
        )
    return results


def compute_scenario_comparison(inputs: CanonicalModelInputs):
    comparison = {}
    for scenario_id in ("scenario_table_1", "scenario_table_2"):
        m5 = compute_month_pnl(scenario_id, 5, inputs)
        totals = compute_24_month_totals(scenario_id, inputs)
        comparison[scenario_id] = {
            "client_volume_per_day": inputs.scenario_records[scenario_id]["client_volume"]["value"],
            "steady_state_revenue": m5["revenue"]["total_revenue"],
            "steady_state_payroll": m5["payroll"],
            "steady_state_opex": m5["operating_expenses"],
            "steady_state_total_operating_costs": m5["total_operating_costs"],
            "steady_state_net_operating_result": m5["net_operating_result"],
            "annualised_revenue": totals["annualised_revenue_steady_state"],
            "annualised_net_operating_result": totals["annualised_net_operating_result_steady_state"],
        }
    return comparison


def compute_month_snapshot_comparison(inputs: CanonicalModelInputs):
    snapshot_months = [1, 3, 5, 12, 24]
    out = {}
    for scenario_id in ("scenario_table_1", "scenario_table_2"):
        out[scenario_id] = {m: compute_month_pnl(scenario_id, m, inputs) for m in snapshot_months}
    return out


def main(argv):
    inputs = CanonicalModelInputs()
    scenarios = ["scenario_table_1", "scenario_table_2"]
    if "--scenario" in argv:
        idx = argv.index("--scenario")
        scenarios = [argv[idx + 1]]

    for scenario_id in scenarios:
        print(f"\n=== {scenario_id} -- 24-Month P&L ===")
        months = compute_24_month_pnl(scenario_id, inputs)
        print(f"{'Mo':<4}{'Revenue':>12}{'Payroll':>12}{'GrossContrib':>14}{'OpEx':>10}{'TotalCosts':>12}{'NetResult':>12}")
        for m in months:
            print(
                f"{m['forecast_month']:<4}{m['revenue']['total_revenue']:>12,.2f}{m['payroll']:>12,.2f}"
                f"{m['gross_contribution']:>14,.2f}{m['operating_expenses']:>10,.2f}"
                f"{m['total_operating_costs']:>12,.2f}{m['net_operating_result']:>12,.2f}"
            )
        totals = compute_24_month_totals(scenario_id, inputs)
        print(f"24mo totals: {totals}")
        print(f"Break-even: {compute_breakeven(scenario_id, inputs)}")

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
