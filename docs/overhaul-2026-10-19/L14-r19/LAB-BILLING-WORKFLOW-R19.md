# LAB-BILLING-WORKFLOW-R19: how the lab gets its A$27.85 without GTT touching it

Author: Grace (Operations Manager, GTT Center Perth). Date: 2026-10-26 (Round 19). DRAFT for Anthony. Nothing was sent to any lab. All money in AUD. Web pages were read on 2026-10-25. VERIFIED means I read the sentence on the page named. UNVERIFIED means I could not read it or it is a search summary only. Legal points cite only the library on the server (/opt/openclaw/second-brain/knowledge/legal/, Catherine's files); I did not ingest or interpret any statute.

## 1. Anthony's goals, in his words

1. GTT does not hold the lab's money, so GTT cannot gain from it (float, interest, terms).
2. GTT pays no card fees on the lab's A$27.85.
3. The lab bills the mother itself, either after she books or after the lab receives the paperwork and sample.
4. No Part IIBA kickback risk.

Already locked, and this plan keeps it: Founder Rule 6 ("lab payment is split online if possible; backup: the client pays the lab directly through a link") and Theodore R18 Q3 (GTT checkout takes only A$272.15; the lab bills the mother separately). Founder Rule 7: GTT earns interest on its own package money only, never on the lab portion.

## 2. How Australian labs already bill a patient who is not bulk-billed (research)

| Lab | What the page says (quoted) | Page and status |
|---|---|---|
| **WDP** | Billing policy: for samples "collected by someone other than our pathology, for example, by your doctor", the patient pays "after testing has been finalised"; for doctor and hospital collected samples "you may receive a message regarding an out-of-pocket payment". Out-of-pocket page: "If your tests require an out-of-pocket payment, we'll send you a follow-up message with a secure link to your invoice." The patient opens the link and enters the postcode from the request form. Pay by Visa/MasterCard (BPOINT), BPAY, phone 1800 350 046 or at Australia Post. There is a request-a-receipt page and a Medicare rebate page. | https://wdp.com.au/patients/pay-my-bill and https://wdp.com.au/patients/billing-policy . **VERIFIED**, read 2026-10-25. No page date. |
| **Australian Clinical Labs** | "Clinical Labs sends patients an account upon completion of a test." Non-Medicare patients get "an itemised Tax Invoice within 14 days of their sample being taken." Pay online (BPoint link), BPAY from the invoice slip, or phone 1300 369 762 (Visa/MasterCard). "The patient will need the receipt and invoice to claim a rebate from Medicare if eligible." Also: "Clinical Labs can directly submit a claim to the Department of Human Services." | https://www.clinicallabs.com.au/billing-information . **VERIFIED**, read 2026-10-25. Page shows only a 2026 copyright. The older URL under /patient/billing-payments/ returned 404 for me. |
| **PathWest** | "You might receive a PathWest invoice if your tests are forwarded to us by the pathology provider you've visited." Pay by BPoint (Visa/MasterCard), phone (08) 6457 1200 weekdays 9am to 4pm, or internet banking quoting the invoice number. Rebate: "Once you receive your rebate cheque from Medicare, forward that along with the outstanding balance." | https://pathwest.health.wa.gov.au/For-Patients/Pay-a-Bill . **VERIFIED**, page "Last Updated: 07/09/2026", read 2026-10-25. Its rebate-cheque route looks older than the other two labs. |
| **Saturn Pathology** | The site menu lists "Billing Policy", "Payment and Debt Policy" and "Fees and Medicare Rebates". I could not retrieve their text (the site loads content by script). | https://saturnpathology.com.au/ . **UNVERIFIED** on content. Contact page read 2026-10-25: contactus@saturnpathology.com.au. |

Reading: every lab already runs "test first, invoice the patient after" for samples that someone else collected. That is exactly GTT's situation, because the collectors are employed by GTT Medical, not by the lab (Catherine R16). So Option 1 below asks the lab to use a process it already has. It is not a new system.

**How the mother claims Medicare** (library, REFERRAL-TELEHEALTH-BILLING-MECHANICS.md section 3.2, verified by Catherine 2026-10-19 from servicesaustralia.gov.au; my own re-fetch of those pages timed out, so I rely on her file):

| Step | Detail |
|---|---|
| She must have paid the account in full | "Only verified payments count": she pays first, then claims (section 3.3). |
| Ways to claim | Medicare online account or app (upload invoice and receipt), by mail, in person, or at the provider if the provider claims electronically. |
| Timing | Online "usually ... within 7 days"; mail "within 21 days". |
| Deadline | The online system refuses services over 2 years old; the Act limit for this kind of claim is 1 year unless extended (s 20B(1)(c)(ii)). Claim promptly. |
| Amount | Test A$16.95 + collection A$5.10 = A$22.05. With the consult (A$32.95) the total is A$55.00 (Theodore R18 Q2). |

Timing consequence for Option 1: the invoice arrives after the test (ACL: on completion, up to 14 days for non-Medicare; WDP: after processing, no set days; PathWest: by post). So the mother's test claim happens roughly 1 to 3 weeks after the test day, plus up to 7 days for Medicare to pay. Her consult claim can be made earlier. The booking confirmation should say this in plain words.

## 3. The three options, ranked

All three: GTT never touches the money, GTT pays **A$0** card fees on the lab's A$27.85 (the lab pays its own merchant fees; ask whether it surcharges), and nothing is held, so there is no float or interest to gain.

| | **1. Lab invoices after it has the request and sample (RECOMMENDED)** | **2. Lab-owned payment link or QR** | **3. Lab terminal in the collection room** |
|---|---|---|---|
| Flow | Booking page says "A$27.85 pathology fee, billed to you by [lab] after your test". On test day the mother fills in the **lab's own** registration form (paper in the specimen bag, or the lab's QR page): mobile, email, Medicare details, and her consent to be billed. The lab receives request plus sample, tests, then sends a text or email with a secure link (WDP style) or an invoice with BPAY and card details (ACL, PathWest style). She pays on her phone. | At booking (or at the lab's registration on test day) the mother gets a link or QR that opens the **lab's own** payment page. She pays the lab directly before or on the day. Variant 2b: the lab is a second merchant on the same screen as the GTT checkout, charged separately in the lab's name (Theodore R18 Q3 point 3). | A terminal owned and run by the lab sits in the collection room. The mother taps her own card after the first draw. A receipt prints or is sent by the lab. |
| What GTT never touches | Money, card details, the lab invoice, non-payment, refunds of the lab fee, the lab's patient contact details (the lab takes them itself) | Money and card details. GTT only displays a lab-owned link (2) or nothing (2b if the lab hosts) | Money and card details, if GTT staff do not operate the terminal |
| Card fees GTT pays | A$0 | A$0 | A$0 |
| Part IIBA risk (library) | **Lowest.** No benefit moves to GTT. "Benefit" is wide: "money, property or services ... actual or potential" (s 23DZZID). A lab benefit to a requester or someone connected is prohibited unless a permitted benefit under s 23DZZIF(2) to (6). Here the lab's billing is the lab's own work for itself, so GTT receives nothing. Keep it that way: no discount, credit, free software or fee from the lab for passing clients (s 23DZZIF(7)(a): never tied to the number of requests). | **Low to medium.** Same rule. Watch: a payment page or widget built by the lab for GTT's site is a "service" to GTT; it must be paid for at market value (s 23DZZIF(6)) or stay the lab's own page that GTT only links to. Pre-payment also puts refunds on the lab if the midwife issues no request. | **Highest.** The room is used by GTT Medical, which is a requester (it employs the midwife; library REFERRAL section 2.3, s 23DZZIE(1)(b), (c)). Lab "equipment at premises of the beneficiary" is excluded from permitted benefits when provided "for the purpose of providing pathology services" (s 23DZZIF(7)(b)). Whether a payment terminal counts is **not answered in the library: question C-b for Catherine.** If GTT staff operate it, GTT becomes the lab's payment agent, the thing Anthony wants to avoid. |
| What the lab must agree to | Bill GTT-collected samples after testing by text/secure link or invoice (it already does for doctor-collected samples); provide a registration form or QR for the mother; one fixed fee for GTT clients (A$27.85, or A$25.85 if collection is 73928); accept non-payment as its own risk; issue a receipt; say whether it can lodge the Medicare claim for the mother (ACL page says it can); no card surcharge | Host a pay page tied to a booking reference; accept prepayment and refund if no request is issued; no surcharge; receipt | Supply, insure and maintain a terminal; agree to unattended tap-to-pay; put up with a payment point in someone else's room; settle any Part IIBA advice |
| What the mother sees | Fee shown at booking. A text from the lab a few days after the test with a link. She pays in under a minute, gets a receipt, claims Medicare. | A pay button or QR at booking or on test day. She pays once, before the test. She keeps the receipt for Medicare. | A tap-to-pay on the day while she is already seated. |
| Main weakness | The lab carries the chance she does not pay. A lab may ask for payment before the test instead. | Pre-payment before the midwife has issued the request: the lab must refund if there is no test. Two payment steps for the mother. | Highest legal doubt and the highest ask of the lab. |

### Recommendation

1. **Ask the lab first whether it will bulk-bill the test.** That is Anthony's number one priority (Medicare bulk-billing or a client rebate). If it does, the lab accepts the assignment as full payment (s 20A, library section 3.5), receives the benefit itself, and the mother pays the lab A$0. Her net on Package 1 would be A$272.15 minus the A$32.95 consult rebate, A$239.20 (my arithmetic on Theodore R18 numbers). All billing logistics then vanish.
2. If not, **Option 1** is the primary. It uses a process each lab already has and puts no step, no data and no money through GTT.
3. **Fallback: Option 2**, in its simplest form (the lab's QR on the lab registration form at collection, opening the lab's own pay page). This matches Founder Rule 6's backup ("client pays the lab directly through a link").
4. **Option 3 only if the lab insists and Catherine clears it.**

## 4. Privacy and consent

What the library already holds (Catherine R16 section 6): the Privacy Act 1988 applies to every health service provider whatever its turnover (s 6D(4)(b)); privacy policy (APP 1), collection notice (APP 5), security (APP 11), eligible data breach notification (Part IIIC).

What it does not hold: APP 6 (use or disclosure of personal information) and APP 8 (cross-border) as applied to GTT passing booking details to a lab, and what consent wording is needed. **Question C-a for Catherine.**

Design that avoids the problem: in Option 1 GTT passes the lab **nothing at booking**. The lab already receives the mother's name and address on the request (Regulations s 34) and takes her mobile and email from its own form on test day. GTT's phlebotomist only hands her the lab's form. If Catherine says a notice is still needed, the booking page carries a one-line APP 5 notice: "[Lab] will bill you directly for the pathology fee and will collect the contact details it needs from you on the day".

## 5. First-call lab questions (written, by email only, after the lab names a contact; Anthony: emails only)

L1. Will you bulk-bill the pregnancy glucose tolerance test (item 66548) and its collection item for our clients?
L2. If not, will you bill each client directly after you receive the request and sample, by text or email link, as you already do for samples collected by a doctor?
L3. What fee do you charge the client for test plus collection (A$27.85 with item 73938, A$25.85 with 73928; AskMBS is being asked which item applies)?
L4. Will you supply a registration and payment-consent form, paper and QR, that the client completes herself at collection?
L5. Do you add any card surcharge? Which payment channels do you offer (card link, BPAY, phone)?
L6. Can you lodge the Medicare claim for the client, or only give her a paid receipt?
L7. Who carries the risk if a client does not pay, and do you require prepayment?
L8. If the midwife issues no request after the consult, or the client does not attend, what do you refund and when?

## 6. Questions for Catherine (W6, precise)

C-a. Privacy Act APP 6 and APP 5: does GTT need the client's written consent to pass booking details (name, mobile, email, test date) to the partner lab, and what is the minimum wording? Is it enough that the lab collects its own details on its own form and GTT passes nothing?
C-b. Part IIBA: where the room is a GTT Medical practice room (not an approved collection centre), does a lab-owned payment terminal, QR sign or lab-built payment widget count as "equipment" or "services" provided to a person connected to a requester (ss 23DZZID(1), 23DZZIF(6), (7)(b))? And does GTT staff handing a client the lab's form, or displaying the lab's pay link on GTT's site, count as a benefit in either direction?

Both already assume the structure Catherine locked in R16 (GTT Medical employs the midwife and collectors; Lounge sells the package).

## 7. Honest gaps

- Saturn's billing text and WDP's rebate page content: not read.
- The Services Australia claim pages timed out on my fetch; the claim steps come from Catherine's verified file.
- Whether each lab will agree to Option 1 for a non-ACC, GTT-collected setting: unknown until asked.
- Collection item 73928 versus 73938 changes the lab fee between A$25.85 and A$27.85 (AskMBS question, answer 8).
- GST: not examined here; Theodore treats the lab fee as the lab's own GST-free supply.
