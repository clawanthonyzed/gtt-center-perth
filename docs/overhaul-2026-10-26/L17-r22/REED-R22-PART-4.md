# REED R22 Part 4: Record keeping options (Job 4)

Reed, commercial consultant. Researched 2026-10-26. Costs are for information only, NOT for the financial model. Tags: V verified (URL opened 2026-10-26), E estimate, U unverified.

## READ-FIRST CHECK
- Venue manager opens at 06:30 (Mon to Fri 06:30 to 15:00); the first draw is 07:00. R
- Path A = PREFERRED (package with GTT midwife consult); Path B = NOT preferred (outside referral). R
- Path A A$320 / A$370 shown, GTT charges A$292.15 / A$342.15; Path B A$300 / A$350 all in. R <!-- factcheck:ok -->
- Rebates used: A$32.95 consult + A$22.05 lab = A$55.00. R
- Midwives 08:00 to 16:00; first consult 08:15; 25 minute blocks to 10:30. R
- Late rule: test no grace; consult 5 to 10 minutes if the midwife can finish (OPEN). R
- Out of date: FINANCIAL-CENTER-OF-TRUTH.md (20 minute consult). GTT-READ-FIRST.md wins. <!-- factcheck:ok -->
- Locked: GTT passes no booking details to the lab; the paper folder becomes a computer record (method being researched, this file). R

## Compared options
US dollar prices converted at the Reserve Bank rate in logs/fx_aud.json, as of 2026-10-26: US$1 = A$1.4223 (converted, not a quote).
| Option | Published price (date opened 2026-10-26) | Data in Australia? | Audit log | Secure messaging | Online booking | Waitlist emails |
|---|---|---|---|---|---|---|
| Halaxy https://www.halaxy.com/pricing | Core platform free. Add-ons by credits, A$0.15 to A$0.22 a credit incl GST. No per-practitioner price shown | Privacy policy: "Your data is stored in Australia", but lists US sub-processors such as AWS (https://www.halaxy.com/privacy) | Not confirmed | Paid credit add-on | Yes, free core | Not mentioned. NOT CONFIRMED |
| Cliniko https://www.cliniko.com/pricing/ | US$45 a month for 1 practitioner (A$64.00); US$95 for 2 to 5 (A$135.12); SMS US$0.10 each | Yes: "New Cliniko accounts based in Australia will have their data stored safely in Australia" (https://www.cliniko.com/security/). 2FA available | Not stated on pages opened | Not stated | Not stated on pricing page | Not stated. NOT CONFIRMED |
| Zanda Health (was Power Diary) https://zandahealth.com/pricing/ | Starter US$19 for 1 practitioner (A$27.02); Growth US$49 base (A$69.69) plus US$19 (A$27.02) per extra practitioner. AUD price not shown | Page says "ISO 27001-certified infrastructure", no location. A search result for Zanda's support site says Sydney data centres; I could not open that text. U | Yes: "All user activity is automatically recorded and can be audited" | Unlimited email; SMS US$0.09 each, two-way SMS included | Yes, clients book and pay online | Yes: "notifications when a slot opens" |
| Nookal https://www.nookal.com/pricing/ | A$49 Essentials, A$59 Professional, per practitioner per month | Not stated on the pages opened (security page last updated 11 Jun 2026). U | Yes: "Key user activities are logged" (https://www.nookal.com/legal/security); 2FA available | Add-on from A$1.50 per user a month on Professional; none on Essentials | Yes | Basic waitlist on Essentials; "upgraded" version listed as coming soon |
| Best Practice (Bp Premier) https://bestpracticesoftware.com/?p=146029 | A$1,489.41 a year full-time doctor, A$893.65 part-time doctor, A$521.29 a year allied health, ex GST, from 1 July 2026 (about A$43 a month for allied health, my arithmetic). Which tier a midwife falls in: NOT CONFIRMED. Medical Director: price not found | Search summary says on-premises (own server); I did not open that FAQ. U | Not checked | Not checked | Not checked | Not checked |
| Microsoft 365 Business Premium (document storage, not a booking system) | Reseller page: A$28.10 per user a month ex GST, undated, currency not stated (https://voipitup.com.au/microsoft-365/). Microsoft's own AU page timed out. U | Australia is listed as a Local Region Geography with data residency commitments (https://learn.microsoft.com/en-us/microsoft-365/enterprise/o365-data-locations, dated 2026-10-08) | Purview Audit (Standard) listed in the same page | Email and Teams | No booking page opened or verified | No, needs a separate tool |
| Google Workspace https://workspace.google.com/intl/en_au/pricing | A$9.90 Starter, A$19.80 Standard, A$30.90 Plus, per user a month, annual plan | Google's data-regions page lists only United States, European Union, or no preference. No Australian region (https://knowledge.workspace.google.com/admin/compliance/choose-a-geographic-location-for-your-data) | Not checked | Gmail | No | No |

## Picks
- Cheapest that meets the privacy needs with the facts confirmed: none is fully confirmed. The cheapest path to confirm first is Halaxy (free core, data stated as stored in Australia), but its audit log and waitlist are not confirmed. Cliniko is the cheapest paid option with Australian hosting confirmed (about A$135 a month for 2 to 5 practitioners, information only).
- Best all-in-one: Zanda Health Growth. It is the only option where audit log, online booking and waitlist emails are all shown on its own pricing page. For 2 permanent plus 1 casual midwife that is US$87 a month (US$49 plus 2 x US$19), about A$123.74 (E, assumes each midwife counts as a practitioner). Ask Zanda to confirm Sydney hosting in writing.
- Nookal Professional (A$59 each, about A$177 for 3) is the fallback with an Australian-dollar price and audit logs, once hosting is confirmed.
- Microsoft 365 is a good place for referral copies (Australian data residency, audit) but not a booking or waitlist tool. Google Workspace fails on Australian hosting.

## NOT confirmed (ask each vendor before choosing)
Australian hosting for Zanda and Nookal; audit log for Halaxy and Cliniko; waitlist email for Halaxy and Cliniko; whether any option can claim Medicare for the midwife; how a referral copy is stored per client; how long records must be kept (Catherine); whether a vendor can exclude lab details so GTT passes nothing to the lab; exit and export of records.

## QUESTIONS FOR ANTHONY
1. Who is the records owner: GTT Medical, the midwife, or you? Options: (a) GTT Medical company, (b) the midwife as practitioner. Recommendation: (a), then Catherine writes the privacy notice.
2. Choose which two vendors Grace should email for written answers? Recommendation: Zanda and Cliniko. Nothing is sent until you approve.

Regards.
