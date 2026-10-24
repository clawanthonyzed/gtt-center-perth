"""Theodore R16 (2026-10-24). EXTENDS theodore_r15.py (imported; it imports theodore_r14.py and theodore_r13.py).
No second calculator: package split from r15.split_pkg, card fee from r15.fee_pct, payroll tax from r14.ptax,
taxable midwife wages from r15.mw_taxable_month, midwife hourly cost and fixed costs from r14.hourly / r14.COST,
three-company running cost from r15.run3. Repo base numbers are read, never changed.
New in R16: Anthony's prices (package 1 = A$300 total, lounge A$162.15; package 2 = A$350 total, lounge A$212.15),
GST shown both ways, mother's out of pocket, and ROSTERED midwives (1 or 2, 9 to 5 Monday to Friday) instead of
consult-driven hours. Labels: R repo, V official source, E estimate, Q quote needed. AUD.
"""
import contextlib, importlib.util, io, json, math, os

HERE = os.path.dirname(os.path.abspath(__file__))
R15 = os.path.join(HERE, "..", "L10-r15", "theodore_r15.py")
spec = importlib.util.spec_from_file_location("theodore_r15", R15)
r15 = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(r15)          # r15 rewrites its own results json on import; content is unchanged (checked with git status)
r14, r13 = r15.r14, r15.r13
f2 = r15.f2
WEEKS_M = r14.WEEKS_M
AFTER_GST = r15.AFTER_GST                 # R 23,442.58 repo profit after GST (R9/R11 planning basis)
CLIENTS = 396                             # R Monday to Friday AM visits a month
LAB, CONSULT, REPO_LOUNGE = 27.85, 110.0, 250.0
REBATE = 75.65 + 16.95 + 6.80             # V items: 82110 consult + 66548 + 73938 = 99.40
PKGS = {"package_1": 300.0, "package_2": 350.0}
out = {"generated": "2026-10-24", "imports": "theodore_r15.py -> theodore_r14.py -> theodore_r13.py", "labels": "R repo, V official, E estimate, Q quote needed"}

# ---------------- Part D. prices, GST both ways, out of pocket, net group revenue ----------------
def price_row(P):
    s = r15.split_pkg(P)                                  # GST-inclusive reading (recommended)
    lounge = s["lounge"]
    on_top_gst = f2(lounge * 0.10)
    incl = dict(client_pays=P, lounge_incl_gst=lounge, gst=s["lounge_gst"], lounge_ex_gst=s["lounge_ex_gst"],
                gst_free_part=f2(CONSULT + LAB), taxable_part=lounge,
                group_keeps_incl_gst=s["group_keeps_gross"], group_keeps_ex_gst=s["group_keeps_ex_gst"])
    top = dict(client_pays=f2(P + on_top_gst), lounge_ex_gst=lounge, gst=on_top_gst, lounge_incl_gst=f2(lounge + on_top_gst),
               gst_free_part=f2(CONSULT + LAB), taxable_part=f2(lounge + on_top_gst),
               group_keeps_incl_gst=f2(CONSULT + lounge + on_top_gst), group_keeps_ex_gst=f2(CONSULT + lounge))
    card_Y = f2(r15.fee_pct(P - LAB))                      # Option Y: lab paid at the lab, card fee only on GTT's part
    net_rev = f2(s["group_keeps_ex_gst"] - card_Y)
    repo_ex = REPO_LOUNGE / 1.1
    return dict(package=P, gst_inclusive=incl, gst_on_top=top, out_of_pocket_after_rebate=f2(P - REBATE),
                out_of_pocket_on_top=f2(P + on_top_gst - REBATE), out_of_pocket_vs_repo_250=f2(P - REBATE - REPO_LOUNGE),
                card_fee_option_Y=card_Y, net_group_revenue_per_client_ex_gst_after_card=net_rev,
                repo_revenue_per_client_ex_gst=f2(repo_ex), change_per_client_vs_repo_before_midwife=f2(net_rev - repo_ex),
                month_396_net_group_revenue=f2(net_rev * CLIENTS), month_396_repo_revenue=f2(repo_ex * CLIENTS),
                month_396_change_before_midwife=f2((net_rev - repo_ex) * CLIENTS),
                meets_250_into_gtt_ex_gst=s["group_keeps_ex_gst"] >= 250)
pD = {k: price_row(P) for k, P in PKGS.items()}
pD["reference"] = dict(break_even_r15_A=r15.be5["break_even_price_A"], break_even_r15_B=r15.be5["break_even_price_B"],
                       like_for_like=387.85, like_for_like_out_of_pocket=f2(387.85 - REBATE),
                       price_where_mother_pays_same_as_repo_250=f2(REPO_LOUNGE + REBATE),
                       rebate=f2(REBATE), rebate_mix_average=f2(r15.mix_rebate))
out["partD_pricing"] = pD

# ---------------- Part G. rostered midwives 9 to 5 Monday to Friday ----------------
def rostered(k, case="base", grossup=False):
    c = r14.COST[case]; mx = r14.MIX[case]
    fee, ben, mins = r14.mix_stats(mx)
    hours_w = r14.FTE_H * k                                # 38 ordinary hours each (9 to 5 less a 30 min unpaid break, close to 38) E
    cap_w = hours_w * c["util"] * 60 / (mins + c["admin"])
    cap_m = cap_w * WEEKS_M
    in_person = mx.get("82100", 0) + (1 - mx.get("82100", 0)) * (1 - c["tele"])
    rooms = max(1, math.ceil(k * in_person - 1e-9))
    rate = r14.hourly(c, 0.0)                              # weekday only, R14 on-cost 1.20
    if grossup: rate = rate / c["oncost"] * r15.bu_worked  # permanent staff with leave covered (R15 1.3)
    wage_m = hours_w * WEEKS_M * rate
    fixed_m = k * ((r14.AHPRA + c["pi"] + c["cpd"]) / 12 + c["sw_m"] + c["equip"] / 60) + rooms * r14.ROOM_M2 * r14.RENT
    return dict(midwives=k, hours_week=hours_w, capacity_week=round(cap_w, 1), capacity_month=round(cap_m, 1), rooms=rooms,
                hourly_cost=f2(rate), wage_month=f2(wage_m), fixed_month=f2(fixed_m), consum_per_consult=c["consum"])

def group(P, k, case="base", grossup=False, addons=False):
    m = rostered(k, case, grossup)
    n = min(CLIENTS, m["capacity_month"])                 # consult (bundle) clients; the rest keep the repo A$250 lounge-only price (E)
    s = r15.split_pkg(P)
    consult_rev = CONSULT * n
    lounge_delta = n * (s["lounge"] / 1.1 - REPO_LOUNGE / 1.1)
    card = n * r15.fee_pct(P - LAB)
    mid_cost = m["wage_month"] + m["fixed_month"] + n * m["consum_per_consult"]
    tax_mid = (r15.mw_taxable_month(m["wage_month"], r15.bu_worked) * r15.LEAVE_GROSSUP if grossup
               else r15.mw_taxable_month(m["wage_month"], 1.20)) * 12
    add_y = r15.ADDON_TAXABLE_Y if addons else 0.0
    base_y = r15.REPO_TAXABLE_Y + add_y
    pt_repo = r14.ptax(r15.REPO_TAXABLE_Y) / 12
    pt_added = (r14.ptax(base_y + tax_mid) - r14.ptax(r15.REPO_TAXABLE_Y)) / 12
    add_cost = sum(a["loaded_month"] for a in r15.addons) if addons else 0.0
    three = r15.run3["base"]["total_month"]
    before = AFTER_GST + consult_rev + lounge_delta - card - mid_cost - pt_repo - pt_added - three - add_cost
    ctax = max(0.0, before) * 0.25
    return dict(package=P, midwives=k, consult_clients=round(n, 1), share_of_396=round(n / CLIENTS, 3), repo_after_gst=AFTER_GST,
                consult_income=f2(consult_rev), lounge_repricing_ex_gst=f2(lounge_delta), card_fees=-f2(card),
                midwife_wages=-m["wage_month"], midwife_fixed_and_consumables=-f2(m["fixed_month"] + n * m["consum_per_consult"]),
                payroll_tax_repo_wages=-f2(pt_repo), payroll_tax_added=-f2(pt_added), payroll_tax_group_total=-f2(pt_repo + pt_added),
                receptionist_host_addon=-f2(add_cost), three_company_cost=-three,
                group_before_company_tax=f2(before), company_tax_25=-f2(ctax), group_after_company_tax=f2(before - ctax),
                change_vs_repo_after_gst=f2(before - AFTER_GST), hourly_cost=m["hourly_cost"], capacity_month=m["capacity_month"])

G = {}
for pk, P in PKGS.items():
    for k in (1, 2):
        G[f"{pk}|{k}_midwife"] = {"base": group(P, k), "leave_covered": group(P, k, grossup=True),
                                  "with_receptionist_host": group(P, k, addons=True),
                                  "adverse_cost": group(P, k, case="adverse"), "favourable_cost": group(P, k, case="favourable")}
G["reference_no_midwife"] = dict(repo_after_gst=AFTER_GST, payroll_tax=-f2(r14.ptax(r15.REPO_TAXABLE_Y) / 12),
                                 three_company=-r15.run3["base"]["total_month"],
                                 group_before_company_tax=f2(AFTER_GST - r14.ptax(r15.REPO_TAXABLE_Y) / 12 - r15.run3["base"]["total_month"]))
G["rostered"] = {k: rostered(k) for k in (1, 2, 3)}
G["full_396_three_midwives"] = {pk: group(P, 3) for pk, P in PKGS.items()}
out["partG_rostered_midwives"] = G

# ---------------- Part E. lab money float (Option X) and interest ----------------
float_X = r15.float_held                                   # A$ held for the lab at 396 a month (R15)
out["partE_lab_money"] = dict(float_held_option_X=float_X,
                              interest_year_at_4pct_E=f2(float_X * 0.04), interest_year_at_5pct_E=f2(float_X * 0.05),
                              note="Interest on the lab's money belongs to the lab unless the written agency agreement says otherwise; GTT keeping it could be a benefit from a pathology provider to a requester (Part IIBA, Catherine). E rates.")

# ---------------- Part A. three companies: extra cost of the parent alone ----------------
par = dict(asic_review=r15.ASIC_REVIEW, accountant=2500, bookkeeping=600, bank=240)
par["total_year"] = sum(par.values()); par["total_month"] = f2(par["total_year"] / 12)
out["partA_parent_cost_E"] = par
out["partA_inter_company_gst_example"] = dict(room_licence_month=960, gst_if_no_group=96.0, credit_claimed_by_medical=96.0, net_gst=0.0,
                                              note="Medical makes GST-free supplies, so it can still claim the GST credit (GST-free is not input taxed). Cash timing only.")

json.dump(out, open(os.path.join(HERE, "theodore_r16_results.json"), "w"), indent=1)

if __name__ == "__main__":
    for k, v in pD.items(): print(k, json.dumps(v))
    for k, v in G.items():
        if "|" in k:
            for sc, g in v.items(): print(k, sc, g["consult_clients"], g["payroll_tax_group_total"], g["group_before_company_tax"], g["group_after_company_tax"], g["change_vs_repo_after_gst"], g["hourly_cost"])
    print(G["rostered"]); print(G["reference_no_midwife"]); print({k: (v["group_before_company_tax"], v["group_after_company_tax"]) for k, v in G["full_396_three_midwives"].items()})
    print(out["partE_lab_money"]); print(par)
    print(json.dumps(G["package_1|1_midwife"]["base"], indent=0)); print(json.dumps(G["package_2|2_midwife"]["base"], indent=0))
