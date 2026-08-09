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
| AM Weekday Direct Labor (A$48,254.67/month total, split A$41,076.67 treatment staff + A$7,178.00 phlebotomist — see §4a) | **Fixed from Month 1** | Explicitly FTE/fixed-salary, "UNCHANGED... same 8+2 headcount" per `docs/CURRENT-STATE.md` §5 — these staff are on payroll regardless of actual daily booking volume. |
| AM Saturday Direct Labor (scenario-specific: A$2,419.11/day Table 1, A$1,612.74/day Table 2) | **Fixed from Month 1**, at the scenario's own committed level | "Scales with volume" language in this repo refers to scaling between committed scenarios (12→18 clients), not a month-to-month ramp-up methodology, which does not exist anywhere in this repo. A genuine reduced-headcount option exists for lower-volume days (7 staff instead of 8) but `staffing.yml`'s own `staff_treatment_massage_beauty_pool` record explicitly flags this has NOT been re-verified against Table 1/Table 2's cadence — cannot be safely applied without inventing an unconfirmed methodology. **Disclosed limitation, not a discovered fact** — see `conflict_am_labor_ramp_unmodelled`. |
| PM Weekday Direct Labor | **Ramps**, per the session-count curve + 3-hour floor (§5) | Directly tied to session count via `docs/pm-staffing-roster.md`'s own hours-based costing formula. |
| PM Saturday Direct Labor (A$654.32/day) | **Fixed**, mathematically, regardless of ramp | Even at full 8-session steady state, hours/role/day (1.54hrs) is already below the 3-hour casual-minimum floor — the cost cannot fall below the floor amount at any session-count assumption. |
| Opening-time increment (A$44.50/day) | **Fixed from Month 1** | A per-trading-day operational cost, not booking-volume-dependent. |
| Receptionist/Relief Pool (A$339.00/day) | **Fixed from Month 1** | Receptionist is a committed Day-1 hire, not session-dependent. |
| Workers Comp (1.7%) | **Ramps automatically** | A percentage of Direct Labor + Opening Costs — moves with whatever that total is each month. |
| Superannuation (12%) | **Ramps automatically, per §4a** | Applied to the super-exclusive components only — see below. |

---

## 4a. Superannuation (added 2026-08-09, resolving `docs/VERIFICATION-TRACKER.md` item 46)

**Source/evidence:** `docs/financial-break-even-staff.md`'s "Award Wage Summary (Effective 1 July 2025)" table (lines 29-37) explicitly labels 6 of 7 roles' annual salary figures **"incl. super"** — Receptionist/Manager, Beauty therapist, Nail technician, Hairdresser, Massage therapist, PM Service Therapist — but does **not** apply that label to the Phlebotomist row ("A$43,068 (25hr/wk each)", no "incl. super" text). This is a real, disclosed asymmetry read directly off the source table, not an inference. Rate: 12% of Ordinary Time Earnings (`wages.yml#wage_superannuation_rate`, MODELLED, well-corroborated across 3 internal documents — `financial-break-even-staff.md`, `hr-framework.md`, `docs/01_conflicts_log.md`'s own consistency sweep).

**Treatment (rate × base × formula):**

| Component | Super treatment | Reasoning |
|---|---|---|
| AM Weekday — Treatment Staff (A$41,076.67/month, 8 staff) | **No super added** | Already included in the source's "incl. super" annual salary figures — adding it again would double-count. |
| AM Weekday — Phlebotomist (A$7,178.00/month, 2 staff) | **+12% added** = A$861.36/month | Source table does not label this role "incl. super" — the only role with this asymmetry. |
| AM Saturday Direct Labor (scenario-specific) | **+12% added** | Built from the raw hourly `casual_loaded` award rate, which the source table's own structure treats as exclusive of super (super only appears once annualised into a "incl. super" package figure). |
| PM Weekday Direct Labor | **+12% added** | Same reasoning — hourly-rate-based. |
| PM Saturday Direct Labor | **+12% added** | Same reasoning. |
| Opening-Time Increment, Receptionist/Relief Pool | **No super added — genuinely UNRESOLVED**, not guessed | Neither is a role-specific wage figure with a known super treatment; the Receptionist/Relief figure is itself only an approximate, bundled "~A$339.00/day" figure (see `conflict_direct_labor_reconciliation_gap`), not cleanly decomposable back to the Receptionist's own "incl. super" annual salary. See `conflict_superannuation_partial_coverage`. |

**Eligibility rule:** not stated anywhere in this repo (no minimum-earnings threshold, no age threshold mentioned) — the 12% rate is applied universally to every super-exclusive component above, not independently verified against current Australian SG eligibility rules.

**Monthly impact:** Table 1 steady state: A$3,619.92/month (Months 1-4: A$3,608.77/month, slightly lower since PM weekday labor is floor-constrained and lower pre-Month-5). Table 2 steady state: A$3,200.92/month (Months 1-4: A$3,189.78/month).

**Implementation:** `tools/cost_ramp_model.py`'s `SUPERANNUATION_RATE_PCT` constant and `compute_payroll()` — NOT a special case in `tools/master_financial_model.py`, which reads the already-super-inclusive `payroll_costs` from `cost_ramp.yml` automatically. Confirmed by `tests/test_master_financial_model.py`'s `SuperannuationRegressionTests.test_master_financial_model_has_no_special_case_superannuation_code`.

**Remaining uncertainty:** if the Receptionist's own wage component (embedded somewhere inside the bundled Opening-Time Increment / Receptionist-Relief figure) does NOT already include super via that bundling, this file's superannuation total is a modest underestimate — disclosed, not resolved (`conflict_superannuation_partial_coverage`).

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

**Figures below RECALCULATED 2026-08-09 to include superannuation (§4a, `docs/VERIFICATION-TRACKER.md` item 46, resolved). Was Payroll A$80,939.77 (M1-4) / A$81,034.18 (M5+) before super was added.**

| Month | Fixed | Variable | Payroll (incl. super) | Total Operating Costs |
|---|---|---|---|---|
| M1 | A$12,480.00 | A$600.00 | A$84,548.54 | A$97,628.54 |
| M2 | A$12,480.00 | A$800.00 | A$84,548.54 | A$97,828.54 |
| M3 | A$12,480.00 | A$1,000.00 | A$84,548.54 | A$98,028.54 |
| M4 | A$12,480.00 | A$1,200.00 | A$84,548.54 | A$98,228.54 |
| M5+ | A$12,480.00 | A$1,500.00 | A$84,654.10 | **A$98,634.10** |

**Reconciliation, disclosed not hidden:** `docs/CURRENT-STATE.md` §5's own stated Table 1 Total Costs is A$94,763.41 (no superannuation — never included in this repo's history). This file's Month 5+ Total Operating Costs (A$98,634.10) differs by A$3,870.69/month (4.1%) — A$250.77/month of that is the pre-existing, disclosed Direct Labor + Opening Costs reconciliation gap (§4's "Receptionist/Relief" figure taken at face value, not back-solved — see `conflict_direct_labor_reconciliation_gap`); the remaining A$3,619.92/month is the newly-included superannuation (§4a).

---

## 9. Table 2 Results (12 clients/day)

**Figures below RECALCULATED 2026-08-09 to include superannuation (§4a). Was Payroll A$77,388.82 (M1-4) / A$77,483.24 (M5+) before super was added.**

| Month | Fixed | Variable | Payroll (incl. super) | Total Operating Costs |
|---|---|---|---|---|
| M1 | A$12,480.00 | A$600.00 | A$80,578.60 | A$93,658.60 |
| M2 | A$12,480.00 | A$800.00 | A$80,578.60 | A$93,858.60 |
| M3 | A$12,480.00 | A$1,000.00 | A$80,578.60 | A$94,058.60 |
| M4 | A$12,480.00 | A$1,200.00 | A$80,578.60 | A$94,258.60 |
| M5+ | A$12,480.00 | A$1,500.00 | A$80,684.16 | **A$94,664.16** |

A$3,451.69/month gap against `docs/CURRENT-STATE.md`'s own stated Table 2 Total Costs (A$91,212.47) — A$250.77 pre-existing reconciliation gap + A$3,200.92 newly-included superannuation, same composition as Table 1. Also carries `docs/VERIFICATION-TRACKER.md` item 1o's own open question (whether the A$44.50/day opening increment should apply to Table 2's 08:00 start) — included unchanged, not independently resolved.

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
7. **New 2026-08-09:** whether superannuation should also apply to the Opening-Time Increment and Receptionist/Relief Pool components — genuinely unresolved, since neither is a role-specific wage figure with a known super treatment (`conflict_superannuation_partial_coverage`). If the Receptionist's own wage is not already super-inclusive via that bundling, this file's superannuation total is a modest underestimate.
8. **New 2026-08-09:** the eligibility rule for superannuation (any minimum-earnings threshold) is not stated anywhere in this repo — applied universally, not independently verified against current Australian SG eligibility rules.

---

## 11. Conflicts

Five declared in `data/canonical/cost_ramp.yml`'s `conflicts` list: `conflict_am_labor_ramp_unmodelled`, `conflict_direct_labor_reconciliation_gap`, `conflict_table2_opening_increment_unresolved`, `conflict_variable_vs_fixed_classification_carried_forward`, and (added 2026-08-09) `conflict_superannuation_partial_coverage`. Full detail in each record, not repeated here.

---

## 12. Limitations

This is a cost-side data-model component, not a cash-flow or funding-requirement tool. It does not know when the venture opens, does not sequence startup capital deployment, and — critically — startup and capex costs are structurally excluded (§13), not merely flagged, since `tools/cost_ramp_model.py` never reads `startup_costs.yml` or `capex.yml` at all (confirmed by `tests/test_cost_ramp.py`'s `NoCapexLeakageTests`).

---

## 13. Startup/Capex Exclusion — Confirmed by Design, Not Just by Convention

`tools/cost_ramp_model.py` does not import, reference, or read `data/canonical/startup_costs.yml` or `data/canonical/capex.yml` anywhere in its source code — a structural guarantee, not a discipline that could be silently violated by a future edit. `opex.yml` records classified `STARTUP` (e.g. `opex_accountant_initial_brief`, `opex_food_safety_supervisor_cert`) carry `monthly_equivalent: null` by design in their own source records and are never referenced by this module — confirmed by `tests/test_cost_ramp.py`'s `NoStartupCostLeakageTests`.

---

## 14. Relationship to `revenue_ramp.yml`

Both files share the same Month 1-5+/scenario structure and month vocabulary (M1-M4, M5plus), enabling a future Net P&L calculation (`revenue_ramp.yml`'s `total_revenue` minus this file's `total_operating_costs`, per month per scenario) — explicitly NOT computed here, per the coordinator's financial-model boundary. The two files use genuinely different ramp curves for their respective PM components (revenue: blanket 43/64/79/93/100%; cost: session-count-based, floor-adjusted) — a disclosed, deliberate divergence, not an oversight, since PM revenue and PM labor cost are governed by different underlying mechanics (average price vs. hours-based casual engagement rules).
