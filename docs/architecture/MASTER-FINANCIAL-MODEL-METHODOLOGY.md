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
- **AM direct labour** — `payroll_breakdown.am_weekday_direct_labor` + `am_saturday_direct_labor` (fixed from Month 1, see `cost_ramp.yml#conflict_am_labor_ramp_unmodelled`).
- **PM direct labour** — `payroll_breakdown.pm_weekday_direct_labor` + `pm_saturday_direct_labor` (ramps via the PM session-count curve, floor-constrained — see `docs/architecture/COST-RAMP-METHODOLOGY.md` §5).
- **Workers comp** — `payroll_breakdown.workers_comp` (1.7% of Direct Labor + Opening Costs).
- **Superannuation** — **NOT** in `cost_ramp.yml`'s own payroll total. A genuinely new finding this phase: superannuation (`wages.yml#wage_superannuation_rate`, 12% of OTE) is not included anywhere in this venture's payroll modelling — not in `cost_ramp.yml`, and not in any historical `CURRENT-STATE.md` figure either. Shown here as a disclosed, **supplementary** line (`superannuation_supplementary` in every P&L month), calculated but NOT folded into the primary Total Operating Costs / Net Operating Result, to preserve exact traceability to `cost_ramp.yml`'s already-validated total. See `conflict_superannuation_not_in_cost_ramp` and the new tracker item this phase adds.
- **Other** — `opening_time_increment` + `receptionist_relief` (payroll-adjacent but not strictly labor).

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

| Month | Revenue | Payroll | Gross Contribution | Operating Expenses | Total Operating Costs | Net Operating Result |
|---|---|---|---|---|---|---|
| M1 | A$66,742.79 | A$80,939.77 | −A$14,196.98 | A$13,080.00 | A$94,019.77 | **−A$27,276.98** |
| M2 | A$99,338.11 | A$80,939.77 | A$18,398.34 | A$13,280.00 | A$94,219.77 | **A$5,118.34** |
| M3 | A$122,620.48 | A$80,939.77 | A$41,680.71 | A$13,480.00 | A$94,419.77 | **A$28,200.71** |
| M4 | A$144,350.69 | A$80,939.77 | A$63,410.92 | A$13,680.00 | A$94,619.77 | **A$49,730.92** |
| M5-M24 (each) | A$155,215.80 | A$81,034.18 | A$74,181.62 | A$13,980.00 | A$95,014.18 | **A$60,201.62** |

**24-month totals:** Revenue A$3,537,368.07; Total Operating Costs A$2,277,562.68; Net Operating Result A$1,259,805.39. **Annualised (steady state):** Revenue A$1,862,589.60; Operating Costs A$1,140,170.16; Net Operating Result A$722,419.44.

**If superannuation is included** (supplementary, not primary): Month 1-4 Net Operating Result would be ~A$9,550.41/month lower; Month 5+ ~A$9,561.56/month lower.

---

## 9. Table 2 — 24-Month P&L

| Month | Revenue | Payroll | Gross Contribution | Operating Expenses | Total Operating Costs | Net Operating Result |
|---|---|---|---|---|---|---|
| M1 | A$49,759.94 | A$77,388.82 | −A$27,628.88 | A$13,080.00 | A$90,468.82 | **−A$40,708.88** |
| M2 | A$74,061.31 | A$77,388.82 | −A$3,327.51 | A$13,280.00 | A$90,668.82 | **−A$16,607.51** |
| M3 | A$91,419.43 | A$77,388.82 | A$14,030.61 | A$13,480.00 | A$90,868.82 | **A$550.61** |
| M4 | A$107,620.34 | A$77,388.82 | A$30,231.52 | A$13,680.00 | A$91,068.82 | **A$16,551.52** |
| M5-M24 (each) | A$115,720.80 | A$77,483.24 | A$38,237.56 | A$13,980.00 | A$91,463.24 | **A$24,257.56** |

**24-month totals:** Revenue A$2,637,277.02; Total Operating Costs A$2,192,340.08; Net Operating Result A$444,936.94. **Annualised (steady state):** Revenue A$1,388,649.60; Operating Costs A$1,097,558.88; Net Operating Result A$291,090.72.

**Notable finding:** Table 2's Month 3 Net Operating Result is only +A$550.61 — a thin margin, materially different from Table 1's comfortable Month 3 profitability (+A$28,200.71).

---

## 10. Scenario Comparison

| | Table 1 | Table 2 |
|---|---|---|
| Clients/day | 18 | 12 |
| Steady-state revenue | A$155,215.80 | A$115,720.80 |
| Steady-state payroll | A$81,034.18 | A$77,483.24 |
| Steady-state opex | A$13,980.00 | A$13,980.00 |
| Total operating costs | A$95,014.18 | A$91,463.24 |
| Monthly operating result | A$60,201.62 | A$24,257.56 |
| Annualised revenue | A$1,862,589.60 | A$1,388,649.60 |
| Annualised operating result | A$722,419.44 | A$291,090.72 |

**Month snapshot comparison (M1/M3/M5/M12/M24):** M12 and M24 are identical to M5 for both scenarios under the flat-extension rule (§4). Table 1 is profitable from Month 2; Table 2 from Month 3 (barely). Neither scenario is marked primary.

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

| | Table 1 | Table 2 |
|---|---|---|
| Cumulative position, M1 | −A$27,276.98 | −A$40,708.88 |
| Cumulative position, M4 | A$55,772.99 | −A$40,214.26 |
| Cumulative position, M12 | A$537,385.95 | A$153,846.22 |
| Cumulative position, M24 | A$1,259,805.39 | A$444,936.94 |
| Trough month | M1 | M2 |
| Trough cumulative position | **−A$27,276.98** | **−A$57,316.39** |

**These trough figures are OPERATING cash movements only** — they do NOT include startup capital deployment and must not be read as "the venture needs only this much funding" (`conflict_funding_requirement_not_established`, explicitly disclosed).

---

## 13. Break-Even — Scope and Defensibility

A traditional contribution-margin break-even (fixed costs ÷ contribution margin %) is **not** computed. Reason, stated explicitly per the coordinator's instruction: nearly every cost in `cost_ramp.yml` is classified FIXED (including AM/PM payroll under this model's current, disclosed treatment — see `conflict_am_labor_ramp_unmodelled`), and the one disputed classification (GTT supplies/consumables/laundry) remains unresolved (`conflict_variable_vs_fixed_classification_carried_forward`).

**What IS computed and defensible:** an AM client-volume break-even, holding Month 5+ PM revenue/payroll/opex fixed and treating AM revenue as the one genuinely linear-in-volume component (price × operating days).

| | Table 1 | Table 2 |
|---|---|---|
| Break-even AM client volume/day | **8.854** | **8.315** |
| Break-even monthly revenue | A$95,012.26 | A$91,464.29 |
| Committed client volume/day | 18 | 12 |
| Margin of safety (clients/day) | 9.146 (~51% of committed) | 3.685 (~31% of committed) |

Table 2's margin of safety is materially thinner — a genuine, disclosed risk-profile difference between the two scenarios.

---

## 14. Sensitivity Analysis

**Client volume (50/75/100/125% of committed):** payroll and opex held at Month 5+ steady state, per `assumption_sensitivity_payroll_not_flexed` (matching the base case's own disclosed conservatism — no invented payroll-flex methodology). Table 1 remains marginally profitable even at 50% of committed volume (+A$959.12/month); Table 2 is loss-making at 50% (−A$15,237.44/month) — a materially different risk profile.

**Insurance (modelled A$400/month vs. itemised A$975-1,583/month, mandatory policies only):** at Table 1, Net Operating Result ranges A$59,684.96-60,201.62/month depending on which insurance figure is used — a small (~0.9%) but real sensitivity. Neither figure is chosen as correct (`opex.yml#conflict_insurance_estimate`, unresolved).

**Payroll (wage conflicts 16-18):** **not** flexed in this sensitivity — the underlying wage-rate/penalty-rate conflicts remain PLACEHOLDER/UNRESOLVED (`wages.yml`), and this model does not invent a resolution to produce a sensitivity range that doesn't exist in the source data.

**AM staffing ramp:** only the full-from-Month-1 treatment is modelled — no alternative reduced-headcount ramp is computed, since no source-supported methodology exists for it against Table 1/Table 2's current cadence (`staffing.yml`'s own disclosed gap, see `cost_ramp.yml#conflict_am_labor_ramp_unmodelled`). Per the coordinator's explicit instruction, an alternative is not invented.

**Consumables:** the FIXED-vs-VARIABLE classification conflict remains visible and unresolved — not flexed into a sensitivity range this phase (see `cost_ramp.yml#conflict_variable_vs_fixed_classification_carried_forward`, `gtt_supplies_variable_alternative`).

---

## 15. Historical Reconciliation

| | Canonical | Historical (superseded) | Gap |
|---|---|---|---|
| Table 1 Monthly Revenue | **A$155,215.80** (CALCULATED) | A$157,792.16 (SUPERSEDED) | A$2,576.36, origin permanently unresolved (item 36) |
| Table 2 Monthly Revenue | **A$115,720.80** (CALCULATED) | A$118,297.16 (SUPERSEDED) | Same gap, same disclosed origin |
| Table 1 Monthly NET P&L (historical) | — | **A$63,028.75** (SUPERSEDED) | **This is Net P&L, NOT revenue** — confirmed again this phase (`docs/VERIFICATION-TRACKER.md` item 40). This model's own comparable figure is Net Operating Result (A$60,201.62 for Table 1) — a third, genuinely different number, since it is built on canonical revenue AND `cost_ramp.yml`'s own slightly different payroll total (`conflict_direct_labor_reconciliation_gap`). Not a typo — three distinct figures for related-but-different things. |

None of these historical figures was altered to match the canonical model, and the canonical model was not altered to match them, per explicit instruction.

---

## 16. Data Traceability — Example Dependency Chains

1. **Table 1 Month 12 Revenue** → `outputs.steady_state_summary` (this model) → `revenue_ramp.yml#ramp_table1_m5plus` (Month 12 = M5plus, per §4) → `docs/architecture/CANONICAL-REVENUE-METHODOLOGY.md` → `scenarios.yml#scenario_table_1.client_volume` → `pricing.yml#am_price_used_for_revenue`, `#pm_alacarte_average`.
2. **Table 1 Month 12 Payroll** → `cost_ramp.yml#cost_table1_m5plus.payroll_breakdown` → `staffing.yml` (headcount) + `wages.yml` (rates) → `wages.yml#wage_casual_minimum_engagement` (the 3-hour floor governing PM labor).
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
7. **New this phase:** superannuation is not included in any payroll total anywhere in this repo's history — a materially significant, newly-surfaced gap (§6, new tracker item).
8. **New this phase:** no opening funding requirement is established — the cash-flow trough figures are operating-only, explicitly not a funding conclusion.

---

## 18. Limitations

This model does not sequence startup capital deployment against the operating cash flow (no canonical timing data exists). It does not model debtor/creditor payment timing (cash ≈ accrual is a disclosed simplification). It does not flex payroll with actual client volume during ramp-up (matches `cost_ramp.yml`'s own disclosed conservatism). It does not resolve any pre-existing unresolved tracker item. It is not a substitute for accountant review before any real funding conversation.
