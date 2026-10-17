"""M2 part 4: re-computes every break-even figure that sits in the 3-way model, P&L and cash-flow documents
under the adaptive phlebotomist rule (phmode 'scaled'), using the same functions as the 2026-10-16 M driver."""
import sys, math
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import m2_driver as M
D, P, n3 = M.D, M.P, M.n3

def bes(**kw):
    kw.setdefault("phmode", "scaled"); kw.setdefault("policy", "plan")
    return P.be_search(**kw)

print("## rent cases (repo / GST)")
for name, (rent, ceil_) in {"8000": (8000.0, False), "9500": (9500.0, False), "10500": (10500.0, False), "ceiling": (10500.0, True)}.items():
    print(name, bes(rent=rent, ceiling=ceil_), bes(rent=rent, ceiling=ceil_, gst=True))
print("## lab fee")
for name, (rent, ceil_) in {"8000": (8000.0, False), "10500": (10500.0, False), "ceiling": (10500.0, True)}.items():
    for fee in (0, 10, 20, 30):
        print(name, fee, bes(rent=rent, ceiling=ceil_, fee=fee), bes(rent=rent, ceiling=ceil_, fee=fee, gst=True))
print("## two tier (headline rent)")
for cl in (0, 25, 50, 75):
    print(cl, bes(gst=True, clinical=cl))
print("## sensitivities")
def sens(am_clients, am_price, pm_factor, rent_delta=0.0):
    tc = P.cost_n(9, "scaled")[0] + rent_delta
    pm = P.PM_REV * pm_factor
    cr = (8000 + rent_delta + 5088.34 + 800) / 11
    be_ = (tc - pm) / (am_price * P.DAYS)
    beg = (tc - cr - pm * 10 / 11) / (am_price * P.DAYS * 10 / 11)
    return n3(be_), n3(beg)
print("base", sens(18, 250, 1)); print("vol-20", sens(14.4, 250, 0.8)); print("price-10", sens(18, 225, 0.9))
print("rent7000", sens(18, 250, 1, -1000)); print("rent9000", sens(18, 250, 1, 1000)); print("12/day", sens(12, 250, 1))
print("## two-stream")
for label, tc in (("old adaptive", P.cost_n(8, "base2")[0]), ("new adaptive", P.cost_n(8, "scaled")[0]), ("full roster", P.cost_n(18, "base2")[0])):
    rev = 143070.37
    v = tc / rev * 684
    am = v * 474 / 684; pm = v - am
    print(label, round(v, 1), round(am, 1), round(pm, 1), round(am / P.DAYS, 2), round(v / 684 * 100, 1))
print("## runway 70% (staff 13 -> ph 2, unchanged)")

# ---- consistent 'spaced' (cheapest pattern) version of be_search, same logic as m_part2.be_search ----
import m2_part2 as Q
lo, hi = Q.extremes()
CHEAP = {n: lo[n][0] for n in range(1, 19)}
PLAN = {n: P.cost_n(n, "scaled")[0] for n in range(1, 19)}
def be_cost(costs, rent=8000.0, ceiling=False, fee=0.0, gst=False, clinical=0.0, price=250.0, pm_factor=1.0):
    other = 5088.34 - (1250.0 if ceiling else 0.0)
    credits = (rent + other + 800.0) / 11
    occ = (rent - 8000.0) - (1250.0 if ceiling else 0.0)
    pm = P.PM_REV * pm_factor
    for n in range(1, 19):
        tc = costs[n] + occ
        if not gst:
            v = (tc - pm) / (price * P.DAYS - fee * P.DAYS)
        else:
            per = price * P.DAYS - (price - clinical) / 11 * P.DAYS - fee * P.DAYS * 10 / 11
            v = (tc - credits - pm * 10 / 11) / per
        if v <= n + 1e-12 and v > n - 1: return round(v, 3), n
        if v <= n - 1 and n > 1: return float(n - 1), n
print("## SPACED (cheapest) versions")
for name, (rent, ceil_) in {"8000": (8000.0, False), "9500": (9500.0, False), "10500": (10500.0, False), "ceiling": (10500.0, True)}.items():
    print("rent", name, be_cost(CHEAP, rent, ceil_), be_cost(CHEAP, rent, ceil_, gst=True), "plan", be_cost(PLAN, rent, ceil_), be_cost(PLAN, rent, ceil_, gst=True))
for name, (rent, ceil_) in {"8000": (8000.0, False), "10500": (10500.0, False), "ceiling": (10500.0, True)}.items():
    for fee in (0, 10, 20, 30):
        print("fee", name, fee, be_cost(CHEAP, rent, ceil_, fee), be_cost(CHEAP, rent, ceil_, fee, gst=True))
for cl in (0, 25, 50, 75):
    print("clinical", cl, be_cost(CHEAP, gst=True, clinical=cl))
