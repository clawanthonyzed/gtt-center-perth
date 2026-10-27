> SUPERSEDED where it disagrees with docs/GTT-READ-FIRST.md (Round 25 integrity banner, 2026-10-27). Read that file first.

# Theodore R21, Part 2: the business in single segments

Date: 2026-10-26. Source: [theodore_r21.py](theodore_r21.py), results in [theodore_r21_results.json](theodore_r21_results.json). Repo figures only, locked Round 20 case (473.94 clients a month, Package 1, ex GST). Excluded as you decided: interest, Package 2 take-up, standalone consults, card quotes, discounts. Tags: R repo, E estimate. Every cost line below is a line already in the accepted model.

## 1. The answer in three lines

1. The consult segment and the afternoon segment each make a profit on their own. The morning lounge segment on its own does not.
2. The whole morning package (consult + lounge) does make a profit without the afternoon: A$22,663.54 a month after its fair share of shared costs.
3. The consult carries the lounge. Your rule "each single form profitable" holds for consult, afternoon and the morning package as a whole, but not for the lounge cut out by itself.

## 2. Segments, a month (A$)

| Line | (a) Consult | (b) Lounge, morning | (c) Lab | (d) Afternoon | (e) Shared |
|---|---|---|---|---|---|
| Revenue ex GST | 61,612.20 | 69,863.50 | 0.00 | 22,350.34 | 0.00 |
| Midwife wages (E) | -12,000.38 | | | | |
| Midwife fixed costs, consumables (E) | -2,840.65 | | | | |
| Treatment staff and phlebotomists, with super and workers comp (R) | | -71,145.86 | | | |
| Afternoon staff, with super and workers comp (R) | | | | -14,445.29 | |
| Card fees (E) | -1,111.40 | -1,386.26 | | -480.99 | |
| **Direct costs** | -15,952.43 | -72,532.12 | 0.00 | -14,926.28 | |
| **Profit before shared costs** | **45,659.77** | **-2,668.62** | **0.00** | **7,424.06** | |
| Shared costs, allocated | -9,525.94 | -10,801.68 | 0.00 | -3,455.61 | 23,783.23 in total |
| **Profit before company tax** | **36,133.83** | **-13,470.30** | **0.00** | **3,968.45** | |
| Stands alone? | Yes | **No** | Not applicable | Yes | |

## 3. Shared costs and the allocation rule

| Shared cost | A$ a month | Tag |
|---|---|---|
| Venue manager 07:00 start, with super and workers comp | 8,004.48 | R |
| Venue manager extra half hour (06:30 start) | 500.28 | R rate |
| Rent, insurance, overheads, supplies, after GST credits (13,025.76 = 14,288.34 less 1,262.58) | 13,025.76 | R |
| WA payroll tax, whole group | 1,344.04 | E |
| Three-company running cost | 908.67 | E |
| **Total** | **23,783.23** | |

Rule: split by each segment's share of revenue ex GST. Shares: consult 40.05%, lounge 45.42%, afternoon 14.53%. Reason: the repo has no floor-area or hours-of-use split, so revenue share is the simplest rule that invents nothing. A different rule moves profit between segments but never changes the total. Card fees are split between consult and lounge by the share of the A$292.15 charge (A$130.00 and A$162.15).

The lab carries no profit or loss: the client pays the lab A$27.85 directly (A$13,199.23 a month at 473.94 clients). It never touches GTT's books, so it adds nothing to revenue or cost.

## 4. Adding it back to the accepted figure

| Step | A$ a month |
|---|---|
| Consult | 36,133.83 |
| Lounge, morning | -13,470.30 |
| Lab | 0.00 |
| Afternoon | 3,968.45 |
| **Sum of segments (profit before company tax)** | **26,631.98** |
| Accepted headline | 26,631.97 |
| Difference | A$0.01, rounding only |
| Company tax 25% | -6,657.99 |
| **Net after company tax** | **19,973.98** |

## 5. Does the morning package alone make a profit?

| Test | A$ a month | Per client |
|---|---|---|
| Consult + lounge, before shared costs | 42,991.15 | 90.71 |
| Less their revenue share of shared costs (20,327.62) | 22,663.54 | 47.82 |
| Worst case: morning carries ALL shared costs (23,783.23) | 19,207.92 | 40.53 |

Yes, with or without the afternoon the morning package makes a profit. The afternoon adds A$7,424.06 before shared costs (A$3,968.45 after its share). The lounge is the weak piece: it loses A$5.63 a client before shared costs, and the consult makes A$96.34 a client before shared costs, so the consult carries it. This is partly a labelling effect. The client pays A$292.15 for the pair, and splitting it as A$130.00 consult plus A$162.15 lounge is your price choice. Look at the pair, not the pieces.

## 6. Per-client table (morning only, no afternoon line)

| Per client, A$ | Revenue ex GST | Direct costs | Before shared | Shared share | After shared |
|---|---|---|---|---|---|
| Consult segment | 130.00 | 33.66 | 96.34 | 20.10 | **76.24** |
| Lounge segment | 147.41 | 153.04 | -5.63 | 22.79 | **-28.42** |
| Both (the morning package) | 277.41 | 186.70 | 90.71 | 42.89 | **47.82** |

Before company tax. The 47.82 is lower than the A$56.19 in the Center of Truth because that figure also includes the afternoon sales per morning client. Per client direct costs: consult 33.66 = midwife 31.31 + card 2.35; lounge 153.04 = staff 150.11 + card 2.93.

## 7. What this means for decisions

1. Do not cut the consult price to win clients: it is the segment that pays for the lounge staff.
2. Sell the lounge alone only at a higher price. Section 3 of Part 3 shows what the outside-referral price does.
3. The model's number does not change; only its labels do.

## QUESTIONS FOR ANTHONY

1. Which shared cost rule do you want shown to Grace and the accountant? (a) revenue share, recommended, simplest; (b) the morning package carries all shared costs, the cautious view (A$19,207.92); (c) another rule you give me.
2. Do you want the lounge reported as a loss-making piece inside a profitable package, or only the combined morning package? (a) combined, recommended; (b) both.

Regards.
