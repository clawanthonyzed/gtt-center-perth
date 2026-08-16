# GTT Center Perth — Reading Order & Big-Picture Status

**Last updated:** 2026-08-15 (reassessed — see changelog) | Structure below the 60-second version is otherwise unchanged from the 2026-07-20 rebuild except where individually flagged.
**Total documents:** 110+ in `docs/*.md` alone, plus a further ~40 across `docs/strategy/`, `docs/naming/`, `docs/experience/`, `docs/architecture/`, and `outputs/brand/` — see `docs/00_document_inventory.md`'s new "Strategy / Brand / Venue / Naming Layer" section for that part of the corpus, which this file did not cover before 2026-08-15.
**Purpose:** Read this ONE document to see the current, accurate, big-picture state of the venture and what order to read everything else in. `docs/00_document_inventory.md` is the full per-file status list. **For the current canonical model (pricing, capacity, headcount, P&L), always defer to [docs/CURRENT-STATE.md](CURRENT-STATE.md) over any figure stated in this file.**

---

## THE 60-SECOND VERSION

GTT Center Perth is a concept for WA's first premium wellness venue built around the mandatory Glucose Tolerance Test — patients spend the ~2-2.5 hour test wait getting massage/nails/hair/brows instead of sitting in a bare pathology room. **No venue location is secured yet — that is the single blocking gate on everything else** (staff recruitment, fit-out, everything downstream), though a real property shortlist with two strong Tier-1 candidates now exists (`docs/strategy/PERTH-PROPERTY-SHORTLIST.md`), unactioned. **Current committed operational model (per `docs/CURRENT-STATE.md`, RECALCULATED 2026-08-09 for superannuation — corrects the figures previously stated here):** PRIMARY reference is Table 1, 18 clients/day, 07:00 start, 25-min pair cadence, projected **+A$56,581.70/month** at Month 5+ steady state; SECONDARY reference is Table 2, 12 clients/day, 08:00 start, same cadence, **+A$21,056.64/month**. Both are planning estimates, not real trading data. Two package prices (A$250/A$300), full payment collected at booking. Pathology partner (WDP, priority 1) has been in active correspondence since 2026-07-27 — several regulatory/commercial questions resolved, the commercial rental figure still outstanding, status is simply **waiting on Carole/WDP**, not a research gap. **Naming is narrowed to two live candidates, SOLENA and ELOWEN, neither selected** — trademark clearance is written and ready, deliberately deferred by Anthony to a later funding milestone (`docs/naming/NAMING-DECISION-STATE.md`). **A full visual brand system is built and locked** (palette, typography, wordmark-led logo direction — `outputs/brand/warm-stone-tokens.css`), applied identically to both names, viewable in `outputs/brand/SOLENA-vs-ELOWEN-VISUAL-REVIEW.pdf`. Self-funded (Anthony + Imara joint savings), no external investor, no launch date set.

**For a presentation to a non-technical stakeholder (e.g., Anthony's partner Imara): read [gtt-center-perth-overview-for-imara.md](gtt-center-perth-overview-for-imara.md).** It's a plain-language, story-format walkthrough built specifically for this purpose. [executive-summary.md](executive-summary.md) is the fuller, more technically-sourced standalone summary if more detail is needed (figures corrected 2026-08-15).

**For a document to actually hand a property agent, WDP, a pathology partner, a bank, an accountant, or a solicitor: read [`outputs/GTT-CENTER-PERTH-VENTURE-OVERVIEW.md`](../outputs/GTT-CENTER-PERTH-VENTURE-OVERVIEW.md).** New 2026-08-15/16 — built specifically for external professional handoff, existing figures only.

---

## WHAT'S NEW — 2026-08-15/16 EXTERNAL EXECUTION ROUND

An execution round focused on BUILT, committed outputs rather than more recommendations. Five new deliverables — all committed locally, not yet pushed (see `docs/00_document_inventory.md`'s new "External Execution Round" section for the full table with status):

1. **[`outputs/landing-page/`](../outputs/landing-page/index.html)** — public-ready, neutral-name demand-validation landing page, reskinned to the locked brand palette. Repo-ready, not internet-live — see `outputs/landing-page/qa/QA-NOTES.md` for exactly what deploying it publicly would still require.
2. **[`outputs/GTT-CENTER-PERTH-VENTURE-OVERVIEW.md`](../outputs/GTT-CENTER-PERTH-VENTURE-OVERVIEW.md)** — the external-facing pack, see above.
3. **Three ready-now outreach drafts** — [accountant](accountant-engagement-email-draft.md), [insurance broker](insurance-broker-quote-request-draft.md), [Fair Work Infoline script](fairwork-infoline-query-script.md).
4. **[`docs/architecture/STARTUP-COST-REDUCTION-ACTIONS.md`](architecture/STARTUP-COST-REDUCTION-ACTIONS.md)** — concrete DO NOW / WAIT FOR VENUE / WAIT FOR WDP action table, no new analysis.
5. **[`docs/experience/AM-TO-PM-DATA-CAPTURE-SPECIFICATION.md`](experience/AM-TO-PM-DATA-CAPTURE-SPECIFICATION.md)** — what data needs capturing to eventually measure the RETURN-LOOP.md mechanism.

**What Anthony can action immediately from this round, with zero further drafting needed:** send the accountant/insurance emails (once he picks a firm/broker), call the Fair Work Infoline, send the curtain-supplier pricing enquiry (`STARTUP-COST-REDUCTION-ACTIONS.md` Appendix B), and decide whether/when to take the landing page live (5 concrete pre-conditions listed in its own QA notes).

---

## ANTHONY'S READING PATH — REASSESSED 2026-08-15, SMALLEST USEFUL SET

Nine documents genuinely cover the venture as it stands today. Everything else in this file is detail, reference, or historical trace — read on demand, not linearly.

**READ FIRST (essential — the current picture, ~30 min total):**
1. [CURRENT-STATE.md](CURRENT-STATE.md) — the one file every number in the venture traces back to. Read this before trusting any figure anywhere else.
2. [strategy/STRATEGIC-REPORT.md](strategy/STRATEGIC-REPORT.md) — the consolidated synthesis of business, experience, and naming state as of 2026-08-14; the fastest way to get current on everything at once.
3. [naming/NAMING-DECISION-STATE.md](naming/NAMING-DECISION-STATE.md) — exactly where naming stands (SOLENA conditional leader, ELOWEN live fallback, why neither is locked yet).
4. [strategy/PERTH-PROPERTY-SHORTLIST.md](strategy/PERTH-PROPERTY-SHORTLIST.md) — the real, actionable item: two Tier-1 property candidates exist and are waiting on a phone call.
5. [VERIFICATION-TRACKER.md](VERIFICATION-TRACKER.md) — the single prioritised list of what's actually still open and who can resolve it.

**READ SECOND (important — the brand/venue/experience picture, ~20 min):**
6. `outputs/brand/SOLENA-vs-ELOWEN-VISUAL-REVIEW.pdf` — see the actual brand work rather than reading about it; both names, side by side, real applications.
7. [strategy/VENUE-FUNCTIONAL-BRIEF.md](strategy/VENUE-FUNCTIONAL-BRIEF.md) — what a real venue needs to provide, validated against the 18/day model.
8. [experience/RETURN-LOOP.md](experience/RETURN-LOOP.md) — the AM→PM mechanism the whole growth thesis depends on, and the single biggest unmodelled financial gap.

**READ THIRD (operational/financial detail — only if you need the underlying number):**
9. [business-plan.md](business-plan.md) — full detail behind everything summarised above.

**READ ONLY WHEN NEEDED (reference, not narrative):** `docs/00_document_inventory.md` (full file-by-file status), `docs/01_conflicts_log.md` (why a figure changed), individual financial breakdowns (`profit-loss-tables.md`, `data/canonical/*.yml`), legal drafts (`privacy-policy.md`, `consent-form.md` — both still solicitor-review-pending).

**DO NOT READ YET / DEFER:** `HANDOFF.md` (superseded twice, historical trace only), `capacity-pricing-audit.md` (superseded), anything in `docs/archive/`, the older sage-palette `outputs/brand/BRAND-SYSTEM.md`/`outputs/landing-page/` (superseded by the locked palette and the named landing pages).

---

## WHAT CHANGED THIS SESSION (2026-07-19 to 2026-07-20) — Read This Before Anything Else

This was a large consolidation session. If you read nothing else in this section, know these five things:

1. **"Imara" no longer means the on-site operator anywhere in this corpus.** A new "Venue Manager" role (not yet hired, recruitment gated on securing a venue location) now covers every day-to-day duty. Imara remains the funding partner/trust beneficiary — her role is ownership/funding only, unchanged.
2. **The financial model was internally inconsistent across several documents — this is now resolved (CONFLICT-08).** Some older documents ([pm-staffing-roster.md](pm-staffing-roster.md), [feasibility.md](feasibility.md), [capacity-pricing-audit.md](capacity-pricing-audit.md)) carried stale figures (an 8-client AM model instead of the current 10-client Scenario C, and a WA-births figure that didn't match [research.md](research.md)). All are now corrected or clearly flagged as superseded. **[profit-loss-tables.md](profit-loss-tables.md) v2.0 is the current authoritative financial figure: +A$25,087.07/month at Month 5+ steady state.**
3. **The payment/deposit policy was also inconsistent — this is now resolved (CONFLICT-09).** Confirmed model: full package price collected at time of booking, not a deposit. Corrected everywhere it appeared wrong.
4. **12 new documents were built** covering regulatory tracking, SWOT, a ranked risk register, break-even/sensitivity analysis, a referral partnership plan, a pricing/billing strategy explainer, a project timeline, plus this session's audit-trail documents (`00`-`05` numbered files) and a new scheduling investigation ([scenario-e-floating-chair-investigation.md](scenario-e-floating-chair-investigation.md)).
5. **Two things were genuinely unresolved and flagged as of 2026-07-20, not silently ignored — status corrected 2026-08-08:** [operations-manual.md](operations-manual.md)'s detailed scheduling section (CONFLICT-03) **was subsequently rewritten 2026-07-30** to the then-current 12-client model — it no longer shows the old 8-client model, though it is now itself one rebase behind `docs/CURRENT-STATE.md`'s 2026-08-05 Table 1/Table 2 figures (see the Phase 4/5 notes below). [workflow.md](workflow.md)'s staffing table **still describes the old subtenant model** (CONFLICT-04) — confirmed still open as of 2026-08-08, not yet rewritten. Neither document is safe to train new staff from as-is.

**For the full session work log:** [01_conflicts_log.md](01_conflicts_log.md) (every conflict found, with resolution status) and [00_document_inventory.md](00_document_inventory.md) (every file, current status).

---

## THE CORE STATUS DOCUMENTS (Legacy Index — Superseded as the "Read First" List by the Reassessed Path Above)

**This table is retained for its still-useful Phase 1-12 detailed operational index below (PHASE 1 through PHASE 12 sections) — but as a *first* reading list it has been superseded by "ANTHONY'S READING PATH" above, which reflects everything now in the repository, not just `docs/*.md`.** Use this table only if you want the original July reading sequence for the operational/financial/clinical layer specifically.

| # | Document | What it's for | Time |
|---|---|---|---|
| 1 | **This file ([reading-order.md](reading-order.md))** | Big-picture entry point — you're reading it | 5 min |
| 2 | **[gtt-center-perth-overview-for-imara.md](gtt-center-perth-overview-for-imara.md)** | Plain-language, presentation-ready summary — for a non-technical stakeholder | 10 min |
| 3 | **[executive-summary.md](executive-summary.md)** | Fuller standalone summary, more technically sourced | 10 min |
| 4 | **[HANDOFF.md](HANDOFF.md)** | Session handoff dated 2026-07-17 — **no longer the most recent, and no longer the source of truth for the current model** (superseded twice since: the 2026-07-30 12-client rebase, then the 2026-08-05 Table 1/Table 2 rebase). Retained for methodology/historical detail only — carries its own staleness banner. Use [CURRENT-STATE.md](CURRENT-STATE.md) for current figures | 15 min |
| 5 | **[00_document_inventory.md](00_document_inventory.md)** | Every file in this corpus, current status, one line each | 10 min (reference, not linear read) |
| 6 | **[01_conflicts_log.md](01_conflicts_log.md)** | Every conflict found this session, resolution status — read if you want to know *why* a figure changed | 15 min (reference) |
| 7 | **[VERIFICATION-TRACKER.md](VERIFICATION-TRACKER.md)** | The prioritised, dependency-based to-do list — what to actually do next, in what order | 10 min |
| 8 | **[VERIFICATION-TRACKER.md](VERIFICATION-TRACKER.md)** | The single list of questions only Anthony can answer | 5 min |

---

## PHASE 1: THE BUSINESS CASE

| # | Document | What it contains |
|---|---|---|
| 8 | [business-plan.md](business-plan.md) | Full business plan — vision, model, market, competitive position, financials, risks (v3.0, fully rewritten this session) |
| 9 | [feasibility.md](feasibility.md) | Go/no-go assessment, market sizing (corrected this session), risks |
| 10 | [swot-analysis.md](swot-analysis.md) | Strengths/Weaknesses/Opportunities/Threats — new this session |
| 11 | [risk-register.md](risk-register.md) | Ranked risk table (likelihood × impact × mitigation × owner) — new this session |
| 12 | [VERIFICATION-TRACKER.md](VERIFICATION-TRACKER.md) | Regulatory/accreditation checklist with status — new this session |
| 12a | [external-resources-and-advisors.md](external-resources-and-advisors.md) | Which external professionals/services are needed and when — new this session |

## PHASE 2: FINANCIALS

| # | Document | What it contains |
|---|---|---|
| 13 | [profit-loss-tables.md](profit-loss-tables.md) | **Current canonical P&L** — weekday/weekly/monthly/quarterly/yearly steady-state, plus Year 1 monthly ramp and Years 1-3 annual (added this session) |
| 14 | [cash-flow.md](cash-flow.md) | 18-month cash flow — methodology reference only, absolute figures are stale (built on the old 8-client model), see its own banner |
| 15 | [break-even-sensitivity-analysis.md](break-even-sensitivity-analysis.md) | Best/base/worst case on volume and pricing — new this session |
| 16 | [price-increase-comparison.md](price-increase-comparison.md) | Analysis of when/whether to raise package prices — new this session |
| 17 | [pricing-billing-strategy.md](pricing-billing-strategy.md) | Private vs bulk billing rationale, Medicare specifics flagged as requiring verification — new this session |
| 17a | [pm-package-structure.md](pm-package-structure.md) | **COMMITTED direction** — PM now offers set/fixed packages alongside standalone services, with a "push toward package" sales strategy; proposed pricing needs Anthony's sign-off. Supersedes the deleted `pm-package-exploration.md`. |
| 18 | [financial-break-even-staff.md](financial-break-even-staff.md) | Per-employee break-even, package pricing model |
| 19 | [unit-economics.md](unit-economics.md) | Revenue per visit |
| 20 | [financial-setup.md](financial-setup.md) | Trust bank accounts, Xero, payment systems (payment policy corrected this session) |
| 20a | [revenue-extraction-options.md](revenue-extraction-options.md) | General mechanisms for Anthony/Imara to draw income from the trust (distribution, wages, director fees) — TPI-specific optimisation explicitly out of scope, new this session |
| 21 | [financial-model.md](financial-model.md) | **SUPERSEDED (self-declared)** — trust/ownership entity structure content only, left untouched this session per explicit scope instruction |

## PHASE 3: SERVICES & PRICING

| # | Document | What it contains |
|---|---|---|
| 22 | [services-master-table.md](services-master-table.md) | Every service, staff, duration, price |
| 23 | [services-pricing-locked.md](services-pricing-locked.md) | **Canonical pricing** — Package 1 (A$250, fixed 2×30min) + Package 2 (A$300, flexible composition), renamed/renumbered 2026-07-20, same 2 price points as before |
| 24 | [extended-wellness-services.md](extended-wellness-services.md) | GDM info, belly casting, birth plan, day spa expansion |
| 25 | [market-research-findings.md](market-research-findings.md) | Competitor (MIWM) research, pricing benchmarks — 3D scan reframed as future/Phase 2 this session |

## PHASE 4: CLINICAL & SCHEDULING

| # | Document | What it contains |
|---|---|---|
| 26 | [gtt-clinical-protocol.md](gtt-clinical-protocol.md) | GTT procedure detail, phlebotomist protocol |
| 27 | [gtt-test-reference.md](gtt-test-reference.md) | Quick reference card for staff |
| 28 | [pathology-collection-room.md](pathology-collection-room.md) | Collection room fit-out spec |
| 29 | [scenario-c-sync-timetables.md](scenario-c-sync-timetables.md) | **Canonical scheduling model** — originally 10 clients/day (historical), synchronized start, verified zero double-bookings; now also houses the current 18-client Table 1 primary model (2026-08-05 rebase) |
| 30 | [draw-event-scheduler-findings.md](draw-event-scheduler-findings.md) | Solver-based verification of why the current model is at its true capacity optimum |
| 31 | [scenario-e-floating-chair-investigation.md](scenario-e-floating-chair-investigation.md) | New this session — investigated whether decoupling clients from a fixed chair adds capacity (verdict: no, zero gain, exploratory only); also answers the specific 11th-client-at-09:55 question (no) |
| 31a | [am-staffing-by-volume.md](am-staffing-by-volume.md) | Checked phlebotomist/treatment staffing + full-day rosters for every AM volume from 3 to 10 clients/day (historical volume range, methodology still valid, see docs/CURRENT-STATE.md for the current committed volume) |
| 32 | [scenario-d-investigation.md](scenario-d-investigation.md) | Growth scenario — 15 clients/day, 3rd phlebotomist, not yet committed |
| 33 | [am-capacity-weekend.md](am-capacity-weekend.md) | AM capacity history, Saturday/Sunday trading rationale — contains superseded staggered-chair content, see its own flags |
| 34 | [option-b-collection-centre.md](option-b-collection-centre.md) | Reference only — in-house accreditation path, rejected |

**Known gap, corrected 2026-08-08:** [operations-manual.md](operations-manual.md)'s scheduling section was rewritten 2026-07-30 to the (then-current) 12-client model — **it does not show the old 8-client model any more**, but it has also not been updated for the 2026-08-05 Table 1/Table 2 rebase, so it is now one rebase behind `docs/CURRENT-STATE.md` in turn. Use [scenario-c-sync-timetables.md](scenario-c-sync-timetables.md) (which does house the current Table 1/Table 2 tables) for the actual current timetable until [operations-manual.md](operations-manual.md) is brought current.

## PHASE 5: DAILY OPERATIONS

| # | Document | What it contains |
|---|---|---|
| 35 | [operations-manual.md](operations-manual.md) | Daily cadence, opening checklists — **scheduling section flagged stale, rest of document current** |
| 36 | [workflow.md](workflow.md) | Patient journey — **staffing table flagged stale (old subtenant model), rest of document current** |
| 37 | [grace-startup-plan.md](grace-startup-plan.md) | 90-day operations startup plan |
| 38 | [project-timeline-milestones.md](project-timeline-milestones.md) | Gantt-style relative-sequence milestone view, no calendar dates — new this session |

## PHASE 6: PEOPLE

| # | Document | What it contains |
|---|---|---|
| 39 | [team-startup.md](team-startup.md) | Empire agents + physical hires, ownership vs operational role split |
| 40 | [staff-plan.md](staff-plan.md) | Full staffing roster |
| 41 | [hr-framework.md](hr-framework.md) | Award obligations, Venue Manager critical-path hire section |
| 42 | [venue-manager-job-posting.md](venue-manager-job-posting.md) | Ready-to-use recruitment document — **not yet active, gated on securing a venue location** |
| 43 | [phlebotomist-job-posting.md](phlebotomist-job-posting.md) | Ready-to-use recruitment document — same gating rule applies |
| 44 | [onboarding.md](onboarding.md) | Staff and client onboarding procedures |

## PHASE 7: EQUIPMENT & SOURCING

| # | Document | What it contains |
|---|---|---|
| 45 | [equipment-costs.md](equipment-costs.md) | Complete equipment list by room/service area, capital vs recurring |
| 46 | [hire-purchase-china.md](hire-purchase-china.md) | China sourcing guide, TGA compliance |

## PHASE 8: PARTNERSHIPS & BOOKING

| # | Document | What it contains |
|---|---|---|
| 47 | [reed-partnerships.md](reed-partnerships.md) | Pathology partner outreach — live status tracker (WDP emailed, awaiting reply) |
| 48 | [pathology-partnership-brief.md](pathology-partnership-brief.md) | Pathology partnership model detail |
| 49 | [lab-partnership-email-draft.md](lab-partnership-email-draft.md) | The actual outreach email used — new this session |
| 50 | [cutoff-time-CORRECTION.md](cutoff-time-CORRECTION.md) | The still-unresolved WDP courier cutoff question |
| 51 | [referral-partnership-plan.md](referral-partnership-plan.md) | GP/OB/midwife referral strategy, named practices — new this session |
| 52 | [ivy-booking-system.md](ivy-booking-system.md) | Booking system spec (payment policy corrected this session) |

## PHASE 9: LOCATION

| # | Document | What it contains |
|---|---|---|
| 53 | [location-scouting.md](location-scouting.md) | Location search — **no venue secured yet, this is the current blocking gate** |
| 54 | [floor-plan-v3.svg](floor-plan-v3.svg) / [floor-plan-v3.pdf](floor-plan-v3.pdf) | **Current** floor plan concept |
| 55 | [floor-plan-concept.md](floor-plan-concept.md) | Text room schedule |

## PHASE 10: MARKETING & BRAND

| # | Document | What it contains |
|---|---|---|
| 56 | [poppy-marketing.md](poppy-marketing.md) | Instagram, referral network, launch strategy |
| 57 | [afternoon-marketing-plan.md](afternoon-marketing-plan.md) | Afternoon/standalone marketing |
| 58 | [brand-guide.md](brand-guide.md) | Brand standards — **"GTT Center Perth" is a placeholder name, not final, see banner in that document** |
| 59 | [website-spec.md](website-spec.md) | Website requirements (payment policy corrected this session) |

## PHASE 11: COMPLIANCE & LEGAL

| # | Document | What it contains |
|---|---|---|
| 60 | [patient-intake-form.md](patient-intake-form.md) | Patient intake form |
| 61 | [consent-form.md](consent-form.md) | GTT consent form (draft, solicitor review required) |
| 62 | [privacy-policy.md](privacy-policy.md) | Privacy policy (draft, solicitor review required) |
| 63 | [emergency-plan.md](emergency-plan.md) | Emergency procedures |
| 64 | [review-audit.md](review-audit.md) | Historical full business audit |
| 65 | [venture-timeline.md](venture-timeline.md) | Month-by-month phase plan — some illustrative calendar dates retained from an earlier draft, not committed |

## PHASE 12: THIS SESSION'S AUDIT TRAIL

| # | Document | What it contains |
|---|---|---|
| 66 | [00_document_inventory.md](00_document_inventory.md) | Every file, current status |
| 67 | [01_conflicts_log.md](01_conflicts_log.md) | Every conflict found, resolution status |
| 68 | [02_issues_and_risks.md](02_issues_and_risks.md) | Narrative gap analysis |
| 69 | [03_improvements.md](03_improvements.md) | Process improvement suggestions |
| 70 | [VERIFICATION-TRACKER.md](VERIFICATION-TRACKER.md) | Prioritised to-do list |
| 71 | [VERIFICATION-TRACKER.md](VERIFICATION-TRACKER.md) | Founder-only questions |

---

## REFERENCE ONLY / ARCHIVED (Not Required Reading)

| Document | Status |
|---|---|
| [agents.md](agents.md) | Empire agent roster reference |
| [inhouse-gtt-research.md](archive/inhouse-gtt-research.md) | ARCHIVED — in-house lab rejected |
| [research-supplement-day48-ARCHIVED.md](archive/research-supplement-day48-ARCHIVED.md) | ARCHIVED — merged into [research.md](research.md) v3.0 |
| [research-supplement-day48.md](archive/research-supplement-day48.md) | ARCHIVED — stale duplicate of the file above |
| [bloom-baby-case-study.md](archive/bloom-baby-case-study.md) | ARCHIVED — 3D scan removed from launch scope (future/Phase 2 only, see [market-research-findings.md](market-research-findings.md)) |
| [floor-plan-visual.html](archive/floor-plan-visual.html) / [floor-plan-visual.pdf](archive/floor-plan-visual.pdf) | SUPERSEDED — this is v2, use [floor-plan-v3.svg](floor-plan-v3.svg)/[.pdf](floor-plan-v3.pdf) instead |
| [capacity-pricing-audit.md](capacity-pricing-audit.md) | SUPERSEDED — its "12-client model" depended on a Draw-3 rule that was not carried forward. **Updated 2026-08-08:** the capacity ceiling it referenced has itself moved twice more since this row was last written (10 -> 14-proven-ceiling -> now 18-client Table 1 PRIMARY / 12-client Table 2 SECONDARY, per `docs/CURRENT-STATE.md` §1/§3) — do not quote any specific ceiling number from this row, see CURRENT-STATE.md for the live figures |
| [pm-staffing-roster.md](pm-staffing-roster.md) | Staffing structure decisions still valid; its own P&L figures are stale, see banner — use [profit-loss-tables.md](profit-loss-tables.md) v2.0 instead |
| [research.md](research.md) | **UNTOUCHED (per explicit scope instruction)** — comprehensive research doc, covers trust/ownership structure, authoritative source for market-sizing figures used elsewhere |
| [dva-tpi-research.md](dva-tpi-research.md) | **UNTOUCHED (per explicit scope instruction)** — Imara's personal TPI/DVA implications, out of scope for the operational rename |
| [investor-memorandum.md](investor-memorandum.md), [strategic-concerns-growth.md](strategic-concerns-growth.md), [multirole-CORRECTION.md](multirole-CORRECTION.md), [booking-service-capacity-rule.md](booking-service-capacity-rule.md), [scenario-d-demand-analysis.md](scenario-d-demand-analysis.md), [scenario-c-timeline.html](scenario-c-timeline.html) | Supporting reference documents, not required linear reading |

---

## OPEN DECISIONS REQUIRING ANTHONY'S INPUT

**See [VERIFICATION-TRACKER.md](VERIFICATION-TRACKER.md) for the complete, single-source, currently-maintained list.** Do not track founder-only questions here — that document is the single source of truth, per this repo's own convention (see [03_improvements.md](03_improvements.md) P5).

---

## Changelog

**2026-07-19** — Founder decision (confirmed 2026-07-18): reviewed for operational/on-site "Imara" references as part of the empire-wide Imara -> Venue Manager rename. Left the one strategic-decision reference unchanged (Imara's funding-partner role).

**2026-07-19 (audit pass)** — Flagged duplicate/superseded reference files.

**2026-07-19 (founder feedback round 3)** — Removed DVA from the Open Decisions table.

**2026-07-20 (full rebuild)** — This document was significantly out of date (still said "45 documents," listed the superseded 8-client Scenario B as current, retained a fixed "October 2026" launch date, and had no reference to any of this session's 12 new documents or conflict resolutions). Fully rebuilt as a genuine single-entry-point document per Anthony's request: a 60-second summary, a "what changed this session" section, a condensed reading order across 12 phases (down from the prior no-longer-accurate phase list), and explicit pointers to [00_document_inventory.md](00_document_inventory.md) (full file-by-file detail) and [01_conflicts_log.md](01_conflicts_log.md) (conflict resolution detail) rather than duplicating their content here. Removed the "Cross-Document Consistency Rule" linked-parameter table (it listed stale values matching the old model) — the same discipline is now better served by pointing to [profit-loss-tables.md](profit-loss-tables.md) v2.0 and [scenario-c-sync-timetables.md](scenario-c-sync-timetables.md) as single sources of truth rather than maintaining a parallel value-tracking table that itself goes stale.

**2026-07-20 (Imara overview added)** — Added `docs/gtt-center-perth-overview-for-imara.md` as the recommended presentation-ready document for a non-technical stakeholder, ahead of [executive-summary.md](executive-summary.md) in the core reading order.

**2026-07-20 (hyperlinks added)** — Converted every document name in this file to a clickable markdown relative hyperlink (e.g. `[business-plan.md](business-plan.md)`), so Anthony can click through directly on GitHub rather than needing to navigate manually.

**2026-07-20 (external resources + PM package exploration added)** — Added row 12a for [external-resources-and-advisors.md](external-resources-and-advisors.md) (Phase 1) and row 17a for [pm-package-exploration.md](pm-package-exploration.md) (Phase 2), both new documents this session.

**2026-07-20 (package renumbering)** — Updated the [services-pricing-locked.md](services-pricing-locked.md) row to reflect the renaming to Package 1 (A$250)/Package 2 (A$300) — same 2 price points as the prior "Package 2/3" naming. This completes the corpus-wide package-renumbering sweep across all live-referencing documents (see [services-pricing-locked.md](services-pricing-locked.md)'s own changelog for the full list).

**2026-07-20 (revenue extraction doc added)** — Added row 20a for [revenue-extraction-options.md](revenue-extraction-options.md), new this session.

**2026-07-20 (AM staffing-by-volume added)** — Added row 31a for [am-staffing-by-volume.md](am-staffing-by-volume.md), new this session. Updated row 31's description to note it also answers the specific 11th-client-at-09:55 question.

**2026-07-20 (PM packages committed)** — Updated row 17a: `pm-package-exploration.md` deleted and replaced by [pm-package-structure.md](pm-package-structure.md), reflecting Anthony's confirmation that PM packages are now a committed direction, not exploratory.

**2026-08-15 (reassessed reading path — the strategy/brand/venue/naming layer added, root cause of "flying blind" fixed)** — A dedicated execution audit found this file's "60-second version" still cited the pre-superannuation figures (+A$63,028.75/+A$27,084.69) and, more significantly, that neither this file nor `docs/00_document_inventory.md` referenced any of `docs/strategy/`, `docs/naming/`, `docs/experience/`, or `outputs/brand/` — a real, current, ~40-file layer built 2026-08-05 through 2026-08-15. Corrected the 60-second version's figures to the current canonical ones (+A$56,581.70/+A$21,056.64, RECALCULATED 2026-08-09 for superannuation). Added a new "ANTHONY'S READING PATH — REASSESSED 2026-08-15" section — a genuinely reassessed, 9-document smallest-useful-set covering the whole venture as it stands today, superseding the old "CORE STATUS DOCUMENTS" table as the first-read list (that table is retained below for its still-useful Phase 1-12 detailed index, now explicitly marked as secondary). No prose in the Phase 1-12 body was rewritten — only the entry points above it changed.

**2026-08-15/16 (External Execution Round outputs added)** — Added a new "For a document to actually hand a property agent..." pointer near the top, and a new "WHAT'S NEW — 2026-08-15/16 EXTERNAL EXECUTION ROUND" section listing all 5 new deliverables (landing page, venture overview pack, 3 outreach drafts, cost-reduction action table, AM->PM data-capture spec) with what Anthony can action immediately. All 5 are committed locally, not yet pushed.

**2026-08-08 (F-2 correction — this file's own "current model" references brought back in line with docs/CURRENT-STATE.md)** — `docs/architecture/REPOSITORY-AUDIT.md` (part of an architecture-only planning phase) found this file's headline "60-second version," its HANDOFF.md row, its `operations-manual.md` gap notes, and its `capacity-pricing-audit.md` reference row all still described the 2026-07-20 model (10 clients/day, +A$25,087/month) — two rebases behind `CURRENT-STATE.md`'s current figures (12-client rebase, 2026-07-30; Table 1/Table 2 18-/12-client rebase, 2026-08-05). This is the exact class of drift `CURRENT-STATE.md` was built to prevent at the figures layer, recurring one layer up in this navigation document. Corrected the specific stale claims listed above; did not rewrite the rest of this document's historical "what changed 2026-07-19 to 2026-07-20" narrative, which remains an accurate record of that specific session. **No decision was made here on the still-open Table 1 vs. Table 2 framing question (`VERIFICATION-TRACKER.md` item 1m)** — both are presented, PRIMARY/SECONDARY, matching `CURRENT-STATE.md`'s own current framing exactly, not resolved further.
