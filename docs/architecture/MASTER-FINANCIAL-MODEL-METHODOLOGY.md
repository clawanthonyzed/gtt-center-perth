# Master Financial Model Methodology

**Date:** 2026-08-09 | **Type:** Phase 9 — the first phase that calculates a real P&L. Combines `docs/architecture/CANONICAL-REVENUE-METHODOLOGY.md`, `data/canonical/revenue_ramp.yml`, and `data/canonical/cost_ramp.yml` into a 24-month deterministic financial model. **Still NOT** investor PDFs, business-plan PDFs, Word docs, Excel presentation workbooks, dashboards, or a funding proposal — those are separately-authorised, later phases.

**Priority order for this phase, per explicit instruction:** correctness > traceability > reproducibility > transparency > scenario separation > auditability > presentation (presentation explicitly last / out of scope).

---

## 1. Purpose and Scope

This document defines the Master Financial Model: a deterministic engine (`tools/master_financial_model.py`) that reads `data/canonical/revenue_ramp.yml` and `data/canonical/cost_ramp.yml` — nothing else for revenue/cost figures — and produces a 24-month P&L, a basic accrual-proxy cash flow, a scoped break-even calculation, a scenario comparison, and sensitivity analysis for both Table 1 and Table 2. Configuration, assumptions, and generated output summaries are recorded in `data/models/master_financial_model.yml`.

**Does not calculate:** EBITDA, EBIT (undefined terms — not used anywhere in this repo), an opening funding requirement, NPV, or IRR. Does not choose Table 1 or Table 2 as primary.

---

## 2. Cost Classifications and Source Hierarchy

Unchanged from `docs/architecture/COST-RAMP-METHODOLOGY.md` §2-3 — this phase does not reclassify any cost. Revenue/cost figures trace, in order: `data/canonical/revenue_ramp.yml` / `data/canonical/cost_ramp.yml` (this phase's direct source) → `docs/architecture/CANONICAL-REVENUE-METHODOLOGY.md` / `docs/architecture/COST-RAMP-METHODOLOGY.md` (the methodology those files implement) → `data/canonical/pricing.yml`, `client_assumptions.yml`, `scenarios.yml`, `staffing.yml`, `wages.yml`, `opex.yml` (the underlying facts).

---

## 3. Model Structure — Scenario A / Scenario B

Per the coordinator's explicit instruction, this document refers to Table 1 (18 clients/day, `scenario_table_1`) and Table 2 (12 clients/day, `scenario_table_2`) — neither becomes primary automatically. `data/canonical/scenarios.yml`'s `is_primary: false` for both is unchanged. `docs/VERIFICATION-TRACKER.md` item 1m remains the pending decision — flagged, not resolved.

---

## 4. 24-Month Forecast Methodology

Months 1-4 map 1:1 to `revenue_ramp.yml`/`cost_ramp.yml`'s own M1-M4 records. **Months 5 through 24 all map to the same M5plus (steady-state) record, held flat.** Per the coordinator's explicit instruction: *"Do NOT invent growth after Month 5 — if there's no documented growth assumption past Month 5, keep revenue flat at canonical steady-state through Month 24."* No document anywhere in this repo states a post-Month-5 growth curve — this is a disclosed absence of an invented assumption, not a claim the venture will not grow. See `data/models/master_financial_model.yml#assumption_24month_extension_flat`.

---

## 5. Revenue

Read directly from `revenue_ramp.yml`'s `am_revenue`, `pm_revenue`, `ancillary_revenue`, `total_revenue` fields — never hard-coded (confirmed by `tests/test_master_financial_model.py`'s `NoHardCodedFinancialOutputsTests`, which greps the engine's source for the canonical/historical headline figures and asserts none appear as literals). Ancillary revenue is shown explicitly as **A$0.00** at every month, not omitted — matching `revenue_ramp.yml`'s own `rev_ancillary_excluded_from_baseline` (VERIFIED) treatment.

**Canonical steady-state (Month 5+):** Table 1 = **A$155,215.80/month** (AM A$118,485.00 + PM A$36,730.80 + Ancillary A$0.00). Table 2 = **A$115,720.80/month** (AM A$78,990.00 + PM A$36,730.80 + Ancillary A$0.00).

---

## 6. Costs

Read directly from `cost_ramp.yml`'s `fixed_costs`, `variable_costs`, `payroll_costs`, `total_operating_costs`, and `payroll_breakdown` fields.

**Payroll breakdown (per the coordinator's requested lines):**
- **AM direct labour** — `payroll_breakdown.am_weekday_direct_labor` (split into `am_weekday_treatment_staff` + `am_weekday_phlebotomist`, see Superannuation below) + `am_saturday_direct_labor` (fixed from Month 1, see `cost_ramp.yml#conflict_am_labor_ramp_unmodelled`).
- **PM direct labour** — `payroll_breakdown.pm_weekday_direct_labor` + `pm_saturday_direct_labor` (ramps via the PM session-count curve, floor-constrained — see `docs/architecture/COST-RAMP-METHODOLOGY.md` §5).
- **Workers comp** — `payroll_breakdown.workers_comp` (1.7% of Direct Labor + Opening Costs).
- **Superannuation** — **RESOLVED 2026-08-09** (`docs/VERIFICATION-TRACKER.md` item 46). `payroll_breakdown.superannuation`, now included directly in `cost_ramp.yml`'s own authoritative `payroll_costs` total — **not** a model-layer special case. Evidence: `docs/financial-break-even-staff.md`'s Award Wage Summary table labels 6 of 7 roles' annual salaries "incl. super" but explicitly not the Phlebotomist row — so super (12% of OTE) is added to the phlebotomist AM-weekday portion, AM Saturday, and both PM Direct Labor components, but NOT to the treatment-staff AM-weekday portion (already included) or to the Opening-Time Increment/Receptionist-Relief components (genuinely unresolved — see `cost_ramp.yml#conflict_superannuation_partial_coverage`). Full sourced reasoning: `docs/architecture/COST-RAMP-METHODOLOGY.md` §4a.
- **Other** — `opening_time_increment` + `receptionist_relief` (payroll-adjacent but not strictly labor; no superannuation applied to these two, per the disclosed gap above).

**Operating expenses (non-payroll):** `cost_ramp.yml`'s `fixed_costs` (Non-Wage Overhead minus marketing — premises, utilities, technology, professional, insurance, consumables, laundry, misc, all FIXED per the status-quo classification) + `variable_costs` (the marketing ramp, the one documented volume/time-ramped opex line).

Startup costs and capex do **not** enter recurring opex — see §13.

---

## 7. Monthly P&L — Terminology and Line Definitions

Per the coordinator's explicit instruction, only terminology this repo actually supports plus a small number of new, explicitly-defined terms this phase introduces:

| Line | Definition | Source |
|---|---|---|
| Revenue | `revenue_ramp.yml`'s `total_revenue` | Canonical |
| Payroll | `cost_ramp.yml`'s `payroll_costs` | Canonical |
| **Gross Contribution** | Revenue − Payroll | **New term, this model's own definition** (not previously used in this repo — defined explicitly here, not invented to "look professional") |
| Operating Expenses | `cost_ramp.yml`'s `fixed_costs` + `variable_costs` | Canonical |
| Total Operating Costs | `cost_ramp.yml`'s `total_operating_costs` (= Payroll + Operating Expenses) | Canonical |
| Net Operating Profit/(Loss) | Revenue − Total Operating Costs (= Gross Contribution − Operating Expenses) | Derived |

No EBITDA, EBIT, or "Net Profit" line is used — these terms are not defined anywhere in this repo's canonical data and are not invented here.

---

## 8. Table 1 — 24-Month P&L

**RECALCULATED 2026-08-09 to include superannuation (`docs/VERIFICATION-TRACKER.md` item 46, resolved). Was Payroll A$80,939.77 (M1-4) / A$81,034.18 (M5+), Net Operating Result A$60,201.62 (M5+) before super was added — see §15 for the prior figure, retained for trace.**

| Month | Revenue | Payroll (incl. super) | Gross Contribution | Operating Expenses | Total Operating Costs | Net Operating Result |
|---|---|---|---|---|---|---|
| M1 | A$66,742.79 | A$84,548.54 | −A$17,805.75 | A$13,080.00 | A$97,628.54 | **−A$30,885.75** |
| M2 | A$99,338.11 | A$84,548.54 | A$14,789.57 | A$13,280.00 | A$97,828.54 | **A$1,509.57** |
| M3 | A$122,620.48 | A$84,548.54 | A$38,071.94 | A$13,480.00 | A$98,028.54 | **A$24,591.94** |
| M4 | A$144,350.69 | A$84,548.54 | A$59,802.15 | A$13,680.00 | A$98,228.54 | **A$46,122.15** |
| M5-M24 (each) | A$155,215.80 | A$84,654.10 | A$70,561.70 | A$13,980.00 | A$98,634.10 | **A$56,581.70** |

**24-month totals:** Revenue A$3,537,368.07; Total Operating Costs A$2,364,396.16; Net Operating Result A$1,172,971.91. **Annualised (steady state):** Revenue A$1,862,589.60; Operating Costs A$1,183,609.20; Net Operating Result A$678,980.40.

---

## 9. Table 2 — 24-Month P&L

**RECALCULATED 2026-08-09 to include superannuation. Was Payroll A$77,388.82 (M1-4) / A$77,483.24 (M5+), Net Operating Result A$24,257.56 (M5+) before super.**

| Month | Revenue | Payroll (incl. super) | Gross Contribution | Operating Expenses | Total Operating Costs | Net Operating Result |
|---|---|---|---|---|---|---|
| M1 | A$49,759.94 | A$80,578.60 | −A$30,818.66 | A$13,080.00 | A$93,658.60 | **−A$43,898.66** |
| M2 | A$74,061.31 | A$80,578.60 | −A$6,517.29 | A$13,280.00 | A$93,858.60 | **−A$19,797.29** |
| M3 | A$91,419.43 | A$80,578.60 | A$10,840.83 | A$13,480.00 | A$94,058.60 | **−A$2,639.17** |
| M4 | A$107,620.34 | A$80,578.60 | A$27,041.74 | A$13,680.00 | A$94,258.60 | **A$13,361.74** |
| M5-M24 (each) | A$115,720.80 | A$80,684.16 | A$35,036.64 | A$13,980.00 | A$94,664.16 | **A$21,056.64** |

**24-month totals:** Revenue A$2,637,277.02; Total Operating Costs A$2,269,117.60; Net Operating Result A$368,159.42. **Annualised (steady state):** Revenue A$1,388,649.60; Operating Costs A$1,135,969.92; Net Operating Result A$252,679.68.

**Material finding:** Table 2's Month 3 Net Operating Result FLIPPED from marginally positive (+A$550.61, pre-super) to **negative (−A$2,639.17)** once superannuation was correctly included — Table 2 does not turn cumulatively profitable on a monthly basis until Month 4.

*(24-month totals shown in §9 above.)*

---

## 10. Scenario Comparison

**RECALCULATED 2026-08-09 for superannuation (item 46).**

| | Table 1 | Table 2 |
|---|---|---|
| Clients/day | 18 | 12 |
| Steady-state revenue | A$155,215.80 | A$115,720.80 |
| Steady-state payroll (incl. super) | A$84,654.10 | A$80,684.16 |
| Steady-state opex | A$13,980.00 | A$13,980.00 |
| Total operating costs | A$98,634.10 | A$94,664.16 |
| Monthly operating result | A$56,581.70 | A$21,056.64 |
| Annualised revenue | A$1,862,589.60 | A$1,388,649.60 |
| Annualised operating result | A$678,980.40 | A$252,679.68 |

**Month snapshot comparison (M1/M3/M5/M12/M24):** M12 and M24 are identical to M5 for both scenarios under the flat-extension rule (§4). Table 1 is profitable from Month 2; Table 2 does not turn profitable until Month 4 (Month 3 is now a loss, −A$2,639.17, once superannuation is included — see §9). Neither scenario is marked primary.

---

## 11. Startup Costs, Capex, and Working Capital — Separate Sections

Kept structurally out of the operating P&L. `tools/master_financial_model.py`'s P&L-critical functions (`compute_month_pnl`, `compute_24_month_pnl`, `compute_cash_flow`) never reference `startup_costs.yml` or `capex.yml` — confirmed by `tests/test_master_financial_model.py`'s `NoStartupCapexLeakageTests`.

**Startup costs:** the adopted range remains A$292,335–594,900 (`docs/CURRENT-STATE.md` §7.4, Anthony's own reconciliation) — **not** re-verified or chosen as "correct" here. `docs/architecture/STARTUP-COST-RECONCILIATION.md`'s finding of 6-9 distinct historical figures stays unresolved.

**Capex:** not aggregated into a single figure this phase — doing so would imply a precision the startup-cost reconciliation itself does not have. `data/canonical/capex.yml`'s itemised asset detail remains the reference.

**Working capital:** `docs/CURRENT-STATE.md` §7.3's reserve (A$85,000-110,000) is itself flagged stale (tracker item 30). This model's own cash-flow trough figures (§12) are a new, more current data point, but this phase does **not** conclude the existing reserve is oversized or undersized — the two figures are not directly comparable without further work (different bases: a 3-month ramp-loss estimate vs. this model's 24-month view).

---

## 12. Basic 24-Month Cash Flow

**Opening cash:** an explicit, un-invented input — `data/models/master_financial_model.yml#assumption_opening_cash_not_invented` (PLACEHOLDER, defaults to `null`). No canonical source states an opening cash figure anywhere in this repo.

**Methodology:** operating cash flow = net operating result, as an **accrual-basis proxy**, explicitly **not** a true cash-basis forecast — no debtor/creditor timing data exists anywhere in this repo (see `assumption_cashflow_accrual_proxy`). Startup expenditure and capex timing are **not** included — no canonical per-month timing schedule exists for either.

**RECALCULATED 2026-08-09 for superannuation (item 46). Was: Table 1 trough −A$27,276.98 (M1); Table 2 trough −A$57,316.39 (M2).**

| | Table 1 | Table 2 |
|---|---|---|
| Cumulative position, M1 | −A$30,885.75 | −A$43,898.66 |
| Cumulative position, M4 | A$41,337.91 | −A$52,973.38 |
| Cumulative position, M12 | A$493,991.51 | A$115,479.74 |
| Cumulative position, M24 | A$1,172,971.91 | A$368,159.42 |
| Trough month | M1 | **M3 (moved from M2)** |
| Trough cumulative position | **−A$30,885.75** | **−A$66,335.12** |

**Material change:** Table 2's trough moved from Month 2 to Month 3 and deepened materially (was −A$57,316.39, now −A$66,335.12), because Month 3's net operating result flipped from marginally positive to a loss once superannuation was correctly included (§9).

**These trough figures are OPERATING cash movements only** — they do NOT include startup capital deployment and must not be read as "the venture needs only this much funding" (`conflict_funding_requirement_not_established`, explicitly disclosed, item 47 untouched this phase).

---

## 13. Break-Even — Scope and Defensibility

A traditional contribution-margin break-even (fixed costs ÷ contribution margin %) is **not** computed. Reason, stated explicitly per the coordinator's instruction: nearly every cost in `cost_ramp.yml` is classified FIXED (including AM/PM payroll under this model's current, disclosed treatment — see `conflict_am_labor_ramp_unmodelled`), and the one disputed classification (GTT supplies/consumables/laundry) remains unresolved (`conflict_variable_vs_fixed_classification_carried_forward`).

**What IS computed and defensible:** an AM client-volume break-even, holding Month 5+ PM revenue/payroll/opex fixed and treating AM revenue as the one genuinely linear-in-volume component (price × operating days).

**RECALCULATED 2026-08-09 for superannuation (item 46). Was: Table 1 8.854 clients/day (margin 9.146); Table 2 8.315 clients/day (margin 3.685).**

| | Table 1 | Table 2 |
|---|---|---|
| Break-even AM client volume/day | **9.404** | **8.801** |
| Break-even monthly revenue | A$98,632.63 | A$94,663.38 |
| Committed client volume/day | 18 | 12 |
| Margin of safety (clients/day) | 8.596 (~48% of committed) | 3.199 (~27% of committed) |

Break-even volume rose and margin of safety narrowed for both scenarios once superannuation was included, but Table 1 remains comfortably below committed volume. Table 2's margin of safety is now materially thinner (~27%, down from ~31%) — a genuine, disclosed risk-profile difference between the two scenarios.

---

## 14. Sensitivity Analysis

**RECALCULATED 2026-08-09 for superannuation (item 46).**

**Client volume (50/75/100/125% of committed):** payroll and opex held at Month 5+ steady state, per `assumption_sensitivity_payroll_not_flexed` (matching the base case's own disclosed conservatism — no invented payroll-flex methodology). **Material change: Table 1 at 50% of committed volume is now LOSS-MAKING (−A$2,660.80/month)**, reversing the prior (pre-super) finding that it remained marginally profitable (+A$959.12/month). Table 2 at 50% deepens to −A$18,438.36/month (was −A$15,237.44/month) — a materially different risk profile from Table 1 at the same relative shortfall.

**Insurance (modelled A$400/month vs. itemised A$975-1,583/month, mandatory policies only):** at Table 1, Net Operating Result now ranges A$56,065.04-56,581.70/month depending on which insurance figure is used — the same ~A$516.66/month delta as before, now measured against a lower (post-super) base. Neither figure is chosen as correct (`opex.yml#conflict_insurance_estimate`, unresolved).

**Payroll (wage conflicts 16-18):** **not** flexed in this sensitivity — the underlying wage-rate/penalty-rate conflicts remain PLACEHOLDER/UNRESOLVED (`wages.yml`), and this model does not invent a resolution to produce a sensitivity range that doesn't exist in the source data.

**AM staffing ramp:** only the full-from-Month-1 treatment is modelled — no alternative reduced-headcount ramp is computed, since no source-supported methodology exists for it against Table 1/Table 2's current cadence (`staffing.yml`'s own disclosed gap, see `cost_ramp.yml#conflict_am_labor_ramp_unmodelled`). Per the coordinator's explicit instruction, an alternative is not invented.

**Consumables:** the FIXED-vs-VARIABLE classification conflict remains visible and unresolved — not flexed into a sensitivity range this phase (see `cost_ramp.yml#conflict_variable_vs_fixed_classification_carried_forward`, `gtt_supplies_variable_alternative`).

---

## 15. Historical Reconciliation

| | Canonical | Historical (superseded) | Gap |
|---|---|---|---|
| Table 1 Monthly Revenue | **A$155,215.80** (CALCULATED) | A$157,792.16 (SUPERSEDED) | A$2,576.36, origin permanently unresolved (item 36) |
| Table 2 Monthly Revenue | **A$115,720.80** (CALCULATED) | A$118,297.16 (SUPERSEDED) | Same gap, same disclosed origin |
| Table 1 Monthly NET P&L (historical) | — | **A$63,028.75** (SUPERSEDED) | **This is Net P&L, NOT revenue** — confirmed again this phase (`docs/VERIFICATION-TRACKER.md` item 40). This model's own comparable figure is Net Operating Result (**A$56,581.70** for Table 1, RECALCULATED 2026-08-09 to include superannuation, item 46 — was A$60,201.62 before) — a third, genuinely different number, since it is built on canonical revenue, `cost_ramp.yml`'s own slightly different payroll total (`conflict_direct_labor_reconciliation_gap`), AND now superannuation (never included in the historical figure at all). Not a typo — genuinely different figures for related-but-different things. |

None of these historical figures was altered to match the canonical model, and the canonical model was not altered to match them, per explicit instruction.

---

## 16. Data Traceability — Example Dependency Chains

1. **Table 1 Month 12 Revenue** → `outputs.steady_state_summary` (this model) → `revenue_ramp.yml#ramp_table1_m5plus` (Month 12 = M5plus, per §4) → `docs/architecture/CANONICAL-REVENUE-METHODOLOGY.md` → `scenarios.yml#scenario_table_1.client_volume` → `pricing.yml#am_price_used_for_revenue`, `#pm_alacarte_average`.
2. **Table 1 Month 12 Payroll** → `cost_ramp.yml#cost_table1_m5plus.payroll_breakdown` → `staffing.yml` (headcount) + `wages.yml` (rates) → `wages.yml#wage_casual_minimum_engagement` (the 3-hour floor governing PM labor) → `wages.yml#wage_superannuation_rate` (12% OTE, added 2026-08-09, item 46) → `docs/financial-break-even-staff.md` Award Wage Summary lines 29-37 (inclusive/exclusive treatment per role).
3. **Table 1 Month 12 Insurance** → `outputs.sensitivity_insurance` → `cost_ramp.yml#cost_table1_m5plus.fixed_costs` → `opex.yml#opex_insurance_modelled` → `docs/profit-loss-tables.md` §4 (original source) → `opex.yml#conflict_insurance_estimate` (UNRESOLVED).

Full chains (5 total) recorded in `data/models/master_financial_model.yml#traceability`.

---

## 17. Unresolved Assumptions — Full List

1. Wage conflicts (`wages.yml` items 16-18) — MA000005 penalty rates, base-rate disagreement, staleness. **Not resolved** — this model does not reference disputed penalty rates at all.
2. PM pre-booking discount (item 39) — **not** applied; PM revenue at steady state remains the full undiscounted A$36,730.80.
3. Revenue ramp curve origin (items 41-42) — reused as-is, origin remains undocumented.
4. AM labour ramp (item 43) — this model's cost figures assume full AM staffing from Month 1; **not** silently changed, explicitly labelled a current modelling assumption (`assumption_sensitivity_payroll_not_flexed`).
5. Direct Labor reconciliation gap (item 44) — the ~A$246.57/month gap stays disclosed, propagates into this model's Net Operating Result unchanged.
6. Consumables/laundry classification (item 45) — not invented, GTT-supplies-only exploratory alternative remains non-primary.
7. **RESOLVED 2026-08-09 (item 46):** superannuation was not included in any payroll total anywhere in this repo's history — now implemented at the canonical cost/wage layer (`wages.yml` + `cost_ramp.yml`, §6/§4a of `docs/architecture/COST-RAMP-METHODOLOGY.md`), flowing through this model automatically. A narrower gap remains: superannuation is NOT applied to the Opening-Time Increment or Receptionist/Relief Pool components (`cost_ramp.yml#conflict_superannuation_partial_coverage`) — genuinely unresolved, not guessed at. The eligibility rule (minimum-earnings threshold, if any) is also not stated anywhere in this repo.
8. No opening funding requirement is established — the cash-flow trough figures are operating-only, explicitly not a funding conclusion. **Item 47 remains untouched this phase, per explicit instruction** — only the trough figures themselves were kept numerically consistent with the recalculated cash flow (§12).

---

## 18. Limitations

This model does not sequence startup capital deployment against the operating cash flow (no canonical timing data exists). It does not model debtor/creditor payment timing (cash ≈ accrual is a disclosed simplification). It does not flex payroll with actual client volume during ramp-up (matches `cost_ramp.yml`'s own disclosed conservatism). It does not resolve any pre-existing unresolved tracker item. It is not a substitute for accountant review before any real funding conversation.
