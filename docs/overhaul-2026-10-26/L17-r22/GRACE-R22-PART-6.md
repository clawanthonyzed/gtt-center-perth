> SUPERSEDED where it disagrees with docs/GTT-READ-FIRST.md (Round 25 integrity banner, 2026-10-27). Read that file first.

# GRACE-R22-PART-6: Record keeping recommendation (computer record)

Author: Grace. Date: 2026-10-26 (Round 22). DRAFT for Anthony. Nothing was sent. Source: Reed R22 Part 4 (prices opened 2026-10-26; US dollars converted at the Reserve Bank rate in logs/fx_aud.json, US$1 = A$1.4223, converted not quoted). Costs are INFORMATION ONLY and are not in the financial model. Tags: R repo, V verified (Reed), E estimate, U unverified.

## READ-FIRST CHECK (from GTT-READ-FIRST.md, 2026-10-26)
- Venue manager start: 06:30 Mon to Fri (07:00 is the first draw).
- Path A = PREFERRED, package WITH the GTT midwife consult. Path B = NOT preferred, outside referral, no GTT consult.
- Prices: Path A shown A$320 / A$370, GTT charges A$292.15 / A$342.15. Path B A$300 / A$350 all in.  <!-- factcheck:ok -->
- Rebates (planning, "about"): consult A$32.95 + lab A$22.05 = A$55.00.
- Midwife on site 08:00, first consult 08:15, shift ends 16:00.
- Late rule: "Please arrive at least 10 minutes before your appointment, because late means from your appointment time onwards and we cannot fit a first blood draw in after that."

## 1. Short answer
Pick one practice system for the clinical record, and keep the lounge booking page separate unless the system proves it can run our two-path rules. The easiest and cheapest choice that shows every feature we need on its own price page is **Zanda Health, Growth plan**: about US$87 a month for 2 permanent plus 1 casual midwife, about A$123.74 (E, assumes each midwife counts as a practitioner). It is the only option where the audit log, online booking and waitlist emails are all shown (V, Reed). Its Australian hosting is NOT CONFIRMED and must be confirmed in writing before we choose.
Fallbacks, in order: Cliniko (Australian hosting stated, V; US$95 a month for 2 to 5 practitioners, about A$135.12), then Nookal Professional (A$59 each, about A$177 for 3, audit log, hosting not stated). Halaxy has a free core and says data is stored in Australia, but its audit log and waitlist are not confirmed. Google Workspace has no Australian data region, so it is out for records. Microsoft 365 suits referral copies, not booking.
We do not need the system to send claims to Medicare, because the client claims her own rebate (Structure B, R).

## 2. Comparison (information only)
| Option | Cost | Data in Australia | Audit log | Booking and waitlist |
|---|---|---|---|---|
| Zanda Health Growth | US$49 + US$19 per extra practitioner, about A$123.74 for 3 | NOT CONFIRMED | Yes | Yes, waitlist emails |
| Cliniko | US$95 for 2 to 5 practitioners, about A$135.12 | Yes (V) | Not confirmed | Not confirmed |
| Nookal Professional | A$59 each | Not stated | Yes | Basic waitlist |
| Halaxy | Free core, add-ons by credit | Stated, with US sub-processors | Not confirmed | Booking yes, waitlist not confirmed |

## 3. What GTT would store, and for how long
| Item | Stored? | Where |
|---|---|---|
| Consult note with start and end times (Medicare may check, V Reed) | Yes | Clinical record |
| Written request (pathology request) issued by the midwife | Yes | Clinical record, filed to the test-day record |
| Copy of a Path B client's outside referral | Yes | Test-day record, marked "client upload" or "emailed in" |
| Result follow-up log: one line per attempt | Yes | Clinical record |
| Consent choices (how she may be contacted) | Yes | Booking profile |
| Payment details | No, the card provider holds them | Card provider |
| Exception codes (EX-1 to EX-4) | Yes, codes only | Booking profile |
| Lab results | Only what the midwife needs; storage method NOT IN REPO | Clinical record |
| Health letters or certificates | No copies kept; deleted after the decision | |
Retention: common practice is at least 7 years from the last entry (U, R21; no WA or Commonwealth period found); Catherine and the insurer to confirm. The test-day working view clears 28 days after the test; the clinical record stays.

## 4. Who has access
| Person | Flags | Clinical record | Delete |
|---|---|---|---|
| Midwife on duty | Yes | Yes | No |
| Phlebotomists (GTT Medical) | Yes | Test day only | No |
| Venue manager (Lounge) | Flags only | No | No |
| Lounge and service staff | No | No | No |
| System administrator | Yes | Only to restore, logged | Yes, logged |
Anthony's administrator role is an open issue (hours and MRCA). Until Catherine and DVA clear it, the administrator login should belong to a named GTT Medical manager, with Anthony limited to the owner duties Catherine allows. Every look at a record is logged by name and time. The partner lab gets nothing from this system; the paper request travels with the sample.

## 5. Set-up steps
1. Anthony names the records owner: GTT Medical (Reed's recommendation).
2. After Anthony approves, Grace emails Zanda and Cliniko the unconfirmed list: Australian hosting, audit log, waitlist email, referral copy storage, exporting records on exit, and whether lab details can be excluded. Nothing is sent before approval.
3. Choose the system; start a trial if offered (NOT CONFIRMED).
4. Create users and roles from section 4; switch on the second sign-in step; set the screen lock.
5. Build the templates: consult note with start and end time, request, result follow-up log, exception code field.
6. Catherine writes the privacy notice and the retention rule.
7. Set the daily backup and test a restore once.
8. Train the midwives and phlebotomists; the venue manager is trained on flags only.
9. Set up the breach plan (a lost record may be a reportable breach).
10. Test run on 5 dummy bookings before opening.

## QUESTIONS FOR ANTHONY
1. Who is the records owner?
   - A: GTT Medical. B: The midwife. C: You.
   - Recommendation: A.
2. Approve Grace to email Zanda and Cliniko for written answers?
   - A: Yes, both. B: Zanda only. C: Wait.
   - Recommendation: A.

Regards.
Grace
