# Round 14 (Theodore): midwife P&L at real GTT volume, lab cash journey, package uptake, WA payroll tax

General knowledge and desk research, not personal documents. Verify before acting. Prepared 2026-10-24. A plan, not a forecast. All amounts are Australian dollars (A$). Script: [theodore_r14.py](theodore_r14.py) (imports and reuses [theodore_r13.py](../L8-r13/theodore_r13.py); no second calculator). Results: [theodore_r14_results.json](theodore_r14_results.json).

Labels: **V** = verified from an official or listed source this round. **E** = my estimate. **Q** = quote needed.

## The answers first

1. **The midwife is not a big profit engine on Medicare bulk billing alone.** At the real GTT volume she earns about A$61 a paid hour (bulk billed, base mix, after admin and idle time) and costs A$63 to A$65 a paid hour all-in (wages, consumables, fixed costs). Base case, bulk billed: roughly break-even (-A$1,306 to +A$747 a month). With private fees (schedule fee plus 30% gap on half of clients) base case is +A$2,852 to +A$5,837 a month. More consults do not fix a thin margin; a better fee per hour does.
2. **She needs 1.4 to 2.2 full-time midwives at 54 to 84 consults a week**, so you need a second midwife (or a locum) in every scenario, and a third at 84 a week on a six-day roster.
3. **Under bulk billing GTT pays the lab nothing per sample.** GTT is still out of pocket about A$2.57 to A$24.33 a client for the drink, cups, and (if charged at market price) tubes, needles and courier. Base A$14.78. If Medicare refuses a claim and GTT absorbs the lab bill, add A$27.85 a client.
4. **Package uptake break-even is 65.7%.** Below that GTT loses money every month. At 100% (Anthony's mandatory model) net is the repo A$35,186.40. At 80% it falls to A$11,786. The old repo "break-even 7.25 clients a day (40.3%)" was a volume figure with one phlebotomist; it does not apply to uptake because all 18 clients still need two phlebotomists.
5. **Payroll tax starts almost at once.** Repo wages are A$987,817 a year, A$12,183 under the A$1,000,000 WA threshold. Any midwife wage bill above A$1,015 a month crosses it.

## Part 1. Midwife P&L

### 1.1 Verified Medicare items (MBS Online item pages, read 2026-10-24, V)

I read these through a page summariser. Each page showed fee and 85% benefit. 85% arithmetic checks out (91211 shows A$32.95 against A$32.94 by arithmetic, a rounding point).

| Item | Service | Fee | Benefit 85% | Minutes | Telehealth item |
|---|---|---|---|---|---|
| 82100 | Initial antenatal, **once per pregnancy** | A$89.00 | A$75.65 | 60 | None (not telehealth) |
| 82105 | Short antenatal | A$38.75 | A$32.95 | 10 | 91211 video, 91218 phone |
| 82110 | Routine antenatal | A$89.00 | A$75.65 | 40 | 91212 video, 91219 phone |
| 82130 | Short postnatal, within 6 weeks | A$63.90 | A$54.35 | 20 | 91214 video, 91221 phone |
| 82135 | Routine postnatal, within 6 weeks | A$130.80 | A$111.20 | 40 | 91215 video, 91222 phone |

The 82110 = 82100 fee anomaly: both pages say A$89.00, so it is as published. A 40-minute routine visit pays the same as a 60-minute initial visit. Postnatal fees (82135 A$130.80) are higher than antenatal. Catherine to confirm against the MBS PDF, but I used the published numbers. Telehealth pays the same fee as in person. Telehealth is out-of-hospital only and only where safe and clinically appropriate.

### 1.2 How the mix changes income (bulk billed, per consult)

Consults happen days to weeks before test day, so I use **antenatal items only**. The postnatal tail is upside (below). Only one 82100 per pregnancy, so the share of 82100 is capped by how many clients are new to midwife care.

| Mix | 82100 / 82105 / 82110 | Avg clinical min | Bulk billed per consult | Private at schedule | Bulk per clinical hour |
|---|---|---|---|---|---|
| Adverse (E) | 10 / 70 / 20 | 21.0 | A$45.76 | A$53.83 | A$130.74 |
| Base (E) | 25 / 35 / 40 | 34.5 | A$60.71 | A$71.41 | A$105.57 |
| Favourable (E) | 40 / 15 / 45 | 43.5 | A$69.25 | A$81.46 | A$95.51 |

Journey for one client, bulk billed (V fees): initial only A$75.65 (60 min). Initial plus short A$108.60 (70 min). Initial plus routine A$151.30 (100 min). Initial plus routine plus short A$184.25 (110 min). A client with no initial and one short visit pays A$32.95 (10 min). Postnatal upside per client who stays with the midwife: A$54.35 (82130) or A$111.20 (82135), not in any net figure below.

### 1.3 Capacity: how many midwives?

Full-time = 38 hours (Award). "With admin" adds 10 minutes a consult and 75% utilisation (E).

| Consults a week | 30 min each | 45 min each | 60 min each |
|---|---|---|---|
| 54 (clinical hours only) | 27.0 h, 0.71 FTE | 40.5 h, 1.07 FTE | 54.0 h, 1.42 FTE |
| 54 (with admin, utilisation) | 1.26 FTE | 1.74 FTE | 2.21 FTE |
| 84 (clinical hours only) | 42.0 h, 1.11 FTE | 63.0 h, 1.66 FTE | 84.0 h, 2.21 FTE |
| 84 (with admin, utilisation) | 1.96 FTE | 2.70 FTE | 3.44 FTE |

### 1.4 Monthly and weekly P&L, net to GTT (before payroll tax)

Four volumes. The two "396 basis" rows follow Anthony's request (50% = 198, 80% = 317 a month; weeks = month / (52/12)). The two "six-day" rows follow the 9 and 14 a day figures (54 and 84 a week, x 52/12 = 234 and 364 a month). **These two sets disagree because 396 is a Monday to Friday count (18 x 22).** The repo's A$118,485 AM revenue uses 473.94 clients a month, a six-day week, so the six-day rows are the ones that match the repo money. Pick one and keep it.

Low = adverse mix and cost. Base. High = favourable mix and cost. Wage uses Fair Work Pay Guide MA000034 from 1 Jul 2026 (V): RN L3 pp1 A$42.93, L2 pp4 A$41.59, L2 pp1 A$39.59 an hour ordinary, Saturday 150%. On-costs 1.25 / 1.20 / 1.14 (super 12% V, rest E). Award class for an endorsed midwife is E.

**Bulk billed (all clients):**

| Volume | Consults wk / mo | Midwives (base) | Net a week low / base / high | Net a month low / base / high |
|---|---|---|---|---|
| A 50%, 396 basis | 45.7 / 198 | 2 (1.19 FTE) | -A$1,003 / -A$57 / +A$751 | -A$4,346 / -A$245 / +A$3,255 |
| A 50%, six-day | 54 / 234 | 2 (1.41) | -A$1,299 / -A$209 / +A$753 | -A$5,628 / -A$907 / +A$3,262 |
| B 80%, 396 basis | 73.1 / 317 | 2 (1.90) | -A$1,244 / +A$172 / +A$1,407 | -A$5,389 / +A$747 / +A$6,099 |
| B 80%, six-day | 84 / 364 | 3 (2.19) | -A$1,987 / -A$301 / +A$1,190 | -A$8,610 / -A$1,306 / +A$5,157 |

**Mixed pricing (half bulk billed, half private at fee + 30% gap, gap is E, no Perth benchmark found):**

| Volume | Net a week low / base / high | Net a month low / base / high |
|---|---|---|
| A 50%, 396 basis | -A$450 / +A$677 / +A$1,589 | -A$1,949 / +A$2,936 / +A$6,884 |
| A 50%, six-day | -A$645 / +A$658 / +A$1,742 | -A$2,795 / +A$2,852 / +A$7,551 |
| B 80%, 396 basis | -A$358 / +A$1,347 / +A$2,747 | -A$1,553 / +A$5,837 / +A$11,905 |
| B 80%, six-day | -A$970 / +A$1,048 / +A$2,730 | -A$4,203 / +A$4,542 / +A$11,828 |

Private at schedule fee only (no gap) sits between the two (A 396 basis: -A$2,749 / +A$1,875 / +A$5,674 a month). Full grid in the JSON.

Base line items, A 50% six-day, bulk billed: revenue A$14,205 a month (A$3,278 a week); wages A$12,511 (53.4 paid hours a week at A$54.07 an hour with on-costs and Saturday mix); consumables A$702 (A$3 a consult, E); fixed A$1,899 (two midwives' registration A$193 a year each V, indemnity A$2,500 E, CPD, software, equipment over 5 years, two rooms at A$40 per sqm rent, 12 sqm). Net -A$907. Room cost is small because rooms are 12 sqm at the repo rate and telehealth cuts room need.

**Why more consults barely helps:** one bulk-billed paid hour earns about A$61 and costs A$63 to A$65 including on-costs, consumables and fixed costs. The profit comes from fee per hour (private gap, short items, telehealth with no room), not from volume. Break-even consults a week, base cost: bulk billed 27, private at schedule 12, mixed 9. Adverse cost never breaks even.

### 1.5 If only some clients are GTT-eligible (no GP request)

Consults scale down with the share of clients who really need the midwife to order the test. Base case, six-day, net a month:

| Eligible share | A 50% bulk | A 50% mixed | B 80% bulk | B 80% mixed | Midwives |
|---|---|---|---|---|---|
| 100% | -A$907 | +A$2,852 | -A$1,306 | +A$4,542 | 2 / 3 |
| 70% | -A$255 | +A$2,376 | -A$819 | +A$3,274 | 1 / 2 |
| 40% | -A$553 | +A$951 | -A$332 | +A$2,007 | 1 / 1 |

It does not fall in a straight line because a whole extra midwife (indemnity, equipment, room) switches on or off. Dropping from 2 midwives to 1 at 70% removes the idle second head. Low and high are in the JSON.

## Part 2. Lab per-sample charge under the midwife route

**What the lab charges GTT per sample: nothing published, and under bulk billing nothing is due.** The lab bills Medicare for 66548 (A$19.90 fee, A$16.95 at 85%) plus the collection item 73938 (A$7.95, A$6.80). Total Medicare to the lab A$23.75 at 85% (repo basis). If the benefit were 100% of fee it would be A$27.85; I have not confirmed which applies here, so I used the repo 85%. GTT pays no test fee. I found no published Perth lab "per sample service fee". Whether a lab may lawfully charge GTT one, and the Part IIBA rules on market-value consideration (s 23DZZIF(6): free tubes or courier need market consideration, per [ACC-GAME-PLAN.md](../L3-acc/ACC-GAME-PLAN.md)), is Catherine's. I give cost lines only.

### 2.1 Costs GTT may still carry per client (3 draws)

| Line | Low | Base | High | Source and label |
|---|---|---|---|---|
| Glucose drink 75g | A$2.27 | A$2.39 | A$2.52 | V listing: [Livingstone Glucaid 75g, 24 per carton, A$54.41 to A$60.45 incl GST](https://www.livingstone.com.au/products/glucaid075n-glucaid-drink-75g-300ml-24-ctn-clear). PathWest does not supply the drink ([PARTNER-LAB-REQUIREMENTS.md](../L2-medicare/PARTNER-LAB-REQUIREMENTS.md)) |
| Cups, water, tissues | A$0.30 | A$0.60 | A$1.00 | E |
| Grey top tubes x 3 | A$0 | A$0.99 | A$0.99 | V listing: [Livingstone fluoride oxalate 100 box A$32.95 incl GST](https://www.livingstone.com.au/Product/id/BCTFLOX/BLOOD-PLASTIC-TUBE-FLUORIDE-OXALATE-5ML-13X100MM-GREY-100-BX). Low: PathWest said tubes and bags are free |
| Needles x 3 (butterfly set) | A$0 | A$9.00 | A$10.89 | V single unit [Livingstone 21G set A$3.63](https://www.livingstone.com.au/products/bd368652nl-livingstone-blood-collection-set-21gx0-75-needle-green-each). Base A$3.00 each is E (box discount) |
| Courier | A$0 | A$1.50 | A$3.33 | Q. No Perth rate found. High = A$60 run / 18 clients |
| Sharps and waste | A$0 | A$0.30 | A$0.60 | E |
| Hypothetical per-sample lab fee | A$0 | A$0 | A$5.00 | Q. Does not exist in anything I found |
| **Total GTT out of pocket** | **A$2.57** | **A$14.78** | **A$24.33** | |

Month at 396 clients (bulk billed): A$1,018 / A$5,853 / A$9,635. At 473.94 (six-day) base: A$7,005.

### 2.2 Cash journey per client (base case, A$)

| Step | (a) Bulk billed | (b) Medicare refuses, GTT absorbs | (b2) Refused, client pays lab |
|---|---|---|---|
| Client pays GTT (package, separate) | 250.00 | 250.00 | 250.00 |
| Client pays lab | 0 | 0 | 27.85 |
| Medicare pays lab | 23.75 | 0 | 0 |
| Lab bills GTT | 0 | 27.85 | 0 |
| GTT pays suppliers (drink, tubes, needles, courier) | 14.78 | 14.78 | 14.78 |
| **GTT out of pocket for the test** | **14.78** | **42.63** | **14.78** |

Low case: A$2.57 / A$30.42 / A$2.57. High case: A$24.33 / A$52.18 / A$24.33. If 2% of claims are refused and GTT absorbs them, the expected cost rises by A$0.56 a client; at 5% by A$1.39. If every claim at 396 a month were refused and absorbed, GTT would pay A$16,881 a month. **Answer: GTT is out of pocket on the supplies, not on the test, under bulk billing.** GTT earns no Medicare test money (the lab keeps it).

## Part 3. Package versus free lane

Basis: repo net A$35,186.40 a month at 18 clients a day, 473.94 AM clients a month, package A$250 (V repo), A$118,485 AM revenue. Method: uptake u is the share of the 18 daily clients who buy the package. Non-package ("free lane") clients still have their blood drawn (2 phlebotomists stay), earn GTT nothing (the lab keeps Medicare), and need no therapist. Therapist cost follows the repo rostering ladder ([CURRENT-STATE.md](https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/CURRENT-STATE.md) section 10: 2, 4, 6 or 8 therapists by clients booked; A$7,222.68 a therapist a month and A$6,682.23 a phlebotomist, derived from the ladder and checked against its 9-client row A$11,516.81). Expected cost uses a binomial spread of package clients across days. No other cost moves (rent, manager, PM, overhead are fixed). I did not model the 10% post-test discount.

| Package uptake | Package clients a day | Package revenue a month | Net a month (expected) |
|---|---|---|---|
| 100% (Anthony's mandatory model) | 18.0 | A$118,485 | **+A$35,186** (repo) |
| 80% | 14.4 | A$94,788 | **+A$11,786** |
| 60% | 10.8 | A$71,091 | **-A$2,100** |
| 40% | 7.2 | A$47,394 | **-A$9,772** |
| 20% | 3.6 | A$23,697 | -A$29,035 |
| 0% | 0 | A$0 | -A$25,517 |

Range note: a flat "round it to whole clients" version gives 80% +A$11,489, 60% -A$12,208, 40% -A$7,014. The repo ladder has a valley at 10 to 12 clients (roster steps up), so the 60% result is sensitive; expected value is the fair figure.

**Break-even uptake: 65.7%** (package only). The repo's own break-even is 7.25 clients a day (40.3% of 18) but that assumes the other clients are not booked at all, so a phlebotomist is saved. In the free lane they are booked, so it does not carry over.

### 3.1 Add the midwife (six-day volumes, base cost)

| Uptake | Package only | + Midwife A 50% bulk | + A 50% mixed | + B 80% bulk | + B 80% mixed |
|---|---|---|---|---|---|
| 100% | +A$35,186 | +A$34,279 | +A$38,039 | +A$33,881 | +A$39,729 |
| 80% | +A$11,786 | +A$10,879 | +A$14,638 | +A$10,480 | +A$16,328 |
| 60% | -A$2,100 | -A$3,007 | +A$752 | -A$3,406 | +A$2,442 |
| 40% | -A$9,772 | -A$10,679 | -A$6,920 | -A$11,078 | -A$5,230 |

Break-even uptake with the midwife: 67.5% (A 50% bulk), 49.9% (B 80% mixed). The midwife serves every client whether or not she buys the package, so her P&L does not move with uptake.

### 3.2 No package at all, Medicare only

GTT keeps all fixed costs and two phlebotomists, removes the therapists, and earns Medicare only through the midwife (the lab keeps the test money). Net before the midwife: **-A$25,517 a month**. With the midwife: -A$26,424 (A 50% bulk), -A$22,665 (A 50% mixed), -A$26,823 (B 80% bulk), -A$20,975 (B 80% mixed). A no-package lounge is a loss at the repo cost base. Cutting rent and the manager is not in the repo, so I did not model it.

## Part 4. WA payroll tax 2026-27

| Item | Value | Label and source |
|---|---|---|
| Annual threshold | A$1,000,000 (monthly A$83,333) | V: [WA Payroll Tax Employer Guide, Calculation](https://www.wa.gov.au/government/multi-step-guides/payroll-tax-employer-guide/calculation-payroll-tax-employer-guide), page last updated 2 June 2026 |
| Rate | 5.5% on taxable wages | V, same page. Rate table "from 1 July 2023" |
| Taper | Deduction = A$1,000,000 - (wages - A$1,000,000) x 2/13, nil at A$7,500,000 | V, same page (its example: A$1.2m gives A$969,231) |
| 2026-27 change | None found. The RevenueWA/WA pages do not name 2026-27 separately | E: treat 2025-26 settings as 2026-27 until RevenueWA confirms |

Repo wages: A$82,318.05 a month (the "Total Direct Labor + Opening Costs" line, with on-costs, [CURRENT-STATE.md](https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/CURRENT-STATE.md) section 5; whether it includes all super and leave loading is E) = **A$987,817 a year, A$12,183 below the threshold**. GTT crosses it when added wages exceed A$1,015 a month. Practical effect:

| Case (base, bulk billed) | Midwife wages a month | Total wages a year | Payroll tax a year / month | Midwife net after tax |
|---|---|---|---|---|
| Repo only | 0 | A$987,817 | A$0 | n/a |
| A 50% six-day | A$12,511 | A$1,137,953 | A$8,755 / A$730 | -A$1,637 a month |
| B 80% six-day | A$19,462 | A$1,221,362 | A$14,048 / A$1,171 | -A$2,476 a month |

Marginal cost above the threshold is 6.35% of extra wages (5.5% x 15/13). If repo wages came in 20% higher, tax would be A$11,764 a year. Grouping with other businesses under common control counts together (not modelled; accountant to check). A midwife engaged as a contractor may still be wages under WA's relevant contract rules.

## Assumptions

1. Repo basis unchanged: 07:00, 2 chairs, 25-minute pairs, 18 a day, A$35,186.40 net. 2. 396 is Monday to Friday; the repo money uses six days (473.94 clients). 3. All MBS fees are V from MBS Online item pages (read via a summariser). 4. Mix, admin minutes (6 / 10 / 15), utilisation (85 / 75 / 65%), gap fee 30%, on-costs and fixed costs are E. 5. The midwife is employed by GTT and GTT receives her Medicare payments (Catherine to confirm legality). 6. Midwife consults do not depend on package uptake. 7. Non-package clients still draw (2 phlebotomists). 8. 73938 stays with the lab. 9. No company tax, GST line, or depreciation modelled. 10. Medicare benefit for the test taken at 85% (repo).

## Open items

1. Catherine: confirm 82100 and 82110 fees, the 100% versus 85% test benefit, whether a lab may charge GTT a fee, and the contractor point. 2. Quotes needed: courier, needle box price, indemnity. 3. Ring two Perth midwife practices for a private fee benchmark (the 30% gap is a placeholder). 4. RevenueWA to confirm 2026-27 settings and whether the labour line is the full wages base.
