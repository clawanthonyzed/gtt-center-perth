"""Part 2 of the M workstream driver: exact-rounding costs, break-even, Year 1 with no ramp,
GST-stress, cash roll-forward (with a control that reproduces the old v0.4 ramped model),
Saturday proof, fill sensitivity, rent and lab-fee cases."""
import sys, json, math
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import m_model_driver as D
crm, L = D.crm, D.L

def ph_lines(ph):
    wd = round(ph * 34.375 * 6 * 22, 2)
    sat_daily = round(ph * 51.5625 * 6, 2)
    sat = round(sat_daily * 4.33, 2)
    return wd + sat

def total_costs(lines, ph):
    """Same arithmetic and rounding as tools/am_demand_tier_financial_ladder.payroll_for_headcount,
    with the phlebotomist count as a parameter (the ladder hard-codes 2)."""
    vm = D.VM
    mb = round((lines["MB"] * 37.50) * 6 * 22 + (lines["MB"] * 56.25) * 6 * 4.33, 2)
    na = round((lines["Nails"] * 36.81) * 6 * 22 + (lines["Nails"] * 55.215) * 6 * 4.33, 2)
    ha = round((lines["Hair"] * 36.81) * 6 * 22 + (lines["Hair"] * 55.215) * 6 * 4.33, 2)
    direct = round(vm + ph_lines(ph) + mb + na + ha + D.PM_LAB, 2)
    sup = round(direct * crm.SUPERANNUATION_RATE_PCT / 100, 2)
    wc = round(direct * crm.WORKERS_COMP_RATE_PCT / 100, 2)
    payroll = round(direct + sup + wc, 2)
    return round(payroll + 14288.34, 2), payroll

NOAM = total_costs({"MB": 0, "Nails": 0, "Hair": 0}, 0)[0]   # fixed costs with no AM roster
def am_labour_month(lines, ph):
    return round(total_costs(lines, ph)[0] - NOAM, 2)

LINES_BY_N = {n: D.solve(D.planning_counts(n))[0] for n in range(1, 19)}
PH_SOLVER = {n: D.solve(D.planning_counts(n))[1] for n in range(1, 19)}
def cost_n(n, phmode):
    lines = LINES_BY_N[n]
    ph = 2 if phmode == "base2" else PH_SOLVER[n]
    return total_costs(lines, ph)[0], am_labour_month(lines, ph), lines, ph

PM_REV = D.PM_REV
DAYS = D.DAYS
REVC = D.REV_PER_CLIENT_MONTH
FIXED = round(NOAM, 2)

def be(total_cost, gst=False, credits=1262.58):
    if not gst:
        return (total_cost - PM_REV) / REVC
    return (total_cost - credits - PM_REV * 10 / 11) / (REVC * 10 / 11)

# ---------- cash roll-forward (rules exactly as the 3-way model states them) -------------
CAPITAL, CAPEX0, RESERVE = 336198.00, 251198.00, 85000.00
DEFER = {4: 5600.00, 6: 7774.00}
def cash_model(rev, costs, credits, capital=CAPITAL, capex0=CAPEX0, months=24):
    n = len(rev)
    res = {"rows": []}
    cash = capital - capex0
    cum_repo = -capex0
    cum_gst = -capex0
    gst_prev = 0.0
    lowest = cash
    low_m = 0
    pay_repo = pay_gst = None
    for m in range(1, months + 1):
        i = min(m, n) - 1
        net = rev[i] - costs[i]
        gst_owed = round(rev[i] / 11 - credits[i], 2)
        d = DEFER.get(m, 0.0)
        cash = cash + net - gst_prev - d
        cum_repo += net - d
        cum_gst += net - gst_prev - d
        if cash < lowest: lowest, low_m = cash, m
        if pay_repo is None and cum_repo >= 0: pay_repo = m
        if pay_gst is None and cum_gst >= 0: pay_gst = m
        res["rows"].append({"m": m, "net": round(net, 2), "gst_paid": round(gst_prev, 2), "deferred": d,
                            "closing": round(cash, 2), "cum_repo": round(cum_repo, 2), "cum_gst": round(cum_gst, 2),
                            "gst_owed": round(gst_owed, 2), "net_after_gst": round(net - gst_owed, 2)})
        gst_prev = gst_owed
    res.update(lowest=round(lowest, 2), low_m=low_m, peak_funding=round(capital - lowest, 2),
               payback_repo=pay_repo, payback_gst=pay_gst, capital=capital)
    return res

def control_old_v04():
    rev = [61520.26, 91565.04, 113025.59, 133055.44] + [143070.37] * 8
    costs = [78093.29, 83782.53, 93733.11, 103033.67] + [107883.97] * 8
    credits = [1180.76, 1198.94, 1217.12, 1235.30] + [1262.58] * 8
    r = cash_model(rev, costs, credits)
    return r["peak_funding"], r["payback_repo"], r["payback_gst"], r["rows"][1]["gst_paid"], r["rows"][10]["cum_repo"]

# ---------- scenarios -------------------------------------------------------------------
def steady(rent=8000.0, ceiling=False, fee=0.0, clinical=0.0, fill=1.0, phmode="base2", n_override=None):
    """Steady state at full capacity (no ramp), returns dict of monthly figures."""
    clients = 18 * fill if n_override is None else n_override
    n_staff = math.ceil(clients - 1e-9)
    tc, _, lines, ph = cost_n(n_staff, phmode)
    am_rev = clients * REVC
    rev = am_rev + PM_REV
    other = 5088.34 - (1250.0 if ceiling else 0.0)
    occupancy_delta = (rent - 8000.0) - (1250.0 if ceiling else 0.0)
    fee_cost = fee * clients * DAYS
    costs = tc + occupancy_delta + fee_cost
    net = rev - costs
    credits = round((rent + other + 800.0) / 11 + fee_cost / 11, 2)
    gst_sales = round(rev / 11, 2) - round(clinical * clients * DAYS / 11, 2)
    # clinical share is GST-free: remove its GST from sales
    net = round(net, 2)
    net_gst = round(net - gst_sales + credits, 2)
    return {"clients": clients, "staff": n_staff, "rev": rev, "costs": costs, "net": net, "credits": credits,
            "gst_sales": gst_sales, "net_gst": net_gst, "lines": lines, "ph": ph}

def rent_capital(rent):
    return CAPITAL + 2 * (rent - 8000.0), CAPEX0 + 2 * (rent - 8000.0)

if __name__ == "__main__":
    print("CONTROL old v0.4:", control_old_v04())
    for n in (9, 18):
        print(n, cost_n(n, "base2")[:2])
    print("NOAM", NOAM, "FIXED", FIXED)
    for mode in ("base2", "scaled"):
        tc = cost_n(8, mode)[0]
        print(mode, "BE", round(be(tc), 3), "BE gst", round(be(tc, True), 3))
    print("BE full 18 roster", round(be(cost_n(18, "base2")[0]), 3), round(be(cost_n(18,"base2")[0], True), 3))


_BEST = None
def _best():
    global _BEST
    if _BEST is None:
        _BEST = D.range_over_placements()[0]
    return _BEST

def cost_policy(n, policy, phmode="base2"):
    if policy == "plan":
        return cost_n(n, phmode)[0]
    if policy == "spaced":
        t, ph, counts, lines = _best()[n]
        return total_costs(lines, 2 if phmode == "base2" else ph)[0]
    if policy == "stacked":
        lines, ph, _, _ = D.solve(D.stacked_counts(n))
        return total_costs(lines, 2 if phmode == "base2" else ph)[0]
    raise ValueError(policy)

def be_search(rent_delta=0.0, fee=0.0, gst=False, clinical=0.0, pm_factor=1.0, price=250.0, phmode="base2", rent=8000.0, ceiling=False, policy="plan"):
    """Lowest continuous AM volume per day at which monthly profit is zero, using the planning-case
    roster tier for ceil(volume). Returns (volume, tier). Repo method (ladder breakeven_for_headcount),
    applied tier by tier, so a break-even that falls above 9 picks up the 6 or 8 therapist cost."""
    other = 5088.34 - (1250.0 if ceiling else 0.0)
    credits = (rent + other + 800.0) / 11
    occ = (rent - 8000.0) - (1250.0 if ceiling else 0.0)
    pm = PM_REV * pm_factor
    for n in range(1, 19):
        tc = cost_policy(n, policy, phmode) + occ
        if not gst:
            per = price * DAYS - fee * DAYS
            v = (tc - pm) / per
        else:
            # fee includes GST and is claimable; clinical share of the package is GST-free
            per = price * DAYS - (price - clinical) / 11 * DAYS - fee * DAYS * 10 / 11
            v = (tc - credits - pm * 10 / 11) / per
        if v <= n + 1e-12 and v > n - 1:
            return round(v, 3), n
        if v <= n - 1 and n > 1:
            return float(n - 1), n   # already profitable at the foot of this tier
    return None, None
