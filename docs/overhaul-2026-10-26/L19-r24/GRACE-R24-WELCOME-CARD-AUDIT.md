# GRACE R24 Welcome card audit: is every earlier element still saved?

Author: Grace. Date: 2026-10-27. DRAFT for Anthony. Nothing is sent.

## READ-FIRST CHECK (from GTT-READ-FIRST.md, 2026-10-27)
- Venue manager: hired, starts 06:30, Mon to Fri 06:30 to 15:00. First draw 07:00. Anthony is not the venue manager. <!-- factcheck:ok -->
- Path A = PREFERRED (package WITH the GTT midwife consult). Path B = NOT preferred (outside referral, no GTT consult) and not limited.
- Prices: Path A A$320 / A$370, Path B A$300 / A$350, lab fee A$27.85 included. (R)
- Rebates used: consult A$32.95 + lab A$22.05 = about A$55.00. (R)
- Midwives 08:00 to 16:00, first consult 08:15.
- Late rule: draws no wiggle room; consults 10 minute grace window.

## Short answer
No. The Round 22 card detail was NOT all saved next to the Round 23 locks. Of 25 elements checked: 4 intact, 17 lost from at least one current locked file, 4 changed. Nothing is gone from the repo (the Round 22 and Catherine files still hold everything), but the files staff and agents actually read (GTT-READ-FIRST.md, the preamble, the operations manual, Round 23 Rule 5) each held only part. All 17 are now restored in one master definition: docs/operations-manual.md section 9, "Welcome card master definition".

## How to read the table
Y = present, n = absent. Columns are the files as they stood BEFORE this round's fixes. RF = GTT-READ-FIRST.md. PRE = playbooks/GTT-LOCKED-FACTS-PREAMBLE.md (@welcome). OM = docs/operations-manual.md. R23 = L18-r23 GRACE-R23-OPERATIONS-LOCK-IN-PART-2.md rule 5. R22 = L17-r22 GRACE-R22-PART-4.md. CAT = Catherine R22A-PART-3 and R22B-PART-6. SRV = server draft /opt/openclaw/second-brain/overnight/gtt-r22-12-welcome-card-final-copy/ (checked by ssh). Intact = in all four of RF, PRE, OM, R23.

L15-r20 and L16-r21 hold no welcome card definition. They only mention the venue manager welcoming clients (reception duty) and an arrival message step, so they cannot have lost anything.

| # | Element | First defined | RF | PRE | OM | R23 | R22 | CAT | SRV | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | A5 card, front and back | R22 | n | Y | n | n | Y | n | Y | lost |
| 2 | Welcome and first name, her date, "keep this card" line | R22 | n | Y | n | Y | Y | Y | Y | lost |
| 3 | Timetable of draws and services with times | R22 | Y | Y | n | Y | Y | Y | Y | lost |
| 4 | Staff names for the draw and each service | R22 | Y | Y | n | Y | Y | Y | Y | lost |
| 5 | Midwife row for a same-morning consult | R22 | n | n | n | n | Y | Y | Y | lost |
| 6 | Pre-purchased food or drink listed | R23 | Y | Y | Y | Y | n | n | n | intact |
| 7 | Availability note when nothing pre-purchased | R23 | Y | Y | Y | Y | n | n | n | intact |
| 8 | Stand-alone service after last draw: what, staff name, time | R23 | Y | Y | Y | Y | n | n | n | intact |
| 9 | Late sentence on the card, word for word | R22 | n | Y | n | Y | Y | n | Y | lost |
| 10 | Venue manager name line ("Ask {name} at the front desk if anything changes") | R22 | n | n | n | part | Y | n | Y | changed |
| 11 | Thank-you line | R22 | n | Y | n | n | Y | n | Y | lost |
| 12 | Social media (handles NOT IN REPO) | R22 | Y | Y | n | Y | Y | n | Y | lost |
| 13 | Google review request | R22 | Y | Y | old | Y | Y | Y | Y | changed |
| 14 | Review is neutral, no reward | R22 | n | Y | n | Y | Y | Y | Y | lost |
| 15 | Never-on-card list (price, rebate, result, due date, path, health detail) | R22 | n | Y | n | n | Y | Y | n | lost |
| 16 | Staff first names only, with written agreement in contract | CAT R22B-6 | n | part | n | n | part | Y | n | lost |
| 17 | Venue manager prints cards and day list the day before | R22 | Y | Y | Y | Y | Y | n | n | intact |
| 18 | Print run checks: 48 hour cutoff, work printer, same order, count, check, closed folder, reprint errors | R22 | n | n | n | n | Y | Y | n | lost |
| 19 | Day list contents (first name, surname initial, Draw 1 time, staff names) | R22 | n | Y | n | n | Y | Y | n | lost |
| 20 | Day list kept in locked drawer, shredded at end of test day | R22 | n | Y | n | n | Y | Y | n | lost |
| 21 | Shred log (date, printed, shredded, initials) and missing list = possible breach | R22 / CAT | n | n | n | n | Y | Y | n | lost |
| 22 | Roster change on the morning (before 06:45 reprint; after, reprint at desk, no handwriting) | R22 | n | n | n | n | Y | n | n | lost |
| 23 | Reply to reviews: neutral thank-you, never confirm she was a client | CAT R22B-6 | n | n | n | n | n | Y | n | lost |
| 24 | Venue manager source on card: SRV says "Anthony or paid hire (OPEN)" | SRV | n/a | n/a | n/a | n/a | n/a | n/a | Y | changed |
| 25 | Consult grace on the draft card: SRV says "OPEN, Catherine prefers fixed 10" | SRV | n/a | n/a | n/a | n/a | n/a | n/a | Y | changed |

Reasons for "changed": row 10, Round 23 kept only a food-row version ("Ask {venue_manager_first_name}") and dropped the bottom-of-card line. Row 13, the old OM text (welcome pack with a separate "QR code card (Google review)") described a different thing from the card's back-side invitation; replaced. Rows 24 and 25 are stale text in the server draft, which was written before Round 23 and Round 24 (Anthony is not the venue manager; consult grace is now locked at 10 minutes). The server draft was left untouched as history; the manual is the current copy. <!-- factcheck:ok -->

## What I restored (edits made)
| File | Change |
|---|---|
| docs/operations-manual.md section 9 | New "Welcome card master definition" holding all 25 elements (format, front, timetable, midwife row, food and drink, stand-alone service, late sentence, venue manager line, back, never-on-card, staff names, day list contents and handling, shredding and log, morning changes, review replies) |
| docs/operations-manual.md section 1 | Old receptionist "welcome pack with QR code card" line replaced with a pointer to section 9 |
| docs/GTT-READ-FIRST.md | Welcome card bullet rewritten with every element and a pointer to the manual master |
| playbooks/GTT-LOCKED-FACTS-PREAMBLE.md (@welcome) | Added venue manager line, midwife row, first names only; added pointer to the manual; shredding now says every copy and unused card plus a log |
| L18-r23 GRACE-R23-OPERATIONS-LOCK-IN-PART-2.md rule 5 | Pointer to the master added |
| L17-r22 GRACE-R22-PART-4.md | History banner pointing to the master |

## Still not in the repo (honest list)
- Social media handles: NOT IN REPO.
- Brand name on the card: on hold, stays a merge field.
- Whether the Google review wording passes Ahpra advertising limits: lawyer to check (Catherine R22A).
- The server draft in /opt/openclaw/second-brain/overnight/ is unchanged and stale; do not use it.

## QUESTIONS FOR ANTHONY
None needed.

Regards.
Grace
