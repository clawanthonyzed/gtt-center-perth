# THEODORE R22C PART 1: cashflow timeline, repaying the owners' start-up money first

Author: Theodore (financial consultant, GTT Center Perth). Date 2026-10-26. General knowledge and the repo's own figures, not your personal documents. Verify before acting. Not tax advice; accountant to confirm. Nothing sent. Tags: R repo, E estimate, U unverified.

## READ-FIRST CHECK (GTT-READ-FIRST.md, 2026-10-26)

- Venue manager starts 06:30 (Mon to Fri 06:30 to 15:00); 07:00 is the first draw.
- Path A = PREFERRED, package WITH the GTT midwife consult. Path B = NOT preferred, outside referral, no GTT consult.
- Prices: Path A A$320 / A$370 shown, GTT charges A$292.15 / A$342.15. Path B A$300 / A$350 all in, GTT charges A$272.15 / A$322.15.
- Rebates used: consult A$32.95 + lab A$22.05 = A$55.00.
- Midwife on site 08:00 to 16:00, first consult 08:15, 25 minute blocks to 10:30, then normal midwife bookings.
- Late rule: from the appointment time onwards; a consult may allow 5 to 10 minutes if the midwife can finish in the time left (OPEN).

## 1. The idea in plain words

The owners put start-up money into the company as a **shareholder loan** (a written loan, signed before the money moves). The company pays that loan back first, month by month. Only when the loan is at zero can a dividend be declared. Repaying a loan is giving the owners their own money back, not income. Part 2 explains the rules.

Locked profit (R): A$26,631.97 a month before company tax, A$19,973.98 after 25 percent company tax. The model is `theodore_r22c.py` (the repo calculator `theodore_r22.py` with its Center of Truth writer switched off, plus the loan timeline at the bottom). Results: `theodore_r22c_results.json`.

## 2. What the repo does and does not have

| Item | In the repo? | Tag |
|---|---|---|
| Start-up planning figure | A$251,198 pre-opening capital (Anthony approved in principle 2026-08-10). Excludes the working capital reserve | R |
| Working capital reserve | A$85,000 to A$110,000, built on the older model (stale) | R |
| Your figures A$250,000 to A$336,000 | A$336,000 is almost exactly A$251,198 + A$85,000 = A$336,198. A$250,000 is almost the pre-opening figure alone | E (my reading) |
| Owners' joint savings | About A$200,000, self-funded, no external investor (repo CLAUDE.md, corrected 2026-07-29) | R |
| How the gap above A$200,000 is funded | NOT IN REPO. See question 1 | |
| Revenue ramp | 43, 64, 79, 93, 100 percent in months 1 to 5 (revenue_ramp.yml, Table 1) | R |
| Cost ramp | Repo cost model: costs are nearly fixed (rise only A$900 from month 1 to month 5) | R |
| Final start-up cost list on today's prices | NOT IN REPO | |

The A$250,000 to A$336,000 range is more than the joint savings of about A$200,000. That gap is A$50,000 to A$136,000, and the repo does not say who lends it. Possible routes (for the accountant and lender, none assumed): a bank or equipment loan to the company, staged payments, or a smaller opening. Each changes the repayment order, so the answer is a question for you.

## 3. Method (simple on purpose)

1. Month 0: the owners lend the capital. The company spends A$251,198 on start-up. What is left is opening cash (high case A$84,802; low case minus A$1,198, so it starts short).
2. Ramp months 1 to 4 (E): profit = locked steady profit minus (1 minus ramp percent) times locked revenue ex GST of A$153,826.03, because the repo cost model treats costs as fixed. Month 5 on = locked steady state.
3. Company tax at 25 percent is charged only once cumulative profit is above zero (early losses carried forward, a simplification).
4. If cash runs out the owners must lend more (shown as top-up). No repayment before month 5, so the reserve is not repaid and then missed.
5. From month 5, all cash above zero repays the loan. First dividend month = the month after the loan reaches zero.

## 4. The two timelines (conservative main case, A$ per month)

| | Low case A$250,000 | High case A$336,000 |
|---|---|---|
| Month 0 start-up spend | A$251,198 | A$251,198 |
| Opening cash after start-up | -A$1,198 | A$84,802 |
| Month 1 (43 percent), cash after tax | -A$61,048.87 | -A$61,048.87 |
| Month 2 (64 percent) | -A$28,745.40 | -A$28,745.40 |
| Month 3 (79 percent) | -A$5,671.50 | -A$5,671.50 |
| Month 4 (93 percent) | A$15,864.15 | A$15,864.15 |
| Month 5 on, cash for repayment | A$26,631.97 (no tax yet), then A$26,558 in month 7, then A$19,973.98 | same |
| Extra owner top-up needed | **A$96,663.78** | **A$10,663.78** |
| Total owners lend by month 3 | A$346,663.78 | A$346,663.78 |
| Loan balance, end month 6 | A$277,535.69 | A$277,535.69 |
| Loan balance, end month 12 | A$151,107.40 | A$151,107.40 |
| **Month the loan is cleared** | **Month 20** | **Month 20** |
| **First dividend month** | **Month 21** | **Month 21** |

Both cases end at the same place because the company needs about A$346,700 in total to get through the ramp on this basis. The A$250,000 owners simply have to find about A$86,000 more, in months 1 to 3. The A$336,000 owners are short by about A$10,700.

## 5. Sensitivity

| Basis | Low case cleared | High case cleared | Top-up low / high |
|---|---|---|---|
| Main: costs fixed, locked revenue | Month 20 | Month 20 | A$96,663.78 / A$10,663.78 |
| Repo tools' own ramp shortfall (older price basis) | Month 19 | Month 19 | A$82,302.31 / A$0.00 |
| Simplification: A$19,973.98 from month 1, no ramp | Month 13 | Month 13 | A$0 / A$0 |

The no-ramp line is shown only to size the error. It is not a forecast, because it ignores the ramp-up losses the repo itself expects.

## 6. NOT MODELLED (do not rely on these months to the day)

- Company tax instalment timing: tax is charged in the month the profit arises. Real instalments and the first return lag.
- GST and BAS timing: quarterly GST cash, the GST held, and refunds on set-up costs.
- Working capital beyond the repo reserve: wages before takings, deposits, bonds, stock, prepaid float.
- The start-up cost list: only the A$251,198 planning figure exists; no final list on today's prices.
- Break-even and cash flow re-run on current prices: the ramp is the older 43/64/79/93/100 curve.
- Depreciation, tax losses carried beyond a simple rule, interest on any loan, bank fees.
- Excluded as locked: interest on prepaid money, standalone consults, card quotes, Package 2, retail, post-test discount.

## QUESTIONS FOR ANTHONY

1. How is the gap above the owners' joint savings of about A$200,000 funded? Options: (a) a bank or equipment loan to the company, (b) a smaller opening, (c) another lender. Recommendation: (b) or (a) with the accountant, then I re-run the timeline with the real loan terms.
2. Do you want a cash floor (for example A$50,000 kept in the company before any repayment)? Recommendation: yes, it delays clearing by about 2.5 months.

Regards.
Theodore
