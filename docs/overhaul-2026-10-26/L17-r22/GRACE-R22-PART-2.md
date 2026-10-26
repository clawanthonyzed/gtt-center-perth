# GRACE-R22-PART-2: Waitlist (cancellation list) rules, emails and booking engine

Author: Grace. Date: 2026-10-26 (Round 22). DRAFT for Anthony. Nothing was sent. Tags: R repo, E estimate, U unverified. Client wording: Catherine to confirm (privacy and consumer law).

## READ-FIRST CHECK (from GTT-READ-FIRST.md, 2026-10-26)
- Venue manager start: 06:30 Mon to Fri (07:00 is the first draw).
- Path A = PREFERRED, package WITH the GTT midwife consult. Path B = NOT preferred, outside referral, no GTT consult. (My Round 21 files used the opposite labels: they are out of date.)
- Prices: Path A shown A$320 / A$370, GTT charges A$292.15 / A$342.15. Path B A$300 / A$350 all in.  <!-- factcheck:ok -->
- Rebates (planning, "about"): consult A$32.95 + lab A$22.05 = A$55.00.
- Midwives 08:00 to 16:00, on site 08:00, first consult 08:15, 25 minute blocks.
- Late rule: "Please arrive at least 10 minutes before your appointment, because late means from your appointment time onwards and we cannot fit a first blood draw in after that."

## 1. The rules (locked by Anthony, Round 22)
| # | Rule |
|---|---|
| 1 | Free to join. No deposit. Joining is a tick box on the booking page, plus her name and email. |
| 2 | She chooses what she wants to hear about: a test time, a midwife time, or both; any day, or a date range (E, my suggestion). |
| 3 | When a test slot or a midwife slot opens, EVERYONE on the matching list gets the email at the same moment, automatically. |
| 4 | No queue and no order. First client to book and pay gets it. |
| 5 | The slot stays with the list for 48 hours. If nobody books it, it goes to the public booking page. Nobody on the list is emailed again. |
| 6 | Midwife slots: clients with a booked test and no consult yet are emailed first (test clients have priority, R). Clients wanting a standalone consult are emailed when the slot goes public. Standalone is upside only and never counted. See question 2. |
| 7 | If a client books a better time, her old time is freed on the spot and goes through rule 3. |
| 8 | She pays only the GTT amount at booking. The lab bills her later (R). |

## 2. SPOT THE PROBLEM: a slot freed less than 48 hours before the appointment
A time freed 20 hours before cannot sit with the list for 48 hours; it would pass before anyone could use it. Three fair options:
| Option | How it works | Good | Bad |
|---|---|---|---|
| A | List for 48 hours OR until 12 hours before the appointment, whichever is first. Freed under 12 hours before: list and public page open at the same moment. | One easy rule to say | Little time to react for early draws |
| B | List gets half of the time left, never more than 48 hours, never less than 3 hours. | Always proportional | Harder to explain |
| C | Under 48 hours: list gets 6 hours, then public. | Simple | A 07:00 slot freed the night before gets no list time |
Recommendation: A. Warning for all three: a client booking under 12 hours ahead must tick "I understand the fasting instructions" (fasting hours: NOT IN REPO, the lab sets them).

## 3. Automatic email (draft)
Sender name: the business name. Subject: "A time you asked for is free". Preview line: "First to book gets it." No health words in the subject, the preview or the body (no test name, no midwife, no pregnancy). Catherine A/B privacy check pending.
> Hello [first name],
> A booking time you asked us about is now free: [day, date, time].
> It is not held for you. The first person to book it gets it. To book, press the button: [BOOK THIS TIME].
> If it is gone, you stay on the list and we will email you the next time one opens. To leave the list: [link].
> Please arrive at least 10 minutes before your appointment, because late means from your appointment time onwards and we cannot fit a first blood draw in after that.
> Regards.
> GTT Center Perth

Details (test or consult, price) show only after she presses the button, on the secure booking page.

## 4. "Slot taken" message (screen and email)
> "Sorry, someone else booked that time a moment ago. You are still on the list, and we will email you when the next time opens. Regards."
While another client is paying (10 minute hold, E): "This time is being booked right now. Try again in a few minutes."

## 5. Booking engine behaviour (for the developer)
| Step | Behaviour |
|---|---|
| 1 | A cancellation, change or release sets the slot to "offered to list" with a start time and an end time (rule A: 48 hours or 12 hours before). |
| 2 | The system sends one email to each matching list member at once. It sends one email per slot per person. |
| 3 | The link opens that one slot. Pressing "Book this time" holds it 10 minutes (E) while she pays. |
| 4 | The first completed payment wins. The check and the booking happen in one step, so two people cannot both get it. |
| 5 | The loser sees the slot taken message. |
| 6 | Winner: removed from that list. She gets the normal confirmation with the late rule. |
| 7 | End time reached, slot still free: it appears on the public page, the list is not emailed again. |
| 8 | A hold that was not paid for expires after 10 minutes and the slot goes back to "offered". |
| 9 | Log every offer and booking (slot, time, who booked). |
| 10 | Each email address can be on a list once. Rate limit the link so a script cannot grab slots. |

## QUESTIONS FOR ANTHONY
1. Slots freed under 48 hours before the appointment: which option?
   - A: list until 12 hours before, then public. B: half the time left. C: 6 hours then public.
   - Recommendation: A.
2. Midwife slots: test clients first for 48 hours, then standalone?
   - A: Yes. B: Everyone at once.
   - Recommendation: A (matches your priority rule).
3. Email only people whose chosen days match, or everyone on the list?
   - A: Matching only. B: Everyone.
   - Recommendation: A (fewer emails, same result).

Regards.
Grace
