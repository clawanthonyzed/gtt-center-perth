# THEODORE R25 PART 1: Would moving costs, payroll or the venue manager into GTT Medical help?

Theodore, financial consultant, 2026-10-27. Numbers from [theodore_r22.py](../L17-r22/theodore_r22.py) (Round 25 block, re-run; the script stops if the headline moves). General knowledge and desk research, not tax advice; the accountant confirms. Nothing sent. Tags: R repo, V verified (URL, date read 2026-10-27), E estimate.

## READ-FIRST CHECK
- Venue manager starts 06:30 (Mon to Fri 06:30 to 15:00); 07:00 is the first draw. A hired person, not Anthony.
- Path A = PREFERRED, package with the GTT midwife consult. Path B = NOT preferred, outside referral, no GTT consult, not limited.
- Prices: Path A A$320 / A$370 (GTT charges A$292.15 / A$342.15). Path B A$300 / A$350 all in (GTT charges A$272.15 / A$322.15).  <!-- factcheck:ok -->
- Rebates: consult A$32.95 + lab A$22.05 = about A$55.00.
- Midwives 08:00 to 16:00, first consult 08:15.
- Late rule: blood draws no wiggle room; consults 10 minute grace.

## 1. Answer first
**No.** Moving the venue manager, payroll or any cost into Medical does not raise revenue or profit, and does not lower company tax, GST or payroll tax. The group result stays **A$26,631.97 before tax and A$19,973.98 after** in every case below (R, asserted by the script).

| A$ a month | Medical profit | Lounge profit | Group tax (consolidated) | Tax if each company were taxed alone |
|---|---|---|---|---|
| Locked split | A$32,295.25 | -A$5,663.28 | A$6,657.99 | A$8,073.81 |
| Venue manager (A$8,504.76) moved to Medical | A$23,790.49 | A$2,841.48 | A$6,657.99 | A$6,657.99 |
| Whole shared block (A$23,783.23) moved | A$8,512.02 | A$18,119.95 | A$6,657.99 | A$6,657.99 |
| All service staff payroll (A$72,226.63) moved | -A$39,931.38 | A$66,563.35 | A$6,657.99 | A$16,640.84 |

## 2. Point by point
**(a) Company tax.** In a consolidated group Holdings lodges one return for all three; dealings inside the group are ignored (V, [ATO Consolidation](https://www.ato.gov.au/businesses-and-organisations/corporate-tax-measures-and-assurance/consolidation), updated 25 Aug 2026). So tax is 25% of A$26,631.97 = A$6,657.99 wherever a cost sits. Moving costs would only matter if the companies were taxed separately (last column); consolidation (locked, Year 1) already fixes that, saving A$1,415.82 a month (R).

**(b) GST.** One correction to the idea: a GST-free sale does NOT cost you GST credits. Credits are blocked only for purchases that relate to **input-taxed** sales (V, [ATO When you can claim a GST credit](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/claiming-gst-credits/when-you-can-claim-a-gst-credit), updated 14 Sep 2026). GTT makes no input-taxed sales (no financial supplies, no home rent) (E). So Medical (GST-free consult, s38-7 as a Medicare-item service, E: Act text not read today) and Lounge (taxable) both claim full credits. In the GST group, sales between members are ignored (V, [ATO GST groups](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/registering-for-gst/gst-groups-and-branches/gst-groups), updated 14 Sep 2026). Result: GST credits stay A$1,262.58 a month (R) wherever costs sit.

**(c) GST-free medical supplies.** A medical aid is GST-free only if it is listed in GST Act Schedule 3 (or the regulations), is specifically designed for people with an illness or disability, and is not widely used by people without one (V, [ATO Medical aids and appliances](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/in-detail/your-industry/gst-and-health/medical-aids-and-appliances), updated 8 Oct 2025; [Schedule 3](https://www.ato.gov.au/law/view/document?DocID=PAC/19990055/Sch3&PiT=99991231235958), read 2026-10-27).

| Item GTT buys | Schedule 3? | Likely GST | Tag |
|---|---|---|---|
| Gloves, tourniquets, collection tubes | Not listed | Taxable | V list, E outcome |
| Venepuncture needles | Item 37 "needles and syringes" sits under Diabetes; GTT needles are used on every client, so they fail the "not widely used" test | Taxable | V item, E test |
| Alcohol skin wipes | Item 35, under Diabetes; generic swabs fail the same test | Taxable | V item, E test |
| Glucose drink (75 g) | Not listed. Health goods list is condoms, folic acid, sunscreen and similar (V, [ATO Health goods](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/in-detail/your-industry/gst-and-health/health-goods), updated 13 Jun 2024). Whether it is a restricted medicine: NOT VERIFIED | Probably taxable | E |
| Goods used inside the consult | GST-free when a necessary part of a GST-free service (V, [ATO goods in a GST-free health service](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/in-detail/your-industry/gst-and-health/goods-supplied-as-part-of-a-gst-free-health-service), 12 Jun 2024). This is about what Medical sells, already GST-free | No change | V |

**Even where a supplier sells an item GST-free, GTT saves A$0**: it would otherwise claim that GST back as a credit (only about one quarter of cash timing). The supplier sets the GST on its invoice.

**(d) Payroll tax.** WA adds the wages of all three companies together: A$1,254,144.89 a year, tax A$16,128.43 a year = A$1,344.04 a month, whichever company employs whom (V rule, R wages; Part 2).

**(e) Medicare and health rules.** I found no ruling that rewards a consult-only company for paying a venue manager (E). The rebate is set by the item (A$32.95 on 82105) whatever the company's costs.

**(f) Revenue.** No change: A$153,826.03 a month ex GST (R). Costs do not create sales.

**(g) Risks of moving costs on paper only.**
- Part IVA (the general anti-avoidance rule) targets schemes done mainly for a tax benefit (E). Here there is no benefit, only risk.
- The real employer (who hires, directs and pays) carries the award, workers comp and payroll tax return (E). A venue manager running the Lounge but "employed" by Medical is a mismatch.
- Medicare billing integrity: Medical carries the clinical service. A Lounge cost placed in Medical misstates the business and muddies the set-up Catherine is checking (E).
- Room fee between the companies: market price, in writing (E).

## 3. Verdict
| Option | Group tax | GST | Payroll tax | Revenue | Risk | Recommended |
|---|---|---|---|---|---|---|
| Venue manager into Medical | No change | No change | No change | No change | Medium | No |
| Shared costs into Medical | No change | No change | No change | No change | Medium | No |
| Service payroll into Medical | No change | No change | No change | No change | High | No |
| Buy "GST-free" supplies | No change | A$0 saving | n/a | No change | Low | Not worth chasing |
| Keep the locked split | Baseline | Baseline | Baseline | Baseline | Low | **Yes** |

## 4. What DOES legally cut tax and fees
See [THEODORE-R25-PART-2.md](THEODORE-R25-PART-2.md) section 6 (instant asset write-off, card fee quotes, GST credits, the payroll tax deduction, Payday Super).

## QUESTIONS FOR ANTHONY
None needed.

Regards.
Theodore
