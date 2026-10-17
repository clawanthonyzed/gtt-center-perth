"""GTT Center Perth, overhaul 2026-10-17, workstream M2 (R1 adaptive phlebotomy, R2 10% post-test discount).
Thin driver ONLY. It imports the 2026-10-16 M drivers (which wrap tools/am_volume_tier_staffing_solver.py,
tools/cost_ramp_model.py and tools/am_demand_tier_financial_ladder.py) and changes one input:
the phlebotomist count per morning ('scaled' = the repo solver's own draw-concurrency count).
No new calculator: every wage, on-cost, revenue and roster number comes from the repo tools."""
import sys, math
from pathlib import Path
REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO / "docs/overhaul-2026-10-16/M-model"))
sys.path.insert(0, str(REPO / "tools"))
import m_model_driver as D
import m_part2 as P

def a(x, d=2):
    s = f"{abs(x):,.{d}f}"
    return ("-A$" if x < -0.004 else "A$") + s
def n3(x): return f"{x:.3f}"

ON = D.ONCOST
PH_WD, PH_SAT = 34.375, 51.5625
CASUAL_MIN_H = 3.0   # tools/cost_ramp_model.py CASUAL_MINIMUM_ENGAGEMENT_HOURS (wages.yml, VERIFIED)

def table():
    rows = []
    for n in range(1, 19):
        tb, lb, lines, pb = P.cost_n(n, "base2")
        ta, la, _, pa = P.cost_n(n, "scaled")
        lbd, lad = D.labour(lines, pb), D.labour(lines, pa)
        rev_m = n * P.REVC
        rows.append(dict(n=n, lines=lines, th=sum(lines.values()), pb=pb, pa=pa,
            wd_b=lbd["wd_inc"], wd_a=lad["wd_inc"], sat_a=lad["sat_inc"], sat_b=lbd["sat_inc"],
            cwd_a=250*n-lad["wd_inc"], cwd_b=250*n-lbd["wd_inc"], csat_a=250*n-lad["sat_inc"],
            lab_b=lb, lab_a=la, cm_a=rev_m-la, net_b=rev_m+P.PM_REV-tb, net_a=rev_m+P.PM_REV-ta,
            tc_b=tb, tc_a=ta, last=D.S.fmt_time(D.solve(D.planning_counts(n))[2])))
    return rows

if __name__ == "__main__":
    rows = table()
    print("## A TABLE")
    for r in rows:
        print(f"| {r['n']} | {r['pb']}->{r['pa']} | {r['lines']['MB']}/{r['lines']['Nails']}/{r['lines']['Hair']}={r['th']} | {r['last']} | wdB {a(r['wd_b'])} wdA {a(r['wd_a'])} | satA {a(r['sat_a'])} | cwdB {a(r['cwd_b'])} cwdA {a(r['cwd_a'])} | csatA {a(r['csat_a'])} | labmA {a(r['lab_a'])} | cmA {a(r['cm_a'])} | netB {a(r['net_b'])} netA {a(r['net_a'])} | d {a(r['net_a']-r['net_b'])}")
    print("## B CALL-IN")
    for h in (3.0, 6.0):
        print(h, "wd", round(h*PH_WD*ON,2), "sat", round(h*PH_SAT*ON,2))
    for k in (0,2,4,8,13,26.33):
        print("calls/month", k, "3h weekday-mix cost", round(k*3*PH_WD*ON,2), "6h", round(k*6*PH_WD*ON,2))
    sd_wd = 3*PH_WD*ON*22; sd_sat = 3*PH_SAT*ON*4.33
    print("option D (second phleb 3h shift every <=9 morning) month", round(sd_wd+sd_sat,2), "per wd", round(3*PH_WD*ON,2))
    full_saving = rows[0]["lab_b"]-rows[0]["lab_a"]
    print("full saving 6h second phleb per month", round(full_saving,2))
    print("## C BREAK-EVEN")
    for ph in ("base2","scaled"):
        for pol in ("plan","spaced","stacked"):
            print(ph, pol, P.be_search(policy=pol, phmode=ph), P.be_search(policy=pol, phmode=ph, gst=True))
    for ph in ("base2","scaled"):
        tc = P.cost_n(8, ph)[0]
        print(ph, "tc", tc, "AMlab", P.am_labour_month(P.LINES_BY_N[8], 2 if ph=="base2" else 1), "cover", round(tc-P.PM_REV,2), "BE", n3(P.be(tc)), "gstBE", n3(P.be(tc,True)),
              "MoS", round(18-P.be(tc),3), round((18-P.be(tc))/18*100,1), "pct", round(P.be(tc)/18*100,1))
    tcs = P.cost_n(8,"scaled")[0]
    for k in (0,2,4,8,13,26.33):
        add = k*3*PH_WD*ON
        print("calls", k, "BE", n3((tcs+add-P.PM_REV)/P.REVC), "GST", n3(P.be(tcs+add, True)))
    add = sd_wd+sd_sat
    print("option D BE", n3((tcs+add-P.PM_REV)/P.REVC), "GST", n3(P.be(tcs+add,True)), "cost", round(tcs+add,2))
    print("## D SATURDAY")
    for n in (9, 10, 18):
        r = rows[n-1]
        print(n, "satlab", round(r["sat_a"],2), "contrib", round(r["csat_a"],2), "wd contrib", round(r["cwd_a"],2))
    print("Sat direct BE 1 phleb+4 ther", round(rows[8]["sat_a"]/250,3), " 2+4:", round(rows[8]["sat_b"]/250,3), " 2+8:", round(rows[17]["sat_a"]/250,3))
    print("## E YEAR1")
    for fill in (1.0, 0.85, 0.70, 0.60, 0.50):
        for ph in ("base2","scaled"):
            s = P.steady(fill=fill, phmode=ph)
            cm = P.cash_model([s["rev"]]*72,[s["costs"]]*72,[s["credits"]]*72, months=72)
            y1 = sum(r["net"] for r in cm["rows"][:12]); y1g = sum(r["net_after_gst"] for r in cm["rows"][:12])
            print(fill, ph, "clients", round(s["clients"],2), "staff", s["staff"], "ph", s["ph"], "net", round(s["net"],2), "gst", round(s["net_gst"],2), "Y1", round(y1,2), round(y1g,2), "low", cm["lowest"], cm["low_m"], "peak", cm["peak_funding"], "pay", cm["payback_repo"], cm["payback_gst"])
    s = P.steady()
    cm = P.cash_model([s["rev"]]*12,[s["costs"]]*12,[s["credits"]]*12)
    print("18/day:", round(sum(r["net"] for r in cm["rows"][:12]),2), round(sum(r["net_after_gst"] for r in cm["rows"][:12]),2), cm["peak_funding"], cm["payback_repo"], cm["payback_gst"], round(s["costs"]*12,2), round(s["rev"]*12,2))
