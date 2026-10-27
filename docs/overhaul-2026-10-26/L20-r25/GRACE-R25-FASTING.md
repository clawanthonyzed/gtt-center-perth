# GRACE R25: Fasting rules for the pregnancy glucose tolerance test

Author: Grace. Date: 2026-10-27. DRAFT for Anthony. Nothing is sent. General information from published sources, not medical advice. Lab confirms before launch.

## READ-FIRST CHECK (GTT-READ-FIRST.md, 2026-10-27)
- Venue manager: hired, starts 06:30 (Mon to Fri 06:30 to 15:00). 07:00 is the first draw. Anthony is owner and director, 0 operational hours.
- Path A = PREFERRED, package WITH the GTT midwife consult. Path B = NOT preferred, outside referral, no GTT consult, no limit on Path B.
- Prices: Path A A$320 / A$370, Path B A$300 / A$350, all including the A$27.85 lab fee (R).
- Rebates used: consult A$32.95 + lab A$22.05 = about A$55.00 (R).
- Midwives 08:00 to 16:00, first consult 08:15.
- Late rule: blood draws have no wiggle room; consults have a 10 minute grace window.
Tags: R repo, V verified source (URL and date read), E estimate, U unverified.

## 1. Answer first
The "at least 8 hours and no more than 14 hours" wording is NOT supported by any Western Australian lab, so do not put it on the booking page. The three WA labs say different things. The only window that satisfies all three is **10 to 12 hours, water only**. That is also the value already in the repo (docs/gtt-clinical-protocol.md, "10 to 12 hours"). Use it as the planning value; the lab GTT partners with confirms the final wording before launch.

## 2. What each source says (all read 2026-10-27)
| Source | Fasting window | Water | During the test | Tag |
|---|---|---|---|---|
| PathWest patient sheet SOP-2484 v1.0, issued 24/07/2026 ([PDF](https://pathwest.health.wa.gov.au/~/media/PathWest/Documents/For-Patients/Preparing-for-Your-Test/Patient-Testing-Instructions-2026/English/Glucose-Tolerance-Test-GTT-Patient-Instructions--English.pdf)) | "at least 10 - 12 hours ... but no longer than 16 hours"; no tea, coffee, juice, milk, gum or lozenges | "You may drink water if thirsty" | Stay in the centre and remain seated; no smoking for 1 hour before and during; plan 2 to 3 hours; eat a regular diet with carbohydrates for the 3 days before | V |
| Clinipath GTT page ([link](https://www.clinipathpathology.com.au/patients/prepare-for-your-test/glucose-tolerance-test/), read through crawl4ai because plain requests returned 403) and FAQ ([link](https://clinipathpathology.com.au/patients/faqs-and-results)) | "8 to 16 hours (12 hours is optimal)"; FAQ says 10 to 16 hours, never over 16 | Water allowed, "no more than 2 glasses" on the morning | No smoking or strenuous exercise for 8 hours before and during; walk-in, no appointment | V |
| Western Diagnostic Pathology (WDP) ([link](https://www.wdp.com.au/pre-test-collection-information/glucose-tolerance-test-gtt)) | "at least 8 hours"; "preferable you do not fast for more than 12 hours" | "Water with no additives can be consumed" | No strenuous exertion before or during (including brisk walking to the clinic); no smoking for 1 hour before and during; about 2 hours | V |
| NSW Health Pathology sheet, 26 Aug 2022 ([PDF](https://pathology.health.nsw.gov.au/documents/dietary-requirement_glucose-tolerance-test)) | No food or drink except water from 10:00 pm the night before | Water only, "a small amount" during the test | Sit quietly in the centre; at least 150 g carbohydrate a day for 3 days before | V (another state, for comparison) |
| RACGP, Gestational diabetes (aligned to ADIPS 2025 on 01/08/2025) ([link](https://www.racgp.org.au/clinical-resources/clinical-guidelines/key-racgp-guidelines/view-all-racgp-guidelines/management-of-type-2-diabetes/gestational-diabetes)) | "an 8- to 12-hour overnight fast", start before 9.30 am | Not addressed | Drink the glucose within 5 minutes; stay seated for the 2 hours; postpone if acutely ill | V |
| ADIPS 2014 consensus, Nankervis et al, modified Nov 2014 (adips.org PDF) | No fasting hours stated in the text I read | Not stated | Says there is "no need for a 3 day high carbohydrate diet" before the test | V |
| ADIPS 2025 consensus, MJA 223(3), published 23 June 2025, doi 10.5694/mja2.52696 ([link](https://www.mja.com.au/journal/2025/223/3/australasian-diabetes-pregnancy-society-adips-2025-consensus-recommendations)) | No fasting hours stated on the page read | Not stated | Diagnostic thresholds only; warns that tube choice and transport delay cause under-diagnosis | V |

## 3. What I could NOT read (honest gaps)
- **No ADIPS 2020 update exists in what I found.** The updates are the ADIPS 2024 summary and the 2025 MJA consensus. Neither states fasting hours on the pages read.
- **RANZCOG** statement on GDM diagnosis: not retrieved (search returned secondary sources only). U.
- **RCPA / Pathology Tests Explained** (ptex.au glucose page): HTTP 404. U.
- **WHO 2013 guidance** (NCBI Bookshelf NBK169357): blocked by a browser check. A research study quotes "8 to 14 hours" for the 75 g test, which is probably where the 8-to-14 figure comes from, but I could not confirm it in a WHO document. U.
- **Conflict to settle with the lab:** ADIPS 2014 says no 3 day carbohydrate loading is needed; PathWest, NSW and RACGP still ask for regular carbohydrates for 3 days. Use the lab's wording; it is harmless advice.

## 4. Planning value for the booking page and reminders
Wording (plain English, lab to confirm): "Do not eat or drink anything except plain water for at least 10 hours and no more than 12 hours before your first blood test. No tea, coffee, juice, milk, gum or lollies. Water is fine. Do not smoke for the hour before and during the test, and do not exercise hard that morning."

Because the first draw is 07:00 and the old advice said "from midnight", the old advice is too short (only 7 hours before a 07:00 draw). Give each client her own "last food and drink" time, as the repo already plans (docs/gtt-clinical-protocol.md, personalised fasting start time):
| Her Draw 1 | Last food and drink between |
|---|---|
| 07:00 | 7pm and 9pm the night before | <!-- factcheck:ok -->
| 08:15 | 8:15pm and 10:15pm |
| 10:20 | 10:20pm and 12:20am |
Maths: Draw 1 time minus 12 hours (earliest) and minus 10 hours (latest). Tag E, derived from the lab ranges.

## 5. Water only during the test
Supported by PathWest (stay seated, water if thirsty), Clinipath (water allowed), WDP (water with no additives), NSW ("a small amount of water") and RACGP (stay seated). Rule for the welcome pack: water only, small sips, until Draw 3 is done. Tea and food only after Draw 3.

Important catch: PathWest, NSW and RACGP say the client stays at the collection centre and remains seated for the whole test. GTT's model has her in massage, nails or hair chairs between draws (R). Services are seated or reclined, but they are away from the collection chair. WDP's page does not say this, and the repo timetable is built on clinical marks from WDP's Carole Rivers (R), but a written yes from the chosen lab that supervised seated services inside the same premises meet its rule is NOT IN REPO. Nearest compliant fallback if the lab says no: services stay seated and are brought to the lounge chair beside the collection rooms. Add to the lab question list.

## 6. Fixes the repo needs (not applied; for Anthony)
1. docs/operations-manual.md front desk step 2 says under 8 hours fasting means do not proceed. That matches WDP and Clinipath but not PathWest (10 hours). Set it to the chosen lab's minimum.
2. Any file that says "from midnight" should use the personal last-food time in section 4.

## QUESTIONS FOR ANTHONY
1. Fasting wording: use 10 to 12 hours now (recommended, fits all three labs), or wait for the chosen lab to say? Recommendation: use 10 to 12 and replace it when the lab replies.

Regards.
Grace
