# Appointment reminder messages (DRAFT for Anthony, nothing is sent)

## READ-FIRST CHECK
- Venue manager: hired, starts 06:30; first draw 07:00. Anthony is owner and director only.
- Path A = with GTT midwife consult (preferred). Path B = outside referral, no GTT consult.
- Prices and rebates: not used in these messages.
- Midwives 08:00 to 16:00, first consult 08:15. The Path A consult is usually 1 to 28 days BEFORE the test, on a different day.
- Late rule: draws no wiggle room; consults 10 minute grace.

## Summary
Six messages: Path A 48 hour email, Path B 48 hour email, Path A and Path B evening-before texts (each under 300 characters), and a missed test follow-up. Fasting hours are NOT IN REPO (needs the lab and the midwife to confirm). No health detail in any text.

## Deliverable

**1. Path A, 48 hours email**
Subject: Your visit in 2 days
Body: Hi {first_name}, a reminder of your visit on {appointment_date}. Draw 1 is at {draw1_time}. Please arrive at least 10 minutes before your appointment, because late means from your appointment time onwards and we cannot fit a first blood draw in after that. We have no wiggle room for draws. Your consult with our midwife is on {consult_date} at {consult_time}; a consult has a 10 minute grace window. If you have not booked your consult yet, you can book it up to 28 days ahead: {booking_link}. A same-morning consult is possible only if it ends before your draw. Fasting instructions: NOT IN REPO. You can change or cancel until 48 hours before: {manage_link}. Regards. GTT team

**2. Path B, 48 hours email**
Subject: Your visit in 2 days
Body: Hi {first_name}, a reminder of your visit on {appointment_date}. Draw 1 is at {draw1_time}. Please bring your outside referral, or email it in before the day: {referral_email}. Please arrive at least 10 minutes before your appointment, because late means from your appointment time onwards and we cannot fit a first blood draw in after that. We have no wiggle room for draws. Fasting instructions: NOT IN REPO. You can change or cancel until 48 hours before: {manage_link}. Regards. GTT team

**3. Path A, evening-before text**
GTT: Hi {first_name}, see you tomorrow at {draw1_time}. Please arrive 10 minutes early, no wiggle room for draws. Need to change? {manage_link}

**4. Path B, evening-before text**
GTT: Hi {first_name}, see you tomorrow at {draw1_time}. Please bring your referral and arrive 10 minutes early. Change? {manage_link}

**5. If you are unwell**
Subject: Need to rebook?
Body: Hi {first_name}, if you cannot make it, reply with the word "unwell" or any short note. We will never ask why. We will help you pick a new time: {manage_link}. Regards. GTT team

**6. Missed test follow-up**
Subject: We missed you today
Body: Hi {first_name}, we did not see you at {draw1_time} today and hope all is well. You can pick a new time here: {booking_link}. Regards. GTT team

### Merge fields
| Field | Source |
|---|---|
| first_name | Booking |
| appointment_date, draw1_time | Booking |
| consult_date, consult_time | Booking, Path A only |
| booking_link, manage_link | Booking system |
| referral_email | NOT IN REPO |

## Next step for Anthony
Approve the wording. QUESTIONS FOR ANTHONY: 1. Who confirms the fasting hours (recommend the lab, with the midwife checking)?

Regards.
