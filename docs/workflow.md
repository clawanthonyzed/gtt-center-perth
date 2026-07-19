# GTT Center Perth — Operational Workflow

---

## Customer Journey

```
1. BOOKING
   Customer books via website/phone
   → Selects GTT date/time (synced with pathology partner schedule)
   → Selects service package (Relax / Restore / Glow / Complete)
   → Receives confirmation + pre-appointment instructions

2. ARRIVAL
   Customer arrives fasting (8hrs min)
   → Welcomed at reception
   → Pathology phlebotomist takes first blood draw (T=0)
   → Customer given glucose drink

3. WAIT (T=0 to T=60)
   First service begins immediately after glucose drink
   → Massage OR nails OR hair (60 min)

4. SECOND BLOOD DRAW (T=60)
   Phlebotomist returns for second draw
   → Customer resumes or begins second service

5. THIRD BLOOD DRAW (T=120)
   Final blood draw
   → 3D scan (if booked) during wind-down period
   → Snacks/refreshments provided

6. DEPARTURE
   Results via pathology provider (same-day or next-day per partner agreement)
   → Customer departs with keepsake scan photos (if booked)
   → Follow-up booking prompt sent via SMS/email
```

---

## Booking System Requirements

- GTT slot pairing: every service booking MUST link to a confirmed pathology appointment time
- Buffer enforcement: no service booking accepted without confirmed GTT time first
- Service slot auto-calculation: system calculates available service windows from GTT start time
- Subtenant availability calendar: real-time visibility of which practitioners are available
- Waitlist management: automatic waitlist for cancelled slots
- Reminder sequence: 48hr + 24hr SMS reminders (confirm fasting instructions)
- Cancellation policy: 24hr notice required (GTT slots are limited)

---

## Subtenant Daily Flow

- Practitioners arrive 15 min before first booking
- Each sublet room has own access, storage, and equipment
- Booking system notifies practitioners of their daily schedule
- No-show protocol: venue contacts practitioner, 15-min grace, then customer offered alternative
- End of day: room left clean and stocked for next day

---

## Pathology Partner Flow

- PathWest/WDP phlebotomist stationed on-site during operating hours OR on-call for each GTT slot
- Dedicated collection room (minimum 3x3m, sharps disposal, hand wash, privacy screen)
- Blood draws at T=0, T=60, T=120
- Results delivered to referring doctor (not to GTT Center Perth — no medical role)
- Emergency protocol: phlebotomist has first aid certification; venue has first aid kit; emergency contact list posted in collection room

---

## Staffing Model (Launch)

| Role | Model | Hours |
|---|---|---|
| Reception/host | Employed (Venue Manager oversight — new hire, not yet in place) | Mon–Fri 8am–5pm |
| Massage therapist | Sublet | Per booking |
| Nail technician | Sublet | Per booking |
| Hairdresser | Sublet | Per booking |
| Keepsake scan operator | Sublet | Per booking |
| Phlebotomist | PathWest/WDP staff | On-site or on-call |

---

## Space Requirements

| Room | Min Size | Notes |
|---|---|---|
| Reception / waiting | 20–30 sqm | Comfortable seating, snacks station |
| Treatment room x2 (massage, hair) | 12–15 sqm each | Soundproofed preferred |
| Nail station | 10–12 sqm | Good lighting, ventilation |
| Scan room | 15–20 sqm | 60" display, dim lighting, family seating |
| Pathology collection room | 9 sqm min | Dedicated, WA Health compliant |
| Staff/storage | 6–8 sqm | |
| **Total** | **~100–130 sqm** | |

---

## Agent Responsibilities

| Agent | Responsibility |
|---|---|
| **Grace** | Overall operations, partner relationships, financial oversight |
| **Ivy** | Booking system config, scheduling, customer comms templates |
| **Reed** | Pathology partner outreach, subtenant recruitment and contracts |
| **Poppy** | Instagram, referral network (midwives/OBs), Google Business Profile, SEO |

---

## Changelog

**2026-07-19** — Founder decision (confirmed 2026-07-18): replaced operational reference to "Imara" (Reception/host employment line) with "Venue Manager" (new hire, not yet in place). Ownership/trust structure unaffected — see `financial-model.md`/`research.md`. Note: this document's staffing/subtenant model (sublet massage/nails/hair/scan) is an early draft superseded by `staff-plan.md`'s employed-staff model — flagged separately in `docs/01_conflicts_log.md`.
