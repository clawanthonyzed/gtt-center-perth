# Round 17 (Theodore): your 10 questions, on your decisions

General knowledge and desk research, not your personal documents. Verify before acting. Prepared 2026-10-24. All amounts in Australian dollars (A$). Company names are placeholders. Nothing was sent to anyone.

Script: [theodore_r17.py](theodore_r17.py). It imports [theodore_r16.py](../L11-r16/theodore_r16.py), which imports R15, R14 and R13. No second calculator. Results: [theodore_r17_results.json](theodore_r17_results.json). Repo master numbers are unchanged.

Tags: **E** = established (law, official page or repo figure). **U** = uncertain (my estimate or reading). **ACC** = ask the accountant. **Q** = quote or provider confirmation needed.

## Your decisions I treated as fixed (not re-opened)

| Decision | Status |
|---|---|
| Structure B | Fixed |
| At least A$250 reaches GTT as a whole (Medical + Lounge). The lab's A$27.85 does not count | Fixed |
| Package 1: client A$300 = consult A$110 + lab A$27.85 + lounge A$162.15 | Fixed |
| Package 2: client A$350 = consult A$110 + lab A$27.85 + lounge A$212.15 | Fixed |
| Plan on the lower package. Keep 2 packages for choice | Fixed |
| Tax consolidation and a GST group in year 1. Route B | Fixed |
| 2 midwives on the books, splitting Monday to Saturday. No hosts, only a venue manager | Fixed |

## What I got wrong before (one line each, all fixed below)

| # | Error | Fix |
|---|---|---|
| 1 | A$222.15 was Round 15's example at the **old A$250 all-in price**. It is not your current number | Q1: A$272.15 (package 1) and A$322.15 (package 2) reach GTT |
| 2 | Round 16 left clients the midwife could not see on the **old A$250 lounge-only price**, and counted Monday to Friday only | All 474 clients a month (repo six-day volume) now buy a package |
| 3 | Round 16 compared the **mother's** cost after rebate with the old A$250. That confused GTT revenue with her cost | Q8 |
| 4 | GST on top of A$162.15 was shown as A$16.21. Correct is **A$16.22** (0.5 cent rounds up), so A$178.37 | Q7 |
| 5 | The room licence (A$960) covered consult rooms only and left out the 2 collection rooms | Q3: about A$2,478 a month ex GST |
| 6 | Break-even "A$338" came from Round 15's smaller volumes. It was on the group basis (medical + lounge), not lounge only, but it is out of date | Q6: **A$345.38** like for like |

---

## Q1. Does A$250 reach GTT?

**Verdict: Yes. Both packages clear A$250, with GST inside and with GST taken out.** E

| Per client | Package 1 | Package 2 |
|---|---|---|
| Client pays | A$300.00 | A$350.00 |
| Less lab (passes to the lab, not GTT) | -A$27.85 | -A$27.85 |
| **Reaches GTT, GST inside** (A$110 + lounge) | **A$272.15** | **A$322.15** |
| Less GST on the lounge part (lounge / 11) | -A$14.74 | -A$19.29 |
| **Reaches GTT, ex GST** | **A$257.41** | **A$302.86** |
| Less card fee (1.7% + A$0.30 on GTT's part, E) | -A$4.93 | -A$5.78 |
| Reaches GTT, ex GST, after card fee | A$252.48 | A$297.08 |
| Clears A$250? | Yes, by A$7.41 ex GST | Yes, by A$52.86 ex GST |

The old A$222.15 (A$110 + A$112.15) was the Round 15 example at A$250 all-in. It did not clear A$250. That was the pre-increase price, so you were right to push.

---

## Q2. How one payment splits itself

**Verdict: One checkout on Stripe Connect. Lounge is the platform and takes the payment. Each payment automatically sends A$110 to Medical's own connected account. The lab is never in GTT's checkout: the mother pays the lab herself.** U, Q

| Option | How it works | Good | Weak | Tag |
|---|---|---|---|---|
| **A. Stripe Connect, "separate charges and transfers" (pick)** | Lounge's platform account takes A$272.15. Stripe moves A$110 to Medical's connected account on each charge (linked by a transfer group) | Automatic, per client, audit trail, works in Australia | The A$110 sits in Lounge's Stripe balance for seconds or days (Lounge is a disclosed agent for Medical). More set-up work | E (Stripe docs list Australia); fit for health: Q |
| B. One Lounge merchant account + clearing account + daily sweep | Lounge takes the full A$272.15. The booking system splits the invoice. Each night the bank (or bookkeeper) moves the A$110 lines to Medical | Simple; any booking software | A person or a bank rule must do the sweep; mistakes are possible | U |
| C. Two invoices, two payments | Mother pays Medical A$110 and Lounge A$162.15 separately | Cleanest legally | Two card taps: poor experience | E |
| D. Trust account | A formal trust account holding money for others | Not needed for intra-group money | Extra rules and cost for no gain | U |

**Who holds which merchant account**

| Company | Account | Takes |
|---|---|---|
| Lounge | Stripe platform account (merchant) | The checkout: lounge A$162.15 or A$212.15, plus Medical's A$110 as disclosed agent |
| Medical | Stripe connected account, own bank account | A$110 consult. Issues the paid consult account so the mother can claim |
| Holdings | None | Nothing from clients |
| Lab | Its own terminal or link | A$27.85, straight from the mother |

**How the mother pays the lab** (pick in this order):
1. The lab bills her directly (its own SMS or online link, or its account after the test). GTT touches nothing. Best.
2. The lab's own card terminal, in the lab's name, used at the collection room. Money goes to the lab's bank.
3. Never a GTT terminal for the lab's money.

**Needs confirmation (Q):** Stripe accepts a health platform with a Medical connected account; your booking software can run Stripe Connect (Fresha, used in the repo, runs its own payments: U); the lab will bill her directly or place its terminal; the terms say Lounge collects Medical's A$110 as a disclosed agent (Catherine R15).

---

## Q3. Who pays whom for the rooms?

**Verdict: You are right. Lounge holds the lease, so Medical pays Lounge a flat licence fee every month.** E (direction); U (amount)

No earlier round wrote it the other way. Round 15 (line 262) and Round 16 both say "Medical to Lounge". The error was the **size**: A$960 counted consult rooms only.

**Method:** Medical's share of the floor × (rent + outgoings), at market value, fixed, never a % of Medicare money (Catherine R16).

| Line | Working | Monthly |
|---|---|---|
| Rent per sqm | A$8,000 rent budget / 200 sqm (repo) | A$40.00 |
| Medical's own rooms | Consult room 13 sqm (Grace R16, U) + 2 collection rooms 18 sqm each (repo) = 49 sqm | |
| Rent part | 49 × A$40 | A$1,960.00 |
| Outgoings part | 49 × A$126.90 a year / 12 (one listing in the repo's rent research, U) | A$518.18 |
| **Licence fee, ex GST** | | **A$2,478.18** |
| Shared areas (reception, toilets, waiting) | Add a fair share; a valuer sets it | Q |

**GST and consolidation effect**

| Case | GST | Income tax | Group profit |
|---|---|---|---|
| GST group + consolidation (your year 1 choice) | None. Supplies inside the group are ignored | Ignored (one group return) | **No change** |
| Without them | Lounge adds A$247.82 GST; Medical claims it back (GST-free sellers can still claim credits) | Income in Lounge, deduction in Medical | No change, cash timing only |

---

## Q4. Why GTT should not hold the lab's money, and how you can still earn

**Verdict: The A$27.85 is the lab's money. The interest on it would be about A$90 to A$570 a year, which is not worth the legal risk. Earn interest on GTT's own prepaid money instead: about A$744 to A$3,238 a year.** U, ACC

**Why not**

| Reason | Plain words | Tag |
|---|---|---|
| It is the lab's money | The lab bills in its own pathologist's name. GTT can only collect as the lab's agent | E (HIA s16A, Catherine) |
| Income tax | Agent money is not GTT income, and paying it on is not a GTT expense | U, ACC |
| GST | It is the lab's GST-free supply. It is not on GTT's BAS | U, ACC |
| Interest ownership | Interest on the lab's money belongs to the lab unless the agreement says otherwise | U |
| Part IIBA (anti-kickback) | If the lab lets GTT keep that interest, the lab is giving value to a company connected to the requesting midwife. That can be a prohibited benefit | U (Catherine to confirm) |

**Workarounds**

| Option | What it is | Earns | Risk | Verdict |
|---|---|---|---|---|
| (a) Lab bills the mother directly | Option Y | A$0 | None | **Do this** |
| (b) Trust or clearing account; agreement says interest is GTT's admin fee | Lab agrees in writing; settle weekly | Table below | **High**: Part IIBA (U). Ask the lab, Catherine and the accountant first | Not recommended |
| (c) Negotiate lab payment terms | E.g. GTT pays the lab 14 days after the test | Small | Same Part IIBA question if the terms are better than normal | Only at normal terms |
| (d) **Interest on GTT's own cash** | Prepaid packages and retained profit in a business saver | Below | Low. It is GTT's income, taxed at 25% | **Do this** |

**Rates (U, not verified current):** big-bank business saver about **1.00%** (CommBank's tiers were 0.40% to 1.30% from 15 May 2026). Bank Australia online saver **4.35%** (from 20 May 2026). The cash rate was 4.10% after the March 2026 rise. Check before choosing.

Lab money held under (b). Working: A$27.85 × clients / 30.4 days × days held. "Paid at booking" means held through a 21-day booking lead (E, repo books 2 to 4 weeks ahead).

| 396 clients a month | Settle weekly | Settle monthly |
|---|---|---|
| Paid at booking: average held | A$8,888 | A$13,133 |
| Interest a year at 1.00% / 4.35% | A$89 / A$387 | A$131 / A$571 |
| Paid on test day: average held | A$1,270 | A$5,514 |
| Interest a year at 1.00% / 4.35% | A$13 / A$55 | A$55 / A$240 |

At 474 clients a month (six days), paid at booking: weekly A$106 / A$463; monthly A$157 / A$684.

**(d) GTT's own money:** 396 × A$272.15 prepaid, held 21 days on average = **A$74,447**. Interest = **A$744 a year at 1.00%, A$3,238 a year at 4.35%**. That is about 6 times more than the lab's money, with no Part IIBA risk.

---

## Q5. Tax consolidation and a GST group in year 1: locked

**Verdict: Locked. Holdings is the head company. Your accountant does most of it; the cost is a few thousand dollars once.** E where shown, U elsewhere

| # | Step | Form or rule | When | Who | Rough cost | Tag |
|---|---|---|---|---|---|---|
| 1 | Register Holdings first, then Medical and Lounge as 100% subsidiaries | ASIC | Before the lease | Accountant or solicitor | In R15 set-up costs | E |
| 2 | ABN and GST registration for each company (Medical's GST-free consults count toward GST turnover) | ABR | At registration | Accountant | A$0 ATO fee | U |
| 3 | **GST group**: Holdings as representative member. Needs 90% common ownership, same tax periods and same accounting basis | ATO application, online or by tax agent (form number U) | From the start of a tax period you choose: aim for the first BAS period | Accountant | A$300 to A$800 time (Q) | U |
| 4 | **Choice to consolidate**: Holdings chooses in writing, then notifies the ATO on **NAT 6781** | ATO | No later than the day Holdings lodges its first-year return. ATO suggests 28 days before. **Cannot be undone** | Public officer or tax agent | A$1,500 to A$5,000 (Q) | E |
| 5 | **Tax sharing agreement**: limits each subsidiary's share of group tax debts | ITAA 1997 s721-25 | Signed before the head company's return is due (U) | Solicitor + accountant | A$1,500 to A$3,000 (Q) | U |
| 6 | **WA payroll tax group**: grouped by law. Register with RevenueWA and name one designated group employer, which claims the single A$1m threshold | Pay-roll Tax Assessment Act 2002 (WA) | From the first month group wages pass about A$83,333 (already true) | Accountant | Bookkeeping time | E (grouping) |
| 7 | PAYG withholding, super and workers comp for each employing company | ATO, insurer | Before the first pay run | Bookkeeper | In R16 | E |

**Ask the accountant:**
1. Which date should consolidation start, and does it line up with the GST group start?
2. Will you draft the tax sharing agreement, or should a solicitor?
3. Any reason not to consolidate in year 1 (losses, the franking account under Route B)?
4. Which company should be the payroll tax designated group employer?
5. Your fixed fee for steps 3 to 6.

---

## Q6. Why break-even was A$338, and what it really is

**Verdict: Old A$338 was out of date, not lounge only. Like for like, with the same costs, break-even is A$345.38 at the repo consult mix, or A$308.13 if the package consult is a short visit. Package 1 at A$300 sits below both.** U (model)

**Before and now, per client** (package 1, all 474 clients, ex GST):

| Line | Before midwife (repo) | Now, package 1 | Change |
|---|---|---|---|
| Reaches GTT, ex GST | A$227.27 (A$250 / 1.1, all lounge, taxable) | A$257.41 (A$110 + A$147.41) | **+A$30.14** |
| Card fee | none in repo | -A$4.93 | -A$4.93 |
| Midwife cost per client (wages, fixed, consumables; repo consult mix, 108 hours a week) | none | -A$62.48 | -A$62.48 |
| Extra payroll tax per client | none | -A$3.20 | -A$3.20 |
| **Net change per client** | | | **-A$40.47** |
| × 474 clients a month | | | **-A$19,183** |

**Group profit before company tax, a month:** before = A$21,971 (repo A$23,443, less the same payroll tax A$562 and three-company cost A$909). Now (package 1, repo consult mix) = A$2,789.

**Break-even price** (one price for everyone, profit back to A$21,971):

| Consult length | Midwife cost per client | Break-even price | Package 1 A$300 | Package 2 A$350 |
|---|---|---|---|---|
| Repo mix (average 34.5 minutes + 10 admin) | A$62.48 | **A$345.38** | Below by A$45.38 | Above by A$4.62 |
| Short consult (item 82105, 10 minutes + 10 admin) | A$31.04 | **A$308.13** | Below by A$8.13 | Above by A$41.87 |

Against the repo A$23,443 with no structure costs: A$348.85. The A$387.85 "like for like" in Round 15 kept the lounge at A$250 and added the consult on top. That is not your rule, and I have retired it.

---

## Q7. GST on A$162.15 and A$212.15

**Verdict: Treat both as GST-inclusive. That keeps your A$300 and A$350 totals and still gets more than A$250 to GTT.** E (maths), U (ACL)

| | (a) GST inside (recommend) | (b) GST on top |
|---|---|---|
| Package 1 lounge | A$162.15 = A$147.41 + GST A$14.74 | A$162.15 + GST A$16.22 = A$178.37 |
| Package 1 client sees | **A$300.00** | A$316.22 |
| Package 1 reaches GTT, ex GST | A$257.41 (clears A$250) | A$272.15 |
| Package 2 lounge | A$212.15 = A$192.86 + GST A$19.29 | A$212.15 + GST A$21.22 = A$233.37 |
| Package 2 client sees | **A$350.00** | A$371.22 |
| Package 2 reaches GTT, ex GST | A$302.86 | A$322.15 |

Option (b) breaks your A$300 and A$350 totals. Consumer prices must also be shown as one price including GST (U, ACL single-price rule).

**What carries GST in each package**

| Part | Package 1 | Package 2 | GST | Tag |
|---|---|---|---|---|
| Midwife consult (Medical) | A$110.00 | A$110.00 | GST-free (Medicare benefit payable, GST Act s38-7) | E/U |
| Lab test (the lab's supply) | A$27.85 | A$27.85 | GST-free, and on the lab's BAS, not GTT's | E |
| Lounge | A$162.15 | A$212.15 | Taxable, 1/11 is GST | E |

**BAS a month (one group BAS)**

| | Package 1, 396 | Package 1, 474 | Package 2, 396 | Package 2, 474 |
|---|---|---|---|---|
| Taxable lounge sales (GST inside) | A$64,211.40 | A$76,849.37 | A$84,011.40 | A$100,546.37 |
| **GST collected** | **A$5,837.04** | **A$6,985.88** | **A$7,638.84** | **A$9,142.30** |
| GST-free consult sales | A$43,560.00 | A$52,133.40 | A$43,560.00 | A$52,133.40 |
| Lab money | A$0 | A$0 | A$0 | A$0 |

GST credits on rent and supplies reduce the GST payable. They are already inside the repo's after-GST A$23,443 (R).

---

## Q8. A$300 vs A$350: the money map

**Verdict: A$50 more on the price means A$50 more to GTT (A$45.45 after GST). The lab's share and the Medicare rebate do not change.** E

The confusing Round 16 sentence, fixed: "At A$350 the **mother's own cost after her Medicare rebate** (A$250.60) is about the same as the old A$250 lounge price. **GTT itself receives A$322.15**, not A$250."

| Per client | Package 1 | Package 2 |
|---|---|---|
| Client pays | A$300.00 | A$350.00 |
| Medicare pays back (example: consult 82110 A$75.65 + test A$23.75) | A$99.40 | A$99.40 |
| **Mother's net cost** | **A$200.60** | **A$250.60** |
| Mother's net cost on the average consult mix (rebate A$84.46) | A$215.54 | A$265.54 |
| **GTT receives** (GST inside / ex GST) | **A$272.15 / A$257.41** | **A$322.15 / A$302.86** |
| Lab receives | A$27.85 | A$27.85 |

If the package consult is the short 82105, the rebate falls to A$56.70, so the mother pays A$243.30 or A$293.30 net. Flag (U, Catherine): the repo lists collection item 73928 (A$5.10 back), while the A$27.85 lab price uses 73938 (A$6.80 back). That changes the rebate by A$1.70, not your prices.

---

## Q9. Two packages: locked

**Verdict: Locked. Package 1 = one 45-minute service; Package 2 = two 45-minute services (your instruction via Grace R16). The repo still says 2 × 30 and "flexible" (CURRENT-STATE section 2). Grace owns service content and should update it.** E (your decision), U (therapist time)

| | Package 1 | Package 2 |
|---|---|---|
| Services | Consult + GTT + one 45-minute service | Consult + GTT + two 45-minute services |
| Client price | A$300 | A$350 |
| Reaches GTT, ex GST | A$257.41 | A$302.86 |

**Capacity, with 2 midwives (the key point):**

| Consult length | Midwife hours needed a week, 474 clients | Do 2 midwives fit? |
|---|---|---|
| Repo mix (34.5 minutes average) | 108.2 (2.85 full-time) | **No.** 2 full-time = 76 hours |
| Short consult (82105, 10 minutes) | 48.6 (1.28 full-time) | **Yes.** 2 part-timers at about 24 hours each |

Grace and the clinical lead decide the consult length (U). Your 2-midwife plan works with the short consult.

**Monthly, 474 clients, before company tax** (baseline with the same costs and no midwife: A$21,971):

| Mix (P1 / P2) | GTT revenue ex GST | Short consult, 2 midwives | After 25% tax | Repo mix (needs 2.85 FTE) |
|---|---|---|---|---|
| **100% P1 (planning case)** | A$121,997 | **A$18,526** | A$13,894 | A$2,789 |
| 70 / 30 | A$128,459 | A$24,867 | A$18,650 | A$9,130 |
| 50 / 50 | A$132,767 | A$29,095 | A$21,821 | A$13,358 |
| 100% P2 | A$143,537 | A$39,664 | A$29,748 | A$23,927 |

With leave fully covered (on-cost 1.366), the planning case is A$16,952. Not modelled: extra therapist time for Package 2's 90 minutes against the repo's 60 (U). That makes the P2 rows a top estimate.

---

## Q10. Midwife pay: casual, part-time or full-time?

**Verdict: Two permanent part-time midwives, about 24 hours each, splitting Monday to Saturday (e.g. one on Monday, Wednesday and Friday, the other on Tuesday, Thursday and Saturday, 8 hours a day). Add one casual relief midwife on the books for leave and sick days.** U

**Facts**

| Point | Answer | Tag |
|---|---|---|
| Award | Nurses Award 2020 (MA000034) covers registered nurses and midwives employed in health. Not the Health Professionals Award | E (rates used since R13); private company coverage U (strong) |
| Rate used | RN level 2 pay point 4: A$41.59 weekday, A$62.39 Saturday (150%) | E (Fair Work pay guide, via R14) |
| Casual | 25% loading instead of leave: A$51.99 weekday, A$77.99 Saturday (175%) | E (rates), U (Saturday multiplier) |
| Minimum engagement | Not verified this round | U |
| Part-time | Needs an agreed, written regular pattern of hours | U |
| Permanent leave | 4 weeks annual + 17.5% loading, 10 days personal/carer's, compassionate leave, public holidays | E (NES + award) |
| Casual leave | No paid annual or personal leave. Paid family and domestic violence leave applies to casuals too | E |
| Casual conversion | Employee can ask to convert after 6 months (12 for small business) | U |
| Super | 12%, paid with each pay from 1 July 2026 | E |

**Cost a month at the 48.6 hours a week needed (short consult)**

| Type | Rate an hour (blended 5/6 weekday, 1/6 Saturday) | All-in an hour | A month | Notes |
|---|---|---|---|---|
| Casual | A$56.32 | A$64.04 (+12% super, +1.7% workers comp) | **A$13,487** | No continuity; can leave at short notice |
| **2 part-time (recommend)** | A$45.06 | A$61.54 a worked hour (super, workers comp, leave loading, leave cover) | **A$12,960** | Same midwives, continuity of care for PSR records |
| 2 full-time (76 paid hours) | A$45.06 | A$51.84 a paid hour | **A$17,073** + relief during leave | About 27 hours a week more than needed |

At the repo consult mix (108.2 hours) the costs are A$30,026 casual and A$28,854 permanent. That needs a third midwife or shorter consults.

---

## Sources

- Repo (fresh clone): [CURRENT-STATE.md](../../CURRENT-STATE.md) sections 00, 2, 5; [DECISION-LOG.md](../../DECISION-LOG.md) 2026-10-19 round 9; [profit-loss-tables.md](../../profit-loss-tables.md); tools/master_financial_model.py (run: no GST or Medicare lines, A$250 is all lounge revenue)
- [THEODORE-R16.md](../L11-r16/THEODORE-R16.md), [GRACE-R16.md](../L11-r16/GRACE-R16.md), [THEODORE-R15.md](../L10-r15/THEODORE-R15.md), [THEODORE-R14.md](../L9-r14/THEODORE-R14.md)
- Catherine R15 and R16 (second brain, knowledge/legal/r15 and r16)
- [Stripe: separate charges and transfers](https://docs.stripe.com/connect/separate-charges-and-transfers)
- [ATO: notify us when forming an income tax consolidated group (NAT 6781)](https://www.ato.gov.au/forms-and-instructions/consolidated-groups-notification-forming-an-income-tax-consolidated-group)
- [CommBank Business Online Saver rates](https://www.commbank.com.au/business/bank-accounts/business-online-saver.html), [Bank Australia rate rise](https://www.bankaust.com.au/blog/bank-australia-increases-interest-rates-across-savings-and-transaction-account-products), [Savings.com.au: RBA March 2026](https://www.savings.com.au/news/rba-savings-accounts-march-2026)
- [FairWorkMate: midwife rates under MA000034](https://fairworkmate.com.au/tools/pay-rates/midwife-nsw) (secondary; check the Fair Work pay guide)
