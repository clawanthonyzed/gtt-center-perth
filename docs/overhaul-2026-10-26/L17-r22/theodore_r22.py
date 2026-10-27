"""Theodore R22 (2026-10-26) = R21 engine + Round 22 additions at the bottom (Path B, shared-cost block, VM sensitivity, Center of Truth writer). Older docstring follows.
Theodore R20 (2026-10-26). Copy of the R19 structure, EXTENDED. Engine is unchanged and imported, never re-written:
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


# =====================  ROUND 21  =====================
# R21 extends this copied R20 engine: Medicare validation, segmented P&L, option A (outside referral), 30 minute listing.
# The R20 centre-of-truth writer was removed from this copy; nothing here rewrites docs/FINANCIAL-CENTER-OF-TRUTH.md.
def pct5(x):                       # Medicare rounding: benefit rounded UP to the next 5 cents (checked against the official pages)
    return round(math.ceil(round(x * 100 / 5, 6)) * 5 / 100, 2)
ITEMS = {"82105": 38.75, "66548": 19.90, "73928": 5.95, "73938": 7.95}
OFFICIAL85 = {"82105": 32.95, "66548": 16.95, "73928": 5.10, "73938": 6.80}
for k, fee_ in ITEMS.items():
    assert pct5(fee_ * 0.85) == OFFICIAL85[k], k
out["R21_J1_items"] = {k: dict(fee=ITEMS[k], exact85=round(ITEMS[k] * .85, 4), benefit85=pct5(ITEMS[k] * .85)) for k in ITEMS}
assert f2(ITEMS["66548"] + ITEMS["73938"]) == LAB and f2(ITEMS["66548"] + ITEMS["73928"]) != LAB
def medicare_case(coll, lab_fee):
    lab_rebate = f2(OFFICIAL85["66548"] + OFFICIAL85[coll]); tot = f2(OFFICIAL85["82105"] + lab_rebate)
    return dict(collection_item=coll, lab_fee=lab_fee, lab_rebate=lab_rebate, total_rebate=tot, lab_cost_after=f2(lab_fee - lab_rebate),
                p1_all_in=f2(LOUNGE_P1 + CONSULT_NEW + lab_fee), p1_after_medicare=f2(LOUNGE_P1 + CONSULT_NEW + lab_fee - tot),
                p2_all_in=f2(LOUNGE_P2 + CONSULT_NEW + lab_fee), p2_after_medicare=f2(LOUNGE_P2 + CONSULT_NEW + lab_fee - tot))
out["R21_J1_cases"] = {"repo_today_73928_rebate_but_27.85_lab": medicare_case("73928", 27.85),
                       "A_73938_applies": medicare_case("73938", 27.85),
                       "B_73928_applies_lab_charges_schedule_fees": medicare_case("73928", f2(ITEMS["66548"] + ITEMS["73928"]))}

# ---- JOB 2: segments (all figures from LOCK / pb, the R20 locked case) ----
L = LOCK
load = (pb["superannuation"] + pb["workers_comp"]) / pb["direct_labor_and_opening_total"]
lab_am = (pb["am_weekday_direct_labor"] + pb["am_saturday_direct_labor"]) * (1 + load)
lab_pm = (pb["pm_weekday_direct_labor"] + pb["pm_saturday_direct_labor"]) * (1 + load)
vm_loaded = pb["opening_time_increment"] * (1 + load)
assert abs(lab_am + lab_pm + vm_loaded - abs(L["repo_payroll"])) < 0.05, "payroll split"
share_c = R1["consult_medical_gst_free"] / R1["gtt_receives_incl_gst"]
card_am = -L["card_fees"]; card_pm = -L["card_fees_pm"]
card_consult, card_lounge = card_am * share_c, card_am * (1 - share_c)
seg = {}
seg["consult"] = dict(revenue=L["rev_consult_gst_free"], direct=dict(midwife_wages=-L["midwife_wages"], midwife_fixed_consumables=-L["midwife_fixed_consumables"], card_fee_share=card_consult))
seg["lounge_am"] = dict(revenue=L["rev_lounge_service_am_ex_gst"], direct=dict(treatment_staff_and_phlebotomists_with_super_wc=lab_am, card_fee_share=card_lounge))
seg["afternoon"] = dict(revenue=L["rev_pm_ex_gst"], direct=dict(pm_staff_with_super_wc=lab_pm, card_fee=card_pm))
shared = dict(venue_manager_0700_with_super_wc=vm_loaded, venue_manager_0630_extra=-L["venue_manager_0630"],
              rent_insurance_overheads_supplies_net_of_gst_credits=-L["repo_operating_expenses"] - L["less_gst_credits"],
              wa_payroll_tax_group=-L["payroll_tax_group"], three_company_running_cost=-L["three_company"])
SH = sum(shared.values())
RT = sum(v["revenue"] for v in seg.values())
for k, v in seg.items():
    v["direct_total"] = sum(v["direct"].values()); v["profit_before_shared"] = v["revenue"] - v["direct_total"]
    v["shared_alloc_by_revenue"] = SH * v["revenue"] / RT; v["profit_after_shared"] = v["profit_before_shared"] - v["shared_alloc_by_revenue"]
recon = sum(v["profit_after_shared"] for v in seg.values())
assert abs(recon - BEFORE) < 0.05, (recon, BEFORE)
out["R21_J2_segments"] = seg; out["R21_J2_shared"] = dict(items=shared, total=SH, rule="split across consult, lounge and afternoon by share of revenue ex GST", revenue_shares={k: v["revenue"] / RT for k, v in seg.items()})
out["R21_J2_recon"] = dict(sum_segments=recon, headline_before_tax=BEFORE, company_tax=L["company_tax_25"], net=AFTER, lab_pass_through_per_month=f2(N * LAB))
morn = seg["consult"]["profit_before_shared"] + seg["lounge_am"]["profit_before_shared"]
morn_sh = seg["consult"]["shared_alloc_by_revenue"] + seg["lounge_am"]["shared_alloc_by_revenue"]
out["R21_J2_morning_package"] = dict(before_shared=morn, shared_revenue_rule=morn_sh, after_shared_revenue_rule=morn - morn_sh,
                                     if_morning_carries_all_shared=morn - SH, afternoon_before_shared=seg["afternoon"]["profit_before_shared"])
pc2 = lambda x: f2(x / N)
out["R21_J2_per_client"] = {k: dict(revenue=pc2(seg[k]["revenue"]), direct=pc2(seg[k]["direct_total"]), before_shared=pc2(seg[k]["profit_before_shared"]),
                                    shared=pc2(seg[k]["shared_alloc_by_revenue"]), after_shared=pc2(seg[k]["profit_after_shared"])) for k in ("consult", "lounge_am")}
out["R21_J2_per_client"]["morning_package_both"] = dict(before_shared=pc2(morn), shared_revenue_rule=pc2(morn_sh), after_shared=pc2(morn - morn_sh))

# ---- JOB 3: option A (outside referral) ----
def optA(all_in):
    gtt = f2(all_in - LAB); gst = f2(gtt / 11); ex = f2(gtt - gst); card = f2(fee(gtt)); net = f2(ex - card)
    return dict(client_all_in=all_in, lab=LAB, gtt_receives_incl_gst=gtt, gst=gst, ex_gst=ex, card_fee=card, gtt_net_after_card=net)
A1, A2 = optA(265.0), optA(315.0)
mw_per_client = f2(-(L["midwife_wages"] + L["midwife_fixed_consumables"]) / N)
mw_var_only = CONS_COST
c1 = R1["gtt_ex_gst_after_card"]
out["R21_J3"] = dict(option_A_p1=A1, option_A_p2=A2, consult_route_gtt_receives=dict(p1=R1["gtt_receives_incl_gst"], p2=R2["gtt_receives_incl_gst"]),
    receives_shortfall_p1=f2(R1["gtt_receives_incl_gst"] - A1["gtt_receives_incl_gst"]), receives_shortfall_p2=f2(R2["gtt_receives_incl_gst"] - A2["gtt_receives_incl_gst"]),
    midwife_cost_per_client_if_roster_flexes=mw_per_client, midwife_consumables_only_if_roster_fixed=mw_var_only,
    consult_route_net_per_client_before_midwife=c1, consult_route_after_midwife_flex=f2(c1 - mw_per_client), consult_route_after_midwife_fixed=f2(c1 - mw_var_only),
    delta_A_vs_consult_flex=f2(A1["gtt_net_after_card"] - (c1 - mw_per_client)), delta_A_vs_consult_fixed=f2(A1["gtt_net_after_card"] - (c1 - mw_var_only)))
mix = []
for s in (0, .10, .20):
    for lab_, d in (("roster_flexes", out["R21_J3"]["delta_A_vs_consult_flex"]), ("roster_fixed", out["R21_J3"]["delta_A_vs_consult_fixed"])):
        b = BEFORE + s * N * d
        mix.append(dict(share_option_A=s, midwife_roster=lab_, clients_A=round(s * N, 1), before_tax=f2(b), company_tax=-f2(max(0, b) * TAX), net=f2(b - max(0, b) * TAX), vs_headline=f2(b - max(0, b) * TAX - AFTER)))
out["R21_J3_mix_LABELLED_ILLUSTRATION"] = mix

# ---- JOB 4: 30 minute listing ----
BLOCK, LISTED = 25, 30
out["R21_J4"] = dict(mins_needed_25=N / r18.DAYS_M * BLOCK, mins_needed_30=N / r18.DAYS_M * LISTED, paid_min_day=PAID_DAY * 60, on_site_min_day=ONSITE_H * 60,
    first_appt="08:15", last_end_25="15:45", last_end_30_if_18="17:15", consults_fit_30_in_paid=int(PAID_DAY * 60 // LISTED), consults_fit_25_in_paid=int(PAID_DAY * 60 // BLOCK))
v54 = v20(mw_hours=54.0)
out["R21_J4"].update(midwife_hours_week_if_30=54.0, profit_before_tax_at_54h=v54["profit_before_company_tax"],
                     cost_vs_headline_before_tax=f2(v54["profit_before_company_tax"] - BEFORE), net_at_54h=v54["profit_after_company_tax"], net_change=f2(v54["profit_after_company_tax"] - AFTER))


# =====================  ROUND 22  =====================
# Adds: Path B (outside referral, A$300/A$350 all in), one shared-cost block, venue manager sensitivity, rebate lock,
# and the Center of Truth writer (re-added; R21 had removed it). Path A = consult package (preferred), Path B = outside referral (not preferred).
VM_BASE_LOADED = f2(vm_loaded)                                   # repo base (07:00 start), with super and workers comp
VM_EXTRA = f2(-L["venue_manager_0630"])                          # the extra half hour
VM_COMBINED = f2(VM_BASE_LOADED + VM_EXTRA)
assert abs(VM_BASE_LOADED - 8004.48) < 0.01 and abs(VM_EXTRA - 500.28) < 0.01 and abs(VM_COMBINED - 8504.76) < 0.01, (VM_BASE_LOADED, VM_EXTRA)
out["R22_venue_manager"] = dict(start="06:30", hours="Mon-Fri 06:30 to 15:00", first_draw="07:00", repo_base_loaded=VM_BASE_LOADED, extra_half_hour=VM_EXTRA, combined_loaded_month=VM_COMBINED,
                                per_client=pc(VM_COMBINED))

# ---- JOB 1: rebate lock ----
out["R22_J1_rebate_lock"] = dict(consult=dict(item="82105", fee=38.75, rebate=REBATE_CONSULT, status="confirmed V"),
    lab_test=dict(item="66548", fee=19.90, rebate=REBATE_TEST, status="confirmed V"),
    collection=dict(item="73928", fee=5.95, rebate=REBATE_COLL, alt_item="73938", alt_fee=7.95, alt_rebate=6.80, status="unresolved, AskMBS later; GTT's own money does not change"),
    lab_rebate_locked=LAB_REBATE, total=REBATE, client_cost_pathA=dict(p1=f2(P1 - REBATE), p2=f2(P2 - REBATE)))
assert REBATE == 55.0 and LAB_REBATE == 22.05 and f2(P1 - REBATE) == 265.0 and f2(P2 - REBATE) == 315.0
assert abs(AFTER - 19973.98) < 0.005 and abs(BEFORE - 26631.97) < 0.005, (BEFORE, AFTER)
out["R22_J1_headline_check"] = dict(before_tax=BEFORE, after_tax=AFTER, unchanged=True)

# ---- JOB 2: Path B economics ----
GST_RATE = 1 / 11
def pathB(all_in):
    gtt = f2(all_in - LAB); gst = f2(gtt * GST_RATE); ex = f2(gtt - gst); card = f2(fee(gtt)); net = f2(ex - card)
    return dict(client_all_in=all_in, lab_to_lab=LAB, gtt_receives_incl_gst=gtt, gst_1_11=gst, ex_gst=ex, card_fee=card, gtt_net_after_card=net, whole_amount_taxable=True)
B1, B2 = pathB(300.0), pathB(350.0)
net_A = {"p1": R1["gtt_ex_gst_after_card"], "p2": R2["gtt_ex_gst_after_card"]}
mw_flex, mw_fixed = mw_per_client, mw_var_only
def vsA(B, key):
    a = net_A[key]
    return dict(pathA_net_before_midwife=a, pathA_after_midwife_flex=f2(a - mw_flex), pathA_after_midwife_fixed=f2(a - mw_fixed),
                pathB_net=B["gtt_net_after_card"], B_minus_A_flex=f2(B["gtt_net_after_card"] - (a - mw_flex)), B_minus_A_fixed=f2(B["gtt_net_after_card"] - (a - mw_fixed)))
out["R22_J2"] = dict(pathB_p1=B1, pathB_p2=B2, vs_pathA_p1=vsA(B1, "p1"), vs_pathA_p2=vsA(B2, "p2"),
                     midwife_cost_per_client_flex=mw_flex, midwife_consumables_only_fixed=mw_fixed,
                     pathA_gtt_receives=dict(p1=R1["gtt_receives_incl_gst"], p2=R2["gtt_receives_incl_gst"]),
                     gtt_receives_gap=dict(p1=f2(R1["gtt_receives_incl_gst"] - B1["gtt_receives_incl_gst"]), p2=f2(R2["gtt_receives_incl_gst"] - B2["gtt_receives_incl_gst"])))
def breakeven(target_net):
    g = (target_net + 0.30) / ((1 - GST_RATE) - 0.017)           # GTT-receives amount where net after GST and card equals target
    return dict(gtt_receives=f2(g), all_in_price=f2(g + LAB))
out["R22_J2_breakeven"] = {k: dict(vs_flex=breakeven(net_A[k] - mw_flex), vs_fixed=breakeven(net_A[k] - mw_fixed), vs_pathA_no_midwife_cost=breakeven(net_A[k])) for k in ("p1", "p2")}
for k, B in (("p1", B1), ("p2", B2)):
    be = out["R22_J2_breakeven"][k]
    be["selected_price_clears_flex"] = B["client_all_in"] >= be["vs_flex"]["all_in_price"]
    be["selected_price_clears_fixed"] = B["client_all_in"] >= be["vs_fixed"]["all_in_price"]
mixB = []
for sh in (0, .10, .20):
    for lab_, d in (("roster_flexes", out["R22_J2"]["vs_pathA_p1"]["B_minus_A_flex"]), ("roster_fixed", out["R22_J2"]["vs_pathA_p1"]["B_minus_A_fixed"])):
        b = BEFORE + sh * N * d
        mixB.append(dict(share_pathB=sh, midwife_roster=lab_, clients_B=round(sh * N, 1), before_tax=f2(b), company_tax=-f2(max(0, b) * TAX),
                         net=f2(b - max(0, b) * TAX), vs_headline=f2(b - max(0, b) * TAX - AFTER)))
out["R22_J2_mix_LABELLED_ILLUSTRATION"] = mixB

# ---- JOB 4: one shared-cost block ----
SH_ITEMS = dict(venue_manager_combined_0630_to_1500=VM_COMBINED,
                rent_insurance_overheads_supplies_net_of_gst_credits=f2(-L["repo_operating_expenses"] - L["less_gst_credits"]),
                wa_payroll_tax_group=f2(-L["payroll_tax_group"]), three_company_running_cost=f2(-L["three_company"]))
SH_TOTAL = f2(sum(SH_ITEMS.values()))
forms = dict(consult=seg["consult"]["profit_before_shared"], morning_lounge=seg["lounge_am"]["profit_before_shared"], lab=0.0, afternoon=seg["afternoon"]["profit_before_shared"])
FORMS_TOTAL = sum(forms.values())
assert abs(FORMS_TOTAL - SH_TOTAL - BEFORE) < 0.05, (FORMS_TOTAL, SH_TOTAL, BEFORE)
out["R22_J4"] = dict(forms_before_shared={k: f2(v) for k, v in forms.items()}, forms_total=f2(FORMS_TOTAL), shared_items=SH_ITEMS, shared_total=SH_TOTAL,
                     total_before_company_tax=BEFORE, company_tax=L["company_tax_25"], net=AFTER, lab_pass_through_month=f2(N * LAB),
                     consult_plus_morning_lounge_before_shared=f2(forms["consult"] + forms["morning_lounge"]),
                     per_client_before_shared={k: pc(v) for k, v in forms.items()})

# ---- JOB 5: venue manager at zero (sensitivity only) ----
vm_taxable_y = (r18.OPEN_INC + r18.VM_EXTRA_WAGES) * (1 + r15.SUPER) * 12
ptax_new = r14.ptax(L["payroll_taxable_wages_year"] - vm_taxable_y) / 12
ptax_saving = f2(-L["payroll_tax_group"] - ptax_new)
b_nosave = BEFORE + VM_COMBINED
b_save = BEFORE + VM_COMBINED + ptax_saving
out["R22_J5"] = dict(venue_manager_line=VM_COMBINED, applied=False, label="SENSITIVITY ONLY, not the headline",
    before_tax_payroll_tax_unchanged=f2(b_nosave), after_tax_payroll_tax_unchanged=f2(b_nosave * 0.75), change_after_vs_headline_unchanged=f2(b_nosave * 0.75 - AFTER),
    payroll_tax_saving_E=ptax_saving, before_tax_with_payroll_saving=f2(b_save), after_tax_with_payroll_saving=f2(b_save * 0.75), change_after_with_saving=f2(b_save * 0.75 - AFTER))

# ---- banned table for the Center of Truth (R22) ----
BANNED22 = [(b, w) for b, w in BANNED if b not in ("A$300 / A$350", "A$272.15 / A$322.15", "venue manager starting 07:00")] + [
 ("venue manager 07:00", "The venue manager starts 06:30 (Mon-Fri 06:30 to 15:00). 07:00 is the first draw. Combined loaded cost A$8,504.76 a month"),
 ("venue manager starting 07:00", "Venue manager starts 06:30 (07:00 is the first draw)"),
 ("Path A = outside referral", "Reversed label. Path A = consult package (preferred)"),
 ("Path B = consult package", "Reversed label. Path B = outside referral (not preferred)"),
 ("Path A (outside referral", "Reversed label. Path A = consult package (preferred)"),
 ("Path B (consult package", "Reversed label. Path B = outside referral (not preferred)")]
NOT_IN = [("Interest on prepaid money", "see THEODORE-R20.md section 5"), ("Standalone midwife consults", "upside only, see THEODORE-R20.md section 2"),
          ("Package 2 take-up", "plan is 100 percent Package 1"), ("Retail", "none in the plan"), ("Food and drink", "none in the plan"),
          ("Gap-filling services", "not planned"), ("Card quotes", "model uses 1.7% + A$0.30 (E) until a provider quotes"),
          ("Post-test discount (10 percent)", "repo estimate -A$1,386.27 a month at 25% take-up"), ("Health lawyer cost", "general knowledge about A$2,500 to A$8,000 fixed fee, not a quote")]

# =====================  ROUND 24 (2026-10-27)  =====================
# Anthony R24 lock: the 2 phlebotomists are employed by GTT MEDICAL, not the Lounge. Their wages, super and workers comp move
# from Lounge to Medical in the company split. Whole-venture totals must not move (asserted). Shared costs stay ONE block.
SAT_DAYS = pb["am_saturday_direct_labor"] / crm.AM_SATURDAY_DAILY_LABOR["scenario_table_1"]
assert abs(SAT_DAYS - 4.33) < 0.001, SAT_DAYS                      # Table 1 (18 a day) Saturday labour, 4.33 Saturdays a month (R)
PHLEB_SAT_DAY = 2 * 51.5625 * 6                                    # R: cost_ramp_model.py comment, 2 phlebotomists x A$51.5625/h x 6 h = A$618.75 a Saturday
PHLEB_WAGES = f2(crm.AM_WEEKDAY_PHLEBOTOMIST_MONTHLY + PHLEB_SAT_DAY * SAT_DAYS)   # A$9,075.00 weekday + Saturday
PHLEB_LOADED = PHLEB_WAGES * (1 + load)                            # same super + workers comp load the R21 segment split uses
assert pb["am_weekday_phlebotomist"] == crm.AM_WEEKDAY_PHLEBOTOMIST_MONTHLY == 9075.00
def company_split(phleb_in_medical):
    med_direct = dict(midwife_wages=-L["midwife_wages"], midwife_fixed_consumables=-L["midwife_fixed_consumables"], card_fee_share=card_consult)
    lng_direct = dict(am_service_staff_with_super_wc=lab_am - PHLEB_LOADED, am_card_fee_share=card_lounge, pm_staff_with_super_wc=lab_pm, pm_card_fee=card_pm)
    (med_direct if phleb_in_medical else lng_direct)["phlebotomists_with_super_wc"] = PHLEB_LOADED
    med = dict(revenue=L["rev_consult_gst_free"], direct=f2(sum(med_direct.values())), shared_block=0.0)
    lng = dict(revenue=f2(L["revenue_total_ex_gst"] - L["rev_consult_gst_free"]), shared_block=SH_TOTAL)
    med["before_shared"] = f2(med["revenue"] - med["direct"])
    lng["before_shared"] = f2(BEFORE + SH_TOTAL - med["before_shared"])          # Lounge carries the 1 cent rounding so the companies add to the locked headline
    assert abs(lng["before_shared"] - (L["rev_lounge_service_am_ex_gst"] + L["rev_pm_ex_gst"] - sum(lng_direct.values()))) < 0.02
    lng["direct"] = f2(lng["revenue"] - lng["before_shared"])
    for c in (med, lng):
        c["profit_before_tax"] = f2(c["before_shared"] - c["shared_block"])
        c["tax_25_if_taxed_alone"] = f2(max(0.0, c["profit_before_tax"]) * TAX)
    tot = dict(revenue=f2(med["revenue"] + lng["revenue"]), direct=f2(med["direct"] + lng["direct"]), shared_block=SH_TOTAL)
    tot["profit_before_tax"] = f2(med["profit_before_tax"] + lng["profit_before_tax"])
    tot["tax_25_consolidated"] = f2(tot["profit_before_tax"] * TAX)
    tot["after_tax_consolidated"] = f2(tot["profit_before_tax"] - tot["tax_25_consolidated"])
    return dict(medical=med, lounge=lng, holdings=dict(revenue=0.0, direct=0.0, shared_block=0.0, profit_before_tax=0.0, note="no sales; dividends from Medical and Lounge ignored inside a consolidated group"), total=tot)
SPLIT_BEFORE, SPLIT_AFTER = company_split(False), company_split(True)
for s_ in (SPLIT_BEFORE, SPLIT_AFTER):                             # LOCK: the headline must not move
    assert abs(s_["total"]["profit_before_tax"] - BEFORE) < 0.02 and abs(s_["total"]["after_tax_consolidated"] - AFTER) < 0.02, s_["total"]
# payroll tax grouping (WA): one group, aggregate wages; the designated group employer claims the one deductible amount (V, wa.gov.au, 2026-10-27)
W_GROUP = L["payroll_taxable_wages_year"]
DED = max(0.0, r14.TH - (W_GROUP - r14.TH) * 2 / 13)
assert abs(r14.ptax(W_GROUP) / 12 - (-L["payroll_tax_group"])) < 0.01
med_w = -L["midwife_wages"] + PHLEB_LOADED; all_w = -L["repo_payroll"] - L["midwife_wages"] - L["venue_manager_0630"]
out["R24"] = dict(phlebotomist_wages_month=PHLEB_WAGES, phlebotomist_loaded_month=f2(PHLEB_LOADED), load_super_wc=round(load, 5), saturdays_month=round(SAT_DAYS, 2),
    split_before_phleb_in_lounge=SPLIT_BEFORE, split_after_phleb_in_medical=SPLIT_AFTER,
    headline=dict(before_tax=BEFORE, after_tax=AFTER, unchanged=True),
    payroll_tax=dict(grouped_wages_year=W_GROUP, threshold=r14.TH, upper=r14.UP, rate=r14.RATE, over_threshold_by=f2(W_GROUP - r14.TH), deductible_amount=f2(DED),
                     taxable_after_deduction=f2(W_GROUP - DED), tax_year=r14.ptax(W_GROUP), tax_month=f2(r14.ptax(W_GROUP) / 12), changes_with_phleb_move=False,
                     medical_wage_share_E=round(med_w / all_w, 4), lounge_wage_share_E=round(1 - med_w / all_w, 4)))
CF = json.load(open(os.path.join(HERE, "..", "L18-r23", "theodore_r23_results.json"), encoding="utf-8"))   # approved 24-month cash flow (R23), read not re-run

def money(x): return f"A${x:,.2f}" if x >= 0 else f"-A${-x:,.2f}"
def split_md():
    B, A = SPLIT_BEFORE, SPLIT_AFTER; P = out["R24"]["payroll_tax"]
    row = lambda lab, key: f"| {lab} | {money(B['medical'][key])} | {money(A['medical'][key])} | {money(B['lounge'][key])} | {money(A['lounge'][key])} | {money(A['total'][key])} |"
    return ["### 4A. Company split, Round 24 (phlebotomists employed by GTT Medical)", "",
        f"The 2 phlebotomists' wages, super and workers comp ({money(PHLEB_LOADED)} a month, R) move from Lounge to Medical. Holdings has no sales. "
        "The shared block stays ONE block and sits with Lounge, which holds the lease and employs the venue manager. The room fee Medical pays Lounge is NOT IN REPO; it moves profit between the two companies only.", "",
        "| A$ a month | Medical before | Medical after | Lounge before | Lounge after | Group (unchanged) |", "|---|---|---|---|---|---|",
        row("Revenue, ex GST", "revenue"), row("Direct costs", "direct"),
        f"| Profit before shared block | {money(B['medical']['before_shared'])} | {money(A['medical']['before_shared'])} | {money(B['lounge']['before_shared'])} | {money(A['lounge']['before_shared'])} | {money(BEFORE + SH_TOTAL)} |",
        row("Less shared-cost block (one block)", "shared_block"),
        row("Profit before tax", "profit_before_tax"),
        f"| Company tax 25% | {money(B['medical']['tax_25_if_taxed_alone'])} alone | {money(A['medical']['tax_25_if_taxed_alone'])} alone | A$0.00 (loss) | A$0.00 (loss) | {money(A['total']['tax_25_consolidated'])} consolidated |",
        f"| Profit after tax | | | | | {money(A['total']['after_tax_consolidated'])} |", "",
        f"With tax consolidation (Year 1, locked) Holdings lodges one return: 25% of {money(BEFORE)} = {money(-L['company_tax_25'])}, net {money(AFTER)}. "
        f"Taxed alone, Medical would pay {money(A['medical']['tax_25_if_taxed_alone'])} while the Lounge loss could not be used: consolidation lets the loss offset the profit (E). Lounge carries the 1 cent rounding.", "",
        "### 4B. WA payroll tax grouping (Round 24)", "",
        "| Item | Value | Tag |", "|---|---|---|",
        f"| Grouped wages, all three companies, a year | {money(P['grouped_wages_year'])} | R (unchanged by the phlebotomist move) |",
        f"| Threshold / taper / upper limit | {money(P['threshold'])}; reduced by 2/13 of wages above it; nil from {money(P['upper'])} | V wa.gov.au, 2026-10-27 |",
        f"| Deductible amount (one, for the group) | {money(P['deductible_amount'])} | V formula, R wages |",
        f"| Taxable wages after deduction | {money(P['taxable_after_deduction'])} | maths |",
        f"| Payroll tax at 5.5% | {money(P['tax_year'])} a year = {money(P['tax_month'])} a month | V rate |",
        f"| Wage share (for choosing the designated group employer) | Medical about {P['medical_wage_share_E']*100:.0f}%, Lounge about {P['lounge_wage_share_E']*100:.0f}% | E |", "",
        "Why grouped: Holdings owns 100% of Medical and Lounge (related bodies corporate; one set of owners has a controlling interest). Each company registers and lodges, the group's wages are added together, only the designated group employer claims the deductible amount, and every member is jointly and severally liable (V, wa.gov.au grouping page). Payroll tax grouping is separate from the GST group and from tax consolidation.", ""]
def cf_md():
    T = CF["T4_inputs"]; F = CF["T4"]
    lab = "illustrative, not decided, deferred by Anthony"
    return ["### 4C. APPROVED 24-month cash flow (reference, headline lines only)", "",
        "Approved by Anthony 2026-10-27. Full table: [THEODORE-R23-CASHFLOW.md](overhaul-2026-10-26/L18-r23/THEODORE-R23-CASHFLOW.md) (built by theodore_r23_cashflow.py).", "",
        "| Line | Value | Tag |", "|---|---|---|",
        f"| Takings a month, incl GST | {money(T['takings_incl_gst'])} | R |",
        f"| Profit before company tax a month | {money(BEFORE)} | R |",
        f"| Start-up spend, month 0 | {money(T['startup'])} | R |",
        f"| GST to the ATO each quarter (net) | {money(T['gst_net_quarter'])}, paid 28 Oct, 28 Feb, 28 Apr, 28 Jul | V dates |",
        f"| Company tax set aside a month | {money(T['tax_per_month_provision'])} | E |",
        f"| Year 1 company tax | {money(T['tax_year1'])}, paid about month 23 | E amount, U date |",
        "| Lowest cash month | Month 0, right after the start-up spend | R model |",
        f"| Loan repayment timing (loan cleared month {F['336000_floor0']['loan_cleared_month']}, first dividend month {F['336000_floor0']['first_dividend_month']}) | {lab} | E |",
        f"| A$50,000 cash-floor scenario (loan cleared month {F['336000_floor50000']['loan_cleared_month']}, first dividend month {F['336000_floor50000']['first_dividend_month']}) | {lab} | E |", ""]
def build_centre():
    yml = {"generated_by": "docs/overhaul-2026-10-26/L17-r22/theodore_r22.py", "date": "2026-10-27", "currency": "AUD",
           "paths": {"path_a": "consult package, PREFERRED", "path_b": "outside referral, NOT preferred"},
           "prices": {"path_a_package_1_full": P1, "path_a_package_2_full": P2, "path_a_client_pays_gtt_p1": R1["gtt_receives_incl_gst"], "path_a_client_pays_gtt_p2": R2["gtt_receives_incl_gst"],
                      "consult_gst_free": CONSULT_NEW, "lounge_service_p1_taxable": LOUNGE_P1, "lounge_service_p2_taxable": LOUNGE_P2, "lab_paid_to_lab_not_gtt": LAB,
                      "path_b_p1_all_in": 300.0, "path_b_p2_all_in": 350.0, "path_b_gtt_receives_p1": B1["gtt_receives_incl_gst"], "path_b_gtt_receives_p2": B2["gtt_receives_incl_gst"],
                      "path_b_whole_amount_taxable": True, "pm_average_incl_gst": PM_PRICE, "plan_mix_p1": 1.0},
           "rebate_lock": {"consult_item": "82105", "consult_fee": 38.75, "consult_rebate": REBATE_CONSULT, "lab_test_item": "66548", "lab_test_fee": 19.90, "lab_test_rebate": REBATE_TEST,
                           "collection_item": "73928", "collection_fee": 5.95, "collection_rebate": REBATE_COLL, "collection_alt_item": "73938", "collection_alt_fee": 7.95, "collection_alt_rebate": 6.80,
                           "collection_status": "unresolved, AskMBS later", "lab_rebate": LAB_REBATE, "total_rebate": REBATE, "client_cost_path_a_p1": f2(P1 - REBATE), "client_cost_path_a_p2": f2(P2 - REBATE)},
           "volumes": {"am_clients_day": 18, "ramp": "none, 18 a day from month 1 (R23)", "am_clients_month": N, "pm_transactions_month": round(PM_TX, 2)},
           "venue_manager": {"start": "06:30", "hours": "Mon-Fri 06:30 to 15:00", "first_draw": "07:00", "repo_base_loaded": VM_BASE_LOADED, "extra_half_hour": VM_EXTRA, "combined_loaded_month": VM_COMBINED,
                             "who": "a hired venue manager; Anthony is Owner and Director with 0 operational hours (locked R23)"},
           "midwives": {"hours": "08:00 to 16:00", "first_consult": "08:15", "consult_blocks_min": 25, "paid_h_per_shift": PAID_DAY, "paid_h_week_both": 45.0, "block": "fortnightly Mon-Wed / Thu-Sat",
                        "oncost": round(r15.bu_worked, 4), "medicare_participating": "hired as participating, or plan how they get it"},
           "shared_costs_month": SH_ITEMS, "shared_costs_total": SH_TOTAL,
           "headline": {"profit_before_company_tax": BEFORE, "company_tax": L["company_tax_25"], "net_after_all": AFTER, "threshold": TARGET, "above_threshold": AFTER > TARGET},
           "phlebotomists": {"count": 2, "employer": "GTT Medical (locked R24, Anthony 2026-10-27)", "wages_month": PHLEB_WAGES, "loaded_month_with_super_wc": f2(PHLEB_LOADED)},
           "path_b_fact": "Path B earns A$26.66 less per client than Path A on the fixed roster; the midwife is on site every day and can take standalone or package consults, so the amount can be earned another way. NOT A LIMIT.",
           "company_split_month": {"before_r24_phleb_in_lounge": {k: SPLIT_BEFORE[k] for k in ("medical", "lounge", "total")},
                                   "after_r24_phleb_in_medical": {k: SPLIT_AFTER[k] for k in ("medical", "lounge", "total")},
                                   "holdings": "no sales", "shared_block_holder": "Lounge (holds the lease, employs the venue manager); one block, not split",
                                   "room_fee_medical_to_lounge": "NOT IN REPO; moves profit between companies only, no group effect"},
           "payroll_tax_grouping": {k: out["R24"]["payroll_tax"][k] for k in ("grouped_wages_year", "threshold", "upper", "rate", "deductible_amount", "taxable_after_deduction", "tax_year", "tax_month")}
                                   | {"grouped_because": "common control: Holdings owns 100% of Medical and Lounge (related bodies corporate); one deductible amount claimed by the designated group employer",
                                      "source": "wa.gov.au payroll tax employer guide, calculation and grouping pages, read 2026-10-27"},
           "gst_group_and_consolidation": "both established in Year 1 (locked R24); steps in L19-r24/THEODORE-R24-PART-1.md",
           "cash_flow_24m_APPROVED": {"file": "docs/overhaul-2026-10-26/L18-r23/THEODORE-R23-CASHFLOW.md", "takings_month_incl_gst": CF["T4_inputs"]["takings_incl_gst"],
                                      "gst_net_quarter": CF["T4_inputs"]["gst_net_quarter"], "company_tax_year1": CF["T4_inputs"]["tax_year1"], "tax_held_back_month": CF["T4_inputs"]["tax_per_month_provision"],
                                      "startup_month0": CF["T4_inputs"]["startup"],
                                      "loan_repayment_timing": "illustrative, not decided, deferred by Anthony",
                                      "cash_floor_50000_scenario": "illustrative, not decided, deferred by Anthony"}}
    with open(os.path.join(HERE, "center_of_truth.yml"), "w", encoding="ascii", errors="replace") as fh:
        yaml.safe_dump(yml, fh, sort_keys=False, allow_unicode=False, width=200)
    yaml.safe_load(open(os.path.join(HERE, "center_of_truth.yml"), encoding="ascii"))
    rows = [("Lounge + service, morning, ex GST (474 x A$147.41)", L["rev_lounge_service_am_ex_gst"], "R volume, E split"),
            ("Afternoon sales, ex GST (repo A$24,585.37 / 1.1)", L["rev_pm_ex_gst"], "R"),
            ("Consult, GST-free (474 x A$130, Medical)", L["rev_consult_gst_free"], "E"),
            ("**Revenue, ex GST**", L["revenue_total_ex_gst"], ""),
            ("Repo staff (8 AM service, 2 phlebotomists employed by Medical, 4 PM, venue manager repo base), super, workers comp", L["repo_payroll"], "R"),
            ("Repo running costs (rent, insurance, overheads, supplies)", L["repo_operating_expenses"], "R"),
            ("GST credits on costs", L["less_gst_credits"], "R"),
            ("Card fees, morning (on A$292.15)", L["card_fees"], "E"), ("Card fees, afternoon (210.13 x A$117)", L["card_fees_pm"], "E"),
            ("Midwife wages (45 paid h a week, on-cost 1.366, casual leave cover inside)", L["midwife_wages"], "E"),
            ("Midwife fixed costs and consumables (one consult room)", L["midwife_fixed_consumables"], "E"),
            ("Venue manager extra half hour (the 06:30 to 07:00 opening time before the first draw)", L["venue_manager_0630"], "R rate"),
            ("WA payroll tax, whole group", L["payroll_tax_group"], "E"), ("Three-company running cost", L["three_company"], "E"),
            ("**Profit before company tax**", BEFORE, ""), ("Company tax 25%", L["company_tax_25"], "E"),
            ("**Net profit after GST, card fees, payroll tax and company tax (franked dividend available)**", AFTER, "")]
    wf22 = []
    for k, v in wf:
        if k.startswith("Less repo staff"):
            k = "Less repo staff (8 AM service, 2 phlebotomists, 4 PM, venue manager repo base cost)"
        elif k.startswith("Less venue manager"):
            k = f"Less venue manager extra half hour (venue manager 06:30 to 15:00 costs {money(VM_COMBINED)} a month in total = {money(pc(VM_COMBINED))} a client)"
        wf22.append((k, v))
    md = ["# GTT Center Perth: Financial Center of Truth", "",
          "**One place for every money variable.** Generated by [theodore_r22.py](overhaul-2026-10-26/L17-r22/theodore_r22.py); do not edit by hand. Re-run the script after any decision change and this file and "
          "[center_of_truth.yml](overhaul-2026-10-26/L17-r22/center_of_truth.yml) regenerate together. All amounts AUD a month unless stated. "
          "General knowledge and desk research, not your personal documents. Verify before acting. If this file disagrees with [GTT-READ-FIRST.md](GTT-READ-FIRST.md), that file wins.", "",
          "Tags: **R** repo figure, **V** official source, **E** estimate, **Q** quote needed, **U** unverified.", "",
          "**Words (Round 22): Path A = consult package (PREFERRED). Path B = outside referral (NOT preferred).** Older files that say the opposite are out of date.", "",
          "## 1. Prices and money flow (Structure B, Round 22 decisions)", "",
          "| Item | Package 1 | Package 2 | GST | Who receives it | Tag |", "|---|---|---|---|---|---|",
          f"| Path A full advertised price (includes the lab fee) | {money(P1)} | {money(P2)} | inside | | Locked |",
          f"| Lab test | A${LAB} | A${LAB} | GST-free | The lab, paid by the client directly. Never GTT money | Locked |",
          f"| Consult (20 min, item 82105) | {money(CONSULT_NEW)} | {money(CONSULT_NEW)} | GST-free | Medical | Locked |",
          f"| Lounge + service | {money(LOUNGE_P1)} | {money(LOUNGE_P2)} | taxable, 1/11 is GST | Lounge | Locked |",
          f"| **Path A: client pays GTT at checkout** | **{money(R1['gtt_receives_incl_gst'])}** | **{money(R2['gtt_receives_incl_gst'])}** | | Medical + Lounge | R maths |",
          f"| Path A reaches GTT, ex GST | {money(R1['gtt_receives_ex_gst'])} | {money(R2['gtt_receives_ex_gst'])} | | | R maths |",
          f"| **Path A: client's own cost after Medicare (lab fee included)** | **{money(P1 - REBATE)}** | **{money(P2 - REBATE)}** | | | V |",
          f"| Path B all in (includes the lab fee) | {money(300.0)} | {money(350.0)} | whole GTT part taxable | | Locked |",
          f"| **Path B: client pays GTT** | **{money(B1['gtt_receives_incl_gst'])}** | **{money(B2['gtt_receives_incl_gst'])}** | 1/11 GST | Lounge. No consult line | R maths |",
          f"| Path B reaches GTT, ex GST | {money(B1['ex_gst'])} | {money(B2['ex_gst'])} | | | R maths |",
          f"| Standalone private consult | {money(CONSULT_NEW)} | | GST-free | Upside only. Client gets {money(REBATE_CONSULT)} back | Locked |", "",
          "Path B is the outside-referral route: the client keeps her own referral, there is no GTT consult and no Medicare benefit at GTT. Booking order for Path A: the client books the test, then the consult, 1 to 28 days before the test or the same morning before the draw. "
          "Checkout shows the full price but charges only the GTT amount. Medical pays Lounge a flat market room fee (inside the group, no profit effect). Plan: 100% Package 1, 100% Path A for the headline.", "",
          "**Path B fact line (Round 24):** Path B earns A$26.66 less per client than Path A on the fixed roster; the midwife is on site every day and can take standalone or package consults, so the amount can be earned another way. NOT A LIMIT. Path B has no cap, no restriction and no warning (Anthony, locked R24).", "",
          "## 1A. REBATE LOCK (every rebate figure used for planning)", "",
          "| Item | MBS item | Schedule fee | Rebate (85%) | Status |", "|---|---|---|---|---|",
          f"| Consult | 82105 | A$38.75 | {money(REBATE_CONSULT)} | Confirmed (V, health.gov.au MBS, 2026-10-26) |",
          f"| Lab test | 66548 | A$19.90 | {money(REBATE_TEST)} | Confirmed (V) |",
          f"| Collection | 73928 | A$5.95 | {money(REBATE_COLL)} | Unresolved: AskMBS later. 73938 is A$6.80 benefit, A$7.95 fee |",
          f"| **Lab rebate (test + collection)** | | | **{money(LAB_REBATE)}** | Locked for planning |",
          f"| **Total rebate, consult + lab** | | | **{money(REBATE)}** | Locked for planning, shown as 'about' |",
          f"| **Client cost after rebates, Path A** | | | **{money(P1 - REBATE)} / {money(P2 - REBATE)}** | Package 1 / Package 2 |", "",
          "GTT's own money does not change whichever collection item applies. Do not reopen this.", "",
          "## 2. Volumes, staffing and hours (checked against the repo by the script)", "",
          "| Variable | Value | Source |", "|---|---|---|",
          f"| Morning clients | 18 a day, Mon-Sat = {N} a month | R (18 a day x 26.33 trading days a month = 22 weekdays + 4.33 Saturdays, a calendar count). No ramp: full volume from month 1 (Anthony, R23) |",
          f"| Afternoon transactions | {PM_TX:.2f} a month (8.70 weekday, 4.35 Saturday a day) at A$117 = A$24,585.37 | R (revenue_assumptions.yml, Model E) |",
          "| AM service staff | 8 (4 massage and beauty, 2 nails, 2 hair), 6 h, 07:00-13:00 | R |",
          f"| Phlebotomists | 2 at 10-18 booked, 1 at 9 or fewer, none PM. **Employed by GTT Medical** (locked R24). Wages {money(PHLEB_WAGES)} a month, {money(PHLEB_LOADED)} with super and workers comp | R |",
          "| PM service staff | 4 casual, 3-hour floor | R |",
          f"| Venue manager | **Starts 06:30, Mon-Fri 06:30 to 15:00.** 07:00 is the first draw. Cost {money(VM_COMBINED)} a month loaded = repo base {money(VM_BASE_LOADED)} + extra half hour {money(VM_EXTRA)}. A hired venue manager, not Anthony (Anthony is Owner and Director, 0 operational hours, locked R23) | R rate, locked time |",
          "| Hosts | none | Locked |",
          "| Midwives | 08:00 to 16:00 (8 h on site, 7.5 h paid after a 30 minute unpaid break E). First consult 08:15, 25 minute blocks 08:15 to 10:30 to match the draws, then normal midwife bookings. 2 permanent part-time, fortnightly block Mon-Wed / Thu-Sat, + 1 casual. Hired with Medicare participating status, or we plan how they get it | Locked |",
          f"| Midwife time | 18 GTT consults x 20 min = 6.0 h a day; 7.5 h paid; {SPARE_SLOTS_DAY} spare 20-minute slots a day for standalone consults (upside only) | maths |",
          "| Consult rooms / collection rooms | 1 / 2 (one chair each) | Locked |",
          "| Late rule | Clients arrive at least 10 minutes early; late means from the appointment time onwards. Blood draws: no wiggle room. Consults: a 10 minute grace window | Locked R24 |", "",
          "## 3. Rates and tax", "",
          "| Variable | Value | Tag |", "|---|---|---|",
          f"| Midwife rate | Nurses Award RN L2 pp4 A$41.59 weekday, 150% Saturday; blended A${r18.RATE_BLEND:.2f} | E |",
          f"| Midwife on-cost (used) | {r15.bu_worked:.3f}: super 12%, workers comp 1.7%, leave loading, paid leave covered by the casual | E |",
          "| Midwife on-cost (sensitivity only) | 1.20 (no leave cover) | E |",
          "| Card fee | 1.7% + A$0.30 a transaction on all card takings, AM and PM (repo lists Tyro 1.4% / Square 1.6%, provider not chosen) | E |",
          "| WA payroll tax | 5.5%; annual threshold A$1,000,000, deduction tapers by 2/13 of wages above it, nil from A$7,500,000; one threshold for the group, claimed by the designated group employer | V, wa.gov.au payroll tax employer guide (calculation and grouping pages), read 2026-10-27 |",
          "| Company tax | 25% (base rate entity), one consolidated return; three companies (Holdings, Medical, Lounge), no trust; franked dividends direct to Anthony and partner (Route B). GST group and tax consolidation established in Year 1 (locked R24) | E |", "",
          "## 4. Monthly P&L, whole venture (Holdings + Medical + Lounge), locked case, Path A, GTT clients only", "",
          "| Line | Monthly | Tag |", "|---|---|---|"] + [f"| {k} | {money(v)} | {t} |" for k, v, t in rows] + [
          "", f"GST passed to the ATO (not revenue): morning {money(L['gst_collected_am'])}, afternoon {money(L['gst_collected_pm'])}. Target: net profit above A$20,000 a month after all of the above. "
          f"Result: {money(AFTER)} ({'above' if AFTER > TARGET else 'below'} by {money(abs(AFTER - TARGET))}). Standalone private consults are upside and are NOT in this P&L.", "",
          "### Shared costs as one block (GTT is one business)", "", "| Single form, profit BEFORE shared costs | Monthly |", "|---|---|",
          f"| Consult | {money(forms['consult'])} |", f"| Morning lounge | {money(forms['morning_lounge'])} |", "| Lab | A$0.00 (the client pays the lab; never GTT money) |",
          f"| Afternoon | {money(forms['afternoon'])} |", f"| **Total before shared costs** | **{money(FORMS_TOTAL)}** |",
          f"| Shared: venue manager 06:30 to 15:00 (combined loaded) | -{money(VM_COMBINED)} |",
          f"| Shared: rent, insurance, overheads, supplies, after GST credits | -{money(SH_ITEMS['rent_insurance_overheads_supplies_net_of_gst_credits'])} |",
          f"| Shared: WA payroll tax, whole group | -{money(SH_ITEMS['wa_payroll_tax_group'])} |", f"| Shared: three-company running cost | -{money(SH_ITEMS['three_company_running_cost'])} |",
          f"| **One shared block** | **-{money(SH_TOTAL)}** |", f"| **Profit before company tax** | **{money(BEFORE)}** |", ""] + split_md() + cf_md() + [
          "## 5. Per-client waterfall (Path A, Package 1, A$320 full price)", "", "| Step | A$ per client |", "|---|---|"] + [f"| {k} | {money(v)} |" for k, v in wf22] + [
          "", f"The client then gets A$55.00 back from Medicare, so her own cost is {money(P1 - REBATE)} ({money(P2 - REBATE)} on Package 2), lab fee included.", "",
          "## 6. Not in any financial", "", "| Item | Status |", "|---|---|"] + [f"| {a} | {b} |" for a, b in NOT_IN] + [
          "| Senior cover loading (afternoon gap, Saturday) | Not in repo |", "| 50 percent lounge refund policy | Cost per case in THEODORE-R20.md section 6; not deducted |", "",
          "## 7. Banned stale values (pre-send fact check)", "",
          "Run `python tools/factcheck_locked_facts.py <file>` before anything goes to Anthony. The first column is what the checker bans. Round 22: the figures for Path B are now valid, so the checker bans them only when they sit next to the words Path A (a pattern in the tool, not a table row).", "",
          "| Banned | Correct |", "|---|---|"] + [f"| {b} | {w} |" for b, w in BANNED22] + [
          "", "## 8. Change log", "", "| Date | Change | By |", "|---|---|---|",
          "| 2026-10-26 | Round 20: consult A$130 inside packages and standalone, midwives 08:00 to 16:00, same-day consult | Theodore R20 |",
          f"| 2026-10-26 | Round 22: Path A/B renamed, Path B A$300/A$350, rebate lock, venue manager 06:30 to 15:00 combined {money(VM_COMBINED)}, one shared-cost block; headline unchanged {money(BEFORE)} before and {money(AFTER)} after company tax | Theodore R22 |",
          "| 2026-10-27 | Round 23: no revenue ramp (18 a day from month 1; the 22 + 4.33 day count is a calendar count, not a ramp); venue manager is a hired person, Anthony is Owner and Director; three companies, no trust. Headline unchanged | Theodore R23 |",
          "| 2026-10-27 | Round 24: phlebotomists employed by Medical (company split re-run), payroll tax grouping verified on wa.gov.au, 24-month cash flow APPROVED (cash floor and loan repayment illustrative, deferred), GST group and consolidation in Year 1, Path B fact line (not a limit), late rule split. Headline unchanged | Theodore R24 |", ""]
    with open(os.path.join(REPO, "docs", "FINANCIAL-CENTER-OF-TRUTH.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(md))

if __name__ == "__main__" and len(sys.argv) > 2 and sys.argv[1] == "--check":
    hits = fact_check(sys.argv[2])
    for h in hits: print(f"line {h[0]}: {h[2]}  ->  {h[3]}")
    print(f"fact_check: {len(hits)} hit(s)"); sys.exit(1 if hits else 0)
build_centre()
json.dump(out, open(os.path.join(HERE, "theodore_r22_results.json"), "w"), indent=1, default=str)
if __name__ == "__main__":
    for k in [k for k in out if k.startswith("R22")]:
        print(k, json.dumps(out[k], indent=1, default=str))
