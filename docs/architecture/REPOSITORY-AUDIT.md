# GTT Center Perth — Repository Audit

**Compiled:** 2026-08-08 | **Scope:** Architecture-only planning phase (see `docs/architecture/TARGET-ARCHITECTURE.md`). This audit categorises the repo as it exists today. **No file was deleted, archived, or rewritten to produce this document.** Where this audit would normally recommend archiving a file (per `rules/CLAUDE.md` companion rule 1, "archive, don't flag"), it instead flags it — see the note at the end of this file and the fuller discussion in the final report.

**Method:** Read every top-level directory, `docs/00_document_inventory.md`, `docs/01_conflicts_log.md`, `docs/CURRENT-STATE.md`, `docs/VERIFICATION-TRACKER.md`, `rules/CLAUDE.md`, `tools/check_consistency.py`, all six `tools/*.py` scripts, `README.md`, and `agents/*.md`. Categorisation below is derived from that reading, cross-checked against the two existing conflict/inventory logs rather than re-litigated from scratch.

---

## 1. Repository Shape

```
gtt-center-perth/
├── CLAUDE.md                  root agent context (Grace) — skills, governance pointers, standing facts
├── README.md                  repo front page — STALE, see §6 finding F-1
├── .claude/skills/             5 activated skills (tax/business/financial/property-AU advisory, stop-slop) + stop-slop refs
├── agents/                     8 agent persona files (grace, ivy, reed, poppy, bruno, cora, fern, jade)
├── rules/
│   └── CLAUDE.md                venture governance rules — VERIFIED/MODELED/PLACEHOLDER tagging, "archive don't flag"
├── docs/                        98 markdown files + 4 non-markdown (2 SVG/PDF pairs, 2 HTML) + 9 staff-profile files
│   ├── CURRENT-STATE.md          canonical numbers file (created 2026-07-29, most recently updated 2026-08-08)
│   ├── VERIFICATION-TRACKER.md   canonical open-items ledger (created 2026-07-29, most recently updated 2026-08-08)
│   ├── 00_document_inventory.md  full file-by-file status list — LAST UPDATED 2026-07-20, see F-2
│   ├── 01_conflicts_log.md       conflict detection/resolution log — LAST UPDATED 2026-07-20, see F-2
│   ├── 02_issues_and_risks.md    narrative gap analysis
│   ├── 03_improvements.md        process improvement suggestions
│   ├── reading-order.md          single navigational entry point — LAST UPDATED 2026-07-20, see F-2
│   ├── HANDOFF.md                2026-07-17 session handoff, self-described as "MOST RECENT SESSION SUMMARY" (no longer true)
│   ├── staff-profiles/            8 persona files + 1 TEMPLATE.md
│   └── archive/                   10 files already archived (6 original + this session finds no new ones added since)
└── tools/                       6 Python scripts — see §4
```

**Total corpus:** ~20,000 lines across `docs/*.md` alone (`wc -l docs/*.md` = 19,956), plus agent files, skills, and tools. This is a mature, heavily-iterated markdown research/planning repo, not a blank slate.

---

## 2. Document Categories (what's actually in `docs/`)

| Category | Representative files | Count (approx) |
|---|---|---|
| **Canonical/governance** | `CURRENT-STATE.md`, `VERIFICATION-TRACKER.md`, `rules/CLAUDE.md` | 3 |
| **Meta/audit/navigation** | `00_document_inventory.md`, `01_conflicts_log.md`, `02_issues_and_risks.md`, `03_improvements.md`, `reading-order.md`, `HANDOFF.md`, `review-audit.md` | 7 |
| **Core planning & strategy** | `business-plan.md`, `feasibility.md`, `executive-summary.md`, `investor-memorandum.md`, `swot-analysis.md`, `strategic-concerns-growth.md`, `venture-timeline.md`, `gtt-center-perth-overview-for-imara.md` | 8 |
| **Financial** | `financial-model.md`, `cash-flow.md`, `profit-loss-tables.md`, `unit-economics.md`, `capacity-pricing-audit.md`, `services-pricing-locked.md`, `financial-setup.md`, `equipment-costs.md`, `break-even-sensitivity-analysis.md`, `price-increase-comparison.md`, `revenue-extraction-options.md`, `rent-budget-2026-07-28.md` | 12 |
| **Services & pricing** | `services-master-table.md`, `services-pricing-locked.md` (dup-listed), `extended-wellness-services.md`, `pm-package-structure.md` | 4 |
| **Clinical & pathology** | `gtt-clinical-protocol.md`, `gtt-test-reference.md`, `pathology-collection-room.md`, `pathology-partnership-brief.md`, `patient-intake-form.md`, `consent-form.md`, `cutoff-time-CORRECTION.md`, `king-edward-start-time-constraint.md`, `multirole-CORRECTION.md` | 9 |
| **Scheduling / scenario analysis** | `scenario-c-sync-timetables.md`, `scenario-d-investigation.md`, `scenario-d-demand-analysis.md`, `scenario-e-floating-chair-investigation.md`, `am-capacity-weekend.md`, `am-staffing-by-volume.md`, `draw-event-scheduler-findings.md`, `booking-service-capacity-rule.md`, `scenario-comparison-master-2026-08.md`, `dual-role-staffing-model-2026-07-28.md`, `capacity-pricing-audit.md` (dup-listed) | 11 |
| **Operations & staffing** | `operations-manual.md`, `workflow.md`, `staff-plan.md`, `hr-framework.md`, `team-startup.md`, `grace-startup-plan.md`, `pm-staffing-roster.md`, `pm-casual-roles-job-posting.md`, `financial-break-even-staff.md`, `financial-break-even-staff.md` (dup-listed), `am-staffing-by-volume.md` (dup-listed) | 8 |
| **Equipment & sourcing** | `equipment-costs.md` (dup-listed), `hire-purchase-china.md` | 2 |
| **Partnerships & correspondence** | `reed-partnerships.md`, `pathology-partnership-brief.md` (dup-listed), `lab-partnership-email-draft.md`, `lab-outreach-2026-07-28.md`, `pathwest-clinipath-outreach-2026-07-27.md`, `wdp-reply-carole-2026-07-30.md`, `wdp-reply-carole-2026-08-03.md`, `wdp-reply-carole-2026-08-07.md`, `partner-profitability-brief.md`, `referral-partnership-plan.md`, `ivy-booking-system.md` | 11 |
| **Location / physical space** | `location-scouting.md`, `property-links-2026-07-28.md`, `floor-plan-concept.md`, `floor-plan-v3.svg/.pdf`, `reference-floorplans-2026-07-28.md`, `standards-floorplan-crosscheck-2026-07-28.md` | 6 |
| **Marketing & brand** | `poppy-marketing.md`, `afternoon-marketing-plan.md`, `brand-guide.md`, `website-spec.md` | 4 |
| **Compliance & legal** | `privacy-policy.md`, `emergency-plan.md`, `industry-standards-reference-2026-07-28.md` | 3 |
| **Research (protected/untouched by prior sessions' own scope)** | `research.md`, `dva-tpi-research.md`, `market-research-findings.md` | 3 |
| **Recruitment** | `receptionist-job-posting.md`, `phlebotomist-job-posting.md`, `venue-manager-job-posting.md`, `pm-casual-roles-job-posting.md` (dup-listed) | 3 |
| **Timeline/milestones** | `project-timeline-milestones.md` | 1 |
| **Staff persona templates** | `staff-profiles/staff-1.md`–`staff-8.md`, `staff-profiles/TEMPLATE.md` | 9 |
| **Non-markdown generated visuals** | `scenario-c-sync-timeline.html`, `scenario-c-timeline.html`, `floor-plan-v3.svg`, `floor-plan-v3.pdf` | 4 |
| **Already archived** | `docs/archive/*` — 10 files | 10 |

(Some files legitimately span two categories — dup-listed above rather than force a single bucket.)

---

## 3. Existing Claude/Agent Instructions

- **Root `CLAUDE.md`** (this venture's Grace agent-context file) — skills activation record, working principles, standing facts, and pointers to `rules/CLAUDE.md` + `docs/CURRENT-STATE.md` + `docs/VERIFICATION-TRACKER.md`. Actively maintained (last standing-fact update 2026-08-05).
- **`rules/CLAUDE.md`** — venture-scoped governance: the VERIFIED/MODELED/PLACEHOLDER tagging system, the "archive don't flag" rule, canonical-file pointers, changelog. Created 2026-07-29 in direct response to an external repo review.
- **`agents/*.md`** — 8 persona files (grace, ivy, reed, poppy, bruno, cora, fern, jade) defining each agent's role, not consulted further in this audit (out of scope — this phase concerns documents/data/models, not agent roster).
- **`.claude/skills/`** — 5 skills copied in from the empire shared library (australian-tax-accounting, business-advisory-australia, financial-planning-australia, property-investment-australia, stop-slop), activation verified 2026-07-19 per `CLAUDE.md`.

---

## 4. Existing Python Tools

| Script | Purpose | Architecture-readiness |
|---|---|---|
| `tools/check_consistency.py` | Grep-based sweep of `docs/*.md` (excluding `docs/archive/`) for known-stale figures, cross-referenced against a hardcoded list of "canonical vs stale" regex pairs sourced from `docs/CURRENT-STATE.md`. | **Reusable as-is** — this is the one tool in the repo already built as a standing, re-runnable check rather than a one-off script. Its `CHECKS` list is hand-maintained in the script itself, not sourced from a machine-readable canonical file — a coupling point noted in `VALIDATION-ARCHITECTURE.md`. |
| `tools/draw-event-scheduler.py` | Solver: finds the maximum client count for a given start-time/cutoff constraint via a multi-resolution sweep. Produced the "14-client PROVEN CEILING" and "18-client Table 1" findings cited in `CURRENT-STATE.md`. | One-off script, correct and rigorous, but **not parameterized** — durations/tolerances are hardcoded constants in the docstring/code, not read from any shared data file. |
| `tools/multirole-analysis.py` | Answers 3 specific staffing-concurrency questions for the (now-historical) 10-client synchronized timetable via sweep-line peak-concurrency. | One-off script. Client/interval data (`clients_x`, chair assignment) is a **hardcoded dict in the file**, specific to one scenario — the same logic re-run for Table 1/Table 2 required writing new, separate scripts rather than re-parameterizing this one. |
| `tools/scenario-d-staff-solver.py` | Fixed a sweep-line concurrency bug from an earlier (unfound/lost) version, computes staffing for Scenario D. | Same pattern — hardcoded `clients_x`/`chair_of` dicts. |
| `tools/scenario-d-staffing.py` | Scenario D (15 clients, 3 chairs) staffing/load model, imports `multirole_analysis.peak_concurrent`/`fmt`. | Same pattern — the one script with a cross-file import, showing informal reuse already happening organically. |
| `tools/sync-treatment-solver.py` | Verifies treatment-staff feasibility under synchronized chair starts for the historical 10-client model. | Same pattern — hardcoded `slots`/`chairs` lists specific to one scenario. |

**Finding:** all six scripts are genuine, rigorous, independently-verified solvers (the two-method cross-check pattern — sweep-line peak concurrency + greedy first-fit — recurs throughout `CURRENT-STATE.md` and traces back to these scripts). But **every script hardcodes its own scenario's input data** rather than reading from a shared source. Re-running the same methodology against a new scenario (e.g. the 2026-08-05 Table 1/Table 2 rebase) required writing new one-off scripts rather than re-parameterizing existing ones — this is exactly the gap `MODEL-ARCHITECTURE.md`'s Master Operations Model section addresses.

---

## 5. Existing Templates and Generated Files

- **Templates:** `docs/staff-profiles/TEMPLATE.md` is the only explicit template file. `emergency-plan.md`, `privacy-policy.md`, `consent-form.md` are draft-with-blanks documents (governed by `rules/CLAUDE.md` companion rule 5 — placeholders must stay honest blanks, never fabricated) — these function as templates in effect, though not labelled as such.
- **Generated visuals:** `floor-plan-v3.svg`/`.pdf`, `scenario-c-sync-timeline.html`, `scenario-c-timeline.html` are hand-built (SVG/HTML authored directly), not code-generated from a data source. There is currently no pipeline anywhere in this repo that produces a visual/document artifact from structured data — every visual output found was authored by hand.
- **No XLSX/DOCX/PDF generation pipeline exists.** `floor-plan-v3.pdf` and the archived `floor-plan-visual.pdf` are binary exports of hand-authored source files, not generated reports.

---

## 6. Authoritative vs Historical vs Duplicated vs Obsolete vs Contradictory

### Authoritative (current canonical sources, per the repo's own governance)
- `docs/CURRENT-STATE.md` — canonical numbers (pricing, capacity, headcount, P&L, startup capital), most recently updated 2026-08-08.
- `docs/VERIFICATION-TRACKER.md` — canonical open-items ledger, most recently updated 2026-08-08.
- `rules/CLAUDE.md` — canonical governance rules.
- `docs/scenario-c-sync-timetables.md` — canonical scheduling model (houses both the historical 10/12/14-client tables and the current Table 1/Table 2 model).
- `docs/services-pricing-locked.md` — canonical pricing (though its content is now a subset of `CURRENT-STATE.md` §2 — a candidate for becoming a pure pointer, see F-3 below).
- `docs/profit-loss-tables.md`, `docs/financial-break-even-staff.md`, `docs/equipment-costs.md`, `docs/pm-staffing-roster.md` (staffing structure only, not its own P&L figures) — the detailed-calculation documents that feed `CURRENT-STATE.md`'s summary figures.

### Historical (retained for trace, explicitly marked, per the "archive, don't flag" rule already being followed correctly for numeric content)
- The 12-client/23-minute-cadence model and its 14-client "proven ceiling" — retained in full inside `CURRENT-STATE.md` itself under "Historical, superseded 2026-08-05" headers. This is the tagging system working as designed: numbers, not whole files.
- The 10→12→14→18-client evolution chain visible across `docs/VERIFICATION-TRACKER.md`'s changelog — a genuine, well-documented iteration history, not clutter.

### Duplicated
- **Three separate navigational "entry point" documents** (`reading-order.md`, `00_document_inventory.md`, `HANDOFF.md`) with overlapping purpose (all three claim to be where a new reader should start), none of which has been updated since the 2026-08-05/08-08 financial rebase (see F-2 below) — this is navigation-layer duplication, not numeric duplication, but it means three different documents currently give three different pictures of "what's current."
- `docs/00_document_inventory.md`'s own reading-order table lists `VERIFICATION-TRACKER.md` twice (rows 12/70) — a leftover artifact from the pre-merge `04_roadmap_next_steps.md`/`05_open_questions_for_founder.md` split, not corrected when those two files were merged into one.

### Obsolete (already correctly archived)
- `docs/archive/*` — 10 files, all with clear supersession banners and correct in-repo cross-references, per `docs/00_document_inventory.md`'s 2026-07-29 changelog entry describing the archive sweep. No new obsolete files were found un-archived beyond what's flagged below.

### Contradictory (cross-checked against `docs/01_conflicts_log.md` and `docs/CURRENT-STATE.md`'s own open items)
See §6.1 New Findings below and the existing, still-open conflicts already tracked in `docs/01_conflicts_log.md` (CONFLICT-03, CONFLICT-04) and `docs/VERIFICATION-TRACKER.md` (item 1m's framing flag, item 6's unreconciled startup-capital ranges).

---

## 6.1 New Findings This Audit (not previously logged)

**F-1 — `README.md` (repo root) contradicts the confirmed operating model, more visibly than any file already flagged.**
The root `README.md`'s "Model" section states: *"Services: Sublet chairs/rooms to self-employed practitioners (massage, nails, hair)"* and *"3D Scan: Sublet scan room to existing Perth keepsake operator."* This is the pre-Day-51 subtenant model. The confirmed, current model (per `CLAUDE.md`'s Standing Facts, `docs/CURRENT-STATE.md` throughout, and `docs/staff-plan.md`) is **employed staff, no subtenants** — the exact same issue already logged as CONFLICT-04 against `workflow.md`, but never checked against `README.md`, which is the single most likely file a new reader (or this session) opens first. `README.md`'s Onboarding Checklist is also stale — it shows `[x]` for "Business plan written" with no reference to the 2026-08-05 rebase, and does not reflect the venture's `STANDBY` activation-trigger status described in `agents/grace.md`.

**F-2 — The meta/navigation layer has itself gone stale relative to `CURRENT-STATE.md`, mirroring the exact failure pattern `CURRENT-STATE.md` was built to prevent, one layer up.**
`docs/reading-order.md`, `docs/00_document_inventory.md`, and `docs/01_conflicts_log.md` are all dated 2026-07-20 (their own changelogs confirm this) and describe the **10-client/A$25,087-per-month model** as current — both figures are now two rebases behind (10→12→18 clients; +A$25,087→+A$27,085→+A$63,029/month). `docs/HANDOFF.md` still self-describes as "MOST RECENT SESSION SUMMARY" though it is dated 2026-07-17, three weeks and multiple rebases old. None of these three files carries a `[VERIFIED]`/`[MODELED]`/`[PLACEHOLDER]` tag system themselves (they predate `rules/CLAUDE.md`), so `tools/check_consistency.py` — which only scans for specific known-stale numeric patterns — does not currently catch prose in these particular files describing an outdated model in general terms (vs. quoting a specific stale figure). This is a genuine gap: the canonical-numbers fix (`CURRENT-STATE.md`) solved the "which number is true" problem but the navigation layer that tells a reader *which document to trust first* was not brought into the same discipline.

**F-3 — `services-pricing-locked.md` is now a strict subset of `CURRENT-STATE.md` §2, a candidate for becoming a pointer-only file once the canonical-data layer exists.**
Both files state the same two figures (Package 1 = A$250, Package 2 = A$300) with the same tags. This is not currently a contradiction (values agree), but it is a second place a future price change would need editing — the same duplication risk `rules/CLAUDE.md` was written to eliminate for numeric figures generally. Flagged for the target architecture (`TARGET-ARCHITECTURE.md`), not touched here.

**F-4 — Existing conflicts already logged and still genuinely open, restated here for completeness (not re-investigated):**
- **CONFLICT-03** (`docs/01_conflicts_log.md`) — `operations-manual.md`'s GTT Scheduling Timetables section: per that file's own changelog it was rewritten 2026-07-30 to show the (then-current) 12-client model — this audit did not re-verify whether it has since been updated for the 2026-08-05 Table 1/Table 2 rebase; flagged as unconfirmed, not re-checked, in the interest of not expanding this audit's scope beyond inspection.
- **CONFLICT-04** (`docs/01_conflicts_log.md`) — `workflow.md`'s "Staffing Model (Launch)" table still describes the sublet/subtenant model. Still flagged, not rewritten, per that log's own status. Same root issue as F-1 above.
- **`docs/VERIFICATION-TRACKER.md` item 1m** — the "framing flag" on whether Table 1 (18-client, the natural reading) or Table 2 (12-client) is the actual committed daily target is explicitly **not yet confirmed by Anthony**. Every canonical figure downstream of this choice (revenue, headcount-derived payroll headline, capacity claims) is provisionally on Table 1 pending that confirmation.
- **`docs/CURRENT-STATE.md` §6** — the startup capital range remains explicitly UNRECONCILED across (now) 6 different data points, with an adopted range (A$292,335–594,900) that the same document discloses does not exactly reconcile with its own component-by-component sum. This is not a hidden contradiction — the document is explicit about it — but it means no single number exists for "how much capital does this venture need," which the future Master Financial Model (`MODEL-ARCHITECTURE.md`) will need to resolve or explicitly model as a range, not a point estimate.

---

## 7. What Needs to Become Structured Data (candidates for `02_CANONICAL`)

Package prices, client-volume/capacity figures, headcount by scenario, wage rates, payroll totals, non-wage overhead line items, startup-capital component figures, revenue-assumption parameters (utilisation %, ancillary revenue lines), and the clinical-timing constants currently embedded as prose tables in `docs/CURRENT-STATE.md` §1–§8 and duplicated in the six `tools/*.py` scripts as hardcoded dicts. Full schema proposal: `docs/architecture/CANONICAL-DATA-SCHEMA.md`.

## 8. What Should Eventually Become an Excel Model

`profit-loss-tables.md`, `cash-flow.md`, `break-even-sensitivity-analysis.md`, `equipment-costs.md`, `financial-break-even-staff.md`, `unit-economics.md` — all currently hand-maintained markdown tables with the underlying arithmetic shown inline in prose rather than in reusable formulas. Full proposal: `docs/architecture/MODEL-ARCHITECTURE.md`.

## 9. What Should Become a Formal Generated Document

`executive-summary.md`, `business-plan.md`, `investor-memorandum.md`, `feasibility.md`, `operations-manual.md`, `risk-register.md`, and the staff-facing roster/timetable documents — all currently hand-authored, mixing narrative prose with figures that should instead be pulled from canonical data at generation time. Full proposal: `docs/architecture/DOCUMENT-GENERATION.md`.

## 10. What Should Stay as Research / Source Material

`research.md`, `dva-tpi-research.md`, `market-research-findings.md`, `industry-standards-reference-2026-07-28.md`, `property-links-2026-07-28.md`, the `wdp-reply-carole-*.md` correspondence log, `standards-floorplan-crosscheck-2026-07-28.md`, and every document in `docs/archive/` — these are primary evidence, not canonical facts or model outputs. Full proposal: `docs/architecture/TARGET-ARCHITECTURE.md`'s `01_SOURCE` layer.

---

## Note on the "Archive, Don't Flag" Tension

`rules/CLAUDE.md` companion rule 1 states that a superseded document should be physically moved to `docs/archive/` (or rewritten in place) in the same session it is identified — not left flagged in place. **This audit deliberately does not follow that rule.** Anthony's instructions for this specific architecture-only phase explicitly override it: no existing document is to be archived, deleted, or rewritten this phase, even ones this audit would otherwise recommend moving (there were none newly identified as archive-candidates beyond what's already in `docs/archive/` — F-1 through F-4 above are flagged, not moved). **This is a one-phase override of a standing rule, not a change to the rule itself** — see the final report for this instruction stated back to Anthony explicitly.
