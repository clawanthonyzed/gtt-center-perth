# Human-Readable Financial Model Summary

**Date:** 2026-08-16 | **Purpose:** E1 — a human-readable companion to the canonical, machine-readable `data/models/master_financial_model.yml` (which stays as-is — this document does not change it, and is not itself authoritative if the two ever disagree). **Direct link to the canonical model: [`data/models/master_financial_model.yml`](../../data/models/master_financial_model.yml).** Every figure below is sourced to that file or to `docs/CURRENT-STATE.md` §5-§8, both already-canonical — nothing here is independently derived.

---

## 1. Revenue

| | Table 1 (18/day, planning model) | Table 2 (12/day, downside/backup) |
|---|---|---|
| AM GTT package revenue | Up to 18 packages/day × A$250 (Package 1, conservative planning price) × 22 trading days/month | Up to 12 packages/day × A$250 |
| PM standalone + set packages | ~A$95/session average, ~16 sessions/day capacity, unaffected by AM volume | Same |
| Ancillary (cafe/retail) | Excluded from every P&L figure below — placeholder, no bottom-up derivation | Same |
| **Total Monthly Revenue** | **A$155,215.80** (canonical methodology, `docs/architecture/CANONICAL-REVENUE-METHODOLOGY.md`) | **A$115,720.80** |

## 2. Costs

| | Table 1 | Table 2 |
|---|---|---|
| AM Direct Labor (weekday, FTE-based) | A$48,254.67/month — 2 phlebotomists + 8 dual-qualified treatment staff, identical headcount both scenarios | Same |
| Saturday AM labor | Scales proportionally with the longer Table 1 AM day | Lower (shorter AM day) |
| Workers Comp | 1.7% of Direct Labor | Same rate |
| Non-Wage Overhead | A$13,980.00/month (rent/utilities, not client-volume-driven) | Same |
| **Total Costs** | **A$98,634.10** | **A$94,664.16** |

**What's not yet in these cost figures, disclosed rather than smoothed over:** real (not 13-month-stale) wage rates — researched 2026-08-16, not yet propagated through this recompute; a revised insurance placeholder (A$1,279/month, up from A$400) — not yet propagated; recalculated GTT supplies for the 18-client model (A$792/month, up from A$400) — not yet propagated. All three are flagged as a distinct, scoped follow-up recompute phase, not silently ignored — see `docs/VERIFICATION-TRACKER.md`.

## 3. Profit

| | Table 1 (PLANNING MODEL) | Table 2 (DOWNSIDE/BACKUP) |
|---|---|---|
| **Net Operating Result (superannuation-corrected, 2026-08-09)** | **+A$56,581.70/month** | **+A$21,056.64/month** |
| Quarterly | +A$169,745.10 | +A$63,169.92 |
| Yearly (steady-state run rate) | +A$678,980.40 | +A$252,679.68 |

## 4. Margin

| | Table 1 | Table 2 |
|---|---|---|
| Net margin (Net Result ÷ Revenue) | 36.5% | 18.2% |
| Gross margin driver | Fixed AM labor cost serves 50% more daily clients at zero extra weekday wage cost — the central finding of the 2026-08-05 rebase | — |

## 5. Break-Even

| | Table 1 | Table 2 |
|---|---|---|
| Break-even client volume | 9.404 clients/day | 8.801 clients/day |
| As % of planning target | 52.2% | 73.3% (of its own 12/day target) |
| Margin of safety | ~48% of target volume | ~27% |

## 6. Startup Capital

| Figure | Amount | Status |
|---|---|---|
| **Adopted planning figure (2026-08-10)** | **A$251,198** (Pre-Opening Capital) | Anthony approved "in principle" — not a locked final cost |
| + Working Capital Reserve | A$85,000-110,000 | Unchanged historical figure |
| **Combined funding-requirement case** | **A$336,198-361,198** | Current planning basis |
| Wider reconciled historical range | A$292,335-594,900 | Retained alongside, not replaced |

Real, itemised purchasable-item detail: [`docs/architecture/ITEMISED-PURCHASE-LIST.md`](ITEMISED-PURCHASE-LIST.md). Human-readable companion to `data/canonical/startup_costs.yml`: [`docs/architecture/HUMAN-READABLE-STARTUP-COSTS.md`](HUMAN-READABLE-STARTUP-COSTS.md).

## 7. Cash Requirements

| | Table 1 | Table 2 |
|---|---|---|
| Operating cash trough (Month 1-3 ramp) | -A$30,885.75 (Month 1) | -A$66,335.12 (Month 3) |
| **This is operating cash movement only — not the funding requirement on its own.** The Working Capital Reserve (§6) already covers this; do not add the two together (would double-count). | | |

## 8. Key Assumptions

- **Planning price:** A$250 (Package 1, the lower of the two current packages) used for every AM revenue calculation — a deliberate conservative safety margin, not a blended average.
- **PM average:** ~A$95/session — a planning estimate, no real booking data exists yet.
- **Headcount:** 8 dual-qualified treatment staff + 2 phlebotomists, confirmed identical at both 18-client and 12-client volumes.
- **Trading days:** 22/month (Mon-Sat), Sunday closed.
- **Superannuation:** 12% of OTE, confirmed current for FY2026-27 (researched 2026-08-16).
- **Workers Comp:** 1.7% of Direct Labor — a planning estimate, not a confirmed WorkCover WA rate quote.

## 9. Sensitivity

- **The single largest revenue lever:** which table is used as the planning basis — Table 1 vs Table 2 is worth **+A$35,525.06/month** in Net Operating Result, at identical headcount. This is why Table 1 (18/day) is the settled planning model.
- **The single largest unmodelled variable:** AM→PM conversion rate — genuinely unknowable pre-operational (per standing instruction), not stress-tested here because there is no number to stress-test yet. See `docs/experience/AM-TO-PM-DATA-CAPTURE-SPECIFICATION.md` for how this becomes measurable once trading starts.
- **Break-even margin of safety** (§5) means the venture could lose nearly half its planning-target AM volume (Table 1) and still break even — a real, disclosed resilience finding, not an assumption.

## 9a. AM Standalone Weekday Contribution (C6)

**A real, already-computed figure, surfaced here explicitly.** The AM segment's own standalone contribution (weekday revenue minus weekday AM direct labor only, before Non-Wage Overhead/Workers Comp/PM) — per `docs/CURRENT-STATE.md` §7's Fourth Delta table:

| | Table 1 (18/day) | Table 2 (12/day) |
|---|---|---|
| AM revenue (weekday, 22 days) | A$99,000/month (18 × A$250 × 22) | A$66,000/month |
| AM direct labor (weekday, FTE) | A$48,254.67/month (unchanged, same headcount) | A$48,254.67/month |
| **AM segment standalone contribution (weekday)** | **+A$50,745.33/month** | **+A$17,745.33/month** |

**This is the central finding behind the 2026-08-05 rebase:** Table 1 serves 50% more daily clients than Table 2 at literally zero extra weekday labor cost, because these are fixed-salary FTE roles and the extended day still fits the existing shift budget — the entire +A$33,000/month revenue delta between the two tables flows straight to this contribution line.

## 10. 18-Client Scenario (Table 1) — This Is the Planning Model

Every figure in this document's primary column is Table 1. See `docs/strategy/18-CLIENT-COMMERCIAL-STRESS-TEST.md` for the full break-even/margin-of-safety stress test and `docs/strategy/18-CLIENT-OPERATIONAL-STRESS-TEST.md` for the minute-by-minute operational verification.

## 11. Downside Scenario (Table 2)

Table 2 (12/day, 08:00 start) is the downside/backup reference model — used if information from WDP/Carole changes which operating model is more beneficial. Same headcount as Table 1, lower revenue ceiling, still profitable (+A$21,056.64/month) and still has its own break-even margin of safety (§5).

---

## What This Document Deliberately Does Not Do

- Does not change `data/models/master_financial_model.yml` — that file remains canonical and machine-readable, this is a human-readable companion only.
- Does not invent any figure not already present in `docs/CURRENT-STATE.md` or the canonical model.
- Does not resolve the still-open wage-rate/insurance/GTT-supplies propagation gap (§2) — flagged, not silently closed.

---

## Changelog

**2026-08-16** — Created per E1. Companion to `data/models/master_financial_model.yml`, direct-linked at the top. Built entirely from already-canonical figures in `docs/CURRENT-STATE.md` §5-§8 and the canonical model itself — no new financial derivation.
