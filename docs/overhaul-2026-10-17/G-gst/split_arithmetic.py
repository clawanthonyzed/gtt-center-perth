"""GTT Center Perth, workstream G (B2a, B2b): GST split arithmetic overlay.

This is NOT a replacement for tools/master_financial_model.py. It takes the repo's own
steady-state outputs as inputs and only applies the GST rule (price/11) to a chosen
GST-free share of the AM package. Every input is a repo figure:
  N          = 18 clients x 26.33 trading days = 473.94 clients a month (MODEL-WORKINGS.md)
  PM_REV     = A$24,585.37 (3-way model, steady state PM services)
  OP250      = A$35,186.40 net operating profit at A$250, GST-inclusive, no GST line
  CREDITS    = A$1,262.58 input tax credits on non-wage costs (3-way model section 3d)
  Price move = N x (P - 250) added to operating profit (repo fee-sensitivity basis,
               A$4,739.40 a month per A$10; demand held constant, elasticity not modelled)
GST rule: GST = 1/11 of the GST-inclusive price of the taxable part (GST Act s 9-75, 9-80;
GSTR 2001/8 para 114). GST-free supplies keep their input tax credits (GST Act s 38-1).
"""
import csv, sys
N = 18 * 26.33
PM_REV = 24585.37
OP250 = 35186.40
CREDITS = 1262.58
GST_STRESS_250 = 23442.58          # repo GST-stress, monthly
NONWAGE = 14288.34                 # rent 8000 + overhead 5088.34 + goods 1200 (3-way model)
# value-based evidence (see GST-SPLIT-MODEL.md section 4)
MBS_VISIT = 25.85                  # L workstream: item 66548 A$19.90 + collection episode 73928 A$5.95 per visit
MBS_COLLECT = 5.95                 # item 73928 patient episode initiation (collection) alone
PHLEB_WAGES = 9075.00 + 618.75 * 4.33          # repo cost_ramp_model: weekday 2 x 34.375 x 6 x 22 + Saturday 2 x 51.5625 x 6 x 4.33
ONCOST = 1.137                                  # super 12% + workers comp 1.7%
PHLEB_PER_CLIENT = PHLEB_WAGES * ONCOST / N
CONSUMABLES_PER_CLIENT = 1200.00 / N
A_COST = PHLEB_PER_CLIENT + CONSUMABLES_PER_CLIENT
AM_VAR_LABOUR = 71145.86
THERAPIST_PER_CLIENT = (AM_VAR_LABOUR - PHLEB_WAGES * ONCOST) / N
COST_SHARE = A_COST / (A_COST + THERAPIST_PER_CLIENT)

def r(x):
    v = round(x + 0.0, 2)
    return 0.0 if v == 0 else v

def row(P, label, a, status):
    am_rev = N * P
    op = OP250 + N * (P - 250)
    total_rev = am_rev + PM_REV
    gst_pm = 2235.04            # repo figure (PM_REV / 11 rounded up in the 3-way model: A$13,006.40 total GST on sales)
    out = {"price": P, "split": label, "component_A_share_pct": r(a * 100), "component_A_per_client": r(a * P),
           "component_B_per_client": r((1 - a) * P), "legal_status": status}
    for tag, share in (("qualifies", a), ("not_qualifying", 0.0)):
        gst_a_free_part = 0.0                       # GST on Component A is nil when it qualifies
        gst_a_taxable_part = round(a * P * N / 11, 2) if tag == "not_qualifying" else 0.0
        if tag == "not_qualifying":
            gst_am = round(am_rev / 11, 2)                 # whole AM package taxable
            gst_b = round(gst_am - gst_a_taxable_part, 2)
        else:
            gst_b = round((1 - a) * P * N / 11, 2)
            gst_am = gst_b
        gst_total = gst_am + gst_pm
        net_gst = gst_total - CREDITS
        net_profit = op - net_gst
        out.update({
            f"{tag}_GST_on_component_A": r(gst_a_taxable_part),
            f"{tag}_GST_on_component_B": r(gst_b),
            f"{tag}_GST_on_PM": r(gst_pm),
            f"{tag}_input_tax_credits": r(CREDITS),
            f"{tag}_net_GST_payable_month": r(net_gst),
            f"{tag}_net_revenue_ex_GST_month": r(total_rev - gst_total),
            f"{tag}_net_profit_month": r(net_profit),
            f"{tag}_cashflow_month_steady": r(net_profit),
            f"{tag}_net_profit_year1": r(r(net_profit) * 12),
            f"{tag}_net_GST_payable_year": r(r(net_gst) * 12),
            f"{tag}_year1_cash_after_BAS": r(r(op) * 12 - r(net_gst) * 11),
        })
    full = out["not_qualifying_net_profit_month"]
    out["upside_vs_fully_taxable_month"] = r(out["qualifies_net_profit_month"] - full) + 0.0
    out["upside_vs_fully_taxable_year"] = r(r(out["qualifies_net_profit_month"] - full) * 12) + 0.0
    if P == 250:
        out["qualifies_vs_repo_GST_stress_month"] = r(out["qualifies_net_profit_month"] - GST_STRESS_250)
    return out

def row_base(P):
    op = OP250 + N * (P - 250)
    return op - ((N * P + PM_REV) / 11 - CREDITS)

def ratios(P):
    return [
        ("0/100 (nothing to A)", 0.0, "AVAILABLE: this is the law as it stands for GTT's own charges"),
        ("50/50", 0.5, "HYPOTHETICAL: needs a GTT supply of Component A that meets s 38-7 or s 38-10; none in the current model"),
        ("60/40", 0.6, "HYPOTHETICAL: as above"),
        ("70/30", 0.7, "HYPOTHETICAL: as above"),
        ("100/0 (all to A)", 1.0, "HYPOTHETICAL ONLY: wellness lounge priced at nil; GSTR 2001/8 paras 81ZD, 96; Div 165"),
        ("Value split, market anchor (whole MBS lab visit A$25.85)", MBS_VISIT / P, "ARITHMETIC OF THE LAB'S SERVICE: that value is the lab's, billed to Medicare, not GTT revenue"),
        ("Value split, market anchor (MBS collection episode only A$5.95)", MBS_COLLECT / P, "ARITHMETIC OF THE LAB'S SERVICE: the collection fee is the lab's, not GTT revenue"),
        ("Value split, cost share (collection cost vs treatment cost)", COST_SHARE, "HYPOTHETICAL: cost-only basis; GSTR 2001/8 para 112 warns it is unreliable if mark-ups differ"),
    ]

if __name__ == "__main__":
    rows = []
    for P in (250, 200, 300):
        for label, a, status in ratios(P):
            rows.append(row(P, label, a, status))
    with open(sys.argv[1], "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)
    print("N", N, "PHLEB_PER_CLIENT", r(PHLEB_PER_CLIENT), "CONS", r(CONSUMABLES_PER_CLIENT), "A_COST", r(A_COST),
          "THER", r(THERAPIST_PER_CLIENT), "COST_SHARE", round(COST_SHARE * 100, 2), "MBS share @250", round(MBS_VISIT/250*100,2))
    print("check P250 a0 net", rows[0]["not_qualifying_net_profit_month"], "(expect 23442.58)")
    print("check P250 a1 net", rows[4]["qualifies_net_profit_month"], "year", rows[4]["qualifies_net_profit_year1"])
    print("per-point", r(N * 2.5 / 11), "per 1 pct", "all", r(N * 250 / 11))
    # credits sensitivity at 250
    for cred in (0, CREDITS, NONWAGE / 11):
        print("credits", r(cred), "fully taxable net", r(OP250 - ((N*250+PM_REV)/11 - cred)),
              "70pct qualifies", r(OP250 - ((N*250*0.3+PM_REV)/11 - cred)))
