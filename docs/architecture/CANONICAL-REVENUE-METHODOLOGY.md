# Canonical Revenue Methodology

**Adopted:** 2026-08-09, per Anthony's direct decision. **Status:** the days-based first-principles formula below is now the canonical revenue-calculation methodology for GTT Center Perth going forward. **Not a Master Financial Model** — this document defines and reproduces revenue only. No P&L, cash-flow forecast, balance sheet, Excel, PDF, or chart is built here.

---

## 1. Purpose

`docs/architecture/REVENUE-RECONCILIATION-INVESTIGATION.md` traced the venture's inherited headline revenue figures (A$157,792.16/month Table 1, A$118,297.16/month Table 2) back through this repo's git history to an original historical 10-client, ancillary-included baseline (A$113,712.16) whose exact calculation method is not preserved anywhere in this repo's saved working, and confirmed no tested weekly-scaling convention reproduces it exactly. Anthony's decision: stop treating that untraceable inheritance as authoritative, and adopt instead the one revenue methodology that **is** fully reproducible from this repo's own canonical data — the days-based first-principles formula already used, and endorsed, in `docs/profit-loss-tables.md`'s own 2026-08-07 nine-step re-verification of Table 1. This document defines that methodology formally, states its exact inputs and formula, and calculates the resulting canonical figures for Table 1 and Table 2.

---

## 2. Why the Inherited A$113,712.16 Baseline Isn't Authoritative

Summarised from `docs/architecture/REVENUE-RECONCILIATION-INVESTIGATION.md` (full detail there, not repeated in full here):

- The A$113,712.16 figure (historical 10-client, ancillary-included Monthly Total Revenue) is the earliest point in this repo's git history where the venture's headline monthly revenue appears.
- Every subsequent revision (ancillary exclusion, 10→12→18 client volume changes, the 2026-08-05 Table 1/Table 2 rebase) is built from it by clean, exact, fully-reproducible additive deltas — verified to the cent.
- The original A$113,712.16 figure itself is **not** reproducible from any weekly-scaling convention tested (×4.33, ×4.345, ×52/12), nor from the days-based formula this document adopts, nor from any other candidate mechanism tested.
- This repo's own Appendix (`docs/profit-loss-tables.md`) already disclosed an unreconciled discrepancy against this same figure at the moment it was first touched in this repo (commit `e94a0d6`, 2026-07-30) — this is a pre-existing, previously-flagged gap, not a new problem.
- Because the figure's origin is untraceable, it cannot be verified, reproduced, or audited going forward — the opposite of what a canonical figure needs to be.

**This document does not claim the historical figure was wrong.** It may reflect real information (e.g. slightly different historical inputs) that was never fully saved. The decision to move on from it is a governance choice, not a claim that A$113,712.16 was an error.

---

## 3. Canonical Inputs

All inputs below trace to an existing canonical-data id. No new assumption was invented — where a needed input did not already have its own canonical id, it was given one this phase because it is already a consistently-used repo-wide convention (see individual notes), not because a new number was decided.

| Input | Canonical id | File | Value | Status |
|---|---|---|---|---|
| Table 1 client volume | `scenario_table_1.client_volume` | `data/canonical/scenarios.yml` | 18 clients/day | VERIFIED |
| Table 2 client volume | `scenario_table_2.client_volume` | `data/canonical/scenarios.yml` | 12 clients/day | VERIFIED |
| AM revenue-calculation price | `am_price_used_for_revenue` | `data/canonical/pricing.yml` | A$250.00 (Package 1, conservative convention) | DECIDED |
| PM average service price | `pm_alacarte_average` | `data/canonical/pricing.yml` | A$95.00 | MODELLED |
| PM weekday session volume | `pm_steady_state_capacity` | `data/canonical/client_assumptions.yml` | 16 sessions/day | MODELLED |
| PM Saturday session volume | `rev_pm_saturday_sessions` | `data/canonical/revenue_assumptions.yml` | 8 sessions/day | MODELLED |
| Trading weekdays/month | `operating_days_per_month_weekday` | `data/canonical/client_assumptions.yml` | 22 days | MODELLED (new record this phase, see §13) |
| Trading Saturdays/month | `operating_saturdays_per_month` | `data/canonical/client_assumptions.yml` | 4.33 days | MODELLED (new record this phase, see §13) |
| Ancillary revenue (current baseline) | `rev_ancillary_excluded_from_baseline` | `data/canonical/revenue_assumptions.yml` | A$0.00/month | VERIFIED |
| Saturday client-volume assumption | `saturday_volume_assumption` | `data/canonical/client_assumptions.yml` | Saturday reuses the same client count as weekday | MODELLED (inference, not directly restated in CURRENT-STATE.md's table structure) |
| PM pre-booking discount (not applied) | `rev_discount_pm_prebooking` | `data/canonical/revenue_assumptions.yml` | 10% (unapplied — see §11) | VERIFIED |

**Inputs deliberately not used, and why:** `service_mix_am_package_split` (PLACEHOLDER, no real data — the formula uses the DECIDED `am_price_used_for_revenue` convention instead, not a real mix); the 3 proposed PM packages (`pm_package_duo/refresh/glow`, all PLACEHOLDER — not incorporated, per `rev_pm_service_mix_current`'s own explicit statement that package uptake isn't modelled yet); the 3 ancillary historical aggregates (`rev_ancillary_*_historical`, all excluded from the baseline per Anthony's 2026-07-30 instruction, represented by `rev_ancillary_excluded_from_baseline` = A$0 instead).

---

## 4. Formula

```
Monthly Revenue =
    (client_volume x am_price_used_for_revenue x operating_days_per_month_weekday)      [AM Weekday]
  + (client_volume x am_price_used_for_revenue x operating_saturdays_per_month)         [AM Saturday]
  + (pm_steady_state_capacity x pm_alacarte_average x operating_days_per_month_weekday) [PM Weekday]
  + (rev_pm_saturday_sessions x pm_alacarte_average x operating_saturdays_per_month)    [PM Saturday]
  + rev_ancillary_excluded_from_baseline                                                [Ancillary, currently A$0]
```

No discount is netted out (see §11). No rounding is applied at any intermediate step (see §12).

---

## 5. Calculation Sequence

1. Look up `client_volume` for the scenario being calculated (`scenario_table_1` or `scenario_table_2`).
2. Compute AM Weekday revenue = `client_volume × am_price_used_for_revenue × operating_days_per_month_weekday`.
3. Compute AM Saturday revenue = `client_volume × am_price_used_for_revenue × operating_saturdays_per_month` (using `saturday_volume_assumption`'s inference that Saturday client volume equals weekday volume).
4. Compute PM Weekday revenue = `pm_steady_state_capacity × pm_alacarte_average × operating_days_per_month_weekday` (identical for every scenario — PM volume is not AM-client-volume-dependent).
5. Compute PM Saturday revenue = `rev_pm_saturday_sessions × pm_alacarte_average × operating_saturdays_per_month` (identical for every scenario).
6. Add `rev_ancillary_excluded_from_baseline` (currently A$0.00).
7. Sum all components = Total Monthly Revenue.
8. Optionally derive Daily (Weekday/Saturday), Weekly, Quarterly, Half-Yearly, and Yearly figures per §15's worked examples — Quarterly/Half-Yearly/Yearly use the same steady-state run-rate scaling convention (Monthly × 3/6/12) already established in `docs/CURRENT-STATE.md` §5.

---

## 6. Table 1 Calculation (18 clients/day)

| Component | Formula | Result |
|---|---|---|
| AM Weekday | 18 × A$250.00 × 22 | A$99,000.00 |
| AM Saturday | 18 × A$250.00 × 4.33 | A$19,485.00 |
| PM Weekday | 16 × A$95.00 × 22 | A$33,440.00 |
| PM Saturday | 8 × A$95.00 × 4.33 | A$3,290.80 |
| Ancillary | — | A$0.00 |
| **Total Monthly Revenue** | Sum | **A$155,215.80** |

Matches `data/canonical/revenue_assumptions.yml`'s `rev_reconstruction_table1_monthly` exactly.

---

## 7. Table 2 Calculation (12 clients/day)

| Component | Formula | Result |
|---|---|---|
| AM Weekday | 12 × A$250.00 × 22 | A$66,000.00 |
| AM Saturday | 12 × A$250.00 × 4.33 | A$12,990.00 |
| PM Weekday | 16 × A$95.00 × 22 | A$33,440.00 |
| PM Saturday | 8 × A$95.00 × 4.33 | A$3,290.80 |
| Ancillary | — | A$0.00 |
| **Total Monthly Revenue** | Sum | **A$115,720.80** |

Matches `data/canonical/revenue_assumptions.yml`'s `rev_reconstruction_table2_monthly` exactly.

---

## 8. Treatment of AM Revenue

AM revenue always uses `am_price_used_for_revenue` (A$250.00, Package 1) — a deliberate conservative modelling convention (DECIDED), not a claim about the real AM Package 1/Package 2 booking mix, which remains genuinely unknown (`service_mix_am_package_split`, PLACEHOLDER). If real booking-mix data becomes available, AM revenue under this methodology could be recalculated using an actual blended average instead — not done here, since no such data exists yet. Saturday AM volume is assumed equal to weekday AM volume (`saturday_volume_assumption`, an inference, not a directly-stated figure — see §16).

---

## 9. Treatment of PM Revenue

PM revenue uses `pm_alacarte_average` (A$95.00), an aggregate planning average across all PM a-la-carte services, not any single service's price — the 3 proposed PM packages (Duo/Refresh/Glow) are explicitly not incorporated (`rev_pm_service_mix_current`). PM session volume (16 weekday, 8 Saturday) is identical across every AM scenario — it is not driven by AM client volume, and this document's formula reflects that by using the same PM figures for both Table 1 and Table 2.

---

## 10. Treatment of Ancillary Revenue

Ancillary revenue (spray tan, retail, café) is included in the formula structurally (§4) but currently evaluates to A$0.00/month, per Anthony's 2026-07-30 instruction (`rev_ancillary_excluded_from_baseline`, VERIFIED) — "too much of a variable with no real basis yet." The 3 historical ancillary aggregates (`rev_ancillary_spraytan_historical` A$58,000/yr, `rev_ancillary_retail_historical` A$25,000/yr, `rev_ancillary_cafe_historical` A$15,000/yr) remain in the canonical data as historical planning figures, unchanged by this phase, but are not summed into this formula's output. If ancillary revenue is ever reintroduced, it would need its own bottom-up volume × per-item-price build (see `conflict_ancillary_aggregate_vs_itemised`, unresolved) before being added back into this formula — not done here.

---

## 11. Treatment of Discounts

The 10% PM pre-booking discount (`rev_discount_pm_prebooking`, VERIFIED as a real, sourced policy) is **not** netted out of PM revenue in this formula, matching how every revenue figure in this repo — historical and canonical alike — has always treated it. This is a disclosed, not silently ignored, omission: what share of the 16 weekday / 8 Saturday PM sessions are GTT-paired and pre-booked online (and therefore discount-eligible) is unknown (`docs/VERIFICATION-TRACKER.md` item 39, unresolved, reviewed this phase but not resolved — no new evidence surfaced to resolve it). If that share becomes known, PM revenue under this methodology should be reduced by 10% of the GTT-paired portion — an upper bound of roughly A$3,673/month at Table 1 if 100% of PM sessions were GTT-paired (not a finding that this is the real figure, an illustrative ceiling only).

---

## 12. Treatment of Rounding

No intermediate rounding is applied anywhere in this formula — every component (§6, §7) is computed to full precision and summed directly. `docs/architecture/REVENUE-RECONCILIATION-INVESTIGATION.md` §9 already tested this formula's own rounding behaviour against multiple alternative weeks-per-month conventions (4.33 vs. 4.345 vs. 52/12) and confirmed none of them closes the gap against the old inherited figure — this methodology retains 4.33 (the figure already used consistently throughout this repo's saved working, see `operating_saturdays_per_month`'s own notes) not because it was proven more mathematically precise than the alternatives, but because it is the figure this repo has consistently used.

---

## 13. Treatment of Operating Days

`operating_days_per_month_weekday` (22) and `operating_saturdays_per_month` (4.33) are new canonical records added this phase to `data/canonical/client_assumptions.yml`. **These are not new assumptions** — both figures are already used consistently, dozens of times, throughout this repo's existing saved working (`docs/CURRENT-STATE.md` §5, `docs/profit-loss-tables.md`'s Appendix and Downtime-Fill/Early-Release formulas, `docs/investor-memorandum.md`, `docs/booking-service-capacity-rule.md`) — this phase simply gives that pre-existing, repeatedly-applied convention its own canonical id for the first time, so this formula can reference it by id rather than restating the bare number inline (per this repo's no-duplicate-figures rule). No independent derivation of "why 22" (the literal 52 weeks/year × 5 weekdays ÷ 12 months = 21.67, not 22) is stated anywhere in this repo — it reads as a standard rounded planning convention, not re-derived here.

---

## 14. Treatment of Scenario Differences

Table 1 and Table 2 differ **only** in `client_volume` (18 vs. 12), which affects only the AM Weekday and AM Saturday components. PM Weekday, PM Saturday, and Ancillary components are identical between the two scenarios (§9), matching `docs/CURRENT-STATE.md` §7's own delta table, which states PM/ancillary are "unchanged" across the rebase. Neither scenario is marked primary by this methodology — consistent with `data/canonical/scenarios.yml`'s existing `is_primary: false` for both, pending Anthony's resolution of `docs/VERIFICATION-TRACKER.md` item 1m.

---

## 15. Worked Examples

**Table 1 (18 clients/day) — full breakdown:**

| Period | AM Weekday | AM Saturday | PM Weekday | PM Saturday | Total |
|---|---|---|---|---|---|
| Per weekday | A$4,500.00 | — | A$1,520.00 | — | A$6,020.00/weekday |
| Per Saturday | — | A$4,500.00 | — | A$760.00 | A$5,260.00/Saturday |
| Weekly (5 weekdays + 1 Saturday) | A$22,500.00 | A$4,500.00 | A$7,600.00 | A$760.00 | **A$35,360.00/week** |
| Monthly (22 weekdays + 4.33 Saturdays) | A$99,000.00 | A$19,485.00 | A$33,440.00 | A$3,290.80 | **A$155,215.80/month** |
| Quarterly | — | — | — | — | A$465,647.40 |
| Half-Yearly | — | — | — | — | A$931,294.80 |
| Yearly (steady-state run-rate) | — | — | — | — | A$1,862,589.60 |

**Table 2 (12 clients/day) — full breakdown:**

| Period | AM Weekday | AM Saturday | PM Weekday | PM Saturday | Total |
|---|---|---|---|---|---|
| Per weekday | A$3,000.00 | — | A$1,520.00 | — | A$4,520.00/weekday |
| Per Saturday | — | A$3,000.00 | — | A$760.00 | A$3,760.00/Saturday |
| Weekly (5 weekdays + 1 Saturday) | A$15,000.00 | A$3,000.00 | A$7,600.00 | A$760.00 | **A$26,360.00/week** |
| Monthly (22 weekdays + 4.33 Saturdays) | A$66,000.00 | A$12,990.00 | A$33,440.00 | A$3,290.80 | **A$115,720.80/month** |
| Quarterly | — | — | — | — | A$347,162.40 |
| Half-Yearly | — | — | — | — | A$694,324.80 |
| Yearly (steady-state run-rate) | — | — | — | — | A$1,388,649.60 |

**Important, disclosed non-equivalence:** the Weekly figure above (A$35,360.00 for Table 1) should **not** be multiplied by 4.33 to re-derive the Monthly figure — doing so gives A$153,108.80, not A$155,215.80, because Weekly uses "5 weekdays" while Monthly uses "22 weekdays" (5 × 4.33 = 21.65 weekdays, not 22 — the exact same day-count mismatch already identified as the historical gap's likely shape in `docs/architecture/REVENUE-RECONCILIATION-INVESTIGATION.md` §9). Monthly is calculated directly from the canonical 22/4.33 operating-day inputs (§4), not by scaling the Weekly figure — the Weekly figure is shown for intuition only, matching `docs/profit-loss-tables.md` §3's own existing warning about the same distinction for its historical tables.

---

## 16. Known Limitations

1. `operating_days_per_month_weekday` (22) and `operating_saturdays_per_month` (4.33) are repo-wide conventions, not independently re-derived first-principles figures — see §13.
2. `saturday_volume_assumption` (Saturday AM client volume = weekday AM client volume) is an inference (MODELLED), not a directly-stated figure in `docs/CURRENT-STATE.md`'s own scenario tables.
3. AM revenue uses a fixed Package 1 price convention, not the real (unknown) AM package mix.
4. PM revenue uses an aggregate average price, not itemised per-service revenue, and does not incorporate the 3 proposed PM packages.
5. The 10% PM pre-booking discount is not netted out (§11) — a known, disclosed potential overstatement.
6. Ancillary revenue is A$0 by policy, not because it has been proven to be zero in practice.
7. This methodology has not been extended to any ramp-up (Month 1-5+) figure — `docs/VERIFICATION-TRACKER.md` item 37 remains open and out of scope for this phase.
8. This is a revenue-only methodology — it says nothing about costs, payroll, or Net P&L.

---

## 17. Reconciliation Against Historical Figures

| Scenario | Canonical (this methodology) | Historical/inherited (`docs/CURRENT-STATE.md` §5) | Difference |
|---|---|---|---|
| Table 1 | A$155,215.80/month | A$157,792.16/month | **−A$2,576.36** (canonical is lower) |
| Table 2 | A$115,720.80/month | A$118,297.16/month | **−A$2,576.36** (canonical is lower) |

**No reconciliation was forced.** Per the explicit instruction for this phase, these figures do not need to equal the historical totals — the goal is a methodology that is traceable and reproducible from canonical inputs, not agreement with a number whose own origin cannot be verified (§2). The A$2,576.36 gap is the same one identified and traced in `docs/architecture/REVENUE-RECONCILIATION-INVESTIGATION.md` — its ultimate historical origin remains unresolved (`docs/VERIFICATION-TRACKER.md` item 36), but it no longer blocks this methodology from being treated as canonical going forward.

---

## 18. Status of the Methodology

**CANONICAL, adopted 2026-08-09, per Anthony's direct decision.** This methodology is now the reference calculation for future revenue modelling (any future P&L, cash-flow forecast, or financial model — none built by this document). The historical/inherited figures (A$157,792.16, A$118,297.16, and the untraceable A$113,712.16 origin) remain preserved in `data/canonical/revenue_assumptions.yml` (`rev_historical_table1_monthly_inherited`, `rev_historical_table2_monthly_inherited`, both `status: SUPERSEDED`) and in `docs/CURRENT-STATE.md`'s existing prose, for trace only — not deleted, not treated as current. Reproducibility of this methodology is enforced by `tests/test_revenue_methodology.py`, which computes both Table 1 and Table 2 revenue directly from the canonical YAML inputs listed in §3 and asserts the result matches this document's figures exactly.
