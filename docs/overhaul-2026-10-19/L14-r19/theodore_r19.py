"""Theodore R19 (2026-10-26). EXTENDS theodore_r18.py (imported; it imports r17 -> r16 -> r15 -> r14 -> r13). No second calculator.
Every money line comes from r18.venture() (which runs the repo's own tools/master_financial_model.py live). R19 only:
  (1) re-points two r18 module inputs through a context manager (consult price, midwife paid hours) instead of re-deriving maths;
  (2) adds the card fee the repo never counted on AFTERNOON sales and on the NO-MIDWIFE baseline (R18 counted it only on today's
      morning takings, so the R18 comparison was uneven). Fee formula reused: r15.fee_pct (1.7% + A$0.30, E);
  (3) checks the staffing inputs against the repo (cost_ramp_model.py constants, cost_ramp.yml payroll breakdown,
      demand_driven_staffing_solver.py run at N=18 with 45-minute services);
  (4) solves the price needed for three profit targets (bisection on r18.venture output, no new formula);
  (5) WRITES docs/FINANCIAL-CENTER-OF-TRUTH.md and L14-r19/center_of_truth.yml, so the centre can never drift from this script;
  (6) a banned-stale-values fact check:  python theodore_r19.py --check <file.md>
LOCKED (Anthony): Structure B; P1 A$300 (2 x 30 min) / P2 A$350 (2 up to 45 min), GST inside; plan 100% P1; consult 20 min item 82105
(rebate A$32.95; total rebate A$55.00), consult 1 to 28 days BEFORE the test; lab A$27.85 paid by the mother to the lab; consult A$110
GST-free (Medical); lounge + service A$162.15 / A$212.15 taxable (Lounge); 18 AM clients a day Mon-Sat; 8 AM service staff, 4 PM service
staff, venue manager from 06:30, no hosts; 2 permanent part-time midwives 22.5 h each + 1 casual for leave, one consult room;
payroll tax accepted; one consolidated venture; Route B. Labels: R repo, V official, E estimate, Q quote. AUD.
"""
import contextlib, importlib.util, io, json, os, re, sys
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
spec = importlib.util.spec_from_file_location("theodore_r18", os.path.join(HERE, "..", "L13-r18", "theodore_r18.py"))
r18 = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(r18)          # r18..r13 rewrite their own results json on import; content unchanged (git status checked)
r17, r15, r14 = r18.r17, r18.r15, r18.r14
f2 = r15.f2
sys.path.insert(0, os.path.join(REPO, "tools"))
import cost_ramp_model as crm
import demand_driven_staffing_solver as dds

N = r18.N                                    # 473.94 AM clients a month (R)
LAB, REBATE_CONSULT, REBATE_TEST, REBATE_COLL = 27.85, 32.95, 16.95, 5.10
REBATE = f2(REBATE_CONSULT + REBATE_TEST + REBATE_COLL)               # 55.00 (V, MBS Online via R18)
TARGET_REPO = r14.BASE_NET                                             # 35,186.40 (R)
TAX = 0.25
out = {"generated": "2026-10-26", "imports": "theodore_r18.py -> r17 -> r16 -> r15 -> r14 -> r13; tools/master_financial_model.py (live via r18); "
       "tools/cost_ramp_model.py; tools/demand_driven_staffing_solver.py"}

# ---------------- pre-generation fact check: inputs against the repo ----------------
pb = r18.BASE["payroll_breakdown"]
mb, nails, hair = crm.AM_HEADCOUNT_HIGH
am_staff = mb + nails + hair
am_treat_check = f2(22 * 6 * (mb * 37.50 + (nails + hair) * 36.81))
pm_check = f2(22 * crm.PM_ROLES * crm.CASUAL_MINIMUM_ENGAGEMENT_HOURS * crm.PM_WEEKDAY_BLENDED_CASUAL_RATE)
vm_check = f2(22 * crm.OPENING_TIME_INCREMENT_DAILY)
ra = {r["id"]: r for r in yaml.safe_load(open(os.path.join(REPO, "data", "canonical", "revenue_assumptions.yml"), encoding="utf-8"))["records"]}
pr = {r["id"]: r for r in yaml.safe_load(open(os.path.join(REPO, "data", "canonical", "pricing.yml"), encoding="utf-8"))["records"]}
PM_PRICE = float(pr["pm_alacarte_average"]["price"])                   # A$117 incl GST (R)
PM_TX = ra["rev_pm_weekday_transactions"]["value"] * 22 + ra["rev_pm_saturday_transactions"]["value"] * 4.33
with contextlib.redirect_stdout(io.StringIO()):
    peak18 = dds.assign_and_check(18)                                    # repo solver, 45-minute services, 25-minute cadence
inputs = dict(
    am_service_staff=am_staff, am_service_staff_expected=8,
    am_treatment_wages_repo=pb["am_weekday_treatment_staff"], am_treatment_wages_rebuilt=am_treat_check,
    phlebotomists_full_roster=2, phlebotomist_wages_repo=pb["am_weekday_phlebotomist"], phlebotomist_wages_rebuilt=f2(22 * 2 * 6 * 34.375),
    pm_service_staff=crm.PM_ROLES, pm_service_staff_expected=4, pm_weekday_wages_repo=pb["pm_weekday_direct_labor"], pm_weekday_wages_rebuilt=pm_check,
    venue_manager_repo_0700_wages=pb["opening_time_increment"], venue_manager_rebuilt=vm_check, venue_manager_0630_extra_loaded=r18.VM_EXTRA_LOADED,
    am_clients_month=N, am_clients_day=round(N / (22 + 4.33), 2),
    pm_transactions_month=round(PM_TX, 2), pm_transactions_weekday_day=ra["rev_pm_weekday_transactions"]["value"],
    pm_transactions_saturday_day=ra["rev_pm_saturday_transactions"]["value"], pm_price_incl_gst=PM_PRICE,
    pm_revenue_repo=r18.REV["pm_revenue"], pm_revenue_rebuilt=f2(PM_TX * PM_PRICE),
    solver_service_minutes=dds.SERVICE_MINUTES, solver_staff_at_18=peak18["total_headcount"], midwife_hours_week_r18=r18.MW_HOURS_W)
assert am_staff == 8 and crm.PM_ROLES == 4
assert abs(am_treat_check - pb["am_weekday_treatment_staff"]) < 0.05
assert abs(pm_check - pb["pm_weekday_direct_labor"]) < 0.05
assert abs(vm_check - pb["opening_time_increment"]) < 0.05
assert abs(PM_TX * PM_PRICE - r18.REV["pm_revenue"]) < 5.0             # 210.13 x A$117 = A$24,585 (rounded day counts)
assert abs(round(N / 26.33, 2) - 18.0) < 0.01
assert r18.MW_HOURS_W == 45.0 and peak18["total_headcount"] == 8 and dds.SERVICE_MINUTES == 45   # P2's 45-minute services fit the costed 8
out["T1_inputs_check"] = inputs

# ---------------- the R19 venture: r18.venture + the missing card fees ----------------
@contextlib.contextmanager
def patched(consult=110.0, mw_hours=45.0):
    old = (r17.CONSULT, r18.CONSULT, r18.MW_HOURS_W)
    r17.CONSULT = r18.CONSULT = consult; r18.MW_HOURS_W = mw_hours
    try:
        yield
    finally:
        r17.CONSULT, r18.CONSULT, r18.MW_HOURS_W = old

PM_CARD = f2(PM_TX * r15.fee_pct(PM_PRICE))                            # card fee on afternoon sales (R18 missed it)
BASE_AM_CARD = f2(N * r15.fee_pct(250.0))                              # card fee on the old A$250 (R18 baseline missed it)

def v19(p1=300.0, p2=350.0, share_p1=1.0, consult=110.0, mw_hours=45.0, basis="leave_covered_1.366", mid=True, vm=True):
    with patched(consult, mw_hours):
        v = r18.venture(p1, p2, share_p1, basis, vm, mid)
    v = dict(v)
    v["card_fees_pm"] = -PM_CARD
    if not mid:
        v["card_fees"] = -BASE_AM_CARD
    v["card_fees_total"] = f2(v["card_fees"] + v["card_fees_pm"])
    before = f2(v["profit_before_company_tax"] - PM_CARD - (BASE_AM_CARD if not mid else 0.0))
    v["total_costs"] = f2(v["total_costs"] - PM_CARD - (BASE_AM_CARD if not mid else 0.0))
    v["profit_before_company_tax"] = before
    v["company_tax_25"] = -f2(max(0, before) * TAX)
    v["profit_after_company_tax"] = v["franked_dividend_available"] = f2(before - max(0, before) * TAX)
    v["franking_credits_attached"] = f2(max(0, before) * TAX)
    v["consult_price"], v["p1"], v["p2"], v["share_p1"], v["midwife_hours_week"], v["oncost_basis"] = consult, p1, p2, share_p1, mw_hours, basis
    return v

LOCK = v19()
GRACE = v19(basis="grace_1.20")
BASE0 = v19(mid=False, vm=False)
assert abs(LOCK["profit_before_company_tax"] - (r18.Q1["locked_leave_covered"]["profit_before_company_tax"] - PM_CARD)) < 0.02
out["locked"], out["locked_grace_1_20"], out["baseline_no_midwife"] = LOCK, GRACE, BASE0

# ---------------- T1: bridge from the repo A$35,186.40 to today, line by line ----------------
pt_repo = r14.ptax(r15.REPO_TAXABLE_Y) / 12
lounge_cut = BASE0["rev_lounge_service_am_ex_gst"] - LOCK["rev_lounge_service_am_ex_gst"]   # = 474 x (A$250 - A$162.15) / 1.1, per-client rounding as the model
mw_fix = -LOCK["midwife_fixed_consumables"]
bridge = [
 ("A. Repo net today (CURRENT-STATE line 30): no GST, no card fees, no payroll tax, no company structure cost, before company tax", TARGET_REPO),
 ("GST the repo never took out (it counts the GST-inclusive A$250 and A$117 as revenue), net of GST credits on costs", r17.AFTER_GST - TARGET_REPO),
 ("Card fees on the old A$250 morning price (repo opex flags this as missing: VERIFICATION-TRACKER 23)", -BASE_AM_CARD),
 ("Card fees on afternoon sales (same repo gap)", -PM_CARD),
 ("Payroll tax on the repo's own wages (never in the repo net)", -pt_repo),
 ("Three-company running cost (Holdings + Medical + Lounge)", -r15.run3["base"]["total_month"]),
 ("B. Like-for-like starting point, no midwife, old A$250 package", BASE0["profit_before_company_tax"]),
 ("Consult revenue now labelled separately: 474 x A$110 (GST-free, Medical)", LOCK["rev_consult_gst_free"]),
 ("Lounge + service line: was the whole A$250, now A$162.15 (474 x A$87.85 / 1.1)", -lounge_cut),
 ("Extra card fee: GTT now takes A$272.15 a client instead of A$250", LOCK["card_fees"] + BASE_AM_CARD),
 ("Midwife wages: 45 h a week, permanent with leave covered by the casual (on-cost 1.366)", LOCK["midwife_wages"]),
 ("Midwife fixed costs and consumables (registration, indemnity, training, software, equipment, one consult room)", LOCK["midwife_fixed_consumables"]),
 ("Venue manager 06:30 start (extra 0.5 h on 22 weekdays)", LOCK["venue_manager_0630"]),
 ("Extra payroll tax on midwife and venue manager wages", LOCK["payroll_tax_group"] + pt_repo),
 ("C. Today, before company tax (locked case)", LOCK["profit_before_company_tax"]),
 ("Company tax 25% (the repo A$35,186.40 was always BEFORE company tax)", LOCK["company_tax_25"]),
 ("D. Today, after company tax = franked dividend available", LOCK["profit_after_company_tax"])]
bridge = [(k, f2(v)) for k, v in bridge]
s = lambda a, b: sum(x[1] for x in bridge[a:b])
assert abs(s(0, 6) - bridge[6][1]) < 0.05 and abs(bridge[6][1] + s(7, 14) - bridge[14][1]) < 0.05
assert abs(bridge[14][1] + bridge[15][1] - bridge[16][1]) < 0.05
out["T1_bridge"] = bridge
restate = f2(bridge[6][1] - TARGET_REPO)                                # -15,852: never-real part
decisions = f2(bridge[14][1] - bridge[6][1])                            # -2,020: package + midwife + VM
out["T1_split"] = dict(restatement_never_in_repo=restate, decisions_package_midwife_vm=decisions, company_tax=LOCK["company_tax_25"],
                       old_repo_if_taxed_25=f2(TARGET_REPO * 0.75), r18_headline_after_tax=r18.Q1["locked_leave_covered"]["profit_after_company_tax"],
                       revenue_change=f2(LOCK["revenue_total_ex_gst"] - BASE0["revenue_total_ex_gst"]),
                       cost_change=f2(LOCK["total_costs"] - BASE0["total_costs"]))

# per-client waterfall (Package 1, A$300), whole venture costs spread over the 474 morning clients
R = r17.reach(300.0)
pc = lambda x: f2(x / N)
wf = [("Mother pays at booking (Package 1)", 300.00),
      ("To the lab, paid by the mother to the lab (never GTT money)", -LAB),
      ("Reaches GTT (consult A$110 + lounge + service A$162.15)", R["gtt_receives_incl_gst"]),
      ("GST inside the lounge + service part, passed to the ATO", -R["lounge_gst_inside"]),
      ("Card fee on GTT's A$272.15", -R["card_fee"]),
      ("GTT keeps from the morning package", R["gtt_ex_gst_after_card"]),
      ("Plus afternoon sales per morning client (ex GST, after card fee)", pc(LOCK["rev_pm_ex_gst"] - PM_CARD)),
      ("Less repo staff (8 AM service, 2 phlebotomists, 4 PM, venue manager 07:00)", pc(LOCK["repo_payroll"])),
      ("Less repo running costs (rent, insurance, overheads, supplies), after GST credits", pc(LOCK["repo_operating_expenses"] + LOCK["less_gst_credits"])),
      ("Less midwife wages", pc(LOCK["midwife_wages"])),
      ("Less midwife fixed costs and consumables", pc(LOCK["midwife_fixed_consumables"])),
      ("Less venue manager 06:30", pc(LOCK["venue_manager_0630"])),
      ("Less payroll tax (whole group)", pc(LOCK["payroll_tax_group"])),
      ("Less three-company running cost", pc(LOCK["three_company"])),
      ("Profit per client before company tax", pc(LOCK["profit_before_company_tax"])),
      ("Company tax 25%", pc(LOCK["company_tax_25"])),
      ("Profit per client after company tax (franked dividend)", pc(LOCK["profit_after_company_tax"]))]
out["T1_waterfall_per_client"] = wf
out["T1_mother"] = dict(pays=300.0, rebate=REBATE, out_of_pocket_p1=f2(300 - REBATE), out_of_pocket_p2=f2(350 - REBATE),
                        note="out of pocket INCLUDES the A$27.85 lab fee (rebate covers A$22.05 of it)")

# ---------------- T2: level the midwife ----------------
with patched():
    mw = r18.midwife("leave_covered_1.366")
no_mw_pt = v19(mid=False, vm=True)
mw_ptax = f2(-(LOCK["payroll_tax_group"] - no_mw_pt["payroll_tax_group"]))     # payroll tax caused by the midwives alone
consult_card = f2(N * 0.017 * 110)
mw_all = f2(mw["wage"] + mw["fixed"] + mw["consum"] + mw_ptax)
out["T2_midwife_vs_consult"] = dict(consult_revenue_month=LOCK["rev_consult_gst_free"], consult_card_fee_month=consult_card,
    midwife_wages=f2(mw["wage"]), midwife_fixed=f2(mw["fixed"]), midwife_consumables=f2(mw["consum"]), midwife_payroll_tax=mw_ptax,
    midwife_all_in_month=mw_all, midwife_surplus_month=f2(LOCK["rev_consult_gst_free"] - consult_card - mw_all),
    per_client=dict(consult=110.0, card=f2(consult_card / N), midwife_all_in=f2(mw_all / N), surplus=f2((LOCK["rev_consult_gst_free"] - consult_card - mw_all) / N)),
    consult_hours_needed_week=f2(N / 26.33 * 6 * 20 / 60), paid_hours_week=45.0)
P = LOCK["profit_before_company_tax"]
lv = lambda v: dict(before_tax=v["profit_before_company_tax"], after_tax=v["profit_after_company_tax"],
                    change_before=f2(v["profit_before_company_tax"] - P), change_after=f2(v["profit_after_company_tax"] - LOCK["profit_after_company_tax"]))
levers = {
 "a_consult_plus_10": lv(v19(310, 360, consult=120)), "a_consult_plus_20": lv(v19(320, 370, consult=130)),
 "b_lounge_plus_10": lv(v19(310, 360)), "b_lounge_plus_20": lv(v19(320, 370)),
 "d_p2_share_10pct": lv(v19(share_p1=0.9)), "d_p2_share_30pct": lv(v19(share_p1=0.7)), "d_p2_share_50pct": lv(v19(share_p1=0.5)),
 "e_hours_42": lv(v19(mw_hours=42)), "e_hours_39": lv(v19(mw_hours=39)), "e_hours_36": lv(v19(mw_hours=36)),
 "grace_1_20_basis": lv(GRACE)}
# (c) priced optional extra: the repo's own 30 -> 45 minute massage upgrade price gap (A$120 - A$75 = A$45, pricing.yml), per 10% take-up
UP = float(pr["service_massage_standard"]["price"]) - float(pr["service_massage_express"]["price"])
levers["c_extra_upgrade_A45_per_10pct"] = dict(change_before=f2(0.1 * N * (UP / 1.1 - 0.017 * UP)), price=UP,
    note="illustrative take-up; fits inside the costed 8-staff roster (solver runs 45-minute services); no repo uptake data")
out["T2_levers"] = levers

# ---------------- T3: price needed for each target ----------------
def solve(target_before, route):
    def prof(d):
        if route == "A_consult": v = v19(300 + d, 350 + d, consult=110 + d)
        elif route == "B_lounge": v = v19(300 + d, 350 + d)
        else: v = v19(300 + d, 350 + d, consult=110 + d / 2)
        return v["profit_before_company_tax"]
    lo, hi = -50.0, 300.0
    for _ in range(60):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if prof(mid) < target_before else (lo, mid)
    d = round(hi + 0.005, 2)
    return dict(increase=d, p1=f2(300 + d), p2=f2(350 + d), oop_p1=f2(300 + d - REBATE), oop_p2=f2(350 + d - REBATE),
                gap_to_245=f2(d), gap_to_295=f2(d), consult_price=f2(110 + (d if route == "A_consult" else d / 2 if route == "C_split" else 0)),
                lounge_service_p1=f2(162.15 + (d if route == "B_lounge" else d / 2 if route == "C_split" else 0)),
                profit_before=f2(prof(d)), profit_after=f2(prof(d) * 0.75))
TARGETS = {"i_repo_35186_before_company_tax": TARGET_REPO, "ii_35186_after_company_tax": f2(TARGET_REPO / 0.75),
           "iii_no_midwife_parity_21971": r17.BASELINE, "iii_b_corrected_like_for_like_19334": BASE0["profit_before_company_tax"]}
out["T3_targets_before_tax"] = TARGETS
out["T3_prices"] = {t: {rt: solve(v, rt) for rt in ("A_consult", "B_lounge", "C_split")} for t, v in TARGETS.items()}

# nearest compliant mix and the recommendation
mixes = {
 "M1_plus20_lounge": v19(320, 370),
 "M2_plus20_consult": v19(320, 370, consult=130),
 "M3_plus20_lounge_hours42": v19(320, 370, mw_hours=42),
 "M4_plus20_consult_hours42": v19(320, 370, consult=130, mw_hours=42),
 "M5_plus20_lounge_hours42_p2_30pct": v19(320, 370, share_p1=0.7, mw_hours=42),
 "M6_plus20_consult_hours39_p2_50pct": v19(320, 370, consult=130, share_p1=0.5, mw_hours=39),
 "M7_plus30_consult_hours42_p2_50pct": v19(330, 380, consult=140, share_p1=0.5, mw_hours=42)}
out["T3_mixes"] = {k: dict(p1=v["p1"], p2=v["p2"], consult=v["consult_price"], hours=v["midwife_hours_week"], p2_share=f2(1 - v["share_p1"]),
                           oop_p1=f2(v["p1"] - REBATE), oop_p2=f2(v["p2"] - REBATE),
                           before_tax=v["profit_before_company_tax"], after_tax=v["profit_after_company_tax"]) for k, v in mixes.items()}
REC = mixes["M1_plus20_lounge"]
out["recommendation"] = dict(name="M1: +A$20 on lounge + service (P1 A$320, P2 A$370); approved 45-hour midwife roster kept; plan stays 100% P1; sell Package 2 as the upgrade",
                             before_tax=REC["profit_before_company_tax"], after_tax=REC["profit_after_company_tax"],
                             oop_p1=f2(320 - REBATE), oop_p2=f2(370 - REBATE), upgrade_if_accountant_agrees="M2 (same A$20 on the consult instead): +A$862.57 a month before tax", upgrade_if_anthony_agrees="midwife paid hours 45 -> 42: +A$850.04 before tax",
                             upside_not_banked="each 10% of clients on Package 2 adds about A$2,114 a month before tax")

# ---------------- T4: A$20 test and ladder ----------------
ladder = []
for d in range(10, 101, 10):
    a, b = v19(300 + d, 350 + d, consult=110 + d), v19(300 + d, 350 + d)
    ladder.append(dict(add=d, oop_p1=f2(245 + d), oop_p2=f2(295 + d),
                       lounge_kept_per_client=f2(r17.reach(300 + d)["gtt_ex_gst_after_card"] - R["gtt_ex_gst_after_card"]),
                       lounge_month_before=f2(b["profit_before_company_tax"] - P), lounge_profit_before=b["profit_before_company_tax"], lounge_profit_after=b["profit_after_company_tax"],
                       consult_kept_per_client=f2(d * (1 - 0.017)), consult_month_before=f2(a["profit_before_company_tax"] - P),
                       consult_profit_before=a["profit_before_company_tax"], consult_profit_after=a["profit_after_company_tax"]))
out["T4_ladder"] = ladder
out["T4_r18_confirm"] = dict(r18_per_client=r18.out["Q12_plus_20"]["per_client_p1_extra_ex_gst"], r18_month=f2(N * r18.out["Q12_plus_20"]["per_client_p1_extra_ex_gst"]),
                             r18_profit_before_at_320=r18.out["Q12_plus_20"]["locked_320_370"]["profit_before_company_tax"],
                             r19_profit_before_at_320=v19(320, 370)["profit_before_company_tax"])

# ---------------- T6 payroll basis reconcile numbers ----------------
out["payroll_basis"] = dict(grace_1_20=dict(midwife_wages=GRACE["midwife_wages"], before_tax=GRACE["profit_before_company_tax"], after_tax=GRACE["profit_after_company_tax"]),
                            theodore_1_366=dict(midwife_wages=LOCK["midwife_wages"], before_tax=LOCK["profit_before_company_tax"], after_tax=LOCK["profit_after_company_tax"]),
                            oncost_parts=dict(super=r15.SUPER, workers_comp=r15.WC, leave_loading=round(r15.AL_LOAD, 5), leave_grossup=round(r15.LEAVE_GROSSUP, 4), total=round(r15.bu_worked, 4)))

# ---------------- banned stale values (pre-send fact check) ----------------
BANNED = [
 (r"A\$99\.40", "A$99.40 rebate: that is a 40-minute consult (82110). The 20-minute consult is 82105; total rebate A$55.00"),
 (r"A\$222\.15", "A$222.15: old R15 example at the A$250 all-in price. GTT receives A$272.15 (P1) / A$322.15 (P2)"),
 (r"A\$338(?![.,\d])","A$338 break-even: R15 volumes, retired"),
 (r"A\$345\.38|A\$308\.13", "R17 break-even prices on old inputs, retired"),
 (r"(?<!no )\bhosts?\b(?!\s*\|\s*none)","No hosts. The venue manager does reception and welcome"),
 (r"venue manager (starts|start|from|arrives|at|begins)[^.\n|]{0,10}07:00","Venue manager starts 06:30 (07:00 is the first draw)"),
 (r"lounge \+ consult|lounge and consult", "Say 'consult + lounge + service'"),
 (r"two consult rooms|2 consult rooms", "One consult room"),
 (r"alternating days|alternate days|A and B alternating", "Fortnightly block: Mon-Wed / Thu-Sat, swap each fortnight"),
 (r"lab (money|fee|price)[^.\n]{0,40}through GTT|GTT (collects|holds) the lab", "Lab A$27.85 is paid by the mother straight to the lab"),
 (r"A\$201\b|A\$251\b|A\$200\.60|A\$250\.60", "Out of pocket is A$245 (P1) / A$295 (P2) after the A$55 rebate"),
 (r"A\$18,526|A\$18,525\.98", "R17 headline, superseded"),
 (r"A\$13,346|A\$17,795", "R18 headline, superseded by R19 (afternoon card fees added)"),
 (r"48\.6 h", "Midwife paid hours are 45 a week on the approved roster"),
 (r"A\$12,166\.54", "Receptionist/host add-on, removed"),
 (r"\b396 clients", "Volume is 473.94 morning clients a month"),
 (r"consult[^.\n]{0,40}after the (test|draw)", "The consult is 1 to 28 days BEFORE the test"),
 (r"40[- ]minute consult", "Consult is 20 minutes"),
]
BANNED_PLAIN = ["A$99.40", "A$222.15", "A$338", "A$345.38 / A$308.13", "hosts", "venue manager starting 07:00", "lounge + consult",
                "two consult rooms", "Midwife A/B alternating days", "lab money through GTT", "A$201 / A$251 / A$200.60 / A$250.60 out of pocket",
                "A$18,526", "A$13,346 / A$17,795", "48.6 h midwife", "A$12,166.54", "396 clients", "consult after the test", "40-minute consult"]
assert len(BANNED_PLAIN) == len(BANNED)
SKIP_HEAD = re.compile(r"banned|error|root cause|why mistakes|change log|stale", re.I)
def fact_check(path):
    hits, skip = [], False
    for i, line in enumerate(open(path, encoding="utf-8"), 1):
        if line.startswith("#"):
            skip = bool(SKIP_HEAD.search(line))
        if skip or "[stale-ok]" in line:
            continue
        for pat, why in BANNED:
            if re.search(pat, line, re.I):
                hits.append((i, pat, why, line.strip()[:120]))
    return hits

# ---------------- write the centre of truth (md + yml) ----------------
def money(x): return f"A${x:,.2f}" if x >= 0 else f"-A${-x:,.2f}"
def build_centre():
    L = LOCK
    yml = {"generated_by": "docs/overhaul-2026-10-19/L14-r19/theodore_r19.py", "date": "2026-10-26", "currency": "AUD",
           "prices": {"package_1": 300.0, "package_2": 350.0, "gst_inside": True, "planning_mix_p1": 1.0,
                      "consult_medical_gst_free": 110.0, "lab_paid_to_lab_not_gtt": LAB,
                      "lounge_service_p1_taxable": 162.15, "lounge_service_p2_taxable": 212.15,
                      "gtt_receives_p1_incl_gst": R["gtt_receives_incl_gst"], "gtt_receives_p1_ex_gst": R["gtt_receives_ex_gst"],
                      "gtt_receives_p2_incl_gst": r17.reach(350)["gtt_receives_incl_gst"], "gtt_receives_p2_ex_gst": r17.reach(350)["gtt_receives_ex_gst"],
                      "pm_average_transaction_incl_gst": PM_PRICE},
           "medicare": {"consult_item": "82105", "consult_minutes": 20, "consult_rebate": REBATE_CONSULT, "test_item": "66548", "test_rebate": REBATE_TEST,
                        "collection_item": "73928 (AskMBS to confirm vs 73938)", "collection_rebate": REBATE_COLL, "total_rebate": REBATE,
                        "out_of_pocket_p1": f2(300 - REBATE), "out_of_pocket_p2": f2(350 - REBATE), "rebate_paid_to": "mother, by Medicare, never through GTT",
                        "consult_timing": "1 to 28 days before the test, booked with the test"},
           "volumes": {"am_clients_day": 18, "am_clients_month": N, "days": "Mon-Sat (22 weekdays + 4.33 Saturdays a month)",
                       "draws": "07:00 to 10:30, 25-minute pair cadence", "pm_transactions_month": round(PM_TX, 2),
                       "pm_sessions_day": "10 weekday, 5 Saturday (Model E)", "services_end": "18:00"},
           "staffing": {"am_service_staff": 8, "am_mix": "4 massage and beauty, 2 nails, 2 hair", "phlebotomists": "2 at 10-18 booked, 1 at 9 or fewer, none PM",
                        "pm_service_staff": 4, "pm_hours": "3-hour casual floor weekday", "venue_manager": "Mon-Fri 06:30-15:00 (repo costs 07:00-15:00 at A$40/h; extra 0.5 h added)",
                        "saturday_cover": "senior staff member already rostered (no loading costed)", "hosts": 0,
                        "midwives": "2 permanent part-time, 22.5 h each, fortnightly block Mon-Wed / Thu-Sat, 09:00 start, + 1 casual for leave",
                        "midwife_paid_hours_week": 45.0, "consult_rooms": 1, "collection_rooms": 2, "adaptive_rostering": "service staff and phlebotomists"},
           "rates": {"midwife_award": "Nurses Award 2020 RN L2 pp4 A$41.59 weekday, 150% Saturday (E)", "midwife_blended_hour": r18.RATE_BLEND,
                     "oncost_used": round(r15.bu_worked, 4), "oncost_sensitivity_grace": 1.20, "super": 0.12, "workers_comp": 0.017,
                     "card_fee": "1.7% + A$0.30 a transaction (E; repo lists Tyro 1.4% / Square 1.6%, provider not chosen)",
                     "payroll_tax": "WA 5.5%, A$1m threshold tapering, one group (E, check RevenueWA)", "company_tax": 0.25},
           "monthly_pnl_locked": {k: L[k] for k in ("rev_lounge_service_am_ex_gst", "rev_pm_ex_gst", "rev_consult_gst_free", "revenue_total_ex_gst",
                                  "repo_payroll", "repo_operating_expenses", "less_gst_credits", "card_fees", "card_fees_pm", "midwife_wages",
                                  "midwife_fixed_consumables", "venue_manager_0630", "payroll_tax_group", "three_company",
                                  "profit_before_company_tax", "company_tax_25", "profit_after_company_tax", "gst_collected_am", "gst_collected_pm")},
           "baseline_no_midwife_like_for_like_before_tax": BASE0["profit_before_company_tax"],
           "repo_master_net_unchanged": TARGET_REPO,
           "per_client_waterfall_p1": [[k, v] for k, v in wf],
           "banned_stale_values": [why for _, why in BANNED],
           "not_in_pnl": {"post_test_discount_10pct": "adopted 2026-10-17, repo estimate -A$1,386.27 a month at 25% take-up, not deducted (R)",
                          "senior_cover_loading": "not in repo", "casual_midwife_minimum_engagement": "inside the 1.366 leave gross-up, not separately quoted"}}
    with open(os.path.join(HERE, "center_of_truth.yml"), "w", encoding="ascii", errors="replace") as fh:
        yaml.safe_dump(yml, fh, sort_keys=False, allow_unicode=False, width=200)
    yaml.safe_load(open(os.path.join(HERE, "center_of_truth.yml"), encoding="ascii"))

    pnl_rows = [("Lounge + service, morning, ex GST (474 x A$147.41)", L["rev_lounge_service_am_ex_gst"], "R volume, E split"),
                ("Afternoon sales, ex GST (repo A$24,585.37 / 1.1)", L["rev_pm_ex_gst"], "R"),
                ("Consult, GST-free (474 x A$110, Medical)", L["rev_consult_gst_free"], "E"),
                ("**Revenue, ex GST**", L["revenue_total_ex_gst"], ""),
                ("Repo staff (8 AM service, 2 phlebotomists, 4 PM, venue manager 07:00), super, workers comp", L["repo_payroll"], "R"),
                ("Repo running costs (rent, insurance, overheads, supplies)", L["repo_operating_expenses"], "R"),
                ("GST credits on costs", L["less_gst_credits"], "R"),
                ("Card fees, morning (on A$272.15)", L["card_fees"], "E"),
                ("Card fees, afternoon (210.13 x A$117)", L["card_fees_pm"], "E"),
                ("Midwife wages (45 h/week, on-cost 1.366, casual leave cover inside)", L["midwife_wages"], "E"),
                ("Midwife fixed costs and consumables (one consult room)", L["midwife_fixed_consumables"], "E"),
                ("Venue manager 06:30 start", L["venue_manager_0630"], "R rate"),
                ("WA payroll tax, whole group", L["payroll_tax_group"], "E"),
                ("Three-company running cost", L["three_company"], "E"),
                ("**Profit before company tax**", L["profit_before_company_tax"], ""),
                ("Company tax 25%", L["company_tax_25"], "E"),
                ("**Profit after company tax = franked dividend available**", L["profit_after_company_tax"], "")]
    md = ["# GTT Center Perth: Financial Center of Truth", "",
          "**One place for every money variable.** Generated by [theodore_r19.py](overhaul-2026-10-19/L14-r19/theodore_r19.py); do not edit by hand. "
          "Re-run the script after any decision change and this file and [center_of_truth.yml](overhaul-2026-10-19/L14-r19/center_of_truth.yml) regenerate together. "
          "The repo master model figure (A$35,186.40, CURRENT-STATE line 30) is NOT changed by this file; it is shown here restated to a like-for-like basis. "
          "All amounts AUD a month unless stated. General knowledge and desk research, not your personal documents. Verify before acting.", "",
          "Tags: **R** repo figure, **V** official source, **E** estimate, **Q** quote needed.", "",
          "## 1. Prices and money flow (Structure B)", "",
          "| Item | Package 1 | Package 2 | GST | Who receives it | Tag |", "|---|---|---|---|---|---|",
          "| Mother pays | A$300.00 | A$350.00 | inside | | Locked |",
          f"| Lab test | A${LAB} | A${LAB} | GST-free | The lab, paid by the mother directly. Never GTT money | Locked |",
          "| Consult (20 min, item 82105) | A$110.00 | A$110.00 | GST-free | Medical | Locked |",
          "| Lounge + service | A$162.15 | A$212.15 | taxable, 1/11 is GST | Lounge | Locked |",
          f"| Reaches GTT, GST inside | {money(R['gtt_receives_incl_gst'])} | {money(r17.reach(350)['gtt_receives_incl_gst'])} | | Medical + Lounge | R maths |",
          f"| Reaches GTT, ex GST | {money(R['gtt_receives_ex_gst'])} | {money(r17.reach(350)['gtt_receives_ex_gst'])} | | | R maths |",
          f"| Medicare rebate to the mother (A$32.95 + A$16.95 + A$5.10) | {money(REBATE)} | {money(REBATE)} | | The mother, from Medicare | V |",
          f"| **Mother's out of pocket (includes the lab fee)** | **{money(300 - REBATE)}** | **{money(350 - REBATE)}** | | | V |", "",
          "Consult is booked with the test and happens 1 to 28 days BEFORE it. Medical pays Lounge a flat market room fee (inside the group, no profit effect). Plan: 100% Package 1.", "",
          "## 2. Volumes, staffing and hours (checked against the repo by the script)", "",
          "| Variable | Value | Source |", "|---|---|---|",
          f"| Morning clients | 18 a day, Mon-Sat = {N} a month | R (revenue_ramp.yml, 22 + 4.33 days) |",
          f"| Afternoon transactions | {PM_TX:.2f} a month (8.70 weekday, 4.35 Saturday a day) at A$117 = A$24,585.37 | R (revenue_assumptions.yml, Model E: 10 sessions weekday, 5 Saturday) |",
          "| AM service staff | 8 (4 massage and beauty, 2 nails, 2 hair), 6 h, 07:00-13:00 | R (cost_ramp_model.py; solver verifies 8 at N=18 with 45-minute services) |",
          "| Phlebotomists | 2 at 10-18 booked, 1 at 9 or fewer, none PM | R |",
          "| PM service staff | 4 casual, 3-hour floor | R |",
          "| Venue manager | Mon-Fri 06:30-15:00 (repo 07:00 + 0.5 h added, A$500.28 loaded) | R rate, locked time |",
          "| Hosts | none | Locked |",
          "| Midwives | 2 permanent part-time 22.5 h each (45 paid h a week), fortnightly block Mon-Wed / Thu-Sat, 09:00, + 1 casual for leave | Locked |",
          f"| Consult hours needed | 18 x 20 min = 6.0 h a day, 36 h a week (80% of 45 paid) | maths |",
          "| Consult rooms / collection rooms | 1 / 2 (one chair each) | Locked |", "",
          "## 3. Rates and tax", "",
          "| Variable | Value | Tag |", "|---|---|---|",
          f"| Midwife rate | Nurses Award RN L2 pp4 A$41.59 weekday, 150% Saturday; blended A${r18.RATE_BLEND:.2f} | E |",
          f"| Midwife on-cost (used) | {r15.bu_worked:.3f}: super 12%, workers comp 1.7%, leave loading, paid leave covered by the casual | E |",
          "| Midwife on-cost (sensitivity) | 1.20 (Grace: no leave cover) | E |",
          "| Repo staff on-cost | casual rates incl. 25% loading, + super 12% + workers comp 1.7% | R |",
          "| Card fee | 1.7% + A$0.30 a transaction on all card takings, AM and PM | E (repo: Tyro 1.4% / Square 1.6%, provider not chosen) |",
          "| WA payroll tax | 5.5% above the A$1m grouped threshold (tapering deduction) | E, check RevenueWA |",
          "| Company tax | 25% (base rate entity), one consolidated return; franked dividends direct to Anthony and partner (Route B) | E |", "",
          "## 4. Monthly P&L, whole venture (Holdings + Medical + Lounge), locked case", "",
          "| Line | Monthly | Tag |", "|---|---|---|"] + [f"| {k} | {money(v)} | {t} |" for k, v, t in pnl_rows] + [
          "", f"GST passed to the ATO (not revenue): morning {money(L['gst_collected_am'])}, afternoon {money(L['gst_collected_pm'])}. "
          f"Like-for-like with no midwife (old A$250 package, same costs): {money(BASE0['profit_before_company_tax'])} before company tax.", "",
          "## 5. Per-client waterfall (Package 1, A$300)", "", "| Step | A$ per client |", "|---|---|"] + [f"| {k} | {money(v)} |" for k, v in wf] + [
          "", f"The mother then gets A$55.00 back from Medicare, so her own cost is A$245.00 (A$295.00 on Package 2), lab fee included.", "",
          "## 6. Not in the P&L (known, flagged)", "", "| Item | Status |", "|---|---|",
          "| 10% post-test discount (adopted 2026-10-17) | Repo estimate -A$1,386.27 a month at 25% take-up; not deducted (R) |",
          "| Senior cover loading (afternoon gap, Saturday) | Not in repo |",
          "| Collection item 73928 vs 73938 | AskMBS to confirm; changes the lab's price and rebate by A$1.70, not GTT's revenue |", "",
          "## 7. Open price decision (NOT in the P&L above until Anthony decides)", "",
          f"Theodore R19 recommends +A$20 on lounge + service (P1 A$320, P2 A$370; out of pocket A$265 / A$315): profit {money(REC['profit_before_company_tax'])} before, "
          f"{money(REC['profit_after_company_tax'])} after company tax. Full options: [THEODORE-R19.md](overhaul-2026-10-19/L14-r19/THEODORE-R19.md).", "",
          "## 8. Banned stale values (pre-send fact check)", "",
          "Run `python docs/overhaul-2026-10-19/L14-r19/theodore_r19.py --check <file>` before anything goes to Anthony.", "",
          "| Banned | Correct |", "|---|---|"] + [f"| {b} | {w} |" for b, (_, w) in zip(BANNED_PLAIN, BANNED)] + [
          "", "## 9. Change log", "", "| Date | Change | By |", "|---|---|---|",
          "| 2026-10-26 | Created. Afternoon card fees added (A$480.99 a month); like-for-like baseline now includes card fees; headline A$17,314.31 before / A$12,985.73 after company tax | Theodore R19 |", ""]
    with open(os.path.join(REPO, "docs", "FINANCIAL-CENTER-OF-TRUTH.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(md))

if __name__ == "__main__" and len(sys.argv) > 2 and sys.argv[1] == "--check":
    hits = fact_check(sys.argv[2])
    for h in hits: print(f"line {h[0]}: {h[2]}  ->  {h[3]}")
    print(f"fact_check: {len(hits)} banned value(s) found"); sys.exit(1 if hits else 0)

build_centre()
out["fact_check_centre"] = len(fact_check(os.path.join(REPO, "docs", "FINANCIAL-CENTER-OF-TRUTH.md")))
json.dump(out, open(os.path.join(HERE, "theodore_r19_results.json"), "w"), indent=1, default=str)
if __name__ == "__main__":
    print(json.dumps({k: out[k] for k in ("T1_split", "T2_midwife_vs_consult", "recommendation", "T4_r18_confirm", "fact_check_centre")}, indent=1))
    for row in bridge: print(row)
    print("LOCK", LOCK["profit_before_company_tax"], LOCK["profit_after_company_tax"], "BASE0", BASE0["profit_before_company_tax"])
    for k, v in out["T2_levers"].items(): print(k, v)
    for t, d in out["T3_prices"].items():
        for rt, x in d.items(): print(t, rt, x["p1"], x["p2"], x["oop_p1"], x["oop_p2"], x["profit_before"])
    for k, v in out["T3_mixes"].items(): print(k, v)
    for r in ladder: print(r)
    print(out["payroll_basis"])
