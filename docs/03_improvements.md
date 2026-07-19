# GTT Center Perth — Improvement Suggestions

**Compiled:** 2026-07-19 | **Compiled by:** Grace (Operations Manager, audit pass)
**Purpose:** Process and documentation improvements suggested by this session's audit, distinct from `02_issues_and_risks.md` (which lists gaps/risks) — this document focuses on how the corpus is maintained going forward, plus a few substantive operational suggestions.

---

## Documentation Process Improvements

### P1. Adopt a Single "Current Operational Model" Pointer Document
The Scenario B/C conflict (see `01_conflicts_log.md` CONFLICT-03) happened because the capacity/scheduling model changed but the full timetable tables in `operations-manual.md`, `staff-plan.md`, and `gtt-clinical-protocol.md` weren't all updated at once. `HANDOFF.md` already does a good job of this for the most recent session, but it's a session-handoff document, not a permanent fixture.

**Suggestion:** Create one short, permanent "current model" document (e.g. `CURRENT-MODEL.md`) at the top of the reading order, containing only the handful of numbers that change most often — client volume/scenario, package pricing, operating days, current headcount — each with a one-line pointer to its full detail document. Every other document references *this* file's numbers rather than restating them. When the model changes, only this one file needs an update to keep everything else honest, even if the full detail rewrite in `operations-manual.md` etc. lags behind by a few days.

### P2. Rename-or-Delete Discipline for Superseded Files
Both duplicate/stale-file conflicts found this session (`research-supplement-day48.md`, `floor-plan-visual.*`) happened because a newer version was created without the older version being renamed, flagged, or removed. The `-ARCHIVED` suffix convention already exists and works well (see `research-supplement-day48-ARCHIVED.md`, `inhouse-gtt-research.md`) — it just wasn't applied consistently.

**Suggestion:** When creating a v2/v3 of any document (especially visual/binary files like floor plans, which can't carry an inline banner as easily as markdown), immediately either (a) rename the old version with a `-SUPERSEDED` or `-ARCHIVED` suffix, or (b) add an entry to `reading-order.md`'s Reference Only table in the same commit. Treat this as part of "done," not a follow-up task.

### P3. Reading-Order.md Should List Every File
This session found that `floor-plan-*` files (4 of them) weren't listed in `reading-order.md` at all — neither as required reading nor reference-only. A document that isn't listed anywhere gives no signal about its currency to a new reader.

**Suggestion:** Audit `reading-order.md` against `00_document_inventory.md` (created this session) periodically and add any missing files. The inventory doc can serve as the master checklist for this.

### P4. Version/Date Banner on Every File
Most documents have a `**Version:** X.X | **Date:** YYYY-MM-DD` line near the top — this made the audit significantly easier for files that had it (e.g. `staff-plan.md`'s multiple dated supersession banners were easy to follow chronologically). A few files lack this entirely (`workflow.md` has no version/date banner at all, which contributed to it going stale unnoticed).

**Suggestion:** Add the version/date banner convention to any file still missing it, starting with `workflow.md` when it gets its staffing-model rewrite (see `02_issues_and_risks.md` M2).

### P5. Founder-Only Questions Collected in One Place
Before this session, founder-only open questions were scattered across `reading-order.md`'s "Open Decisions" table, `HANDOFF.md`'s "Still Open" list, individual CORRECTION files, and inline notes in `review-audit.md`. This made it easy to lose track of what still needed Anthony's input.

**Suggestion (implemented this session):** `05_open_questions_for_founder.md` now exists as the single running list. **Recommend this becomes the standing convention** — any new founder-only question discovered in future sessions gets added there first, with a pointer from wherever it was discovered, rather than being logged only inline.

---

## Substantive Operational Suggestions

### O1. Give the Venue Manager Hire the Same Rigor as the Phlebotomist Hire
`phlebotomist-job-posting.md` is a genuinely excellent, complete recruitment document — job description, ad copy, interview questions, reference-check script, fallback agency plan. The Venue Manager role is now confirmed as an equally (arguably more) critical-path hire, but has no equivalent document. Given the Venue Manager interviews the phlebotomist in that document's process, the sequencing gap is real, not just a documentation nicety.

**Suggestion:** Build a `venue-manager-job-posting.md` using `phlebotomist-job-posting.md` as a structural template, reusing the role detail already in `staff-plan.md` §3 and `hr-framework.md` §13.

### O2. Reconcile the WDP Cutoff Time Before Committing to Any Scenario Above 8 Clients/Day
Both `H2` in the issues log and the existing `cutoff-time-CORRECTION.md` flag this, but it's worth restating as an improvement rather than just a risk: the entire value of moving from Scenario B to Scenario C (25% more daily revenue capacity) rests on an unconfirmed number. This is a cheap, one-phone-call fix (per `cutoff-time-CORRECTION.md`'s own recommendation) relative to the revenue at stake.

**Suggestion:** Prioritise the WDP call above almost everything else in the pre-launch checklist — it's the single highest-leverage open item in the entire corpus.

### O3. Consider a Lightweight "Model Change Impact Checklist"
Every time the client-volume model has changed (Scenario A → B → C staggered → C sync → D), it has required updates across roughly 4-6 documents (operations-manual.md, staff-plan.md, gtt-clinical-protocol.md, financial docs, patient-facing materials). This session's audit shows that checklist isn't being consistently followed.

**Suggestion:** A short checklist — "when the client-volume scenario changes, update: [ ] operations-manual.md timetables [ ] gtt-clinical-protocol.md client count [ ] staff-plan.md headcount note [ ] any patient-facing SMS/email copy [ ] financial break-even figures" — attached to `am-capacity-weekend.md` or the new `CURRENT-MODEL.md` (see P1) would reduce the chance of a repeat of CONFLICT-03.

### O4. Reduce Redundant Scenario-C Documentation
There are currently three separate scheduling documents touching Scenario C in some form (`am-capacity-weekend.md`'s staggered version, `scenario-c-sync-timetables.md`, and two HTML visual timelines). Once the sync version is confirmed as final, consider consolidating to avoid the kind of drift found in CONFLICT-03 — e.g., archive the staggered tables in `am-capacity-weekend.md` (keep the narrative/rationale sections, drop the superseded table) once `operations-manual.md` is rewritten to point to the sync version directly.

---

## Not Recommended (Explicitly Out of Scope This Session)

- **Full rewrite of every "not reviewed this pass" document** — recommended as a follow-up sweep (see `02_issues_and_risks.md` M5), not attempted here to keep this session's scope to what was explicitly requested (Imara rename, known duplicates, and issues found along the way).
- **Deleting any superseded file** — this session consistently chose to flag/banner rather than delete, matching the existing repo convention of keeping `-ARCHIVED` files rather than removing them. Recommend continuing this convention rather than switching to deletion.
