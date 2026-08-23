"""
GTT Center Perth: Demand-Scenario Financial Model (6/12/18 clients/day).

Purpose: makes the 6-client demand-flexed staffing scenario a reproducible,
tested calculation rather than dossier-only prose (it previously existed
only as narrative figures in Chapter 31, with no committed script behind
them). Reuses the exact canonical wage rates and formula already
established in tools/cost_ramp_model.py (does not invent new rates),
parameterized by treatment headcount so any (Massage+Beauty, Nails, Hair)
combination can be costed, not just the single committed 8-person figure.

CALIBRATION, not a fresh assumption: verified this round to reproduce
tools/cost_ramp_model.py's own published constants exactly at the committed
8-treatment/2-phlebotomist headcount (AM_WEEKDAY_TREATMENT_STAFF_MONTHLY =
A$39,235.68, AM_WEEKDAY_PHLEBOTOMIST_MONTHLY = A$9,075.00,
AM_SATURDAY_DAILY_LABOR["scenario_table_1"] = A$3,293.91/day) before its
demand-flexed output is treated as trustworthy.

GENUINE, DISCLOSED LIMIT: at the committed 25-minute pair cadence, the
AM staffing solvers (tools/demand_driven_staffing_solver.py,
tools/am_staggered_staffing_solver.py) already established that 6 and 12
clients/day both still require the full 8 treatment staff, because peak
concurrency is driven by cadence overlap, not total client count. A
reduction to 4 treatment staff (2 Massage+Beauty + 1 Nail + 1 Hair) is only
solver-verified achievable at 6 clients/day if the pair cadence is widened
to 45 minutes or more, comfortably inside the WDP guidance window, but
NOT adopted as policy anywhere in this repo (requires a real day-ahead
rostering mechanism to know a given day will be a low-volume day, and
Anthony's confirmation that a widened cadence is acceptable client
experience). This module presents BOTH the committed-cadence (always 8
treatment staff) and demand-flexed (widened-cadence, 4 treatment staff at
6/day) figures side by side, never silently picking one as "the" answer.

Usage: python tools/demand_scenario_financial_model.py
"""

import sys
from pathlib import Path

_TOOLS_DIR = Path(__file__).resolve().parent
if str(_TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(_TOOLS_DIR))

import cost_ramp_model as crm  # reuse canonical wage rates, do not re-derive

AM_SHIFT_HOURS = 6
WEEKDAY_DAYS = 22
SATURDAY_DAYS = 4.33

WEEKDAY_RATES = {"MB": 37.50, "Nails": 36.81, "Hair": 36.81, "Phleb": 34.375}
SATURDAY_RATES = {"MB": 56.25, "Nails": 55.215, "Hair": 55.215, "Phleb": 51.5625}

SUPERANNUATION_RATE_PCT = crm.SUPERANNUATION_RATE_PCT
WORKERS_COMP_RATE_PCT = crm.WORKERS_COMP_RATE_PCT

# Fixed components that do NOT change with AM treatment headcount (per
# Chapter 31's own established scope: "only changes AM weekday treatment-
# staff labor... AM Saturday labor [phlebotomist portion], PM labor, and
# the opening-time increment are held at Table 1's steady-state values").
AM_PHLEBOTOMIST_WEEKDAY = round(2 * WEEKDAY_RATES["Phleb"] * AM_SHIFT_HOURS * WEEKDAY_DAYS, 2)
AM_PHLEBOTOMIST_SATURDAY_DAILY = round(2 * SATURDAY_RATES["Phleb"] * AM_SHIFT_HOURS, 2)


def am_treatment_weekday(n_mb, n_nails, n_hair):
    return round(
        (n_mb * WEEKDAY_RATES["MB"] + n_nails * WEEKDAY_RATES["Nails"] + n_hair * WEEKDAY_RATES["Hair"])
        * AM_SHIFT_HOURS * WEEKDAY_DAYS,
        2,
    )


def am_treatment_saturday_daily(n_mb, n_nails, n_hair):
    return round(
        (n_mb * SATURDAY_RATES["MB"] + n_nails * SATURDAY_RATES["Nails"] + n_hair * SATURDAY_RATES["Hair"])
        * AM_SHIFT_HOURS,
        2,
    )


def calibrate():
    """Reproduces tools/cost_ramp_model.py's own published committed
    constants exactly, at 4 Massage+Beauty + 2 Nails + 2 Hair + 2
    Phlebotomists (Table 1/Table 2's committed headcount)."""
    treatment_weekday = am_treatment_weekday(4, 2, 2)
    treatment_saturday_daily = am_treatment_saturday_daily(4, 2, 2)
    phleb_weekday = AM_PHLEBOTOMIST_WEEKDAY
    phleb_saturday_daily = AM_PHLEBOTOMIST_SATURDAY_DAILY

    checks = {
        "treatment_weekday": (treatment_weekday, crm.AM_WEEKDAY_TREATMENT_STAFF_MONTHLY),
        "phlebotomist_weekday": (phleb_weekday, crm.AM_WEEKDAY_PHLEBOTOMIST_MONTHLY),
        "combined_saturday_daily": (
            round(treatment_saturday_daily + phleb_saturday_daily, 2),
            crm.AM_SATURDAY_DAILY_LABOR["scenario_table_1"],
        ),
    }
    all_match = all(abs(computed - published) < 0.01 for computed, published in checks.values())
    return checks, all_match


def compute_scenario(n_mb, n_nails, n_hair, am_price_per_client, client_volume, pm_revenue,
                      ancillary_revenue, saturday_headcount=(4, 2, 2)):
    """Computes Total Revenue, Total Operating Costs, and Net Operating
    Result for a given AM weekday treatment headcount and client volume,
    holding every other component (phlebotomists, Saturday treatment
    headcount, PM, opening increment, fixed non-wage overhead) at the
    Table 1 Month 5+ steady-state values already published and tested in
    tools/master_financial_model.py / tools/cost_ramp_model.py.

    saturday_headcount defaults to the committed (4, 2, 2) regardless of
    the weekday n_mb/n_nails/n_hair passed in: this matches Chapter 31's
    own explicitly disclosed scope for the demand-flexed alternative
    ("only changes AM weekday treatment-staff labor... AM Saturday labor
    [is] held at Table 1's steady-state values"), not an oversight. Pass a
    different saturday_headcount only when deliberately testing a wider
    scope than Chapter 31's own published scenario."""
    am_revenue = round(client_volume * am_price_per_client * (WEEKDAY_DAYS + SATURDAY_DAYS), 2)
    total_revenue = round(am_revenue + pm_revenue + ancillary_revenue, 2)

    treatment_weekday = am_treatment_weekday(n_mb, n_nails, n_hair)
    sat_mb, sat_nails, sat_hair = saturday_headcount
    treatment_saturday = round(am_treatment_saturday_daily(sat_mb, sat_nails, sat_hair) * SATURDAY_DAYS, 2)
    phleb_weekday = AM_PHLEBOTOMIST_WEEKDAY
    phleb_saturday = round(AM_PHLEBOTOMIST_SATURDAY_DAILY * SATURDAY_DAYS, 2)

    am_direct_labor = round(treatment_weekday + treatment_saturday + phleb_weekday + phleb_saturday, 2)

    # PM/opening/fixed-nonwage held at the published Table 1 steady-state
    # values (Chapter 27/28), reused directly, not re-derived here.
    pm_and_opening = crm.PM_WEEKDAY_M5PLUS_DAILY_LABOR_CANONICAL_ANCHOR * WEEKDAY_DAYS \
        + crm.PM_SATURDAY_DAILY_LABOR * SATURDAY_DAYS \
        + crm.OPENING_TIME_INCREMENT_DAILY * WEEKDAY_DAYS \
        + crm.VENUE_MANAGER_SATURDAY_DAILY * SATURDAY_DAYS
    pm_and_opening = round(pm_and_opening, 2)

    direct_labor_and_opening = round(am_direct_labor + pm_and_opening, 2)
    superannuation = round(direct_labor_and_opening * SUPERANNUATION_RATE_PCT / 100, 2)
    workers_comp = round(direct_labor_and_opening * WORKERS_COMP_RATE_PCT / 100, 2)
    payroll_total = round(direct_labor_and_opening + superannuation + workers_comp, 2)

    fixed_nonwage = crm.CanonicalCostInputs().fixed_nonwage_excl_marketing + \
        crm.find_record(crm.load_yaml("opex.yml")["records"], "opex_marketing_ads_steady_state")["amount"]
    fixed_nonwage = round(fixed_nonwage, 2)

    total_operating_costs = round(payroll_total + fixed_nonwage, 2)
    net_operating_result = round(total_revenue - total_operating_costs, 2)

    return {
        "client_volume": client_volume,
        "am_revenue": am_revenue,
        "total_revenue": total_revenue,
        "am_treatment_headcount": n_mb + n_nails + n_hair,
        "am_direct_labor": am_direct_labor,
        "payroll_total": payroll_total,
        "fixed_nonwage": fixed_nonwage,
        "total_operating_costs": total_operating_costs,
        "net_operating_result": net_operating_result,
    }


def main():
    print("=== Calibration: reproduce tools/cost_ramp_model.py's own published constants ===\n")
    checks, all_match = calibrate()
    for name, (computed, published) in checks.items():
        status = "MATCHES" if abs(computed - published) < 0.01 else "DOES NOT MATCH: STOP, DO NOT TRUST SCENARIOS BELOW"
        print(f"  {name}: computed={computed}, published={published} -> {status}")
    if not all_match:
        print("\nCALIBRATION FAILED.")
        return

    pricing = crm.load_yaml("pricing.yml")
    am_price = crm.find_record(pricing["records"], "am_price_used_for_revenue")["price"]
    pm_revenue = 36225.69   # Chapter 9/28's own published, fixed PM revenue figure
    ancillary_revenue = 0.0

    print("\n=== Committed-cadence view: 8 treatment staff at every volume (the venture's actual committed rostering) ===")
    for label, volume in (("18/day (Table 1, committed)", 18), ("12/day (Table 2, secondary)", 12), ("6/day", 6)):
        r = compute_scenario(4, 2, 2, am_price, volume, pm_revenue, ancillary_revenue)
        print(f"  {label}: revenue={r['total_revenue']}, opex={r['total_operating_costs']}, "
              f"result={r['net_operating_result']}, AM treatment headcount={r['am_treatment_headcount']}")

    print("\n=== Demand-flexed view, NOT adopted as policy: staffing solver-verified appropriate to each volume ===")
    print("(18/day and 12/day cannot reduce below 8 treatment staff at the committed 25-min cadence, solver-verified;")
    print(" 6/day CAN reduce to 4 only if the cadence is widened to 45min+, requiring Anthony's confirmation)")
    configs = {18: (4, 2, 2), 12: (4, 2, 2), 6: (2, 1, 1)}
    for label, volume in (("18/day", 18), ("12/day", 12), ("6/day (widened cadence, not adopted)", 6)):
        n_mb, n_nails, n_hair = configs[volume]
        r = compute_scenario(n_mb, n_nails, n_hair, am_price, volume, pm_revenue, ancillary_revenue)
        print(f"  {label}: revenue={r['total_revenue']}, opex={r['total_operating_costs']}, "
              f"result={r['net_operating_result']}, AM treatment headcount={r['am_treatment_headcount']}")

    print("\n=== Cross-check against Chapter 31's own published 6-day demand-flexed figures ===")
    r6 = compute_scenario(2, 1, 1, am_price, 6, pm_revenue, ancillary_revenue)
    published_opex = 88239.03
    published_result = -12518.34
    opex_match = abs(r6["total_operating_costs"] - published_opex) < 0.02
    result_match = abs(r6["net_operating_result"] - published_result) < 0.02
    print(f"  Computed opex={r6['total_operating_costs']} vs published {published_opex}: "
          f"{'MATCHES (within rounding)' if opex_match else 'DOES NOT MATCH'}")
    print(f"  Computed result={r6['net_operating_result']} vs published {published_result}: "
          f"{'MATCHES (within rounding)' if result_match else 'DOES NOT MATCH'}")


if __name__ == "__main__":
    main()
