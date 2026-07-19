# GTT Center Perth — Conflicts Log

**Compiled:** 2026-07-19 | **Compiled by:** Grace (Operations Manager, audit pass)
**Purpose:** Every detected conflict, duplicate, or inconsistency across the docs corpus, with resolution status. Companion to `00_document_inventory.md` and `review-audit.md` (which already logs many historical conflicts — this log adds newly found ones and cross-references the historical ones still open).

---

## CONFLICT-01 | `research-supplement-day48.md` — Stale Duplicate

**Status: RESOLVED 2026-07-19**

**Finding:** `docs/research-supplement-day48.md` and `docs/research-supplement-day48-ARCHIVED.md` are byte-identical (confirmed via `diff` — zero output). `reading-order.md` already correctly lists `research-supplement-day48-ARCHIVED.md` as "ARCHIVED. Merged into research.md v3.0." The non-archived copy (`research-supplement-day48.md`) was never renamed or removed when the Day 48 supplement was merged into `research.md` v3.0 (confirmed via `research.md`'s own header: "Supersedes: v2.0 + research-supplement-day48.md").

**Root cause:** When the merge into research.md v3.0 happened (2026-06-09), one copy was renamed to `-ARCHIVED` and the original filename copy was left in place instead of being deleted or also renamed.

**Resolution:**
- Added a superseded banner to `research-supplement-day48.md` pointing to `research.md` as canonical.
- Added an entry for `research-supplement-day48.md` in `reading-order.md`'s Reference Only table, marked ARCHIVED with the same status as its sibling.
- File retained (not deleted) to preserve history per repo convention (other archived docs are kept, not removed).

---

## CONFLICT-02 | `floor-plan-v3.*` vs `floor-plan-visual.*` — Version Mismatch, No Supersession Marker

**Status: RESOLVED 2026-07-19 (partial — see note on PDF)**

**Finding:** Two floor plan concept renders exist with different layouts and no cross-reference:
- `floor-plan-visual.html` / `floor-plan-visual.pdf` — git history confirms this is v2 (commit d85c56c, 2026-07-01), box-fill room layout.
- `floor-plan-v3.svg` / `floor-plan-v3.pdf` — git history confirms this is v3 (commit 25bdc5d, 2026-07-10), open-plan lounge with furniture and accessible door swing arcs — described in its own commit message as a deliberate revision of the earlier version.

`HANDOFF.md` (2026-07-17, most recent session summary) lists `floor-plan-v3.svg`/`.pdf` as current with no mention of the v2 files, implying the v2 files are stale but this was never stated explicitly anywhere in the docs themselves, and neither file was flagged as superseded.

**Resolution:**
- Added a red, bold superseded banner directly into `floor-plan-visual.html`'s visible subtitle, pointing to `floor-plan-v3.svg`/`.pdf` as current.
- Added entries for all four floor-plan files (plus `floor-plan-concept.md`) to `reading-order.md`'s Reference Only table with accurate status.
- **`floor-plan-visual.pdf` (binary) could not be text-edited** with available tools — its superseded status is recorded in `reading-order.md` and `00_document_inventory.md` instead. If Anthony wants the PDF itself visually marked, it needs to be re-exported from the (now-updated) HTML or regenerated.

---

## CONFLICT-03 | Scenario B (8 clients/day) vs Scenario C Sync (10 clients/day) — Operational Model Mismatch

**Status: PARTIALLY RESOLVED 2026-07-19 — flagged, not fully rewritten**

**Finding:** This is the most significant conflict found this session. Per `HANDOFF.md` (2026-07-17, the most recent and most authoritative session summary), **the current committed operational model is Scenario C, synchronized-chair-start: 10 clients/day, 07:00 first draw** — fully verified in `docs/scenario-c-sync-timetables.md` (programmatic double-booking check, zero conflicts across 2 phlebotomists and 8 treatment staff).

However, `docs/operations-manual.md` — the primary day-to-day operations reference, read by all staff — still contains an entire "GTT SCHEDULING TIMETABLES" section built around **Scenario B (8 clients/day, 07:40 first draw)**, labelled "LAUNCH MODEL," with full per-client and per-staff tables. This is the document staff-plan.md, gtt-clinical-protocol.md, and patient-facing materials point to as authoritative.

`docs/gtt-clinical-protocol.md` also stated "8 GTT patients per day" and pointed to operations-manual.md for the verified timetable — doubly wrong (wrong number, and pointing to a now-also-wrong source).

**Why this matters:** If a Venue Manager or new staff member reads `operations-manual.md` cover-to-cover (as instructed by `reading-order.md`), they will train on an 8-client/07:40-start model that does not match the actual committed 10-client/07:00-start model. This could cause real scheduling errors at launch — under- or over-booking the day, wrong arrival-time communications to patients, wrong phlebotomist load expectations.

**Secondary finding:** Even within the "Scenario C" family, there are two versions:
1. Staggered Scenario C (20-min offset between chairs) — in `am-capacity-weekend.md`, dated 2026-07-16.
2. Synchronized Scenario C (both chairs start together) — in `scenario-c-sync-timetables.md`, dated 2026-07-17, one day newer, described as adding a treatment-staff concurrency check "previously only asserted, not built."

The synchronized version is the more recent and more rigorously verified of the two, and `am-capacity-weekend.md` itself (line ~405) confirms the sync variant is consistent with the original Scenario C finding. **`scenario-c-sync-timetables.md` should be treated as the single canonical timetable.**

**Resolution so far:**
- Added a clear superseded banner to `operations-manual.md`'s GTT Scheduling Timetables section, pointing to `scenario-c-sync-timetables.md` as canonical. **The Scenario B tables were NOT deleted or rewritten** — only flagged — because a full rewrite of the per-client/per-staff tables, the "Notes" analysis, and the Scenario A/D cross-references in that section is a substantial editorial task warranting its own dedicated pass (recommended as a priority action — see `04_roadmap_next_steps.md`).
- Updated `gtt-clinical-protocol.md`'s client count from 8 to 10 and repointed its reference to `scenario-c-sync-timetables.md`.
- Added a clarifying note to `staff-plan.md` confirming the headcount conclusions (2 phlebotomists + 8 treatment staff, 2 per category) are unaffected by the Scenario B->C change — Scenario C explicitly runs on the same staff numbers, just a tighter schedule.

**Not yet resolved — recommended follow-up (see roadmap):**
- Full rewrite of `operations-manual.md`'s GTT Scheduling Timetables section to replace the Scenario B tables with the Scenario C sync tables (or a direct pointer + brief summary, if a full table duplication isn't desired).
- Flag/update `scenario-c-timeline.html` (the visual companion to the staggered, non-sync Scenario C) — likely also superseded by `scenario-c-sync-timeline.html`, not confirmed or flagged this session due to time.
- Confirm whether any patient-facing materials (SMS templates, confirmation emails, website copy) reference "8 clients" or 07:40-based times anywhere — not checked this session.

---

## Cross-Reference: Historical Conflicts Already Logged in `review-audit.md`

`review-audit.md` (the pre-existing full business audit) already documents a substantial set of conflicts, most now resolved. Listed here for completeness — do not re-litigate:

| ID | Conflict | Status per review-audit.md |
|---|---|---|
| IC-01 | Ramp-up assumptions (financial-model.md vs cash-flow.md) | RESOLVED Day 50 — cash-flow.md canonical |
| IC-02 | Staff hours (staff-plan.md vs cash-flow.md/gtt-test-reference) | RESOLVED Day 51 — AM-only confirmed, PM via dedicated hire |
| IC-03 | Package pricing (multiple conflicting price lists) | RESOLVED Day 50 — standardised, later further resolved to Package 2/3 only |
| IC-04 | Operating days | RESOLVED — no change needed |
| IC-05 | GTT capacity (6-9 vs 5 slots) | RESOLVED Day 49 — 8 clients/2 phlebotomists (**now itself superseded by Scenario C, 10 clients — see CONFLICT-03 above**) |
| IC-06 | Startup capital | RESOLVED Day 50 — cash-flow.md figures canonical |
| CF-07 | TPI pension interaction (Imara/Anthony) | DEFERRED, not blocking — still requires DVA-adviser sign-off. Clarified 2026-07-19 that this is separate from the new Venue Manager payroll role. |
| OG-03 | Emergency response plan | RESOLVED Day 48 — emergency-plan.md exists. Wording refreshed 2026-07-19 (Imara -> Venue Manager). |

**Note:** IC-05's "RESOLVED Day 49" status is now itself stale per CONFLICT-03 above — the audit trail shows scheduling conflicts have been resolved and re-opened multiple times as the model evolved (8 -> 10 clients). This is a natural consequence of active iteration, not a process failure, but reinforces the recommendation in the roadmap to designate one single "current operational model" document that everything else points to, rather than letting the most-recently-edited file become accidentally authoritative.

---

## Other Consistency Checks Performed (No Conflict Found)

- **Package pricing:** `services-pricing-locked.md`, `HANDOFF.md`, and `financial-break-even-staff.md` all agree: Package 2 (A$250) + Package 3 (A$300) only, Package 1 dropped. Consistent.
- **Saturday/Sunday model:** `HANDOFF.md`, `am-capacity-weekend.md` agree: Saturday reuses AM model + PM standalone (hours-based costing), Sunday closed. Consistent.
- **PM staffing model:** `pm-staffing-roster.md` is consistently cited as canonical by `business-plan.md`, `staff-plan.md`, and `operations-manual.md` banners. Consistent (all three defer to it correctly).
- **Superannuation rate (12%):** Consistent across `staff-plan.md`, `hr-framework.md`, `financial-setup.md`.
- **No subtenants:** Consistent across `staff-plan.md`, `operations-manual.md` (Day 51 update explicitly removes subtenant-rent references). **Exception: `workflow.md` still describes a sublet model (massage/nails/hair/scan) — flagged below.**

---

## CONFLICT-04 | `workflow.md` — Stale Subtenant/Sublet Staffing Model

**Status: FLAGGED 2026-07-19 — not rewritten**

**Finding:** `docs/workflow.md`'s "Staffing Model (Launch)" table describes massage therapist, nail technician, hairdresser, and keepsake scan operator as **"Sublet"** roles, with phlebotomist as PathWest/WDP staff. This entirely contradicts the current, canonical model in `staff-plan.md`, `financial-break-even-staff.md`, and the Day 51 updates elsewhere: **all service delivery staff are employed** by GTT Center Perth (wage-based, not room rental), **there are no subtenants**, and the phlebotomists are **employed directly** by GTT Center Perth (not PathWest/WDP staff) — WDP/PathWest only provides the NATA accreditation umbrella and credentialing.

**Likely cause:** `workflow.md` appears to be an early draft (no version/date banner, no supersession markers anywhere in the file) that predates the Day 51 "no subtenants, employed model confirmed" decision and was never updated or flagged.

**Resolution:** Added a note in this session's changelog entry within `workflow.md` flagging the staffing table as stale, pointing to `staff-plan.md` as the current model. **The table itself was not rewritten** — recommended as a follow-up action (see roadmap) since it requires re-deriving the "keepsake scan operator" row too, which no longer exists in current scope (3D scan removed entirely per Day 51).

---

## Summary

| Conflict | Severity | Status |
|---|---|---|
| CONFLICT-01: research-supplement-day48.md duplicate | Low (no operational impact, just clutter/confusion risk) | RESOLVED |
| CONFLICT-02: floor-plan v2/v3 mismatch | Low-Medium (fit-out brief risk if wrong version used) | RESOLVED (HTML); PDF flagged, not edited |
| CONFLICT-03: Scenario B vs Scenario C sync | **HIGH** (training/scheduling risk if operations-manual.md read as-is) | FLAGGED, partially resolved — full rewrite recommended as priority action |
| CONFLICT-04: workflow.md stale subtenant model | Medium (could mislead a new reader on employment structure) | FLAGGED, not rewritten — recommended as follow-up action |

See `04_roadmap_next_steps.md` for prioritised follow-up actions on the items not fully resolved this session.
