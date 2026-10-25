# Round 19 (Theodore): why profit fell, how to level the midwife, the price to get back to A$35k, and one Center of Truth

General knowledge and desk research, not your personal documents. Verify before acting. Prepared 2026-10-26. All amounts are Australian dollars (A$), per month unless stated. GTT is ONE venture: Holdings + Medical + Lounge consolidated. Nothing was sent to anyone. Structure B is not re-opened. Bulk billing is not discussed.

Script: [theodore_r19.py](theodore_r19.py). It imports [theodore_r18.py](../L13-r18/theodore_r18.py) (which imports R17, R16, R15, R14, R13) and runs the repo's own `tools/master_financial_model.py`, `tools/cost_ramp_model.py` and `tools/demand_driven_staffing_solver.py`. No second calculator. Results: [theodore_r19_results.json](theodore_r19_results.json). The script also writes [docs/FINANCIAL-CENTER-OF-TRUTH.md](../../FINANCIAL-CENTER-OF-TRUTH.md) and [center_of_truth.yml](center_of_truth.yml). Repo master numbers are unchanged.

Tags: **R** repo figure. **V** official source. **E** estimate. **Q** quote needed. **ACC** ask the accountant.

## The short answer

| Question | Answer |
|---|---|
| Why did profit drop from A$35,186 to about A$13k? | **Mostly it did not drop. A$15,852 of the A$35,186 was never real** (the repo never took out GST, card fees, payroll tax or company running costs). **A$4,329 is company tax**, and the A$35,186 was always before company tax. **Only A$2,020 a month is caused by your new decisions** (package split + midwife + venue manager 06:30) |
| Today's profit (corrected) | **A$17,314.31 before company tax, A$12,985.73 after** (A$480.99 lower than R18: I had missed card fees on afternoon sales) |
| Does the midwife lose money? | **No. The consult brings in A$110 a client; the midwife costs A$32.90 a client all in. She makes A$35,656 a month.** The money that went is lounge + service money |
| Price for A$35,186 after company tax | P1 **A$363.54** (out of pocket **A$308.54**) on the consult, or A$370.02 on lounge + service. **Not reachable at A$245 / A$295.** |
| A$20 test | **Confirmed: A$17.84 kept per client, A$8,455.09 a month before tax.** On the consult instead: A$19.66, A$9,317.66 |
| My one recommendation | **+A$20 on lounge + service (P1 A$320, P2 A$370; out of pocket A$265 / A$315). Profit A$25,769.40 before, A$19,327.05 after company tax.** Sell Package 2 as the upgrade (each 10% who take it: +A$2,113.77) |

## Pre-generation fact check (run before any number was written)

| Locked fact | Checked against | Result |
|---|---|---|
| 8 AM service staff | `cost_ramp_model.py` AM_HEADCOUNT_HIGH (4, 2, 2); wages rebuilt 22 x 6 h x (4 x A$37.50 + 4 x A$36.81) = A$39,235.68 = repo | PASS (R) |
| 2 phlebotomists on a full morning | 22 x 2 x 6 h x A$34.375 = A$9,075.00 = repo | PASS (R) |
| 4 PM service staff | PM_ROLES = 4; 22 x 4 x 3 h x A$37.155 = A$9,808.92 = repo | PASS (R) |
| Venue manager | Repo 22 x A$320 (07:00 to 15:00) = A$7,040.00; plus 0.5 h for 06:30 = A$500.28 loaded | PASS, both in the P&L |
| No hosts | No host line in the repo payroll or in R19 | PASS |
| 18 morning clients | 473.94 a month / 26.33 days = 18.00 | PASS (R) |
| Repo PM client count | 8.6957 weekday + 4.3478 Saturday transactions a day = **210.13 a month** x A$117 = A$24,585.37 = repo | PASS (R) |
| Package 2 fits the 8 staff | Repo solver runs 45-minute services: 8 staff at N = 18 | PASS: P2 needs no extra AM wages (closes R18 gap 5) |
| Midwives 45 paid h a week, one consult room | R18 inputs: 45.0 h, 1 room | PASS |
| Consult 20 min, item 82105, rebate A$32.95; total A$55.00 | MBS figures from R18 (V) | PASS |
| Consult 1 to 28 days BEFORE the test | No money effect; roster no longer tied to draw times | PASS (noted in T2 e) |
| Lab A$27.85 paid to the lab | Not in GTT revenue, not in GTT card fees | PASS |
| Card fees on every card sale | **R18 FAILED this**: no card fee on afternoon sales or on the no-midwife baseline | **FIXED in R19** |
| Banned stale values | `theodore_r19.py --check` on this file and the Center of Truth | 0 found outside the error tables |

---

## T1. Why the drop: the bridge, line by line

**The A$37,850 "lounge + service price cut", in plain English.** The old model put the whole A$250 into one line: lounge. The new A$300 package is split three ways: A$27.85 goes to the lab, A$110 is the consult (Medical) and only A$162.15 is lounge + service. So the lounge line falls by A$87.85 a client (A$79.86 ex GST) x 474 = **A$37,850.14**. But the consult line rises by **A$52,133.40** at the same time. It is mostly a relabel: net of the two, GTT takes **A$14,283.26 more**. It is not a price cut.

| Step | Change | Running figure |
|---|---|---|
| **A. Repo net today** (CURRENT-STATE line 30): no GST, no card fees, no payroll tax, no structure cost, before company tax | | **A$35,186.40** |
| GST the repo never took out (it counts the GST-inclusive A$250 and A$117 as revenue), net of GST credits | -A$11,743.82 | A$23,442.58 |
| Card fees on the old A$250 morning price (repo opex flags this as missing, VERIFICATION-TRACKER 23) | -A$2,156.43 | A$21,286.15 |
| Card fees on afternoon sales (same repo gap) | -A$480.99 | A$20,805.16 |
| Payroll tax on the repo's own wages (never in the repo net) | -A$562.45 | A$20,242.71 |
| Three-company running cost | -A$908.67 | |
| **B. Like-for-like start, no midwife, old A$250 package** | | **A$19,334.04** |
| Consult revenue, 474 x A$110 (GST-free, Medical) | +A$52,133.40 | |
| Lounge + service line: whole A$250 before, A$162.15 now (474 x A$87.85 / 1.1) | -A$37,850.14 | |
| Extra card fee (GTT now takes A$272.15 instead of A$250) | -A$180.09 | |
| Midwife wages, 45 h a week, leave covered by the casual (on-cost 1.366) | -A$12,000.38 | |
| Midwife fixed costs and consumables (one consult room) | -A$2,840.65 | |
| Venue manager 06:30 start | -A$500.28 | |
| Extra payroll tax on midwife and venue manager wages | -A$781.59 | |
| **C. Today, before company tax** | | **A$17,314.31** |
| Company tax 25% (the A$35,186.40 was always BEFORE this) | -A$4,328.58 | |
| **D. Today, after company tax = franked dividend available** | | **A$12,985.73** |

**Revenue up, profit down, why:** revenue rose A$14,283.26 a month, but costs rose A$16,302.99 (midwife A$14,841.03, venue manager A$500.28, payroll tax A$781.59, card fee A$180.09). Net **-A$2,019.73**. Per client: +A$30.14 more revenue ex GST, less A$0.38 card, A$31.31 midwife, A$1.06 venue manager, A$1.65 payroll tax = **-A$4.26 a client**.

**Like for like after company tax:** the old plan, if it had been costed honestly, was A$19,334.04 before tax = **A$14,500.53 after tax**. Today is A$12,985.73. The real gap is **A$1,514.80 a month after tax**, not A$22,000. Even the raw A$35,186.40 after company tax would be A$26,389.80, never A$35k in Anthony's hands.

**Whole venture: yes.** Both lines include Medical (consult, midwife) and Lounge (lounge + service, afternoon, all repo staff), plus Holdings' running cost. Inputs are 8 AM service staff, 2 phlebotomists, 4 PM service staff, venue manager (07:00 repo + 06:30 extra), 18 morning clients and 210.13 afternoon transactions (fact check above). R18 used the same staff inputs; what it got wrong was card fees (below).

### Per-client waterfall, Package 1 at A$300

| Step | Per client |
|---|---|
| Mother pays at booking | A$300.00 |
| To the lab (mother pays the lab, never GTT money) | -A$27.85 |
| **Reaches GTT** (consult A$110 + lounge + service A$162.15) | **A$272.15** |
| GST inside lounge + service, to the ATO | -A$14.74 |
| Card fee on A$272.15 | -A$4.93 |
| **GTT keeps from the package** | **A$252.48** |
| Plus afternoon sales per morning client (ex GST, after card fee) | +A$46.14 |
| Less repo staff (8 AM service, 2 phlebotomists, 4 PM, venue manager base) | -A$197.48 |
| Less repo running costs after GST credits | -A$27.48 |
| Less midwife wages | -A$25.32 |
| Less midwife fixed costs and consumables | -A$5.99 |
| Less venue manager 06:30 | -A$1.06 |
| Less payroll tax (group) | -A$2.84 |
| Less three-company cost | -A$1.92 |
| **Profit per client before company tax** | **A$36.53** |
| Company tax 25% | -A$9.13 |
| **Profit per client after company tax** | **A$27.40** |

Then Medicare pays the mother A$55.00 (A$32.95 consult + A$16.95 test + A$5.10 collection), so **her own cost is A$245.00 on Package 1 and A$295.00 on Package 2, and that already includes the A$27.85 lab fee.**

---

## T2. Levelling the midwife: she already pays for herself three times

| | Per client | Per month |
|---|---|---|
| Consult revenue (GST-free) | A$110.00 | A$52,133.40 |
| Card fee on the consult | -A$1.87 | -A$886.27 |
| Midwife wages (45 h, on-cost 1.366) | -A$25.32 | -A$12,000.38 |
| Midwife fixed costs | -A$2.99 | -A$1,418.83 |
| Consumables | -A$3.00 | -A$1,421.82 |
| Payroll tax caused by the midwives | -A$1.58 | -A$750.31 |
| **Midwife surplus** | **A$75.23** | **A$35,655.79** |

So the midwife side is not the problem. The problem is that only A$22.15 more of the package reaches GTT than the old A$250 (A$300 less A$27.85 lab = A$272.15), while the package now carries a midwife. To "level" the change itself you need **+A$4.26 a client**: **+A$4.34 on the consult or +A$4.79 on lounge + service** (target iii-b below).

### Every compliant lever, monthly effect (base A$17,314.31 before tax)

| Lever | What changes | Before tax | After tax | Tag |
|---|---|---|---|---|
| (a) Consult +A$10 (A$120) | GST-free, so GTT keeps A$9.83 a client | +A$4,658.83 | +A$3,494.12 | E |
| (a) Consult +A$20 (A$130) | | +A$9,317.66 | +A$6,988.25 | E |
| (b) Lounge + service +A$10 | GST takes 1/11 | +A$4,227.54 | +A$3,170.66 | E |
| (b) Lounge + service +A$20 | | +A$8,455.09 | +A$6,341.32 | E |
| (c) Priced extra: 30 to 45 minute massage upgrade, A$45 (repo prices A$120 vs A$75), per 10% of clients | Fits the costed 8 staff | +A$1,902.59 | +A$1,426.94 | E, take-up illustrative |
| (d) Package 2 share 10% / 30% / 50% | No extra AM wages (solver, 45-minute services) | +A$2,113.77 / +A$6,341.32 / +A$10,568.86 | +A$1,585.33 / +A$4,755.99 / +A$7,926.65 | E |
| (e) Midwife paid hours 45 to 42 / 39 / 36 | Consults need 36 h; 20 min already includes notes | +A$850.04 / +A$1,700.09 / +A$2,550.14 | +A$637.53 / +A$1,275.07 / +A$1,912.61 | E |
| (f) Afternoon | Repo PM is locked at 10 sessions weekday, 5 Saturday (Anthony, 2026-09-19); `pm_solver.py` still runs the superseded 12.81 figure | No lever without re-opening that decision | | R |

**(a) Correcting my R18 Q9.** R18 said raising the consult "does not help". **That was wrong.** I mixed up the mother's rebate (fixed at A$32.95) with GTT's revenue. Every A$1 added to the consult is A$1 more GTT revenue, GST-free, and A$0.983 more profit before tax (only the card fee comes off). It beats the lounge route by about A$0.09 per A$1 (A$862.57 a month on A$20). What limits it:

1. **The mother pays all of it.** Her rebate stays A$32.95, so out of pocket rises dollar for dollar.
2. **The market.** A 20-minute consult at A$130 is 3.4 times the A$38.75 schedule fee. No Perth price data was gathered this round (gap).
3. **GST apportionment.** In one checkout the split between the GST-free consult and the taxable lounge must have a reasonable basis ([ATO GSTR 2001/8](https://www.ato.gov.au/law/view/pdf/pbr/gstr2001-008da.pdf)). Raising the consult just to save GST invites ATO review. It is defensible only if Medical charges the same consult fee to every patient, package or not (ACC).
4. **The consult fee covers the consult only.** It cannot include lounge or service value (Services Australia, cited R18, V).
5. **Informed financial consent.** Tell the mother the fee and her expected out of pocket in writing before the consult ([RACS position paper](https://www.surgeons.org/about-racs/position-papers/informed-financial-consent-2019); the AMA 2024 position statement says the same). This is professional guidance, not a statute.

**(e) Hours:** with the consult 1 to 28 days before the test, the midwife no longer has to wait for draws, so a shorter day is possible. But 42 h means 86% of paid time is booked, and you approved 45. That is a question for you, not a recommendation.

**Not a lever, a cost:** the 10% post-test discount you adopted on 2026-10-17 is not in any profit figure (repo estimate -A$1,386.27 a month at 25% take-up, R).

---

## T3. Price needed to restore profit

Three targets, all after GST, card fees and payroll tax:

| Target | Means | Profit before company tax needed |
|---|---|---|
| (i) | The repo's A$35,186.40, comparably restated, **before** company tax | A$35,186.40 |
| (ii) | **A$35,186 AFTER company tax** (what you asked: net after tax and payroll tax) | A$46,915.20 |
| (iii) | Parity with the no-midwife A$21,971 (R16/R18 baseline) | A$21,971.46 |
| (iii-b) | Parity with the corrected no-midwife baseline (card fees in) | A$19,334.04 |

P2 always stays P1 + A$50. Out of pocket = price minus A$55.00 (lab fee inside). Gap = above A$245 / A$295.

| Target | Route | Consult | Lounge + service (P1) | P1 | P2 | Out of pocket P1 / P2 | Gap |
|---|---|---|---|---|---|---|---|
| (i) | A all on consult | A$148.36 | A$162.15 | A$338.36 | A$388.36 | A$283.36 / A$333.36 | +A$38.36 |
| (i) | B all on lounge + service | A$110.00 | A$204.42 | A$342.27 | A$392.27 | A$287.27 / A$337.27 | +A$42.27 |
| (i) | C 50/50 | A$130.11 | A$182.26 | A$340.22 | A$390.22 | A$285.22 / A$335.22 | +A$40.22 |
| **(ii)** | A | A$173.54 | A$162.15 | **A$363.54** | **A$413.54** | **A$308.54 / A$358.54** | **+A$63.54** |
| **(ii)** | B | A$110.00 | A$232.17 | A$370.02 | A$420.02 | A$315.02 / A$365.02 | +A$70.02 |
| **(ii)** | C | A$143.31 | A$195.46 | A$366.62 | A$416.62 | A$311.62 / A$361.62 | +A$66.62 |
| (iii) | A | A$120.00 | A$162.15 | A$310.00 | A$360.00 | A$255.00 / A$305.00 | +A$10.00 |
| (iii) | B | A$110.00 | A$173.16 | A$311.01 | A$361.01 | A$256.01 / A$306.01 | +A$11.01 |
| (iii) | C | A$115.24 | A$167.39 | A$310.48 | A$360.48 | A$255.48 / A$305.48 | +A$10.48 |
| (iii-b) | A / B / C | A$114.34 / A$110 / A$112.28 | | A$304.34 / A$304.79 / A$304.55 | +A$50 | about A$249.50 / A$299.50 | about +A$4.50 |

**Blunt:** target (ii) needs mothers to pay about A$309 to A$315 out of pocket on Package 1. That is A$64 to A$70 above the A$245 you say they accept. **On the 100% Package 1 plan, A$35k after tax is not reachable at acceptable prices.**

### Nearest compliant mixes (price + mix + hours)

| Mix | P1 / P2 | Out of pocket | Midwife h | Package 2 share | Before tax | After tax |
|---|---|---|---|---|---|---|
| **M1 (recommended)**: +A$20 lounge + service | A$320 / A$370 | A$265 / A$315 | 45 | 0% | **A$25,769.40** | **A$19,327.05** |
| M2: +A$20 on the consult | A$320 / A$370 | A$265 / A$315 | 45 | 0% | A$26,631.97 | A$19,973.98 |
| M3: M1 + 42 h | A$320 / A$370 | A$265 / A$315 | 42 | 0% | A$26,619.44 | A$19,964.58 |
| M5: M3 + 30% Package 2 | A$320 / A$370 | A$265 / A$315 | 42 | 30% | A$32,962.18 | A$24,721.64 |
| M6: consult +A$20, 39 h, 50% Package 2 | A$320 / A$370 | A$265 / A$315 | 39 | 50% | A$38,900.92 | A$29,175.69 |
| M7: consult +A$30, 42 h, 50% Package 2 | A$330 / A$380 | A$275 / A$325 | 42 | 50% | A$42,709.71 | A$32,032.28 |

Even M7, which bets on half the mothers buying Package 2, stays A$3,154 short of A$35,186 after tax.

### My one recommendation

**+A$20 on lounge + service (P1 A$320, P2 A$370). Keep your approved 45-hour midwife roster. Keep the 100% Package 1 plan. Sell Package 2 as the upgrade.**

- Profit: **A$25,769.40 before company tax, A$19,327.05 after** (up A$6,341.32 a month after tax).
- Mother: A$265 / A$315 out of pocket, A$20 above today.
- Why lounge + service, not the consult: no GST apportionment question, no change to Medical's fee. If the accountant confirms A$130 as Medical's standard fee for everyone, switch the A$20 to the consult: +A$862.57 a month.
- Upside not banked: each 10% of mothers on Package 2 adds A$2,113.77; trimming to 42 h adds A$850.04 if you agree.

---

## T4. The A$20 test, and a ladder to A$100

**Confirmed.** R18: A$17.84 kept per client = **A$8,455.09 a month** before company tax. R18's profit at A$320 was A$26,250.39. **Corrected for afternoon card fees it is A$25,769.40.** The A$8,455 gain itself is unchanged.

| Add | Out of pocket P1 / P2 | Lounge + service: kept per client | Month before tax | Profit before / after tax | Consult: kept per client | Month before tax | Profit before / after tax |
|---|---|---|---|---|---|---|---|
| A$10 | A$255 / A$305 | A$8.92 | +A$4,227.54 | A$21,541.85 / A$16,156.39 | A$9.83 | +A$4,658.83 | A$21,973.14 / A$16,479.85 |
| **A$20** | **A$265 / A$315** | **A$17.84** | **+A$8,455.09** | **A$25,769.40 / A$19,327.05** | **A$19.66** | **+A$9,317.66** | **A$26,631.97 / A$19,973.98** |
| A$30 | A$275 / A$325 | A$26.76 | +A$12,682.63 | A$29,996.94 / A$22,497.70 | A$29.49 | +A$13,976.49 | A$31,290.80 / A$23,468.10 |
| A$40 | A$285 / A$335 | A$35.68 | +A$16,910.18 | A$34,224.49 / A$25,668.37 | A$39.32 | +A$18,635.32 | A$35,949.63 / A$26,962.22 |
| A$50 | A$295 / A$345 | A$44.60 | +A$21,137.72 | A$38,452.03 / A$28,839.02 | A$49.15 | +A$23,294.15 | A$40,608.46 / A$30,456.35 |
| A$60 | A$305 / A$355 | A$53.52 | +A$25,365.27 | A$42,679.58 / A$32,009.69 | A$58.98 | +A$27,952.98 | A$45,267.29 / A$33,950.47 |
| A$70 | A$315 / A$365 | A$62.45 | +A$29,597.55 | A$46,911.86 / A$35,183.90 | A$68.81 | +A$32,611.81 | A$49,926.12 / A$37,444.59 |
| A$80 | A$325 / A$375 | A$71.37 | +A$33,825.10 | A$51,139.41 / A$38,354.56 | A$78.64 | +A$37,270.64 | A$54,584.95 / A$40,938.71 |
| A$90 | A$335 / A$385 | A$80.29 | +A$38,052.64 | A$55,366.95 / A$41,525.21 | A$88.47 | +A$41,929.47 | A$59,243.78 / A$44,432.83 |
| A$100 | A$345 / A$395 | A$89.21 | +A$42,280.19 | A$59,594.50 / A$44,695.88 | A$98.30 | +A$46,588.30 | A$63,902.61 / A$47,926.96 |

Rule of thumb: each A$1 on lounge + service = A$422.75 a month before tax. Each A$1 on the consult = A$465.88.

---

## T5. Center of Truth

Created: [docs/FINANCIAL-CENTER-OF-TRUTH.md](../../FINANCIAL-CENTER-OF-TRUTH.md) plus machine copy [center_of_truth.yml](center_of_truth.yml). Both are **written by theodore_r19.py**, so they regenerate together and cannot drift. They hold prices, rebates, fees, volumes, staffing and hours, rates, GST, tax, the monthly P&L, the per-client waterfall, R/V/E tags, items not in the P&L, the banned stale values list and a change log. Pointer lines were added to CURRENT-STATE.md (section 000) and DECISION-LOG.md (2026-10-26). No calculator number or master figure was changed.

Pre-send check for Idea Lobster: `python docs/overhaul-2026-10-19/L14-r19/theodore_r19.py --check <file.md>` (exit 1 if a banned value is found).

---

## T6. Why mistakes keep happening, and the fix

### Root causes (R16 to R19)

| # | Round | Error | Cause |
|---|---|---|---|
| 1 | R16, R17 | A$99.40 rebate (40-minute consult, item 82110) | **Assumed consult length** instead of asking or reading the lock |
| 2 | R16 | Mother's after-rebate cost compared with the old A$250 GTT price | **Different bases** (mother's money vs GTT's money) in one sentence |
| 3 | R16, R17 | A$222.15 and A$338 break-even carried forward | **Stale outputs reused** from R15 without re-running them |
| 4 | R16 | Room fee A$960 left out the 2 collection rooms | Partial input list |
| 5 | R17 | A$18,526: 48.6 h demand hours instead of your 45 h roster, two consult rooms, no 06:30, no leave cover | **Did not re-read locked facts** before running |
| 6 | R17 | 396 clients for the prepaid float (model is 474) | **Stale volume constant** from an older round |
| 7 | R17 | "Lounge + consult" wording | No terminology list |
| 8 | R18 | Q9: "raising the consult does not help" | **Mixed up rebate and revenue**; no "who receives each dollar" check |
| 9 | R18 | Card fees only on today's morning sales, not afternoon or baseline: headline A$481 too high, midwife effect shown as -A$4,176 instead of -A$2,020 | **Uneven bases** between the two sides of a comparison |
| 10 | R17, R18 | Grace 1.20 vs Theodore 1.366 on-cost, 26.33 days vs 4.333 weeks; A$35,186 (before tax) set beside A$13,346 (after tax) | **Two consultants, two bases, no shared source**; before-tax and after-tax figures shown side by side |

### Pre-generation checklist (stops each one)

1. Read `docs/FINANCIAL-CENTER-OF-TRUTH.md` first. Every input comes from it or from the script that writes it (1, 3, 5, 6, 10).
2. Run the script's input asserts (staff, volumes, hours, rooms) before writing any number (4, 5, 6).
3. For every figure, write who receives the dollar: mother, lab, Medicare, Medical, Lounge, ATO (2, 8).
4. Both sides of any comparison must carry the same cost lines (GST, card fees, payroll tax, structure cost) (9).
5. Label every profit "before" or "after company tax", and never put the two side by side (10).
6. Never assume a clinical fact (consult length, item number). If it is not locked, ask (1).
7. Run `theodore_r19.py --check` on the draft before it goes to Idea Lobster (all).

### Payroll basis: one choice

**Center of Truth uses 1.366 (Theodore), with Grace's 1.20 kept as a sensitivity.** The midwives are permanent part-time, so they get paid annual leave (4 weeks plus 17.5% loading), 10 days personal leave and public holidays. You locked a casual to cover that leave, so GTT pays twice for those weeks. 1.366 = (1 + 12% super + 1.35% leave loading + 1.7% workers comp) x 52 / 43.8 productive weeks. Grace's 1.20 has no paid-leave cover. It suits the repo's casual staff, whose 25% loading replaces leave, and your 2026-08-21 rule that normal rostering absorbs their absences. The month basis is 45 h x 52 / 12 weeks (Grace's 26.33 days x 7.5 h overstates by A$122.70). On 1.20 the profit would be A$18,889.75 before / A$14,167.31 after company tax (+A$1,575.44 before tax).

---

## Questions that genuinely need you

1. Do you approve +A$20 on lounge + service (P1 A$320, P2 A$370; mother A$265 / A$315 out of pocket)? Or (a) a smaller rise, (b) none?
2. Do you want the 45 paid midwife hours cut to 42 (7 paid hours a day), now the consult is on a separate day? This changes your approved roster (+A$850.04 a month).
3. Should the 10% post-test discount (repo estimate -A$1,386.27 a month) go into the headline profit, or stay a separate line?

## Honest gaps

1. No Perth market price for a 20-minute private midwife consult was found. That limits how far lever (a) can go.
2. Card fee is an estimate (1.7% + A$0.30). The repo lists Tyro 1.4% / Square 1.6%, provider not chosen.
3. Package 2 and extras take-up are illustrations, not demand data.
4. Midwife award class, the 30-minute unpaid break and casual relief rates are still E (unchanged from R14 to R18).
5. GSTR 2001/8: I cited the ruling but did not read its "reasonable basis" text this round.
6. Collection item 73928 vs 73938 is still with AskMBS. It changes the lab's price and the rebate by A$1.70, not GTT's revenue.

## Sources

- Repo (fresh clone 2026-10-26): docs/CURRENT-STATE.md (lines 30, sections 000 and 00), data/canonical/cost_ramp.yml (M5plus payroll breakdown), revenue_assumptions.yml (PM transactions), pricing.yml (A$117, A$75 / A$120 massage), opex.yml (opex_eftpos_transaction_fee "genuinely missing"), tools/master_financial_model.py, cost_ramp_model.py, demand_driven_staffing_solver.py (8 staff at N = 18, 45-minute services), check_consistency.py
- [THEODORE-R18.md](../L13-r18/THEODORE-R18.md), [ROSTER-R18.md](../L13-r18/ROSTER-R18.md), [THEODORE-R17.md](../L12-r17/THEODORE-R17.md), [GRACE-R17-ROSTER.md](../L12-r17/GRACE-R17-ROSTER.md)
- [ATO GSTR 2001/8 (draft addendum PDF)](https://www.ato.gov.au/law/view/pdf/pbr/gstr2001-008da.pdf)
- [RACS: Informed financial consent position paper](https://www.surgeons.org/about-racs/position-papers/informed-financial-consent-2019)
- MBS item figures and Services Australia fee rule: as cited in R18 (V)
