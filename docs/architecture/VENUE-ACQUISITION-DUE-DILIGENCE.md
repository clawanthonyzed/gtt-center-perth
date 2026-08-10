# Venue Acquisition & Commercial Due Diligence Phase

**Phase:** Venue Acquisition & Commercial Due Diligence — frameworks and templates only. No venue is selected or scored in this document. No financial assumption, canonical figure, or the financial model itself is changed. This phase converts the validated business model into a venue-ready decision package: tools Anthony can use, not decisions made on his behalf.

**Date:** 2026-08-10
**Version used as source of truth:** commit `829c3a9` (Commercial Validation Framework) and everything it built on.

**Source documents used:** `docs/floor-plan-concept.md`, `docs/location-scouting.md`, `docs/property-links-2026-07-28.md`, `docs/rent-budget-2026-07-28.md`, `docs/standards-floorplan-crosscheck-2026-07-28.md`, `docs/industry-standards-reference-2026-07-28.md`, `docs/CURRENT-STATE.md` §6/§7, `docs/architecture/COMMERCIAL-VALIDATION-FRAMEWORK.md`, `outputs/GTT-Center-Perth-Financial-Model.xlsx`/`*.docx`/`*.pdf`, `docs/wdp-reply-carole-2026-07-30.md`, `docs/cutoff-time-CORRECTION.md`, `docs/lab-outreach-2026-07-28.md`, `docs/reed-partnerships.md`, `docs/VERIFICATION-TRACKER.md`.

---

## 1. Venue Evaluation Framework

A weighted scoring system for evaluating potential venue candidates, once found. **No candidate is scored in this document** — the two live property leads referenced below (6/325 Harborne Street, and the wider `property-links-2026-07-28.md` search) are used only to calibrate what "real data looks like" for each criterion, not as venue selections.

### 1.1 Scoring Criteria and Weights

| Criterion | Weight | Grounded in |
|---|---|---|
| Rent affordability | 20% | `rent-budget-2026-07-28.md`'s established A$96,000/yr true-occupancy-cost budget (rent + outgoings + GST) |
| Parking | 20% | `location-scouting.md`'s own non-negotiable rule: minimum 8–10 dedicated off-street spaces, checked FIRST, before anything else |
| Room suitability / size fit | 20% | `floor-plan-concept.md`'s room schedule — day-one footprint ~239sqm (what the current financial model's construction cost is based on), recommended search target ~249–262sqm including growth-reservation space (see §1.3 below) |
| Pathology/WDP requirements | 15% | `location-scouting.md`'s explicit blocking rule: "WDP collection room spec must be obtained BEFORE signing any lease"; WA Skin Penetration Code / NPAAC findings below |
| Fit-out complexity | 15% | `STARTUP-COST-RECONCILIATION.md` §4's own finding that construction cost is "inherently provisional without a real tenancy" — an existing compatible fit-out (e.g. a former medical/health tenancy) is a real, material cost lever |
| Opening timeline | 10% | `grace-startup-plan.md`'s FINANCIAL GATES/week-based sequencing — a venue requiring less remediation reaches Week 19–20 (first revenue) sooner |

**These weights are a starting proposal, not a settled decision.** Anthony should adjust them before first real use — they are grounded in what this repo already treats as non-negotiable (parking, WDP room spec) versus adjustable (rent, size), but the specific percentages are this framework's own proposal, not sourced to an existing document.

### 1.2 Scoring Rubric (1–5 per criterion, weighted sum = venue score out of 5)

| Score | Rent affordability | Parking | Room suitability | Pathology/WDP fit | Fit-out complexity | Opening timeline |
|---|---|---|---|---|---|---|
| **5** | True occupancy cost well under A$96,000/yr, meaningful buffer | 10+ dedicated spaces, well-lit, pram-accessible | ≥262sqm (day-one + full growth reservation), open-plan-friendly shape | Existing medical/pathology-compliant fitout or explicit WDP sign-off already obtained | Former health/medical/beauty tenancy, plumbing/HVAC already present | Lease-ready now, minimal fit-out, could realistically open in <12 weeks |
| **4** | At or modestly under A$96,000/yr | 8–9 dedicated spaces | 249–261sqm (day-one + partial growth reservation) | Existing plumbed wet areas, WDP spec not yet confirmed but no known blocker | Existing HVAC or plumbing (not both) | 12–16 weeks to open |
| **3** | Within ~10% over A$96,000/yr, would need offset elsewhere | 6–7 dedicated spaces, or free public parking within 50m | 239–248sqm (day-one fit only, no growth-reservation room) | Raw shell, no plumbing precedent, but shape appears WDP-compatible on paper | Raw shell, standard commercial services present (3-phase power, base plumbing) | 17–20 weeks to open (matches `grace-startup-plan.md`'s own baseline schedule) |
| **2** | 10–25% over budget | 3–5 dedicated spaces | 150–238sqm (below day-one target, real layout compromise needed) | Layout shape questionable for a 2-chair collection room + adjacent wet areas | Raw shell, missing 3-phase power or requiring significant services upgrade | >20 weeks, or timeline genuinely unclear |
| **1** | >25% over budget | <3 dedicated spaces or street-parking-only | <150sqm (below the stated floor) or unworkable shape | No plumbed wet area anywhere in the tenancy, or upper floor (excludes ground-floor requirement entirely) | Requires structural work, disputed planning-zone use class | Timeline blocked by an unresolved planning-zone or landlord issue |

### 1.3 Calibration Notes (not scoring examples — inputs used to build the rubric)

- **Rent budget:** A$8,000/month = A$96,000/year, sourced to `profit-loss-tables.md`'s Non-Wage Overhead line — the working comparison figure for "true occupancy cost," not a bare headline rent number. `property-links-2026-07-28.md`'s own worked example (45 Stirling Highway, Nedlands, 150sqm tenancy) shows the calculation method: (net rent $/sqm/yr + outgoings $/sqm/yr) × sqm + car-bay fees, before GST — a real worked calculation already exists in this repo to reuse, not invent.
- **Size target — two figures, not one, and the distinction matters:**
  - **~239sqm (day-one only)** is what `CURRENT-STATE.md` §7.2's construction-cost estimate is actually built against — this is the figure the current financial model uses.
  - **~249–262sqm (day-one + growth reservation)** is `property-links-2026-07-28.md`'s own recommended search target, reflecting Anthony's instruction to reserve (not staff or cost) one extra station per service type. `floor-plan-concept.md`'s own most recent recalculation (after fixture-count corrections) states this combined figure as ~262sqm, up from an earlier ~249sqm pass — both figures are shown in that document's own changelog, neither superseded silently. A venue below ~239sqm is a real compromise against the current committed model; a venue between ~239 and ~262sqm fits day-one operations but with a tighter or absent growth margin.
- **Parking:** `location-scouting.md`'s own words: "do NOT view any property without first confirming parking count." One candidate already found in this repo's own search (Suite 6, 1 Alvan Street, Mount Lawley — 2 exclusive bays) was explicitly flagged as a likely disqualifier for exactly this reason, despite otherwise-attractive rent — a real, already-applied example of this criterion in action.
- **Pathology/WDP requirements:** the WA Skin Penetration Code (via `standards-floorplan-crosscheck-2026-07-28.md`) does NOT govern the Blood Collection Room — Anthony's own 2026-07-29 decision places that room under NPAAC/WDP's own Licensed Collection Centre spec instead, which remains unobtained. The Code DOES apply (2-sink/hands-free-tap requirement) to the Nail Station Area and Facial/Beauty Rooms specifically, not to Massage Rooms or the Hairdressing Area, which only need standard hygiene sinks. A venue's existing wet-area count and layout should be checked against this room-by-room breakdown, not a blanket "how many sinks" question.
- **Fit-out complexity:** `53 Hardy Road, Nedlands` (an unverified candidate already found in `property-links-2026-07-28.md`) is flagged in that document as "the closest match to GTT's actual layout need found so far" precisely because it is an existing medical/consulting fitout with 4 consulting rooms and a real reception — a concrete illustration of what a high fit-out-complexity score (favourable) looks like in practice, without this framework scoring or selecting that candidate.
- **Opening timeline:** `grace-startup-plan.md`'s FINANCIAL GATES table gives the baseline sequencing (lease Week 9–10, fit-out complete Week 16, soft launch Week 19) — a venue that shortens any of these stages (e.g. an existing compatible fitout skipping most of Weeks 11–13) directly compresses time-to-first-revenue.

---

## 2. Venue Data Capture Template

Directly usable — Anthony fills this out per property under consideration. One copy per candidate.

```
VENUE DATA CAPTURE — [Property Address]
Date captured: __________  Captured by: __________  Agent/contact: __________

## LEASE TERMS
- Lease length offered: __________ (target: 3 years initial + 3-year option, per location-scouting.md)
- Rent review mechanism: [ ] Fixed CPI  [ ] Market review  [ ] Other: __________
- Rent-free / incentive period offered: __________ (target: 3-6 months during fit-out)
- Personal guarantee required: [ ] None  [ ] Capped at __________  [ ] Open-ended
- Entity to sign: YETI Tipi Holdings PTY LTD as trustee for YETI Holding Trust

## RENT & OUTGOINGS
- Face rent: $__________ /sqm/yr  OR  $__________ /month flat
- Outgoings: [ ] Included in face rent  [ ] Additional, $__________ /sqm/yr or $__________ flat
- GST treatment: [ ] Rent is GST-exclusive (10% added)  [ ] GST-inclusive  [ ] Unclear — ask agent
- Car bay fees (if separate from rent): $__________ /bay/month × __________ bays
- TOTAL TRUE OCCUPANCY COST (rent + outgoings + car bays, before GST): $__________ /yr
  → Compare against the A$96,000/yr budget (per rent-budget-2026-07-28.md)

## BOND / DEPOSIT
- Bond amount: $__________ (target: capped at reasonable multiple of monthly rent)
- Deposit due date/stage: __________

## SIZE & LAYOUT
- Usable floor area: __________ sqm (target: ~239sqm day-one minimum, ~249-262sqm preferred for growth reservation — see §1.3)
- Ground floor: [ ] Yes  [ ] No (excludes automatically if No)
- Existing plumbed wet areas: __________ count, locations: __________
- Existing HVAC: [ ] Yes  [ ] No
- 3-phase power confirmed: [ ] Yes  [ ] No  [ ] Unconfirmed
- Prior tenancy use: __________ (flag if former health/medical/beauty — real fit-out cost saving)
- Loading/delivery access for fit-out: [ ] Yes  [ ] No

## PARKING
- Dedicated off-street spaces: __________ (minimum required: 8-10, per location-scouting.md)
- Free public parking within 50m, if dedicated spaces insufficient: __________ spaces
- Well-lit for 7:30am winter arrivals: [ ] Yes  [ ] No
- Additional staff parking (3-5 spaces needed): [ ] Available  [ ] Not available

## COMPLIANCE / FIT-OUT REQUIREMENTS
- Planning zone confirmed for health/beauty use: [ ] Yes  [ ] No  [ ] Pending council confirmation
- Women's accessible WC on-premises: [ ] Yes  [ ] No, needs adding
- WDP collection-room spec obtained and checked against this floor plate: [ ] Yes  [ ] No — MUST be done BEFORE lease signing
- WA Skin Penetration Code 2-sink requirement checked (Nail/Facial-Beauty rooms only): [ ] Yes  [ ] No
- Landlord's building insurance / certificate-of-currency requirements noted: __________

## TIMELINE
- Earliest lease commencement date: __________
- Estimated fit-out duration from lease start: __________ weeks
- Estimated date to soft launch: __________ (compare against grace-startup-plan.md's Week 19-20 baseline)

## AGENT / LISTING DETAILS
- Listing URL: __________
- Agent name(s) and phone: __________
- Verification status: [ ] VERIFIED (URL + price + availability all confirmed directly)  [ ] UNVERIFIED CANDIDATE
  (per property-links-2026-07-28.md's own terminology standard — do not call it "verified" without all three)

## NOTES / FLAGS
__________________________________________________________________
```

---

## 3. Landlord Negotiation Package Framework

Identifies the documents required to present a credible tenancy proposal to a landlord — framework only, no package is assembled in this phase.

### 3.1 Required Documents

| Document | Purpose | Current status | Source to build from |
|---|---|---|---|
| Business overview | Explains what GTT Center Perth is and its intended use of the premises | Not yet assembled as a landlord-facing document — `business-plan.md` exists but is written for internal/founder use | `business-plan.md`, `docs/gtt-center-perth-overview-for-imara.md` (already a simplified overview format, could be adapted) |
| Financial summary | Demonstrates the venture's revenue/profitability model and ability to sustain the tenancy | `outputs/GTT-Center-Perth-Financial-Model.xlsx`, `*.docx`, `*.pdf` already exist and are professionally formatted — but were built for internal/founder decision-making, with governance-status tags (CANONICAL/MODELLED/BOUNDED) and internal jargon not appropriate for a landlord audience as-is | The 3 Document Generation Phase deliverables — would need a landlord-appropriate extract/re-packaging, not a rebuild, per `COMMERCIAL-VALIDATION-FRAMEWORK.md` §4.3's own finding |
| Proof-of-funds presentation | Demonstrates financial capacity to pay rent for the lease term | **Does not exist anywhere in this repo** — `COMMERCIAL-VALIDATION-FRAMEWORK.md` §4.3 already identified this as the primary concrete gap for landlord readiness | Would need a bank statement/financial-capacity letter, likely from Anthony's own accountant once engaged (`financial-setup.md` STEP 1) |
| Insurance requirements evidence | Landlords typically require public liability cover confirmed before lease signing | **Not yet obtained** — insurance is not purchased pre-lease under the current sequencing (`financial-setup.md` STEP 8, Week 10); item 19 in `VERIFICATION-TRACKER.md` remains open | 3 broker quotes (per the External Validation Requirements Register, `COMMERCIAL-VALIDATION-FRAMEWORK.md` §2) — a certificate of currency is the actual document a landlord will want to see |
| Proposed tenancy use statement | Confirms the specific use class being sought, for the landlord's own planning-zone/insurance checks | Implicit in the business overview but not a standalone document | Should state: health/beauty services use class, hours of operation (Monday–Saturday, AM/PM sessions), expected foot traffic pattern, no overnight occupancy |

### 3.2 What Still Needs Closing (from the Commercial Validation Framework)

`COMMERCIAL-VALIDATION-FRAMEWORK.md` §4.3 already assessed landlord-negotiation readiness as "the closest of the three [bank/investor/landlord] to being ready," with exactly two concrete gaps:

1. **Proof-of-funds document** — does not exist in this repo in any form; likely the simplest of the two to produce once the venue search narrows enough to justify the effort (accountant/bank-provided, not something this repo's tooling can generate).
2. **Public liability insurance** — unconfirmed; `financial-setup.md` STEP 8 itself states this is required "before lease signing" for many landlords, and a certificate of currency is the concrete artefact needed.

**Everything else** (business overview, financial summary source material) already exists in a usable-but-not-landlord-packaged form — the gap there is presentation/audience adaptation, not missing content.

### 3.3 Sequencing Note

Per `financial-setup.md`'s own week numbering, insurance (STEP 8) is scheduled for Week 10, after lease signing (Week 9–10) — but many landlords want a certificate of currency BEFORE signing, per that same document's own note. This is a genuine internal sequencing tension worth flagging, not resolving here: either insurance needs to be obtained earlier than currently scheduled, or the specific landlord's own requirement needs to be confirmed as flexible on this point (see the Venue Data Capture Template §"Compliance/Fit-Out Requirements" field for capturing this per-property).

---

## 4. WDP Commercial Validation Checklist

Built directly on the existing correspondence history — not starting from scratch. What follows is a precise map of what has already been asked and answered, what has been asked but not yet answered, and what has never been asked at all.

### 4.1 Already Asked AND Answered

| Question | Answer | Source |
|---|---|---|
| Is courier/GTT specimen collection feasible at all? | Yes, feasible with the correct specimen tubes | `lab-outreach-2026-07-28.md` |
| What is the specimen dispatch cutoff time? | No single fixed cutoff — overnight storage viable "in some circumstances" (fluoride-oxalate tubes stable ~24hrs); "a late booking would not necessarily prevent collection, although specimen type and storage requirements would always need to be considered" | `cutoff-time-CORRECTION.md`, `[VERIFIED — Carole Rivers, WDP, email, 2026-07-30]` |
| What is WDP's guidance on GTT start time? | "Would not normally commence a GTT after 10:30am" (exceptions exist, e.g. shift workers) | `VERIFICATION-TRACKER.md` item 1b, `king-edward-start-time-constraint.md` |
| Does the collector ever perform wellness/general-venue duties? | Settled by Anthony's own decision: collector staff never take on wellness or general-venue duties, regardless of employment model | `VERIFICATION-TRACKER.md` item 1j |
| Would a doctors-on-site requirement affect site approval? | No — Carole confirmed directly: "the absence of doctors on site would not present an operational concern" | `VERIFICATION-TRACKER.md` item 1c |

### 4.2 Already Asked, Not Yet Answered (Anthony's 2026-07-31 sent reply — awaiting Carole's response)

| Question asked | Why it matters | Status |
|---|---|---|
| What would a WDP-supplied staffing/rental arrangement cost commercially (even an indicative range)? | Directly determines whether AM Direct Labor stays in-house (~A$48,255/month) or shifts to a rental fee — compare against the already-computed A$104,800–106,600/yr in-house break-even threshold | AWAITING REPLY |
| Should we expect a consistent collector most days, or is rotation likely? | Affects continuity of care/client experience, and potentially onboarding/training overhead if the collector rotates | AWAITING REPLY |
| Does daily, Monday–Saturday volume put GTT under the standard collection-centre placement model, or the "occasional dates" structure Carole mentioned? | Different structures likely carry different commercial terms | AWAITING REPLY |
| What does "under observation" require during the 2-hour wait once a client has moved to a wellness room — a check-in point, or does responsibility shift once the client leaves the collector's area? | Directly affects the operational schedule/staffing model for the wait period, and clarifies WDP's liability position during that window | AWAITING REPLY (narrower framing of the sightline/observation sub-question flagged in `VERIFICATION-TRACKER.md` item 1j) |

### 4.3 Not Yet Asked At All — Genuine Gaps

| Missing question | Why it's needed | Priority |
|---|---|---|
| WDP's exact collection-room dimensions and plumbing spec | `location-scouting.md`'s own explicit rule: must be obtained BEFORE signing any lease. Not yet requested in any correspondence reviewed | HIGH — blocks venue confirmation directly |
| Whether WDP requires exclusivity, or GTT Center Perth could operate WDP alongside a fallback pathology partner (PathWest/Clinipath) | Affects contract flexibility and whether the still-open PathWest/Clinipath outreach thread (item 4) remains relevant once a WDP arrangement is finalised | MEDIUM |
| Contract term length, renewal, and termination/notice provisions for the rental/placement arrangement | Standard commercial-agreement due diligence, not yet raised in any correspondence | MEDIUM |
| WDP's specific insurance/certificate-of-currency requirements for GTT Center Perth | `financial-setup.md` STEP 8 already notes a certificate is required "before accreditation inspection," but WDP's own specific minimums/coverage requirements haven't been directly confirmed | MEDIUM |
| Payment structure and frequency for the eventual rental fee (annual upfront, monthly, etc.) | Affects cash-flow timing once a real figure exists | LOW until a commercial figure is actually quoted |
| **Whether the committed daily volume WDP is quoting against is still accurate** | Anthony's sent 2026-07-31 reply told Carole "12 clients each morning" — this reflects the pre-2026-08-05 model. `CURRENT-STATE.md`'s current PRIMARY committed model is now Table 1 (18 clients/day), per the 2026-08-05 rebase. **Any commercial quote WDP provides based on the 12-client figure may need to be re-scoped against the higher, current committed volume** | HIGH — a real, previously-undetected gap between the volume already told to WDP and this venture's current committed model |

### 4.4 Recommended Immediate Action (framework only — not actioned here)

Before Carole's reply to the 2026-07-31 email arrives (or in the same follow-up), Anthony may want to flag the volume discrepancy in §4.3 directly — clarifying that planning has since moved to 18 clients/day as the primary committed model, so any commercial figure WDP provides should be scoped against that volume, not the 12/day figure originally quoted. This is a recommendation for Anthony to action, not something this phase performs.

---

## Validation — Confirmed No Model Changes Occurred

- `git status --short` before this phase: clean.
- File created this phase: `docs/architecture/VENUE-ACQUISITION-DUE-DILIGENCE.md` only.
- Full pytest suite: **114 passed**, 0 failed.
- `tools/validate_canonical_data.py`: **13 files checked, 0 errors, 27 warnings** — identical to every prior phase.
- `tools/check_consistency.py`: **0 findings** — identical to every prior phase.
- `git diff --stat` against `data/canonical/`, `data/models/`, and `tools/*.py`: zero changes.
- No venue was selected or scored. No financial assumption, canonical figure, or open tracker item was changed. No investor or lender materials were created.

## Recommended Next Step

Two independent, zero-cost actions are available immediately: (1) Anthony flagging the volume discrepancy to Carole (§4.3/§4.4) before or alongside her reply, since it costs nothing and closes a real gap in an already-active conversation; and (2) beginning to populate the Venue Data Capture Template (§2) against the existing unverified candidates in `property-links-2026-07-28.md` (53 Hardy Road, Nedlands is flagged in that document as the strongest layout match found so far and would benefit most from a direct agent call to fill in the missing size/price fields). Both actions use tools this phase built without requiring a venue decision yet.
