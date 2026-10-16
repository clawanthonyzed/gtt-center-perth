# s38-10 GST Structure for GTT Packages (L5, P20d)

Prepared 2026-10-16 by Grace for Theodore (CFO), the accountant and the solicitor. This is research and a draft structure, not tax advice. Every conclusion marked TO CONFIRM must be settled by the accountant, and ideally by an ATO private ruling (see ACCOUNTANT-ATO-PRIVATE-RULING-BRIEF.md).

## 1. Plain answer (read this first)

Anthony's instruction: make Component A (clinical phlebotomy and specimen handling) 100% GST-free under s38-10 and shield the majority of the package from GST.

What the law actually says, from the sources in section 2:

1. **s38-10 does not cover phlebotomy.** It is a closed table of 21 listed health services (acupuncture, nursing, paramedical, physiotherapy and so on). Blood collection by a phlebotomist is not on the table, and a phlebotomist is not a "recognised professional" in any listed service. The ATO states the service "must be one of the listed services and cannot just be similar".
2. **The GST-free pathology service is the laboratory's supply under s38-7 (medical services).** The GTT test is billed to Medicare by the lab. A collector working for the lab is covered by the lab's GST-free supply only where the service is billed in the name of the lab and the lab accepts full responsibility (ATO medical services guidance, nurse-takes-blood example). That is the lab's supply to the patient, not GTT's.
3. **GTT's own supplies are different.** GTT sells the lounge, wellness treatments and refreshments (taxable). If GTT charges the lab for collection staff or room use, that is a supply to a business, and the ATO says health services supplied to a third party other than an insurer, compensation scheme or Australian Government agency are not GST-free. So it is taxable.
4. **Splitting a package price to push most of it into a "clinical" line is the pattern the ATO warns about.** GSTR 2001/8 requires a fair and reasonable valuation, rejects contrived allocations (paras 81ZD, 96 and Example 13B), and Division 165 can cancel a GST benefit from a scheme whose dominant purpose is the GST saving.

Result: the structure Anthony described (a large GST-free Component A inside a GTT invoice) is **not available as framed**. The closest legal version is in section 4. The repo's own GST-stress case (whole package taxable) is the correct planning base, and is consistent with the cash-flow document, which reached the same view earlier.

**Risk rating**

| Version | Rating | Why |
|---|---|---|
| As framed: GTT invoices a GST-free "clinical phlebotomy" component and shields most of the package | HIGH. Do not adopt | No listed profession, GTT is not the pathology supplier, contrived allocation, Division 165 exposure, penalties and interest on every package sold |
| Recommended: clinical pathology stays on the lab's own bill; GTT invoices only its own taxable supplies; GST managed through input tax credits and GST-inclusive pricing | LOW | Matches the law as written; nothing to defend |
| Variant: collection by an AHPRA registered nurse, charged by GTT as a "nursing service" (item 10) | MEDIUM to HIGH. Ruling needed first | Arguable only; the same collection is already paid through the lab's Medicare billing, so charging again risks double charging |

## 2. Sources (retrieved 2026-10-16)

- GST Act s38-7 and s38-10: https://www.ato.gov.au/law/view/document?docid=PAC/19990055/38-7 and https://www.ato.gov.au/law/view/document?docid=PAC/19990055/38-10
- s195-1 definition of "medical service": https://www.ato.gov.au/law/view/document?docid=PAC/19990055/195-1
- ATO, Other health services: https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/in-detail/your-industry/gst-and-health/other-health-services
- ATO, Medical services: https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/in-detail/your-industry/gst-and-health/medical-services
- ATO, Supply of services through a third party: https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/in-detail/your-industry/gst-and-health/supply-of-services-through-a-third-party
- ATO, Appropriate treatment: https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/in-detail/your-industry/gst-and-health/appropriate-treatment
- GSTR 2001/8: https://www.ato.gov.au/law/view/document?docid=GST/GSTR20018/NAT/ATO/00001
- s9-80: https://www.ato.gov.au/law/view/document?docid=PAC/19990055/9-80
- Division 165, ss165-5 and 165-10: https://www.ato.gov.au/law/view/document?docid=PAC/19990055/165-5 and https://www.ato.gov.au/law/view/document?docid=PAC/19990055/165-10

Note: the three operative paragraphs of s38-10(1) did not extract cleanly. They are taken from the ATO page: a listed service, performed by a recognised professional (or assistant), generally accepted in that profession as necessary for the appropriate treatment of the recipient. TO CONFIRM against the Act text.

## 3. The key questions

**Is blood collection by a GTT-employed phlebotomist GST-free under s38-7 or s38-10?**
No, not in GTT's hands on the facts we hold. s38-10 has no phlebotomy item and a phlebotomist is not a recognised professional. Under s38-7 the GST-free supply is the lab's medical service. The ATO "on behalf of" test needs the service billed in the lab's name, the lab accepting full responsibility, and the lab being involved in at least part of the service. A GTT employee is not the lab's employee, so even that route is doubtful (the Medicare collector rule in PATHOLOGY-LICENSING-AND-ACCREDITATION.md points the same way).

**Is the GST-free pathology service the lab's Medicare-billed supply?**
Yes. GTT earns zero pathology revenue and the partner bills Medicare (pathology-partnership-brief.md, pricing-billing-strategy.md).

**What part of a GTT package can legitimately be GST-free?**
On the current model, none of GTT's own charges. Conditions under which something could be, each needing the accountant:
1. A nursing service (item 10) delivered by an AHPRA registered nurse, separately priced and itemised, generally accepted in nursing as necessary for the appropriate treatment of the client, and not already paid through Medicare (otherwise it is a double charge). TO CONFIRM that doctor-requested specimen collection counts as nursing treatment of the recipient.
2. Pass-through of the lab's private fee for a non-Medicare client: the lab is the supplier, sets the price and issues its own receipt, and GTT is a disclosed agent earning only a taxable commission. The lab fee is not GTT revenue.
3. Goods supplied during a GST-free health service (s38-7(3)) apply to the lab's service, not to GTT's lounge.

**How must a split be valued so it is defensible?**
GSTR 2001/8: any reasonable method supported by the facts, chosen on the circumstances and not because of the result (para 95). Direct method: the price GTT charges when each part is sold alone (market value). Indirect method: cost plus a consistent margin (para 109). Cost alone is not reasonable if margins differ between parts (para 112). Historical cost and residual value are generally not acceptable (para 113). Giving a real service nil or token value is a contrivance (paras 81ZD and 81ZH, Example 13B, where a doctor charged only the GST-free drug and nothing for the taxable procedure).

**What would make it fail?**
- No listed profession, or no registration, for the person performing the service.
- A GST-free label placed on something GTT does not supply (the lab does).
- A "clinical" line priced well above market value while lounge and wellness carry token amounts.
- The same collection paid twice (Medicare and the client).
- A package sold as one experience: the ATO may treat it as a single composite supply taxed in full (GSTR 2001/8 paras 41 to 66).
- No evidence: no separate price list, no records, no practitioner registration on file.
- Division 165: dominant purpose of the allocation is the GST saving.

## 4. Recommended structure (most favourable legal design)

### 4.1 Package component list

| Component | Supplier | GST status | Invoice |
|---|---|---|---|
| Glucose tolerance test and specimen collection | Pathology partner (lab) | GST-free medical service (lab's supply) | Lab's own bill or Medicare bulk bill. Not on GTT's invoice |
| Wellness Lounge access and wellness service (30 or 45 minute window) | GTT | Taxable, 10% | GTT tax invoice |
| Private Refreshment Counter items | GTT | Taxable, 10% (some basic food may be GST-free; accountant to classify each item) | GTT tax invoice |
| Pre-booked afternoon standalone services | GTT | Taxable, 10% | GTT tax invoice |

### 4.2 Legitimate ways to protect net profit
1. Register for GST before the first sale and claim input tax credits on fit-out, equipment, supplies, rent GST and professional fees (financial-model.md says registration is required once trading; accountant to confirm timing and which entity).
2. Price packages GST-inclusive. At the committed price points the GST inside is one eleventh: A$250 contains A$22.73, A$300 contains A$27.27. Margin is set on the ex-GST amount.
3. Any lab payment to GTT (room, collection arrangement) is a taxable supply to a business; the lab can claim credits. Keep it at market value (Medicare rules, see licensing document).
4. Ask the accountant to classify refreshment items individually (some basic food is GST-free).
5. Decide whether any nurse-delivered clinical step is genuinely part of the model. If not, drop the nursing idea.

### 4.3 Invoice layout (GTT tax invoice)

```
TAX INVOICE   [Entity name]   ABN [xx]   Invoice no. [n]   Date [d]
Client: [name]                          Booking ref [ref]

Description                                   Amount (incl GST)   GST
Wellness Lounge and treatment session (30 min)   [price]           [1/11]
Private Refreshment Counter pre-order            [price]           [1/11]
TOTAL                                            [total]           [GST total]
Total includes GST of [x].

The glucose tolerance test is provided and billed separately by [pathology partner].
GTT Center Perth does not bill for pathology. No pathology charge appears on this invoice.
```

If a ruling ever approves a nursing line, it would be a separate line labelled "GST-free nursing service", with the nurse's AHPRA number held on file.

### 4.4 POS and merchant settings (Fresha and EFTPOS)
- One GST-taxable tax code on every GTT item. No GST-free item code unless a ruling is received.
- Separate item categories (Lounge and wellness; Refreshments; Afternoon services) so reports tie to BAS.
- Do not route lab fees through GTT's merchant account. If a non-Medicare client pays a lab fee, the lab collects it directly. Splitting one GTT payment between GST-free and taxable lines is not recommended.
- Full prepayment at booking is the confirmed policy; the GST point arises at the earlier of payment or invoice. TO CONFIRM treatment of refunds and unused prepayments.

### 4.5 Wording for service descriptions
Use: "Wellness Lounge and treatment session", "Private Refreshment Counter pre-order", "Pre-booked wellness treatment". Avoid: "clinical package", "includes pathology", "medical service", "GST-free health package". Marketing may say the glucose tolerance test is "arranged with our pathology partner and billed separately", never that GTT provides it.

### 4.6 Record keeping
- Pathology partner agreement showing the lab bills and is responsible for the test.
- Price list showing each item sold stand-alone (market value evidence).
- Staff register with qualifications and AHPRA numbers where relevant.
- Accountant advice and any ATO private ruling, held for the life of the arrangement plus the standard retention period (accountant to confirm; five years is the usual rule).
- BAS working papers by category.

## 5. Link to the existing GST-stress case
The plan's GST-stress case treats the whole package as taxable (steady state +A$23,442.58 per month against +A$35,186.40 baseline, DECISION-LOG v0.4 entry). Tracker item 7 already asks the accountant whether the AM package is fully taxable or mixed. The recommended structure is the GST-stress case. Treat it as the planning base and any GST-free element a ruling might later allow as upside only.

## 6. Card for Anthony (C2)

**C2: GST and the s38-10 question, in plain English**
- You asked for: the clinical part of the package GST-free, shielding most of the price.
- The law allows: only the pathology lab's own test is GST-free, and the lab bills that itself. A phlebotomist is not on the s38-10 list, and our wellness lounge is taxable.
- So GTT's package is taxable. Our GST-stress numbers already assume that.
- What we do: register for GST, claim back the GST on everything we buy, price GST-inclusive.
- What we do not do: put a big "clinical" price on our invoice to cut GST. The ATO treats that as a contrived split and can penalise every package sold.
- Possible upside: if a registered nurse does a nursing step, that part might be GST-free. Only an ATO private ruling can settle it.
- Risk: framed version HIGH, recommended version LOW.
- Next step: accountant lodges the private ruling (brief is ready).
