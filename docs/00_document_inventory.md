# GTT Center Perth — Document Inventory

**Compiled:** 2026-07-19 | **Compiled by:** Grace (Operations Manager, audit pass — updated through Phase 6/7 pass, same day)
**Purpose:** Single reference listing every file in `docs/`, its status, and its role in the corpus. Companion to [reading-order.md](reading-order.md) (which orders reading, not status) and [01_conflicts_log.md](01_conflicts_log.md) (which details specific conflicts).

> **NEW 2026-08-15/16 — External Execution Round outputs added.** Five new, committed (not yet pushed) deliverables exist from a "build, don't just recommend" execution round: a public-ready demand-validation landing page, an external-facing venture overview pack, three professional outreach drafts, a startup-cost-reduction action table, and an AM->PM data-capture specification. See the new **## External Execution Round (2026-08-15/16)** section below (placed directly after the Strategy/Brand/Venue/Naming Layer section) for the full list with status and what to look at.

> **CORRECTED 2026-08-15 — this file omitted an entire, current, actively-maintained layer of the repository.** Everything below this banner (all pre-2026-08-08 content) covers only `docs/*.md` — it never listed `docs/strategy/`, `docs/naming/`, `docs/experience/`, `docs/DECISION-LOG.md`, or `outputs/brand/`, which together are the most current strategic/brand/venue work in the repo (built 2026-08-05 through 2026-08-15). This was identified as the root cause of "flying blind" in a dedicated execution audit and is fixed here with a new section (jump to **## Strategy / Brand / Venue / Naming Layer** below) rather than a full rewrite of the rest of this file, which otherwise still accurately describes the `docs/*.md` layer's July/early-August state. Read the new section first for anything strategic, brand, venue, or naming-related — the old sections below remain correct for financial/operational/clinical/legal detail.

> **Correction, 2026-08-08 (F-2, per `docs/architecture/REPOSITORY-AUDIT.md`):** this file's per-row status descriptions had gone stale relative to `docs/CURRENT-STATE.md`'s 2026-07-30 and 2026-08-05 rebases in several places (see the corrected rows for `HANDOFF.md`, `operations-manual.md`, `scenario-c-sync-timetables.md`, `cash-flow.md` below, each individually marked with this date). **The file count below (80) and the Summary Counts table near the end of this file were NOT independently recounted or re-verified this pass** — a genuine current count is given in `docs/reading-order.md`'s header (110+, as of 2026-08-08); flagged here rather than silently republished as still-accurate, since re-verifying every row's status individually is a larger task than this correction pass covers.

**Total files:** 80 (70 markdown in `docs/` + 12 new Phase 6/7 documents listed below, 8 staff-profile markdown files in `docs/staff-profiles/`, 6 non-markdown visual/export files) — **stale as of 2026-08-08, see correction note above; do not treat as current**

## Strategy / Brand / Venue / Naming Layer (2026-08-05 to 2026-08-15) — Read This Section First

This layer sits on top of everything else in this file — it translates the canonical financial/operating model (`docs/CURRENT-STATE.md`, `data/canonical/`) into strategy, brand identity, venue requirements, and customer experience. **Status vocabulary used only in this section** (distinct from the legacy CURRENT/SUPERSEDED/ARCHIVED legend below, per the 2026-08-15 consolidation instruction): **COMPLETE**, **CURRENT/CANONICAL**, **IN PROGRESS**, **WAITING (WDP/Carole)**, **BLOCKED (genuine dependency)**, **FOUNDER ACTION**, **EXTERNAL ACTION**, **DEFERRED**, **SUPERSEDED**.

### Strategy (`docs/strategy/`)

| File | Status | Notes |
|---|---|---|
| [STRATEGIC-REPORT.md](strategy/STRATEGIC-REPORT.md) | CURRENT/CANONICAL | Consolidated synthesis of the business/experience/naming state as of 2026-08-14 — good starting point for the whole layer. |
| [OPERATING-COMMERCIAL-ARCHITECTURE.md](strategy/OPERATING-COMMERCIAL-ARCHITECTURE.md) | CURRENT/CANONICAL | Translates 18/day into operating + commercial architecture — AM/PM structure, staffing, replicability. |
| [18-CLIENT-OPERATIONAL-STRESS-TEST.md](strategy/18-CLIENT-OPERATIONAL-STRESS-TEST.md) | CURRENT/CANONICAL | Minute-by-minute schedule reconstruction, resolved the AM/PM transition and nail-duration questions. |
| [18-CLIENT-COMMERCIAL-STRESS-TEST.md](strategy/18-CLIENT-COMMERCIAL-STRESS-TEST.md) | CURRENT/CANONICAL | Break-even, margin-of-safety, 12-vs-18 resilience comparison — canonical-sourced throughout. |
| [BRAND-EXPERIENCE-FOUNDATION.md](strategy/BRAND-EXPERIENCE-FOUNDATION.md) | COMPLETE | Strategic brand foundation — positioning, naming territory, AM/PM brand architecture, A/B/C/D-classified recommendations. |
| [VISUAL-BRAND-DIRECTION.md](strategy/VISUAL-BRAND-DIRECTION.md) | COMPLETE | Colour/type/logo-territory creative brief. **Colour palette section is SUPERSEDED by the founder-locked palette** — see the outputs/brand/ row below; typography (Fraunces + DM Sans) and wordmark-led logo territory remain current. |
| [VENUE-FUNCTIONAL-BRIEF.md](strategy/VENUE-FUNCTIONAL-BRIEF.md) | CURRENT/CANONICAL | Venue requirements validated against 18/day — room counts, floor-area tiers, A/B/C/D-tagged requirements. |
| [PROPERTY-SEARCH-FRAMEWORK.md](strategy/PROPERTY-SEARCH-FRAMEWORK.md) | CURRENT/CANONICAL | Screening framework applied to real listings — hard requirements, scoring model. |
| [PERTH-PROPERTY-SHORTLIST.md](strategy/PERTH-PROPERTY-SHORTLIST.md) | IN PROGRESS | Real candidates found (2 Tier-1), zero inspected. **FOUNDER ACTION required to move this forward** — see report §5. |
| [BRAND-ARCHITECTURE.md](strategy/BRAND-ARCHITECTURE.md), [BRAND-STRATEGY-NAME-AGNOSTIC.md](strategy/BRAND-STRATEGY-NAME-AGNOSTIC.md), [PREMIUM-POSITIONING.md](strategy/PREMIUM-POSITIONING.md) | CURRENT/CANONICAL | Name-agnostic brand strategy, architecture, and cost-discipline principles — feed into BRAND-EXPERIENCE-FOUNDATION.md, still individually referenced throughout. |

### Naming (`docs/naming/`)

| File | Status | Notes |
|---|---|---|
| [NAMING-DECISION-STATE.md](naming/NAMING-DECISION-STATE.md) | CURRENT/CANONICAL | The single current-status file for naming — read this one, not the others, for "where does naming stand." |
| [NAMING-FINAL-COMPARISON.md](naming/NAMING-FINAL-COMPARISON.md) | CURRENT/CANONICAL | SOLENA 71.6% / ELOWEN 68.8% / ELOWYN 65.9% — the weighted comparison the decision state summarises. |
| [AUSTRALIAN-TRADEMARK-CLEARANCE-BRIEF.md](naming/AUSTRALIAN-TRADEMARK-CLEARANCE-BRIEF.md) | WAITING (FOUNDER ACTION) | Ready to send to an attorney. Not sent — deliberately deferred by Anthony to a later funding/validation milestone. Not legal advice. |
| [SOLENA-ELOWEN-STRATEGIC-HANDOVER-DECISION-AUDIT.md](naming/SOLENA-ELOWEN-STRATEGIC-HANDOVER-DECISION-AUDIT.md), [NAME-INVESTIGATION-REPORT.md](naming/NAME-INVESTIGATION-REPORT.md), [CLAUDE-NAMING-INVESTIGATION.md](naming/CLAUDE-NAMING-INVESTIGATION.md) | CURRENT/CANONICAL (historical reasoning trail) | The full evidence trail behind the current decision state — read only if you want the "why," not the "what." |
| `naming/assets/` (Claude Design boards) | CURRENT | Visual exploration boards referenced by the naming reports. |

**Naming status in one sentence:** SOLENA and ELOWEN both remain live candidates; no name is selected; trademark clearance is the only real blocker and it is a founder-timing decision, not a research gap.

## External Execution Round (2026-08-15/16) — New Outputs

**Context:** a dedicated "build, don't just recommend" round. All five items below are BUILT and committed locally (not pushed — see the venture's own commit log, `git log` on this repo). Each becomes a live clickable GitHub link only once pushed to `origin/main`.

| Item | Status | What it is / what to look at |
|---|---|---|
| [`outputs/landing-page/`](../outputs/landing-page/index.html) (`index.html`, `styles.css`, `favicon.svg`, `script.js`, `qa/QA-NOTES.md`) | COMPLETE — repo-ready, NOT internet-live | The public-ready, neutral-working-name demand-validation landing page, reskinned to the founder-locked palette/typography. `qa/QA-NOTES.md` lists exactly what's still needed to actually deploy it publicly (hosting, a real submission endpoint — `script.js` currently only logs to console, a domain, the still-DRAFT `privacy-policy.md`, analytics) — none of that has been actioned, deliberately, pending Anthony's decision. |
| [`outputs/GTT-CENTER-PERTH-VENTURE-OVERVIEW.md`](../outputs/GTT-CENTER-PERTH-VENTURE-OVERVIEW.md) | COMPLETE | A concise, external-facing summary for professional advisers (property agent, WDP, pathology partner, bank, accountant, solicitor) — built entirely from `CURRENT-STATE.md`/`master_financial_model.yml`/`business-plan.md`/`executive-summary.md`/`investor-memorandum.md`, no invented figures, explicitly discloses what's not yet confirmed. |
| [`docs/accountant-engagement-email-draft.md`](accountant-engagement-email-draft.md) | READY TO SEND once a firm is chosen | First-contact accountant engagement email, built from `financial-setup.md` Step 1's existing brief. |
| [`docs/insurance-broker-quote-request-draft.md`](insurance-broker-quote-request-draft.md) | READY TO SEND once a broker is chosen | Indicative insurance quote-request email, built from `financial-setup.md` Step 8. |
| [`docs/fairwork-infoline-query-script.md`](fairwork-infoline-query-script.md) | READY TO USE (call 13 13 94) | Closes the Saturday ordinary-hours (MA000027) gap flagged in `hr-framework.md` — a phone script, no recipient-selection blocker. |
| [`docs/architecture/STARTUP-COST-REDUCTION-ACTIONS.md`](architecture/STARTUP-COST-REDUCTION-ACTIONS.md) | COMPLETE | Concrete DO NOW / WAIT FOR VENUE / WAIT FOR WDP / OUTSOURCE action table extracted from the existing `STARTUP-COST-OPTIMISATION.md`/`MVP-OPENING-DECISION-REVIEW.md` analysis (no re-analysis, no invented savings). Includes a WA SBDC free-advisory booking step and an acoustic/fire-rated curtain supplier pricing-request draft. |
| [`docs/experience/AM-TO-PM-DATA-CAPTURE-SPECIFICATION.md`](experience/AM-TO-PM-DATA-CAPTURE-SPECIFICATION.md) | COMPLETE (design spec, not yet implemented) | What data (Fresha tags/fields + one roster-sheet column) needs capturing to eventually measure whether `RETURN-LOOP.md`'s AM->PM conversion mechanism is working. No new software, no client-facing change. Implementation gated on the Venue Manager being hired (§5 of the spec). |

**Nothing above requires Anthony to write anything from scratch** — every outreach draft is genuinely send-ready pending a recipient choice (accountant/insurance) or is usable immediately (Fair Work call, curtain supplier enquiry in `STARTUP-COST-REDUCTION-ACTIONS.md` Appendix B).

### Experience (`docs/experience/`) + Governance

| File | Status | Notes |
|---|---|---|
| [CUSTOMER-JOURNEY.md](experience/CUSTOMER-JOURNEY.md) | CURRENT/CANONICAL | Full AM/PM journey map, name-agnostic. |
| [RETURN-LOOP.md](experience/RETURN-LOOP.md) | CURRENT/CANONICAL | The AM→PM retention mechanism — the single highest-priority unmodelled financial gap traces back to this document. |
| [AM-TO-PM-DATA-CAPTURE-SPECIFICATION.md](experience/AM-TO-PM-DATA-CAPTURE-SPECIFICATION.md) | COMPLETE (design spec, 2026-08-15/16) | What data needs capturing (Fresha tags + one roster-sheet column) to eventually measure whether RETURN-LOOP.md's mechanism is working — no new software, implementation gated on Venue Manager hire. |
| [DECISION-LOG.md](../DECISION-LOG.md) | CURRENT/CANONICAL | Append-only record of major decisions (naming leader, retail strategy, etc.) — check here before assuming a decision is still open. |

### Brand Output (`outputs/brand/`)

| Item | Status | Notes |
|---|---|---|
| `warm-stone-tokens.css` | CURRENT/CANONICAL | **Founder-locked palette** (2026-08-15): Warm Ivory #FAF6EE, Warm Stone #E8DAC5, Deep Brown #33261E, Earthy Terracotta #A9654E, Muted Olive #5E5F45, Soft Dusty Rose #D9A08C, Warm Brass #9C7A46 (fine-line/hardware/signage detail only). Typography: Fraunces + DM Sans. Logo direction: wordmark-led. Do not reopen without a new founder decision. |
| `solena/`, `elowen/` (wordmarks, applications, monogram tests, landing pages) | COMPLETE (first pass) | Real, viewable assets for both names, identical treatment, built to let Anthony judge visually. Not final production art. |
| `comparison/` (comparison board, brand-system sheet, print-review) | COMPLETE | Side-by-side Solena/Elowen comparison; `SOLENA-vs-ELOWEN-VISUAL-REVIEW.pdf` is the offline-review export. |
| `BRAND-SYSTEM.md`, `brand-tokens.css`, top-level `wordmark.svg`/`favicon.svg`/etc. | SUPERSEDED | The original sage/terracotta placeholder-name system, predates the naming split and the palette lock. Kept for trace, not current. |
| `outputs/landing-page/` (top-level, "GTT Center Perth" branded) | SUPERSEDED | Predates the Solena/Elowen split and the palette lock — the two named versions under `outputs/brand/{solena,elowen}/landing-page/` are current. |

---

## New Documents Created This Session (Phase 7 + audit deliverables)

| File | Purpose |
|---|---|
| `00_document_inventory.md` | This file |
| [01_conflicts_log.md](01_conflicts_log.md) | Conflict detection and resolution log (9 conflicts logged, CONFLICT-01 through 09) |
| [02_issues_and_risks.md](02_issues_and_risks.md) | Narrative gap-analysis (High/Medium/Low severity) |
| [03_improvements.md](03_improvements.md) | Process and operational improvement suggestions |
| ~~04_roadmap_next_steps.md~~ | Originally: tiered, dependency-based roadmap. **Merged into [VERIFICATION-TRACKER.md](VERIFICATION-TRACKER.md) 2026-07-29; source file archived to `archive/`.** |
| ~~05_open_questions_for_founder.md~~ | Originally: single running list of founder-only questions. **Merged into [VERIFICATION-TRACKER.md](VERIFICATION-TRACKER.md) 2026-07-29; source file archived to `archive/`.** |
| [lab-partnership-email-draft.md](lab-partnership-email-draft.md) | Corrected pathology-partner outreach email (no venture name, planning-stage framing, email-only reply ask) |
| [price-increase-comparison.md](price-increase-comparison.md) | Financial comparison of package price-increase timing options |
| [venue-manager-job-posting.md](venue-manager-job-posting.md) | Ready-to-use Venue Manager recruitment document (location-gated, not yet active) |
| ~~regulatory-accreditation-tracker.md~~ | Originally: Phase 7 — Option A regulatory/accreditation checklist with status tracking. **Merged into [VERIFICATION-TRACKER.md](VERIFICATION-TRACKER.md) 2026-07-29; source file archived to `archive/`.** |
| [swot-analysis.md](swot-analysis.md) | Phase 7 — Strengths/Weaknesses/Opportunities/Threats |
| [risk-register.md](risk-register.md) | Phase 7 — ranked risk table (likelihood × impact × mitigation × owner), distinct from [02_issues_and_risks.md](02_issues_and_risks.md)'s narrative format |
| [break-even-sensitivity-analysis.md](break-even-sensitivity-analysis.md) | Phase 7 — best/base/worst case on volume and pricing |
| [referral-partnership-plan.md](referral-partnership-plan.md) | Phase 7 — GP/OB/midwife referral strategy, named practices from [poppy-marketing.md](poppy-marketing.md) |
| [pricing-billing-strategy.md](pricing-billing-strategy.md) | Phase 7 — private vs bulk billing rationale, Medicare specifics flagged as requiring verification |
| [project-timeline-milestones.md](project-timeline-milestones.md) | Phase 7 — Gantt-style relative-sequence milestone view, no calendar dates |

## Documents Significantly Rewritten or Fixed This Session (Phase 6 verification + contradiction scan)

| File | What changed |
|---|---|
| [business-plan.md](business-plan.md) | Full currency rewrite (v3.0) — fixed Scenario B->C, dropped Package 1, removed fixed calendar milestones, surfaced new PM-profitability/market-sizing discrepancy (CONFLICT-08) |
| [executive-summary.md](executive-summary.md) | Full currency rewrite (v2.0) — made genuinely standalone per spec, fixed same stale figures as business-plan.md |
| [profit-loss-tables.md](profit-loss-tables.md) | Added Year 1 monthly ramp + Years 1-3 annual (previously Month-5+ steady-state only) |
| [cash-flow.md](cash-flow.md) | Verified spec compliance (already had full monthly + startup capital detail); flagged 3-way figure discrepancy with [pm-staffing-roster.md](pm-staffing-roster.md)/[profit-loss-tables.md](profit-loss-tables.md) |
| [equipment-costs.md](equipment-costs.md) | Added missing Beauty/Brows equipment section (§5A); added capital-vs-recurring classification; corrected 3D scan framing |
| [hire-purchase-china.md](hire-purchase-china.md) | Reframed 3D scanner as future/Phase 2 income stream, not "removed entirely" |
| [market-research-findings.md](market-research-findings.md) | Reframed 3D scan from "core differentiator" to future/Phase 2 addon |
| [ivy-booking-system.md](ivy-booking-system.md) | Fully rewritten subtenant model -> employed-staff model; fixed stale 8-client reference; removed 3D scan/dietitian from booking flow |
| [onboarding.md](onboarding.md) | All 19 "Manager" instances -> "Venue Manager" |
| [brand-guide.md](brand-guide.md) | Fixed Instagram bio/highlight icons advertising "Scan"/"Dietitian" as current services |
| [venture-timeline.md](venture-timeline.md) | Removed fixed Centre 2 date targets; removed DVA from action lists |
| [reading-order.md](reading-order.md) | Removed DVA from Open Decisions table |
| [review-audit.md](review-audit.md) | Removed DVA from Action Priority List |
| [02_issues_and_risks.md](02_issues_and_risks.md) | Removed H4 (DVA); resolved M1 (Venue Manager job posting) |
| [am-capacity-weekend.md](am-capacity-weekend.md) | Added Scenario D 09:55 verification (verified via actual event simulation) |
| [king-edward-start-time-constraint.md](king-edward-start-time-constraint.md) | Updated Scenario D recommendation per the 09:55 verification |
| [cutoff-time-CORRECTION.md](cutoff-time-CORRECTION.md) | Added WDP-emailed status + overnight-storage follow-up question |
| [reed-partnerships.md](reed-partnerships.md) | Added live outreach-status tracker; corrected email template |
| [pathology-partnership-brief.md](pathology-partnership-brief.md) | Updated status line to match outreach tracker |
| [hr-framework.md](hr-framework.md) | Added §13 Venue Manager critical-path section; MA000027 investigation (capability gap flagged) |
| [staff-plan.md](staff-plan.md) | Fixed hiring-timeline sequencing (location-gated, not "begin immediately") |
| [phlebotomist-job-posting.md](phlebotomist-job-posting.md) | Fixed same location-gating sequencing issue |
| Plus all 20 Priority 0 files from the original Imara -> Venue Manager rename (staff-plan.md, operations-manual.md, emergency-plan.md, hr-framework.md, financial-setup.md, gtt-clinical-protocol.md, patient-intake-form.md, phlebotomist-job-posting.md, team-startup.md, venture-timeline.md, grace-startup-plan.md, feasibility.md, business-plan.md, reading-order.md, review-audit.md, website-spec.md, workflow.md, poppy-marketing.md, brand-guide.md, afternoon-marketing-plan.md) plus consent-form.md, executive-summary.md, gtt-test-reference.md found via full-repo sweep | See individual changelogs in each file |

---

## Status Legend

- **CURRENT** — accurate, no known conflicts, safe to use as-is
- **CURRENT (with caveats)** — accurate but has an open question or unconfirmed figure noted inline
- **SUPERSEDED** — content has been replaced by a newer document; retained for history, do not use for current decisions
- **ARCHIVED** — explicitly retired, not applicable to current model
- **STALE / NEEDS REWRITE** — contains outdated figures/model that should be updated but has not been rewritten yet (flagged this session)

---

## Core Planning & Strategy

| File | Status | Notes |
|---|---|---|
| [business-plan.md](business-plan.md) | CURRENT (with caveats) | v2.0, Day 51 updates applied. PM model banner at top notes a further correction — see [pm-staffing-roster.md](pm-staffing-roster.md) for current PM figures. |
| [feasibility.md](feasibility.md) | CURRENT | Go/no-go assessment, Venue Manager critical-path hire noted 2026-07-19. |
| [executive-summary.md](executive-summary.md) | CURRENT (with caveats) | Contains supersession markers — verify against latest financial docs before quoting figures. |
| [investor-memorandum.md](investor-memorandum.md) | CURRENT (with caveats) | Contains supersession markers. |
| [venture-timeline.md](venture-timeline.md) | CURRENT (with caveats) | Original Week 1 "is Imara the operational manager" question formally resolved 2026-07-19 (see changelog). Some dates (Day 48-era) are historical. |
| [strategic-concerns-growth.md](strategic-concerns-growth.md) | CURRENT | Growth path, profit ceiling, interstate expansion considerations. |
| [reading-order.md](reading-order.md) | CURRENT | Document index — read this first. Updated 2026-07-19 with duplicate/superseded file flags. |
| [HANDOFF.md](HANDOFF.md) | **SUPERSEDED as "most recent"/"authoritative," corrected 2026-08-08** | 2026-07-17. Carries its own 2026-08-07 staleness banner. **No longer the authoritative source for the current model** — superseded twice since (12-client rebase 2026-07-30, then Table 1/Table 2 rebase 2026-08-05). Retained for methodology/historical detail (what worked, what didn't, regulatory findings). Use [CURRENT-STATE.md](CURRENT-STATE.md) for any current figure. |
| [agents.md](agents.md) | CURRENT | Empire agent roster for this venture. |

## Operations & Staffing

| File | Status | Notes |
|---|---|---|
| [operations-manual.md](operations-manual.md) | **CURRENT (with caveats) — status corrected 2026-08-08** | Imara->Venue Manager rename complete. GTT Scheduling Timetables section **was rewritten 2026-07-30** to the then-current 12-client model (no longer shows the old Scenario B 8-client tables — that specific gap is closed, contrary to this row's prior wording). **Not yet updated for the 2026-08-05 Table 1/Table 2 (18-/12-client) rebase — one rebase behind `docs/CURRENT-STATE.md`.** Rest of document (daily/weekly cadence, booking protocol, incident management, QC) is current. |
| [staff-plan.md](staff-plan.md) | CURRENT (with caveats) | Multiple internal supersession banners (Day 49/50/51) — read banners in order. Venue Manager critical-path hire added 2026-07-19. Headcount conclusions valid under both Scenario B and C. |
| [hr-framework.md](hr-framework.md) | CURRENT | Venue Manager critical-path hire section (§13) added 2026-07-19. |
| [financial-break-even-staff.md](financial-break-even-staff.md) | CURRENT — CANONICAL PAYROLL MODEL | v2.0, referenced as canonical by staff-plan.md and others. |
| [pm-staffing-roster.md](pm-staffing-roster.md) | CURRENT — CANONICAL PM MODEL | Supersedes PM figures in business-plan.md, staff-plan.md, operations-manual.md. |
| [team-startup.md](team-startup.md) | CURRENT | Imara's role restructured 2026-07-19 to separate ownership (Imara) from operations (Venue Manager). |
| [grace-startup-plan.md](grace-startup-plan.md) | CURRENT | 90-day startup plan. Venue Manager critical path noted 2026-07-19. |
| [emergency-plan.md](emergency-plan.md) | CURRENT | Imara->Venue Manager rename complete. Still has placeholder fields ([to be inserted]) pending venue address confirmation. |
| [gtt-clinical-protocol.md](gtt-clinical-protocol.md) | CURRENT (with caveats) | Imara->Venue Manager rename complete. Client-count updated 8->10 to match Scenario C 2026-07-19; full timetable detail lives in [scenario-c-sync-timetables.md](scenario-c-sync-timetables.md), not this file. |
| [onboarding.md](onboarding.md) | CURRENT | All 19 generic "Manager" instances corrected to "Venue Manager" for consistency (2026-07-19). |
| `staff-profiles/staff-1.md` through [staff-8.md](staff-profiles/staff-8.md), [TEMPLATE.md](staff-profiles/TEMPLATE.md) | Not reviewed this pass | Individual staff persona/profile templates — out of scope for Imara rename (no operational Imara references expected) and Scenario B/C (not schedule-specific). |

## Financial

| File | Status | Notes |
|---|---|---|
| [financial-model.md](financial-model.md) | **RESOLVED 2026-07-29 — split, not archived whole** | Was previously marked "SUPERSEDED (self-declared)" in full. Opened and checked directly per Anthony's instruction: contained both stale P&L content and still-relevant trust/tax content. Stale P&L section archived to `archive/financial-model-superseded-pnl-section-2026-06-11.md`; trust/tax-treatment content kept live in `financial-model.md` v3.0 (renamed in scope, not filename, to "Trust Structure & Tax Treatment") with dollar figures flagged as needing a re-run against current P&L. No longer "untouched" — see that document's own 2026-07-29 changelog. |
| [cash-flow.md](cash-flow.md) | CURRENT (methodology) — **absolute figures stale, flagged 2026-08-08** | v2.0, fully rebuilt 2026-07-20 against the then-current model (2 packages, individual PM services, 10-client AM cap) — that AM cap is now historical, superseded twice (12-client 2026-07-30, Table 1/Table 2 2026-08-05); dollar figures have not been re-run against the current model. Methodology (18-month structure, GST-apportionment flag) still valid. Flags ancillary-revenue sourcing and a likely GST-apportionment inconsistency needing accountant confirmation. |
| [profit-loss-tables.md](profit-loss-tables.md) | CURRENT — CANONICAL | v2.0, conservative baseline, no Sunday trading. |
| [unit-economics.md](unit-economics.md) | CURRENT (with caveats) | Verify PM figures against [pm-staffing-roster.md](pm-staffing-roster.md). |
| [capacity-pricing-audit.md](capacity-pricing-audit.md) | CURRENT (with caveats) | Contains correction markers — read in full before quoting. |
| [services-pricing-locked.md](services-pricing-locked.md) | CURRENT — CANONICAL PRICING | Package 1 (A$250, fixed 2×30min) + Package 2 (A$300, flexible composition), renumbered 2026-07-20 — same 2 price points as before. |
| [services-master-table.md](services-master-table.md) | CURRENT | Service list/durations. |
| [financial-setup.md](financial-setup.md) | CURRENT | Imara->Venue Manager rename complete for operational duties; Imara's personal remuneration question retained. |
| [equipment-costs.md](equipment-costs.md) | CURRENT (Phase 6 reviewed) | v1.2 — added missing Beauty/Brows section, capital-vs-recurring classification. |
| [hire-purchase-china.md](hire-purchase-china.md) | CURRENT (with caveat) | 3D scanner section reframed as future/Phase 2 reference material, not a current purchase decision. |

## Clinical & Pathology

| File | Status | Notes |
|---|---|---|
| [gtt-test-reference.md](gtt-test-reference.md) | CURRENT (with caveat, reviewed via full-repo Imara sweep) | Imara reference fixed; Scenario B/C client-count flag added. |
| [inhouse-gtt-research.md](archive/inhouse-gtt-research.md) | ARCHIVED | In-house lab rejected per reading-order.md. |
| [option-b-collection-centre.md](option-b-collection-centre.md) | Reference / contingency | Covers the NATA-accreditation "Option B" path, not the current Option A (WDP/PathWest partner) launch model. Cross-referenced from [VERIFICATION-TRACKER.md](VERIFICATION-TRACKER.md). |
| [pathology-collection-room.md](pathology-collection-room.md) | CURRENT | Room spec for collection room build. |
| [pathology-partnership-brief.md](pathology-partnership-brief.md) | CURRENT | Status updated 2026-07-19 — WDP emailed/awaiting reply, PathWest/Clinipath not yet contacted. |
| [patient-intake-form.md](patient-intake-form.md) | CURRENT | Imara->Venue Manager rename complete. |
| [consent-form.md](consent-form.md) | CURRENT (reviewed via full-repo Imara sweep) | Imara reference fixed. |
| [cutoff-time-CORRECTION.md](cutoff-time-CORRECTION.md) | CURRENT — ACTIVE OPEN QUESTION | WDP courier cutoff time (11:30 vs 12:30) never formally confirmed. See open questions doc. |
| [king-edward-start-time-constraint.md](king-edward-start-time-constraint.md) | CURRENT — ACTIVE OPEN QUESTION | KEMH "start before 10am" guidance not independently source-verified. Scenario C passes; Scenario D fails on strict reading. |

## Scheduling / Scenario Analysis (chronological — read newest first)

| File | Status | Notes |
|---|---|---|
| [am-capacity-weekend.md](am-capacity-weekend.md) | CURRENT (with caveats) — PARTIALLY SUPERSEDED | Contains Scenario B, staggered Scenario C, and Scenario D analysis. The staggered Scenario C timetable within this file is itself superseded by [scenario-c-sync-timetables.md](scenario-c-sync-timetables.md) (see line ~405 of this file, which confirms the sync variant). Still valuable for methodology, weekend trading rationale, and Scenario D. |
| [scenario-c-sync-timetables.md](scenario-c-sync-timetables.md) | **CURRENT — CANONICAL LAUNCH TIMETABLE** | Originally 2026-07-17, synchronized-chair-start, 10 clients/day (now historical). **Updated 2026-08-08 note: this file has been kept current through every rebase since — it now also houses the 2026-08-05 Table 1 (18-client, PRIMARY) / Table 2 (12-client, SECONDARY) tables, per `docs/CURRENT-STATE.md` §0.6a.** Programmatically verified zero double-bookings at every stage. This is the timetable operations-manual.md and gtt-clinical-protocol.md should be pointing to (partially done — see conflicts log; operations-manual.md itself is one rebase behind, see its own row above). |
| [scenario-c-sync-timeline.html](scenario-c-sync-timeline.html) | CURRENT | Visual companion to scenario-c-sync-timetables.md — not independently verified this session but no reason to doubt given recency. |
| [scenario-c-timeline.html](scenario-c-timeline.html) | Likely SUPERSEDED | Visual companion to the staggered (pre-sync) Scenario C — same status question as am-capacity-weekend.md's staggered table. Not renamed/flagged this session — recommend follow-up. |
| [scenario-c-sync-timetables.md](scenario-c-sync-timetables.md) (duplicate mention) | — | (listed once above) |
| [scenario-d-investigation.md](scenario-d-investigation.md) | CURRENT — GROWTH SCENARIO, NOT COMMITTED | 15 clients/day, 3rd phlebotomist. Growth lever, not current launch model. |
| [scenario-d-demand-analysis.md](scenario-d-demand-analysis.md) | CURRENT — GROWTH SCENARIO | Demand/catchment analysis for Scenario D. |
| [draw-event-scheduler-findings.md](draw-event-scheduler-findings.md) | CURRENT | Solver-based (not manual) scheduling verification — supports both staggered and sync Scenario C results. |
| [booking-service-capacity-rule.md](booking-service-capacity-rule.md) | CURRENT | General booking rule, scenario-agnostic. |
| [multirole-CORRECTION.md](multirole-CORRECTION.md) | CURRENT — CORRECTION LOG | Multi-role headcount correction (7 not 6). |

## Marketing & Brand

| File | Status | Notes |
|---|---|---|
| [poppy-marketing.md](poppy-marketing.md) | CURRENT | Imara founder-story references reviewed and correctly retained 2026-07-19. |
| [afternoon-marketing-plan.md](afternoon-marketing-plan.md) | CURRENT | Imara->Venue Manager rename complete for operational outreach duties. |
| [brand-guide.md](brand-guide.md) | CURRENT | Imara founder-role references reviewed and correctly retained 2026-07-19. |
| [website-spec.md](website-spec.md) | CURRENT | Imara->Venue Manager rename complete (contact form routing). |
| [extended-wellness-services.md](extended-wellness-services.md) | CURRENT (reviewed via contradiction scan) | Fixed one stale cross-reference to archived [bloom-baby-case-study.md](archive/bloom-baby-case-study.md). |
| [reed-partnerships.md](reed-partnerships.md) | CURRENT | Added live outreach-status tracker; corrected the pathology outreach email template. |

## Location / Physical Space

| File | Status | Notes |
|---|---|---|
| [location-scouting.md](location-scouting.md) | CURRENT | Per HANDOFF.md, "all current, no known stale figures" (2026-07-17). |
| [floor-plan-concept.md](floor-plan-concept.md) | CURRENT | Text room schedule, 2026-07-01. Room list consistent across v2/v3 visuals. |
| [floor-plan-v3.svg](floor-plan-v3.svg) / [floor-plan-v3.pdf](floor-plan-v3.pdf) | **CURRENT** | v3, 2026-07-10 — open-plan lounge, furniture, accessible door swing arcs. Canonical per HANDOFF.md. |
| [floor-plan-visual.html](archive/floor-plan-visual.html) / [floor-plan-visual.pdf](archive/floor-plan-visual.pdf) | SUPERSEDED (flagged 2026-07-19) | v2, 2026-07-01 — box-fill room layout. Superseded banner added to the HTML file. PDF is a binary export of the same v2 content — cannot be text-edited; status recorded in [reading-order.md](reading-order.md) and this inventory instead. |

## Compliance & Legal

| File | Status | Notes |
|---|---|---|
| [privacy-policy.md](privacy-policy.md) | CURRENT (reviewed via contradiction scan) | No issues found. |
| [dva-tpi-research.md](dva-tpi-research.md) | UNTOUCHED (per instruction) | Covers Imara's personal TPI/DVA implications — explicitly out of scope for the Imara->Venue Manager operational rename. |
| [research.md](research.md) | UNTOUCHED (per instruction) | v3.0, comprehensive research doc, covers trust/ownership structure among other things. |
| [market-research-findings.md](market-research-findings.md) | CURRENT (with caveat) | 3D scan reframed from "core differentiator" to future/Phase 2 addon; market-sizing discrepancy with feasibility.md flagged, not resolved (CONFLICT-08). |

## Audit / QC / Meta

| File | Status | Notes |
|---|---|---|
| [review-audit.md](review-audit.md) | CURRENT | Full business audit. Imara/Venue Manager distinction clarified 2026-07-19 in CF-07 and OG-03. DVA removed from Action Priority List. |
| [ivy-booking-system.md](ivy-booking-system.md) | CURRENT | Fully rewritten from subtenant model to employed-staff model; fixed stale 8-client reference; removed 3D scan/dietitian from booking flow. |
| [workflow.md](workflow.md) | CURRENT (with caveats) | Imara->Venue Manager rename complete. Staffing model in this doc (sublet massage/nails/hair/scan) is an early draft — superseded by staff-plan.md's employed-staff model. See conflicts log — still flagged, not rewritten (CONFLICT-04). |

## Duplicates / Archived

| File | Status | Notes |
|---|---|---|
| [research-supplement-day48-ARCHIVED.md](archive/research-supplement-day48-ARCHIVED.md) | ARCHIVED (correctly labelled) | Merged into research.md v3.0. |
| [research-supplement-day48.md](archive/research-supplement-day48.md) | ARCHIVED (flagged 2026-07-19) | Byte-identical duplicate of the file above, left over from the merge — was never renamed/removed. Superseded banner added. |
| [bloom-baby-case-study.md](archive/bloom-baby-case-study.md) | ARCHIVED | 3D scan removed from scope entirely (Day 51). |
| [inhouse-gtt-research.md](archive/inhouse-gtt-research.md) | ARCHIVED | In-house lab rejected. |

---

## Summary Counts (Updated After Phase 6/7 Pass — **stale as of 2026-08-08, not recounted this pass, see correction note at top of file**)

| Status | Count (approx.) |
|---|---|
| CURRENT / CURRENT (with caveats) | ~65 (up from ~48 — the "not reviewed this pass" backlog has been cleared) |
| New Phase 7 documents | 7 ([VERIFICATION-TRACKER.md](VERIFICATION-TRACKER.md), [swot-analysis.md](swot-analysis.md), [risk-register.md](risk-register.md), [break-even-sensitivity-analysis.md](break-even-sensitivity-analysis.md), [referral-partnership-plan.md](referral-partnership-plan.md), [pricing-billing-strategy.md](pricing-billing-strategy.md), [project-timeline-milestones.md](project-timeline-milestones.md)) |
| New audit-deliverable documents (00-05 + supporting) | 8 (`00_document_inventory.md`, [01_conflicts_log.md](01_conflicts_log.md), [02_issues_and_risks.md](02_issues_and_risks.md), [03_improvements.md](03_improvements.md), [VERIFICATION-TRACKER.md](VERIFICATION-TRACKER.md), [VERIFICATION-TRACKER.md](VERIFICATION-TRACKER.md), [lab-partnership-email-draft.md](lab-partnership-email-draft.md), [price-increase-comparison.md](price-increase-comparison.md), [venue-manager-job-posting.md](venue-manager-job-posting.md)) |
| SUPERSEDED (self-declared or flagged this session) | ~6 |
| STALE / NEEDS REWRITE (flagged, not yet fixed) | 2 ([operations-manual.md](operations-manual.md) scheduling section; [scenario-c-timeline.html](scenario-c-timeline.html) likely; [workflow.md](workflow.md) staffing table also still flagged, CONFLICT-04) |
| ARCHIVED | 4 |
| Not reviewed this pass | 0 — the entire "not reviewed this pass" backlog from the original audit was cleared during the Phase 6/7 verification and contradiction-scan passes |
| Untouched by explicit instruction (ownership/trust scope) | 2 (dva-tpi-research.md, research.md). **financial-model.md removed from this list 2026-07-29** — opened and split per Anthony's direct instruction (no longer "untouched"), see its row above and its own changelog. |

**Nine conflicts logged and tracked in [01_conflicts_log.md](01_conflicts_log.md) (CONFLICT-01 through 09).** Six resolved/fixed this session; three remain flagged and unresolved (CONFLICT-03/04 — documentation rewrites recommended as follow-up; CONFLICT-08/09 — financial figure and payment-policy reconciliation needed, recommended as priority follow-up work, not founder decisions).

---

## Changelog

**2026-07-19 (Phase 6/7 pass)** — Updated this inventory to reflect: 12 new documents created (6 Phase 7 deliverables + [lab-partnership-email-draft.md](lab-partnership-email-draft.md), [price-increase-comparison.md](price-increase-comparison.md), [venue-manager-job-posting.md](venue-manager-job-posting.md), plus this file/01/02/03/04/05 from the earlier audit pass), and every "not reviewed this pass" file from the original audit now reviewed and fixed where needed ([equipment-costs.md](equipment-costs.md), [hire-purchase-china.md](hire-purchase-china.md), [gtt-test-reference.md](gtt-test-reference.md), [consent-form.md](consent-form.md), [privacy-policy.md](privacy-policy.md), [market-research-findings.md](market-research-findings.md), [ivy-booking-system.md](ivy-booking-system.md), [extended-wellness-services.md](extended-wellness-services.md), [reed-partnerships.md](reed-partnerships.md), [onboarding.md](onboarding.md), `staff-profiles/*.md`). Updated summary counts accordingly. Skipped from Phase 7 spec: none — all 7 requested Phase 7 documents were built. See `docs/04_roadmap_next_steps.md` for what remains as follow-up work (CONFLICT-03/04/08/09).

**2026-07-20 (package renumbering)** — Updated the [HANDOFF.md](HANDOFF.md) and [services-pricing-locked.md](services-pricing-locked.md) entries to reflect the 2026-07-20 package renumbering (new Package 1 = A$250 fixed 2×30min, new Package 2 = A$300 flexible composition) — same 2 price points as the prior "Package 2/3" naming, renamed only.

**2026-07-20 (hyperlink sweep)** — Converted every backtick-wrapped filename reference in this document to a clickable relative markdown hyperlink, per the repo-wide hyperlink rule.

**2026-07-20 (cash-flow.md status updated)** — Updated the `cash-flow.md` status-table entry to reflect its full rebuild this session (v2.0) — no longer flagged as carrying a stale 3-way figure discrepancy, since that discrepancy has now been fixed at the source rather than just flagged.

**2026-07-29 (external audit response — archive, don't flag)** — An outside reviewer found that this repo's process of adding a "SUPERSEDED"/"ARCHIVED" banner without physically moving the file (see [operations-manual.md](operations-manual.md)'s Scenario B section, left in place for 10 days after being flagged) had itself caused a real staff-training risk. Actioned this session: every file already marked SUPERSEDED/ARCHIVED in this inventory as of 2026-07-19 has now been physically moved to `docs/archive/` via `git mv` (history preserved) — [inhouse-gtt-research.md](archive/inhouse-gtt-research.md), [research-supplement-day48-ARCHIVED.md](archive/research-supplement-day48-ARCHIVED.md), [research-supplement-day48.md](archive/research-supplement-day48.md), [bloom-baby-case-study.md](archive/bloom-baby-case-study.md), [floor-plan-visual.html](archive/floor-plan-visual.html), [floor-plan-visual.pdf](archive/floor-plan-visual.pdf). All in-repo links/references to these 6 files updated to the new path (verified via grep sweep, [research.md](research.md) left untouched — protected file, its one reference is a historical "supersedes" note, not a live pointer). **Update 2026-07-29 (later same session):** [financial-model.md](financial-model.md) was initially left as an open, unresolved conflict (it met the literal archive criteria but was also one of 3 files marked out-of-scope/untouched per an earlier session's instruction). Anthony directly instructed this be checked and resolved rather than left open — opened the file, confirmed it mixed stale P&L content with still-relevant trust/tax-treatment content, and **split it**: stale P&L archived to `archive/financial-model-superseded-pnl-section-2026-06-11.md`, trust/tax content kept live in `financial-model.md` v3.0. See that document's own row above and changelog for full detail. [operations-manual.md](operations-manual.md)'s Scenario B section (the file the review specifically named) was not archived as a separate file — it was rewritten in place with the current Scenario C model inlined, since it's one section of an otherwise-current document, not a standalone stale file. See `docs/CURRENT-STATE.md` (new this session) for the single canonical numbers file every other document now points to instead of re-stating figures independently.

**2026-08-15 (repository consolidation — the strategy/brand/venue/naming layer added, root cause of "flying blind" fixed)** — A dedicated execution audit found this file had no entry anywhere for `docs/strategy/`, `docs/naming/`, `docs/experience/`, `docs/DECISION-LOG.md`, or `outputs/brand/` — a real, current, actively-maintained ~30-file layer built 2026-08-05 through 2026-08-15, entirely invisible to anyone using this inventory as their map. Added the new "Strategy / Brand / Venue / Naming Layer" section above (with its own, more actionable status vocabulary: COMPLETE / CURRENT-CANONICAL / IN PROGRESS / WAITING / BLOCKED / FOUNDER ACTION / EXTERNAL ACTION / DEFERRED / SUPERSEDED) rather than rewriting the rest of this file, which still accurately describes the `docs/*.md` layer. Also flagged (not rewritten in place) that `docs/executive-summary.md` and `docs/investor-memorandum.md` cited a Net P&L figure two model-generations stale — both corrected directly at their specific figure locations only, see those files' own 2026-08-15 changelog/banner entries.

**2026-08-15/16 (External Execution Round — 5 new outputs added)** — Added the new "External Execution Round (2026-08-15/16)" section above, listing the 5 deliverables built this round: the reskinned public-ready landing page, the external-facing venture overview pack, 3 professional outreach drafts (accountant, insurance, Fair Work), the startup-cost-reduction action table, and the AM->PM data-capture specification. Also added a row for the data-capture spec to the existing Experience table. All 5 items are committed locally, not yet pushed — see this repo's own `git log` for the exact commit hashes.

**2026-08-08 (F-2 correction — this file's own status rows brought back in line with `docs/CURRENT-STATE.md`)** — `docs/architecture/REPOSITORY-AUDIT.md` found this file's rows for `HANDOFF.md`, `operations-manual.md`, `scenario-c-sync-timetables.md`, and `cash-flow.md` still described the 2026-07-19/20 model (8- or 10-client, HANDOFF.md as "most recent"/"authoritative"), two rebases behind `CURRENT-STATE.md`'s current figures. Corrected each row individually (see the rows themselves for full detail); notably, `operations-manual.md`'s status improved from "STALE / NEEDS REWRITE" to "CURRENT (with caveats)" because its scheduling section actually was rewritten 2026-07-30 (the file itself was accurate, this inventory's description of it was not) — it is however now one rebase behind in turn (not yet updated for the 2026-08-05 Table 1/Table 2 change). The file-count header and the Summary Counts table were flagged as unverified rather than recounted, in the interest of a bounded correction pass rather than a full re-audit. **No decision was made on the still-open Table 1 vs. Table 2 primary/secondary question** — nothing in this file states a preference either way.
