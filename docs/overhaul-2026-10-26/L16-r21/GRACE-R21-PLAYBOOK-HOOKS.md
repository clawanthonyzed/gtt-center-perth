# GRACE-R21-PLAYBOOK-HOOKS: changes needed in playbooks/GTT-LOCKED-FACTS-PREAMBLE.md

Author: Grace. Date: 2026-10-26 (Round 21). For Idea Lobster to apply before tonight's 22:00 AWST run. I did NOT edit the preamble. Line numbers are the file lines in the current preamble (the block between BEGIN and END). Tags: LOCKED = Anthony decided in Round 21; PENDING = apply only after his answer (until then write the old line plus "OPEN"). After editing, run `python3 tools/factcheck_locked_facts.py playbooks/GTT-LOCKED-FACTS-PREAMBLE.md` (no em dashes, no talk of any other billing model).

| # | Line | Status | Old -> New |
|---|---|---|---|
| 1 | 7 (STYLE) | LOCKED | Old: "Plain English a 16 year old can read." New: add "Say 'client' or 'expecting mother', never the bare word for a parent. Sign off 'Regards.'" |
| 2 | 9 (PRICES) | LOCKED | Old: "Package 1 advertised A$320 and Package 2 A$370, both INCLUDING the lab fee of A$27.85 ..." New: "BOOKING STEP 1 is 'Do you have a referral?'. Path B (GTT midwife consult package): Package 1 A$320 and Package 2 A$370, both including the lab fee of A$27.85. Path A (client keeps her own outside referral, no GTT consult): Package 1 A$265 and Package 2 A$315, all in, including the lab fee of A$27.85. Lab fee is the same on both paths." |
| 3 | 10 (MONEY SPLIT) | PENDING (Anthony Q1, Part 1) | Old: "GTT receives A$292.15 ... A$342.15." New: keep for Path B. Add: "Path A: GTT receives A$237.15 (Package 1) or A$287.15 (Package 2), which is A$55.00 less than Path B, no consult line, and the whole amount is lounge with GST inside (A$21.56 and A$26.10). OPEN until Anthony accepts or changes the Path A price." |
| 4 | 10 (MONEY SPLIT) | LOCKED | Add: "The lab bills the client after it receives the paperwork and samples. GTT never passes booking details to the lab. Checkout shows the full price and the breakdown, shows rebates as 'about', and charges only the GTT amount." |
| 5 | 11 (MEDICARE) | LOCKED | Old: "...Client's own cost after Medicare A$265 (Package 1) or A$315 (Package 2)..." New: add "Rebates apply to Path B only. Path A (outside request): no Medicare benefit for a test done at GTT; the screen says so (wording: Catherine to confirm). Every rebate line is 'about, subject to confirmation' until Theodore's re-check is done. Path A client's cost is A$265 / A$315 with no rebate." |
| 6 | 12 (ORDER OF EVENTS) | LOCKED | Old: "Every client tested at GTT has a GTT midwife consult (an outside request gets no Medicare benefit at GTT). No consult, no test." New: "Path B clients have a GTT midwife consult; no consult, no test. Path A clients keep their own outside referral: no consult, no Medicare benefit, request checked at the door; if it is not suitable on the day there is no draw (she may switch to Path B with a top-up if a block is free and her pair is 08:40 or later). Standalone consults are upside only and never counted." |
| 7 | 12 (ORDER OF EVENTS) | LOCKED | Old: "It can be 1 to 28 days before the test, or on the morning of the test only for the draw pairs 08:40 and later (one per pair)..." New: add "Client has up to 28 days to book the consult. Test clients get PRIORITY access to midwife slots. Same-morning consult only when it ends before her draw. Consult blocks: first appointment 08:15; midwife on site 08:00 for set-up." Pairs 08:40 and later stays true for 25 minute blocks. PENDING Anthony Q1 (25 or 30 minute): with 30 minute blocks the 08:40 pair is dropped and the pairs become 09:05 and later, 4 a morning. |
| 8 | 13 (TEST MORNING) | LOCKED | Old: "Clients arrive 06:50 with no allowance for late arrivals." New: "Arrive at least 10 minutes before the appointment. Late means from the appointment time onwards. We cannot fit a first blood draw in after that. Use this sentence word for word on the booking page, terms, confirmation, reminders, arrival message and follow-up." |
| 9 | 14 (PEOPLE) | LOCKED | Old: "...they work 08:00 to 16:00 and also take standalone private pregnancy consults when time allows." New: add "Midwife on site 08:00 for set-up, first appointment 08:15, last finish by 16:00. The midwife phones only abnormal results; normal results get a generic text or email ('your result is ready', no health detail)." |
| 10 | 14 (PEOPLE) | PENDING (Midwife slots Q2) | Add: "OPEN: the unpaid 30 minute meal break plus 15 minutes of set-up leaves 435 minutes, which is 17 blocks of 25 minutes, not 18. Do not state 18 blocks a day until Anthony decides the 16:15 finish." |
| 11 | 14 (PEOPLE) | LOCKED | Venue manager: add "sees booking flags only, never the request copy (Catherine to confirm)." |
| 12 | New line after 15 (FILING) | LOCKED | Add: "FILING: the paper weekly folder is replaced by a secure computer record per test day. Midwife files; phlebotomists see 'Today' on test morning; venue manager sees flags only; backups; retention to be set by Catherine. Printed evening list for internet outages only if Anthony agrees (OPEN)." |
| 13 | New line (CHANGES) | PENDING (Waitlist Q1) | Add: "CHANGE WINDOW: OPEN, 1 week or 48 hours (Grace recommends 48 hours). WAITLIST: free to join, offered in order of joining, test slot and midwife slot move together, automatic email when a slot opens. ILLNESS: ask the least proof (one tick, no diagnosis; a short note only on a second claim). 50 percent lounge-refund rule (R20) stands pending Anthony's final answer; a delivered consult stays earned." |
| 14 | 18 (MONEY RESULT) | LOCKED | Old: "...Standalone consults, interest and the 10 percent post-test discount are NOT in that figure. Do not recompute." New: add "The A$19,973.98 assumes every client is on Path B (A$292.15 to GTT). Path A clients earn A$55.00 less each in GTT cash and are NOT in that figure. Do not recompute. Do not quote any other profit figure." |
| 15 | 19 (HARD STOPS) | LOCKED | Add: "no health lawyer cost in any financial figure." |
| 16 | 5 (header note, also the Source line 3) | LOCKED | Add the Round 21 source files: GRACE-R21-BOOKING-FLOW-PART-1.md, PART-2.md, MIDWIFE-SLOTS.md, WAITLIST-AND-LATE.md, COMPUTER-FILING.md. |

Also update `tools/factcheck_locked_facts.py` list only if Idea Lobster wants old strings blocked: "arrive 06:50 with no allowance" and "paper folder" are now stale (U, no stale-table change made by me).

## QUESTIONS FOR ANTHONY

1. Apply the PENDING rows (3, 7 part, 10, 13) tonight as "OPEN" lines, or wait for your answers?
   - A: Apply as OPEN. B: Wait. C: Apply Grace's recommendations as the working case.
   - Recommendation: A, so the 22:00 drafts do not state an old number as final.
2. Should overnight drafts treat Path A as in scope?
   - A: Yes, both paths. B: Path B only until you decide Path A pricing. C: Path A text only, no money lines.
   - Recommendation: C.

Regards.
Grace
