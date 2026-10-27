> SUPERSEDED where it disagrees with docs/GTT-READ-FIRST.md (Round 25 integrity banner, 2026-10-27). Read that file first.

# GRACE-R21-BOOKING-FLOW-PART-2: Path B (package with GTT midwife consult) and the receipts

Author: Grace. Date: 2026-10-26 (Round 21). DRAFT for Anthony. Nothing was sent or published. Part 1 has Step 1 and Path A. Tags as in Part 1. Quoted text is client-facing. Price and rebate wording: Catherine to confirm.

## 1. Path B screens in order

| Screen | Name |
|---|---|
| B1 | Choose your package |
| B2 | Choose your test day and time (she books the TEST first) |
| B3 | Book your midwife consult (second) |
| B4 | Your details and consents |
| B5 | Checkout |
| B6 | Confirmation |

### B1 Choose your package
Cards show the full value: "A$320" (Package 1) and "A$370" (Package 2). Under each: "Includes your 20 minute midwife consult and the lab fee of A$27.85, which you pay to the lab. About A$55 may come back from Medicare." Same services as Path A.

### B2 Choose your test day and time
Monday to Saturday, pairs 07:00 to 10:20. The pairs 08:40, 09:05, 09:30, 09:55 and 10:20 show a tag: "Midwife consult on the same morning possible". No tag on 07:00 to 08:15. Text under the grid:
> "You book your test first, then your midwife consult. Your consult can be up to 28 days before your test. Arrive at least 10 minutes before your appointment. Late means from your appointment time onwards. We cannot fit a first blood draw in after that."

### B3 Book your midwife consult
> "Your consult is 20 minutes with our midwife. She checks you and writes your request for the test. It must finish before your first blood draw. You can book it up to 28 days before your test. Clients who have booked a test see midwife times first."

Developer rule: test clients get PRIORITY. Standalone clients only see blocks nobody with a test booking needs (details in GRACE-R21-MIDWIFE-SLOTS.md). Her test slot is held for 15 minutes (E, developer choice) while she picks a consult.

Tab 1, "On the morning of my test": shown only for a pair that allows it and a free block. Otherwise grey with: "Not available for your test time. Please choose an earlier day." Warning, ticked before going on:
> **Please stay fasted.** "If you choose a consult on the morning of your test, stay fasted for the consult and the test. Water only. Your consult comes first, then your first blood sample. If you would rather not wait fasted, choose an earlier day. It costs the same."
> [ ] I understand I must stay fasted on the morning of my consult and test.

Tab 2, "On an earlier day": calendar from 28 days to 1 day before the test. "You do not need to be fasted for an earlier-day consult."

Rule: same-morning is offered only when the consult ends before her draw (R20 rule; timing in the midwife slots file). If no consult can be found in the window, the test slot is released and she is told.

### B4 Your details and consents
Name, mobile, email, due date, Medicare card details (needed for her claim, U), booking terms, privacy notice. No booking detail is passed to the lab (one line in the privacy notice, Catherine to confirm).

### B5 Checkout
Shown in section 2. B6 Confirmation: both appointments, the fasting rules, the late rule, "Bring your Medicare card", and the lab fee note.

## 2. Checkout receipt, both paths

Common lines, same text on both receipts:
> "We charge only the GTT amount today. The lab bills you after it receives your paperwork and samples. We do not pass your booking details to the lab. Rebates are estimates ('about'). Medicare decides."

| Receipt line | Path A, Package 1 | Path A, Package 2 | Path B, Package 1 | Path B, Package 2 |
|---|---|---|---|---|
| Full price (all in) | A$265.00 | A$315.00 | A$320.00 | A$370.00 |
| Midwife consult 20 min (GST-free) | none | none | A$130.00 | A$130.00 |
| Lounge, 2 services and drinks (GST included) | A$237.15 | A$287.15 | A$162.15 | A$212.15 |
| **Charged by GTT today** | **A$237.15** | **A$287.15** | **A$292.15** | **A$342.15** |
| Billed later by the lab to the client | A$27.85 | A$27.85 | A$27.85 | A$27.85 |
| Medicare rebate, about (table in section 3) | none | none | about A$55.00 | about A$55.00 |
| Cost to the client after rebates, about | A$265.00 | A$315.00 | about A$265.00 | about A$315.00 |

Maths check (MATHS): 237.15 + 27.85 = 265.00; 287.15 + 27.85 = 315.00; 130.00 + 162.15 = 292.15; 292.15 + 27.85 = 320.00; 130.00 + 212.15 = 342.15; 342.15 + 27.85 = 370.00; 320.00 - 55.00 = 265.00; 370.00 - 55.00 = 315.00.

Path B text above the pay button:
> "Full price A$320.00. You pay GTT Center Perth A$292.15 today (consult A$130.00 plus lounge A$162.15). The lab bills you A$27.85 later. You may claim about A$55.00 back from Medicare, so your cost after rebates is about A$265.00."

Developer: the one prominent figure is the full price (single-price rule, Catherine R20, V). Keep every rebate number in ONE settings table so Theodore's re-check changes one place.

## 3. Rebate lines (about, subject to confirmation)

Theodore is re-verifying these. Until he reports, every line is "about" and unconfirmed.

| Rebate line | Amount, about | Source | Status |
|---|---|---|---|
| Midwife consult, item 82105 | about A$32.95 | R (Center of Truth) | about, subject to confirmation |
| Glucose test, item 66548 | about A$16.95 | R | about, subject to confirmation |
| Collection, item 73928 (or 73938, AskMBS to confirm) | about A$5.10 | R | about, subject to confirmation; changes the lab total by A$1.70 if 73938 |
| Lab total | about A$22.05 | MATHS 16.95 + 5.10 | about, subject to confirmation |
| Total, consult plus lab | about A$55.00 | MATHS 32.95 + 22.05 | about, subject to confirmation |
| Path A | none | Catherine R20 flag F1 (V reading of HIA s 16A) | Catherine to confirm |

Never say "A$55 for the consult". The consult alone is about A$32.95.

Lines under every Path B receipt (Catherine to confirm): "After you pay GTT Center Perth, claim your consult rebate through your Medicare account. Claim the lab rebate after you have paid the lab's bill. You need to be enrolled in Medicare."

## 4. Order of events in Path B (R)

Book test, book consult (priority, 1 to 28 days before; same morning only if it ends before her draw), consult and request, test day. No consult, no test. If her test moves beyond 28 days after the consult, she needs a new consult (A$130).

## QUESTIONS FOR ANTHONY

1. Path A clients cannot claim Medicare. Is it OK that the Path A screen says so in plain words in three places (Step 1, package card, own referral screen)?
   - A: Yes, three places. B: Two places. C: Only on the own referral screen.
   - Recommendation: A, so nobody is surprised. Catherine to confirm the wording.
2. Receipt: show the rebate table to the client or only the total?
   - A: Total only (about A$55.00) with the consult amount in brackets. B: All lines. C: No rebate lines, a link only.
   - Recommendation: A. Fewer numbers, less risk if an item changes.
3. When the lab bills her after the test, should reception tell her the bill is coming?
   - A: Yes, in the confirmation and the arrival message. B: Confirmation only. C: No.
   - Recommendation: A.

Regards.
Grace
