import sys, json, math
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import m_model_driver as D
import m_part2 as P


def a(x, d=2):
    s = f"{abs(x):,.{d}f}"
    return ("-A$" if x < -0.004 else "A$") + s


def n3(x):
    return f"{x:.3f}"


best, worst = D.range_over_placements()

# ---- 1. roster table ----
rows = []
for n in range(1, 19):
    tcb, labb, lines, phb = P.cost_n(n, "base2")
    tcs, labs, _, phs = P.cost_n(n, "scaled")
    lb = D.labour(lines, phb)
    ls = D.labour(lines, phs)
    rev_m = n * P.REVC
    lastmin = D.S.fmt_time(D.solve(D.planning_counts(n))[2])
    bl = best[n][3]
    rows.append(dict(n=n, lines=lines, th=sum(lines.values()), ph=phb, ph_s=phs, lab_wd=lb["wd_inc"], lab_sat=lb["sat_inc"],
                     lab_month=labb, rev_day=250 * n, c_day=250 * n - lb["wd_inc"], c_sat=250 * n - lb["sat_inc"],
                     c_month=rev_m - labb, net=rev_m + P.PM_REV - tcb, net_s=rev_m + P.PM_REV - tcs,
                     c_month_s=rev_m - labs, lab_month_s=labs, lab_wd_s=ls["wd_inc"], lab_sat_s=ls["sat_inc"], last=lastmin,
                     best_th=best[n][0], worst_th=worst[n][0], best_ph=best[n][1], best_lines=bl,
                     best_net=rev_m + P.PM_REV - P.total_costs(bl, 2)[0],
                     best_net_s=rev_m + P.PM_REV - P.total_costs(bl, best[n][1])[0]))

print("## ROSTER base (2 phlebotomist minimum)")
for r in rows:
    print(f"| {r['n']} | {r['ph']} | {r['lines']['MB']}/{r['lines']['Nails']}/{r['lines']['Hair']}={r['th']} | {r['ph']+r['th']} | {r['last']} | {a(r['lab_wd'])} | {a(r['lab_sat'])} | {a(r['rev_day'],0)} | {a(r['c_day'])} | {a(r['c_sat'])} | {a(r['lab_month'])} | {a(r['rev_day']*0+r['n']*P.REVC)} | {a(r['c_month'])} | {a(r['net'])} | steered {r['best_th']} {a(r['best_net'])} | worst {r['worst_th']}")
print("## ROSTER scaled phlebotomists")
for r in rows:
    print(f"| {r['n']} | ph {r['ph_s']} | {a(r['lab_wd_s'])} | {a(r['lab_sat_s'])} | {a(r['lab_month_s'])} | {a(r['c_month_s'])} | {a(r['net_s'])} | steered ph {r['best_ph']} {a(r['best_net_s'])}")

# ---- 2. break-even ----
print("## BREAK-EVEN")
for mode in ("base2", "scaled"):
    tc, lab, lines, ph = P.cost_n(8, mode)
    print(mode, "tc", tc, "lab", lab, "fixed", P.FIXED, "PM", P.PM_REV, "cover", round(tc - P.PM_REV, 2), "BE", n3(P.be(tc)), "GST BE", n3(P.be(tc, True)),
          "pct18", round(P.be(tc) / 18 * 100, 1), "MoS", round(18 - P.be(tc), 3), "MoSpct", round((18 - P.be(tc)) / 18 * 100, 1))
tc18 = P.cost_n(18, "base2")[0]
print("full roster", tc18, round(tc18 - P.PM_REV, 2), n3(P.be(tc18)), n3(P.be(tc18, True)))

# ---- 3. year 1 no ramp ----
print("## YEAR 1")
h = P.steady()
print("steady", {k: (round(v, 2) if isinstance(v, float) else v) for k, v in h.items() if k != "lines"})
cm = P.cash_model([h["rev"]] * 12, [h["costs"]] * 12, [h["credits"]] * 12)
print("CASH", {k: cm[k] for k in ("lowest", "low_m", "peak_funding", "payback_repo", "payback_gst")})
for r in cm["rows"][:13]:
    print(r)
y1 = sum(r["net"] for r in cm["rows"][:12])
y1g = sum(r["net_after_gst"] for r in cm["rows"][:12])
print("Y1 repo", round(y1, 2), "Y1 gst", round(y1g, 2), "rev", round(h["rev"] * 12, 2), "costs", round(h["costs"] * 12, 2))
print("margin", round(h["net"] / h["rev"] * 100, 3), "annual", round(h["net"] * 12, 2), round(h["net_gst"] * 12, 2))

# ---- 4. rent cases ----
print("## RENT CASES")
cases = {"A$8,000": (8000.0, False), "A$9,500": (9500.0, False), "A$10,500": (10500.0, False), "ceiling": (10500.0, True)}
for name, (rent, ceil_) in cases.items():
    s = P.steady(rent=rent, ceiling=ceil_)
    cap, cap0 = P.rent_capital(rent)
    cmr = P.cash_model([s["rev"]] * 12, [s["costs"]] * 12, [s["credits"]] * 12, capital=cap, capex0=cap0)
    occ = (rent - 8000.0) - (1250.0 if ceil_ else 0.0)
    tc_staff = P.cost_n(9, "base2")[0] + occ
    be_r = P.be_search(rent=rent, ceiling=ceil_, policy="spaced")[0]
    be_g = P.be_search(rent=rent, ceiling=ceil_, gst=True, policy="spaced")[0]
    y1 = sum(r["net"] for r in cmr["rows"][:12])
    y1g = sum(r["net_after_gst"] for r in cmr["rows"][:12])
    print(name, "net", round(s["net"], 2), "gst", round(s["net_gst"], 2), "BE", n3(be_r), "BEgst", n3(be_g), "peak", cmr["peak_funding"], "low", cmr["lowest"], cmr["low_m"], "pay", cmr["payback_repo"], cmr["payback_gst"], "Y1", round(y1, 2), round(y1g, 2), "cap", cap)

# ---- 5. fill ----
print("## FILL")
for fill in (1.0, 0.85, 0.70):
    s = P.steady(fill=fill)
    cmf = P.cash_model([s["rev"]] * 72, [s["costs"]] * 72, [s["credits"]] * 72, months=72)
    y1 = sum(r["net"] for r in cmf["rows"][:12])
    print("fill", fill, "clients", round(s["clients"], 2), "staff", s["staff"], "net", round(s["net"], 2), "gst", round(s["net_gst"], 2), "peak", cmf["peak_funding"], "low", cmf["lowest"], cmf["low_m"], "Y1", round(y1, 2), "pay", cmf["payback_repo"], cmf["payback_gst"])
s = P.steady(fill=0.70)
cmf = P.cash_model([s["rev"]] * 40, [s["costs"]] * 40, [s["credits"]] * 40, months=40)
print("70% closing cash", [r["closing"] for r in cmf["rows"][:16]])
print("70% net after GST", round(s["net_gst"], 2))

# ---- 6. lab fee ----
print("## LAB FEE")
for name, (rent, ceil_) in cases.items():
    for fee in (0, 10, 20, 30):
        s = P.steady(rent=rent, ceiling=ceil_, fee=fee)
        cap, cap0 = P.rent_capital(rent)
        cmr = P.cash_model([s["rev"]] * 72, [s["costs"]] * 72, [s["credits"]] * 72, capital=cap, capex0=cap0)
        occ = (rent - 8000.0) - (1250.0 if ceil_ else 0.0)
        tc = P.cost_n(9, "base2")[0] + occ
        be_r = P.be_search(rent=rent, ceiling=ceil_, fee=fee, policy="spaced")
        be_g = P.be_search(rent=rent, ceiling=ceil_, fee=fee, gst=True, policy="spaced")
        print(name, "fee", fee, "net", round(s["net"], 2), "gst", round(s["net_gst"], 2), "BE", be_r, be_g, "peak", cmr["peak_funding"], "headroom", round(cmr["lowest"], 2), "pay", cmr["payback_repo"], cmr["payback_gst"])

# ---- 7. two-tier ----
print("## TWO TIER")
for name, (rent, ceil_) in cases.items():
    for cl in (0, 25, 50, 75):
        s = P.steady(rent=rent, ceiling=ceil_, clinical=cl)
        cap, cap0 = P.rent_capital(rent)
        saved = cl * 18 * P.DAYS / 11
        # reduce GST owed by saved: model as extra credit
        cmr = P.cash_model([s["rev"]] * 24, [s["costs"]] * 24, [s["credits"] + saved] * 24, capital=cap, capex0=cap0)
        occ = (rent - 8000.0) - (1250.0 if ceil_ else 0.0)
        tc = P.cost_n(9, "base2")[0] + occ
        be_g = P.be_search(rent=rent, ceiling=ceil_, gst=True, clinical=cl, policy="spaced")
        print(name, "clinical", cl, "saved", round(saved, 2), "net_gst", round(s["net_gst"], 2), "BEgst", be_g, "payback_gst", cmr["payback_gst"])

# ---- 8. sensitivity ----
print("## SENS")


def sens(am_clients, am_price, pm_factor, rent_delta=0.0):
    am_rev = am_clients * am_price * P.DAYS
    pm = P.PM_REV * pm_factor
    n_staff = math.ceil(am_clients)
    tc = P.cost_n(n_staff, "base2")[0] + rent_delta
    net = am_rev + pm - tc
    rev = am_rev + pm
    cr = (8000 + rent_delta + 5088.34 + 800) / 11
    g = net - rev / 11 + cr
    be_ = (P.cost_n(9, "base2")[0] + rent_delta - pm) / (am_price * P.DAYS)
    beg = (P.cost_n(9, "base2")[0] + rent_delta - cr - pm * 10 / 11) / (am_price * P.DAYS * 10 / 11)
    return round(net, 2), round(g, 2), n3(be_), n3(beg)


print("base", sens(18, 250, 1))
print("vol-20", sens(14.4, 250, 0.8))
print("price-10", sens(18, 225, 0.9))
print("rent7000", sens(18, 250, 1, -1000))
print("rent9000", sens(18, 250, 1, 1000))
print("12/day PM full", sens(12, 250, 1))

# ---- 9. balance sheet ----
print("## BALANCE")
rows12 = cm["rows"]
for m in (6, 12):
    cash = rows12[m - 1]["closing"]
    cumnet_gst = sum(r["net_after_gst"] for r in rows12[:m])
    fitout = 204132.0 + (13374.0 if m >= 6 else (5600.0 if m >= 4 else 0))
    if m >= 6:
        fitout = 204132.0 + 13374.0
    assets = cash + fitout + 2585.0 + 8000.0
    gst_pay = rows12[m - 1]["gst_owed"]
    re = -36481.0 + cumnet_gst
    equity = 336198.0 + re
    print(m, "cash", cash, "fitout", fitout, "assets", round(assets, 2), "gst payable", gst_pay, "RE", round(re, 2), "equity", round(equity, 2), "check", round(assets - gst_pay - equity, 2))
