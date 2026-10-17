# A1: What if the lab fee is not bulk-billed? Cost model

This is general knowledge, not your personal documents. Verify with a qualified adviser before acting.

Prepared 2026-10-17 by Grace with Theodore (CFO) and Catherine (legal). Every GTT figure comes from the repo calculators run with a changed input (`docs/overhaul-2026-10-16/M-model/m_part2.py`, which wraps `tools/am_demand_tier_financial_ladder.py` and `tools/cost_ramp_model.py`); no new calculator was written. The driver call is saved as `l_fee_driver.py` in this folder. Fees come from MBS Online only (see PRIMARY-SOURCES.md section 4). **Lab private fees may differ from MBS fees. No fee quoted yet by PathWest, WDP or Clinipath.** GST treatment is set aside (the GST-stress column is shown for reference only).

## 1. The fee for one gestational glucose tolerance test visit (MBS, fetched 2026-10-17)

| Item | What it covers | Schedule fee | Medicare benefit at 85% (out of hospital) |
|---|---|---|---|
| 66548 | Oral glucose tolerance test in pregnancy: glucose administration, at least 3 blood glucose measurements | A$19.90 | A$16.95 |
| 73928 | Patient episode initiation: specimen collected in an approved collection centre (this is the only collection-related fee in the table; there is no separate venepuncture item) | A$5.95 | A$5.10 |
| **Total** | | **A$25.85** | **A$22.05** |

Notes: (a) The 75 per cent benefit applies only to services in a hospital episode; the Act s10(2)(b) gives 85 per cent otherwise, and pathology is not on the 100 per cent list. (b) Item 73920 (A$2.40) replaces 73928 only where the lab's collection centre sits in the same premises as its own GX or GY laboratory. That is not GTT's case, so A$2.40 is not used. (c) If the lab bulk-bills item 73928 it also receives the bulk-billing incentive item 74995 (A$4.00), paid by Medicare, not by GTT. (d) Group P12 bulk-billing items are for unreferred services to under-16s and concession card holders, so they do not apply. (e) Item 66548 may differ from the lab's actual test mix if extra tests are ordered (for example item 66695 hormone tests); this model uses only the GTT.

## 2. Volume (from the repo)

18 AM clients a morning x 26.33 trading days a month = **473.94 clients a month**. A$250 package, A$6,582.50 revenue per daily client per month. Baseline: net operating profit **A$35,186.40 a month** (A$422,236.80 a year), break-even 8.266 clients a morning (spaced), GST-stress net A$23,442.58 and break-even 9.255.

## 3. The three cases

| | Case 1: Medicare bulk-bills (lab fee to GTT zero) | Case 2: client pays the lab privately at the MBS fee | Case 3: GTT absorbs the fee |
|---|---|---|---|
| Fee per client borne by GTT | A$0.00 | A$0.00 (the lab collects it directly, not through GTT) | A$25.85 |
| Cost to GTT per morning (18 clients) | A$0.00 | A$0.00 | A$465.30 |
| Cost to GTT per month (473.94 clients) | A$0.00 | A$0.00 | **A$12,251.35** |
| Net operating profit per month | **A$35,186.40** | A$35,186.40 if demand holds | **A$22,935.05** (down A$12,251.35, 34.8%) |
| Year 1 net (12 months, no ramp) | A$422,236.80 | A$422,236.80 if demand holds | **A$275,220.60** (down A$147,016.20) |
| GST-stress net per month (reference) | A$23,442.58 | A$23,442.58 | A$12,304.99 |
| Break-even clients per morning (repo, spaced) | 8.266 | 8.266 | **9.219** (so 10 clients in whole bookings) |
| GST-stress break-even | 9.255 | 9.255 | 13.014 |
| What the client pays | A$250 | A$250 + A$25.85 = A$275.85 headline, less any Medicare rebate she can claim | A$250 |
| Client cash outlay after Medicare | A$250 | If the collection qualifies for Medicare: A$250 + A$3.80 gap (fee A$25.85 less rebate A$22.05). If it does not qualify: A$275.85 with no rebate | A$250 |

Source of Case 3 numbers: `P.steady(fee=25.85)` and `P.be_search(fee=25.85, policy="spaced")` in the repo driver. Cross-check: the repo's own lab-fee table (3-WAY-FINANCIAL-MODEL-AUD.md section 10) gives A$4,739.40 a month per A$10 a client; 2.585 x 4,739.40 = A$12,251.35. It agrees.

**Price GTT would need to charge to stay whole (Case 3):** A$250 + A$25.85 = **A$275.85** (GST aside). Rerunning the repo break-even at A$275.85 with the A$25.85 fee returns 8.266, identical to the baseline, which proves the arithmetic. If GST applies to the whole package the uplift must be grossed up (TO CONFIRM with the accountant).

Smaller fee if the lab counts only the test (A$19.90, no collection item): A$9,431.41 a month, net A$25,754.99, break-even 8.980.

## 4. What the cases mean

1. Case 1 is the committed plan and needs the lab to hold the collection centre approval and Medicare to pay for GTT's collections. That depends on the collector rule (MEDICARE-FEASIBILITY-REPORT.md section 3).
2. Case 2 protects GTT's profit only if clients accept paying A$25.85 more. The repo's own fill sensitivity (MODEL-WORKINGS.md section 5) shows the exposure: at 85 per cent fill net is +A$17,413.65 a month (Year 1 A$208,963.80); at 70 per cent fill it is -A$359.10 a month. A price rise of 10 per cent could move fill; no demand data exists, so this is not modelled. Legal point: if GTT's room is not an approved collection centre, s23DNL of the Act requires GTT to tell each client no Medicare benefit is payable.
3. Case 3 leaves GTT profitable at A$22,935.05 a month and still breaks even at 10 bookings, but it removes A$147,016.20 from Year 1. It is the fallback, not the plan.
4. Do not let GTT collect the lab's fee and pass it on. The R workstream (S38-10-GST-STRUCTURE.md) advises that the lab, as supplier, takes any private fee directly.

## 5. Phlebotomist cost lines (for the workaround comparison)

From the repo calculator: 2 phlebotomists on shift = wages A$11,754.19 a month (A$9,075.00 weekdays at A$34.375 an hour x 6 hours x 22 days x 2, plus A$2,679.19 Saturdays at 1.5 times) and **A$13,364.51 a month with super 12 per cent and workers compensation 1.7 per cent**, about A$6,682.29 per phlebotomist on shift. That is the saving to GTT if a lab supplies the collectors (workaround ii), before any charge the lab makes: net would move from A$35,186.40 to about A$48,550.91 (TO CONFIRM; the lab may charge a market-value fee for the service, which is lawful if not tied to doctor request volumes). Comparing: Case 3 costs A$12,251.35 a month, almost the same as the A$13,364.51 collector wage bill, so "GTT pays the collectors but Medicare pays the lab" is worth about as much as "the lab pays the collectors but GTT pays the lab fee". The collectors are already inside the baseline, so the realistic worst case is Case 3, net A$22,935.05, not a double count.
