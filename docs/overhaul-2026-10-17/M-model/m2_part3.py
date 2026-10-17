"""M2 part 3: writes the markdown tables (as files in ./tables) so documents carry exactly the solver-driven numbers."""
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import m2_driver as M
import m2_part2 as Q
D, P, a, n3 = M.D, M.P, M.a, M.n3
OUT = HERE / "tables"; OUT.mkdir(exist_ok=True)
rows = M.table()
lo, hi = Q.extremes()
def w(name, lines): (OUT / name).write_text("\n".join(lines) + "\n", encoding="utf-8")

# T1: roster table for the 3-way model (adaptive)
t = ["| Confirmed bookings that morning | Phlebotomists | Therapists (Massage and Beauty / Nails / Hair) | Last first draw | Weekday labour | Saturday labour | Labour per client (weekday) | Therapists if bookings are spaced (best) | Therapists if bookings stack in pairs (worst) |",
     "|---|---|---|---|---|---|---|---|---|", "| 0 | 0 | 0 | n/a | A$0.00 | A$0.00 | n/a | 0 | 0 |"]
for r in rows:
    n = r["n"]
    bt = sum(lo[n][1].values()); wt = sum(hi[n][1].values())
    t.append(f"| {n} | {r['pa']} | {r['lines']['MB']} / {r['lines']['Nails']} / {r['lines']['Hair']} = {r['th']} | {r['last']} | {a(r['wd_a'])} | {a(r['sat_a'])} | {a(r['wd_a']/n)} | {bt} | {wt} |")
w("T1_roster_3way.md", t)

# T2: before / after
t = ["| Booked | Phlebotomists before / after | Weekday labour before | Weekday labour after | Contribution per weekday morning (after) | Contribution per Saturday (after) | AM labour per month (after) | Net operating profit per month before | Net operating profit per month after | Change per month |",
     "|---|---|---|---|---|---|---|---|---|---|"]
for r in rows:
    t.append(f"| {r['n']} | {r['pb']} / {r['pa']} | {a(r['wd_b'])} | {a(r['wd_a'])} | {a(r['cwd_a'])} | {a(r['csat_a'])} | {a(r['lab_a'])} | {a(r['net_b'])} | {a(r['net_a'])} | {a(r['net_a']-r['net_b'])} |")
w("T2_before_after.md", t)

# T4 break-even working before / after
tcb, tca = P.cost_n(8, "base2")[0], P.cost_n(8, "scaled")[0]
amb, ama = P.am_labour_month(P.LINES_BY_N[8], 2), P.am_labour_month(P.LINES_BY_N[8], 1)
fx = P.FIXED
t = ["| Step | Working | Before (2 phlebotomists + 4 therapists) | After (1 phlebotomist + 4 therapists) |", "|---|---|---|---|",
     f"| 1. Fixed costs | rent 8,000 + other overhead 5,088.34 + cost of goods 1,200 + (afternoon labour 12,704.74 + Venue Manager 7,040) x 1.137 | {a(fx)} | {a(fx)} |",
     f"| 2. Morning roster | wages x 1.137, 22 weekdays + 4.33 Saturdays | + {a(amb)} | + {a(ama)} |",
     f"| 3. Total costs | step 1 + step 2 | {a(tcb)} | {a(tca)} |",
     f"| 4. Less afternoon revenue | 8.6957 x A$117 x 22 + 4.3478 x A$117 x 4.33 | - {a(P.PM_REV)} | - {a(P.PM_REV)} |",
     f"| 5. Costs the mornings must cover | step 3 - step 4 | {a(tcb-P.PM_REV)} | {a(tca-P.PM_REV)} |",
     f"| 6. Revenue per daily client per month | A$250 x 26.33 trading days | {a(P.REVC)} | {a(P.REVC)} |",
     f"| 7. **Break-even** | step 5 / step 6 | **{n3(P.be(tcb))}** | **{n3(P.be(tca))}** |",
     f"| 8. Share of 18-a-day capacity | break-even / 18 | {P.be(tcb)/18*100:.1f}% | {P.be(tca)/18*100:.1f}% |",
     f"| 9. Margin of safety at 18 | 18 - break-even | {18-P.be(tcb):.3f} clients ({(18-P.be(tcb))/18*100:.1f}%) | {18-P.be(tca):.3f} clients ({(18-P.be(tca))/18*100:.1f}%) |",
     f"| 10. GST-stress break-even | whole package and afternoon taxable at 10% | {n3(P.be(tcb,True))} | {n3(P.be(tca,True))} |"]
w("T4_breakeven.md", t)

# T5 by booking pattern
plan = {n: P.cost_n(n, "scaled")[0] for n in range(1, 19)}
stack = {n: P.total_costs(D.solve(D.stacked_counts(n))[0], D.solve(D.stacked_counts(n))[1])[0] for n in range(1, 19)}
cheap = {n: lo[n][0] for n in range(1, 19)}
oldplan = {n: P.cost_n(n, "base2")[0] for n in range(1, 19)}
oldstack = {n: P.cost_policy(n, "stacked") for n in range(1, 19)}
def bp(cb, g=False):
    r = Q.be_pattern(cb, g); return n3(r[0])
t = ["| Booking pattern | Before: break-even | Before: GST-stress | After: break-even | After: GST-stress |", "|---|---|---|---|---|",
     f"| Planning case: one client per slot from 07:00 first | {bp(oldplan)} | {bp(oldplan,True)} | **{bp(plan)}** | {bp(plan,True)} |",
     f"| Cheapest pattern of all 19,683 ways of placing the bookings | 8.266 | 9.255 | {bp(cheap)} | {bp(cheap,True)} |",
     f"| Bookings stack in pairs from 07:00 (both chairs from the second booking) | {bp(oldstack)} | {bp(oldstack,True)} | {bp(stack)} | {bp(stack,True)} |"]
w("T5_patterns.md", t)

# T3 options on mornings of 9 or fewer
ON = M.ON
cwd = 3 * M.PH_WD * ON; csat = 3 * M.PH_SAT * ON
c6wd = 6 * M.PH_WD * ON; c6sat = 6 * M.PH_SAT * ON
optD = round(cwd * 22 + csat * 4.33, 2)
satfloor = round(c6sat * 4.33, 2)
net9a = rows[8]["net_a"]; net9b = rows[8]["net_b"]
def be_add(extra): return n3((tca + extra - P.PM_REV) / P.REVC)
t = ["| Option for mornings of 9 or fewer | Phlebotomist cost | Extra cost a month | Net operating profit a month at 9 booked | Break-even | Basis |", "|---|---|---|---|---|---|",
     f"| 0. Previous rule: 2 phlebotomists, full 6-hour shift | 2 x 6 hours | A$0.00 (reference) | {a(net9b)} | {n3(P.be(tcb))} | Previous model |",
     f"| 1. **Adaptive: 1 phlebotomist; the second collector is called in only if needed** | 1 x 6 hours + call-in when needed | A$0.00 with no call-ins | {a(net9a)} | **{be_add(0)}** | Repo solver draw check. Call-in cost is separate, next table |",
     f"| 2. Adaptive plus a short second shift (3 hours, 07:00 to 10:00) on every such morning | 1 x 6 + 1 x 3 hours | {a(optD)} | {a(net9a-optD)} | {be_add(optD)} | Three-hour casual minimum engagement (repo, verified) |",
     f"| 3. Adaptive plus a second collector on every such Saturday only | 1 x 6 + 1 x 6 hours on Saturdays | {a(satfloor)} | {a(net9a-satfloor)} | {be_add(satfloor)} | Repo Saturday rate (A$51.5625 an hour); proposal, see the safety note |",
     "| 4. Paid standby allowance for the on-call collector | not in the repo | not modelled | not modelled | not modelled | **No allowance rate exists in the repo and none is invented. The award and the lab would set it. TO CONFIRM** |"]
w("T3_options.md", t)

# T3b call-in cost
t = ["| Call-ins a month (second collector attends) | Cost at the 3-hour minimum | Cost if she works the full 6-hour shift | Break-even added (3-hour call-ins) | Break-even with the call-ins |", "|---|---|---|---|---|"]
for k in (0, 2, 4, 8, 13, 26):
    t.append(f"| {k} | {a(k*cwd)} | {a(k*c6wd)} | +{k*cwd/P.REVC:.3f} | {n3((tca+k*cwd-P.PM_REV)/P.REVC)} |")
t.append(f"| One call-in | {a(cwd)} weekday / {a(csat)} Saturday | {a(c6wd)} weekday / {a(c6sat)} Saturday | | |")
w("T3b_callins.md", t)
print("per call-in", round(cwd,2), round(csat,2), round(c6wd,2), round(c6sat,2), "optD", optD, "satfloor", satfloor)

# Saturday proof
sat = ["Saturday direct-labour break-even (clients to cover that Saturday's staff):",
       f"1 phlebotomist + 4 therapists: {rows[8]['sat_a']/250:.2f} clients; 2 + 4 (before): {rows[8]['sat_b']/250:.2f}; 2 + 8: {rows[17]['sat_a']/250:.2f}",
       f"At 9 booked after: labour {a(rows[8]['sat_a'])}, contribution {a(rows[8]['csat_a'])}"]
w("T6_saturday.md", sat)

# fill table before / after
t = ["| Average morning | Roster before | Roster after | Monthly net before (repo / GST-stress) | Monthly net after (repo / GST-stress) | Year 1 net before (repo / GST) | Year 1 net after (repo / GST) | Payback before (repo / GST) | Payback after (repo / GST) |", "|---|---|---|---|---|---|---|---|---|"]
for fill, label in ((1.0, "18 (100%)"), (0.85, "15.3 (85%)"), (0.70, "12.6 (70%)"), (0.50, "9 (50%)")):
    out = {}
    for ph in ("base2", "scaled"):
        s = P.steady(fill=fill, phmode=ph)
        cm = P.cash_model([s["rev"]]*72, [s["costs"]]*72, [s["credits"]]*72, months=72)
        y1 = sum(r["net"] for r in cm["rows"][:12]); y1g = sum(r["net_after_gst"] for r in cm["rows"][:12])
        out[ph] = (s, y1, y1g, cm)
    sb, sa = out["base2"][0], out["scaled"][0]
    pb = lambda cm: f"Month {cm['payback_repo']}" if cm["payback_repo"] else "none"
    pg = lambda cm: f"Month {cm['payback_gst']}" if cm["payback_gst"] else "none"
    t.append(f"| {label} | {sb['ph']} + {sum(sb['lines'].values())} | {sa['ph']} + {sum(sa['lines'].values())} | {a(sb['net'])} / {a(sb['net_gst'])} | {a(sa['net'])} / {a(sa['net_gst'])} | {a(out['base2'][1],0)} / {a(out['base2'][2],0)} | {a(out['scaled'][1],0)} / {a(out['scaled'][2],0)} | {pb(out['base2'][3])} / {pg(out['base2'][3])} | {pb(out['scaled'][3])} / {pg(out['scaled'][3])} |")
w("T7_fill.md", t)

# R2 tables
N = 18 * D.DAYS
lab_txn = D.PM_LAB * D.ONCOST / (8.6957 * 22 + 4.3478 * 4.33)
base_net = 35186.40
t = ["| Take-up (share of testing clients who redeem) | Redemptions a month | Cost a month: one treatment at A$117 | Cost: PM Restore at A$135 | Cost: PM Refresh at A$185 | Cost at A$117 as share of monthly net profit | Break-even added (A$117) | Break-even after adaptive roster (A$117) |", "|---|---|---|---|---|---|---|---|"]
for tk in (0.05, 0.10, 0.15, 0.25, 0.40):
    R = N * tk
    c117, c135, c185 = R*117*0.1, R*135*0.1, R*185*0.1
    t.append(f"| {int(tk*100)}% | {R:.1f} | {a(c117)} | {a(c135)} | {a(c185)} | {c117/base_net*100:.1f}% | +{c117/D.REV_PER_CLIENT_MONTH:.3f} | {n3((tca+c117-P.PM_REV)/P.REVC)} |")
w("T8_discount_cost.md", t)

t = ["| Price basis | If the extra hours are already paid (idle capacity) | If the extra hours must be paid (loaded afternoon labour A$%.2f a booking) |" % lab_txn, "|---|---|---|"]
for nm, s in (("Treatment A$117", 117.0), ("PM Restore A$135", 135.0), ("PM Refresh A$185", 185.0)):
    t.append(f"| {nm} | {0.1*s/s*100:.1f}% of redeemers must be new bookings | {0.1*s/(s-lab_txn)*100:.1f}% of redeemers must be new bookings |")
w("T9_breakeven_uplift.md", t)

t = ["| Take-up | New bookings among redeemers | Net effect a month (extra hours already paid) | Net effect a month (extra hours must be paid) | Monthly net profit after (extra hours already paid) |", "|---|---|---|---|---|"]
for tk in (0.05, 0.10, 0.25):
    R = N * tk
    for q in (0.0, 0.10, 0.25, 0.50):
        e0 = R*q*(0.9*117) - R*(1-q)*0.1*117
        e1 = R*q*(0.9*117 - lab_txn) - R*(1-q)*0.1*117
        t.append(f"| {int(tk*100)}% | {int(q*100)}% | {a(e0)} | {a(e1)} | {a(base_net+e0)} |")
w("T10_net_effect.md", t)
print("N", round(N,2), "lab_txn", round(lab_txn,2))
