# R1: Adaptive phlebotomist rostering (workstream M2, 2026-10-17)

This is general knowledge, not your personal documents. Verify with a qualified adviser before acting. Clinical, award and Medicare points below are for Anthony, the pathology partner and the accountant to confirm; nothing here has been sent to anyone.

## 1. Decision implemented

Anthony (2026-10-17): phlebotomists are rostered adaptively from confirmed advance bookings, like every other role. The fixed minimum of 2 per GTT morning is retired. Workings use the repo's own solvers with one input changed (the phlebotomist count per morning is taken from the solver's draw-concurrency check instead of fixed at 2). Drivers: `m2_driver.py`, `m2_part2.py`, `m2_part3.py` in this folder; they wrap `tools/am_volume_tier_staffing_solver.py`, `tools/cost_ramp_model.py` and `tools/am_demand_tier_financial_ladder.py` and write no new calculator. Controls that pass: 18 clients still reproduces A$107,883.97 total cost and +A$35,186.40 a month; the previous break-even 8.266 is reproduced when the second phlebotomist is forced back in.

## 2. The rule (from the repo's own logic)

Why one phlebotomist can carry up to 9 clients: the solver (`phlebotomist_headcount_check_odd`) models each draw as 5 minutes (`DRAW_MINUTES`) at 0, 60 and 120 minutes after the client's slot. With pairs 25 minutes apart and one client per slot, the draws of every client land at 0, 10 and 20 minutes into each 25-minute cycle, so no two draws overlap and peak draw concurrency is 1. As soon as two clients share a slot (the tenth booking onward) two draws fall at the same time and peak concurrency is 2. The collector is drawing 15 of every 25 minutes (three 5-minute draws), leaving 10 free minutes per cycle.

| Confirmed bookings that morning | Phlebotomists rostered | Second collector |
|---|---|---|
| 0 | 0 | none |
| 1 to 9 (no two clients in the same slot) | **1** (Chair A) | **On call**, named on the roster, not paid unless called in (Option 1, assumed; Options 2 and 3 in section 3) |
| 10 to 18 (two chairs running pairs) | **2** (Chair A and Chair B) | The pool supplies cover for absence only |
| Afternoon (any volume) | **0** | not applicable |

Booking order rule used by the roster: bookings fill the 07:00 slot first and one client per slot (Chair A) until all nine slots hold one client; the tenth booking opens Chair B. The roster is published 1 to 2 weeks ahead from the confirmed bookings; a morning's phlebotomist count is re-checked by the solver on the actual slot list, so a morning of 9 with two clients stacked in one slot still gets 2.

The afternoon needs no phlebotomist: the afternoon roster is the four afternoon therapists plus the Venue Manager (no phlebotomy line in the afternoon labour of A$12,704.74), the phlebotomist shift is AM only (07:00 to 13:00, `STAFFING-COVERAGE-VALIDATION.md` section 2 wage table), and the last draw of the last client ends at 12:25 (last first draw 10:20 + 120 minutes + 5-minute draw), inside the morning shift.

## 3. The on-call second collector: options and costs

The repo supports two prices: the casual three-hour minimum engagement (`CASUAL_MINIMUM_ENGAGEMENT_HOURS` = 3.0 in `tools/cost_ramp_model.py`, marked VERIFIED in the wages file) and its own relief method, where a relief person works the full 6-hour shift (`FINANCIAL-FIGURE-REFERENCE.md` section 5). It does **not** contain a paid standby or on-call allowance, so none is invented here (Option 4, TO CONFIRM against the award).

| Option for mornings of 9 or fewer | Phlebotomist cost | Extra cost a month | Net operating profit a month at 9 booked | Break-even | Basis |
|---|---|---|---|---|---|
| 0. Previous rule: 2 phlebotomists, full 6-hour shift | 2 x 6 hours | A$0.00 (reference) | A$4,834.58 | 8.266 | Previous model |
| 1. **Adaptive: 1 phlebotomist; the second collector is called in only if needed** | 1 x 6 hours + call-in when needed | A$0.00 with no call-ins | A$11,516.81 | **7.250** | Repo solver draw check. Call-in cost is separate, next table |
| 2. Adaptive plus a short second shift (3 hours, 07:00 to 10:00) on every such morning | 1 x 6 + 1 x 3 hours | A$3,341.13 | A$8,175.68 | 7.758 | Three-hour casual minimum engagement (repo, verified) |
| 3. Adaptive plus a second collector on every such Saturday only | 1 x 6 + 1 x 6 hours on Saturdays | A$1,523.12 | A$9,993.69 | 7.482 | Repo Saturday rate (A$51.5625 an hour); proposal, see the safety note |
| 4. Paid standby allowance for the on-call collector | not in the repo | not modelled | not modelled | not modelled | **No allowance rate exists in the repo and none is invented. The award and the lab would set it. TO CONFIRM** |

Cost of a call-in (a casual second collector called in for a difficult draw, a faint, or a late clinical need) at A$34.375 an hour weekday and A$51.5625 Saturday, with super 12% and workers compensation 1.7%:

| Call-ins a month (second collector attends) | Cost at the 3-hour minimum | Cost if she works the full 6-hour shift | Break-even added (3-hour call-ins) | Break-even with the call-ins |
|---|---|---|---|---|
| 0 | A$0.00 | A$0.00 | +0.000 | 7.250 |
| 2 | A$234.51 | A$469.01 | +0.036 | 7.286 |
| 4 | A$469.01 | A$938.02 | +0.071 | 7.322 |
| 8 | A$938.02 | A$1,876.05 | +0.143 | 7.393 |
| 13 | A$1,524.29 | A$3,048.58 | +0.232 | 7.482 |
| 26 | A$3,048.58 | A$6,097.16 | +0.463 | 7.714 |
| One call-in | A$117.25 weekday / A$175.88 Saturday | A$234.51 weekday / A$351.76 Saturday | | |

What is assumed: Option 1 is the headline because it is exactly what the repo solver produces and invents no payment. It **assumes** a casual on-call collector will attend when called without a standby payment; a casual cannot be compelled to be available, so if a guaranteed second pair of hands is needed on light mornings, Option 2 (7.758 break-even) is the practical form and still beats the previous rule (8.266). The number of call-ins a month is **not known** (no data); the table shows the cost per call-in so any rate can be read off. Even a call-in on every single trading day adds only 0.463 to break-even.

## 4. Before and after, 1 to 18 booked clients

Planning case (bookings one per slot first), 25-minute cadence, 6-hour shifts, on-costs 13.7% (super 12% + workers compensation 1.7%), 22 weekdays + 4.33 Saturdays. Net operating profit = morning contribution + afternoon revenue A$24,585.37 - fixed costs A$36,738.11. Previous rule had 2 phlebotomists at every volume.

| Booked | Phlebotomists before / after | Weekday labour before | Weekday labour after | Contribution per weekday morning (after) | Contribution per Saturday (after) | AM labour per month (after) | Net operating profit per month before | Net operating profit per month after | Change per month |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 2 / 1 | A$975.96 | A$741.45 | -A$491.45 | -A$862.17 | A$21,127.63 | -A$33,380.10 | -A$26,697.87 | A$6,682.23 |
| 2 | 2 / 1 | A$1,482.90 | A$1,248.39 | -A$748.39 | -A$1,372.59 | A$35,572.95 | -A$41,242.92 | -A$34,560.69 | A$6,682.23 |
| 3 | 2 / 1 | A$1,482.90 | A$1,248.39 | -A$498.39 | -A$1,122.59 | A$35,572.95 | -A$34,660.42 | -A$27,978.19 | A$6,682.23 |
| 4 | 2 / 1 | A$1,482.90 | A$1,248.39 | -A$248.39 | -A$872.59 | A$35,572.95 | -A$28,077.92 | -A$21,395.69 | A$6,682.23 |
| 5 | 2 / 1 | A$1,482.90 | A$1,248.39 | A$1.61 | -A$622.59 | A$35,572.95 | -A$21,495.42 | -A$14,813.19 | A$6,682.23 |
| 6 | 2 / 1 | A$1,482.90 | A$1,248.39 | A$251.61 | -A$372.59 | A$35,572.95 | -A$14,912.92 | -A$8,230.69 | A$6,682.23 |
| 7 | 2 / 1 | A$1,482.90 | A$1,248.39 | A$501.61 | -A$122.59 | A$35,572.95 | -A$8,330.42 | -A$1,648.19 | A$6,682.23 |
| 8 | 2 / 1 | A$1,482.90 | A$1,248.39 | A$751.61 | A$127.41 | A$35,572.95 | -A$1,747.92 | A$4,934.31 | A$6,682.23 |
| 9 | 2 / 1 | A$1,482.90 | A$1,248.39 | A$1,001.61 | A$377.41 | A$35,572.95 | A$4,834.58 | A$11,516.81 | A$6,682.23 |
| 10 | 2 / 2 | A$1,989.84 | A$1,989.84 | A$510.16 | -A$484.76 | A$56,700.52 | -A$3,028.26 | -A$3,028.26 | A$0.00 |
| 11 | 2 / 2 | A$2,496.78 | A$2,496.78 | A$253.22 | -A$995.18 | A$71,145.86 | -A$10,891.10 | -A$10,891.10 | A$0.00 |
| 12 | 2 / 2 | A$2,496.78 | A$2,496.78 | A$503.22 | -A$745.18 | A$71,145.86 | -A$4,308.60 | -A$4,308.60 | A$0.00 |
| 13 | 2 / 2 | A$2,496.78 | A$2,496.78 | A$753.22 | -A$495.18 | A$71,145.86 | A$2,273.90 | A$2,273.90 | A$0.00 |
| 14 | 2 / 2 | A$2,496.78 | A$2,496.78 | A$1,003.22 | -A$245.18 | A$71,145.86 | A$8,856.40 | A$8,856.40 | A$0.00 |
| 15 | 2 / 2 | A$2,496.78 | A$2,496.78 | A$1,253.22 | A$4.82 | A$71,145.86 | A$15,438.90 | A$15,438.90 | A$0.00 |
| 16 | 2 / 2 | A$2,496.78 | A$2,496.78 | A$1,503.22 | A$254.82 | A$71,145.86 | A$22,021.40 | A$22,021.40 | A$0.00 |
| 17 | 2 / 2 | A$2,496.78 | A$2,496.78 | A$1,753.22 | A$504.82 | A$71,145.86 | A$28,603.90 | A$28,603.90 | A$0.00 |
| 18 | 2 / 2 | A$2,496.78 | A$2,496.78 | A$2,003.22 | A$754.82 | A$71,145.86 | A$35,186.40 | A$35,186.40 | A$0.00 |

Reading it: mornings of 1 to 9 improve by A$6,682.23 a month each (A$234.51 a weekday morning, A$351.76 a Saturday morning for the second phlebotomist). Mornings of 10 to 18 do not change (both chairs run). The valley at 10 to 12 clients stays: 9 booked now earns +A$11,516.81 a month, more than any of 10 to 14 booked (10: -A$3,028.26; 13: +A$2,273.90; 14: +A$8,856.40), because the tenth booking opens Chair B and steps the roster up to 2 phlebotomists and 6 therapists.

## 5. Break-even, recomputed (working as a table)

Method as in the repo ladder (`breakeven_for_headcount`), applied tier by tier: costs = fixed costs + the morning roster that the break-even number of clients needs. 7.250 falls in the tier for 8 booked clients (roster 1 phlebotomist + 4 therapists); the check is that the roster for 7 clients is the same, so the answer is stable inside the tier.

| Step | Working | Before (2 phlebotomists + 4 therapists) | After (1 phlebotomist + 4 therapists) |
|---|---|---|---|
| 1. Fixed costs | rent 8,000 + other overhead 5,088.34 + cost of goods 1,200 + (afternoon labour 12,704.74 + Venue Manager 7,040) x 1.137 | A$36,738.11 | A$36,738.11 |
| 2. Morning roster | wages x 1.137, 22 weekdays + 4.33 Saturdays | + A$42,255.18 | + A$35,572.95 |
| 3. Total costs | step 1 + step 2 | A$78,993.29 | A$72,311.06 |
| 4. Less afternoon revenue | 8.6957 x A$117 x 22 + 4.3478 x A$117 x 4.33 | - A$24,585.37 | - A$24,585.37 |
| 5. Costs the mornings must cover | step 3 - step 4 | A$54,407.92 | A$47,725.69 |
| 6. Revenue per daily client per month | A$250 x 26.33 trading days | A$6,582.50 | A$6,582.50 |
| 7. **Break-even** | step 5 / step 6 | **8.266** | **7.250** |
| 8. Share of 18-a-day capacity | break-even / 18 | 45.9% | 40.3% |
| 9. Margin of safety at 18 | 18 - break-even | 9.734 clients (54.1%) | 10.750 clients (59.7%) |
| 10. GST-stress break-even | whole package and afternoon taxable at 10% | 9.255 | 8.138 |

By booking pattern (all 19,683 ways of placing 1 to 18 bookings in the nine slots were run through the solver):

| Booking pattern | Before: break-even | Before: GST-stress | After: break-even | After: GST-stress |
|---|---|---|---|---|
| Planning case: one client per slot from 07:00 first | 8.266 | 14.083 | **7.250** | 8.138 |
| Cheapest pattern of all 19,683 ways of placing the bookings | 8.266 | 9.255 | 7.250 | 8.138 |
| Bookings stack in pairs from 07:00 (both chairs from the second booking) | 12.655 | 14.083 | 12.655 | 14.083 |

What the headline means: 7.250 morning clients a day if bookings fall one per slot (the booking engine's default order). If clients choose the same slots and stack in pairs from 07:00, both chairs run from the second booking and break-even is unchanged at 12.655. Break-even with a paid 3-hour second shift (Option 2): 7.758; with a call-in every day: 7.714.

## 6. Saturday proof (P18a re-run)

At 18 clients nothing changes: revenue A$4,500.00, labour A$3,745.18 (2 phlebotomists + 8 therapists at 1.5 times), contribution **+A$754.82 a Saturday** (about A$3,268 over 4.33 Saturdays). Lower volumes improve: at 9 booked the Saturday roster is 1 phlebotomist + 4 therapists, labour A$1,872.59, contribution **+A$377.41** (was +A$25.65). Saturday direct-labour break-even falls from 8.90 to **7.49 clients** on the 4-therapist roster; the full 2 + 8 roster still needs 14.98 clients.

## 7. Year 1, GST-stress, peak funding, payback

At the committed 18 a morning, both chairs run every morning, so **these do not change**: Year 1 A$422,236.80 (revenue A$1,716,844.44, costs A$1,294,607.64); GST-stress A$281,310.96; peak funding A$251,198.00 (pre-opening capital, Month 1 already profitable); lowest cash A$85,000.00; payback Month 8 (repo) and Month 11 (after GST). The adaptive rule does not add profit at full capacity; it removes cost on mornings that are not full, which matters because the plan has no ramp-up and fill is the central risk.

| Average morning | Roster before | Roster after | Monthly net before (repo / GST-stress) | Monthly net after (repo / GST-stress) | Year 1 net before (repo / GST) | Year 1 net after (repo / GST) | Payback before (repo / GST) | Payback after (repo / GST) |
|---|---|---|---|---|---|---|---|---|
| 18 (100%) | 2 + 8 | 2 + 8 | A$35,186.40 / A$23,442.58 | A$35,186.40 / A$23,442.58 | A$422,237 / A$281,311 | A$422,237 / A$281,311 | Month 8 / Month 11 | Month 8 / Month 11 |
| 15.3 (85%) | 2 + 8 | 2 + 8 | A$17,413.65 / A$7,285.54 | A$17,413.65 / A$7,285.54 | A$208,964 / A$87,426 | A$208,964 / A$87,426 | Month 16 / Month 35 | Month 16 / Month 35 |
| 12.6 (70%) | 2 + 8 | 2 + 8 | -A$359.10 / -A$8,871.51 | -A$359.10 / -A$8,871.51 | -A$4,309 / -A$106,458 | -A$4,309 / -A$106,458 | none / none | none / none |
| 9 (50%) | 2 + 4 | 1 + 4 | A$4,834.58 / -A$1,523.56 | A$11,516.81 / A$5,158.67 | A$58,015 / -A$18,283 | A$138,202 / A$61,904 | Month 55 / none | Month 23 / Month 51 |

Reading the 9-a-day row: if the waitlist delivers only half a morning, the previous rule would leave the business at a small repo-basis profit (+A$4,834.58 a month) and a loss after GST; under the adaptive rule it earns +A$11,516.81 a month (+A$5,158.67 after GST) and pays back in Month 23. The 85% and 70% rows are unchanged because 15.3 and 12.6 clients a morning still need both chairs (averages hide days under 10; a real fill pattern with quiet mid-week mornings will do slightly better than these rows).

## 8. Headcount on the books and position register

Peak simultaneous need is still 2 phlebotomists (mornings of 10 or more) and 8 therapists. The repo's reliability method (each person unavailable on about 8% of shifts; 4 phlebotomists give 99.81% that at least 2 are available) is unchanged, and the on-call second collector on a light morning is drawn from the same pool, so the pool stays **4 phlebotomists** (3 is the repo's disclosed lower bound at 98.18%). Total on the books stays **21** (12 morning therapists + 4 afternoon therapists + 4 phlebotomists + 1 Venue Manager).

What changes is the use of the pool: at 18 a day, 12 phlebotomist shifts a week over 4 people (3 shifts each, 18 hours); at 9 a day, 6 shifts a week (1.5 shifts each, 9 hours); the second pool member on a light morning is on call. Position changes: GTT-02 (Chair A) is rostered every GTT morning with a booking; GTT-03 (Chair B) is rostered only when 10 or more clients are booked, and is the named on-call second collector otherwise; GTT-04 and GTT-05 stay relief. Exact register wording is in `FOR-DOCUMENTS-AGENT.md`.

**Conflicts flagged:** (a) the phlebotomist job posting offers permanent part-time 25 hours a week, Monday to Friday 07:15 to 12:30 (`docs/phlebotomist-job-posting.md`); an adaptive roster cannot guarantee 25 hours (about 9 to 18 hours a week per person on the 4-person pool), so phlebotomists should be engaged as casual (the cost model already prices casual rates) or on a guaranteed minimum roster, employment type TO CONFIRM with Fair Work; (b) the 2026-09-19 decision records that GTT employs both phlebotomists directly (CLOSED); the Medicare and pathology-licensing position on that is being re-examined by workstream L (section 10).

## 9. Clinical-safety conditions (proposed, to be recorded in the decision log)

Taken from the repo's own protocol (`docs/gtt-clinical-protocol.md` adverse events and difficult venepuncture; the fit-out list in `outputs/FINANCIALS/3-WAY-FINANCIAL-MODEL-AUD.md` includes a vasovagal recovery chair). They are proposals for Anthony and the pathology partner, not clinical advice.

1. **Difficult draw.** Maximum 2 attempts by the first collector. Today the protocol hands over to "the second on-site phlebotomist"; with one collector on light mornings the second is the named on-call collector, and if she cannot attend in time the existing fallback applies (reschedule or refer back to the requesting doctor or midwife, per the pathology partner's protocol). The partner's own escalation steps are TO CONFIRM with them.
2. **Fainting and vasovagal response.** Client kept seated or lying, not allowed to stand; Venue Manager called immediately; 000 if unconscious; vasovagal recovery chair used. A single collector must not leave a recovering client alone, so the Venue Manager (first aider, on site 07:00 to 15:00 Monday to Friday) takes over the client and the collector resumes the next draw; the 10 free minutes in each 25-minute cycle are the only slack, so a faint delays following draws and the roster note must say so.
3. **Saturday.** The Venue Manager does not work Saturdays (an experienced rostered staff member covers). Because no manager is present, this study recommends a second collector on every Saturday (Option 3, A$1,523.12 a month, break-even 7.482) until a first-aid-trained cover person is confirmed. Proposal only; the model headline does not include it.
4. **Named on-call.** Every light-morning roster names the on-call second collector and her phone is reachable from 06:50 to 13:00.
5. **Pathology partner sign-off** that one collector per chair for up to 9 clients meets its collection-site conditions, before this roster is used. If the partner or the Medicare rules require the lab to supply or employ the collectors, the roster becomes the lab's decision (section 10).

## 10. Dependencies and what is open

- **Pathology partner:** whether it requires 2 collectors, and whether collectors must be its employees. TO CONFIRM. The earlier work (2026-10-16) found no regulation in the repo requiring 2.
- **Medicare and lab-employment rules:** workstream L (`docs/overhaul-2026-10-17/L-medicare/`) had not been published when this was written; check it before committing. If the lab must supply or employ the collectors, GTT's phlebotomist wage lines move to a lab fee and the roster follows the lab's staffing rule.
- **Award:** casual minimum engagement (3 hours, VERIFIED in the repo), Saturday penalty (1.5 times assumed), any standby or on-call allowance (none in the repo): TO CONFIRM with Fair Work.
- **Not modelled:** relief for absence (repo allowance A$940.34 a month for phlebotomists is outside the A$78,993.29 and A$72,311.06 totals, as before), call-in frequency, public holiday premiums, shorter shifts on very light mornings (3-hour floor upside, not counted, consistent with the repo).
