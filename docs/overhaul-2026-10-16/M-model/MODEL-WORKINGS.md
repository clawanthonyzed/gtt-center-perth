# M workstream: model and operations workings (2026-10-16)

Calculators run (not replaced): `tools/am_volume_tier_staffing_solver.py` (line-by-line peak overlap, draw overlap), `tools/cost_ramp_model.py` (wages, shifts, Saturday 1.5x, super 12%, workers comp 1.7%, PM labour, Venue Manager), `tools/am_demand_tier_financial_ladder.py` (PM revenue, overhead). The drivers `m_model_driver.py`, `m_part2.py`, `m_part3.py` in this folder only change the input (which of the nine 25-minute slots the booked clients sit in) and add the cash roll-forward. Controls that pass: 18 clients reproduces A$107,883.97 total cost and +A$35,186.40; 2 + 4 roster reproduces A$78,993.29; the roll-forward reproduces the earlier ramped model exactly (peak funding A$267,771.03, payback M11 / M15, Year 1 A$322,014.93).

## 1. Why 2 phlebotomists, and what is open

Evidence: (a) the 3-way model and AM-STAFFING-RAMP-OPTIMISATION call 2 "structural" because "a single-chair mode has never been solved", a modelling gap; (b) `docs/gtt-clinical-protocol.md` uses a second on-site phlebotomist for a difficult blood draw; (c) the 2026-10-11 decision recorded "2 phlebotomists on every GTT morning" as GTT's clinical standard. No regulation requiring 2 exists anywhere in the repo. On the 25-minute cadence the three draws of each client fall 0, 10 and 20 minutes into the 25-minute cycle, so one chair never overlaps itself (solver draw check = 1 for up to 9 clients one per slot). **Treated as a clinical standard: kept as the minimum, flagged to Anthony.** Option shown beside it. Ask the pathology partner whether it requires 2 collectors (TO CONFIRM).

## 2. Roster, cost and contribution by booked clients (25-minute cadence, planning case)

Planning case: bookings fill from 07:00, one client per slot first (Chair A), a second client (Chair B) only after all nine slots have one. Labour includes super 12% and workers comp 1.7%, 6-hour shifts, 22 weekdays + 4.33 Saturdays at the same volume. Net operating profit = AM contribution + PM revenue A$24,585.37 - fixed costs A$36,738.11. Phlebotomists: 2 (minimum). Best / worst = fewest / most therapists over all 19,683 ways of placing the clients in the slots.

| Booked | Therapists MB/N/H | Staff | Last first draw | Labour per weekday morning | Revenue per morning | Contribution weekday | Contribution Saturday | AM labour per month | AM contribution per month | Net operating profit per month | Best / worst therapists |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1/1/0 = 2 | 4 | 07:00 | A$975.96 | A$250 | -A$725.96 | -A$1,213.93 | A$27,809.86 | -A$21,227.36 | -A$33,380.10 | 2 / 2 |
| 2 | 2/2/0 = 4 | 6 | 07:25 | A$1,482.90 | A$500 | -A$982.90 | -A$1,724.35 | A$42,255.18 | -A$29,090.18 | -A$41,242.92 | 2 / 4 |
| 3 | 2/2/0 = 4 | 6 | 07:50 | A$1,482.90 | A$750 | -A$732.90 | -A$1,474.35 | A$42,255.18 | -A$22,507.68 | -A$34,660.42 | 2 / 6 |
| 4 | 2/2/0 = 4 | 6 | 08:15 | A$1,482.90 | A$1,000 | -A$482.90 | -A$1,224.35 | A$42,255.18 | -A$15,925.18 | -A$28,077.92 | 2 / 8 |
| 5 | 2/2/0 = 4 | 6 | 08:40 | A$1,482.90 | A$1,250 | -A$232.90 | -A$974.35 | A$42,255.18 | -A$9,342.68 | -A$21,495.42 | 2 / 8 |
| 6 | 2/2/0 = 4 | 6 | 09:05 | A$1,482.90 | A$1,500 | A$17.10 | -A$724.35 | A$42,255.18 | -A$2,760.18 | -A$14,912.92 | 4 / 8 |
| 7 | 2/2/0 = 4 | 6 | 09:30 | A$1,482.90 | A$1,750 | A$267.10 | -A$474.35 | A$42,255.18 | A$3,822.32 | -A$8,330.42 | 4 / 8 |
| 8 | 2/2/0 = 4 | 6 | 09:55 | A$1,482.90 | A$2,000 | A$517.10 | -A$224.35 | A$42,255.18 | A$10,404.82 | -A$1,747.92 | 4 / 8 |
| 9 | 2/2/0 = 4 | 6 | 10:20 | A$1,482.90 | A$2,250 | A$767.10 | A$25.65 | A$42,255.18 | A$16,987.32 | A$4,834.58 | 4 / 8 |
| 10 | 3/2/1 = 6 | 8 | 10:20 | A$1,989.84 | A$2,500 | A$510.16 | -A$484.76 | A$56,700.52 | A$9,124.48 | -A$3,028.26 | 4 / 8 |
| 11 | 4/2/2 = 8 | 10 | 10:20 | A$2,496.78 | A$2,750 | A$253.22 | -A$995.18 | A$71,145.86 | A$1,261.64 | -A$10,891.10 | 6 / 8 |
| 12 | 4/2/2 = 8 | 10 | 10:20 | A$2,496.78 | A$3,000 | A$503.22 | -A$745.18 | A$71,145.86 | A$7,844.14 | -A$4,308.60 | 6 / 8 |
| 13 | 4/2/2 = 8 | 10 | 10:20 | A$2,496.78 | A$3,250 | A$753.22 | -A$495.18 | A$71,145.86 | A$14,426.64 | A$2,273.90 | 6 / 8 |
| 14 | 4/2/2 = 8 | 10 | 10:20 | A$2,496.78 | A$3,500 | A$1,003.22 | -A$245.18 | A$71,145.86 | A$21,009.14 | A$8,856.40 | 6 / 8 |
| 15 | 4/2/2 = 8 | 10 | 10:20 | A$2,496.78 | A$3,750 | A$1,253.22 | A$4.82 | A$71,145.86 | A$27,591.64 | A$15,438.90 | 8 / 8 |
| 16 | 4/2/2 = 8 | 10 | 10:20 | A$2,496.78 | A$4,000 | A$1,503.22 | A$254.82 | A$71,145.86 | A$34,174.14 | A$22,021.40 | 8 / 8 |
| 17 | 4/2/2 = 8 | 10 | 10:20 | A$2,496.78 | A$4,250 | A$1,753.22 | A$504.82 | A$71,145.86 | A$40,756.64 | A$28,603.90 | 8 / 8 |
| 18 | 4/2/2 = 8 | 10 | 10:20 | A$2,496.78 | A$4,500 | A$2,003.22 | A$754.82 | A$71,145.86 | A$47,339.14 | A$35,186.40 | 8 / 8 |

One-phlebotomist option (mornings 1 to 9 only; 10 and above need both chairs): weekday labour falls by A$234.51, monthly by A$6,682.23. For example 9 clients: labour A$1,248.39 a weekday morning, net operating profit +A$11,516.81 a month.

## 3. S10b answer

At about 12.6 booked clients (12 or 13 on a real morning) the roster is 2 phlebotomists and 8 therapists in the planning case, 6 therapists if the second-chair bookings sit in alternate slots. Therapists = the number of 45-minute services overlapping at the busiest moment. Pairs 25 minutes apart overlap with their neighbours: one client per slot keeps it to two first services and two second services (4 therapists, 2 to 9 clients); neighbouring double-booked slots (from 10 to 11 clients) put four first services in the room (4 + 2 + 2 = 8). Eight is a consequence of overlap, never a standard.

## 4. Break-even working (task 3)

| Step | Working | Result |
|---|---|---|
| Fixed costs | rent 8,000 + other overhead 5,088.34 + cost of goods 1,200 + (PM labour 12,704.74 + Venue Manager 7,040) x 1.137 | A$36,738.11 |
| AM roster, 2 + 4 | wages x 1.137, 22 weekdays + 4.33 Saturdays | + A$42,255.18 |
| Total costs | | A$78,993.29 |
| Less PM revenue | | - A$24,585.37 |
| Must be covered by AM | | A$54,407.92 |
| Revenue per daily client per month | A$250 x 26.33 | A$6,582.50 |
| **Break-even** | 54,407.92 / 6,582.50 | **8.266** |

New number equals the old figure: the old 8.266 was the cost of a 2 + 4 roster; the 25-minute cadence needs that same roster for up to 9 clients one per slot. It changes with booking pattern: spaced 8.266; planning 8.266; stacked in pairs 12.655 (cost A$107,883.97); planning with 1 phlebotomist 7.250 (cost A$72,311.06). GST-stress: 9.255 (spaced), 14.083 (planning or stacked), 8.138 (1 phlebotomist). Margin of safety at 18: 9.734 clients (54.1%).

## 5. Year 1 with no ramp, P20a, S12c, P19b

Ramp removed (all months = steady state; marketing A$1,500 from Month 1). Year 1: revenue A$1,716,844.44, costs A$1,294,607.64, net A$422,236.80; GST-stress A$281,310.96 (12 x 23,442.58). Peak funding A$251,198 (pre-opening capital; Month 1 is profitable, lowest cash A$85,000 at opening); payback Month 8 (repo) / Month 11 (after GST).

Old baseline A$322,014.93 = Month 1 to 4 at 43 / 64 / 79 / 93% of capacity (-16,573.03; 7,782.51; 19,292.48; 30,021.77) + 8 x 35,186.40. Old GST-stress A$196,608.65 was the same year after GST (the A$250 price taken as including 10% GST). New figures replace both: +A$100,221.87 and +A$84,702.31, the profit the ramp assumption was giving away. Steady state confirmed: +A$35,186.40 x 12 = A$422,236.80 (S12c); margin 35,186.40 / 143,070.37 = 24.59%, about 24.6% (P19b).

**Anthony's "$196k-$234k" claim:** not supported by the repo. A$196,609 is the old ramped Year 1 GST-stress figure; no GST-stress figure of about A$234k exists (A$234,241 in the model is an unrelated fit-out subtotal). Repo GST-stress Year 1 across rent cases was A$169,336 to A$196,609 (ramped). On the new no-ramp basis the range is A$254,038 (rent A$10,500) to A$281,311 (rent A$8,000); gross ceiling A$267,675, A$9,500 A$264,947. Monthly GST-stress is A$21,170 to A$23,443.

Fill sensitivity (no ramp makes fill the central risk): 85% = +A$17,413.65 a month, Year 1 A$208,963.80, payback Month 16 / 35; 70% = -A$359.10 a month, no payback, reserve gone in Month 10.

## 6. GST treatment and value per point (L5, task 5)

Base case (repo basis): GST-inclusive P&L with no GST line, so in effect no GST leaks and no credits are claimed. GST-stress: whole package and PM taxable at 10% (GST on sales A$13,006.40, credits A$1,262.58, net after GST A$23,442.58). Proposed two-tier (not adopted): clinical component GST-free, wellness taxable. Each 1 percentage point (A$2.50) of the A$250 package GST-free = 473.94 clients a month x 2.50 / 11 = **A$107.71 a month (A$1,292.56 a year)**; each A$1 = A$43.09 a month; 100% of the AM package = A$10,771.36 a month. PM GST (A$2,235.04) is outside the split. Whether any part is GST-free under s38-10 is for the accountant / ATO ruling (R workstream); not claimed here.

## 7. Saturday proof (P18a)

At 18 clients (Table 1 Saturday volume): revenue 18 x A$250 = A$4,500.00. Wages at 1.5x: Massage+Beauty 4 x 56.25 x 6 = 1,350.00; Nails 2 x 55.215 x 6 = 662.58; Hair 662.58; phlebotomists 2 x 51.5625 x 6 = 618.75; total 3,293.91; super 12% 395.27; workers comp 1.7% 56.00; **labour A$3,745.18**. **Contribution +A$754.82 a Saturday (16.8%)**, about A$3,268 over 4.33 Saturdays. The Venue Manager does not work Saturdays, rent and overheads are fixed, so this is incremental profit. At the whole-venue break-even of 8.266 clients: revenue 2,066.50 against labour 2,224.35 (2 + 4 roster), -A$157.85. Saturday direct-labour break-even: 8.90 clients with the 2 + 4 roster (so 9 clients: +A$25.65) and 14.98 clients with the 2 + 8 roster (15 clients: +A$4.82). Penalty rate carve-out (risk register item 7) unconfirmed, so this is conservative.

## 8. Headcount on the books (P17a, P17d)

Peak simultaneous need: 8 therapists (4 Massage+Beauty, 2 Nails, 2 Hair) and 2 phlebotomists. Pool sized to the repo reliability target (each person unavailable on about 8% of shifts; 95% of days fully staffed; phlebotomists 98%+), `docs/architecture/STAFFING-COVERAGE-VALIDATION.md`: Massage+Beauty 6 (99.15%), Nails 3 (98.18%), Hair 3 (98.18%), phlebotomists 4 (99.81%; 3 is the lower bound at 98.18%). PM: 4 dedicated casuals (massage, beauty, nails, hair), relief from the AM pool. Venue Manager 1. **On the books: 16 therapists (12 AM + 4 PM), 4 phlebotomists, 1 Venue Manager = 21.** Weekly loading at 18 a day, six trading days: Massage+Beauty 24 shifts over 6 people (4 each), Nails 12 over 3 (4), Hair 12 over 3 (4), phlebotomists 12 over 4 (3). Under adaptive rostering lighter mornings simply call in fewer. Not modelled: planned multi-week leave, public holiday premiums, induction.

Employment type conflict flagged: job postings say Venue Manager full-time salaried and phlebotomists permanent part-time (25 hours); the cost model prices both at hourly casual-equivalent rates. TO CONFIRM.
