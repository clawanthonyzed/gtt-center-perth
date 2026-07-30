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
| AM GTT capacity ceiling | 10 clients/day | `[VERIFIED — scenario-c-sync-timetables.md, 2026-07-17, programmatic zero-double-booking simulation across 2 phlebotomists + 8 treatment staff]`. This verifies **scheduling feasibility**, not booking demand — it is a ceiling, not a guarantee that 10 clients/day will actually be sold. |
| AM start time | 07:00, synchronized dual-chair start | `[VERIFIED — same source]` |
| Chairs / phlebotomists | 2 chairs, 2 phlebotomists | `[VERIFIED — same source]` |
| Operating days | **Settled 2026-07-30:** AM runs Mon-Fri AND Saturday (6 days); PM Mon-Fri + Sat bolt-on; Sunday closed | `[VERIFIED — Anthony's direct instruction, 2026-07-30 — Saturday trading is settled, not deferred]`. Sunday's conditional reopening remains `[MODELED — assumption: Sunday reopens only once standalone PM demand is proven and profitable; a business choice, not a legal requirement per WA Retail Trading Hours Act exemption — am-capacity-weekend.md]` |
| WDP specimen dispatch cutoff | **Conditional, not a blanket "no cutoff"** — overnight storage viable "in some circumstances" (fluoride oxalate tubes stable ~24hrs); a late booking "would not necessarily prevent collection, although specimen type and storage requirements would always need to be considered" | `[VERIFIED — Carole Rivers, WDP, email, 2026-07-30]`. **Corrected 2026-07-30** — the earlier 2026-07-29 verbal readback oversimplified this into a blanket "no cutoff," which was wrong; this is real, written, primary-source correspondence, but conditional, not unconditional. Not yet actioned into any scheduling document — exact storage/handling conditions with WDP still need to be nailed down before re-running the capacity model on an assumption of a wider window. See `cutoff-time-CORRECTION.md`. |
| WDP GTT start-time guidance | "Would not normally commence a GTT after 10:30am" (exceptions for shift workers etc.) — supersedes the earlier PathWest-sourced "preferably before 10am" | `[VERIFIED — Carole Rivers, WDP, email, 2026-07-30]`. Scenario C's last Draw 1 (09:40) clears this with 50 minutes to spare — see `king-edward-start-time-constraint.md`. |
| WDP commercial/rental structure | Annual rental arrangement, terms depend on pathology volume, referring-doctor count on-site, location/accessibility, business opportunity — **no figure quantified anywhere** | `[PLACEHOLDER — not yet known]`. Owner: Anthony/WDP commercial negotiation. Do not invent a rental estimate. See `docs/VERIFICATION-TRACKER.md`. |
| Growth path (not committed) | Scenario D, 15 clients/day, 3rd phlebotomist/chair | `[MODELED — am-capacity-weekend.md, scenario-d-investigation.md; provisional on the WDP cutoff answer above]` |
| Growth path — 6th slot/chair (12 clients/day), solver-checked 2026-07-30 | **Clears cleanly at the current 8-staff (no-pooling) baseline** — last Draw 1 10:20am (inside WDP's "not normally after 10:30am" guidance, 10min margin), last departure ~12:48pm (vs ~12:08-12:25pm at 10 clients — a real ~25-40min extension to the AM day). Massage/Beauty/Nails/Hair each still peak at exactly 2 concurrent, same as the 10-client model — no headcount increase above the original 8. **But the Massage+Beauty (7-staff) and Nails+Hair (6-staff) pooling reductions from 2026-07-29 do NOT hold at 12 clients/day — both fail (specific clients unassignable).** Phlebotomist/chair side re-verified zero-collision at 12 clients (not assumed from the 10-client pattern). | `[VERIFIED — solver result (extended sync-treatment-solver.py method), scenario timing rules, checked 2026-07-30]`. Not yet a committed model — this answers "does it schedule," not "should we do it" (referral pipeline, WDP volume/rental terms, and departure-time extension all still need Anthony's sign-off before quoting 12/day to WDP). |
| Chair B opening policy — settled 2026-07-30 | Chair A is the default/guaranteed chair per slot. **Chair B opens only once 2 enquiries exist for the same slot** — not automatically alongside Chair A. First enquiry confirms immediately on Chair A; 2nd enquiry triggers Chair B (its own phlebotomist + matching treatment lines) and both convert to confirmed bookings. | `[VERIFIED — Anthony's direct instruction, 2026-07-30]` — see `ivy-booking-system.md` Chair B Opening Policy section. Cost consequence: ~A$306 unavoidable added cost when Chair B opens at all (1 phlebotomist + 2 treatment staff at the 3-hour minimum engagement floor, Nails+Hair pairing) — `[MODELED — hand-derived from confirmed award rates, not solver-verified, directionally right not exact]`. Break-even: 1 Chair B client doesn't clear it (~-A$56), 2 does (~+A$194) — consistent with the 2-enquiry trigger. |
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
| AM GTT capacity ceiling | 220 visits/month (10/day × 22 trading days) | `[VERIFIED capacity]` + `[MODELED — depends on referral pipeline filling all 10 daily slots; not a revenue guarantee]` |
| AM GTT weekly ceiling (6-day week incl. Saturday) | 60 slots/week | `[MODELED — derived: 10/day × 6 days]` |
| Perth metro GTT tests/week (addressable market) | ~277/week | `[MODELED — research.md ABS/AIHW-derived estimate, not primary market research]` |
| Share of addressable market at full AM capacity | ~22% (6-day operating week) | `[MODELED — derived from the two rows above; business-plan.md flags this has not been re-run against every underlying assumption]` |
| PM individual services capacity (steady state) | ~16 sessions/day (~350/month) | `[MODELED — assumption: ~50% utilisation of theoretical 4-line capacity, pm-staffing-roster.md; no real demand data exists yet]` |

---

## 4. Headcount

| Role | Qty | Tag |
|---|---|---|
| Venue Manager (Managing Director) | 1 — new hire, not yet in place | `[PLACEHOLDER — critical-path hire, recruitment gated on securing a physical venue location, not yet begun]` |
| Phlebotomist (AM only, Chair A / Chair B) | 2 | `[MODELED — financial-break-even-staff.md award-rate structure]`. **CRITICAL OPEN DEPENDENCY (flagged 2026-07-30):** this entire row, and the ~A$48,255/month AM Direct Labor figure it feeds into (§7 below), assumes GTT Center Perth employs its own phlebotomist(s) directly — the current modelled baseline. Carole Rivers' 2026-07-30 email raises a real possibility that under WDP's rental-clinic model, WDP supplies/employs the phlebotomist instead (their email: phlebotomist "safety, wellbeing and employment responsibilities... would remain with Western Diagnostic Pathology"), which would replace this wage line with a to-be-negotiated rental fee. **Anthony's explicit answer: NOT DECIDED — needs to ask Carole directly.** Do not treat the current in-house figure as settled once this is answered — it may change materially. `[PLACEHOLDER — critical, high-priority, see docs/VERIFICATION-TRACKER.md]` |
| AM treatment staff (Massage, Nail, Hair, Beauty) | **7 or 8 — not yet decided** | `[MODELED — 8 is the traceable payroll-table baseline; profit-loss-tables.md's Treatment Headcount analysis confirms 7 is the genuine minimum via Massage+Beauty cross-training at the current 10-client volume, but adopting 7 is an unactioned operational hiring decision for the Venue Manager]` |
| Receptionist / Manager (split shift) | 1 | `[MODELED]` |
| PM dedicated casual roster (1 each: massage, hair, nail, beauty) | 4 | `[MODELED — pm-staffing-roster.md, hours-based costing, not a flat FTE headcount]` |
| Casual Relief Pool | Budget line, not a fixed headcount | `[MODELED — A$15,000/yr budgeted]` |
| **Total heads (AM 8-staff baseline + PM + relief pool structure)** | **~16-17** | `[MODELED — sum of above]` |
| Possible combined AM/PM rotating pool (2026-07-28 proposal) | Potentially fewer than 11 total treatment/PM heads across both shifts | `[PLACEHOLDER — dual-role-staffing-model-2026-07-28.md v3.0 explicitly states this is "not booked as a confirmed saving," pending real roster data]` |
| Hiring model | **Settled 2026-07-30:** cross-qualified hires where trades allow (Massage+Beauty dual-Cert-IV pairing, per `profit-loss-tables.md`'s Treatment Headcount section). All service staff hired as casuals initially; reviewed for conversion to part-time once regular, proven hours exist per role (matches `pm-staffing-roster.md`'s existing "casual for first 3-6 months, review conversion at Month 3-6" policy). | `[VERIFIED — Anthony's direct instruction, 2026-07-30]` |
| Possible Nails+Hair cross-qualification (solver-checked 2026-07-30) | Would bring combined treatment headcount to 6 (down from 7) — Massage+Beauty pool peaks at 3, Nails+Hair pool (if also pooled) peaks at 3, per direct re-run of the scheduling solver against the real Scenario C timetable | `[VERIFIED — solver result, scenario-c-sync-timetables.md booking data, checked 2026-07-30]` for the scheduling-feasibility number itself. `[PLACEHOLDER — hireability]`: a genuine Nails+Hair dual-qualified hire is NOT the same easy find as Massage+Beauty — Nail Technology (Cert II/III) and Hairdressing (Cert III apprenticeship) are separate trade pathways with no natural training overlap (`am-capacity-weekend.md`'s Multi-Role Relief Hiring section already flags this). This is a scheduling-feasibility answer, not a claim that such a hire is readily recruitable. |

---

## 5. Monthly Net P&L

> **2026-07-30 — ancillary revenue excluded from every figure below, per Anthony's direct instruction ("too much of a variable" with no real basis yet).** Every figure in this section is now A$8,580/month lower than it was before 2026-07-30. Ancillary is kept visible only as a separate pure-upside line — see `profit-loss-tables.md`'s "Ancillary Revenue — Excluded From Baseline" section. Do not fold it back into any figure below.

| Period | Figure | Tag |
|---|---|---|
| Month 1 (ramp) | ~-A$46,907/month (unaffected — ancillary was already excluded from this ramp-month figure's own build) | `[MODELED — cash-flow.md v2.0, ramp-percentage assumption applied to current steady-state ceilings]` |
| Month 2 | ~-A$26,532/month | `[MODELED — same basis]` |
| Month 3 | ~-A$11,979/month | `[MODELED — same basis]` |
| Month 4 | ~+A$1,603/month | `[MODELED — same basis; marginally profitable]` |
| Month 5+ (steady state, precise weekday/Saturday-blended calculation) | **+A$16,507.07/month** (was +A$25,087.07/month before ancillary exclusion) | `[MODELED — profit-loss-tables.md v2.1, 2026-07-30 ancillary-excluded recalculation; the underlying calculation is fully traceable for every revenue/overhead/workers-comp line, but the AM Direct Labor exact per-staff-member hour allocation is not preserved as a saved worksheet — see that document's own Appendix]` |
| Month 5+ (simplified ramp-table sum — do not quote as headline) | ~-A$185.09/month (was ~+A$8,395/month before ancillary exclusion) | `[MODELED — same source, a rounding/methodology artifact of the simpler ramp table, not a competing figure — profit-loss-tables.md discloses this explicitly]` |
| Year 1 (ramp-matched estimate) | Likely in the range of a modest loss to modestly positive, roughly -A$20,000 to +A$5,000 (flat-cost approximation shows ~-A$105,381 but is known to understate profitability — was ~-A$13,000 before ancillary exclusion) | `[MODELED — profit-loss-tables.md Years 1-3 Annual Projection, disclosed as a known simplification, not a confident forecast]` |
| Year 2-3 (steady state, no further capacity growth) | ~+A$198,084.84/year (was ~+A$301,044.84/year before ancillary exclusion) | `[MODELED — same source; "no growth" placeholder if Scenario D is not activated]` |

**None of the above is based on real trading data — there is no venue open yet.**

**Also not included in any figure above:** the Between-Client Downtime-Fill Revenue (A$9,509.50/month) and Early-Release Cost Saving (A$14,647.05/month) — see §8 below.

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

---

## 8. Downtime-Fill Revenue & Early-Release Saving — Two Separate Tagged Pools (Corrected 2026-07-30)

> **Corrected 2026-07-30, later the same day — this section previously showed one blended figure (A$28,528.50/month from a claimed 1,260 min/day total). Anthony corrected this: between-booking gaps and lead-in/tail time are two different pools with two different treatments, and must not be blended.**

**Policy (permanent, not ramp-up-only):**
- **Between-client gaps** (mid-shift, strictly between two of a staff member's own bookings) — fillable with standalone/non-GTT bookings **made in advance online only** (not walk-in, not day-of). This is the only pool that generates revenue.
- **Lead-in/tail** (before a staff member's first booking, or after their last, that day) — NOT sellable. That staff member's engagement starts later or ends earlier instead — a cost saving, subject to the 3-hour minimum casual engagement.

Both per `financial-break-even-staff.md`'s Staff Downtime Protocol (updated 2026-07-30) and `pm-staffing-roster.md`'s Booking-Driven Rostering Policy (permanent, not ramp-up-only).

**Independently re-derived minute totals** (walked directly from `scenario-c-sync-timetables.md` §2, per staff member, using a 07:00-12:30 nominal shift boundary sourced from `operations-manual.md`'s own Daily Operations Cadence):

| Item | Value | Tag |
|---|---|---|
| Between-booking gaps (pool a), all 8 AM treatment staff | 420 min/day = 7.0 staff-hours | `[VERIFIED — scenario-c-sync-timetables.md §2, walked directly per staff member; not estimated]` |
| Lead-in + tail (pool b), naive/unconstrained | 1,320 min/day | `[VERIFIED — same source]` |
| Lead-in + tail (pool b), SAVEABLE after the 3-hour minimum engagement floor | 1,100 min/day | `[MODELED — 4 of 8 staff (those with only 2 bookings/day) cannot trim to their natural ~125-min span without breaching the 3hr floor; 55 min/person retained as mandatory buffer]` |
| **(a) Between-Client Downtime-Fill Revenue (headline)** | **A$9,509.50/month** | `[MODELED — assumption: 50% utilisation, same discount factor as standalone PM demand elsewhere in this repo; throughput 1.3 sessions/hr and A$95/session average reused from pm-staffing-roster.md]` |
| **(b) Early-Release Cost Saving (headline)** | **A$14,647.05/month** | `[MODELED — assumption: staggered per-person engagement start/end times, subject to the 3hr floor; wage rates from financial-break-even-staff.md, traceable]` |
| 3-hour minimum casual engagement (constraint applied above) | MA000005 clause 11.5, MA000027 clause 11.2 | `[VERIFIED — Fair Work Ombudsman/Fair Work Commission, checked via direct WebFetch against awards.fairwork.gov.au, 2026-07-30]` |

**Reconciliation against the earlier (same-day) 1,260 min/day figure:** that figure used a narrower, shared 07:15-11:45 (270 min) window per staff and didn't distinguish the two pools. The new split uses a wider, sourced 07:00-12:30 (330 min) boundary; 420+1,320=1,740 min/day, and 1,740-1,260=480 min = exactly 60 min/staff × 8 staff (the window-width difference) — fully reconciled, not a mystery.

**Neither (a) nor (b) is included in §5's +A$16,507.07/month baseline — both are separate, tagged lines, and are not blended with each other either.** Full derivation, per-staff breakdown, and caveats in `profit-loss-tables.md`'s "Downtime-Fill Revenue & Early-Release Saving" section. Treat both as planning-conversation figures, not inputs to cash-flow or break-even calculations.

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
