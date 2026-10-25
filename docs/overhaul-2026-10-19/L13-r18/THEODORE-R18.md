# Round 18 (Theodore): 12 answers plus refund mechanics, on your locked decisions

General knowledge and desk research, not your personal documents. Verify before acting. Prepared 2026-10-25. All amounts are Australian dollars (A$), per month unless stated. GTT is treated as ONE venture: Holdings + Medical + Lounge consolidated. Company names are placeholders. Nothing was sent to anyone.

Script: [theodore_r18.py](theodore_r18.py). It imports [theodore_r17.py](../L12-r17/theodore_r17.py) (which imports R16, R15, R14, R13) and runs the repo's own `tools/master_financial_model.py` live for the base lines. No second calculator. Results: [theodore_r18_results.json](theodore_r18_results.json). Repo master numbers are unchanged.

Tags: **R** repo figure. **V** verified on an official page this round. **E** estimate or secondary source. **U** uncertain. **ACC** ask the accountant. **Q** quote needed.

## Locked answers applied (not re-asked)

| Item | Locked |
|---|---|
| Structure | B: private, all-inclusive; the mother claims her own Medicare rebate |
| Package 1 | 2 x 30-minute services, A$300, GST inside. **Planning case: 100% Package 1** |
| Package 2 | 2 services up to 45 minutes, A$350 |
| Consult | Short, 20 minutes, referral only. One consult room |
| Midwives | 2 permanent part-time (one Mon to Wed, the other Thu to Sat, swap each fortnight) + 1 casual for leave. One midwife rostered a day, 09:00 start |
| Venue manager | Starts 06:30 (repo says 07:00). First draw 07:00, clients arrive 06:50 |
| Volume | 18 morning clients a day = 473.94 a month over six days (R). Services done before 18:00 |
| Collection | 2 collection rooms, 1 chair each |
| Lab money | Straight to the lab. Interest only on clients' prepaid package money |
| Tax | Payroll tax accepted as a cost. Tax consolidation and a GST group go on the year 1 to-do list |

## Errors I own this round (fixed below)

| # | Error | Where | Fix |
|---|---|---|---|
| 1 | The A$99.40 rebate assumed a 40-minute consult (item 82110). Your consult is 20 minutes, which can only be item **82105** (MBS Online: "at least 10 minutes", A$32.95 back). The mother's rebate is about **A$55**, not A$99 | R16 D1, R17 Q8 headline | Q2, Q10 |
| 2 | R17's A$18,526 left out the venue manager's 06:30 start, sized midwife hours from demand (48.6 a week) instead of your roster (45), costed two consult rooms, and ignored leave cover for permanent midwives | R17 Q9 | Q1, Q11 |
| 3 | R17 used 396 clients for the prepaid-money float (A$74,447). The model volume is 474 | R17 Q4 | Q5 |
| 4 | "Lounge + consult" wording | R17 artifact, roadmap | Q7 |

---

## Q1. Whole-venture P&L, one month, locked case

**Answer: A$17,795 profit before company tax, A$13,346 after 25% company tax. All A$13,346 is available as a fully franked dividend (A$4,449 of franking credits attached), subject to the solvency test.** R base, E midwife lines.

| Line | Monthly | Tag |
|---|---|---|
| Lounge + service revenue, morning packages, ex GST (474 x A$147.41) | A$69,863.50 | R17 split |
| Afternoon (PM) revenue, ex GST (repo A$24,585.37 / 1.1) | A$22,350.34 | R |
| **Consult revenue, GST-free** (474 x A$110, Medical) | **A$52,133.40** | E |
| **Total revenue, ex GST** | **A$144,347.23** | |
| Repo payroll, Table 1 full roster (wages, super, workers comp) | -A$93,595.63 | R |
| Repo operating costs (rent, insurance, overheads, cost of goods) | -A$14,288.34 | R |
| GST credits on costs (implied by the repo's after-GST basis) | +A$1,262.58 | R |
| Card fees (1.7% + A$0.30 on GTT's A$272.15) | -A$2,336.52 | E |
| Midwife wages: 45 h/week, Nurses Award RN level 2 pay point 4, permanent with leave covered (on-cost 1.366) | -A$12,000.38 | E |
| Midwife fixed costs (registration, indemnity, training, software, equipment, consult room) + consumables | -A$2,840.65 | E |
| Venue manager 06:30 start (0.5 h x 22 weekdays x A$40, loaded) | -A$500.28 | R rate |
| **WA payroll tax, whole group** | **-A$1,344.04** | E |
| Three-company running cost | -A$908.67 | E |
| **Profit before company tax** | **A$17,795.30** | |
| Company tax 25% (one consolidated return) | -A$4,448.82 | E |
| **Profit after company tax = franked dividend available** | **A$13,346.47** | |

GST you collect and pass to the ATO (not revenue): morning lounge + service A$6,985.88, afternoon A$2,235.03. On Grace's on-cost basis (1.20, no leave cover) the profit is A$19,371 before tax, A$14,528 after.

## Q2. Your reading of the money, checked to the dollar

**Answer: "Reaches GTT" is right. The rebate and out-of-pocket are wrong for a 20-minute consult.** V (MBS Online, read 2026-10-25)

| Package | Your reading | Correct | Right? |
|---|---|---|---|
| P1 reaches GTT | A$272 | A$272.15 (consult A$110 + lounge + service A$162.15). Ex GST A$257.41 | Yes |
| P2 reaches GTT | A$322 | A$322.15. Ex GST A$302.86 | Yes |
| Rebate | A$99 | **A$55.00**: consult 82105 A$32.95 + test 66548 A$16.95 + collection 73928 A$5.10 | No |
| P1 out of pocket | A$201 | **A$245.00** | No |
| P2 out of pocket | A$251 | **A$295.00** | No |

A$201 and A$251 are right (A$200.60 and A$250.60) only for a 40-minute consult (82110, A$75.65) with the higher collection item 73938. Medicare pays the rebate to the mother, never through GTT.

**Collection item mismatch (U, for Catherine and the lab):** the repo uses collection item 73928 (approved collection centre, fee A$5.95). The A$27.85 lab price uses 73938 (collected for the treating practitioner, A$7.95). Under 73928 the lab price would be A$25.85. This changes the rebate by A$1.70 and the lab's price, not GTT's.

| Consult item | Collection item | Rebate | P1 out of pocket | P2 out of pocket |
|---|---|---|---|---|
| 82105 short (locked) | 73928 (repo) | A$55.00 | **A$245.00** | **A$295.00** |
| 82105 short | 73938 | A$56.70 | A$243.30 | A$293.30 |
| 82110 (40 min, not your plan) | 73938 | A$99.40 | A$200.60 | A$250.60 |

## Q3. One checkout including the lab?

**Answer: No. One checkout for GTT's part only (consult + lounge + service, A$272.15), split automatically between Medical and Lounge. The lab bills the mother itself.** U, Q

| Pros of putting the lab inside GTT's checkout | Cons, and what breaks |
|---|---|
| One tap for the mother | The lab must bill in its own pathologist's name (Health Insurance Act s16A, Catherine). Money through GTT makes GTT a collecting agent holding the lab's money |
| One booking record | Part IIBA (anti-kickback): any benefit GTT gets from holding or handling lab money (float interest, better terms) can be a prohibited benefit from a lab to a company connected to the requester (U, Catherine) |
| | Refunds: a cancelled test means GTT refunds the lab's money and must claw it back from the lab |
| | Chargebacks land on GTT's merchant account, including disputes about the lab's test |
| | Card fee on lab money: about A$0.47 a client, about A$223 a month at 474 |
| | Medicare paid-in-full rule: the mother needs the lab's own paid account to claim by bank transfer |

**Recommendation:** (1) GTT checkout (Stripe Connect or similar) takes A$272.15: Lounge is the platform, A$110 goes automatically to Medical's connected account. (2) Lab money by the lab's own SMS or online link, or its own terminal at the collection room. (3) Only if the lab agrees: the lab as its own merchant on the same screen (a separate charge in the lab's name, never through GTT's balance). Fallback if the split fails: Lounge collects A$272.15 as Medical's disclosed agent and transfers Medical's A$110 weekly with a statement.

## Q4. Direction of money: Medical pays Lounge for rooms

**Answer: The direction is right in every Theodore R16 and R17 output and in the R17 artifact. Two wording or basis problems found in other files.** R

| File | Says | Problem | Fix |
|---|---|---|---|
| THEODORE-R16 A4 step 6, R17 Q3, r17 artifact | "Medical pays Lounge" licence fee | None | |
| THEODORE-R16 A2 | Room fee example A$960 | Right direction, old amount | A$2,478.18 ex GST (R17 Q3, consult + 2 collection rooms) |
| GRACE-R17 roadmap step 42 | "Medical licence of rooms (Lounge to Medical)" | Reads as if money flows Lounge to Medical | "Room licence: Lounge grants the licence; **Medical pays Lounge** a flat monthly fee" |
| THEODORE-R15 line 261 | "Management fee, Medical to Lounge, 5% of Medical revenue (reception, booking, hosts)" | Direction right. Basis wrong: a percentage of Medicare-linked revenue is what Catherine R16 rules out, and hosts were removed | Flat market-value fee, written agreement |

**Direction-of-money self-check I ran (keep for every round):**

- [x] Rooms: Medical pays Lounge (Lounge holds the lease)
- [x] Consult A$110: Lounge collects as Medical's agent and passes to Medical; never the other way
- [x] Lab A$27.85: mother pays the lab; never through GTT
- [x] Medicare rebate: Medicare pays the mother; never through GTT
- [x] Dividends: Medical and Lounge to Holdings; Holdings to Anthony and partner (Route B)
- [x] GST: GTT pays the ATO; inside a GST group, no GST between the companies
- [x] Payroll tax: one designated group employer lodges for the whole group
- [x] Refunds: GTT refunds its own private fees only (see Q23)

## Q5. Lab money and interest on prepaid package money

**Answer: GTT holds no lab money. Prepaid package money (474 x A$272.15, held about 21 days before the visit) averages about A$89,100, earning about A$900 to A$4,450 a year.** E

| Rate | Source and status | Interest a year |
|---|---|---|
| 1.00% big-bank business saver | CommBank page did not load this round. **Not verified** | A$891 |
| 4.30% CommBank 3-month business term deposit | Aspire comparison, July 2026, secondary, before the September rise. E | A$3,831 |
| 4.60% RBA cash rate | RBA, effective 30 Sep 2026. **V** (a reference, not a product) | A$4,099 |
| 5.00% Great Southern Bank / Bank Australia 3-month business term deposit | Aspire, July 2026, secondary. E | A$4,455 (A$3,341 after 25% tax) |

The money is held for about 21 days and must stay ready for refunds, so an at-call business saver fits better than a 3-month term deposit. Ask the bank for its current at-call business rate (Q).

## Q6. Year 1 to-do list (trigger: when the entities exist)

- [ ] Register Holdings, then Medical and Lounge as 100% subsidiaries (ASIC). Trigger: before the lease
- [ ] ABN + GST registration for each company. Trigger: on registration
- [ ] **GST group** application (Holdings as representative member; 90% ownership, same tax periods and accounting basis). Lodged through the tax agent; form number not verified. Trigger: before the first BAS period. ACC
- [ ] **Tax consolidation** choice in writing by Holdings, then notify the ATO on **NAT 6781** no later than Holdings' first return (ATO suggests 28 days before). Cannot be undone. ACC
- [ ] **Tax sharing agreement** (ITAA 1997 s721-25), signed before the head company's return is due. Solicitor + accountant
- [ ] **WA payroll tax group**: register with RevenueWA, name one designated group employer to claim the single A$1,000,000 threshold. Trigger: the first month group wages pass about A$83,333 (already true from day 1)
- [ ] PAYG withholding, super (Payday Super, within 7 business days of payday) and workers comp for each employing company. Trigger: before the first pay run

## Q7. Terminology

| Term | Means |
|---|---|
| **Lounge** | The venue and its hospitality: recliners, refreshments after the last draw, the space |
| **Service** | Each massage, beauty, nails or hair treatment (Package 1 = 2 x 30 minutes) |
| **Consult** | The midwife's 20-minute antenatal consult (Medical, GST-free, item 82105) |
| **Package** | Lounge + service + consult, sold at A$300 or A$350. The lab test is paid to the lab separately |
| **Draw** | Each blood collection on test morning (fasting, 1 hour, 2 hours) |

Corrections (listed here; the round 17 records are left as written):

| File | Wrong | Right |
|---|---|---|
| r17 artifact, money table | "GTT receives (lounge + consult)" | "GTT receives (lounge + service + consult)" |
| GRACE-R17 roadmap step (Theodore row) | "split payment checkout (lounge and consult)" | "(lounge + service + consult)" |
| THEODORE-R17 Q1 | "A$110 + lounge" | "consult A$110 + lounge + service" |
| THEODORE-R17 Q7, ledger P3 | "Lounge price A$162.15" | "Lounge + service price A$162.15" |

## Q8. Does the midwife change monthly revenue?

**Answer: Revenue goes up; profit goes down. Like for like at 474 clients, GTT takes A$14,283 more revenue but keeps A$4,176 less profit a month.** E

| Per client (ex GST) | Before midwife | After (P1) | Change |
|---|---|---|---|
| Revenue reaching GTT | A$227.27 | A$257.41 | +A$30.14 |
| Card fee | 0 | -A$4.93 | -A$4.93 |
| Midwife (wages, fixed, consumables) | 0 | -A$31.31 | -A$31.31 |
| Extra payroll tax | | -A$1.65 | -A$1.65 |
| Venue manager 06:30 | | -A$1.06 | -A$1.06 |
| **Net per client** | | | **-A$8.81** |

| Monthly | Before | After | Change |
|---|---|---|---|
| Revenue, ex GST | A$130,063.97 | A$144,347.23 | +A$14,283.26 |
| Profit before company tax | A$21,971.46 | A$17,795.30 | **-A$4,176.16** |

## Q9. Can the consult price be raised?

**Answer: Legally yes, but it does not help.** Services Australia: "Health professionals are free to set their own fees"; Medicare pays 85% of the schedule fee, whatever is charged (V). A$110 is GTT's own fee. The MBS fee is A$38.75 for 82105 (A$89.00 for 82110), not A$110.

- Raising the consult does not raise the rebate (fixed at A$32.95). The mother just pays more.
- The consult fee "cannot include charges for goods or services outside the MBS item" (Services Australia). Lounge value cannot be moved into the GST-free consult, and shifting price into it to avoid GST invites ATO apportionment and anti-avoidance review (U, ACC).
- **Compliant levers:** raise the lounge + service price (Q12), or sell priced optional extras (longer services, extra service, take-home products), all taxable.

## Q10. Package value against your A$200 to A$250 belief

| | Package 1 | Package 2 |
|---|---|---|
| Price | A$300 | A$350 |
| Rebate (short consult, Q2) | A$55.00 | A$55.00 |
| **Out of pocket** | **A$245.00** (inside your range) | **A$295.00** (A$45 above it) |
| Of which consult gap (A$110 - A$32.95) | A$77.05 | A$77.05 |
| Of which test gap (A$27.85 - A$22.05) | A$5.80 | A$5.80 |
| Of which lounge + service | A$162.15 | A$212.15 |

Reality check (E, secondary): Fresha listings show a 60-minute pregnancy massage in Perth at about A$99 to A$160 (for example A$99 Doubleview, A$120 North Perth, A$155 Scarborough day spa). Package 1's lounge + service part (A$162.15 for 2 x 30 minutes plus the lounge) sits at the top of that range, and adds the consult and the test. Package 2 at A$295 out of pocket is the harder sell. I have no data on what mothers will pay; this is not a survey.

## Q11. The missing profit: bridge to the dollar

**Answer: The "about A$38k" is A$38,705.33, a repo figure struck out on 2026-08-21. The repo's current figure is A$35,186.40, with no GST taken out. Both are whole-venture (morning + afternoon). A$18,526 was also whole-venture (Holdings + Medical + Lounge). Every step:** R

| Step | Change | Running figure |
|---|---|---|
| A. Old repo figure, 2026-08-21, struck out (CURRENT-STATE line 179) | | **A$38,705.33** |
| Dedicated afternoon reception removed (2026-08-21) | +A$5,460.84 | A$44,166.17 |
| Afternoon capacity locked at 10 sessions a day (2026-09-19) | -A$11,640.32 | |
| Payroll: venue manager Mon to Fri, phlebotomist model closed (2026-09-19) | +A$2,660.55 | |
| B. **Repo today, no GST line** (CURRENT-STATE line 30, live model run) | | **A$35,186.40** |
| GST taken out: the repo counts the GST-inclusive A$250 as revenue | -A$11,743.82 | A$23,442.58 |
| Repo payroll tax (never in the repo net) | -A$562.45 | |
| Three-company running cost | -A$908.67 | |
| C. Like-for-like baseline, no midwife | | **A$21,971.46** |
| Consult income, 474 x A$110 | +A$52,133.40 | |
| Lounge + service price A$250 to A$162.15, ex GST | -A$37,850.14 | |
| Card fees | -A$2,336.52 | |
| Midwife wages, R17 basis (48.6 h/week, on-cost 1.20) | -A$11,388.88 | |
| Midwife fixed + consumables (two consult rooms) | -A$3,320.65 | |
| Extra payroll tax on midwives | -A$682.68 | |
| D. **R17 headline** | | **A$18,525.98** |
| Your roster: 45 h/week, one consult room | +A$1,325.62 | |
| Venue manager 06:30 | -A$500.28 | |
| Payroll tax effect of those two | +A$19.42 | |
| E. Locked, Grace on-cost 1.20 | | A$19,370.74 |
| Leave cover for permanent midwives (casual relief) + its payroll tax | -A$1,575.44 | |
| F. **R18 locked, before company tax** | | **A$17,795.30** |
| Company tax 25% | -A$4,448.82 | |
| G. **After company tax = franked dividend** | | **A$13,346.47** |

Plainly: the biggest single step is GST (A$11,744). The repo has never taken GST out. Swapping A$250 of taxable lounge + service for A$110 of GST-free consult + A$162.15 of lounge + service adds about A$14,283 of revenue, but the midwife costs about A$14,841 plus card fees and payroll tax. My error: R17's A$18,526 did not include the venue manager change, leave cover or your exact roster.

## Q12. Final payroll maths and the A$20 test

**Answer: Payroll added = A$500.28 (venue manager) + A$12,000.38 (midwives, leave covered) = A$12,500.66 a month. On Grace's 1.20 basis it is A$11,043.54 (Grace's A$11,166.24 counted 26.33 days a month instead of 4.333 weeks; A$122.70 difference).** E

| Payroll tax check | Amount | Tag |
|---|---|---|
| Group taxable wages a year, repo only | A$1,106,355 | R |
| Group taxable wages a year, locked | A$1,254,145 | E |
| One WA threshold (grouped) | A$1,000,000 | E, check current RevenueWA figure |
| **Over the threshold?** | **Yes, by A$254,145. Already over (A$106,355) before any midwife** | |
| Payroll tax a month (5.5%, threshold deduction tapers) | A$1,344.04 (repo alone A$562.45) | E |

| Monthly | A$300 / A$350 (locked) | A$320 / A$370 |
|---|---|---|
| Per P1 client: extra GST | | +A$1.82 |
| Per P1 client: extra to GTT ex GST, after card fee | | +A$17.84 |
| Profit before company tax | A$17,795.30 | **A$26,250.39** |
| After 25% company tax (franked dividend) | A$13,346.47 | **A$19,687.79** |
| Mother out of pocket, P1 / P2 | A$245 / A$295 | A$265 / A$315 |

GST is already inside A$300. Adding A$20 does not "cover GST": GST takes A$1.82 of the A$20, the card fee A$0.34, and GTT keeps A$17.84 (A$8,455 a month at 474).

**Adaptive rostering: confirmed, unchanged** (Grace R17): phlebotomists 1 when 9 or fewer are booked, 2 for 10 to 18; therapists 2 for 1 client, 4 for 2 to 9, 6 for 10, 8 for 11 to 18. The model costs the full 18-client roster, so quieter days only cost less. Midwives are not adaptive: one a day, fixed. Roster check: 18 consults a day x 20 minutes = 6 hours of a 7.5-hour paid day (80% booked). It fits, with 1.5 hours for walk-ins and running late.

## Q23. Refund mechanics: are we providing the refund or is Medicare?

**Answer: Both, for different money. Medicare pays the rebate to the mother. GTT refunds only its own fees, and never refunds or repays a rebate.**

| Question | Answer | Tag |
|---|---|---|
| Who pays the rebate? | Medicare (Services Australia) pays it to the person who paid the account, into her bank account. GTT is not involved (Health Insurance Act s20) | V |
| When? | Only after the service has happened and she has paid in full. Paying at booking does not bring it forward | V (s20(2): an unpaid account gets a cheque made out to the provider instead) |
| How much? | 85% of the MBS schedule fee: 82105 A$32.95, 66548 A$16.95, 73928 A$5.10. Fixed by the schedule, not by GTT's price. It cannot be more than the fee charged | V |
| Any cap? | The benefit is capped at the schedule-fee percentage and never more than she paid. The Medicare Safety Net can lift rebates once her yearly out-of-pocket costs pass a threshold; amounts **not verified** this round | V / not verified |
| She cancels before the consult | No service, so no Medicare claim. GTT refunds its private fees under its booking terms and the Australian Consumer Law | E (terms Q, Catherine) |
| She had the consult, then cancels the test | The consult account stands; she still claims A$32.95. GTT refunds the unused lounge + service part under its terms. The lab refunds or never charges its test | E |
| Rebate already paid, then GTT refunds the consult | Must not happen: a refunded service means she did not incur the cost, and the claim would need correcting with Services Australia. Not verified; ask Catherine | not verified |
| Lab money | The lab's own refund, never GTT's (Q3) | E |

---

## Honest gaps

1. Collection item 73928 vs 73938 changes the lab price (A$25.85 vs A$27.85). Lab and Catherine to confirm.
2. Midwife unpaid break (30 minutes) and casual relief indemnity are assumptions (E, Q).
3. Savings and term deposit rates are secondary sources from July 2026; only the RBA cash rate is verified.
4. Medicare Safety Net amounts and the refund-after-claim rule are not verified.
5. Package 2's extra therapist time (90 vs 60 minutes) is not modelled; the plan is 100% Package 1.

## Sources

- Repo (fresh clone 2026-10-25): docs/CURRENT-STATE.md lines 30 and 179; data/models/master_financial_model.yml (steady_state_summary status notes); tools/master_financial_model.py (live run, Table 1 steady month); data/canonical/cost_ramp.yml (opening_time_increment A$7,040); [THEODORE-R17.md](../L12-r17/THEODORE-R17.md); [GRACE-R17-ROSTER.md](../L12-r17/GRACE-R17-ROSTER.md); [THEODORE-R16.md](../L11-r16/THEODORE-R16.md); [THEODORE-R15.md](../L10-r15/THEODORE-R15.md)
- MBS Online: [82105](https://www9.health.gov.au/mbs/fullDisplay.cfm?type=item&q=82105), [82110](https://www9.health.gov.au/mbs/fullDisplay.cfm?type=item&q=82110), [73928](https://www9.health.gov.au/mbs/fullDisplay.cfm?type=item&q=73928), [73938](https://www9.health.gov.au/mbs/fullDisplay.cfm?type=item&q=73938)
- [Services Australia operational blueprint: Medicare benefits and fees](https://operational.servicesaustralia.gov.au/public/Pages/your-health/011-43010010-01.html)
- [Health Insurance Act 1973 s20 (AustLII)](https://www5.austlii.edu.au/au/legis/cth/consol_act/hia1973164/s20.html)
- [Services Australia Medicare claim form MS014](https://www.servicesaustralia.gov.au/individuals/forms/ms014)
- [RBA cash rate](https://www.rba.gov.au/statistics/cash-rate/)
- [Aspire: business term deposit rates (July 2026)](https://aspireapp.com/en-au/blog/best-business-term-deposit-rates-australia), [Mozo savings accounts](https://mozo.com.au/savings-accounts)
- [Fresha: pregnancy massage, Perth](https://fresha.com/lp/da/tt/gravidmassager/au-perth) (secondary)
- [ATO: NAT 6781 consolidation notification](https://www.ato.gov.au/forms-and-instructions/consolidated-groups-notification-forming-an-income-tax-consolidated-group)
