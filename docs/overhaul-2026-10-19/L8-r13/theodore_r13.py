"""Theodore R13 (2026-10-23): (1) GTT-owned lowest-category (Category S) glucose lab, refreshed from R10;
(2) participating-midwife revenue model and requester-only model.
Repo figures are read, never altered. AUD. Every outside number carries a label: VERIFIED / ESTIMATE / QUOTE NEEDED.
Basis: 07:00 start, 2 chairs, 25 min pair cadence, 18 clients/day, 22 days/month = 396 visits/month, 264 days/year.
"""
import json, os

# ---------------- repo basis (read only) ----------------
BASE_NET_MONTH = 35186.40          # repo net operating result, no GST line (CURRENT-STATE, 2026-09-19)
BASE_NET_MONTH_AFTER_GST = 23442.58  # R9/R11 after-GST basis, shown for reference only
CPD, DAYS_M = 18, 22
VISITS_M = CPD * DAYS_M            # 396
VISITS_Y = VISITS_M * 12           # 4752
DAYS_Y = DAYS_M * 12               # 264
assert VISITS_M == 396 and VISITS_Y == 4752
BEN_66548, BEN_73928, BEN_73938 = 16.95, 5.10, 6.80   # 85% benefits (MBS; 73938 per Catherine R12)
REV_ACC = round(BEN_66548 + BEN_73928, 2)             # 22.05
REV_TPR = round(BEN_66548 + BEN_73938, 2)             # 23.75
assert REV_ACC == 22.05 and REV_TPR == 23.75
RENT_PER_M2_MONTH = 40.0           # repo rent basis: A$40/sqm/month (CURRENT-STATE s52); repo says may be understated
ONCOST_R10 = 1.25                  # R10 on-cost (super 12% + leave loading + workers comp), ESTIMATE
FX = 1.4337                        # RBA AUD per USD, fx_aud.json 2026-10-19 (converted, labelled)
WEEKS_M = 52 / 12

# =============== PART 1: Category S lab ===============
LAB = {
 "low": dict(director=150000, sci=100000, relief=0.05, asst_sal=60523, asst_fte=0.4,
   analyser=10055, backup=2000, centrifuge=2000, fridge=3000, kit=2000, lis_setup=3000, lis_yr=2400,
   m2=12, fit_rate=3000, consult=5000, nata_init=5000, nata_yr=3500, apl=0, acc=2000, approval_months=12, carry_months=3,
   eqa=2500, qc=1500, svc=0.05, waste=1800, courier=1200, insurance=4000, other=2500, reagent=0.10, consum=4.0),
 "base": dict(director=250000, sci=135000, relief=0.10, asst_sal=68780, asst_fte=0.6,
   analyser=25000, backup=3000, centrifuge=3500, fridge=6000, kit=3000, lis_setup=8000, lis_yr=6000,
   m2=20, fit_rate=4000, consult=10000, nata_init=12000, nata_yr=6000, apl=0, acc=2000, approval_months=18, carry_months=6,
   eqa=4000, qc=2500, svc=0.08, waste=3000, courier=2400, insurance=8000, other=4000, reagent=0.30, consum=6.0),
 "high": dict(director=450000, sci=158894, relief=0.15, asst_sal=81776, asst_fte=1.0,
   analyser=round(40000 * FX), backup=4000, centrifuge=6000, fridge=10000, kit=5000, lis_setup=25000, lis_yr=15000,
   m2=25, fit_rate=7000, consult=20000, nata_init=25000, nata_yr=12000, apl=0, acc=2000, approval_months=24, carry_months=9,
   eqa=7000, qc=4000, svc=0.10, waste=5000, courier=4800, insurance=18000, other=7000, reagent=0.60, consum=9.0),
}
DRAWS, REAGENT_WASTE = 3, 1.15

def lab_run(c, cpd=CPD):
    sci = c["sci"] * ONCOST_R10 * (1 + c["relief"])
    asst = c["asst_sal"] * c["asst_fte"] * ONCOST_R10
    staff = c["director"] + sci + asst
    rent = c["m2"] * RENT_PER_M2_MONTH * 12
    other = (c["lis_yr"] + c["nata_yr"] + c["eqa"] + c["qc"] + c["analyser"] * c["svc"] + c["waste"]
             + c["courier"] + c["insurance"] + c["other"])
    fixed_ex_rent = staff + other
    fixed = fixed_ex_rent + rent
    var = c["reagent"] * DRAWS * REAGENT_WASTE + c["consum"]
    cl_y = cpd * DAYS_Y
    contrib = REV_ACC - var
    rev = REV_ACC * cl_y
    opex = fixed + var * cl_y
    carry = (c["director"] + sci) / 12 * c["carry_months"]
    items = dict(analyser=c["analyser"], backup_meter=c["backup"], centrifuge=c["centrifuge"], fridge_freezer_logging=c["fridge"],
                 pipettes_loggers_kit=c["kit"], lis_setup=c["lis_setup"], bench_fitout=c["m2"] * c["fit_rate"],
                 consultancy_nata_prep=c["consult"], nata_application_assessment=c["nata_init"], apl_fee=c["apl"],
                 acc_tax_hw035=c["acc"], pre_income_staff_carry=round(carry))
    capex = sum(items.values())
    net = rev - opex
    return dict(
      staff_year=round(staff), rent_year_at_repo_rate=round(rent), other_fixed_year=round(other), fixed_year=round(fixed),
      var_per_client=round(var, 2), running_cost_year=round(opex), medicare_income_year=round(rev), net_year=round(net),
      setup_items={k: round(v) for k, v in items.items()}, setup_total=round(capex),
      breakeven_cpd_running=round(fixed / contrib / DAYS_Y, 1),
      breakeven_cpd_with_setup_5yr=round((fixed + capex / 5) / contrib / DAYS_Y, 1),
      breakeven_cpd_running_ex_rent=round(fixed_ex_rent / contrib / DAYS_Y, 1),
      max_fixed_cost_carried_at_18=round(contrib * cl_y),
      months_to_approval=c["approval_months"],
      net_vs_partner_lab_year=round(net),     # partner lab route: lab keeps the 22.05, GTT gets 0 from Medicare
      net_month=round(net / 12),
    )

lab_res = {k: lab_run(v) for k, v in LAB.items()}
assert lab_res["low"]["net_year"] > lab_res["base"]["net_year"] > lab_res["high"]["net_year"]
assert lab_res["base"]["medicare_income_year"] == round(22.05 * 4752)
# staff-free-of-specialist sensitivity (best conceivable): director cost 0
lab_sens = {}
for k, v in LAB.items():
    c = dict(v); c["director"] = 0
    lab_sens[k] = lab_run(c)["net_year"]
vol = {str(n): lab_run(LAB["base"], n)["net_year"] for n in (18, 36, 60, 90, 120)}

# =============== PART 2: midwife model ===============
# MBS Online fetches 2026-10-23 (www9.health.gov.au/mbs, item pages). VERIFIED text; fees read via a page summariser, re-check before use.
ITEMS = {
 "82100": dict(desc="Initial antenatal attendance, participating midwife, at least 60 min; once per pregnancy; not telehealth", fee=89.00, ben85=75.65, mins=60),
 "82105": dict(desc="Short antenatal attendance, at least 10 min (video equivalent exists)", fee=38.75, ben85=32.95, mins=10),
 "82110": dict(desc="Routine antenatal attendance, at least 40 min (video 91212 $89.00/$75.65; phone 91219)", fee=89.00, ben85=75.65, mins=40),
 "82115": dict(desc="Maternity care plan, at least 90 min, beyond 28 weeks, needs 2 prior antenatal attendances in 6 months; once per pregnancy; midwife intends to stay primary carer", fee=381.75, ben85=324.50, mins=90),
 "82130": dict(desc="Short postnatal attendance, at least 20 min, within 6 weeks of birth", fee=63.90, ben85=54.35, mins=20),
 "82135": dict(desc="Routine postnatal attendance, at least 40 min, within 6 weeks of birth", fee=130.80, ben85=111.20, mins=40),
}
for k, v in ITEMS.items():
    assert abs(v["fee"] * 0.85 - v["ben85"]) < 0.06, (k, v["fee"] * .85)   # arithmetic check on 85%
MIX = {"low": {"82100": .05, "82105": .35, "82110": .40, "82130": .20},        # low = thin mix (lots of short visits)
       "base": {"82100": .12, "82105": .25, "82110": .43, "82130": .20},
       "high": {"82100": .15, "82105": .15, "82110": .50, "82135": .10, "82130": .10}}
for m in MIX.values(): assert abs(sum(m.values()) - 1) < 1e-9
def mix_stats(mx):
    return (sum(ITEMS[i]["fee"] * s for i, s in mx.items()), sum(ITEMS[i]["ben85"] * s for i, s in mx.items()),
            sum(ITEMS[i]["mins"] * s for i, s in mx.items()))

# Wages: Fair Work Pay Guide, Nurses Award 2020 MA000034, from 1 Jul 2026 (VERIFIED; calculate.fairwork.gov.au/payguides/pact/MA000034/20260701)
WAGES = {  # hourly ordinary, Saturday (FT/PT 150%), casual ordinary, casual Saturday
 "RN L1 pp1": (32.09, 48.14, 40.11, 60.17), "RN L2 pp1": (39.59, 59.39, 49.49, 74.24), "RN L2 pp4": (41.59, 62.39, 51.99, 77.99),
 "RN L3 pp1": (42.93, 64.40, 53.66, 80.49), "NP yr1": (49.39, 74.09, 61.74, 92.61), "NP yr2": (50.86, 76.29, 63.58, 95.37)}
SUPER, WC = 0.12, 0.017                       # super 12% (ATO SG rate from 1 Jul 2025, VERIFIED); WA workers comp 1.7% = repo figure
MW = {  # cost cases; award classification of an endorsed midwife is an ESTIMATE (Award maps midwives into RN levels)
 "low":  dict(rate="RN L2 pp1", casual=False, oncost=1 + SUPER + WC, sat_share=0.0, util=0.80, ahpra=193, pi=1200, sw_m=80, equip=2500, consum=1.5, m2=12, room_share=0.0, cpd_yr=300),
 "base": dict(rate="RN L2 pp4", casual=False, oncost=1.20, sat_share=1/6, util=0.70, ahpra=193, pi=2500, sw_m=120, equip=4500, consum=3.0, m2=12, room_share=0.5, cpd_yr=600),
 "high": dict(rate="RN L3 pp1", casual=True, oncost=1 + SUPER + WC, sat_share=1/3, util=0.60, ahpra=193, pi=4500, sw_m=200, equip=8000, consum=5.0, m2=12, room_share=1.0, cpd_yr=1200)}
PRICING = {"bulk_billed": 0, "private_at_schedule": 1, "private_gap_30pct": 2, "mixed_50_50": 3}
GAP = 1.30      # ESTIMATE: no published Perth fee found. Gap fee assumed = 130% of schedule fee

def rev_per_consult(mx, pricing):
    fee, ben, _ = mix_stats(mx)
    return {"bulk_billed": ben, "private_at_schedule": fee, "private_gap_30pct": fee * GAP,
            "mixed_50_50": 0.5 * ben + 0.5 * fee * GAP}[pricing]

def hourly_cost(c):
    ordn, sat, cord, csat = WAGES[c["rate"]]
    base = (cord if c["casual"] else ordn) * (1 - c["sat_share"]) + (csat if c["casual"] else sat) * c["sat_share"]
    return base * c["oncost"]

def mw_run(cost_case, mix_case, consults_week, pricing):
    c = MW[cost_case]; mx = MIX[mix_case]
    fee, ben, mins = mix_stats(mx)
    rev_c = rev_per_consult(mx, pricing)
    paid_h_week = consults_week * mins / 60 / c["util"]
    wage_week = paid_h_week * hourly_cost(c)
    consumables_week = consults_week * c["consum"]
    rev_week = consults_week * rev_c
    fixed_month = (c["ahpra"] + c["pi"] + c["cpd_yr"]) / 12 + c["sw_m"] + c["equip"] / 5 / 12 \
                  + c["m2"] * RENT_PER_M2_MONTH * c["room_share"]
    rev_m, wage_m, cons_m = rev_week * WEEKS_M, wage_week * WEEKS_M, consumables_week * WEEKS_M
    net_m = rev_m - wage_m - cons_m - fixed_month
    return dict(consults_week=consults_week, avg_minutes=round(mins, 1), paid_hours_week=round(paid_h_week, 1),
                revenue_per_consult=round(rev_c, 2), wage_cost_per_paid_hour=round(hourly_cost(c), 2),
                rev_week=round(rev_week, 2), wage_week=round(wage_week, 2), consumables_week=round(consumables_week, 2),
                fixed_week=round(fixed_month / WEEKS_M, 2), net_week=round(net_m / WEEKS_M, 2),
                rev_month=round(rev_m, 2), wage_month=round(wage_m, 2), consumables_month=round(cons_m, 2),
                fixed_month=round(fixed_month, 2), net_month=round(net_m, 2),
                gtt_total_net_month=round(BASE_NET_MONTH + net_m, 2))

# Revenue mix is the base mix in all three columns, so low/base/high differ ONLY by cost.
mw_grid = {}
for pr in PRICING:
    for n in (10, 15, 20):
        mw_grid[f"{pr}|{n}"] = {cc: mw_run(cc, "base", n, pr) for cc in ("low", "base", "high")}
# break-even consults a week (base cost, each pricing)
def be_consults(pr, cc="base"):
    for n in range(1, 80):
        if mw_run(cc, "base", n, pr)["net_month"] > 0: return n
    return None
mw_be = {pr: {cc: be_consults(pr, cc) for cc in MW} for pr in PRICING}

# Requester-only (B3 route): the midwife sees each GTT client who has no usable request; bills 82105 (10 min) or cost-only.
REQ = {"low": dict(share=0.25, mins_paid=15, rate="RN L2 pp1", casual=False, oncost=1 + SUPER + WC),
       "base": dict(share=0.50, mins_paid=20, rate="RN L2 pp4", casual=False, oncost=1.20),
       "high": dict(share=1.00, mins_paid=30, rate="RN L3 pp1", casual=True, oncost=1 + SUPER + WC)}
def req_run(k, bill_82105):
    r = REQ[k]; m = MW[k]
    n_m = VISITS_M * r["share"]
    paid_h_m = n_m * r["mins_paid"] / 60
    sat_w = r["share"] * 0 + (1/6)
    ordn, sat, cord, csat = WAGES[r["rate"]]
    hr = ((cord if r["casual"] else ordn) * (1 - sat_w) + (csat if r["casual"] else sat) * sat_w) * r["oncost"]
    wage = paid_h_m * hr
    cons = n_m * m["consum"]
    fixed = (m["ahpra"] + m["pi"] + m["cpd_yr"]) / 12 + m["sw_m"] + m["equip"] / 5 / 12 + m["m2"] * RENT_PER_M2_MONTH * m["room_share"]
    rev = n_m * ITEMS["82105"]["ben85"] if bill_82105 else 0.0     # bulk billed at 85% benefit
    net = rev - wage - cons - fixed
    return dict(requests_month=round(n_m), paid_hours_month=round(paid_h_m, 1), paid_hours_week=round(paid_h_m / WEEKS_M, 1),
                wage_month=round(wage, 2), consumables_month=round(cons, 2), fixed_month=round(fixed, 2),
                revenue_month=round(rev, 2), net_month=round(net, 2), gtt_total_net_month=round(BASE_NET_MONTH + net, 2),
                clinical_minutes_per_morning_82105=round(n_m / DAYS_M * 10, 1))
req = {k: {"bill_82105_bulk": req_run(k, True), "cost_only_no_billing": req_run(k, False)} for k in REQ}
# collection benefit: who earns it
coll = dict(per_client_73938_vs_73928_extra=round(BEN_73938 - BEN_73928, 2),
            month_extra_if_passed_through=round((BEN_73938 - BEN_73928) * VISITS_M, 2),
            year_extra_if_passed_through=round((BEN_73938 - BEN_73928) * VISITS_Y, 2),
            full_73938_month_if_GTT_were_paid_it=round(BEN_73938 * VISITS_M, 2),
            who_earns="The lab claims 73938 (A$7.95 fee, A$6.80 at 85%). GTT earns none of it. Any pass-through to GTT is blocked or doubtful under Part IIBA (Catherine R12 B3). Excluded from every net figure.",
            client_rebate_total_66548_plus_73938=REV_TPR, client_rebate_acc_route=REV_ACC)

out = dict(generated="2026-10-23", basis=dict(base_net_month_repo=BASE_NET_MONTH, base_net_month_after_gst=BASE_NET_MONTH_AFTER_GST,
           visits_month=VISITS_M, visits_year=VISITS_Y, days_year=DAYS_Y, rent_per_m2_month=RENT_PER_M2_MONTH, fx_aud_per_usd=FX),
   lab=dict(inputs=LAB, results=lab_res, net_year_if_specialist_cost_zero=lab_sens, base_volume_sensitivity_net_year=vol),
   midwife=dict(items=ITEMS, mix=MIX, wages=WAGES, cost_cases=MW, pricing_gap_factor=GAP,
                mix_stats={k: dict(zip(("avg_fee", "avg_benefit85", "avg_minutes"), map(lambda x: round(x, 2), mix_stats(v)))) for k, v in MIX.items()},
                grid=mw_grid, breakeven_consults_week=mw_be, requester_only=req, collection_benefit=coll))
here = os.path.dirname(os.path.abspath(__file__))
json.dump(out, open(os.path.join(here, "theodore_r13_results.json"), "w"), indent=1)

print("LAB");
for k, v in lab_res.items(): print(k, {x: v[x] for x in ("setup_total","running_cost_year","medicare_income_year","net_year","breakeven_cpd_running","breakeven_cpd_with_setup_5yr","max_fixed_cost_carried_at_18","staff_year")})
print("lab zero-director net", lab_sens, "vol", vol)
print("MIX", out["midwife"]["mix_stats"])
for pr in PRICING:
    for n in (10, 15, 20):
        g = mw_grid[f"{pr}|{n}"]
        print(pr, n, {cc: (g[cc]["net_week"], g[cc]["net_month"], g[cc]["paid_hours_week"], g[cc]["revenue_per_consult"]) for cc in g})
print("BE", mw_be)
for k, v in req.items(): print("REQ", k, v)
print(coll)
