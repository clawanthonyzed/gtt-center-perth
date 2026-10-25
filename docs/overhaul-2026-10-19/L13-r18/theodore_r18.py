"""Theodore R18 (2026-10-25). EXTENDS theodore_r17.py (imported; it imports r16 -> r15 -> r14 -> r13). No second calculator.
Repo base lines come from a LIVE run of the repo's own tools/master_financial_model.py (Table 1, steady month), never typed in.
Reused: r17.reach (package split, GST half-up), r15.fee_pct (card fee), r14.ptax (WA payroll tax), r14.WAGES / r14.COST / r14.AHPRA
(midwife rate and fixed costs), r15.bu_worked / r15.SUPER / r15.WC (on-costs), r15.mw_taxable_month, r15.run3 (three-company cost),
r14.ITEMS (MBS fees, re-read on MBS Online 2026-10-25).
LOCKED (Anthony, not re-opened): Structure B; Package 1 = 2 x 30 min services A$300, Package 2 = 2 services up to 45 min A$350, GST inside;
plan 100% Package 1; SHORT 20-minute consult, referral only (MBS 82105: "at least 10 minutes"); 1 midwife rostered per day Mon-Sat
09:00-17:00 (2 permanent part-time + 1 casual for leave), ONE consult room; venue manager starts 06:30 (repo 07:00);
18 AM clients a day (repo 473.94 a month, six days); payroll tax accepted; tax consolidation + GST group year 1.
Labels: R repo, V official source, E estimate, Q quote needed. AUD.
"""
import contextlib, importlib.util, io, json, os, sys
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
spec = importlib.util.spec_from_file_location("theodore_r17", os.path.join(HERE, "..", "L12-r17", "theodore_r17.py"))
r17 = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(r17)          # r17..r13 rewrite their own results json on import; content unchanged (checked with git status)
r16, r15, r14 = r17.r16, r17.r15, r17.r14
f2, c2 = r15.f2, r17.c2

# ---------- repo base, live from the repo's own model (R) ----------
sys.path.insert(0, os.path.join(REPO, "tools"))
import master_financial_model as mfm
BASE = mfm.compute_month_pnl("scenario_table_1", 12, mfm.CanonicalModelInputs())
assert abs(BASE["net_operating_result"] - r14.BASE_NET) < 0.01          # 35,186.40
REV, PAY, OPEX = BASE["revenue"], BASE["payroll"], BASE["operating_expenses"]
AM_OLD = REV["am_revenue"]                                               # 118,485.00 = 473.94 x A$250
GST_CREDITS = f2(r17.AFTER_GST - (REV["total_revenue"] / 1.1 - BASE["total_operating_costs"]))   # implied by the R9/R11 after-GST basis
N = r17.CL6                                                              # 473.94 AM clients a month
LAB, CONSULT = r17.LAB, r17.CONSULT
out = {"generated": "2026-10-25", "imports": "theodore_r17.py -> r16 -> r15 -> r14 -> r13; tools/master_financial_model.py (live)",
       "labels": "R repo, V official, E estimate, Q quote", "repo_base_live": BASE, "gst_credits_implied": GST_CREDITS}

# ---------- locked roster inputs ----------
cr = yaml.safe_load(open(os.path.join(REPO, "data", "canonical", "cost_ramp.yml"), encoding="utf-8"))
OPEN_INC = 7040.00                                                       # R opening_time_increment a month (VM 07:00-15:00, 22 weekdays x 8 h)
VM_RATE = OPEN_INC / 22 / 8                                              # R A$40.00 an hour
VM_EXTRA_WAGES = 0.5 * 22 * VM_RATE                                      # 06:30 start: +0.5 h on 22 weekdays
VM_EXTRA_LOADED = f2(VM_EXTRA_WAGES * (1 + r15.SUPER + r15.WC))          # 500.28 (Grace R17)
MW_HOURS_W = 7.5 * 6                                                     # 1 midwife a day, 09:00-17:00 less 30 min break, Mon-Sat (E break)
SAT = 1 / 6
c = r14.COST["base"]
o, s, _, _ = r14.WAGES[c["rate"]]
RATE_BLEND = o * (1 - SAT) + s * SAT                                     # A$ an hour before on-costs
CONSULT_SLOT = 20                                                        # minutes, Anthony (clinical + notes)
DAYS_M = 22 + 4.33                                                       # R repo convention
consults_day = N / DAYS_M

def midwife(basis):
    oncost = {"grace_1.20": c["oncost"], "leave_covered_1.366": r15.bu_worked}[basis]
    wage = MW_HOURS_W * r14.WEEKS_M * RATE_BLEND * oncost
    heads = 2                                                            # 2 permanent; casual relief's indemnity is a Q
    fixed = heads * ((r14.AHPRA + c["pi"] + c["cpd"]) / 12 + c["sw_m"] + c["equip"] / 60) + 1 * r14.ROOM_M2 * r14.RENT
    taxable_y = r15.mw_taxable_month(wage, oncost) * 12 * (r15.LEAVE_GROSSUP if basis.startswith("leave") else 1)   # relief wages are taxable too (as R16)
    return dict(wage=wage, fixed=fixed, consum=N * c["consum"], taxable_y=taxable_y, oncost=oncost)

def venture(p1=300.0, p2=350.0, share_p1=1.0, basis="leave_covered_1.366", vm=True, mid=True):
    """Whole venture (Holdings + Medical + Lounge consolidated), one month, ex GST."""
    prices = {"P1": (p1, share_p1), "P2": (p2, 1 - share_p1)}
    lounge_ex = gst_am = consult_rev = card = takings = 0.0
    for P, sh in prices.values():
        r = r17.reach(P); m = N * sh
        if mid:
            lounge_ex += m * r["lounge_ex_gst"]; gst_am += m * r["lounge_gst_inside"]; consult_rev += m * CONSULT
            card += m * r["card_fee"]; takings += m * (P - LAB)
        else:
            lounge_ex += m * 250 / 1.1; gst_am += m * 250 / 11; takings += m * 250
    pm_ex = REV["pm_revenue"] / 1.1
    mw = midwife(basis) if mid else dict(wage=0, fixed=0, consum=0, taxable_y=0)
    vm_cost = VM_EXTRA_LOADED if vm else 0.0
    vm_tax_y = VM_EXTRA_WAGES * (1 + r15.SUPER) * 12 if vm else 0.0
    taxable_y = r15.REPO_TAXABLE_Y + mw["taxable_y"] + vm_tax_y
    ptax = r14.ptax(taxable_y) / 12
    three = r15.run3["base"]["total_month"]
    rev_total = lounge_ex + pm_ex + consult_rev
    costs = dict(repo_payroll=PAY, repo_operating_expenses=OPEX, less_gst_credits=-GST_CREDITS, card_fees=card,
                 midwife_wages=mw["wage"], midwife_fixed_consumables=mw["fixed"] + mw["consum"], venue_manager_0630=vm_cost,
                 payroll_tax_group=ptax, three_company=three)
    before = rev_total - sum(costs.values())
    ctax = max(0.0, before) * 0.25
    return dict(clients=round(N, 2), takings_incl_gst_to_gtt=f2(takings + REV["pm_revenue"]),
                rev_lounge_service_am_ex_gst=f2(lounge_ex), rev_pm_ex_gst=f2(pm_ex), rev_consult_gst_free=f2(consult_rev),
                revenue_total_ex_gst=f2(rev_total), gst_collected_am=f2(gst_am), gst_collected_pm=f2(REV["pm_revenue"] / 11),
                **{k: -f2(v) for k, v in costs.items()}, total_costs=-f2(sum(costs.values())),
                payroll_taxable_wages_year=f2(taxable_y), payroll_tax_threshold=1_000_000, over_threshold_by=f2(taxable_y - 1_000_000),
                profit_before_company_tax=f2(before), company_tax_25=-f2(ctax), profit_after_company_tax=f2(before - ctax),
                franked_dividend_available=f2(before - ctax), franking_credits_attached=f2(ctax))

# Q1 / Q12: locked case and variants
Q1 = {"locked_leave_covered": venture(), "locked_grace_1.20": venture(basis="grace_1.20"),
      "no_midwife_no_vm_baseline": venture(mid=False, vm=False), "r17_basis_check_no_vm": venture(vm=False)}
assert abs(Q1["no_midwife_no_vm_baseline"]["profit_before_company_tax"] - r17.BASELINE) < 1.0      # 21,971 reproduced
out["Q1_whole_venture_pnl"] = Q1
out["Q12_plus_20"] = {"locked_320_370": venture(320.0, 370.0), "locked_320_370_grace": venture(320.0, 370.0, basis="grace_1.20"),
                      "per_client_p1_extra_ex_gst": f2(r17.reach(320)["gtt_ex_gst_after_card"] - r17.reach(300)["gtt_ex_gst_after_card"]),
                      "per_client_p1_extra_gst": f2(r17.reach(320)["lounge_gst_inside"] - r17.reach(300)["lounge_gst_inside"])}
out["Q12_payroll_added"] = dict(venue_manager_0630=VM_EXTRA_LOADED,
                                midwives_grace_1_20=f2(midwife("grace_1.20")["wage"]), midwives_leave_covered=f2(midwife("leave_covered_1.366")["wage"]),
                                total_grace=f2(VM_EXTRA_LOADED + midwife("grace_1.20")["wage"]),
                                total_leave_covered=f2(VM_EXTRA_LOADED + midwife("leave_covered_1.366")["wage"]))
out["roster_check"] = dict(midwife_hours_week=MW_HOURS_W, consults_per_day=round(consults_day, 2),
                           consult_hours_per_day=round(consults_day * CONSULT_SLOT / 60, 2), paid_hours_per_day=7.5,
                           utilisation=round(consults_day * CONSULT_SLOT / 60 / 7.5, 3), rate_blend=f2(RATE_BLEND))

# Q2 / Q10: rebate arithmetic (MBS Online re-read 2026-10-25, V)
IT = r14.ITEMS
TEST = {"66548+73928_repo_item": 16.95 + 5.10, "66548+73938_as_lab_price": 16.95 + 6.80}
Q2 = {}
for pk, P in (("P1", 300.0), ("P2", 350.0)):
    r = r17.reach(P)
    for cons in ("82105", "82110"):
        for tk, tv in TEST.items():
            reb = IT[cons]["ben"] + tv
            Q2[f"{pk}|{cons}|{tk}"] = dict(client_pays=P, reaches_gtt_incl_gst=r["gtt_receives_incl_gst"], reaches_gtt_ex_gst=r["gtt_receives_ex_gst"],
                                           lab=LAB, rebate=f2(reb), out_of_pocket=f2(P - reb))
out["Q2_rebate"] = Q2
out["Q2_lab_price_check"] = dict(lab_price_used=LAB, with_73938=f2(19.90 + 7.95), with_73928_repo_item=f2(19.90 + 5.95))

# Q8: midwife impact, per client and month, like for like (474)
before_pc = f2(250 / 1.1)
after_pc_rev = r17.reach(300)["gtt_receives_ex_gst"]
mw_lc = midwife("leave_covered_1.366")
mw_pc = f2((mw_lc["wage"] + mw_lc["fixed"] + mw_lc["consum"]) / N)
out["Q8_midwife_impact"] = dict(per_client_revenue_before_ex_gst=before_pc, per_client_revenue_after_ex_gst=after_pc_rev,
                                per_client_card_fee=r17.reach(300)["card_fee"], per_client_midwife_cost=mw_pc,
                                month_revenue_before=Q1["no_midwife_no_vm_baseline"]["revenue_total_ex_gst"],
                                month_revenue_after=Q1["locked_leave_covered"]["revenue_total_ex_gst"],
                                month_profit_before=Q1["no_midwife_no_vm_baseline"]["profit_before_company_tax"],
                                month_profit_after=Q1["locked_leave_covered"]["profit_before_company_tax"])

# Q10: out of pocket by package (consult 82105 short, repo collection item)
out["Q10_oop"] = {pk: Q2[f"{pk}|82105|66548+73928_repo_item"]["out_of_pocket"] for pk in ("P1", "P2")}
out["Q10_oop_plus20"] = {pk: f2(v + 20) for pk, v in out["Q10_oop"].items()}

# Q5: interest on GTT's own prepaid money (lab money: none held)
RATES = {"big_bank_business_saver_1.00_U": 0.01, "cba_3m_business_td_4.30_E": 0.043, "best_3m_business_td_5.00_E": 0.05, "rba_cash_4.60_V": 0.046}
held = r17.reach(300)["gtt_receives_incl_gst"] * N / 30.4 * 21
out["Q5_prepaid"] = dict(clients=round(N, 2), average_held_21_days=f2(held), r17_figure_396=74447,
                         **{f"interest_year_{k}": f2(held * v) for k, v in RATES.items()}, after_25pct_tax_at_5=f2(held * 0.05 * 0.75), lab_money_held=0.0)

# Q11: bridge old figures to R17 A$18,526 and to R18 locked
yml = yaml.safe_load(open(os.path.join(REPO, "data", "models", "master_financial_model.yml"), encoding="utf-8"))
old = [x for x in yml["outputs"]["steady_state_summary"] if x["scenario_id"] == "scenario_table_1"][0] if "outputs" in yml else None
r17row = r17.out["Q9_packages_mix"]["short_82105_10min|100% P1"]["permanent_r14_oncost"]
L, G = Q1["locked_leave_covered"], Q1["locked_grace_1.20"]
bridge = [
 ("A. Old struck figure 2026-08-21 (CS line 179)", 38705.33),
 ("Dedicated PM reception removed, 2026-08-21 (yml status note)", 44166.17 - 38705.33),
 ("B. Repo yml figure, 2026-08-21 later", 44166.17),
 ("PM revenue: PM capacity locked at 10 sessions a day (2026-09-19)", REV["pm_revenue"] - 36225.69),
 ("Payroll: venue manager Mon-Fri and phlebotomist model closed (2026-09-19)", 96256.18 - PAY),
 ("C. Repo today, no GST line (CS line 30)", BASE["net_operating_result"]),
 ("GST taken out (repo after-GST basis R9/R11)", r17.AFTER_GST - BASE["net_operating_result"]),
 ("D. Repo after GST", r17.AFTER_GST),
 ("Repo payroll tax (was never in the repo net)", -r14.ptax(r15.REPO_TAXABLE_Y) / 12),
 ("Three-company running cost", -r15.run3["base"]["total_month"]),
 ("E. Like-for-like baseline, council rounds (R16/R17)", r17.BASELINE),
 ("Consult income 474 x A$110 (GST-free, Medical)", r17row["consult_income"]),
 ("Lounge and service price A$250 -> A$162.15 (ex GST)", r17row["lounge_change_vs_old_250"]),
 ("Card fees", r17row["card_fees"]),
 ("Midwife wages, R17 demand basis 48.6 h/week x 1.20", r17row["midwife_wages"]),
 ("Midwife fixed and consumables", r17row["midwife_fixed_consumables"]),
 ("Extra payroll tax on midwives", r17row["payroll_tax_group"] + r14.ptax(r15.REPO_TAXABLE_Y) / 12),
 ("F. R17 headline (100% P1, short consult)", r17row["group_before_company_tax"]),
 ("Midwife roster: 45 h/week instead of 48.6, one consult room instead of two (same 1.20)", None),
 ("Venue manager 06:30 start", -VM_EXTRA_LOADED),
 ("Payroll tax on the venue manager change and roster change", None),
 ("G. R18 locked, Grace on-cost 1.20", G["profit_before_company_tax"]),
 ("Leave cover for permanent midwives (1.20 -> 1.366, casual relief) and its payroll tax", L["profit_before_company_tax"] - G["profit_before_company_tax"]),
 ("H. R18 locked, leave covered (headline)", L["profit_before_company_tax"]),
 ("Company tax 25%", L["company_tax_25"]),
 ("I. R18 after company tax = franked dividend available", L["profit_after_company_tax"])]
# fill the two derived lines so the bridge adds to the dollar
gr = G["profit_before_company_tax"]; f = r17row["group_before_company_tax"]
mw_g, mw17 = -midwife("grace_1.20")["wage"], r17row["midwife_wages"]
fix_g = -(midwife("grace_1.20")["fixed"] + midwife("grace_1.20")["consum"])
bridge[18] = (bridge[18][0], (mw_g - mw17) + (fix_g - r17row["midwife_fixed_consumables"]))
bridge[20] = (bridge[20][0], gr - f - bridge[18][1] - bridge[19][1])
out["Q11_bridge"] = [(k, f2(v)) for k, v in bridge]
chk = lambda a, b: abs(a - b) < 0.05
assert chk(bridge[0][1] + bridge[1][1], bridge[2][1]) and chk(bridge[2][1] + bridge[3][1] + bridge[4][1], bridge[5][1])
assert chk(bridge[10][1] + sum(x[1] for x in bridge[11:17]), bridge[17][1])
assert chk(bridge[17][1] + sum(x[1] for x in bridge[18:21]), bridge[21][1])

json.dump(out, open(os.path.join(HERE, "theodore_r18_results.json"), "w"), indent=1, default=str)
if __name__ == "__main__":
    for k, v in Q1.items(): print(k, json.dumps(v))
    for k in ("Q12_plus_20", "Q12_payroll_added", "roster_check", "Q2_lab_price_check", "Q8_midwife_impact", "Q10_oop", "Q5_prepaid"):
        print(k, json.dumps(out[k]))
    for k, v in Q2.items(): print(k, v)
    for row in out["Q11_bridge"]: print(row)
    print("gst_credits", GST_CREDITS)
