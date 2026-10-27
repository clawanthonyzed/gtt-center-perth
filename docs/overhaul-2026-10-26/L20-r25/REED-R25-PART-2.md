# Reed R25 Part 2: Insurance baselines (Gap 2)

## READ-FIRST CHECK
- Venue manager: a hired person, starts 06:30 (Mon to Fri 06:30 to 15:00). First draw 07:00. Anthony is owner and director, 0 operational hours.
- Path A = package WITH the GTT midwife consult (preferred). Path B = outside referral, no GTT consult (not preferred, not limited).
- Prices: Path A A$320 / A$370 advertised, GTT charges A$292.15 / A$342.15. Path B A$300 / A$350, GTT charges A$272.15 / A$322.15.
- Rebates used: about A$32.95 consult + A$22.05 lab = A$55.00.
- Midwives on site 08:00 to 16:00, first consult 08:15.
- Late rule: blood draws no wiggle room; consults 10 minute grace window.
- Tags: R repo, V verified source (URL and date), E estimate, U unverified. Locked profit not changed.

## What the repo has now (R)
- Model insurance line: A$708.34 a month (A$8,500 a year) for public liability + professional indemnity + property and contents. It is a planning estimate, not a quote (data/canonical/opex.yml, FINANCIAL-ASSUMPTION-REGISTER.md).
- Itemised in the repo: public liability A$2,500 to 4,500; professional indemnity A$2,000 to 4,000; property and contents A$1,500 to 2,500; business interruption A$1,200 to 2,000 (optional, not in the model). All R, none quoted.
- Workers compensation is modelled separately as 1.7 percent of wages (R). The repo also holds an older flat guess of A$4,500 to 6,000 a year that the repo itself labels "not the modelled figure".
- No cyber and no management liability line anywhere (searched the data and docs). Missing.
- An older broker email draft exists (docs/insurance-broker-quote-request-draft.md, August 2026). It is OUT OF DATE: it says a third-party pathology partner runs the collection room, asks for professional indemnity of A$5M and 10 to 12 staff. Part 3 of this file replaces it.

## The table

How to read "who requires it": LAW = legislation; LANDLORD = usual lease clause (the lease itself is NOT IN REPO); LAB = the pathology lab or collection partner, NOT KNOWN until a real person replies.

| Cover | Who requires it | Usual baseline | Rough premium a year | Tag and source |
|---|---|---|---|---|
| Workers compensation (every employer, all 3 companies with staff) | LAW. WA employers must insure through an approved private insurer. WorkCover WA publishes yearly recommended rates by industry class; insurers price from them, and must warn an employer if their quote is more than 75 percent above the recommended rate | Cover for all wages, no cap choice | Repo method 1.7 percent of wages. Applying that to the repo wage bill gives about A$18,600 a year (E, my sum: staff A$93,596 and midwives A$12,000 a month loaded, taken back to wages). General market range 1 to 2 percent of wages, not WA-specific | The 2026-27 rate table is U (WorkCover page blocked me, error 403). E: [WorkCover WA rates](https://www.workcover.wa.gov.au/resources/rates), [premium page](https://www.workcover.wa.gov.au/employers/getting-an-insurance-policy/understanding-your-insurance-premium/); range from [Upcover, 2 Sep 2026](https://www.upcover.com/blog/workers-compensation-insurance-cost-australia) |
| Public and products liability | LANDLORD almost always. Possibly LAB. Not law | A$10m to A$20m. Plan A$20m (repo and landlords) | Repo A$2,500 to 4,500. Broker data: A$10m averaged A$57.10 a month, A$20m A$91.10 a month (about A$685 and A$1,093 a year) for firms under 10 staff, 2018-19 data. Health services average A$50 a month. GTT has about 15 staff and clients with a health risk, so expect above these averages | E. [BizCover](https://www.bizcover.com.au/public-liability-insurance-cost/), read 2026-10-27 |
| Professional indemnity: midwives | LAW. The Nursing and Midwifery Board registration standard says every midwife must hold appropriate cover and make a yearly declaration. Cover through an employer is accepted if it meets the standard. The midwife holds the duty, so GTT should give each midwife written proof the employer policy covers her work | Must include automatic reinstatement after a claim. No fixed dollar amount found (U) | Part of the clinic policy below, or the midwife's own union or insurer cover. Usually A$0 extra if GTT Medical's policy names employed midwives | U on the exact standard text (Board page blocked, error 403). E from summaries: [NMBA fact sheet](https://www.nursingmidwiferyboard.gov.au/Codes-Guidelines-Statements/FAQ/Fact-sheet-PII.aspx), [NMBA standard](https://www.nursingmidwiferyboard.gov.au/Registration-Standards/Professional-indemnity-insurance-arrangements.aspx) |
| Medical malpractice or clinic professional indemnity, GTT Medical (covers consults, blood draws, phlebotomists, vicarious liability for staff) | Practical: Medicare provider conditions, the lab, the landlord. Not a stated law for a company | A$5m to A$10m is common; repo asks A$5m. Ask the broker (U) | Repo A$2,000 to 4,000 for professional indemnity, but that figure was for wellness work. A clinical policy for midwives and draws may cost more (U) | R and U. Broker quote needed |
| Property, contents, fit-out | LANDLORD (fit-out and glass), lender if any | Replacement value of fit-out and equipment. Repo fit-out A$139,678 and equipment A$19,280 (R) | Repo A$1,500 to 2,500 (R). Likely higher with a A$139,678 fit-out insured (E) | R, U |
| Business interruption | Nobody. Optional | 6 to 12 months of gross profit | Repo A$1,200 to 2,000 (R) | R |
| Cyber (client health and booking data) | LAW gap: privacy and notifiable breach rules apply to health data. Insurance itself is not compulsory. LAB may ask | A$1m is the usual small-business start | Guide: A$3,000 to 8,000 for A$1m with good security. Survey averages A$2,222 (1 to 5 staff) and A$3,272 (6 to 20 staff) | E. [Pickle guide](https://thinkpickle.com.au/blog/cyber-insurance-australia-small-business), [CSO Australia](https://www.csoonline.com/article/3501343/uninsured-small-australian-businesses-breached-at-nearly-twice-the-rate-of-the-us.html) |
| Management liability (directors, employment claims, one policy for the group) | Nobody. Advisable with 3 companies and about 15 staff | A$1m limit is usual | A$60 to 200 a month = A$720 to 2,400 a year | E. [Upcover, July 2026](https://www.upcover.com/blog/management-liability-insurance-cost-australia) (broker figure, indicative) |
| Phlebotomist and lab-related cover | LAB may set it. NOT KNOWN | Ask: needle-stick and sample handling inside the Medical policy; goods in transit if GTT ever carries samples (it should not) | Usually inside the clinic policy | U |

## Total and what it means for the locked profit
Rough total a year if all covers are bought: public liability about 2,500 to 4,500 + clinic professional indemnity 2,000 to 6,000 + property 1,500 to 4,000 + cyber 2,200 to 8,000 + management liability 720 to 2,400 = about A$9,000 to 25,000 (E, my addition of the ranges above), before workers compensation. The model holds A$8,500 plus workers compensation at 1.7 percent. So the model is at or near the bottom of this range once cyber and management liability are added. The gap is up to about A$16,500 a year, or about A$1,400 a month, if everything is bought at the top. This does not change the locked profit; it is a risk note until real quotes arrive.

## Notes
- Check: the repo says the A$20m public liability comes from a NATA requirement. GTT is not itself a laboratory, so I could not confirm that requirement for GTT (U). The lab partner may or may not impose it.
- The Commonwealth run-off scheme for privately practising midwives exists, but GTT employs midwives, so it probably does not apply (U; ask the broker).

Regards.
