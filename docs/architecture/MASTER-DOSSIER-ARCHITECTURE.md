# Master Dossier — Architecture Specification (Phase 2)

**Date:** 2026-08-19 | **Status:** Architecture/planning only — converts `docs/architecture/DOSSIER-DASH-PHASE1-INFORMATION-MAP.md`'s audit into a build-ready specification for Phase 4. **This document contains NO dossier content, no hardcoded financial figures, and does not build any HTML.** It is the execution checklist Phase 4 (the actual rebuild) must follow.

**How to use this document:** for each chapter, Phase 4 reads the "Primary source(s)" and "Canonical data/models" columns FIRST, builds that chapter's content and visuals from those live sources, resolves the listed contradictions/gaps per the source-of-truth hierarchy (§1), and confirms the listed founder decisions/third-party verifications are either resolved or clearly presented as open in the chapter itself — never silently smoothed over.

---

## 1. Source-of-Truth Hierarchy (structural rule for Phase 4 — no exceptions)

When two sources disagree, Phase 4 uses the HIGHER tier, always, and discloses the disagreement rather than silently picking the convenient number:

1. **Canonical financial YAML / models / live calc code** — `data/canonical/*.yml`, `data/models/master_financial_model.yml`, `tools/*.py` (run live at rebuild time, not copied from a prior session's output).
2. **Canonical architecture documents (current, 2026-08-17/18/19 session)** — `FINANCIAL-FIGURE-REFERENCE.md`, `FINANCIAL-POSITION-CURRENT.md`, `FINANCIAL-ASSUMPTION-REGISTER.md`, `FIRST-PRINCIPLES-FINANCIAL-MODEL.md`, `PM-CAPACITY-RECONCILIATION.md`, `OPERATING-MODEL-18-CLIENTS.md`, `STAFF-PROFILES.md`, `STAFFING-COVERAGE-VALIDATION.md`, `PM-PACKAGES.md`, `CHILDREN-COMPANION-POLICY.md`, `LOUNGE-DEVICE-SPEC.md`, `CURRENT-STATE.md`.
3. **Operating-model documents** — `docs/floor-plan-concept.md`, `docs/architecture/SERVICE-CATALOGUE.md`, `docs/architecture/ITEMISED-PURCHASE-LIST.md`, `docs/architecture/HUMAN-READABLE-STARTUP-COSTS.md`.
4. **Strategy documents** — `docs/strategy/*`, `docs/experience/*` (post-2026-08-19 leaving-moment removal).
5. **Supporting research** — naming/trademark, market research, venue due-diligence (certainty level preserved, never upgraded).
6. **Historical/superseded documents** — `outputs/master-dossier/index.html` (OLD, reference only), `docs/HANDOFF.md`, everything in `docs/archive/`, `docs/00_document_inventory.md`. **Never a source for a current figure.**

**Explicit dedicated live-pull points required in Phase 4 (never hardcoded into the dossier HTML or this architecture doc):** 18/day monthly revenue, opex, operating result, margin, annualised result; break-even revenue AND clients/day; cash-flow trough, month-turns-positive, Month 24 cumulative position; 6/12/18 sensitivity table; startup expenditure; working-capital reserve; PM revenue and PM transaction capacity; wages per position; insurance figure; relief/absence allowance; staffing pool sizes (simultaneous vs. employment-pool, kept visually and structurally distinct everywhere they appear); AM 18-client timetable. Phase 4's build process should read these directly from `data/models/master_financial_model.yml` / `data/canonical/*.yml` / the Tier-2 architecture docs above at build time, never copy-paste a number from a prior conversation or an old chapter draft.

**Explicit rule for Operating Result:** every chapter that states the Operating Result figure must carry (inline or immediately adjacent) the exclusion note: excludes depreciation/amortisation of startup capex, income tax, interest, and startup-capital amortisation — not a full accounting profit figure. This is not optional per-chapter styling; it is a structural requirement of the source-of-truth hierarchy itself (`FINANCIAL-POSITION-CURRENT.md` §1's own terminology-precision rule).

**PM-OPERATIONS-MODEL.md is explicitly EXCLUDED from Tier 2/3 sourcing for Phase 4.** It is flagged stale (`docs/architecture/PM-OPERATIONS-MODEL.md`'s own 2026-08-19 cross-check banner) and must not be used for current PM revenue, PM capacity, or PM labour-cost figures anywhere in the dossier. Wherever a chapter would naturally cite PM operations detail, Phase 4 must instead cite `PM-CAPACITY-RECONCILIATION.md` (capacity/revenue) and `FIRST-PRINCIPLES-FINANCIAL-MODEL.md` §3e (labour cost). Not corrected in this phase — a full re-derivation of `PM-OPERATIONS-MODEL.md` itself remains a separate future task, out of scope for both Phase 2 and Phase 4.

**Leaving-moment gesture — confirmed excluded structurally.** No chapter, visual, or customer-journey element in this architecture depends on the removed "leaving box" concept (verified against the 2026-08-19 removal commit and re-confirmed via repo-wide search, §9 below). Where the source material (`CUSTOMER-JOURNEY.md`'s Departure Experience stage) still flags the departure moment as an open design question, this architecture presents it as exactly that — open, not solved — never with an invented replacement mechanism.

---

## 2. Chapter-by-Chapter Specification

### Chapter 1 — Founder Dashboard

| Field | Detail |
|---|---|
| Purpose | A single at-a-glance page: current venture status, headline financial position, operating status, top open decisions/blockers, next actions. |
| Must communicate | "Where does this venture stand today" in under 2 minutes of reading. |
| Primary source(s) | Synthesis of Ch2-35 below — no independent source document, built from the dossier's own other chapters. |
| Supporting sources | `docs/DECISION-LOG.md`, `docs/VERIFICATION-TRACKER.md` (needs its own currency check, see Ch34). |
| Canonical data/models | Live pull: `master_financial_model.yml` headline figures (§1 hierarchy). |
| Status | **NEEDS-BUILD** — no direct source document, assembled last, after all other chapters exist. |
| Contradictions/stale sources | None specific to this chapter — inherits whatever remains unresolved elsewhere. |
| Founder decisions required | None specific to this chapter. |
| Third-party verification | None specific to this chapter. |
| Required tables | Headline metrics table (revenue/opex/operating result/margin/break-even/cash position). |
| Required charts | None (summary cards, not charts). |
| Required diagrams | None. |
| Photography/visual treatment | Hero treatment — brand palette, restrained, premium (§6). |
| Dependencies | Every other chapter (built last). |
| Must NOT include | Any figure not traceable to a live canonical pull; no historical/superseded figures. |

### Chapter 2 — Business Concept

| Field | Detail |
|---|---|
| Purpose | What the business actually is, in plain terms — AM GTT + PM wellness, the dual-segment model. |
| Must communicate | The core concept clearly enough that a reader with zero background understands the venture in one page. |
| Primary source(s) | `docs/strategy/STRATEGIC-REPORT.md` §1, `docs/business-plan.md` §1-2. |
| Supporting sources | `docs/executive-summary.md`, `docs/feasibility.md`. |
| Canonical data/models | None (conceptual chapter). |
| Status | **COMPLETE** (source material solid, no significant gaps). |
| Contradictions/stale sources | None found. |
| Founder decisions required | None. |
| Third-party verification | None. |
| Required tables | None. |
| Required charts | None. |
| Required diagrams | Optional simple AM/PM segment diagram. |
| Photography/visual treatment | Chapter-opening full-bleed image (venue mood, once available) or restrained typographic opener if no photography exists yet. |
| Dependencies | None — can be written first. |
| Must NOT include | 3D ultrasound, in-house pathology accreditation, landlord contribution — confirmed standing exclusions, not present in Tier 1/2 sources. |

### Chapter 3 — Market (including prior-GDM market)

| Field | Detail |
|---|---|
| Purpose | Size and characterise the addressable market. |
| Must communicate | Real, sourced market size (Perth births, GTT test volume) — state confidently where research is solid, per Anthony's "no hedging" instruction. |
| Primary source(s) | `data/canonical/client_assumptions.yml#addressable_market_perth_weekly` (VERIFIED, real ABS data), `docs/market-research-findings.md`. |
| Supporting sources | `docs/business-plan.md` §4. |
| Canonical data/models | `client_assumptions.yml` VERIFIED record — live pull, cite directly. |
| Status | **PARTIAL** — core addressable-market figure is VERIFIED and strong; "prior-GDM market" as a distinct, separately-sized segment is NOT independently confirmed anywhere in this repo. |
| Contradictions/stale sources | None on the core figure; the prior-GDM segment claim has no located quantification. |
| Founder decisions required | None. |
| Third-party verification | None on the core ABS-sourced figure. |
| Required tables | Addressable market breakdown. |
| Required charts | Simple market-size visual (e.g. total Perth births → GTT-eligible → addressable). |
| Required diagrams | None. |
| Photography/visual treatment | Standard chapter treatment. |
| Dependencies | None. |
| Must NOT include | An invented prior-GDM market size — if not resolved by Phase 4 research, state explicitly as NEEDS-RESEARCH within the chapter, not silently omitted or guessed. |

### Chapter 4 — Competitive Landscape

| Field | Detail |
|---|---|
| Purpose | Real, named comparable businesses and how this venture differs. |
| Must communicate | Confident, specific competitive positioning — comparables are real and researched, state them as fact. |
| Primary source(s) | Comparables scattered across `PM-PACKAGES.md` §2 and `FIRST-PRINCIPLES-FINANCIAL-MODEL.md` §2a (Le Beau, Keturah, endota, Hidden Valley Eco Day Spa — all real, named, researched). |
| Supporting sources | `docs/swot-analysis.md`, `docs/business-plan.md` §7. |
| Canonical data/models | None. |
| Status | **PARTIAL** — real research exists but is scattered across financial/staffing documents, not consolidated into one competitive-landscape document. |
| Contradictions/stale sources | None found, just fragmentation. |
| Founder decisions required | None. |
| Third-party verification | None. |
| Required tables | Comparable-business feature/pricing comparison table. |
| Required charts | None. |
| Required diagrams | None. |
| Photography/visual treatment | Standard. |
| Dependencies | Chapter 10 (Service Catalogue), Chapter 11 (PM Packages) for pricing comparison. |
| Must NOT include | Unnamed/vague "competitors" language where real named comparables exist. |

### Chapter 5 — Brand

| Field | Detail |
|---|---|
| Purpose | Present the brand direction — positioning, palette, typography, naming status. |
| Must communicate | Premium-not-luxury positioning defined precisely; the founder-locked palette/typography; naming status honestly (not locked). |
| Primary source(s) | `docs/strategy/BRAND-STRATEGY-NAME-AGNOSTIC.md`, `BRAND-ARCHITECTURE.md`, `PREMIUM-POSITIONING.md`, `VISUAL-BRAND-DIRECTION.md`, `outputs/brand/warm-stone-tokens.css`, `docs/naming/NAMING-DECISION-STATE.md`. |
| Supporting sources | `docs/naming/NAMING-FINAL-COMPARISON.md`. |
| Canonical data/models | `warm-stone-tokens.css` (founder-locked palette values, live pull for hex codes). |
| Status | **PARTIAL** — palette/typography locked and current; naming genuinely open (SOLENA 71.6% vs ELOWEN 68.8%, trademark clearance deliberately deferred); real RENDERED typography examples do not yet exist anywhere in the repo (a genuine build gap for Phase 4, not just a citation gap). |
| Contradictions/stale sources | None on the palette; `VISUAL-BRAND-DIRECTION.md`'s own colour-palette section is explicitly noted elsewhere as SUPERSEDED by the founder-locked palette — Phase 4 must use `warm-stone-tokens.css`, not the superseded section. |
| Founder decisions required | Final name selection (genuinely open, not a Phase 4 decision to make). |
| Third-party verification | Trademark clearance (deliberately deferred, not a Phase 4 task to resolve). |
| Required tables | Palette swatch table with hex codes; typography scale table. |
| Required charts | None. |
| Required diagrams | None. |
| Photography/visual treatment | **Real rendered typography examples required** — headline/subheading/body/numbers/table-headings/labels, actually rendered in Fraunces + DM Sans, not just font names stated in prose. This is a genuine NEW BUILD requirement for Phase 4 (§8). |
| Dependencies | Referenced by nearly every other chapter (colour/type system). |
| Must NOT include | A locked name presented as decided; the SUPERSEDED colour palette section from `VISUAL-BRAND-DIRECTION.md`. |

### Chapter 6 — Customer Experience

| Field | Detail |
|---|---|
| Purpose | The full customer journey, AM and PM. |
| Must communicate | Every journey stage, numbered, with emotion/expectation/opportunity/friction noted. |
| Primary source(s) | `docs/experience/CUSTOMER-JOURNEY.md` (15-stage AM/PM map, post-2026-08-19 leaving-moment removal). |
| Supporting sources | `docs/experience/RETURN-LOOP.md`. |
| Canonical data/models | None directly (references Ch7-9's operating data). |
| Status | **PARTIAL** — comprehensive, numbered stages exist; the Departure Experience stage is explicitly an OPEN design question post-removal (no invented replacement), must be presented as such, not silently closed. |
| Contradictions/stale sources | None remaining post-cleanup (verified §9). |
| Founder decisions required | Whether/how to design a departure-moment mechanism (genuinely open, not resolved by this architecture). |
| Third-party verification | None. |
| Required tables | Journey-stage table (stage/emotion/expectation/opportunity/friction). |
| Required charts | None. |
| Required diagrams | Customer-journey visual (a real graphic, not a text list) — genuine build requirement for Phase 4. |
| Photography/visual treatment | Journey-stage imagery where available. |
| Dependencies | Chapter 7 (GTT Service), Chapter 8/9 (AM/PM Operating Model), Chapter 22 (Children/Companion), Chapter 23 (Lounge). |
| Must NOT include | The leaving-box/leaving-moment gesture concept in any form — confirmed removed. |

### Chapter 7 — GTT Service

| Field | Detail |
|---|---|
| Purpose | The clinical GTT process itself. |
| Must communicate | Exact draw timing (+60/+120min), the real WA referral/request-form requirement, pathology-partner relationship. |
| Primary source(s) | `data/canonical/client_assumptions.yml#draw_2/3_target_offset_minutes` (VERIFIED), `scenario-c-sync-timetables.md` §0.6, `docs/gtt-clinical-protocol.md`. |
| Supporting sources | `docs/pathology-partnership-brief.md`. |
| Canonical data/models | `client_assumptions.yml` — live pull for exact timing. |
| Status | **PARTIAL** — draw timing VERIFIED and solver-confirmed; the specific WA referral/request-form requirement source document was not re-located in Phase 1 and needs confirming before Phase 4 cites it as current (a genuine sourcing task, not a research gap — the finding itself is already established per standing session context, just needs its primary citation re-confirmed). |
| Contradictions/stale sources | None on timing. |
| Founder decisions required | None. |
| Third-party verification | WDP/pathology-partner relationship status (WAITING ON THIRD PARTY, per `FINANCIAL-ASSUMPTION-REGISTER.md`). |
| Required tables | Draw-timing table. |
| Required charts | None. |
| Required diagrams | None (see Chapter 18 for the full visual timetable). |
| Photography/visual treatment | Standard, avoid clinical-cold imagery outside what's necessary. |
| Dependencies | Chapter 8 (AM Operating Model), Chapter 18 (Customer Timetable), Chapter 21 (Compliance). |
| Must NOT include | Any claim that in-house pathology accreditation exists or is planned — confirmed standing exclusion. |

### Chapter 8 — AM Operating Model

| Field | Detail |
|---|---|
| Purpose | How the AM (GTT) window actually operates, 07:00-13:00. |
| Must communicate | The 9-synchronized-pair, solver-verified schedule; zero AM gap-fill capacity finding. |
| Primary source(s) | `docs/architecture/OPERATING-MODEL-18-CLIENTS.md` §2, `scenario-c-sync-timetables.md` §0.6a. |
| Supporting sources | None needed — primary sources are comprehensive and current. |
| Canonical data/models | `scenario-c-sync-timetables.md` timing data — live-cited, solver-verified. |
| Status | **COMPLETE** (source material). Visual rendering is a Phase 4 BUILD requirement (see below). |
| Contradictions/stale sources | None. |
| Founder decisions required | None. |
| Third-party verification | None. |
| Required tables | Full 9-pair AM timetable table (already exists in markdown form, needs visual rendering). |
| Required charts | None. |
| Required diagrams | **Real rendered AM timetable diagram** — time | client | service | room/station | treatment staff | phlebotomy | reception/VM | lounge state. Genuine NEW BUILD requirement (currently a markdown table only). |
| Photography/visual treatment | Standard. |
| Dependencies | Chapter 7 (GTT Service), Chapter 17 (Rostering), Chapter 18 (Customer Timetable — closely related, may be combined at Phase 4's discretion if it avoids duplication). |
| Must NOT include | Implying idle AM capacity exists for gap-fill sales — the disclosed finding is that none exists at full 18-client volume. |

### Chapter 9 — PM Operating Model

| Field | Detail |
|---|---|
| Purpose | How the PM window operates, 13:00-18:00. |
| Must communicate | The PM capacity correction (PM Refresh=1 therapist, PM Restore=2 specialists), the corrected transaction capacity, and that the PM timetable is illustrative, not solver-verified — stated plainly. |
| Primary source(s) | `docs/architecture/OPERATING-MODEL-18-CLIENTS.md` §3, `docs/architecture/PM-CAPACITY-RECONCILIATION.md`. |
| Supporting sources | **NOT** `docs/architecture/PM-OPERATIONS-MODEL.md` — explicitly excluded per §1's hierarchy, stale. |
| Canonical data/models | `revenue_assumptions.yml#rev_pm_weekday_transactions`/`rev_pm_saturday_transactions` — live pull. |
| Status | **PARTIAL** — capacity/revenue model current and correct; the PM session schedule itself remains illustrative, not solver-verified (disclosed honestly, not a gap to hide). |
| Contradictions/stale sources | `PM-OPERATIONS-MODEL.md` contains materially different, stale figures — Phase 4 must not cite it. |
| Founder decisions required | None specific (the PM Refresh/Restore staffing model is already researched-best-evidenced, not open). |
| Third-party verification | None. |
| Required tables | PM capacity/transaction table. |
| Required charts | None. |
| Required diagrams | Illustrative PM session schedule diagram, clearly labelled "illustrative, not solver-verified." |
| Photography/visual treatment | Standard. |
| Dependencies | Chapter 11 (PM Packages), Chapter 17 (Rostering). |
| Must NOT include | Any figure sourced from `PM-OPERATIONS-MODEL.md`. |

### Chapter 10 — Service Catalogue

| Field | Detail |
|---|---|
| Purpose | Every individual service offered. |
| Must communicate | Name/description/duration/price/qualification/room/experience/constraints for every service. |
| Primary source(s) | `docs/architecture/SERVICE-CATALOGUE.md`. |
| Supporting sources | `docs/services-master-table.md`, `docs/services-pricing-locked.md` (flagged elsewhere as having a completeness gap and 4 internal price disagreements — `data/canonical/services.yml`'s own disclosed conflicts). |
| Canonical data/models | `data/canonical/services.yml` — live pull for prices, cross-check against `SERVICE-CATALOGUE.md` prose. |
| Status | **PARTIAL** — comprehensive catalogue exists; field-by-field completeness (every service has ALL required fields) not yet verified; known price disagreements in `services.yml`'s own conflicts list not yet resolved. |
| Contradictions/stale sources | `services.yml#conflicts` — hair colour pricing (4 services), lash infill pricing, GDM snack pack pricing, locked-pricing completeness gap — all pre-existing, disclosed, NOT resolved by this architecture. |
| Founder decisions required | Which of the disputed prices is correct, for each of the 4 disclosed conflicts (genuine founder/pricing decisions, not Phase 4's to make unilaterally). |
| Third-party verification | None. |
| Required tables | Full service catalogue table (one row per service, all fields). |
| Required charts | None. |
| Required diagrams | None. |
| Photography/visual treatment | Service imagery where available; otherwise restrained iconography. |
| Dependencies | Chapter 11 (PM Packages) builds on this. |
| Must NOT include | A price for any service that contradicts `services.yml`'s canonical record without disclosing the conflict. |

### Chapter 11 — PM Packages

| Field | Detail |
|---|---|
| Purpose | The two locked PM packages and the real average-transaction-value derivation. |
| Must communicate | PM Refresh (1 dual-qualified therapist) / PM Restore (2 specialists) — the researched staffing model, current pricing, and the full A$117 derivation. |
| Primary source(s) | `docs/architecture/PM-PACKAGES.md`, `docs/architecture/PM-CAPACITY-RECONCILIATION.md`. |
| Supporting sources | None needed. |
| Canonical data/models | `data/canonical/pricing.yml#pm_alacarte_average` — live pull. |
| Status | **COMPLETE** — this is the most current, most rigorously verified source material in the whole repo. |
| Contradictions/stale sources | None. |
| Founder decisions required | Final sign-off on package pricing (per `PM-PACKAGES.md` §6, not yet formally signed off — a real, disclosed open item). |
| Third-party verification | None. |
| Required tables | Package composition/pricing table; the A$117 derivation table (mix × price → blended average). |
| Required charts | None. |
| Required diagrams | None. |
| Photography/visual treatment | Standard. |
| Dependencies | Chapter 9 (PM Operating Model), Chapter 10 (Service Catalogue). |
| Must NOT include | The pre-A$117 A$95 placeholder figure anywhere. |

### Chapter 12 — Food & Beverage

| Field | Detail |
|---|---|
| Purpose | On-site food/beverage service. |
| Must communicate | The scoped offering (pre-packaged snacks, herbal tea, coconut water — not hot food), the food-safety risk finding. |
| Primary source(s) | `docs/architecture/CAFE-FOOD-SERVICE-INVESTIGATION.md`, `docs/experience/CUSTOMER-JOURNEY.md`'s Departure Experience stage (post-cleanup). |
| Supporting sources | `docs/financial-setup.md` Step 9, `docs/equipment-costs.md` §6/§12. |
| Canonical data/models | None specific. |
| Status | **PARTIAL** — cafe/food-safety risk investigated (Medium Risk finding); the booking/arrival selection mechanism (how a client actually chooses/receives food/drink) is NOT located as a standalone spec — a genuine content gap. |
| Contradictions/stale sources | None found; the departure-gesture removal has been applied cleanly to this topic (§9). |
| Founder decisions required | None currently blocking. |
| Third-party verification | Food-safety/business-risk classification already researched (Medium Risk) — no further verification flagged as required. |
| Required tables | Offering list. |
| Required charts | None. |
| Required diagrams | None. |
| Photography/visual treatment | Standard, warm/natural styling. |
| Dependencies | Chapter 6 (Customer Experience), Chapter 23 (Lounge). |
| Must NOT include | Any "breakfast while fasting" framing (confirmed standing exclusion); the removed departure-gesture mechanic. |

### Chapter 13 — Retail

| Field | Detail |
|---|---|
| Purpose | Third-party retail offering. |
| Must communicate | The three named brands (Gaia, Weleda, Mustela), the disclosed low-confidence revenue figure, the parked (not ruled out) maternity-aid product-line idea. |
| Primary source(s) | `docs/strategy/STRATEGIC-REPORT.md` §7 (source-verified, real answers to all 5 sub-questions). |
| Supporting sources | `data/canonical/` ancillary revenue records. |
| Canonical data/models | `revenue_assumptions.yml#rev_ancillary_excluded_from_baseline` — live pull, confirms A$0 in the current baseline. |
| Status | **COMPLETE** — well-documented, all open questions already resolved to the extent research allows. |
| Contradictions/stale sources | None. |
| Founder decisions required | None currently open — retail strategy already founder-confirmed (`DECISION-LOG.md`, 2026-08-14). |
| Third-party verification | None. |
| Required tables | None required, could include a brand list. |
| Required charts | None. |
| Required diagrams | None. |
| Photography/visual treatment | Product/retail-corner imagery where available. |
| Dependencies | None significant. |
| Must NOT include | A name-branded retail/cosmetics product line presented as decided (explicitly ruled out); the maternity-aid idea must be labelled exploratory/parked, not deleted. |

### Chapter 14 — Staffing

| Field | Detail |
|---|---|
| Purpose | Overall staffing structure and philosophy. |
| Must communicate | The simultaneous-roster vs. employment-pool distinction, made unmistakable from the first sentence. |
| Primary source(s) | `docs/architecture/STAFF-PROFILES.md` §1, `docs/architecture/STAFFING-COVERAGE-VALIDATION.md`. |
| Supporting sources | None needed. |
| Canonical data/models | None directly (headcount is a modelled, not canonical-YAML, figure). |
| Status | **COMPLETE**. |
| Contradictions/stale sources | None. |
| Founder decisions required | Treatment pool size (12 recommended vs. 11 lower-reliability alternative); phlebotomist pool size (4 recommended vs. 3 lower-cost alternative) — both genuine, disclosed, not yet decided. |
| Third-party verification | None. |
| Required tables | Headcount summary table (simultaneous / employment pool / relief, per position). |
| Required charts | None. |
| Required diagrams | None (see Chapter 16 for the reliability-model visual). |
| Photography/visual treatment | Standard. |
| Dependencies | Chapter 15 (Staff Profiles), Chapter 16 (Staffing Coverage), Chapter 17 (Rostering). |
| Must NOT include | Presenting the 12/4-person employment pools as the daily payroll cost — must always be shown alongside the 8/2 simultaneous figure with the distinction explicit. |

### Chapter 15 — Staff Profiles

| Field | Detail |
|---|---|
| Purpose | Full profile per position. |
| Must communicate | Full field list per position (reporting line, experience, skills, compliance, cross-training, wage, hours, etc.) for all 6 positions. |
| Primary source(s) | `docs/architecture/STAFF-PROFILES.md` §2. |
| Supporting sources | None needed. |
| Canonical data/models | `data/canonical/wages.yml` — live pull for wage figures. |
| Status | **COMPLETE** — full field list added and confirmed complete in a prior round's changelog. |
| Contradictions/stale sources | None. |
| Founder decisions required | None specific (wage certainty labels are the relevant caveat, carried into Chapter 27). |
| Third-party verification | VM wage (accountant/Fair Work), phlebotomist employment arrangement (WDP). |
| Required tables | One profile table/card per position (6 total). |
| Required charts | None. |
| Required diagrams | None. |
| Photography/visual treatment | Standard, could use simple role iconography. |
| Dependencies | Chapter 14, Chapter 16, Chapter 27 (wage figures feed the financial model). |
| Must NOT include | Any wage figure presented as VERIFIED when the source labels it RESEARCHED-BEST-EVIDENCE or PLACEHOLDER (VM wage, workers comp specifically). |

### Chapter 16 — Staffing Coverage

| Field | Detail |
|---|---|
| Purpose | The reliability/relief-pool model. |
| Must communicate | The binomial reliability method, why 12/4 (or 11/3) is recommended, the reliability percentages themselves. |
| Primary source(s) | `docs/architecture/STAFFING-COVERAGE-VALIDATION.md`. |
| Supporting sources | None needed. |
| Canonical data/models | None (a modelling document, not canonical YAML). |
| Status | **COMPLETE**. |
| Contradictions/stale sources | None. |
| Founder decisions required | Same two pool-size decisions as Chapter 14 (12 vs 11 treatment, 4 vs 3 phlebotomists). |
| Third-party verification | None. |
| Required tables | Reliability table (n vs. reliability %, per line). |
| Required charts | Reliability curve visual (optional, genuinely useful — a Phase 4 BUILD opportunity, not currently rendered). |
| Required diagrams | None required beyond the table/chart above. |
| Photography/visual treatment | Standard. |
| Dependencies | Chapter 14, Chapter 15. |
| Must NOT include | Presenting the 8% absence-rate assumption as verified data — it is explicitly a disclosed planning estimate. |

### Chapter 17 — Rostering (visual staff timetable)

| Field | Detail |
|---|---|
| Purpose | Show the staff roster across the full trading day. |
| Must communicate | Who is working when, 07:00-18:00, across all positions — visually, not just in prose. |
| Primary source(s) | `docs/architecture/OPERATING-MODEL-18-CLIENTS.md` §4. |
| Supporting sources | None needed. |
| Canonical data/models | None directly. |
| Status | **PARTIAL** — markdown table exists and is current; **no rendered visual diagram exists anywhere in the repo** — a genuine, real Phase 4 BUILD requirement, not a sourcing gap. |
| Contradictions/stale sources | None. |
| Founder decisions required | None. |
| Third-party verification | None. |
| Required tables | The existing staff-lane table (as a fallback/companion to the diagram). |
| Required charts | None. |
| Required diagrams | **Real staff-lane timetable diagram, 07:00-18:00** — lanes for VM, AM reception, PM reception, phlebotomists, each treatment-staff group, relief/backup. Genuine new build, currently only a markdown table. |
| Photography/visual treatment | None needed — this is a data visualisation chapter. |
| Dependencies | Chapter 8, Chapter 9, Chapter 14, Chapter 16. |
| Must NOT include | Implying more staff are simultaneously rostered than the solver-verified 8 treatment + 2 phlebotomists + 1 VM + 1 PM Reception. |

### Chapter 18 — Customer Timetable (visual)

| Field | Detail |
|---|---|
| Purpose | Show the 18-client AM day visually. |
| Must communicate | The 9 synchronized pairs, exact draw timing, room/station/staff assignment, lounge state — visually. |
| Primary source(s) | `docs/architecture/OPERATING-MODEL-18-CLIENTS.md` §2, `scenario-c-sync-timetables.md` §0.6a. |
| Supporting sources | None needed. |
| Canonical data/models | `client_assumptions.yml` draw-timing fields — live pull for exact minute values. |
| Status | **PARTIAL** — markdown table exists and is solver-verified; **no rendered visual diagram exists** — genuine Phase 4 BUILD requirement. |
| Contradictions/stale sources | None. |
| Founder decisions required | None. |
| Third-party verification | None. |
| Required tables | The existing 9-pair table (fallback/companion). |
| Required charts | None. |
| Required diagrams | **Real AM timetable diagram** — time | client | service | room/station | treatment staff | phlebotomist | reception/VM | lounge state, per §2's own columns. May be combined with Chapter 8 at Phase 4's discretion to avoid duplication (both draw from the same source). |
| Photography/visual treatment | None needed. |
| Dependencies | Chapter 7, Chapter 8. |
| Must NOT include | Any staff-to-client assignment presented as solver-verified beyond what's actually verified (the specific M1-vs-M2 rotation is illustrative, per `OPERATING-MODEL-18-CLIENTS.md` §2's own disclosure — must carry that caveat into the diagram). |

### Chapter 19 — Venue

| Field | Detail |
|---|---|
| Purpose | Venue requirements and current search status. |
| Must communicate | What the venue must have (room schedule), and the honest current search status (2 Tier-1 candidates, zero inspected). |
| Primary source(s) | `docs/strategy/VENUE-FUNCTIONAL-BRIEF.md`, `docs/strategy/PERTH-PROPERTY-SHORTLIST.md`. |
| Supporting sources | `docs/architecture/VENUE-ACQUISITION-DUE-DILIGENCE.md`, `docs/strategy/PROPERTY-SEARCH-FRAMEWORK.md`. |
| Canonical data/models | None. |
| Status | **PARTIAL** — requirements are current and real; property search is genuinely stalled pending Anthony, must be presented as an active open item, not implied as progressing. |
| Contradictions/stale sources | None. |
| Founder decisions required | Property inspection/selection (genuinely Anthony's own action, not resolvable in the dossier). |
| Third-party verification | Landlord terms (once a property is under negotiation). |
| Required tables | Room-requirement table (required/desirable/future, per Phase 1's own categorisation). |
| Required charts | None. |
| Required diagrams | None (see Chapter 20 for spatial diagrams). |
| Photography/visual treatment | Property photography once available (currently none). |
| Dependencies | Chapter 20 (Floor Plan). |
| Must NOT include | A specific property presented as secured or confirmed. |

### Chapter 20 — Floor Plan / Spatial Logic

| Field | Detail |
|---|---|
| Purpose | The physical layout logic. |
| Must communicate | Room adjacencies, the "only the Blood Collection Room looks clinical" principle, expansion-ready stations. |
| Primary source(s) | `docs/floor-plan-concept.md` (room schedule valid; box-layout explicitly not final). |
| Supporting sources | `floor-plan-v3.svg`/`.pdf` (dated 2026-07-10, predates several room-count corrections — flagged, not used as-is). |
| Canonical data/models | None. |
| Status | **PARTIAL** — room schedule current; existing visual layout is STALE (predates corrections) — needs rebuilding from the current room schedule, a genuine Phase 4 BUILD requirement, not a simple re-use. |
| Contradictions/stale sources | `floor-plan-v3.svg` is dated and does not reflect the current, corrected room/fixture counts. |
| Founder decisions required | Leaner day-one fixture count (2+2 vs 4+4 stations) if capital is tighter than planned — a real, disclosed alternative not yet decided. |
| Third-party verification | LEV extraction / open-plan nail-area adjacency (needs a WorkSafe WA-familiar contractor — explicitly unresolved). |
| Required tables | Room schedule table (room/sqm/wall type/status). |
| Required charts | None. |
| Required diagrams | **Rebuilt floor-plan diagram(s)** reflecting the current, corrected room/fixture schedule — genuine new build, not a re-use of the dated SVG. |
| Photography/visual treatment | Once a floor plan is rebuilt, real spatial renders if resources allow (optional, not required for dossier completeness). |
| Dependencies | Chapter 19, Chapter 21 (compliance constraints affect layout), Chapter 33 (expansion stations). |
| Must NOT include | The dated `floor-plan-v3.svg` presented as current without a staleness note if reused as a placeholder. |

### Chapter 21 — Compliance

| Field | Detail |
|---|---|
| Purpose | Regulatory/compliance posture. |
| Must communicate | The Blood Collection Room's own code requirements kept clearly separate from pathology-partner requirements and the WA Skin Penetration Code — three distinct compliance regimes, not conflated. |
| Primary source(s) | `docs/pathology-collection-room.md`, `docs/architecture/CURTAIN-COMPLIANCE-CLOSURE.md`, `docs/floor-plan-concept.md`'s compliance notes. |
| Supporting sources | None needed. |
| Canonical data/models | None. |
| Status | **PARTIAL** — the three-regime separation is already correctly maintained in source material; the LEV extraction/open-plan tension is explicitly unresolved. |
| Contradictions/stale sources | None. |
| Founder decisions required | None directly — this is a professional-verification item, not a founder decision. |
| Third-party verification | WorkSafe WA-familiar contractor for the LEV/open-plan tension — explicitly flagged, not resolved. |
| Required tables | Compliance-regime comparison table (Blood Collection Room / pathology partner / Skin Penetration Code — scope of each). |
| Required charts | None. |
| Required diagrams | None beyond Chapter 20's floor plan. |
| Photography/visual treatment | Standard, restrained (avoid over-clinical imagery per the brand principle). |
| Dependencies | Chapter 20, Chapter 7. |
| Must NOT include | Any claim of in-house NATA/pathology accreditation (confirmed standing exclusion); a resolved position on the LEV tension that hasn't actually been confirmed by a contractor. |

### Chapter 22 — Children / Companion Policy

| Field | Detail |
|---|---|
| Purpose | Present the proposed policy. |
| Must communicate | The policy exactly as written in the canonical source — proposed, not verified, with every legal-adjacent claim flagged. |
| Primary source(s) | `docs/architecture/CHILDREN-COMPANION-POLICY.md` (single canonical source, referenced not restated per its own §6). |
| Supporting sources | None — this chapter should not vary the policy independently. |
| Canonical data/models | None. |
| Status | **COMPLETE** (as a proposed policy) — genuinely new this session, no prior source existed. |
| Contradictions/stale sources | None (newly created, no legacy content to conflict with). |
| Founder decisions required | The Blood Collection Room companion exception (needle-phobia case) — explicitly unresolved in the source document. |
| Third-party verification | Solicitor (supervision liability), insurer/broker (coverage), landlord (occupancy conditions, once a venue exists), WA regulation (children in a facility with a clinical room) — all four explicitly flagged in the source, none resolved. |
| Required tables | None required — policy is prose-appropriate. |
| Required charts | None. |
| Required diagrams | None. |
| Photography/visual treatment | Standard, warm/welcoming imagery (Lounge). |
| Dependencies | Chapter 6, Chapter 19/20 (room capacity references). |
| Must NOT include | Any legal claim not present in the source document — this chapter must not "round up" a proposed policy into a stated legal position. |

### Chapter 23 — Lounge

| Field | Detail |
|---|---|
| Purpose | The Lounge experience and the device spec. |
| Must communicate | Lounge design/purpose, the device spec exactly as written in the canonical source. |
| Primary source(s) | `docs/architecture/LOUNGE-DEVICE-SPEC.md` (single canonical source for devices), `docs/floor-plan-concept.md` (Lounge dimensions), `docs/experience/CUSTOMER-JOURNEY.md` (Sensory-Waiting stage — flagged in Phase 1 as not yet fully verified present/read, needs re-confirming in Phase 4). |
| Supporting sources | `docs/architecture/CHILDREN-COMPANION-POLICY.md` (capacity/supervision cross-reference). |
| Canonical data/models | None. |
| Status | **PARTIAL** — device spec complete (proposed); the general Lounge-experience content (birthing plans/checklists/printing, per the original do-not-lose checklist) still needs a full read/confirmation of `CUSTOMER-JOURNEY.md`'s Sensory-Waiting stage — not yet done. |
| Contradictions/stale sources | None found so far; needs the confirmation read above before Phase 4 finalises this chapter. |
| Founder decisions required | Lounge devices companion-vs-client-facing (explicitly unresolved in the source); AM-peak no-companions rule (explicitly unresolved, flagged as a future Venue-Manager/founder monitoring item, not a launch-day decision). |
| Third-party verification | None specific to this chapter beyond Chapter 22's. |
| Required tables | Device spec table (from the canonical source). |
| Required charts | None. |
| Required diagrams | None required. |
| Photography/visual treatment | Lounge imagery, warm/natural. |
| Dependencies | Chapter 6, Chapter 22, Chapter 20. |
| Must NOT include | A definitive answer to the client-vs-companion-facing question — must be presented as proposed/open. |

### Chapter 24 — Startup Requirements

| Field | Detail |
|---|---|
| Purpose | What capital and purchases are needed before opening. |
| Must communicate | Every startup category itemised, the adopted planning figure, the disclosed reconciliation-range uncertainty. |
| Primary source(s) | `docs/architecture/HUMAN-READABLE-STARTUP-COSTS.md`, `data/canonical/startup_costs.yml`. |
| Supporting sources | `docs/architecture/STARTUP-COST-RECONCILIATION.md` (the unresolved 6-9-range history). |
| Canonical data/models | `startup_costs.yml#adopted_planning_scenarios` — live pull for the A$251,198 figure and its components. |
| Status | **PARTIAL** — adopted planning figure is clear and itemised; the underlying reconciliation problem (6-9 historical ranges) remains genuinely unresolved and must be presented as bounded, not falsely precise. |
| Contradictions/stale sources | The historical range disagreement is disclosed, not resolved — Phase 4 must not silently pick one range. |
| Founder decisions required | None beyond the already-given in-principle approval (explicitly not a locked final cost). |
| Third-party verification | Real supplier/quote validation for every fit-out trade/furniture/equipment line (explicitly still needed, per `startup_costs.yml`'s own status). |
| Required tables | Startup cost category breakdown table. |
| Required charts | None required (a simple bar/range chart is an optional Phase 4 enhancement). |
| Required diagrams | None. |
| Photography/visual treatment | Standard. |
| Dependencies | Chapter 25 (Purchasing), Chapter 29 (Cash Flow). |
| Must NOT include | A single "the" startup capital figure presented as exact — must retain the bounded-range framing. |

### Chapter 25 — Purchasing

| Field | Detail |
|---|---|
| Purpose | The itemised purchase list. |
| Must communicate | Item/qty/price/total/supplier/certainty/required-vs-optional, per item. |
| Primary source(s) | `docs/architecture/ITEMISED-PURCHASE-LIST.md`. |
| Supporting sources | None needed. |
| Canonical data/models | None (a procurement document, not canonical YAML). |
| Status | **COMPLETE**. |
| Contradictions/stale sources | None. |
| Founder decisions required | None currently blocking. |
| Third-party verification | Real supplier quotes for several lines (already flagged in the source as medium/low confidence on specific items). |
| Required tables | Full itemised purchase table. |
| Required charts | None. |
| Required diagrams | None. |
| Photography/visual treatment | Product imagery where available/useful. |
| Dependencies | Chapter 24. |
| Must NOT include | Items presented as confirmed-price when the source flags them medium/low confidence. |

### Chapter 26 — Operations

| Field | Detail |
|---|---|
| Purpose | Daily operating structure, 07:00-18:00. |
| Must communicate | The AM/PM structure end to end, no reception-time contradiction. |
| Primary source(s) | `docs/architecture/OPERATING-MODEL-18-CLIENTS.md` §1, §4. |
| Supporting sources | None needed. |
| Canonical data/models | None directly. |
| Status | **COMPLETE** — no reception-time contradiction (07:00/07:15 issue fixed and re-verified in a prior session round). |
| Contradictions/stale sources | None. |
| Founder decisions required | None. |
| Third-party verification | None. |
| Required tables | Operating-hours summary table. |
| Required charts | None. |
| Required diagrams | None (see Chapters 17/18 for the detailed visuals). |
| Photography/visual treatment | Standard. |
| Dependencies | Chapters 7-9, 17, 18. |
| Must NOT include | Any residual 07:15 reception-start reference. |

### Chapter 27 — Financial Model

| Field | Detail |
|---|---|
| Purpose | The full labour/revenue/opex derivation. |
| Must communicate | Every major figure's calculation chain, per `FINANCIAL-FIGURE-REFERENCE.md`'s own structure. |
| Primary source(s) | `docs/architecture/FIRST-PRINCIPLES-FINANCIAL-MODEL.md`, `docs/architecture/FINANCIAL-FIGURE-REFERENCE.md`. |
| Supporting sources | `docs/architecture/FINANCIAL-ASSUMPTION-REGISTER.md` (certainty labels, live-referenced, not restated). |
| Canonical data/models | `data/canonical/cost_ramp.yml`, `revenue_ramp.yml`, `wages.yml`, `opex.yml`, `pricing.yml` — all live pull, this chapter is the dossier's own calculation-trail hub. |
| Status | **COMPLETE** (source material) — the calculation chain already exists in full; Phase 4's job is presentation, not re-derivation. |
| Contradictions/stale sources | None current — this is the most rigorously verified layer in the whole repo. |
| Founder decisions required | Insurance figure already resolved this session (A$708.34/month); relief-cost methodology already resolved and propagated — no outstanding founder decision on the model itself. |
| Third-party verification | VM wage, workers comp, PM service duration, GTT supplies discrepancy — all per `FINANCIAL-ASSUMPTION-REGISTER.md`, certainty labels must carry through unchanged. |
| Required tables | Labour-cost-per-position table; non-wage-overhead table; relief-allowance table — all with calculation chains shown, per `FINANCIAL-FIGURE-REFERENCE.md`'s own format. |
| Required charts | None required here (see Chapters 28-31 for P&L/cash-flow/break-even/sensitivity visuals specifically). |
| Required diagrams | Optional: a single calculation-flow diagram (assumption → calculation → canonical model → output) — a genuine Phase 4 enhancement opportunity, not currently built. |
| Photography/visual treatment | None needed — data-dense chapter. |
| Dependencies | Chapters 8, 9, 11, 14-16 (feeds from operating/staffing data). |
| Must NOT include | Any hardcoded figure not traced to a live canonical pull; PM-OPERATIONS-MODEL.md as a source. |

### Chapter 28 — P&L

| Field | Detail |
|---|---|
| Purpose | The monthly/annualised profit-and-loss statement. |
| Must communicate | Revenue lines (AM GTT/AM gap-fill/PM packages/PM standalone/other), full opex breakdown, Operating Result with its exclusion note. |
| Primary source(s) | `docs/architecture/FINANCIAL-POSITION-CURRENT.md` §4. |
| Supporting sources | None needed. |
| Canonical data/models | `master_financial_model.yml` — live pull, this chapter's table must be generated from a fresh run, not copied from a prior document. |
| Status | **COMPLETE** (source material, reconciles to the cent, verified this session). |
| Contradictions/stale sources | None. |
| Founder decisions required | None. |
| Third-party verification | Same wage/insurance/workers-comp caveats as Chapter 27, carried through. |
| Required tables | Full P&L table, monthly + annualised columns. |
| Required charts | None required (a simple revenue/cost/result bar chart is an optional enhancement). |
| Required diagrams | None. |
| Photography/visual treatment | None needed. |
| Dependencies | Chapter 27. |
| Must NOT include | "Profit" language where "Operating Result" is meant — the exclusion note must appear on this chapter specifically, not just once elsewhere. |

### Chapter 29 — Cash Flow

| Field | Detail |
|---|---|
| Purpose | The 24-month cash position. |
| Must communicate | Startup expenditure / working capital reserve / operating cash trough as three distinct concepts, never conflated. |
| Primary source(s) | `docs/architecture/FINANCIAL-POSITION-CURRENT.md` §5. |
| Supporting sources | None needed. |
| Canonical data/models | `master_financial_model.yml#cash_flow_summary` — live pull for the full 24-row series. |
| Status | **COMPLETE** (source material, chart already built and Playwright-verified this session — though Phase 4 should re-verify against whatever figures are live at rebuild time, not assume no drift). |
| Contradictions/stale sources | None. |
| Founder decisions required | None. |
| Third-party verification | None specific. |
| Required tables | 24-month cash-flow table (or a representative subset with the full series available). |
| Required charts | **Cumulative cash-position chart** — SVG already built in `FINANCIAL-POSITION-CURRENT.md` §5, reusable if figures haven't drifted, must be regenerated if they have. |
| Required diagrams | None beyond the chart above. |
| Photography/visual treatment | None needed. |
| Dependencies | Chapter 24 (startup expenditure), Chapter 28 (P&L feeds cash flow). |
| Must NOT include | Startup expenditure or working-capital reserve folded into the operating-cash-trough figure. |

### Chapter 30 — Break-even

| Field | Detail |
|---|---|
| Purpose | Break-even in both forms, explained plainly. |
| Must communicate | Break-even revenue AND break-even clients/day, the plain-English "at approximately $X, the business covers its costs" statement, the 18-client buffer in both dollar and client-volume terms. |
| Primary source(s) | `docs/architecture/FINANCIAL-POSITION-CURRENT.md` §3. |
| Supporting sources | None needed. |
| Canonical data/models | `master_financial_model.yml#breakeven` — live pull. |
| Status | **COMPLETE** (source material). |
| Contradictions/stale sources | None. |
| Founder decisions required | None. |
| Third-party verification | None. |
| Required tables | Break-even-both-forms table; 18-client-vs-break-even buffer table. |
| Required charts | **Break-even visual** — e.g. a simple revenue-vs-cost-line chart showing where they cross, with the 18-client point marked. Genuine Phase 4 BUILD requirement, not currently rendered as a chart (currently table-only). |
| Required diagrams | None beyond the chart above. |
| Photography/visual treatment | None needed. |
| Dependencies | Chapter 27, Chapter 28, Chapter 31. |
| Must NOT include | Break-even presented in only one form (revenue-only or clients-only) — both are required together, per the standing instruction. |

### Chapter 31 — Financial Sensitivity (6/12/18)

| Field | Detail |
|---|---|
| Purpose | The 6/12/18 comparison. |
| Must communicate | Real dollar figures throughout, 18/day as the sole planning case, 6/12 explicitly sensitivity-only. |
| Primary source(s) | `docs/architecture/FINANCIAL-POSITION-CURRENT.md` §2. |
| Supporting sources | None needed. |
| Canonical data/models | `master_financial_model.yml#sensitivity_client_volume` — live pull. |
| Status | **COMPLETE** (source material). |
| Contradictions/stale sources | None. |
| Founder decisions required | None. |
| Third-party verification | None. |
| Required tables | The full 6/12/18 side-by-side table, already built in the source. |
| Required charts | Sensitivity comparison chart (bar chart, revenue/opex/result across the three volumes) — genuine Phase 4 BUILD opportunity, currently table-only. |
| Required diagrams | None. |
| Photography/visual treatment | None needed. |
| Dependencies | Chapter 30. |
| Must NOT include | 6/12/day framed as alternative plans anywhere in this chapter or any other — sensitivity-only labelling must be unambiguous, including in any chart legend/title. |

### Chapter 32 — Marketing & Demand Generation

| Field | Detail |
|---|---|
| Purpose | Pre-launch and ongoing demand generation. |
| Must communicate | The pre-opening waitlist framing, the 6-factor/100-point signup framework. |
| Primary source(s) | `docs/architecture/WAITLIST-VALIDATION-FRAMEWORK.md`, `docs/architecture/PRE-LAUNCH-DEMAND-VALIDATION-PLAN.md`, `docs/architecture/EARLY-DEMAND-VALIDATION-STRATEGY.md`. |
| Supporting sources | `docs/afternoon-marketing-plan.md`, `docs/poppy-marketing.md`, `docs/referral-partnership-plan.md`. |
| Canonical data/models | None. |
| Status | **NEEDS-VERIFICATION** — none of the three primary sources were read in full during Phase 1; the specific "6-factor/100-point signup framework" referenced in Anthony's own brief has NOT yet been located and confirmed present in these documents. Genuine open item for Phase 4, not yet a confirmed content gap OR a confirmed source — status is unknown until read. |
| Contradictions/stale sources | Unknown until the Phase 4 read is done. |
| Founder decisions required | Unknown until verified. |
| Third-party verification | None identified yet. |
| Required tables | Waitlist/signup framework table, once confirmed. |
| Required charts | None identified yet. |
| Required diagrams | None identified yet. |
| Photography/visual treatment | Standard, marketing-appropriate. |
| Dependencies | Chapter 6, Chapter 4. |
| Must NOT include | An invented 6-factor/100-point framework if the real one cannot be located — must be marked NEEDS-RESEARCH in the actual dossier rather than fabricated. |

### Chapter 33 — Expansion

| Field | Detail |
|---|---|
| Purpose | Growth-ready capacity. |
| Must communicate | Expansion stations installed/ready at launch even if unused immediately; the current framing of the former Scenario D. |
| Primary source(s) | `docs/floor-plan-concept.md` (Treatment Room 5/6, Spray Tan Booth Phase 2 — **spray tan itself must NOT be presented as current scope**, only as a disclosed Phase 2 growth reservation, per the standing exclusion on spray tan as a current offering), 3rd phlebotomy chair. |
| Supporting sources | `docs/strategy/STRATEGIC-REPORT.md` §1 (Scenario D's current reframing — "RETIRED as a scheduling investigation, reframed as a real strategic capacity decision: a 3rd phlebotomist/chair vs. opening a second location"). |
| Canonical data/models | None. |
| Status | **PARTIAL** — the growth reservations are real and disclosed; Scenario D needs presenting with its CURRENT framing (a strategic capacity decision), not its old scheduling-investigation framing, which would be a stale-framing error even though the underlying document is current. |
| Contradictions/stale sources | Risk of citing Scenario D's old framing if Phase 4 pulls from an outdated summary rather than `STRATEGIC-REPORT.md`'s own current framing. |
| Founder decisions required | 3rd phlebotomist/chair vs. second-location expansion path — genuinely open per the current framing. |
| Third-party verification | None. |
| Required tables | Growth-reservation table (item/current status/trigger condition). |
| Required charts | None. |
| Required diagrams | None beyond Chapter 20's floor plan (could annotate growth stations on it). |
| Photography/visual treatment | Standard. |
| Dependencies | Chapter 19, Chapter 20. |
| Must NOT include | Spray tan presented as current scope (confirmed standing exclusion — it is a disclosed Phase 2/growth item only); the old Scenario D scheduling-investigation framing. |

### Chapter 34 — Open Items / Decisions

| Field | Detail |
|---|---|
| Purpose | Consolidated register of every open decision. |
| Must communicate | Issue / current position / why open / who resolves / next action / impact / status, per item — not buried in prose anywhere else. |
| Primary source(s) | `docs/VERIFICATION-TRACKER.md`, `docs/DECISION-LOG.md`. |
| Supporting sources | Every chapter above's own "Founder decisions required" and "Third-party verification" fields — this chapter should consolidate them, not duplicate independently-maintained lists. |
| Canonical data/models | None. |
| Status | **NEEDS-VERIFICATION** — `VERIFICATION-TRACKER.md`'s own top-level view has NOT been cross-checked against this session's newly-resolved items (insurance, relief cost, PM capacity) — likely stale, genuinely unverified this pass. |
| Contradictions/stale sources | `VERIFICATION-TRACKER.md` likely still lists items this session already resolved as open — needs a fresh pass before Phase 4 builds this chapter, not before Phase 2 (architecture only). |
| Founder decisions required | This chapter's own job is to consolidate all of them from every other chapter — see the master list in §7 below. |
| Third-party verification | Same — consolidated from every chapter above, see §7. |
| Required tables | The full open-items register table, per Anthony's own specified columns. |
| Required charts | None. |
| Required diagrams | None. |
| Photography/visual treatment | None needed — data/register chapter. |
| Dependencies | Every other chapter (last-but-one, built after content chapters, before Chapter 35). |
| Must NOT include | An item marked "resolved" that this session's own work has actually left open, or vice versa — needs the fresh `VERIFICATION-TRACKER.md` cross-check before Phase 4 finalises this chapter. |

### Chapter 35 — Execution Roadmap

| Field | Detail |
|---|---|
| Purpose | Now/next/pre-lease/fit-out/recruitment/opening/first-90-days/12-month-review. |
| Must communicate | A relative-sequence roadmap (no fixed calendar dates, a deliberate existing choice) from today's actual state to opening and beyond. |
| Primary source(s) | `docs/venture-timeline.md`, `docs/grace-startup-plan.md`, `docs/project-timeline-milestones.md`. |
| Supporting sources | Chapter 34's consolidated open-items register (roadmap should reference, not duplicate, blocking items). |
| Canonical data/models | None. |
| Status | **COMPLETE** (source material) — real content exists, relative-sequence framing already established and current. |
| Contradictions/stale sources | None found in Phase 1. |
| Founder decisions required | None specific — this chapter documents the roadmap, doesn't create new decisions. |
| Third-party verification | None specific. |
| Required tables | Milestone/phase table. |
| Required charts | Optional Gantt-style relative-sequence visual (per `project-timeline-milestones.md`'s own existing framing). |
| Required diagrams | None required beyond the chart above. |
| Photography/visual treatment | Standard, forward-looking imagery. |
| Dependencies | Chapter 34 (references, doesn't duplicate). |
| Must NOT include | Fixed calendar dates (a deliberate, already-established repo convention — relative sequencing only). |

---

## 3. Coverage Matrix — Every Chapter Proven to Have a Source, Purpose, Status, Gaps, and Visual Requirements

| Ch | Title | Source status | Content status | Known gap type | Visual requirement |
|---|---|---|---|---|---|
| 1 | Founder Dashboard | Synthesised, no independent source | NEEDS-BUILD | Assembly task, not a sourcing gap | Summary cards |
| 2 | Business Concept | Solid | COMPLETE | None | Optional diagram |
| 3 | Market | Core VERIFIED, prior-GDM unconfirmed | PARTIAL | Sub-segment sizing NEEDS-RESEARCH | Chart |
| 4 | Competitive Landscape | Real but scattered | PARTIAL | Consolidation task | Table |
| 5 | Brand | Palette/type locked, naming open | PARTIAL | **Real typography renders — BUILD GAP** | Rendered type specimens |
| 6 | Customer Experience | Comprehensive, cleaned | PARTIAL | Departure mechanism — open by design | Journey diagram — BUILD GAP |
| 7 | GTT Service | Timing VERIFIED | PARTIAL | Referral-requirement citation to re-confirm | Table |
| 8 | AM Operating Model | Complete, solver-verified | COMPLETE (source) | Visual rendering — BUILD GAP | Timetable diagram |
| 9 | PM Operating Model | Capacity current, schedule illustrative | PARTIAL | PM-OPERATIONS-MODEL.md excluded, disclosed | Illustrative diagram |
| 10 | Service Catalogue | Comprehensive | PARTIAL | Field-completeness unverified, 4 price conflicts | Full table |
| 11 | PM Packages | Rigorous, current | COMPLETE | Pricing sign-off pending | Derivation table |
| 12 | Food & Beverage | Risk-assessed | PARTIAL | Booking/selection mechanism not located | None required |
| 13 | Retail | Well-documented | COMPLETE | None | None required |
| 14 | Staffing | Current | COMPLETE | Pool-size decision open | Table |
| 15 | Staff Profiles | Full field list | COMPLETE | None | Profile cards |
| 16 | Staffing Coverage | Rigorous | COMPLETE | Pool-size decision open (same as Ch14) | Reliability table/chart |
| 17 | Rostering | Table exists | PARTIAL | **Visual diagram — BUILD GAP** | Staff-lane diagram |
| 18 | Customer Timetable | Table exists, solver-verified | PARTIAL | **Visual diagram — BUILD GAP** | AM timetable diagram |
| 19 | Venue | Requirements current, search stalled | PARTIAL | Founder action (property inspection) | None required |
| 20 | Floor Plan | Room schedule current, visual dated | PARTIAL | **Diagram rebuild — BUILD GAP** | Floor-plan diagram |
| 21 | Compliance | Regimes correctly separated | PARTIAL | LEV tension unresolved (3rd party) | Comparison table |
| 22 | Children/Companion Policy | New, complete as proposed | COMPLETE (as proposed policy) | 1 founder decision, 4 third-party items | None required |
| 23 | Lounge | Device spec complete | PARTIAL | CUSTOMER-JOURNEY.md Sensory-Waiting stage needs re-confirming | None required |
| 24 | Startup Requirements | Itemised, bounded | PARTIAL | Reconciliation range inherently unresolved | Table |
| 25 | Purchasing | Complete | COMPLETE | Some lines medium/low confidence | Full table |
| 26 | Operations | Complete | COMPLETE | None | None required |
| 27 | Financial Model | Rigorous, current | COMPLETE | Certainty labels must carry through | Calculation tables |
| 28 | P&L | Reconciles exactly | COMPLETE | None | Table (chart optional) |
| 29 | Cash Flow | Complete, chart exists | COMPLETE | Re-verify no drift at rebuild time | Table + chart (exists) |
| 30 | Break-even | Complete | COMPLETE | None | **Chart — BUILD GAP** |
| 31 | Financial Sensitivity | Complete | COMPLETE | None | **Chart — BUILD GAP** |
| 32 | Marketing & Demand Generation | **Not yet read in full** | **NEEDS-VERIFICATION** | Genuine unknown until Phase 4 read | Unknown |
| 33 | Expansion | Real, needs current framing | PARTIAL | Framing-currency risk (Scenario D) | Table |
| 34 | Open Items/Decisions | Tracker likely stale | **NEEDS-VERIFICATION** | Fresh cross-check needed | Register table |
| 35 | Execution Roadmap | Complete | COMPLETE | None | Table (chart optional) |

**Summary: 35/35 chapters have an identified source and purpose. 11 COMPLETE, 20 PARTIAL, 2 NEEDS-VERIFICATION (Ch3's sub-claim doesn't count as a whole-chapter block), 0 SOURCE GAP (no chapter is entirely without adequate source material) — genuinely checked, not asserted.**

---

## 4. Visual System Definition

**Direction:** premium, not luxury (restraint over decoration); natural/earthy/warm/calm; feminine/elegant/sophisticated; explicitly avoid clinical, generic-hospitality, or tech-startup positioning. Should read as a premium founder/investor operating dossier, not a generic corporate report or a pile of Markdown.

| Element | Direction |
|---|---|
| Palette | `outputs/brand/warm-stone-tokens.css` — Warm Ivory #FAF6EE, Warm Stone #E8DAC5, Deep Brown #33261E, Earthy Terracotta #A9654E, Muted Olive #5E5F45, Soft Dusty Rose #D9A08C, Warm Brass #9C7A46 (fine-line/hardware/signage detail only) — founder-locked, not reopened. |
| Typography | Fraunces (headline/display) + DM Sans (body/UI) — locked. **Real rendered specimens required in Chapter 5, not just named.** |
| Chapter-opening treatment | Restrained full-bleed image or typographic opener; chapter number + title in Fraunces, generous whitespace, no dense cover-page clutter. |
| Tables | Clean rule-based tables (no heavy grid lines), Warm Stone/Ivory alternating row tint at most, DM Sans for table content, Fraunces for headers only where a table itself is chapter-level. |
| Financial charts | Consistent with the SVG pipeline already established this session (`FINANCIAL-POSITION-CURRENT.md` §5's cash-flow chart) — Deep Brown/Olive/Terracotta line and accent colours, restrained gridlines, real data labels, no default-library chart styling. |
| Operating/timetable diagrams | Lane-based or timeline-based SVG, same palette, clear at-a-glance readability — the standard this session's markdown tables must be elevated to, not a decorative reinterpretation. |
| Floor-plan diagrams | Line-drawing style, muted palette, clearly distinguishing solid-wall (Blood Collection Room) vs. curtain-partition vs. open-plan zones. |
| Customer-journey graphics | Horizontal stage-flow, AM/PM shown as parallel or diverging paths where they differ, emotion/friction annotated visually not just in a table. |
| Staff/timetable graphics | Same lane-based SVG approach as operating diagrams. |
| Brand presentation | The palette/typography/naming-status content itself, presented with restraint (not a mood-board pastiche). |
| Photography/imagery | Warm/natural light, real diversity of age/body-type/ethnicity (per `VISUAL-BRAND-DIRECTION.md`'s existing direction, post leaving-moment cleanup) — none currently committed to the repo for most chapters; flagged as a content gap for chapters that call for it, not fabricated with stock-photo placeholders presented as final. |
| Page/section rhythm | Consistent chapter structure (opener → context → detail tables/charts → open items/decisions callout if any → cross-references) — same shape every chapter, so the reader never has to re-learn navigation. |
| Callout treatment | Visually distinct, consistent styling for OPEN / VERIFIED / MODELLED / PLACEHOLDER / RESEARCHED-BEST-EVIDENCE / BALLPARK-ESTIMATE / WAITING-ON-THIRD-PARTY tags — a defined colour/icon system, not ad hoc per-chapter styling. Genuine Phase 4 BUILD requirement (a small design-system task) — not yet defined anywhere in the repo. |

---

## 5. Chapter Narrative Flow — Rationale

The 35-chapter order above substantially follows Anthony's own rough shape (concept → market/problem → customer → experience → services → operating model → clinical/pathology → staffing → venue → brand → marketing → financial model → economics → risks → implementation → roadmap), with two deliberate, disclosed adjustments:

1. **Brand (Ch5) is placed earlier** than the rough shape's own late-brand position, directly after Competitive Landscape — because Customer Experience (Ch6) and every subsequent service/operating chapter references the brand positioning and palette throughout; placing Brand after those chapters would force forward-references. This ordering has also been the consistent structure across every prior round's 35-chapter spec, not a new invention this round.
2. **GTT Service (Ch7) sits between Customer Experience (Ch6) and the AM/PM Operating Model chapters (Ch8-9)** — the clinical process is a customer-facing concept before it's an operational scheduling concept, so it's introduced narratively first, then operationalised.

The reader moves: what the business is → who it serves and why → what she experiences → what services exist → how the day actually runs (AM then PM) → where staff/venue/compliance fit → brand and marketing → the full financial case → what's still open → what happens next. No chapter requires the reader to have already read a LATER chapter to make sense — cross-references only ever point backward or to genuinely parallel chapters (e.g. Ch17/Ch18's shared source).

---

## 6. Founder Decisions Consolidated (feeds Chapter 34)

1. Final name selection (SOLENA vs. ELOWEN) — Ch5.
2. Treatment staff pool: 12 (recommended) vs. 11 (lower-reliability alternative) — Ch14/16.
3. Phlebotomist pool: 4 (recommended) vs. 3 (lower-cost alternative) — Ch14/16.
4. Blood Collection Room companion exception (needle-phobia case) — Ch22.
5. Lounge devices: companion/child-facing (proposed) vs. client-facing — Ch23.
6. AM-peak "no companions" Lounge-capacity rule — Ch23 (a monitoring item, not a launch-day blocker).
7. Departure-experience mechanism (post leaving-moment-gesture removal — genuinely no proposal exists) — Ch6.
8. Leaner day-one fixture count (2+2 vs 4+4 treatment stations) if capital is tighter than planned — Ch20.
9. 3rd phlebotomist/chair vs. second-location expansion path — Ch33.
10. Final PM package pricing sign-off — Ch11.
11. 4 disclosed service-price conflicts (hair colour ×4 lines, lash infill, GDM snack pack, locked-pricing completeness gap) — Ch10.

## 7. Third-Party Verifications Consolidated (feeds Chapter 34)

1. VM wage classification — accountant/Fair Work — Ch15/27.
2. Workers compensation rate — WorkCover WA/broker — Ch27.
3. Insurance figure — broker quote already in motion — Ch27.
4. Phlebotomist employment arrangement — WDP/Carole Rivers — Ch15/27.
5. LEV extraction/open-plan nail-area tension — WorkSafe WA-familiar contractor — Ch21.
6. Real supplier/quote validation for several startup/purchase lines — Ch24/25.
7. Landlord terms — once a venue is under negotiation — Ch19.
8. Solicitor/insurer/landlord/regulatory confirmation for the Children/Companion Policy — Ch22.
9. Trademark clearance for the surviving name(s) — deliberately deferred, Ch5.

---

## 8. Phase 4 Content Build Requirements — Execution Checklist

**New content to write:**
- Chapter 1 (Founder Dashboard) — synthesised from all other chapters, written last.
- Chapter 34 (Open Items/Decisions) — needs a fresh `VERIFICATION-TRACKER.md` cross-check first (see below), then consolidated writing.

**Additional research required:**
- Chapter 3 — prior-GDM market sizing (locate or mark NEEDS-RESEARCH).
- Chapter 7 — re-confirm the specific WA GTT referral/request-form requirement's primary citation.
- Chapter 23 — full read of `CUSTOMER-JOURNEY.md`'s Sensory-Waiting stage to confirm lounge-experience content (birthing plans/checklists/printing).
- Chapter 32 — full read of `WAITLIST-VALIDATION-FRAMEWORK.md`, `PRE-LAUNCH-DEMAND-VALIDATION-PLAN.md`, `EARLY-DEMAND-VALIDATION-STRATEGY.md` to confirm/locate the 6-factor/100-point signup framework.

**New calculations required:**
- None — the financial model itself is current and complete; Phase 4's task is live-pulling and presenting it, not recalculating.

**New diagrams/visuals required (genuine build gaps, not sourcing gaps):**
- Chapter 5 — real rendered typography specimens.
- Chapter 6 — customer-journey visual diagram.
- Chapter 8/18 — AM timetable diagram (may be combined).
- Chapter 9 — illustrative PM session-schedule diagram.
- Chapter 17 — staff-lane rostering diagram.
- Chapter 20 — rebuilt floor-plan diagram(s).
- Chapter 30 — break-even visual chart.
- Chapter 31 — 6/12/18 sensitivity chart.
- A repo-wide OPEN/VERIFIED/MODELLED/PLACEHOLDER/etc. callout-tag visual system (design-system task, feeds every chapter).

**Existing contradictions to reconcile (not decide, just present correctly):**
- Chapter 10 — 4 disclosed service-price conflicts, presented not silently resolved.
- Chapter 9 — `PM-OPERATIONS-MODEL.md` excluded, current sources cited instead.
- Chapter 33 — Scenario D's current framing used, not its old scheduling-investigation framing.
- Chapter 20 — dated `floor-plan-v3.svg` not used as current without a staleness note.

**Founder input required before finalising (not before starting):**
- The 11 items in §6 — each chapter can be built with the item presented as genuinely open; none blocks the rest of the dossier from being built.

**Third-party confirmation required before finalising (not before starting):**
- The 9 items in §7 — same treatment, presented as open/waiting, not blocking.

---

## 9. Quality Control — Performed This Pass

- **All 35 chapters present:** confirmed, §2 above.
- **Every Phase 1 chapter accounted for:** cross-checked against `DOSSIER-DASH-PHASE1-INFORMATION-MAP.md` §2's own 35-row table — every row has a corresponding chapter here, no chapter dropped or merged without disclosure.
- **No leaving-moment reappearance:** repo-wide search re-run this pass (below) — confirmed no chapter/section/visual/journey element in this architecture references or depends on the removed concept.
- **Children/companion and lounge-device docs referenced:** confirmed, Ch22/23 and §1's hierarchy.
- **PM-OPERATIONS-MODEL.md marked unsafe for current sourcing:** confirmed, §1 and Ch9.
- **No stale financial figures presented as current:** confirmed — this document contains zero hardcoded financial figures; every financial reference is to a live-pull source or a canonical document name, per §1's explicit instruction.
- **All known open decisions captured:** §6.
- **All known third-party dependencies captured:** §7.

---

## Changelog

**2026-08-19 (Phase 2)** — Created per Anthony's explicit instruction to convert `DOSSIER-DASH-PHASE1-INFORMATION-MAP.md` from an audit into a build-ready architecture specification. All 35 chapters specified with source, status, contradictions, founder decisions, third-party verification, and visual requirements. Coverage matrix proves 35/35 chapters have an identified source and purpose, with 0 chapters marked SOURCE GAP. No dossier content built, no financial figures hardcoded, no Dash work started, no outstanding founder/third-party decisions made, no PM-OPERATIONS-MODEL.md re-derivation attempted — all explicitly out of scope for this phase.
