# GTT Center Perth — Roadmap & Next Steps

**Compiled:** 2026-07-19 | **Compiled by:** Grace (Operations Manager, audit pass)
**Status:** PRIMARY DELIVERABLE of this session's audit/consolidation pass.
**Purpose:** Prioritised action list bringing together this session's findings (`00_document_inventory.md`, `01_conflicts_log.md`, `02_issues_and_risks.md`, `03_improvements.md`) into one execution-ready roadmap. No fixed launch date — sequence is by dependency only, per standing instruction.

---

## How to Read This Roadmap

Actions are grouped by **dependency tier**, not calendar date (no launch date is set). Within each tier, items are ordered by severity/leverage. Founder-only decisions are marked and cross-referenced to `05_open_questions_for_founder.md` — do not attempt to resolve those without Anthony's input.

---

## TIER 0 — Blocking Gates (Nothing Else Should Proceed Confidently Without These)

> **Note (2026-07-19):** DVA/TPI pension advice is Anthony's personal matter, handled by him directly — it is not a GTT Center Perth task and is not listed in this roadmap (removed per direct instruction, stated twice). See `docs/05_open_questions_for_founder.md` for the removal note.

| # | Action | Why it blocks | Owner | Ref |
|---|---|---|---|---|
| 1 | **Confirm WDP courier/specimen cutoff time directly with WDP** | Every AM capacity figure above 8 clients/day (i.e. the entire Scenario C model, +25% revenue capacity vs Scenario B) rests on an unconfirmed number (11:30 vs 12:30, neither sourced). Cheapest, highest-leverage open item in the corpus. WDP emailed 2026-07-19, awaiting reply — see `cutoff-time-CORRECTION.md`. | Reed (partnerships agent), approved by Anthony | `cutoff-time-CORRECTION.md`, H2 in `02_issues_and_risks.md` |
| 2 | **Secure a physical venue location** | Nothing else on the critical path (Venue Manager recruitment, fit-out, staff hiring) starts until a location is confirmed — per Anthony's direct instruction (2026-07-19): GTT Center Perth is not recruiting or looking for staff, including the Venue Manager, until a physical location is sorted. This is now the actual first blocking gate, ahead of any hiring action. | Anthony | `location-scouting.md`, Tier 1 #6 |
| 3 | **Venue Manager recruitment — critical-path hire, starts only after location is confirmed** | Venue cannot safely open without this role — first-aid/EpiPen holder, fire warden, clinical escalation contact, staff supervisor, day-to-day payment approver. Recruitment document now built and ready (`docs/venue-manager-job-posting.md`) but **not to be posted/actioned until Tier 0 #2 (location) is resolved** — do not imply active recruitment before then. | Anthony/Grace (once location confirmed) | `staff-plan.md` §7, `hr-framework.md` §13, `docs/venue-manager-job-posting.md`, M1 in `02_issues_and_risks.md` |
| 4 | **Source-verify or formally confirm the King Edward Hospital "start before 10am" guidance** | Currently sourced only as general internet research, not a specific document (clarified 2026-07-19 — see `king-edward-start-time-constraint.md`). Scenario C passes; Scenario D (growth scenario) fails on a strict reading. Needed before Scenario D can be treated as a real option. | Anthony/Reed | `king-edward-start-time-constraint.md`, H3 |

---

## TIER 1 — Documentation Fixes Needed Before Staff Training / Onboarding

These don't block the business commercially but **must be fixed before any new staff member is trained off these documents**, since they currently contain wrong operational numbers.

| # | Action | Detail | Ref |
|---|---|---|---|
| 5 | **Rewrite `operations-manual.md`'s GTT Scheduling Timetables section** | Replace the Scenario B (8-client) tables with the Scenario C sync (10-client) tables from `scenario-c-sync-timetables.md`. This is the single most important documentation fix from this session — flagged with a superseded banner, not yet rewritten. | H1, CONFLICT-03 |
| 6 | ~~Build a Venue Manager job posting/recruitment document~~ **DONE 2026-07-19** | `docs/venue-manager-job-posting.md` created, using `phlebotomist-job-posting.md` as a structural template. **This is a document to have ready, not to post yet** — do not action recruitment until Tier 0 #2 (location) is resolved. | M1, O1 |
| 7 | **Rewrite `workflow.md`'s staffing model table** | Currently describes a sublet/subtenant model that contradicts the confirmed employed-staff, no-subtenant model everywhere else. Also still lists a "keepsake scan operator" role removed from scope entirely at Day 51. | M2, CONFLICT-04 |
| 8 | **Verify and flag `scenario-c-timeline.html`** | Likely superseded by `scenario-c-sync-timeline.html` (same relationship as the staggered vs sync markdown tables) but not confirmed this session. | M6 |

---

## TIER 2 — Verification Sweep (No Known Issue, But Not Actively Checked This Session)

| # | Action | Detail | Ref |
|---|---|---|---|
| 9 | **Follow-up review of ~10 "not reviewed this pass" documents** | `equipment-costs.md`, `hire-purchase-china.md`, `gtt-test-reference.md`, `consent-form.md`, `privacy-policy.md`, `market-research-findings.md`, `ivy-booking-system.md`, `extended-wellness-services.md`, `reed-partnerships.md`, `onboarding.md`, `staff-profiles/*.md`. Check specifically for stale Scenario B references and any other Imara operational references missed by the Priority 0 file list. | M5 |
| 10 | **Confirm no patient-facing materials reference "8 clients" or a 07:40-based schedule** | SMS templates, confirmation emails, website copy — not checked this session for Scenario B/C consistency. | Follow-up from CONFLICT-03 |
| 11 | **MA000027 Saturday phlebotomist ordinary-hours carve-out** | Confirm with payroll advisor or Fair Work directly. Upside risk only (potential cost saving currently modelled conservatively as full penalty rate). | M3 |

---

## TIER 3 — Process Improvements (Ongoing, Not One-Time)

See `03_improvements.md` for full detail. Summary:

| # | Improvement | Ref |
|---|---|---|
| 12 | Create a single "current operational model" pointer document (client volume, pricing, headcount) that everything else references | P1 |
| 13 | Apply rename-or-flag discipline consistently when superseding any document (especially non-markdown/visual files) | P2 |
| 14 | Keep `reading-order.md` in sync with `00_document_inventory.md` — audit periodically | P3 |
| 15 | Add version/date banners to any file still missing them (starting with `workflow.md`) | P4 |
| 16 | Continue using `05_open_questions_for_founder.md` as the single running list for all future founder-only questions | P5 |

---

## TIER 4 — Founder Decisions Required Before Further Progress

**Do not guess at these. See `05_open_questions_for_founder.md` for the complete, single-source list.** Summary of what's blocking what:

- WDP cutoff confirmation (Tier 0 #1) — blocks confidently committing to Scenario C/D capacity. WDP emailed, awaiting reply.
- Physical venue location (Tier 0 #2) — blocks Venue Manager recruitment and every downstream hiring/fit-out action. Per Anthony's direct instruction (2026-07-19), no staff recruitment (including Venue Manager) starts until this is resolved.
- King Edward guidance sourcing (Tier 0 #4) — blocks Scenario D (growth scenario) being treated as fully reliable; clarified as general internet research, not a specific document.
- Package price-increase timing (Month 3 vs 4, or "once at capacity") — not blocking, supported by `docs/price-increase-comparison.md`.

**Not listed here:** DVA/TPI pension advice is Anthony's personal matter, not a GTT Center Perth task — removed from this roadmap per his direct instruction (stated twice). MA000027 Saturday carve-out has been investigated and documented (see `hr-framework.md`) — a genuine capability gap was flagged (no live web-fetch tool this session to verify current award text), not left as an open founder question.

---

## What This Session Did NOT Do (Explicitly Out of Scope)

- Did not set a launch date (per standing instruction — sequence by dependency only).
- Did not re-litigate any of the "already resolved" items listed in the task brief (launch date, funding source, AM model choice of Scenario C, package structure, Saturday/Sunday model).
- Did not delete any file — all supersessions were handled via banners/flags, preserving history.
- Did not rewrite `operations-manual.md`'s timetables or `workflow.md`'s staffing table — still flagged as Tier 1 priority actions, not completed, because each is a substantial standalone editorial task.
- Did not imply Venue Manager recruitment is starting now — per Anthony's direct instruction (2026-07-19), no staff recruitment happens until a physical location is confirmed. The job posting document (Tier 1 #6) was built so it is ready, not to signal active recruitment.
- Did not touch `financial-model.md`, `dva-tpi-research.md`, or `research.md` — explicitly out of scope per task instruction (these cover trust/ownership structure, not day-to-day ops).
- Does not list DVA/TPI advice anywhere in this roadmap — Anthony's personal matter, not a GTT task, removed per his direct instruction (stated twice).

---

## Recommended Order for the Next Working Session

1. Tier 0 #1 (WDP cutoff call) — cheapest, highest leverage, unblocks confidence in the whole Scenario C model. Already in progress (emailed, awaiting reply).
2. Tier 0 #2 (secure a physical venue location) — this is now the actual gating item before any hiring action, including the Venue Manager. Nothing in Tier 0 #3 starts before this.
3. Tier 1 #5 (rewrite operations-manual.md timetables) — now safe to do properly once Tier 0 #1 confirms the real cutoff time (avoids rewriting twice if the cutoff changes the schedule). Independent of the location gate — can proceed in parallel.
4. Tier 0 #3 (Venue Manager recruitment) — begins only once Tier 0 #2 (location) is resolved. The job posting document is ready (Tier 1 #6, done).
5. Tier 0 #4, Tier 1 #7-8, Tier 2, Tier 3 — as capacity allows, no strict dependency order among these.

---

## Changelog

**2026-07-19 (founder feedback round 2)** — Removed DVA/TPI adviser consultation entirely from this roadmap (was Tier 0 #2) per Anthony's direct instruction, stated twice: this is his personal matter, not a GTT Center Perth task. Replaced Tier 0 #2 with "secure a physical venue location" — the actual gating item before any staff recruitment, including the Venue Manager, per Anthony's confirmation that GTT Center Perth is not recruiting/looking for staff until a location is sorted. Updated Tier 0 #3 (Venue Manager recruitment) to explicitly not start until location is confirmed. Marked Tier 1 #6 (Venue Manager job posting) as done — `docs/venue-manager-job-posting.md` built as a ready-to-use document, not an active posting. Updated the recommended order and "did not do" sections to match.
