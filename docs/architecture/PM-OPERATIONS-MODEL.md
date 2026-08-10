# PM Operations Model

**Phase:** Commercial Assumption Alignment & External Readiness, focus area 2 of 4 — investigation and optimisation only. **No financial model file was modified.** Every figure below is derived from already-canonical data (`data/canonical/pm_staffing`-equivalent fields in `staffing.yml`, `cost_ramp.yml`, `revenue_ramp.yml`, `docs/pm-staffing-roster.md`). This document sits alongside `docs/architecture/AM-OPERATIONS-SENSITIVITY-MODEL.md` as the matching operational view for the afternoon segment.

**Date:** 2026-08-10

---

## 1. PM Revenue Model — Scenario-Independent

`docs/architecture/REVENUE-RAMP-METHODOLOGY.md` §6 confirms PM revenue is genuinely identical regardless of which AM scenario (Table 1 or Table 2) is committed — PM revenue does not depend on AM client volume at all. Steady state: A$36,730.80/month (PM weekday + PM Saturday A$3,290.80). Ramp (both tables): M1 A$15,794.24 → M2 A$23,507.71 → M3 A$29,017.33 → M4 A$34,159.64 → M5+ A$36,730.80.

---

## 2. Room/Station Utilisation

PM does not use dedicated rooms — it shares the same physical treatment rooms/stations built for AM (Massage rooms, Facial/Beauty rooms, Nail Station Area, Hairdressing Area), operating in the afternoon window (Mon-Fri 12:00-18:00) after the AM GTT clients have moved through. **PM room utilisation is therefore a direct function of how many of the built stations are open, not a separate fit-out question.**

`docs/pm-staffing-roster.md` states steady-state PM volume (16 sessions/day combined across 4 lines) is ~50% of the theoretical 4-line maximum (~31 sessions/day at ~1.3 sessions/hr/role throughput) — a genuinely conservative utilisation assumption, not a capacity-constrained one. **This means PM demand at steady state does not, on its own numbers, require the full 4-station build to be met** — but the AM-driven, already-disclosed rostering-flexibility rationale for the extra stations (`equipment-costs.md`) remains the primary driver for building to 4, not PM utilisation pressure specifically.

---

## 3. Therapist Requirements

Per `data/canonical/staffing.yml`: 4 PM dedicated casual roles, 1 each (Massage, Hair, Nail, Beauty) — `staff_pm_massage`, `staff_pm_hair`, `staff_pm_nail`, `staff_pm_beauty`. **Costed on an hours-based formula, not a fixed shift:** hours/role/week = (sessions/day ÷ 4 roles × 5 days) ÷ 1.3 sessions/hr throughput, subject to the MA000005/MA000027 3-consecutive-hour casual minimum engagement floor.

**A structural finding directly relevant to this document's brief, already disclosed but not previously framed against the ramp curve this precisely:** at steady state (16 sessions/day), the 3-hour floor is only marginally cleared (3.08hrs/role/day) — `data/canonical/cost_ramp.yml`'s own status_detail confirms this exact figure. Below steady state (Months 1–4, fewer sessions per either PM ramp interpretation), **the floor is not cleared at all**, meaning PM staff are paid the 3-hour minimum regardless of actual session volume. Cross-checked directly against `cost_ramp.yml`: `pm_weekday_direct_labor` is **A$9,587.16/month identically for Months 1 through 4**, only rising to A$9,680.00 at Month 5+ steady state — confirming PM labour cost, like AM labour cost (see the companion AM document), **does not meaningfully ramp down with lower early-month PM volume.** This is the PM-side counterpart to item 43's AM finding.

---

## 4. Additional-Station Timing — Tied to the Month-4 Trigger

`docs/architecture/MVP-OPENING-DECISION-REVIEW.md` §4.3 already established the governing principle for this question: stations 3–4 (nail and hair) should be purchased and installed by **Month 4**, timed to the PM revenue ramp reaching 93%+ of steady state, rather than an arbitrary calendar window. This document confirms that timing is well-supported from the PM side specifically, using a cross-check the prior review did not perform:

- Using the canonical blanket-curve ramp (the interpretation `data/canonical/revenue_ramp.yml` actually implements): Month 4 PM volume ≈93% × 16 sessions/day ≈ **14.9 sessions/day**.
- Using the competing, unresolved session-count ramp (`docs/pm-staffing-roster.md`'s own 4/8/12/15/16 figures, item 41's still-open conflict): Month 4 PM volume = **15 sessions/day** exactly.

**Both interpretations converge closely on Month 4 regardless of which one is eventually confirmed correct** — a reassuring finding for planning the station-purchase timing specifically, even though item 41's underlying conflict (which ramp governs PM revenue) remains genuinely unresolved and is not resolved by this document.

---

## 5. Revenue Capacity — Headroom Above Steady State

The theoretical 4-line maximum (~31 sessions/day) implies real headroom above the current steady-state PM revenue assumption (16 sessions/day) — **not modelled into any current P&L figure**, and this document does not propose changing that. It is flagged here as a genuine, disclosed upside not currently captured: if real PM demand exceeds the conservative 16-session planning assumption, the built 4-station capacity (once purchased per §4) could absorb meaningfully more PM revenue without a further fit-out change, since the physical ceiling (~31 sessions/day) is nearly double the current planning assumption.

---

## 6. Risks Identified

- **PM labour cost is floor-constrained-flat in the same way AM labour cost is fixed** — the ramp curve's revenue side builds smoothly while the cost side does not track it downward in the early months, for the same underlying reason (a 3-hour casual-engagement minimum that low early-month volume does not clear).
- **The station-purchase timing trigger (Month 4) is well-supported by both competing PM ramp interpretations, but the underlying conflict between them (item 41) remains open** — if real trading data eventually shows the two ramps diverge more than they appear to at the Month 4 checkpoint specifically, this timing recommendation would need revisiting.
- **The ~50% utilisation assumption at steady state has never been tested against real demand** — flagged consistently with `docs/architecture/COMMERCIAL-VALIDATION-FRAMEWORK.md`'s own Revenue Ramp Evidence Framework finding that no conversion-rate or real-demand evidence exists anywhere in this repository for either the AM or PM ramp.

## 7. Recommended Next Decisions

1. **Adopt the Month 4 station-purchase trigger with confidence** — this document's independent cross-check against both competing PM ramp interpretations supports the timing already recommended in the MVP decision review.
2. **Do not expect early-month PM labour savings from lower volume** — early-month cash-flow planning should treat PM labour as a near-fixed cost from Month 1, the same treatment already applied to AM labour, not a cost that scales down with the ramp.

---

## Validation

No canonical YAML, financial model, or revenue/cost methodology was modified by this document. Every figure is quoted directly from `data/canonical/*.yml` or computed transparently from formulas already established in this repository (see full validation summary in this phase's combined report-back).
