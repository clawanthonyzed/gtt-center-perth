# Unit economics: GTT Center Perth -- AM GTT package only (one revenue stream of two; see report notes for the full business)

Every number below comes from the input file. Nothing is looked up or guessed.

## One AM GTT package visit

| line | per AM GTT package visit |
| --- | ---: |
| Price | $250.00 |
| GTT supplies (glucose, tubes) | -$2.27 |
| **Contribution** (what each AM GTT package visit leaves to pay the fixed costs) | **$247.73** (99%) |

## The margin that matters

Fixed costs: $88,625 a month (Total payroll + non-wage overhead (whole-business, conservative baseline, profit-loss-tables.md v2.0) $88,625).

- **Break-even: 12 AM GTT package visits a day.** Below that you lose money every month.
- **Profit margin at your plan** (7 a day): **-70%** of every sale, after every cost.
- Capacity: 8 a day.

## Year 1, month by month

| month | AM GTT package visits a day | revenue | profit | cumulative (after $0 startup) |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 4 | $30,000 | -$58,897 | -$58,897 |
| 2 | 5 | $37,500 | -$51,466 | -$110,363 |
| 3 | 5 | $37,500 | -$51,466 | -$161,829 |
| 4 | 6 | $45,000 | -$44,034 | -$205,862 |
| 5 | 6 | $45,000 | -$44,034 | -$249,896 |
| 6 | 6 | $45,000 | -$44,034 | -$293,930 |
| 7 | 7 | $52,500 | -$36,602 | -$330,532 |
| 8 | 7 | $52,500 | -$36,602 | -$367,133 |
| 9 | 7 | $52,500 | -$36,602 | -$403,735 |
| 10 | 7 | $52,500 | -$36,602 | -$440,337 |
| 11 | 7 | $52,500 | -$36,602 | -$476,939 |
| 12 | 7 | $52,500 | -$36,602 | -$513,540 |

- **Year 1 operating profit: -$513,540** on $555,000 of revenue.
- After the $0 startup spend: -$513,540.
- Startup money earned back: not within year 1.
- Cash you need before it pays for itself: **$513,540**.

## What if

| scenario | margin at plan | break-even a day | year 1 profit |
| --- | ---: | ---: | ---: |
| Base plan | -70% | 12 | -$513,540 |
| Price -10% | -89% | 14 | -$569,040 |
| Volume -20% | -112% | 12 | -$623,533 |
| Unit costs +15% | -70% | 12 | -$514,296 |

## Red flags

- Break-even needs 12 AM GTT package visits a day but capacity is 8.
- Year 1 loses money on operations (-$513,540).
- The startup spend is not earned back within year 1.

---

## IMPORTANT CAVEAT — read before using this report

This tool models ONE product (price, one variable cost) against ONE fixed-cost pool. GTT Center Perth's real business has **two revenue streams sharing the same fixed costs**: AM GTT packages (~$250/visit) and PM standalone services (~$95/visit), plus ancillary retail/cafe spend. The run above puts the WHOLE business's $88,625/month fixed costs onto the AM-GTT stream alone and ignores PM revenue completely — so its break-even (12/day) and Year-1 loss (-$513,540) are NOT the real picture. They understate the business.

**The real, current, authoritative monthly figures** (source: gtt-center-perth/docs/profit-loss-tables.md v2.0, the conservative baseline model, confirmed current as of this report):

| Metric | Amount |
| --- | ---: |
| Total Revenue | $113,712.16 |
| Total Costs (payroll + non-wage overhead) | $88,625.09 |
| **Net P&L** | **+$25,087.07/month profit** |

GTT Center Perth is modelled as **already profitable** at this conservative baseline — not loss-making. The 108 visits/month break-even figure Anthony cited in this brain dump does not match any figure in the venture's current documentation and should be treated as stale; the current model runs on ~220 AM GTT visits/month + ~350 PM standalone visits/month (570 total) plus ancillary revenue, not a single blended visit count.

No two-stream-capable version of this tool exists yet. Treat the single-stream run above as an illustrative sensitivity check on the AM-GTT package alone, not as GTT's real break-even.
