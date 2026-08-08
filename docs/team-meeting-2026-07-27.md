# GTT Center Perth — Team Meeting: Planning-to-Operating Transition
**Date:** 2026-07-27 | **Facilitator:** Grace (Operations Manager) | **Attendees:** Ivy, Reed, Poppy, Quinn, Bruno, Cora, Fern, Jade

## Purpose
Move from planning docs to an operating business. Every blocker below was re-verified against live server docs today -- not assumed from prior session memory.

---

## Verified Status of Known Blockers (as of 2026-07-27)

| # | Blocker | Status 2026-07-21 | Verified Status Today | Owner |
|---|---|---|---|---|
| 1 | Venue Manager hire | Not recruited | STILL OPEN. staff-plan.md still lists Imara as "Managing Director / Venue Manager" in the org chart and pay table -- this is STALE and contradicts the confirmed 2026-07-18 decision (Imara has zero operational involvement; new Venue Manager hire takes all her duties). grace.md (agent identity) is correct; staff-plan.md (the actual operating doc) was never fixed. Recruitment itself has not started. | Fern (fix doc + write job ad) / Anthony (approve budget, run hire) |
| 2 | WDP pathology courier | Emailed 2026-07-19, awaiting reply | UNVERIFIED -- cannot confirm the email was sent or a reply received. pathology-partnership-brief.md still reads "Status: Action required -- WDP call is Week 1 priority before any venue is signed," i.e. pre-outreach language. No email log, sent-confirmation, or reply found in the repo. Flagging per capability-gap rule rather than assuming Reed's earlier outreach is current. | Reed (confirm actual send status) / Anthony (if a real reply exists outside repo, share it) |
| 3 | PathWest + Clinipath contact | Not yet emailed | Consistent -- still not contacted. Correctly sequenced behind WDP (2nd/3rd priority per pathology-partnership-brief.md), not a bug. | Reed (only after WDP resolves) |
| 4 | Property leads | No listing URLs/agent/ID in repo | OUT OF DATE -- repo is actually ahead of the brief. location-scouting.md (Quinn) has 3 specific Osborne Park properties with agent names and a commercialrealestate.com.au listing ID (2A/236 Main Street - Ray White Commercial WA; 6/325 Harborne Street - AGORA Property Group; 20 Parkland Road - listing #16969571), sourced Empire Day 71. Maylands/Hardy St leads referenced elsewhere appear to be an older, narrower shortlist since superseded. None have been called or viewed yet. | Anthony (call agents, book inspections) -- Quinn to hand off contact list |
| 5 | Price-increase timing (Month 3 vs 4) | Built, needs decision | Confirmed still open, documented in HANDOFF.md as awaiting Anthony, recommendation leans Month 4. | Anthony (decision only, ~5 min) |
| 6 | 3D scan scope conflict | Flagged, not fixed | Cannot verify a conflicts log exists. No 01_conflicts_log.md or any conflicts-log file found anywhere in the repo -- either already resolved/removed, renamed, or never committed. 21 docs still reference 3D scan/keepsake/ultrasound content; not manually diffed against current scope in this session. Flagging as unverified rather than assuming stale references are fixed. | Poppy + Jade (grep + align marketing copy to current scope) |
| 7 | ivy-booking-system.md stale model | Needs update | CONFIRMED STILL STALE. Explicitly references "8-client/morning schedule," "4-5 subtenants," and "Subtenant Rent Billing" -- none of which match the committed 10-client, employed-staff (not subtenant) model. This is a real, current doc-accuracy blocker, not resolved by any session since. | Ivy (rewrite booking spec against committed model) |

## New Finding (not in original brief)
CortexOS venture registration -- already done, contrary to what the brief implied might still be open. Verified by direct DB query: `ventures` table has `gtt-perth`, and all 9 agent rows (grace, ivy, reed, poppy, quinn, bruno, cora, fern, jade) are correctly tagged `venture=gtt-perth`. This blocking gate from the onboarding checklist is closed -- no further action needed here.

---

## Functional Perspectives

**Ivy (Booking & Scheduling):** Can't stand up a real booking system on a spec that describes the wrong model. Fresha platform choice and GTT-pairing workaround logic are still sound and reusable -- only the capacity/pricing assumptions need correcting. This is a rewrite, not a re-architecture. ~1 day of work once she has the final locked model to reference (services-pricing-locked.md, am-capacity-weekend.md).

**Reed (Pathology & Subtenant Partnerships -- role title itself is stale, "subtenant" no longer applies):** Owns the single most schedule-critical open item. Without a live WDP conversation, nothing else -- venue signing, equipment purchase, phlebotomist hiring -- can proceed with confidence, because WDP's collection-room spec and courier cutoff time gate the floor plan and the AM timetable's tightest constraint (5-minute buffer at higher volumes). Needs to personally confirm send/reply status today, not assume the earlier outreach is still live.

**Poppy (Marketing):** Can't finalize any public-facing copy (Instagram, referral cards, website) while the 3D scan scope is ambiguous in the docs -- risk of promoting a feature that was dropped. Needs Grace/Anthony to confirm current scope in writing so marketing copy has one source of truth.

**Quinn (Location & Site Research):** Has done more than credited -- three real, contactable Osborne Park leads sit idle. This is now purely an execution gap (calls + inspections), not a research gap. Ready to hand off.

**Bruno (Finance):** Flags that Imara's remuneration structure (salary vs trust distribution) still needs accountant sign-off, and the whole staff-plan.md pay table needs to reflect the Venue Manager replacing Imara's line item before it's usable for a real pay run.

**Cora (Clinical Coordinator):** Collection room standards and phlebotomist credentialing are downstream of Reed's WDP conversation -- WDP's minimum room spec must be in hand before Quinn's shortlisted venues can be assessed for viability, and before Cora can finalize the clinical protocol doc.

**Fern (HR & Compliance):** Venue Manager is the most consequential open recruit -- emergency response, EpiPen administration, fire warden, and payment approval authority under A$2,000 all sit with this role per emergency-plan.md. Fern needs Anthony's go-ahead to write the job ad and open recruitment; this cannot start until staff-plan.md's org chart is corrected first (recruiting against a wrong reporting line wastes the hire).

**Jade (Customer Experience):** End-to-end journey design needs the 3D scan scope resolved for the same reason as Poppy -- first-touchpoint materials (referral cards, website) cannot be finalized on an ambiguous offer.

---

## Prioritized Next Steps

| # | Action | Owner | Est. Time | Blocking? |
|---|---|---|---|---|
| 1 | Confirm real-world status of WDP outreach (was the 2026-07-19 email actually sent? any reply?) and if not sent, send it today with the scripted call/email in pathology-partnership-brief.md | Reed | 1 hr + wait time | YES -- gates venue viability, floor plan, timetable |
| 2 | Fix staff-plan.md: replace Imara with "Venue Manager (to be hired)" across org chart, pay table, EOD/close duties, Food Safety Supervisor line | Fern | 2 hrs | YES -- blocks correct recruiting |
| 3 | Write Venue Manager job ad + open recruitment (after #2 is fixed) | Fern | 1 day to draft, Anthony to approve budget/post | YES -- critical path, venue cannot safely open without this hire |
| 4 | Call the 3 Osborne Park agents (Ray White Commercial WA, AGORA Property Group, and the #16969571 listing) to book inspections | Anthony | 1-2 hrs of calls | YES -- nothing else physical can start without a venue |
| 5 | Rewrite ivy-booking-system.md against the committed employed-staff model (drop subtenant billing language, correct client-count references — historical text said 10-client, now 18-client, see docs/CURRENT-STATE.md) | Ivy | 1 day | Not launch-blocking short-term, but must be fixed before Fresha setup begins |
| 6 | Resolve 3D scan scope ambiguity -- Grace to state current scope in one line, Poppy/Jade to grep and align all marketing-facing docs | Grace + Poppy + Jade | 2-3 hrs | Not launch-blocking, but a legal/marketing accuracy risk if left |
| 7 | Decide package price-increase timing: Month 3 vs Month 4 | Anthony | 5 min decision | No -- can be decided any time before Month 3 |
| 8 | PathWest/Clinipath outreach | Reed | N/A | No -- correctly sequenced behind WDP, do not start early |

## Needs Anthony Directly
- Item #3: approve Venue Manager recruitment budget and post the role (Fern drafts, Anthony greenlights -- this is the single longest lead-time item on the critical path)
- Item #4: agent calls / property inspections (Quinn has done the research; only Anthony or a delegated commercial agent can physically transact this)
- Item #7: price-increase timing decision
- Confirm whether the WDP outreach genuinely went out -- if Anthony has a reply or sent-confirmation outside the repo, share it so Reed isn't duplicating outreach

## Unverifiable / Flagged Per Capability-Gap Rule
- WDP email send/reply status -- no evidence found in repo either way
- Whether a 3D-scan conflicts log ever existed under a different name/path, or was resolved and the doc deleted -- not confirmed either way
- Whether the 21 docs referencing 3D scan content actually contain a real scope conflict or just consistent keepsake-only framing -- not individually diffed in this session

---
*Compiled by Grace, synthesizing Ivy/Reed/Poppy/Quinn/Bruno/Cora/Fern/Jade functional input against live server docs verified 2026-07-27.*
