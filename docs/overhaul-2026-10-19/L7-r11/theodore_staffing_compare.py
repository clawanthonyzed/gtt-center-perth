"""Theodore R11: staffing structure comparison for GTT Center Perth (plan, not a forecast; project name is an unregistered placeholder).
All figures A$ per month unless stated. Inputs are repo figures only (sources in comments). Rent rows are illustrative, NOT in repo.
Two bases are shown because the repo has both:
  OP  = repo operating profit with no GST line (CURRENT-STATE, NON-BULK-BILLED-COST-MODEL): baseline 35,186.40.
  GST = Round 9 after-GST result (theodore_model.after_gst): baseline 23,442.58 at 18 clients a day."""
import json, os
# ---- repo constants ----
BASE_OP = 35186.40                 # repo net operating profit, 18 a morning, 26.33 days (no GST line)
AM_GST_FULL, PM_GST, ITC = 10771.36, 2235.04, 1262.58   # theodore_model.py
GST_DRAG = AM_GST_FULL + PM_GST - ITC                   # 11,743.82
def after_gst(op): return op - GST_DRAG
BASE_GST = after_gst(BASE_OP)
assert abs(BASE_GST - 23442.58) < 0.01, BASE_GST        # matches Round 9 STEADY
WAGE_SAVE_REPO = 13364.52          # R1-ADAPTIVE-PHLEBOTOMY / ROUTE-1: 2 collectors, with super and workers comp
PER_COLLECTOR_QUOTED = 6682.28     # per collector as quoted in ROUTE-1
WAGE_SAVE_QUOTED = 2 * PER_COLLECTOR_QUOTED             # 13,364.56
WAGE_CALC_BASE = 13364.51          # NON-BULK-BILLED-COST-MODEL s5 calculator: 11,754.19 wages x (1+0.12+0.017)
CLIENTS_MONTH = 473.94             # 18 x 26.33
LAB_FEE_PER_CLIENT = 25.85         # item 66548 A$19.90 + item 73928 A$5.95 (MBS, 2026-10-17)
LAB_FEE_MONTH = round(LAB_FEE_PER_CLIENT * CLIENTS_MONTH, 2)   # 12,251.35
assert abs(LAB_FEE_MONTH - 12251.35) < 0.01
BENEFIT_PER_CLIENT = 22.05; GAP = 3.80
TAX = 0.25
r2 = lambda x: round(x + 0.0, 2)

# ---- options ----
def opt_a(op=True):   # lab employs collectors, recharge 0
    v = BASE_OP + WAGE_SAVE_REPO
    return r2(v if op else after_gst(v))
def opt_c(op=True):   # GTT employs, absorbs lab fee. Lab fee is a GST-inclusive cost with ITC of 1/11 (repo GST-stress column 12,304.99 proves this treatment)
    if op: return r2(BASE_OP - LAB_FEE_MONTH)
    return r2(after_gst(BASE_OP - LAB_FEE_MONTH) + LAB_FEE_MONTH / 11)
assert abs(opt_a(True) - 48550.92) < 0.005           # repo figure
assert abs(opt_c(True) - 22935.05) < 0.005           # repo figure
assert abs(opt_c(False) - 12304.99) < 0.01           # repo GST-stress Case 3 figure
def b_profit(fee_ex_gst, itc=True):
    """(b) lab recharge fee F (ex-GST). Invoice = 1.1F. GTT claims ITC F/10 if itc (same treatment as repo gives the lab fee)."""
    incl = fee_ex_gst * 1.1
    net_cost = fee_ex_gst if itc else incl
    return r2(after_gst(BASE_OP + WAGE_SAVE_REPO) - net_cost), r2(incl)
def be(target, itc=True):
    gap = after_gst(BASE_OP + WAGE_SAVE_REPO) - target
    ex = gap if itc else gap / 1.1
    return r2(ex), r2(ex * 1.1)
be_base = be(BASE_GST); be_c = be(opt_c(False))
be_base_noitc = be(BASE_GST, itc=False); be_c_noitc = be(opt_c(False), itc=False)
assert abs(b_profit(be_base[0])[0] - BASE_GST) < 0.02
assert abs(b_profit(be_c[0])[0] - opt_c(False)) < 0.02

sweep = []
for k in range(0, 11):
    f = r2(WAGE_SAVE_REPO * k / 10)
    p, inv = b_profit(f); pn, _ = b_profit(f, itc=False)
    sweep.append(dict(share_of_wage_cost=k/10, fee_ex_gst=f, invoice_incl_gst=inv, profit_after_gst=p, profit_if_no_itc=pn,
                      vs_baseline=r2(p - BASE_GST), annual=r2(p*12), annual_after_company_tax=r2(p*12*(1-TAX))))
# rent sensitivity: lab pays GTT rent R (GST-inclusive, taxable commercial supply, GTT remits R/11). ILLUSTRATIVE, NOT IN REPO.
rent = []
for R in (0, 500, 1000, 2000):
    add = R - R / 11
    rent.append(dict(rent_incl_gst=R, net_of_gst=r2(add), a_profit_after_gst=r2(opt_a(False) + add),
                     b_at_half_wage_profit=r2(b_profit(WAGE_SAVE_REPO/2)[0] + add),
                     label="illustrative, valuer needed, NOT in repo"))

def yr(m): return dict(month=r2(m), year=r2(m*12), company_tax_25pct=r2(max(m,0)*12*TAX), year_after_company_tax=r2(m*12 - max(m,0)*12*TAX))
out = dict(
 basis_note="OP = repo operating profit with no GST line; GST = Round 9 after-GST. Same wage saving and same lab fee apply on both.",
 constants=dict(BASE_OP=BASE_OP, GST_DRAG=r2(GST_DRAG), BASE_GST=r2(BASE_GST), WAGE_SAVE_REPO=WAGE_SAVE_REPO,
                WAGE_SAVE_QUOTED_2x6682_28=WAGE_SAVE_QUOTED, WAGE_CALC_BASE=WAGE_CALC_BASE, LAB_FEE_MONTH=LAB_FEE_MONTH,
                CLIENTS_MONTH=CLIENTS_MONTH, LAB_FEE_PER_CLIENT=LAB_FEE_PER_CLIENT),
 reconcile=dict(
   quoted_components=r2(BASE_OP + WAGE_SAVE_QUOTED), repo_figure=opt_a(True), cent_difference=r2(BASE_OP + WAGE_SAVE_QUOTED - opt_a(True)),
   user_stated_48550=48550.0, diff_to_user_stated=r2(opt_a(True) - 48550.0),
   note="2 x 6,682.28 = 13,364.56 but the repo saving is 13,364.52 (calculator 13,364.51 elsewhere, 13,364.50 in GST-SPLIT-MODEL). Repo A$48,550.92 used. Spread is A$0.06 and is rounding of the per-collector figure."),
 options={
  "d_baseline": dict(op=BASE_OP, after_gst=r2(BASE_GST), **{"year_" + k: v for k, v in yr(BASE_GST).items()}),
  "a_lab_employs_no_recharge": dict(op=opt_a(True), after_gst=opt_a(False), **{"year_" + k: v for k, v in yr(opt_a(False)).items()}),
  "c_gtt_employs_absorbs_lab_fee": dict(op=opt_c(True), after_gst=opt_c(False), **{"year_" + k: v for k, v in yr(opt_c(False)).items()}),
 },
 a_minus_c=dict(month_op=r2(opt_a(True)-opt_c(True)), year_op=r2((opt_a(True)-opt_c(True))*12),
                month_after_gst=r2(opt_a(False)-opt_c(False)), year_after_gst=r2((opt_a(False)-opt_c(False))*12),
                year_after_gst_after_company_tax=r2((opt_a(False)-opt_c(False))*12*(1-TAX))),
 lab_fee_composition=dict(item_66548=19.90, item_73928=5.95, per_client=LAB_FEE_PER_CLIENT, clients_month=CLIENTS_MONTH,
                          month=LAB_FEE_MONTH, year=r2(LAB_FEE_MONTH*12), medicare_benefit_85pct_per_client=BENEFIT_PER_CLIENT,
                          client_gap_if_lab_bills_full=GAP,
                          note="12,251.35 = A$25.85 x 473.94 clients. It is the lab's Medicare schedule fee for each pregnancy glucose test visit (test + collection episode), not wages."),
 b_sweep=sweep,
 b_break_even=dict(equal_to_baseline=dict(fee_ex_gst=be_base[0], invoice_incl_gst=be_base[1]),
                   equal_to_option_c=dict(fee_ex_gst=be_c[0], invoice_incl_gst=be_c[1]),
                   if_gtt_cannot_claim_itc=dict(equal_to_baseline_invoice_incl=be_base_noitc[1], equal_to_c_invoice_incl=be_c_noitc[1])),
 b_gst_assumption="Recharge assumed taxable (lab charges GST at 10%); GTT claims the 1/11 credit, the same way the repo treats the lab fee (Case 3 GST-stress A$12,304.99). If GTT cannot claim, the invoice itself is the cost (see profit_if_no_itc).",
 rent_sensitivity=rent,
 rent_note="Lab-to-GTT payment must be market rent only for space actually used (valuer needed; Catherine to confirm the Health Insurance Act rules on pathology arrangements). Any payment tied to referrals, bookings or doctor requests is not allowed. Rent amounts are placeholders, NOT in repo.",
 pregnant_client_price=dict(bulk_billed_client_pays=0.00, full_fee_client_pays=GAP, price_for_c_to_restore_baseline_gst_aside=250+LAB_FEE_PER_CLIENT,
   note="Repo has A$0 vs A$3.80 but both are paid to the lab, not GTT, so GTT revenue does not change and no payback period exists. Option c has no capex either."),
)
here = os.path.dirname(os.path.abspath(__file__))
json.dump(out, open(os.path.join(here, "theodore_staffing_compare_results.json"), "w"), indent=1)

# ---- markdown ----
f = lambda x: ("-" if x < 0 else "") + "A$" + format(abs(x), ",.2f")
d, a, c = out["options"]["d_baseline"], out["options"]["a_lab_employs_no_recharge"], out["options"]["c_gtt_employs_absorbs_lab_fee"]
amc = out["a_minus_c"]; bb = out["b_break_even"]
md = []
md += ["# Staffing structure compare: who employs the collectors", "",
 "General knowledge and repo figures, not personal documents. Verify before acting. Prepared 2026-10-20 by Theodore (CFO role). The financial model is a plan, not a forecast. Project name is an unregistered placeholder. Script: [theodore_staffing_compare.py](theodore_staffing_compare.py). Output: [theodore_staffing_compare_results.json](theodore_staffing_compare_results.json). All amounts Australian dollars, 18 clients a day, 473.94 clients a month.", "",
 "## What changed in this note", "",
 "- New: three-way comparison of (a) lab employs collectors for nothing, (b) lab employs and charges GTT a fee, (c) GTT employs and absorbs the lab fee, against (d) today's plan.",
 f"- Reconciled: Anthony's A$48,550 is the repo figure {f(a['op'])}. Two collectors at A$6,682.28 = A$13,364.56, which would give {f(BASE_OP+WAGE_SAVE_QUOTED)}; the repo saving is A$13,364.52, so the A$0.04 gap is rounding.",
 "- Flagged: the repo quotes A$35,186.40 as profit with no GST line. Round 9 puts the after-GST figure at A$23,442.58. Both bases are shown; do not mix them.",
 "- What the A$12,251.35 is: A$25.85 (test A$19.90 plus collection A$5.95) x 473.94 clients. It is the lab's Medicare schedule fee, not wages. Medicare would pay A$22.05 of it per client; the client gap is A$3.80.", "",
 "## Table 1. The three structures and today's plan", "",
 "| Option | Month, repo basis (no GST line) | Month, after GST | Year, after GST | Company tax 25% | Year after company tax |", "|---|---|---|---|---|---|"]
for lab, o in (("(d) Today's plan: GTT employs, Medicare pays", d), ("(a) Lab employs collectors, no recharge", a), ("(c) GTT employs, no Medicare, GTT absorbs lab fee", c)):
    md.append(f"| {lab} | {f(o['op'])} | {f(o['after_gst'])} | {f(o['year_year'])} | {f(o['year_company_tax_25pct'])} | {f(o['year_year_after_company_tax'])} |")
md += ["", f"Difference (a) minus (c): {f(amc['month_op'])} a month on the repo basis, {f(amc['month_after_gst'])} a month after GST, {f(amc['year_after_gst'])} a year after GST ({f(amc['year_after_gst_after_company_tax'])} after 25% company tax). After GST, option (c) is {f(c['after_gst'])} because GTT claims back one eleventh of the lab fee, as the repo does (Case 3, A$12,304.99).", "",
 "## Table 2. Option (b): lab employs collectors and charges GTT a management fee", "",
 "Fee is shown before GST. Assumption: the lab's recharge is taxable (10% GST added) and GTT claims the credit, matching how the repo treats the lab fee. Last column is the worst case where GTT cannot claim.", "",
 "| Fee as share of the A$13,364.52 wage cost | Fee before GST | Invoice with GST | Profit a month after GST | Against today's plan | Year after company tax | Month if no credit |", "|---|---|---|---|---|---|---|"]
for s in sweep:
    md.append(f"| {int(round(s['share_of_wage_cost']*100))}% | {f(s['fee_ex_gst'])} | {f(s['invoice_incl_gst'])} | {f(s['profit_after_gst'])} | {f(s['vs_baseline'])} | {f(s['annual_after_company_tax'])} | {f(s['profit_if_no_itc'])} |")
md += ["", f"- Break-even against today's plan ({f(BASE_GST)}): fee {f(bb['equal_to_baseline']['fee_ex_gst'])} before GST ({f(bb['equal_to_baseline']['invoice_incl_gst'])} invoiced). That is the full wage cost: any fee above the wages saved leaves GTT worse off than employing them itself. If GTT cannot claim the credit, break-even is an invoice of {f(bb['if_gtt_cannot_claim_itc']['equal_to_baseline_invoice_incl'])}.",
 f"- Equal to option (c) ({f(c['after_gst'])}): fee {f(bb['equal_to_option_c']['fee_ex_gst'])} before GST. That is above the wage cost, so a fee inside the sweep never makes (b) worse than (c).", "",
 "## Table 3. Optional: lab pays GTT rent for the collection room (illustrative, valuer needed, NOT in repo)", "",
 "Rent shown GST-inclusive; GTT remits one eleventh. Applied to option (a) and to option (b) with a fee of half the wage cost. Lounge rent from the lab: not in repo.", "",
 "| Rent from lab a month | After GST to GTT | Option (a) profit a month | Option (b, half-wage fee) profit a month | Label |", "|---|---|---|---|---|"]
for r in rent:
    md.append(f"| {f(r['rent_incl_gst'])} | {f(r['net_of_gst'])} | {f(r['a_profit_after_gst'])} | {f(r['b_at_half_wage_profit'])} | {r['label']} |")
md += ["", "## Compliance notes", "",
 "- A recharge paid by GTT to the lab for staff is a commercial service charge. Set it at a documented market rate for the work done.",
 "- Any money flowing from the lab to GTT must be market rent only, for space actually used, set by a valuer. It must not vary with doctor requests, bookings or client numbers. Catherine to confirm before any figure goes in a contract.",
 "- Pregnant-client price: the repo has A$0 (lab bulk bills) or A$3.80 (lab bills the full fee). Both are paid to the lab, so GTT revenue is unchanged and no payback period applies. If GTT absorbed the fee (c), the price that restores today's profit is A$275.85, GST aside, per the repo.",
 "- Nothing here is signed or quoted. Lab fees, recharge and rent are unknown until a lab answers in writing.", ""]
open(os.path.join(here, "STAFFING-COMPARE.md"), "w").write("\n".join(md))
print(json.dumps(dict(options=out["options"], a_minus_c=amc, reconcile=out["reconcile"], b_break_even=bb), indent=1))
