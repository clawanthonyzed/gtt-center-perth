"""Theodore R10: GTT-owned Category S glucose lab vs Route 1 (partner lab runs collection centre inside GTT).
GTT repo figures are read, never altered: steady state after-GST profit A$23,442.58 a month (theodore_model.py, CURRENT-STATE.md).
Every external price is an ESTIMATE with a named source, or QUOTE NEEDED. AUD only. Fetched 2026-10-20.
"""
import json, os
FX_AUD_PER_USD = 1.4337          # RBA, /opt/openclaw/logs/fx_aud.json as of 2026-10-19 (converted, labelled)
# ---- repo inputs (read only) ----
REPO_STEADY_MONTH = 23442.58     # real profit after GST, before company tax (CURRENT-STATE / L4 theodore_model)
REPO_STEADY_YEAR = 281310.96
assert abs(REPO_STEADY_MONTH * 12 - REPO_STEADY_YEAR) < 0.01
CLIENTS_PER_DAY_REPO = 18        # AM max, 9 pairs x 2 chairs (CURRENT-STATE s00 item 1)
DAYS_PER_MONTH = 22              # weekdays, repo convention
DAYS_YEAR = DAYS_PER_MONTH * 12
BEN_66548 = 16.95                # Medicare benefit (85%) per Anthony brief; schedule fee A$19.90
BEN_73928 = 5.10                 # collection benefit (85%); schedule fee A$5.95
REV_PER_CLIENT = round(BEN_66548 + BEN_73928, 2)
assert REV_PER_CLIENT == 22.05   # repo CURRENT-STATE item 8
GAP_PER_CLIENT = 3.80            # client gap per repo; upside sensitivity only, not in base
ONCOST = 1.25                    # super 12% + leave loading + workers comp (estimate, Theodore)
AREA_M2 = 20

CASES = {
 "low": dict(
  director=150000, director_note="specialist retainer, part-time claim; may NOT satisfy full time S4.1",
  scientist_salary=100000, relief_pct=0.05, assistant_salary=60523, assistant_fte=0.4,
  analyser=10055, backup_poc=2000, centrifuge=2000, fridge_freezer=3000, small_equip=2000,
  lis_setup=3000, lis_annual=2400, fit_rate=3000, prep_legal=5000, nata_initial=5000, nata_annual=3500,
  apl=750, acc_tax=2000, preopen_months=2,
  rcpaqap=2500, qc=1500, service_pct=0.05, waste=1800, insurance=4000, other_fixed=2500,
  reagent_per_test=0.10, consumables_per_client=4.0),
 "base": dict(
  director=250000, director_note="obstetrician full-time package (HCA Doctors / Payscale ~A$250k)",
  scientist_salary=135000, relief_pct=0.10, assistant_salary=68780, assistant_fte=0.6,
  analyser=25000, backup_poc=3000, centrifuge=3500, fridge_freezer=6000, small_equip=3000,
  lis_setup=8000, lis_annual=6000, fit_rate=4000, prep_legal=10000, nata_initial=12000, nata_annual=6000,
  apl=750, acc_tax=2000, preopen_months=3,
  rcpaqap=4000, qc=2500, service_pct=0.08, waste=3000, insurance=8000, other_fixed=4000,
  reagent_per_test=0.30, consumables_per_client=6.0),
 "high": dict(
  director=450000, director_note="top of HCA Doctors O&G range A$250k-450k",
  scientist_salary=158894, relief_pct=0.15, assistant_salary=81776, assistant_fte=1.0,
  analyser=round(40000 * FX_AUD_PER_USD), backup_poc=4000, centrifuge=6000, fridge_freezer=10000, small_equip=5000,
  lis_setup=25000, lis_annual=15000, fit_rate=7000, prep_legal=20000, nata_initial=25000, nata_annual=12000,
  apl=750, acc_tax=2000, preopen_months=6,
  rcpaqap=7000, qc=4000, service_pct=0.10, waste=5000, insurance=18000, other_fixed=7000,
  reagent_per_test=0.60, consumables_per_client=9.0),
}
GLUCOSE_DRAWS = 3          # fasting, 1h, 2h (OGTT); reagent tests per client
REAGENT_WASTE = 1.15       # calibration, QC, repeats

def run(c, clients_per_day=CLIENTS_PER_DAY_REPO):
    scientist_cost = c["scientist_salary"] * ONCOST * (1 + c["relief_pct"])
    assistant_cost = c["assistant_salary"] * c["assistant_fte"] * ONCOST
    staff = c["director"] + scientist_cost + assistant_cost
    fixed_other = (c["lis_annual"] + c["nata_annual"] + c["rcpaqap"] + c["qc"] + c["analyser"] * c["service_pct"]
                   + c["waste"] + c["insurance"] + c["other_fixed"])
    fixed = staff + fixed_other
    var_per_client = c["reagent_per_test"] * GLUCOSE_DRAWS * REAGENT_WASTE + c["consumables_per_client"]
    clients_year = clients_per_day * DAYS_YEAR
    opex = fixed + var_per_client * clients_year
    revenue = REV_PER_CLIENT * clients_year
    fit_out = AREA_M2 * c["fit_rate"]
    preopen = (c["director"] + scientist_cost) / 12 * c["preopen_months"]
    capex_items = dict(analyser=c["analyser"], backup_poc=c["backup_poc"], centrifuge=c["centrifuge"],
        fridge_freezer=c["fridge_freezer"], small_equip=c["small_equip"], lis_setup=c["lis_setup"], fit_out=fit_out,
        prep_legal=c["prep_legal"], nata_initial=c["nata_initial"], apl_fee=c["apl"], acc_tax=c["acc_tax"],
        preopening_staff=round(preopen))
    capex = sum(capex_items.values())
    net = revenue - opex
    contrib = REV_PER_CLIENT - var_per_client
    be_opex_cpd = fixed / contrib / DAYS_YEAR                       # clients/day to cover running cost only
    be_full_cpd = (fixed + capex / 5) / contrib / DAYS_YEAR         # opex + capex over 5 years straight line
    out = dict(
      staff_cost=round(staff), scientist_cost=round(scientist_cost), assistant_cost=round(assistant_cost),
      fixed_opex_year=round(fixed), var_cost_per_client=round(var_per_client, 2),
      opex_12m=round(opex), revenue_12m=round(revenue), net_12m=round(net), net_month=round(net / 12),
      capex=round(capex), capex_items={k: round(v) for k, v in capex_items.items()},
      contribution_per_client=round(contrib, 2),
      breakeven_clients_day_opex_only=round(be_opex_cpd, 1),
      breakeven_clients_day_with_capex_5yr=round(be_full_cpd, 1),
      capacity_clients_day=CLIENTS_PER_DAY_REPO,
      payback_months=(round(capex / (net / 12), 1) if net > 0 else None),
      pays_for_itself_on_glucose_alone=net > 0,
      max_fixed_cost_affordable_at_18=round(contrib * clients_year),
      net_12m_if_client_gap_collected=round((REV_PER_CLIENT + GAP_PER_CLIENT) * clients_year - opex),
      tax_shield_25pct_on_loss=round(max(0, -net) * 0.25),
    )
    # sums
    assert abs(sum(capex_items.values()) - capex) < 1e-6
    assert abs(revenue - opex - net) < 1e-6
    # Route comparison: Route 1 = repo figure, unchanged; Route 2 = repo + lab net (lab net is a loss in all cases)
    out["route1_gtt_profit_year"] = REPO_STEADY_YEAR
    out["route2_gtt_profit_year"] = round(REPO_STEADY_YEAR + net)
    out["route2_minus_route1_year"] = round(net)
    out["extra_funding_needed_vs_repo_peak_251198"] = round(capex)
    return out

res = {k: run(v) for k, v in CASES.items()}
res_inputs = CASES
# volume sensitivity (base): what if the lab could serve more clients/day (e.g. adds 66542 non-pregnant stream, NOT modelled in repo)
sens = {str(n): run(CASES["base"], n)["net_12m"] for n in (18, 36, 60, 90, 120)}
assert res["low"]["net_12m"] > res["base"]["net_12m"] > res["high"]["net_12m"]
assert res["base"]["revenue_12m"] == round(22.05 * 18 * 264)
out = dict(generated="2026-10-20", fx_aud_per_usd=FX_AUD_PER_USD, rev_per_client=REV_PER_CLIENT,
           clients_per_day=CLIENTS_PER_DAY_REPO, days_year=DAYS_YEAR, results=res, base_volume_sensitivity_net_12m=sens,
           inputs=CASES)
here = os.path.dirname(os.path.abspath(__file__))
json.dump(out, open(os.path.join(here, "theodore_categoryS_results.json"), "w"), indent=1)
for k, v in res.items():
    print(k, {x: v[x] for x in ("capex","opex_12m","revenue_12m","net_12m","breakeven_clients_day_opex_only","breakeven_clients_day_with_capex_5yr","max_fixed_cost_affordable_at_18","payback_months")})
print(sens)
