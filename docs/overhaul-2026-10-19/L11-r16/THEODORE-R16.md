# Round 16 (Theodore): group tax, insurance, HR on-costs, Anthony's prices, lab money, Medicare timing, rostered midwives

General knowledge and desk research, not personal documents. Verify before acting. Prepared 2026-10-24. A plan, not a forecast. Company names are unregistered placeholders. All amounts are Australian dollars (A$). Nothing was sent to anyone.

Script: [theodore_r16.py](theodore_r16.py). It imports [theodore_r15.py](../L10-r15/theodore_r15.py), which imports R14 and R13. No second calculator. Results: [theodore_r16_results.json](theodore_r16_results.json). **Repo master numbers are unchanged.**

Confidence tags: **E** established (law, official page or repo figure). **U** uncertain (my estimate or reading, not confirmed). **ACC** = check with the accountant before acting. **Q** = quote needed.

## The answers first

| # | Question | Verdict | Tag |
|---|---|---|---|
| A | Three companies | Keep Holdings, but **elect tax consolidation and a GST group** in year 1. Then the parent adds no tax: dividends, fees and GST between the companies wash out. Second venue: **reuse Medical; add a new Lounge company only if you want each lease ring-fenced** | U, ACC |
| B | Insurance | Must-haves: midwife indemnity plus medical malpractice (Medical), public liability (Lounge and Medical), workers comp (each employer), business interruption (Lounge), cyber (Medical), directors and officers (Holdings) | U, Q |
| C | HR | Workers comp is compulsory for employers in WA and every state. Super is 12% (final rate) and from 1 July 2026 must be paid within 7 business days of each payday. Leave loading 17.5% comes from the awards, not the National Employment Standards, and only for permanent staff | E / U as marked |
| D | Prices | Treat A$162.15 as **GST-inclusive**. A$300 gives GTT A$257.41 ex GST (meets your A$250), mother pays **A$200.60** after rebate. A$350: mother pays **A$250.60**, the same as today's A$250 lounge price. **A$300 is below the A$338 break-even; A$350 is above it** | E maths, U market |
| E | Lab money | Recommend **Option Y** (mother pays the lab at the appointment). Under X the A$27.85 is the lab's money held as agent: **not GTT income, not a GTT expense, not on GTT's BAS**. Interest on it belongs to the lab | U, ACC |
| F | Medicare timing | **Two separate rebates.** Consult rebate (A$75.65) after the consult; test rebate (A$23.75) after the test. Each paid to her bank, usually within 7 days of claiming online, once the account is paid in full | E |
| G | Profit with rostered midwives | Package 1 (A$300): **A$16,009** (1 midwife) and **A$10,047** (2 midwives) a month before company tax, against the repo A$23,443. Package 2 (A$350): **A$23,436** (1) and **A$24,900** (2). Group payroll tax A$1,055 (1) and A$1,548 (2) a month | U (model) |

---

## A. Three-company structure (tax side)

### A1. Second venue: reuse or add companies?

| Option | Extra cost a year | Tax effect | Verdict | Tag |
|---|---|---|---|---|
| Reuse Medical and Lounge for venue 2 | about A$0 extra company cost | None. One more location on the books | **Default.** Medical runs both sites under one clinical governance. Each midwife needs a provider number for each new location (free) | U |
| Reuse Medical, new "Lounge 2" for the new lease | about A$5,450 (half of R15's A$10,904 for two companies) | None if consolidated | **Choose this if** the landlord wants a guarantee you want capped to one site | U, ACC |
| Two more companies (Medical 2 + Lounge 2) | about A$10,900 | None if consolidated | Not needed. Splitting Medical gives no payroll tax or Medicare benefit | U |

### A2. Do we pay more tax moving money through the parent?

| Flow | If consolidated (recommended) | If NOT consolidated | Tag |
|---|---|---|---|
| Dividends Medical or Lounge to Holdings | Ignored for tax (one head company return) | Franked dividend: Holdings grosses up and gets a franking offset, so **no extra tax** | U, ACC |
| Dividends Holdings to Anthony and partner | Franked at 25%. Anthony's excess credits refundable (SRDP tax exempt). Partner tops up at her rate | Same | E (Route B) |
| Room licence and management fees between companies | Ignored for income tax | Income in one, deduction in the other: net nil, but a loss in one company cannot offset profit in another | U |
| GST on those fees | With a GST group: no GST at all, one BAS | 10% GST charged, payer claims it back. Example: A$960 room fee + A$96 GST, Medical claims the A$96 (GST-free sellers still claim credits). **Net A$0, cash timing only** | U, ACC |
| Holdings living on royalties | Not a problem (test runs on the group) | **Risk:** 100% passive income means 30% tax, not 25% | E (s23AB, R15) |
| Payroll tax | One A$1,000,000 threshold for the group | Same: grouped by law either way | E |

**Three companies sharing one payroll tax threshold: still fine.** The repo is already A$106,355 over the threshold, so splitting neither helps nor hurts. Watch the joint liability: every company is liable for the group's payroll tax (E, RevenueWA via Catherine).

### A3. Is the parent worth it under Route B?

| Without Holdings (Anthony and partner own Medical and Lounge directly) | With Holdings |
|---|---|
| Saves about **A$3,682 a year** (E: ASIC review A$342, accounts A$2,500, bookkeeping A$600, bank A$240) | Tax consolidation possible (sister companies cannot consolidate) |
| Two dividend streams to manage | One franking account, one dividend source |
| A loss in Medical cannot shelter Lounge profit | A A$10,000 Medical loss saves A$2,500 tax against Lounge profit |
| Venue 2 and a later sale are messier | Brand, IP and spare cash sit away from day-to-day risk; one share sale sells the whole group |

**Verdict:** worth it **only if you consolidate**. Without consolidation it costs about A$3,700 a year for little benefit. U, ACC.

### A4. Cash journey (draw this, Option Y)

1. **Booking (online, one checkout, three lines).** Mother pays A$272.15 by card: A$162.15 to **Lounge's** merchant account (lounge part) and A$110.00 to **Medical's** account (consult). Best: a split-payment checkout. Fallback: Lounge collects both as Medical's disclosed agent and transfers the A$110 to Medical every week with a statement. Documents: order summary showing all three lines and the A$300 total.
2. **Consult (days or weeks before test day).** Midwife sees her. **Medical** issues a **paid account** (item 82110, provider number, midwife name). GST-free. Mother claims about **A$75.65** from Medicare.
3. **Pathology request.** Midwife sends the GTT request to the lab.
4. **Test day.** Mother pays the **lab** A$27.85 on the lab's terminal. Lab issues its own account in its pathologist's name. GST-free. Mother claims about **A$23.75**.
5. **Lounge tax invoice.** Lounge issues a GST tax invoice for A$162.15 (includes A$14.74 GST).
6. **Inside the group, monthly.** Medical pays Lounge a flat room licence fee and a management fee (written agreements, market value). With a GST group, no GST on these.
7. **Wages.** Medical pays midwives and phlebotomists; Lounge pays the rest. Super with every pay run (Payday Super). Payroll tax lodged by the designated group employer.
8. **BAS.** One BAS for the GST group: GST on lounge sales, credits on rent and supplies. Medical's consults and the lab's tests carry no GST.
9. **Year end.** Holdings lodges one consolidated return, 25% company tax. Subsidiaries pay franked dividends to Holdings (ignored for tax). Holdings passes the solvency test (s254T) and pays franked dividends to Anthony and partner with dividend statements.

---

## B. Insurance

| Cover | Holder | Why it matters | Annual cost | Tag |
|---|---|---|---|---|
| Midwife professional indemnity | Medical (employer policy naming each midwife). MIGA scheme cover if she practises privately under her own provider number | Biggest single liability; MIGA scheme gives A$2m with Commonwealth cover above that | A$1,200 to A$7,500 per midwife (R14 estimate range; older MIGA scheme report about A$7,500 full time) | U, **Q** |
| Medical malpractice / healthcare liability | Medical | Collection injuries, fainting during the glucose load, specimen errors by phlebotomists | Q | U |
| Public liability (A$20m typical) | Lounge (occupier and head tenant) and Medical (suites) | Slips, falls, recliner incidents; landlords demand it | Inside repo A$708.34 a month for all insurance (R) | E repo, **Q** split |
| Product liability (food and drink) | Lounge | Refreshments after the test | Usually bundled with public liability | U, Q |
| Workers compensation | Each employing company (Medical, Lounge). Not Holdings if it employs no one | Compulsory | Repo placeholder 1.7% of wages (A$1,399.41 a month, R). Health rate Q | E law, Q rate |
| Business interruption + property and fit-out | Lounge (owns the fit-out, holds the lease) | Protects revenue: pays lost gross profit after a fire, flood or forced closure. Pick a 12-month indemnity period | Q | U |
| Cyber | Medical (holds health records), group policy through Holdings | Booking platform and health data; breach notice costs | Q | U |
| Directors and officers + management liability | Holdings, covering all three | PSR and insolvent-trading exposure of directors (Catherine R15 A2) | Q | U |

Priority for maximum protection: 1 indemnity and malpractice, 2 public liability, 3 workers comp, 4 business interruption, 5 cyber, 6 directors and officers.

---

## C. HR on-costs

| Question | Answer | Tag |
|---|---|---|
| Workers comp mandatory in WA? | **Yes.** Every employer must insure its workers with an approved insurer (Workers Compensation and Injury Management Act 2023, in force 1 July 2024) | E (WorkCover WA) |
| Nationally? | Yes in every state and territory; there is no single national scheme for private employers. Each state's law applies where the work is done | E |
| Directors | **Working directors are covered only if the company opts them in** on its policy and declares their pay (WorkCover WA guidance citing ss16, 57, 59, 209). Anthony as an unpaid director is not covered and should not be (MRCA 10-hour rule: no wage) | E guidance, U sections |
| Contractors | A contractor can still count as a "worker" (s12, contract for performing work) unless she runs her own business, does not sublet, etc. Moot for midwives and phlebotomists: **Medical must employ them** (s16A(5AA), Catherine) | E |
| Super guarantee minimum | **12%** from 1 July 2025, the final legislated rate; no further rise scheduled | E (rate), U (no-change) |
| Change from 1 July 2026 | **Payday Super**: super must reach the fund within 7 business days of each payday, not quarterly. Cash flow: budget super weekly or fortnightly | E (passed Nov 2025) |
| Leave loading 17.5%: where from? | **Not the National Employment Standards** (they give 4 weeks' leave, no loading). It comes from the **modern awards**: Nurses Award MA000034 (17.5% on up to 152 hours a year; shiftworkers get the higher of 17.5% or their penalties). Hair and Beauty MA000005, Health Professionals MA000027 and Clerks MA000002 also carry 17.5% | E (Nurses), U (others) |
| Must it be included? | Yes, for **permanent** full-time and part-time staff under those awards. **Not for casuals** (their 25% loading replaces leave). Repo staff are casual, so no loading there; the midwives are permanent, so it is in (1.35% of wages) | E |

**"Divided by 58% billable share", in two sentences.** Only 58% of every paid midwife hour is spent with a mother; the rest is notes, set-up and gaps between bookings. So the true cost of one hour with a mother is the paid-hour cost divided by 0.58.

Worked example: pay a midwife for 10 hours at the all-in A$65.31 = **A$653**. She spends 5.8 hours with mothers. A$653 / 5.8 = **A$112.60 per hour with a mother** (R15: A$112.32).

---

## D. Pricing

### D1. How each package splits (Option Y, rebate example A$99.40)

| | Package 1, GST inside (recommended) | Package 1, GST on top | Package 2, GST inside (recommended) | Package 2, GST on top |
|---|---|---|---|---|
| Mother pays | **A$300.00** | A$316.21 | **A$350.00** | A$371.22 |
| GST-free part (consult A$110 + lab A$27.85) | A$137.85 | A$137.85 | A$137.85 | A$137.85 |
| Taxable lounge part (incl GST) | A$162.15 | A$178.36 | A$212.15 | A$233.37 |
| GST to the ATO | A$14.74 | A$16.21 | A$19.29 | A$21.22 |
| GTT group keeps, ex GST | **A$257.41** | A$272.15 | **A$302.86** | A$322.15 |
| Out of pocket after A$99.40 rebate | **A$200.60** | A$216.81 | **A$250.60** | A$271.82 |

**Recommend GST-inclusive.** Consumer prices must be shown as one total that includes GST (U, ACL single-price rule), and A$300 / A$350 are clean headline prices. If you want GTT to keep the full A$162.15 ex GST, the honest price is A$316.21, not "A$300 plus GST".

Mix-average rebate is A$84.45 (not every consult is an 82110), so out of pocket is about A$15 higher for some mothers (U).

### D2. Can the price rise?

| Price | Out of pocket | Against today (A$250 lounge-only) | Against R15 break-even A$338 |
|---|---|---|---|
| A$300 | A$200.60 | Mother pays **A$49.40 less** than today | Below: group worse off |
| A$338 (break-even) | A$238.60 | A$11.40 less | Equal |
| **A$349.40** | **A$250.00** | **Same as today** | Above |
| A$350 | A$250.60 | A$0.60 more | Above |
| A$387.85 (like-for-like) | A$288.45 | A$38.45 more | Well above |

**Yes, it can rise.** At A$350 the mother's real cost is the same as today's A$250 price, but she also gets a midwife consult. A$300 gives away about A$49 a mother. The lounge price has no Medicare cap (Catherine R15 C1). U on market acceptance.

### D3. Net group revenue per client and at 396 clients (all with a consult, before midwife costs)

| | Package 1 (A$300) | Package 2 (A$350) | Repo (A$250 lounge) |
|---|---|---|---|
| Per client, ex GST, after card fee | **A$252.48** | **A$297.08** | A$227.27 |
| Per client change vs repo | +A$25.21 | +A$69.81 | |
| A month at 396 | **A$99,982** | **A$117,644** | A$90,000 |
| Monthly change before midwife cost | +A$9,982 | +A$27,644 | |

A midwife costs about **A$58 per consult** (rostered, base case). So package 1 loses about A$33 per consult client and package 2 gains about A$12. Full 396 with consults needs 3 midwives: group profit before company tax **A$1,786 (package 1)** or **A$19,449 (package 2)** a month.

---

## E. Lab money

### E1. Option X vs Y

| | Option X: all online, GTT remits | **Option Y: lab paid at appointment (recommended)** |
|---|---|---|
| Where the A$27.85 lands | GTT account held for the lab, then paid on weekly | Lab's own terminal |
| GTT money held for the lab at 396 a month | about **A$7,618** (R15) | A$0 |
| Books | A liability "owing to lab", reconciled weekly | Nothing |
| Card fee on the lab part | GTT pays about A$0.47 a client, about A$186 a month | A$0 |
| Risk | Agency clause, ring-fenced account, AskMBS comfort (Catherine) | None |

Option Z (U): a split-payment checkout where the lab is its own payee. One tap for the mother and the lab's money never touches GTT. Ask the lab and the payment provider.

### E2. Can the lab's money be a GTT expense?

**No, and it does not need to be.** (U, ACC)

| Point | Answer | Tag |
|---|---|---|
| Agent or principal? | **Agent only.** The lab must bill in its own pathologist's name (HIA s16A), and the mother needs the lab's account to claim. GTT cannot buy and resell the test | E (Catherine) |
| Income tax | Money received as agent is the lab's, not GTT's income. Paying it on is not a deduction. Net effect nil | U |
| GST and BAS | The supply is the lab's to the mother and is GST-free (s38-7 medical services: Medicare benefit payable). Nothing for GTT to report (GSTR 2000/37 agency principles) | U, ACC |
| If treated as principal | Turnover and expenses both rise by A$27.85; tax unchanged; but it breaks the Medicare billing rules. Do not | U |

### E3. Can the lab's money earn interest first?

| Point | Answer | Tag |
|---|---|---|
| Who owns the interest | The lab, unless the written agency agreement says otherwise (agent's duty to account) | U |
| If GTT keeps it | It is GTT's taxable income **and** may be a benefit from a pathology provider to a requester's connected company (Part IIBA). Do not | U (Catherine to confirm) |
| Size | A$7,618 at 4 to 5% = **about A$305 to A$381 a year** (E) | E maths |
| Trust account rules | No special statutory trust-account law found for this; general agency duties apply: separate account named for the lab, no mixing, weekly reconciliation | U |

**Recommendation: Option Y (or Z). Do not earn interest on lab money.**

---

## F. Medicare timing (the mother claims both)

| | Midwife consult | Pathology test |
|---|---|---|
| When the service is done | Consult day (days or weeks before the test) | After the collections on test day (66548 covers the full test) |
| Who issues the account | GTT Medical Services | The lab |
| Who claims | The mother (claimant) | The mother |
| Amount back (example) | A$75.65 (82110) | A$23.75 (66548 A$16.95 + 73938 A$6.80) |
| How paid | Electronic transfer to her bank, **only if the account is paid in full**. Part-paid = cheque made out to the provider | Same |
| Typical timing | Online or Medicare app: **usually within 7 days** (Services Australia). Payment cycle 1 to 3 days after processing | Same, counted from when the lab account is issued and she claims |
| Claim at the counter (if GTT's software supports patient claiming) | Lodged for her on the day; paid to her bank in about 1 to 3 days | Lab's choice |
| Tag | E (7 days, EFT, paid-in-full rule); U (counter timing) | E / U |

So the mother gets **two payments**: A$75.65 after the consult and A$23.75 after the test. Paying at booking does not speed this up: Medicare pays only after each service has happened. Claim time limit 2 years (U).

---

## G. Profit with rostered midwives (9 to 5, Monday to Friday, 38 hours each)

Basis: 396 clients a month. Each midwife can see about **166.5 consult clients a month** (base mix 34.5 minutes, 10 minutes admin, 75% utilisation). Clients beyond her capacity keep today's A$250 lounge-only price with an outside request (E). Midwife cost A$49.91 an hour (RN level 2 pay point 4, R14 on-cost 1.20). Card fees, payroll tax, three-company cost included. Repo profit after GST A$23,442.58 (R).

| Monthly, base | P1 A$300, 1 midwife | P1 A$300, 2 midwives | P2 A$350, 1 midwife | P2 A$350, 2 midwives |
|---|---|---|---|---|
| Consult clients (share of 396) | 166.5 (42%) | 333 (84%) | 166.5 (42%) | 333 (84%) |
| Repo profit after GST (R) | 23,443 | 23,443 | 23,443 | 23,443 |
| + Consult income | +18,315 | +36,630 | +18,315 | +36,630 |
| Lounge repricing vs A$250, ex GST | -13,297 | -26,595 | -5,729 | -11,458 |
| Card fees | -820 | -1,641 | -962 | -1,924 |
| Midwife wages | -8,218 | -16,436 | -8,218 | -16,436 |
| Midwife fixed + consumables | -1,449 | -2,898 | -1,449 | -2,898 |
| **Group payroll tax (repo A$562 + midwives)** | **-1,055** | **-1,548** | **-1,055** | **-1,548** |
| Three-company cost | -909 | -909 | -909 | -909 |
| **Group profit before company tax** | **16,009** | **10,047** | **23,436** | **24,900** |
| Company tax 25% | -4,002 | -2,512 | -5,859 | -6,225 |
| **After company tax** | **12,007** | **7,535** | **17,577** | **18,675** |
| Change vs repo A$23,443 | -7,433 | -13,396 | -7 | +1,458 |

Sensitivities (before company tax):

| Case | P1, 1 | P1, 2 | P2, 1 | P2, 2 |
|---|---|---|---|---|
| Permanent, leave covered (on-cost 1.366) | 14,781 | 7,591 | 22,208 | 22,444 |
| Plus receptionist and host (E, A$12,167 a month) | 3,082 | -2,880 | 10,509 | 11,973 |
| Adverse cost | 14,906 | 7,841 | 22,864 | 23,756 |
| Favourable cost | 17,375 | 12,776 | 24,944 | 27,910 |

**What the repo numbers become** (shown beside the repo, not written into it): the repo A$23,443 after GST becomes **A$16,009 / A$10,047** at package 1 and **A$23,436 / A$24,900** at package 2 (1 / 2 midwives). Like-for-like baseline with no midwife (payroll tax and three companies only) is A$21,971.

**Solve, do not shrink:** package 2 at A$350 with 2 midwives is the strongest base case. If you keep A$300 as the entry price, run 1 midwife and send the rest of the request load to outside GPs until volume proves itself; adding the second midwife at A$300 costs about A$6,000 a month.

---

## Flags for the accountant (ACC)

1. Tax consolidation election and tax sharing agreement, year 1.
2. GST group for Holdings, Medical, Lounge.
3. Franking: partner's top-up rate and Anthony's refund under Route B.
4. Agency treatment of lab money if Option X is ever used.
5. Payroll tax registration from the first full month (monthly taxable wages already above A$83,333).

## Sources read this round

- [WorkCover WA: workers compensation for working directors](https://www.workcover.wa.gov.au/employers/understanding-your-rights-obligations/covering-your-workers/workers-compensation-working-directors/) and [contractors guidance, Aug 2025](https://www.workcover.wa.gov.au/wp-content/uploads/2025/08/Workers-compensation-insurance-for-contractors-August-2025.pdf)
- [ATO: employers prepare for Payday Super](https://www.ato.gov.au/media-centre/ato-calls-on-employers-to-prepare-for-payday-super)
- [Services Australia: Medicare claims](https://www.servicesaustralia.gov.au/individuals/subjects/medicare-claims) and [operational blueprint EFT cycle](https://operational.servicesaustralia.gov.au/public/Pages/your-health/011-43010040-05.html)
- [MIGA: midwives](https://miga.com.au/insuring-with-us/midwives) and [Health: Midwife Professional Indemnity Scheme](https://www.health.gov.au/our-work/midwife-professional-indemnity-scheme-mpis)
- [Workstem: Nurses Award guide (leave loading)](https://www.workstem.com/au/blog/nurses-award-guide/) (secondary; check the clause in the current award)
- Catherine R15 (corporate group, Structure B money, payroll tax grouping) and Theodore R15 (break-even, float, payroll tax base).
