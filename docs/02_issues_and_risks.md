# GTT Center Perth — Issues and Risks (Gap Analysis)

**Compiled:** 2026-07-19 | **Compiled by:** Grace (Operations Manager, audit pass)
**Purpose:** Consolidated gap analysis across the docs corpus — combines newly found issues from this session's audit with still-open items already logged elsewhere (`review-audit.md`, `cutoff-time-CORRECTION.md`, `king-edward-start-time-constraint.md`). Organized by severity. Founder-only decisions are cross-referenced to `05_open_questions_for_founder.md`, not duplicated in full here.

---

## HIGH SEVERITY

### H1. Operations Manual Trains Staff on the Wrong Scenario
**Source:** This session (`01_conflicts_log.md` CONFLICT-03)
`operations-manual.md` — the document new staff and the Venue Manager will read to learn the day's schedule — still describes Scenario B (8 clients/day, 07:40 start) as the launch model. The actual committed model is Scenario C synchronized-start (10 clients/day, 07:00 start), verified in `scenario-c-sync-timetables.md`. Flagged with a superseded banner this session but **not yet rewritten**. Risk: real scheduling/training errors if the section is used as-is before rewrite. **Action: full rewrite of operations-manual.md's GTT Scheduling Timetables section — priority 1 in the roadmap.**

### H2. WDP Courier/Specimen Cutoff Time Unconfirmed
**Source:** `cutoff-time-CORRECTION.md` (existing, still open)
Two different unconfirmed numbers (11:30 and 12:30) have been used across documents as if confirmed. Neither came from an actual WDP reply — the 12:30 figure appears to be a back-calculated target, not a real logistics constraint. This number is load-bearing for the entire AM window's end time. At Scenario D's 15-client volume the buffer is only 5 minutes — very tight if the real number turns out to be earlier. **Action: direct WDP confirmation required before treating any AM capacity figure above 8 clients/day as final.** Founder-only aspect (approving Reed to press WDP for a direct answer) — see open questions doc.

### H3. King Edward Hospital "Start Before 10am" Guidance Not Source-Verified
**Source:** `king-edward-start-time-constraint.md` (existing, still open)
Anthony reported this guidance from KEMH; a search for the underlying published document failed to locate it. Scenario C passes comfortably (last draw at 09:40) but Scenario D fails on a strict reading (last draw at exactly 10:00, not before it). If this constraint is wrong or misremembered, it currently blocks/complicates the 15-client growth scenario for no real reason; if it's right and unwritten anywhere accessible, GTT Center Perth needs the actual source before relying on or disputing it. **Action: locate the source document, or get written confirmation from KEMH/referring practices.**

### H4. ~~TPI Pension / Trust Distribution Interaction (CF-07) Still Deferred~~ — REMOVED FROM THIS LOG 2026-07-19
**Source:** `review-audit.md` CF-07
Previously listed here as a High-severity blocking item. **Removed 2026-07-19 per Anthony's direct instruction, stated twice: DVA/TPI pension advice is his personal matter, not a GTT Center Perth task, and should not be tracked as a GTT issue/risk.** CF-07's underlying legal analysis in `review-audit.md` is unaffected — only its tracking here is removed.

---

## MEDIUM SEVERITY

### M1. Venue Manager Is a New Critical-Path Hire With No Named Candidate
**Source:** This session (Priority 0 task) — **RESOLVED 2026-07-19 (job posting built); recruitment timing corrected 2026-07-19 (founder feedback)**
The entire operational model — first-aid/EpiPen response, fire warden, clinical escalation, HR discipline, weekly P&L, WDP liaison, day-to-day payment approval — depends on a Venue Manager role that is a new hire, not yet in place. Unlike the phlebotomist hire (which has a full job posting, interview process, and fallback agency plan in `phlebotomist-job-posting.md`), no equivalent recruitment document existed for the Venue Manager role — **now built: `docs/venue-manager-job-posting.md`**, using `phlebotomist-job-posting.md` as a structural template. **Important sequencing correction (2026-07-19):** Anthony confirmed GTT Center Perth is NOT recruiting or looking for any staff, including the Venue Manager, until a physical venue location is confirmed — the job posting document is ready in advance, not an active posting. The document itself flags that its own interview-process section assumes a Venue Manager already exists to interview the phlebotomist — this remains a real sequencing dependency to resolve once recruitment actually begins (Venue Manager first, then phlebotomist).

### M2. `workflow.md` Describes a Contradictory Staffing Model (Subtenants)
**Source:** This session (`01_conflicts_log.md` CONFLICT-04)
This document describes massage/nails/hair/scan roles as "Sublet," directly contradicting the current employed-staff, no-subtenant model confirmed everywhere else (Day 51). Flagged this session but not rewritten. Low risk of active harm (this document isn't in the Priority 0 reading path) but risks confusing anyone who reads it in isolation, especially since it also still lists a "Keepsake scan operator" role that no longer exists in scope. **Action: rewrite workflow.md's staffing table to match the current employed model, remove the scan-operator row.**

### M3. MA000027 Saturday Phlebotomist Ordinary-Hours Carve-Out Unconfirmed
**Source:** `HANDOFF.md` (existing, still open)
A clause potentially allowing Saturday 8am–4:30pm to count as ordinary hours (not penalty rate) for private pathology practices under the Health Professionals Award has not been verified with a payroll advisor or Fair Work directly. All current financial models conservatively assume full penalty rates, so this is an upside risk (potential cost saving), not a downside risk — but it should be confirmed rather than left as an assumption indefinitely. **Action: payroll advisor or Fair Work direct check.**

### M4. Package Price-Increase Timing Not Decided
**Source:** `HANDOFF.md` (existing, still open)
Introductory package pricing is in place; the timing of a price increase (Month 3 vs Month 4) is not yet confirmed by Anthony. Recommendation in HANDOFF.md leans Month 4 (aligns with break-even milestone) but is not decided. **Action: founder decision — see open questions doc.**

### M5. "Not Reviewed This Pass" Documents Carry Unknown Risk
**Source:** This session (`00_document_inventory.md`)
Roughly 10 documents (equipment-costs.md, hire-purchase-china.md, gtt-test-reference.md, consent-form.md, privacy-policy.md, market-research-findings.md, ivy-booking-system.md, extended-wellness-services.md, reed-partnerships.md, onboarding.md, staff-profiles/*) were not actively re-verified for Scenario B/C consistency or other issues in this session, since they were outside the explicit Priority 0 scope and the two named duplicate/conflict pairs. They have no *known* issues, but "not reviewed" is different from "confirmed clean." **Action: a follow-up sweep of these documents specifically for Scenario B/C references and any other stale figures — see roadmap.**

### M6. Second, Non-Sync Scenario C Visual Timeline Not Flagged
**Source:** This session (`01_conflicts_log.md` CONFLICT-03, secondary finding)
`scenario-c-timeline.html` (the visual companion to the staggered, pre-sync Scenario C) was identified as likely superseded by `scenario-c-sync-timeline.html` but was not confirmed or flagged this session due to time constraints. **Action: verify and flag/update if confirmed stale.**

---

## LOW SEVERITY

### L1. Emergency Plan Has Unfilled Placeholder Fields
**Source:** Existing (`emergency-plan.md`)
AED location, exit routes, venue address, and several emergency contact numbers are marked "[to be inserted]" pending venue selection. Expected at this pre-lease stage, but flagged so it isn't forgotten once a venue is signed — this document is explicitly marked "MANDATORY... before the first patient enters the venue."

### L2. Historical Audit Trail Shows Repeated Re-Opening of the Same Conflict Class (Scheduling)
**Source:** This session, cross-referenced against `review-audit.md`
IC-05 ("GTT capacity") was marked RESOLVED Day 49 at 8 clients/day, then the model moved to 10 clients/day (Scenario C) without IC-05's resolution note being updated, and now there's a fresh unresolved instance (H1 above) of essentially the same conflict class. This isn't a process failure given the venture is in active, fast-iterating planning — but it suggests scheduling/capacity conclusions age faster than other document types and may benefit from a lighter-weight "current model" pointer document that's updated every time the number changes, rather than updating full timetable tables in multiple files each time.

### L3. Duplicate and Superseded File Housekeeping
**Source:** This session (`01_conflicts_log.md` CONFLICT-01, CONFLICT-02)
Both resolved this session, but the underlying process gap (files not renamed/flagged when superseded) could recur. No action needed beyond what's already done, but worth noting as a pattern for whoever maintains this corpus going forward.

---

## Summary Table

| ID | Issue | Severity | Status |
|---|---|---|---|
| H1 | operations-manual.md trains on wrong scenario | High | Flagged, rewrite pending |
| H2 | WDP cutoff time unconfirmed | High | Open — needs WDP reply |
| H3 | KEMH start-time guidance unsourced | High | Open — needs source or confirmation |
| H4 | ~~TPI pension / trust distribution risk (CF-07)~~ | — | REMOVED 2026-07-19 — Anthony's personal matter, not a GTT task |
| M1 | Venue Manager recruitment document | Medium | RESOLVED — `docs/venue-manager-job-posting.md` built; recruitment does not start until location confirmed |
| M2 | workflow.md contradictory staffing model | Medium | Flagged, rewrite pending |
| M3 | MA000027 Saturday carve-out unconfirmed | Medium | Open — needs payroll/Fair Work check |
| M4 | Package price-increase timing undecided | Medium | Founder decision needed |
| M5 | ~10 docs not reviewed this pass | Medium | Follow-up sweep recommended |
| M6 | scenario-c-timeline.html status unconfirmed | Medium | Follow-up check recommended |
| L1 | Emergency plan placeholder fields | Low | Expected at this stage, tracked |
| L2 | Scheduling conflict class re-opens repeatedly | Low | Process observation, no action needed |
| L3 | Duplicate/superseded file housekeeping | Low | Resolved this session, pattern noted |

See `03_improvements.md` for suggested process improvements addressing the root causes (especially L2/L3), and `04_roadmap_next_steps.md` for prioritised next actions.

---

## Changelog

**2026-07-19 (founder feedback round 3)** — Removed H4 (TPI/DVA pension interaction) from this log entirely — Anthony's personal matter, not a GTT task, stated twice. Resolved M1 (Venue Manager job posting) — `docs/venue-manager-job-posting.md` now built; also corrected the recruitment-timing framing to reflect that recruitment does not begin until a physical venue location is confirmed.
