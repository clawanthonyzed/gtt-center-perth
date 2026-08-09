# Revenue Reconciliation Investigation — the A$2,576.36/month Gap

**Date:** 2026-08-09 | **Type:** Targeted investigation, NOT canonical-data migration. No financial model, Excel, PDF, or pricing decision produced by this document.

**Trigger:** Phase 6 (`docs/architecture/REVENUE-ASSUMPTION-AUDIT.md`) independently reconstructed monthly revenue from canonical inputs and found both Table 1 and Table 2 land exactly A$2,576.36 below `docs/CURRENT-STATE.md` §5's own stated totals. This document traces that gap back through the repo's own git history to find its origin, and separately investigates a second figure, A$63,028.75, that the coordinator had been treating as a revenue number.

---

## 1. Executive Finding

**The A$2,576.36/month gap was not introduced by the 2026-08-05 Table 1/Table 2 rebase, and it is not a rounding artifact of any 4.33-weeks-per-month scaling step currently used in this repo.** It is inherited, unchanged, from a single historical figure — the original historical 10-client, ancillary-included Monthly Total Revenue of **A$113,712.16** — that first appears in this repo's saved working with no exact reproducible formula behind it. Every revenue figure built since (the historical 10-client ancillary-excluded total, the 12-client total, the 18-client Table 1 total) was derived from that one figure by clean, exact, fully-reproducible arithmetic (flat ancillary subtraction, then additive client-volume deltas using the 22-weekday/4.33-Saturday convention) — meaning the *same* A$2,576.36 discrepancy against a "first-principles" days-based reconstruction propagates untouched through every subsequent model revision, which is exactly why it appears identical at every client-volume stage tested (10, 12, and 18 clients/day).

**A$63,028.75 was found — it is present, sourced, and traceable, but it is Net P&L (monthly profit after all costs), not revenue.** The coordinator's framing of it as "a revenue figure" does not match how it is used anywhere in the repo. This is documented in full in §7.

**Neither rounding nor the 10% PM pre-booking discount contributes to the A$2,576.36 gap** — both were tested directly against the actual figures and ruled out with evidence (§8, §9).

---

## 2. Known Revenue Figures

| Figure | Value | What it is | Source |
|---|---|---|---|
| Table 1 Total Revenue (stated) | A$157,792.16/month | 18-client/day, delta-built from the 12-client baseline | `docs/CURRENT-STATE.md` §5 |
| Table 2 Total Revenue (stated) | A$118,297.16/month | 12-client/day, identical to the old committed baseline | `docs/CURRENT-STATE.md` §5 |
| Table 1 Total Revenue (canonical reconstruction) | A$155,215.80/month | First-principles: 18×250×22 + 18×250×4.33 + 16×95×22 + 8×95×4.33 | `docs/profit-loss-tables.md` PRIMARY REBASED MODEL walkthrough; `data/canonical/revenue_assumptions.yml` |
| Table 2 Total Revenue (canonical reconstruction) | A$115,720.80/month | Same formula at 12 clients/day | This investigation, §6; `data/canonical/revenue_assumptions.yml` |
| historical 10-client Total Revenue, ancillary included (historical) | A$113,712.16/month | The original figure this entire chain traces back to | `docs/profit-loss-tables.md`, pre-2026-07-30 version (git commit before `e94a0d6`) |
| historical 10-client Total Revenue, ancillary excluded (historical) | A$105,132.16/month | = A$113,712.16 − A$8,580.00 flat ancillary subtraction | `docs/profit-loss-tables.md` §4, commit `e94a0d6` |
| A$63,028.75 | — Net P&L, not revenue — | Table 1's Monthly Net P&L (Total Revenue A$157,792.16 minus Total Costs A$94,763.41) | `docs/CURRENT-STATE.md` §5; `docs/profit-loss-tables.md` |

---

## 3. Canonical Reconstruction (Recap of Phase 6, Re-verified This Session)

Formula used (matches `docs/profit-loss-tables.md`'s own 9-step walkthrough for Table 1, extended to Table 2):

```
AM Weekday = clients/day × A$250 × 22 trading days
AM Saturday = clients/day × A$250 × 4.33 Saturdays/month
PM Weekday = 16 sessions × A$95 × 22 trading days   (unchanged across all scenarios)
PM Saturday = 8 sessions × A$95 × 4.33 Saturdays/month  (unchanged across all scenarios)
```

Re-verified by direct calculation this session (not just re-quoted from Phase 6):

- Table 1 (18 clients): 99,000.00 + 19,485.00 + 33,440.00 + 3,290.80 = **155,215.80**
- Table 2 (12 clients): 66,000.00 + 12,990.00 + 33,440.00 + 3,290.80 = **115,720.80**

Both match Phase 6's figures exactly — no drift.

---

## 4. `CURRENT-STATE.md`'s Own Calculation (Delta-Built, Not First-Principles)

`docs/CURRENT-STATE.md` §5 does **not** build Table 1/Table 2 revenue from the formula in §3 above. It states the method explicitly: *"delta-reconciliation build from the validated 12-client baseline in `profit-loss-tables.md`, same methodology as every prior model-change round."* Traced and re-verified this session:

| Step | Calculation | Result | Matches stated delta? |
|---|---|---|---|
| 12→18 client delta (Table 2 → Table 1) | 6 extra clients × A$250 × 22 days + 6 × A$250 × 4.33 Saturdays | A$33,000.00 + A$6,495.00 = **A$39,495.00** | Yes — exact match to `CURRENT-STATE.md`'s stated "+A$39,495.00" |
| 10→12 client delta (historical 10-client → 12-client, 2026-07-30) | 2 extra clients × A$250 × 22 days + 2 × A$250 × 4.33 Saturdays | A$11,000.00 + A$2,165.00 = **A$13,165.00** | Yes — exact match to `profit-loss-tables.md`'s implied delta (A$118,297.16 − A$105,132.16 = A$13,165.00 exactly) |
| Ancillary exclusion (2026-07-30) | A$113,712.16 − A$8,580.00 (flat annual ancillary ÷ 12, subtracted as a lump sum) | **A$105,132.16** | Yes — exact match, confirmed directly in the `e94a0d6` commit diff |

**Every delta step above is clean, exact, and fully reproducible from its own stated formula — zero rounding drift at any step.** This directly rules out the client-volume rebase, the ancillary exclusion, and the Table 1/Table 2 split itself as sources of the A$2,576.36 gap. The gap must therefore already exist in the one figure that is *not* built from any of these deltas: the original A$113,712.16 base.

---

## 5. The A$2,576.36 Discrepancy — Where It Actually Sits

Because the delta chain in §4 is exact, the gap between the canonical first-principles reconstruction (§3) and the stated totals (§2) is identical at every stage — historical 10-client, 12-client, and 18-client — because it is **the same, single, unexplained gap present in the original A$113,712.16 figure, simply carried forward by addition ever since.**

Confirmed directly:
```
Reconstructed (historical 10-client, ancillary excluded, days-based) = A$102,555.80
Stated (historical 10-client, ancillary excluded)                     = A$105,132.16
Gap                                                          = A$2,576.36  ← identical to Table 1/Table 2's gap
```

This is the earliest point in the repo's saved working where the gap can be isolated with the current days-based formula. It predates the 2026-08-05 rebase by more than a month and predates the 12-client model itself.

---

## 6. Exact Calculation Trace — Full Backward Chain

```
Table 1 stated (18-client)          A$157,792.16
   = Table 2 stated (12-client)      A$118,297.16
   + clean delta (6 clients)        + A$ 39,495.00   [exact, verified §4]

Table 2 stated (12-client)          A$118,297.16
   = historical 10-client ancillary-excluded    A$105,132.16
   + clean delta (2 clients)        + A$ 13,165.00   [exact, verified §4]

historical 10-client ancillary-excluded        A$105,132.16
   = historical 10-client WITH ancillary        A$113,712.16
   − flat ancillary subtraction     − A$  8,580.00   [exact, verified §4, commit e94a0d6]

historical 10-client WITH ancillary (A$113,712.16) is the ORIGIN — no exact
formula in this repo's current or historical saved working reproduces
this number. See the candidate-testing table in §9.
```

**The gap is not "in" the scaling from 10→12→18 clients. It is baked into the starting figure itself**, and every subsequent, otherwise-clean model revision has correctly carried it forward without ever re-deriving the base from scratch.

---

## 7. A$63,028.75 Investigation

**Classification: (A) present and traceable — but it is Net P&L, not revenue.**

Found in `docs/CURRENT-STATE.md` §5 ("Net P&L — NEW PRIMARY COMMITTED STEADY-STATE FIGURE: +A$63,028.75/month") and `docs/profit-loss-tables.md`'s Changelog and PRIMARY REBASED MODEL section, both dated 2026-08-05, independently re-verified 2026-08-07 ("full 9-step first-principles walkthrough... Result: A$63,028.75/month confirmed, exact match, no rounding drift").

It is derived as: **Total Revenue (A$157,792.16) − Total Costs (A$94,763.41, comprising Direct Labor + Opening Costs A$79,433.05, Workers Comp A$1,350.36, Non-Wage Overhead A$13,980.00) = A$63,028.75.**

Full search performed for A$63,028.75 as a revenue figure specifically: not found anywhere in this repo used as a revenue line. It appears exclusively as the whole-venture Monthly Net P&L for Table 1, referenced repeatedly (e.g. `docs/CURRENT-STATE.md` §7's delta table: "Whole-venture Monthly Net P&L: +A$63,028.75/month") and cross-referenced in `investor-memorandum.md`. No rounded/comma variant, no annualised variant, and no alternative-derivation match was found anywhere else in the repo.

**Conclusion: this is not a case of a missing or superseded figure — it is a labelling mismatch in how the number has been described outside this repo.** A$63,028.75 is the venture's headline monthly *profit* figure for the primary committed model (Table 1), not a revenue total. The actual Table 1 revenue figure is A$157,792.16 (stated) / A$155,215.80 (canonical reconstruction) — a materially different number, ~2.5x larger than A$63,028.75. Confusing the two in any investor or funding conversation would misstate the venture's revenue by more than half. See §11 tracker item added for this.

---

## 8. PM Discount Investigation (10%)

**Where defined:** `docs/services-pricing-locked.md`, Model Confirmation section: *"Discount policy: 10% online pre-booking discount on afternoon/standalone services booked at the same time as a GTT reservation. No discount on in-center upsells (add-ons, cafe, retail, spray tan) — full price applies on the day."* Restated identically at the foot of the PM pricing table (line 172).

**Scope:** applies only to PM/afternoon standalone services booked online *at the same time as* a GTT reservation (i.e., GTT-paired advance bookings). Explicitly does **not** apply to same-day walk-ins, in-center upsells, add-ons, cafe, retail, or spray tan.

**Mandatory or optional:** stated as a standing policy ("Discount policy: ..."), not framed as optional per-booking — but no document states what share of the 16 weekday / 8 Saturday PM sessions are actually GTT-paired and pre-booked online vs. standalone/same-day (this exact gap is already tracked as tracker item 39, added in Phase 6).

**Does any existing revenue calculation apply it?** No. Checked every PM revenue line across `docs/profit-loss-tables.md` (Appendix: "16 sessions × A$95 average individual-service price"), `docs/CURRENT-STATE.md` §5, and `data/canonical/revenue_assumptions.yml` — all use the full undiscounted A$95/session average with no 90%-scaling applied anywhere.

**Does applying it change Table 1 or Table 2?** Not currently — since it isn't applied anywhere, no live figure is affected. If applied to 100% of PM sessions (an upper-bound, not-evidenced assumption) it would reduce PM revenue by 10%, i.e. roughly A$3,673/month at Table 1 (10% of A$36,730.80 combined weekday+Saturday PM revenue) — a real, separate potential overstatement, but this is a hypothetical upper bound only, not a finding that the discount is currently baked in anywhere.

**Is it relevant to the A$2,576.36 gap?** No. PM revenue (A$1,520.00/day weekday, A$760.00/day Saturday, based on 16×95 and 8×95 respectively) is **identical and unchanged across every stage of the historical chain traced in §6** — the historical 10-client, 12-client, and 18-client models all use the same PM figures. Since the A$2,576.36 gap is already fully explained as being embedded in the original historical 10-client-with-ancillary AM+PM+Ancillary total (§5-6), and PM's own component figures reconcile exactly to their stated 16×95/8×95 formulas with no unexplained residual, the PM discount cannot be a contributing mechanism to this specific gap — ruled out by direct arithmetic, not by assumption.

---

## 9. Rounding Investigation

Tested every plausible weekly-to-monthly scaling convention against both the historical historical 10-client-with-ancillary total (A$113,712.16) and the current 12-client-ancillary-excluded total (A$118,297.16), computed to full floating-point precision (no intermediate rounding applied by this investigation):

| Candidate mechanism | Result (historical 10-client, w/ ancillary) | Gap vs A$113,712.16 |
|---|---|---|
| Weekly total × 4.33 | A$110,663.98 | A$3,048.18 |
| Weekly total × 4.345 | A$111,047.34 | A$2,664.82 |
| Weekly total × (52/12 = 4.3333) | A$110,749.17 | A$2,962.99 |
| Weekly total × 52 ÷ 12 | A$110,749.17 | A$2,962.99 |
| Days-based, ancillary applied to 22 weekdays only | A$112,224.80 | A$1,487.36 |
| Days-based, ancillary applied to all 26.33 operating days | A$114,127.84 | −A$415.68 |
| Average-day × 365.25/12 (blended across all 6 trading days) | A$129,651.07 | −A$15,938.91 |

| Candidate mechanism | Result (12-client, ancillary excluded) | Gap vs A$118,297.16 |
|---|---|---|
| Weekly total × 4.33 | A$114,138.80 | A$4,158.36 |
| Weekly total × 4.345 | A$114,534.20 | A$3,762.96 |
| **Days-based (22 weekdays + 4.33 Saturdays)** | **A$115,720.80** | **A$2,576.36** |

**Finding: no tested weekly-scaling variant (4.33, 4.345, or 52/12 weeks/month) reproduces either stated total exactly, or reproduces a gap of exactly A$2,576.36 against the historical 10-client base.** The only mechanism that produces the precise, repeatable A$2,576.36 figure is the current days-based formula compared against the *already-fixed* stated totals — which is exactly what Phase 6 and this investigation both did. **Rounding at the delta-step level contributes zero to the gap** (§4's deltas are exact to the cent). **Rounding cannot be ruled in or out as a contributor to the original A$113,712.16 figure specifically**, because that figure's exact original build method is not preserved anywhere in this repo's saved working — the same "not preserved as a saved worksheet" caveat pattern `profit-loss-tables.md`'s own Appendix already applies to its AM Direct Labor figures.

---

## 10. Tested Hypotheses

| # | Hypothesis | Tested against | Result |
|---|---|---|---|
| 1 | Weekly×4.33 monthly scaling produces the gap | historical 10-client and 12-client bases | Does not reproduce either stated total or the exact A$2,576.36 gap — REJECTED |
| 2 | Weekly×4.345 or 52/12 (more precise weeks/month) closes the gap | Same | Neither closes it exactly — REJECTED |
| 3 | Ancillary applied over a different day-count (22 vs 26.33) explains the pre-exclusion figure | historical 10-client with ancillary | Neither variant reproduces A$113,712.16 exactly — REJECTED |
| 4 | The gap is introduced by the 2026-08-05 Table 1/Table 2 rebase | Delta math §4 | Rebase delta (A$39,495.00) is exact — REJECTED, rebase is clean |
| 5 | The gap is introduced by the 2026-07-30 10→12 client volume correction | Delta math §4 | Delta (A$13,165.00) is exact — REJECTED |
| 6 | The gap is introduced by the ancillary-exclusion subtraction | Commit `e94a0d6` diff | Subtraction (A$8,580.00 flat) is exact — REJECTED |
| 7 | The 10% PM discount, if applied, explains the gap | PM component figures across all 3 model stages | PM figures are identical and internally consistent at every stage, no unexplained residual — REJECTED |
| 8 | The gap originates in the original historical 10-client-with-ancillary total (A$113,712.16), predating any formula preserved in this repo | Git history back to earliest commit containing this figure | **CONFIRMED as the origin point** — no formula reproduces A$113,712.16 exactly; the repo's own Appendix already flagged an unreconciled discrepancy (~A$3,048-3,964) against its own weekly-scaled check at the exact commit this figure was last touched (`e94a0d6`), predating this investigation entirely |

**`HYPOTHESIS — NOT SOURCE VERIFIED`:** the most plausible explanation for A$113,712.16's own origin, based on the shape of the numbers but not confirmed by any surviving worksheet, is that it was built in an early planning session using a weekly-scaling approach with inputs (session counts, per-session or per-package pricing, or the exact ancillary split) that differ slightly from the values currently documented — i.e., the underlying methodology may be sound but was applied to inputs that have since been revised (package renumbering 2026-07-20, PM session count changes, ancillary component changes) without the monthly total being fully re-derived from scratch each time, only delta-adjusted. This is offered as a plausible historical explanation only, not presented as fact, and does not change the conclusion that the exact mechanism cannot currently be reproduced from this repo's saved working.

---

## 11. Confirmed Facts

1. The A$2,576.36 gap is real, exact, reproducible, and identical across Table 1 and Table 2 — independently confirmed a second time this session via direct backward calculation through git history, not just re-quoted from Phase 6.
2. The gap is not introduced by the 2026-08-05 rebase, the 2026-07-30 client-volume correction, or the 2026-07-30 ancillary exclusion — all three are exact, clean, fully-reproducible arithmetic steps.
3. The gap already existed in the original historical 10-client, ancillary-included Monthly Total Revenue (A$113,712.16), the earliest point in this repo's history where it can be isolated.
4. This repo's own Appendix (`profit-loss-tables.md`) already disclosed an unreconciled discrepancy against this same figure at the moment it was created (2026-07-30 commit `e94a0d6`), before any of this investigation's work — this is not a newly-introduced problem, it is a genuinely pre-existing, previously-disclosed-but-not-traced one.
5. No tested rounding or weeks-per-month convention (4.33, 4.345, 52/12) reproduces the historical base figure exactly.
6. The 10% PM pre-booking discount is not applied anywhere in any current revenue figure, and is not a contributing mechanism to the A$2,576.36 gap specifically (PM revenue is unchanged and internally consistent across all three model stages).
7. A$63,028.75 is real, sourced, and traceable — it is Table 1's Monthly Net P&L (profit), not a revenue figure. It has not been found used as a revenue line anywhere in this repo.

## 12. Unresolved Questions

1. The exact original calculation method behind A$113,712.16 (historical 10-client, ancillary-included) remains unrecoverable from this repo's saved working — no worksheet, formula, or intermediate step survives.
2. Whether the A$2,576.36 gap should be corrected (i.e., whether the days-based first-principles method or the inherited delta-built figure should be treated as canonical going forward) is a modelling decision for Anthony/whoever next rebuilds the revenue calculation — not decided by this investigation, per the explicit scope limit.
3. What share of PM bookings are GTT-paired and therefore discount-eligible remains unknown (already tracked, item 39) — this investigation adds no new information on that specific question beyond confirming it doesn't bear on the A$2,576.36 gap.

## 13. Recommended Action

Two independent, non-conflicting options, neither of which is a financial-model rebuild:

1. **Adopt the days-based first-principles formula as canonical going forward**, explicitly retiring the inherited A$113,712.16-derived chain — since the days-based formula is the one this repo's own most recent, most rigorously re-verified work (`profit-loss-tables.md`'s 2026-08-07 nine-step walkthrough) already uses and endorses, and every step of it is exactly reproducible, unlike the historical figure. This would close the gap by design rather than by further tracing, and would need Anthony's sign-off since it changes the headline revenue-figures by ~1.6-2.2%.
2. **Correct the external reference to A$63,028.75** wherever it has been described as a revenue figure — it is Net P&L. Continuing to use it as a revenue number in any investor-facing context would materially misstate the venture's top line.

Neither option is actioned by this document — both are flagged for Anthony's decision, per the explicit scope limit (no P&L rebuild, no figure changes).
