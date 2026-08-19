# Dossier + Dash Rebuild — Phase 1: Repository Audit & Information Map

**Date:** 2026-08-18 | **Purpose:** Per Anthony's explicit instruction ("work through Phase 1 first and report back rather than trying to do everything at once"), this document is the Phase 1 deliverable ONLY — a full information map of what exists in this repository and where it belongs in the 35-chapter dossier / Dash rebuild. **No dossier or Dash content has been built yet.** `outputs/master-dossier/index.html` is treated as obsolete presentation per the standing instruction, referenced here only to note what it contains that needs correcting or replacing, not as a source of truth.

---

## 1. Source-of-Truth Tier Map (applied throughout this document and the eventual rebuild)

- **Tier 1 (canonical, authoritative):** `data/canonical/*.yml`, `data/models/master_financial_model.yml`, live calc code (`tools/*.py`), and this session's new current-architecture docs (`FINANCIAL-FIGURE-REFERENCE.md`, `FINANCIAL-POSITION-CURRENT.md`, `FINANCIAL-ASSUMPTION-REGISTER.md`, `FIRST-PRINCIPLES-FINANCIAL-MODEL.md`, `PM-CAPACITY-RECONCILIATION.md`, `OPERATING-MODEL-18-CLIENTS.md`, `STAFF-PROFILES.md`, `STAFFING-COVERAGE-VALIDATION.md`, `PM-PACKAGES.md`, `CURRENT-STATE.md`).
- **Tier 2 (current operational/business):** `docs/strategy/*`, `docs/experience/*`, `docs/architecture/SERVICE-CATALOGUE.md`, `docs/architecture/ITEMISED-PURCHASE-LIST.md`, `docs/architecture/HUMAN-READABLE-STARTUP-COSTS.md`, `docs/business-plan.md`, `docs/floor-plan-concept.md`, `docs/DECISION-LOG.md`.
- **Tier 3 (current research/evidence, certainty preserved):** naming/trademark docs, market research, competitor research, venue-acquisition due-diligence docs.
- **Tier 4 (reference only, current info always wins on conflict):** `outputs/master-dossier/index.html`, `docs/HANDOFF.md`, everything in `docs/archive/`, `docs/00_document_inventory.md` (itself dated 2026-07-19 to 2026-08-16, now stale relative to today).

**Critical finding: this repository's own navigation documents are themselves stale.** `docs/00_document_inventory.md` and `docs/reading-order.md` predate the entire Phase C financial rebuild, the PM capacity reconciliation, the Financial Finalisation round, and the staffing coverage recalculation — all built this session (2026-08-17/18). Neither should be trusted as a current map without cross-checking against this document and `docs/CURRENT-STATE.md`.

## 2. Chapter-by-Chapter Source Map

| # | Chapter (per Anthony's spec) | Primary source(s) | Tier | Status/Certainty | Gaps found |
|---|---|---|---|---|---|
| 1 | Founder Dashboard | Synthesis of §3-35 below, no single source | — | New content to build | — |
| 2 | Business Concept | `docs/strategy/STRATEGIC-REPORT.md` §1, `docs/business-plan.md` §1-2 | 2 | CURRENT, well-documented | None significant |
| 3 | Market (incl. prior-GDM) | `docs/market-research-findings.md`, `docs/business-plan.md` §4, `client_assumptions.yml#addressable_market_perth_weekly` (VERIFIED, real ABS data) | 2/1 | Mostly solid; ABS birth-rate figure is VERIFIED | "Prior-GDM market" specifically — not yet independently confirmed as a distinct, separately-sized segment anywhere found this pass; flagged for Phase 2 research |
| 4 | Competitive Landscape | `docs/business-plan.md` §7 (SWOT-adjacent), `docs/swot-analysis.md`, comparable-business research scattered across `PM-PACKAGES.md` §2, `FIRST-PRINCIPLES-FINANCIAL-MODEL.md` §2a (Le Beau, Keturah, endota, Hidden Valley cited) | 2/3 | Real, named comparables exist — should be stated confidently per Anthony's "no hedging where research is solid" instruction | Needs consolidation into one chapter — currently scattered across financial/staffing docs, not a single competitive-landscape document |
| 5 | Brand | `docs/strategy/BRAND-STRATEGY-NAME-AGNOSTIC.md`, `BRAND-ARCHITECTURE.md`, `PREMIUM-POSITIONING.md`, `VISUAL-BRAND-DIRECTION.md`, `outputs/brand/warm-stone-tokens.css` (founder-locked palette), `docs/naming/NAMING-DECISION-STATE.md` | 2/3 | Palette/typography LOCKED (Fraunces + DM Sans, Warm Ivory/Stone/Deep Brown/Terracotta/Olive/Rose/Brass); naming NOT locked (SOLENA 71.6% vs ELOWEN 68.8%, trademark clearance deliberately deferred) | Needs real RENDERED typography examples (not just font names) — not yet built anywhere in the repo; premium-vs-luxury definition exists in `PREMIUM-POSITIONING.md`, needs pulling into the dossier directly |
| 6 | Customer Experience | `docs/experience/CUSTOMER-JOURNEY.md` (15-stage AM/PM map) | 2 | Comprehensive, numbered stages already exist | **CONTRADICTION FOUND:** this document treats the "welcome card" and "leaving box/leaving-moment gesture" as validated, adopted concepts — but this session's standing constraints (repeated across many prior rounds) explicitly state the leaving-moment gesture is "never Anthony's idea" and must not appear. This is a genuine, unresolved conflict between two real repo documents, not a fabrication — flagged for Anthony's decision, not silently resolved either way |
| 7 | GTT Service | `client_assumptions.yml#draw_2/3_target_offset_minutes` (VERIFIED, exact +60/+120min), `scenario-c-sync-timetables.md` §0.6 | 1 | Exact draw timing VERIFIED and solver-confirmed | **WA GTT referral/request-form requirement:** this session's standing constraint notes "a real pathology request form IS required — corrects Anthony's original assumption" (already resolved in a prior round per CLAUDE.md context) — needs locating the specific source document and citing it directly in the new chapter, not just referencing the correction |
| 8 | AM Operating Model | `docs/architecture/OPERATING-MODEL-18-CLIENTS.md` §2, `scenario-c-sync-timetables.md` §0.6a | 1 | Solver-verified, current | None |
| 9 | PM Operating Model | `docs/architecture/OPERATING-MODEL-18-CLIENTS.md` §3, `docs/architecture/PM-OPERATIONS-MODEL.md` (not yet read this pass — flagged for Phase 2) | 1/2 | PM timetable is illustrative, not solver-verified (disclosed) | `PM-OPERATIONS-MODEL.md` needs cross-checking against `OPERATING-MODEL-18-CLIENTS.md` for consistency before the rebuild — not yet done |
| 10 | Service Catalogue | `docs/architecture/SERVICE-CATALOGUE.md` | 2 | COMPLETE per `00_document_inventory.md`, real Perth market research | Needs verification that every service has ALL required fields (name/description/duration/price/qualification/room/experience/constraints) — not yet checked field-by-field |
| 11 | PM Packages | `docs/architecture/PM-PACKAGES.md`, `docs/architecture/PM-CAPACITY-RECONCILIATION.md` | 1 | Current, this session's own work — PM Refresh=1 therapist, PM Restore=2 specialists, fully reconciled | None — this is the most current, most rigorously-verified chapter's source material in the whole repo |
| 12 | Food & Beverage | Referenced in `STRATEGIC-REPORT.md` §8 (glucose drink, cafe counter) and `docs/architecture/CAFE-FOOD-SERVICE-INVESTIGATION.md` | 2 | Cafe/food-safety risk investigated (Medium Risk finding) | Booking/arrival selection mechanism specifically — not located as a standalone spec this pass, may need building fresh or locating in `CUSTOMER-JOURNEY.md`'s AM stages |
| 13 | Retail | `STRATEGIC-REPORT.md` §7 (source-verified, real answer to all 5 sub-questions), `data/canonical/` ancillary revenue records | 2/1 | Well-documented — 3 named brands (Gaia, Weleda, Mustela), retail revenue explicitly PLACEHOLDER/unconfirmed | A separate "practical maternity-aid product line" idea (TENS machines, peanut balls etc.) exists as a parked, not-ruled-out future idea (`STRATEGIC-REPORT.md` §1) — must be preserved and clearly labelled exploratory, not deleted |
| 14 | Staffing | `docs/architecture/STAFF-PROFILES.md` §1, `STAFFING-COVERAGE-VALIDATION.md` | 1 | Current, this session's own recalculated work | None |
| 15 | Staff Profiles | `docs/architecture/STAFF-PROFILES.md` §2 (all 6 positions, full field list added this session) | 1 | COMPLETE per that document's own 2026-08-18 changelog | None |
| 16 | Staffing Coverage | `docs/architecture/STAFFING-COVERAGE-VALIDATION.md` | 1 | Current — 12 treatment (or 11)/4 phlebotomists (or 3), full reliability-model reasoning shown | None |
| 17 | Rostering (visual staff timetable) | `docs/architecture/OPERATING-MODEL-18-CLIENTS.md` §4 | 1 | Exists as a markdown table, NOT yet a rendered visual diagram | **Real deliverable gap** — needs actual SVG/graphical rendering, not just a markdown table, for the dossier |
| 18 | Customer Timetable (visual) | `docs/architecture/OPERATING-MODEL-18-CLIENTS.md` §2, `scenario-c-sync-timetables.md` §0.6a | 1 | Same as above — markdown table exists, not a rendered visual | Same gap as #17 |
| 19 | Venue | `docs/strategy/VENUE-FUNCTIONAL-BRIEF.md`, `docs/strategy/PERTH-PROPERTY-SHORTLIST.md`, `docs/architecture/VENUE-ACQUISITION-DUE-DILIGENCE.md` | 2/3 | Real candidates found (2 Tier-1), zero inspected — FOUNDER ACTION required | Property search is genuinely stalled pending Anthony |
| 20 | Floor Plan/Spatial Logic | `docs/floor-plan-concept.md` (PARKED pending a real architect, room list/sqm valid), `floor-plan-v3.svg`/`.pdf` | 2 | Room schedule real and current; visual layout itself explicitly NOT final | Needs real diagrams built from the CURRENT room schedule — existing SVG is dated 2026-07-10, predates several room-count corrections |
| 21 | Compliance | `docs/pathology-collection-room.md`, `docs/architecture/CURTAIN-COMPLIANCE-CLOSURE.md`, floor-plan compliance notes (WA Skin Penetration Code, LEV extraction tension flagged, not resolved) | 2 | Blood Collection Room vs. pathology requirements vs. skin penetration code genuinely kept separate already, per `STRATEGIC-REPORT.md` §9's own framing | LEV extraction / open-plan nail-area adjacency tension explicitly unresolved — needs a WorkSafe WA-familiar contractor, flagged not solved |
| 22 | Children/Companion Policy | **NOT FOUND anywhere in this repository this pass** | — | **Genuine content gap** | No dedicated document addresses whether children/companions may accompany clients. This needs either locating (a further, more exhaustive search) or building fresh with Anthony's input — flagged explicitly, not fabricated |
| 23 | Lounge (iPads/tablets/birthing plans/checklists/printing) | **NOT FOUND as a dedicated spec this pass** — `CUSTOMER-JOURNEY.md`'s "Sensory-Waiting" stage likely touches this but was not read in full this pass | 2 (unconfirmed) | **Needs Phase 2 verification** | Flagged rather than assumed present or absent — requires a full read of `CUSTOMER-JOURNEY.md` before the dossier chapter is built |
| 24 | Startup Requirements | `docs/architecture/HUMAN-READABLE-STARTUP-COSTS.md`, `data/canonical/startup_costs.yml` | 1/2 | Adopted planning figure A$251,198, itemised | Startup-cost reconciliation itself remains genuinely unresolved (6-9 historical ranges) — must be presented as bounded, not falsely precise |
| 25 | Purchasing | `docs/architecture/ITEMISED-PURCHASE-LIST.md` | 2 | COMPLETE per `00_document_inventory.md` — real brand/supplier/GST/confidence detail | None significant |
| 26 | Operations (07:00-18:00) | `docs/architecture/OPERATING-MODEL-18-CLIENTS.md` §1, §4 | 1 | Current, no reception-time contradiction (07:00/07:15 issue fixed in a prior round, re-verified this session) | None |
| 27 | Financial Model | `docs/architecture/FIRST-PRINCIPLES-FINANCIAL-MODEL.md`, `FINANCIAL-FIGURE-REFERENCE.md` | 1 | Current, fully rebuilt this session | None |
| 28 | P&L | `docs/architecture/FINANCIAL-POSITION-CURRENT.md` §4 | 1 | Current, reconciles to the cent, verified this session | None |
| 29 | Cash Flow | `docs/architecture/FINANCIAL-POSITION-CURRENT.md` §5 (24mo table + SVG chart, Playwright-verified) | 1 | Current | None |
| 30 | Break-even | `docs/architecture/FINANCIAL-POSITION-CURRENT.md` §3 | 1 | Current, both forms, plain-English explanation already built | None |
| 31 | Financial Sensitivity (6/12/18) | `docs/architecture/FINANCIAL-POSITION-CURRENT.md` §2 | 1 | Current, real dollar figures throughout, 18/day clearly the sole planning case | None |
| 32 | Marketing & Demand Generation | `docs/architecture/WAITLIST-VALIDATION-FRAMEWORK.md`, `docs/architecture/PRE-LAUNCH-DEMAND-VALIDATION-PLAN.md`, `docs/architecture/EARLY-DEMAND-VALIDATION-STRATEGY.md` (none read in full this pass) | 2 (unconfirmed depth) | **Needs Phase 2 read** | "6-factor/100-point signup framework" specifically referenced in Anthony's brief — not yet located and confirmed present in these documents this pass |
| 33 | Expansion | `docs/floor-plan-concept.md` (Treatment Room 5/6, Spray Tan Booth Phase 2, 3rd phlebotomy chair/Scenario D) | 2 | Real, disclosed growth reservations exist | Scenario D itself was "RETIRED as a scheduling investigation, reframed as a strategic capacity decision" (`STRATEGIC-REPORT.md` §1) — needs the current framing, not the old scheduling-investigation framing |
| 34 | Open Items/Decisions | `docs/VERIFICATION-TRACKER.md`, `docs/DECISION-LOG.md` | 2 | Both exist, DECISION-LOG.md is append-only and current | `VERIFICATION-TRACKER.md`'s own top-level navigation view needs cross-checking against this session's newly-resolved items (insurance, relief cost, PM capacity) — likely stale, not yet verified this pass |
| 35 | Execution Roadmap | `docs/venture-timeline.md`, `docs/grace-startup-plan.md`, `docs/project-timeline-milestones.md` | 2 | Real content exists, relative-sequence (no fixed calendar dates, a deliberate choice) | None significant |

## 3. Entity Structure — Located, Status Noted

`docs/financial-setup.md` and `docs/research.md` (both explicitly marked "UNTOUCHED (per instruction)" in the stale `00_document_inventory.md` — covers trust/ownership structure among other things) contain entity-structure content. Per the standing CLAUDE.md context, entity structure is presented as "genuinely open (not decided)" — this framing must be preserved in the dossier, not resolved.

## 4. Do-Not-Lose Checklist — Cross-Checked Against This Map

Every item on Anthony's own do-not-lose list has been checked for a genuine source in this repository:

| Item | Found? | Source |
|---|---|---|
| 18/day planning case; 6/12/18 sensitivity only | YES | `FINANCIAL-POSITION-CURRENT.md` §2 |
| Visual 18-client timetable; visual staff timetable | PARTIAL — markdown tables exist, not rendered diagrams | `OPERATING-MODEL-18-CLIENTS.md` §2/§4 — **real deliverable gap for Phase 2/3** |
| 12 treatment / 4 phlebotomists recommendations | YES | `STAFFING-COVERAGE-VALIDATION.md` |
| PM Reception relief concept | YES | `STAFFING-COVERAGE-VALIDATION.md` §4a |
| PM Refresh=1 therapist / PM Restore=2 specialists | YES | `PM-CAPACITY-RECONCILIATION.md` §2 |
| Exact +60/+120min draws | YES | `client_assumptions.yml`, VERIFIED |
| Current WA GTT referral requirement | YES (per standing context), source doc not re-located this pass | Flagged for Phase 2 |
| Prior-GDM market | NOT independently confirmed as a distinct segment | Flagged gap |
| Pre-opening waitlist framing; 6-factor/100-point signup framework | NOT YET VERIFIED this pass | Flagged for Phase 2 read of `WAITLIST-VALIDATION-FRAMEWORK.md` |
| Full PM service catalogue with descriptions; PM pricing | YES | `SERVICE-CATALOGUE.md`, `PM-PACKAGES.md` |
| Food/drink upsell | PARTIAL | `CAFE-FOOD-SERVICE-INVESTIGATION.md` — booking/selection mechanism not located |
| Lounge iPads/tablets | NOT CONFIRMED this pass | Flagged gap |
| Retail ideas preserved | YES | `STRATEGIC-REPORT.md` §7, both third-party resale and the parked maternity-aid idea |
| Expansion-ready stations at opening | YES | `floor-plan-concept.md` |
| Child policy | **NOT FOUND** | Genuine gap |
| Blood Collection Room compliance | YES | `pathology-collection-room.md`, floor-plan compliance notes |
| Floor-plan diagrams | PARTIAL — exist but dated, predate room-count corrections | Needs rebuilding |
| Startup purchase breakdown; purchasing list | YES | `HUMAN-READABLE-STARTUP-COSTS.md`, `ITEMISED-PURCHASE-LIST.md` |
| Staff profiles; wages + certainty labels | YES | `STAFF-PROFILES.md`, `FINANCIAL-ASSUMPTION-REGISTER.md` |
| Staffing coverage | YES | `STAFFING-COVERAGE-VALIDATION.md` |
| Financial assumptions | YES | `FINANCIAL-ASSUMPTION-REGISTER.md` |
| Full P&L; full cash flow; dollar + client-volume break-even | YES | `FINANCIAL-POSITION-CURRENT.md` |
| Figure derivation | YES | `FINANCIAL-FIGURE-REFERENCE.md` |
| Insurance A$708.34/mo; relief allowance A$6,128.53/mo; operating result A$32,576.80/mo; cash trough -A$76,532.52; Month 24 A$598,232.91 | YES, all VERIFIED current this session | Canonical model, live-checked |
| VM wage / workers comp / PM service duration / GTT supplies / WDP dependency unresolved | YES, all correctly labelled | `FINANCIAL-ASSUMPTION-REGISTER.md` |
| Entity structure open | YES | `financial-setup.md`/`research.md`, framing preserved |
| No 3D ultrasound / no in-house accreditation / no landlord contribution / no em dashes | Confirmed as standing exclusions, not present in Tier 1 current docs | — |
| **No leaving-moment gesture** | **RESOLVED 2026-08-19** — Anthony's decision: REMOVE, not approved, must not appear anywhere. Actioned repo-wide across all 10 forward-facing documents that referenced it (see `FOUNDER-FEEDBACK-IMPLEMENTATION-MATRIX.md` item 17c for the full file list), each replaced with an explicit removal disclosure, not silently deleted or renamed | **CLOSED** |
| No historical figures in the dossier | Will be enforced during the actual rebuild (Phase 2/3) | — |

## 5. Financial Source-of-Truth Cross-Check

Verified live against `data/models/master_financial_model.yml` and `data/canonical/cost_ramp.yml` this pass — the figures in the coordinator's message match the canonical model exactly, no drift: Revenue A$154,710.69/mo, Opex A$122,133.89/mo, Operating result A$32,576.80/mo, annualised A$390,921.60, cash trough -A$76,532.52 (Month 2), positive from Month 6, Month 24 cumulative A$598,232.91. Break-even A$122,133.90/mo, 13.051 clients/day (**note: the coordinator's message cited A$115,696.21/mo, 12.073 clients/day, 49.1% buffer — this is the PRE-Financial-Finalisation figure, one round stale. The genuinely current figure, verified against the canonical model right now, is A$122,133.90/month, 13.051 clients/day, margin of safety 4.949 clients/day (27.5% buffer), A$32,576.79/month revenue buffer (26.7%)** — flagged per the coordinator's own instruction to "use the real current value and explain the discrepancy" rather than silently using the stale figure).

---

## 6. Recommended Next Phase

**Phase 2** should NOT attempt the full dossier rebuild in one pass. Recommended sequence, given the genuine content gaps found:
1. Close the identified content gaps first (child/companion policy, lounge tablets, waitlist/signup framework, PM operating model cross-check) — either locate existing content missed this pass, or flag as genuinely needing fresh research/founder input.
2. Resolve the leaving-moment-gesture contradiction with Anthony directly before it appears (or doesn't) in the new dossier.
3. Only then begin the actual dossier architecture (Phase 2 of Anthony's own numbering) and content rebuild (Phase 3).

---

## Changelog

**2026-08-18** — Created as the Phase 1 deliverable for the dossier/Dash rebuild, per Anthony's explicit instruction not to skip ahead. Full repository audit performed (chapter-by-chapter source mapping, do-not-lose checklist cross-check, financial source-of-truth verification). Two genuine findings surfaced: (1) a real, unresolved contradiction between this repo's own experience-strategy documents and the standing "no leaving-moment gesture" constraint; (2) the financial figures relayed in this round's brief were themselves one round stale relative to the canonical model — corrected here with the live-verified current figures.
