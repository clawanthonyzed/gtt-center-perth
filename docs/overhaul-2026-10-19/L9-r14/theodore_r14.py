"""Theodore R14 (2026-10-24). EXTENDS theodore_r13.py (imported, not copied): re-uses its repo basis, award wages, on-cost
conventions and MBS item table. Adds: (1) midwife P&L at real GTT volume, (2) lab per-sample cash journey,
(3) package uptake model, (4) WA payroll tax. AUD. Labels: V verified, E estimate, Q quote needed.
"""
import contextlib, importlib.util, io, json, math, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
R13 = os.path.join(HERE, "..", "L8-r13", "theodore_r13.py")
if not os.path.exists(R13):
    R13 = r"C:\tmp\gtt_r14\docs\overhaul-2026-10-19\L8-r13\theodore_r13.py"
spec = importlib.util.spec_from_file_location("theodore_r13", R13)
r13 = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(r13)          # note: rewrites r13 results json with identical content

WEEKS_M = r13.WEEKS_M                     # 52/12
BASE_NET = r13.BASE_NET_MONTH             # 35,186.40 repo
VISITS_M = r13.VISITS_M                   # 396
WAGES = r13.WAGES

# ---------------- verified MBS items (MBS Online item pages, read 2026-10-24) ----------------
ITEMS = {
 "82100": dict(fee=89.00, ben=75.65, mins=60, tele=None,    note="initial antenatal, >=60 min, ONCE PER PREGNANCY, no telehealth version"),
 "82105": dict(fee=38.75, ben=32.95, mins=10, tele="91211 video / 91218 phone (same fee 38.75, ben 32.95)", note="short antenatal >=10 min"),
 "82110": dict(fee=89.00, ben=75.65, mins=40, tele="91212 video (fee 89.00, ben 75.65) / 91219 phone", note="routine antenatal >=40 min. Fee equals 82100: read twice on MBS Online, anomaly stands as published"),
 "82130": dict(fee=63.90, ben=54.35, mins=20, tele="91214 video / 91221 phone", note="short postnatal >=20 min, within 6 weeks of birth"),
 "82135": dict(fee=130.80, ben=111.20, mins=40, tele="91215 video / 91222 phone", note="routine postnatal >=40 min, within 6 weeks of birth"),
}
# Antenatal-only mix (Anthony: consults happen days/weeks BEFORE test day). Postnatal tail shown separately as upside.
MIX = {  # share of consults. 82100 is capped by how many clients are new to midwife care (once per pregnancy)
 "adverse": {"82100": .10, "82105": .70, "82110": .20},
 "base":    {"82100": .25, "82105": .35, "82110": .40},
 "favourable": {"82100": .40, "82105": .15, "82110": .45}}
for m in MIX.values(): assert abs(sum(m.values()) - 1) < 1e-9

COST = {  # E unless stated. hourly rate from Fair Work Pay Guide MA000034 from 1 Jul 2026 (V) via r13.WAGES
 "adverse":    dict(rate="RN L3 pp1", oncost=1.25, util=0.65, admin=15, pi=4500, cpd=1200, sw_m=200, equip=8000, consum=5.0, tele=0.0),
 "base":       dict(rate="RN L2 pp4", oncost=1.20, util=0.75, admin=10, pi=2500, cpd=600,  sw_m=120, equip=4500, consum=3.0, tele=0.30),
 "favourable": dict(rate="RN L2 pp1", oncost=1.14, util=0.85, admin=6,  pi=1200, cpd=300,  sw_m=80,  equip=2500, consum=1.5, tele=0.50)}
AHPRA, FTE_H, GAP, ROOM_M2, RENT = 193, 38.0, 1.30, 12, r13.RENT_PER_M2_MONTH
PRICING = ["bulk_billed", "private_at_schedule", "mixed_50_50_bulk_and_gap30"]

def mix_stats(mx):
    fee = sum(ITEMS[i]["fee"] * s for i, s in mx.items()); ben = sum(ITEMS[i]["ben"] * s for i, s in mx.items())
    mins = sum(ITEMS[i]["mins"] * s for i, s in mx.items())
    return fee, ben, mins
def rev_per_consult(mx, pricing):
    fee, ben, _ = mix_stats(mx)
    return {"bulk_billed": ben, "private_at_schedule": fee, "mixed_50_50_bulk_and_gap30": .5 * ben + .5 * fee * GAP}[pricing]
def hourly(c, sat_share):
    o, s, _, _ = WAGES[c["rate"]]
    return (o * (1 - sat_share) + s * sat_share) * c["oncost"]

def mw(case, consults_month, pricing, sat_share, mixcase=None, mixover=None):
    c = COST[case]; mx = mixover or MIX[mixcase or case]
    fee, ben, mins = mix_stats(mx)
    rpc = rev_per_consult(mx, pricing)
    cw = consults_month / WEEKS_M
    paid_h_w = cw * (mins + c["admin"]) / 60 / c["util"]
    heads = max(1, math.ceil(paid_h_w / FTE_H - 1e-9))
    in_person = mx.get("82100", 0) + (1 - mx.get("82100", 0)) * (1 - c["tele"])
    rooms = max(1, math.ceil(heads * in_person - 1e-9))
    wage_m = paid_h_w * WEEKS_M * hourly(c, sat_share)
    fixed_m = heads * ((AHPRA + c["pi"] + c["cpd"]) / 12 + c["sw_m"] + c["equip"] / 60) + rooms * ROOM_M2 * RENT
    rev_m = consults_month * rpc
    cons_m = consults_month * c["consum"]
    net_m = rev_m - wage_m - cons_m - fixed_m
    return dict(consults_month=round(consults_month, 1), consults_week=round(cw, 1), avg_clinical_min=round(mins, 1),
                paid_hours_week=round(paid_h_w, 1), fte=round(paid_h_w / FTE_H, 2), midwives_needed=heads, rooms=rooms,
                rev_per_consult=round(rpc, 2), rev_week=round(rev_m / WEEKS_M, 2), rev_month=round(rev_m, 2),
                wage_month=round(wage_m, 2), consumables_month=round(cons_m, 2), fixed_month=round(fixed_m, 2),
                net_week=round(net_m / WEEKS_M, 2), net_month=round(net_m, 2), wage_per_hour=round(hourly(c, sat_share), 2),
                wages_month_for_payroll_tax=round(wage_m, 2))

SCEN = {  # label: (consults per month, saturday share of hours, note)
 "A_50pct_396basis": (0.5 * VISITS_M, 0.0, "198/month = 50% of repo 396 weekday visits (45.7/wk)"),
 "A_50pct_6day": (54 * WEEKS_M, 1 / 6, "9/day x 6 = 54/week = 234/month (six-day week, matches repo AM revenue base 473.94 clients)"),
 "B_80pct_396basis": (0.8 * VISITS_M, 0.0, "317/month = 80% of 396 (73.1/wk)"),
 "B_80pct_6day": (84 * WEEKS_M, 1 / 6, "14/day x 6 = 84/week = 364/month")}
ELIG = {"all_100": 1.0, "elig_70": 0.7, "elig_40": 0.4}   # share of the target consults that really occur (no GP request / eligible)

grid = {}
for sk, (n, sat, note) in SCEN.items():
    for pr in PRICING:
        for ek, e in ELIG.items():
            grid[f"{sk}|{pr}|{ek}"] = {cs: mw(cs, n * e, pr, sat) for cs in COST}

# mix effect: income per consult and per client journey
mix_effect = {}
for nm, mx in {"all_initial_82100": {"82100": 1.0}, "all_short_82105": {"82105": 1.0}, "all_routine_82110": {"82110": 1.0},
               "adverse_mix": MIX["adverse"], "base_mix": MIX["base"], "favourable_mix": MIX["favourable"]}.items():
    fee, ben, mins = mix_stats(mx)
    mix_effect[nm] = dict(bulk_per_consult=round(ben, 2), fee_per_consult=round(fee, 2), clinical_min=round(mins, 1),
                          bulk_per_clinical_hour=round(ben / mins * 60, 2))
# one client journey, bulk billed: 82100 once, then follow-ups
journeys = {"initial_only": ["82100"], "initial_plus_short": ["82100", "82105"], "initial_plus_routine": ["82100", "82110"],
            "initial_plus_routine_plus_short": ["82100", "82110", "82105"], "no_initial_short_only": ["82105"],
            "no_initial_routine": ["82110"]}
journey_tbl = {k: dict(bulk=round(sum(ITEMS[i]["ben"] for i in v), 2), private_fee=round(sum(ITEMS[i]["fee"] for i in v), 2),
                       clinical_min=sum(ITEMS[i]["mins"] for i in v)) for k, v in journeys.items()}
# postnatal tail upside per client who stays with the midwife (82130 or 82135 once), bulk
postnatal_upside = dict(short_82130=54.35, routine_82135=111.20)

# capacity: FTE needed for 54 / 84 consults a week at 30/45/60 minutes
capacity = {}
for cw in (54, 84):
    for m in (30, 45, 60):
        capacity[f"{cw}_a_week_{m}min"] = {
            "clinical_hours_week": round(cw * m / 60, 1), "fte_clinical_only": round(cw * m / 60 / FTE_H, 2),
            "fte_with_10min_admin_75pct_util": round(cw * (m + 10) / 60 / .75 / FTE_H, 2)}

# break-even consults per week, base case (396 basis, no Saturday), by pricing
def be_week(pricing, case="base"):
    for n in range(1, 300):
        if mw(case, n * WEEKS_M, pricing, 0.0)["net_month"] > 0: return n
be = {pr: {cs: be_week(pr, cs) for cs in COST} for pr in PRICING}

# =============== PART 2: lab cash journey ===============
FEE = dict(i66548=19.90, i73928=5.95, i73938=7.95)
BEN = dict(i66548=16.95, i73928=5.10, i73938=6.80)
OOP_CASES = {  # per client, GTT pays. drink: Livingstone Glucaid 75g, A$54.95 carton of 24 (V listing, tiers 54.41-60.45 inc GST) -> 2.27-2.52
 "low":  dict(drink=2.27, cups_water=0.30, tubes_3=0.00, needles_3=0.00, courier=0.00, sharps_waste=0.00, lab_fee=0.00, note="lab supplies tubes, needles, courier free (PathWest said tubes/bags free; needles not stated)"),
 "base": dict(drink=2.39, cups_water=0.60, tubes_3=0.99, needles_3=9.00, courier=1.50, sharps_waste=0.30, lab_fee=0.00, note="GTT pays market price for tubes, needles, courier (Part IIBA s23DZZIF(6) caution). Needles 3 x A$3.00 E"),
 "high": dict(drink=2.52, cups_water=1.00, tubes_3=0.99, needles_3=10.89, courier=3.33, sharps_waste=0.60, lab_fee=5.00, note="single-unit prices, A$60 courier run / 18 clients, plus a hypothetical A$5 per-sample lab fee (no published fee exists)")}
for v in OOP_CASES.values():
    v["total"] = round(sum(x for k, x in v.items() if k != "note"), 2)
claim_refused_private = round(FEE["i66548"] + FEE["i73938"], 2)   # 27.85 lab private fee if Medicare refuses
bulk_medicare_to_lab = round(BEN["i66548"] + BEN["i73938"], 2)    # 23.75 at 85% (repo basis)
bulk_if_100pct = round(FEE["i66548"] + FEE["i73938"], 2)          # 27.85 if benefit is 100% of fee (not confirmed for this route)
cash = {}
for k, v in OOP_CASES.items():
    cash[k] = dict(
      bulk_billed=dict(gtt_collects_test=0.0, medicare_pays_lab=bulk_medicare_to_lab, client_pays_lab=0.0, gtt_pays_out=v["total"], gtt_out_of_pocket=v["total"]),
      refused_gtt_absorbs=dict(medicare_pays_lab=0.0, lab_private_bill=claim_refused_private, gtt_pays_out=round(v["total"] + claim_refused_private, 2), gtt_out_of_pocket=round(v["total"] + claim_refused_private, 2)),
      refused_client_pays=dict(medicare_pays_lab=0.0, client_pays_lab=claim_refused_private, gtt_pays_out=v["total"], gtt_out_of_pocket=v["total"]))
    for ref_rate in (0.02, 0.05):
        cash[k][f"expected_per_client_if_{int(ref_rate*100)}pct_refused_and_gtt_absorbs"] = round(v["total"] + ref_rate * claim_refused_private, 2)
    cash[k]["month_396_bulk"] = round(v["total"] * VISITS_M, 2)
    cash[k]["month_473_6day_bulk"] = round(v["total"] * 473.94, 2)
    cash[k]["month_396_all_refused_gtt_absorbs"] = round((v["total"] + claim_refused_private) * VISITS_M, 2)

# =============== PART 3: package uptake ===============
PKG = 250.0; CLIENTS_M = 118485.00 / PKG        # 473.94 AM clients a month (repo AM revenue base, 6-day week)
THER_M, PHLEB_M = (71145.86 - 2 * 6682.23) / 8, 6682.23   # per therapist / phlebotomist per month, from repo ladder (CURRENT-STATE s10)
assert abs(PHLEB_M * 2 + THER_M * 8 - 71145.86) < 0.05
def tier(p):
    return 0 if p == 0 else 2 if p == 1 else 4 if p <= 9 else 6 if p == 10 else 8
def exp_ther(u):
    return sum(math.comb(18, k) * u**k * (1 - u)**(18 - k) * tier(k) for k in range(19))
def pkg_net(u, deterministic=False):
    t = tier(round(18 * u)) if deterministic else exp_ther(u)
    return BASE_NET - PKG * CLIENTS_M * (1 - u) + (8 - t) * THER_M
# check: repo ladder at 9 clients/day with 1 phleb: 11,516.81
chk9 = BASE_NET - 0.5 * 118485 + (71145.86 - 35572.95)
assert abs(chk9 - 11516.81) < 0.1, chk9
def be_u(f, extra=0.0):
    lo, hi = 0.0, 1.0
    for _ in range(80):
        mid = (lo + hi) / 2
        if f(mid) + extra > 0: hi = mid
        else: lo = mid
    return round(hi, 4)
uptake = {}
for u in (1.0, 0.8, 0.6, 0.4, 0.2, 0.0):
    uptake[str(u)] = dict(package_clients_a_day=round(18 * u, 1), expected_therapists=round(exp_ther(u), 2),
                          net_month_expected=round(pkg_net(u), 2), net_month_deterministic=round(pkg_net(u, True), 2),
                          package_revenue_month=round(PKG * CLIENTS_M * u, 2))
# midwife base net at 50% and 80% six-day, bulk and mixed
def mwnet(sc, pr, case="base"): return grid[f"{sc}|{pr}|all_100"][case]["net_month"]
combo = {}
for u in (1.0, 0.8, 0.6, 0.4):
    row = dict(package_only=round(pkg_net(u), 2))
    for sc in ("A_50pct_6day", "B_80pct_6day"):
        for pr in ("bulk_billed", "mixed_50_50_bulk_and_gap30"):
            row[f"plus_midwife_{sc}_{pr}_base"] = round(pkg_net(u) + mwnet(sc, pr), 2)
    combo[str(u)] = row
be_pkg = dict(repo_volume_breakeven_clients_day=7.25, repo_volume_breakeven_share_of_18=round(7.25 / 18, 4),
              uptake_breakeven_package_only=be_u(pkg_net),
              uptake_breakeven_with_midwife_A_bulk_base=be_u(pkg_net, mwnet("A_50pct_6day", "bulk_billed")),
              uptake_breakeven_with_midwife_B_mixed_base=be_u(pkg_net, mwnet("B_80pct_6day", "mixed_50_50_bulk_and_gap30")))
# no package at all: lab keeps the Medicare (GTT earns none); revenue only from midwife (+ PM, already in repo base)
nopkg_base = pkg_net(0.0)
no_pkg = dict(package_structure_net=round(nopkg_base, 2),
              plus_midwife={f"{sc}|{pr}": round(nopkg_base + mwnet(sc, pr), 2) for sc in ("A_50pct_6day", "B_80pct_6day") for pr in ("bulk_billed", "mixed_50_50_bulk_and_gap30")},
              note="Holds all repo fixed costs, PM, manager and 2 phlebotomists; only therapist cost is removed. Medicare test money goes to the lab (GTT earns nil). Cutting rent/manager would help but is not in the repo.")

# =============== PART 4: WA payroll tax ===============
TH, UP, RATE = 1_000_000, 7_500_000, 0.055
def ptax(W):
    if W <= TH: return 0.0
    ded = max(0.0, TH - (W - TH) * 2 / 13) if W < UP else 0.0
    return round(max(0.0, W - ded) * RATE, 2)
REPO_WAGES_M = 82318.05            # "Total Direct Labor + Opening Costs", CURRENT-STATE s5 (with on-costs incl. super) ; excludes workers comp
repo_W = REPO_WAGES_M * 12
mw_wages = {}
for sc in ("A_50pct_6day", "B_80pct_6day"):
    r = grid[f"{sc}|bulk_billed|all_100"]["base"]
    W = repo_W + r["wage_month"] * 12
    mw_wages[sc] = dict(midwife_wages_month=r["wage_month"], total_wages_year=round(W), tax_year=ptax(W), tax_month=round(ptax(W) / 12, 2),
                        net_midwife_after_payroll_tax_month=round(r["net_month"] - ptax(W) / 12 + ptax(repo_W) / 12, 2))
payroll = dict(threshold=TH, rate=RATE, upper=UP, taper="deduction = 1,000,000 - (wages - 1,000,000) x 2/13, nil from 7,500,000", monthly_threshold=83333,
               repo_wages_month=REPO_WAGES_M, repo_wages_year=round(repo_W), headroom_year=round(TH - repo_W), headroom_month=round((TH - repo_W) / 12, 2),
               tax_on_repo_wages=ptax(repo_W), midwife_wages_month_that_trips_threshold=round((TH - repo_W) / 12, 2),
               marginal_rate_above_threshold=round(RATE * (1 + 2 / 13), 5), cases=mw_wages,
               if_repo_wages_20pct_higher=dict(year=round(repo_W * 1.2), tax_year=ptax(repo_W * 1.2)),
               wages_that_pay_nothing_if_midwife_is_contractor="Not advised: WA deems many contractors to be employees for payroll tax (relevant contracts). Catherine/accountant.")

out = dict(generated="2026-10-24", basis=dict(repo_net_month=BASE_NET, visits_396=VISITS_M, six_day_am_clients_month=round(CLIENTS_M, 2), weeks_month=round(WEEKS_M, 4)),
           items=ITEMS, mix=MIX, cost_cases=COST, scenarios={k: dict(consults_month=round(v[0], 1), consults_week=round(v[0] / WEEKS_M, 1), note=v[2]) for k, v in SCEN.items()},
           grid=grid, mix_effect=mix_effect, journeys=journey_tbl, postnatal_upside=postnatal_upside, capacity=capacity, breakeven_consults_week=be,
           lab=dict(fees=FEE, benefits=BEN, oop_cases=OOP_CASES, cash=cash, refused_private_bill=claim_refused_private,
                    bulk_to_lab_85pct=bulk_medicare_to_lab, bulk_if_100pct_of_fee=bulk_if_100pct),
           package=dict(uptake=uptake, combined_with_midwife=combo, breakeven=be_pkg, no_package=no_pkg, therapist_month=round(THER_M, 2), phleb_month=PHLEB_M),
           payroll_tax=payroll)
json.dump(out, open(os.path.join(HERE, "theodore_r14_results.json"), "w"), indent=1)

if __name__ == "__main__":
    for sc in SCEN:
        for pr in PRICING:
            g = grid[f"{sc}|{pr}|all_100"]
            print(sc, pr, {cs: (g[cs]["net_week"], g[cs]["net_month"], g[cs]["fte"], g[cs]["midwives_needed"], g[cs]["rev_per_consult"]) for cs in g})
    for ek in ELIG:
        g = grid[f"A_50pct_6day|bulk_billed|{ek}"]; print("ELIG", ek, {cs: g[cs]["net_month"] for cs in g})
    print(be); print(mix_effect); print(journey_tbl); print(capacity)
    print({k: v["total"] for k, v in OOP_CASES.items()}, claim_refused_private)
    print(uptake); print(be_pkg); print(no_pkg); print(combo); print(payroll)
