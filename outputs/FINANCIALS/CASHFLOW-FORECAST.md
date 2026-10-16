# Cashflow Forecast and Startup Capital

| | |
|---|---|
| **Business** | GTT Center Perth |
| **Document** | Startup capital and 12-month cashflow forecast |
| **Prepared by** | Theodore (CFO) for Anthony Zed. Updated 2026-10-16 (Grace, to Anthony's instructions of 2026-10-16) |
| **Date** | 2026-10-16 |
| **Status** | DRAFT for review |
| **Legal entity** | TO CONFIRM |
| **Currency** | Australian dollars (A$) |
| **Basis** | 3-Way Financial Model v0.5 (2026-10-16), 25-minute cadence, adaptive rostering, full capacity from Month 1 (no ramp-up), headline rent A$8,000 per month |

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

Figures in A$. Negative = cash out. There is no ramp-up: every month is a full-capacity month (18 clients a morning), so receipts and operating payments are the same in every month.

| A$ | Opening cash | Funding in | Receipts | Operating payments | Pre-opening capex | Deferred capex | GST paid (BAS) | Net cash flow | **Closing cash** | Cumulative (after GST) | Cumulative (repo basis) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| M0 | 0.00 | 336,198.00 | 0.00 | 0.00 | -251,198.00 | 0.00 | 0.00 | 85,000.00 | **85,000.00** ◄ LOW | -251,198.00 ◄ PEAK FUNDING | -251,198.00 |
| M1 | 85,000.00 | 0.00 | 143,070.37 | -107,883.97 | 0.00 | 0.00 | 0.00 | 35,186.40 | **120,186.40** | -216,011.60 | -216,011.60 |
| M2 | 120,186.40 | 0.00 | 143,070.37 | -107,883.97 | 0.00 | 0.00 | -11,743.82 | 23,442.58 | **143,628.98** | -192,569.02 | -180,825.20 |
| M3 | 143,628.98 | 0.00 | 143,070.37 | -107,883.97 | 0.00 | 0.00 | -11,743.82 | 23,442.58 | **167,071.56** | -169,126.44 | -145,638.80 |
| M4 | 167,071.56 | 0.00 | 143,070.37 | -107,883.97 | 0.00 | -5,600.00 | -11,743.82 | 17,842.58 | **184,914.14** | -151,283.86 | -116,052.40 |
| M5 | 184,914.14 | 0.00 | 143,070.37 | -107,883.97 | 0.00 | 0.00 | -11,743.82 | 23,442.58 | **208,356.72** | -127,841.28 | -80,866.00 |
| M6 | 208,356.72 | 0.00 | 143,070.37 | -107,883.97 | 0.00 | -7,774.00 | -11,743.82 | 15,668.58 | **224,025.30** | -112,172.70 | -53,453.60 |
| M7 | 224,025.30 | 0.00 | 143,070.37 | -107,883.97 | 0.00 | 0.00 | -11,743.82 | 23,442.58 | **247,467.88** | -88,730.12 | -18,267.20 |
| M8 | 247,467.88 | 0.00 | 143,070.37 | -107,883.97 | 0.00 | 0.00 | -11,743.82 | 23,442.58 | **270,910.46** | -65,287.54 | 16,919.20 ◄ PAYBACK (repo basis) |
| M9 | 270,910.46 | 0.00 | 143,070.37 | -107,883.97 | 0.00 | 0.00 | -11,743.82 | 23,442.58 | **294,353.04** | -41,844.96 | 52,105.60 |
| M10 | 294,353.04 | 0.00 | 143,070.37 | -107,883.97 | 0.00 | 0.00 | -11,743.82 | 23,442.58 | **317,795.62** | -18,402.38 | 87,292.00 |
| M11 | 317,795.62 | 0.00 | 143,070.37 | -107,883.97 | 0.00 | 0.00 | -11,743.82 | 23,442.58 | **341,238.20** | 5,040.20 ◄ PAYBACK (after GST) | 122,478.40 |
| M12 | 341,238.20 | 0.00 | 143,070.37 | -107,883.97 | 0.00 | 0.00 | -11,743.82 | 23,442.58 | **364,680.78** | 28,482.78 | 157,664.80 |
| **M1 to M12 total** | | **0.00** | **1,716,844.44** | **-1,294,607.64** | **0.00** | **-13,374.00** | **-129,182.02** | **279,680.78** | | | |

**How to read the table**
- Opening cash, funding, pre-opening capex, deferred capex, GST paid and closing cash follow the 3-Way Financial Model v0.5 §4. The model's own rules are unchanged: all funding in before opening, no debt, clients prepay at booking (no debtor or creditor timing), GST paid monthly in the month after.
- Receipts are model §3 total revenue and payments are model §3 total costs. Receipts less payments equals the model's operating cash in every month.
- **Cumulative (after GST)** = closing cash less A$336,198 capital in. **Cumulative (repo basis)** excludes GST paid.

### 2a. Key cash measures

| Measure | Figure | Source |
|---|---:|---|
| **Peak funding requirement (with GST timing)** | **A$251,198.00** | Model §4a. Equal to the pre-opening capital, because with no ramp-up there is no operating loss to fund |
| Lowest cash point | A$85,000.00, **at opening (Month 0)** | Model §4. The A$85,000 working-capital reserve is never drawn |
| How it is reached | A$251,198 pre-opening capital; Month 1 makes a profit | Model §4a |
| **Payback, repo basis** | **Month 8** (cumulative +A$16,919.20) | Model §7 |
| **Payback, after GST** | **Month 11** (cumulative +A$5,040.20) | Model §7 |

The earlier ramped forecast showed peak funding of A$267,771.03 (the Month 1 loss on top of the pre-opening capital) and payback in Month 11 (repo basis) and Month 15 (after GST). Removing the ramp-up removes the Month 1 to 4 losses, so peak funding falls to the pre-opening capital and payback comes about 3 to 4 months sooner. Both rest on the waitlist delivering a full morning from the first day.

---

## 3. Working capital buffer

| Measure | Figure | Source |
|---|---:|---|
| Working capital reserve at opening | A$85,000.00 | Model §2b |
| Deepest drop after opening | A$0.00 (cash rises from Month 1) | Model §4a |
| **Cash remaining above the low point (headroom)** | **A$85,000.00** | Model §4a |
| Runway if fill falls to 70% (12.6 clients a morning) from Month 1 | 9 full months (net after GST -A$8,871.51 a month; cash goes negative in Month 10) | Model §4b |

What the buffer is for (model §4a, §8):
- The uncosted fit-out for the larger 257 to 290 sqm floor area, indicatively up to A$63,750.
- Cafe equipment (A$5,000 to A$12,650), not in the base.
- Rent during the fit-out period, not in the base.
- Unspent contingency (up to A$26,914) and GST credits on fit-out would add headroom. Not counted.

At the A$10,500 gross ceiling peak funding is A$256,198.00 and the lowest cash point is A$85,000.00 (opening); the reserve is still not drawn (model §9).

---

## 4. Funding

Funding source per the repo: **self-funded from founder savings, about A$200,000 (funding and ownership structure TO CONFIRM). No external investor sought to date** (repo executive-summary.md and GTT-CENTER-PERTH-VENTURE-OVERVIEW.md; this figure is not in CURRENT-STATE.md).

| Measure | Requirement | Less savings (about) | **Gap** |
|---|---:|---:|---:|
| Pre-opening capital only | A$251,198 | A$200,000 | **A$51,198** |
| **Peak funding requirement** | **A$251,198** | A$200,000 | **A$51,198** |
| Total startup capital incl. A$85,000 reserve | A$336,198 | A$200,000 | **A$136,198** |

The gaps are simple subtractions of the two sourced figures. How the gap is to be funded (loan, lease finance, investor) is **not in model**: the model assumes all capital is put in before opening with no debt (model §4, §8 item 25). Interest and repayments are therefore not in model.

---

## 5. Notes

1. **No debt assumed.** All A$336,198 is received before opening. No loan drawdowns, interest or repayments are modelled.
2. **Pre-opening capital** (A$251,198, including the full contingency) is spent in Month 0. This is conservative.
3. **GST.** Monthly BAS, paid the month after (model §4). All sales are treated as taxable. GST treatment is general information only and must be confirmed with the accountant. The repo's own P&L carries no GST line, so the repo-basis payback is Month 8 and the after-GST payback is Month 11.
4. **Receipts timing.** Clients prepay at booking. No debtor or creditor timing is modelled.
5. **No ramp-up, fill rate is the central risk.** Fill is assumed 100% from Month 1. At 85% fill, peak funding stays A$251,198 but payback is Month 16 (repo basis) and Month 35 (after GST). At 70% fill the business does not pay back and the A$85,000 reserve is used up in about 9 months (model §13).
6. **Lab fee** is assumed A$0 to GTT (repo assumption). Tender fees are TO CONFIRM.
7. **Rent** is the A$8,000 headline per Anthony's instruction. Rent during fit-out is not in the base.
8. **Not in model:** income tax, depreciation, interest, loan funding, cafe equipment, fit-out for the larger floor area.

*Arithmetic check: every cash row was rolled forward by script from opening cash. The same roll-forward rules reproduced the earlier ramped forecast exactly (peak funding A$267,771.03, paybacks Month 11 and Month 15) before the ramp was removed.*
