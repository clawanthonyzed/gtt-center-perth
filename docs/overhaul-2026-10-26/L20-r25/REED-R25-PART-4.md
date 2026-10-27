# Reed R25 Part 4: Fees a new GTT faces before opening (Gap 4)

## READ-FIRST CHECK
- Venue manager: a hired person, starts 06:30 (Mon to Fri 06:30 to 15:00). First draw 07:00. Anthony is owner and director, 0 operational hours.
- Path A = package WITH the GTT midwife consult (preferred). Path B = outside referral, no GTT consult (not preferred, not limited).
- Prices: Path A A$320 / A$370 advertised, GTT charges A$292.15 / A$342.15. Path B A$300 / A$350, GTT charges A$272.15 / A$322.15.
- Rebates used: about A$32.95 consult + A$22.05 lab = A$55.00.
- Midwives on site 08:00 to 16:00, first consult 08:15.
- Late rule: blood draws no wiggle room; consults 10 minute grace window.
- Tags: R repo, V verified source (URL, 2026-10-27), E estimate, U unverified. Locked profit not changed.

## What the repo start-up list holds (R)
Source: HUMAN-READABLE-STARTUP-COSTS.md, total A$251,198. Relevant lines: Premises bond and legal A$19,000; Design and approvals A$4,100; Professional services A$539 (accountant, ASIC, solicitor bundled, insurance brokerage); Technology A$820; Staffing before opening A$22,872; Marketing A$1,250. Signage is inside fit-out (startup_costs.yml note). Ongoing costs in opex.yml include laundry, cleaning and insurance.

## Fee list with checks against the repo

| Fee or charge | When | Approx cost | Tag and source | Repo status |
|---|---|---|---|---|
| Company registration, 3 companies (Holdings, Medical, Lounge) | Before opening | A$636 each = about A$1,908 (2026-27, third-party sites; ASIC schedule to confirm) | E. [ausbusinessregister.com.au](https://ausbusinessregister.com.au/asic-fees-australia/) | **MISSING or too small.** Whole professional services line is A$539, which also holds accountant, solicitor and brokerage |
| ASIC yearly review, 3 companies | Each year | A$342 each = about A$1,026 a year | E. [ausbusinessregister.com.au](https://ausbusinessregister.com.au/asic-annual-review-guide-2026/) | MISSING from opex |
| Business name (if trading under "GTT Center Perth") | Before opening | A$47 for 1 year or A$108 for 3 years | E. [sleek.com](https://sleek.com/au/resources/5/) | MISSING (small) |
| GST group, tax consolidation, payroll tax group set-up | Year 1 | Accountant time. Amount NOT IN REPO | U | Only "accountant" in A$539. Likely MISSING |
| Medicare provider numbers (midwives, and each place of work) | Before first consult claim | No fee found in an official page (a recruiter says free) | U. [Services Australia](https://www.servicesaustralia.gov.au/apply-for-initial-provider-and-prescriber-numbers) | Not a money line. TIME: processing is said to take up to 28 days (third-party), which matters for the 2 month opening. Also a number does not automatically mean billing rights |
| AHPRA registration (midwives, and phlebotomists if registered) | Staff pay their own | Staff cost. GTT pays only if it chooses | Brief says staff pay | Not a GTT cost |
| Local government approval for hair, beauty, massage-type skin penetration work | Before opening | Example A$125 (Shire of Manjimup application). Metro councils vary | V (example only). [ABLIS Manjimup](https://ablis.business.gov.au/service/wa/notification-of-a-skin-penetration-establishment-shire-of-manjimup/21120). Law: Health (Skin Penetration Procedure) Regulations 1998, apply as local laws | Possibly inside "Design and approvals" A$4,100, but not itemised. FLAG |
| Food business notification (only if GTT supplies glucose drink, food or drinks) | Before opening | Notification about A$87 to 88; low-risk yearly A$108 to A$168 depending on council; very low-risk can be A$0 | V. [City of Kwinana](https://ablis.business.gov.au/service/wa/local-registration-notification-of-a-food-business/22525), [City of Wanneroo](https://ablis.business.gov.au/service/wa/notification-registration-of-a-food-business-city-of-wanneroo/22581). How a glucose drink is rated is U | MISSING. Repo has a food and drink side (excluded from locked profit) |
| Planning approval or change of use, building permit for fit-out | Before fit-out | Council fees depend on works value (A$139,678 fit-out). Amount NOT IN REPO | U | Probably inside "Design and approvals" A$4,100. FLAG as too small until checked |
| Signage permit | If new signs | Council fee U | U | Signage is inside fit-out, permit fee not itemised |
| Music licence (OneMusic: APRA AMCOS and PPCA, one licence) | Before playing music | Priced by floor area and music source; no public price. Get a quote | U. [OneMusic hair and beauty](https://onemusic.com.au/licences/hair-and-beauty/) | **MISSING.** Zero hits in the repo for APRA or PPCA |
| Clinical waste pail and sharps collection | Before first draw | Sharps containers about A$3.90 to 12.50 each ex GST; 50 L clinical pail A$75 to A$102 per service. Perth service area not confirmed (Waster pages conflict) | E. [Waster sharps costs](https://help.waster.com.au/sharps-supply-treatment-costs), [Waster pail](https://waster.com.au/product/50-litre-medical-waste-pail-service-clinical-waste-bin/). Perth supplier alternative: Initial Hygiene | Equipment for sharps is in capex. The recurring collection fee is MISSING from opex |
| Trade waste approval (drains from basins, drink prep) | If required | Unknown. Ask the Water Corporation whether low volume needs approval | U | MISSING (probably nil) |
| Cleaning and laundry | Monthly | In repo opex lines | R | Present |
| First aid course for all staff | Before opening | Cost NOT IN REPO (a GTT midwife may run it, Round 25 lock) | U | Check; may be inside staffing before opening |
| Police checks | Before start | Cost by staff category in Catherine's file | U | Check |
| First-year insurance paid up front or as a deposit | Before opening | See Part 2: about A$9,000 to 25,000 plus workers compensation | E | Not in the start-up table. The repo note says it sits in a working capital line on an old A$400 a month basis |
| Landlord legal and lease costs | Lease signing | In premises line A$19,000 | R | Present |
| Lawyer for the room licence and the three-company paperwork | Before opening | NOT IN REPO | U | Only "solicitor (bundled)" inside A$539 |

## Lines I would add to the start-up list (planning, not locked)
1. Three company registrations and group set-up: at least A$1,908 plus accountant time (E).
2. Council and health approvals itemised: skin penetration, food notification (if any), planning, signage (U until the council is known).
3. Music licence quote (U).
4. Clinical waste collection as a monthly running cost (E, quote needed).
5. First-year insurance: Part 2 ranges.
6. Lawyer time for licence and group set-up (U).

None of these changes the locked profit of A$26,631.97 before company tax. They change the start-up total (A$251,198, which already includes a 12 percent contingency of A$26,914) and a few running lines. Totalled, the items with a figure (company registration, business name, insurance deposit) are roughly A$11,000 to A$27,000 (E, my sum), so the contingency may absorb the low end only.

## QUESTIONS FOR ANTHONY
1. Do you want these lines added to the start-up list now as estimates, or wait for real quotes? Options: (a) add as estimates, (b) wait for the lease and quotes. Recommendation: (a), flagged E, so the funding picture is honest.
2. Will GTT supply the glucose drink itself, or does the lab supply it? Options: GTT supplies / lab supplies. Recommendation: confirm with the lab when a real person replies, since it decides the food business approval.
3. May Reed ask a broker for indicative quotes once you choose one (you send, not us)? Options: yes, after the lease / now. Recommendation: now for indicative figures; the lease only changes the property line.

Regards.
