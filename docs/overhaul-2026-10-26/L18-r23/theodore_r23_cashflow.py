"""Theodore R23 (2026-10-27). Reuses theodore_r22c.py (-> theodore_r22 engine -> r18 .. r13 -> tools/master_financial_model.py live).
No new profit model: every monthly money line is the locked case (A$26,631.97 before tax, A$19,973.98 after).
Adds:  T1 Path B margin on a fixed midwife roster;  T3 shareholder-loan timeline with NO ramp;
       T4 24-month cash flow with company tax timing, quarterly GST (BAS), working capital and loan repayment.
Writes theodore_r23_results.json and THEODORE-R23-CASHFLOW.md.  Tags: R repo, V verified source, E estimate, U unverified.
Run: python theodore_r23_cashflow.py
"""
import contextlib, importlib.util, io, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("theodore_r22c", os.path.join(HERE, "..", "L17-r22", "theodore_r22c.py"))
E = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(E)
f2 = E.f2
L, N, BEFORE, AFTER, TAX = E.LOCK, E.N, E.BEFORE, E.AFTER, E.TAX
assert abs(BEFORE - 26631.97) < 0.005 and abs(AFTER - 19973.98) < 0.005 and abs(N - 473.94) < 0.005
R = {"generated": "2026-10-27", "engine": "theodore_r22c.py (unchanged) imported; locked case only", "locked": dict(before=BEFORE, after=AFTER, clients_month=N)}

# ================= T1: Path B vs Path A, fixed roster =================
J2 = E.out["R22_J2"]
A1, B1 = E.R1, J2["pathB_p1"]
CONS = E.CONS_COST                                   # A$3.00 consult consumables a consult (E, repo chain r14)
a_keep = f2(A1["gtt_ex_gst_after_card"] - CONS)       # 269.14
b_keep = B1["gtt_net_after_card"]                     # 242.48
gap = f2(b_keep - a_keep)
assert abs(gap - J2["vs_pathA_p1"]["B_minus_A_fixed"]) < 0.005 and abs(gap + 26.66) < 0.005
decomp = dict(takings_to_gtt=f2(B1["gtt_receives_incl_gst"] - A1["gtt_receives_incl_gst"]),
              more_gst=f2(-(B1["gst_1_11"] - A1["lounge_gst_inside"])),
              card_fee_saved=f2(A1["card_fee"] - B1["card_fee"]), consult_consumables_saved=CONS)
assert abs(sum(decomp.values()) - gap) < 0.011
# the consult view: what Path A earns from the consult line vs what Path B earns from the larger lounge line
consult_net = f2(130.0 - 0.017 * 130.0 - CONS)        # consult A$130 GST-free, less its card share and consumables
extra_lounge_ex = f2(110.0 / 1.1 - 0.017 * 110.0)     # Path B lounge line is A$110 bigger incl GST
mw_month = f2(-L["midwife_wages"]); mw_fixed_month = f2(-L["midwife_fixed_consumables"])
mix = []
for s in (0.05, 0.10, 0.20):
    b = s * N * gap
    mix.append(dict(share=s, clients_month=round(s * N, 2), clients_day=round(s * 18, 2), change_before_tax=f2(b), change_after_tax=f2(b * (1 - TAX)),
                    before_tax=f2(BEFORE + b), after_tax=f2((BEFORE + b) * (1 - TAX))))
be = E.out["R22_J2_breakeven"]
R["T1"] = dict(pathA_keep_after_gst_card_consumables=a_keep, pathA_keep_before_consumables=A1["gtt_ex_gst_after_card"], pathB_keep=b_keep, gap_per_client=gap,
               decomposition=decomp, consult_line_net=consult_net, extra_lounge_line_net=extra_lounge_ex,
               midwife_wages_month_fixed=mw_month, midwife_fixed_costs_month=mw_fixed_month, midwife_per_client=f2((mw_month + mw_fixed_month) / N),
               retired_roster_flex_gap=J2["vs_pathA_p1"]["B_minus_A_flex"], mix=mix,
               equal_price_fixed=dict(p1_all_in=be["p1"]["vs_fixed"]["all_in_price"], p1_gtt=be["p1"]["vs_fixed"]["gtt_receives"],
                                      p2_all_in=be["p2"]["vs_fixed"]["all_in_price"], p2_gtt=be["p2"]["vs_fixed"]["gtt_receives"]),
               receipt_option3=dict(lounge_and_service=B1["gtt_receives_incl_gst"], gst_inside=B1["gst_1_11"], consult_line=0.0, lab_paid_to_lab=E.LAB))

# ================= T3: R22C loan timeline with the ramp stripped =================
E.RAMP_PCT = {k: 1.0 for k in E.RAMP_PCT}             # flat 100 percent from month 1 (Anthony R23; DECISION-LOG 2026-10-16 (c))
T3 = {}
for cap in (250000.0, 336000.0):
    t = E.timeline(cap, start_repay_month=1)
    T3[str(int(cap))] = {k: v for k, v in t.items() if k != "rows"} | {"first_rows": t["rows"][:3]}
R["T3_no_ramp_simple"] = T3
R["T3_r22c_ramped_for_reference"] = {k: dict(cleared=v["loan_cleared_month"], topup=v["extra_owner_funding_needed"]) for k, v in E.TL.items()}

# ================= T4: 24-month cash flow =================
D = 30.42                                             # days in an average month (365/12, E)
CARD_LAG_D, WAGE_LAG_D = 1.0, 7.0                     # E: card money lands next business day; wages fortnightly, paid about 7 days after period end
STARTUP = E.STARTUP_PLAN                               # A$251,198 (R, includes bond and one month's advance rent)
DEFERRED = {4: 5600.0, 6: 7774.0}                      # R: CASHFLOW-FORECAST.md section 1c
TAKINGS = f2(L["rev_consult_gst_free"] + L["rev_lounge_service_am_ex_gst"] + L["gst_collected_am"] + L["rev_pm_ex_gst"] + L["gst_collected_pm"])
CARD = f2(-L["card_fees_total"])
WAGES = f2(-(L["repo_payroll"] + L["midwife_wages"] + L["venue_manager_0630"]))   # loaded: wages, super, workers comp
RUN_INCL = f2(-L["repo_operating_expenses"])          # paid incl GST (R)
CREDITS = f2(L["less_gst_credits"])                    # GST credits on those costs (R, implied by repo after-GST basis)
MW_FIXED = f2(-L["midwife_fixed_consumables"]); THREE = f2(-L["three_company"]); PTAX = f2(-L["payroll_tax_group"])
GST_OUT = f2(L["gst_collected_am"] + L["gst_collected_pm"]); GST_NET = f2(GST_OUT - CREDITS)
chk = TAKINGS - GST_OUT - CARD - WAGES - (RUN_INCL - CREDITS) - MW_FIXED - THREE - PTAX
assert abs(chk - BEFORE) < 0.05, chk
BAS_PAY = {4: (1, 3), 8: (4, 6), 10: (7, 9), 13: (10, 12), 16: (13, 15), 20: (16, 18), 22: (19, 21)}   # V: 28 Oct, 28 Feb, 28 Apr, 28 Jul (opening in July, E)
TAX_Y1 = f2(12 * BEFORE * TAX); TAX_PAY = {23: TAX_Y1}  # U: first-year return, small company with agent, lodge and pay about 15 May (month 23)

def run(capital, floor=0.0, repay=True, provision=True, n=24):
    cash = capital - STARTUP; loan = capital; top = 0.0
    if cash < floor: top = floor - cash; cash = floor; loan += top
    rows = [dict(m=0, cash=f2(cash), loan=f2(loan), note="start-up spend A$251,198")]
    gst_owed = 0.0; tax_prov = 0.0; ptax_owed = 0.0; low = (0, cash); cleared = None; divs = 0.0
    for m in range(1, n + 1):
        rec = TAKINGS - CARD - (TAKINGS - CARD) * CARD_LAG_D / D * (1 if m == 1 else 0)
        wages = WAGES * (1 - WAGE_LAG_D / D) if m == 1 else WAGES
        pt = ptax_owed; ptax_owed = PTAX
        gst_owed += GST_NET
        gst_paid = 0.0
        if m in BAS_PAY:
            q = BAS_PAY[m]; gst_paid = GST_NET * (q[1] - q[0] + 1); gst_owed -= gst_paid
        tax_paid = TAX_PAY.get(m, 0.0)
        tax_prov += BEFORE * TAX - tax_paid
        out = wages + RUN_INCL + MW_FIXED + THREE + pt + gst_paid + tax_paid + DEFERRED.get(m, 0.0)
        cash += rec - out
        t = 0.0
        if cash < floor: t = floor - cash; cash += t; loan += t; top += t
        held = floor + (tax_prov if provision else 0.0) + gst_owed + ptax_owed
        rep = min(loan, max(0.0, cash - held)) if repay else 0.0
        cash -= rep; loan -= rep
        div = max(0.0, cash - held) if (repay and loan <= 0.005) else 0.0   # E: spare cash paid as franked dividends once the loan is clear
        cash -= div; divs += div
        if loan <= 0.005 and cleared is None: cleared = m
        if cash < low[1]: low = (m, cash)
        rows.append(dict(m=m, receipts=f2(rec), paid_out=f2(out), gst_paid=f2(gst_paid), tax_paid=f2(tax_paid), topup=f2(t), repaid=f2(rep), dividend=f2(div),
                         loan=f2(loan), cash=f2(cash), held_back=f2(held)))
    return dict(capital=capital, floor=floor, extra_owner_cash=f2(top), loan_cleared_month=cleared, first_dividend_month=(cleared + 1 if cleared else None),
                lowest_cash_month=low[0], lowest_cash=f2(low[1]), dividends_24m=f2(divs), rows=rows)

T4 = {}
for cap in (250000.0, 336000.0):
    for fl in (0.0, 50000.0):
        T4[f"{int(cap)}_floor{int(fl)}"] = run(cap, fl)
NOREPAY = {str(int(c)): run(c, 0.0, repay=False) for c in (250000.0, 336000.0)}
NOPROV = run(336000.0, 0.0, provision=False)
R["T4_inputs"] = dict(takings_incl_gst=TAKINGS, card_fees=CARD, wages_loaded=WAGES, running_costs_incl_gst=RUN_INCL, gst_credits=CREDITS, midwife_fixed=MW_FIXED,
                      three_company=THREE, payroll_tax=PTAX, gst_collected=GST_OUT, gst_net_month=GST_NET, gst_net_quarter=f2(3 * GST_NET),
                      tax_year1=TAX_Y1, tax_per_month_provision=f2(BEFORE * TAX), deferred_capex=DEFERRED, startup=STARTUP)
R["T4"] = {k: {a: b for a, b in v.items() if a != "rows"} for k, v in T4.items()}
R["T4_rows_336000_floor0"] = T4["336000_floor0"]["rows"]; R["T4_rows_250000_floor0"] = T4["250000_floor0"]["rows"]
R["T4_no_repayment_lowest"] = {k: dict(month=v["lowest_cash_month"], cash=v["lowest_cash"], cash_m24=v["rows"][-1]["cash"]) for k, v in NOREPAY.items()}
R["T4_no_tax_provision_336000"] = dict(lowest_cash_month=NOPROV["lowest_cash_month"], lowest_cash=NOPROV["lowest_cash"], topup=NOPROV["extra_owner_cash"])
json.dump(R, open(os.path.join(HERE, "theodore_r23_results.json"), "w"), indent=1, default=str)

# ---------- THEODORE-R23-CASHFLOW.md (table file) ----------
def mny(x): return f"A${x:,.2f}" if x >= 0 else f"-A${-x:,.2f}"
M = ["Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "Jan", "Feb", "Mar", "Apr", "May", "Jun"]
r = T4["336000_floor0"]["rows"]; r2 = T4["250000_floor0"]["rows"]
lines = ["# THEODORE R23: 24-month cash flow, flat 18 clients a day, tax, GST and working capital", "",
 "Theodore, 2026-10-27. Built by [theodore_r23_cashflow.py](theodore_r23_cashflow.py), results in theodore_r23_results.json. General knowledge and repo figures, not your personal documents. Not tax advice; accountant to confirm. Nothing sent.", "",
 "## READ-FIRST CHECK", "",
 "- Venue manager starts 06:30 (Mon to Fri 06:30 to 15:00); 07:00 is the first draw. Anthony is Owner and Director, not the venue manager.",
 "- Path A = PREFERRED, package with the GTT midwife consult. Path B = NOT preferred, outside referral, no GTT consult.",
 "- Prices: Path A A$320 / A$370, GTT charges A$292.15 / A$342.15. Path B A$300 / A$350 all in, GTT charges A$272.15 / A$322.15.  <!-- factcheck:ok -->",
 "- Rebates: consult A$32.95 + lab A$22.05 = A$55.00 (shown as about).",
 "- Midwives 08:00 to 16:00, first consult 08:15, 25 minute blocks to 10:30.",
 "- Late rule: clients arrive 10 minutes early; late means from the appointment time onwards. Blood draws: no wiggle room. Consults: 10 minute grace window (R24).", "",
 "**STATUS (Round 24): APPROVED by Anthony 2026-10-27** (company tax, GST and working capital). The loan repayment timing and the A$50,000 cash-floor scenario below are **illustrative, not decided, deferred by Anthony**. Numbers kept, not deleted.", "",
 "## Assumptions (every one tagged)", "", "| Item | Used | Tag |", "|---|---|---|",
 f"| Monthly money lines | Locked case: takings {mny(TAKINGS)} incl GST, profit {mny(BEFORE)} before tax | R |",
 "| Volume | 18 clients a day from month 1, 473.94 a month, no ramp | R (Anthony R23) |",
 f"| Start-up spend, month 0 | {mny(STARTUP)} (includes bond and one month's advance rent) | R |",
 "| Deferred buys | A$5,600 month 4, A$7,774 month 6 | R |",
 "| Card money | lands next business day (1 day lag) | E |",
 "| Wages, super | fortnightly, paid about 7 days after the period; super paid with wages | E |",
 "| Rent | monthly in advance; first month already inside start-up | R / E |",
 "| Supplier credit | none (pay on the day, cautious) | E |",
 "| WA payroll tax | paid the month after | U |",
 f"| GST | collected {mny(GST_OUT)} a month; credits only on the repo running costs {mny(CREDITS)}; consult GST-free | R |",
 "| GST split of midwife costs, card fees, deferred buys | NOT IN REPO, no credit taken (E) | E |",
 "| BAS | quarterly, paid 28 Oct, 28 Feb, 28 Apr, 28 Jul (ato.gov.au, BAS due dates, read 2026-10-27) | V |",
 "| Opening month | July, so year 1 is one income year (launch date not set) | E |",
 f"| Company tax | 25 percent; year 1 tax {mny(TAX_Y1)} paid about 15 May of year 2 (month 23) | E rate, U date |",
 "| PAYG instalments | a company enters after a tax return shows A$2m+ instalment income or A$500+ notional tax, or as head company of a consolidated group (ato.gov.au, Starting PAYG instalments, read 2026-10-27). First instalment falls after month 24 here | V rule, U date |",
 f"| Tax held back | {mny(BEFORE * TAX)} a month set aside, never used to repay the loan | E (prudent) |",
 "| GST credits on start-up spend | NOT IN REPO whether A$251,198 includes GST; not counted | E |", "",
 "## A$336,000 case, no cash floor (A$ month-end; Repaid, Dividend, Loan left: illustrative, deferred)", "",
 "| Mth | Cal | Receipts | Paid out | of which GST | of which tax | Repaid | Dividend | Loan left | Cash | Held for GST/tax |", "|---|---|---|---|---|---|---|---|---|---|---|",
 f"| 0 | | | {mny(STARTUP)} | | | | | {mny(r[0]['loan'])} | {mny(r[0]['cash'])} | |"]
for x in r[1:]:
    lines.append(f"| {x['m']} | {M[(x['m'] - 1) % 12]} | {mny(x['receipts'])} | {mny(x['paid_out'])} | {mny(x['gst_paid'])} | {mny(x['tax_paid'])} | {mny(x['repaid'])} | {mny(x['dividend'])} | {mny(x['loan'])} | {mny(x['cash'])} | {mny(x['held_back'])} |")
s = lambda k: T4[k]
lines += ["", "## Headline results (repayment timing and floor: illustrative, not decided, deferred by Anthony)", "", "| Case | Extra owner cash | Loan cleared | First dividend | Dividends to month 24 |", "|---|---|---|---|---|"]
for k, lab in (("250000_floor0", "A$250,000, no floor"), ("336000_floor0", "A$336,000, no floor"), ("250000_floor50000", "A$250,000, A$50,000 floor (illustrative, deferred)"), ("336000_floor50000", "A$336,000, A$50,000 floor (illustrative, deferred)")):
    v = s(k); lines.append(f"| {lab} | {mny(v['extra_owner_cash'])} | month {v['loan_cleared_month']} | month {v['first_dividend_month']} | {mny(v['dividends_24m'])} |")
nr = R["T4_no_repayment_lowest"]
lines += ["", f"**Lowest cash month: month 0**, right after the start-up spend. With no repayments, cash only rises after that (A$336,000 case: {mny(nr['336000']['cash_m24'])} by month 24). "
          f"With repayments, cash never drops below the money held back for GST, payroll tax and company tax (lowest {mny(T4['336000_floor0']['lowest_cash'])} in month 1). That money belongs to the tax office, not to GTT.", "",
          f"Why tax is held back: if the company paid out every spare dollar and did NOT hold back tax, the {mny(TAX_Y1)} year 1 tax bill in month 23 would leave a hole, and the owners would have to put {mny(R['T4_no_tax_provision_336000']['topup'])} back in.", "",
          "**Buffer:** the only real gap is at month 0: A$1,198 on the A$250,000 case, none on A$336,000. The A$50,000 cash floor is illustrative, not decided, deferred by Anthony.", "",
          "## QUESTIONS FOR ANTHONY", "",
          "None. The cash floor and the shareholder loan repayment schedule are deferred by Anthony (Round 24); funding above joint savings is dropped for now.", "", "Regards.", "Theodore", ""]
md = "\n".join(lines)
open(os.path.join(HERE, "THEODORE-R23-CASHFLOW.md"), "w", encoding="utf-8").write(md)
if __name__ == "__main__":
    print(json.dumps({k: R[k] for k in ("T1", "T3_no_ramp_simple", "T3_r22c_ramped_for_reference", "T4_inputs", "T4", "T4_no_repayment_lowest", "T4_no_tax_provision_336000")}, indent=1, default=str))
    print("md chars", len(md))
