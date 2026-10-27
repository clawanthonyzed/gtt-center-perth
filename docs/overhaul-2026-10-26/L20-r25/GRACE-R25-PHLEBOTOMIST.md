# GRACE R25: Phlebotomist shift, derived from the repo

Author: Grace. Date: 2026-10-27. DRAFT for Anthony. Nothing is sent. Theodore cost-checks section 5.

## READ-FIRST CHECK (GTT-READ-FIRST.md, 2026-10-27)
- Venue manager: hired, starts 06:30 (Mon to Fri 06:30 to 15:00). 07:00 is the first draw. Anthony is owner and director, 0 operational hours.
- Path A = PREFERRED, package WITH the GTT midwife consult. Path B = NOT preferred, client keeps an outside referral, no GTT consult, no limit on Path B.
- Prices: Path A A$320 / A$370, Path B A$300 / A$350, all including the A$27.85 lab fee (R).
- Rebates used: consult A$32.95 + lab A$22.05 = about A$55.00 (R).
- Midwives 08:00 to 16:00, first consult 08:15.
- Late rule: blood draws have no wiggle room; consults have a 10 minute grace window.
Tags: R repo, V verified source, E estimate, U unverified.

## 1. Answer first
The phlebotomist finishes at **12:55** and works **5 hours 55 minutes (5.92 h)**, 07:00 to 12:55 (E for the paperwork part, R for the draws). Both phlebotomists finish together. The old "5 hour" figure is wrong. The repo's costed 07:00 to 13:00 (6 hours) is right, with 5 minutes spare.

## 2. Which schedule (and why the old tool is not used as is)
The locked schedule is Table 1 in docs/scenario-c-sync-timetables.md section 0.6a, shown again in docs/architecture/OPERATING-MODEL-18-CLIENTS.md section 2 (R): 9 pairs, 25 minutes apart from 07:00, Draw 2 exactly 60 minutes and Draw 3 exactly 120 minutes after Draw 1, every draw 5 minutes, two chairs.

tools/draw-event-scheduler.py is the OLDER model (Draw 2 at 75 minutes plus or minus 5, Draw 3 at 135 plus or minus 10, Draw 1 of 15 minutes). I ran it: it admits 10 clients in the 10:05 window and 16 in the 11:00 window, not 18, so it is out of date for the locked schedule. I did not write a new calculator. I checked Table 1 with a short throwaway script: 27 draws per phlebotomist, zero overlaps. A 15 minute Draw 1 would collide (a Draw 2 and a Draw 1 overlap from the second pair on), so Draw 1 stays at 5 minutes as in Table 1.

## 3. The exact timeline (each phlebotomist: one chair, 9 clients, 27 draws)
| Step | Time | Tag |
|---|---|---|
| First Draw 1 (pair 1) | 07:00 | R locked |
| Pair first draws | 07:00, 07:25, 07:50, 08:15, 08:40, 09:05, 09:30, 09:55, 10:20 | R |
| Last pair first draw (pair 9, clients 17 and 18) | 10:20 | R |
| Last Draw 2 | 11:20 to 11:25 | R |
| Last Draw 3 | 12:20 to 12:25 | R |
| Last tubes into the centrifuge (within 10 minutes of the draw) | by 12:35, ideally 12:25 | R, docs/pathology-collection-room.md |
| Spin (10 minutes, mandatory per the repo) | ends 12:35 if loaded at 12:25 | R, docs/am-capacity-weekend.md |
| Paperwork and close-down: bag and label, cool pack, dispatch log, clean and pack the collection room | 12:25 to 12:55 (30 minutes) | E, see below |
| **Finish** | **12:55** | E |

Paperwork allowance: the repo gives no minutes for the final batch alone. The closest documented value is the 30 minute close block in docs/operations-manual.md section 1 ("12:00 to 12:30: dispatch final specimens, clean and pack collection room, complete logs"). I use 30 minutes, tag E. The spin runs inside those 30 minutes, so it does not add time.

## 4. Workload and sharing
- The two phlebotomists do not share draws. Chair A takes the odd clients, Chair B the even clients, at the same clock times (R).
- Each: 27 draws x 5 minutes = 135 minutes of drawing in a 355 minute shift (38 percent). The longest gap between draws is 20 minutes (07:05 to 07:25, 07:30 to 07:50, 11:35 to 11:55, 12:00 to 12:20).
- Both finish 12:55. With 9 or fewer clients, 1 phlebotomist works (R, Center of Truth); the same clock logic applies.

## 5. Old "5 hour" figure versus the derived shift (for Theodore)
| Figure | Where | Verdict |
|---|---|---|
| 5 hours (07:30 to 12:30) | docs/pm-staffing-roster.md, docs/capacity-pricing-audit.md | WRONG. Ends before the last Draw 3 is even finished at 12:25 plus paperwork. Older 08:00 first-patient era |
| 5.5 hours | docs/am-capacity-weekend.md (10 client model) | WRONG for 18 clients. Ends 12:30 |
| 6 hours (07:00 to 13:00) | Center of Truth, OPERATING-MODEL-18-CLIENTS.md section 7 (R) | RIGHT as the costed shift. Derived 5.92 h is 5 minutes less |
Locked cost uses 6 hours each (wages A$11,754.19 a month for two, A$13,364.52 loaded, R). A 5 hour 55 minute paid shift would be 1.4 percent lower, about A$186 a month loaded before Saturday loading (E, my arithmetic: 5/360 x A$13,364.52). Recommendation: keep 07:00 to 13:00 on the roster and in the cost; plan the finish at 12:55.

## 6. Problems found (not answers invented)
1. **Setup before 07:00.** docs/operations-manual.md still says the phlebotomist arrives 07:15 (older 08:00 era, out of date). The locked start is 07:00 = first draw. Checklist time (room, labels, fridge, drink out at room temperature 20 minutes) is NOT IN REPO.
2. **Courier cutoff.** The repo assumes a lab pickup around 12:30 (docs/am-capacity-weekend.md, never confirmed by the lab) and docs/gtt-clinical-protocol.md says "latest 11:30" (older). Last tubes are ready about 12:35 to 12:55. Nearest compliant fix: the lab confirms a latest pickup of 13:00, or a GTT drop-off by a staff member (docs/architecture/WDP-PARTNERSHIP-ACTIVATION-PLAN.md raises this).
3. **Meal break.** 5 hours 55 minutes is "no more than 6 hours", so MA000027 cl 15.1(c) lets the phlebotomist forgo the unpaid meal break with the employer's consent (V, awards.fairwork.gov.au/MA000027.html, 2026-10-27). No 30 minute gap exists between draws. Details: GRACE-R25-BREAKS-ROSTER.md.

## QUESTIONS FOR ANTHONY
1. Roster 07:00 to 13:00 (costed, 5 minutes spare, recommended) or 07:00 to 12:55? Recommendation: 07:00 to 13:00.
2. Add setup time before 07:00 for the phlebotomists? Options: (a) none, (b) 15 minutes at 06:45 paid. Recommendation: ask the lab first what its collection room opening checks take.

Regards.
Grace
