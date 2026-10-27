> SUPERSEDED where it disagrees with docs/GTT-READ-FIRST.md (Round 25 integrity banner, 2026-10-27). Read that file first.

# GRACE-R21-BOOKING-FLOW-PART-1: Step 1 and Path A (own referral)

Author: Grace. Date: 2026-10-26 (Round 21). DRAFT for Anthony. Nothing was sent or published. Words only, no drawings. Part 2 has Path B and the receipts.
Tags: R repo, V verified, E estimate, U unverified, MATHS my arithmetic. Text in quotes is client-facing. Everything else is for the developer. Wording marked "Catherine to confirm" must not go live until she clears it.

## 1. Step 1 (first screen of the whole flow)

Title: "Do you have a referral?"

| Button | Text on the button | Goes to |
|---|---|---|
| 1 | "Yes, and I will use my own referral." Small print: "No GTT midwife consult. No Medicare benefit for this test. Price A$265 (Package 1) or A$315 (Package 2), lab fee included." | Path A |
| 2 | "No, or I would like the GTT midwife to do my consult." Small print: "Package with a 20 minute GTT midwife consult. Full price A$320 (Package 1) or A$370 (Package 2). About A$55 may come back from Medicare." | Path B |

Developer: store the choice on the booking. A client can switch paths until she pays. Rebate wording: Catherine to confirm. Do not pre-select a button (question 2).

## 2. The money check on Path A (Anthony asked me to check "GTT still gets the same amount")

| Line | Package 1 | Package 2 | Tag |
|---|---|---|---|
| Client pays in total, all in | A$265.00 | A$315.00 | R (Anthony) |
| Lab fee, paid to the lab, never GTT money | A$27.85 | A$27.85 | R |
| **GTT receives (265 - 27.85, 315 - 27.85)** | **A$237.15** | **A$287.15** | MATHS |
| GTT receives on Path B (consult 130.00 + lounge) | A$292.15 | A$342.15 | R |
| Path A is lower by | A$55.00 | A$55.00 | MATHS |
| GST inside the Path A amount (divide by 11) | A$21.56 | A$26.10 | MATHS |
| Path A amount without GST | A$215.59 | A$261.05 | MATHS |
| Path B without GST (lounge divided by 1.1, plus consult 130.00 GST-free) | A$277.41 | A$322.86 | MATHS |
| Path A is lower without GST by | A$61.82 | A$61.81 | MATHS |
| Path A lounge price is higher than the Path B lounge price by | A$75.00 | A$75.00 | MATHS |

Reading: GTT does NOT get the same amount. It gets A$55.00 less per client in cash and about A$61.82 less without GST. Reasons: (1) A$265 includes the A$27.85 lab fee, and (2) the whole GTT amount is lounge, which carries GST, where the A$130 consult was GST-free. Whether GST applies to all of it: accountant to confirm (U). The midwife cost saved when there is no consult is not worked out here (Theodore). The locked A$19,973.98 assumes every client is on Path B, so each Path A client lowers it. I did not recompute it (locked). See question 1.

## 3. Path A screens in order

| Screen | Name |
|---|---|
| A1 | Choose your package |
| A2 | Choose your test day and time |
| A3 | Your own referral |
| A4 | Your details and consents |
| A5 | Checkout |
| A6 | Confirmation |

### A1 Choose your package
Cards show one single price each, large: "A$265" and "A$315". Under each: "All in. Includes the lab fee of A$27.85, which you pay to the lab. No Medicare benefit for this test." (Catherine to confirm. The single-price rule, ACL s 48, was read by Catherine in R20, V.) Package 1: 2 services of 30 minutes. Package 2: 2 services of up to 45 minutes. Both have lounge access and approved drinks.

### A2 Choose your test day and time
Monday to Saturday. All 9 draw pairs, 07:00 to 10:20, 2 clients each (R). No midwife tags, because there is no consult. Text under the grid:
> "Your test takes about 2 hours. Arrive at least 10 minutes before your appointment. Late means from your appointment time onwards. We cannot fit a first blood draw in after that."

### A3 Your own referral
> "You are keeping your own referral. Please read this before you go on.
> - Bring the original (paper or on your phone) on test day. We check it at the door.
> - A request from outside GTT gets no Medicare benefit for a test done here. You cannot claim a rebate for this test. (Catherine to confirm)
> - If your request is not suitable on the day, we may not be able to do your test. You can then change to the package with our midwife consult if a midwife time is free, or you rebook under our terms.
> - Our midwife consult costs more up front, but about A$55 may come back from Medicare."

Buttons: "Switch to the package with the midwife consult" (goes to Part 2, B1) and "Continue with my own referral". Optional: "Add a photo of your referral now" (stored in the secure record, see GRACE-R21-COMPUTER-FILING.md; privacy: Catherine to confirm). Not compulsory.

### A4 Your details and consents
Name, mobile, email, due date. Tick boxes: booking terms (shows the late rule and the change window), privacy notice (Catherine to confirm). The privacy notice says GTT does not pass booking details to the lab (R21 decision).

### A5 Checkout
> **Your booking**
> Full price, all in: **A$265.00**
> - Paid to GTT Center Perth today: **A$237.15** (lounge, two 30 minute services and drinks; GST included A$21.56)
> - Billed to you by the lab after it gets your paperwork and samples: **A$27.85**
> Medicare rebate you can expect: none for this booking.
> "We charge only A$237.15 today. The lab sends you its own bill. We do not pass your booking details to the lab."

Package 2: full A$315.00, GTT today A$287.15 (GST A$26.10), lab A$27.85.
Above the pay button, with a tick box: the late rule and the change window (Catherine R20, V: a term must show at checkout, not only in a link).

### A6 Confirmation
> "You are booked for [date] at [time]. Arrive at least 10 minutes before your appointment. Late means from your appointment time onwards. We cannot fit a first blood draw in after that. Stay fasted, water only, for the hours on your instruction sheet. Bring your own referral and your ID."

Fasting hours: NOT IN REPO (the lab sets them). Square-bracket items are merge fields filled by the system.

## 4. Arrival checks on the morning

| Step | Who | Check |
|---|---|---|
| 1 | Venue manager at the door (from 06:30) | A request is there (original, phone, or the photo in the record). Name matches the booking. A date is on it. She does not judge if it is medically right. |
| 2 | Phlebotomist | Request is for the pregnancy glucose test and meets the partner lab's rules. What the lab accepts: NOT IN REPO. |
| 3 | If unsure | Midwife (on site from 08:00), or phone the lab. |
| 4 | Suitable | Draw as booked. |

## 5. If her outside request is not suitable on the day

| Situation | What staff do (draft) |
|---|---|
| Pair 08:40 or later and a midwife block is free | Offer the midwife consult now. She tops up A$55.00 (A$292.15 less A$237.15, MATHS; Anthony to confirm), moves to Path B, and may claim about A$55 from Medicare. Consult first, then draw. |
| Pair 07:00 to 08:15, or no free block | No draw. Move her to a later pair the same day only if the midwife can see her first. Otherwise rebook. |
| No request at all | Same as above, then the late-change rule in the terms. |
| Request not suitable | One free rebook (question 3). |

Staff never write, copy or fix a request. No suitable request, no draw (R).

## QUESTIONS FOR ANTHONY

1. GTT gets A$55.00 less per Path A client (A$237.15 and A$287.15). Accept it?
   - A: Accept, keep A$265 / A$315. B: Raise Path A to A$320 / A$370 (same cash as Path B, but she gets no rebate). C: Raise it to A$290 / A$340 (halfway).
   - Recommendation: A only if the midwife time saved covers it; Theodore to price that. Your call.
2. Should neither button be pre-selected?
   - A: Neither. B: Path B pre-selected. C: Path A pre-selected.
   - Recommendation: A.
3. Request not suitable: what is the fee?
   - A: One free rebook, then the late-change rule. B: Always the late-change rule. C: Always free, plus the top-up option.
   - Recommendation: A.

Regards.
Grace
