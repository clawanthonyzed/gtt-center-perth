# Staffing structure compare: who employs the collectors

General knowledge and repo figures, not personal documents. Verify before acting. Prepared 2026-10-20 by Theodore (CFO role). The financial model is a plan, not a forecast. Project name is an unregistered placeholder. Script: [theodore_staffing_compare.py](theodore_staffing_compare.py). Output: [theodore_staffing_compare_results.json](theodore_staffing_compare_results.json). All amounts Australian dollars, 18 clients a day, 473.94 clients a month.

## What changed in this note

- New: three-way comparison of (a) lab employs collectors for nothing, (b) lab employs and charges GTT a fee, (c) GTT employs and absorbs the lab fee, against (d) today's plan.
- Reconciled: Anthony's A$48,550 is the repo figure A$48,550.92. Two collectors at A$6,682.28 = A$13,364.56, which would give A$48,550.96; the repo saving is A$13,364.52, so the A$0.04 gap is rounding.
- Flagged: the repo quotes A$35,186.40 as profit with no GST line. Round 9 puts the after-GST figure at A$23,442.58. Both bases are shown; do not mix them.
- What the A$12,251.35 is: A$25.85 (test A$19.90 plus collection A$5.95) x 473.94 clients. It is the lab's Medicare schedule fee, not wages. Medicare would pay A$22.05 of it per client; the client gap is A$3.80.

## Table 1. The three structures and today's plan

| Option | Month, repo basis (no GST line) | Month, after GST | Year, after GST | Company tax 25% | Year after company tax |
|---|---|---|---|---|---|
| (d) Today's plan: GTT employs, Medicare pays | A$35,186.40 | A$23,442.58 | A$281,310.96 | A$70,327.74 | A$210,983.22 |
| (a) Lab employs collectors, no recharge | A$48,550.92 | A$36,807.10 | A$441,685.20 | A$110,421.30 | A$331,263.90 |
| (c) GTT employs, no Medicare, GTT absorbs lab fee | A$22,935.05 | A$12,304.99 | A$147,659.88 | A$36,914.97 | A$110,744.91 |

Difference (a) minus (c): A$25,615.87 a month on the repo basis, A$24,502.11 a month after GST, A$294,025.32 a year after GST (A$220,518.99 after 25% company tax). After GST, option (c) is A$12,304.99 because GTT claims back one eleventh of the lab fee, as the repo does (Case 3, A$12,304.99).

## Table 2. Option (b): lab employs collectors and charges GTT a management fee

Fee is shown before GST. Assumption: the lab's recharge is taxable (10% GST added) and GTT claims the credit, matching how the repo treats the lab fee. Last column is the worst case where GTT cannot claim.

| Fee as share of the A$13,364.52 wage cost | Fee before GST | Invoice with GST | Profit a month after GST | Against today's plan | Year after company tax | Month if no credit |
|---|---|---|---|---|---|---|
| 0% | A$0.00 | A$0.00 | A$36,807.10 | A$13,364.52 | A$331,263.90 | A$36,807.10 |
| 10% | A$1,336.45 | A$1,470.10 | A$35,470.65 | A$12,028.07 | A$319,235.85 | A$35,337.00 |
| 20% | A$2,672.90 | A$2,940.19 | A$34,134.20 | A$10,691.62 | A$307,207.80 | A$33,866.91 |
| 30% | A$4,009.36 | A$4,410.30 | A$32,797.74 | A$9,355.16 | A$295,179.66 | A$32,396.80 |
| 40% | A$5,345.81 | A$5,880.39 | A$31,461.29 | A$8,018.71 | A$283,151.61 | A$30,926.71 |
| 50% | A$6,682.26 | A$7,350.49 | A$30,124.84 | A$6,682.26 | A$271,123.56 | A$29,456.61 |
| 60% | A$8,018.71 | A$8,820.58 | A$28,788.39 | A$5,345.81 | A$259,095.51 | A$27,986.52 |
| 70% | A$9,355.16 | A$10,290.68 | A$27,451.94 | A$4,009.36 | A$247,067.46 | A$26,516.42 |
| 80% | A$10,691.62 | A$11,760.78 | A$26,115.48 | A$2,672.90 | A$235,039.32 | A$25,046.32 |
| 90% | A$12,028.07 | A$13,230.88 | A$24,779.03 | A$1,336.45 | A$223,011.27 | A$23,576.22 |
| 100% | A$13,364.52 | A$14,700.97 | A$23,442.58 | A$0.00 | A$210,983.22 | A$22,106.13 |

- Break-even against today's plan (A$23,442.58): fee A$13,364.52 before GST (A$14,700.97 invoiced). That is the full wage cost: any fee above the wages saved leaves GTT worse off than employing them itself. If GTT cannot claim the credit, break-even is an invoice of A$13,364.52.
- Equal to option (c) (A$12,304.99): fee A$24,502.11 before GST. That is above the wage cost, so a fee inside the sweep never makes (b) worse than (c).

## Table 3. Optional: lab pays GTT rent for the collection room (illustrative, valuer needed, NOT in repo)

Rent shown GST-inclusive; GTT remits one eleventh. Applied to option (a) and to option (b) with a fee of half the wage cost. Lounge rent from the lab: not in repo.

| Rent from lab a month | After GST to GTT | Option (a) profit a month | Option (b, half-wage fee) profit a month | Label |
|---|---|---|---|---|
| A$0.00 | A$0.00 | A$36,807.10 | A$30,124.84 | illustrative, valuer needed, NOT in repo |
| A$500.00 | A$454.55 | A$37,261.65 | A$30,579.39 | illustrative, valuer needed, NOT in repo |
| A$1,000.00 | A$909.09 | A$37,716.19 | A$31,033.93 | illustrative, valuer needed, NOT in repo |
| A$2,000.00 | A$1,818.18 | A$38,625.28 | A$31,943.02 | illustrative, valuer needed, NOT in repo |

## Compliance notes

- A recharge paid by GTT to the lab for staff is a commercial service charge. Set it at a documented market rate for the work done.
- Any money flowing from the lab to GTT must be market rent only, for space actually used, set by a valuer. It must not vary with doctor requests, bookings or client numbers. Catherine to confirm before any figure goes in a contract.
- Pregnant-client price: the repo has A$0 (lab bulk bills) or A$3.80 (lab bills the full fee). Both are paid to the lab, so GTT revenue is unchanged and no payback period applies. If GTT absorbed the fee (c), the price that restores today's profit is A$275.85, GST aside, per the repo.
- Nothing here is signed or quoted. Lab fees, recharge and rent are unknown until a lab answers in writing.
