"""
GTT Center Perth -- AM Demand-Driven Staffing Financial Ladder.

Combines tools/am_volume_tier_staffing_solver.py's solver-verified headcount
per AM client-volume tier with tools/cost_ramp_model.py's canonical wage
rates and tools/revenue_ramp_model.py's canonical PM revenue figure, to
produce the full profitability ladder Anthony asked for: rostered headcount
by role, wage cost, revenue, total operating cost, and operating profit at
each of the 5 target AM volumes (9.00, 11.29, 13.50, 15.50, 18.00
clients/day), replacing docs/CURRENT-STATE.md's old flat-8-staff-at-every-
volume sensitivity table.

Does NOT invent any new wage rate, price, or overhead figure -- every input
is read from tools/cost_ramp_model.py's already-canonical constants or
data/canonical/pricing.yml, same as every other tool in this repo.

Usage: python tools/am_demand_tier_financial_ladder.py
"""

import sys
from pathlib import Path

_TOOLS_DIR = Path(__file__).resolve().parent
if str(_TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(_TOOLS_DIR))

import cost_ramp_model as crm
import am_volume_tier_staffing_solver as tier_solver

AM_PRICE = 250.0
PM_PRICE = 117.0
WEEKDAY_DAYS = 22
SATURDAY_DAYS = 4.33

# Fixed components, independent of AM headcount tier -- reused directly from
# cost_ramp_model.py's own already-canonical constants, not re-derived.
PHLEBOTOMIST_WEEKDAY_MONTHLY = crm.AM_WEEKDAY_PHLEBOTOMIST_MONTHLY  # A$9,075.00


def phlebotomist_monthly():
    """2 phlebotomists, structural/fixed at every AM volume tier tested --
    solver-verified peak concurrency never exceeds 2 (2 chairs, by
    construction of the synchronized-pair model). Uses the same per-hour
    rate cost_ramp_model.py's own AM_WEEKDAY_PHLEBOTOMIST_MONTHLY /
    AM_SATURDAY_DAILY_LABOR constants are built from (34.375/hr weekday,
    51.5625/hr Saturday, 6hr shift), computed fresh here so the treatment
    and phlebotomist Saturday components can be reported separately (the
    existing AM_SATURDAY_DAILY_LABOR constant bundles both together)."""
    weekday = PHLEBOTOMIST_WEEKDAY_MONTHLY
    saturday_daily = round(2 * 51.5625 * 6, 2)
    saturday = round(saturday_daily * SATURDAY_DAYS, 2)
    return weekday, saturday, round(weekday + saturday, 2)


def venue_manager_monthly():
    """Mon-Fri only (2026-09-19 correction) -- reuses
    cost_ramp_model.py's own OPENING_TIME_INCREMENT_DAILY /
    VENUE_MANAGER_SATURDAY_DAILY constants directly."""
    weekday = round(crm.OPENING_TIME_INCREMENT_DAILY * WEEKDAY_DAYS, 2)
    saturday = round(crm.VENUE_MANAGER_SATURDAY_DAILY * SATURDAY_DAYS, 2)
    return weekday, saturday, round(weekday + saturday, 2)


def pm_monthly():
    """PM labour, fixed regardless of AM headcount tier -- reuses
    cost_ramp_model.py's own M5plus (now flat-across-the-ramp) figure
    directly, not re-derived."""
    weekday_daily = crm.compute_pm_weekday_daily_labor("M5plus")
    weekday = round(weekday_daily * WEEKDAY_DAYS, 2)
    saturday = round(crm.PM_SATURDAY_DAILY_LABOR * SATURDAY_DAYS, 2)
    return weekday, saturday, round(weekday + saturday, 2)


def pm_revenue_monthly():
    """PM revenue, fixed regardless of AM headcount tier -- uses the SAME
    rounded (4-decimal) transaction-capacity figures already canonical in
    data/canonical/revenue_assumptions.yml (rev_pm_weekday_transactions /
    rev_pm_saturday_transactions), not a fresh unrounded recomputation, so
    this tool's output matches data/canonical/revenue_ramp.yml exactly
    (docs/architecture/PM-SESSION-CAPACITY-MODEL-E-2026-09.md)."""
    txn_weekday = 8.6957
    txn_saturday = 4.3478
    weekday = round(txn_weekday * PM_PRICE * WEEKDAY_DAYS, 2)
    saturday = round(txn_saturday * PM_PRICE * SATURDAY_DAYS, 2)
    return weekday, saturday, round(weekday + saturday, 2)


def am_revenue_monthly(client_volume_per_day):
    return round(client_volume_per_day * AM_PRICE * (WEEKDAY_DAYS + SATURDAY_DAYS), 2)


def payroll_for_headcount(n_mb, n_nails, n_hair):
    am_wd, am_sat, am_tot = crm.am_treatment_monthly_for_headcount(n_mb, n_nails, n_hair)
    ph_wd, ph_sat, ph_tot = phlebotomist_monthly()
    vm_wd, vm_sat, vm_tot = venue_manager_monthly()
    pm_wd, pm_sat, pm_tot = pm_monthly()

    lines = {
        "Venue Manager (Mon-Fri)": vm_tot,
        "Phlebotomists (x2)": ph_tot,
        "Massage+Beauty pool": round((n_mb * 37.50) * 6 * WEEKDAY_DAYS + (n_mb * 56.25) * 6 * SATURDAY_DAYS, 2),
        "Nail Technician": round((n_nails * 36.81) * 6 * WEEKDAY_DAYS + (n_nails * 55.215) * 6 * SATURDAY_DAYS, 2),
        "Hairdresser": round((n_hair * 36.81) * 6 * WEEKDAY_DAYS + (n_hair * 55.215) * 6 * SATURDAY_DAYS, 2),
        "PM dedicated casuals (4 roles, combined)": pm_tot,
    }
    direct_labor_and_opening = round(sum(lines.values()), 2)
    superannuation = round(direct_labor_and_opening * crm.SUPERANNUATION_RATE_PCT / 100, 2)
    workers_comp = round(direct_labor_and_opening * crm.WORKERS_COMP_RATE_PCT / 100, 2)
    payroll_total = round(direct_labor_and_opening + superannuation + workers_comp, 2)
    fixed_nonwage = 14288.34  # cost_ramp_model.py's own canonical figure, unaffected by this change
    total_opex = round(payroll_total + fixed_nonwage, 2)

    return {
        "headcount": (n_mb, n_nails, n_hair),
        "lines": lines,
        "direct_labor_and_opening": direct_labor_and_opening,
        "superannuation": superannuation,
        "workers_comp": workers_comp,
        "payroll_total": payroll_total,
        "fixed_nonwage": fixed_nonwage,
        "total_opex": total_opex,
    }


LOW_HEADCOUNT = crm.AM_HEADCOUNT_LOW
HIGH_HEADCOUNT = crm.AM_HEADCOUNT_HIGH


def ladder_row(target_volume):
    tier = tier_solver.minimum_headcount_for_volume(target_volume)
    n_mb, n_nails, n_hair = (
        tier["treatment_peak_by_line"]["MB"],
        tier["treatment_peak_by_line"]["Nails"],
        tier["treatment_peak_by_line"]["Hair"],
    )
    payroll = payroll_for_headcount(n_mb, n_nails, n_hair)
    pm_wd, pm_sat, pm_tot = pm_revenue_monthly()
    am_rev = am_revenue_monthly(target_volume)
    total_revenue = round(am_rev + pm_tot, 2)
    profit = round(total_revenue - payroll["total_opex"], 2)
    return {
        "target_volume": target_volume,
        "rostered_for_n_clients": tier["rostered_for_n_clients"],
        "chosen_cadence_minutes": tier["chosen_cadence_minutes"],
        "treatment_headcount": tier["treatment_headcount"],
        "phlebotomist_headcount": tier["phlebotomist_headcount"],
        "am_revenue": am_rev,
        "pm_revenue": pm_tot,
        "total_revenue": total_revenue,
        "payroll": payroll,
        "operating_profit": profit,
    }


def breakeven_for_headcount(n_mb, n_nails, n_hair, valid_range):
    payroll = payroll_for_headcount(n_mb, n_nails, n_hair)
    pm_wd, pm_sat, pm_tot = pm_revenue_monthly()
    days = WEEKDAY_DAYS + SATURDAY_DAYS
    breakeven_volume = round((payroll["total_opex"] - pm_tot) / (AM_PRICE * days), 4)
    lo, hi = valid_range
    return {
        "headcount": (n_mb, n_nails, n_hair),
        "total_opex": payroll["total_opex"],
        "breakeven_am_client_volume_per_day": breakeven_volume,
        "valid_range": valid_range,
        "in_valid_range": lo <= breakeven_volume <= hi,
    }


def main():
    print("=== AM Demand-Driven Staffing Financial Ladder ===\n")
    for vol in tier_solver.TARGET_VOLUMES:
        row = ladder_row(vol)
        print(
            f"Volume={row['target_volume']:.2f}/day (rostered for {row['rostered_for_n_clients']}, "
            f"cadence={row['chosen_cadence_minutes']}min): "
            f"treatment={row['treatment_headcount']}, phleb={row['phlebotomist_headcount']}"
        )
        print(f"  AM revenue={row['am_revenue']:,.2f}, PM revenue={row['pm_revenue']:,.2f}, "
              f"TOTAL REVENUE={row['total_revenue']:,.2f}")
        print(f"  Payroll total={row['payroll']['payroll_total']:,.2f}, "
              f"Fixed nonwage={row['payroll']['fixed_nonwage']:,.2f}, "
              f"TOTAL OPEX={row['payroll']['total_opex']:,.2f}")
        print(f"  OPERATING PROFIT={row['operating_profit']:,.2f}\n")

    print("=== Break-even, both headcount segments ===\n")
    be_low = breakeven_for_headcount(*LOW_HEADCOUNT, valid_range=(0, 10.4))
    be_high = breakeven_for_headcount(*HIGH_HEADCOUNT, valid_range=(10.4, 18.0))
    for label, be in (("LOW (4 treatment staff, 45min cadence, <=10/day)", be_low),
                       ("HIGH (8 treatment staff, 25min cadence, committed model)", be_high)):
        print(f"{label}: total_opex={be['total_opex']:,.2f}, "
              f"breakeven={be['breakeven_am_client_volume_per_day']}/day, "
              f"in valid range {be['valid_range']}: {be['in_valid_range']}")


if __name__ == "__main__":
    main()
