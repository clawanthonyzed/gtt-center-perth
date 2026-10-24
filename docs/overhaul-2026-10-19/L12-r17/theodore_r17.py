"""Theodore R17 (2026-10-24). EXTENDS theodore_r16.py (imported; it imports r15 -> r14 -> r13). No second calculator.
Reused: r15.split_pkg (package split), r15.fee_pct (card fee), r14.mw (midwife hours, wages, fixed costs from consult demand),
r14.ptax (WA payroll tax), r15.mw_taxable_month, r15.run3 (three-company cost), r14.WAGES (Nurses Award rates), r15.bu_paid/bu_worked.
Anthony's fixed decisions (not re-opened): Structure B; A$250 minimum reaches GTT as a whole (Medical + Lounge, lab excluded);
lounge A$162.15 / A$212.15, client totals A$300 / A$350; plan on the lower; 2 packages; tax consolidation + GST group in year 1;
Route B; 2 midwives on the books splitting Mon-Sat; no hosts, venue manager only.
New in R17: every one of the repo's 473.94 six-day AM clients buys a package (R16 wrongly left overflow clients on the old A$250);
like-for-like break-even with the same structure costs; GST rounding half-up (ATO rule); lab float interest; room licence; pay types.
Labels: R repo, V official source, E estimate, Q quote needed. AUD.
"""
import contextlib, importlib.util, io, json, os
from decimal import Decimal, ROUND_HALF_UP

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("theodore_r16", os.path.join(HERE, "..", "L11-r16", "theodore_r16.py"))
r16 = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(r16)          # r16/r15 rewrite their own results json on import; content unchanged (checked with git status)
r15, r14 = r16.r15, r16.r14
f2 = r15.f2
def c2(x): return float(Decimal(str(x)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))   # cent rounding, 0.5 rounds up

AFTER_GST = r16.AFTER_GST                  # R 23,442.58 repo profit after GST (planning basis)
CL6 = r14.CLIENTS_M                        # R 473.94 six-day AM clients a month (118,485 / 250)
CL5 = r14.VISITS_M                         # R 396 Mon-Fri
LAB, CONSULT, OLD = 27.85, 110.0, 250.0
PKG = {"P1": 300.0, "P2": 350.0}
SAT = 1 / 6                                # midwife hours spread Mon-Sat: one day in six is Saturday (E)
out = {"generated": "2026-10-24", "imports": "theodore_r16.py -> r15 -> r14 -> r13", "labels": "R repo, V official, E estimate, Q quote"}

# ---------- Q1 / Q7: what reaches GTT, GST both ways ----------
def reach(P):
    lounge = P - CONSULT - LAB
    gst_in = c2(lounge / 11); ex_in = c2(lounge - gst_in)
    gst_top = c2(lounge * 0.10)
    card = c2(r15.fee_pct(P - LAB))
    return dict(client_pays=P, consult_medical_gst_free=CONSULT, lab_gst_free_not_gtt=LAB, lounge_incl_gst=c2(lounge),
                lounge_gst_inside=gst_in, lounge_ex_gst=ex_in,
                gtt_receives_incl_gst=c2(CONSULT + lounge), gtt_receives_ex_gst=c2(CONSULT + ex_in),
                card_fee=card, gtt_ex_gst_after_card=c2(CONSULT + ex_in - card),
                clears_250_incl=CONSULT + lounge >= 250, clears_250_ex_gst=CONSULT + ex_in >= 250,
                gst_on_top=gst_top, lounge_with_gst_on_top=c2(lounge + gst_top), client_pays_gst_on_top=c2(P + gst_top),
                gtt_ex_gst_if_gst_on_top=c2(CONSULT + lounge))
Q1 = {k: reach(P) for k, P in PKG.items()}
Q1["r15_old_example_250_all_in"] = reach(250.0)
out["Q1_reach_gtt"] = Q1

def bas(P, n):
    r = reach(P)
    return dict(clients=round(n, 2), gst_collected_lounge=c2(r["lounge_gst_inside"] * n), gst_free_consult_sales=c2(CONSULT * n),
                taxable_lounge_sales_incl_gst=c2(r["lounge_incl_gst"] * n), lab_on_gtt_bas=0.0,
                gst_collected_if_on_top=c2(r["gst_on_top"] * n))
out["Q7_bas_month"] = {f"{k}|{lab}": bas(P, n) for k, P in PKG.items() for lab, n in (("396", CL5), ("474", CL6))}

# ---------- Q8: client, Medicare, GTT, lab ----------
REB = {"82110_example": 75.65, "82105_short": 32.95, "mix_avg_base": r14.mix_stats(r14.MIX["base"])[1]}
TEST_REB = {"73938_as_r16": 16.95 + 6.80, "73928_as_repo": 16.95 + 5.10}   # repo CS item 8 says 73928 (A$5.95); lab A$27.85 = 19.90 + 7.95 (73938)
Q8 = {}
for k, P in PKG.items():
    r = reach(P)
    for rk, rv in REB.items():
        back = rv + TEST_REB["73938_as_r16"]
        Q8[f"{k}|{rk}"] = dict(client_pays=P, rebate_back=f2(back), mother_net=f2(P - back), gtt_receives_incl_gst=r["gtt_receives_incl_gst"],
                               gtt_receives_ex_gst=r["gtt_receives_ex_gst"], lab_receives=LAB)
Q8["note_test_rebate_alt_73928"] = f2(TEST_REB["73928_as_repo"])
out["Q8_money_map"] = Q8

# ---------- group P&L: every client on a package, midwife hours from consult demand (r14.mw) ----------
def group(mix_p1, case="base", consult_mix=None, n=CL6, oncost_grossup=False):
    mw = r14.mw(case, n, "bulk_billed", SAT, mixover=consult_mix)
    wage = mw["wage_month"]
    if oncost_grossup: wage = wage / r14.COST[case]["oncost"] * r15.bu_worked
    shares = {"P1": mix_p1, "P2": 1 - mix_p1}
    rev = lounge_delta = card = 0.0
    for k, s in shares.items():
        r = reach(PKG[k]); m = n * s
        rev += m * (CONSULT + r["lounge_ex_gst"])
        lounge_delta += m * (r["lounge_ex_gst"] - OLD / 1.1)
        card += m * r["card_fee"]
    consult_rev = CONSULT * n
    consum = mw["consumables_month"]; fixed = mw["fixed_month"]
    tax_mid = r15.mw_taxable_month(wage, r15.bu_worked if oncost_grossup else r14.COST[case]["oncost"]) * 12
    pt_repo = r14.ptax(r15.REPO_TAXABLE_Y) / 12
    pt_added = (r14.ptax(r15.REPO_TAXABLE_Y + tax_mid) - r14.ptax(r15.REPO_TAXABLE_Y)) / 12
    three = r15.run3["base"]["total_month"]
    before = AFTER_GST + consult_rev + lounge_delta - card - wage - consum - fixed - pt_repo - pt_added - three
    return dict(clients=round(n, 1), p1_share=mix_p1, gtt_revenue_ex_gst=f2(rev), consult_income=f2(consult_rev),
                lounge_change_vs_old_250=f2(lounge_delta), card_fees=-f2(card), midwife_hours_week=mw["paid_hours_week"],
                midwife_fte=mw["fte"], midwife_wages=-f2(wage), midwife_fixed_consumables=-f2(fixed + consum),
                payroll_tax_group=-f2(pt_repo + pt_added), three_company=-three,
                group_before_company_tax=f2(before), company_tax_25=-f2(max(0, before) * .25), group_after_company_tax=f2(before - max(0, before) * .25),
                change_vs_like_for_like_baseline=f2(before - BASELINE), change_vs_repo_23443=f2(before - AFTER_GST))
BASELINE = f2(AFTER_GST - r14.ptax(r15.REPO_TAXABLE_Y) / 12 - r15.run3["base"]["total_month"])   # same structure costs, no midwife (R16: 21,971)
SHORT = {"82105": 1.0}
MIXES = {"100% P1": 1.0, "70/30": 0.7, "50/50": 0.5, "100% P2": 0.0}
Q9 = {}
for consult, cm in (("base_mix_34.5min", None), ("short_82105_10min", SHORT)):
    for ml, s in MIXES.items():
        Q9[f"{consult}|{ml}"] = {"permanent_r14_oncost": group(s, consult_mix=cm), "permanent_leave_covered": group(s, consult_mix=cm, oncost_grossup=True)}
out["Q9_packages_mix"] = Q9
out["baseline_same_costs_no_midwife"] = BASELINE

# ---------- Q6: break-even single price (all clients at one price), like-for-like ----------
def be_price(consult_mix=None, target=None):
    target = BASELINE if target is None else target
    saved = dict(PKG)
    lo, hi = 250.0, 600.0
    for _ in range(60):
        mid = (lo + hi) / 2
        PKG["P1"] = mid
        ok = group(1.0, consult_mix=consult_mix)["group_before_company_tax"] >= target
        hi, lo = (mid, lo) if ok else (hi, mid)
    PKG.update(saved)
    return round(hi, 2)
per_client_before = f2(OLD / 1.1)
mw_base = r14.mw("base", CL6, "bulk_billed", SAT)
mw_short = r14.mw("base", CL6, "bulk_billed", SAT, mixover=SHORT)
Q6 = dict(before_per_client_ex_gst=per_client_before, before_incl_gst=OLD,
          p1_per_client_ex_gst_after_card=Q1["P1"]["gtt_ex_gst_after_card"], p2_per_client_ex_gst_after_card=Q1["P2"]["gtt_ex_gst_after_card"],
          midwife_cost_per_client_base=f2((mw_base["wage_month"] + mw_base["fixed_month"] + mw_base["consumables_month"]) / CL6),
          midwife_cost_per_client_short=f2((mw_short["wage_month"] + mw_short["fixed_month"] + mw_short["consumables_month"]) / CL6),
          payroll_tax_added_per_client_base=f2(-(group(1.0)["payroll_tax_group"] + r14.ptax(r15.REPO_TAXABLE_Y) / 12) / CL6),
          break_even_price_base_mix=be_price(), break_even_price_short_consult=be_price(SHORT),
          break_even_vs_repo_23443_base=be_price(target=AFTER_GST), r15_figure=338, r15_like_for_like=387.85)
out["Q6_break_even"] = Q6

# ---------- Q2 / Q4: lab money float and interest ----------
RATES = {"big4_business_saver_1.00pct": 0.01, "best_online_saver_4.35pct": 0.0435}   # E: CBA BOS 0.40-1.30% (15 May 2026), Bank Australia 4.35% (20 May 2026); not verified current
def float_row(n, lead_days, settle):
    daily = LAB * n / 30.4
    hold = lead_days + {"weekly": 3.5, "monthly": 15.2}[settle]
    bal = daily * hold
    return dict(clients=round(n, 1), lead_days=lead_days, settle=settle, average_balance=f2(bal),
                **{f"interest_year_{k}": f2(bal * v) for k, v in RATES.items()})
out["Q4_float_interest"] = [float_row(n, lead, st) for n in (CL5, CL6) for lead in (21, 0) for st in ("weekly", "monthly")]
gtt_own = Q1["P1"]["gtt_receives_incl_gst"] * CL5 / 30.4 * 21     # GTT's own prepaid package money held 21 days at 396 (E)
out["Q4_gtt_own_cash"] = dict(average_prepaid_balance_396=f2(gtt_own), **{f"interest_year_{k}": f2(gtt_own * v) for k, v in RATES.items()})

# ---------- Q3: room licence Medical -> Lounge ----------
RENT_M, AREA = 8000.0, 200.0                 # R rent budget A$8,000 on 200 sqm planning footprint (CS s52)
EXCL = {"consult_room": 13.0, "collection_room_1": 18.0, "collection_room_2": 18.0}   # consult 12-14 (Grace R16 E), collection 18 (repo)
OUTG = 126.90                                 # E: outgoings A$/sqm/yr, Wembley listing in repo RENT-ECONOMICS-FORENSICS (one data point)
a = sum(EXCL.values())
lic = dict(exclusive_sqm=a, share_of_footprint=round(a / AREA, 4), rent_per_sqm_month=RENT_M / AREA, rent_part=f2(a * RENT_M / AREA),
           outgoings_part_E=f2(a * OUTG / 12))
lic["licence_ex_gst"] = f2(lic["rent_part"] + lic["outgoings_part_E"]); lic["gst_if_no_group"] = c2(lic["licence_ex_gst"] * .1)
lic["licence_incl_gst_if_no_group"] = f2(lic["licence_ex_gst"] + lic["gst_if_no_group"]); lic["r15_r16_figure"] = 960.0
out["Q3_room_licence"] = lic

# ---------- Q10: midwife pay types (Nurses Award MA000034 RN level 2 pay point 4, r14.WAGES) ----------
o, s, co, cs = r14.WAGES["RN L2 pp4"]
perm_paid = (o * (1 - SAT) + s * SAT)
cas = (co * (1 - SAT) + cs * SAT)
Q10 = {}
for label, hw in (("short_consult_hours", mw_short["paid_hours_week"]), ("base_mix_hours", mw_base["paid_hours_week"])):
    Q10[label] = dict(hours_week=hw,
        casual=dict(rate_blend=f2(cas), loaded=f2(cas * (1 + r15.SUPER + r15.WC)), month=f2(hw * r14.WEEKS_M * cas * (1 + r15.SUPER + r15.WC))),
        part_or_full_time=dict(rate_blend=f2(perm_paid), loaded_paid_hour=f2(perm_paid * r15.bu_paid), loaded_worked_hour=f2(perm_paid * r15.bu_worked),
                               month_leave_covered=f2(hw * r14.WEEKS_M * perm_paid * r15.bu_worked)))
out["Q10_pay_types"] = Q10

json.dump(out, open(os.path.join(HERE, "theodore_r17_results.json"), "w"), indent=1)
if __name__ == "__main__":
    print(json.dumps({k: out[k] for k in ("Q1_reach_gtt", "Q6_break_even", "Q3_room_licence", "Q10_pay_types", "Q4_gtt_own_cash")}, indent=0))
    for k, v in Q9.items(): print(k, {kk: (vv["midwife_hours_week"], vv["midwife_fte"], vv["gtt_revenue_ex_gst"], vv["group_before_company_tax"], vv["group_after_company_tax"], vv["change_vs_like_for_like_baseline"]) for kk, vv in v.items()})
    for r in out["Q4_float_interest"]: print(r)
    for k, v in out["Q7_bas_month"].items(): print(k, v)
    for k, v in Q8.items(): print(k, v)
    print("baseline", BASELINE)
