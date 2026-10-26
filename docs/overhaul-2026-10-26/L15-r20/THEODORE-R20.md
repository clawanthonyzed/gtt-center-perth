# THEODORE R20: Money after the consult rise to A$130

Theodore, financial and tax consultant, GTT Center Perth. 2026-10-26.
Numbers come from [theodore_r20.py](theodore_r20.py) (results in [theodore_r20_results.json](theodore_r20_results.json)). It reuses the same engine as before and the repo's own model, run live. Nothing was sent to anyone. This is general knowledge and desk research, not your personal documents. Verify before acting.

Tags: **R** repo figure, **V** official source, **E** estimate, **U** unverified, **Q** quote needed. All amounts are Australian dollars (A$).

## The answer in one box

| Question | Answer |
|---|---|
| Profit each month before company tax (GTT clients only) | **A$26,631.97** |
| Company tax at 25 percent | -A$6,657.99 |
| **Net profit each month after GST, card fees, payroll tax and company tax** | **A$19,973.98** |
| Is it above A$20,000 a month after tax? | **No. It is A$26.02 short.** About A$34.70 more profit before tax would reach it |
| Standalone private consults (upside, not in the line above) | +A$2,022.96 (low) / +A$4,855.11 (middle) / +A$9,833.47 (high) a month after tax. Any of the three takes the total above A$20,000 |

The headline counts only the 18 GTT clients each morning. Standalone consults, prepaid interest and the refund policy are shown separately and are not in it.

## 1. The locked case, line by line

### 1.1 Monthly profit and loss (whole venture: Holdings, Medical and Lounge)

| Line | A$ a month | Tag |
|---|---|---|
| Lounge + service, morning, ex GST (473.94 clients) | 69,863.50 | R volume, E split |
| Afternoon sales, ex GST | 22,350.34 | R |
| Consult, GST-free (473.94 x A$130) | 61,612.20 | E |
| **Revenue, ex GST** | **153,826.03** | |
| Repo staff, super and workers comp | -93,595.63 | R |
| Repo running costs | -14,288.34 | R |
| GST credits on costs | +1,262.58 | R |
| Card fees, morning (on A$292.15 each) | -2,497.66 | E |
| Card fees, afternoon | -480.99 | E |
| Midwife wages | -12,000.38 | E |
| Midwife fixed costs and consumables | -2,840.65 | E |
| Venue manager 06:30 start | -500.28 | R rate |
| WA payroll tax, whole group | -1,344.04 | E |
| Three-company running cost | -908.67 | E |
| **Profit before company tax** | **26,631.97** | |
| Company tax 25 percent | -6,657.99 | E |
| **Net profit, the number compared with A$20,000** | **19,973.98** | |

GST passed on to the ATO is not revenue: A$6,985.88 on the morning lounge part and A$2,235.03 on afternoon sales. The consult is GST-free, so the A$130 carries no GST.

### 1.2 What one client's money does (Package 1)

| Step | A$ per client |
|---|---|
| Full advertised price, shown at checkout | 320.00 |
| Lab fee, paid by the client to the lab (never GTT money) | -27.85 |
| **Client pays GTT** (consult 130.00 + lounge and service 162.15) | **292.15** |
| GST inside the lounge and service part, passed to the ATO | -14.74 |
| Card fee on the full A$292.15 | -5.27 |
| GTT keeps from the morning package | 272.14 |
| Plus afternoon sales per morning client (see section 4) | +46.14 |
| Repo staff | -197.48 |
| Repo running costs, after GST credits | -27.48 |
| Midwife wages | -25.32 |
| Midwife fixed costs and consumables | -5.99 |
| Venue manager 06:30 | -1.06 |
| Payroll tax | -2.84 |
| Three-company running cost | -1.92 |
| **Profit per client before company tax** | **56.19** |
| Company tax 25 percent | -14.05 |
| **Net per client** | **42.14** |

Package 2: the client pays GTT A$342.15 (consult A$130 plus lounge and service A$212.15), full price A$370.

What the client gets back: Medicare pays her A$55.00 in total. That is the **consult A$32.95 plus the lab test A$16.95 plus collection A$5.10 (A$22.05 for the lab)**. The A$55 is the total for both. The consult alone is A$32.95. Her own cost after Medicare is A$265.00 (Package 1) or A$315.00 (Package 2), lab fee included. The rebates follow the Medicare schedule, so they do not move with the A$20.

### 1.3 Card fee rate check

The model charges 1.7 percent plus A$0.30 on every card payment (E): A$5.27 on A$292.15. The repo lists two providers, Tyro at 1.4 percent and Square at 1.6 percent for cards present, and has not chosen one (R, opex.yml). Those have no A$0.30. At 1.6 percent the card fee is A$4.97 and net profit rises to about A$20,097 (E). So the model is the cautious case.

### 1.4 What would push it over A$20,000

| Lever | Effect on net a month | Status |
|---|---|---|
| Card provider at the repo's 1.6 percent rate | about +A$123 | E, provider not chosen |
| Any standalone consults (section 2) | +A$2,023 and up | E, assumption |
| Keep the 10 percent post-test discount out of the headline (as now) | 0 | flagged below |

Flagged, not deducted: the 10 percent post-test discount adopted on 2026-10-17. The repo estimates it at -A$1,386.27 a month before tax at 25 percent take-up (R). If it were deducted the net would be about A$18,934 (E). It stays out of the headline until you decide.

## 2. Midwives, 08:00 to 16:00

### 2.1 Honest paid hours

| Item | Value |
|---|---|
| On site per shift | 8.0 hours |
| Unpaid meal break (E, check the award) | 0.5 hour |
| Paid per shift | 7.5 hours |
| Shifts per midwife per fortnight | 6 (Mon-Wed one fortnight, Thu-Sat the next) |
| **Paid hours per midwife per fortnight** | **45.0** (on site 48.0) |
| Paid hours per midwife per week, averaged | 22.5 |
| Paid hours, both midwives, per week | 45.0 |
| Cost per midwife per fortnight, loaded (on-cost 1.366) | A$2,769.32 (E) |
| Both midwives per month, wages | A$12,000.38 (E) |
| Fixed costs and consumables per month | A$2,840.65 (E) |

The earlier start moves the hours earlier in the day and does not add paid hours. The casual midwife covers leave and is inside the 1.366 on-cost. Basis used: the Center of Truth, on-cost 1.366, blended A$45.06 an hour before on-cost (Nurses Award RN L2 pp4, 150 percent Saturday).

**Sensitivity only, not the headline:**

| Basis (labelled) | Midwife wages | Net a month | Change |
|---|---|---|---|
| On-cost 1.20, no leave cover | A$10,543.26 | A$21,155.56 | +A$1,181.58 |
| Break paid, so 8.0 paid hours a shift and 48 a week | A$12,800.41 | A$19,336.44 | -A$637.54 |

### 2.2 Where the midwife time goes

| Item | Value |
|---|---|
| GTT consults | 18 each day x 20 minutes = 6.0 hours (advance and same-day) |
| Paid time each day | 7.5 hours = 22.5 slots of 20 minutes |
| GTT share of the paid time | 80 percent |
| Spare for standalone consults | **4 whole slots a day** (10 minutes left over) = 24.3 a week, 105.3 a month |

### 2.3 Standalone private consults at A$130, GST-free (upside only)

Reed read the market and found no Perth data on how many women book a standalone private midwife consult, so these take-up levels are Reed's assumptions ([REED-R20.md](REED-R20.md) section 3.2): low 5 a week, middle 12 a week, high the full spare capacity.

| | Low | Middle | High |
|---|---|---|---|
| Consults a week | 5 | 12 | 24.3 |
| Consults a month | 21.7 | 52.0 | 105.3 |
| Share of spare slots used | 21 percent | 49 percent | 100 percent |
| Takings (GST-free) | A$2,816.67 | A$6,760.00 | A$13,691.60 |
| Card fees (1.7 percent + A$0.30 on A$130 = A$2.51 each) | -A$54.38 | -A$130.52 | -A$264.35 |
| Consumables (A$3.00 each, E) | -A$65.00 | -A$156.00 | -A$315.96 |
| Extra midwife wages | A$0 | A$0 | A$0 |
| **Extra profit before company tax** | A$2,697.28 | A$6,473.48 | A$13,111.29 |
| Company tax 25 percent | -A$674.32 | -A$1,618.37 | -A$3,277.82 |
| **Extra net profit** | **A$2,022.96** | **A$4,855.11** | **A$9,833.47** |
| Headline plus this upside (net) | A$21,996.94 | A$24,829.09 | A$29,807.45 |

Why wages are A$0 here: the midwives are already paid for the 45 hours in the headline, so a standalone consult in a spare slot only adds the card fee and the consumables. Reed's rough figure of about A$107 a consult takes off a share of midwife pay as well. Both are fair views. Mine matches how the books work, and I would plan on the low case.

One consult: the client pays A$130, no GST. GTT keeps about A$124.49 before tax. The client gets A$32.95 back and nets A$97.05.

**GST note.** The sale is GST-free (your locked fact: medical, item 82105). A GST-free sale still lets the company claim the GST on its costs, so there is no apportionment cut on the credits (E, I did not verify an ATO ruling for midwife consults; the accountant should confirm). Medical and Lounge sit in one GST group, so no GST passes between them.

**Payroll tax.** The group pays A$1,344.04 a month. Taxable group wages are about A$1,254,145 a year, A$254,145 over the A$1,000,000 threshold (E). Standalone consults inside the 45 paid hours add no wages and so no payroll tax. If you added paid hours to chase more consults, each extra paid midwife hour costs about A$61.54 in loaded wages plus about A$3.85 of payroll tax (E).

## 3. Market check on A$130

Reed's table ([REED-R20.md](REED-R20.md) section 1) lists later antenatal visits at A$120 (Cherished Parenting, up to 60 minutes), A$120 (Perth Women's Specialist Clinic), A$130 (POGS) and A$150 (My Midwives, 60 minutes). Those are listed prices read on 2026-10-26.

| Test | Result |
|---|---|
| Is A$130 inside the Perth range for the dollars charged? | **Yes.** It sits between A$120 and A$150 |
| After the A$32.95 rebate | The client nets A$97.05. Cherished nets about A$47, My Midwives about A$74, so ours is higher out of pocket |
| Per minute | A$6.50 a minute for 20 minutes, against A$2.00 to A$2.50 for a 60-minute visit |
| Any Perth 20-minute standalone listing | None found, so there is nothing to match directly |

Reading: for a GTT client the consult is part of a package, so A$130 is easy to accept. A woman shopping only for a private consult will compare it with a 60-minute visit and needs to be told it is a short, fast check. That is why I use the low take-up case for planning. Reed could not confirm the A$32.95 rebate on the public page; AskMBS should confirm it.

## 4. "Afternoon sales per morning client", in plain English

**Where it comes from.** The words are my own label in the per-client table in [theodore_r19.py](../../overhaul-2026-10-19/L14-r19/theodore_r19.py) (the line `"Plus afternoon sales per morning client (ex GST, after card fee)"`). The repo has no line with that name. The repo holds the three inputs behind it:

| Input | Repo source | Value |
|---|---|---|
| Weekday afternoon sales | `data/canonical/revenue_assumptions.yml`, id `rev_pm_weekday_transactions` (10 sessions a day / 1.15 sessions a sale) | 8.6957 sales a day |
| Saturday afternoon sales | same file, id `rev_pm_saturday_transactions` (half the weekday figure) | 4.3478 sales a day |
| Average afternoon sale | `data/canonical/pricing.yml`, id `pm_alacarte_average` | A$117 including GST |

The sum: 210.13 sales a month x A$117 = A$24,585.37 with GST. Take off the GST (divide by 1.1) = A$22,350.34. Take off card fees A$480.99 = A$21,869.35. Divide by the 473.94 morning clients = **A$46.14**.

**What it is.** A way to share the whole month of afternoon sales across the morning clients so one per-client table adds up to the monthly total.

**What it is not.** It is not a promise that each morning client buys A$46.14 of afternoon services. It is not an upsell rate. Most afternoon customers are other people. The afternoon total comes from how many afternoon appointments the staff can serve (10 sessions on weekdays, 5 on Saturday), not from the morning list.

**Does the A$20 consult rise change it?** No. Afternoon prices are not changed (they "will be figured out in time"), the afternoon volume is the same, and the morning client count is the same. It stays A$46.14. One trap: if morning clients ever dropped while the afternoon stayed busy, this per-client number would rise by arithmetic alone and could mislead. Use the monthly total when in doubt.

## 5. Interest on prepaid money over a full 12 months

Your question: "Is that A$89k a month meaning more interest in a full year?"

**Short answer.** The A$89,000 was a standing balance, the amount sitting in the account on an average day. It is not an amount that arrives every month. So you do not multiply it by 12. You earn interest on that balance for 12 months, once.

**Picture a bath.** The tap adds new client money every day, and the drain takes money out when the client visits and the money becomes earned sales that pay wages, rent and the ATO. The water level stays about the same. Interest is earned on the level, not on all the water that ever flowed through.

| Item | Value |
|---|---|
| What GTT holds per client | A$292.15 (the GTT amount only). The lab fee A$27.85 is **never** held: A$0 |
| New client money arriving each month | A$138,461.57 (473.94 x A$292.15) |
| Days held before the visit | 21 (E; the repo has no booking lead time) |
| **Average standing balance** | **A$95,647.80** (was about A$89,100; the A$20 rise adds A$6,547.86) |
| What 12 x the balance would wrongly say | A$1,147,773.60. Do not use this |

**Interest on that balance, simple rate, from opening day** (the balance builds up for the first 21 days, so year 1 is 97.1 percent of a steady year):

| Rate | Status | Interest in the first 12 months | A steady year | After 25 percent company tax (first 12 months) |
|---|---|---|---|---|
| **4.60 percent RBA cash rate** | **V** (a reference rate, not a bank product) | **A$4,273.23** | A$4,399.80 | A$3,204.92 |
| 5.00 percent 3-month business term deposit (Aspire, July 2026) | **U** | A$4,644.81 | A$4,782.39 | A$3,483.61 |
| 4.30 percent CommBank 3-month business term deposit (before the September rise) | **U** | A$3,994.54 | A$4,112.86 | A$2,995.91 |
| 1.00 percent big-bank business saver (page did not load) | **U** | A$928.96 | A$956.48 | A$696.72 |

The only verified rate is 4.60 percent. An at-call business account usually pays less than the cash rate, so treat the first row as the top end until a bank quotes (Q). The money must stay ready for refunds, which suits an at-call account better than a term deposit.

Per month in a steady year the 4.60 percent case is about A$366.65. The A$20 rise adds about A$301 a year at 4.60 percent.

If the money is held for a different time: 7 days gives a balance of A$31,882.60 (about A$1,467 a year at 4.60 percent); 14 days A$63,765.20 (about A$2,933); 28 days A$127,530.39 (about A$5,866). Interest is upside and is not in the headline.

## 6. Refund maths for the 50 percent lounge policy

The rule: the client attends her consult, then misses the test completely or is late. She gets 50 percent of the lounge amount back and pays the full lounge amount again to rebook. The consult stays earned (A$130) and the lab fee is the lab's matter (the lab's own policy is NOT IN REPO). I do not decide the policy. Reed's benchmarks and recommendation are in [REED-R20.md](REED-R20.md) section 2.

**What happens to GTT's money, Package 1 (lounge and service A$162.15):**

| Item | A$ |
|---|---|
| Refund paid to the client (50 percent) | 81.08 |
| GST given back to the ATO through the BAS (1/11) | 7.37 |
| Real cost of the refund before tax | 73.70 |
| Real cost after the company tax saving at 25 percent | 55.28 |
| GTT keeps if she never rebooks | 81.08 (A$73.70 ex GST), for a chair that could not be re-sold |
| Second payment when she rebooks | 162.15, with a new card fee of A$3.06 |
| GTT lounge takings if she rebooks and attends | 243.23 (A$221.11 ex GST) for one visit |

Package 2 (lounge and service A$212.15): refund A$106.08, GST A$9.64, real cost before tax A$96.43, takings if she rebooks A$318.23.

Reading it plainly: if she comes back, GTT ends up A$81.08 ahead of a normal visit, so the rule is not a loss. If she never comes back, GTT keeps A$81.08 and has given up A$81.08 compared with keeping all of it. The original card fee is normally not returned by the card provider (E, provider not chosen, so NOT IN REPO). Staff for that slot are already rostered, so the empty chair still carries its share of wages.

**Other percentages, Package 1 (client's refund / GTT keeps if she never rebooks / takings if she rebooks):**

| Refund | Client gets back | GTT keeps | Takings if she rebooks |
|---|---|---|---|
| 0 percent | A$0.00 | A$162.15 | A$324.30 |
| 25 percent | A$40.54 | A$121.61 | A$283.76 |
| **50 percent** | **A$81.08** | **A$81.08** | **A$243.23** |
| 75 percent | A$121.61 | A$40.54 | A$202.69 |
| 100 percent | A$162.15 | A$0.00 | A$162.15 |

**Illustration only (there is no repo data on no-shows):** at 1, 3, 5 and 10 percent of 473.94 clients missing the test, the refunds come to A$384.25, A$1,152.74, A$1,921.23 and A$3,842.47 a month before GST and tax. After GST and 25 percent company tax the same cases cost A$261.99, A$785.96, A$1,309.93 and A$2,619.86.

## 7. Break-even and cash flow

| Item | Effect | Re-run? |
|---|---|---|
| Extra kept per client (A$20 less the extra card fee of A$0.34) | +A$19.66 before tax | Yes, script |
| Same, per month on 473.94 clients | +A$9,317.66 before tax | Yes, script |
| GST | No change: the consult is GST-free | Yes |
| Prepaid cash held in the account | +A$6,547.86 on average | Yes, script |
| Card fees on A$292.15 | A$5.27 each | Yes, script |
| Break-even clients a day | Moves in the safe direction (each client keeps more) | **Not re-run.** Needs the repo break-even and cash-flow models with new prices |
| Start-up capital and cash runway | Not changed by this work | **Not re-run** |
| Company tax cash timing (instalments) | Not modelled | **Not re-run** |
| Standalone consults, interest, refunds | Upside or cost shown above | Yes, not in headline |

## 8. Center of Truth

[FINANCIAL-CENTER-OF-TRUTH.md](../../FINANCIAL-CENTER-OF-TRUTH.md) is replaced in place with the consult at A$130, the new totals, midwives 08:00 to 16:00, the same-day consult and the word "client". Section 7 holds the banned stale values: the old consult price, the old package prices as GTT-charge figures, the old out-of-pocket figures and the older profit figures. The fact-check tool (`tools/factcheck_locked_facts.py`) reads that table, and it was run on this file, the Center of Truth and the question files with 0 hits (result at the end of the run log).

Other documents (for example the R19 workflow file) still describe the earlier booking order and the later midwife start. They need Grace to update them.

## QUESTIONS FOR ANTHONY

1. **The net lands A$26.02 short of A$20,000 a month. What do you want to do?**
   - A: Accept it as on target and treat standalone consults as the cushion. B: Get a card quote from Tyro and Square first (at 1.6 percent it clears A$20,000). C: Change a price or cost.
   - Recommendation: A and B together.
2. **Same-day consult and the 08:00 start.** A consult takes 20 minutes, so a client drawn at 08:15 or earlier (the first four pairs, 8 of the 18 clients) cannot have a same-day consult after an 08:00 start.
   - A: Same-day consult only for the 08:40 pairs and later. B: A midwife starts earlier on some days (adds paid hours, about A$61.54 plus A$3.85 payroll tax an hour). C: Early pairs must book the consult in advance.
   - Recommendation: C, with A shown on the booking page.
3. **Is the midwife's 30-minute meal break unpaid?** It sets paid hours at 45 or 48 a week.
   - A: Unpaid (45 hours). B: Paid (48 hours, net about A$637.54 a month lower).
   - Recommendation: A, after Grace confirms it against the Nurses Award.
4. **How long before the visit do clients usually pay?** I used 21 days. NOT IN REPO.
   - A: 14 days. B: 21 days. C: 28 days.
   - Recommendation: B for planning only, then replace it with real booking data.
5. **Where should the prepaid money sit?**
   - A: At-call business saver. B: 3-month term deposit. C: Leave it in the main trading account.
   - Recommendation: A, because refunds need the money ready.
6. **Should the 10 percent post-test discount (repo estimate -A$1,386.27 a month before tax) come off the headline?**
   - A: Yes, now. B: Show it as its own line, as now. C: Drop the discount.
   - Recommendation: B until you set the real take-up.
7. **Lounge refund policy.** Which do you want me to cost next?
   - A: The 50 percent rule as it stands. B: 50 percent plus Reed's notice window, medical exception and grace time. C: Stricter, 100 percent kept for a no-show.
   - Recommendation: B, per Reed.
8. **Which standalone take-up should the plan quote?**
   - A: Low (5 a week). B: Middle (12 a week). C: High (full spare capacity).
   - Recommendation: A until real bookings exist.

Regards.
Theodore
