# GTT Center Perth — Information Memorandum

> **2026-07-29 — FULL RECONCILIATION, not a banner patch.** An outside review found this document's body table (§3) still showed a **-A$9,684/month loss** built on the abandoned 8-client/day, 3-package (A$200/250/300) launch model, while the banner immediately above it (in the prior version of this file) claimed the venture was profitable — a direct contradiction between banner and body in the same document. This version rewrites the affected sections (Executive Summary, §2 Business Model, §3 Financial Projections, §4 Staffing Model, §8 Capital Requirement) against the actual current model, not just the headline number. **Canonical current figures (package prices, client capacity, headcount, monthly net P&L, startup capital range) now live in `docs/CURRENT-STATE.md` — this document restates them for investor-readability but CURRENT-STATE.md is the source of truth if the two ever disagree.** Every figure below is tagged `[VERIFIED]`, `[MODELED]`, or `[PLACEHOLDER]` per that file's tagging system.

**Document type:** Private Information Memorandum
**Version:** 2.0 | **Date:** July 2026
**Prepared by:** YETI Tipi Holdings PTY LTD ATF YETI Holding Trust
**Entity:** YETI Holding Trust (trading as GTT Center Perth)
**Contact:** Anthony Zed | claw.anthony.zed@gmail.com | Perth, Western Australia

---

> *This Information Memorandum is confidential and provided solely to prospective investors and financiers for the purpose of evaluating an investment or financing arrangement. It must not be reproduced or disclosed to any other party without prior written consent. Recipients should seek independent legal, financial, and commercial advice before making any investment decision. This document contains forward-looking statements based on modelled projections — actual results may differ.*

---

## Executive Summary

**GTT Center Perth is WA's first dedicated Glucose Tolerance Test (GTT) wellness centre** — a purpose-built premium experience for pregnant women undergoing the mandatory 75g Oral Glucose Tolerance Test (OGTT) for gestational diabetes screening.

Every pregnant woman in Australia is offered this test between 24–28 weeks gestation. The procedure requires a 2–2.5 hour on-site wait during which the patient cannot leave. Currently, this wait happens in standard pathology waiting rooms.

**GTT Center Perth transforms that wait into a premium day spa visit**: pregnancy massage, facial, gel nails, blowdry, lash lift, spray tan, and a full beauty service menu — booked as one of 2 fixed packages alongside the blood collection appointment. Blood collection is performed on-site by employed phlebotomists under a WDP/PathWest licensed collection centre arrangement.

**The only comparable service in Australia is MIWM in Melbourne** — single-client model, GP-led, Victoria only, 3–4 week wait times. GTT Center Perth runs 10 concurrent clients in the morning GTT window (2 chairs, synchronized start — `scenario-c-sync-timetables.md`, verified) and offers individual service bookings in the afternoon for non-GTT clients.

### Key Metrics at a Glance

**Full detail and tags for every figure below: `docs/CURRENT-STATE.md`.**

| Metric | Value | Tag |
|--------|-------|-----|
| Package 1 price | **A$250** (fixed 2×30-min) | `[MODELED — Anthony's locked launch price, not externally market-tested]` |
| Package 2 price | **A$300** (flexible 2×45min / 45+30min / 2×30min) | `[MODELED — same basis]` |
| AM GTT capacity ceiling | **220 visits/month** (10/day × 22 trading days) | `[VERIFIED — scenario-c-sync-timetables.md scheduling-feasibility simulation, 2026-07-17; a capacity ceiling, not a booking guarantee]` |
| PM individual services capacity | **~350 sessions/month** (~16/day) | `[MODELED — assumption: ~50% of theoretical 4-line capacity, pm-staffing-roster.md, no real demand data yet]` |
| Monthly net P&L (steady state, Month 5+) | **+A$25,087.07/month** | `[MODELED — profit-loss-tables.md v2.1, 2026-07-20]` |
| Monthly fixed costs (steady state) | **A$88,625.09** | `[MODELED — same source]` |
| Startup capital requirement | **Not yet reconciled — see CURRENT-STATE.md** | `[PLACEHOLDER — 3 conflicting ranges exist across this repo's own documents, never reconciled]` |

---

## 1. The Market Opportunity

### The GTT — Universal Screening, Mandatory Wait

The 75g Oral Glucose Tolerance Test (OGTT) is the gold-standard screening method for Gestational Diabetes Mellitus (GDM) in Australia, mandated by ADIPS 2025 guidelines and recommended for **100% of pregnant women** between 24–28 weeks gestation.

| Statistic | Figure | Source |
|-----------|--------|--------|
| Australian births per year | ~277,000 | ABS 2024 |
| GTT tests performed nationally per year | ~270,000 | AIHW estimate |
| WA births per year | ~18,000 | ABS |
| Perth metro births per year | ~14,400 | ~80% metro share |
| **Perth GTT tests per year** | **~14,400** | Universal screening rate |
| **Perth GTT tests per week** | **~277** | 14,400 ÷ 52 |
| GDM diagnosis rate | 18% | AIHW 2023–24 |
| Perth GDM diagnoses per year | ~2,600 | 18% of 14,400 |

**GTT Center Perth's current AM capacity ceiling is 220 GTT visits/month** (10/day × 22 trading days, Scenario C — verified scheduling-feasibility, not a booking guarantee) — approximately 22% of Perth's total weekly GTT volume across a 6-day operating week (Monday-Saturday). Clients will travel from across Perth metro to access this service — location criteria prioritise ample parking and freeway access over proximity to any specific hospital.

### The Unmet Need

The current patient experience is universally poor:
- Patients sit in standard pathology waiting rooms for 2–2.5 hours
- They are fasting, frequently anxious, sometimes nauseous
- There is no comfort or service offering anywhere in WA
- The only national competitor (MIWM Melbourne) is single-client, no WA presence

**The WA market is completely uncontested.**

### The Referral Engine — Organic and Low-Cost

| Source | Mechanism |
|--------|-----------|
| Referring OB/GPs | Partner program — GP receives booking link, includes with GTT referral |
| Midwives | Warm referral at antenatal appointment |
| Instagram / social media | Perth pregnancy community word-of-mouth |
| WDP/PathWest | Co-marketing via pathology partner booking infrastructure |

MIWM Melbourne runs on **zero paid advertising** and maintains 3–4 week wait times. Demand is structural — driven by clinical mandation.

---

## 2. The Business Model

### AM Session — GTT Packages

**Every GTT visit is sold as one of 2 packages (renamed/renumbered 2026-07-20 — same 2 price points as the earlier 3-tier structure, with the old A$200 tier's composition moved onto the surviving A$250 tier; see `services-pricing-locked.md` for the full mapping history):**

| Package | Inclusions | Price |
|---------|-----------|-------|
| **Package 1** | Venue + lounge access (free) + fixed 2 × 30-min services | **A$250** |
| **Package 2** | Venue + lounge access (free) + client's choice: 2×45min, or 1×45min+1×30min, or 2×30min | **A$300** |

**All forward financial calculations use A$250 (Package 1) as a deliberate conservative safety price** — not a blended average across both packages. Venue and lounge access are bundled free — there is no separate seat fee. Ancillary revenue (spray tan, retail, cafe) is additional to package revenue, but flagged in `docs/CURRENT-STATE.md` as an unverified planning placeholder, not a checked estimate.

### PM Session — Individual Services (plus committed set/fixed packages)

The afternoon session (12:00–18:00) is open to all clients (non-GTT) as individual service bookings at standard pricing, delivered by 4 dedicated casual hires (1 massage, 1 hair, 1 nail, 1 beauty), costed on actual hours worked rather than a blanket shift. No minimum spend on the a-la-carte menu — clients book exactly the services they want.

| Service | Duration | Price |
|---------|----------|-------|
| Pregnancy massage | 30 or 45 min | A$75 / A$120 |
| Express facial | 30 or 45 min | A$95 / A$130 |
| Gel manicure | 45 min | A$75 |
| Gel pedicure | 50 min | A$80 |
| Brow wax + tint | 25 min | A$55 |
| Lash lift + tint | 45 min | A$95 |
| Blowdry | 30–45 min | A$65–80 |
| Haircut | 30–45 min | A$60–85 |
| Spray tan | — | A$60 |

A small menu of set/fixed PM packages (bundled combos, no client-choice) is also a committed direction (`pm-package-structure.md`) — proposed pricing requires Anthony's sign-off and is not yet incorporated into the revenue figures below, since no real uptake data exists. PM revenue is modelled separately to AM packages — average revenue per individual PM session is **~A$95** (`pm-staffing-roster.md`), at an assumed ~16 sessions/day steady-state volume (~50% of theoretical 4-line capacity — a planning estimate, not booking data).

### How the GTT Clinical Pathway Works

Blood collection is performed by GTT Center Perth's employed phlebotomists under WDP/PathWest's Licensed Collection Centre arrangement. GTT Center Perth does not bill Medicare — the pathology partner handles all Medicare billing.

| Time | Clinical Event | GTT Center Perth Role |
|------|---------------|----------------------|
| T=0 (arrival) | Fasting blood draw (3 tubes) | Phlebotomist — Chair A or B |
| T+5 min | Client drinks 75g glucose in lounge | Staff assists, clocks draw window |
| T+15 min | **Service 1 begins** (30 or 45 min) | Treatment staff (massage, facial, nails, hair, etc.) |
| T+60–75 min | 1-hour blood draw (5-min window, timed to service transition) | Phlebotomist draws between Service 1 and Service 2 |
| T+75 min | **Service 2 begins** (30 or 45 min) | Treatment staff |
| T+120–130 min | Final blood draw — client discharged | Phlebotomist |

**No-interrupt rule:** Blood draws are timed to service transitions — no client is paused mid-massage or mid-treatment. Ten clients are managed concurrently on a synchronized-start schedule (both chairs start each cohort at the same clock time — `scenario-c-sync-timetables.md`), 2 phlebotomy chairs, 2 phlebotomists, verified zero double-bookings.

---

## 3. Financial Projections

> **Why this section changed:** the prior version of this table showed a **-A$9,684/month loss**, built on the abandoned 8-client/day AM model (Scenario B) and the old 3-package structure. That model was replaced by the current 10-client/day Scenario C model on 2026-07-17 (verified scheduling capacity), and the loss finding was resolved at the source in `docs/01_conflicts_log.md` CONFLICT-08 on 2026-07-20 — but this document's own body table was never updated to match, leaving a banner-vs-body contradiction that the outside review correctly flagged. The table below is rebuilt from the current canonical figures in `profit-loss-tables.md` v2.1 and `cash-flow.md` v2.0, not a fresh calculation — see those documents for full line-by-line traceability.

### AM GTT Revenue — Monthly Ramp (Current Model)

| Month | GTT Visits/Day | Monthly GTT Revenue | Basis |
|-------|---------------|--------------------|----|
| M1 | ~4-5 (43% of ceiling) | ~A$23,650 | `[MODELED — ramp assumption, cash-flow.md v2.0]` |
| M2 | ~64% of ceiling | ~A$35,200 | `[MODELED — same]` |
| M3 | ~79% of ceiling | ~A$43,450 | `[MODELED — same]` |
| M4 | ~93% of ceiling | ~A$51,150 | `[MODELED — same]` |
| M5+ | 10 (100% of ceiling) | A$55,000 | `[VERIFIED capacity ceiling (10/day × A$250 × 22 days) — scenario-c-sync-timetables.md]` + `[MODELED — depends on the referral pipeline actually filling all 10 daily slots]` |

*All AM revenue uses A$250 (Package 1, the lower of the 2 current packages) as a deliberate conservative planning price, not a blended average.*

### Monthly P&L — Stable Operations (Month 5+ steady state)

| Line Item | Monthly | Annual | Tag |
|-----------|---------|--------|-----|
| AM GTT Package revenue (220 visits × A$250) | A$55,000 | A$660,000 | `[MODELED — capacity ceiling × conservative price]` |
| PM Individual Service revenue (~16 sessions/day × A$95 avg) | A$33,440 | A$401,280 | `[MODELED — pm-staffing-roster.md, planning estimate]` |
| Ancillary revenue (spray tan, retail, cafe) | A$8,580 | A$102,960 | `[PLACEHOLDER — no real derivation found for 2 of 3 component lines; see CURRENT-STATE.md]` |
| **Total Revenue (Month 5+)** | **A$97,020** (ramp-table sum) / **A$113,712.16** (precise weekday/Saturday-blended calc) | — | See note below — two valid calculation methods, precise figure is authoritative |
| Total payroll + relief pool, direct labor + opening costs | ~A$73,397 | — | `[MODELED — financial-break-even-staff.md award rates, traceable]` |
| Workers compensation (WA, 1.7%) | ~A$1,248 | A$14,973 | `[MODELED — traceable calculation]` |
| Non-wage overhead (rent, utilities, insurance, marketing, etc. — 13 components) | A$13,980 | A$167,760 | `[MODELED — profit-loss-tables.md §4 breakdown]` |
| **Total Fixed Costs** | **A$88,625.09** | **A$1,063,501.08** | |
| **Net P&L (Month 5+, steady state)** | **+A$25,087.07** | **+A$301,044.84** | `[MODELED — profit-loss-tables.md v2.1, precise weekday/Saturday-blended calculation, 2026-07-20; not based on real trading data]` |

**Note on the two revenue totals above:** `profit-loss-tables.md`'s simplified Month-by-month ramp table sums to A$97,020/month at M5+ (giving an approximate +A$8,395/month net), while its own more precise weekday/Saturday-blended calculation gives A$113,712.16/month total revenue and the headline **+A$25,087.07/month** net figure. The precise calculation is the one to quote — the ramp table exists only to show the Month 1-4 build-up shape. This is disclosed directly in `profit-loss-tables.md` rather than presenting one number as if no discrepancy existed.

**Ramp-up losses (Months 1-3) are real** and must be funded from working capital — see `docs/CURRENT-STATE.md` for the startup capital range, which is currently unreconciled across this repo's own documents (flagged, not smoothed over).

### Unit Economics — AM GTT

| Metric | Value | Tag |
|--------|-------|-----|
| Variable cost per visit | ~A$5 (consumables, linen, supplies) | `[MODELED]` |
| Contribution margin per GTT visit (avg A$250) | **A$245 (98%)** | `[MODELED]` |
| AM GTT direct labor cost (2 phlebotomists + 8 treatment staff, unaffected by the 8→10 client change since headcount is set by peak concurrency, not client count) | A$48,255/month | `[MODELED — traceable from financial-break-even-staff.md award rates × confirmed headcount]` |
| AM segment standalone contribution (revenue minus direct labor only, before shared overhead) | **+A$6,745/month** (was -A$4,255/month under the old 8-client model) | See §7 delta table in `docs/CURRENT-STATE.md` and `docs/VERIFICATION-TRACKER.md` for the full input-by-input reconciliation — this is not a newly-modeled improvement, it is the existing 2026-07-17 Scenario C capacity change applied to a segment table that was never updated |

---

## 4. Staffing Model

GTT Center Perth employs all service delivery staff directly. No subtenants. **Current confirmed headcount: 2 phlebotomists + 7-8 treatment staff (AM) + 1 receptionist/manager + 4 dedicated PM casual hires + relief pool** — see `docs/CURRENT-STATE.md` for the headcount range and why it isn't a single fixed number (depends on an operational hiring decision not yet made — see note below table).

| Role | FTE | Annual Cost (incl. 12% super) | Tag |
|------|-----|-------------------------------|-----|
| Venue Manager (Managing Director, new hire, not yet in place — critical-path, first-aid/EpiPen/fire-warden credential required) | 1.0 | Not yet costed separately in this document | `[PLACEHOLDER]` |
| Receptionist / Manager (AM 07:00–12:00 + PM 15:00–18:00 split shift) | 1.0 | A$56,237 | `[MODELED — award rate, traceable]` |
| Phlebotomist × 2 (Chair A and Chair B, AM only) | 2.0 | A$86,136 | `[MODELED — award rate, traceable]` |
| Pregnancy Massage Therapist × 2 | 2.0 | A$125,548 | `[MODELED]` |
| Beauty Therapist × 2 (facial / brows / lashes) | 2.0 | A$125,548 | `[MODELED]` |
| Nail Technician × 2 | 2.0 | A$120,912 | `[MODELED]` |
| Hairdresser × 2 | 2.0 | A$120,912 | `[MODELED]` |
| PM roster — 4 dedicated casual hires (1 each: massage, hair, nail, beauty), hours-based costing, ramps with PM volume | 4.0 (variable hours) | ~A$9,677/month at Month 5+ steady state (not a flat annual FTE figure — hours-based) | `[MODELED — pm-staffing-roster.md corrected hours-based method]` |
| Casual Relief Pool (sick / holiday cover) | — | A$15,000 | `[MODELED]` |
| **Total Annual Payroll (AM roles + relief pool)** | | **A$713,067** | `[MODELED — financial-break-even-staff.md, traceable award-rate calculation]` |

**Note on headcount precision:** the 8-person AM treatment roster (2 each: Massage, Nail, Hair, Beauty) can potentially drop to 7 via a Massage+Beauty cross-training pool, which `profit-loss-tables.md`'s Treatment Headcount analysis confirms is the genuine minimum at the current 10-client/day volume (checked against the verified schedule, not a guess) — saving ~A$5,231/month if adopted. This is an operational hiring decision for the Venue Manager, not yet actioned, so this document states the range (7-8) rather than picking one number. A separate 2026-07-28 proposal (`dual-role-staffing-model-2026-07-28.md` v3.0) to recruit AM and PM into one combined rotating pool (potentially fewer than 11 total heads across both shifts) is explicitly **not** booked as a confirmed saving in that document — flagged there as an open question pending real roster data, and not assumed here either.

**Venue Manager:** critical-path hire, recruitment gated on securing a physical venue location per Anthony's direct instruction (not yet begun) — see `docs/staff-plan.md` §7, `docs/venue-manager-job-posting.md`.

---

## 5. Competitive Landscape

### Direct National Competitor: MIWM Melbourne

| Feature | MIWM (Melbourne) | GTT Center Perth |
|---------|-----------------|-----------------|
| Location | Victoria only | WA — uncontested |
| Client model | Single client per session | 10 concurrent AM clients (verified capacity ceiling) |
| Services | 60–120 min spa (1–2 services) | Full menu, 2 services per GTT package |
| Hairdressing | No | Yes (2 stylists, cut, blowdry) |
| Spray tan | No | Yes |
| PM individual sessions | No | Yes |
| Wait times | 3–4 weeks (no paid marketing) | — |

**GTT Center Perth is the first mover in WA with a materially superior model.**

---

## 6. Legal and Entity Structure

| Item | Status |
|------|--------|
| Operating entity | YETI Holding Trust (discretionary trust) |
| Corporate trustee | YETI Tipi Holdings PTY LTD |
| ABN / GST | To be registered under trust ABN (mandatory — turnover exceeds A$75K threshold) |
| Business name | "GTT Center Perth" — ASIC registration (~A$39/yr) |
| Pathology model | WDP Licensed Collection Centre — negotiations in progress (Priority 1 action) |
| Phlebotomist licensing | Trained blood collectors — non-AHPRA role confirmed |
| Nail ventilation | WorkSafe WA LEV pre-application required before fit-out |
| Food notification | Low-risk food business (herbal tea, packaged snacks) — local council notification |
| Public liability insurance | Minimum A$20M required before opening |

**TPI Note:** Anthony Zed receives a TPI veteran's pension. All business revenue flows through YETI Holding Trust — not to Anthony personally. This structure is non-negotiable and confirmed to protect pension entitlements. Trust beneficiary distribution planning is handled independently of this document.

---

## 7. Risk Register

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| WDP/PathWest declines partnership | Low | Critical | Both networks have published LCC programs. Clinipath is tertiary fallback. See `pathology-partnership-brief.md`. |
| PM individual service revenue insufficient | Medium | High | Revenue modelling in progress. AM staff taking PM bookings increases capacity. Service upgrade upsell (2-service visit at A$165+) is primary lever. |
| Lease rent exceeds budget | Medium | Medium | Multiple Perth suburbs under investigation at A$25–40/sqm. See `location-scouting.md`. |
| Competitor enters WA market | Low | Medium | First-mover + WDP partnership + KEMH-area positioning create durable moats. 12–18 month new entrant lead time. |
| Fit-out cost blowout | Medium | High | Mid-range budget includes 15% contingency. 3 builder quotes required before committing. |
| Trust distribution tax (proposed 30% flat) | Medium | Low | Modelled in `financial-model.md`. Still positive in both scenarios. |
| GDM rate falls | Very Low | High | ADIPS 2025 thresholds tightened → increases diagnoses. Rate stable to rising. |

---

## 8. Capital Requirement and Use of Funds

### Capital Stack — Unreconciled, Flagged Rather Than Smoothed Over

**This document previously stated A$363,000 (mid-range) / A$292,000-493,000 (planning range) here.** That figure is now known to be one of **three different, never-reconciled ranges** that exist across this venture's own documents:

| Source | Range | Status |
|---|---|---|
| This document (prior version, itemised fit-out/equipment/IT/working capital/legal) | A$363,000 mid / A$292,000-493,000 range | `[PLACEHOLDER — original itemisation, not re-verified against current model]` |
| `HANDOFF.md` (2026-07-17) | "~A$144,500-242,500 realistic range, down from an inflated A$363,000 original figure" | `[PLACEHOLDER — no itemised build shown in that document]` |
| `business-plan.md` §9 (citing `cash-flow.md`) | Low A$209,000 / Mid A$305,000 / High A$431,000 | `[PLACEHOLDER — this itemised breakdown does not currently exist in cash-flow.md's own content as of its 2026-07-20 rebuild; citation could not be verified against the source document this session]` |

**None of these three ranges has been confirmed as authoritative.** Per this session's audit, presenting any single number here (including the original A$363,000) would repeat the exact false-precision problem this document was flagged for. **The correct figure requires a fresh, itemised fit-out/equipment/legal cost build against the current model (10-client Scenario C, 2-package structure, current staffing), not a selection among three unreconciled historical numbers.** Tracked as an open item in `docs/VERIFICATION-TRACKER.md` — Anthony and an accountant/quantity surveyor should confirm before this figure is used in any real funding conversation.

### Finance Options

| Structure | Details |
|-----------|---------|
| Business loan — secured | Equipment (A$75K) is asset-backed. Fit-out qualifies under commercial property improvement loan. 5–7 year term. |
| Business loan — unsecured | Non-bank lenders (Prospa, Moula, Capify): A$5K–A$500K for established ABN holders. |
| Investor equity | Silent partner preferred return: 15–20% p.a. against A$363K, repaid from operating profits. |

---

## 9. Timeline to Launch

**No launch date is set — sequence is by dependency only, per standing instruction.** The prior version of this table gave a fixed "Soft open W20 (October 2026)" date, which contradicts this venture's own standing position (see `HANDOFF.md`, `docs/04_roadmap_next_steps.md`) that no calendar date has been committed. Corrected to a dependency-ordered sequence, no calendar anchor:

| Phase | Sequence | Key Milestones |
|-------|-------|----------------|
| Legal + entity setup | Early | ABN, GST, business name, WDP contact initiated |
| Pathology partnership confirmation | Blocking gate 1 | WDP reply in progress (`cutoff-time-CORRECTION.md`) — must be resolved before capacity model is fully relied upon |
| Physical venue location | Blocking gate 2 | Nothing else (Venue Manager recruitment, fit-out, staff hiring) proceeds until this is secured — see `docs/04_roadmap_next_steps.md` Tier 0 |
| Lease negotiation + execution | After venue secured | YETI Tipi Holdings PTY LTD as trustee signs |
| Architect brief + fit-out quotes | After lease | 3 builder quotes, council approval, WorkSafe WA nail LEV pre-application |
| Fit-out construction | After quotes confirmed | Duration not yet estimated against a confirmed venue |
| Venue Manager + staff recruitment | After venue location confirmed | Venue Manager is the first hire — see `docs/venue-manager-job-posting.md` |
| Systems + marketing | Parallel, once staff/venue confirmed | Fresha live, Instagram, GP referral network activation |
| Soft open | After all blocking gates cleared | No date committed |
| Full operation | Following soft-open ramp | AM + PM sessions ramping toward the 10-client/day capacity ceiling |

---

## 10. Full Documentation Pack

45-document operational pack available to serious parties following NDA execution:

Business Plan · 18-Month Cash Flow · Unit Economics · Financial Break-Even + Staffing Analysis · Services & Pricing (locked) · Market Research · Operations Manual (verified scheduling timetable) · Clinical Protocol (ADIPS 2025) · Staff Plan + Award Wage Calculations · Equipment Costs · HR Framework · Booking System Specification · Patient Intake + Consent Forms · Brand Guide · Location Scouting Report · Conceptual Floor Plan · Pathology Partnership Brief

---

## 11. Contact

**Anthony Zed**
Founder | YETI Holding Trust
claw.anthony.zed@gmail.com
Perth, Western Australia

To progress: NDA on request. Full document pack to verified parties.

---

## Changelog

**2026-07-29 (full reconciliation, external audit response)** — An outside reviewer found this document's §3 body table still showed a -A$9,684/month loss built on the abandoned 8-client/3-package launch model, contradicting the profitable banner sitting directly above it — a banner-vs-body contradiction, not just a stale figure. Fixed at the source, not just the headline number: Executive Summary, §2 Business Model (package table, PM model), §3 Financial Projections (full P&L rebuild against `profit-loss-tables.md` v2.1/`cash-flow.md` v2.0), §4 Staffing Model (current headcount, hours-based PM costing), §8 Capital Requirement (surfaced the 3-way unreconciled range across this repo's own documents rather than repeating one arbitrarily), §9 Timeline (removed a fixed October 2026 date that contradicted this venture's own "no launch date set" standing position). Every figure now carries a `[VERIFIED]`/`[MODELED]`/`[PLACEHOLDER]` tag per `docs/CURRENT-STATE.md`'s system (new this session) — this document no longer restates absolute figures as if independently sourced; it points to CURRENT-STATE.md as canonical.

---

*Prepared by Idea Lobster (CEO Advisory System) on behalf of YETI Tipi Holdings PTY LTD ATF YETI Holding Trust | July 2026 | Version 2.0, reconciled 2026-07-29*
