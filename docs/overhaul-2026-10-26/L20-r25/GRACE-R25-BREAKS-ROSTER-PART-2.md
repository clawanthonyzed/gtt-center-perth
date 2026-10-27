# GRACE R25: Adaptive break grids (time grids only, no floor plans)

Author: Grace. Date: 2026-10-27. DRAFT for Anthony. Nothing is sent. Part 1: GRACE-R25-BREAKS-ROSTER.md.

## READ-FIRST CHECK (GTT-READ-FIRST.md, 2026-10-27)
- Venue manager: hired, starts 06:30 (Mon to Fri 06:30 to 15:00). 07:00 is the first draw. Anthony is owner and director, 0 operational hours.
- Path A = PREFERRED, package WITH the GTT midwife consult. Path B = NOT preferred, outside referral, no GTT consult, no limit on Path B.
- Prices: Path A A$320 / A$370, Path B A$300 / A$350, all including the A$27.85 lab fee (R).
- Rebates used: consult A$32.95 + lab A$22.05 = about A$55.00 (R).
- Midwives 08:00 to 16:00, first consult 08:15.
- Late rule: blood draws have no wiggle room; consults have a 10 minute grace window.
Tags: R repo, E estimate.

## 1. How the morning grid was built
Service blocks come from Table 1 (docs/scenario-c-sync-timetables.md section 0.6a, R): 9 pairs 25 minutes apart from 07:00, services 45 minutes, so the odd client gets massage then beauty, the even client nails then hair. Peak need is 4 massage and beauty, 2 nails, 2 hair. I treated each break as a job that cannot overlap that person's services, and checked by script that every service is still covered (throwaway check, not a new calculator). Planning rule (E, not an award term): lunch starts between 10:00 and 12:00 (hour 3 to 5), so it begins inside the first 5 hours. The service blocks already include set-up and clean (45 minutes, R).

## 2. Morning shift, 8 service staff, 07:00 to 13:00 (E)
S = services (first to last, back to back with 5 minute gaps).
| Staff | Rest 10 min (paid) | Services | Lunch 30 min (unpaid) | Free after |
|---|---|---|---|---|
| Pool 1 (massage/beauty) | 07:35 | 07:55 to 11:10 | 11:10 to 11:40 | 11:40 |
| Pool 2 | 07:55 | 07:05 to 07:50, 08:20 to 10:45, 11:25 to 12:10 | 10:45 to 11:15 | 12:10 |
| Pool 3 | 07:40 | 08:05 to 11:20 | 11:20 to 11:50 | 11:50 |
| Pool 4 | 08:15 | 07:30 to 08:15, 08:30 to 11:45 | 11:45 to 12:15 | 12:15 |
| Nails 1 | 07:15 | 07:30 to 10:45 | 10:45 to 11:15 | 11:15 |
| Nails 2 | 11:10 | 07:05 to 11:10 | 11:20 to 11:50 | 11:50 |
| Hair 1 | 07:45 | 08:05 to 11:20 | 11:20 to 11:50 (see note) | 11:50 |
| Hair 2 | 08:05 | 08:30 to 11:45 | 11:45 to 12:15 | 12:15 |
Rest sits in the longer work period before lunch (MA000005 cl 16.1). Staff 3 and 4 and the hair pair are not needed until 08:05 to 08:30, which is why their rests fall early; they use that time for set-up.
**Hair note.** The two stylists are booked back to back from 08:30 to 11:45 (gaps are 5 minutes), so Hair 1's lunch only works if Nails 1 (free from 11:15) takes the 11:25 to 12:10 hair service. That needs a nail technician who also cuts and styles hair; repo says hair plus nails dual hires are "preferred where found, not assumed" (docs/dual-role-staffing-model-2026-07-28.md). If not: Hair 1 lunches 12:10 to 12:40, which is 5 hours 10 minutes in. Catherine confirms whether the award wants the break to start before 5 hours.

**Everyone else, same morning**
| Person | Break | Cover |
|---|---|---|
| Phlebotomists (both, draws are simultaneous) | Paid 10 minute tea break 11:35 to 11:45 (draws 11:30 to 11:35 are in the centrifuge, next draw 11:55). No 30 minute gap exists (longest 20 minutes), so the meal break is forgone with written consent (shift 5 h 55 m) | Draws untouched |
| Midwife | 12:30 to 13:00, diary blocked, never recalled. Consults run 08:15 to 10:30, then normal bookings | Venue manager per incident steps |
| Venue manager | 11:45 to 12:15 (E; her award NOT IN REPO). Last arrival 10:10, departures about 10:53, 11:15, 11:40, 12:05, 12:33 | Pool 1, free from 11:40, covers the desk for the 12:05 departure |

Coverage check: draws are done by phlebotomists, not service staff. Every service from 07:05 to 12:10 has a person; at most 2 of 8 are away on a break at the same time, and never during a booked service of their own. Front desk: venue manager covers all arrivals; no arrivals after 10:10.

## 3. Afternoon shift, 4 service slots (E)
Afternoon hours are NOT FIXED: the ops model has reception 13:00 to 18:00 (R), the older roster has service staff 12:00 to 18:00 (R, docs/pm-staffing-roster.md), and the staff floor is 3 hours. Rules by length: under 4 hours no rest; 4 to 5 hours one paid rest only; over 5 hours one rest plus the 30 minute lunch.
Grid for 12:00 to 18:00 (6 hours). Never more than 1 of 4 away at once:
| Slot | Rest 10 min | Lunch 30 min |
|---|---|---|
| 1 | 12:45 | 14:30 to 15:00 |
| 2 | 13:15 | 15:00 to 15:30 |
| 3 | 13:45 | 15:30 to 16:00 |
| 4 | 14:15 | 16:00 to 16:30 |
For a 13:00 to 18:00 shift (5 hours, no lunch entitlement) use the rests only, moved 45 minutes later. Adapt: if a booking sits on a slot, swap two staff; lunch must start by hour 5 (17:00 on a 12:00 start). PM reception (13:00 to 18:00, R) holds the desk; the venue manager is there until 15:00.

## QUESTIONS FOR ANTHONY
1. Afternoon hours: 12:00 to 18:00 or 13:00 to 18:00? Recommendation: 13:00 to 18:00 (matches reception, no unpaid lunch to arrange), if demand allows.

Regards.
Grace
