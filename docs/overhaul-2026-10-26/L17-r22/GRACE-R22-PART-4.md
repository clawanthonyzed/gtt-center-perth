# GRACE-R22-PART-4: Welcome card spec (words only, no drawings)

> ROUND 24 NOTE: this is the Round 22 history file. It has no food and drink line and no stand-alone service line (added Round 23). The single current definition is docs/operations-manual.md section 9, "Welcome card master definition". Where this file differs, the manual wins.

Author: Grace. Date: 2026-10-26 (Round 22). DRAFT for Anthony. Nothing was printed or sent. Tags: R repo, E estimate, U unverified. Review and privacy wording: Catherine A and B to confirm.

## READ-FIRST CHECK (from GTT-READ-FIRST.md, 2026-10-26)
- Venue manager start: 06:30 Mon to Fri (07:00 is the first draw).
- Path A = PREFERRED, package WITH the GTT midwife consult. Path B = NOT preferred, outside referral, no GTT consult. (My Round 21 files used the opposite labels: out of date.)
- Prices: Path A shown A$320 / A$370, GTT charges A$292.15 / A$342.15. Path B A$300 / A$350 all in.  <!-- factcheck:ok -->
- Rebates (planning, "about"): consult A$32.95 + lab A$22.05 = A$55.00.
- Midwives 08:00 to 16:00, first consult 08:15, 25 minute blocks.
- Late rule: "Please arrive at least 10 minutes before your appointment, because late means from your appointment time onwards and we cannot fit a first blood draw in after that."

## 1. What the card is
One card per client, printed by the venue manager the day before. A5 size, one side is the timetable, the other side is the thank-you and social media. It is handed to the client at the door. Draw times follow the repo timetable: Draw 1 at her time, Draw 2 exactly 60 minutes later, Draw 3 exactly 120 minutes later; services sit between the draws (R, scenario-c-sync-timetables.md).

## 2. Layout, top to bottom (front side)
1. Top line: the business name and "Welcome, [first name]". (Brand name is on hold, so the name is a merge field.)
2. Her date, and one line: "Please keep this card with you. It is your plan for the morning."
3. A timetable in rows, in time order. Each row has the time on the left, then what happens, then the name of the person: Arrive (10 minutes before); Draw 1 with [phlebotomist first name]; Service 1 with [practitioner first name and service]; Draw 2; Service 2; Draw 3; Finish. A midwife row appears only if she has a same-morning consult.
4. Under the table: the late rule sentence, word for word.
5. Bottom: "Ask [venue manager first name] at the front desk if anything changes."

## 3. Back side
1. A thank-you line in plain words.
2. Social media: "Find us on" followed by the handles (NOT IN REPO, no handles chosen yet).
3. Google review request: a neutral invitation with a short link or a code you scan. Draft: "If you would like to tell others about your visit, you can leave a Google review. There is no reward for a review and you are free to say what you like." (Catherine A: testimonial and advertising limits for a health service; do not offer gifts or discounts for reviews, do not choose or edit reviews, and keep the card about the lounge visit. Wording to be cleared.)
4. No price, no rebate, no result, no due date and no health detail anywhere on the card.

## 4. Data fields (from the booking system)
| Field | Source | On the card? |
|---|---|---|
| First name | booking | Yes |
| Test date and Draw 1 time | booking | Yes |
| Draw 2, Draw 3 times | calculated (+60, +120 minutes) | Yes |
| Phlebotomist first name | roster | Yes |
| Service 1 and 2 type, time, practitioner first name | booking and roster | Yes |
| Same-morning consult time | booking | Only if booked |
| Path (A or B) | booking | No |
| Due date, referral, notes | record | No, never |

## 5. The day before: print run (venue manager)
| Step | Check |
|---|---|
| 1 | Print after the booking cutoff for changes (48 hours, R) and again at the end of the shift for late bookings. Use the work printer only. |
| 2 | Print the client list (the "day list") and the cards in the same order, by Draw 1 time. |
| 3 | Count: cards printed equals clients on the list. Write the count on the list. |
| 4 | Check each card: first name, times, staff names match the roster. |
| 5 | Check spelling of first names against the booking. |
| 6 | Put the cards in time order in a closed folder. Keep the folder in the locked front desk drawer overnight. |
| 7 | Reprint any card with an error. Shred the wrong one. |

## 6. Privacy of the day list
The day list shows first name and surname initial, time and staff names only. It has no referral, no consult note, no due date, no path, no health detail (Catherine B to confirm that this is enough, because the business is a pregnancy testing service). The venue manager is not a GTT Medical employee, so the list is built from booking data only and never from the clinical record (R21, U). Keep the list in the locked drawer; staff who need it get a copy at the door; shred the list and any unused cards at the end of the test day with a signed one-line destruction log. Never leave a list on the front desk or a table.

## 7. If the roster changes on the morning
| Situation | What the venue manager does |
|---|---|
| A practitioner is sick or swapped | Open the roster before 06:45. Change the name in the system. Reprint only the affected cards. Shred the old ones. |
| Change after 06:45 | Tell the client at the door and write nothing by hand on the card; reprint at the desk before she sits. If the printer fails, say the name out loud and fix the card at the end of the service. |
| Draw time moves | Reprint, do not strike out. Tell the phlebotomist and the practitioners. |
| A client is late or no-show | Do not reprint. Follow the late rule (Part 3). |

## 8. Path B clients (outside referral) may email it in
1. On the Path B screen she can choose "Email my referral" or upload a photo. Recommended: the secure upload, with email as a backup, because plain email is not private (see question 1).
2. The email goes to a mailbox read only by GTT Medical staff (the midwife or phlebotomists), never the venue manager. Mailbox address: NOT IN REPO.
3. Subject she is asked to use: her booking number only, no health words.
4. Reply (automatic): "Thank you. We have received your document for booking [number]. Please also bring the original to your appointment. Regards."
5. The staff member files it to the test-day record (computer filing, R21) and ticks "outside request checked" on the morning.
6. On the morning the phlebotomist still checks it at the door. No suitable referral, no draw. She also signs the Medicare notice before the draw (Catherine B Part 5).

## QUESTIONS FOR ANTHONY
1. Path B referral: secure upload, plain email, or both?
   - A: Both, upload preferred. B: Email only. C: Upload only.
   - Recommendation: A.
2. Should the card show the midwife consult time (same-morning only)?
   - A: Yes. B: No, say it at the door.
   - Recommendation: A.

Regards.
Grace
