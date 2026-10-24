# Round 15 (Theodore): loaded midwife cost, scaled midwife P&L, payroll tax, full workforce, 3-company structure, Structure B cash flow

General knowledge and desk research, not personal documents. Verify before acting. Prepared 2026-10-24. A plan, not a forecast. Project name is an unregistered placeholder. All amounts are Australian dollars (A$). No em dashes. Nothing was sent to anyone.

Script: [theodore_r15.py](theodore_r15.py). It imports [theodore_r14.py](../L9-r14/theodore_r14.py), which imports [theodore_r13.py](../L8-r13/theodore_r13.py). Midwife P&L numbers come from `r14.mw()`, payroll tax from `r14.ptax()`. No second calculator. Results: [theodore_r15_results.json](theodore_r15_results.json). Repo base numbers are unchanged.

Labels: **R** repo figure. **V** official source read this round. **E** my estimate. **Q** quote needed.

## The answers first

1. **The A$63 to A$65 was never "wage plus on-costs".** It was the all-in cost of one PAID hour: wage with on-costs A$54.07, plus consumables A$3.03, plus fixed costs (indemnity, registration, software, equipment, rooms) A$8.21 = **A$65.31** (base, Scenario A, six-day). Your sum (A$45 to A$54, plus 12% super, 10% leave loading, 1.7% workers comp) gives A$55.67 to A$66.80. That lands in the same range, but only by coincidence: on R14's actual base wage (A$45.06 blended) your sum gives A$55.74, not A$65. The gap is consumables and fixed costs, not wages. And per **billable hour** (time with a client) the cost is much higher, **A$112.32**, because only 58% of a paid hour is client time. Revenue per billable hour on bulk billing is A$105.57. That is why bulk billing loses money.
2. **Bulk billing loses, Structure B (private all-inclusive, client claims the rebate) makes money.** Base case net a month: bulk billed -A$907 (A) and -A$1,306 (B). Structure B at the A$110 consult example, item-scaled: **+A$5,541 (A, 54 a week) and +A$8,725 (B, 84 a week)**. Midwives needed: 2 for A, 3 for B (1.41 and 2.19 FTE).
3. **Correction to R14 payroll tax: R14 was wrong on the starting line.** The repo's A$987,817 is wages only. The repo adds super (A$9,878.17 a month) separately, and WA counts super as taxable wages. True repo taxable wages are **A$1,106,355 a year, A$106,355 OVER the A$1,000,000 threshold before any midwife**. Repo-only payroll tax is **A$6,749 a year, A$562 a month**. R14's A$730 and A$1,171 were the whole group's tax computed on the wrong base, not the midwives' share. Midwives add A$750 (A) to A$1,167 (B) a month at the margin (6.35% of their taxable wages). Hours were not the problem: the A scenario already had 53 paid hours a week (231 a month).
4. **The repo has no receptionist, no clinic host, no midwives and no payroll tax.** Repo payroll is A$82,318.05 wages, A$93,595.63 loaded, all service staff plus venue manager. Adding a receptionist and a host (E) adds A$12,166.54 a month loaded. Midwives A or B add A$12,511 or A$19,462. Combined clinic payroll **A$118,274 (A) or A$125,224 (B)** a month loaded.
5. **The most important finding in the three-company numbers: Structure B at A$250 all-in cuts the lounge from A$250 to A$112.15 a client.** The group keeps A$222.15 (consult A$110 plus lounge A$112.15) instead of A$250. At A$250, group profit after GST falls from the repo A$23,443 to about A$4,746 (A) or -A$5,536 (B) before payroll tax and structure costs. **Break-even package price against the repo is about A$338.** The like-for-like price (lounge stays A$250) is **A$387.85**, client pays A$288.45 after the A$99.40 rebate.
6. **Recommended cash flow (Option Y):** client pays the package part (A$222.15) online, pays the lab's A$27.85 to the lab directly at the appointment. No agent money, no float, no GST on the lab share. If you insist on one payment of A$250 (Option X), GTT holds about A$7,618 of the lab's money at 396 clients a month and needs a ring-fenced account.
7. **Route 1 costs: A$1,955 now (three companies A$1,908, business name A$47), about A$24,125 more at lease signing** (legal review, two months bond, first insurance quarter). Provider number, ABN, PRODA and the Ahpra check cost A$0.

## Part 1. Loaded midwife cost, step by step

### 1.1 How R14 got A$63 to A$65 (base case, Scenario A, six-day, bulk billed)

| Step | A$ per hour | What it is |
|---|---|---|
| 1. Award ordinary rate, RN level 2 pay point 4 (V, Fair Work Pay Guide MA000034, 1 Jul 2026) | 41.59 | Monday to Friday |
| 2. Blended with Saturday at 150% (one sixth of hours) | 45.06 | R13 and R14 convention |
| 3. + super 12% (V, ATO Super Guarantee from 1 Jul 2025) | 50.46 | +5.40 |
| 4. + annual leave loading 17.5% on 4 weeks (1.35% of wage) (V rule, applies to permanent staff) | 51.07 | +0.61 |
| 5. + workers compensation 1.7% (R placeholder; WA health rate is Q) | 51.84 | +0.77. **Built-up multiplier 1.1505** |
| R14 used a flat on-cost multiplier of 1.20 instead of 1.1505 | **54.07** | R14 wage cost per paid hour (E). 1.20 is steps 3 to 5 plus about 5% for other leave costs |
| + consumables A$3 a consult (E) | +3.03 | per paid hour |
| + fixed costs: Ahpra A$193 a year (V), indemnity A$2,500, CPD, software, equipment over 5 years, 2 rooms (E) | +8.21 | per paid hour |
| **= all-in cost per PAID hour** | **65.31** | The number R14 called A$63 to A$65 |
| Revenue per paid hour, bulk billed | 61.39 | R14 "earns about A$61" |
| Billable share of a paid hour (clinical minutes 34.5 per consult, 10 min admin, 75% utilisation) | 58.15% | 34.5 / 44.5 x 0.75 |
| **Wage only per BILLABLE hour** (54.07 / 0.5815) | **92.99** | |
| **All-in cost per BILLABLE hour** (65.31 / 0.5815) | **112.32** | Revenue per billable hour 105.57 |

Low, base, high (R14 favourable, base, adverse; "low cost" first):

| | Low cost | Base | High cost |
|---|---|---|---|
| Award rate used | RN L2 pp1 A$39.59 | RN L2 pp4 A$41.59 | RN L3 pp1 A$42.93 |
| Blended hourly | 42.89 | 45.06 | 46.51 |
| R14 on-cost multiplier | 1.14 | 1.20 | 1.25 |
| Wage cost per paid hour | 48.89 | 54.07 | 58.14 |
| Built-up multiplier steps 3 to 5 | 49.34 | 51.84 | 53.51 |
| Consumables plus fixed per paid hour | 8.10 | 11.24 | 17.51 |
| All-in per paid hour | 56.99 | 65.31 | 75.70 |
| Utilisation and admin | 85%, 6 min | 75%, 10 min | 65%, 15 min |
| Billable share of paid hour | 74.7% | 58.2% | 38.0% |
| All-in per billable hour | 76.28 | 112.32 | 199.46 |
| Revenue per billable hour, bulk billed | 95.51 | 105.57 | 130.74 |

(The R13 figures A$45.01 / A$54.07 / A$71.18 are R13's own low, base, high wage cost per paid hour: low has no Saturday hours, high is a casual level 3 nurse. R14 and R15 use the table above. The base A$54.07 is the same in all three rounds.)

### 1.2 Does your arithmetic reproduce R14's number?

| Test | Result |
|---|---|
| A$45 + 12% + 10% + 1.7% (add the percentages, 1.237) | A$55.67 |
| A$54 with the same sum | A$66.80 |
| Compounded (1.12 x 1.10 x 1.017 = 1.253) | A$56.38 to A$67.66 |
| Same sum on R14's actual base wage A$45.06 | **A$55.74** |
| R14 all-in per paid hour | **A$65.31** |

**No, it does not reproduce R14 on its own.** The sum lands in R14's range only because your A$45 to A$54 range is wide. For the same wage R14 spent A$54.07 on wage plus on-costs; the extra **A$11.24** an hour is consumables (A$3.03) and fixed costs (A$8.21), not leave or loading. Then dividing by the billable share (utilisation and admin) turns A$65 into A$112 per client hour.

### 1.3 Is R14's 1.20 on-cost too low? Yes, if the midwife is permanent

Leave loading is not the big item. Paid leave is. A permanent midwife is paid for 52 weeks but works about 43.8 (annual leave 4 weeks, personal leave 2 weeks, about 11 public holidays = 2.2 weeks, E). To deliver the clinic hours the hourly cost must be grossed up by 52 / 43.8 = 1.187.

| On-cost basis | Multiplier | Wage per paid hour | Net a month, A (54 a week) | Net a month, B (84 a week) |
|---|---|---|---|---|
| R14 flat | 1.20 | 54.07 | -A$907 | -A$1,306 |
| Built-up, paid hour (super + loading + workers comp) | 1.1505 | 51.84 | -A$391 | -A$502 |
| **Built-up, per worked hour (adds paid leave)** | **1.366** | **61.54** | **-A$2,636** | **-A$3,995** |
| Casual alternative: A$51.99 casual rate x (1 + 12% + 1.7%) | n/a | 59.11 | similar to the row above (E) | |

R14's 1.20 sits between the two. If the midwives are permanent and their leave must be covered, bulk billed results are about A$1,700 (A) to A$2,700 (B) a month worse than R14 showed. Structure B results (Part 2) have room for this.

## Part 2. Scaled midwife P&L, bulk billed versus Structure B

### 2.1 What the MBS items are (V, MBS Online, read 2026-10-24)

| Item | What it is | Fee | Benefit 85% | Notes |
|---|---|---|---|---|
| 82100 | Initial antenatal visit, 60 min | A$89.00 | A$75.65 | Once per pregnancy |
| 82110 | Routine antenatal visit, 40 min | A$89.00 | A$75.65 | Video 91212 same fee |
| 82105 | Short antenatal visit, 10 min | A$38.75 | A$32.95 | Video 91211 same fee |
| 82115 | **Maternity care plan**, 90 min, after 28 weeks | A$381.75 | A$324.50 | Needs 2 prior visits in 6 months with this midwife, written care plan, once per pregnancy, midwife intends to stay main carer. Excludes labour and birth. It is not a GTT-test visit |
| 91211 | Video version of 82105 | A$38.75 | A$32.95 | 10 min or more |

82115 is upside only if GTT midwives become the woman's main carer. One delivered 82115 earns A$324.50 (bulk) against about A$123 of wage and consumables, a margin of **A$201** (A$259 at schedule private fee). Ten a month = about A$2,013 (E). It is not in any figure below.

### 2.2 Private fee used for Structure B (E)

Your R14 example is A$110 on 82110. I scaled every item by 110 / 89 = 1.236: 82100 A$110.00, 82110 A$110.00, 82105 A$47.89 (E, no Perth benchmark; Q). The client claims the schedule benefit back, not the private fee. For the bundle table in Part 5 the consult line is a flat A$110.

### 2.3 Gross billings by item, base mix (25% initial, 35% short, 40% routine)

| Item | A: count / month | Bulk billed | Private (E) | B: count / month | Bulk billed | Private (E) |
|---|---|---|---|---|---|---|
| 82100 | 58.5 | A$4,426 | A$6,435 | 91.0 | A$6,884 | A$10,010 |
| 82105 | 81.9 | A$2,699 | A$3,922 | 127.4 | A$4,198 | A$6,102 |
| 82110 | 93.6 | A$7,081 | A$10,296 | 145.6 | A$11,015 | A$16,016 |
| **Total** | **234** | **A$14,205** | **A$20,653** | **364** | **A$22,097** | **A$32,128** |

### 2.4 Net monthly profit to GTT, after loaded wages, consumables and fixed costs (before payroll tax)

Six-day basis (matches the repo money, 473.94 clients). A = 9 a day, 54 a week, 234 a month. B = 14 a day, 84 a week, 364 a month. Low, base, high = adverse, base, favourable mix and cost.

| Scenario | Pricing | Low | Base | High | Midwives (base) | FTE (base) |
|---|---|---|---|---|---|---|
| A, 54 a week | **Bulk billed** | -A$5,628 | -A$907 | +A$3,262 | 2 | 1.41 |
| A, 54 a week | **Structure B private (E)** | -A$769 | **+A$5,541** | +A$10,619 | 2 | 1.41 |
| A, 54 a week | Half bulk, half gap 30% (R14) | -A$2,795 | +A$2,852 | +A$7,551 | 2 | 1.41 |
| B, 84 a week | **Bulk billed** | -A$8,610 | -A$1,306 | +A$5,157 | 3 | 2.19 |
| B, 84 a week | **Structure B private (E)** | -A$1,052 | **+A$8,725** | +A$16,601 | 3 | 2.19 |
| B, 84 a week | Half bulk, half gap 30% (R14) | -A$4,203 | +A$4,542 | +A$11,828 | 3 | 2.19 |

396 basis (Monday to Friday only; A = 198 a month, 45.7 a week; B = 317 a month, 73.1 a week):

| Scenario | Pricing | Low | Base | High | Midwives / FTE (base) |
|---|---|---|---|---|---|
| A | Bulk billed | -A$4,346 | -A$245 | +A$3,255 | 2 / 1.19 |
| A | Structure B private (E) | -A$235 | +A$5,211 | +A$9,480 | 2 / 1.19 |
| B (14.4 a day) | Bulk billed | -A$5,389 | +A$747 | +A$6,099 | 2 / 1.90 |
| B (14.4 a day) | Structure B private (E) | +A$1,190 | +A$9,477 | +A$16,059 | 2 / 1.90 |

Base line items, A six-day: bulk revenue A$14,205, private A$20,653; wages A$12,511 (53.4 paid hours a week at A$54.07 on-cost-loaded); consumables A$702; fixed A$1,899. B six-day: revenue A$22,097 bulk or A$32,128 private; wages A$19,462 (83.1 hours); consumables A$1,092; fixed A$2,848.

**Which is which:** "Bulk billed" = GTT receives only the Medicare benefit and the client pays nothing. "Structure B private" = GTT Medical Services charges the full private fee, the client pays it and claims the rebate back from Medicare herself. Gross billings to GTT Medical are the private fee, not the rebate. The cost side is identical. The consult income is GST-free (E, Medicare-rebated medical service; Catherine to confirm).

If leave is grossed up as in 1.3 (E), subtract about A$1,700 (A) or A$2,700 (B) a month from every row.

## Part 3. WA payroll tax

### 3.1 The rule (V, WA Government payroll tax guide, calculation page)

| Item | Value |
|---|---|
| Rate | 5.5% of taxable wages |
| Annual threshold | A$1,000,000 (monthly A$83,333) |
| Mechanism | **Not "excess only".** A deduction that tapers: deduction = A$1,000,000 - (wages - A$1,000,000) x 2/13. Zero at A$7,500,000. Tax = 5.5% x (wages - deduction). Page example: A$1.2m wages gives deduction A$969,231 |
| Marginal rate above A$1m | 5.5% x 15/13 = **6.35%** on every extra dollar |
| 2026-27 change | None found on the page (E: same settings) |
| Super counts? | **Yes.** Pay-roll Tax Assessment Act 2002 (WA) Division 2A s9CB treats super contributions as wages. I could confirm the section heading; the WA guide page itself did not show it. Catherine to confirm |
| Workers comp premium | Not taxable wages |
| Grouping | Related bodies corporate share ONE deduction. Splitting into Holdings, Medical and Lounge gives no extra threshold. You model with the group total (Catherine confirms) |

### 3.2 Reconciling R14

| | R14 | Corrected |
|---|---|---|
| Repo base used | A$987,817 (wages only, A$82,318.05 x 12) | **A$1,106,355** (wages A$82,318.05 + super A$9,878.17 = A$92,196.22 a month x 12) |
| Repo position vs threshold | A$12,183 under | **A$106,355 over** |
| Repo-only tax | A$0 | **A$6,749 a year, A$562 a month** |
| Scenario A total tax | A$8,755 a year, **A$730 a month** | A$15,749 a year, **A$1,312 a month** (midwives add A$750) |
| Scenario B total tax | A$14,048 a year, **A$1,171 a month** | A$20,749 a year, **A$1,729 a month** (midwives add A$1,167) |

R14's A$730 and A$1,171 were the **whole group's** tax, not the midwives' share, and they started from a base that left super out. The midwife hours in R14 were not too few: A was 53.4 paid hours a week (231 a month) and B 83.1 (360 a month). The workers comp component of the repo (A$1,399.41 a month) is correctly excluded. Note the repo net of A$35,186.40 contains no payroll tax at all, so A$562 a month is a new cost line against the repo.

### 3.3 Tax by group payroll (annual taxable wages = wages + super + leave loading)

| Case | Taxable wages a year | Tax a year | Tax a month | Added by this change a month |
|---|---|---|---|---|
| Repo only | A$1,106,355 | A$6,749 | A$562 | n/a |
| Repo + receptionist + host (E) | A$1,250,171 | A$15,876 | A$1,323 | +A$761 |
| Repo + 1 full-time midwife (38 h) | A$1,207,269 | A$13,154 | A$1,096 | +A$534 |
| Repo + 2 full-time midwives | A$1,308,183 | A$19,558 | A$1,630 | +A$1,067 |
| Repo + 3 full-time midwives | A$1,409,098 | A$25,962 | A$2,164 | +A$1,601 |
| Repo + Scenario A hours (2 midwives, 53.4 h a week) | A$1,248,166 | A$15,749 | A$1,312 | +A$750 |
| Repo + Scenario B hours (3 midwives, 83.1 h a week) | A$1,326,950 | A$20,749 | A$1,729 | +A$1,167 |
| Repo + receptionist/host + A | A$1,391,982 | A$24,876 | **A$2,073** | +A$1,511 |
| Repo + receptionist/host + B | A$1,470,766 | A$29,876 | **A$2,490** | +A$1,927 |

Midwife taxable wage bill against tax (repo base included): A$0 a month = A$562 tax; A$1,000 = A$626; A$2,500 = A$721; A$5,000 = A$880; A$10,000 = A$1,198; A$15,000 = A$1,515; A$20,000 = A$1,833; A$25,000 = A$2,151 a month. Every extra A$1,000 a month of wages costs A$63.46 a month in tax. Monthly taxable wages are A$92,196 against the A$83,333 monthly threshold, so GTT must register and lodge from the first full pay month.

## Part 4. Complete clinic workforce

The repo costs service staff and the venue manager only. After the founder decision of 2026-08-21 there is **no receptionist cost line** (AM reception is the venue manager's 8-hour day, PM check-in is done by PM treatment staff). There is no clinic host and no midwife in the repo. Rates in the repo are casual loaded (25%) and 12% super plus 1.7% workers comp are added on top.

### 4.1 Roster, hours and cost (monthly, 22 weekdays and 4.33 Saturdays)

| Role (profession) | Award and level | Heads | Hours a week (all heads) | Hourly rate | Wages a month | Loaded a month (wages + 12% super + 1.7% workers comp) | Entity | Source |
|---|---|---|---|---|---|---|---|---|
| Massage and beauty therapists | Hair and Beauty Industry MA000005, repo L3/L4, casual loaded | 4 | 145.8 | A$37.50 | A$25,645.50 | A$29,158.93 | Lounge | R |
| Nail technicians | MA000005 L3, casual loaded | 2 | 72.9 | A$36.81 | A$12,586.81 | A$14,311.20 | Lounge | R |
| Hairdressers | MA000005 L3, casual loaded | 2 | 72.9 | A$36.81 | A$12,586.81 | A$14,311.20 | Lounge | R |
| Phlebotomists (full roster 10 to 18 booked; 1 on mornings of 9 or fewer) | Health Professionals and Support Services MA000027, casual loaded | 2 | 72.9 | A$34.375 | A$11,754.19 | A$13,364.51 | Medical | R |
| Venue manager (Mon to Fri) | MA000005 L6 salon manager (repo; confirm) | 1 | 40.6 | A$40.00 | A$7,040.00 | A$8,004.48 | Lounge | R |
| PM treatment staff (4 roles, 3-hour floor, 10 sessions) | MA000005 casual loaded | 4 | 72.9 | A$37.16 blended | A$12,704.74 | A$14,445.29 | Lounge | R |
| **Repo total** | | | | | **A$82,318.05** | **A$93,595.63** | | R |
| AM receptionist / guest coordinator (5.25 h Mon to Sat) | Clerks Private Sector MA000002 L1 to L2 (job posting), casual loaded | 1 | 31.9 | A$33.38 | A$4,993.61 | A$5,677.73 | Lounge | **E** |
| Clinic host (6 h Mon to Sat) | Clerks MA000002 or hospitality; Grace and Anthony to confirm | 1 | 36.5 | A$33.38 proxy | A$5,706.98 | A$6,488.83 | Lounge | **E** |
| Midwives, Scenario A (base) | Nurses MA000034 RN L2 pp4, permanent (class E) | 2 | 53.4 | A$54.07 loaded | A$12,511 | A$12,511 (on-cost included) | Medical | R14, E |
| Midwives, Scenario B (base) | as above | 3 | 83.1 | A$54.07 loaded | A$19,462 | A$19,462 | Medical | R14, E |

Reconciliation: the six repo rows add to A$82,318.05, exactly the repo "Direct Labor + Opening Costs" line (cost_ramp.yml cost_table1_m5plus). Repo super A$9,878.17 and workers comp A$1,399.41 add to A$93,595.63. Differences: none beyond cents. **What the repo lacks:** receptionist, host, midwives, payroll tax, any award uplift after 1 July 2025 (repo rates are the 2025-07-01 table). Receptionist and host rates use the repo's receptionist rate A$33.38 (2025-07-01). A 1 July 2026 uplift is Q (a third-party site says 4.75%, not confirmed).

### 4.2 Total clinic payroll a month and the split between companies

| Case | Medical (midwives, phlebotomists) | Lounge (therapists, manager, reception, host, PM) | Total loaded | Taxable wages (wages + super) |
|---|---|---|---|---|
| Repo as is | A$13,365 | A$80,231 | A$93,596 | A$92,196 |
| Repo + receptionist + host (E) | A$13,365 | A$92,398 | A$105,762 | A$104,181 |
| Repo + receptionist + host + midwives A | A$25,876 | A$92,398 | **A$118,274** | A$115,998 |
| Repo + receptionist + host + midwives B | A$32,827 | A$92,398 | **A$125,224** | A$122,564 |

Group payroll tax on these totals: A$562, A$1,323, **A$2,073** and **A$2,490** a month (Part 3). The entity split makes no difference to payroll tax (one group threshold).

### 4.3 Flags for Grace and Anthony

1. **Phlebotomist award rate.** The repo uses A$27.50 ordinary (A$34.375 casual loaded). Your R14 note puts collectors at Levels 5 to 7, A$30.45 to A$32.67 ordinary (a third-party site shows A$30.63 for Certificate III under 12 months). Casual loaded that is A$38.06 to A$40.84. For two phlebotomists on the repo hours: wages +A$1,261 to +A$2,210 a month, loaded +A$1,434 to +A$2,513. Not changed in the repo. Needs confirmation.
2. Venue manager award level (MA000005 L6) is E in the repo itself.
3. Massage and beauty therapists: Hair and Beauty Industry Award MA000005 is the repo's choice. A massage therapist can also fall under HPSS MA000027. **Needs Grace's and Anthony's confirmation.**
4. The phlebotomist job posting promises 25 hours a week; the adaptive roster gives 9 to 18. Casual or a guaranteed minimum (repo flag).
5. Route 1 would move the phlebotomists to the lab: Medical drops A$13,365 a month (and the payroll tax base drops by their taxable wages).

## Part 5. Three-tier structure financials

GTT Holdings Pty Ltd owns 100% of GTT Medical Services Pty Ltd and GTT Lounge Sanctuary Pty Ltd. Names are unregistered placeholders.

### 5.1 Set-up and running cost of 3 companies against 1 (extra two companies)

| Item | Low | Base | High | Label |
|---|---|---|---|---|
| ASIC registration, 2 extra companies at A$636 | A$1,272 | A$1,272 | A$1,272 | V-secondary (sites quote ASIC from 1 Jul 2026; the ASIC page did not render figures) |
| Legal: constitutions, shareholder agreement, inter-company agreements, IP assignment | A$3,000 | A$7,500 | A$15,000 | Q |
| Accountant: restructure, tax consolidation and GST group set-up | A$1,500 | A$3,000 | A$6,000 | Q |
| Business name (A$47 one year or A$108 three years, per your brief; not re-verified) | A$47 | A$108 | A$108 | per brief |
| **One-off total** | **A$5,819** | **A$11,880** | **A$22,380** | |
| ASIC annual review fee, 2 extra at A$342 | A$684 | A$684 | A$684 | V-secondary |
| Accountant: statutory accounts and tax workpapers, 2 extra entities | A$3,000 | A$5,000 | A$8,000 | E |
| Bookkeeping, BAS and payroll compliance, 2 extra | A$1,200 | A$3,000 | A$6,000 | E (one BAS if GST group) |
| Bank accounts and payroll software | A$360 | A$720 | A$1,200 | E |
| Insurance (separate policies or endorsements) | A$500 | A$1,500 | A$3,000 | Q |
| **Running total a year / a month** | **A$5,744 / A$479** | **A$10,904 / A$909** | **A$18,884 / A$1,574** | |

Payroll tax: **no saving and no extra threshold** (grouped). Three payroll registrations, one deduction.

### 5.2 How the A$250 Structure B package splits

| Part | Amount | Who | GST (E) | Share of A$250 |
|---|---|---|---|---|
| Midwife consult | A$110.00 | Medical | GST-free (Medicare-rebated medical service) | 44.0% |
| Lab test and collection (66548 A$19.90 + 73938 A$7.95) | A$27.85 | Lab's own account. GTT is the lab's agent if it collects, and remits. **Not GTT revenue** | GST-free pathology | 11.1% |
| Lounge services | A$112.15 | Lounge | Taxable: GST A$10.20, ex GST A$101.95 | 44.9% |
| **GTT group keeps** | **A$222.15** (A$211.95 ex GST) | Medical + Lounge | | 88.9% |
| Medicare rebate to the client (75.65 + 16.95 + 6.80) | A$99.40 | Paid to the mother's bank | | |
| **Client pays after rebate** | **A$150.60** | | | |

With the base mix average rebate (A$84.46) the client pays A$165.54. Holdings keeps none of the A$250 directly. It receives only what the inter-company agreements say (below).

### 5.3 Inter-company flows (illustrative, E) and tax

| Flow | Illustration | Tax effect |
|---|---|---|
| IP licence fee, subsidiaries to Holdings | 2% of lounge revenue ex GST: about A$2,601 a month on all lounge revenue, A$477 on bundle clients only | Nil when consolidated. Otherwise a **royalty is passive income** for Holdings |
| Management fee, Medical to Lounge (reception, booking, hosts) | 5% of Medical revenue: about A$1,287 a month at Scenario A | Nil when consolidated |
| Facility/room fee, Medical to Lounge | 2 rooms x 12 sqm x A$40 = A$960 a month (already inside R14 fixed costs) | Nil when consolidated |
| Dividends up to Holdings, then to Anthony and partner | Franked at 25% | Franking credits flow out with Route B dividends |

- **Base rate entity (25% rate):** needs turnover under A$50m and no more than 80% passive income. Catherine's [BASE-RATE-ENTITY.md](/opt/openclaw/second-brain/knowledge/legal/BASE-RATE-ENTITY.md) (V, s23AB): dividends from a 100% owned subsidiary are non-portfolio dividends and are **not** passive. Royalties and rent **are** passive. **Rate risk:** if Holdings is left outside tax consolidation and its income is only an IP licence royalty, it is 100% passive and pays 30%, not 25%. **Tax consolidation removes the risk** (head company return, intra-group flows ignored, the test runs on the group). I model the group as consolidated at 25%.
- **GST grouping:** a GST group makes inter-company charges GST-neutral (one BAS). Otherwise cash timing only.
- **Division 7A:** a loan from one group company to another company is not itself a deemed dividend (s109J); one that ends with an individual shareholder or associate is (s109T). Owners' loans into the group (R4 loan-first repayment) go the other way. Catherine to confirm.
- **Company tax** is 25% of group profit in the table below. Not in the repo.

### 5.4 Raising the package price (monthly, group, after GST, before payroll tax and structure costs)

Basis: Structure B bundle for the consult clients (A = 234 a month, B = 364 a month), consult flat A$110 (GST-free E), lab A$27.85 passes through, the rest is lounge (GST-inclusive). Those clients would have paid the repo A$250 lounge-only price. Repo after-GST profit **A$23,442.58 (R)**. Midwife cost from R14 base. Rebate to the client A$99.40 (example). Break-even = the profit that equals the repo.

| Package price | Client pays after A$99.40 rebate | Lounge part (incl GST) | GST on lounge | Group net, A (234) | Group net, B (364) | Against repo A$23,443 |
|---|---|---|---|---|---|---|
| A$250 | A$150.60 | A$112.15 | A$10.20 | **A$4,746** | **-A$5,536** | well below |
| A$275 | A$175.60 | A$137.15 | A$12.47 | A$10,064 | A$2,737 | below |
| A$300 | A$200.60 | A$162.15 | A$14.74 | A$15,382 | A$11,010 | below |
| A$325 | A$225.60 | A$187.15 | A$17.01 | A$20,701 | A$19,283 | below |
| A$350 | A$250.60 | A$212.15 | A$19.29 | A$26,019 | A$27,555 | above |
| **A$387.85 (lounge stays A$250)** | A$288.45 | A$250.00 | A$22.73 | **A$34,070** | **A$40,080** | above by A$10.6k / A$16.6k |

- **Break-even package price against the repo: A$337.89 (A) and A$337.57 (B).** Below it, putting the consult inside the package makes the group worse off than today's model. Minimum bundle clients at A$350: 50 a month; at A$387.85: 18 a month. Below A$325 no number of clients reaches break-even.
- Compare with **bulk billing the consult and keeping the lounge at A$250**: group net **A$22,535 (A)** and **A$22,137 (B)**, change -A$907 and -A$1,306 (Part 2). The client pays A$250 and nothing for the consult.
- Whether the client accepts A$288 after rebate is a market question, not mine. Uptake is not modelled here. R14's package uptake break-even (65.7% at A$250) still applies to the lounge package.

### 5.5 Group P&L, monthly (base cost, bundle clients, group consolidated, E)

| Line | P = A$250, A | P = A$250, B | P = A$387.85, A | P = A$387.85, B |
|---|---|---|---|---|
| Repo profit after GST (R) | 23,443 | 23,443 | 23,443 | 23,443 |
| + Consult income (A$110 each) | +25,740 | +40,040 | +25,740 | +40,040 |
| - Midwife wages, consumables, fixed | -15,112 | -23,402 | -15,112 | -23,402 |
| Lounge repricing against repo, ex GST | -29,324 | -45,616 | 0 | 0 |
| - Card fees (1.7% + 30c on A$ collected) | -954 | -1,484 | -1,502 | -2,337 |
| - Payroll tax on repo wages (new line) | -562 | -562 | -562 | -562 |
| - Payroll tax added by midwives | -750 | -1,167 | -750 | -1,167 |
| - Three-company running cost (base) | -909 | -909 | -909 | -909 |
| **Group profit before company tax** | **1,571** | **-9,657** | **30,347** | **35,106** |
| Company tax 25% | 393 | 0 | 7,587 | 8,776 |
| **After company tax** | **1,178** | **-9,657** | **22,760** | **26,329** |

Baseline with no midwife: repo A$23,443 less payroll tax A$562 less three-company cost A$909 = **A$21,971**. The **extra cost of the 3-company structure** is A$479 / A$909 / A$1,574 a month plus A$5,819 / A$11,880 / A$22,380 once. It has no tax saving unless the company is later sold or an asset (IP, lease) needs protection; that is Catherine's.

## Part 6. Structure B cash flow

### 6.1 Per client, at A$250 (card fee 1.7% + 30c, E, provider Q)

| Step | Option X: pay all A$250 online | Option Y (recommended): pay A$222.15 online, lab A$27.85 at appointment |
|---|---|---|
| At online booking | Client pays A$250.00. Card fee A$4.55. Lab's A$27.85 held in a separate account | Client pays A$222.15. Card fee A$4.08 |
| At appointment | Nothing further. GTT remits A$27.85 to the lab (weekly or at test day) | Client pays A$27.85 to the lab on the lab's own terminal. Lab issues its own account and receipt |
| Midwife consult account | GTT Medical gives a paid tax invoice for A$110 with the item number so the client can claim | Same |
| Medicare | Client claims: consult item A$75.65 (82110 example) plus test A$16.95 plus collection A$6.80 = **A$99.40**, paid to her bank. Never touches GTT | Same |
| GST | Lounge A$112.15 includes A$10.20 GST due to the ATO. Consult and lab GST-free (E) | Same |
| GTT keeps before staff and rent | A$207.40 | **A$207.88** |
| Client's net cost | A$150.60 (A$165.54 on the mix-average rebate) | Same |
| Cash-timing gap | GTT holds A$27.85 per booked client for the 2 to 4 week lead. At 396 clients a month about **A$7,618** (E) is the lab's money. Needs a ring-fenced account, agency terms, and the lab's invoice rules | None |

Medicare pays the client's bank a few days after she claims (E); that is not GTT's cash. GTT pays the lab on no terms under Y. Under X the terms are whatever the lab agrees, and I recommend weekly remittance. **Recommendation: Y.** One payment is nicer for the client; Y costs her one tap at the lab and removes the agent, float and GST risk. The online booking page should say "plus A$27.85 pathology fee paid to the lab at your appointment".

### 6.2 Refund guarantee reserve (cap A$27.85 per client, per Catherine)

Exposure = refused clients x A$27.85. Reserve = two months of exposure (E).

| Clients a month | Refusal rate | Refused clients | Exposure a month | Two-month reserve |
|---|---|---|---|---|
| 396 | 2% | 7.9 | A$221 | **A$441** |
| 396 | 5% | 19.8 | A$551 | **A$1,103** |
| 396 | 10% | 39.6 | A$1,103 | **A$2,206** |
| 473.94 (six-day) | 2% | 9.5 | A$264 | A$528 |
| 473.94 | 5% | 23.7 | A$660 | A$1,320 |
| 473.94 | 10% | 47.4 | A$1,320 | A$2,640 |

**Does 100% of the lounge portion stay with the Lounge?** Yes: A$112.15 of A$250 (44.9%) is Lounge revenue if the Lounge invoices it and has its own merchant account (provider Q). If one merchant account sits in Medical or Holdings, the lounge portion must be swept to the Lounge by written inter-company entry the same week. I recommend a Lounge account.

## Part 7. Route 1 steps: cost now and at lease signing

Grace owns the checklist. These are the cost lines I can state.

| Step | Cost now | Cost at lease signing | Label |
|---|---|---|---|
| Medicare provider number, form HW088 | A$0 | A$0 | E (no fee found) |
| ABN, each company | A$0 | A$0 | V |
| PRODA account | A$0 | A$0 | V |
| Ahpra registration check | A$0 | A$0 (renewal A$193 a year is the midwife's or by contract) | V |
| Register 3 companies | **A$1,908** | A$0 | V-secondary |
| Business name for the Lounge (1 year) | **A$47** (A$108 for 3 years) | A$0 | per brief |
| Lab agreement and second paper (legal review) | A$0 | about A$6,000 (A$3,000 to A$15,000) | Q |
| Landlord written consent | A$0 | A$0 | E |
| Bond, about 2 months rent | A$0 | **A$16,000** (A$8,000 a month, R) | R |
| Insurance, first quarter | A$0 | **A$2,125** (A$708.34 a month, R) | R |
| Collection-centre approval paperwork | A$0 | A$0 (the lab applies) | R |
| **Total** | **A$1,955** | **A$24,125** | |

## Decisions Anthony must make

1. **Package price for Structure B.** At A$250 all-in the group loses about A$18,700 (A) to A$29,000 (B) a month against the repo. Pick: A$387.85 like-for-like (client pays A$288.45 after rebate), a price near A$338 or higher, or bulk bill the consult and keep the lounge at A$250.
2. **Private consult fee.** A$110 for 82110 is your R14 example (E). I scaled the others by 1.236. Needs a Perth benchmark (Q).
3. **Permanent or casual midwives.** Permanent, with leave covered, costs about A$1,700 to A$2,700 a month more than R14 showed on bulk billing.
4. **Cash option X or Y** (I recommend Y).
5. **Three companies or one.** Costs A$909 a month and A$11,880 up front (base) with no payroll tax or income tax saving. Needs Catherine's view on asset protection and the lab or midwife liability side.
6. **Receptionist and host.** Hire them (A$12,167 a month loaded, E) or leave the venue manager to cover reception. Grace's roster decides. Their rates and award (Clerks MA000002 or hospitality) need her confirmation.
7. **Phlebotomist and therapist award levels** (flags 4.3.1 and 4.3.3).
8. Whether payroll tax is accepted as a new cost line in the repo (A$562 a month today). I have not changed the repo.

## What is verified and what is not

V: MBS items and fees (MBS Online, read 2026-10-24; 82115 re-read this round); WA payroll tax rate, threshold, taper (WA Government guide); base rate entity passive income (s23AB, Catherine's file); ASIC A$636 and A$342 are secondary-source figures (the ASIC page did not render them). Not verified: super in WA taxable wages (statute heading seen, WA guide page silent), midwifery GST status (E; ATO s38-10 list I could read did not show midwifery, but Medicare-rebated services are generally GST-free medical services), 2026-27 award uplift, WA workers comp rate for health, Perth private midwife fees, legal and accountant quotes.
