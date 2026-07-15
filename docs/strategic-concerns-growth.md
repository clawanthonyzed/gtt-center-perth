# GTT Center Perth — Strategic Concerns & Growth Plan

**Version:** 1.0 | **Date:** 2026-07-14
**Status:** First multi-location/growth planning pass — Venture is still pre-launch (Venue 1 not yet signed)

---

## Problem Statement

GTT Center Perth's single-venue model is close to finalised (corrected staffing, profitable from Month 4), but Anthony has raised six unresolved concerns that sit above the day-to-day launch plan: whether AM clients can reliably get the services they select, whether the venture is understaffed, what real profit ceiling exists, and — critically — no growth plan exists beyond the first venue. These need answering before capital is committed, since some (venue count, interstate ambition) affect how Venue 1's lease term and systems should be built (e.g. whether to build "franchisable" systems from Day 1 or retrofit them later).

## Goals

- AM clients can reliably book their preferred services with no more than the residual risk explained below
- A concrete, monitored process exists to detect and prevent understaffing before it causes a service failure
- Anthony has a realistic, evidence-based profit ceiling for the single-venue model at capacity
- A staged growth path exists: single venue → proven model → second Perth venue → (conditional) interstate
- Interstate expansion has a stated set of preconditions rather than being an open, undated ambition

## Non-Goals

- Not committing capital to a second venue or interstate expansion at this stage — this is a planning document, not a decision to act
- Not resolving the AM 3rd-chair/10-client expansion (Scenario A, already deferred, no verified timetable) — flagged as a lever, not built out here
- Not designing a franchise/licensing legal structure — noted as a future model option only

## User Stories

- As Anthony, I want to know the realistic single-venue profit ceiling so I can decide whether this venture justifies the capital and time versus other ventures in the portfolio.
- As a GTT client, I want to know before I arrive whether my preferred services are actually available that day, so I'm not disappointed on-site.
- As the Manager, I want an early-warning signal for understaffing so a gap is caught before a client is turned away.
- As Anthony, I want to know what has to be true before a second venue or interstate expansion makes sense, so I'm not guessing when the time comes.

## Technical/Operational Requirements

### 1. AM Clients Not Getting Their Selected Services

**Root cause:** only 2 staff per service line, staggered 20-minute arrivals, 8 clients/day cap. If the same service (e.g. hairdressing) is already booked out for that morning's cohort, a later-booking client physically cannot get that service that day.

**Mitigation already structurally in place:** clients select services at booking time (not on arrival), so Fresha can show real-time per-slot availability — if hair is full for a given morning, the client simply cannot select it and is offered an alternative or a different day.

- Confirm Fresha's booking flow actually blocks selection once a service line is full for a given AM cohort — **this must be tested before launch, not assumed**
- Use the waitlist service-interest data (see `pm-staffing-roster.md` Waitlist model) to pre-bias which line gets its 2nd concurrent hire first, reducing the odds any one line fills disproportionately fast
- Residual risk: a line can still legitimately sell out on a popular day. This is a capacity ceiling, not a system failure — the fix is either accurate real-time availability (so clients aren't disappointed after committing) or, longer-term, AM capacity expansion (Scenario A, 3rd chair)

### 2. Understaffing Risk

**Mitigation already built this session:** booking-driven rostering (staff rostered to confirmed Fresha bookings, not blanket presence), dedicated cross-shift casual relief pool with fortnightly fairness rotation, minimum-engagement compliance.

**Residual risk:** a small relief pool (1 per line) has zero buffer on a day when 2 people are simultaneously sick, or during the first weeks before the relief pool has built rapport/availability patterns. This is a real, un-eliminated risk at launch — flagged, not solved, here.

### 3. Realistic Monthly and Yearly Profit — At Current Capacity Ceiling

Single-venue, current model, capacity-capped at 14 visits/day (8 AM GTT + up to ~16 PM individual sessions):

| Period | Figure |
|---|---|
| Month 4 (break-even reached) | +A$4,924/month |
| Month 5+ steady state | **+A$6,663/month (+A$79,956/year)** |
| Bear case (AM-only, no PM/ancillary — see `cash-flow.md` sensitivity) | Loss — model depends on both AM and PM contributing |
| Bull case (premium package mix + extended PM hours, per `cash-flow.md` sensitivity) | Materially higher — not yet recalculated against the corrected PM model |

**This is a hard ceiling under the current design** — AM is capped by 2 phlebotomists/2 chairs, PM by the 4-role roster's realistic throughput. Growing profit beyond ~A$80K/year at a single venue requires one of the growth levers below, not just "more marketing."

### 4. Growing the Business Beyond the Single-Venue Steady State

Levers, roughly in order of effort required:

| Lever | What It Requires | Notes |
|---|---|---|
| Extend operating days (add Saturday) | Saturday penalty rates (1.33x) — not yet in the model | Adds revenue days without adding a venue |
| PM package upsell option | Pricing design only (Open Question already flagged in `pm-staffing-roster.md`) | Already identified as upside, not required for break-even now |
| AM 3rd chair (Scenario A, 10-client/day) | 3rd phlebotomist, verified timetable (currently none exists) | Deferred — biggest single-venue lever, needs its own planning pass |
| Second Perth venue | Proven Venue 1 track record (recommend 12+ months operating history), fresh capital raise, new WDP site approval | See Section 5 |
| Interstate | See Section 6 — much higher bar |

### 5. Expansion to New Locations Within Perth/WA

**Precondition:** Venue 1 should have a minimum of 12 months' proven operating history (stable break-even or better, real booking conversion data, real staffing-model performance) before committing capital to Venue 2. Expanding before proof-of-model risks compounding an unvalidated assumption across two sites.

**What replicates cheaply:** brand, service menu, Fresha configuration, staffing model/award structure, marketing playbook, onboarding/T&Cs documents — all reusable with minor edits.

**What does not replicate cheaply:** the WDP (or alternate pathology partner) relationship requires separate site approval per venue — WDP inspects each physical collection room individually, this is not a blanket approval. A second venue needs its own WDP conversation and its own collection room build, in full, regardless of Venue 1's track record with WDP.

**Candidate second-venue locations:** the location-scouting.md priority list (Osborne Park, Joondalup, Cannington, Myaree/Murdoch) already covers 4 corridors — whichever corridor is NOT chosen for Venue 1 becomes the natural Venue 2 candidate, since it avoids cannibalising Venue 1's catchment.

### 6. Expansion to Different Australian States

**This is materially harder than a second WA venue and should be treated as a Year 3+ consideration, not a near-term goal.**

Key differences from in-state expansion:
- **No WDP presence outside WA.** Each state has its own dominant pathology providers (e.g. Melbourne Pathology/Dorevitch in VIC, Douglass Hanly Moir/4Cyte in NSW, Sullivan Nicolaides in QLD) — an entirely new partnership negotiation is required per state, starting from zero relationship history
- **No brand recognition outside WA** — the referral-network engine (GP/midwife word-of-mouth) that makes Perth low-cost-of-acquisition does not exist interstate; marketing spend assumptions from the WA model don't transfer
- **State-based business registration and payroll tax thresholds differ** — though Fair Work awards are national, workers comp/insurance and state payroll tax registration are state-specific compliance items
- **Trust/company structure implications** — YETI Holding Trust's structure and Anthony's TPI pension protection would need re-verification for cross-state trading (accountant input required, not assumed safe)

**Recommendation:** treat interstate expansion as explicitly conditional on: (a) Venue 1 proven profitable for 12+ months, (b) at least one successful second WA venue demonstrating the model replicates, (c) a state-specific pathology partnership pre-negotiated before any lease is signed in that state (same "WDP first" discipline as Venue 1).

## Open Questions

1. Does Fresha's booking flow actually block a service selection once that AM cohort's line is full? Must be tested before launch, not assumed.
2. What is the realistic conversion rate from waitlist signup to confirmed paid booking? No data exists yet — see `pm-staffing-roster.md` waitlist section.
3. Is a Saturday shift (with penalty rates) worth modelling as a near-term profit lever, or reserved for later once Venue 1 is stable?
4. What relief-pool size is actually "safe" versus the current 1-per-line minimum? No incident data exists yet to calibrate this.
5. Is there appetite to model AM's 3rd-chair/10-client Scenario A now, or defer until Venue 1 is operating and real demand data exists?
6. ~~For interstate expansion: is there a specific state Anthony has in mind~~ **ANSWERED 2026-07-15:** Victoria, informally — no timeline attached, an early thought only. Logged here so it is not lost, not treated as a commitment.

## Definition of Done

- [ ] Fresha per-slot availability behaviour tested and confirmed before launch
- [ ] Waitlist conversion rate tracked from Week 13 onward (see `pm-staffing-roster.md`)
- [ ] Relief pool adequacy reviewed after first full month of live operations
- [ ] Venue 2 candidate corridor identified (by elimination, once Venue 1 site is chosen)
- [ ] Interstate expansion explicitly deferred with stated preconditions (this document) rather than left as an undated open ambition

---

## Assumptions Made

- Assumed 12 months of Venue 1 operating history is the right proof-of-model threshold before Venue 2 — this is a reasonable default, not a number Anthony has confirmed
- Assumed WDP-equivalent partnerships are required per-venue (not blanket) based on how pathology collection centre approvals generally work (per-site physical inspection) — consistent with what's already documented for Venue 1 in `pathology-partnership-brief.md`
- Assumed interstate expansion is a Year 3+ conversation, not sooner — flagged as Open Question 6 rather than assumed as fact, since Anthony hasn't stated a timeline

## Decisions Needed Before Work Begins

1. Confirm Fresha availability-blocking behaviour before launch (technical test, not a strategic decision — but blocking)
2. Confirm whether Saturday trading and AM 3rd-chair expansion should be actively planned now or deferred until Venue 1 is live
3. Confirm interstate ambition — genuinely open, or is there a target state/timeline in mind
