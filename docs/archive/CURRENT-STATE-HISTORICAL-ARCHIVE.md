# CURRENT-STATE.md — Historical Archive

**Date archived:** 2026-08-16 (D1) | **Purpose:** `docs/CURRENT-STATE.md` is meant to contain current-state figures only, per its own stated purpose — but had accumulated multiple full superseded/historical tables and a very long changelog inline, making it harder to find the actual current figures. This file relocates that historical content so it can't be mistaken for current — nothing is deleted, per this repo's own never-delete-history convention. `docs/CURRENT-STATE.md` itself now contains only current-state figures, with a one-line pointer to this file wherever historical content used to sit inline.

**Do not use anything below for any current planning, financial, or operational decision — everything here is explicitly superseded.** See `docs/CURRENT-STATE.md` for the current figures.

---

## Historical §1 — Old 12-14-Client/23-Minute-Cadence Model (superseded 2026-08-05 by Table 1/Table 2)

| Parameter | Value | Tag |
|---|---|---|
| AM GTT capacity — HISTORICAL, superseded 2026-08-05 (was COMMITTED MODEL, corrected 2026-07-30) | **12 clients/day** — supersedes the 10-client Scenario C model as the current committed operating volume. Same 2 chairs, 2 phlebotomists, synchronized start, 6 slots/chair at 40-min spacing (was 5 slots/chair). Last Draw 1 10:20am, last departure ~12:48pm. | `[VERIFIED — programmatically checked, zero double-bookings (extended sync-treatment-solver.py method, both the phlebotomist/chair side and treatment-staff concurrency independently re-verified), 2026-07-30]`. This confirms **scheduling feasibility**, not booking demand — a ceiling, not a guarantee 12/day will actually be sold. |
| AM start time | 07:00, synchronized dual-chair start | `[VERIFIED — same source]` |
| Chairs / phlebotomists | 2 chairs, 2 phlebotomists | `[VERIFIED — same source]` |
| AM shift window (staff) | 07:00–13:00 | `[VERIFIED — financial-break-even-staff.md's existing Shift Structure section]` |
| Operating days | AM runs Mon-Fri AND Saturday (6 days); PM Mon-Fri + Sat bolt-on; Sunday closed | `[VERIFIED — Anthony's direct instruction, 2026-07-30]` |
| WDP specimen dispatch cutoff | Conditional, not a blanket "no cutoff" — overnight storage viable "in some circumstances" | `[VERIFIED — Carole Rivers, WDP, email, 2026-07-30]` |
| WDP GTT start-time guidance | "Would not normally commence a GTT after 10:30am" | `[VERIFIED — Carole Rivers, WDP, email, 2026-07-30]` |
| Growth path (not committed) | Scenario D, 15 clients/day, 3rd phlebotomist/chair | `[MODELED]` |
| 14 clients/day — PROVEN CEILING, HISTORICAL | Anthony's decision, 2026-07-31: "have 14 as the ceiling and prove it. 12 clients a day is what we will aim for each day." | `[VERIFIED]` |
| 14-client PROVEN CEILING — search method | Chair/phlebotomist ceiling: 14 clients/day, two tight bursts separated by a ~2hr09min mid-morning gap | `[VERIFIED — solver search, zero collisions]` |
| 14-client PROVEN CEILING — headcount | 9 dual-qualified treatment staff (3 Massage+Beauty pool + 3 Nails + 3 Hair), proven via sweep-line peak concurrency AND greedy first-fit, exact agreement | `[VERIFIED]` |
| 14-client PROVEN CEILING — full P&L | Monthly Net P&L: +A$36,726.23 (pre-superannuation). Total Revenue A$131,462.16. Total Costs A$94,735.93. | `[MODELED]` |
| 14-client PROVEN CEILING — downtime-fill/early-release | Between-Client Downtime-Fill Revenue A$20,717.12/month. Early-Release Cost Saving A$14,026.54/month. | `[MODELED]` |

**This entire model was RETIRED 2026-08-05** when Table 1 (18-client/day, 07:00 start, 25-min cadence) was adopted as the new PRIMARY committed model — same 8-treatment/2-phlebotomist headcount as this old model, 50% more daily revenue, strictly dominating it. See `docs/CURRENT-STATE.md` §1 for the current model.

---

## Historical §5 — Old Committed Model P&L (12-client/23-min, superseded 2026-08-05)

| Period | Figure | Tag |
|---|---|---|
| Month 1 (ramp) | ~-A$46,150/month | `[MODELED]` |
| Month 2 | ~-A$25,467/month | `[MODELED]` |
| Month 3 | ~-A$10,751/month | `[MODELED]` |
| Month 4 | ~+A$2,970/month (marginally profitable) | `[MODELED]` |
| Month 5+ (steady state) | +A$27,084.69/month (pre-superannuation) | `[MODELED]` |
| Year 1 (ramp-matched estimate) | Directionally similar shape, not independently re-derived | `[MODELED]` |
| Year 2-3 (steady state) | ~+A$325,016.22/year | `[MODELED]` |

---

## Historical §7 — Second and Third Delta Tables (10→12 client, 12→14 client, both superseded 2026-08-05)

### Second Delta — 10-Client Model vs 12-Client Committed Model (2026-07-30)

| Input | Old value (10-client) | New value (12-client) | Changed? |
|---|---|---|---|
| AM client volume/day | 10 | 12 | Yes |
| AM treatment headcount | 8 | 8 (7/6-staff pooling confirmed unavailable) | No change in headcount |
| AM direct labor cost | A$48,255/month | A$48,255/month | No — unchanged |
| AM revenue | A$55,000/month | A$66,000/month | Yes |
| AM segment standalone contribution | +A$6,745/month | +A$17,745/month | Swing: +A$11,000/month |

### Third Delta — 12-Client Daily Target vs 14-Client PROVEN CEILING

| Input | 12-client | 14-client | Changed? |
|---|---|---|---|
| AM client volume/day | 12 | 14 | Yes |
| AM treatment headcount | 8 | 9 | +1 |
| AM direct labor cost | A$48,255/month | A$53,099.50/month | +A$4,844.83/month |
| AM revenue | A$66,000/month | A$77,000/month | +A$11,000/month |
| AM segment standalone contribution | +A$17,745/month | +A$23,900.17/month | +A$6,155.17/month |
| Whole-venture Monthly Net P&L | +A$27,084.69/month | +A$36,726.23/month | +A$9,641.54/month |

**Superseded 2026-07-30 naive-headcount version (kept for trace within this archive):** an early estimate used a naive per-line multiply (12 treatment staff needed, not 9) and concluded 14 was worse than 12 (-A$9,538.33/month) — this was WRONG, corrected the same day via dual-qualification re-testing (see above).

---

## Historical §8 — Old Downtime-Fill/Early-Release Figures (12-client/23-min, superseded 2026-08-05)

| Item | Value (12-client) | Value (10-client, historical) |
|---|---|---|
| Between-booking gaps (pool a), all 8 staff | 560 min/day = 9.33 staff-hours | 420 min/day |
| Lead-in + tail (pool b), naive/unconstrained | 1,240 min/day | 1,320 min/day (naive) |
| Lead-in + tail (pool b), SAVEABLE after 3-hour minimum | 1,240 min/day — full amount | 1,100 min/day (buffer needed) |
| (a) Between-Client Downtime-Fill Revenue | A$12,679.33/month | A$9,509.50/month |
| (b) Early-Release Cost Saving | A$16,511.22/month | A$14,647.05/month |

---

## Full Historical Changelog (2026-07-29 through 2026-08-05)

Every changelog entry from `docs/CURRENT-STATE.md`'s creation (2026-07-29) through the 2026-08-05 Table 1/Table 2 rebase — the full, detailed history of every model change, correction, and finding across that period. Relocated here in full, verbatim, not summarised or altered.

**2026-08-07 (reclining chair/exam couch added as a real costed line, per Anthony's direct instruction)** — Previously only a flagged gap (`docs/VERIFICATION-TRACKER.md` item 30). Added to `equipment-costs.md` §1 as A$500-900 `[MODELED]`. Propagated: Equipment line A$42,690-96,530 -> A$43,190-97,430, §7.1 TOTAL A$60,690-139,530 -> A$61,190-140,430, §7.4 component sum A$356,890-576,280 -> A$357,390-577,180. Anthony's own adopted total (A$292,335-594,900) unaffected.

**2026-07-29 (created)** — Built in response to an outside review that found the financial model had moved 5+ times with contradicting numbers across documents, false precision on a pre-revenue business, and at least one document still training staff on an abandoned model 10 days after being flagged.

**2026-07-29 (later same session)** — WDP specimen-pickup cutoff row updated to VERIFIED (verbal, WDP, 2026-07-29). Confirmed no funding-source wording errors in this file.

**2026-07-30 (permanent downtime policy + tagged upside line)** — Added downtime-fill/early-release rows and policy. Headline figure A$28,528.50/month (superseded further below).

**2026-07-30 (later — Carole Rivers' real email + 8 settled items)** — WDP cutoff corrected from blanket "no cutoff" to conditional. WDP start-time guidance added. WDP commercial/rental-structure row added. CRITICAL flag added re: phlebotomist employment-model dependency. 8 settled items: trading days, hiring model, downtime-fill split into two pools, 3-hour minimum verified via WebFetch, PM package direction confirmed, ancillary revenue excluded, orphaned local clone flagged, Nails+Hair cross-qualification solver result (6 staff possible, hireability caveat).

**2026-07-30 (later — 6th-slot solver check + Chair B policy)** — 12-client/day confirmed feasible at 8-staff baseline. Chair B enquiry-threshold policy added (~A$306 cost-to-open, 2-client break-even).

**2026-07-30 (correction — 12 clients/day is the COMMITTED model)** — 12/day replaces 10-client Scenario C as committed. Monthly Net P&L +A$28,488.42/month (was +A$16,507.07/month).

**2026-07-30 (later — full N_max search; true chair-only ceiling 14, needs 12 treatment staff not 8 per the naive estimate)** — N_max=14 explored using a naive per-line multiply, initially rejected (worse than 12 by -A$9,538.33/month). 12-client/8-staff model confirmed as remaining committed at this point.

**2026-07-31 (PRIORITY — N_max headcount re-tested with dual-qualification, conclusion reversed)** — Re-tested via direct interval-overlap simulation: true minimum headcount at N=14 is 9, not 12. Net +A$6,155.17/month better than staying at 12 — the earlier conclusion reversed. "Unpooled" retired permanently everywhere per Anthony's direct instruction.

**2026-07-31 (later — Anthony's decision: 14 is a CEILING, 12 stays the daily target)** — "have 14 as the ceiling and prove it. 12 clients a day is what we will aim for each day." Full whole-venture P&L completed at N=14 (+A$36,726.23/month). Headcount independently re-verified via greedy first-fit, exact agreement with sweep-line method.

**2026-07-31 (later — full Section 7 startup capital build)** — Original Section 7 rebuild: A$268,142-583,559, later retired same day (see next entry).

**2026-07-31 (later still — Section 7 RECONCILED)** — Anthony's review applied 2 corrections: landlord contribution removed from headline, insurance relabelled PLACEHOLDER. Adopted total: A$292,335-594,900.

**2026-07-31 (later still — PM 3-hour minimum checked; Saturday PM Direct Labor corrected; market-size figures corrected; booking system corrected; marketing ramp modelled; trust-structure investigation added)** — Market-size figures corrected to real ABS/KPMG data (~33,570 WA, ~26,790 Perth metro, nearly double the old estimate). Booking system corrected (no per-staff Fresha accounts). Marketing spend re-timed to a genuine Month 1-4 ramp. Trust structure investigation added re: 2028 minimum trust distribution tax. Saturday PM Direct Labor corrected (A$335.55/day -> A$654.32/day) after being found non-compliant with the 3-hour minimum casual engagement rule — new baseline +A$27,084.69/month (was +A$28,488.42/month).

**2026-08 (master scenario comparison assembled)** — Cross-reference to `docs/scenario-comparison-master-2026-08.md` added, consolidating all 7 schedule scenarios discussed across the engagement.

**2026-08 (later — Carole-facing tables swapped)** — Anthony replaced the Carole-facing tables with the 25-minute-cadence pair (07:00-start/18-client and 08:00-start/12-client) — a presentation change only at this point, not yet the financial basis venture-wide.

**2026-08-05 (REBASE — the 25-min-cadence tables become the actual financial basis venture-wide)** — Item 1: tested whether Table 2 could take a 7th pair at 10:25 — rejected, requires 11 staff not 8 at every collision-free insertion point tested. Full financial rebase: the old 23-min-cadence/12-14-client pair (all content above in this archive file) RETIRED to historical status, Table 1 (18-client/07:00) adopted as the new PRIMARY committed daily model. Full recompute across every section of `docs/CURRENT-STATE.md`. This is the point at which the content in this archive file stopped being current.

---

*For the full, unabridged changelog continuing past 2026-08-05 (superannuation correction, MVP cost-optimisation, curtain compliance, WDP alignment review, waitlist validation, and this 2026-08-16 D1 archival itself), see `docs/CURRENT-STATE.md`'s own Changelog section, which remains in that file since it documents changes up to and including the current state, not superseded history.*
