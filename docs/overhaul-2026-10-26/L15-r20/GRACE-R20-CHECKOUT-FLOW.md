# GRACE-R20-CHECKOUT-FLOW: booking screens, receipt text, fasting warning, reminders

Author: Grace (Operations Manager, GTT Center Perth). Date: 2026-10-26 (Round 20). **DRAFT for Anthony. Not approved. Nothing was sent or published.** Written for a web developer. Words only, no drawings. The business name is on hold, so the text says "GTT Center Perth" (working name).

Marks used:
- **legal wording pending**: Catherine is checking how price and rebate statements may be worded. Do not publish these lines until she clears them.
- **NOT IN REPO**: a fact nobody has given us yet. Listed in the questions at the end.
- Text inside quotation marks and indented is client-facing copy. Everything else is a note to the developer.

Locked numbers used (Round 20 brief, Center of Truth, Theodore R20): consult A$130 (GST-free, 20 minutes, item 82105); lounge and service A$162.15 (Package 1) and A$212.15 (Package 2); lab fee A$27.85 paid to the lab; rebates A$32.95 (consult) and A$22.05 (lab: A$16.95 test plus A$5.10 collection) = A$55.00 total.

## 1. The screens in order

| Screen | Name | What the client does |
|---|---|---|
| 1 | Choose your package | Picks Package 1 or Package 2 |
| 2 | Choose your test day and time | Picks the test slot (she books the TEST first) |
| 3 | Your referral | Picks "I need a referral" or "I have a referral" |
| 4A | Book your midwife consult (if "I need a referral") | Picks the consult: same morning (when offered) or an earlier day |
| 4B | Using your own referral (if "I have a referral") | Reads the recommendation, then continues or switches to 4A |
| 5 | Your details and consents | Name, mobile, email, due date, Medicare details, accepts terms and privacy notice |
| 6 | Checkout summary | Sees the full price, what she pays today, the lab fee, the expected Medicare rebates |
| 7 | Confirmation | Sees both appointments and the fasting rules |

## 2. Screen 1: Choose your package

Package names and contents are as in the business plan (Package 1: 2 services of 30 minutes; Package 2: 2 services of up to 45 minutes; both with lounge access and approved drinks during the test). The price shown on each card is the **full value including the lab fee** (A$320 and A$370), with the line "includes the lab fee of A$27.85, which you pay to the lab" (**legal wording pending**).

## 3. Screen 2: Choose your test day and time

Developer rules: show only days Monday to Saturday. Show the pairs 07:00 to 10:20 (rules in GRACE-R20-ROSTER-BOOKING.md section 4). On each pair that can have a same-morning consult (08:40, 09:05, 09:30, 09:55, 10:20) show a small tag:

> "Midwife consult on the same morning possible"

No tag on 07:00, 07:25, 07:50 and 08:15. Text under the grid:

> "Your test takes about 2 hours. You need a midwife consult first, to get the referral for the test. You can book it on the day of your test (before the test) or on an earlier day."

## 4. Screen 3: Your referral

Title: "Do you have a referral for the glucose test?"

Two large choices. Choice 1 is shown first and is marked "Recommended".

> **I need a referral** (Recommended)
> "Book a 20 minute consult with our midwife. She checks you and writes your referral for the test. Everything is in one booking."

> **I have a referral**
> "You already have a referral from your doctor or midwife. You book the package only."

Developer note: the choice is stored on the booking. "I need a referral" sends her to screen 4A. "I have a referral" sends her to screen 4B.

## 5. Screen 4A: Book your midwife consult

Intro text:

> "Your consult is 20 minutes with our midwife. It must happen before your test, so the referral is ready. Choose a time that suits you."

Two tabs.

**Tab 1: "On the morning of my test"** (shown only when the test slot is a pair that allows it and the consult block is free; otherwise the tab is greyed out with the text: "Not available for your test time. Please choose an earlier day.")

Shows the one consult time that goes with her test pair (table in GRACE-R20-ROSTER-BOOKING.md section 3.2). Warning box, in bold, ticked before continuing:

> **Please stay fasted.** "If you choose a consult on the morning of your test, you must stay fasted for the consult and the test. Water only. Your consult comes first, then your first blood sample. You will be here about 50 minutes before your first sample. If you would rather not wait fasted, choose a consult on an earlier day. It costs the same."
> [ ] I understand I must stay fasted on the morning of my consult and test.

(Fasting hours: **NOT IN REPO**. The partner lab sets the number of hours. Until the lab confirms, the developer shows "Follow the fasting hours on your instruction sheet".)

**Tab 2: "On an earlier day"**

Calendar of days from 1 to 28 days before her test, Monday to Saturday, with free 25 minute blocks from 08:00. Text:

> "Your consult can be from 1 to 28 days before your test. Booking at least a day ahead means you arrive for your test already with your referral. You do not need to be fasted for an earlier-day consult."

Developer note: the 28 day rule and the other engine rules are in GRACE-R20-ROSTER-BOOKING.md section 4.

## 6. Screen 4B: Using your own referral

Title: "Using your own referral"

> "You can use a referral from your own doctor or midwife. We will check it on the morning of your test."
>
> **We strongly recommend booking our midwife consult instead.** "Our midwife checks you before the test and makes sure your referral is ready. If your referral is missing or not suitable on the morning, we may not be able to do your test, and you would need to rebook."
>
> **If you keep your own referral:**
> "Please bring the original (paper or on your phone) on test day."
> (Option for Anthony, question 3: upload a photo of the referral at booking.)

Buttons: "Add a midwife consult (recommended)" (goes to screen 4A) and "Continue with my own referral".

Developer note: GTT staff cannot judge whether an outside referral is clinically right for the test, and the lab decides what it will accept. This is **NOT IN REPO** and is for Catherine and the partner lab (question 4).

## 7. Screen 5: Your details and consents

Same fields as the earlier booking flow (name, mobile, email, due date, Medicare details, accept booking terms and privacy notice). The booking terms link opens the cancellation table (GRACE-R20-CANCELLATION.md, **draft, not approved**). Privacy notice wording: **Catherine to confirm**.

## 8. Screen 6: Checkout summary and receipt text

The checkout shows the **full value including the lab costs**, but **charges only the GTT amount**. Below are the exact receipt blocks. Amounts in A$. All lines about price and rebates are **legal wording pending**.

### 8.1 Package 1, "I need a referral"

> **Your booking summary**
>
> Full value of your visit (includes the lab fee): **A$320.00**
>
> **What you pay GTT Center Perth today: A$292.15**
> - Midwife consult, 20 minutes (GST-free): A$130.00
> - Lounge, two 30 minute services and drinks (GST included): A$162.15
>
> **The lab bills you separately: A$27.85.**
> "You pay the lab directly. GTT Center Perth never takes this money."
>
> **Medicare rebates you can expect to claim back:**
> - For your consult: A$32.95
> - For your lab test and sample collection: A$22.05 (test A$16.95 plus collection A$5.10)
> - **Total expected from Medicare: A$55.00**
>
> "The A$55.00 is the total for the consult and the lab test together. The consult on its own is A$32.95."
>
> **Your estimated out of pocket cost: A$265.00**
> "This is the full A$320.00 minus the expected A$55.00 from Medicare. You claim the rebates yourself from Medicare. Rebates are an estimate and Medicare makes the final decision."

Maths check (shown to developer only): 130.00 + 162.15 = 292.15; 292.15 + 27.85 = 320.00; 32.95 + 22.05 = 55.00; 320.00 - 55.00 = 265.00.

### 8.2 Package 2, "I need a referral"

> Full value of your visit (includes the lab fee): **A$370.00**
>
> **What you pay GTT Center Perth today: A$342.15**
> - Midwife consult, 20 minutes (GST-free): A$130.00
> - Lounge, two services of up to 45 minutes and drinks (GST included): A$212.15
>
> **The lab bills you separately: A$27.85.** "You pay the lab directly."
>
> Medicare rebates you can expect: consult A$32.95; lab test and collection A$22.05; **total A$55.00**.
>
> **Your estimated out of pocket cost: A$315.00**

Maths check: 130.00 + 212.15 = 342.15; 342.15 + 27.85 = 370.00; 370.00 - 55.00 = 315.00.

### 8.3 "I have a referral" (package only) **derived, Anthony to confirm**

The brief says "package only". I derived these lines from the locked lounge amounts and the lab rebate; the price of a package without the consult is not stated as a separate locked line (question 1).

Package 1:
> Full value of your visit (includes the lab fee): **A$190.00**
> **What you pay GTT Center Perth today: A$162.15** (lounge, two 30 minute services and drinks)
> **The lab bills you separately: A$27.85.**
> Medicare rebate you can expect: lab test and collection **A$22.05**. (No consult, so no consult rebate.)
> **Your estimated out of pocket cost: A$167.95**

Package 2 follows the same pattern: full value A$240.00, GTT charge A$212.15, lab A$27.85, rebate A$22.05, out of pocket A$217.95.

Maths check: 162.15 + 27.85 = 190.00; 190.00 - 22.05 = 167.95; 212.15 + 27.85 = 240.00; 240.00 - 22.05 = 217.95.

### 8.4 Lines under every receipt

> "To claim: after you have paid GTT Center Perth, claim your consult rebate through your Medicare online account or app. Claim your lab rebate after you have paid the lab's bill in full. You need to be enrolled in Medicare to receive rebates." (**legal wording pending**; the "enrolled in Medicare" line is an assumption for Catherine.)
>
> "Booking terms apply, including our cancellation and late rules."

## 9. Screen 7: Confirmation (client-facing)

> **You are booked.**
> Your midwife consult: day, time. (Or "on the morning of your test at the time shown".)
> Your test: day, time. Arrive 10 minutes before your first appointment.
>
> **Fasting.** "Stay fasted before your test, water only, for the number of hours on your instruction sheet. If your consult is on the morning of your test, you must be fasted for the consult too."
>
> "Bring your Medicare card. If you have your own referral, bring it too."

Developer note: show the lab fee note "A$27.85, billed by the lab" again here.

## 10. Reminder wording (drafts, for Anthony's approval; nothing is sent)

All sign off "Regards." The business name is the working name only.

### 10.1 SMS, 2 days before an earlier-day consult
> "GTT Center Perth: your midwife consult is on [date] at [time]. It takes 20 minutes. You do not need to be fasted for this visit. Regards."

### 10.2 SMS, the day before the test (also the day before a same-morning consult)
> "GTT Center Perth: your glucose test is tomorrow at [time]. Please stay fasted, water only, for the hours on your instruction sheet. Arrive 10 minutes early. Bring your Medicare card and your referral if you have your own. Regards."

### 10.3 Email, 2 days before the test (and the same text to a same-morning consult client)
Subject: Getting ready for your glucose test

> Hello [first name],
>
> Your glucose test is on [date] at [time]. Here is how to get ready.
>
> - Stay fasted before your test. Water only, for the hours on your instruction sheet.
> - If your midwife consult is on the morning of your test, you must be fasted for the consult too. Your consult comes first at [time], then your first blood sample at [time]. You will be here about 50 minutes before your first sample.
> - Arrive 10 minutes before your first appointment.
> - Bring your Medicare card. If you are using your own referral, bring it.
> - Your test takes about 2 hours. You will have two relaxing services between blood samples.
> - If you feel unwell at any point, tell the staff straight away.
>
> The lab bills you A$27.85 separately. After you pay GTT Center Perth and the lab, you can claim your Medicare rebates (expected A$55.00 in total: A$32.95 for the consult and A$22.05 for the lab). (**legal wording pending**)
>
> Regards.
> GTT Center Perth

Developer note: the square-bracket items are merge fields filled by the booking engine from the booking record. They are not unfinished text.

### 10.4 SMS, morning of a same-morning consult (06:30, sent only to those clients)
> "GTT Center Perth: today your midwife consult is at [time], then your test at [time]. Please stay fasted, water only. If you feel unwell, tell the team. Regards."

## 11. Open points in this draft

| Point | Status |
|---|---|
| Price of a package without the consult (section 8.3) | Derived, Anthony to confirm |
| Fasting hours in the client text | NOT IN REPO, partner lab to confirm |
| Whether outside referrals are accepted, and for which tests | NOT IN REPO, Catherine and the lab |
| Rebate and price wording | legal wording pending (Catherine) |
| Rebate item 73928 or 73938 | AskMBS to confirm; the A$22.05 total changes by A$1.70 if it is 73938, so keep the rebate lines editable in one place |
| Privacy notice and consent wording | Catherine to confirm |

## QUESTIONS FOR ANTHONY

1. What does a "I have a referral" client pay?
   - A: Lounge amount only (A$162.15 / A$212.15), as drawn in 8.3. B: Same price as the consult-included package (she still pays for the consult). C: Lounge amount plus a smaller "referral check" fee.
   - Recommendation: A, with the strong midwife recommendation on screen 4B.
2. Should "I need a referral" be pre-selected on screen 3?
   - A: Yes, pre-selected. B: No, client must choose. C: Pre-selected only for a first-time GTT client.
   - Recommendation: A.
3. Should the "I have a referral" client upload a photo of her referral at booking?
   - A: Yes, compulsory. B: Yes, optional. C: No, bring it on the day.
   - Recommendation: B (it feeds the paper register and lets the midwife spot problems early). Privacy: Catherine to confirm.
4. If an outside referral is not suitable on the morning, can she buy a same-morning consult (pairs from 08:40 only) and carry on?
   - A: Yes, if a block is free. B: No, rebook under the terms. C: Yes, and the rebook fee is waived.
   - Recommendation: A (see GRACE-R20-PAPER-SAFETY-NET.md section 6).

Regards.
Grace
