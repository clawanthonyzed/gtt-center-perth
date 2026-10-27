# R22-16 Abnormal results call, voicemail and email (Round 24 corrected version)

DRAFT for Anthony. Nothing is sent. Lawyer to check every item. No real person is addressed.

## READ-FIRST CHECK
- Venue manager: a hired person, not Anthony. Starts 06:30 Monday to Friday (06:30 to 15:00) to open. The first draw is 07:00.
- Path A (preferred) = package WITH the GTT midwife consult. Path B (not preferred) = the client keeps an outside referral, no GTT consult. Path B is not limited in any way.
- Prices (R): Path A advertised A$320 / A$370, GTT charges A$292.15 / A$342.15. Path B A$300 / A$350, GTT charges A$272.15 / A$322.15. The lab fee A$27.85 is paid by the client to the lab.
- Rebates used (R, about): consult A$32.95 + lab A$22.05 = A$55.00, Path A only.
- Midwives are on site 08:00 to 16:00. First consult 08:15, in 25 minute blocks.
- Late rule: arrive 10 minutes early. Blood draws have no wiggle room. Consults have a 10 minute grace window.
- Source: GTT-READ-FIRST.md (2026-10-27). Any older file that calls the outside referral Path A is out of date.

## Summary
The wording for contacting a Path A client about her results. Round 24 lock applied: for abnormal results the midwife phones; no answer means a voicemail, then an email saying the midwife has tried to make contact regarding results. The email goes only if the client agreed at booking. No result detail anywhere. Fixed from last night: the old email avoided the word results, the follow-up text is retired, and the made-up phone number is gone.

## Deliverable

### 1. Consent question (Path A details screen, final text)
How may our midwife contact you about your results? Tick all that you allow.
- Call my mobile.
- Leave a voicemail asking me to call GTT.
- Send me an email saying the midwife has tried to make contact regarding my results.
- Send me a text or email when a result needs nothing more from me.
No tick means we will not leave that voicemail or send that message. Lawyer to check.

### 2. Call script (identity check before any detail)
1. Hello, may I speak to {full_name}? This is {caller_first_name}, from {business_name}.
2. Is now a good time to talk in private? If no: When can I ring back today?
3. Before I go on, can you tell me your full name and date of birth? No match, no detail.
4. I am calling about your recent visit. One of your results needs a follow-up, and I would like to explain what happens next.
5. Do you have any questions? You can call us on {phone} any time we are open.

### 3. Voicemail (only if she ticked voicemail)
This message is for {first_name}. This is {caller_first_name} from {business_name}. Please call us back on {phone}. Thank you.

### 4. Follow-up email (only if she ticked this email; sent after the voicemail)
Subject: Please call us
Hello {first_name}, the midwife has tried to make contact regarding results. Please call us on {phone} when you can. Regards.
No result value, no diagnosis, no advice in the email.

### 5. Follow-up text for abnormal results
None. Round 24 locked voicemail then email only.

### 6. Normal results (only if she ticked the normal result option)
Email subject: A message from {business_name}
Email and text: Hello {first_name}, your midwife has reviewed your recent visit and no action is needed. Call {phone} with any questions. Regards.

### 7. Contact flow, log line and front desk line
- The midwife phones the client's mobile (checked at booking) the same day, inside her shift.
- No answer: voicemail (if allowed), then the email (if allowed) within about 15 minutes.
- A second call 2 to 3 hours later, before 16:00.
- Still no contact: the clinical protocol decides. Timings: NOT IN REPO.
- Log, midwife only, one line per attempt: date, time, channel, outcome, midwife name. The venue manager never sees a result.
- If the client rings GTT, the front desk takes name and number only and says: I will get her to ring you straight back.
- Path B: results go to the outside practitioner, so GTT makes no results call.

### 8. Merge fields

| Field | What goes in it |
|---|---|
| {first_name} | Client first name from the booking |
| {full_name} | Client full name from the booking |
| {caller_first_name} | First name of the midwife calling |
| {business_name} | Final trading name, NOT IN REPO (brand names on hold) |
| {phone} | GTT phone number, NOT IN REPO |

## Next step for Anthony
Send the consent text and the email to Catherine and the lawyer. Do not use any of this until both agree.

## QUESTIONS FOR ANTHONY
1. Clinical protocol after two missed contacts, with timings: NOT IN REPO. Held by the lead midwife once hired. Recommendation: the lead midwife writes it in the first week.
2. Final trading name and GTT phone number: NOT IN REPO. Brand names are on hold. Recommendation: leave as merge fields.

Regards.
