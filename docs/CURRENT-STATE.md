# GTT Center Perth — Current State (Canonical Numbers)

**Created:** 2026-07-29 | **Purpose:** The single canonical file for today's actual figures — package prices, client capacity, headcount, monthly net P&L, and startup capital range. Every other document in this repo defers to this file for these figures; they no longer independently restate them as sources of truth.

**Why this file exists:** an outside review of this repo found the financial model had moved 5+ times across different documents with contradicting numbers, false precision on a pre-revenue business, and a stale document (`operations-manual.md`) still training staff on an abandoned scheduling model 10 days after being flagged. This file exists to stop that pattern: one number per fact, one tag per number, one place to look.

**Tagging system — every figure below carries exactly one tag:**
- `[VERIFIED — source, date]` — confirmed by an external party (a real WDP email, a signed quote, an accountant confirmation, or a programmatic scheduling simulation that is itself the primary source, not an assumption about the real world)
- `[MODELED — assumption: <name it>]` — internally calculated from other modeled or verified inputs
- `[PLACEHOLDER — not yet known]` — still a guess, or genuinely unreconciled across this repo's own documents

**No figure enters this file without a tag. If you can't tag it, don't put a number here — write PLACEHOLDER and add it to `docs/VERIFICATION-TRACKER.md` instead.**

---

## 1. Operational Model

| Parameter | Value | Tag |
|---|---|---|
| AM GTT capacity — COMMITTED MODEL (corrected 2026-07-30) | **12 clients/day** — supersedes the 10-client Scenario C model as the current committed operating volume. Same 2 chairs, 2 phlebotomists, synchronized start, 6 slots/chair at 40-min spacing (was 5 slots/chair). Last Draw 1 10:20am, last departure ~12:48pm. | `[VERIFIED — programmatically checked, zero double-bookings (extended sync-treatment-solver.py method, both the phlebotomist/chair side and treatment-staff concurrency independently re-verified), 2026-07-30]`. This confirms **scheduling feasibility**, not booking demand — a ceiling, not a guarantee 12/day will actually be sold. |
| AM start time | 07:00, synchronized dual-chair start | `[VERIFIED — same source]` |
| Chairs / phlebotomists | 2 chairs, 2 phlebotomists | `[VERIFIED — same source]` |
| AM shift window (staff) | 07:00–13:00 (per `financial-break-even-staff.md`'s stated AM shift structure) — comfortably covers the new ~12:48pm last departure | `[VERIFIED — financial-break-even-staff.md's existing Shift Structure section]`. **Methodology correction (2026-07-30):** the prior downtime-fill calculation (10-client model) used `operations-manual.md`'s 12:30 "EOD wrap" time as the shift boundary — that was the wrong source for the treatment-staff shift specifically; this document's own explicit 07:00-13:00 AM shift statement is the correct one, used for the 12-client recompute below. |
| Operating days | AM runs Mon-Fri AND Saturday (6 days) at the new 12-client committed volume; PM Mon-Fri + Sat bolt-on; Sunday closed | `[VERIFIED — Anthony's direct instruction, 2026-07-30 — Saturday trading is settled, not deferred, and reuses the same committed AM volume as weekdays]`. Sunday's conditional reopening remains `[MODELED — assumption: Sunday reopens only once standalone PM demand is proven and profitable; a business choice, not a legal requirement per WA Retail Trading Hours Act exemption — am-capacity-weekend.md]` |
| WDP specimen dispatch cutoff | **Conditional, not a blanket "no cutoff"** — overnight storage viable "in some circumstances" (fluoride oxalate tubes stable ~24hrs); a late booking "would not necessarily prevent collection, although specimen type and storage requirements would always need to be considered" | `[VERIFIED — Carole Rivers, WDP, email, 2026-07-30]`. **Corrected 2026-07-30** — the earlier 2026-07-29 verbal readback oversimplified this into a blanket "no cutoff," which was wrong; this is real, written, primary-source correspondence, but conditional, not unconditional. Exact storage/handling conditions with WDP still need to be nailed down. See `cutoff-time-CORRECTION.md`. |
| WDP GTT start-time guidance | "Would not normally commence a GTT after 10:30am" (exceptions for shift workers etc.) — supersedes the earlier PathWest-sourced "preferably before 10am." **This is the guidance the new 12-client committed model is built around** — last Draw 1 10:20am, 10 minutes inside it. | `[VERIFIED — Carole Rivers, WDP, email, 2026-07-30]`. See `king-edward-start-time-constraint.md`. |
| WDP commercial/rental structure | Annual rental arrangement, terms depend on pathology volume, referring-doctor count on-site, location/accessibility, business opportunity — **no figure quantified anywhere** | `[PLACEHOLDER — not yet known]`. Owner: Anthony/WDP commercial negotiation. Do not invent a rental estimate. See `docs/VERIFICATION-TRACKER.md`. |
| Growth path (not committed) | Scenario D, 15 clients/day, 3rd phlebotomist/chair | `[MODELED — am-capacity-weekend.md, scenario-d-investigation.md; provisional on the WDP cutoff answer above; now a growth path BEYOND the 12-client committed model, not beyond 10]` |
| Chair B opening policy — interaction with the 12-client committed model FLAGGED, not resolved (2026-07-30) | The 2026-07-30 Chair B enquiry-threshold policy (Chair A default/guaranteed, Chair B opens only on a 2nd enquiry per slot) was recorded the same session the 10-client model was still current. **The now-committed 12-client model runs both chairs synchronized across all 6 daily slots as the baseline** — this appears to conflict with "Chair B only opens on demand." **Not resolved here — flagged for Anthony:** does the enquiry-threshold policy still apply (e.g., only during ramp-up before real demand reaches 12/day), or is it superseded now that both-chairs-always-on is the committed target? Do not guess either way. | `[PLACEHOLDER — explicitly flagged for Anthony's clarification, not assumed]`. See `docs/VERIFICATION-TRACKER.md` item 1f. |
| Rostering policy | Roster only the roles a given day's confirmed bookings actually require — a **standing, permanent operating rule**, not a ramp-up-period measure | `[VERIFIED — Anthony's direct instruction, 2026-07-30]` — see `pm-staffing-roster.md`'s Booking-Driven Rostering Policy section, formalized as permanent 2026-07-30 |
| Staff downtime policy | **Two separate pools (corrected 2026-07-30):** between-client gaps fillable by advance-online-booking only (not walk-in/day-of) — sellable revenue. Lead-in/tail (before first/after last booking) — not sellable, staff engagement starts later/ends earlier instead (early release), subject to the 3-hour minimum casual engagement. | `[VERIFIED — Anthony's direct instruction, 2026-07-30]` — see `financial-break-even-staff.md`'s Staff Downtime Protocol. Quantified: §8 below. |

---

## 2. Package Prices

| Item | Value | Tag |
|---|---|---|
| Package 1 (fixed 2×30-min services) | A$250 | `[MODELED — assumption: Anthony's locked launch price, services-pricing-locked.md renumbered 2026-07-20; not externally market-tested]` |
| Package 2 (flexible: 2×45min, or 1×45+1×30min, or 2×30min) | A$300 | `[MODELED — same basis]` |
| AM revenue calculations use which price | A$250 (Package 1) as a deliberate conservative safety price, not a blended average | `[MODELED — standing instruction, not a re-derivation]` |
| PM individual a-la-carte average | ~A$95/session | `[MODELED — assumption: pm-staffing-roster.md planning estimate, no real booking data]` |
| PM set/fixed packages | **Confirmed direction 2026-07-30** (PM Duo/Refresh/Glow menu) — pricing itself still requires Anthony's final sign-off | `[VERIFIED — Anthony's direct instruction, 2026-07-30, direction confirmed]` + `[PLACEHOLDER — final pricing not yet signed off, pm-package-structure.md]` |

---

## 3. Client Capacity

| Item | Value | Tag |
|---|---|---|
| AM GTT capacity ceiling | **264 visits/month (12/day × 22 trading days)** — was 220/month at the superseded 10-client model | `[VERIFIED capacity — solver-checked 2026-07-30]` + `[MODELED — depends on referral pipeline filling all 12 daily slots; not a revenue guarantee]` |
| AM GTT weekly ceiling (6-day week incl. Saturday) | **72 slots/week** (was 60/week) | `[MODELED — derived: 12/day × 6 days]` |
| Perth metro GTT tests/week (addressable market) | ~277/week | `[MODELED — research.md ABS/AIHW-derived estimate, not primary market research]` |
| Share of addressable market at full AM capacity | **~26% (6-day operating week)** (was ~22%) | `[MODELED — derived from the two rows above; business-plan.md flags this has not been re-run against every underlying assumption]` |
| PM individual services capacity (steady state) | ~16 sessions/day (~350/month) | `[MODELED — assumption: ~50% utilisation of theoretical 4-line capacity, pm-staffing-roster.md; no real demand data exists yet]` |

---

## 4. Headcount

| Role | Qty | Tag |
|---|---|---|
| Venue Manager (Managing Director) | 1 — new hire, not yet in place | `[PLACEHOLDER — critical-path hire, recruitment gated on securing a physical venue location, not yet begun]` |
| Phlebotomist (AM only, Chair A / Chair B) | 2 | `[MODELED — financial-break-even-staff.md award-rate structure]`. **CRITICAL OPEN DEPENDENCY (flagged 2026-07-30):** this entire row, and the ~A$48,255/month AM Direct Labor figure it feeds into (§7 below), assumes GTT Center Perth employs its own phlebotomist(s) directly — the current modelled baseline. Carole Rivers' 2026-07-30 email raises a real possibility that under WDP's rental-clinic model, WDP supplies/employs the phlebotomist instead (their email: phlebotomist "safety, wellbeing and employment responsibilities... would remain with Western Diagnostic Pathology"), which would replace this wage line with a to-be-negotiated rental fee. **Anthony's explicit answer: NOT DECIDED — needs to ask Carole directly.** Do not treat the current in-house figure as settled once this is answered — it may change materially. `[PLACEHOLDER — critical, high-priority, see docs/VERIFICATION-TRACKER.md]` |
| AM treatment staff (Massage, Nail, Hair, Beauty) | **8 — no pooling reduction applies at the now-committed 12-client volume.** | `[VERIFIED — solver-checked 2026-07-30 against the 12-client model]`. **Correction, 2026-07-30:** the 2026-07-29 finding that 7 staff (Massage+Beauty pooled) or even 6 staff (Massage+Beauty AND Nails+Hair pooled) could work was correct **only for the 10-client model, now superseded.** Re-ran both pooling configurations against the committed 12-client schedule — both FAIL (specific clients unassignable: 2 at 7-staff, 4 at 6-staff). The full, un-pooled 8-person roster (2 each: Massage, Nail, Hair, Beauty) is required at 12 clients/day. Do not action a 7-staff or 6-staff hiring plan based on the earlier finding — it does not apply at the current committed volume. |
| Receptionist / Manager (split shift) | 1 | `[MODELED]` |
| PM dedicated casual roster (1 each: massage, hair, nail, beauty) | 4 | `[MODELED — pm-staffing-roster.md, hours-based costing, not a flat FTE headcount]` |
| Casual Relief Pool | Budget line, not a fixed headcount | `[MODELED — A$15,000/yr budgeted]` |
| **Total heads (AM 8-staff, no-pooling + PM + relief pool structure)** | **~16-17** | `[MODELED — sum of above; unchanged in absolute headcount from the 10-client model, since 8-staff was always the traceable payroll baseline — what changed 2026-07-30 is that the pooling REDUCTIONS below it are no longer valid at the committed 12-client volume]` |
| Possible combined AM/PM rotating pool (2026-07-28 proposal) | Potentially fewer than 11 total treatment/PM heads across both shifts | `[PLACEHOLDER — dual-role-staffing-model-2026-07-28.md v3.0 explicitly states this is "not booked as a confirmed saving," pending real roster data]` |
| Hiring model | **Settled 2026-07-30:** cross-qualified hires where trades allow (Massage+Beauty dual-Cert-IV pairing, per `profit-loss-tables.md`'s Treatment Headcount section). All service staff hired as casuals initially; reviewed for conversion to part-time once regular, proven hours exist per role (matches `pm-staffing-roster.md`'s existing "casual for first 3-6 months, review conversion at Month 3-6" policy). | `[VERIFIED — Anthony's direct instruction, 2026-07-30]` |
| ~~Possible Nails+Hair cross-qualification (solver-checked 2026-07-29)~~ SUPERSEDED 2026-07-30 | ~~Would bring combined treatment headcount to 6~~ — **this finding was correct only for the 10-client model, which is now superseded.** At the committed 12-client volume, neither the Massage+Beauty (7-staff) nor the Nails+Hair (6-staff) pooling reduction holds — both fail (see the row above). | `[SUPERSEDED — the 2026-07-29 solver result was accurate for its own (now-historical) 10-client scenario; do not action a 6-staff or 7-staff hiring plan]` |

---

## 5. Monthly Net P&L

> **2026-07-30 (major update) — recomputed at the new committed 12-client volume, ancillary still excluded.** The 10-client figures (also ancillary-excluded, dated earlier the same day) are now superseded, not just the pre-ancillary-exclusion ones. Full recompute in `profit-loss-tables.md`.

| Period | Figure | Tag |
|---|---|---|
| Month 1 (ramp, recomputed against the new 12-client/A$66,000 AM ceiling) | ~-A$47,050/month (was ~-A$46,907/month at 10-client) | `[MODELED — ramp-percentage assumption (43% of ceiling) applied to the new 12-client steady-state ceiling]` |
| Month 2 | ~-A$26,167/month (was ~-A$26,532/month) | `[MODELED — same basis, 64% of ceiling]` |
| Month 3 | ~-A$11,251/month (was ~-A$11,979/month) | `[MODELED — same basis, 79% of ceiling]` |
| Month 4 | ~+A$2,670/month (was ~+A$1,603/month) | `[MODELED — same basis, 93% of ceiling; marginally profitable]` |
| Month 5+ (steady state, precise weekday/Saturday-blended calculation) | **+A$28,488.42/month** (was +A$16,507.07/month at 10-client, ancillary excluded both times) | `[MODELED — profit-loss-tables.md, 2026-07-30 12-client recalculation, delta approach from the validated 10-client baseline: +A$13,165.00/month extra AM revenue (2 extra clients/day, unchanged headcount/FTE labor cost) + A$1,164.14/month extra Saturday AM labor (hours-based costing scales with volume, proportional estimate not a fresh Saturday-specific solver rebuild) + resulting Workers Comp uptick]` |
| Year 1 (ramp-matched estimate) | Directionally similar shape to the 10-client estimate, shifted up by the AM revenue increase — not independently re-derived to the same precision this round (flagged, not fabricated) | `[MODELED — profit-loss-tables.md Years 1-3 Annual Projection; needs a dedicated recompute as a follow-up, see docs/VERIFICATION-TRACKER.md]` |
| Year 2-3 (steady state, no further capacity growth) | ~+A$341,861.03/year (was ~+A$198,084.84/year at 10-client) | `[MODELED — Month 5+ figure ×12]` |

**None of the above is based on real trading data — there is no venue open yet.**

**AM Direct Labor recomputed fresh, not reused (per instruction):** 2 phlebotomists (A$86,136/yr) + 8 treatment staff (A$492,920/yr) = A$579,056/yr ÷ 12 = **A$48,254.67/month ≈ A$48,255/month — UNCHANGED from the 10-client figure.** This is not an oversight: headcount is unchanged (solver-confirmed, no pooling reduction applies at 12/day — see §4), these are fixed-salary FTE roles (not hours-billed), and the extended AM day (~12:48pm last departure) still fits inside the already-budgeted 07:00-13:00 shift window (see §1) — so the same 10 salaried staff serving 2 more clients/day is pure margin, not an added cost. Flagged transparently: this FTE-based reasoning is a different (more traceable) method than the original, never-fully-preserved "actual hours per client timetable" approach used for the 10-client figure — a methodology clarification, not a silent inconsistency.

**Also not included in any figure above:** the Between-Client Downtime-Fill Revenue and Early-Release Cost Saving — both recomputed for the 12-client schedule (not carried over from 10-client), see §8 below.

---

## 6. Startup Capital Range — UNRECONCILED, Flagged Rather Than Resolved

**This is the clearest example of the "financial model moved 5+ times" finding.** Three different ranges exist across this repo's own documents, none confirmed as authoritative:

| Source | Range | Tag |
|---|---|---|
| `investor-memorandum.md` (original itemised build: fit-out, equipment, IT, working capital, legal) | A$363,000 mid / A$292,000-493,000 range | `[PLACEHOLDER — itemised, but not re-verified against the current 10-client/2-package model]` |
| `HANDOFF.md` (2026-07-17) | "~A$144,500-242,500 realistic range, down from an inflated A$363,000 original figure" | `[PLACEHOLDER — no itemised build shown in that document — cannot be traced]` |
| `business-plan.md` §9 (attributed to `cash-flow.md`) | Low A$209,000 / Mid A$305,000 / High A$431,000 | `[PLACEHOLDER — this breakdown does not currently exist anywhere in cash-flow.md's own content as of its 2026-07-20 full rebuild; the citation could not be verified this session]` |

**No single figure is presented here as canonical.** Picking one of the three arbitrarily would repeat exactly the false-precision problem this file exists to prevent. **What's actually needed:** a fresh, itemised fit-out/equipment/legal/working-capital build against the current model (10-client Scenario C, 2-package structure, current staffing) — tracked as an open item in `docs/VERIFICATION-TRACKER.md`. Anthony and an accountant/quantity surveyor should confirm before this figure is used in any real funding conversation.

---

## 7. AM/GTT Segment Profitability — Delta Table (Old Model vs Current Model)

**Anthony's belief, per the task brief:** a revised model now shows the AM segment profitable on its own, versus the previously-modeled loss (revenue A$44,000/mo vs direct labor A$48,255/mo, per `pm-staffing-roster.md`).

**Finding after tracing every input:** the swing from loss to profit is real and traceable, but it is **not a new model** — it is the existing 10-client Scenario C capacity change (verified 2026-07-17, already resolved venture-wide as CONFLICT-08 on 2026-07-20) applied to a segment-level table (`pm-staffing-roster.md`'s "Profit Breakdown — AM vs PM Contribution") that had never been updated to match. No document in this repo describes any further AM-specific model change beyond this. The one candidate that could have introduced a further change — `dual-role-staffing-model-2026-07-28.md` v3.0 (combined AM/PM rotating staff pool) — explicitly states its potential headcount saving is **"not booked as a confirmed saving,"** pending real roster data. **I found no sourced basis for any AM-segment improvement beyond the Scenario C change below — if Anthony means something more recent than that, it isn't in this repo's documents and should not be presented as a number until it is.**

| Input | Old value | New value | Changed? | Tag |
|---|---|---|---|---|
| AM client volume/day | 8 (Scenario B) | 10 (Scenario C) | **Yes — this is the only changed input** | Old: `[PLACEHOLDER — early Scenario B planning assumption, never independently verified as a capacity claim]`. New: `[VERIFIED — scenario-c-sync-timetables.md, 2026-07-17, programmatic zero-double-booking simulation]` |
| Package price used | A$250 | A$250 | No | `[MODELED — unchanged, conservative safety price both times]` |
| AM treatment headcount (2 phlebotomists + 8 treatment staff) | 10 people | 10 people | No — same peak-concurrency requirement at both volumes per `profit-loss-tables.md`'s Treatment Headcount analysis | `[MODELED — financial-break-even-staff.md award rates, traceable]` |
| AM direct labor cost | A$48,255/month | A$48,255/month | No | `[MODELED — same, traceable calculation: 2 phlebotomists ($7,178/mo) + 8 treatment staff ($41,077/mo)]` |
| AM revenue (client volume × price × 22 days) | A$44,000/month | A$55,000/month | **Yes — direct consequence of the volume change above** | `[MODELED — arithmetic on the VERIFIED capacity ceiling above; actually earning A$55,000/month still depends on filling all 10 daily slots, which is a referral-pipeline/demand question, not yet proven]` |
| **AM segment standalone contribution (revenue minus direct labor only)** | **-A$4,255/month** | **+A$6,745/month** | **Swing: +A$11,000/month, exactly matching the revenue delta — confirms no other input changed** | See rows above |

**Bottom line:** the AM segment can be presented as profitable on a standalone direct-labor basis (+A$6,745/month) using figures already fully traceable in this repo — but this is the 12-day-old Scenario C correction reaching a table that was overlooked, not a new finding. `pm-staffing-roster.md` has been corrected to match (see that document's 2026-07-29 changelog entry). This does not change the venture-level headline figure, which already incorporated the Scenario C AM revenue correctly since 2026-07-20 — only this one segment-level table was stale.

> **PROMINENT FLAG, added 2026-07-30 — the entire AM Direct Labor figure (A$48,255/month) in this table is contingent on an unresolved employment-model question, not yet settled.** Carole Rivers' (WDP) 2026-07-30 email raises the real possibility that WDP, not GTT Center Perth, employs the phlebotomist under WDP's venue-rental clinic model (their email: phlebotomist employment responsibilities "would remain with Western Diagnostic Pathology"). **Anthony's explicit instruction: this is NOT DECIDED — ask Carole to clarify before assuming either way.** The A$48,255/month figure above assumes the current in-house employment model and has NOT been changed — this flag exists so nobody mistakes it for settled once the employment-model question is actually answered. If WDP ends up supplying/employing the phlebotomist, this whole AM segment delta table would need to be rebuilt against a rental-fee cost structure instead of a wage cost structure — a materially different, not-yet-modeled scenario. See `docs/VERIFICATION-TRACKER.md` (high-priority item) and `cutoff-time-CORRECTION.md`.

### Second Delta — 10-Client Model (above, now historical) vs 12-Client Committed Model (2026-07-30)

**The 10-client model above is itself now superseded** — 12 clients/day is the new committed AM volume (per Anthony's direct correction, WDP's 10:30am start-time guidance and the solver check both confirming feasibility). The table above is retained for historical trace (it correctly resolved the 8→10 question); this table chains the next real change:

| Input | Old value (10-client) | New value (12-client, committed) | Changed? | Tag |
|---|---|---|---|---|
| AM client volume/day | 10 | 12 | **Yes** | Old: `[VERIFIED — 2026-07-17]`. New: `[VERIFIED — solver-checked 2026-07-30 against WDP's 10:30am guidance, zero double-bookings/concurrency violations]` |
| AM treatment headcount | 8 (no pooling reduction adopted) | 8 (no pooling reduction possible — solver-confirmed) | No change in headcount, but the **7/6-staff pooling option is now confirmed unavailable**, not just "not yet adopted" | `[VERIFIED — solver-checked 2026-07-30]` |
| AM direct labor cost | A$48,255/month | A$48,255/month | **No — unchanged.** Same headcount, fixed-salary FTE roles, extended day still fits the existing 07:00-13:00 shift budget. | `[MODELED — recomputed fresh this round, not reused: 2 phlebotomists A$86,136/yr + 8 treatment A$492,920/yr = A$579,056/yr ÷12]` |
| AM revenue (client volume × price × 22 days) | A$55,000/month | A$66,000/month | **Yes** | `[MODELED — arithmetic on the verified 12-client capacity ceiling; still depends on the referral pipeline actually filling all 12 daily slots]` |
| **AM segment standalone contribution** | **+A$6,745/month** | **+A$17,745/month** | **Swing: +A$11,000/month, exactly matching the revenue delta (2 extra clients × A$250 × 22 days) — confirms no other input changed** | See rows above |

**Bottom line:** the AM segment's standalone margin improves further under the 12-client committed model — again because the same fixed headcount serves more clients, not because of any staffing or pricing change. The same phlebotomist-employment-model dependency flagged above applies identically to this new figure — not re-flagged twice, see the prominent flag above.

---

## 8. Downtime-Fill Revenue & Early-Release Saving — Two Separate Tagged Pools (Recomputed 2026-07-30 for the 12-Client Model)

> **This section previously showed figures for the 10-client model (A$9,509.50/month between-client, A$14,647.05/month early-release). Both have been recomputed against the new 12-client schedule's actual, different gap-time pattern below — not carried over unchanged.**

**Policy (permanent, not ramp-up-only, unchanged by the volume increase):**
- **Between-client gaps** (mid-shift, strictly between two of a staff member's own bookings) — fillable with standalone/non-GTT bookings **made in advance online only** (not walk-in, not day-of). This is the only pool that generates revenue.
- **Lead-in/tail** (before a staff member's first booking, or after their last, that day) — NOT sellable. That staff member's engagement starts later or ends earlier instead — a cost saving, subject to the 3-hour minimum casual engagement.

Both per `financial-break-even-staff.md`'s Staff Downtime Protocol and `pm-staffing-roster.md`'s Booking-Driven Rostering Policy (permanent, not ramp-up-only).

**Independently re-derived minute totals for the 12-client schedule** (walked directly from the solver's per-client treatment assignment for the new 6-slot/chair model, per staff member, using the 07:00-13:00 shift boundary — corrected source, see §1): **every one of the 8 treatment staff now has 3 bookings/day (135 min booked each), up from the old mix of 4 staff at 3 bookings and 4 at 2 bookings.** This changes the gap pattern materially, not just the totals:

| Item | Value (12-client) | Value (10-client, historical) | Tag |
|---|---|---|---|
| Between-booking gaps (pool a), all 8 staff | **560 min/day = 9.33 staff-hours** | 420 min/day | `[VERIFIED — walked directly from the solver's 12-client per-staff booking assignment; not estimated]` |
| Lead-in + tail (pool b), naive/unconstrained | **1,240 min/day** | 1,320 min/day (naive) | `[VERIFIED — same source]` |
| Lead-in + tail (pool b), SAVEABLE after the 3-hour minimum engagement floor | **1,240 min/day — full amount, no buffer needed** | 1,100 min/day (buffer needed for 4 of 8 staff) | `[MODELED — at 12 clients/day, every staff member's trimmed span (booked+between = 205 min) already exceeds the 180-min floor, so no mandatory buffer is retained anywhere — a genuine difference from the 10-client pattern, not just a bigger number]` |
| **(a) Between-Client Downtime-Fill Revenue (headline)** | **A$12,679.33/month** (was A$9,509.50/month) | | `[MODELED — assumption: 50% utilisation, same discount factor as standalone PM demand elsewhere in this repo; throughput 1.3 sessions/hr and A$95/session average reused from pm-staffing-roster.md]` |
| **(b) Early-Release Cost Saving (headline)** | **A$16,511.22/month** (was A$14,647.05/month) | | `[MODELED — assumption: staggered per-person engagement start/end times; wage rates from financial-break-even-staff.md, traceable]` |
| 3-hour minimum casual engagement (constraint applied above) | MA000005 clause 11.5, MA000027 clause 11.2 | | `[VERIFIED — Fair Work Ombudsman/Fair Work Commission, checked via direct WebFetch against awards.fairwork.gov.au, 2026-07-30]` |

**Neither (a) nor (b) is included in §5's +A$28,488.42/month baseline — both are separate, tagged lines, and are not blended with each other either.** Full derivation, per-staff breakdown, and caveats in `profit-loss-tables.md`'s "Downtime-Fill Revenue & Early-Release Saving" section. Treat both as planning-conversation figures, not inputs to cash-flow or break-even calculations.

---

## 9. Orphaned Local Clone — Do Not Edit

**A second, never-pushed, now-diverged local clone of this repo exists at `C:\Users\azed9\Documents\GitHub\gtt-center-perth`** (created by an earlier "Claude in Cowork" session on Anthony's machine). Confirmed 2026-07-30:
- Its `git log` shows it stopped at commit `d7fe9bc` — it is missing every commit since (including this file's creation and all subsequent updates).
- It has its own uncommitted, never-pushed local files: a competing `docs/CURRENT-STATE.md` (superseded, do not use), an uncommitted `docs/partner-profitability-brief.md`, and its own `CLAUDE.md` still carrying the "Imara's personal savings" wording error fixed in this repo on 2026-07-29.
- **This scratchpad clone (wherever this session is running from) and the GitHub remote (`clawanthonyzed/gtt-center-perth`) are the only canonical sources.** The orphaned clone should not be edited by any future session.
- **Do not delete it without checking with Anthony first** — it may contain content (the partner-profitability-brief.md draft, a standalone HTML profitability calculator mentioned in a prior session) he still wants to review before it's discarded. If it's ever touched again, re-clone fresh from GitHub rather than trying to reconcile its diverged history.

---

## 10. How to Use This File

- Every document in `docs/` that states a package price, client capacity, headcount, monthly P&L figure, or startup capital range should point here, not restate the figure as its own independent source.
- Run `python tools/check_consistency.py` before quoting any figure externally (investor conversation, lease negotiation, staff training) — it greps every `docs/*.md` file for values that contradict this file.
- When a figure changes here, it does not need to be manually propagated to every other document — those documents should already be pointing here. If you find one that restates a figure independently, add a pointer instead of a second copy.
- See `docs/VERIFICATION-TRACKER.md` for every unconfirmed fact and who can confirm it.

---

## Changelog

**2026-07-29 (created)** — Built in response to an outside review that found the financial model had moved 5+ times with contradicting numbers across documents, false precision on a pre-revenue business, and at least one document (`operations-manual.md`) still training staff on an abandoned model 10 days after being flagged. This file is the process fix, not just a numbers fix — see `rules/CLAUDE.md` for the accompanying hard rule requiring every future figure to carry a tag from this system.

**2026-07-29 (later same session — follow-up corrections from Anthony)** — Two direct corrections applied: (1) the WDP specimen-pickup cutoff row in §1 updated from `[PLACEHOLDER]` to `[VERIFIED — Carole Rivers, WDP, verbal confirmation, 2026-07-29]` — no cutoff exists within business operating hours, per WDP, but this is verbal only and not yet in writing; kept as an open action item in `docs/VERIFICATION-TRACKER.md`, not closed out. (2) Confirmed no funding-source wording errors exist in this file (checked directly) — the "Imara's personal savings" wording error found in 6 other documents this session (`CLAUDE.md`, `executive-summary.md`, `gtt-center-perth-overview-for-imara.md`, `revenue-extraction-options.md`, `risk-register.md`, `swot-analysis.md`, `team-startup.md`, `financial-model.md`) does not appear here since this file never described the funding source. Also: `financial-model.md` was opened and split this session (not left "untouched") — see that document's own changelog; its trust/tax content is separate from this file's scope and not duplicated here.

**2026-07-30 (permanent downtime policy + tagged upside line, per Anthony's direct instruction)** — Added two §1 rows recording the new permanent rostering/downtime policy (previously this was implicitly framed as a ramp-up-period practice in `pm-staffing-roster.md`, now explicitly a standing rule at any volume level). Added new §8 "Downtime-Fill Revenue — Tagged Upside," quantifying the policy using real per-staff gap-time data pulled directly from `scenario-c-sync-timetables.md` (not estimated) — headline figure **A$28,528.50/month**, `[MODELED]`, kept strictly separate from the +A$25,087.07/month baseline in §5, not blended into it. Full derivation in `profit-loss-tables.md`. Also fixed a contradiction the policy change exposed: `operations-manual.md`, `financial-break-even-staff.md`, and `pm-staffing-roster.md` previously stated AM treatment staff could never be reassigned to walk-in/general-public work during the AM window — corrected across all three to reflect that individual downtime between scheduled bookings is now fillable, while the headcount floor (set by peak concurrent demand) is unchanged.

**2026-07-30 (later same day — Carole Rivers' real email + 8 settled items, major update)** — Two batches of corrections, both per Anthony's direct instruction:

*Carole Rivers' actual WDP email (primary source, more authoritative than any prior verbal readback or the PathWest patient-instructions PDF):* corrected §1's WDP cutoff row from a blanket "no cutoff" (2026-07-29 verbal readback, wrong) to the real conditional answer (overnight storage viable "in some circumstances," late bookings "not necessarily" prevented, but specimen type/storage always need considering); added the WDP start-time guidance row (supersedes PathWest sourcing); added the WDP commercial/rental-structure row (no figure exists); added a CRITICAL flag in §4 and §7 that the entire AM Direct Labor figure (A$48,255/month) is contingent on an unresolved phlebotomist employment-model question (in-house vs WDP-supplied) — explicitly NOT DECIDED per Anthony, no P&L figure changed over this.

*Eight settled items:* (1) trading days (Mon-Fri + Saturday) marked settled, fixed a stale "should Saturday be actively planned" open question in `strategic-concerns-growth.md`; (2) hiring model (cross-qualified casuals, review for part-time conversion) added to §4; (3) downtime-fill/early-release corrected from one blended figure to two separate pools — independently re-derived 420 min/day (between-gaps) and 1,320 min/day (naive lead+tail), reconciled exactly against the earlier 1,260 min/day total (window-width difference, fully explained); (4) 3-hour minimum casual engagement checked directly against the primary Fair Work Ombudsman/Commission award text via WebFetch (MA000005 clause 11.5, MA000027 clause 11.2) — `[VERIFIED]`, not just accepted from a claim, applied to reduce the lead+tail saveable pool to 1,100 min/day; (5) PM package direction confirmed (pricing still pending); (6) ancillary revenue excluded entirely from every baseline figure in §5, kept as a separate upside line in `profit-loss-tables.md`; (7) flagged the orphaned local clone at `C:\Users\azed9\Documents\GitHub\gtt-center-perth` (new §9) — diverged, do-not-edit, do-not-delete-without-asking-Anthony; (8) re-ran the treatment-headcount scheduling solver with a hypothetical Nails+Hair cross-qualification pool — result: 6 staff possible (down from 7), solver-verified, hireability caveat flagged (§4).

**2026-07-30 (later same day — 6th-slot solver check + Chair B policy, per Anthony's direct instruction)** — Priority item: re-ran the scheduling solver (extended `sync-treatment-solver.py` method, not hand arithmetic) against WDP's actual 10:30am start-time guidance, testing whether a 6th client/chair (12/day total) clears treatment-staff concurrency, not just draw timing. **Result: yes, at the original 8-staff (no-pooling) baseline — last Draw 1 10:20am, zero concurrency violations, zero phlebotomist/chair collisions (independently re-verified, not assumed from the 10-client pattern). But the 7-staff and 6-staff pooling reductions verified 2026-07-29 do NOT hold at 12 clients/day — both fail.** Added to §1. Also added the Chair B enquiry-threshold opening policy (Chair A default/guaranteed, Chair B opens only on a 2nd enquiry for the same slot) with its hand-derived (not solver-verified, flagged as such) ~A$306 cost-to-open and 2-client break-even — see `ivy-booking-system.md` for the full booking-flow update.

**2026-07-30 (correction, later still — 12 clients/day is now the COMMITTED model, not a "maybe later" ceiling)** — Anthony corrected the framing of the prior entry: 12 clients/day (using the extended morning already solver-verified above) is the new committed AM operating volume, replacing 10-client Scenario C as current. Updated: §1 (committed model, corrected shift-boundary source — `financial-break-even-staff.md`'s 07:00-13:00, not `operations-manual.md`'s 12:30 EOD-wrap, which was the wrong source used for the 10-client downtime calc); §3 (capacity ceiling 264/month, was 220); §4 (headcount confirmed at 8, no pooling — the 2026-07-29 7-staff/6-staff findings explicitly marked superseded, applied only to the now-historical 10-client model); §5 (Monthly Net P&L +A$28,488.42/month, was +A$16,507.07/month — AM Direct Labor recomputed fresh via FTE reasoning, confirmed unchanged at A$48,255/month since headcount is unchanged and the extended day still fits the existing shift budget); §7 (new second delta table, 10→12, AM segment contribution +A$17,745/month, was +A$6,745/month); §8 (both downtime-fill pools recomputed against the actual 12-client gap pattern, not carried over — A$12,679.33/month and A$16,511.22/month, both up from the 10-client figures). **Flagged, not resolved:** whether the Chair B enquiry-threshold policy still makes sense now that both-chairs-synchronized-at-12/day is the committed baseline — added to §1 as an explicit open question for Anthony, not guessed at.
