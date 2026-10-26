# GRACE-R20-SERVICES-AUSTRALIA: backup contact routes for Medicare provider numbers and pathology approvals

Author: Grace (Operations Manager, GTT Center Perth). Checked 2026-10-26. **DRAFT for Anthony. Nothing was sent to anyone.** Builds on SERVICES-AUSTRALIA-R19.md.

How I checked: WebSearch worked; direct page fetches timed out or reset, so per the Anti-Block rule I opened each page with the stealth browser (crawl4ai 0.8.6) on the server root@46.250.244.248 and read the PDF forms with a text extractor. VERIFIED = I opened the page or form and read the text. LISTED ONLY = it appears in a search summary or a link and I did not open the target. UNVERIFIED INBOX = I cannot prove anyone reads it, because I sent nothing.

## 1. Short answer

Services Australia has no general web enquiry form or public enquiry email for pathology approvals or for Medicare provider numbers. It has three real backup routes to email: a secure message inside HPOS, a published email on its provider number application forms, and post. Phone lines also exist. The earlier candidate pathology.registration@servicesaustralia.gov.au is **still unverified**.

## 2. Every real route found

| # | Route | URL | What it is for | Status |
|---|---|---|---|---|
| 1 | **Provider Registration email**: provider.registration@servicesaustralia.gov.au | Printed on form HW088 (midwife or nurse practitioner provider number form, file hw088-2610, September 2026): https://www.servicesaustralia.gov.au/sites/default/files/2026-09/hw088-2610-f.pdf and on form HW093 (allied health): https://www.servicesaustralia.gov.au/sites/default/files/2025-10/hw093-2511en-f.pdf | Returning the provider number application form with supporting documents ("email to provider.registration@servicesaustralia.gov.au"). The form warns that email may be unsecured. | **Address VERIFIED as published on two official forms (I read both). Inbox monitoring UNVERIFIED.** It is for applications, not for general questions. |
| 2 | **Midwife form page HW088** | https://www.servicesaustralia.gov.au/hw088 | Application for a Medicare provider number and/or prescriber number for a midwife or nurse practitioner | VERIFIED page exists (HTTP 200, I opened it). Page last updated 1 October 2026. No email on the page itself; the email is inside the PDF (route 1). |
| 3 | **Provider Registration, post** | Same PDF: "Services Australia, Provider Registration Section, GPO Box 9822, in your capital city" | Paper applications and enquiries | VERIFIED on the forms. Fax 02 6122 9739 also printed on the forms (VERIFIED, not used). |
| 4 | **Provider Registration, phone** | https://www.servicesaustralia.gov.au/health-professionals-contact-information (page last updated 30 September 2026) | Medicare Provider Registration: new provider numbers, existing provider number enquiries: 1300 302 122, Monday to Friday 8 am to 5 pm local time | VERIFIED (opened). Anthony said emails only, so listed for completeness. |
| 5 | **Medicare provider enquiries line** | same contact page | 132 150 (option 2 for provider enquiries and HPOS) | VERIFIED (opened). |
| 6 | **Pathology Approval Enquiries, phone and post** | same contact page | Approved Pathology Authorities, Approved Pathology Practitioners, Accredited Pathology Laboratories: 1300 721 546, Monday to Friday 8:30 am to 5:00 pm AEST; post to "Services Australia, Pathology Approvals, GPO Box 9822, Sydney NSW 2000" | VERIFIED (opened). **No email is listed for Pathology Approval Enquiries on this page.** |
| 7 | **HPOS Messages** (secure message) | https://www.servicesaustralia.gov.au/use-hpos-messages (page last updated 27 August 2024) | Page text: "HPOS Messages is a secure way to directly correspond with our program teams. It's not an email account." The list of program teams reached through HPOS Messages includes **Pathology Registration** | **VERIFIED (opened).** Needs a PRODA account and HPOS access linked to the organisation or provider, which GTT does not have yet. This is the closest thing to a secure enquiry box. |
| 8 | **Upload forms in HPOS** | https://www.servicesaustralia.gov.au/upload-forms-hpos | Sending forms and documents securely | LISTED ONLY (link seen on the HPOS Messages page; not opened). |
| 9 | **Pathology authority and collection pages** | https://www.servicesaustralia.gov.au/approved-pathology-authorities (updated 26 November 2025) | Rules for becoming an Approved Pathology Authority, form HW011 | VERIFIED (opened). No enquiry email on it. |
| 10 | **Write to us (general)** | https://www.servicesaustralia.gov.au/write-to-us (updated 24 June 2026) | General postal addresses by program, including Medicare GPO Box 9822 | VERIFIED (opened). No pathology or provider email. |
| 11 | **Web form for pathology approvals or provider numbers** | none found | n/a | Searched official pages and the contact page; **no online enquiry form exists for these topics**. The only form-style route is the HPOS Messages route above. |
| 12 | **Department of Health pathology collection centres compliance team** | https://www.health.gov.au/contacts/pathology-collection-centres-compliance-team | Compliance questions about pathology collection centres. Email corporate.compliance@health.gov.au. Date last updated 3 June 2025 | **VERIFIED (opened)** as a published contact. This is Department policy, not Services Australia. It is the verified email route. |
| 13 | **Department of Health pathology contacts** | https://www.health.gov.au/topics/pathology/pathology-contacts | Lists corporate.compliance@health.gov.au and other pathology program emails | VERIFIED (opened). |
| 14 | **Contact us (general Services Australia)** | https://www.servicesaustralia.gov.au/contact-us (updated 16 January 2026) | General, mostly for the public | VERIFIED (opened). Not for providers. |

Emails the Services Australia contact page does list (all verified by me as printed there) belong to other programs and are not for pathology approvals or provider numbers: ebusiness@, onlineclaiming@, air@, medical.indemnity@, medicare.disclosure@, statistics@, healthcareidentifiers@, developerliaison@ and others. Do not use them for this.

## 3. Candidates from earlier rounds

| Candidate | Where it came from | Status now |
|---|---|---|
| pathology.registration@servicesaustralia.gov.au | Department of Health PDF "Pathology Accreditation Assessments in 2022" (July 2022), useful contacts | **Still UNVERIFIED.** A new search found only that 2022 document and a summary saying it is dated and may not be active; no 2025 or 2026 Services Australia page lists it. The current contact page lists only phone and post for Pathology Approvals. I did not send anything. |
| co.gp.manager.pathology@servicesaustralia.gov.au | Services Australia form HW009 (R19 finding) | Not rechecked this round. R19 status stands: the address of the practitioner-undertaking inbox, not a public enquiry box. UNVERIFIED as an enquiry route. |

## 4. Recommended backup order

| Order | Route | Why |
|---|---|---|
| 1 | Department of Health emails already approved in earlier rounds (verified inboxes) | Policy questions, Department first |
| 2 | Posted letter to "Services Australia, Pathology Approvals, GPO Box 9822, Sydney NSW 2000" | Verified address; gives a written record |
| 3 | provider.registration@servicesaustralia.gov.au, only to lodge a midwife's HW088 provider number application | Verified as printed on the official form; use only for that |
| 4 | HPOS Messages to "Pathology Registration" once a PRODA account and HPOS access exist | The only secure message route |
| 5 | pathology.registration@servicesaustralia.gov.au | Last, optional, and Anthony decides because it is unverified |
| 6 | Phone lines | Anthony said emails only |

## 5. Gaps I could not close

| Gap | Note |
|---|---|
| Whether any Services Australia inbox is monitored | Cannot be proven without sending. Nothing was sent. |
| Whether a midwife's provider number needs the lab or the venue to be linked | NOT IN REPO; Catherine and Services Australia |
| HPOS access for a company with no ABN yet | NOT IN REPO |

## QUESTIONS FOR ANTHONY

1. May Catherine or I draft (not send) a posted letter and an HW088 cover note for each midwife?
   - A: Yes, both. B: Letter only. C: Wait until the companies exist.
   - Recommendation: C for the letter (the sender entity needs an ABN), A for the HW088 forms when midwives are hired.
2. Should the unverified pathology.registration@ address be added as an extra recipient?
   - A: Yes, as a copy. B: No. C: Only if the posted letter has no reply in 4 weeks.
   - Recommendation: C.

Regards.
Grace
