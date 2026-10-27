# THEODORE R23 PART 1: why Path B makes GTT less money (plain English)

Theodore, financial consultant, 2026-10-27. Numbers from [theodore_r23_cashflow.py](theodore_r23_cashflow.py), which imports my Round 22 scripts unchanged (theodore_r22c.py and theodore_r22.py). General knowledge and repo figures, not your personal documents. Nothing sent. Tags: R repo, E estimate.

## READ-FIRST CHECK

- Venue manager starts 06:30 (Mon to Fri 06:30 to 15:00). 07:00 is the first draw. Anthony is Owner and Director, not the venue manager.
- Path A = PREFERRED: package with the GTT midwife consult. Path B = NOT preferred: client keeps an outside referral, no GTT consult.
- Prices: Path A A$320 / A$370, GTT charges A$292.15 / A$342.15. Path B A$300 / A$350 all in, GTT charges A$272.15 / A$322.15.  <!-- factcheck:ok -->
- Rebates: consult A$32.95 + lab A$22.05 = A$55.00 (shown as about).
- Midwives 08:00 to 16:00, first consult 08:15, 25 minute blocks to 10:30.
- Late rule: clients arrive 10 minutes early; late means from the appointment time onwards.

## 1. Straight answer

You are right. The midwife roster is fixed Monday to Saturday, and a Path B client never sees our midwife. So **the "roster might shrink" idea from Round 22 is retired.** I tested a "roster flex" case where the midwife cost would go down if fewer clients took the consult. That case is wrong under your rules. It is deleted from all my work from today. Standalone midwife appointments and midwife capacity stay out of every financial.

**The midwife only comes up in Path B for one reason: her wage is a cost we pay every day anyway.** When a client picks Path B, the A$130 consult income is lost, but the wage does not go down. That is the whole story.

## 2. One client: Path A against Path B (Package 1, R)

| Step | Path A | Path B |
|---|---|---|
| Client pays GTT | A$292.15 (consult A$130 + lounge A$162.15) | A$272.15 (all lounge)  <!-- factcheck:ok --> |
| GST inside, passed to the tax office | -A$14.74 (lounge part only) | -A$24.74 (the whole amount is taxable) |
| Card fee | -A$5.27 | -A$4.93 |
| Consult consumables | -A$3.00 | none |
| **GTT keeps** | **A$269.14** | **A$242.48** |
| Midwife wage | paid in full | **still paid in full** (fixed daily wage) |

**Path B gives GTT A$26.66 less per client** (R). Here is where the A$26.66 goes:

| Reason | A$ |
|---|---|
| The client pays GTT A$20.00 less | -A$20.00 |
| More of the money is GST (the A$130 consult was GST-free; on Path B every dollar is taxable) | -A$10.00 |
| Smaller card fee | +A$0.34 |
| No consult consumables | +A$3.00 |
| **Total** | **-A$26.66** |

Same thing said the other way: on Path A the consult line earns A$130 GST-free and keeps about A$124.79 after its card fee and consumables. On Path B the lounge line is A$110 bigger, but after GST and card fee that only adds A$98.13. The midwife's wage (A$12,000.38 a month, R) and her room and fixed costs (A$2,840.65 a month, R) are paid either way, so nothing comes back to cover the gap.  <!-- factcheck:ok -->

**What the retired case did wrong:** it treated the midwife as A$31.31 per client that disappears when a client goes Path B. That made Path B look A$1.65 better than Path A. With your fixed roster, that saving does not exist.

## 3. Whole month: what a Path B share does (473.94 clients a month, R)

| Path B share | Clients a month | About a day | Profit change before tax | Change after 25% tax | Net after tax |
|---|---|---|---|---|---|
| 0% (locked case) | 0 | 0 | A$0.00 | A$0.00 | A$19,973.98 |
| 5% | 23.70 | 0.9 | -A$631.76 | -A$473.82 | A$19,500.16 |
| 10% | 47.39 | 1.8 | -A$1,263.52 | -A$947.64 | A$19,026.33 |
| 20% | 94.79 | 3.6 | -A$2,527.05 | -A$1,895.29 | A$18,078.69 |

Rule of thumb: **every 1 Path B client a day costs about A$702 a month before tax** (26.33 trading days x A$26.66), about A$526 after tax. The locked headline stays A$26,631.97 before tax and A$19,973.98 after, because the plan is 100 percent Path A.

## 4. Path B receipt: Option 3 is the layout (R)

| Line on the Path B receipt | Amount |
|---|---|
| Lounge and service (includes GST A$24.74) | A$272.15  <!-- factcheck:ok --> |
| Consult: not included (outside referral) | A$0.00 |
| Pathology fee: paid to the lab, not to us | A$27.85 |

Source: THEODORE-R22-PART-2.md Option 3, recommended by me and found lawful by Catherine (CATHERINE-R22B-PART-1, item 4). The Lounge company issues it. No consult or GST-free line is ever invented on Path B. Note: I found no DECISION-LOG entry that records your approval of Option 3. If you approve it here, it should be logged (question 1).

## 5. Price where Path B would equal Path A (information only, no price change)

On a fixed roster, Path B would need to be **A$329.88 all in** for Package 1 (GTT charges A$302.03) and **A$379.88** for Package 2 (GTT charges A$352.03) to leave GTT the same as Path A (R, theodore_r22.py break-even). Prices are not changed: Path B stays A$300 / A$350.  <!-- factcheck:ok -->

## QUESTIONS FOR ANTHONY

1. Is Option 3 the locked Path B receipt? Options: (a) yes, Option 3; (b) Option 1, one line. Recommendation: (a), and log it in DECISION-LOG.

Regards.
Theodore
