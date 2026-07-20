# GTT Center Perth — Break-Even & Sensitivity Analysis

**Version:** 1.0 | **Date:** 2026-07-19 (Phase 7 new deliverable)
**Purpose:** Best/base/worst case sensitivity on patient volume and pricing, building on `financial-break-even-staff.md`, `capacity-pricing-audit.md`, and `profit-loss-tables.md`. This document consolidates existing sensitivity work into one place rather than re-deriving it from scratch — see sourcing notes throughout.

> **All figures are planning estimates.** There is no real trading data. Where this venture's own documents disagree with each other (a recurring pattern this session has surfaced repeatedly — see `docs/01_conflicts_log.md`), this document uses the most recently dated source and flags the discrepancy rather than silently picking one.

---

## 1. Break-Even — Current Canonical Figure

Per `profit-loss-tables.md` v2.0 (2026-07-17, most recent) and `HANDOFF.md`:

- **Break-even: ~298 visits/month (~13.5/day)** at the A$250 conservative planning price (Package 2, the lower of the two current packages)
- Full break-even (all fixed costs covered with margin) is reached at Month 5+ steady state, per the current 10-client AM Scenario C model
- Marginal break-even (costs just covered) is reached approximately Month 4

**Sourcing note — RESOLVED 2026-07-20 (CONFLICT-08):** the Month 4/5 figures previously appeared to differ across `cash-flow.md` (+A$4,188 at Month 4) and `pm-staffing-roster.md` (+A$4,924) because both were built on the superseded 8-client AM model. This is now resolved — `profit-loss-tables.md` v2.0's own corrected Year 1 Monthly Ramp table (added 2026-07-19, reconciled 2026-07-20) is the current authoritative source for the month-by-month build-up. "Month 4 marginal, Month 5+ full" remains directionally correct and is now backed by a reconciled figure, not just a directional estimate.

**Note on the fifth documentation variant — RESOLVED 2026-07-20 (CONFLICT-08):** `capacity-pricing-audit.md` (2026-06-11)'s "12-client/2-chair model" has been traced and flagged as superseded in that document directly — it depended on a relaxed Draw 3 rule that was not carried forward into subsequent scheduling documents. The current standing capacity ceiling is confirmed as 10 clients/day (Scenario C) or 15/day (Scenario D), not 12. See `docs/01_conflicts_log.md` CONFLICT-08 for the full resolution.

---

## 2. Break-Even Sensitivity to Average Package Price

Per `cash-flow.md`'s existing break-even-visits table (built on the pre-Scenario-C model, but the *relationship* between price and break-even volume is methodologically sound and directionally reusable):

| Avg Package Price | Break-Even Visits/Month | Break-Even Visits/Day |
|---|---|---|
| A$200 (Package 1 — **no longer offered**, retained for reference only) | 372 | 16.9 |
| A$250 (current conservative planning price — Package 2) | 298 | 13.5 |
| A$300 (Package 3 only) | 248 | 11.3 |

**Reading this table:** since Package 1 has been dropped, the realistic range this venture actually operates in is A$250 (conservative, Package 2 only) to A$300 (Package 3 only) — a break-even range of roughly 248-298 visits/month depending on package mix. The current 10-client AM Scenario C model, at full capacity (10/day × ~22 operating days = 220 AM visits/month, plus PM and Saturday), needs to be checked against this range once the PM/Saturday session-count discrepancy (see `business-plan.md` §6) is resolved — this document does not attempt that reconciliation, only surfaces where the two would need to connect.

---

## 3. Best / Base / Worst Case — Patient Volume

Adapted from `cash-flow.md`'s existing Revenue Sensitivity table (§Sensitivity Analysis), re-labelled Best/Base/Worst per this document's spec, with the same caveat that the underlying AM capacity figure (8 vs 10 clients/day) needs updating:

| Scenario | Description | Monthly Revenue (as originally modelled) | Monthly Profit (as originally modelled) |
|---|---|---|---|
| **Worst case** | AM-only at ~70% of capacity, no PM Spa Packages, no ancillary trade | A$30,800 | -A$43,591 (a real loss — this scenario represents a serious under-performance case, not a mild downside) |
| **Base case** | Full modelled capacity at both AM and PM, current conservative A$250 planning price | A$84,623 (as originally modelled — **update this figure once the AM capacity model is reconciled to 10 clients/day, see caveat above**) | +A$10,232 (as originally modelled) |
| **Best case** | Richer Package 3 mix + extended PM hours | A$101,548 (as originally modelled) | +A$25,657 (as originally modelled) |

**This table needs re-running under the current Scenario C AM model before being treated as final** — flagged rather than silently re-derived with unverified numbers, consistent with the ground rule to label every assumption and not assert unverified figures as settled.

---

## 4. Best / Base / Worst Case — Pricing

Building on `financial-break-even-staff.md`'s existing Sensitivity — Package Price vs Margin table (originally built on a 3-package structure that included the now-dropped Package 1):

| Target Margin | Blended Avg Price Needed (as originally modelled, 3-package structure) | Note |
|---|---|---|
| Break-even (0%) | A$289 | Under the current 2-package structure (Package 2/A$250, Package 3/A$300), a break-even blended average of A$289 would require a mix weighted toward Package 3 — e.g., roughly 78% Package 3 / 22% Package 2 to reach A$289 average (illustrative arithmetic, not independently re-verified against current volume assumptions) |
| 5% margin | A$306 | Would require an even heavier Package 3 skew than the mix above |
| 8-10% margin | A$317-325 | Same direction, more heavily skewed |

**This table is retained as directional context, not a current pricing recommendation.** The current standing instruction is to use A$250 (Package 2, the lower of the two packages) as the conservative planning price throughout financial models — this table shows what would be needed if the venture wanted to model a richer package mix instead, not a recommendation to change pricing now. See `docs/price-increase-comparison.md` for the separate, more current analysis of price-increase timing.

---

## 5. Combined Best/Base/Worst — Volume × Pricing Grid

**This grid is new synthesis for this document — combining the volume sensitivity (§3) and pricing sensitivity (§4) into one view, since neither existing source document does this combination.**

| | Worst-case volume (~70% capacity) | Base-case volume (full modelled capacity) | Best-case volume (extended PM hours) |
|---|---|---|---|
| **Worst-case pricing (Package 2 only, A$250)** | Loss (compounds the worst-case volume loss above) | Base case, as modelled (+A$10,232/month, pending re-verification) | Better than base, still Package-2-only pricing |
| **Base-case pricing (current 30/70-ish Package 2/3 mix, ~A$260-270 blended)** | Loss, smaller than the worst-case-pricing row | Slightly better than the base case above | Better still |
| **Best-case pricing (richer Package 3 mix, ~A$289+ blended)** | Still likely a loss at 70% volume — pricing alone cannot offset a genuine volume shortfall | Meaningfully better than base | Best combined outcome modelled |

**Reading this grid:** the worst-case scenario (low volume) is not rescued by pricing alone — `profit-loss-tables.md`'s own "Saturday AM runs at a loss" finding demonstrates that fixed staffing costs are largely insensitive to volume within a session, so a genuine demand shortfall is the dominant risk, not a pricing shortfall. This reinforces why pre-launch waitlist-building (per `business-plan.md` §8 Go-to-Market) is treated as a priority activity — it directly targets the volume axis of this grid, which matters more than the pricing axis at low volume.

---

## Changelog

**2026-07-19** — Created as a new Phase 7 deliverable, building on `financial-break-even-staff.md` §Sensitivity, `capacity-pricing-audit.md`, and `profit-loss-tables.md` rather than re-deriving new figures from scratch. Flagged (not resolved) a fifth instance of the recurring AM-capacity-figure discrepancy — `capacity-pricing-audit.md`'s own "12-client" headline figure, distinct from both the 8-client Scenario B and current 10-client Scenario C models. Added §5 (combined volume × pricing grid) as new synthesis not present in any single existing source document.

**2026-07-20 (final consistency sweep)** — Both sourcing caveats in §1 resolved per CONFLICT-08: the Month 4/5 figure discrepancy and the "12-client model" variant are now both reconciled — see updated §1 and `docs/01_conflicts_log.md`.
