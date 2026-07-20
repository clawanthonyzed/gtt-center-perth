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
- Multi-practitioner calendar: yes — confirmed sufficient for the verified 2-chair/12-staff capacity model (see operations-manual.md per-staff timetable). Each phlebotomist/chair and each service-category staff member needs their own Fresha calendar resource so the daily 10-client/morning GTT schedule (Scenario C, synchronized start) can be built without double-booking.
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
- Multi-practitioner calendar handles all 12 employed staff (2 phlebotomists + 8 AM treatment staff + reception + PM Service Therapist) — see `staff-plan.md`
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
    - Pregnancy Massage (30 or 45 min, per current package structure)
    - Nails — Manicure or Pedicure (30 or 45 min)
    - Brows (20–30 min)
    - Hair (cut, blowdry — 30 or 45 min)
  *(Updated 2026-07-19: removed 3D Keepsake Scan and Dietitian consultation — neither is launch scope. 3D scan is a future/Phase 2 income stream, not a current bookable service, see `hire-purchase-china.md` §1C and `market-research-findings.md`. Dietitian is removed from scope entirely, see `staff-plan.md`.)*
  System shows only combinations that fit within the GTT window
  Customer selects package OR builds à la carte

STEP 4 — Select Practitioners (optional)
  "Any available" default
  OR customer can select preferred practitioner if returning

STEP 5 — Customer Details
  Name, mobile, email, due date (week of pregnancy — for service eligibility check)
  First visit? Yes/No
  How did you hear about us? (tracking)

STEP 6 — Payment (CONFLICT-09 RESOLVED 2026-07-20 — was previously described as a deposit option)
  Full package price charged at time of booking (confirmed by Anthony — no deposit-only option)
  Payment via Fresha Pay (Visa/MC) — no separate EFTPOS balance payment needed at the venue

STEP 7 — Confirmation
  Instant confirmation email + SMS
  Calendar invite (.ics) attached
  Fasting instructions included in email

STEP 8 — 48-Hour SMS Reminder (automated)
STEP 9 — 24-Hour SMS Reminder (automated, with fasting time callout)
STEP 10 — Day-Of Reminder 1 hour before (automated)
STEP 11 — Post-Visit Follow-Up 24 hours after (automated)
```

### Cancellation Policy (corrected 2026-07-20 to match the confirmed full-payment model)
- Cancel ≥48 hours before: full credit, reschedule to any available slot within 90 days (no refund)
- Cancel 24-48 hours before: 50% credit applied to a rescheduled appointment, 50% retained
- Cancel <24 hours / same-day: no credit, no refund, full amount retained
- No-show: full amount already collected at booking, retained
- Practitioner cancels: full refund + priority rebooking

### Late Arrival Policy
- >10 minutes late for booked GTT slot: GTT slot forfeited, full amount already paid at booking is retained (same as a same-day cancellation), client rebooked for next available slot — not squeezed into the existing schedule (would breach draw-timing tolerances for other clients on the same chair)
- See operations-manual.md Late Arrival Policy for full detail

### Waitlist
- Customer joins waitlist for fully booked GTT slot
- System (or staff) notifies waitlist when cancellation occurs
- First on waitlist gets 2-hour window to confirm before next in line is notified

### Staff Management (employed staff — no subtenants)
- Each employed staff member has their own Fresha calendar login
- Roster/availability is set by the Venue Manager (staff do not self-manage availability as an independent subtenant would) — each AM staff member's calendar must reflect their Mon–Fri 7:00–12:30 shift; PM Service Therapist's calendar reflects the 12:00–18:00 PM shift (see `staff-plan.md` §2A)
- Each staff member's calendar shows: bookings for the day, customer name + service only (no personal health details)
- End-of-day summary email: tomorrow's schedule

### Admin View
- Daily booking sheet: all GTT slots + associated services + staff + payments
- Weekly revenue report: booking revenue only (no subtenant rental income exists under the employed-staff model) — see `financial-setup.md`
- No-show rate tracker
- Waitlist volume (demand indicator)

---

## 5. PAYMENT PROCESSING SETUP

**Fresha Pay:**
- Integrated, no separate Stripe account needed for basic setup
- Processing fee: ~1.7% + $0.30 per transaction (Australian standard)
- Payouts: next business day
- All revenue flows to GTT Center Perth directly — no subtenant rent split, since all service delivery staff are employed, not subletting practitioners (see `staff-plan.md` §1)

**Payroll (replaces the subtenant-rent-billing model previously described here):**
- Staff wages processed via Xero payroll (weekly pay run) — not a rent invoice, see `financial-setup.md` and `hr-framework.md`
- No separate rent collection process exists or is needed under the employed-staff model

---

## Sources
- [Fresha Pricing](https://www.fresha.com/pricing)
- [Cliniko Pricing](https://www.cliniko.com/pricing/)
- [Fresha Review 2026 — The Salon Business](https://thesalonbusiness.com/fresha-review/)
- [Cliniko Features](https://www.cliniko.com/features/appointments/)

---

## Changelog

**2026-07-19** — Found via founder-requested contradiction scan. Flagged this document's subtenant/room-rental practitioner model (subtenant calendar logins, subtenant rent invoicing, "4-5 subtenants") as superseded — contradicts the confirmed employed-staff, no-subtenant model. Also fixed a stale "8-client/morning" reference to note the current 10-client Scenario C model. Platform comparison/recommendation (Fresha) unaffected. See `docs/01_conflicts_log.md` CONFLICT-07.

**2026-07-19 (full fix, same day — supersedes the flag-only pass above)** — Actually rewrote every subtenant/room-rental reference to the employed-staff model rather than leaving it flagged: "Practitioner Management" retitled "Staff Management," subtenant calendar logins -> employed-staff calendar logins with Venue Manager-set rosters, subtenant rent invoicing/direct-debit section replaced with a payroll reference (Xero, weekly pay run), "4-5 subtenants" corrected to "12 employed staff." Also rewrote the Step 3 booking-flow service list — removed 3D Keepsake Scan and Dietitian consultation as current bookable services (neither is launch scope; 3D scan is future/Phase 2, dietitian is removed entirely) and corrected massage/nail service durations to match the current 30/45-min package structure. Removed the earlier superseded-content banner now that the fixes are made directly rather than just flagged.

**2026-07-20 (CONFLICT-09 resolved)** — Corrected Step 6 Payment and the Cancellation/Late Arrival Policies: Anthony confirmed full package price is charged at booking, not an A$30 deposit. Replaced the deposit-forfeit mechanism with the tiered credit policy (≥48hrs full credit, 24-48hrs 50% credit, <24hrs no credit) that matches `onboarding.md`'s already-correct draft copy.
