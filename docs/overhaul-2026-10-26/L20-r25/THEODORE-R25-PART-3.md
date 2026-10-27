# THEODORE R25 PART 3: Unified staff pool and phlebotomist hours, cost check

Theodore, financial consultant, 2026-10-27. Numbers from [theodore_r22.py](../L17-r22/theodore_r22.py) Round 25 block (re-run; headline asserted unchanged) and Grace's [GRACE-R25-PHLEBOTOMIST.md](GRACE-R25-PHLEBOTOMIST.md). Nothing sent. Tags: R repo, V verified, E estimate.

## READ-FIRST CHECK
- Venue manager starts 06:30 (Mon to Fri 06:30 to 15:00); 07:00 is the first draw. A hired person, not Anthony.
- Path A = PREFERRED, package with the GTT midwife consult. Path B = NOT preferred, outside referral, no GTT consult, not limited.
- Prices: Path A A$320 / A$370 (GTT charges A$292.15 / A$342.15). Path B A$300 / A$350 all in (GTT charges A$272.15 / A$322.15).  <!-- factcheck:ok -->
- Rebates: consult A$32.95 + lab A$22.05 = about A$55.00.
- Midwives 08:00 to 16:00, first consult 08:15.
- Late rule: blood draws no wiggle room; consults 10 minute grace.

## 1. Answer first
**The locked costs already match.** The phlebotomist shift derived from the repo is 07:00 to 12:55 (5 hours 55 minutes). The profit model pays 07:00 to 13:00 (6 hours). Morning service staff are also inside their costed 07:00 to 13:00. No change to the headline A$26,631.97 before tax / A$19,973.98 after.

## 2. Phlebotomists (2, employed by GTT Medical)
| Step | Time | Source |
|---|---|---|
| Last pair, first draw | 10:20 (07:00 + 8 x 25 minutes) | R, docs/CURRENT-STATE.md and scenario-c-sync-timetables.md Table 1 |
| Last second draw (60 minutes after) | 11:20 to 11:25 | R, Table 1 |
| Last third draw (120 minutes after) | 12:20 to 12:25 | R, Table 1 |
| Paperwork and close-down (bag, label, dispatch log, clean room) | 30 minutes, to 12:55 | R, operations-manual.md close block (30 minutes); E that it fits the final batch |
| **Derived finish** | **12:55** (5.92 h) | Same as Grace |
| Costed in the model | 07:00 to 13:00 = 6 h, A$34.375 an hour weekday, A$51.5625 Saturday | R, tools/cost_ramp_model.py |
| Spare | 5 minutes a day | maths |

The repo's tools/draw-event-scheduler.py uses the older draw timing (second draw at 75 minutes, third at 135); Grace ran it and it does not reproduce the locked 18-client table, so Table 1 is the source (R).

Cost lines (2 phlebotomists, R): wages A$11,754.19 a month, A$13,364.52 with super and workers comp.

**What-ifs only (not applied; the locked headline stays):**

| Case | Extra cost a month (wages, super, workers comp, payroll tax) | Profit before tax | After 25% tax |
|---|---|---|---|
| Locked: 07:00 to 13:00 | A$0.00 | A$26,631.97 | A$19,973.98 |
| Paid only to 12:55 | -A$197.22 (a saving) | A$26,829.19 | A$20,121.89 |
| Last third draw runs 10 minutes late (finish 13:05) | +A$197.22 | A$26,434.75 | A$19,826.06 |
| 15 minutes setup from 06:45 (Grace's open question) | +A$591.66 | A$26,040.31 | A$19,530.23 |

Two notes. (1) Under the health professionals award, a shift of no more than 6 hours lets the phlebotomist skip the unpaid meal break with the employer's consent (V, MA000027 cl 15.1(c), via [GRACE-R24-BREAK-THRESHOLDS.md](../L19-r24/GRACE-R24-BREAK-THRESHOLDS.md)). Any shift past 6 hours (the 13:05 or 06:45 cases) brings back a 30 minute break, which the draw timetable has no gap for. That is a reason to keep the roster at 07:00 to 13:00. (2) Paying only to 12:55 saves A$197 a month but leaves no buffer; I recommend keeping 13:00 (agrees with Grace).

## 3. Morning service staff and afternoon casuals
| Group | Costed (R) | Derived from Table 1 | Match |
|---|---|---|---|
| 8 morning service staff | 07:00 to 13:00, 6 h, weekday A$39,235.68 a month, Saturday at 150% | Last service ends 12:10 (clients 17 and 18); room strip and restock 30 minutes to about 12:40 (R close block, E fit) | Yes, inside 13:00 |
| 4 afternoon casuals | 3 hour minimum engagement floor | Afternoon sales volume (R, Model E) | Yes, unchanged |

The 30 minute lunch where the award gives one and the paid 10 minute rest break: the rest break is paid time already inside the 6 hours, so no cost change. How the unpaid lunch interacts with the 07:00 to 13:00 paid hours is part of the shift-length review Anthony deferred; the model keeps paying 6 hours until then.

## 4. What the unified pool means for the model
- **Same cost.** The model costs by rostered hours and headcount, not by labels: 8 morning places and 4 afternoon places a day (R). Calling them one pool and rostering each person to either shift changes no figure.
- **Rates.** The repo prices every service staff hour at the casual rate (the 25% casual loading is inside the hourly rates in tools/cost_ramp_model.py, R), with Saturday at 150%.
- **Casual versus permanent mix: NOT IN REPO.** A permanent part-time person costs less an hour (no 25% casual loading) but earns paid annual and personal leave and annual leave loading, and needs cover when away. The net effect depends on the mix, which is not decided. Until it is, the all-casual costing stays.
- **One shift a day per person.** If someone works the morning and the afternoon on the same day, broken-shift and overtime rules can apply: NOT IN REPO. The lock says "either morning or afternoon", so the roster keeps one shift per person per day and the cost stays as modelled.
- **Upside:** one pool makes sick-day cover easier (a morning person can pick up an afternoon), which can reduce the replacement cost the repo already allows for (R, cost_ramp_model.py absence allowance). Not counted.

## QUESTIONS FOR ANTHONY
None from me. Grace's two questions (roster 13:00 or 12:55; setup before 07:00) are in her file; the costs for both are in section 2 above.

Regards.
Theodore
