# Opening SOPs: Opening/Closing, Business Continuity, Complaints/Refunds

Status: current as of 2026-08-23. The 3 genuinely missing operating procedures identified in `docs/architecture/VENTURE-OPENING-READINESS-AUDIT.md` and `docs/architecture/OPENING-READINESS-EXECUTION-PLAN.md`. Written so a staff member hired one week before opening can read this and know exactly what to do. Existing, complete SOPs (clinical protocol, emergency response, child/companion policy, privacy/consent) are not rewritten here.

## 1. Opening/Closing Procedure

**Who:** the first-arriving staff member (normally the Venue Manager or Receptionist, per the rostered opening shift) opens; the last-departing staff member closes.

**When:** opening, 30 minutes before the first booked AM slot; closing, once the last client and staff member for the day have left.

**Opening sequence:**
1. Unlock the venue, disarm any security system.
2. Turn on lighting, HVAC, and equipment requiring warm-up (coffee machine, water tap).
3. Check the Blood Collection Room: sharps containers not full, biohazard bin liner in place, specimen fridge at temperature (2-8C, per the cold-chain requirement in the procurement register), consumables stocked (gloves, swabs, glucose solution).
4. Check each treatment station (Massage, Beauty, Nail, Hair) for clean linen, stocked consumables, and functioning equipment.
5. Check the Cafe: fridge temperatures logged, display stock checked, coffee machine ready.
6. Turn on the POS/booking system, confirm the day's roster against Fresha.
7. Unlock the front door at the scheduled opening time.

**Closing sequence:**
1. Confirm no client remains on-site.
2. Blood Collection Room: dispatch any remaining specimens per the specimen-handling protocol (`docs/gtt-clinical-protocol.md`), secure sharps containers, wipe down surfaces with TGA-listed disinfectant.
3. Treatment stations: strip and bag linen for laundry (per the laundry model, once that founder decision is made), wipe down surfaces, secure consumables.
4. Cafe: cover/refrigerate perishable stock, clean equipment, empty food-waste bin.
5. Cash/POS reconciliation (if any cash handling exists; Fresha's own reporting covers card transactions).
6. Turn off non-essential lighting/equipment, set HVAC to overnight mode.
7. Arm any security system, lock all doors.

**Records required:** a daily opening/closing checklist (paper or digital, ticked by the staff member who performed it), retained for the same period as other operational records.

**Escalation:** if any check fails (e.g. a fridge out of temperature, a sharps container full, equipment malfunction), the Venue Manager is notified immediately and the affected service is not offered until resolved. A specimen cold-chain failure is escalated to WDP directly, per the existing clinical protocol.

## 2. Business Continuity / Emergency Closure

**Purpose:** distinct from `docs/emergency-plan.md` (which covers physical emergencies: fire, medical incident, evacuation). This SOP covers what happens when the venue cannot open or must close unexpectedly for a non-emergency reason: key staff illness, equipment failure preventing safe operation, a venue-related issue (power/water outage), or any other disruption to normal trading.

**Who is responsible:** the Venue Manager decides whether to close or modify service; Anthony is notified of any full-day closure or any closure affecting the Blood Collection service specifically.

**Sequence:**
1. Identify the disruption (staff absence beyond relief-pool coverage, equipment failure, utility outage).
2. Assess whether a modified service is possible (e.g. Blood Collection continues but one wellness service is unavailable) versus a full closure being required.
3. If Blood Collection cannot proceed safely (e.g. no phlebotomist available, specimen cold-chain compromised), all affected bookings for that day are contacted directly (phone/SMS), not left to discover on arrival. WDP is notified if the disruption affects specimen dispatch.
4. If a full closure is required, all bookings for the closure period are contacted, given a clear reason (kept brief, not over-explained), and offered rebooking priority.
5. Update the Google Business Profile/website (once they exist, per `docs/architecture/OPENING-READINESS-EXECUTION-PLAN.md` Section 8) with a temporary closure notice if the disruption extends beyond same-day.
6. Log the disruption, cause, and resolution for review, since repeated disruptions of the same type indicate a genuine operational gap to fix (e.g. recurring staff-absence gaps indicate the relief pool needs expanding).

**Escalation:** any disruption affecting the Blood Collection service specifically is escalated to Anthony and, where relevant, to WDP directly (medical waste, specimen handling, or collection-room compliance issues are never handled as a purely internal business-continuity matter).

**Records required:** an incident log entry per disruption (date, cause, clients affected, resolution, whether it recurred).

## 3. Complaints / Refunds / Service Recovery

**Purpose:** extends the existing booking terms and conditions (`docs/onboarding.md` B0) with what happens when a client is dissatisfied, requests a refund, or a service does not go as expected.

**Who is responsible:** the Venue Manager handles all complaints and refund decisions; Reception is the first point of contact for a client raising an issue in person or by phone.

**Sequence:**
1. **Receive:** any staff member receiving a complaint listens without immediately promising a specific outcome, and refers the client to the Venue Manager (or takes contact details if the Venue Manager is not immediately available).
2. **Log:** every complaint is logged (date, client, service affected, nature of the issue), regardless of how minor, so patterns are visible over time.
3. **Assess:** the Venue Manager assesses whether the issue is a service-quality issue (e.g. a treatment not meeting expectations), an operational issue (e.g. a delay, a booking error), or a clinical issue (e.g. a concern about the blood draw itself, which is escalated per the clinical protocol and, where relevant, to WDP, not resolved as a standard service complaint).
4. **Resolve:** standard service-quality or operational issues are resolved at the Venue Manager's discretion: a partial or full refund, a complimentary future service, or a direct apology and explanation, proportionate to the issue. A clinical-safety concern is never resolved with a refund alone; it triggers the incident-reporting process regardless of whether the client also wants a refund.
5. **Follow up:** the client is contacted within 48 hours of the resolution to confirm they are satisfied with the outcome.
6. **Review:** complaints are reviewed monthly by the Venue Manager (and Anthony, for anything clinical or reputation-affecting) to identify recurring issues.

**Cancellations/no-shows:** governed by the existing booking policy in `docs/onboarding.md` B0; this SOP does not duplicate that policy, only the complaint-handling process for when a client disputes a cancellation/no-show charge.

**Records required:** a complaints log (date, nature, resolution, follow-up outcome), retained and reviewed monthly.

## What This Document Deliberately Does Not Do

It does not rewrite the existing clinical protocol, emergency response plan, child/companion policy, privacy policy, or booking terms and conditions, all of which already exist and are complete. It does not invent a specific refund percentage or compensation scale, since no such policy has been decided anywhere in this repository; the Venue Manager's discretion, proportionate to the issue, is the current standard until a more specific policy is decided.

## Sourcing

`docs/architecture/VENTURE-OPENING-READINESS-AUDIT.md`, `docs/architecture/OPENING-READINESS-EXECUTION-PLAN.md`, `docs/emergency-plan.md`, `docs/gtt-clinical-protocol.md`, `docs/onboarding.md`.

## Changelog

**2026-08-23 (created):** Built per direct founder instruction as the 3 genuinely missing operating procedures identified in the opening-readiness audit and execution plan, written to be usable by a newly hired staff member, not rewriting any existing complete SOP.
