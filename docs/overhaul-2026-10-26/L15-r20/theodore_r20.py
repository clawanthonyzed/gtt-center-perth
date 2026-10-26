"""Theodore R20 (2026-10-26). Copy of the R19 structure, EXTENDED. Engine is unchanged and imported, never re-written:
theodore_r18.py (-> r17 -> r16 -> r15 -> r14 -> r13) which runs the repo's own tools/master_financial_model.py live.
R20 changes only inputs, through the same context manager R19 used (consult price, midwife paid hours):
  * consult A$130 GST-free inside the packages (P1 A$320 / P2 A$370 full price; client pays GTT A$292.15 / A$342.15; lab A$27.85 paid to the lab);
  * midwives 08:00 to 16:00 (same paid hours: 8 h on site less a 30 minute unpaid break = 7.5 h);
  * standalone private consults at A$130 GST-free in the spare midwife slots (UPSIDE ONLY, never in the headline);
  * prepaid float and interest, refund maths, break-even/cash-flow deltas;
  * writes docs/FINANCIAL-CENTER-OF-TRUTH.md + center_of_truth.yml, and a banned-stale-values fact check.
Labels: R repo, V official, E estimate, Q quote needed, U unverified. AUD.   Run:  python theodore_r20.py   |   python theodore_r20.py --check file.md
"""
import contextlib, importlib.util, io, json, math, os, re, sys
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
spec = importlib.util.spec_from_file_location("theodore_r18", os.path.join(HERE, "..", "..", "overhaul-2026-10-19", "L13-r18", "theodore_r18.py"))
r18 = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(r18)
r17, r15, r14 = r18.r17, r18.r15, r18.r14
f2 = r15.f2
sys.path.insert(0, os.path.join(REPO, "tools"))
import cost_ramp_model as crm
import demand_driven_staffing_solver as dds

N = r18.N
LAB, REBATE_CONSULT, REBATE_TEST, REBATE_COLL = 27.85, 32.95, 16.95, 5.10
REBATE = f2(REBATE_CONSULT + REBATE_TEST + REBATE_COLL)               # 55.00 total (consult 32.95 + lab 22.05)
LAB_REBATE = f2(REBATE_TEST + REBATE_COLL)                            # 22.05
CONSULT_NEW, P1, P2 = 130.0, 320.0, 370.0
TAX, TARGET = 0.25, 20000.0
LOUNGE_P1, LOUNGE_P2 = f2(P1 - CONSULT_NEW - LAB), f2(P2 - CONSULT_NEW - LAB)      # 162.15 / 212.15 unchanged
out = {"generated": "2026-10-26", "engine": "theodore_r18.py (-> r17 .. r13) + tools/master_financial_model.py live; same context-manager patching as R19"}

# ---- inputs checked against the repo (same checks as R19) ----
pb = r18.BASE["payroll_breakdown"]
mb, nails, hair = crm.AM_HEADCOUNT_HIGH
ra = {r["id"]: r for r in yaml.safe_load(open(os.path.join(REPO, "data", "canonical", "revenue_assumptions.yml"), encoding="utf-8"))["records"]}
pr = {r["id"]: r for r in yaml.safe_load(open(os.path.join(REPO, "data", "canonical", "pricing.yml"), encoding="utf-8"))["records"]}
PM_PRICE = float(pr["pm_alacarte_average"]["price"])
PM_WD, PM_SAT = ra["rev_pm_weekday_transactions"]["value"], ra["rev_pm_saturday_transactions"]["value"]
PM_TX = PM_WD * 22 + PM_SAT * 4.33
with contextlib.redirect_stdout(io.StringIO()):
    peak18 = dds.assign_and_check(18)
assert mb + nails + hair == 8 and crm.PM_ROLES == 4 and peak18["total_headcount"] == 8 and dds.SERVICE_MINUTES == 45
assert abs(PM_TX * PM_PRICE - r18.REV["pm_revenue"]) < 5.0 and abs(round(N / 26.33, 2) - 18.0) < 0.01
assert abs(r18.CONSULT_SLOT - 20) < 1e-9
out["inputs_check"] = dict(am_staff=8, pm_staff=4, solver_staff_at_18=peak18["total_headcount"], am_clients_month=N, pm_tx_month=round(PM_TX, 2),
                           pm_price_incl_gst=PM_PRICE, pm_weekday_tx_day=PM_WD, pm_saturday_tx_day=PM_SAT, pm_revenue_repo=r18.REV["pm_revenue"])

# ---- the R20 venture ----
@contextlib.contextmanager
def patched(consult, mw_hours):
    old = (r17.CONSULT, r18.CONSULT, r18.MW_HOURS_W)
    r17.CONSULT = r18.CONSULT = consult; r18.MW_HOURS_W = mw_hours
    try:
        yield
    finally:
        r17.CONSULT, r18.CONSULT, r18.MW_HOURS_W = old

PM_CARD = f2(PM_TX * r15.fee_pct(PM_PRICE))
def v20(p1=P1, p2=P2, share_p1=1.0, consult=CONSULT_NEW, mw_hours=45.0, basis="leave_covered_1.366"):
    with patched(consult, mw_hours):
        v = dict(r18.venture(p1, p2, share_p1, basis, True, True))
    v["card_fees_pm"] = -PM_CARD
    v["card_fees_total"] = f2(v["card_fees"] - PM_CARD)
    before = f2(v["profit_before_company_tax"] - PM_CARD)
    v["total_costs"] = f2(v["total_costs"] - PM_CARD)
    v["profit_before_company_tax"] = before
    v["company_tax_25"] = -f2(max(0, before) * TAX)
    v["profit_after_company_tax"] = v["franked_dividend_available"] = f2(before - max(0, before) * TAX)
    v["franking_credits_attached"] = f2(max(0, before) * TAX)
    v["consult_price"], v["p1"], v["p2"], v["midwife_hours_week"], v["oncost_basis"] = consult, p1, p2, mw_hours, basis
    return v

LOCK = v20()
out["locked"] = LOCK
BEFORE, AFTER = LOCK["profit_before_company_tax"], LOCK["profit_after_company_tax"]
out["T1_headline"] = dict(profit_before_company_tax=BEFORE, company_tax=LOCK["company_tax_25"], net_after_all=AFTER, threshold=TARGET,
                          above_threshold=AFTER > TARGET, margin_vs_threshold=f2(AFTER - TARGET),
                          before_tax_needed_for_threshold=f2(TARGET / 0.75), shortfall_before_tax=f2(TARGET / 0.75 - BEFORE))
with patched(CONSULT_NEW, 45.0):
    R1, R2 = r17.reach(P1), r17.reach(P2)
assert R1["gtt_receives_incl_gst"] == 292.15 and R2["gtt_receives_incl_gst"] == 342.15 and R1["lounge_incl_gst"] == LOUNGE_P1
out["T1_reach"] = dict(p1=R1, p2=R2, out_of_pocket_p1=f2(P1 - REBATE), out_of_pocket_p2=f2(P2 - REBATE))
# card fee: the model uses 1.7% + A$0.30 on what the client pays GTT (E); the repo lists Tyro 1.4% / Square 1.6% (cards present), provider not chosen
fee = lambda x, pct=0.017: pct * x + 0.30
out["T1_card_fee_rate_check"] = dict(model_rate="1.7% + A$0.30 a transaction (E) on the full A$292.15", fee_model=f2(fee(292.15)),
    repo_tyro_1_4=f2(fee(292.15, 0.014)), repo_square_1_6=f2(fee(292.15, 0.016)), model_matches_r18_reach=R1["card_fee"],
    month_profit_before_if_repo_rate_1_6=f2(BEFORE + N * (R1["card_fee"] - fee(292.15, 0.016)) + PM_CARD - PM_TX * fee(PM_PRICE, 0.016)),
    note="The repo opex.yml lists Tyro 1.4% and Square 1.6% for cards present and has NO fixed A$0.30; the model's 1.7% + A$0.30 is the more cautious estimate.")

pc = lambda x: f2(x / N)
wf = [("Client pays GTT at checkout (Package 1, lab fee not included)", R1["gtt_receives_incl_gst"]),
      ("   made of: consult (GST-free, Medical)", CONSULT_NEW),
      ("   made of: lounge + service incl GST (Lounge)", LOUNGE_P1),
      ("GST inside the lounge + service part, passed to the ATO", -R1["lounge_gst_inside"]),
      ("Card fee on the full A$292.15", -R1["card_fee"]),
      ("GTT keeps from the morning package", R1["gtt_ex_gst_after_card"]),
      ("Plus afternoon sales per morning client (ex GST, after card fee)", pc(LOCK["rev_pm_ex_gst"] - PM_CARD)),
      ("Less repo staff (8 AM service, 2 phlebotomists, 4 PM, venue manager 07:00)", pc(LOCK["repo_payroll"])),
      ("Less repo running costs, after GST credits", pc(LOCK["repo_operating_expenses"] + LOCK["less_gst_credits"])),
      ("Less midwife wages", pc(LOCK["midwife_wages"])),
      ("Less midwife fixed costs and consumables", pc(LOCK["midwife_fixed_consumables"])),
      ("Less venue manager 06:30", pc(LOCK["venue_manager_0630"])),
      ("Less payroll tax (whole group)", pc(LOCK["payroll_tax_group"])),
      ("Less three-company running cost", pc(LOCK["three_company"])),
      ("Profit per client before company tax", pc(BEFORE)),
      ("Company tax 25%", pc(LOCK["company_tax_25"])),
      ("Net per client after GST, card fees, payroll tax and company tax", pc(AFTER))]
out["T1_waterfall_per_client"] = wf
out["T1_client_view"] = dict(full_price_p1=P1, lab_to_lab=LAB, to_gtt=R1["gtt_receives_incl_gst"], medicare_back=REBATE, out_of_pocket=f2(P1 - REBATE),
                             note="A$55.00 is the TOTAL back from Medicare: consult A$32.95 + lab test A$16.95 + collection A$5.10. The consult alone is A$32.95.")

# ---- T2: midwives 08:00 to 16:00 ----
ONSITE_H, BREAK_H = 8.0, 0.5
PAID_DAY = ONSITE_H - BREAK_H                                        # 7.5 (E: 30 minute unpaid meal break)
SLOTS_DAY_CAP = PAID_DAY * 60 / 20                                   # 22.5 slots of 20 minutes
GTT_DAY = N / r18.DAYS_M                                             # 18.0
SPARE_SLOTS_DAY = math.floor(SLOTS_DAY_CAP - GTT_DAY + 1e-9)         # 4 whole slots (10 minutes left over)
SPARE_SLOTS_MONTH = SPARE_SLOTS_DAY * r18.DAYS_M                     # 105.32
mw = None
with patched(CONSULT_NEW, 45.0):
    mw = r18.midwife("leave_covered_1.366")
FORT_PER_MONTH = r14.WEEKS_M / 2                                     # fortnights per month (2.1667)
roster = dict(on_site_hours_per_shift=ONSITE_H, unpaid_break_h=BREAK_H, paid_hours_per_shift=PAID_DAY, shifts_per_midwife_per_fortnight=6,
              on_site_h_per_midwife_fortnight=6 * ONSITE_H, paid_h_per_midwife_fortnight=6 * PAID_DAY, paid_h_per_midwife_week=3 * PAID_DAY,
              paid_h_both_midwives_week=6 * PAID_DAY, wage_cost_per_midwife_per_fortnight_loaded=f2(-LOCK["midwife_wages"] / FORT_PER_MONTH / 2),
              wage_cost_both_per_month=-LOCK["midwife_wages"], fixed_and_consumables_month=-LOCK["midwife_fixed_consumables"], oncost=round(r15.bu_worked, 4),
              blended_hourly_before_oncost=f2(r18.RATE_BLEND), slots_per_day_capacity=SLOTS_DAY_CAP, gtt_consults_per_day=round(GTT_DAY, 2),
              gtt_consult_hours_day=round(GTT_DAY * 20 / 60, 2), utilisation_by_gtt=round(GTT_DAY * 20 / 60 / PAID_DAY, 3),
              spare_slots_day=SPARE_SLOTS_DAY, spare_minutes_left_over=int(round((SLOTS_DAY_CAP - GTT_DAY - SPARE_SLOTS_DAY) * 20)), spare_slots_month=round(SPARE_SLOTS_MONTH, 2))
out["T2_roster"] = roster
SENS = {"grace_1.20_basis": v20(basis="grace_1.20"), "paid_8h_shift_no_unpaid_break_48h_week": v20(mw_hours=48.0)}
out["T2_sensitivity_LABELLED"] = {k: dict(midwife_wages=v["midwife_wages"], payroll_tax=v["payroll_tax_group"], before_tax=v["profit_before_company_tax"], after_tax=v["profit_after_company_tax"],
                                          change_after_vs_headline=f2(v["profit_after_company_tax"] - AFTER)) for k, v in SENS.items()}
ptax_per_extra_h = f2((LOCK["payroll_tax_group"] - SENS["paid_8h_shift_no_unpaid_break_48h_week"]["payroll_tax_group"]) / (48.0 - 45.0) / r14.WEEKS_M)
out["T2_payroll_tax"] = dict(headline_hours_change_vs_0900_roster="none (still 45 paid h a week)", group_taxable_wages_year=LOCK["payroll_taxable_wages_year"],
    over_threshold_by=LOCK["over_threshold_by"], payroll_tax_month=-LOCK["payroll_tax_group"], standalone_consults_add_payroll_tax="none while they fit inside the 45 paid hours (no new wages)",
    payroll_tax_per_extra_paid_midwife_hour_incl_oncost_wage_E=ptax_per_extra_h)

# standalone private consults (UPSIDE ONLY)
CONS_COST = r14.COST["base"]["consum"]                                # A$3.00 a consult (E)
def standalone(per_week, label):
    k = min(per_week * r14.WEEKS_M, SPARE_SLOTS_MONTH); takeup = k / SPARE_SLOTS_MONTH
    rev, card, cons = k * CONSULT_NEW, k * fee(CONSULT_NEW), k * CONS_COST
    before = rev - card - cons
    tax = before * TAX
    return dict(label=label, consults_week=round(k / r14.WEEKS_M, 1), share_of_spare_slots=round(takeup, 3), consults_month=round(k, 1), consults_day=round(k / r18.DAYS_M, 2), gross=f2(rev), card_fees=-f2(card), consumables=-f2(cons),
                midwife_wages_added=0.0, payroll_tax_added=0.0, before_tax=f2(before), company_tax=-f2(tax), after_tax=f2(before - tax),
                gst_on_sale=0.0, client_out_of_pocket=f2(CONSULT_NEW - REBATE_CONSULT))
TAKEUPS = [(5, "low (Reed: 5 a week, assumption)"), (12, "middle (Reed: 12 a week, assumption)"), (999, "high (Reed: full spare capacity, about 24 a week, assumption)")]
READ_REED = os.path.join(HERE, "REED-R20.md")
out["T2_reed_file_present"] = os.path.isfile(READ_REED)
out["T2_standalone_upside"] = [standalone(t, l) for t, l in TAKEUPS]
out["T2_with_upside_after_tax"] = [dict(label=s["label"], headline_after_tax=AFTER, upside_after_tax=s["after_tax"], total_after_tax=f2(AFTER + s["after_tax"])) for s in out["T2_standalone_upside"]]
out["T2_one_consult"] = dict(price=CONSULT_NEW, gst=0.0, card_fee=f2(fee(CONSULT_NEW)), consumables=CONS_COST, kept_before_tax=f2(CONSULT_NEW - fee(CONSULT_NEW) - CONS_COST),
                             client_gets_back=REBATE_CONSULT, client_nets=f2(CONSULT_NEW - REBATE_CONSULT))

# ---- T3 market: filled after reading REED-R20.md (prices typed into the md by hand) ----
out["T3_market"] = dict(gtt_standalone=CONSULT_NEW, client_nets=f2(CONSULT_NEW - REBATE_CONSULT), see="THEODORE-R20.md section 3 (Reed range)")

# ---- T4 afternoon sales per morning client ----
out["T4_afternoon"] = dict(afternoon_ex_gst=LOCK["rev_pm_ex_gst"], afternoon_card_fees=PM_CARD, afternoon_net=f2(LOCK["rev_pm_ex_gst"] - PM_CARD), morning_clients=N,
    per_morning_client=pc(LOCK["rev_pm_ex_gst"] - PM_CARD), pm_tx_month=round(PM_TX, 2), pm_weekday_tx_day=PM_WD, pm_saturday_tx_day=PM_SAT, pm_price_incl_gst=PM_PRICE,
    pm_revenue_incl_gst=r18.REV["pm_revenue"], changes_with_consult_rise=False)

# ---- T5 prepaid money and interest (GTT's own money only; lab fee never held) ----
DAYS_HELD = 21                                                        # E: R18 assumption, booking to visit. No repo data on booking lead time
def float_bal(days, per_client=R1["gtt_receives_incl_gst"]): return per_client * N / 30.4 * days
HELD = f2(float_bal(DAYS_HELD))
daily_in = R1["gtt_receives_incl_gst"] * N / 30.4
RATES = [("RBA cash rate 4.60% (V, a reference rate, not a bank product)", 0.046, "V"), ("5.00% 3-month business term deposit (Aspire, July 2026, secondary)", 0.05, "U"),
         ("4.30% CommBank 3-month business term deposit (Aspire, July 2026, before the September rise)", 0.043, "U"), ("1.00% big-bank business saver (page did not load)", 0.01, "U")]
# first 12 months from opening day: balance builds linearly for 21 days then stays level
first_year_factor = 1 - DAYS_HELD / (2 * 365)
out["T5_interest"] = dict(per_client_held=R1["gtt_receives_incl_gst"], lab_fee_held=0.0, clients_month=N, new_money_in_per_month=f2(R1["gtt_receives_incl_gst"] * N),
    days_held=DAYS_HELD, average_standing_balance=HELD, first_year_factor=round(first_year_factor, 4),
    sens_balance_by_days_held={str(d): f2(float_bal(d)) for d in (7, 14, 21, 28)},
    rates=[dict(name=n, rate=r, status=s, interest_year_steady=f2(HELD * r), interest_first_12_months=f2(HELD * r * first_year_factor), interest_per_month_steady=f2(HELD * r / 12),
                after_25pct_company_tax_first_12m=f2(HELD * r * first_year_factor * 0.75)) for n, r, s in RATES],
    extra_float_from_consult_rise=f2(20 * N / 30.4 * DAYS_HELD),
    wrong_multiplication_if_balance_times_12=f2(HELD * 12), note="in the steady state the balance is replaced, not added to: money in each month equals money out each month")

# ---- T6 refund maths for the 50 percent lounge policy ----
def refund_case(lounge, pct=0.5):
    gross = lounge * pct
    gst_back = gross / 11
    ex = gross - gst_back
    orig_fee_not_returned = fee(lounge)       # fee share on the lounge part of the first payment (E: processors do not return the original fee)
    second_fee = fee(lounge)
    return dict(lounge_paid=lounge, refund_pct=pct, refund_to_client=f2(gross), gst_adjustment_back_from_ato=f2(gst_back), refund_net_of_gst=f2(ex),
                refund_net_of_gst_and_company_tax=f2(ex * 0.75), gtt_keeps_if_never_rebooks=f2(lounge - gross), gtt_keeps_if_never_rebooks_ex_gst=f2((lounge - gross) * 10 / 11),
                rebook_second_payment=lounge, second_card_fee=f2(second_fee), gtt_lounge_takings_if_rebooks_and_attends=f2(lounge - gross + lounge),
                of_which_ex_gst=f2((lounge - gross + lounge) * 10 / 11), extra_vs_one_normal_lounge=f2(-gross + lounge) , extra_card_fee_from_second_payment=f2(second_fee))
out["T6_refund"] = dict(p1=refund_case(LOUNGE_P1), p2=refund_case(LOUNGE_P2),
    ladder_p1=[{**refund_case(LOUNGE_P1, p), "pct": p} for p in (0.0, 0.25, 0.5, 0.75, 1.0)],
    consult_kept=CONSULT_NEW, consult_not_refunded=True,
    month_if_no_show_rate=[dict(rate=r, cases=round(N * r, 2), refunds_gross=f2(N * r * LOUNGE_P1 * 0.5), refunds_net_of_gst_and_tax=f2(N * r * LOUNGE_P1 * 0.5 / 1.1 * 0.75)) for r in (0.01, 0.03, 0.05, 0.10)],
    note="No-show rates are illustrations; there is no repo data on no-shows.")

# ---- break-even and cash-flow deltas ----
out["T7_effects"] = dict(extra_kept_per_client_before_tax=f2(20 * (1 - 0.017)), extra_kept_month_before_tax=f2(N * 20 * (1 - 0.017)),
    extra_float=out["T5_interest"]["extra_float_from_consult_rise"], gst_change_on_consult_rise=0.0, break_even_rerun=False,
    note_break_even="The break-even level needs the repo break-even and cash-flow models re-run with the new prices. Not re-run this round. Direction: each client now keeps about A$19.66 more before tax, so break-even moves in the safe direction.")

# ---- banned stale values ----
BANNED = [
 ("A$110", "Old consult price. The consult is A$130 (GST-free), inside packages and standalone"),
 ("A$300 / A$350", "Old package prices. Full advertised price is A$320 (Package 1) / A$370 (Package 2). Do not use as the GTT charge"),
 ("A$272.15 / A$322.15", "Old GTT-charge figures. The client pays GTT A$292.15 (P1) / A$342.15 (P2); the lab fee A$27.85 is paid to the lab"),
 ("A$245 / A$295", "Old out-of-pocket figures. After the A$55 rebate the client's cost is A$265 (P1) / A$315 (P2), lab fee included"),
 ("A$17,314.31 / A$12,985.73", "Older headline profit figures, retired"),
 ("A$25,769.40 / A$19,327.05", "Older option figures, retired"),
 ("A$35,186.40", "Repo master figure on a different basis (no GST, card fees, payroll tax or company tax). Do not compare to the headline"),
 ("A$21,971 / A$19,334.04", "Older baseline figures, retired"),
 ("A$99.40", "A$99.40 rebate: that is a 40-minute consult (82110). The 20-minute consult is 82105; consult rebate A$32.95; total rebate A$55.00"),
 ("A$222.15", "Old example. GTT receives A$292.15 (P1) / A$342.15 (P2)"),
 ("A$338", "Retired break-even"),
 ("A$345.38 / A$308.13", "Retired break-even prices"),
 ("hosts", "No hosts. The venue manager does reception and welcome"),
 ("venue manager starting 07:00", "Venue manager starts 06:30 (07:00 is the first draw)"),
 ("lounge + consult", "Say 'consult + lounge + service'"),
 ("two consult rooms", "One consult room"),
 ("Midwife A/B alternating days", "Fortnightly block: Mon-Wed / Thu-Sat, swap each fortnight"),
 ("lab money through GTT", "Lab A$27.85 is paid by the client straight to the lab"),
 ("A$201 / A$251 / A$200.60 / A$250.60", "Out of pocket is A$265 (P1) / A$315 (P2) after the A$55 rebate"),
 ("A$18,526", "Older headline, superseded"),
 ("A$13,346 / A$17,795", "Older headlines, superseded"),
 ("48.6 h midwife", "Midwife paid hours are 45 a week on the approved roster"),
 ("A$12,166.54", "Receptionist/host add-on, removed"),
 ("396 clients", "Volume is 473.94 morning clients a month"),
 ("consult after the test", "The consult is 1 to 28 days BEFORE the test, or the same morning before the test"),
 ("40-minute consult", "Consult is 20 minutes"),
 ("no same-day consult", "Same-day consult is allowed: the client books the test, then books the consult, and may book it on test morning"),
 ("midwife 09:00", "Midwives work 08:00 to 16:00"),
]
BANNED_RX = [
 (r"A\$110(?![\d,]*\d)", BANNED[0][1]), (r"A\$300(?![\d,]*\d)|A\$350(?![\d,]*\d)", BANNED[1][1]),
 (r"A\$272\.15|A\$322\.15", BANNED[2][1]), (r"A\$245(?![\d,]*\d)|A\$295(?![\d,]*\d)", BANNED[3][1]),
 (r"A\$17,314\.31|A\$12,985\.73", BANNED[4][1]), (r"A\$25,769\.40|A\$19,327\.05", BANNED[5][1]), (r"A\$35,186\.40", BANNED[6][1]),
 (r"A\$21,971|A\$19,334\.04", BANNED[7][1]), (r"A\$99\.40", BANNED[8][1]), (r"A\$222\.15", BANNED[9][1]),
 (r"A\$338(?![.,\d])", BANNED[10][1]), (r"A\$345\.38|A\$308\.13", BANNED[11][1]),
 (r"(?<!no )\bhosts?\b(?!\s*\|\s*none)", BANNED[12][1]), (r"venue manager (starts|start|from|arrives|at|begins)[^.\n|]{0,10}07:00", BANNED[13][1]),
 (r"lounge \+ consult|lounge and consult", BANNED[14][1]), (r"two consult rooms|2 consult rooms", BANNED[15][1]),
 (r"alternating days|alternate days|A and B alternating", BANNED[16][1]), (r"lab (money|fee|price)[^.\n]{0,40}through GTT|GTT (collects|holds) the lab", BANNED[17][1]),
 (r"A\$201\b|A\$251\b|A\$200\.60|A\$250\.60", BANNED[18][1]), (r"A\$18,526|A\$18,525\.98", BANNED[19][1]), (r"A\$13,346|A\$17,795", BANNED[20][1]),
 (r"48\.6 h", BANNED[21][1]), (r"A\$12,166\.54", BANNED[22][1]), (r"\b396 clients", BANNED[23][1]), (r"consult[^.\n]{0,40}after the (test|draw)", BANNED[24][1]),
 (r"40[- ]minute consult", BANNED[25][1]), (r"no same-day consult|same-day consult (is )?blocked", BANNED[26][1]), (r"midwife[^.\n]{0,15}09:00", BANNED[27][1])]
assert len(BANNED) == len(BANNED_RX)
SKIP_HEAD = re.compile(r"banned|error|root cause|why mistakes|change log|stale", re.I)
def fact_check(path):
    hits, skip = [], False
    for i, line in enumerate(open(path, encoding="utf-8"), 1):
        if line.startswith("#"):
            skip = bool(SKIP_HEAD.search(line))
        if skip or "[stale-ok]" in line:
            continue
        if "—" in line:
            hits.append((i, "", "em dash", line.strip()[:120]))
        for pat, why in BANNED_RX:
            if re.search(pat, line, re.I):
                hits.append((i, pat, why, line.strip()[:120]))
    return hits

# ---- write the centre of truth ----
def money(x): return f"A${x:,.2f}" if x >= 0 else f"-A${-x:,.2f}"
def build_centre():
    L = LOCK
    yml = {"generated_by": "docs/overhaul-2026-10-26/L15-r20/theodore_r20.py", "date": "2026-10-26", "currency": "AUD",
           "prices": {"package_1_full": P1, "package_2_full": P2, "plan_mix_p1": 1.0, "consult_gst_free": CONSULT_NEW, "lab_paid_to_lab_not_gtt": LAB,
                      "lounge_service_p1_taxable": LOUNGE_P1, "lounge_service_p2_taxable": LOUNGE_P2,
                      "client_pays_gtt_p1": R1["gtt_receives_incl_gst"], "client_pays_gtt_p2": R2["gtt_receives_incl_gst"], "pm_average_incl_gst": PM_PRICE},
           "medicare": {"consult_item": "82105", "consult_rebate": REBATE_CONSULT, "test_item": "66548", "test_rebate": REBATE_TEST,
                        "collection_item": "73928 (AskMBS to confirm vs 73938)", "collection_rebate": REBATE_COLL, "lab_rebate": LAB_REBATE, "total_rebate": REBATE,
                        "out_of_pocket_p1": f2(P1 - REBATE), "out_of_pocket_p2": f2(P2 - REBATE), "standalone_consult_out_of_pocket": f2(CONSULT_NEW - REBATE_CONSULT)},
           "volumes": {"am_clients_day": 18, "am_clients_month": N, "pm_transactions_month": round(PM_TX, 2)},
           "midwives": {"hours": "08:00 to 16:00", "paid_h_per_shift": PAID_DAY, "paid_h_week_both": 45.0, "block": "fortnightly Mon-Wed / Thu-Sat", "oncost": round(r15.bu_worked, 4),
                        "spare_slots_day": SPARE_SLOTS_DAY, "standalone_consults": "upside only, not in headline"},
           "headline": {"profit_before_company_tax": BEFORE, "company_tax": L["company_tax_25"], "net_after_all": AFTER, "threshold": TARGET, "above_threshold": AFTER > TARGET}}
    with open(os.path.join(HERE, "center_of_truth.yml"), "w", encoding="ascii", errors="replace") as fh:
        yaml.safe_dump(yml, fh, sort_keys=False, allow_unicode=False, width=200)
    yaml.safe_load(open(os.path.join(HERE, "center_of_truth.yml"), encoding="ascii"))
    rows = [("Lounge + service, morning, ex GST (474 x A$147.41)", L["rev_lounge_service_am_ex_gst"], "R volume, E split"),
            ("Afternoon sales, ex GST (repo A$24,585.37 / 1.1)", L["rev_pm_ex_gst"], "R"),
            (f"Consult, GST-free (474 x A$130, Medical)", L["rev_consult_gst_free"], "E"),
            ("**Revenue, ex GST**", L["revenue_total_ex_gst"], ""),
            ("Repo staff (8 AM service, 2 phlebotomists, 4 PM, venue manager 07:00), super, workers comp", L["repo_payroll"], "R"),
            ("Repo running costs (rent, insurance, overheads, supplies)", L["repo_operating_expenses"], "R"),
            ("GST credits on costs", L["less_gst_credits"], "R"),
            ("Card fees, morning (on A$292.15)", L["card_fees"], "E"),
            ("Card fees, afternoon (210.13 x A$117)", L["card_fees_pm"], "E"),
            ("Midwife wages (45 paid h a week, on-cost 1.366, casual leave cover inside)", L["midwife_wages"], "E"),
            ("Midwife fixed costs and consumables (one consult room)", L["midwife_fixed_consumables"], "E"),
            ("Venue manager 06:30 start", L["venue_manager_0630"], "R rate"),
            ("WA payroll tax, whole group", L["payroll_tax_group"], "E"),
            ("Three-company running cost", L["three_company"], "E"),
            ("**Profit before company tax**", BEFORE, ""), ("Company tax 25%", L["company_tax_25"], "E"),
            ("**Net profit after GST, card fees, payroll tax and company tax (franked dividend available)**", AFTER, "")]
    md = ["# GTT Center Perth: Financial Center of Truth", "",
          "**One place for every money variable.** Generated by [theodore_r20.py](overhaul-2026-10-26/L15-r20/theodore_r20.py); do not edit by hand. Re-run the script after any decision change and this file and "
          "[center_of_truth.yml](overhaul-2026-10-26/L15-r20/center_of_truth.yml) regenerate together. All amounts AUD a month unless stated. "
          "General knowledge and desk research, not your personal documents. Verify before acting.", "",
          "Tags: **R** repo figure, **V** official source, **E** estimate, **Q** quote needed, **U** unverified.", "",
          "## 1. Prices and money flow (Structure B, Round 20 decisions)", "",
          "| Item | Package 1 | Package 2 | GST | Who receives it | Tag |", "|---|---|---|---|---|---|",
          f"| Full advertised price (includes the lab fee) | {money(P1)} | {money(P2)} | inside | | Locked |",
          f"| Lab test | A${LAB} | A${LAB} | GST-free | The lab, paid by the client directly. Never GTT money | Locked |",
          f"| Consult (20 min, item 82105) | {money(CONSULT_NEW)} | {money(CONSULT_NEW)} | GST-free | Medical | Locked |",
          f"| Lounge + service | {money(LOUNGE_P1)} | {money(LOUNGE_P2)} | taxable, 1/11 is GST | Lounge | Locked |",
          f"| **Client pays GTT at checkout** | **{money(R1['gtt_receives_incl_gst'])}** | **{money(R2['gtt_receives_incl_gst'])}** | | Medical + Lounge | R maths |",
          f"| Reaches GTT, ex GST | {money(R1['gtt_receives_ex_gst'])} | {money(R2['gtt_receives_ex_gst'])} | | | R maths |",
          f"| Medicare back to the client: consult {money(REBATE_CONSULT)} (82105) + lab test {money(REBATE_TEST)} (66548) + collection {money(REBATE_COLL)} (73928) | {money(REBATE)} | {money(REBATE)} | | The client, from Medicare | V |",
          f"| **Client's own cost after Medicare (lab fee included)** | **{money(P1 - REBATE)}** | **{money(P2 - REBATE)}** | | | V |",
          f"| Standalone private consult | {money(CONSULT_NEW)} | | GST-free | Medical. Client gets {money(REBATE_CONSULT)} back, so nets {money(CONSULT_NEW - REBATE_CONSULT)} | Locked |", "",
          "The A$55.00 Medicare amount is the TOTAL for the consult plus the lab. The consult alone is A$32.95. Rebates follow the Medicare schedule fee, so they do not rise with the consult price. "
          "Booking order: the client books the test, then books the consult. The consult is 1 to 28 days before the test, or the same morning before the test. The booking page warns the client to stay fasted if she has the test straight after. "
          "Checkout shows the full price but charges only the GTT amount. Medical pays Lounge a flat market room fee (inside the group, no profit effect). Plan: 100% Package 1. Afternoon pricing: not changed, to be figured out in time.", "",
          "## 2. Volumes, staffing and hours (checked against the repo by the script)", "",
          "| Variable | Value | Source |", "|---|---|---|",
          f"| Morning clients | 18 a day, Mon-Sat = {N} a month | R (revenue_ramp.yml, 22 + 4.33 days) |",
          f"| Afternoon transactions | {PM_TX:.2f} a month (8.70 weekday, 4.35 Saturday a day) at A$117 = A$24,585.37 | R (revenue_assumptions.yml, Model E) |",
          "| AM service staff | 8 (4 massage and beauty, 2 nails, 2 hair), 6 h, 07:00-13:00 | R |",
          "| Phlebotomists | 2 at 10-18 booked, 1 at 9 or fewer, none PM | R |",
          "| PM service staff | 4 casual, 3-hour floor | R |",
          "| Venue manager | Mon-Fri 06:30-15:00 (repo 07:00 + 0.5 h added, A$500.28 loaded) | R rate, locked time |",
          "| Hosts | none | Locked |",
          f"| Midwives | 08:00 to 16:00 (8 h on site, 7.5 h paid after a 30 minute unpaid break E). 2 permanent part-time, 22.5 paid h a week each (45 paid h a fortnight each), fortnightly block Mon-Wed / Thu-Sat, + 1 casual for leave | Locked |",
          f"| Midwife time | 18 GTT consults x 20 min = 6.0 h a day; 7.5 h paid; {SPARE_SLOTS_DAY} spare 20-minute slots a day ({SPARE_SLOTS_MONTH:.1f} a month) for standalone private consults | maths |",
          "| Consult rooms / collection rooms | 1 / 2 (one chair each) | Locked |", "",
          "## 3. Rates and tax", "",
          "| Variable | Value | Tag |", "|---|---|---|",
          f"| Midwife rate | Nurses Award RN L2 pp4 A$41.59 weekday, 150% Saturday; blended A${r18.RATE_BLEND:.2f} | E |",
          f"| Midwife on-cost (used) | {r15.bu_worked:.3f}: super 12%, workers comp 1.7%, leave loading, paid leave covered by the casual | E |",
          "| Midwife on-cost (sensitivity only) | 1.20 (no leave cover) | E |",
          "| Card fee | 1.7% + A$0.30 a transaction on all card takings, AM and PM, on the full A$292.15 (repo lists Tyro 1.4% / Square 1.6%, provider not chosen) | E |",
          "| WA payroll tax | 5.5% above the A$1m grouped threshold (tapering deduction) | E, check RevenueWA |",
          "| Company tax | 25% (base rate entity), one consolidated return; franked dividends direct to Anthony and partner (Route B) | E |", "",
          "## 4. Monthly P&L, whole venture (Holdings + Medical + Lounge), locked case, GTT clients only", "",
          "| Line | Monthly | Tag |", "|---|---|---|"] + [f"| {k} | {money(v)} | {t} |" for k, v, t in rows] + [
          "", f"GST passed to the ATO (not revenue): morning {money(L['gst_collected_am'])}, afternoon {money(L['gst_collected_pm'])}. Target: net profit above A$20,000 a month after all of the above. "
          f"Result: {money(AFTER)} ({'above' if AFTER > TARGET else 'below'} by {money(abs(AFTER - TARGET))}). Standalone private consults are upside and are NOT in this P&L.", "",
          "## 5. Per-client waterfall (Package 1, A$320 full price)", "", "| Step | A$ per client |", "|---|---|"] + [f"| {k} | {money(v)} |" for k, v in wf] + [
          "", f"The client then gets A$55.00 back from Medicare, so her own cost is {money(P1 - REBATE)} ({money(P2 - REBATE)} on Package 2), lab fee included.", "",
          "## 6. Not in the P&L (known, flagged)", "", "| Item | Status |", "|---|---|",
          "| 10% post-test discount (adopted 2026-10-17) | Repo estimate -A$1,386.27 a month at 25% take-up; not deducted (R) |",
          "| Standalone private consults | Upside only; see THEODORE-R20.md section 2 |",
          "| Interest on prepaid money | Upside only; see THEODORE-R20.md section 5 |",
          "| Senior cover loading (afternoon gap, Saturday) | Not in repo |",
          "| 50 percent lounge refund policy | Cost per case in THEODORE-R20.md section 6; not deducted |",
          "| Collection item 73928 vs 73938 | AskMBS to confirm; changes the lab's price and rebate by A$1.70, not GTT's revenue |", "",
          "## 7. Banned stale values (pre-send fact check)", "",
          "Run `python tools/factcheck_locked_facts.py <file>` before anything goes to Anthony. The first column is what the checker bans.", "",
          "| Banned | Correct |", "|---|---|"] + [f"| {b} | {w} |" for b, w in BANNED] + [
          "", "## 8. Change log", "", "| Date | Change | By |", "|---|---|---|",
          f"| 2026-10-26 | Round 20: consult A$130 inside packages and standalone, midwives 08:00 to 16:00, same-day consult, terminology client; headline {money(BEFORE)} before and {money(AFTER)} after company tax | Theodore R20 |", ""]
    with open(os.path.join(REPO, "docs", "FINANCIAL-CENTER-OF-TRUTH.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(md))

if __name__ == "__main__" and len(sys.argv) > 2 and sys.argv[1] == "--check":
    hits = fact_check(sys.argv[2])
    for h in hits: print(f"line {h[0]}: {h[2]}  ->  {h[3]}")
    print(f"fact_check: {len(hits)} banned value(s) found"); sys.exit(1 if hits else 0)

build_centre()
json.dump(out, open(os.path.join(HERE, "theodore_r20_results.json"), "w"), indent=1, default=str)
if __name__ == "__main__":
    for k in ("T1_headline", "T1_card_fee_rate_check", "T2_roster", "T2_sensitivity_LABELLED", "T2_payroll_tax", "T2_one_consult", "T4_afternoon", "T7_effects"):
        print(k, json.dumps(out[k], indent=1, default=str))
    for k, v in wf: print(f"{v:>10.2f}  {k}")
    for s in out["T2_standalone_upside"]: print(s)
    print(json.dumps(out["T5_interest"], indent=1)); print(json.dumps(out["T6_refund"], indent=1))
    print("reed present", out["T2_reed_file_present"])
    print("centre check hits:", len(fact_check(os.path.join(REPO, "docs", "FINANCIAL-CENTER-OF-TRUTH.md"))))
