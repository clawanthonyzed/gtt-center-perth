# Results line patch (draft for Anthony, no file has been changed)

## READ-FIRST CHECK
- Venue manager: a hired person, starts 06:30 (Mon to Fri 06:30 to 15:00). The first draw is 07:00.
- Path A = PREFERRED: package WITH the GTT midwife consult. Path B = NOT preferred: outside referral, no GTT consult.
- Prices: Path A A$320 / A$370 (GTT charges A$292.15 / A$342.15). Path B A$300 / A$350 (GTT charges A$272.15 / A$322.15).
- Rebates used for planning: about A$55.00 (consult A$32.95 plus lab A$22.05).
- Midwives on site 08:00 to 16:00, first consult 08:15.
- Late rule: draws have no wiggle room; consults have a 10 minute grace window.

## Summary
Five repo files still say GTT never communicates results. That is out of date. The new wording below follows GTT-READ-FIRST.md. Nobody logs in to anything: there is no portal.

## Deliverable
New wording, used in every row where it fits:
- Path A: the lab sends the result to the requesting GTT midwife. She phones abnormal results. No answer: she leaves a voicemail asking the client to call GTT, then sends an email saying the midwife has tried to make contact regarding results, with no result detail. Normal results: a generic text or email saying a message is ready.
- Path B: the result goes to the client's outside doctor or midwife. GTT makes no results call.

| File | Line | Old text | New text | Reason |
|---|---|---|---|---|
| agents/grace.md | 19 | GTT Center Perth never communicates clinical results. | Path A: the lab sends the result to the GTT midwife, who phones abnormal results and sends a generic message for normal ones. Path B: the result goes to the outside doctor or midwife and GTT makes no call. | Midwife now owns Path A results |
| agents/ivy.md | 50 | Ivy never communicates test results | Ivy does not give or explain results. The midwife handles Path A results; Path B results go to the outside practitioner. | Ivy stays out, midwife is named |
| docs/onboarding.md | 150 | GTT Center Perth does not communicate blood test results. Results are sent by WDP/PathWest directly to the referring GP. Clients must follow up with their GP. | Path A: the midwife phones abnormal results and sends a generic message for normal ones. Path B: results go to the client's outside doctor or midwife, who follows up with her. | Matches the two paths |
| docs/pathology-partnership-brief.md | 155 | GTT Center Perth never communicates results to patients. Results go WDP to GP to patient. | Path A: results go from the lab to the GTT midwife, who tells the client. Path B: results go from the lab to the outside practitioner. | Lab must send to the midwife on Path A |
| docs/consent-form.md | 35 | We do NOT communicate your GTT results to you (a long dash follows in the file) results are sent by the laboratory to your referring doctor | If you book with our midwife, she phones you about an abnormal result and a generic message tells you when a message is ready. If your request came from outside GTT, the result goes to your outside doctor or midwife and we do not call you. (Lawyer to check.) | Consent must match what happens |

Generic ready message (text or email, no health detail, no log in): "GTT Center Perth: a message for you is ready. Please call us on {gtt_phone}. Regards."

Same old statement also found, not patched here: docs/gtt-clinical-protocol.md line 157, docs/gtt-test-reference.md line 179, docs/phlebotomist-job-posting.md line 56. Apply the same wording.

File owners check: Grace the midwife duties; Ivy that no result is given at the draw; Catherine the consent wording.

## Next step for Anthony
Approve the wording. Then the files can be changed in one pass.

## QUESTIONS FOR ANTHONY
1. How a normal result is passed on after the ready message is NOT IN REPO. Options: (a) she calls GTT and the midwife tells her, (b) the midwife calls every client. Recommendation: (a).

Regards.
