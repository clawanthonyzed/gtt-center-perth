# WORKFLOW-LOCKED-R19: consult first, test 1 to 28 days later

Author: Grace (Operations Manager, GTT Center Perth). Date: 2026-10-26 (Round 19). DRAFT for Anthony. Nothing was sent. All money in AUD. No new calculator was written; the only arithmetic is multiplication and division of numbers already in the repo (shown inline).

## 1. The Founder Rule (locked, never ask again)

> **Founder Rule, 2026-10-26 (Anthony).** The midwife consult happens 1 to 28 days BEFORE the test, on a different day from the test. The client needs the consult to get the referral. The client picks BOTH the consult slot and the test date and time at booking. The consult produces the referral (the pathology request). No consult, no test.

Written into: docs/DECISION-LOG.md (2026-10-26 entry), docs/CURRENT-STATE.md (section 000, item 25), outputs/OPERATIONS/CLINICAL-OPERATIONS-PLAN.md (section 13, item 25). Note: the file is at outputs/OPERATIONS/, not docs/; there is no docs/CLINICAL-OPERATIONS-PLAN.md.

This closes the open question in ROSTER-R18 section 5 ("when does the consult happen"). I should have read the sequence from "the client comes only for the GTT referral" (answer 5). The referral has to exist before the draw.

## 2. The client journey, step by step

Staff named are the repo's: the midwife and phlebotomists are employees of GTT Medical Services (Catherine R16); the lounge, therapists and venue manager sit in GTT Lounge Sanctuary. Money figures are Theodore R18 (Q2 and Q3 tables) for Package 1; Package 2 is A$50 more. Rebate figures use the repo's collection item 73928 until AskMBS answers.

| # | Step | Who does it | What happens | Money at this step |
|---|---|---|---|---|
| **BOOKING (online, day 0)** | | | | |
| 1 | Choose | Client (booking page) | Picks Package 1 or 2, then a **consult slot** and a **test date and time** in one booking. The engine only offers test dates 1 to 28 days after the consult slot (section 5). | None yet |
| 2 | Consents and details | Client | Name, mobile, email, due date, Medicare details as needed, accepts booking terms and privacy notice. | None |
| 3 | Pay | Client, GTT checkout | One checkout for GTT's part only. | Client pays **A$272.15** (Package 1) or A$322.15 (Package 2). Split by the checkout: **A$110.00 consult to GTT Medical** (GST-free), **A$162.15 lounge and service to GTT Lounge** (GST inside). Card fee about A$4.93 is GTT's cost (Theodore R18). The lab's A$27.85 is **not** taken here. |
| 4 | Confirm | Booking engine / Ivy | Confirmation shows both appointments, the lab fee note ("A$27.85 pathology fee, billed by the lab") and fasting rules from the partner lab. Drafts of these messages need Anthony's approval first (Publishing Shield). | None |
| **CONSULT DAY (1 to 28 days before the test)** | | | | |
| 5 | Arrive | Client; venue manager at reception | Short visit for the consult only (Founder Rule 5: she comes only for the referral). | None |
| 6 | Consult, 20 minutes | Midwife (09:00 to 17:00 shift) | Genuine clinical assessment, decision to request or not recorded with the reason (Catherine R16 locked W2). If yes, the midwife writes the **pathology request for item 66548** (request content rules: Regulations ss 33 to 36, in REFERRAL-TELEHEALTH-BILLING-MECHANICS.md). She marks "request issued" on the booking. | Nothing at the desk. The consult is item 82105 (A$32.95 rebate), claimed by the mother from Medicare (Theodore R18 Q2). |
| 7 | If no request | Midwife, Medical | Test slot is released. Refund follows the booking terms (not decided here, see Anthony question A1). | Refund of GTT's own fees only; GTT never refunds or repays a rebate (Theodore R18 Q23, not yet accepted by Anthony) |
| **BETWEEN** | | | | |
| 8 | Reminders | Booking engine / Ivy | Reminder 2 days and 1 day before the test: fasting, what to bring (the request), arrive 06:50. All drafts, Anthony approves wording. | None |
| **TEST DAY** | | | | |
| 9 | Arrive 06:50, first draw 07:00 | Venue manager (06:30 start) and phlebotomists (Medical employees) | Check "request issued" flag. **No request on file: no draw** (the request must exist before collection, Catherine R16 section 5). Client completes the **lab's** own registration and payment-consent form (Lab Billing doc, Option 1). | None |
| 10 | The 2-hour test | Phlebotomists collect (s 16A(5AA)(c)(iv)); therapists give 2 x 30 minute services between draws | Draws at fixed times; services never interrupt a draw (Founder Rule 1). Midwife arrives 09:00 (Anthony accepted the 07:00 to 09:00 gap, answer 15). | None. Lounge and service already paid at booking. |
| 11 | Samples go | Phlebotomist, lab courier | Samples labelled and sent to the partner lab under the lab's collection manual. | None |
| **AFTER** | | | | |
| 12 | Lab bills the mother | Partner lab | Lab invoices the mother itself after it has the request and samples (recommended Option 1 in LAB-BILLING-WORKFLOW-R19.md). | **A$27.85** goes mother to lab. GTT never touches it. |
| 13 | Results | Lab to midwife | Lab releases results to the requesting midwife. Result schedule in Catherine R16 (urgent same day; others by next business day). | None |
| 14 | Results contact | Midwife | Phones the mother per the schedule. A results consult (item 82105/91211/91218) is billed separately, never inside the package (Catherine R16 section 4). | Separate Medicare consult; amounts not in this file |
| 15 | Mother claims Medicare | Mother, myGov or app | Consult claim once she has paid GTT; test claim once she has **paid the lab account in full**. | Medicare pays the mother's bank: **A$55.00 in total** (A$32.95 + A$16.95 + A$5.10; A$56.70 if collection is 73938). Her net: Package 1 about A$245.00. |

Totals check (Package 1): A$272.15 to GTT + A$27.85 to the lab = A$300.00; minus A$55.00 rebate = A$245.00 (Theodore R18 Q2). The wording of the A$300 headline (does the lab fee sit inside it?) is the one place the R18 text is loose; the tables only work if it does. Booking page must say it plainly.

## 3. What this fixes

| Old problem (ROSTER-R18 section 5) | Now |
|---|---|
| A midwife starting 09:00 cannot cover 07:00 to 08:55 draws if the consult must come before the blood | **Closed.** Nobody needs a consult on test day. The request exists before 07:00. The 09:00 start has no conflict with the draws. |
| One consult room cannot keep pace with two clients every 25 minutes | **Closed.** Consults are on other days, so they do not follow the draw cadence. |
| Consult after the test | **Dropped.** Anthony's rule. A request written after collection would not support a Medicare benefit (Catherine R16 section 5: request must be written before the test day). |
| 07:00 to 09:00 no clinician on site | **Still true, still accepted** by Anthony (answer 15). Not reopened. |

## 4. Midwife demand and the consult room, honestly

| Measure | Working | Result |
|---|---|---|
| Tests a week | 18 a day x 6 days (repo model) | 108 |
| Consults a week | one per test | 108 |
| Consult hours a week | 108 x 20 min = 2,160 min | **36.0 hours** |
| Paid midwife hours a week | 6 days x 7.5 h (ROSTER-R18) | **45.0 hours** |
| Utilisation of paid hours | 36.0 / 45.0 | **80 percent** |
| Spare paid time a week | 45.0 - 36.0 | 9.0 hours (90 minutes a day for notes, calls, results, letters) |
| Consult room open window | 09:00 to 17:00 = 480 min, 6 days | 48 hours a week |
| Room utilisation (consult time only) | 36 / 48 | 75 percent |

**Rooming check, one room, one midwife, 09:00 to 17:00.** The 30 minute unpaid break is the R17 assumption (repo silent), so the midwife is available 450 minutes.

| Time per consult slot | Slots in 480 min (room window) | Slots in 450 min (after break) | Covers 18 a day? |
|---|---|---|---|
| 20 min, no turnover | 24 | 22 | Yes |
| 25 min (20 + 5 notes and turnover) | 19 | **18** | **Yes, exactly, no spare slot** |
| 26 min (20 + 6) | 18 | 17 | Only if there is no break |
| 30 min (20 + 10) | 16 | 15 | **No** |

Plain reading: 18 consults a day fit, but only if turnover and notes stay at 5 minutes a client or less. Turnover time is not in the repo (I used 5 as the test value; nothing is decided). At 25-minute slots the day is full with **zero spare slots**: every cancelled and re-booked consult needs another day. The hard ceiling is 22 slots a day at 20 minutes back to back, which leaves no time for notes. Practical advice for the engine: sell 18 consult slots per midwife per day and keep the 4 extra 20-minute gaps as flexible overflow only for same-week rebookings (a rule for the booking engine, not a costed option).

Example grid for a full day (illustrative): 09:00 to 12:45 nine slots, break 12:45 to 13:15, 13:15 to 17:00 nine slots; last consult starts 16:35.

Leave cover: casual midwife (cost not in repo). Each midwife needs her own provider number for the venue (Catherine R16).

Level loading: 18 consult slots a day equal 18 test slots a day, so consult days and test days must be balanced by the engine or the room will fill on some days and sit empty on others (for example, everyone books a consult on a Saturday for a Monday test).

## 5. What the booking engine must enforce

Hard rules (the engine refuses the booking if any fails):

1. **Two slots in one booking.** Consult slot and test slot are chosen together before payment.
2. **Gap rule.** Test date minus consult date is at least 1 and at most 28 calendar days (Perth time). Same day is never allowed, in either direction. Consult after test is never allowed.
3. **Consult inventory.** One midwife per rostered day, 25-minute blocks from 09:00, 18 blocks a day, six days a week, none on Sunday. The roster follows ROSTER-R18 (fortnightly block). No consult slot is sold for a day with no midwife rostered.
4. **Test inventory.** 18 draws a day, pairs every 25 minutes from 07:00 (repo Table 1 and Founder Rule 16), two collection rooms.
5. **No request, no draw.** The test slot only becomes "cleared" when the midwife marks "request issued" after the consult. The phlebotomist sees the flag before the first draw. A missing flag on the morning means no draw and a rebook; there is no same-day fix because a same-day consult is blocked and the midwife starts at 09:00.
6. **Request tied to the booking.** The request is for item 66548, dated the day of the consult (Regulations s 35 requires the date the test was judged necessary). The test must be within 28 days of that date (Anthony's rule).
7. **Reschedule rules.** Moving the consult: the new date must still be 1 to 28 days before the test. Moving the test: the new date must be 1 to 28 days after the consult; if it falls beyond 28 days, a new consult is needed. Moving a test earlier than consult plus 1 day is refused.
8. **No-show on the consult.** The test slot stays held until 18:00 the day before the test, then is released automatically (the time is my default, Anthony to change).
9. **Request lost or not on file at the door.** Same as rule 5. The engine stores the request digitally; the paper copy is a convenience.
10. **Clinical window not enforced by software.** Gestational timing for a GTT (due date check) is not in the repo. The lead midwife sets it. The booking form collects the due date and shows it to the midwife.

Edge cases decided by these rules: (a) consult yesterday, test today: allowed (gap 1 day). (b) consult 28 days ago, test today: allowed; 29 days: refused, new consult. (c) client who books less than a day ahead: the earliest test is the day after her first available consult slot. (d) late arrival: Founder Rule 14, no wiggle room after 06:50, rebook under the terms. (e) Consult overruns: the engine's 5 minute buffer absorbs it; two overruns in a row push the afternoon and the midwife's notes time, not the clients' times.

## 6. Questions that are genuinely open

For Catherine (W6, precise):

C1. Is there any legal expiry or maximum interval between the date a pathology request is written and the date of collection for the Medicare benefit on item 66548 to be payable (apart from the reg 35 date of necessity)? The engine uses Anthony's 28 days; I do not want it to promise something longer than the law allows or reject something the law allows.

The question Anthony suggested (can a midwife, not a doctor, issue the referral so the lab claims Medicare): **already answered in the library, so not re-asked.** A participating midwife acting as one can request 66548 (HIA s 16A(1)(aa); Regulations s 30 table item 2, Group P2, naming 66548) and midwives cannot request 66542 (REFERRAL-TELEHEALTH-BILLING-MECHANICS.md, Q1.2, verified). Catherine R16 ruled that Medicare law does not require a midwife on site s 16A(5AA)(c)(iv). The only dependency is that each GTT midwife has her own Medicare participating midwife provider number for the venue (Catherine R16).

For Anthony (money or a fact only he knows):

A1. If the mother's consult happens but the midwife issues no request, or the mother misses the consult, what happens to the A$110 consult fee and to the lounge part (full refund, partial, or a credit to rebook)? Options: (1) consult fee kept if the consult took place, lounge refunded; (2) all refunded unless she no-shows; (3) credit valid for 90 days. Theodore R18 Q23 (refund rule) is still waiting for your acceptance.

A2. A mother who already holds a valid request from her own GP or obstetrician: does she still book and pay for the consult (package price unchanged), or can she skip it? The library says GTT should accept any valid request from any clinician (REFERRAL-TELEHEALTH-BILLING-MECHANICS.md section 2.4). Until you answer, the engine makes the consult compulsory for everyone.

## 7. Honest gaps

- Turnover and notes time per consult is not in the repo (5 minutes used only to test the room).
- The 30 minute unpaid break is an R17 assumption.
- Whether the consult day includes any lounge time is not decided; default is the consult only.
- The A$27.85 versus A$25.85 lab price depends on collection item 73938 versus 73928 (AskMBS question, answer 8).
- Casual midwife cost: not in repo.
- Telehealth consults (midwife video item 91211) are an option in the library; not decided, not used here.
