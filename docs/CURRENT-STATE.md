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
| Operating days | Mon-Sat AM (6 days), PM Mon-Fri + Sat bolt-on, Sunday closed | `[MODELED — assumption: Sunday reopens only once standalone PM demand is proven and profitable; a business choice, not a legal requirement per WA Retail Trading Hours Act exemption — am-capacity-weekend.md]` |
| WDP specimen dispatch cutoff | No cutoff within business operating hours (per WDP) — supersedes the earlier 11:30/12:30 conflict | `[VERIFIED — Carole Rivers, WDP, verbal confirmation, 2026-07-29]`. **Verbal only, not yet in writing — do not treat as fully closed out.** Standing action item: get this in writing/email for the permanent record (see `docs/VERIFICATION-TRACKER.md` item 1, `cutoff-time-CORRECTION.md`). Not yet actioned into any scheduling document — the AM/PM capacity ceiling above still uses the original courier-cutoff-constrained schedule until the written confirmation lands and the schedulers are re-run. |
| Growth path (not committed) | Scenario D, 15 clients/day, 3rd phlebotomist/chair | `[MODELED — am-capacity-weekend.md, scenario-d-investigation.md; provisional on the WDP cutoff answer above]` |

---

## 2. Package Prices

| Item | Value | Tag |
|---|---|---|
| Package 1 (fixed 2×30-min services) | A$250 | `[MODELED — assumption: Anthony's locked launch price, services-pricing-locked.md renumbered 2026-07-20; not externally market-tested]` |
| Package 2 (flexible: 2×45min, or 1×45+1×30min, or 2×30min) | A$300 | `[MODELED — same basis]` |
| AM revenue calculations use which price | A$250 (Package 1) as a deliberate conservative safety price, not a blended average | `[MODELED — standing instruction, not a re-derivation]` |
| PM individual a-la-carte average | ~A$95/session | `[MODELED — assumption: pm-staffing-roster.md planning estimate, no real booking data]` |
| PM set/fixed packages | Proposed, not yet priced | `[PLACEHOLDER — pm-package-structure.md, requires Anthony's sign-off]` |

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
| Phlebotomist (AM only, Chair A / Chair B) | 2 | `[MODELED — financial-break-even-staff.md award-rate structure]` |
| AM treatment staff (Massage, Nail, Hair, Beauty) | **7 or 8 — not yet decided** | `[MODELED — 8 is the traceable payroll-table baseline; profit-loss-tables.md's Treatment Headcount analysis confirms 7 is the genuine minimum via Massage+Beauty cross-training at the current 10-client volume, but adopting 7 is an unactioned operational hiring decision for the Venue Manager]` |
| Receptionist / Manager (split shift) | 1 | `[MODELED]` |
| PM dedicated casual roster (1 each: massage, hair, nail, beauty) | 4 | `[MODELED — pm-staffing-roster.md, hours-based costing, not a flat FTE headcount]` |
| Casual Relief Pool | Budget line, not a fixed headcount | `[MODELED — A$15,000/yr budgeted]` |
| **Total heads (AM 8-staff baseline + PM + relief pool structure)** | **~16-17** | `[MODELED — sum of above]` |
| Possible combined AM/PM rotating pool (2026-07-28 proposal) | Potentially fewer than 11 total treatment/PM heads across both shifts | `[PLACEHOLDER — dual-role-staffing-model-2026-07-28.md v3.0 explicitly states this is "not booked as a confirmed saving," pending real roster data]` |

---

## 5. Monthly Net P&L

| Period | Figure | Tag |
|---|---|---|
| Month 1 (ramp) | ~-A$46,907/month | `[MODELED — cash-flow.md v2.0, ramp-percentage assumption applied to current steady-state ceilings]` |
| Month 2 | ~-A$26,532/month | `[MODELED — same basis]` |
| Month 3 | ~-A$11,979/month | `[MODELED — same basis]` |
| Month 4 | ~+A$1,603/month | `[MODELED — same basis; marginally profitable]` |
| Month 5+ (steady state, precise weekday/Saturday-blended calculation) | **+A$25,087.07/month** | `[MODELED — profit-loss-tables.md v2.1, 2026-07-20; the calculation is fully traceable for every revenue/overhead/workers-comp line, but the AM Direct Labor exact per-staff-member hour allocation is not preserved as a saved worksheet — see that document's own Appendix]` |
| Month 5+ (simplified ramp-table sum — do not quote as headline) | ~+A$8,395/month | `[MODELED — same source, a rounding/methodology artifact of the simpler ramp table, not a competing figure — profit-loss-tables.md discloses this explicitly]` |
| Year 1 (ramp-matched estimate) | Likely breakeven-to-+A$25,000-40,000 (flat-cost approximation shows ~-A$13,000 but is known to understate profitability) | `[MODELED — profit-loss-tables.md Years 1-3 Annual Projection, disclosed as a known simplification, not a confident forecast]` |
| Year 2-3 (steady state, no further capacity growth) | ~+A$301,044.84/year | `[MODELED — same source; "no growth" placeholder if Scenario D is not activated]` |

**None of the above is based on real trading data — there is no venue open yet.**

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

**Bottom line:** the AM segment can be presented as profitable on a standalone direct-labor basis (+A$6,745/month) using figures already fully traceable in this repo — but this is the 12-day-old Scenario C correction reaching a table that was overlooked, not a new finding. `pm-staffing-roster.md` has been corrected to match (see that document's 2026-07-29 changelog entry). This does not change the venture-level headline figure (+A$25,087.07/month), which already incorporated the Scenario C AM revenue correctly since 2026-07-20 — only this one segment-level table was stale.

---

## 8. How to Use This File

- Every document in `docs/` that states a package price, client capacity, headcount, monthly P&L figure, or startup capital range should point here, not restate the figure as its own independent source.
- Run `python tools/check_consistency.py` before quoting any figure externally (investor conversation, lease negotiation, staff training) — it greps every `docs/*.md` file for values that contradict this file.
- When a figure changes here, it does not need to be manually propagated to every other document — those documents should already be pointing here. If you find one that restates a figure independently, add a pointer instead of a second copy.
- See `docs/VERIFICATION-TRACKER.md` for every unconfirmed fact and who can confirm it.

---

## Changelog

**2026-07-29 (created)** — Built in response to an outside review that found the financial model had moved 5+ times with contradicting numbers across documents, false precision on a pre-revenue business, and at least one document (`operations-manual.md`) still training staff on an abandoned model 10 days after being flagged. This file is the process fix, not just a numbers fix — see `rules/CLAUDE.md` for the accompanying hard rule requiring every future figure to carry a tag from this system.

**2026-07-29 (later same session — follow-up corrections from Anthony)** — Two direct corrections applied: (1) the WDP specimen-pickup cutoff row in §1 updated from `[PLACEHOLDER]` to `[VERIFIED — Carole Rivers, WDP, verbal confirmation, 2026-07-29]` — no cutoff exists within business operating hours, per WDP, but this is verbal only and not yet in writing; kept as an open action item in `docs/VERIFICATION-TRACKER.md`, not closed out. (2) Confirmed no funding-source wording errors exist in this file (checked directly) — the "Imara's personal savings" wording error found in 6 other documents this session (`CLAUDE.md`, `executive-summary.md`, `gtt-center-perth-overview-for-imara.md`, `revenue-extraction-options.md`, `risk-register.md`, `swot-analysis.md`, `team-startup.md`, `financial-model.md`) does not appear here since this file never described the funding source. Also: `financial-model.md` was opened and split this session (not left "untouched") — see that document's own changelog; its trust/tax content is separate from this file's scope and not duplicated here.
