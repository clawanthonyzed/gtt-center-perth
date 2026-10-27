# THEODORE R24 PART 2: phlebotomists move to Medical, payroll tax grouping, cash flow locked

Theodore, financial consultant, 2026-10-27. Numbers from [theodore_r22.py](../L17-r22/theodore_r22.py) (Round 24 block; writer edited, re-run, nothing typed by hand). General knowledge and repo figures, not your personal documents. Not tax advice. Nothing sent. Tags: R repo, V verified source, E estimate, U unverified.

## READ-FIRST CHECK

- Venue manager starts 06:30 (Mon to Fri 06:30 to 15:00); 07:00 is the first draw. A hired venue manager, not Anthony.
- Path A = PREFERRED, package with the GTT midwife consult. Path B = NOT preferred, outside referral, no GTT consult. Path B is not limited.
- Prices: Path A A$320 / A$370 (GTT charges A$292.15 / A$342.15). Path B A$300 / A$350 all in (GTT charges A$272.15 / A$322.15).  <!-- factcheck:ok -->
- Rebates: consult A$32.95 + lab A$22.05 = about A$55.00.
- Midwives 08:00 to 16:00, first consult 08:15, 25 minute blocks to 10:30.
- Late rule: arrive 10 minutes early; late from the appointment time. Blood draws: no wiggle room. Consults: 10 minute grace window.

## 1. Phlebotomists employed by GTT Medical (locked)

Phlebotomist cost (R, tools/cost_ramp_model.py): weekday A$9,075.00 + Saturday A$618.75 x 4.33 = **A$11,754.19 wages a month**; with super and workers comp (same 13.7% load the model uses) **A$13,364.52**. This moves from Lounge to Medical.

| A$ a month | Medical before | Medical after | Lounge before | Lounge after | Group |
|---|---|---|---|---|---|
| Revenue, ex GST | A$61,612.20 | A$61,612.20 | A$92,213.83 | A$92,213.83 | A$153,826.03 |
| Direct costs | A$15,952.43 | A$29,316.95 | A$87,458.40 | A$74,093.88 | A$103,410.83 |
| Profit before shared block | A$45,659.77 | A$32,295.25 | A$4,755.43 | A$18,119.95 | A$50,415.20 |
| Shared-cost block (one block, with Lounge: lease and venue manager) | A$0.00 | A$0.00 | -A$23,783.23 | -A$23,783.23 | -A$23,783.23 |
| Profit before tax | A$45,659.77 | A$32,295.25 | -A$19,027.80 | -A$5,663.28 | **A$26,631.97** |
| Company tax 25% | A$11,414.94 if alone | A$8,073.81 if alone | A$0.00 (loss) | A$0.00 (loss) | **A$6,657.99** consolidated |
| Profit after tax | | | | | **A$19,973.98** |

Holdings: no sales, nothing to show. **Headline check: unchanged, A$26,631.97 before tax and A$19,973.98 after** (the script asserts this; it stops if either moves). Lounge carries a 1 cent rounding. The room fee Medical pays Lounge is NOT IN REPO; it only moves profit between the two companies. With consolidation the group pays 25% on the total, so the Lounge loss is used.

Legal note (not a question): DECISION-LOG 2026-10-20 flagged Medicare s16A(5AB)(c) on who employs collectors. Anthony has locked Medical; Catherine confirms the compliant set-up.

## 2. WA payroll tax grouping

The three companies are grouped: Holdings owns 100% of Medical and Lounge (related bodies corporate; one set of owners holds a controlling interest of more than 50%) (V, [wa.gov.au grouping page](https://www.wa.gov.au/government/multi-step-guides/payroll-tax-employer-guide/grouping-payroll-tax-employer-guide), read 2026-10-27 via crawl4ai).

| Item | Value | Tag |
|---|---|---|
| Grouped wages, a year (all three) | **A$1,254,144.89** (unchanged by the move: same people, different employer) | R |
| Threshold | A$1,000,000 a year; from 1 July 2023 | V, [wa.gov.au calculation page](https://www.wa.gov.au/government/multi-step-guides/payroll-tax-employer-guide/calculation-payroll-tax-employer-guide), updated 2 Jun 2026 |
| Taper | Deductible amount = A$1,000,000 - (wages - A$1,000,000) x 2/13; nil from A$7,500,000 | V, same page |
| Group deductible amount | A$960,900.79, claimed only by the designated group employer | V rule, R maths |
| Taxable wages | A$293,244.10 | maths |
| Payroll tax at 5.5% | A$16,128.43 a year = **A$1,344.04 a month** (unchanged) | V rate |
| Wage share | Medical about 24%, Lounge about 76% | E |

Each company registers and lodges its own return, but tax is worked out on the group's total wages, and every member is jointly and severally liable. Recommendation: Lounge as designated group employer (WA's default is usually the member with the most WA wages). Payroll tax grouping is separate from the GST group and consolidation.

## 3. Approved cash flow, locked

Anthony approved the 24-month cash flow (company tax, GST, working capital) on 2026-10-27: [THEODORE-R23-CASHFLOW.md](../L18-r23/THEODORE-R23-CASHFLOW.md). It is now an APPROVED reference table in the Center of Truth (section 4C). No figure changed (results JSON identical after re-run). The loan repayment timing (month 13 / 14) and the A$50,000 cash-floor scenario (month 15 / 16) are labelled **"illustrative, not decided, deferred by Anthony"** in the Center of Truth, the cash flow file, THEODORE-R23-PART-3 and the Route B memo; numbers kept. The funding question above joint savings is removed from every open list.

## 4. Files changed

- docs/FINANCIAL-CENTER-OF-TRUTH.md and L17-r22/center_of_truth.yml (regenerated): phlebotomist employer line, sections 4A company split, 4B payroll tax, 4C approved cash flow, Path B fact line, late rule split, payroll tax row V, change log R24.
- L17-r22/theodore_r22.py (Round 24 block and writer), theodore_r22_results.json.
- L18-r23/theodore_r23_cashflow.py (labels only), THEODORE-R23-CASHFLOW.md, THEODORE-R23-PART-1.md (Path B neutral), PART-2 (questions answered), PART-3 and ROUTE-B-CAPITAL-RETURN-MEMO-R23.md (deferred labels).

The Center of Truth is about 18,000 characters: it is the one generated file, so it is not split.

## QUESTIONS FOR ANTHONY

None needed.

Regards.
Theodore
