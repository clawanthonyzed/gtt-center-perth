# Cashflow Forecast and Startup Capital

| | |
|---|---|
| **Business** | GTT Center Perth |
| **Document** | Startup capital and 12-month cashflow forecast |
| **Prepared by** | Theodore (CFO) for Anthony Zed |
| **Date** | 2026-10-12 |
| **Status** | DRAFT for review |
| **Legal entity** | TO CONFIRM |
| **Currency** | Australian dollars (A$) |
| **Basis** | 3-Way Financial Model v0.4 (2026-10-11), demand-responsive rostering, headline rent A$8,000 per month |

All figures are planning estimates. The venue is not yet open and no trading data exists.

---

## 1. Startup capital

### 1a. By group (Low / Base / High)

The base is the founder-approved "Revised Recommended Opening Strategy" (2026-08-10).

| Group | Low | **Base** | High |
|---|---:|---:|---:|
| Equipment, non-clinical | A$12,950 | **A$12,950** | A$34,980 |
| Clinical / blood collection equipment | A$6,330 | **A$6,330** | A$10,240 |
| Furniture, fixtures, fittings, signage | A$14,160 | **A$14,160** | A$51,800 |
| Fit-out / construction | A$138,328 | **A$139,678** | A$306,029 |
| IT / booking setup | A$820 | **A$820** | A$7,550 |
| Compliance, legal, design, approvals | A$7,639 | **A$7,639** | A$28,239 |
| Bond and lease | A$16,000 | **A$16,000** | A$41,500 |
| Pre-opening staff, launch marketing, opening stock | A$21,552 | **A$26,707** | A$57,022 |
| Contingency | A$26,133 | **A$26,914** | A$107,472 |
| **Pre-opening capital (to open)** | **A$243,912** | **A$251,198** | **A$644,832** |
| Working capital reserve | A$85,000 | **A$85,000** | A$110,000 |
| **Total startup capital** | **A$328,912** | **A$336,198** | **A$754,832** |

Source: model §2a, §2b (repo startup_costs.yml, STARTUP-COST-OPTIMISATION.md, MVP-OPENING-DECISION-REVIEW.md). Low is the "Minimum Viable Opening"; High is the "Full Build" with 20% contingency.

**Base = A$251,198 to open + A$85,000 working capital reserve = A$336,198.**

Base detail (model §2b): fit-out includes acoustic curtain fabric (+A$1,350); pre-opening staff A$22,872; launch marketing A$1,250; opening stock A$2,585. Line-by-line items are itemised in the repo only for the full-scope scenarios (model §2c).

### 1b. Range across repo scenarios

| Scenario | Total startup capital | Source |
|---|---:|---|
| Low (Minimum Viable Opening) | A$328,912 | Model §2b |
| **Base, A$8,000 rent (headline)** | **A$336,198** | Model §2b |
| Base, rent A$9,500 | A$339,198 | Model §9 |
| Base, rent A$10,500 or A$10,500 gross ceiling | A$341,198 | Model §9 |
| High (Full Build) | A$754,832 | Model §2b |

The rent cases change only the lease bond and one month's advance rent.

### 1c. Spend deferred to after opening (not in base)

| Item | Amount | Month paid |
|---|---:|---|
| Nail stations 3 and 4 | A$3,000 | Month 4 |
| Hair chairs 3 and 4 | A$2,600 | Month 4 |
| Acoustic treatment for curtain bays | A$4,874 | Month 6 |
| Full website build | A$1,200 | Month 6 |
| Professional photography | A$1,000 | Month 6 |
| 3rd iPad + colour printer | A$700 | Month 6 |
| **Total deferred** | **A$13,374** | M4 A$5,600; M6 A$7,774 |

Source: model §2d.

---

## 2. Month 0 to 12 cash forecast

Figures in A$. Negative = cash out.

| A$ | Opening cash | Funding in | Receipts | Operating payments | Pre-opening capex | Deferred capex | GST paid (BAS) | Net cash flow | **Closing cash** | Cumulative (after GST) | Cumulative (repo basis) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| M0 | 0.00 | 336,198.00 | 0.00 | 0.00 | -251,198.00 | 0.00 | 0.00 | 85,000.00 | **85,000.00** | -251,198.00 | -251,198.00 |
| M1 | 85,000.00 | 0.00 | 61,520.26 | -78,093.29 | 0.00 | 0.00 | 0.00 | -16,573.03 | **68,426.97** ◄ LOW | **-267,771.03** ◄ PEAK FUNDING | -267,771.03 |
| M2 | 68,426.97 | 0.00 | 91,565.04 | -83,782.53 | 0.00 | 0.00 | -4,411.99 | 3,370.52 | **71,797.49** | -264,400.51 | -259,988.52 |
| M3 | 71,797.49 | 0.00 | 113,025.59 | -93,733.11 | 0.00 | 0.00 | -7,125.15 | 12,167.33 | **83,964.82** | -252,233.18 | -240,696.04 |
| M4 | 83,964.82 | 0.00 | 133,055.44 | -103,033.67 | 0.00 | -5,600.00 | -9,057.93 | 15,363.84 | **99,328.66** | -236,869.34 | -216,274.27 |
| M5 | 99,328.66 | 0.00 | 143,070.37 | -107,883.97 | 0.00 | 0.00 | -10,860.65 | 24,325.75 | **123,654.41** | -212,543.59 | -181,087.87 |
| M6 | 123,654.41 | 0.00 | 143,070.37 | -107,883.97 | 0.00 | -7,774.00 | -11,743.82 | 15,668.58 | **139,322.99** | -196,875.01 | -153,675.47 |
| M7 | 139,322.99 | 0.00 | 143,070.37 | -107,883.97 | 0.00 | 0.00 | -11,743.82 | 23,442.58 | **162,765.57** | -173,432.43 | -118,489.07 |
| M8 | 162,765.57 | 0.00 | 143,070.37 | -107,883.97 | 0.00 | 0.00 | -11,743.82 | 23,442.58 | **186,208.15** | -149,989.85 | -83,302.67 |
| M9 | 186,208.15 | 0.00 | 143,070.37 | -107,883.97 | 0.00 | 0.00 | -11,743.82 | 23,442.58 | **209,650.73** | -126,547.27 | -48,116.27 |
| M10 | 209,650.73 | 0.00 | 143,070.37 | -107,883.97 | 0.00 | 0.00 | -11,743.82 | 23,442.58 | **233,093.31** | -103,104.69 | -12,929.87 |
| M11 | 233,093.31 | 0.00 | 143,070.37 | -107,883.97 | 0.00 | 0.00 | -11,743.82 | 23,442.58 | **256,535.89** | -79,662.11 | **22,256.53** ◄ PAYBACK (repo basis) |
| M12 | 256,535.89 | 0.00 | 143,070.37 | -107,883.97 | 0.00 | 0.00 | -11,743.82 | 23,442.58 | **279,978.47** | -56,219.53 | 57,442.93 |
| **M1 to M12 total** | | **0.00** | **1,543,729.29** | **-1,221,714.36** | **0.00** | **-13,374.00** | **-113,662.46** | **194,978.47** | | | |

**How to read the table**
- Opening cash, funding, pre-opening capex, deferred capex, GST paid and closing cash are as published in model v0.4 §4.
- **Receipts and operating payments are derived from v0.4 §3 + §4**: v0.4 §4 publishes only the net operating cash, so receipts are §3 total revenue and payments are §3 total costs. This follows the model's own rule of no debtor or creditor timing (clients prepay at booking). Receipts less payments equals the §4 operating cash in every month.
- **Cumulative (after GST)** = closing cash less A$336,198 capital in. **Cumulative (repo basis)** excludes GST paid. Both match model §7 in every month it publishes (M0, M1, M3, M6, M9, M10, M11). **M2, M4, M5, M7, M8 and M12 cumulative figures are derived from v0.4 §3 + §4.**

### 2a. Key cash measures

| Measure | Figure | Source |
|---|---:|---|
| **Peak funding requirement (with GST timing)** | **A$267,771.03** | Model §4a. LOCKED by Anthony 2026-10-11 |
| Lowest cash point | A$68,426.97, **Month 1** | Model §4 |
| How it is reached | A$251,198 pre-opening capital + A$16,573.03 Month 1 loss | Model §4a |
| **Payback, repo basis** | **Month 11** (cumulative +A$22,256.53) | Model §7 |
| **Payback, after GST** | **Month 15** (cumulative +A$14,108.21) | Model §7 |

Payback after GST falls outside this 12-month table. Model §7 publishes the continuation, assuming steady state carries on:

| Month | Cumulative (repo basis) | Cumulative (after GST) |
|---|---:|---:|
| M13 | A$92,629.33 | -A$32,776.95 |
| M14 | A$127,815.73 | -A$9,334.37 |
| **M15** | A$163,002.13 | **A$14,108.21** ◄ PAYBACK (after GST) |

---

## 3. Working capital buffer

| Measure | Figure | Source |
|---|---:|---|
| Working capital reserve at opening | A$85,000.00 | Model §2b |
| Deepest drop after opening (Month 1 loss) | A$16,573.03 | Model §4a |
| **Cash remaining above the low point (headroom)** | **A$68,426.97** | Model §4a |
| Runway if bookings stall at Month 1 volume | 4 full months (burn A$20,985.02 per month after the first BAS) | Model §4b |

What the buffer is for (model §4a, §8):
- The uncosted fit-out for the larger 257 to 290 sqm floor area, indicatively up to A$63,750. This alone could use most of the headroom.
- Cafe equipment (A$5,000 to A$12,650), not in the base.
- Rent during the fit-out period, not in the base.
- Unspent contingency (up to A$26,914) and GST credits on fit-out would add headroom. Not counted.

At the A$10,500 gross ceiling the lowest cash point is A$67,176.97 (Month 1) and peak funding is A$274,021.03 (model §9).

---

## 4. Funding

Funding source per the repo: **self-funded from founder savings, about A$200,000 (funding and ownership structure TO CONFIRM). No external investor sought to date** (repo executive-summary.md and GTT-CENTER-PERTH-VENTURE-OVERVIEW.md; this figure is not in CURRENT-STATE.md).

| Measure | Requirement | Less savings (about) | **Gap** |
|---|---:|---:|---:|
| Pre-opening capital only | A$251,198 | A$200,000 | **A$51,198** |
| **Peak funding requirement** | **A$267,771** | A$200,000 | **A$67,771** |
| Total startup capital incl. A$85,000 reserve | A$336,198 | A$200,000 | **A$136,198** |

The gaps are simple subtractions of the two sourced figures. How the gap is to be funded (loan, lease finance, investor) is **not in model**: the model assumes all capital is put in before opening with no debt (model §4, §8 item 25). Interest and repayments are therefore not in model.

---

## 5. Notes

1. **No debt assumed.** All A$336,198 is received before opening. No loan drawdowns, interest or repayments are modelled.
2. **Pre-opening capital** (A$251,198, including the full contingency) is spent in Month 0. This is conservative.
3. **GST.** Monthly BAS, paid the month after (model §4). All sales are treated as taxable. GST treatment is general information only and must be confirmed with the accountant. The repo's own P&L carries no GST line, so the repo-basis payback is Month 11 and the after-GST payback is Month 15.
4. **Receipts timing.** Clients prepay at booking. No debtor or creditor timing is modelled.
5. **Fill rate** is assumed 100%. At 85% fill, peak funding is A$271,742.13 and payback is Month 19 / Month 42 (model §13).
6. **Lab fee** is assumed A$0 to GTT (repo assumption). Tender fees are TO CONFIRM.
7. **Rent** is the A$8,000 headline per Anthony's instruction. Rent during fit-out is not in the base.
8. **Not in model:** income tax, depreciation, interest, loan funding, cafe equipment, fit-out for the larger floor area.

*Arithmetic check: every cash row was rolled forward by script from opening cash and agrees to the cent with model v0.4 §4 closing cash and §7 cumulative figures. Column totals were re-summed.*
