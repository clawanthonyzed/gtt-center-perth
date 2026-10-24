# GRACE-R16: Corrected roster, midwife cost, draws, rooms, clinical rules

Author: Grace (Operations Manager, GTT Center Perth). Date: 2026-10-24. Repo: clawanthonyzed/gtt-center-perth (fresh clone, commit 80873ab; the old server clone was 404 commits behind and was not used). All money in AUD. This is general knowledge plus repo figures, not legal advice. Legal points are flagged for Catherine.

Sources used: docs/CURRENT-STATE.md (CS), docs/staff-plan.md (SP), docs/gtt-clinical-protocol.md (CP), docs/pathology-collection-room.md (PCR), docs/onboarding.md (ON), data/canonical/cost_ramp.yml (CR), tools/cost_ramp_model.py (CRM), docs/overhaul-2026-10-19/L10-r15/THEODORE-R15.md (T15), docs/overhaul-2026-10-19/L2-medicare/PARTNER-LAB-REQUIREMENTS.md (PLR), docs/overhaul-2026-10-17/M-model/R1-ADAPTIVE-PHLEBOTOMY.md (R1). My Round 15 workforce model was not used.

## 0. Anthony's corrections versus the repo (what actually differs)

| Item | Repo says | Anthony's correction | Effect |
|---|---|---|---|
| Venue manager hours | Mon-Fri 07:00-15:00, 8 paid hours (SP line 88; CRM OPENING_TIME_INCREMENT_DAILY 8 h x A$40) | Mon-Fri 06:30-15:00, also host and reception | Adds 0.5 h a day: A$440.00 wages, A$500.28 loaded a month (22 days x 0.5 h x A$40, plus 12% super and 1.7% workers comp) |
| AM receptionist and host | SP line 70 shows a 07:00-12:00 receptionist, but CR lines 638-664 and T15 line 182 confirm the repo has no receptionist cost line | None; venue manager does it | No cost. Cancels the A$12,166.54 a month receptionist plus host that T15 added |
| Saturday venue manager | An experienced rostered staff member (CS line 46); pay loading is a placeholder | Senior staff member | No cost line. Loading: not in repo |
| Afternoon after 15:00 | PM treatment staff do check-in in booking gaps (CR lines 638-664) | A senior experienced staff member covers the gap | No new cost if she is one of the four rostered PM staff. Any leading-hand loading: not in repo |
| Packages | Package 1 is a fixed 2 x 30 minute (A$250); Package 2 flexible, up to 2 x 45 (A$300) (CS lines 92-93) | Only Package 2 clients get two 45 minute services; Package 1 gets one | Revenue and price effect: not in repo, not modelled. Therapist load per Package 1 client falls, so the repo staffing tiers are a safe upper bound |
| Workforce master | CS lines 18-26 | Only change is 1 or 2 midwives 9-5 in the consult room | Costed in section 2 |

## 1. Corrected weekly roster, Monday to Saturday

Model: 07:00 first booking, 25 minute pair cadence, 9 pairs, up to 18 clients, last first draw 10:20 (CS line 18). Adaptive rostering, no idle staff (CS lines 19, 23, 83).

| Role | Mon-Fri hours | Saturday hours | Rule and source |
|---|---|---|---|
| Venue manager (host and reception) | 06:30-15:00 | Not rostered. A senior experienced staff member does the manager duties | Anthony 2026-10-24; Saturday cover CS line 46 |
| Senior experienced PM staff member (afternoon cover) | 15:00-18:00, within her PM shift | Same on Saturday as the manager cover, from open to close | Anthony 2026-10-24; she is one of the four PM staff (CR lines 638-664). Pay loading: not in repo |
| Phlebotomists | 07:00-13:00. 1 when 9 or fewer are booked, 2 when 10 to 18. Second collector named and on call on mornings of 9 or fewer | Same | CS lines 19, 23; R1 section 2; shift hours CRM lines 95-108 |
| AM therapists (massage and beauty, nails, hair) | 07:00-13:00. 1 client: 2 therapists. 2 to 9: 4. 10: 6. 11 to 18: 8 | Same | CS line 19 |
| PM treatment staff (4 casual roles) | 12:00-18:00, 10 sessions a day, 3 hour minimum shift | 8 sessions | SP line 76; CS lines 97, 111; CRM lines 213-225 |
| Midwife (new) | 09:00-17:00 in the consult room | 09:00-17:00 only if the six day option is chosen | Anthony 2026-10-24 |
| Casual relief pool | As needed | As needed | CS line 136 |

Who covers gaps:

| Time | Gap | Covered by |
|---|---|---|
| 06:30-07:00 | Opening before first client | Venue manager |
| 07:00-15:00 | Host, reception, check-in, fasting check | Venue manager (no separate host) |
| 12:00-15:00 | PM check-in | PM staff in their booking gaps, venue manager present |
| 15:00-18:00 | Venue manager has left | Senior experienced PM staff member |
| Saturday all day | No venue manager | Senior experienced staff member rostered that day |
| Between booked clients | Idle service staff | Advance online bookings fill sellable gaps, not walk-ins. Lead-in and tail time is not sold: release staff early, subject to the 3 hour casual minimum (CS line 84) |
| Venue manager sick Mon-Fri | Nobody named | Not in repo (SP lines 342-352 flag the compounding risk) |

Not in repo: a named deputy for the venue manager on weekdays, the leading-hand loading, and any paid on-call allowance (R1 section 3 option 4).

## 2. Corrected workforce cost

Calculators run unchanged on the fresh clone: tools/master_financial_model.py, tools/cost_ramp_model.py, tools/am_volume_tier_staffing_solver.py, tools/check_consistency.py (two stale-value flags in unrelated 2026-10-16 and GST files, nothing about staffing). No new calculator was written. The repo does not contain midwives, so the midwife lines are simple multiplication of Theodore's R15 inputs (T15 Part 1): Nurses Award RN level 2 pay point 4, A$41.59 an hour weekday, 150% Saturday, times the R15 on-cost multiplier 1.20 (super, leave loading, workers comp, leave cover). That gives A$49.91 an hour weekday and A$74.86 Saturday.

Repo baseline (unchanged): payroll A$93,595.63 a month loaded, A$82,318.05 wages (CR cost_table1_m5plus). Net A$35,186.40 a month (CS line 179). That net contains no payroll tax (T15 Part 3).

Assumptions I chose, because the repo is silent: 9-5 is 8 hours on site with a 30 minute unpaid break, so 7.5 paid hours; 22 weekdays and 4.33 Saturdays a month (repo convention); the midwife earns no revenue in these lines (repo has none). One midwife cannot work six eight hour days on a permanent award (45 paid hours against about 38 ordinary), so the six day options need two people or overtime.

| Option | Paid hours a week | Midwife cost a month, loaded | Total payroll a month (repo 93,595.63 + VM 500.28 + midwife) | Net a month versus repo 35,186.40, before payroll tax | Extra payroll tax a month, approx 6.35% of wages plus super (T15) | Net after that tax |
|---|---|---|---|---|---|---|
| Venue manager 06:30 only, no midwife | 0 | A$0.00 | A$94,095.91 | A$34,686.12 | A$0 on midwife | A$34,686.12 |
| 1 midwife, Mon-Fri | 37.5 | A$8,234.82 | A$102,330.73 | A$26,451.30 | A$488.05 | A$25,963.25 |
| 1 midwife, Mon-Sat (or 2 part-timers sharing the six days, one on at a time) | 45.0 | A$10,665.96 | A$104,761.87 | A$24,020.16 | A$632.14 | A$23,388.02 |
| 2 midwives, Mon-Fri, both on every day | 75.0 | A$16,469.64 | A$110,565.55 | A$18,216.48 | A$976.10 | A$17,240.38 |
| 2 midwives, Mon-Sat, both on every day | 90.0 | A$21,331.93 | A$115,427.84 | A$13,354.19 | A$1,264.27 | A$12,089.92 |

What changes versus the repo: for 1 midwife the net falls by about A$8,700 (Mon-Fri) to A$11,200 (Mon-Sat), a cost of A$8,235 to A$10,666 plus A$500 for the venue manager half hour. For 2 midwives on every day it falls by about A$17,000 (Mon-Fri) to A$21,800 (Mon-Sat). Break-even and margin-of-safety figures (7.250 clients a day, CS line 31) have not been recomputed, because the repo solver has no midwife input. Break-even rises by the extra fixed cost. Not in repo.

Reconciliation with Theodore (R15):
- His midwife figure for the six day case is A$54.07 an hour (weekday and Saturday blended) times 197.5 hours = A$10,678. Mine is A$10,666. They agree within A$12.
- His A$12,511 (2 midwives) and A$19,462 (3 midwives) were built on consult demand hours (53.4 and 83.1 a week), not on 9-5 cover. They are a different question and do not match mine. That is expected, not an error.
- His combined payroll of A$118,274 and A$125,224 (T15 section 4.2) includes a receptionist and host worth A$12,166.54 a month. Anthony removed both. Without them his numbers become A$106,107 and A$113,057; my six day figures are A$104,762 (1 midwife) and A$115,428 (2 midwives both on). The gap is hours, not method.
- His payroll tax rule (A$562 a month on the repo base, A$63.46 per A$1,000 of extra wages) is applied above as an approximation. The A$562 base is not in the repo net and is not deducted here.
- Award uplift after 1 July 2025 for repo rates is unconfirmed (T15 section 4.1). Midwife award rate is class E (estimate), not verified by an accountant.

## 3. Does the midwife need to be at the clinic for draws?

Operations view:
- Normal collection uses phlebotomists only (CP line 53; CS lines 19-23). A midwife is not part of a pathology draw.
- First draws run 07:00 to 10:20, second draws 08:00 to 11:20, final draws up to about 12:25 (R1 section 2). A midwife on 09:00-17:00 is present for roughly the last 70 percent of that activity and absent for the first two hours.
- She can work normal 9-5 hours. Her consult work is separate from collection and does not depend on the draw timetable.
- Whether the lab or Medicare rules need a midwife present is a legal question. Flag for Catherine.

Handover and escalation when no midwife is present (07:00-09:00), using the repo protocol (CP lines 198-215):

| Event | Who acts | Steps in the repo | Gap or question |
|---|---|---|---|
| Faint or dizzy | Phlebotomist at once, then venue manager | Keep seated or lie flat, do not stand her, call venue manager, 000 if unconscious, record in incident register | Venue manager is on site from 06:30 and is the first aid holder (SP line 312). No clinician is on site before 09:00 |
| Adverse reaction (nausea, vomiting the drink) | Phlebotomist, venue manager | Do not repeat the drink, notify referring doctor, reschedule | Escalation inside the lab's own protocol: not in repo, lab question |
| Difficult draw | Phlebotomist, then on-call second collector | Maximum 2 attempts, then second collector, then reschedule or refer | Lab protocol beyond that: not in repo |
| Urgent or critical result | The lab | Results go to the referring doctor within 24 to 48 hours; GTT Center does not give results (CP line 157) | Critical value call-back route to a midwife or doctor on site: not in repo. Flag for Catherine and the lab |

Suggested ask, not a change to the master plan: a named doctor or midwife phone contact for 07:00-09:00 and a written same-morning escalation line from the lab. A 08:30 midwife start is an option for Anthony to decide; not costed.

## 4. Consult room and collection suite, words only

Not in repo: any consult room specification. Not searched externally this round, so every Australian standard for the consult room is U (not verified). I did not draw a plan.

Consult room (proposal; size U):

| Item | Specification | Basis |
|---|---|---|
| Size | About 12 to 14 sqm (matches the repo's own recommended clinical room size), enough for couch, desk, two chairs and a wheelchair turning space | Repo PCR "12-14 sqm" for collection room; consult standard U |
| Privacy | Solid walls to ceiling, solid door, frosted glazing, no view from the lounge or waiting area, do-not-disturb light | PCR privacy section |
| Sound | Acoustic insulated walls and door seals, no shared ducting, white-noise unit outside the door. No number for sound rating | Rating: U |
| Handwashing | Hands-free basin with soap, paper towel and hand rub inside the room or at its door | PCR plumbing section |
| Couch | Height adjustable examination couch, wipe-clean upholstery, disposable paper roll, a pregnancy wedge | Specifics: U |
| Desk and computer | Desk with screen angled away from the door | |
| Records | Lockable cabinet or lockable drawers, screen lock, no records left on the desk | Privacy Act 1988 reference in PCR; WA and health record rules: U, Catherine |
| Emergency | Wall call button to reception, first aid kit, oxygen and defibrillator location, couch that can lie flat | PCR emergency response section; midwife equipment list: U |
| Accessibility | 850 mm clear door (repo DDA figure), wheelchair turning space, accessible toilet near. Australian accessibility standard: U | PCR door line |
| Feel | Day spa and sanctuary: warm lighting, timber and soft fabrics where they can be wiped, calm colour, no hospital signage. Only the blood collection room is allowed to look clinical (VENUE-FUNCTIONAL-BRIEF line 93, referencing BRAND-ARCHITECTURE) | Repo brand rule |

Collection suite (repo values): two rooms of 18 to 20 sqm with solid walls (floor-plan-concept.md line 38); 18 sqm in the room schedule (VENUE-FUNCTIONAL-BRIEF line 81); non-slip seamless vinyl with coved skirting; no soft furnishings in the room; 400 to 800 lux with CRI above 85; at least 6 air changes an hour and no shared return air; elbow or sensor taps, soap, paper towel and hand rub; at least 4 outlets at bench height; recliner that goes fully flat; centrifuge within 10 minutes of draw; sharps containers to AS/NZS 23907:2023; lockable consumables and documentation storage; wall call button; 850 mm door (PCR sections Room Specifications through Emergency Response). The repo says its NPAAC access attempts failed (8 times), so the NPAAC standard itself is U. The 2013 ACSQHC guideline citation in PCR is the repo's, not verified by me.

## 5. Clinical rules

Source check: I read the PathWest sheet SOP-2484 version 1.0, issued 24/07/2026, directly (the PDF text, not only the repo's quote).

| Rule | Anthony's instruction | What the sheet and repo say | Status |
|---|---|---|---|
| 60 and 120 minute draws | From the first draw unless the lab says otherwise | Sheet: fasting sample, then the glucose drink immediately after, then samples one hour and two hours after the drink. Repo scheduler uses exact 60 and 120 minutes (CS line 60). The difference is a few minutes | Lab question: confirm the clock starts at the draw or at the drink |
| Fasting | | Sheet: at least 10 to 12 hours, no longer than 16. Repo CP line 99: 10 to 12. Repo gtt-test-reference.md line 57 says 8 to 14 hours, which is stale and wrong | Fix the stale file |
| No strenuous activity | Yes | Sheet: no exercise instruction beyond "continue fasting"; repo CP line 106: no exercise on the morning | Use repo wording. Define walking between rooms as allowed: lab question |
| Client stands for each draw, then returns to a waiting area | Yes | Sheet: "required stay in the collection centre and remain seated until the test is finished". Repo CP line 139 seats her or reclines her for draws; vasovagal rule: do not stand a dizzy client (CP line 199) | Conflict. Standing is Anthony's rule but conflicts with the sheet and the faint rule. Lab question, and a safeguard: stand only if she feels well, otherwise seated |
| Massage between draws | | Sheet requires seated. Repo lets her return to services between draws (CP line 151). Massage lying down is not seated | Lab question: does a reclined massage count? Until answered, the seated rule means chair-based or seated services only |
| Herbal tea | Check PathWest and others | Sheet: no tea, coffee, juice or milk during fasting, "water only" on the day of the test; it says nothing that ends the fast after the first draw | See below |

Honest answer to "are you sure herbal tea is only after the first draw?": No, I am not sure, and the repo is wrong. ON line 291 offers herbal tea after the first draw. The PathWest sheet does not support that. It tells the client to remain fasting on the day of the test and to drink water only. The first draw is followed by the glucose drink and two more samples, and the sheet gives no point before the final draw where fasting stops. Current rule to use: water only until the final draw is done; herbal tea and food only after it. Tea could be allowed earlier only if PathWest, and any other partner lab, approves it in writing. Make it a lab question. I did not check Clinipath or any other lab's sheet; the repo has no copy of one (PLR section c holds PathWest only). Status: other labs U.

Lab questions to send (drafts only, nothing sent):
1. Does the 60 and 120 minute clock run from the fasting draw or from the end of the glucose drink?
2. Is a client who walks to a treatment room between draws, and has a reclined or lying treatment, treated as remaining seated?
3. May herbal tea or any drink other than water be given before the final draw? Please answer in writing.
4. What is the lab's escalation for a faint, adverse reaction, or critical result at a non-lab site?
5. Does the lab require a midwife or other clinician on site?

## 6. Open items for Anthony

1. Midwife option: one midwife Mon-Fri, or six days, or two on every day. Net impact in section 2.
2. Does an 07:00-09:00 clinician gap need a named phone contact or an 08:30 start?
3. Leading-hand loading for the Saturday and afternoon senior staff member: not in repo.
4. Package 1 revenue effect of one service only: not modelled.
5. Fix ON line 291 and gtt-test-reference.md line 57.
