"""Theodore R15 (2026-10-24). EXTENDS theodore_r14.py (imported, which itself imports theodore_r13.py). No second calculator:
every midwife P&L figure comes from r14.mw(); payroll tax from r14.ptax(); repo base numbers are read, never changed.
Labels: R repo figure, V official source, E estimate, Q quote needed. AUD. Plain English.
Parts: 1 loaded midwife cost, 2 scaled midwife P&L (bulk billed vs Structure B), 3 payroll tax, 4 workforce, 5 three-tier structure,
6 Structure B cash flow, 7 Route 1 step costs.
"""
import contextlib, copy, importlib.util, io, json, math, os

HERE = os.path.dirname(os.path.abspath(__file__))
R14 = os.path.join(HERE, "..", "L9-r14", "theodore_r14.py")
spec = importlib.util.spec_from_file_location("theodore_r14", R14)
r14 = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(r14)
r13 = r14.r13

WEEKS_M = r14.WEEKS_M
BASE_NET = r14.BASE_NET                      # R 35,186.40 (no GST line)
AFTER_GST = r13.BASE_NET_MONTH_AFTER_GST     # R 23,442.58 (R9/R11 planning basis)
CLIENTS_M = r14.CLIENTS_M                    # R 473.94 (six-day AM clients, 118,485 / 250)
VISITS_M = r14.VISITS_M                      # R 396 (Mon-Fri)
CASES = ("adverse", "base", "favourable")
f2 = lambda x: round(x, 2)

# ---------------- repo payroll (R): data/canonical/cost_ramp.yml cost_table1_m5plus ----------------
REPO = dict(am_weekday=48310.68, am_sat=14262.63, pm_weekday=9808.92, pm_sat=2895.82, opening=7040.00)
REPO_WAGES_M = round(sum(REPO.values()), 2)
assert abs(REPO_WAGES_M - 82318.05) < 0.01
REPO_SUPER_M, REPO_WC_M = 9878.17, 1399.41
assert abs(REPO_WAGES_M * 0.12 - REPO_SUPER_M) < 0.01 and abs(REPO_WAGES_M * 0.017 - REPO_WC_M) < 0.01
REPO_PAYROLL_M = round(REPO_WAGES_M + REPO_SUPER_M + REPO_WC_M, 2)       # 93,595.63

SUPER, WC, AL_LOAD = 0.12, 0.017, 0.175 * 4 / 52           # leave loading 17.5% on 4 weeks (Fair Work rule; applies to permanent staff)
PRODUCTIVE_WEEKS = 52 - (4 + 2 + 2.2)                      # 4 wk annual, 2 wk personal (10 days), ~11 public holidays (E)
LEAVE_GROSSUP = 52 / PRODUCTIVE_WEEKS
MARGINAL_PT = r14.RATE * 15 / 13                           # 6.346% on each extra dollar between 1m and 7.5m
F_PRIV = 110.0 / r14.ITEMS["82110"]["fee"]                 # E: private fee = 1.236 x schedule (anchor A$110 for 82110)

out = {"generated": "2026-10-24", "labels": "R repo, V official, E estimate, Q quote needed"}

# =====================================================================================================
# PART 1. LOADED MIDWIFE COST
# =====================================================================================================
SCEN_A, SCEN_B = "A_50pct_6day", "B_80pct_6day"
nA, satA, _ = r14.SCEN[SCEN_A]; nB, satB, _ = r14.SCEN[SCEN_B]

def step_table(case, sat_share, n_month):
    c = r14.COST[case]; o, s, _, _ = r14.WAGES[c["rate"]]
    blend = o * (1 - sat_share) + s * sat_share
    g = r14.mw(case, n_month, "bulk_billed", sat_share)
    paid_h_m = g["paid_hours_week"] * WEEKS_M
    mx = r14.MIX[case]; fee, ben, mins = r14.mix_stats(mx)
    clin_h_m = n_month * mins / 60
    s1 = o; s2 = blend
    s3 = s2 * (1 + SUPER); s4 = s3 + s2 * AL_LOAD; s5 = s4 + s2 * WC
    s6 = s5 * LEAVE_GROSSUP
    s7 = s6 + (s2 * (1 + SUPER + AL_LOAD)) * LEAVE_GROSSUP * MARGINAL_PT
    r14_wage = g["wage_per_hour"]
    cons_h = g["consumables_month"] / paid_h_m; fixed_h = g["fixed_month"] / paid_h_m
    allin_paid = (g["wage_month"] + g["consumables_month"] + g["fixed_month"]) / paid_h_m
    util_share = clin_h_m / paid_h_m
    return dict(case=case, award_rate=c["rate"], ordinary=f2(s1), blended_with_saturday=f2(s2), plus_super_12pct=f2(s3),
                plus_leave_loading=f2(s4), plus_workers_comp_1_7pct=f2(s5), builtup_multiplier_paid_hour=round(s5 / s2, 4),
                paid_leave_grossup_factor=round(LEAVE_GROSSUP, 4), loaded_per_worked_hour=f2(s6), plus_payroll_tax_marginal=f2(s7),
                r14_oncost_multiplier=c["oncost"], r14_wage_per_paid_hour=r14_wage,
                r14_consumables_per_paid_hour=f2(cons_h), r14_fixed_per_paid_hour=f2(fixed_h),
                r14_allin_per_paid_hour=f2(allin_paid), paid_hours_month=f2(paid_h_m), clinical_hours_month=f2(clin_h_m),
                billable_share_of_paid=round(util_share, 4),
                wage_only_per_clinical_hour=f2(r14_wage / util_share), allin_per_clinical_hour=f2(allin_paid / util_share),
                revenue_per_paid_hour_bulk=f2(g["rev_month"] / paid_h_m), revenue_per_clinical_hour_bulk=f2(g["rev_month"] / clin_h_m),
                util_input=c["util"], admin_min=c["admin"], avg_clinical_min=f2(mins))

p1 = {cs: step_table(cs, satA, nA) for cs in CASES}
base = p1["base"]
# Anthony's arithmetic on the R14 base wage input and on his own 45 to 54 range
def ant(w, additive=True):
    return w * (1 + 0.12 + 0.10 + 0.017) if additive else w * 1.12 * 1.10 * 1.017
p1_anthony = dict(
    additive_45=f2(ant(45)), additive_54=f2(ant(54)), compound_45=f2(ant(45, False)), compound_54=f2(ant(54, False)),
    on_r14_base_blended_wage=f2(ant(float(base["blended_with_saturday"]))),
    r14_actual_wage_per_paid_hour=base["r14_wage_per_paid_hour"], r14_allin_per_paid_hour=base["r14_allin_per_paid_hour"],
    gap_explained_by_consumables_and_fixed=f2(float(base["r14_allin_per_paid_hour"]) - float(base["r14_wage_per_paid_hour"])))
# sensitivity: swap R14 on-cost (1.20) for the built-up worked-hour on-cost (no payroll tax; that is Part 3)
def oncost_swap(case, sat, n, mult):
    saved = r14.COST[case]["oncost"]; r14.COST[case]["oncost"] = mult
    try: return r14.mw(case, n, "bulk_billed", sat)
    finally: r14.COST[case]["oncost"] = saved
bu_paid = (1 + SUPER + AL_LOAD + WC); bu_worked = bu_paid * LEAVE_GROSSUP
p1_sens = {}
for sc, (n, sat, _) in {SCEN_A: r14.SCEN[SCEN_A], SCEN_B: r14.SCEN[SCEN_B]}.items():
    p1_sens[sc] = {nm: dict(wage_per_hour=oncost_swap("base", sat, n, m)["wage_per_hour"], net_month=oncost_swap("base", sat, n, m)["net_month"],
                            wage_month=oncost_swap("base", sat, n, m)["wage_month"])
                   for nm, m in (("r14_1.20", 1.20), ("builtup_paid_hour_1.1505", bu_paid), ("builtup_worked_hour_1.366", bu_worked))}
casual_alt = dict(casual_rate_l2pp4=r13.WAGES["RN L2 pp4"][2], casual_loaded_cost=f2(r13.WAGES["RN L2 pp4"][2] * (1 + SUPER + WC)),
                  permanent_loaded_worked_hour=f2(float(base["loaded_per_worked_hour"])), note="casual 25% loading replaces leave; similar total (E)")
out["part1"] = dict(steps=p1, anthony_arithmetic=p1_anthony, sensitivity_oncost=p1_sens, casual_alternative=casual_alt,
                    leave_weeks=dict(annual=4, personal=2, public_holidays=2.2, productive_weeks=round(PRODUCTIVE_WEEKS, 1)),
                    marginal_payroll_tax=round(MARGINAL_PT, 5), al_loading_pct=round(AL_LOAD * 100, 3))

# =====================================================================================================
# PART 2. SCALED MIDWIFE P&L: bulk billed vs Structure B private
# =====================================================================================================
def grid_row(case, key, pricing):
    n, sat, note = r14.SCEN[key]
    if pricing == "structure_B_private_item_scaled":
        g = dict(r14.mw(case, n, "private_at_schedule", sat))
        fee = r14.mix_stats(r14.MIX[case])[0]
        extra = n * fee * (F_PRIV - 1)
        g["rev_month"] = f2(g["rev_month"] + extra); g["net_month"] = f2(g["net_month"] + extra)
        g["net_week"] = f2(g["net_month"] / WEEKS_M); g["rev_per_consult"] = f2(g["rev_per_consult"] * F_PRIV)
        return g
    return r14.mw(case, n, pricing, sat)
P2_PRICING = ["bulk_billed", "structure_B_private_item_scaled", "mixed_50_50_bulk_and_gap30"]
SCEN_KEYS = ["A_50pct_6day", "B_80pct_6day", "A_50pct_396basis", "B_80pct_396basis"]
p2_grid = {f"{k}|{pr}": {cs: grid_row(cs, k, pr) for cs in CASES} for k in SCEN_KEYS for pr in P2_PRICING}
# item mix table (base mix) at A and B six-day volumes
mx = r14.MIX["base"]
items_tbl = {}
for key, n in ((SCEN_A, nA), (SCEN_B, nB)):
    rows = {}
    for it, sh in mx.items():
        cnt = n * sh; I = r14.ITEMS[it]
        rows[it] = dict(count_month=round(cnt, 1), fee=I["fee"], rebate=I["ben"], private_fee_E=f2(I["fee"] * F_PRIV),
                        gross_bulk=f2(cnt * I["ben"]), gross_schedule=f2(cnt * I["fee"]), gross_private=f2(cnt * I["fee"] * F_PRIV))
    rows["total"] = {k: f2(sum(v[k] for v in rows.values())) for k in ("gross_bulk", "gross_schedule", "gross_private")}
    items_tbl[key] = rows
# 82115 (V, MBS Online read 2026-10-24)
u = r14.COST["base"]; h82115 = (90 + u["admin"]) / 60 / u["util"]; cost82115 = h82115 * r14.hourly(u, 1 / 6)
m82115 = dict(fee=381.75, rebate=324.50, minutes=90, paid_hours=f2(h82115), wage_cost=f2(cost82115),
              margin_bulk=f2(324.50 - cost82115 - u["consum"]), margin_private=f2(381.75 - cost82115 - u["consum"]),
              per_10_delivered_month_bulk=f2(10 * (324.50 - cost82115 - u["consum"])),
              plain="Maternity care plan: 90 minute visit after 28 weeks, only for a woman who has had 2 antenatal visits with this midwife in 6 months and who will stay with her as main carer. Once per pregnancy. Not a GTT-test visit; upside only if GTT midwives become the woman's carer.")
out["part2"] = dict(f_private=round(F_PRIV, 4), grid=p2_grid, items=items_tbl, item_82115=m82115)

# =====================================================================================================
# PART 3. PAYROLL TAX (WA)
# =====================================================================================================
ptax = r14.ptax
REPO_TAXABLE_Y = (REPO_WAGES_M + REPO_SUPER_M) * 12          # wages + super; workers comp is not taxable wages
R14_BASIS_Y = REPO_WAGES_M * 12                              # what R14 used (987,817): wages only, super left out
def tax_row(label, taxable_y, base_y=REPO_TAXABLE_Y):
    t = ptax(taxable_y); t0 = ptax(base_y)
    return dict(label=label, taxable_wages_year=round(taxable_y), tax_year=f2(t), tax_month=f2(t / 12),
                added_vs_repo_year=f2(t - t0), added_vs_repo_month=f2((t - t0) / 12), above_threshold_by=round(taxable_y - r14.TH))
def mw_taxable_month(wage_month_cost, oncost):                # strip R14 on-cost down to wages + super + leave loading (taxable part)
    return wage_month_cost / oncost * (1 + SUPER + AL_LOAD)
gA = r14.mw("base", nA, "bulk_billed", satA); gB = r14.mw("base", nB, "bulk_billed", satB)
tA = mw_taxable_month(gA["wage_month"], 1.20) * 12; tB = mw_taxable_month(gB["wage_month"], 1.20) * 12
blend_base = r14.WAGES["RN L2 pp4"][0] * (5 / 6) + r14.WAGES["RN L2 pp4"][1] / 6
fte_taxable_y = lambda k: 38 * 52 * k * blend_base * (1 + SUPER + AL_LOAD)
# complete-roster add-on wages defined in Part 4; computed first
RECEP_RATE = 33.38                                           # R wages.yml casual loaded receptionist, 2025-07-01 basis (2026 uplift Q)
def addon_wages():
    rows = {}
    wk, sat_d = 22, 4.33
    rows["AM receptionist (5.25 h x 5 days, Sat host cover 5.25 h)"] = (5.25 * wk * RECEP_RATE) + (5.25 * sat_d * RECEP_RATE * 1.5)
    rows["Clinic host (6 h x 5 days, Sat 6 h)"] = (6 * wk * RECEP_RATE) + (6 * sat_d * RECEP_RATE * 1.5)
    return rows
ADDON_WAGES_M = sum(addon_wages().values())
ADDON_TAXABLE_Y = ADDON_WAGES_M * (1 + SUPER) * 12
rows3 = [tax_row("Repo only (wages + super)", REPO_TAXABLE_Y),
         tax_row("R14 basis (wages only, super left out)", R14_BASIS_Y, REPO_TAXABLE_Y),
         tax_row("Repo + receptionist + host (E)", REPO_TAXABLE_Y + ADDON_TAXABLE_Y)]
for k in (1, 2, 3): rows3.append(tax_row(f"Repo + {k} full-time midwife (38 h)", REPO_TAXABLE_Y + fte_taxable_y(k)))
rows3 += [tax_row("Repo + Scenario A hours (54 a week, 2 midwives)", REPO_TAXABLE_Y + tA),
          tax_row("Repo + Scenario B hours (84 a week, 3 midwives)", REPO_TAXABLE_Y + tB),
          tax_row("Repo + roster add-on + Scenario A", REPO_TAXABLE_Y + ADDON_TAXABLE_Y + tA),
          tax_row("Repo + roster add-on + Scenario B", REPO_TAXABLE_Y + ADDON_TAXABLE_Y + tB)]
sweep = [tax_row(f"Midwife taxable wages {m:,} a month", REPO_TAXABLE_Y + m * 12) for m in (0, 1000, 2500, 5000, 10000, 15000, 20000, 25000)]
# R14 reconciliation
r14_A_total = ptax(R14_BASIS_Y + gA["wage_month"] * 12); r14_B_total = ptax(R14_BASIS_Y + gB["wage_month"] * 12)
recon = dict(r14_repo_base_year=round(R14_BASIS_Y), correct_repo_taxable_year=round(REPO_TAXABLE_Y), super_left_out_year=round(REPO_SUPER_M * 12),
             r14_A_tax_year=f2(r14_A_total), r14_A_tax_month=f2(r14_A_total / 12), r14_B_tax_year=f2(r14_B_total), r14_B_tax_month=f2(r14_B_total / 12),
             midwife_wage_month_A=gA["wage_month"], midwife_hours_week_A=gA["paid_hours_week"], midwife_wage_month_B=gB["wage_month"], midwife_hours_week_B=gB["paid_hours_week"],
             corrected_total_A_month=f2(ptax(REPO_TAXABLE_Y + tA) / 12), corrected_total_B_month=f2(ptax(REPO_TAXABLE_Y + tB) / 12),
             corrected_added_by_midwives_A_month=f2((ptax(REPO_TAXABLE_Y + tA) - ptax(REPO_TAXABLE_Y)) / 12),
             corrected_added_by_midwives_B_month=f2((ptax(REPO_TAXABLE_Y + tB) - ptax(REPO_TAXABLE_Y)) / 12),
             monthly_taxable_wages_repo=f2(REPO_TAXABLE_Y / 12), monthly_threshold=83333,
             marginal_rate=round(MARGINAL_PT, 5), midwife_hours_per_month_A=round(gA["paid_hours_week"] * WEEKS_M, 1))
out["part3"] = dict(rule=dict(threshold=r14.TH, rate=r14.RATE, upper=r14.UP, deduction="1,000,000 - (wages - 1,000,000) x 2/13, nil at 7,500,000 (V, WA Gov payroll tax guide)",
                              example_check_1_2m_deduction=round(r14.TH - 200000 * 2 / 13), super_in_taxable_wages="Yes: Pay-roll Tax Assessment Act 2002 (WA) Div 2A s9CB treats super contributions as wages (V statute heading; secondary sources agree; Catherine to confirm)",
                              grouping="Related bodies corporate are grouped and share ONE deduction (V principle, Catherine confirms). Holdings + Medical + Lounge = one threshold."),
                    rows=rows3, sweep=sweep, reconciliation=recon, addon_wages_month=f2(ADDON_WAGES_M))

# =====================================================================================================
# PART 4. COMPLETE CLINIC WORKFORCE
# =====================================================================================================
WK, SAT = 22, 4.33
def roster_row(role, award, qty, h_day_wk, h_day_sat, rate, entity, label, note="", sat_mult=1.5):
    hrs_m = qty * (h_day_wk * WK + h_day_sat * SAT)
    wages = qty * (h_day_wk * WK * rate + h_day_sat * SAT * rate * sat_mult)
    loaded = wages * (1 + SUPER + WC)
    return dict(role=role, award=award, heads=qty, hours_week=f2(hrs_m / WEEKS_M), rate=rate, wages_month=f2(wages), loaded_month=f2(loaded),
                taxable_month=f2(wages * (1 + SUPER)), entity=entity, label=label, note=note)
roster = [
 roster_row("Massage + beauty therapist (pool of 4)", "Hair and Beauty MA000005 (repo cites L3/L4; casual loaded)", 4, 6, 6, 37.50, "Lounge", "R"),
 roster_row("Nail technician", "MA000005 L3 (repo), casual loaded", 2, 6, 6, 36.81, "Lounge", "R"),
 roster_row("Hairdresser", "MA000005 L3 (repo), casual loaded", 2, 6, 6, 36.81, "Lounge", "R"),
 roster_row("Phlebotomist (full roster, 10 to 18 booked)", "Health Professionals and Support Services MA000027, casual loaded", 2, 6, 6, 34.375, "Medical", "R", "adaptive: 1 on mornings of 9 or fewer (saves A$6,682.23 loaded-free wage per R)"),
 roster_row("Venue manager", "MA000005 L6 salon manager (repo; needs confirming)", 1, 8, 0, 40.00, "Lounge", "R", "Mon-Fri only; Saturday covered by an experienced rostered staff member, no pay loading decided"),
]
# PM staff and Saturday AM treatment are inside repo totals; show PM as one aggregate line from the repo
pm_w = REPO["pm_weekday"] + REPO["pm_sat"]
roster.append(dict(role="PM treatment staff (4 roles, 3 h floor, 10 sessions a day)", award="MA000005 casual loaded", heads=4, hours_week=f2((4 * 3 * WK + 4 * 3 * SAT) / WEEKS_M),
                   rate=37.16, wages_month=f2(pm_w), loaded_month=f2(pm_w * (1 + SUPER + WC)), taxable_month=f2(pm_w * (1 + SUPER)), entity="Lounge", label="R", note="blended rate from repo; PM check-in and payment done by these staff (Model C)"))
repo_sum = sum(r["wages_month"] for r in roster)
recon4 = dict(rows_sum=f2(repo_sum), repo_total=REPO_WAGES_M, difference=f2(repo_sum - REPO_WAGES_M),
              note="Difference is rounding (repo PM figure uses a floating-point blended rate, A$0.21 to A$0.44 disclosed in the repo)")
# E add-ons (not in repo)
addons = [
 roster_row("AM receptionist / guest coordinator", "Clerks Private Sector MA000002 L1 to L2 (job posting); casual loaded", 1, 5.25, 5.25, RECEP_RATE, "Lounge", "E", "NOT in repo cost (AM reception is done by the venue manager, PM reception removed 2026-08-21). Hours from receptionist-job-posting (opening ~07:15 to last client). Rate R from wages.yml (2025-07-01), 2026 uplift Q"),
 roster_row("Clinic host (arrival, fasting check, drink, lounge watch)", "Clerks MA000002 or Hospitality (Grace and Anthony to confirm)", 1, 6, 6, RECEP_RATE, "Lounge", "E", "Not in repo. Route 1 plain-English roster shows a host at arrival and in the lounge. Rate proxy = receptionist rate (Q)"),
]
mid_rows = []
for nm, g, sat in (("Midwives, Scenario A (54 consults a week)", gA, satA), ("Midwives, Scenario B (84 consults a week)", gB, satB)):
    w = g["wage_month"]
    mid_rows.append(dict(role=nm, award="Nurses MA000034 RN L2 pp4 (E class), permanent", heads=g["midwives_needed"], hours_week=g["paid_hours_week"], rate=g["wage_per_hour"],
                         wages_month=w, loaded_month=w, taxable_month=f2(mw_taxable_month(w, 1.20)), entity="Medical", label="R14 base, E",
                         note="wage_month already includes R14 on-cost 1.20 (super, leave, workers comp)"))
tot_repo_loaded = REPO_PAYROLL_M
tot_addon = sum(a["loaded_month"] for a in addons)
split = {}
def ent_total(rows, ent, key="loaded_month"): return f2(sum(r[key] for r in rows if r["entity"] == ent))
for nm, mids in (("repo_only", []), ("repo_plus_addons", []), ("repo_addons_midA", [mid_rows[0]]), ("repo_addons_midB", [mid_rows[1]]), ("repo_midA_no_addons", [mid_rows[0]])):
    rows = roster + (addons if "addons" in nm else []) + mids
    split[nm] = dict(Medical=ent_total(rows, "Medical"), Lounge=ent_total(rows, "Lounge"), total_loaded=f2(sum(r["loaded_month"] for r in rows)),
                     total_wages=f2(sum(r["wages_month"] for r in rows)), taxable_month=f2(sum(r["taxable_month"] for r in rows)))
# phlebotomist award flag
phleb_h = 2 * 6 * WK + 2 * 6 * SAT * 1.5
award_flag = {lv: dict(ordinary=o, casual_loaded=f2(o * 1.25), monthly_wages=f2(o * 1.25 * phleb_h), delta_vs_repo_wages=f2(o * 1.25 * phleb_h - 34.375 * phleb_h),
                       delta_loaded=f2((o * 1.25 - 34.375) * phleb_h * (1 + SUPER + WC))) for lv, o in (("L5_30.45", 30.45), ("L6_31.50_E", 31.50), ("L7_32.67", 32.67))}
award_flag["repo_34.375_is_27.50_plus_25pct"] = f2(34.375 / 1.25)
out["part4"] = dict(roster=roster, reconcile_to_repo=recon4, addons=addons, midwives=mid_rows, entity_split=split, phleb_award_flag=award_flag,
                    repo_payroll_loaded_month=REPO_PAYROLL_M, addon_loaded_month=f2(tot_addon),
                    not_in_repo=["receptionist (cost line removed 2026-08-21)", "clinic host", "midwives", "payroll tax", "relief/absence (reverted to A$0)"])

# =====================================================================================================
# PART 5. THREE-TIER STRUCTURE
# =====================================================================================================
ASIC_REG, ASIC_REVIEW = 636, 342                                  # V (secondary sites quoting ASIC from 1 Jul 2026; ASIC page did not render figures)
cost3 = {
 "low":  dict(asic_reg=2 * ASIC_REG, legal_docs=3000, accountant_setup=1500, name_reg=47),
 "base": dict(asic_reg=2 * ASIC_REG, legal_docs=7500, accountant_setup=3000, name_reg=108),
 "high": dict(asic_reg=2 * ASIC_REG, legal_docs=15000, accountant_setup=6000, name_reg=108)}
run3 = {
 "low":  dict(asic_review=2 * ASIC_REVIEW, accountant_extra=2 * 1500, bookkeeping_bas_payroll=2 * 600, bank_and_software=360, insurance_extra=500),
 "base": dict(asic_review=2 * ASIC_REVIEW, accountant_extra=2 * 2500, bookkeeping_bas_payroll=2 * 1500, bank_and_software=720, insurance_extra=1500),
 "high": dict(asic_review=2 * ASIC_REVIEW, accountant_extra=2 * 4000, bookkeeping_bas_payroll=2 * 3000, bank_and_software=1200, insurance_extra=3000)}
for cs in cost3: cost3[cs]["total"] = sum(cost3[cs].values()); run3[cs]["total_year"] = sum(run3[cs].values()); run3[cs]["total_month"] = f2(run3[cs]["total_year"] / 12)
# per-client split of the Structure B package
def split_pkg(P):
    lab = 27.85; consult = 110.0; lounge = P - consult - lab
    return dict(package=P, consult_medical=consult, lab_agent_not_revenue=lab, lounge=f2(lounge), lounge_gst=f2(lounge / 11), lounge_ex_gst=f2(lounge / 1.1),
                client_after_rebate_example=f2(P - 99.40), client_after_rebate_mix_avg=f2(P - (r14.mix_stats(r14.MIX["base"])[1] + 23.75)),
                share_medical=round(consult / P, 4), share_lab=round(lab / P, 4), share_lounge=round(lounge / P, 4),
                group_keeps_gross=f2(P - lab), group_keeps_ex_gst=f2(consult + lounge / 1.1))
pkg250 = split_pkg(250.0)
# package price table: group net after GST vs repo (R 23,442.58), bundle consult flat A$110 per B client
CASE = "base"
def bundle(P, n, sat, proc_fee=False):
    g = r14.mw(CASE, n, "bulk_billed", sat)
    cost_mid = g["rev_month"] - g["net_month"]                   # wages + consumables + fixed (revenue stripped out)
    consult_rev = 110.0 * n                                      # consult line of the bundle (GST-free, E)
    lounge_incl = P - 137.85
    lounge_delta = n * (lounge_incl / 1.1 - 250.0 / 1.1)         # repo: B-client would have paid A$250 lounge-only (GST inclusive)
    fees = n * (0.017 * (P - 27.85) + 0.30) if proc_fee else 0.0
    change = consult_rev - cost_mid + lounge_delta - fees
    return dict(n=round(n, 1), consult_rev=f2(consult_rev), midwife_cost=f2(cost_mid), lounge_delta_ex_gst=f2(lounge_delta), processing=f2(fees),
               change_vs_repo=f2(change), group_net_after_gst=f2(AFTER_GST + change))
PRICES = [250, 275, 300, 325, 350, 387.85]
tbl5d = []
for P in PRICES:
    sp = split_pkg(P)
    row = dict(sp)
    for key, n, sat in (("A", nA, satA), ("B", nB, satB)):
        row[f"scenario_{key}"] = bundle(P, n, sat)
    tbl5d.append(row)
# bulk billing alternative with lounge unchanged at A$250
bulk_alt = {k: dict(change_vs_repo=f2(r14.mw(CASE, n, "bulk_billed", sat)["net_month"]), group_net_after_gst=f2(AFTER_GST + r14.mw(CASE, n, "bulk_billed", sat)["net_month"]))
            for k, n, sat in (("A", nA, satA), ("B", nB, satB))}
# break-even package price (change_vs_repo >= 0) and minimum B clients at each price
def be_price(n, sat):
    lo, hi = 250.0, 800.0
    for _ in range(60):
        mid = (lo + hi) / 2
        if bundle(mid, n, sat)["change_vs_repo"] >= 0: hi = mid
        else: lo = mid
    return round(hi, 2)
def be_clients(P, sat):
    for n in range(1, 475):
        if bundle(P, float(n), sat)["change_vs_repo"] >= 0: return n
    return None
be5 = dict(break_even_price_A=be_price(nA, satA), break_even_price_B=be_price(nB, satB),
           min_B_clients_a_month={str(P): be_clients(P, satA) for P in PRICES})
# group waterfall at P=250 and like-for-like 387.85, Scenario A and B
wf = {}
for P in (250.0, 387.85):
    for key, n, sat in (("A", nA, satA), ("B", nB, satB)):
        b = bundle(P, n, sat, proc_fee=True)
        g = r14.mw(CASE, n, "bulk_billed", sat)
        pt_added = (ptax(REPO_TAXABLE_Y + (tA if key == "A" else tB)) - ptax(REPO_TAXABLE_Y)) / 12
        pt_repo = ptax(REPO_TAXABLE_Y) / 12
        three = run3["base"]["total_month"]
        net = b["group_net_after_gst"] - pt_added - pt_repo - three
        wf[f"P{int(P)}_{key}"] = dict(repo_after_gst=AFTER_GST, structure_B_change=b["change_vs_repo"], of_which_consult_rev=b["consult_rev"], of_which_midwife_cost=-b["midwife_cost"],
                                    of_which_lounge_repricing=b["lounge_delta_ex_gst"], of_which_processing=-b["processing"], payroll_tax_repo_base=-f2(pt_repo),
                                    payroll_tax_added_midwives=-f2(pt_added), three_company_running_cost=-three, group_net_before_company_tax=f2(net),
                                    company_tax_25pct=f2(max(0, net) * 0.25), group_net_after_company_tax=f2(net - max(0, net) * 0.25))
# baseline group with the three-company cost only (no midwife)
wf["baseline_no_midwife"] = dict(repo_after_gst=AFTER_GST, payroll_tax_repo_base=-f2(ptax(REPO_TAXABLE_Y) / 12), three_company_running_cost=-run3["base"]["total_month"],
                                 group_net_before_company_tax=f2(AFTER_GST - ptax(REPO_TAXABLE_Y) / 12 - run3["base"]["total_month"]),
                                 note="payroll tax on repo wages is a NEW cost line: the repo net has none. Not changed in the repo; shown beside it")
# illustrative inter-company flows (E): all tax neutral on consolidation
lounge_rev_ex = 101.95 * nA
flows = dict(
    ip_licence_E="2%% of lounge revenue ex GST, subsidiaries to Holdings: A$%.0f a month at Scenario A bundle volume only; on all lounge revenue (ex GST ~A$%.0f a month) A$%.0f" % (0.02 * lounge_rev_ex, (118485 + 24585.37) / 1.1, 0.02 * (118485 + 24585.37) / 1.1),
    management_fee_E="5%% of Medical revenue, Medical to Lounge for reception, rooms, booking: A$%.0f a month (Scenario A, A$110 consults)" % (0.05 * 110 * nA),
    facility_fee_E="Medical pays Lounge the midwife room rent: %d rooms x 12 sqm x A$40 = A$%.0f a month (already inside R14 fixed costs)" % (r14.mw(CASE, nA, "bulk_billed", satA)["rooms"], r14.mw(CASE, nA, "bulk_billed", satA)["rooms"] * 12 * 40),
    tax_effect="Nil when consolidated (one head-company return; intra-group payments ignored). Without consolidation each entity pays 25% on its own profit, loss in one cannot offset profit in another.",
    gst_effect="Nil when a GST group is formed (intra-group supplies ignored). Otherwise GST on each charge, credit claimed by payer, cash timing only.",
    bre="Holdings: non-portfolio dividends (10% or more voting) are NOT passive income (s23AB(1)(a), Catherine BASE-RATE-ENTITY.md V). Royalties and rent ARE passive. An IP licence fee is a royalty. If Holdings stayed outside consolidation and its only income were royalties, passive share = 100%, over the 80% limit, so its rate is 30% not 25%. Consolidating removes the risk: the test runs on the group.",
    div7a="Loans between companies are not a Division 7A deemed dividend by themselves (s109J, company-to-company) but an interposed-entity loan that ends with a shareholder is (s109T). Owners' shareholder loans into the group (R4 loan-first repayment) are the reverse direction. Catherine to confirm.",
    franking="Tax paid at 25% by the head company generates franking credits that go out with dividends to Anthony and his partner (Route B). Consolidated: one franking account at the head company.")
out["part5"] = dict(setup_cost_extra_two_companies=cost3, running_cost_extra=run3, package_split_250=pkg250, price_table=tbl5d, bulk_billed_alternative_lounge_250=bulk_alt,
                    break_even=be5, waterfall=wf, flows=flows, asic=dict(registration=ASIC_REG, annual_review=ASIC_REVIEW, label="V-secondary (sites quoting ASIC fees from 1 July 2026; asic.gov.au page did not render figures)"),
                    payroll_tax_effect="None: grouped companies share one threshold. Three companies means three payroll registrations but one deduction.")

# =====================================================================================================
# PART 6. STRUCTURE B CASH FLOW
# =====================================================================================================
def fee_pct(x): return 0.017 * x + 0.30
rebate_example = 75.65 + 16.95 + 6.80
mix_rebate = r14.mix_stats(r14.MIX["base"])[1] + 16.95 + 6.80
X = dict(online=250.0, processing=f2(fee_pct(250)), lab_held=27.85, remit_to_lab=27.85, gtt_receives_net=f2(250 - fee_pct(250)),
         gst_on_lounge=f2(112.15 / 11), gtt_keeps_before_costs=f2(250 - 27.85 - fee_pct(250) - 112.15 / 11), lab_fee_absorbed=0)
Y = dict(online=222.15, processing=f2(fee_pct(222.15)), at_appointment_to_lab=27.85, gtt_receives_net=f2(222.15 - fee_pct(222.15)),
         gst_on_lounge=f2(112.15 / 11), gtt_keeps_before_costs=f2(222.15 - fee_pct(222.15) - 112.15 / 11))
rows6 = []
for cl, lab in (("396 (Mon to Fri)", 396), ("473.94 (six-day)", CLIENTS_M)):
    for rr in (0.02, 0.05, 0.10):
        per_month = lab * rr * 27.85
        rows6.append(dict(clients_month=cl, refusal_rate=rr, refused_clients=round(lab * rr, 1), exposure_month=f2(per_month), reserve_two_months=f2(2 * per_month)))
float_held = f2(27.85 * VISITS_M * 21 / 30.4)
out["part6"] = dict(option_X_pay_all_online=X, option_Y_pay_package_online_lab_at_appointment=Y, recommended="Y",
                    rebate_example_99_40=f2(rebate_example), client_after_rebate_example=f2(250 - rebate_example),
                    rebate_mix_avg=f2(mix_rebate), client_after_rebate_mix_avg=f2(250 - mix_rebate),
                    processing_fee_note="1.7% + A$0.30 (E, Q for provider)", reserve_table=rows6, float_held_option_X_at_396=float_held,
                    float_note="Option X: A$27.85 x 396 clients x about 21 days booking lead (E) = money GTT holds that is not GTT's",
                    lounge_stays_with_lounge="Yes, 112.15 of 250 (44.9%) is Lounge revenue, 100% Lounge's if the Lounge invoices it and has its own merchant account (Q provider). Holdings and Medical see none of it except by written inter-company fee.")

# =====================================================================================================
# PART 7. ROUTE 1 STEP COSTS (now vs at lease signing)
# =====================================================================================================
steps7 = [
 ("Medicare provider number for the midwife (form HW088)", 0, 0, "E", "no fee found (R13)"),
 ("ABN for each company", 0, 0, "V", "ABR registration is free"),
 ("PRODA account (individual and organisation)", 0, 0, "V", "free"),
 ("Ahpra registration check (public register)", 0, 0, "V", "free to look up; midwife renewal A$193 a year is hers or GTT's by contract (R14, V)"),
 ("Register GTT Holdings, Medical, Lounge (3 companies)", 3 * ASIC_REG, 0, "V-secondary", "A$636 each; only needed for the structure Anthony chooses"),
 ("Business name for the Lounge", 47, 0, "per brief", "A$47 for 1 year or A$108 for 3 years (not re-verified)"),
 ("Lab agreement and second paper (sub-lease or licence)", 0, 6000, "Q", "legal review A$3,000 to A$15,000 (Q); nothing due until a lab says yes"),
 ("Landlord written consent", 0, 0, "E", "no fee normally; legal cost sits in the lease review"),
 ("Main lease: bond about 2 months rent", 0, 16000, "R", "A$8,000 a month rent budget x 2; refundable"),
 ("Insurance (public liability, professional indemnity, property)", 0, 708.34 * 3, "R", "repo A$708.34 a month; first quarter due at opening"),
 ("Collection-centre approval paperwork", 0, 0, "R", "lab applies in its own name; GTT cost nil"),
]
out["part7"] = dict(steps=[dict(step=s, cost_now=a, cost_at_lease_signing=b, label=l, note=n) for s, a, b, l, n in steps7],
                    total_now=sum(s[1] for s in steps7), total_at_lease=sum(s[2] for s in steps7))

json.dump(out, open(os.path.join(HERE, "theodore_r15_results.json"), "w"), indent=1)

if __name__ == "__main__":
    for cs in CASES: print(cs, {k: v for k, v in p1[cs].items() if k in ("blended_with_saturday", "plus_super_12pct", "plus_leave_loading", "plus_workers_comp_1_7pct", "loaded_per_worked_hour", "r14_wage_per_paid_hour", "r14_allin_per_paid_hour", "billable_share_of_paid", "wage_only_per_clinical_hour", "allin_per_clinical_hour", "revenue_per_clinical_hour_bulk")})
    print(p1_anthony); print(p1_sens)
    for k, v in p2_grid.items(): print(k, {cs: (v[cs]["net_month"], v[cs]["midwives_needed"], v[cs]["fte"], v[cs]["rev_month"]) for cs in CASES})
    print(items_tbl); print(m82115)
    for r in rows3: print(r)
    print(recon); print(sweep[:3])
    for r in roster + addons + mid_rows: print(r["role"], r["hours_week"], r["wages_month"], r["loaded_month"], r["entity"])
    print(recon4); print(split); print(award_flag)
    print(cost3); print(run3); print(pkg250)
    for r in tbl5d: print(r["package"], r["client_after_rebate_example"], r["lounge"], r["scenario_A"]["group_net_after_gst"], r["scenario_B"]["group_net_after_gst"])
    print(bulk_alt, be5); print(json.dumps(wf, indent=0)); print(flows)
    print(X, Y, float_held); print(rows6); print(out["part7"]["total_now"], out["part7"]["total_at_lease"])
