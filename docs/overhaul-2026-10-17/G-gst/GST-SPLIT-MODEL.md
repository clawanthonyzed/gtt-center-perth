# GST SPLIT MODEL: what the A$250 package is worth at every split (B2a, B2b)

This is general knowledge, not your personal documents. Verify with a qualified adviser before acting. Prepared 2026-10-17 by Grace as Theodore (CFO), workstream G. Arithmetic overlay only: it takes the project's own steady-state outputs and applies the GST rule (GST = 1/11 of the GST-inclusive price). It does not replace the project's calculators. Spreadsheet version: [GST-SPLIT-MODEL.csv](https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/overhaul-2026-10-17/G-gst/GST-SPLIT-MODEL.csv). Script: [split_arithmetic.py](https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/overhaul-2026-10-17/G-gst/split_arithmetic.py). Statute position: [STATUTE-ANALYSIS.md](https://github.com/clawanthonyzed/gtt-center-perth/blob/main/docs/overhaul-2026-10-17/G-gst/STATUTE-ANALYSIS.md).

## 1. Read this first: what is legally available and what is arithmetic

| Column | Meaning | Status on the statute text |
|---|---|---|
| (b) If Component A does not qualify | Whole package taxable at 10%. Equals the project's GST-stress case (A$23,442.58 a month at A$250) | AVAILABLE. This is the law for GTT's own charges today (s 38-7 and s 38-10 read; see STATUTE-ANALYSIS.md) |
| (a) If Component A qualifies GST-free | Shows how much is at stake at each split if GTT genuinely supplied a GST-free Component A | HYPOTHETICAL. Needs a GTT supply that satisfies s 38-7 or s 38-10 (for example a nurse-delivered nursing service, or a lab-run service). GTT makes none today. Never invoice on this column without a ruling |

Why no split is legally available today: the A$250 package buys two wellness treatments and lounge access. The pathology test is billed by the lab to Medicare (A$25.85 per visit at schedule fees: item 66548 A$19.90 plus collection A$5.95, from the Medicare findings). When Medicare bulk-bills it the client pays GTT nothing for pathology, so Component A in GTT's hands is A$0 and the correct split is 0 / 100. The 50/50, 60/40 and 70/30 rows are shown so Anthony can see the size of the prize, not because they are supported.

## 2. Inputs (all from the project's own models)

| Input | Value | Source |
|---|---|---|
| AM clients a month | 473.94 (18 a morning x 26.33 trading days) | MODEL-WORKINGS.md |
| Net operating profit at A$250, GST-inclusive, no GST line | A$35,186.40 a month (A$422,236.80 a year, no ramp-up) | 3-way model; MODEL-WORKINGS.md |
| PM revenue (taxable, outside the split) | A$24,585.37 a month; GST A$2,235.04 | 3-way model section 3d |
| Input tax credits on costs | A$1,262.58 a month (rent, consumables and other overhead; wages carry none) | 3-way model section 3d. The model counts credits on running costs only; fit-out and equipment credits are listed as upside (item 27) |
| Price change | Operating profit moves A$4,739.40 a month per A$10 of price at constant demand (elasticity not modelled) | 3-way model fee basis |
| Check | A$250 fully taxable: 35,186.40 - 13,006.40 + 1,262.58 = A$23,442.58 a month; x 12 = A$281,310.96 | Matches the GST-stress case exactly |
| Value evidence | Lab visit A$25.85 (A$19.90 + A$5.95); GTT collector labour A$28.20 per client (A$13,364.50 a month at the project wage rates plus 13.7% on-costs, 473.94 clients) plus consumables A$2.53 = A$30.73; treatment labour A$121.92 per client | L-medicare/PRIMARY-SOURCES.md; cost_ramp_model.py rates |

Method. GST on the taxable part = 1/11 of its GST-inclusive price (GSTR 2001/8 para 114). Net revenue = total GST-inclusive revenue less GST. Net profit = operating profit less (GST on sales less input tax credits). Steady-state cashflow a month equals net profit after GST. The project's cash rule is that BAS is paid the month after, so Year 1 cash keeps one month of GST (12 months of profit less 11 BAS payments, before capital spending). Year 1 = 12 x steady state, no ramp-up. GST-free supplies keep their input tax credits (GST Act s 38-1: "an entitlement to an input tax credit for anything acquired or imported to make the supply is not affected"). Rounding may differ by a few cents.

## 3. The value-based splits

- Component B (lounge, refreshments, amenities and, in GTT's real package, the two wellness treatments) is always taxable. Its GST is shown in the second table of each block.
- "Market anchor": Component A priced at what the lab is paid under Medicare for the visit (A$25.85) or for the collection episode alone (A$5.95). That value is the lab's, billed to Medicare, so it cannot be GTT's GST-free revenue. GSTR 2001/8 para 98 points to what each part would sell for alone, which is why it is shown.
- "Cost share": Component A at its share of direct delivery cost (A$30.73 of A$152.65 = 20.13%). GSTR 2001/8 para 112 warns that cost alone is not reasonable when mark-ups differ between the parts, so treat it as a ceiling, not a basis.

## 4. Ratio tables (A$250 first, then the A$200 and A$300 variants)

### Price A$250: per month and per year

| Split (A / B) | Status | A per client | B per client | (a) GST if A qualifies | (a) Net profit / month | (a) Net profit Year 1 | (a) Year 1 cash after BAS | (b) GST if A does not qualify | (b) Net profit / month | (b) Net profit Year 1 | (b) Year 1 cash after BAS | Upside (a) vs (b) / month | Upside / year |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0/100 (nothing to A) (0.00% to A) | AVAILABLE | A$0.00 | A$250.00 | A$11,743.82 | A$23,442.58 | A$281,310.96 | A$293,054.78 | A$11,743.82 | A$23,442.58 | A$281,310.96 | A$293,054.78 | A$0.00 | A$0.00 |
| 50/50 (50.00% to A) | HYPOTHETICAL | A$125.00 | A$125.00 | A$6,358.14 | A$28,828.26 | A$345,939.12 | A$352,297.26 | A$11,743.82 | A$23,442.58 | A$281,310.96 | A$293,054.78 | A$5,385.68 | A$64,628.16 |
| 60/40 (60.00% to A) | HYPOTHETICAL | A$150.00 | A$100.00 | A$5,281.01 | A$29,905.39 | A$358,864.68 | A$364,145.69 | A$11,743.82 | A$23,442.58 | A$281,310.96 | A$293,054.78 | A$6,462.81 | A$77,553.72 |
| 70/30 (70.00% to A) | HYPOTHETICAL | A$175.00 | A$75.00 | A$4,203.87 | A$30,982.53 | A$371,790.36 | A$375,994.23 | A$11,743.82 | A$23,442.58 | A$281,310.96 | A$293,054.78 | A$7,539.95 | A$90,479.40 |
| 100/0 (all to A) (100.00% to A) | HYPOTHETICAL ONLY | A$250.00 | A$0.00 | A$972.46 | A$34,213.94 | A$410,567.28 | A$411,539.74 | A$11,743.82 | A$23,442.58 | A$281,310.96 | A$293,054.78 | A$10,771.36 | A$129,256.32 |
| Value split, market anchor (whole MBS lab visit A$25.85) (10.34% to A) | ARITHMETIC OF THE LAB'S SERVICE | A$25.85 | A$224.15 | A$10,630.06 | A$24,556.34 | A$294,676.08 | A$305,306.14 | A$11,743.82 | A$23,442.58 | A$281,310.96 | A$293,054.78 | A$1,113.76 | A$13,365.12 |
| Value split, market anchor (MBS collection episode only A$5.95) (2.38% to A) | ARITHMETIC OF THE LAB'S SERVICE | A$5.95 | A$244.05 | A$11,487.47 | A$23,698.93 | A$284,387.16 | A$295,874.63 | A$11,743.82 | A$23,442.58 | A$281,310.96 | A$293,054.78 | A$256.35 | A$3,076.20 |
| Value split, cost share (collection cost vs treatment cost) (20.13% to A) | HYPOTHETICAL | A$50.33 | A$199.67 | A$9,575.36 | A$25,611.04 | A$307,332.48 | A$316,907.84 | A$11,743.82 | A$23,442.58 | A$281,310.96 | A$293,054.78 | A$2,168.46 | A$26,021.52 |

GST split by component, A$250 package (a = Component A qualifies):

| Split | (a) GST on A | GST on B (AM) | GST on PM | Input tax credits | (a) Net GST payable / month | (a) Net revenue ex GST / month | (b) GST on A | (b) Net GST payable / month | (b) Net revenue ex GST / month |
|---|---|---|---|---|---|---|---|---|---|
| 0/100 (nothing to A) | A$0.00 | A$10,771.36 | A$2,235.04 | A$1,262.58 | A$11,743.82 | A$130,063.97 | A$0.00 | A$11,743.82 | A$130,063.97 |
| 50/50 | A$0.00 | A$5,385.68 | A$2,235.04 | A$1,262.58 | A$6,358.14 | A$135,449.65 | A$5,385.68 | A$11,743.82 | A$130,063.97 |
| 60/40 | A$0.00 | A$4,308.55 | A$2,235.04 | A$1,262.58 | A$5,281.01 | A$136,526.78 | A$6,462.82 | A$11,743.82 | A$130,063.97 |
| 70/30 | A$0.00 | A$3,231.41 | A$2,235.04 | A$1,262.58 | A$4,203.87 | A$137,603.92 | A$7,539.95 | A$11,743.82 | A$130,063.97 |
| 100/0 (all to A) | A$0.00 | A$0.00 | A$2,235.04 | A$1,262.58 | A$972.46 | A$140,835.33 | A$10,771.36 | A$11,743.82 | A$130,063.97 |
| Value split, market anchor (whole MBS lab visit A$25.85) | A$0.00 | A$9,657.60 | A$2,235.04 | A$1,262.58 | A$10,630.06 | A$131,177.73 | A$1,113.76 | A$11,743.82 | A$130,063.97 |
| Value split, market anchor (MBS collection episode only A$5.95) | A$0.00 | A$10,515.01 | A$2,235.04 | A$1,262.58 | A$11,487.47 | A$130,320.32 | A$256.36 | A$11,743.82 | A$130,063.97 |
| Value split, cost share (collection cost vs treatment cost) | A$0.00 | A$8,602.90 | A$2,235.04 | A$1,262.58 | A$9,575.36 | A$132,232.43 | A$2,168.47 | A$11,743.82 | A$130,063.97 |

### Price A$200: per month and per year

| Split (A / B) | Status | A per client | B per client | (a) GST if A qualifies | (a) Net profit / month | (a) Net profit Year 1 | (a) Year 1 cash after BAS | (b) GST if A does not qualify | (b) Net profit / month | (b) Net profit Year 1 | (b) Year 1 cash after BAS | Upside (a) vs (b) / month | Upside / year |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0/100 (nothing to A) (0.00% to A) | AVAILABLE | A$0.00 | A$200.00 | A$9,589.55 | A$1,899.85 | A$22,798.20 | A$32,387.75 | A$9,589.55 | A$1,899.85 | A$22,798.20 | A$32,387.75 | A$0.00 | A$0.00 |
| 50/50 (50.00% to A) | HYPOTHETICAL | A$100.00 | A$100.00 | A$5,281.01 | A$6,208.39 | A$74,500.68 | A$79,781.69 | A$9,589.55 | A$1,899.85 | A$22,798.20 | A$32,387.75 | A$4,308.54 | A$51,702.48 |
| 60/40 (60.00% to A) | HYPOTHETICAL | A$120.00 | A$80.00 | A$4,419.30 | A$7,070.10 | A$84,841.20 | A$89,260.50 | A$9,589.55 | A$1,899.85 | A$22,798.20 | A$32,387.75 | A$5,170.25 | A$62,043.00 |
| 70/30 (70.00% to A) | HYPOTHETICAL | A$140.00 | A$60.00 | A$3,557.59 | A$7,931.81 | A$95,181.72 | A$98,739.31 | A$9,589.55 | A$1,899.85 | A$22,798.20 | A$32,387.75 | A$6,031.96 | A$72,383.52 |
| 100/0 (all to A) (100.00% to A) | HYPOTHETICAL ONLY | A$200.00 | A$0.00 | A$972.46 | A$10,516.94 | A$126,203.28 | A$127,175.74 | A$9,589.55 | A$1,899.85 | A$22,798.20 | A$32,387.75 | A$8,617.09 | A$103,405.08 |
| Value split, market anchor (whole MBS lab visit A$25.85) (12.93% to A) | ARITHMETIC OF THE LAB'S SERVICE | A$25.85 | A$174.15 | A$8,475.79 | A$3,013.61 | A$36,163.32 | A$44,639.11 | A$9,589.55 | A$1,899.85 | A$22,798.20 | A$32,387.75 | A$1,113.76 | A$13,365.12 |
| Value split, market anchor (MBS collection episode only A$5.95) (2.98% to A) | ARITHMETIC OF THE LAB'S SERVICE | A$5.95 | A$194.05 | A$9,333.19 | A$2,156.21 | A$25,874.52 | A$35,207.71 | A$9,589.55 | A$1,899.85 | A$22,798.20 | A$32,387.75 | A$256.36 | A$3,076.32 |
| Value split, cost share (collection cost vs treatment cost) (20.13% to A) | HYPOTHETICAL | A$40.26 | A$159.74 | A$7,854.78 | A$3,634.62 | A$43,615.44 | A$51,470.22 | A$9,589.55 | A$1,899.85 | A$22,798.20 | A$32,387.75 | A$1,734.77 | A$20,817.24 |

GST split by component, A$200 package (a = Component A qualifies):

| Split | (a) GST on A | GST on B (AM) | GST on PM | Input tax credits | (a) Net GST payable / month | (a) Net revenue ex GST / month | (b) GST on A | (b) Net GST payable / month | (b) Net revenue ex GST / month |
|---|---|---|---|---|---|---|---|---|---|
| 0/100 (nothing to A) | A$0.00 | A$8,617.09 | A$2,235.04 | A$1,262.58 | A$9,589.55 | A$108,521.24 | A$0.00 | A$9,589.55 | A$108,521.24 |
| 50/50 | A$0.00 | A$4,308.55 | A$2,235.04 | A$1,262.58 | A$5,281.01 | A$112,829.78 | A$4,308.55 | A$9,589.55 | A$108,521.24 |
| 60/40 | A$0.00 | A$3,446.84 | A$2,235.04 | A$1,262.58 | A$4,419.30 | A$113,691.49 | A$5,170.25 | A$9,589.55 | A$108,521.24 |
| 70/30 | A$0.00 | A$2,585.13 | A$2,235.04 | A$1,262.58 | A$3,557.59 | A$114,553.20 | A$6,031.96 | A$9,589.55 | A$108,521.24 |
| 100/0 (all to A) | A$0.00 | A$0.00 | A$2,235.04 | A$1,262.58 | A$972.46 | A$117,138.33 | A$8,617.09 | A$9,589.55 | A$108,521.24 |
| Value split, market anchor (whole MBS lab visit A$25.85) | A$0.00 | A$7,503.33 | A$2,235.04 | A$1,262.58 | A$8,475.79 | A$109,635.00 | A$1,113.76 | A$9,589.55 | A$108,521.24 |
| Value split, market anchor (MBS collection episode only A$5.95) | A$0.00 | A$8,360.73 | A$2,235.04 | A$1,262.58 | A$9,333.19 | A$108,777.60 | A$256.36 | A$9,589.55 | A$108,521.24 |
| Value split, cost share (collection cost vs treatment cost) | A$0.00 | A$6,882.32 | A$2,235.04 | A$1,262.58 | A$7,854.78 | A$110,256.01 | A$1,734.77 | A$9,589.55 | A$108,521.24 |

### Price A$300: per month and per year

| Split (A / B) | Status | A per client | B per client | (a) GST if A qualifies | (a) Net profit / month | (a) Net profit Year 1 | (a) Year 1 cash after BAS | (b) GST if A does not qualify | (b) Net profit / month | (b) Net profit Year 1 | (b) Year 1 cash after BAS | Upside (a) vs (b) / month | Upside / year |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0/100 (nothing to A) (0.00% to A) | AVAILABLE | A$0.00 | A$300.00 | A$13,898.10 | A$44,985.30 | A$539,823.60 | A$553,721.70 | A$13,898.10 | A$44,985.30 | A$539,823.60 | A$553,721.70 | A$0.00 | A$0.00 |
| 50/50 (50.00% to A) | HYPOTHETICAL | A$150.00 | A$150.00 | A$7,435.28 | A$51,448.12 | A$617,377.44 | A$624,812.72 | A$13,898.10 | A$44,985.30 | A$539,823.60 | A$553,721.70 | A$6,462.82 | A$77,553.84 |
| 60/40 (60.00% to A) | HYPOTHETICAL | A$180.00 | A$120.00 | A$6,142.71 | A$52,740.69 | A$632,888.28 | A$639,030.99 | A$13,898.10 | A$44,985.30 | A$539,823.60 | A$553,721.70 | A$7,755.39 | A$93,064.68 |
| 70/30 (70.00% to A) | HYPOTHETICAL | A$210.00 | A$90.00 | A$4,850.15 | A$54,033.25 | A$648,399.00 | A$653,249.15 | A$13,898.10 | A$44,985.30 | A$539,823.60 | A$553,721.70 | A$9,047.95 | A$108,575.40 |
| 100/0 (all to A) (100.00% to A) | HYPOTHETICAL ONLY | A$300.00 | A$0.00 | A$972.46 | A$57,910.94 | A$694,931.28 | A$695,903.74 | A$13,898.10 | A$44,985.30 | A$539,823.60 | A$553,721.70 | A$12,925.64 | A$155,107.68 |
| Value split, market anchor (whole MBS lab visit A$25.85) (8.62% to A) | ARITHMETIC OF THE LAB'S SERVICE | A$25.85 | A$274.15 | A$12,784.34 | A$46,099.06 | A$553,188.72 | A$565,973.06 | A$13,898.10 | A$44,985.30 | A$539,823.60 | A$553,721.70 | A$1,113.76 | A$13,365.12 |
| Value split, market anchor (MBS collection episode only A$5.95) (1.98% to A) | ARITHMETIC OF THE LAB'S SERVICE | A$5.95 | A$294.05 | A$13,641.74 | A$45,241.66 | A$542,899.92 | A$556,541.66 | A$13,898.10 | A$44,985.30 | A$539,823.60 | A$553,721.70 | A$256.36 | A$3,076.32 |
| Value split, cost share (collection cost vs treatment cost) (20.13% to A) | HYPOTHETICAL | A$60.40 | A$239.60 | A$11,295.94 | A$47,587.46 | A$571,049.52 | A$582,345.46 | A$13,898.10 | A$44,985.30 | A$539,823.60 | A$553,721.70 | A$2,602.16 | A$31,225.92 |

GST split by component, A$300 package (a = Component A qualifies):

| Split | (a) GST on A | GST on B (AM) | GST on PM | Input tax credits | (a) Net GST payable / month | (a) Net revenue ex GST / month | (b) GST on A | (b) Net GST payable / month | (b) Net revenue ex GST / month |
|---|---|---|---|---|---|---|---|---|---|
| 0/100 (nothing to A) | A$0.00 | A$12,925.64 | A$2,235.04 | A$1,262.58 | A$13,898.10 | A$151,606.69 | A$0.00 | A$13,898.10 | A$151,606.69 |
| 50/50 | A$0.00 | A$6,462.82 | A$2,235.04 | A$1,262.58 | A$7,435.28 | A$158,069.51 | A$6,462.82 | A$13,898.10 | A$151,606.69 |
| 60/40 | A$0.00 | A$5,170.25 | A$2,235.04 | A$1,262.58 | A$6,142.71 | A$159,362.08 | A$7,755.38 | A$13,898.10 | A$151,606.69 |
| 70/30 | A$0.00 | A$3,877.69 | A$2,235.04 | A$1,262.58 | A$4,850.15 | A$160,654.64 | A$9,047.95 | A$13,898.10 | A$151,606.69 |
| 100/0 (all to A) | A$0.00 | A$0.00 | A$2,235.04 | A$1,262.58 | A$972.46 | A$164,532.33 | A$12,925.64 | A$13,898.10 | A$151,606.69 |
| Value split, market anchor (whole MBS lab visit A$25.85) | A$0.00 | A$11,811.88 | A$2,235.04 | A$1,262.58 | A$12,784.34 | A$152,720.45 | A$1,113.76 | A$13,898.10 | A$151,606.69 |
| Value split, market anchor (MBS collection episode only A$5.95) | A$0.00 | A$12,669.28 | A$2,235.04 | A$1,262.58 | A$13,641.74 | A$151,863.05 | A$256.36 | A$13,898.10 | A$151,606.69 |
| Value split, cost share (collection cost vs treatment cost) | A$0.00 | A$10,323.48 | A$2,235.04 | A$1,262.58 | A$11,295.94 | A$154,208.85 | A$2,602.16 | A$13,898.10 | A$151,606.69 |

## 5. What the tables say

1. Fully taxable (the only legally available column today): A$23,442.58 a month and A$281,310.96 in Year 1 at A$250 (A$293,054.78 cash after BAS timing). That is A$11,743.82 a month of net GST to the ATO.
2. Every percentage point of the A$250 package that is genuinely GST-free is worth A$107.71 a month (A$1,292.56 a year). The ceiling, 100% of the AM package, is A$10,771.36 a month (A$129,256.32 a year).
3. At the splits Anthony named, the stake is A$5,385.68 (50/50), A$6,462.81 (60/40) and A$7,539.95 (70/30) a month, or A$64,628 to A$90,479 a year. None is supported today (STATUTE-ANALYSIS.md section 5, S8).
4. The splits that the available evidence can support are small. If GTT genuinely supplied the collection and it qualified, the market anchors give A$1,113.76 a month (A$25.85 a visit) or A$256.35 a month (A$5.95 collection only). The cost share gives A$2,168.46, which is a ceiling because para 112 distrusts cost-only splits.
5. Price matters more than split. At A$200 the fully taxable profit is A$1,899.85 a month; at A$300 it is A$44,985.30 a month after GST (A$539,823.60 in Year 1; demand held constant, so treat as an upper bound). A A$50 price move is worth about A$23,697 a month before GST, far more than any defensible split.
6. 100/0 is shown only as the limit. It would mean the lounge and wellness treatments were priced at nil. GSTR 2001/8 para 81ZD treats that kind of allocation as a contrivance, and para 81ZI (the doctor who charged only for the GST-free drug) is the ATO's own example.

## 6. Input tax credit sensitivity (A$250)

| Credits a month | Meaning | Fully taxable net profit | 70/30 if A qualifies |
|---|---|---|---|
| A$0.00 | No credits claimed | A$22,180.00 | A$29,719.96 |
| A$1,262.58 | Project model (running costs) | A$23,442.58 | A$30,982.54 |
| A$1,298.94 | Upper bound: 1/11 of all non-wage costs (A$14,288.34) | A$23,478.94 | A$31,018.90 |

Credits do not change with the split, because GST-free supplies keep their credits. Fit-out and equipment credits (one-off, not modelled) would come on top of these numbers. Whether GTT is registered, and in which entity, is for the accountant.

## 7. Medicare not bulk-billing (cross-check with the Medicare findings)

If Medicare does not bulk-bill and GTT absorbed the lab fee of A$25.85, profit falls from A$35,186.40 to A$22,935.05 a month (Medicare findings, A1). That cost sits on top of the GST effect above and does not change the split analysis: the lab's fee is the lab's price, not part of GTT's invoice.

## 8. Not modelled

Price demand elasticity; fit-out credits; the cost of employing a registered nurse or allied-health professional (wages not in repo); any lab fee for collection space or staff (no quote yet, ITC-11); income tax; the entity (E workstream).
