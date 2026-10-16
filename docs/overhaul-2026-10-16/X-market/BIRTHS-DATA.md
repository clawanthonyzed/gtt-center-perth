# Births data (S4a, P6a, P6b)

## Latest release and the next one

| Item | Finding | Source |
|---|---|---|
| Latest ABS release | Births, Australia, reference period 2024, released 15 October 2025 | https://www.abs.gov.au/statistics/people/population/births-australia/latest-release |
| Next release | Births, Australia, reference period 2025, Friday 6 November 2026, 11:30 am AEDT (verified on the ABS release calendar; Anthony's date is correct) | https://www.abs.gov.au/release-calendar/future-releases/202611/rcc_people |
| Latest state health report | WA Health publishes Mothers and Babies as interactive quarterly and annual reports; the last full annual PDF listed is 2016. Use ABS for the headline numbers | https://www.health.wa.gov.au/Reports-and-publications/Western-Australias-Mothers-and-Babies |

2024 is still the latest ABS year. Dated task: on 6 November 2026 pull the 2025 figures for Western Australia and Greater Perth, replace the table below and recalculate the share (item in ITEMS-TO-CONFIRM).

## Replacement data for Slide 4 (2024 final registrations)

| Measure | 2023 | 2024 | Change |
|---|---|---|---|
| Registered births, Western Australia (state of usual residence) | 32,031 | 30,541 | -4.7% |
| Registered births, Greater Perth | 25,436 | 24,271 | -4.6% |
| Total fertility rate, Greater Perth (births per woman) | 1.58 | 1.47 | down |
| Total fertility rate, Western Australia | 1.570 | 1.434 | down |
| Median age of mothers, Western Australia | | 31.9 years | |
| Perth births per week (24,271 / 52) | 489 | 467 | |

Sources: ABS Births, Australia 2024 (WA summary page above) and ABS Data by region, registered births measure for Greater Perth, pulled from the ABS data API on 2026-10-16 (https://data.api.abs.gov.au, dataflow ABS_REGIONAL_ASGS2021, measures BD_2 and BD_3). The ABS notes that part of the 2024 fall reflects a 2023 registration backlog being cleared.

## CONFLICT FLAG: figures currently in the plan do not match ABS

The plan and the model's market-size row state about 33,570 births for Western Australia, about 26,790 for Greater Perth and about 515 tests a week, attributed to a KPMG analysis dated 17 July 2025. Neither number matches the ABS series. ABS shows Western Australia 30,541 and Greater Perth 24,271 for 2024 (and 30,516 on the headline release page), and the ABS release itself is dated 15 October 2025. KPMG's own 2024 article (reported 24 July 2024) put Greater Perth at "just over 25,000" for 2023, which agrees with ABS. The KPMG source for 26,790 could not be found. Recommendation: use the ABS figures. The effect is a market about 9% smaller than the plan states (467 a week, not 515). No financial-model figure depends on it: the model is capacity driven (18 a day, 108 a week). For Idea Lobster to confirm with Anthony before Slide 4 is rebuilt.

## Page 6 market share paragraph (ready to paste)

"Greater Perth recorded 24,271 births in 2024 (Australian Bureau of Statistics), about 467 a week. Gestational diabetes screening is offered to nearly every expecting mother, so we treat the weekly birth count as the weekly pool of glucose tolerance tests. At full capacity GTT Center Perth offers 108 morning testing places a week (18 a day over six days), which is about 23% of that pool. This figure is a ceiling on the places we can offer, not a forecast of bookings and not a claim of market control. Most expecting mothers will continue to be tested at their usual collection centre or hospital, and we expect that to remain the case. GTT Center Perth is a premium, high-desire choice for the expecting mother who wants the wait to be comfortable, booked 2 to 4 weeks ahead, and who is prepared to pay for it. Our plan does not depend on a large share of the market. It depends on filling our own places through the referral pipeline, the pre-launch waitlist and our marketing. The 2025 figures are due on 6 November 2026 and will replace these numbers."

How to read the share: it is places offered divided by tests available in Greater Perth. It does not say how many women choose us. If the 2025 release shows fewer births, the same 108 places become a larger share; the business does not depend on that number.
