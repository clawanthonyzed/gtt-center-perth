# Cost Ramp Methodology — Month 1-5+

**Date:** 2026-08-09 | **Type:** bounded cost-side data-model component, the counterpart to `docs/architecture/REVENUE-RAMP-METHODOLOGY.md`. **Not** the Master Financial Model, P&L, cash-flow forecast, break-even, Excel, or PDF — cost side only. No Net P&L, EBITDA, cash balance, opening funding requirement, NPV, or IRR is calculated anywhere in this document or its supporting code.

---

## 1. Purpose

`docs/architecture/REVENUE-RAMP-METHODOLOGY.md` rebuilt the Month 1-5+ revenue ramp on the canonical revenue methodology. This document does the same for costs: a deterministic, auditable Month 1-5+ cost ramp for Table 1 (18-client) and Table 2 (12-client), broken into Fixed / Variable / Payroll, sourced entirely from canonical data plus a small set of named, individually-cited constants.

---

## 2. Cost Classifications

Every cost in `data/canonical/opex.yml` already carries a `cost_type` (FIXED / VARIABLE / SEMI_VARIABLE / ONE_OFF / STARTUP / CAPEX / COGS / PAYROLL, established Phase 3). This phase does not change any existing `cost_type` value — it builds a ramp calculation ON TOP of the existing classifications, and where a classification is itself disputed (GTT supplies, consumables, laundry — `conflict_variable_vs_fixed_classification`), the status-quo classification is carried forward unchanged for the primary calculation (§6).

---

## 3. Source Hierarchy

1. `data/canonical/opex.yml` — non-payroll operating expenses (13-line Non-Wage Overhead total, A$13,980.00/month).
2. `data/canonical/wages.yml` — hourly/casual rates, superannuation, workers comp rate, casual minimum engagement.
3. `data/canonical/staffing.yml` — headcount, category, employment type.
4. `docs/profit-loss-tables.md`'s own "Appendix — How Every Figure Is Calculated" — the source for every payroll constant this phase reuses (see §4).
5. `docs/CURRENT-STATE.md` §5 — the canonical Month 5+ steady-state Total Costs figures, used as a comparison anchor, not force-reconciled against (§7-8).

---

## 4. Payroll Methodology

Payroll is modelled separately from ordinary opex, per the coordinator's instruction. Six components make up "Direct Labor + Opening Costs," each with its own disclosed ramp behaviour:

| Component | Ramp behaviour | Why |
|---|---|---|
| AM Weekday Direct Labor (A$48,254.67/month) | **Fixed from Month 1** | Explicitly FTE/fixed-salary, "UNCHANGED... same 8+2 headcount" per `docs/CURRENT-STATE.md` §5 — these staff are on payroll regardless of actual daily booking volume. |
| AM Saturday Direct Labor (scenario-specific: A$2,419.11/day Table 1, A$1,612.74/day Table 2) | **Fixed from Month 1**, at the scenario's own committed level | "Scales with volume" language in this repo refers to scaling between committed scenarios (12→18 clients), not a month-to-month ramp-up methodology, which does not exist anywhere in this repo. A genuine reduced-headcount option exists for lower-volume days (7 staff instead of 8) but `staffing.yml`'s own `staff_treatment_massage_beauty_pool` record explicitly flags this has NOT been re-verified against Table 1/Table 2's cadence — cannot be safely applied without inventing an unconfirmed methodology. **Disclosed limitation, not a discovered fact** — see `conflict_am_labor_ramp_unmodelled`. |
| PM Weekday Direct Labor | **Ramps**, per the session-count curve + 3-hour floor (§5) | Directly tied to session count via `docs/pm-staffing-roster.md`'s own hours-based costing formula. |
| PM Saturday Direct Labor (A$654.32/day) | **Fixed**, mathematically, regardless of ramp | Even at full 8-session steady state, hours/role/day (1.54hrs) is already below the 3-hour casual-minimum floor — the cost cannot fall below the floor amount at any session-count assumption. |
| Opening-time increment (A$44.50/day) | **Fixed from Month 1** | A per-trading-day operational cost, not booking-volume-dependent. |
| Receptionist/Relief Pool (A$339.00/day) | **Fixed from Month 1** | Receptionist is a committed Day-1 hire, not session-dependent. |
| Workers Comp (1.7%) | **Ramps automatically** | A percentage of Direct Labor + Opening Costs — moves with whatever that total is each month. |

---

## 5. The PM Session-Count Payroll Ramp

Reuses `data/canonical/revenue_assumptions.yml`'s already-canonical `rev_pm_session_ramp_historical` (4/8/12/15/16 sessions/day), **not** the blanket 43/64/79/93/100% revenue-ramp curve. Justified because PM labor cost is a direct function of session count via the formula `hours/role/day = sessions/day ÷ 4 roles ÷ 1.3 sessions/hr throughput` — this is the session-count curve's most plausible original purpose, per `docs/architecture/REVENUE-RAMP-METHODOLOGY.md` §5's own finding that this same curve does NOT match the revenue figures actually used in `docs/profit-loss-tables.md`'s P&L ramp table.

**Genuine, disclosed finding this phase (not previously computed anywhere in this repo):** the 3-hour casual-minimum-engagement floor (`wages.yml#wage_casual_minimum_engagement`, VERIFIED) means **Months 1, 2, 3, and 4 all produce the identical PM weekday labor cost** (A$435.78/day) — 4, 8, 12, and even 15 sessions/day all fall below the 3.0-hour floor threshold (15 sessions/4 roles/1.3 throughput = 2.885hrs, just under). Only Month 5+ (16 sessions, 3.077hrs/role) clears the floor and reaches the higher rate. PM Direct Labor therefore does NOT ramp gradually across Months 1-4 as revenue does — it is flat, then steps up once at Month 5+.

---

## 6. Variable-Cost Methodology, and the GTT Supplies/Consumables/Laundry Investigation

Per the coordinator's explicit instruction, this phase investigated whether GTT supplies, general consumables, and laundry/linen (currently FIXED in `opex.yml`, per `conflict_variable_vs_fixed_classification` vs. `docs/unit-economics.md`'s historical VARIABLE treatment) should be treated as genuinely volume-dependent in the ramp.

**Finding:** only **GTT supplies** has an unambiguous per-unit volume denominator available in canonical data (1 test per AM GTT client — `client_volume`, already canonical). An exploratory, **non-primary** `gtt_supplies_variable_alternative` calculation was built (§9), using `opex_gtt_supplies`' own stated basis (A$2.00/test), applied to ramped client volume × weekday operating days — matching that record's own already-disclosed "~A$792/month at 396 tests" methodology exactly, not a new assumption.

**Consumables and laundry could NOT safely be migrated to a variable alternative this phase.** `docs/unit-economics.md`'s own per-visit rates for these two ($2.60/visit, $1.14/visit) are denominated in "total visits" — a figure not cleanly defined anywhere in current canonical data (is it AM clients only, PM sessions only, or combined? `unit-economics.md` itself is historical/stale and doesn't resolve this for the current model). Computing a variable alternative for these two would require inventing a "total visits" definition — not done, per the explicit "don't invent" instruction. This is disclosed as a genuine "could not safely migrate" finding, not silently skipped.

**The one already-documented, genuinely volume-dependent opex line is marketing** (`opex_marketing_ads_ramp`, A$600→A$800→A$1,000→A$1,200→A$1,500), which this ramp uses directly as the "Variable Costs" bucket for the top-level Fixed/Variable/Payroll table — the only opex.yml component with an explicit, sourced, already-established Month 1-4 ramp anywhere in this repo.

---

## 7. Ramp Methodology (Revenue Ramp vs. Cost Ramp — Explicitly Not the Same)

Per the coordinator's explicit instruction, the 43/64/79/93/100% revenue curve was **not** automatically applied to every cost. Each cost's ramp behaviour was individually investigated (§4-6):

| Cost | Ramp curve used | Same as revenue ramp? |
|---|---|---|
| Rent, utilities, cleaning, insurance, tech, professional, consumables (status quo) | None — fixed from Month 1 | No |
| Marketing | Its own documented ramp (A$600→A$1,500) | No — a different, independently-sourced curve |
| AM Direct Labor (weekday + Saturday) | None — fixed from Month 1 | No |
| PM Direct Labor (weekday) | Session-count curve (25%/50%/75%/93.75%/100%, floor-adjusted) | **No** — different from the revenue curve, confirmed by direct test (`tests/test_cost_ramp.py`'s `test_pm_payroll_ramp_curve_differs_from_revenue_ramp_curve`) |
| PM Direct Labor (Saturday) | None — mathematically constant | No |
| Workers Comp | Automatic (% of Direct Labor) | Indirectly, only insofar as Direct Labor changes |

---

## 8. Table 1 Results (18 clients/day)

| Month | Fixed | Variable | Payroll | Total Operating Costs |
|---|---|---|---|---|
| M1 | A$12,480.00 | A$600.00 | A$80,939.77 | A$94,019.77 |
| M2 | A$12,480.00 | A$800.00 | A$80,939.77 | A$94,219.77 |
| M3 | A$12,480.00 | A$1,000.00 | A$80,939.77 | A$94,419.77 |
| M4 | A$12,480.00 | A$1,200.00 | A$80,939.77 | A$94,619.77 |
| M5+ | A$12,480.00 | A$1,500.00 | A$81,034.18 | **A$95,014.18** |

**Reconciliation, disclosed not hidden:** `docs/CURRENT-STATE.md` §5's own stated Table 1 Total Costs is A$94,763.41. This file's Month 5+ Total Operating Costs (A$95,014.18) differs by A$250.77/month (0.26%) — traced to a A$246.58/month gap in the Direct Labor + Opening Costs component (§4's "Receptionist/Relief" figure is taken at face value from the source's own "≈" approximate figure, not back-solved to force an exact match, consistent with this repo's established practice of disclosing rather than force-reconciling small gaps — see `conflict_direct_labor_reconciliation_gap`).

---

## 9. Table 2 Results (12 clients/day)

| Month | Fixed | Variable | Payroll | Total Operating Costs |
|---|---|---|---|---|
| M1 | A$12,480.00 | A$600.00 | A$77,388.82 | A$90,468.82 |
| M2 | A$12,480.00 | A$800.00 | A$77,388.82 | A$90,668.82 |
| M3 | A$12,480.00 | A$1,000.00 | A$77,388.82 | A$90,868.82 |
| M4 | A$12,480.00 | A$1,200.00 | A$77,388.82 | A$91,068.82 |
| M5+ | A$12,480.00 | A$1,500.00 | A$77,483.24 | **A$91,463.24** |

Same disclosed A$250.77/month (0.27%) gap against `docs/CURRENT-STATE.md`'s own stated Table 2 Total Costs (A$91,212.47), same root cause as Table 1. Also carries `docs/VERIFICATION-TRACKER.md` item 1o's own open question (whether the A$44.50/day opening increment should apply to Table 2's 08:00 start) — included unchanged, not independently resolved.

**GTT supplies variable alternative (exploratory, not in the totals above):** Table 1 ranges A$340.56 (M1) → A$792.00 (M5+, matching the already-disclosed estimate exactly); Table 2 ranges A$227.04 (M1) → A$528.00 (M5+) — both materially higher than the current flat A$400.00/month modelled figure at steady state, consistent with `docs/VERIFICATION-TRACKER.md` item 22's existing finding.

Both tables generated deterministically by `tools/cost_ramp_model.py` and recorded in `data/canonical/cost_ramp.yml`; reproducibility proven by `tests/test_cost_ramp.py` (35 tests).

---

## 10. Unresolved Assumptions

1. Whether AM (weekday or Saturday) labor should genuinely ramp down during Months 1-4 via a reduced-headcount roster — a real mechanism exists in this repo (7 staff instead of 8) but is unconfirmed against Table 1/Table 2's cadence.
2. Whether the A$44.50/day opening-time increment applies to Table 2's 08:00 start (pre-existing, item 1o).
3. The FIXED-vs-VARIABLE classification of GTT supplies, consumables, and laundry (pre-existing, item 22) — carried forward unresolved.
4. Whether consumables/laundry can ever be safely expressed as a per-visit variable cost without a canonical "total visits" definition — genuinely blocked, not just undecided.
5. The three unresolved MA000005 penalty-rate conflicts (items 16-18) — **not touched, not resolved, not silently picked** — this model does not reference weekend/PH penalty rates at all (Saturday costing uses the already-established, separately-sourced A$654.32/day and A$2,419.11 (or A$1,612.74)/day figures, not a fresh penalty-rate calculation).
6. Whether the historical Fixed-Costs-flat-from-Month-1 simplification in the old 12-client Year 1 Monthly Ramp table (`docs/profit-loss-tables.md`) should be considered superseded now that this file provides an actual payroll ramp — a modelling-authority decision for Anthony/whoever builds the eventual P&L, not decided here.

---

## 11. Conflicts

Four declared in `data/canonical/cost_ramp.yml`'s `conflicts` list: `conflict_am_labor_ramp_unmodelled`, `conflict_direct_labor_reconciliation_gap`, `conflict_table2_opening_increment_unresolved`, `conflict_variable_vs_fixed_classification_carried_forward`. Full detail in each record, not repeated here.

---

## 12. Limitations

This is a cost-side data-model component, not a cash-flow or funding-requirement tool. It does not know when the venture opens, does not sequence startup capital deployment, and — critically — startup and capex costs are structurally excluded (§13), not merely flagged, since `tools/cost_ramp_model.py` never reads `startup_costs.yml` or `capex.yml` at all (confirmed by `tests/test_cost_ramp.py`'s `NoCapexLeakageTests`).

---

## 13. Startup/Capex Exclusion — Confirmed by Design, Not Just by Convention

`tools/cost_ramp_model.py` does not import, reference, or read `data/canonical/startup_costs.yml` or `data/canonical/capex.yml` anywhere in its source code — a structural guarantee, not a discipline that could be silently violated by a future edit. `opex.yml` records classified `STARTUP` (e.g. `opex_accountant_initial_brief`, `opex_food_safety_supervisor_cert`) carry `monthly_equivalent: null` by design in their own source records and are never referenced by this module — confirmed by `tests/test_cost_ramp.py`'s `NoStartupCostLeakageTests`.

---

## 14. Relationship to `revenue_ramp.yml`

Both files share the same Month 1-5+/scenario structure and month vocabulary (M1-M4, M5plus), enabling a future Net P&L calculation (`revenue_ramp.yml`'s `total_revenue` minus this file's `total_operating_costs`, per month per scenario) — explicitly NOT computed here, per the coordinator's financial-model boundary. The two files use genuinely different ramp curves for their respective PM components (revenue: blanket 43/64/79/93/100%; cost: session-count-based, floor-adjusted) — a disclosed, deliberate divergence, not an oversight, since PM revenue and PM labor cost are governed by different underlying mechanics (average price vs. hours-based casual engagement rules).
