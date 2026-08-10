# Funding Requirement Investigation

**Date:** 2026-08-09 | **Type:** bounded investigation, `docs/VERIFICATION-TRACKER.md` item 47. **Investigation-and-close-if-possible, NOT permission to redesign or expand the Master Financial Model.** Does not recalculate revenue/cost methodology, does not invent an opening cash balance or startup/capex payment timing, does not assume operating cash can fund startup costs, and does not choose a primary scenario.

---

## 1. Question

Can `docs/VERIFICATION-TRACKER.md` item 47 ("no opening funding requirement is established anywhere in this repo's canonical/model layer") be closed, bounded, or does it remain genuinely unresolved?

**Answer: OUTCOME 2 — BOUNDED.** A defensible lower/upper range is calculable entirely from already-canonical figures. A single exact figure is **not** established, because the underlying startup-cost reconciliation itself remains genuinely unresolved (`docs/architecture/STARTUP-COST-RECONCILIATION.md` — at least 6-9 distinct historical ranges, unchanged by this investigation).

---

## 2. Required Distinction — (A) / (B) / (C)

Per the coordinator's explicit instruction, three concepts were investigated separately:

- **(A) Pre-opening capital** — money needed before normal operations begin.
- **(B) Opening working-capital requirement** — cash to survive the ramp until cash-positive.
- **(C) Combined opening funding requirement (A+B)** — only if timing evidence legitimately permits combining them.

---

## 3. Evidence — Startup/Capex Timing

**`docs/grace-startup-plan.md`'s "FINANCIAL GATES" table** (dated 2026-06-05) is the only document anywhere in this repo that attaches a timeline to startup cash outlays:

| Gate | Trigger (Week) | Est. Cost |
|---|---|---|
| Legal and professional fees | Week 1 | A$3,000–6,000 |
| Lease deposit + first month | Week 10 | A$5,000–15,000 |
| Fit-out deposit (Stage 1) | Week 10 | A$50,000–80,000 |
| Fit-out completion (Stage 2) | Week 15 | A$50,000–100,000 |
| Equipment, FF&E, stock | Week 14–15 | A$30,000–60,000 |
| **Total pre-revenue capital** | | **A$140,000–260,000** |

The same document's own Phase 4 ("Week 19: Soft Launch", "Week 20: Full Launch — DAILY_MANAGERS registration triggered (first revenue event)") confirms every gate above occurs **before** the first revenue event. This is genuine, sourced, dated evidence that pre-opening capital is sequential to, not overlapping with, the Master Financial Model's Month 1-24 operating P&L.

**Limitation, disclosed not smoothed over:** this timing structure is only attached to the **stale** 2026-06-05 dollar figures (A$140,000-260,000 total) — `data/canonical/startup_costs.yml` already flags this whole table as superseded-by-inference (predates the client-volume, fixture-count, and construction-type rebases). No document re-derives this week-by-week schedule against the current, larger fit-out/equipment figures. **Classification: TIMING PARTIALLY VERIFIED** for pre-opening capital as a category — confirmed sequential to revenue, not confirmed against current dollar amounts.

**`data/canonical/capex.yml`** — checked directly, contains **no** payment-timing, deposit-schedule, or milestone field on any of its asset records. **Classification: TIMING UNKNOWN** for individual capex line items — retained as a cost requirement, no payment date manufactured.

**Working capital reserve** (`funding_working_capital_reserve`) — its own stated purpose ("funds Months 1-3 operating losses") is itself a timing statement: post-opening, not pre-opening. **Classification: TIMING VERIFIED (conceptually)**, but its dollar basis is stale (pre-2026-08-05-rebase Month 1-3 loss estimate, `docs/VERIFICATION-TRACKER.md` item 30).

**Landlord fit-out contribution** (`startup_landlord_fitout_contribution`) — **NOT APPLICABLE**. Already excluded from every headline total in this repo per Anthony's direct instruction; not reintroduced here.

**Already-declared conflicts checked, none re-litigated:** `conflict_lease_cost_overlap`, `conflict_fitout_staged_payments_vs_construction_total` (startup_costs.yml), `conflict_summary_budget_vs_section_totals`, `conflict_it_av_overlap` (capex.yml) — all remain UNRESOLVED, unchanged by this investigation.

---

## 4. (A) Pre-Opening Capital

**Range: A$272,390 – A$467,180** (universal, not scenario-specific — no canonical startup-cost figure varies by Table 1 vs. Table 2, confirmed by direct check of every relevant record's `scenario_applicability` field).

Derivation — a clean decomposition of `docs/CURRENT-STATE.md` §7.4's own already-canonical component build, **not a new calculation**:

```
7.1 Equipment/Furniture/Signage                    A$61,190  – A$140,430
7.2 Construction (startup_construction_current_state_recompute)  A$191,200 – A$298,750
7.3 Legal/entity setup, lease bond (legal/lease-only, EXCLUDING working capital)  A$19,600 – A$27,600
    + embedded insurance                             A$400 – A$400
─────────────────────────────────────────────────────────────────
(A) Pre-Opening Capital                             A$272,390 – A$467,180
```

**Verification, not assumption:** `docs/CURRENT-STATE.md` §7.3's own stated total (A$105,000-138,000) was independently re-summed from its three components (legal/lease A$19,600-27,600 + working capital reserve A$85,000-110,000 + insurance A$400-400 = A$105,000-138,000 exactly) — confirming this decomposition is arithmetically exact, not approximate.

---

## 5. (B) Opening Working-Capital Requirement

**Two methods, neither chosen as correct**, per the coordinator's explicit "don't just add every historical range to the operating cash trough" instruction:

| Method | Range | Basis |
|---|---|---|
| Historical Reserve (existing canonical figure) | **A$85,000 – A$110,000** | `funding_working_capital_reserve` — a pre-2026-08-05-rebase Month 1-3 loss estimate, itself flagged stale (item 30). Not recalculated here. |
| Current Operating-Cash-Trough Cross-Check | Table 1: **A$30,885.75**; Table 2: **A$66,335.12** | This model's own, already-computed, current (post-superannuation) 24-month cash flow trough — scenario-specific, unlike the historical reserve. Shown as an alternative data point only. |

**Both scenarios' current trough figures are lower than the historical reserve range.** This investigation does **not** conclude the historical reserve is oversized — the two are built on genuinely different bases (a flat pre-rebase 3-month estimate vs. this model's own ramp-aware 24-month calculation) and are not directly comparable without further reconciliation work outside this phase's scope.

---

## 6. (C) Combined Opening Funding Requirement

**Timing evidence legitimately permits combining (A) and (B)** — §3 confirmed pre-opening capital occurs before revenue, and working capital by definition funds the post-opening ramp period; these are sequential, non-overlapping cash needs.

**Primary method (A) + historical Working Capital Reserve:**

**Range: A$357,390 – A$577,180** (both scenarios identically — no scenario-specific startup-cost data exists).

This is an **exact match** to `data/canonical/startup_costs.yml#total_current_state_component_sum` — confirming the decomposition above is consistent with, not a new departure from, this repo's own existing figures.

**Alternative cross-check method (A) + current operating-cash-trough** (illustrative only, not chosen as more correct):

| Scenario | Range |
|---|---|
| Table 1 | A$303,275.75 – A$498,065.75 |
| Table 2 | A$338,725.12 – A$533,515.12 |

**What was deliberately NOT done:** the operating cash trough was **not** added on top of the working capital reserve in the primary combined figure — both represent the same underlying "survive the ramp" concept, computed by two different methods. Summing them would double-count.

---

## 7. Relationship to Anthony's Own Adopted Total

`docs/CURRENT-STATE.md` §7.4's adopted, reconciled total (**A$292,335-594,900**, `total_current_state_adopted`) is close to but **not** identical to this investigation's primary combined range (A$357,390-577,180) — `CURRENT-STATE.md` itself already discloses this gap ("a few percent gap on both ends... reconciliation choices... not fully visible in this repo"). The adopted total's own internal A/B split is not independently traceable, so it could not be used as this investigation's basis — the cleanly-decomposable component-sum figure was used instead. **Both figures remain valid and disclosed side by side; neither is superseded by this investigation.**

---

## 8. Every Assumption Used

1. `docs/CURRENT-STATE.md` §7.1/§7.2/§7.3's own component figures are current and correctly attributed (already-canonical, not re-verified from primary sources this phase).
2. Pre-opening capital does not vary by Table 1/Table 2 (confirmed by checking `scenario_applicability` fields, not assumed).
3. `docs/grace-startup-plan.md`'s WEEK-based sequencing (pre-opening before revenue) remains structurally valid even though its dollar figures are stale — a timing-structure assumption, disclosed as such.
4. The working capital reserve and operating cash trough represent the same underlying concept (and should not be summed together) — a modelling judgment, disclosed, not proven by an explicit repo statement equating the two.

## 9. Every Assumption Deliberately NOT Made

1. **No opening cash balance invented** — remains `null`/PLACEHOLDER, unchanged.
2. **No startup/capex payment timing invented** beyond `docs/grace-startup-plan.md`'s own stale table — `capex.yml` items remain TIMING UNKNOWN, no date manufactured.
3. **Operating cash is not assumed able to fund startup costs** — pre-opening capital and working capital are kept structurally external to the operating P&L/cash flow.
4. **No financing, debt, or equity assumption used** — consistent with, not extending, this venture's existing self-funded (Anthony + Imara joint savings) status.
5. **Neither Table 1 nor Table 2 chosen as primary.**
6. **The 6-9-range startup-cost reconciliation problem was not resolved** — only re-partitioned into the requested A/B/C structure using the one already-canonical figure that cleanly decomposes.

---

## 10. New Conflicts

None new. `data/models/master_financial_model.yml#conflict_funding_requirement_not_established` was **updated** (not newly created) to reflect the bounded outcome — its underlying cause (the unresolved startup-cost reconciliation) is unchanged.

---

## 11. What This Investigation Does Not Do

It does not choose a single exact funding requirement. It does not resolve the startup-cost reconciliation's 6-9 competing ranges. It does not obtain real quotes, engage an accountant/quantity surveyor, or confirm a venue. It does not build Excel, PDF, or investor-facing material. It does not alter the canonical revenue or cost methodology, the Master Financial Model's P&L/cash-flow calculations, or any existing unresolved tracker item other than 47.

---

## 12. Update 2026-08-10 — Updated Planning Case Added, Previous Range Unchanged

Following the Founder Risk Acceptance Review (`docs/architecture/MVP-OPENING-DECISION-REVIEW.md`), Anthony approved a Revised Recommended Opening Strategy (A$251,198, Pre-Opening Capital scope) "in principle" as the current planning assumption — explicitly not a locked final cost. `data/models/master_financial_model.yml#funding_requirement_investigation` now carries a new `updated_planning_case_2026_08_10` section alongside (not replacing) `combined_funding_requirement_bounded.primary_method` above:

| | Range low | Range high |
|---|---|---|
| Previous bounded range (§6 above, unchanged) | A$357,390 | A$577,180 |
| Updated planning case (new, A$251,198 pre-opening capital + the same, untouched A$85,000–110,000 working capital reserve) | A$336,198 | A$361,198 |

Both figures are retained side by side — the previous range remains this file's own primary, wider bounded range; the updated case is Anthony's specific, itemised, in-principle-approved figure. Neither the working capital reserve nor the Master Financial Model's own operating-cash-trough figures were recalculated or reduced for this update — see `data/canonical/startup_costs.yml#adopted_planning_scenarios` for full component traceability, and `docs/VERIFICATION-TRACKER.md` item 49 (venue validation required before this could be treated as final).
