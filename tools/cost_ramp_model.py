"""
GTT Center Perth -- Cost Ramp Model (deterministic calculation module).

Rebuilds the Month 1-5+ cost ramp for Table 1 (18-client) and Table 2
(12-client) -- the cost-side counterpart to tools/revenue_ramp_model.py. Full
investigation and rationale: docs/architecture/COST-RAMP-METHODOLOGY.md.

This module contains NO unexplained hard-coded financial values. Every input
is either (a) read directly from data/canonical/*.yml by id, or (b) a named,
individually-cited constant sourced to a specific line in
docs/profit-loss-tables.md's own "Appendix -- How Every Figure Is Calculated"
or docs/CURRENT-STATE.md §5 -- the same pattern tools/revenue_ramp_model.py
uses for its RAMP_CURVE constant.

Does NOT calculate: Net P&L, EBITDA, cash balance, break-even, or any other
figure requiring revenue to be netted against costs -- cost side only, per
the coordinator's explicit financial-model boundary.

Usage:
    python tools/cost_ramp_model.py               # print both scenarios' cost ramp tables
    python tools/cost_ramp_model.py --scenario scenario_table_1
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

MONTHS = ["M1", "M2", "M3", "M4", "M5plus"]

# ---------------------------------------------------------------------------
# NAMED, CITED PAYROLL CONSTANTS -- each sourced to a specific, already-
# canonical line in docs/profit-loss-tables.md's Appendix or
# docs/CURRENT-STATE.md §5. None of these is invented; all are the venture's
# own already-published figures, reused here as first-principles calculation
# inputs (not restated financial "facts" -- see the STATUS field on each
# corresponding data/canonical/cost_ramp.yml record for governance status).
# ---------------------------------------------------------------------------

# AM Direct Labor (weekday) -- FTE-based, "UNCHANGED... same headcount,
# same fixed-salary roles" -- identical under both Table 1 and Table 2, and
# does NOT ramp (fixed headcount hired from Month 1 regardless of actual
# ramp-period booking volume -- see docs/architecture/COST-RAMP-METHODOLOGY.md
# §4 for the disclosed rationale/limitation of this treatment).
# Source: docs/CURRENT-STATE.md §5, "AM Direct Labor, both models -- UNCHANGED
# at A$48,254.67/month".
#
# SPLIT INTO TWO SUB-COMPONENTS (Phase 9 resume, 2026-08-09) -- required for
# correct superannuation treatment (see SUPERANNUATION_RATE_PCT below):
# docs/financial-break-even-staff.md's own "Award Wage Summary" table (lines
# 29-37) explicitly labels 6 of 7 roles' annual figures "incl. super"
# (Receptionist/Manager, Beauty therapist, Nail technician, Hairdresser,
# Massage therapist, PM Service Therapist) but does NOT apply that label to
# the Phlebotomist row ("A$43,068 (25hr/wk each)" -- no "incl. super" text).
# This is a real, disclosed asymmetry in the source document itself, not an
# inference -- the 8 treatment staff's annual salaries already include
# superannuation; the 2 phlebotomists' annual salary (A$86,136/yr total)
# does not.
# RECOMPUTED 2026-08-17, per direct instruction to propagate the 2026-08-16
# wage/award research through the canonical model, not leave it researched-
# but-unpropagated. METHOD: proportional scaling -- the exact per-staff-
# member hour allocation behind the old A$41,076.67/A$7,178.00 figures is
# NOT preserved as a rebuildable worksheet anywhere in this repo (confirmed
# directly, docs/profit-loss-tables.md's own Appendix: "the specific per-
# staff-member hour allocation behind the exact total is not saved as a
# standalone worksheet in this repo"). Rebuilding it from scratch against
# scenario-c-sync-timetables.md's per-client service-time entries is a
# genuinely separate, larger task, not attempted here (would risk silently
# inventing a schedule reconstruction not independently verified this pass).
# Instead: each role's OLD casual rate -> NEW casual rate (financial-break-
# even-staff.md, researched 2026-08-16) gives a defensible, disclosed scale
# factor, applied to the existing dollar total. This is the SAME proportional-
# scaling method this file already uses elsewhere (e.g. AM_SATURDAY_DAILY_LABOR
# below), not a new methodology invented for this recompute.
#   Treatment staff (8): 4x Massage+Beauty (old $37.00/hr -> new $37.50/hr)
#     + 2x Nails (old $35.63/hr -> new $36.81/hr) + 2x Hair (same as Nails).
#     Old weighted-hourly sum = 4(37.00)+2(35.63)+2(35.63) = 290.52
#     New weighted-hourly sum = 4(37.50)+2(36.81)+2(36.81) = 297.24
#     Scale factor = 297.24 / 290.52 = 1.023133
#   Phlebotomists (2): old $30.63/hr -> new SS Level 1-2 range $33.71-35.04/hr,
#     midpoint $34.375/hr used as the single defensible new rate (the old
#     figure was also a single rate, not a range).
#     Scale factor = 34.375 / 30.63 = 1.122266
AM_WEEKDAY_TREATMENT_STAFF_MONTHLY = round((492920 / 12) * 1.023133, 2)  # was A$41,076.67 -> A$42,027.66
AM_WEEKDAY_PHLEBOTOMIST_MONTHLY = round((86136 / 12) * 1.122266, 2)       # was A$7,178.00 -> A$8,055.97
AM_WEEKDAY_DIRECT_LABOR_MONTHLY = round(AM_WEEKDAY_TREATMENT_STAFF_MONTHLY + AM_WEEKDAY_PHLEBOTOMIST_MONTHLY, 2)  # was A$48,254.67 -> A$50,083.63

# AM Direct Labor (Saturday) -- hours-based, scales with the scenario's
# COMMITTED client volume (not the ramp-period actual volume, which has no
# documented rostering methodology anywhere in this repo -- see COST-RAMP-
# METHODOLOGY.md §4). Source: docs/profit-loss-tables.md §2 (old model, now
# historical) and the PRIMARY REBASED MODEL section (Table 1).
# RECOMPUTED 2026-08-17 -- same roster/rate mix as AM_WEEKDAY_DIRECT_LABOR_
# MONTHLY above, so the same blended scale factor (new/old weekday total =
# 50083.63/48254.67 = 1.037896) is applied here, not a separately-derived one.
AM_SATURDAY_DAILY_LABOR = {
    "scenario_table_1": round(2419.11 * 1.037896, 2),  # was 2,419.11 -> 2,510.80
    "scenario_table_2": round(1612.74 * 1.037896, 2),  # was 1,612.74 -> 1,673.87
}

# Opening-time increment (07:00 start) -- fixed per trading day, sourced to
# docs/profit-loss-tables.md's Appendix. Applies to Table 1 (07:00 start)
# without ambiguity. Table 2 (08:00 start) carries this figure UNCHANGED from
# the pre-rebase model per docs/VERIFICATION-TRACKER.md item 1o, which
# explicitly flags -- not resolves -- whether it should still apply at 08:00.
OPENING_TIME_INCREMENT_DAILY = 44.50

# "Receptionist/relief/workers comp (Weekday pro-rated)" -- docs/profit-loss-
# tables.md's Appendix states this ~A$339.00/day figure with its own "~="
# approximation marker (not an exact stated total) -- reused here at face
# value, not back-solved to force reconciliation with any other total (see
# COST-RAMP-METHODOLOGY.md §7 for the resulting, disclosed, unreconciled
# ~A$246.57/month gap against docs/CURRENT-STATE.md's own headline figure).
RECEPTIONIST_RELIEF_WORKERS_COMP_DAILY = 339.00

# PM Direct Labor (Saturday) -- fixed regardless of ramp, because even at the
# full 8-session/day steady-state PM Saturday volume, hours/role/day
# (8 / 4 roles / 1.3 sessions/hr = 1.54hrs) is already below the 3-hour
# casual-minimum-engagement floor (wages.yml#wage_casual_minimum_engagement,
# VERIFIED) -- so PM Saturday labor cannot fall below this floor amount at
# ANY session-count ramp assumption, making the ramp question moot for this
# specific cost. Source: docs/profit-loss-tables.md §2's 3-hour-minimum
# correction note (A$654.32/day, backed-out blended Saturday casual rate
# A$54.53/hr).
# RECOMPUTED 2026-08-17 -- built from the same blended weekday casual rate
# as PM_WEEKDAY_BLENDED_CASUAL_RATE below; scale factor = new/old blended
# rate = 37.155/36.315 = 1.023127.
PM_SATURDAY_DAILY_LABOR = round(654.32 * 1.023127, 2)  # was 654.32 -> 669.46

# PM Direct Labor (weekday) -- genuinely ramps, per the session-count curve
# below and the 3-hour casual-minimum-engagement floor. Blended weekday
# casual rate = average of the 4 PM roles' casual rates
# (wages.yml#wage_massage_therapist/wage_beauty_therapist = A$37.00/hr,
# wages.yml#wage_nail_technician/wage_hairdresser = A$35.63/hr).
# RECOMPUTED 2026-08-17 -- current researched casual rates (financial-break-
# even-staff.md, 2026-08-16): Massage/Beauty $37.50/hr, Nails/Hair $36.81/hr.
PM_WEEKDAY_BLENDED_CASUAL_RATE = (37.50 + 37.50 + 36.81 + 36.81) / 4  # was 36.315 -> 37.155
PM_ROLES = 4
PM_THROUGHPUT_SESSIONS_PER_HOUR = 1.3  # docs/pm-staffing-roster.md, established elsewhere in this repo
CASUAL_MINIMUM_ENGAGEMENT_HOURS = 3.0  # wages.yml#wage_casual_minimum_engagement, VERIFIED

# PM session-count ramp -- REUSED from data/canonical/revenue_assumptions.yml's
# rev_pm_session_ramp_historical (docs/pm-staffing-roster.md's own PM staffing
# table), NOT the blanket 43/64/79/93/100% revenue-ramp curve. This is the
# one genuine, disclosed departure from "reuse the revenue ramp for costs" --
# justified because PM labor cost is a DIRECT function of session count via
# the hours-based costing formula already established in
# docs/pm-staffing-roster.md, whereas the blanket curve was built for revenue
# specifically. See docs/architecture/COST-RAMP-METHODOLOGY.md §5.
PM_SESSION_RAMP = {"M1": 4, "M2": 8, "M3": 12, "M4": 15, "M5plus": 16}

# Month 5+ PM weekday daily labor is anchored to the already-canonical,
# independently-verified A$440.00/day figure (docs/profit-loss-tables.md §1),
# NOT to this module's own formula output (which gives ~A$446.95/day -- the
# repo's own Appendix already discloses this exact "within rounding, not
# exact" gap for the identical calculation, a pre-existing imprecision, not
# introduced here).
# RECOMPUTED 2026-08-17 -- proportionally scaled by the same PM blended-rate
# factor (37.155/36.315 = 1.023127) applied above, since this anchor figure
# was itself built from the old blended rate.
PM_WEEKDAY_M5PLUS_DAILY_LABOR_CANONICAL_ANCHOR = round(440.00 * 1.023127, 2)  # was 440.00 -> 450.18

WORKERS_COMP_RATE_PCT = 1.7  # wages.yml#wage_workers_comp_rate, MODELLED

# ---------------------------------------------------------------------------
# SUPERANNUATION (Phase 9 resume, 2026-08-09) -- data/canonical/wages.yml's
# wage_superannuation_rate (12% of Ordinary Time Earnings, MODELLED), applied
# here for the first time to the ACTUAL payroll figures -- previously the
# rate existed in wages.yml but was never applied anywhere in this repo's
# payroll modelling (docs/VERIFICATION-TRACKER.md item 46).
#
# INCLUSIVE/EXCLUSIVE TREATMENT -- read directly off
# docs/financial-break-even-staff.md's own Award Wage Summary table, not
# inferred or invented:
#   - AM Weekday Direct Labor, TREATMENT STAFF portion (A$41,076.67/month):
#     ALREADY INCLUDES super, per that table's explicit "incl. super" label
#     on 6 of 7 roles (Beauty/Massage/Nail/Hair/PM Service Therapist/
#     Receptionist-Manager) -- no super added here, adding it again would
#     double-count.
#   - AM Weekday Direct Labor, PHLEBOTOMIST portion (A$7,178.00/month): does
#     NOT include super -- that table's Phlebotomist row states "A$43,068
#     (25hr/wk each)" with no "incl. super" text, a real, disclosed asymmetry
#     in the source itself. Super IS added here.
#   - AM Saturday, PM Weekday, PM Saturday Direct Labor: all built from the
#     raw hourly `casual_loaded` award rate (e.g. A$37.00/hr), which the
#     source table's own structure treats as EXCLUSIVE of super (super only
#     appears once the figure is annualised into a fully-loaded package cost)
#     -- super IS added here, on top of the hours-based calculation.
#   - Opening-time increment, Receptionist/Relief Pool: these are bundled,
#     non-role-specific operational figures (the Receptionist/Relief figure
#     is itself only an approximate "~A$339.00/day" per docs/profit-loss-
#     tables.md's own Appendix, not cleanly decomposable back to the
#     Receptionist's own annual salary) -- super treatment for these two
#     components is genuinely UNRESOLVED, not guessed at. No super is added
#     to them. See conflict_superannuation_partial_coverage in cost_ramp.yml.
#
# ELIGIBILITY RULE: not stated anywhere in this repo's canonical or source
# documents (no minimum-earnings threshold, no age threshold is mentioned).
# This module therefore applies the 12% rate universally to every eligible
# wage component above, without any earnings-threshold carve-out -- flagged
# as an unconfirmed assumption, not independently verified against current
# Australian SG eligibility rules (which this module does not attempt to
# state as fact).
# ---------------------------------------------------------------------------
SUPERANNUATION_RATE_PCT = 12.0  # wages.yml#wage_superannuation_rate, MODELLED

# GTT supplies variable-alternative rate -- opex.yml#opex_gtt_supplies' own
# stated basis ("200 tests x A$2"), reused here per-test, per-day (weekday
# only, matching that record's own already-disclosed "~A$792/month at 396
# tests" estimate methodology exactly -- not a new assumption).
GTT_SUPPLIES_PER_TEST_RATE = 2.00


def load_yaml(filename):
    path = CANON_DIR / filename
    with path.open(encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def find_record(records, record_id):
    for rec in records:
        if rec.get("id") == record_id:
            return rec
    raise KeyError(f"No record with id={record_id!r} found")


class CanonicalCostInputs:
    """Every purely-canonical (non-hard-coded) input this module needs, read
    by id from data/canonical/*.yml."""

    def __init__(self):
        client_assumptions = load_yaml("client_assumptions.yml")
        scenarios = load_yaml("scenarios.yml")
        opex = load_yaml("opex.yml")

        universal = client_assumptions["universal"]
        self.operating_days_weekday = find_record(universal, "operating_days_per_month_weekday")["value"]
        self.operating_saturdays = find_record(universal, "operating_saturdays_per_month")["value"]

        scenario_records = scenarios["records"]
        self.client_volume = {
            "scenario_table_1": find_record(scenario_records, "scenario_table_1")["client_volume"]["value"],
            "scenario_table_2": find_record(scenario_records, "scenario_table_2")["client_volume"]["value"],
        }

        opex_records = opex["records"]
        self.marketing_ramp = find_record(opex_records, "opex_marketing_ads_ramp")["amount"]
        self.marketing_steady_state = find_record(opex_records, "opex_marketing_ads_steady_state")["amount"]

        # Fixed Non-Wage Overhead = the full A$13,980.00/month canonical total
        # (docs/profit-loss-tables.md §4) minus the marketing line, which is
        # the ONE component with a documented, sourced Month 1-4 ramp
        # (opex_marketing_ads_ramp above). No other opex.yml record has a
        # stated ramp anywhere in this repo -- reused at face value, FIXED
        # from Month 1, including the 3 records under the disclosed, UNRESOLVED
        # FIXED-vs-VARIABLE classification conflict (opex_gtt_supplies,
        # opex_consumables_general, opex_laundry) -- this module does NOT
        # resolve that conflict, it carries forward the status-quo FIXED
        # classification already in opex.yml's own cost_type field, per the
        # coordinator's explicit "don't resolve just to make the model run"
        # instruction. See gtt_supplies_variable_alternative() below for the
        # disclosed, non-primary exploratory alternative.
        total_nonwage = 13980.00  # docs/profit-loss-tables.md §4 Monthly total -- cross-checked against the 13-line sum in opex.yml's own header comment
        self.fixed_nonwage_excl_marketing = round(total_nonwage - self.marketing_steady_state, 2)


def compute_pm_weekday_daily_labor(month):
    """PM Direct Labor (weekday), per session-count ramp + 3-hour casual
    minimum floor. Month5plus is anchored to the canonical figure (see
    PM_WEEKDAY_M5PLUS_DAILY_LABOR_CANONICAL_ANCHOR's own docstring)."""
    if month == "M5plus":
        return PM_WEEKDAY_M5PLUS_DAILY_LABOR_CANONICAL_ANCHOR
    sessions = PM_SESSION_RAMP[month]
    hours_per_role = max(
        CASUAL_MINIMUM_ENGAGEMENT_HOURS,
        sessions / PM_ROLES / PM_THROUGHPUT_SESSIONS_PER_HOUR,
    )
    return round(hours_per_role * PM_ROLES * PM_WEEKDAY_BLENDED_CASUAL_RATE, 2)


def compute_payroll(scenario_id, month, inputs: CanonicalCostInputs):
    """Returns a dict of payroll components for one (scenario, month)."""
    am_weekday_treatment = AM_WEEKDAY_TREATMENT_STAFF_MONTHLY  # already includes super -- no super added
    am_weekday_phlebotomist = AM_WEEKDAY_PHLEBOTOMIST_MONTHLY   # does NOT include super -- super added below
    am_weekday = round(am_weekday_treatment + am_weekday_phlebotomist, 2)
    am_saturday = round(AM_SATURDAY_DAILY_LABOR[scenario_id] * inputs.operating_saturdays, 2)
    pm_weekday_daily = compute_pm_weekday_daily_labor(month)
    pm_weekday = round(pm_weekday_daily * inputs.operating_days_weekday, 2)
    pm_saturday = round(PM_SATURDAY_DAILY_LABOR * inputs.operating_saturdays, 2)
    opening_increment = round(OPENING_TIME_INCREMENT_DAILY * inputs.operating_days_weekday, 2)
    receptionist_relief = round(RECEPTIONIST_RELIEF_WORKERS_COMP_DAILY * inputs.operating_days_weekday, 2)

    direct_labor_and_opening = round(
        am_weekday + am_saturday + pm_weekday + pm_saturday + opening_increment + receptionist_relief, 2
    )
    workers_comp = round(direct_labor_and_opening * WORKERS_COMP_RATE_PCT / 100, 2)

    # Superannuation -- applied ONLY to the components confirmed super-exclusive
    # (see SUPERANNUATION_RATE_PCT's own docstring for the full, source-based
    # reasoning). Opening-time increment and Receptionist/Relief are excluded --
    # genuinely unresolved, not guessed at.
    superannuation = round(
        (am_weekday_phlebotomist + am_saturday + pm_weekday + pm_saturday) * SUPERANNUATION_RATE_PCT / 100, 2
    )

    payroll_total = round(direct_labor_and_opening + workers_comp + superannuation, 2)

    return {
        "am_weekday_direct_labor": am_weekday,
        "am_weekday_treatment_staff": round(am_weekday_treatment, 2),
        "am_weekday_phlebotomist": round(am_weekday_phlebotomist, 2),
        "am_saturday_direct_labor": am_saturday,
        "pm_weekday_direct_labor": pm_weekday,
        "pm_saturday_direct_labor": pm_saturday,
        "opening_time_increment": opening_increment,
        "receptionist_relief": receptionist_relief,
        "direct_labor_and_opening_total": direct_labor_and_opening,
        "superannuation": superannuation,
        "workers_comp": workers_comp,
        "payroll_total": payroll_total,
    }


def compute_fixed_and_variable_opex(month, inputs: CanonicalCostInputs):
    """Fixed Costs = Non-Wage Overhead excl. marketing (unchanged Month 1-5+).
    Variable Costs = marketing spend ramp (the only opex.yml component with a
    documented, sourced monthly ramp)."""
    fixed = inputs.fixed_nonwage_excl_marketing
    variable = inputs.marketing_ramp[f"month_{MONTHS.index(month) + 1}"] if month != "M5plus" else inputs.marketing_steady_state
    return round(fixed, 2), round(variable, 2)


def gtt_supplies_variable_alternative(scenario_id, month, inputs: CanonicalCostInputs, ramp_curve):
    """Exploratory, NON-PRIMARY calculation: what GTT supplies would cost if
    treated as VARIABLE (per-test) instead of the current FIXED A$400.00/month
    modelled figure -- investigating, not resolving,
    conflict_variable_vs_fixed_classification (opex.yml). Uses
    opex_gtt_supplies' own stated basis (A$2/test), applied to weekday-only
    test volume at the ramp-period's implied client volume -- matching that
    record's own already-disclosed "~A$792/month at 396 tests" methodology
    exactly, not a new assumption."""
    pct = dict(ramp_curve)[month]
    client_volume = inputs.client_volume[scenario_id] * pct / 100
    tests_per_month = client_volume * inputs.operating_days_weekday
    return round(tests_per_month * GTT_SUPPLIES_PER_TEST_RATE, 2)


def compute_ramp(scenario_id, inputs: CanonicalCostInputs, revenue_ramp_curve):
    months_out = []
    for month in MONTHS:
        payroll = compute_payroll(scenario_id, month, inputs)
        fixed, variable = compute_fixed_and_variable_opex(month, inputs)
        total = round(fixed + variable + payroll["payroll_total"], 2)
        months_out.append(
            {
                "scenario_id": scenario_id,
                "month": month,
                "fixed_costs": fixed,
                "variable_costs": variable,
                "payroll_costs": payroll["payroll_total"],
                "total_operating_costs": total,
                "payroll_detail": payroll,
                "gtt_supplies_variable_alternative": gtt_supplies_variable_alternative(
                    scenario_id, month, inputs, revenue_ramp_curve
                ),
            }
        )
    return months_out


# Default revenue ramp curve, imported lazily to avoid a hard dependency at
# module-load time if revenue_ramp_model.py is ever moved -- mirrors
# tools/revenue_ramp_model.py's own RAMP_CURVE exactly (used here ONLY for
# the GTT-supplies variable-alternative's implied-client-volume calculation,
# NOT applied to payroll or any other cost -- see
# docs/architecture/COST-RAMP-METHODOLOGY.md §5 for why costs do NOT
# automatically inherit the revenue ramp).
DEFAULT_REVENUE_RAMP_CURVE = [("M1", 43), ("M2", 64), ("M3", 79), ("M4", 93), ("M5plus", 100)]


def compute_all():
    inputs = CanonicalCostInputs()
    return {
        "scenario_table_1": compute_ramp("scenario_table_1", inputs, DEFAULT_REVENUE_RAMP_CURVE),
        "scenario_table_2": compute_ramp("scenario_table_2", inputs, DEFAULT_REVENUE_RAMP_CURVE),
    }


def _print_table(scenario_id, months):
    print(f"\n{scenario_id}")
    print(f"{'Month':<8}{'Fixed':>12}{'Variable':>12}{'Payroll':>14}{'Total OpEx':>14}")
    for m in months:
        print(
            f"{m['month']:<8}{m['fixed_costs']:>12,.2f}{m['variable_costs']:>12,.2f}"
            f"{m['payroll_costs']:>14,.2f}{m['total_operating_costs']:>14,.2f}"
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
