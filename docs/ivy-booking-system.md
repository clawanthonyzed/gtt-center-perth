# Ivy — Booking System Evaluation + Spec

**Prepared by:** Ivy (Booking & Scheduling Coordinator)  
**Date:** 2026-06-05

---

## 1. PLATFORM COMPARISON

### Critical Requirement
Every service booking MUST be linked to a confirmed GTT appointment time. No platform natively enforces this — it requires either custom configuration or a workaround layer.

### Platform Scorecard

| Platform | Price/month | SMS (AU) | Multi-practitioner | GTT pairing possible? | Verdict |
|---|---|---|---|---|---|
| **Fresha** | Free + 20% new client fee OR $14.95/user Team | Unlimited free SMS | Yes | Partial — can create resource dependency rules | **Best value** |
| **Cliniko** | $45 (1 practitioner) → $95 (2–5) | 10c/SMS | Yes — all tiers | Partial — conditional availability possible | **Best for clinical** |
| **Jane App** | $74 CAD/month base | Included | Yes | Limited custom logic | OK |
| **Acuity Scheduling** | $20–60 USD/month | Via Twilio add-on | Yes (Powerhouse tier) | Intake forms + conditional routing possible | OK |
| **Mindbody** | $139–349 USD/month | Included | Yes | Limited for custom flows | Too expensive for launch |

### Fresha Detail
- **Free subscription** for businesses (no monthly fee)
- Revenue model: 20% commission only on **new clients** who book via Fresha marketplace — existing clients and direct bookings are commission-free
- **$14.95/user/month Team plan** eliminates all marketplace fees
- **Unlimited free SMS notifications** — huge advantage for high-reminder-volume GTT bookings
- Multi-practitioner calendar: yes
- Online payment: yes (Fresha Pay — card processing)
- Retail/product sales: yes
- **Weakness:** Not designed for medical/clinical workflows; GTT slot pairing needs workaround

### Cliniko Detail
- Built for Australian allied health (physiotherapy, massage, psychology, etc.)
- **$95/month for 2–5 practitioners** (covers launch team)
- SMS at 10c each — at 25 bookings/week × 3 reminders = 75 SMS/week = ~$7.50/week ($30/month)
- Excellent clinical notes, consent forms, HIPAA-grade security
- Multi-location support
- **Weakness:** More clinical than beauty/spa; no free tier; GTT pairing needs custom setup

---

## 2. RECOMMENDATION

**Use Fresha (Team plan, $14.95/user/month) with a GTT pairing workaround.**

**Rationale:**
- Unlimited free SMS covers our high-reminder requirement at zero marginal cost
- No marketplace commission on direct bookings (all our bookings are direct — via referrals and website, not Fresha marketplace)
- Multi-practitioner calendar handles all 4–5 subtenants
- Built for beauty/wellness (nails, massage, spa) — matches our service types
- Retail management built in — handles product sales
- Online payment processing included

**GTT Pairing Workaround:**
Fresha doesn't natively block service bookings without a prior GTT slot. **Solution:**
1. Create "GTT Appointment" as a required first service (0-cost, 0-duration "consultation")
2. Set all other services to only appear as add-ons after the GTT appointment is selected
3. Alternatively: GTT slot is booked directly through pathology partner (WDP); customer brings their WDP confirmation number to the GTT Center Perth booking form as a required field before selecting services
4. Longer term: If volume justifies it (~3–6 months in), build a simple custom booking page (Webflow + Zapier) that enforces the pairing with a form validation step

---

## 3. SMS REMINDER DRAFTS

### 48-Hour Reminder
> Hi [Name]! Your GTT appointment at GTT Center Perth is on [Day] at [Time].
>
> **IMPORTANT — FASTING REQUIRED:**
> - Do NOT eat or drink anything (except water) for 8 hours before your appointment
> - Water is fine — stay hydrated
> - No coffee, tea, juice, or chewing gum
> - No exercise on the morning of your test
>
> Wear comfortable, loose clothing. Bring your pathology referral form and Medicare card.
>
> Questions? Call [phone]. See you soon! 🌿

### 24-Hour Reminder
> Reminder: Your GTT + [services] at GTT Center Perth is TOMORROW at [Time].
>
> Last fast check: nothing to eat or drink after [fasting cutoff time] tonight (water OK).
>
> We'll have herbal tea and snacks ready for after your final blood draw. 🍵
>
> Address: [address]. Free parking at [details].
>
> Reply STOP to opt out.

### Day-Of Reminder (1 Hour Before)
> See you soon! Your GTT appointment starts in 1 hour at GTT Center Perth, [address].
>
> Reminder: arrive fasting (water only since [cutoff time]). Bring your referral form + Medicare card.
>
> [Directions link]

### Post-Visit Follow-Up (24 Hours After)
> Hi [Name], we hope you had a wonderful experience at GTT Center Perth! 🌸
>
> Your GTT results will be sent to your doctor/midwife — please follow up with them directly.
>
> We'd love to see you again. Book your next visit: [booking link]
>
> And if you enjoyed your time, a quick Google review means the world to us: [Google review link]

---

## 4. COMPLETE BOOKING FLOW SPEC

### Customer Journey (Online)

```
STEP 1 — Select GTT Date
  Customer lands on booking page
  Sees calendar of available GTT morning slots (synced with pathology partner availability)
  Selects date and time (7:30am / 8:00am / 8:30am / 9:00am / 9:30am options)

STEP 2 — Enter GTT Reference (if pathology books separately)
  If pathology partner books GTT independently:
    Customer enters their WDP/PathWest booking reference
    System validates format (or staff validates manually)
  If GTT and services are co-booked:
    Skip to Step 3

STEP 3 — Select Services
  System calculates available service window from GTT time
  (e.g. GTT at 8:00am → services available 8:05am–10:05am)
  Customer selects from:
    - Pregnancy Massage (60 or 90 min)
    - Nails — Manicure or Pedicure (45–60 min)
    - Brows (20–30 min)
    - 3D Keepsake Scan (25 min) — links to scan operator's calendar
    - Dietitian consultation (60 min) — during or post GTT
  System shows only combinations that fit within the GTT window
  Customer selects package OR builds à la carte

STEP 4 — Select Practitioners (optional)
  "Any available" default
  OR customer can select preferred practitioner if returning

STEP 5 — Customer Details
  Name, mobile, email, due date (week of pregnancy — for service eligibility check)
  First visit? Yes/No
  How did you hear about us? (tracking)

STEP 6 — Payment
  Deposit: A$30 (non-refundable if cancels within 24hrs)
  OR full payment upfront (optional)
  Payment via Fresha Pay (Visa/MC) or EFTPOS at venue

STEP 7 — Confirmation
  Instant confirmation email + SMS
  Calendar invite (.ics) attached
  Fasting instructions included in email

STEP 8 — 48-Hour SMS Reminder (automated)
STEP 9 — 24-Hour SMS Reminder (automated, with fasting time callout)
STEP 10 — Day-Of Reminder 1 hour before (automated)
STEP 11 — Post-Visit Follow-Up 24 hours after (automated)
```

### Cancellation Policy
- Cancel 24+ hours before: deposit refunded or rescheduled free
- Cancel within 24 hours: A$30 deposit forfeited
- No-show: full session charged (deposit + balance)
- Practitioner cancels: full refund + priority rebooking

### Waitlist
- Customer joins waitlist for fully booked GTT slot
- System (or staff) notifies waitlist when cancellation occurs
- First on waitlist gets 2-hour window to confirm before next in line is notified

### Practitioner Management
- Each sublet practitioner has their own calendar login
- They set their own availability (must mark at minimum: Mon–Fri 7:30–12:30 as available)
- Their calendar shows: bookings for the day, customer name + service only (no personal health details)
- End-of-day summary email: tomorrow's schedule

### Admin View
- Daily booking sheet: all GTT slots + associated services + practitioners + payments
- Weekly revenue report: booking revenue + subtenant rental payments
- No-show rate tracker
- Waitlist volume (demand indicator)

---

## 5. PAYMENT PROCESSING SETUP

**Fresha Pay:**
- Integrated, no separate Stripe account needed for basic setup
- Processing fee: ~1.7% + $0.30 per transaction (Australian standard)
- Payouts: next business day
- Can split payments: customer pays booking fee; practitioner rent billed separately

**Subtenant Rent Billing:**
- Invoice each subtenant weekly via Xero or similar accounting software
- Separate from customer booking system
- Direct debit setup preferred (auto-debit their nominated account each Monday)

---

## Sources
- [Fresha Pricing](https://www.fresha.com/pricing)
- [Cliniko Pricing](https://www.cliniko.com/pricing/)
- [Fresha Review 2026 — The Salon Business](https://thesalonbusiness.com/fresha-review/)
- [Cliniko Features](https://www.cliniko.com/features/appointments/)
