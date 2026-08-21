# Dossier Current-State Reconciliation Matrix (2026-08-21)

**Purpose:** the required first step, per direct instruction, before any dossier HTML rewrite: establish current truth per chapter and quantify exactly what stale/repository-archaeology content exists, using a real, automated per-chapter scan of `outputs/master-dossier-v2/index.html` (35 chapters, lines 298-3139) against the categories the founder named as unacceptable in a finished business plan. This is an audit, not a rewrite — no dossier content has been changed as a result of this document. It is the evidence base the actual rewrite (a separate, subsequent, batched piece of work) must work from.

**Method:** every chapter boundary was located by its `id="chN"` anchor; the text between each anchor and the next was scanned for: spray tan, snack-pack/GDM-snack, landlord contribution/incentive, Yeti Tipi Holdings, old specific-property references (Osborne Park/Cockburn/Cannington/Tier-1 candidate), the literal strings "needs research"/"not yet built"/"superseded"/"out of scope"/"ruled out", "Relief pool"/"Relief allowance" language, "leaving-moment" references, and raw em-dash (`&mdash;`) count. Counts are exact hit counts from the live file, not estimates.

## Current Truth Sources (governing hierarchy, per this repo's own rules)

1. `docs/CURRENT-STATE.md` — package prices, client capacity, headcount, monthly net P&L, startup capital range. The single canonical source; everything else defers to it.
2. `docs/VERIFICATION-TRACKER.md` — the running list of every unconfirmed fact and its status (OPEN / WAITING / CLOSED).
3. `docs/DECISION-LOG.md` — founder decisions already made.
4. `data/canonical/*.yml` — the machine-checked canonical data layer (wages, opex, capex, services, revenue/cost ramps).
5. `docs/architecture/*.md` — investigation/methodology documents (e.g. `CANONICAL-REVENUE-METHODOLOGY.md`, `MASTER-FINANCIAL-MODEL-METHODOLOGY.md`, `FIT-OUT-DESIGN-PROCUREMENT-BRIEF.md`, `CHINA-AUSTRALIA-SOURCING-STRATEGY.md`, `FIT-OUT-PROGRAM-DECISION-ANALYSIS.md`, `MARKET-RESEARCH-BIRTHS-GDM-REFERRAL-2026.md` — this session's additions).
6. `docs/strategy/*.md` — operating model, venue functional brief.
7. Historical/superseded working documents — internal audit trail only, explicitly NOT to be carried into the dossier as content (per the founder's own instruction, "the internal governance system can retain that history, the business plan should not").

## Per-Chapter Matrix

| Ch | Title | Current truth source | Stale content found this scan (exact counts) | Action required |
|---|---|---|---|---|
| 1 | Founder Dashboard | `CURRENT-STATE.md`, `VERIFICATION-TRACKER.md` top-level view | 1 snack-pack reference, 1 old-property reference, 1 "relief pool" reference, 8 em dashes | Remove snack-pack/old-property/relief-pool language; strip em dashes |
| 2 | Business Concept | `docs/business-plan.md`, `CURRENT-STATE.md` | 1 relief-pool reference, 12 em dashes | Strip relief-pool language and em dashes |
| 3 | Market | Previously "needs research" (1 hit) — **now resolved by `MARKET-RESEARCH-BIRTHS-GDM-REFERRAL-2026.md`, this session** | 1 "needs research" hit, 3 em dashes | Rewrite using the new market-research doc's ABS/GDM figures directly; strip em dashes |
| 4 | Competitive Landscape | `docs/architecture/STRATEGIC-REPORT.md`, market-research doc | 8 em dashes | Strip em dashes only |
| 5 | Brand | `docs/naming/` decisions, `CURRENT-STATE.md` | 2 "needs research"/"superseded" hits, 18 em dashes | Resolve or clearly label brand-name founder decision (not a research gap); strip em dashes |
| 6 | Customer Experience | `docs/architecture/VENUE-FUNCTIONAL-BRIEF.md`, `CURRENT-STATE.md` | 1 leaving-moment reference, 15 em dashes | Remove leaving-moment reference (resolved/removed concept, per repo history); strip em dashes |
| 7 | GTT Service | `docs/pathology-collection-room.md`, WDP correspondence, market-research doc §3 (referral process) | 3 "needs research"/"superseded" hits, 17 em dashes | Rewrite referral-process content using the new research doc; strip em dashes |
| 8 | AM Operating Model | `docs/CURRENT-STATE.md` §1/§3, solver timetables | 20 em dashes | Rebuild against demand-driven staffing model (§12 of the master prompt) once that model exists; strip em dashes |
| 9 | PM Operating Model | `docs/CURRENT-STATE.md`, `pm-staffing-roster.md` | 1 "needs research" hit, 1 relief-pool reference, 21 em dashes | Rebuild against demand-driven PM staffing (no 1-per-role ceiling); remove relief-pool language; strip em dashes |
| 10 | Service Catalogue | `data/canonical/services.yml` | 1 spray-tan reference, 1 snack-pack reference, 1 "needs research"/"superseded" hit, 15 em dashes | Remove spray tan and snack-pack entirely; apply the 4 locked pricing recommendations; strip em dashes |
| 11 | PM Packages | `docs/CURRENT-STATE.md`, 4 disclosed price conflicts | 1 "needs research" hit, 15 em dashes | Lock PM package pricing per the 4 evidence-based recommendations; strip em dashes |
| 12 | Food & Beverage | Master prompt §20 (new direction) — cafe as real revenue stream, no snack-pack | 1 snack-pack reference, 1 "needs research" hit, 26 em dashes | Full rewrite to the new cafe model (equipment list, 50%-of-AM-clients-spend-$10 assumption, complimentary water/tea); strip em dashes |
| 13 | Retail | Master prompt §21 (no locked brands) | 1 snack-pack reference, 6 "needs research"/"out of scope" hits, 15 em dashes | Rewrite to "future opportunity, no locked brand" framing, remove Gaia/Weleda/Mustela-type specific-brand references if present; strip em dashes |
| 14 | Staffing | Master prompt §12-16 (full staffing rethink) | 1 Yeti Tipi Holdings reference, 1 "needs research" hit, 26 em dashes, 4 relief-pool references | Full rewrite: demand-driven rostering, staff-position register (VMO1/PHB01-04/etc.), remove relief-pool cost line, remove Yeti Tipi Holdings reference; strip em dashes |
| 15 | Staff Profiles | `docs/architecture/STAFF-PROFILES.md` | 1 Yeti Tipi Holdings reference, 30 em dashes, 1 relief-pool reference | Write each treatment-staff profile fully and independently (no "same as other staff"); remove Yeti Tipi Holdings reference; strip em dashes |
| 16 | Staffing Coverage | `docs/architecture/STAFF-PROFILES.md`, coverage matrices | 3 "needs research" hits, 21 em dashes, 3 relief-pool references | Rebuild coverage matrix against demand-driven model; remove relief-pool references; strip em dashes |
| 17 | Rostering | Solver-based timetables | 32 em dashes, 1 relief-pool reference | Rebuild staff-lane timetable (individual employee lanes, not generic role rows) via solver; strip em dashes |
| 18 | Customer Timetable | Solver-verified AM timetable | 6 em dashes | Remove Chair A/Chair B/Room/Lounge status columns per direct instruction; reflect T-10 to T-15 arrival window explicitly; strip em dashes |
| 19 | Venue | `docs/strategy/VENUE-FUNCTIONAL-BRIEF.md`, `FIT-OUT-PROGRAM-DECISION-ANALYSIS.md` (this session) | 4 old-property references, 4 "needs research" hits, 12 em dashes | Remove specific property candidates entirely per direct instruction; replace with venue-requirement brief (size, access, parking, zoning, clinical/fit-out requirements) usable to evaluate future properties; strip em dashes |
| 20 | Floor Plan | `docs/floor-plan-concept.md`, `FIT-OUT-PROGRAM-DECISION-ANALYSIS.md` | 1 "needs research" hit, 7 em dashes | Reconcile against the resolved/reframed station-count decisions (Parts B-D of the decision-analysis doc); strip em dashes |
| 21 | Compliance | `docs/pathology-collection-room.md`, WA regulatory sources | 2 "needs research" hits, 7 em dashes | Research WA skin-penetration/premises requirements per master prompt §26; strip em dashes |
| 22 | Children/Companion Policy | Master prompt §24 (firm policy, not unresolved option) | 1 "needs research" hit, 13 em dashes | Present as current firm policy, not an open option; strip em dashes |
| 23 | Lounge | Master prompt §23 (couches not recliners, tablets, future classes) | 4 "needs research" hits, 12 em dashes | Rewrite furniture direction (couches), tablet content scope, future-classes concept; strip em dashes |
| 24 | Startup Requirements | `docs/CURRENT-STATE.md` §7, `capex.yml` | 1 spray-tan reference, 1 landlord-contribution reference, 22 em dashes | Remove spray tan and landlord-contribution references entirely; strip em dashes |
| 25 | Purchasing | `docs/architecture/ITEMISED-PURCHASE-LIST.md`, `FIT-OUT-EQUIPMENT-SCHEDULE.md` | 2 "needs research" hits, 11 em dashes | Reconcile against resolved station-count interpretation; strip em dashes |
| 26 | Operations | `docs/strategy/OPERATING-COMMERCIAL-ARCHITECTURE.md` | 1 "needs research" hit, 9 em dashes, 1 relief-pool reference | Remove relief-pool reference; strip em dashes |
| 27 | Financial Model | `data/models/master_financial_model.yml`, `MASTER-FINANCIAL-MODEL-METHODOLOGY.md` | 5 "needs research" hits, 5 em dashes, 2 relief-pool references | Rebuild full P&L structure per master prompt §27-28 (demand-driven staffing at 6/12/18 clients/day); remove relief-pool cost line; strip em dashes |
| 28 | P&L | Same as Ch27 | 3 em dashes, 1 relief-pool reference | Same rebuild; strip em dashes |
| 29 | Cash Flow | `data/models/master_financial_model.yml` | 6 em dashes | Strip em dashes; re-run once P&L rebuild (Ch27-28) is complete |
| 30 | Break-even | `data/models/master_financial_model.yml` | 2 em dashes | Strip em dashes; re-run once demand-driven staffing model changes labour costs |
| 31 | Financial Sensitivity | `data/models/master_financial_model.yml` | 7 em dashes | Strip em dashes; re-run against 6/12/18-client scenarios explicitly |
| 32 | Marketing & Demand Generation | `docs/strategy/`, marketing docs | 4 "needs research" hits, 27 em dashes | Strip em dashes; resolve or clearly label any remaining research gaps |
| 33 | Expansion | `docs/scenario-d-investigation.md`, `docs/am-capacity-weekend.md` | 1 "needs research" hit, 20 em dashes | Reconcile against the growth-first venue philosophy addendum; strip em dashes |
| 34 | Open Items/Decisions | `VERIFICATION-TRACKER.md`, `DECISION-LOG.md` | 2 old-property references, 14 "needs research"/"superseded" hits, 37 em dashes, 2 leaving-moment references | This chapter is explicitly allowed to contain genuinely open founder decisions and third-party dependencies (that is its purpose) — but should not contain resolved/superseded content dressed as open; remove leaving-moment references (a closed matter); strip em dashes |
| 35 | Execution Roadmap | `DECISION-LOG.md`, this session's decision-analysis doc | 2 "needs research" hits, 29 em dashes | Strip em dashes; confirm roadmap reflects current decision status |

## Headline Finding — Scale of the Remaining Work

**Total em dashes across the 35-chapter dossier: approximately 560** (sum of the per-chapter counts above). Rule 35 of the master prompt requires zero. This alone is a full-document mechanical pass, not a small edit, and must be done carefully (a blind find-replace risks breaking sentence structure — each instance needs a comma/full stop/colon/semicolon substitution chosen for grammatical correctness, not a single global substitution).

**Chapters requiring more than a mechanical fix (genuine content rebuild):** 3 (market — now unblocked by this session's research), 7 (referral process — now unblocked), 8-9 (AM/PM operating model — needs the demand-driven staffing model, not yet built), 10-11 (pricing — needs the 4 locked-pricing recommendations formally applied), 12 (food and beverage — needs a full rewrite to the new cafe model), 13 (retail — needs reframing), 14-17 (staffing, profiles, coverage, rostering — needs the full staff-position register and solver-verified staff-lane timetable, not yet built), 18 (customer timetable — needs column removal and arrival-window language), 19 (venue — needs property-candidate removal and a requirements-only brief), 22-23 (companion policy, lounge — needs firm-policy and furniture-direction rewrites), 24 (startup requirements — needs spray-tan/landlord-contribution removal), 27-31 (financial model chapters — needs the full P&L rebuild against demand-driven staffing at 3 client-volume scenarios).

**Chapters that are mechanical-only (em-dash strip plus minor language fixes):** 2, 4, 6 (aside from the leaving-moment reference), 15 (aside from Yeti Tipi Holdings), 16, 17, 20-21, 25-26, 28-33, 35.

## What This Matrix Does Not Do

It does not rewrite any dossier content. It does not resolve the station-count founder decisions (see `FIT-OUT-PROGRAM-DECISION-ANALYSIS.md`, unresolved by design). It does not rebuild the financial or staffing models. It does not remove a single em dash. It is the evidence base the next batched passes must work from, so that the actual rewrite is targeted and verifiable rather than another unstructured pass through 150KB of HTML.

## Changelog

**2026-08-21 (created)** — Built via an exact, automated per-chapter scan of the live dossier HTML (not a sample or estimate), per direct instruction to establish current truth before any dossier edit. Confirms the scale of the remaining work (~560 em dashes, multiple chapters needing genuine content rebuilds pending the demand-driven staffing model and full P&L rebuild) rather than assuming it is a light edit. No dossier content changed by this document.
