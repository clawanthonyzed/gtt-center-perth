# GRACE R23 Review of the 28 overnight drafts (R22-01 to R22-26)

Author: Grace. Date: 2026-10-27. Read-only review of /opt/openclaw/second-brain/overnight/gtt-r22-*/. No server file edited, nothing queued.

## READ-FIRST CHECK (from GTT-READ-FIRST.md, 2026-10-27)
- Venue manager: hired (a different person from Anthony), starts 06:30, Mon to Fri 06:30 to 15:00. 07:00 is the first draw.
- Path A = PREFERRED (package WITH the GTT midwife consult). Path B = NOT preferred (outside referral, no GTT consult).
- Prices: Path A A$320 / A$370 (GTT charges A$292.15 / A$342.15). Path B A$300 / A$350 (GTT charges A$272.15 / A$322.15).
- Rebates: consult A$32.95 + lab A$22.05 = about A$55.00.
- Midwives 08:00 to 16:00, first consult 08:15, 25 minute blocks to 10:30.
- Late rule: arrive 10 minutes early; late is the appointment time onwards; no wiggle room.

## Count check
28 queued. 25 files exist (R22-03, 06 and 09 each have two parts). 23 landed; R22-13 and R22-14 have files but were flagged failed; R22-18, 21, 22 have no file. Numbers 05, 27, 28 are not on the server. Characters = file size in bytes (curly quotes count as 3, so true length is a little less).

## Table
| Draft | Chars | Quality | Breaks a Round 23 lock? |
|---|---|---|---|
| R22-01 lab questions, term sheet | 3533 | usable | No. Term 5 (eight weeks) clashes with the 28 day rule; only 10 of 12 terms. Small patch |
| R22-02 GP survey, waitlist test plan | 2724 | thin | Yes: waitlist plan has no "inside 48 hours list AND public" rule and lists it as open |
| R22-03 p1 midwife screening, interview | 2587 | thin | Yes: midwife picks her own break time (twice); Fair Work now answered |
| R22-03 p2 position description, contract | 2897 | thin | Yes: break "chosen by the midwife on the day"; everything is "lawyer to check" |
| R22-04 role descriptions, roster | 3463 | thin | Yes: no meal breaks, no casual midwife, many NOT IN REPO |
| R22-06 p1 booking flow | 2469 | usable | No. Price table correct; nine pairs 07:00 to 10:20 correct |
| R22-06 p2 consent text | 2788 | usable | Yes (minor): "up to 10 minutes late we will still see you" reads as no-wiggle-room breach |
| R22-07 test morning procedure | 4202 | usable | Minor: consult grace left OPEN; clinical rules assumed. Patch only |
| R22-08 results line patch | 3612 | wrong | Yes: invents "log in to view"; no voicemail then email steps |
| R22-09 p1 architect brief changes | 3637 | usable | Minor: midwife break "chosen on the day"; no staff off-duty break space |
| R22-09 p2 consult room, spa feel | 2057 | usable | No |
| R22-10 licence, consumer law, lease | 3516 | thin | Placeholders left ({licence_fee}, {tenant_entity}); not a lock break |
| R22-11 payroll tax, workers comp sheet | 2086 | thin | No. Copies P&L lines; no payroll scenarios |
| R22-12 welcome card | 2707 | wrong | Yes: no food/drink line, no stand-alone service line; venue manager "Anthony or paid hire (OPEN)" |
| R22-13 booking terms (flagged failed) | 3111 | thin | Yes (minor): late grace in the terms; contact left blank |
| R22-14 waitlist emails (flagged failed) | 3008 | usable | Gap: no inside-48-hour "also public" variant |
| R22-15 reminders | 3025 | thin | Yes: says the consult is before the draw on test day; locked norm is 1 to 28 days before |
| R22-16 abnormal results messages | 2919 | usable | Yes (minor): email omits "regarding results"; extra text step. Use Part 2 Rule 6 wording |
| R22-17 day-before print checklist | 1544 | wrong | Broken layout, incomplete |
| R22-18 client FAQ (failed) | 0 | no file | Missing |
| R22-19 opening, closing checklists | 1589 | wrong | Yes: "midwife's chosen meal break"; closing at 18:00 after a 15:00 shift |
| R22-20 staff induction | 837 | thin | Only a list of headings; "{your_name}" placeholder; says "release to clients" |
| R22-21 test morning run sheet (failed) | 0 | no file | Missing |
| R22-22 records vendor questions (failed) | 0 | no file | Missing |
| R22-23 Path B notice set | 1979 | wrong | Garbled wording, misleading Medicare line; "NOT IN REPO" left in copy |
| R22-24 venue manager decision guide | 1712 | wrong | Names Grace as decider; one table row only |
| R22-25 midwife pre-start, consult note | 1646 | thin | Names Grace as checker; no CPR or police check |
| R22-26 staff privacy one-pager | 850 | thin | No content, only a description |

## Counts (28 rows)
- usable: 8 (R22-01, 06p1, 06p2, 07, 09p1, 09p2, 14, 16). Most need only a small patch; 06p2, 09 and 14 are still rebuilt (late line, staff break space, failed flag).
- thin: 11 (R22-02, 03p1, 03p2, 04, 10, 11, 13, 15, 20, 25, 26).
- wrong: 6 (R22-08, 12, 17, 19, 23, 24).
- missing: 3 (R22-18, 21, 22). Total 28.
- Conflict with a Round 23 lock: 14 (R22-02, 03p1, 03p2, 04, 06p2, 08, 09p1, 12, 13, 15, 16, 19, 24, 25).
- Pension or ramp content: none found. Anthony named in the venue manager job: only R22-12 ("Anthony or paid hire"). Venue manager at 07:00: none (R22-07 and R22-19 use 06:30). The bare word for a parent: none found.

## Needs an overnight rebuild: 22
R22-02, 03 (p1 and p2 as one job), 04, 06 p2, 08, 09 (both parts as one job), 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26. Job specs: [REBUILD-SPECS.txt](REBUILD-SPECS.txt). Not rebuilt (patch by hand): R22-01 term 5, R22-07 consult line, R22-16 email wording (Part 2 Rule 6 has the fix), R22-06 p1, R22-09 p2.

## QUESTIONS FOR ANTHONY
None needed for this review.

Regards.
