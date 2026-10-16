"""
GTT Center Perth, overhaul 2026-10-16, workstream M.

Thin driver around the repo's own calculators. It does not replace them.
  - tools/am_volume_tier_staffing_solver.py supplies the line-by-line peak
    concurrency solver (assign_and_check_odd) and the draw-concurrency check
    (phlebotomist_headcount_check_odd). Only the INPUT (which pair-slots the
    booked clients sit in) is changed, by swapping build_clients_odd.
  - tools/cost_ramp_model.py supplies every wage rate, the 6-hour shift, the
    Saturday penalty, super, workers comp, PM labour and the Venue Manager.
  - tools/am_demand_tier_financial_ladder.py supplies PM revenue and the
    non-wage overhead, and its payroll_for_headcount() is the control: the
    driver must reproduce its A$107,883.97 at 18 clients.
Cadence is fixed at 25 minutes. There is no 45-minute cadence path.
"""
import sys, json, itertools, math
from pathlib import Path
REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO / "tools"))
import am_volume_tier_staffing_solver as S
import cost_ramp_model as crm
import am_demand_tier_financial_ladder as L

CADENCE = 25
SLOTS = 9                      # 07:00 to 10:20 inclusive, 25 minutes apart
WD, SAT = 22, 4.33
DAYS = WD + SAT                # 26.33
PRICE = 250.0
ONCOST = 1 + crm.SUPERANNUATION_RATE_PCT / 100 + crm.WORKERS_COMP_RATE_PCT / 100   # 1.137
RATE = {"MB": 37.50, "Nails": 36.81, "Hair": 36.81, "PH": 34.375}
SATRATE = {"MB": 56.25, "Nails": 55.215, "Hair": 55.215, "PH": 51.5625}
HOURS = 6

# ---------- placement of booked clients in the 25-minute pair-slots -------------
_orig = S.build_clients_odd
def _mk(counts):
    def f(n, cad):
        cl = []
        for k, c in enumerate(counts):
            for ch in ("A", "B")[:c]:
                x = k * cad
                cl.append({"id": len(cl) + 1, "chair": ch, "x": x,
                           "s1": (x + S.DRAW_MINUTES, x + S.DRAW_MINUTES + S.SERVICE_MINUTES),
                           "s2": (x + 60 + S.DRAW_MINUTES, x + 60 + S.DRAW_MINUTES + S.SERVICE_MINUTES)})
        return cl
    return f

def planning_counts(n):
    """Planning case: bookings fill from the 07:00 slot onward, ONE client per
    slot first (Chair A, the repo's own default), a second client (Chair B)
    only once all nine slots have one, second clients again from the earliest slot."""
    c = [0] * SLOTS
    for k in range(min(n, SLOTS)): c[k] = 1
    for k in range(max(0, n - SLOTS)): c[k] = 2
    return tuple(c)

def stacked_counts(n):
    """Repo solver as published: full pairs from 07:00, a single last."""
    c = [0] * SLOTS
    for k in range(math.ceil(n / 2)): c[k] = 2
    if n % 2: c[math.ceil(n / 2) - 1] = 1
    return tuple(c)

def solve(counts):
    n = sum(counts)
    S.build_clients_odd = _mk(counts)
    try:
        r = S.assign_and_check_odd(n, CADENCE)
        ph = S.phlebotomist_headcount_check_odd(n, CADENCE)
    finally:
        S.build_clients_odd = _orig
    return r["peak_by_line"], ph, r["last_draw1_minute"], r["last_departure_minute"]

def range_over_placements():
    """Best and worst therapist count over every way of placing n clients in the
    nine slots (0, 1 or 2 per slot). 19,683 patterns, each run through the repo solver."""
    best, worst = {}, {}
    for counts in itertools.product((0, 1, 2), repeat=SLOTS):
        n = sum(counts)
        if n == 0: continue
        lines, ph, _, _ = solve(counts)
        t = sum(lines.values())
        if n not in best or t < best[n][0]: best[n] = (t, ph, counts, lines)
        if n not in worst or t > worst[n][0]: worst[n] = (t, ph, counts, lines)
    return best, worst

# ---------- money -------------------------------------------------------------
def labour(lines, ph):
    wd = HOURS * (lines["MB"] * RATE["MB"] + lines["Nails"] * RATE["Nails"] + lines["Hair"] * RATE["Hair"] + ph * RATE["PH"])
    sat = HOURS * (lines["MB"] * SATRATE["MB"] + lines["Nails"] * SATRATE["Nails"] + lines["Hair"] * SATRATE["Hair"] + ph * SATRATE["PH"])
    return {"wd_wage": wd, "sat_wage": sat, "wd_inc": wd * ONCOST, "sat_inc": sat * ONCOST,
            "month_inc": (wd * WD + sat * SAT) * ONCOST}

PM_REV = L.pm_revenue_monthly()[2]
VM = L.venue_manager_monthly()[2]
PM_LAB = L.pm_monthly()[2]
NONWAGE = 14288.34
FIXED_LAB_INC = (VM + PM_LAB) * ONCOST
FIXED = round(NONWAGE + FIXED_LAB_INC, 2)          # 36,738.11 in the 3-way model
REV_PER_CLIENT_MONTH = PRICE * DAYS                # 6,582.50

def row(n, phleb_mode):
    lines, ph_solver, last_d1, last_dep = solve(planning_counts(n))
    ph = 2 if phleb_mode == "base2" else ph_solver
    lab = labour(lines, ph)
    rev_day = PRICE * n
    rev_m = REV_PER_CLIENT_MONTH * n
    contrib_m = rev_m - lab["month_inc"]
    net = contrib_m + PM_REV - FIXED
    return {"n": n, "lines": lines, "therapists": sum(lines.values()), "ph": ph, "ph_solver": ph_solver,
            "rev_day": rev_day, "lab_wd_inc": lab["wd_inc"], "lab_sat_inc": lab["sat_inc"],
            "contrib_wd": rev_day - lab["wd_inc"], "contrib_sat": rev_day - lab["sat_inc"],
            "lab_month": lab["month_inc"], "rev_month": rev_m, "contrib_month": contrib_m, "net_month": net,
            "last_d1": last_d1}

def control():
    r = row(18, "base2")
    pay = L.payroll_for_headcount(4, 2, 2)
    return {"driver_net_18": round(r["net_month"], 2), "ladder_opex_18": pay["total_opex"],
            "driver_total_costs_18": round(FIXED + r["lab_month"], 2)}

if __name__ == "__main__":
    print("FIXED", round(FIXED, 2), "PM_REV", PM_REV, "VM", VM, "PM_LAB", PM_LAB, "REV/client/month", REV_PER_CLIENT_MONTH)
    print("CONTROL", control())
    for mode in ("base2", "scaled"):
        print("MODE", mode)
        for n in range(1, 19):
            r = row(n, mode)
            print(n, r["lines"], r["therapists"], "ph", r["ph"], "labWD %.2f labSAT %.2f labM %.2f rev/d %.0f cWD %.2f cSAT %.2f cM %.2f NET %.2f" % (r["lab_wd_inc"], r["lab_sat_inc"], r["lab_month"], r["rev_day"], r["contrib_wd"], r["contrib_sat"], r["contrib_month"], r["net_month"]))
