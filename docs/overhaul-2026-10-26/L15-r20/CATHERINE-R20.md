# CATHERINE R20: legal views on checkout pricing, the Medicare note, cancellations, the paper register and same-day consults

Author: Catherine (Legal Consultant, GTT Center Perth). Date: 2026-10-26 (Round 20, Window 6). DRAFT for Anthony. Nothing was sent or published. All money in Australian dollars (A$).

This is a plain English legal view, not formal legal advice. Where a human lawyer must confirm a point, it says **lawyer to check**.

**How to read the tags**

| Tag | Meaning |
|---|---|
| **V** | I read the law itself this round (legislation.gov.au, 2026-10-26). Saved word for word in the legal library: `r20/ACL-PRIVACY-PRICING-TERMS-R20.md` |
| **L** | Already checked word for word in an earlier library file (file named) |
| **S** | Secondary source, such as a court summary or a business web page, not the law itself |
| **U** | My reading or general knowledge. Not checked against a primary source |

**Plain words used below**

| Word | Meaning |
|---|---|
| ACL | Australian Consumer Law (Schedule 2 of the Competition and Consumer Act 2010, Cth) |
| HIA | Health Insurance Act 1973 (Cth), the Medicare law |
| Part IIBA | The part of the HIA that bans kickbacks between pathology labs and the people who order tests |
| Requester | The person who orders a test, or a business that employs one. GTT Medical is a requester because it employs the midwives (HIA s 23DZZIE(1)(b), L) |
| APP (privacy) | Australian Privacy Principle, a rule in Schedule 1 of the Privacy Act 1988 (Cth) |
| Request or referral | The midwife's written pathology request for the glucose test (item 66548) |
| Standard form contract | Terms the business writes and the client must take or leave, like online booking terms |

---

## 0. Three flags to fix first

| # | Flag | Why it matters | Fix |
|---|---|---|---|
| F1 | **The "I have a referral" choice does not work for a test at GTT under the locked structure.** | Medicare only pays for the lab test if the sample is collected in one of the ways listed in HIA s 16A(5AA). GTT's phlebotomists can collect only "on behalf of the treating practitioner" when that practitioner is employed by the same business (s 16A(5AA)(c)(iv), L: HIA-SECTION-16A.md). An outside GP or obstetrician is not employed by GTT Medical, and the GTT room is not an approved collection centre (s 16A(5AA)(d)). So a test collected at GTT on an outside request gets no Medicare benefit, and GTT would also have to give the "no Medicare benefit" warning (s 23DNL, L). Catherine R15 C3 reached the same answer (L). | Every client tested at GTT needs a request from a GTT midwife after a genuine consult. A client who already holds an outside request may still choose a GTT consult and a GTT request; only one test is done (Catherine R14b item 5, L). See Question 1. |
| F2 | **The lab fee and the lab rebate do not come from the same collection item.** | A$27.85 is the schedule fee for 66548 (A$19.90) plus collection item 73938 (A$7.95). A$22.05 is the rebate for 66548 (A$16.95) plus collection item 73928 (A$5.10) (L: REFERRAL-TELEHEALTH-BILLING-MECHANICS.md 3.1; Catherine R13 row 5). If 73938 applies, the lab rebate is A$23.75 and the total is A$56.70. If 73928 applies, the schedule lab fee is A$25.85. The checkout cannot show both A$320 and A$55.00 as exact. | Keep the word "about" on every rebate, get the lab's fee in writing before launch, and update the page once AskMBS answers. Stating a rebate a little low is safer than stating it high. See Question 2. |
| F3 | **Midwives now start at 08:00 but draws start at 07:00.** | The written request must exist before the sample is collected (s 16A(3)(a), (4), L). A client whose first draw is before her same-day consult can have finished cannot have a same-day consult. | The booking engine should offer a same-day consult only when it ends before that client's first draw, with a small buffer. See Question 6. |

---

## 1. Checkout shows the full A$320 (or A$370) but GTT charges only A$292.15 (or A$342.15)

**Verdict: lawful, and the safest way to show it, if A$320 is the biggest number on the page and the lab's part is clearly labelled as billed later by the lab. No Part IIBA problem from showing the lab fee, as long as the lab gives GTT nothing in return.**

### 1.1 The rules

| Rule | What it says (short) | Tag |
|---|---|---|
| ACL s 48(1) single price | If a business states an amount that is "a part of the consideration" for a consumer service, it must also state, "in a prominent way and as a single figure, the single price" | V |
| ACL s 48(5) prominence | The single price must be "at least as prominent as the most prominent of the parts" | V |
| ACL s 48(7) what the single price is | "the minimum quantifiable consideration for the supply ... at the time of the representation", including GST and other unavoidable charges | V |
| ACL s 18 | No conduct that is "misleading or deceptive or is likely to mislead or deceive" | V |
| ACL s 29(1)(i) | No "false or misleading representation with respect to the price of goods or services" | V |
| Drip pricing (from 1 July 2027) | New ACL s 48A: when a base price is shown, any extra charge payable at the same time must be shown next to it, clearly. New s 28B bans "unfair trading practices", including "failing to disclose material information" or giving it in an "unclear ... or untimely" way (Unfair Trading Practices Act 2026, commences 1 July 2027) | V |

### 1.2 How the rules apply

| Point | View | Tag |
|---|---|---|
| Is the lab fee part of GTT's price? | Strictly, the A$27.85 pays for a different service (the lab's test) from a different business. But the booking page sells "your GTT morning", which includes the test. Whichever reading a court took, showing **A$320 as the headline** satisfies s 48. Showing A$292.15 as the headline with A$27.85 in small print would risk s 48(5) on the wider reading. | U, built on V text |
| Is A$320 the "minimum" price? | Only if the lab's fee really is A$27.85 for every GTT client and nothing else is added. If the fee could be A$25.85 (flag F2), A$320 slightly overstates it. Overstating is a smaller risk than understating, but still a price statement that must be true (s 29(1)(i)). Get the fee in writing from the lab before launch. | U |
| Card surcharge | GTT absorbs card fees in the Center of Truth, so no surcharge applies. If a surcharge is ever added, it must be shown. The new s 48A treats payment surcharges separately (s 48A(8)(b)). | V (text); policy from repo |
| GST | Say "GST included" for the lounge part and "GST-free" for the consult. | U |
| The two companies | The consult is supplied by GTT Medical and the lounge by GTT Lounge. The receipt should show both, with the consult listed as a midwife service by GTT Medical, so the client can claim Medicare on it. | U |
| "All-inclusive" | Safe only next to A$320, and only if A$320 is truly everything she pays. Do not use it next to A$292.15. | U |

### 1.3 Part IIBA (lab fee shown next to GTT's price)

| Point | View | Tag |
|---|---|---|
| Does showing the fee create a benefit for GTT? | No, on its own. Part IIBA bans a lab giving a "benefit" ("money, property or services ... actual or potential", s 23DZZID) to a requester or anyone connected to one, unless it is a permitted benefit (s 23DZZIF). GTT printing the lab's own fee is GTT's own conduct; nothing flows from the lab. | L (HIA-PATHOLOGY-REQUESTS-AND-ARRANGEMENTS.md), U application |
| Who is caught | GTT Medical is a requester (s 23DZZIE(1)(b)). GTT Lounge and GTT Holdings are related companies, so they are "connected" (s 23DZZIJ(1)(d)). A benefit given to the Lounge counts. | L |
| Where the risk would start | (a) the lab pays or credits GTT anything for the listing or for sending clients; (b) the lab gives GTT clients a price lower than its normal private fee, which could be argued to be a potential benefit to GTT; (c) any deal tied to the number of requests (s 23DZZIF(7)(a)). A$27.85 equals the schedule fee (flag F2), which is a normal, not special, price. **Lawyer to check (b).** | L text, U application |
| Free choice of lab | The request must not name a pathologist except on clinical grounds (s 16A(3A), L). The checkout should name the partner lab as the lab GTT uses, not as a lab the client is forced to use under her request. | L, U |

### 1.4 Safe checkout wording (DRAFT, Package 1; for Package 2 use A$370, A$342.15 and A$212.15)

> **Package 1: A$320 total**
> You pay GTT today: **A$292.15**. That is your midwife consult, A$130.00 (GST-free), plus your lounge and services, A$162.15 (GST included).
> Paid later, to the lab: **A$27.85** pathology fee. Our partner pathology lab tests your samples and bills you directly after your test. GTT never receives this money.
> There are no other fees.

Do not write: "only A$292.15", "from A$292.15", "lab fee extra" in small print, or "free lab test".

---

## 2. The Medicare note at checkout

**Verdict: lawful if it is clearly an estimate, says the claim is hers, and does not say "A$55 for your consult". The consult rebate is A$32.95; A$55.00 is the total for consult plus lab.**

| Rule | What it means here | Tag |
|---|---|---|
| HIA s 20(1) | The Medicare benefit is paid "to the person who incurs the medical expenses". The rebate belongs to the client, never to GTT. | L |
| HIA s 20(2) | If she has not paid the account, she gets a cheque made out to the provider instead of money. So she should pay each account in full before she claims. | L |
| ACL ss 18 and 29(1)(i), (m) | No misleading statement about price, or about the "existence ... or effect of any ... right". A rebate figure stated as certain, or stated too high, is the main risk. | V |
| Rebates do not rise with the consult price | Rebates are 85 percent of the schedule fee, not of GTT's price (HIA s 10(2), L). Locked rebates: consult A$32.95 (item 82105), test A$16.95 (66548), collection A$5.10 (73928, AskMBS to confirm). | L, locked |

**Safe wording (DRAFT)**

> **Medicare (estimate).** If you are eligible for Medicare, you can claim about **A$55.00 back in total**: about **A$32.95** for your midwife consult and about **A$22.05** for your lab test. You claim these yourself, after you have paid each account in full. The money goes to you, not to GTT. These amounts are based on the Medicare Benefits Schedule from 1 July 2026. Medicare decides each claim. Your lounge and services are not covered by Medicare.
> After Medicare, Package 1 costs you about **A$265.00** (A$320 less A$55.00). Package 2 costs you about **A$315.00**.

(The A$265.00 and A$315.00 are my arithmetic on the locked figures. Theodore to confirm.)

Do not write: "A$55 back on your consult", "Medicare covers your test" (there is a gap), "no gap", "free", "save A$55", or anything that makes the rebate look like a GTT discount.

---

## 3. Cancellation and no-show (consult attended, test missed or late)

**Verdict: a fee for missing the test is lawful if it is clear, fair, matched by GTT's own duties, and roughly in line with GTT's real loss. The plan of keeping 50 percent of the lounge amount and charging the full lounge amount to rebook can be lawful. The consult fee may be kept because the consult was delivered. Anthony picks the percentage; these are the legal limits.**

### 3.1 The rules

| Rule | What it says (short) | Tag |
|---|---|---|
| ACL s 23(1) | An unfair term in a standard form consumer contract is void | V |
| ACL s 23(2A), (2C) | Proposing an unfair term, or relying on one, is itself a contravention, with a money penalty (s 224, amounts not read this round) | V |
| ACL s 24(1) | A term is unfair if it causes "a significant imbalance", is "not reasonably necessary" to protect the business's "legitimate interests", and would cause detriment | V |
| ACL s 24(3), (4) | A term must be "transparent": plain language, legible, clear, readily available. The business must prove the term is reasonably necessary | V |
| ACL s 25 | Examples of unfair terms include (c) penalising only one party for a breach, and (h) letting one party alone decide whether the contract was breached | V |
| ACL s 26(1)(b), (2) | The upfront price is not tested for fairness, but a charge "contingent on the occurrence ... of a particular event" is. A missed-test fee is contingent, so it **is** tested | V |
| ACL s 27 | Online booking terms are presumed to be a standard form contract | V |
| ACL ss 60, 62, 64 | GTT must supply services with due care and skill and on time. These guarantees cannot be excluded by the terms (s 64) | V |
| ACL s 29(1)(m) | Do not misstate her rights, for example "no refunds in any circumstances" | V |
| Penalties rule (court-made law) | The High Court held that bank late fees were not penalties because they protected the bank's legitimate interests, even though they were "not genuine pre-estimates of damage" and were "disproportionate to the actual loss" (Paciocco v ANZ [2016] HCA 28, High Court summary) | S (summary only, full reasons not read) |
| New from 1 July 2027 | ACL s 28B: no design that puts a client "under unreasonable pressure" or hides "material information" | V |

### 3.2 How the rules apply to Anthony's plan

| Part of the plan | View | Tag |
|---|---|---|
| Consult fee kept when the consult happened | Lawful. The service was supplied. A GST-free medical service already delivered is not refundable just because a later test was missed. | U, on V guarantees |
| Request reused on rebooking | The request does not expire under the Act (section 6a). If she rebooks within GTT's 28-day window and the same pregnancy, she should not be charged a second consult. A second consult is only proper if a genuine new consult is needed (for example, past 28 days, or a different midwife). Charging for a consult that is not needed risks s 29(1)(l) ("the need for any goods or services"). | V (s 29), U application |
| 50 percent of the lounge amount kept | Lawful if GTT can show a legitimate interest: rostered staff already paid (casual minimum engagements), a fasting test slot booked days ahead that cannot be resold the same morning, consumables. Package 1: half of A$162.15 is A$81.075; state the rounding (A$81.08). Package 2: A$106.08. | V test, U application |
| Full lounge amount paid again to rebook | Lawful as a new purchase, but the terms must show the total effect plainly. Example to print: "If you miss your test, we keep A$81.08. To rebook you pay A$162.15 again." Hiding the combined effect fails transparency (s 24(3)). | V test, U |
| Is 50 percent "too generous"? | Legally, less is always safer than more. A lower figure, or 50 percent, is easier to defend than 100 percent. 100 percent of the lounge amount for a no-show is the highest-risk choice unless GTT's real loss per missed slot is close to the full amount. **Ask Theodore to price the real cost of one missed slot**; that number is GTT's legal defence. | U |
| What other businesses do | One verified example: endota spa's gift card terms say "Cancellations within 24 hours of your appointment will result in a cancellation fee being charged" (amount not stated; endota.com.au/terms-and-conditions, read 2026-10-26). Its full cancellation page returned an error (403). I did not research industry percentages further. Grace can benchmark. | S |
| "Late" must be defined by the clock | A rule like "late at our discretion" lets GTT alone decide breach, which is an unfair-term example (s 25(h)). Use an objective test, for example "if you are not checked in by the arrival time on your confirmation". | V (s 25), U |
| GTT's own duty must mirror hers | If GTT, its staff or the lab cannot run the test, she gets a full refund of the lounge amount or a free rebook, her choice. Otherwise the term penalises only her (s 25(c)), and the guarantees apply anyway (ss 60, 62, 64). | V |

### 3.3 Exceptions the terms should contain

No section lists these. They are what keeps the term from being "not reasonably necessary" (s 24(1)(b)). U, lawyer to check.

| Exception | Outcome I recommend |
|---|---|
| She is unwell (fever, vomiting, infection) | Free rebook or full lounge refund |
| Pregnancy complication, or a doctor or midwife advises her not to do the test | Free rebook or full lounge refund |
| Hospital admission, labour or birth | Full lounge refund |
| GTT's midwife decides after the consult that the test is not right for her | Full lounge refund (no test can be supplied) |
| The test is stopped under the lab's rules after she arrived (for example she vomits the glucose drink) | Free rebook |
| GTT, its staff or the lab cannot run the session | Full lounge refund or free rebook, her choice |
| Serious family emergency or bereavement | Free rebook (recommended, not required by a section) |
| Not fasted when she arrives | Not an exception if the fasting rule was made clear at booking and in the reminder. Treat as a missed test. |

Ask for "reasonable evidence" only where needed, and collect the least health information possible (APP 3, section 4).

### 3.4 Notice windows and wording (DRAFT, numbers for Anthony)

| Step | Safest practice | Tag |
|---|---|---|
| Free change window | Free cancel or reschedule up to a stated time before the test (Question 3) | U |
| Reminders | Send a reminder before the window closes and the evening before, repeating the fasting rule and the arrival time | U |
| Where the term appears | On the checkout page above the pay button, with a tick box, and in the confirmation email. Not only in a linked document | V (s 24(3)) |
| Wording | "If you attend your consult but miss your test, or arrive after the arrival time on your confirmation, we keep half your lounge amount (A$81.08 for Package 1) and refund the other half. To rebook, you pay the lounge amount again. Your consult fee is not refunded because your consult took place. None of this applies if you are unwell, have a pregnancy complication, are in hospital or in labour, if our midwife or the lab advises you not to do the test, or if we cannot run your session. Then you can rebook free or get a full refund of your lounge amount. Your rights under the Australian Consumer Law are not affected." | U, lawyer to check |

---

## 4. The paper register (weekly folder, one pocket per test day, copies of referrals)

**Verdict: lawful only with tight controls, and it is the weakest part of the plan. A scanned or electronic copy in the clinical record, printed on the test morning, does the same job more safely. Recommended replacement.**

### 4.1 The rules

| Rule | What it says (short) | Tag |
|---|---|---|
| Privacy Act applies whatever GTT's size | Every health service provider is covered (s 6D(4)(b)) | L (Catherine R16) |
| A referral is health information | Includes "information ... about ... a health service provided, or to be provided" and other personal information "collected to provide ... a health service" (s 6FA(a)(iii), (b)) | V |
| APP 3.3 | Sensitive information (health information is sensitive) needs consent to collect, unless an exception applies (s 16B(1): necessary for a health service and collected under professional confidentiality rules) | V |
| APP 5 | At or before collection, tell her who holds it, why, who it goes to, and how to complain | V |
| APP 6.1, 6.2 | Use or disclose only for the purpose collected, or with consent, or where she "would reasonably expect" it and it is "directly related" | V |
| APP 11.1 | Reasonable steps to protect it "from misuse, interference and loss" and "unauthorised access" | V |
| APP 11.2 | Destroy or de-identify it once no longer needed, unless a law requires keeping it | V |
| Related companies | Sharing between related companies is allowed for ordinary personal information but **not for sensitive information** (s 13B(1)) | V |
| Lab keeps the original | The lab's pathologist must keep the written request for 2 years from the test (HIA s 23DK(1)) | V |
| Scanned requests | Medicare has a notice under the Electronic Transactions Act 1999 on scanning and storing pathology requests (reproduced in the NPAAC retention requirements, appendix) | L (npaac/NPAAC-RETENTION-LAB-RECORDS-9TH-2022.md) |
| Data breach | A lost folder may be an eligible data breach that must be reported (Part IIIC) | L (Catherine R16) |
| WA rules for private providers | I found no WA law setting privacy or record-keeping rules for private health businesses. WA's Privacy and Responsible Information Sharing Act 2024 is, as I understand it, for WA public bodies. Not read this round. **Lawyer to check.** | U |
| How long to keep the clinical record | No Commonwealth or WA law found that sets a period for a private midwife's records. Common practice is at least 7 years from the last entry for an adult. **Lawyer and the professional indemnity insurer to confirm.** | U |

### 4.2 What this means for the folder

| Issue | View |
|---|---|
| The folder copy is a duplicate | The midwife's request is GTT Medical's own document and belongs in the clinical record. The original goes to the lab with the sample, and the lab keeps it for 2 years (s 23DK(1)). So the pocket copy is a spare and should be destroyed once the test is done. |
| One folder holds a week | A single lost folder could expose up to 108 clients (18 a day, 6 days). That is a large breach from one mistake. |
| Who may see it | GTT Medical staff only: the midwives and the phlebotomists on the day. Not lounge or service staff, and not the venue manager unless employed by GTT Medical, because sharing health information between the two companies is not covered by s 13B. |
| Storage | Locked cabinet in the consult room or a locked office, never at reception or in the lounge. Key or code held by Medical staff only. Simple sign-out sheet. |
| Destruction | Shred (cross-cut) or use a locked secure-destruction bin the day after the test, once the system shows the request went with the sample. Keep a one-line destruction log. |

### 4.3 Safer low-tech workaround (recommended)

1. The midwife writes the request in GTT Medical's clinical system, or scans her signed paper request into the client's record straight after the consult.
2. On the test morning, the phlebotomist prints that day's requests from the system (access logged), checks each against the client, and sends each original with its sample.
3. If the system is down, a single sealed envelope for that day only (not a weekly folder) is kept in the locked cabinet as the backup.
4. Booking (Lounge) staff see names and times only, never the request.

### 4.4 Consent and notice wording (DRAFT)

> **Your privacy.** GTT Medical Services Pty Ltd collects your health information to provide your midwife consult and glucose test. GTT Lounge Sanctuary Pty Ltd collects your name, contact details and booking times to provide your lounge and services. Only our midwives and phlebotomists see your pathology request and health details. We keep a copy of your request in your secure record so your test can go ahead if you forget your paperwork. Your request and samples go to our partner pathology lab, which tests them and sends the result to our midwife. Our privacy policy explains how to see or correct your information and how to complain.
> ☐ I agree to GTT Medical sharing my booking details with GTT Lounge, and to GTT sharing the details below with the partner pathology lab for my test and its billing.

---

## 5. Same-day consult before the test

**Verdict: lawful. No law sets a minimum time between a request and the collection. The written, dated request must exist before the first draw.**

| Point | View | Tag |
|---|---|---|
| Any waiting period? | None in HIA s 16A or Regulations ss 32 to 37. A request must be in writing (or oral and confirmed in writing within 14 days) and contain the set details (s 16A(4)) | L (REFERRAL-TELEHEALTH-BILLING-MECHANICS.md 1.1; HIA-SECTION-16A.md) |
| Must the request come first? | Yes. Medicare pays only if the test "was rendered pursuant to a request made by the treating practitioner" (s 16A(3)(a)). The midwife must also have "determined" the test "to be necessary" (s 16A(1)(aa)). So the consult ends, the request is signed and dated, and only then is the fasting sample taken | L |
| Booking the test before the consult | Lawful, but the page must say the test goes ahead only if the midwife decides it is right for her. Otherwise it could imply a need that has not been assessed (ACL s 29(1)(l)) | V, U |
| Fasting | The booking page warning (stay fasted for the consult) is a clinical and consumer point, not a legal requirement, and it must be prominent | U |
| Midwife start time | See flag F3 | |
| Consult and test on the same day for Medicare | I found no rule stopping a midwife consult item and a pathology request on the same day. Not checked for item 82105 itself. **AskMBS to confirm.** | U |

Wording (DRAFT): "You can see our midwife the same morning, before your test. Stay fasted: water only. Your test goes ahead only if our midwife decides it is right for you."

---

## 6. Earlier open questions

### 6(a) How long does a pathology request stay valid for item 66548?

**Verdict: the law sets no expiry. GTT's 28-day rule sits safely inside the law.**

| Point | View | Tag |
|---|---|---|
| The Act | s 16A(4) requires writing and the set details. It contains no time limit | L (Catherine R14b 4.4) |
| Medicare's general view | Quoted by a lab: "A written pathology request, in general, remains valid regardless of the time period"; once used, it is spent | S (Catherine R14b) |
| Lab policy | Some labs ask for a fresh request for time-sensitive tests and name the glucose test as one | S (Catherine R14b) |
| Same pregnancy | The request is for this pregnancy only | U |
| Do not mix up | The 12-month rule for a midwife's referral is about referrals to specialists (Regulations, referral validity), not pathology requests | V (regs text) |
| Trap | If the midwife who wrote the request leaves GTT before the test, collection on her request may no longer fit s 16A(5AA)(c)(iv). Another GTT midwife then does a consult and re-requests | L (Catherine R14b) |
| Action | Ask the partner lab, in writing, to confirm it accepts GTT requests up to 28 days old | U |

### 6(b) Privacy consent to pass booking details to the partner lab

**Verdict: the request and sample going to the lab is the main purpose and needs only a clear notice. Passing extra booking details (mobile, email, test date) so the lab can bill her should have her express consent. Safest of all: pass nothing extra, and let the lab collect its own details on its own form.**

| Point | View | Tag |
|---|---|---|
| Request and sample to the lab | The whole point of the test. Covered as the main purpose, or as a directly related purpose she would expect (APP 6.1, 6.2(a)(i)). The APP 5 notice must name the lab or the type of body (APP 5.2(f)) | V |
| Extra details for billing | Probably within APP 6.2(a), but a tick box removes doubt | V text, U application |
| Medicare number | A government identifier with its own rule (APP 9), not read this round. Let the lab collect it directly | U |
| Overseas booking software | If the booking system stores data overseas, APP 8 applies (not read). **Lawyer to check** with the chosen provider | U |

Wording (DRAFT, add to the tick box in 4.4): "With your agreement, we give our partner pathology lab your name, date of birth, mobile number, email and test date so it can register you and send you its bill."

### 6(c) Part IIBA view on the three lab billing options (Grace R19 question C-b)

**Verdict: Option 1 (lab invoices after it receives the request and sample) is the lowest risk. Option 2 (lab payment link) is low risk if the page is the lab's own. Option 3 (lab terminal in the collection room) is the highest risk and should be avoided.**

| Option | Part IIBA view | Tag |
|---|---|---|
| 1. Lab invoices her after the test | Nothing passes from the lab to GTT. The lab bills for its own service with its own system. No benefit to a requester (ss 23DZZID, 23DZZIF) | L text, U application |
| 2. Lab payment link | A plain link to the lab's own page is GTT's conduct, not a benefit from the lab. A widget, page or software built by the lab for GTT's site is a "service" to GTT and is only permitted at market value (s 23DZZIF(6)) | L text, U |
| 3. Lab terminal in the GTT collection room | "Staff or equipment at premises of the beneficiary for the purpose of providing pathology services" is never a permitted benefit (s 23DZZIF(7)(b)). A payment terminal arguably serves the lab's pathology business, and it saves GTT the cost of handling payment. If GTT staff operate it, GTT also becomes the lab's payment agent. **Lawyer to check; avoid** | L text, U |
| GTT staff handing her the lab's form | This is GTT doing a small task for the lab, which is the other direction. Part IIBA's ban is on benefits to requesters. It stays safe only if the lab pays GTT nothing for it, and nothing is tied to the number of requests (s 23DZZIF(7)(a)) | L text, U |

---

## 7. Sources read this round

| Source | Where | Tag |
|---|---|---|
| ACL ss 18, 23 to 27, 29, 48, 60 to 64 (CCA 2010 Sch 2, compilation 16 September 2026) | legislation.gov.au C2004A00109, volume 4 | V |
| Unfair Trading Practices Act 2026 (No. 64, 2026): new ss 28B, 48A; commencement 1 July 2027 | legislation.gov.au C2026A00064 | V |
| Privacy Act 1988 ss 6FA, 13B, 16B(1), APP 3, 5, 6, 11 (compilation 4 June 2026) | legislation.gov.au C2004A03712 | V |
| HIA s 23DK(1) (Compilation No. 136) | legislation.gov.au C2004A00101 | V |
| Health Insurance Regulations 2018, referral validity text | legislation.gov.au F2018L01365 (1 July 2026) | V |
| Paciocco v ANZ [2016] HCA 28, High Court judgment summary | hcourt.gov.au | S |
| endota spa terms and conditions (gift card clause) | endota.com.au/terms-and-conditions | S |
| Library: HIA-SECTION-16A.md, HIA-PATHOLOGY-REQUESTS-AND-ARRANGEMENTS.md, REFERRAL-TELEHEALTH-BILLING-MECHANICS.md, npaac/NPAAC-RETENTION-LAB-RECORDS-9TH-2022.md, r13, r14b, r15, r16 | /opt/openclaw/second-brain/knowledge/legal/ | L |

**Not read (honest gaps):** ACL s 224 penalty amounts; APP 8 and APP 9; Health Practitioner Regulation National Law s 133 (advertising health services); WA Privacy and Responsible Information Sharing Act 2024; the full Paciocco reasons; ACCC and OAIC guidance pages (ACCC returned 403; the OAIC health records page returned 404); any MBS rule on item 82105 and a request on the same day; industry cancellation percentages.

---

## QUESTIONS FOR ANTHONY

1. **The "I have a referral" choice (flag F1).** An outside request cannot be used for a test collected at GTT.
   - (a) Every test booking includes a GTT midwife consult. A client with an outside request brings it to the consult as background. **(Recommended.)**
   - (b) Keep "I have a referral", but send those clients to a lab collection centre for the test, outside the lounge package.
   - (c) Later, ask the partner lab to run its own approved collection room inside GTT so outside requests can be collected there (needs Services Australia approval).

2. **Lab fee and rebate (flag F2).** Until AskMBS says 73928 or 73938:
   - (a) Show A$320 and "about A$55.00" now, get the lab's fee in writing, and correct the page when AskMBS answers. **(Recommended.)**
   - (b) Show the lab fee as "A$25.85 to A$27.85, set by the lab".
   - (c) Hold the checkout page until AskMBS answers.

3. **Free change window before the test.**
   - (a) 24 hours.
   - (b) 48 hours, with reminders before it closes. **(Recommended: gives clients time to plan fasting, and gives GTT a clear line.)**
   - (c) 72 hours.

4. **The missed-test percentage** (legal limits in 3.2; the choice is yours).
   - (a) Keep 50 percent of the lounge amount. **(Recommended, if Theodore's cost of one missed slot is at or above A$81.08.)**
   - (b) Lower it, for example 25 percent, if the real cost is lower.
   - (c) 100 percent for a no-show. Not recommended: highest legal risk.

5. **What counts as "late".**
   - (a) Not checked in by the arrival time on her confirmation. **(Recommended: clear and objective.)**
   - (b) Not checked in by the start of her draw slot.
   - (c) Staff decide on the day. Not recommended (ACL s 25(h)).

6. **Same-day consults with an 08:00 midwife start (flag F3).**
   - (a) The booking engine offers a same-day consult only when it ends before her first draw, with a buffer. **(Recommended.)**
   - (b) Start one midwife earlier on test days.
   - (c) No same-day consults for draws before a set time.

7. **The paper register.**
   - (a) Replace it with the scanned or system copy, printed on the test morning (section 4.3). **(Recommended.)**
   - (b) Keep the weekly folder with every control in 4.2.
   - (c) Use both for the first 3 months, then drop the folder.

8. **A health lawyer's sign-off on the booking terms, privacy notice and checkout page before launch.** Cost: NOT IN REPO.
   - (a) Yes, one fixed-fee review before launch. **(Recommended.)**
   - (b) Only the cancellation and privacy terms.
   - (c) No review.

Regards.
Catherine
