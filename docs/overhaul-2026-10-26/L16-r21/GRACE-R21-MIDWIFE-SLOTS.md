# GRACE-R21-MIDWIFE-SLOTS: consult timing, priority rule, results messages

Author: Grace. Date: 2026-10-26 (Round 21). DRAFT for Anthony. Nothing was sent. Tags: R repo, E estimate, U unverified, MATHS my arithmetic. No new calculator; only adding and dividing locked numbers.

Inputs (R): midwife on site 08:00 for set-up, first appointment 08:15, last finish by 16:00, one consult room, consult 20 minutes, draw pairs every 25 minutes from 07:00 (07:00, 07:25, 07:50, 08:15, 08:40, 09:05, 09:30, 09:55, 10:20), 2 clients a pair, 18 a morning. A consult must END before her draw.

## 1. Option 25: 25 minute blocks (20 minutes consult, 5 minutes to write the request)

| Block | Starts | Consult ends | Block ends | Draw pair it can feed |
|---|---|---|---|---|
| 1 | 08:15 | 08:35 | 08:40 | 08:40 (consult ends 5 minutes before the draw) |
| 2 | 08:40 | 09:00 | 09:05 | 09:05 |
| 3 | 09:05 | 09:25 | 09:30 | 09:30 |
| 4 | 09:30 | 09:50 | 09:55 | 09:55 |
| 5 | 09:55 | 10:15 | 10:20 | 10:20 |
| 6 | 10:20 | 10:40 | 10:45 | none (last pair is 10:20) |

Which pairs can have a same-morning consult: 08:40, 09:05, 09:30, 09:55 and 10:20, one client each. **5 a morning, at most** (MATHS). Pairs 07:00, 07:25, 07:50 and 08:15 cannot (8 clients; consult on an earlier day). So 13 of 18 clients need an earlier day. A tighter version (a 25 minute gap after the block, so draws 09:05 to 10:20 only) gives 4 a morning. Blocks a day: 08:15 + 18 x 25 minutes ends 15:45, so **18 blocks** (MATHS). 108 a week.

## 2. Option 30: list the consult as 30 minutes (20 consult, 10 paperwork)

| Block | Starts | Consult ends | Block ends | Draw pair |
|---|---|---|---|---|
| 1 | 08:15 | 08:35 | 08:45 | 09:05 (not 08:40, the block ends after it) |
| 2 | 08:45 | 09:05 | 09:15 | 09:30 |
| 3 | 09:15 | 09:35 | 09:45 | 09:55 |
| 4 | 09:45 | 10:05 | 10:15 | 10:20 |
| 5 | 10:15 | 10:35 | 10:45 | none |

Same-morning: **4 a morning**, pairs 09:05, 09:30, 09:55 and 10:20. Blocks a day: 465 minutes / 30 = 15 (MATHS), last ends 15:45. 90 a week.

## 3. Side by side (all clients on Path B, MATHS)

| | 25 minute | 30 minute |
|---|---|---|
| Blocks a day / a week | 18 / 108 | 15 / 90 |
| Same-morning consults a morning | 5 | 4 |
| Test clients needing a consult a week | 108 | 108 |
| Test clients who cannot get a consult a week | 0 | 18 (one in six) |
| Paperwork minutes per consult | 5 | 10 |

Path A clients need no block, so each one frees one. The share of Path A clients is NOT IN REPO.

### The meal break problem (found this round)
The midwife is on site 08:00 to 16:00 = 480 minutes. Take the 30 minute unpaid break (E, from R20; the Fair Work meal break rule is NOT VERIFIED) and the 15 minutes of set-up: 480 - 30 - 15 = 435 minutes for consults. That is **17 blocks of 25** (425 minutes) or **14 blocks of 30** (420), not 18 and 15. So 102 a week (25 minute) or 84 a week (30 minute). Fix for 18 blocks: the shift runs to 16:15, 0.25 extra paid hour, about A$14.20 a weekday and A$21.31 on Saturday, about A$92.32 a week (E, using the R20 loaded rates A$56.81 and A$85.22). Option for Anthony, not decided.

## 4. Recommendation (Anthony decides)

**25 minute blocks.** It matches the 25 minute draw rhythm, gives 5 same-morning consults instead of 4, and is the only option that holds all 108 test clients a week (with the 16:15 finish). Listing 30 minutes is kinder on paperwork time but turns away about one client in six. Do not list 30 minutes to the client and book 25 internally (could mislead; Catherine).

## 5. Priority rule for test clients (developer)

1. A client with a booked test sees midwife blocks first, any day 1 to 28 days before her test, plus the same-morning block for her pair.
2. The 5 same-morning blocks of each morning are held for that morning's test pairs until 18:00 the day before.
3. A standalone client sees only blocks left over: open blocks minus the blocks still needed by test clients with no consult yet in the next 28 days. Released at 18:00 the day before (R20 assumption).
4. A block freed by a cancellation goes first to a waitlisted test client, then to a standalone client.
5. Standalone consults (A$130, GST-free, R) are upside only and are NOT counted in any money figure.

## 6. Results calls and messages

Rule: the midwife phones only abnormal results. Normal results get a generic message. Lab turnaround, how the client sees the result, and who may send it: NOT IN REPO. All wording: Catherine to confirm privacy. Nothing is sent.

**Text/SMS (no health detail):**
> "GTT Center Perth: your result is ready. Please check your email. Regards."

**Email (normal result):**
> Subject: Your result is ready
> Hello [first name], your result is ready. [How to see it: NOT IN REPO]. If you have questions, or you feel unwell, please contact your doctor or midwife. In an emergency call 000. Regards. GTT Center Perth

**Abnormal result, phone call (midwife):**
> "Hello [first name], this is [name], the midwife from GTT Center Perth. Is now a good time to talk in private? Before I go on, can you tell me your date of birth?" Then explain the result and the next step for her own doctor or midwife.

If she does not answer (U, lead midwife and Catherine to set): try again later the same day; if still no answer, send "GTT Center Perth: please call us today on [phone, NOT IN REPO]. Regards." and leave no detail on voicemail. Missed and no contact: record each attempt.

## QUESTIONS FOR ANTHONY

1. 25 or 30 minute blocks?
   - A: 25 minutes. B: 30 minutes. C: 25 minutes inside, shown to clients as "about 30 minutes" (not recommended).
   - Recommendation: A.
2. Meal break: how do we get all 18 blocks?
   - A: Shift ends 16:15 (about A$92.32 a week, E). B: Keep 16:00 and accept 17 blocks (102 a week). C: Paid short break, no unpaid break (cost NOT IN REPO).
   - Recommendation: A, after the Fair Work check.
3. Should an abnormal-result call be tried twice (same day) before the "please call us" text?
   - A: Yes. B: Three tries. C: Lead midwife decides.
   - Recommendation: C.

Regards.
Grace
