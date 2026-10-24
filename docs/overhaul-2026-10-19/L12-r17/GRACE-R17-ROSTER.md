# GRACE-R17-ROSTER: Roster lock, two midwives, weekly grid, corrected weekly cost

Author: Grace (Operations Manager, GTT Center Perth). Date: 2026-10-24. Fresh clone of clawanthonyzed/gtt-center-perth (the server copy is stale and was not used). All money in AUD. No floor plans. Nothing was sent to anyone. Repo figures are not changed by this file.

Sources: docs/CURRENT-STATE.md (CS), docs/staff-plan.md (SP), docs/architecture/STAFF-POSITION-REGISTER.md (SPR), data/canonical/cost_ramp.yml and tools/cost_ramp_model.py (CRM, run unchanged on the fresh clone: Table 1 payroll A$93,595.63 a month), docs/overhaul-2026-10-19/L11-r16/GRACE-R16.md (G16) and THEODORE-R16.md (T16), and Catherine r16 and r15 on the server. No new calculator was written. The only arithmetic added is multiplication of the repo's own daily rates and Theodore's midwife rate.

## 1. The locked roster (Anthony, 2026-10-24)

| Role | Who covers it | Hours |
|---|---|---|
| Venue manager | One person. Covers reception and welcome | Monday to Friday 06:30 to 15:00 |
| Afternoon gap (after the venue manager leaves, to close) | A senior experienced staff member, one of the rostered PM therapists | 15:00 to 18:00 |
| Saturday venue manager | A senior staff member already rostered that day | Open to close on Saturday |
| Phlebotomists | Adaptive: 1 when 9 or fewer are booked, 2 when 10 to 18; none in the afternoon; a named second collector on call on mornings of 9 or fewer | 07:00 to 13:00 |
| Therapists (massage and beauty, nails, hair) | Adaptive rostering with gap filling: 1 client = 2; 2 to 9 = 4; 10 = 6; 11 to 18 = 8 | AM 07:00 to 13:00; PM four casual roles |
| Midwives (new) | Two midwives splitting Monday to Saturday | 09:00 to 17:00 in the consult room |

No separate welcome or greeter role exists in the locked roster. The venue manager does it.

Conflict on the venue manager start time, said plainly: the repo says 07:00 to 15:00, 8 paid hours (SP, SPR VM01, CRM OPENING_TIME_INCREMENT_DAILY = A$320 = 8 h x A$40). Anthony's note says 06:30. This file uses 06:30 as instructed and shows the repo basis beside it.

## 2. Conflicts flagged for Anthony (one line each, not decided)

1. Venue manager start: repo 07:00, Anthony 06:30. Costed at 06:30; it adds A$500.28 a month loaded.
2. Package content: the repo says Package 1 is a fixed 2 x 30 minute service pair (A$250) and Package 2 is flexible, up to 2 x 45 (A$300) (CS lines 92 to 93). Anthony's note says only Package 2 clients get two 45 minute services. The repo already agrees on the 45s, but G16 recorded Package 1 as "one service", which would conflict with the repo's two 30 minute services. Not decided here.
3. Prices: the repo has Package 1 A$250 and Package 2 A$300 (lounge only). Theodore R16 section D tests A$300 and A$350 as all-in prices with a midwife consult. Two price sets are in play. Not decided here.
4. SPR still says the venue manager works Monday to Saturday; CS (2026-09-19) says Monday to Friday. CS wins; SPR is stale.
5. Pay loading for the senior staff member who covers Saturday and the afternoon gap: not in repo. Not costed.
6. Herbal tea: repo onboarding.md line 291 allows tea after the first draw; the PathWest sheet and Catherine r16 say water only until the last draw. Lab question.

## 3. Weekly grid: two midwives, Monday to Saturday, about 3 days each

Suggested even split. 9 to 5 is 8 hours on site and 7.5 paid hours (30 minute unpaid break is my assumption; the repo is silent).

| Day | Midwife A | Midwife B | On duty | Hours on site |
|---|---|---|---|---|
| Monday | on | off | A | 09:00 to 17:00 |
| Tuesday | off | on | B | 09:00 to 17:00 |
| Wednesday | on | off | A | 09:00 to 17:00 |
| Thursday | off | on | B | 09:00 to 17:00 |
| Friday | on | off | A | 09:00 to 17:00 |
| Saturday | off | on | B | 09:00 to 17:00 |
| Days a week | 3 | 3 | one midwife each day | |
| Paid hours a week | 22.5 | 22.5 | 45.0 combined | |

Fairness option (Anthony's choice): B carries every Saturday at 150 percent pay. To even this out, use a fortnightly pattern: week 1 as above; week 2 A works Monday, Wednesday, Saturday and B works Tuesday, Thursday, Friday. Total hours and total cost stay the same.

Gaps in this grid (flagged, not solved by me): only one midwife is on any day, so a sick day leaves the consult room empty; no relief midwife is costed (Round 15 open item 4). Each midwife needs her own provider number for the location (Catherine r16, Theodore R16 section A1).

06:45 start question (an option, not a decision). Catherine r16 section 5 says there is no clinician on site from 07:00 to 09:00. Three ways to close it:
- Shift each shift to 06:45 to 14:45. No extra cost; loses consult room time from 14:45 to 17:00.
- Extend to 06:45 to 17:00. Adds 2.25 paid hours a day: about A$3,199.87 a month (22 weekdays x 2.25 h x A$49.91, plus 4.33 Saturdays x 2.25 h x A$74.86), before payroll tax. The rates are Theodore's.
- Keep 09:00 and add a named phone contact plus the lab's written escalation line (Catherine r16, G16 section 3).

## 4. Every role, weekly hours and corrected weekly cost

Method: repo daily rates from CRM (AM weekday A$2,195.94 for the full roster, Saturday x 1.5; PM 4 roles at the 3 hour casual floor and A$37.155 blended; PM Saturday A$668.78; venue manager A$40 an hour). Loaded = wages x 1.137 (12 percent super plus 1.7 percent workers comp, the repo convention). "Full roster" means 18 clients booked. Adaptive days cost less (end of this section).

| Role | Heads on full roster | Weekly hours (all heads) | Weekly wages | Weekly loaded | Basis |
|---|---|---|---|---|---|
| Venue manager | 1 | 42.5 (Mon to Fri 06:30 to 15:00; repo 40.0) | A$1,700.00 (repo A$1,600.00) | A$1,932.90 | CRM, A$40 an hour |
| AM massage and beauty therapists | 4 | 144 (6 h x 6 days x 4) | A$5,850.00 incl. Saturday | A$6,651.45 | CRM A$37.50 |
| AM nail technicians | 2 | 72 | A$2,871.18 incl. Saturday | A$3,264.53 | CRM A$36.81 |
| AM hairdressers | 2 | 72 | A$2,871.18 incl. Saturday | A$3,264.53 | CRM A$36.81 |
| Phlebotomists | 2 (1 on mornings of 9 or fewer) | 72 (36 with one) | A$2,681.25 incl. Saturday | A$3,048.58 | CRM A$34.375 |
| PM casual therapists | 4 | 60 weekday + 12 Saturday = 72 | A$2,898.08 | A$3,295.12 | CRM, 3 hour floor |
| Senior staff cover (afternoon, Saturday) | 0 extra, one of the above | inside the hours above | no loading in repo | not in repo | Anthony 2026-10-24 |
| Midwife A | 1 | 22.5 | Theodore rate | A$1,122.98 | A$49.91 x 7.5 x 3 |
| Midwife B | 1 | 22.5 | Theodore rate | A$1,310.10 | A$49.91 x 7.5 x 2 plus A$74.86 x 7.5 |
| Casual relief pool | budget line | as needed | | A$15,000 a year in the repo | CS line 136 |

Repo roles total: weekly wages A$18,871.69, weekly loaded A$21,457.11. Midwives add A$2,433.08 a week loaded. Midwife inputs are Theodore's (R15, restated in T16 section G): Nurses Award registered nurse level 2 pay point 4, A$41.59 an hour, times on-cost 1.20 = A$49.91 weekday and A$74.86 Saturday (150 percent). The award class and the uplift after 1 July 2025 are unconfirmed (T15 section 4.1) and not verified by an accountant.

Adaptive saving not in the full-roster figures: a morning with 1 phlebotomist and 4 therapists (2 massage and beauty, 1 nails, 1 hair) costs A$1,097.97 less in wages than the full roster (my arithmetic on CRM rates).

## 5. Corrected monthly cost (22 weekdays and 4.33 Saturdays, repo convention)

| Line | Per month |
|---|---|
| Repo payroll, Table 1, loaded (CRM unchanged) | A$93,595.63 |
| Venue manager 06:30 start (0.5 h x 22 x A$40, loaded) | plus A$500.28 |
| Receptionist, welcome or greeter role | A$0.00 (the repo had no cost line; Theodore's R15 add of A$12,166.54 is removed) |
| Two midwives, Monday to Saturday, 45 paid hours a week | plus A$10,665.96 |
| **Corrected payroll** | **A$104,761.87** |
| Net before payroll tax (repo net A$35,186.40) | A$24,020.16 |
| Extra payroll tax on the new wages (Theodore's approximation, A$63.46 per A$1,000) | about A$632.14 |
| Net after that tax | about A$23,388.02 |

Cost change: payroll up A$11,166.24 a month (A$500.28 plus A$10,665.96); net down by the same amount before payroll tax. This matches G16's "1 midwife Monday to Saturday, or two part-timers sharing the six days". Two midwives each on every day is a different, costlier model (A$21,331.93 a month) and is not the locked roster.

Not in this number: midwife consult income (T16 section G models A$18,315 a month for one midwife's consult clients; a different question); the A$562 repo payroll tax base (not in the repo net); leave loading for permanent staff. If the midwives are permanent with leave cover (on-cost 1.366 instead of 1.20, T16 sensitivity) the midwife line is about A$12,141 a month by simple scaling (my arithmetic, not Theodore's output). Break-even (7.250 clients a day, CS line 31) is not recomputed because the repo solver has no midwife input; it rises by the extra fixed cost.

## 6. Roles the repo has that Anthony's note no longer includes (listed, not deleted)

| Repo item | Where | Status |
|---|---|---|
| Receptionist and manager, split shift 07:00 to 12:00 and 15:00 to 18:00 | SP line 70; CS section 4 headcount row | No cost line in the model; the locked roster gives the job to the venue manager and the afternoon senior staff member |
| Dedicated PM reception (position 06, RCO01) | removed 2026-08-21 (CS) | Already removed |
| Separate welcome or greeter role added in Round 15 | Grace R15 and Theodore R15 (A$12,166.54 a month) | Not in the locked roster; delete from any model that uses it |
| Venue manager Monday to Saturday | SPR VM01 | Stale; Monday to Friday since 2026-09-19 |
| Relief positions: phlebotomists PHL03 and PHL04, massage and beauty MB05 and MB06, nails NAIL03, hair HAIR03 | SPR | Recommended pool, not simultaneous; only the A$15,000 a year relief line is costed |
| Fixed minimum of 2 phlebotomists | CS section 4 headcount row | Superseded by the adaptive rule (CS section 00, item 6) |
| 3D scan operator, dietitian, subtenants | SP banners | Already removed |

## 7. Open items for Anthony

1. Approve the A and B grid, or the fortnightly Saturday swap.
2. 06:45 start: shift, extend, or phone contact (section 3).
3. Venue manager 06:30 versus repo 07:00.
4. Package 1 content and the two price sets (section 2, lines 2 and 3).
5. Pay loading for the senior staff member (not in repo).
6. A relief midwife and a named deputy for the venue manager (neither in repo).
