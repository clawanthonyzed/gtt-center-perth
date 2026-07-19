# GTT Center Perth — Roadmap & Next Steps

**Compiled:** 2026-07-19 | **Compiled by:** Grace (Operations Manager, audit pass)
**Status:** PRIMARY DELIVERABLE of this session's audit/consolidation pass.
**Purpose:** Prioritised action list bringing together this session's findings (`00_document_inventory.md`, `01_conflicts_log.md`, `02_issues_and_risks.md`, `03_improvements.md`) into one execution-ready roadmap. No fixed launch date — sequence is by dependency only, per standing instruction.

---

## How to Read This Roadmap

Actions are grouped by **dependency tier**, not calendar date (no launch date is set). Within each tier, items are ordered by severity/leverage. Founder-only decisions are marked and cross-referenced to `05_open_questions_for_founder.md` — do not attempt to resolve those without Anthony's input.

---

## TIER 0 — Blocking Gates (Nothing Else Should Proceed Confidently Without These)

| # | Action | Why it blocks | Owner | Ref |
|---|---|---|---|---|
| 1 | **Confirm WDP courier/specimen cutoff time directly with WDP** | Every AM capacity figure above 8 clients/day (i.e. the entire Scenario C model, +25% revenue capacity vs Scenario B) rests on an unconfirmed number (11:30 vs 12:30, neither sourced). Cheapest, highest-leverage open item in the corpus. | Reed (partnerships agent), approved by Anthony | `cutoff-time-CORRECTION.md`, H2 in `02_issues_and_risks.md` |
| 2 | **DVA-qualified financial adviser consultation (TPI pension interaction)** | Legal prerequisite before signing any lease or hiring anyone, per CLAUDE.md non-negotiable rule and `review-audit.md` CF-07. Not resolved by this session's Venue Manager rename. | Anthony (personal action, cannot be delegated) | CF-07, H4, open questions doc |
| 3 | **Begin Venue Manager recruitment (Week 1 critical path)** | Venue cannot safely open without this role — first-aid/EpiPen holder, fire warden, clinical escalation contact, staff supervisor, day-to-day payment approver. Currently a confirmed critical-path hire with no recruitment document yet built. | Anthony/Grace | `staff-plan.md` §7, `hr-framework.md` §13, M1 in `02_issues_and_risks.md` |
| 4 | **Source-verify or formally confirm the King Edward Hospital "start before 10am" guidance** | Currently unsourced. Scenario C passes; Scenario D (growth scenario) fails on a strict reading. Needed before Scenario D can be treated as a real option. | Anthony/Reed | `king-edward-start-time-constraint.md`, H3 |

---

## TIER 1 — Documentation Fixes Needed Before Staff Training / Onboarding

These don't block the business commercially but **must be fixed before any new staff member is trained off these documents**, since they currently contain wrong operational numbers.

| # | Action | Detail | Ref |
|---|---|---|---|
| 5 | **Rewrite `operations-manual.md`'s GTT Scheduling Timetables section** | Replace the Scenario B (8-client) tables with the Scenario C sync (10-client) tables from `scenario-c-sync-timetables.md`. This is the single most important documentation fix from this session — flagged with a superseded banner, not yet rewritten. | H1, CONFLICT-03 |
| 6 | **Build a Venue Manager job posting/recruitment document** | Use `phlebotomist-job-posting.md` as a structural template (job description, ad copy, interview script, reference checks). No equivalent document currently exists for this critical-path hire. | M1, O1 |
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

- WDP cutoff confirmation (Tier 0 #1) — blocks confidently committing to Scenario C/D capacity.
- DVA adviser consultation (Tier 0 #2) — blocks lease signing and hiring, per non-negotiable rule.
- King Edward guidance sourcing (Tier 0 #4) — blocks Scenario D (growth scenario) being treated as viable.
- Package price-increase timing (Month 3 vs 4) — not blocking, but needs a decision before Month 3 arrives.
- MA000027 Saturday carve-out — upside-only, not blocking, but worth resolving.

---

## What This Session Did NOT Do (Explicitly Out of Scope)

- Did not set a launch date (per standing instruction — sequence by dependency only).
- Did not re-litigate any of the "already resolved" items listed in the task brief (launch date, funding source, AM model choice of Scenario C, package structure, Saturday/Sunday model).
- Did not delete any file — all supersessions were handled via banners/flags, preserving history.
- Did not rewrite `operations-manual.md`'s timetables, `workflow.md`'s staffing table, or build the Venue Manager job posting — these are flagged as Tier 1 priority actions for the next work session, not completed here, because each is a substantial standalone editorial task and this session's scope was audit + the two named conflicts + whatever else was found along the way.
- Did not touch `financial-model.md`, `dva-tpi-research.md`, or `research.md` — explicitly out of scope per task instruction (these cover trust/ownership structure, not day-to-day ops).

---

## Recommended Order for the Next Working Session

1. Tier 0 #1 (WDP cutoff call) — cheapest, highest leverage, unblocks confidence in the whole Scenario C model.
2. Tier 0 #3 (Venue Manager recruitment) — start the clock on the longest lead-time item.
3. Tier 1 #5 (rewrite operations-manual.md timetables) — now safe to do properly once Tier 0 #1 confirms the real cutoff time (avoids rewriting twice if the cutoff changes the schedule).
4. Tier 1 #6 (Venue Manager job posting) — supports Tier 0 #3.
5. Tier 0 #2 and #4, Tier 1 #7-8, Tier 2, Tier 3 — as capacity allows, no strict dependency order among these.
