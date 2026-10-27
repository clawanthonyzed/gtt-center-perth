# THEODORE R25 PART 2: Why GTT Lounge claims the payroll tax group deduction (Question 9)

Theodore, financial consultant, 2026-10-27. Numbers from [theodore_r22.py](../L17-r22/theodore_r22.py) Round 25 block (re-run; headline asserted unchanged). General knowledge, not tax advice. Nothing sent. Tags: R repo, V verified (URL, date read), E estimate.

## READ-FIRST CHECK
- Venue manager starts 06:30 (Mon to Fri 06:30 to 15:00); 07:00 is the first draw. A hired person, not Anthony.
- Path A = PREFERRED, package with the GTT midwife consult. Path B = NOT preferred, outside referral, no GTT consult, not limited.
- Prices: Path A A$320 / A$370 (GTT charges A$292.15 / A$342.15). Path B A$300 / A$350 all in (GTT charges A$272.15 / A$322.15).  <!-- factcheck:ok -->
- Rebates: consult A$32.95 + lab A$22.05 = about A$55.00.
- Midwives 08:00 to 16:00, first consult 08:15.
- Late rule: blood draws no wiggle room; consults 10 minute grace.

## 1. What a designated group employer is
WA treats Holdings, Medical and Lounge as one payroll tax group because Holdings owns all of the other two. The group gets ONE tax-free amount (the "deductible amount"). Only one member, the **designated group employer**, claims it; every member still registers and lodges its own return, and all members are jointly and severally liable for the group's tax. The members nominate the designated group employer; if they do not, the Commissioner picks one, usually the member with the most WA wages (V, [wa.gov.au grouping page](https://www.wa.gov.au/government/multi-step-guides/payroll-tax-employer-guide/grouping-payroll-tax-employer-guide), updated 14 Mar 2026). It "must pay wages in WA" (V, [wa.gov.au calculation page](https://www.wa.gov.au/government/multi-step-guides/payroll-tax-employer-guide/calculation-payroll-tax-employer-guide), updated 2 Jun 2026). At year end the designated group employer lodges the whole group's Australian taxable wages after all members have lodged, and the next year's estimate (V, [wa.gov.au annual reconciliation](https://www.wa.gov.au/government/multi-step-guides/payroll-tax-employer-guide/annual-reconciliation-payroll-tax-employer-guide), updated 2 Jun 2026).

## 2. Wages per company (who employs whom, locked)
| Company | Staff | Wages a month, with super and workers comp | Share | Payroll tax wages a year | Tag |
|---|---|---|---|---|---|
| GTT Medical | 2 midwives + casual cover (A$12,000.38), 2 phlebotomists (A$13,364.52) | A$25,364.90 | 24% | about A$299,834 | R costs, E split |
| GTT Lounge | 8 morning service staff (A$57,781.34), 4 afternoon casuals (A$14,445.29), venue manager 06:30 to 15:00 (A$8,504.76) | A$80,731.39 | 76% | about A$954,311 | R costs, E split |
| GTT Holdings | none | A$0.00 | 0% | A$0.00 | R |
| **Group** | | A$106,096.29 | 100% | **A$1,254,144.89** | R |

Group payroll tax: deductible amount A$960,900.79; tax 5.5% x A$293,244.10 = **A$16,128.43 a year (A$1,344.04 a month)** (V rule, R wages). The yearly split by company uses each company's share of loaded cost (E); the group total is the model figure (R).

## 3. Three choices compared
| Designated group employer | Group payroll tax a year | For | Against |
|---|---|---|---|
| **GTT Lounge (approved)** | A$16,128.43 | Biggest payroll (76%), so it is the member WA would pick anyway. Holds the lease, runs the venue, employs the venue manager who keeps timesheets and payroll records, so the year-end group lodgement sits where the payroll data is. Its wages (about A$954,311) almost use up the deduction (A$960,901) by themselves | Lounge's wages sit about A$6,590 under the deduction (E). Whether WA lets the unused part be used elsewhere in the group: NOT VERIFIED (the WA pages do not say). Worst case about A$362 a year (5.5% of A$6,590, E); accountant to confirm |
| GTT Medical | A$16,128.43 | Simple if it ran payroll | Only 24% of wages (about A$299,834), far below the deduction, so most of the deduction could go unused if WA does not move the excess (NOT VERIFIED). Medical is the clinical company; keep its paperwork simple |
| GTT Holdings | A$16,128.43 in theory | Holds the group tax roles (GST representative and head company) | Pays no wages, and a designated group employer "must pay wages in WA" (V). Not allowed as the structure stands |

**The choice does not change the group's total tax**: A$16,128.43 a year under any member that may legally claim it, as long as the deduction is used in full. It only decides who claims the deduction and who does the year-end group lodgement. All three members stay jointly liable whatever is chosen.

## 4. Why Lounge, in plain words
1. It pays three quarters of the wages: WA's own default points to it.
2. It is the company with the lease, the venue manager and the timesheets, so one company does the group return with its own records in hand.
3. Medical stays a clean clinical company: midwives, phlebotomists, consults.
4. Holdings cannot do it while it pays no wages.

One check for the accountant (not a question for Anthony): confirm how WA treats a deductible amount larger than the designated group employer's own wages. If the excess is lost, the cost is at most about A$362 a year (E), and normal wage growth in Lounge (award increases each July) closes the gap on its own. Do not move staff on paper to close it (Part 1, risks).

## 5. Center of Truth
The writer in theodore_r22.py now adds the row "Designated group employer: GTT Lounge" and the sentence "**Lounge claims the payroll tax group deduction**" to section 4B, a Round 25 change log row, and the same key in center_of_truth.yml. Re-run done; headline unchanged A$26,631.97 / A$19,973.98 (asserted).

## 6. Task 1 follow-on: what DOES legally cut tax and fees
1. **Instant asset write-off:** businesses with aggregated turnover under A$10 million deduct each asset costing under A$20,000 in the year it is first used, for assets first used on or after 1 July 2023 (V, [ATO Instant asset write-off](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/depreciation-and-capital-expenses-and-allowances/simpler-depreciation-for-small-business/instant-asset-write-off), updated 28 Aug 2026; no end date shown, so it covers 2026-27). GTT turnover about A$1.85 million a year (R maths). Which part of the A$251,198 start-up spend is equipment under A$20,000 each: NOT IN REPO. This brings tax forward; it does not add profit.
2. **Card fees:** the model uses 1.7% + A$0.30 (E); the repo lists Tyro at 1.4%. Each 0.3% saved is about A$489 a month on A$163,046.95 takings (E). Get quotes.
3. **Every GST credit:** valid tax invoices for both companies; Medical claims in full even though its consult is GST-free (Part 1).
4. **Payroll tax deduction claimed once, by Lounge** (this file).
5. **Super:** Payday Super applies from 1 July 2026 (V, [ATO Payday Super](https://www.ato.gov.au/businesses-and-organisations/super-for-employers/payday-super)); pay with each payday so the super guarantee charge never applies.
6. Company set-up and accounting costs: small business deduction rules NOT VERIFIED today; the accountant confirms.

## QUESTIONS FOR ANTHONY
None needed.

Regards.
Theodore
