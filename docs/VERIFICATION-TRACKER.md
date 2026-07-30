# GTT Center Perth — Verification Tracker

**Created:** 2026-07-29 | **Merges and replaces:** `05_open_questions_for_founder.md`, `regulatory-accreditation-tracker.md`, `04_roadmap_next_steps.md` (all three archived to `docs/archive/` this session — do not recreate duplicates of their content).

**Purpose:** Single running list of every unconfirmed fact in this venture's documents, who can confirm it, and current status. Companion to `docs/CURRENT-STATE.md` (canonical current figures) — this file tracks what's still open, that file tracks what's currently believed.

**Rule going forward (see `rules/CLAUDE.md`):** when a new unconfirmed fact surfaces, add it here first. Do not scatter new assumptions through other documents. When resolved, update the status and date here, and update `docs/CURRENT-STATE.md` if the resolution changes a canonical figure.

**Status legend:** `BLOCKING` (nothing should proceed with full confidence past this) | `OPEN` (tracked, not urgent) | `IN PROGRESS` (action underway) | `RESOLVED` (confirmed, with source/date) | `NOT APPLICABLE` (decided not to pursue)

---

## BLOCKING

| # | Item | Who can confirm | Status | Detail |
|---|---|---|---|---|
| 1 | WDP specimen dispatch cutoff time (11:30 vs 12:30 — two conflicting unconfirmed figures) | WDP (Carole Rivers, Customer & Commercial Manager, Country) | **RESOLVED (nuanced) 2026-07-30 — real, written, conditional answer** | Carole's actual email (2026-07-30): overnight storage viable "in some circumstances" (fluoride oxalate tubes stable ~24hrs); "a late booking would not necessarily prevent collection, although specimen type and storage requirements would always need to be considered." `[VERIFIED — Carole Rivers, WDP, email, 2026-07-30]`. **Corrects the 2026-07-29 verbal readback, which had oversimplified this into a blanket "no cutoff" — that was wrong.** There is no single fixed cutoff, but it is conditional, not unconditional. Remaining follow-up: the exact storage/handling conditions needed to reliably use the overnight option are not yet spelled out — ask WDP for specifics before re-running the capacity model on a wider-window assumption. See `cutoff-time-CORRECTION.md` 2026-07-30 update. |
| 1b | WDP GTT start-time guidance | WDP (Carole Rivers) | **RESOLVED 2026-07-30** | Carole's email: "would not normally commence a GTT after 10:30am" (exceptions for shift workers etc.) `[VERIFIED — Carole Rivers, WDP, email, 2026-07-30]`. Supersedes the PathWest-sourced "preferably before 10am." Scenario C's 09:40 last draw clears this with margin. See `king-edward-start-time-constraint.md`. |
| 1c | WDP commercial/rental structure for a venue-based collection clinic | Anthony / WDP commercial negotiation | **OPEN — no figure exists** | Carole's email: annual rental arrangement, terms depend on expected pathology volume, number of referring doctors on-site, location/accessibility, overall business opportunity. Nothing quantified. Do not invent a rental estimate — see `docs/CURRENT-STATE.md` §1. |
| 1d | **HIGH PRIORITY — Phlebotomist employment model: in-house (current model) vs WDP-supplied under the rental arrangement** | Anthony — needs to ask Carole directly | **OPEN, NOT DECIDED** | Carole's email states phlebotomist "safety, wellbeing and employment responsibilities... would remain with Western Diagnostic Pathology" under the rental model. This directly affects whether the current ~A$48,255/month AM Direct Labor figure (`docs/CURRENT-STATE.md` §4/§7) stays as-is (in-house employment) or gets replaced by a to-be-negotiated rental fee (WDP-supplied). **Anthony's explicit instruction: NOT DECIDED, do not assume either way — ask Carole to clarify.** No P&L figure has been changed over this; it is flagged as a critical open dependency instead. |
| 2 | Whether overnight blood storage + next-day lab collection is viable as an alternative to the same-day courier cutoff | WDP | **RESOLVED (see item 1) — viable "in some circumstances," not unconditional** | Folded into item 1's 2026-07-30 resolution above — kept as a separate row for trace since it was tracked separately before. |
| 3 | Physical venue location | Anthony (search), landlords (terms) | **BLOCKING** | Nothing else on the critical path (Venue Manager recruitment, fit-out, staff hiring, council permits) starts until this is confirmed, per Anthony's direct instruction. |
| 4 | PathWest/Clinipath partnership replies | PathWest (info.pathwest@health.wa.gov.au), Clinipath (businessdevelopment@clinipath.net) | **IN PROGRESS** | Both emailed 2026-07-27, awaiting reply. **Capability gap flagged:** this agent has no confirmed email-sending capability — outreach is drafted/ready, actual send/delivery needs Anthony or Reed to confirm directly. |
| 5 | King Edward/PathWest "start before 10am" guidance — source strength | Anthony (found), no further action needed | **RESOLVED 2026-07-20** | Real official source found: PathWest's own "Patient Instructions — GTT" (Jan 2019, hosted on KEMH's site) — see `king-edward-start-time-constraint.md`. Kept here for traceability only. |

---

## FINANCIAL — NEEDS ACCOUNTANT CONFIRMATION

| # | Item | Who can confirm | Status | Detail |
|---|---|---|---|---|
| 6 | Startup capital range (3 different, never-reconciled ranges exist: A$363,000 mid / A$292-493K; A$144,500-242,500; A$209-431K) | Accountant / quantity surveyor + Anthony | **OPEN, flagged not resolved** | See `docs/CURRENT-STATE.md` §6 for the full 3-way comparison. Needs a fresh itemised build against the current 10-client/2-package model, not a selection among the three historical figures. |
| 7 | GST treatment of the AM package price — fully taxable, or mixed GST-free-pathology/taxable-wellness apportionment | Accountant | **OPEN** | `cash-flow.md`'s GST Treatment section flags a likely inconsistency: since GTT Center Perth earns zero pathology revenue (the partner bills Medicare directly), the whole package price may be a standard-rated (10% GST) supply, not a mixed apportionment as `financial-setup.md` previously assumed. Confirm before first BAS lodgement. |
| 8 | ABN/GST registration under the trust — covers this trading activity or needs a new registration | Accountant | **OPEN** | `financial-model.md` §1 flags this as unconfirmed. |
| 9 | Proposed 30% flat trust-distribution tax (effective 1 July 2028 per current proposal) — not yet legislated | Accountant / track legislation | **OPEN, not blocking** | Modelled illustratively in `financial-model.md` §2 (split from the old combined doc 2026-07-29 — see that document's changelog) — methodology still valid but dollar figures are built on the abandoned 8-client P&L model and need re-running against `docs/CURRENT-STATE.md`'s current figures before use. |
| 9b | Imara's current employment status vs the trust distribution tax modelling | Accountant | **OPEN** | `financial-model.md` §2 flags that Imara returned to full-time employment (April 2026) — the existing tax-comparison tables assumed "sole income," which no longer holds. Needs re-modelling against her current marginal tax bracket before any distribution decision. |
| 10 | Ancillary revenue lines (spray tan A$58,000/yr, retail A$25,000/yr, cafe A$15,000/yr) — no real derivation found for 2 of 3 | Real post-launch foot-traffic/spend data, or a stated comparable-venue benchmark | **OPEN, PLACEHOLDER** | `cash-flow.md`'s Ancillary Revenue Sourcing section: spray tan's operating-day assumption is stale, retail/cafe have no bottom-up derivation anywhere in this corpus. ~7-8% of total revenue — doesn't change the overall profitability picture materially, but should not be quoted with false confidence. |
| 11 | MA000027 Saturday phlebotomist ordinary-hours carve-out (may reduce Saturday penalty-rate cost if it exists) | Payroll advisor or Fair Work Infoline (13 13 94) | **OPEN — capability gap flagged** | No live web-fetch tool / award-interpretation skill was available in the session that investigated this. All financial models use the conservative full-penalty assumption until confirmed. See `hr-framework.md`. |
| 12 | Whether adopting the 7-staff (not 8) AM treatment headcount via Massage+Beauty cross-training is actually hireable | Venue Manager (once hired) | **OPEN — operational decision, not yet actioned** | `profit-loss-tables.md`'s Treatment Headcount section confirms 7 is the genuine scheduling minimum at 10-client/day volume (saves ~A$5,231/month) but finding a dual-qualified hire is a real-world constraint not yet tested. |
| 13 | Combined AM/PM rotating staff pool — could this reduce total headcount below 11? | Venue Manager, real roster data post-launch | **PLACEHOLDER — explicitly not booked as a confirmed saving** | `dual-role-staffing-model-2026-07-28.md` v3.0 flags this as a genuine open question, not assumed either way. |
| 14 | **Propagation gap — old +A$25,087.07/month headline figure still cited in several documents** | Whoever next edits these docs | **OPEN, tracked, not silently left** | `tools/check_consistency.py` (run 2026-07-30, after the ancillary-exclusion recalculation) found `feasibility.md`, `price-increase-comparison.md`, `rent-budget-2026-07-28.md`, `review-audit.md`, and `pm-staffing-roster.md`'s own remaining trace mentions still citing the pre-2026-07-30 +A$25,087.07/month or +A$301,044.84/year figures. `docs/CURRENT-STATE.md`, `profit-loss-tables.md`, `investor-memorandum.md`, `executive-summary.md`, and `HANDOFF.md` were fixed directly this session (the highest-traffic docs) — the remainder were not, given the volume of documents in this repo (107+ files) and this session's time budget. Fix opportunistically when next touching any of these files, or run a dedicated sweep. |

---

## REGULATORY / ACCREDITATION

| # | Item | Who can confirm | Status | Detail |
|---|---|---|---|---|
| 14 | Pathology partner agreement (WDP, priority 1) | WDP | **IN PROGRESS** | See BLOCKING #1 — same conversation thread. |
| 15 | Pathology partner agreement (PathWest, contingency) | PathWest | **IN PROGRESS** | Emailed 2026-07-27, awaiting reply. |
| 16 | Pathology partner agreement (Clinipath, contingency) | Clinipath | **IN PROGRESS** | Emailed 2026-07-27, awaiting reply. |
| 17 | Phlebotomist credentialing under the partner's NATA accreditation | WDP/PathWest/Clinipath (whichever confirmed) | **NOT STARTED** | Gated on partner agreement + physical venue. |
| 18 | Exact NATA/ACSQHC site-inspection requirements for the collection room | WDP/PathWest/Clinipath | **NEEDS VERIFICATION** | Room spec exists (`pathology-collection-room.md`) but the specific partner's own inspection checklist has not been obtained. |
| 19 | Medicare bulk-billing arrangement for the GTT pathology component — confirmed in writing? | WDP/PathWest/Clinipath, accountant | **NEEDS VERIFICATION** | Standard-arrangement assumption for a Licensed Collection Centre model, not yet confirmed in writing by any partner for this specific venture. |
| 20 | Council planning/health-use permit | Local council (suburb TBD) | **NOT STARTED** | Gated on venue selection. |
| 21 | Food business notification (low-risk category) | Local council | **NOT STARTED** | Confirmed as low-risk category in principle; needs council-specific confirmation once venue suburb chosen. |
| 22 | Local exhaust ventilation (LEV) compliance, nail station | WorkSafe WA | **NOT STARTED (design confirmed)** | Needs physical compliance check at fit-out. |
| 23 | WorkCover WA employer registration | WorkCover WA | **NOT STARTED** | Required before first hire; gated on venue + recruitment start. |
| 24 | Phlebotomist AHPRA registration — confirmed not applicable | AHPRA (not independently checked) | **ASSUMED, not independently verified** | Consistent with general knowledge of how pathology collection roles are credentialed in Australia, but not independently confirmed with AHPRA directly. |
| 25 | 3D keepsake ultrasound — legal/unregulated in WA, no AHPRA requirement for operator (future/Phase 2 only, not current scope) | AHPRA/Medical Board (if/when revisited) | **ASSUMED, working assumption only** | Re-verify against current guidance if the 3D scanner is actually revisited. Never framed as diagnostic. |
| 26 | Privacy Policy — solicitor review | Perth solicitor | **NOT STARTED** | Draft exists (`privacy-policy.md`), explicitly marked "DRAFT — solicitor review required," not to be used to collect data until reviewed. |
| 27 | Patient Consent Form — solicitor review | Perth solicitor | **NOT STARTED** | Draft exists (`consent-form.md`), same status. |
| 28 | Employment contract templates (per Modern Award) | Solicitor | **NOT STARTED** | `hr-framework.md` §3. |

---

## PROPERTY / VENUE

| # | Item | Who can confirm | Status | Detail |
|---|---|---|---|---|
| 29 | 2A/236 Main Street, Osborne Park (144sqm, A$43,200/yr + outgoings) | Agents Tom Jones (0478 771 117) / Lachlan Burrows (0499 552 296), Ray White Commercial WA | **VERIFIED live listing 2026-07-27** | Not yet inspected/negotiated. Listing: https://www.commercialrealestate.com.au/property/2a-236-main-street-osborne-park-wa-6017-16172595 |
| 30 | 6/325 Harborne Street, Osborne Park (268sqm, A$55,000/yr net + GST) | Agent Shannon Swarts, AGORA Property Group | **VERIFIED live listing 2026-07-27** | Not yet inspected/negotiated. Listing: https://reiwa.com.au/6-325-harborne-street-osborne-park-4941752/ |
| 31 | 20 Parkland Road, Osborne Park (994sqm, 28 parking) | Landlord/agent | **FLAGGED, likely not viable** | ~4-6x larger than the 150-250sqm target — Quinn to confirm before treating as a real lead. Listing: https://www.commercialrealestate.com.au/property/20-parkland-road-osborne-park-wa-6017-16969571 |
| 32 | Maylands (160sqm, 10 parking, negotiable rent) | Anthony / Quinn (fresh search) | **UNCONFIRMED — no matching live listing found** | Searched commercialrealestate.com.au and REIWA directly, 2026-07-27 — no property matches these specs. Treated as unconfirmed, not carried as live. |
| 33 | South Perth Hardy St (216sqm, A$4,750/month) | Anthony / Quinn (fresh search) | **UNCONFIRMED — no matching live listing found** | Existing Hardy St listings (19, 22) are marked leased/inactive. Same status as #32. |

---

## OTHER FOUNDER-ONLY DECISIONS (Decided, Kept for Traceability)

| # | Item | Status | Detail |
|---|---|---|---|
| 34 | Is Imara the operational manager? | **RESOLVED NO, 2026-07-18** | A dedicated Venue Manager (new hire, not yet in place) fills this role. Imara holds no operational role — see empire-wide CLAUDE.md rule on this. |
| 35 | DVA adviser consultation (TPI pension / trust distribution interaction) | **REMOVED from this venture's scope, 2026-07-19** | Anthony's personal matter, handled by him directly — not a GTT Center Perth task. |
| 36 | Package price-increase timing | **DECIDED 2026-07-29** | No price increase until 12+ months of operation — deferred entirely, not Month 3/4. See `price-increase-comparison.md` for retained reasoning (historical only). |
| 37 | Second venue / interstate expansion timeline | **CLARIFIED 2026-07-19** | Set only after the first venue is running smoothly — no earlier estimate, none should be implied anywhere. |
| 38 | Brand name | **CLARIFIED, not a pending decision** | "GTT Center Perth" is a working placeholder, not locked. Full branding created later on Anthony's timeline. |
| 39 | Payment policy — full prepayment vs deposit | **RESOLVED 2026-07-20** | Full package price collected at time of booking, no deposit option. |

---

## Changelog

**2026-07-29 (created, merge)** — Merged `05_open_questions_for_founder.md`, `regulatory-accreditation-tracker.md`, and `04_roadmap_next_steps.md`'s founder-decision content into this single file, per the external audit finding that having 3+ separate "open items" documents made it easy for a fix in one to never propagate to the others (the same root cause as the CURRENT-STATE.md file addresses for numbers). The 3 source files are archived to `docs/archive/`, not deleted, to preserve history — their content is fully represented above, so they should not be treated as live references going forward. `docs/04_roadmap_next_steps.md`'s Tier 1/2/3 documentation-fix action items (operations-manual.md rewrite, workflow.md staffing table) are process/roadmap items, not founder-confirmation items — the operations-manual.md rewrite was completed this session (see that document's own changelog); workflow.md's stale subtenant staffing table (CONFLICT-04) remains open and is noted here for continuity: **workflow.md's "Staffing Model (Launch)" table still describes a sublet/subtenant model contradicting the confirmed employed-staff model — flagged in `docs/01_conflicts_log.md` CONFLICT-04, not fixed this session (out of this session's specific scope), recommended as the next documentation-fix priority.**

**2026-07-30 (Carole Rivers' real email integrated — primary source, supersedes prior verbal readback)** — Anthony pasted Carole Rivers' (WDP) actual email reply directly in chat. Corrected item 1 from the 2026-07-29 verbal-only "no cutoff" summary (which had oversimplified a conditional answer into a blanket one) to the real, written, conditional answer: overnight storage viable "in some circumstances," late bookings "not necessarily" prevented, but specimen type/storage always need considering. Added item 1b (start-time guidance, resolved, supersedes PathWest sourcing), item 1c (WDP rental/commercial structure, open, no figure), and item 1d (phlebotomist employment model — in-house vs WDP-supplied — flagged HIGH PRIORITY, explicitly NOT DECIDED per Anthony, no P&L figure changed over this).
