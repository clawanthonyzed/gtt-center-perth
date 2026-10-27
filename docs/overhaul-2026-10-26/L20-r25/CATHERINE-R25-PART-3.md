# CATHERINE R25 PART 3: Normal results by text and email, and review of FAQ answers 7 and 11

DRAFT, 2026-10-27. Tags as in PART-1. Nothing is sent or published.

## READ-FIRST CHECK
- Venue manager starts 06:30 (Mon to Fri 06:30 to 15:00); 07:00 is the first draw.
- Path A = PREFERRED (with GTT midwife consult); Path B = NOT preferred (outside referral, no GTT consult).
- Path A A$320 / A$370 (GTT charges A$292.15 / A$342.15); Path B A$300 / A$350 (GTT charges A$272.15 / A$322.15). <!-- factcheck:ok -->
- Rebates about A$55.00 (consult A$32.95 + lab A$22.05). Midwives 08:00 to 16:00, first consult 08:15.
- Late rule: draws no wiggle room; consults 10 minute grace.

## ITEM 3: Answer in one line
A short text and email saying her midwife has reviewed the result and no follow-up is needed is lawful if she ticked consent for that channel at booking. Do not attach the report and do not build a GTT portal before opening. The venue manager may read a normal result to her only from the midwife's written "normal, client may be told" note, after an identity check, using the script below. Path B results never come to GTT.

## The rules
| Rule | Effect | Source |
|---|---|---|
| Health information is "sensitive information" (Privacy Act s 6) | Use and disclose it only for the purpose collected or one she would expect (APP 6) | V library r20 (Privacy Act ss 6FA, APP 6.1 to 6.2) |
| APP 11 | "Reasonable steps" to protect it; "More rigorous steps may be required as the risks and adverse consequences increase" (11.8); encryption listed as a step (11.12); check the person is authorised, without asking for more than needed (11.8) | V https://www.oaic.gov.au/privacy/australian-privacy-principles/australian-privacy-principles-guidelines/chapter-11-app-11-security-of-personal-information |
| Who gets the lab report | The lab reports to the requester. A "copy to" person is "not ... responsible for receiving, acknowledging or acting on" results; follow-up stays with "the requesting practitioner" | V National Pathology Standards 7.03 and footnote 30 (p 39) |
| Path A | Requester = GTT midwife, so she must review every result before any message goes out, and she owns the follow-up | V as above; R locked results rule |
| Path B | Requester = her outside doctor or midwife. GTT receives no result and sends no result message | R (FAQ 13), V Standard 7.03 |
| Who may speak a result | General practice standards expect a written policy on "what information different team members can convey and how to convey it" | V https://www.racgp.org.au/running-a-practice/practice-standards/standards-5th-edition/standards-for-general-practices-5th-ed/general-practice-standards/gp-standard-2/criterion-gp2-2-follow-up-systems (GP standard, used as a guide only) |

## Recommended safe design
1. **Consent at booking** (existing tick boxes in r23-06 consent text): phone, voicemail, email, text. No tick, no message by that channel.
2. **Midwife review first.** She files the result in the computer record and marks it "normal, client may be told". Only then does the system send the notice.
3. **Text and email content:** that the midwife reviewed it and no follow-up is needed. No test values, no word "diabetes", no lab name. Sent from the GTT Medical sender only, to her own number and address.
4. **Attachment:** NO. A PDF in normal email is not encrypted end to end and may sit in a shared inbox. If she asks for her report, she gets it from the lab's own patient service (whether the partner lab has one is NOT IN REPO; ask in the lab outreach) or from her midwife at a visit, or by encrypted email with a password sent by text, after an identity check (lawyer to check).
5. **GTT portal:** not before opening. It needs secure login, two-step checks, audit logs and Australian hosting. Not on the 2-month critical path.
6. **Speaking a normal result:** the midwife, or the venue manager reading the script below. The venue manager never explains, interprets or answers clinical questions; she books the midwife instead. Abnormal results: the midwife only (locked).
7. **Identity check before speaking:** full name, date of birth and test date match the record.
8. **Her usual pregnancy care provider:** the midwife sends the report to the provider she named at the consult, with her consent (the consent question at the consult is NOT IN REPO; add it; lawyer to check).

## Exact notification wording
**Text message (normal result, Path A):**
> Hello {first_name}, your GTT Center Perth midwife has reviewed your glucose test result. No follow-up is needed from us. Questions? Call {gtt_medical_phone}. Regards, GTT Center Perth

**Email, subject "Your GTT Center Perth test":**
> Hello {first_name},
> Your GTT Center Perth midwife has reviewed your glucose tolerance test result from {test_date}. No follow-up is needed from us. Your usual pregnancy care provider will receive a copy if you asked us to send one. If you would like a copy of your report or would like to talk with the midwife, please call {gtt_medical_phone} between {hours}.
> Regards,
> GTT Center Perth

**Phone script (venue manager, normal result only):**
> "Before I go on, may I confirm your full name, date of birth and the date of your test? Thank you. Your midwife has reviewed your result and has asked me to let you know that no follow-up is needed from us. If you have any questions about the result, I can book you a time to speak with the midwife."

Consent text line 12 ("a short message saying a message is ready, with no health detail") does not match this design. Anthony picks one (QUESTIONS in PART-5).

## FAQ review (r23-18-client-faq.md), copied word for word

**Answer 7 as drafted:**
> **7. Will I get money back from Medicare?** On Path A you can claim about A$55.00 yourself (about A$32.95 for the consult and about A$22.05 for the lab test). On Path B a request from outside GTT gets no Medicare benefit for a test done here. Lawyer to check this wording.

Legal comment: "you can claim" is a promise about the future. The ACL needs reasonable grounds (ss 4, 18, 29). The collection item (73928 or 73938) and the government's written view are still open, and the consult rebate needs a midwife with a Medicare provider number. Add the conditions.

**Safe revision 7:**
> **7. Will I get money back from Medicare?** On Path A, if you have a Medicare card, we expect you can claim about A$55.00 back yourself (about A$32.95 for the midwife consult and about A$22.05 for the lab test). Medicare sets the amounts and they can change, so we cannot promise them. On Path B, a request from outside GTT gets no Medicare benefit for a test done here.

**Answer 11 as drafted:**
> **11. What if I am unwell?** Tell us as soon as you can. You can change your booking up to 48 hours before, and we send reminders. Refund rules: NOT IN REPO, lawyer to check.

Legal comment: as written it reads as if illness inside 48 hours costs her money. Use the PART-2 rule.

**Safe revision 11:**
> **11. What if I am unwell?** Tell us as soon as you can. You only need to say "unwell". If you are unwell, have a pregnancy complication, are in hospital or in labour, or a doctor or midwife advises you not to have the test, you choose a free rebook or a full refund of anything not yet provided, even inside 48 hours.

Regards.
Catherine
