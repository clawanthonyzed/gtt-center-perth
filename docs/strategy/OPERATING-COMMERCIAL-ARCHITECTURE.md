# Operating + Commercial Architecture

**Date:** 2026-08-14 | **Status:** Current. Single consolidated document per explicit instruction — the strategic bridge between `docs/business-plan.md`, `docs/CURRENT-STATE.md`, `docs/strategy/*`, `docs/experience/*`, and `docs/floor-plan-concept.md`. No financial-model figures are changed here; no floor plan is drawn; no naming decision is touched. Every operating figure below is sourced to an existing document — this report translates founder direction into architecture, it does not generate new numbers.

---

## 1. Executive Summary

The founder has resolved five standing open questions: 18 GTT clients/day is the **design target**, not a revenue guarantee — the venue is built for the higher end rather than intentionally capped at 12. GTT is the real business, not a wellness venue with a test attached — the premium experience *is* the product, not a value-add on top of a clinical service. The ambition extends beyond one Perth venue to a second Perth site and eventual multi-city replication. AM and PM are structurally different businesses sharing one roof: AM is time-constrained by the blood-draw clock, PM is unconstrained and serves two roles at once — a real second revenue stream and the mechanism that turns one-off referred visitors into repeat, self-directed customers. This document translates those five decisions into an operating and commercial architecture: how the centre actually runs at 18/day, what the AM and PM menus should be built from, how the AM→PM flywheel is meant to work mechanically, what a future venue must physically provide, and what must be standardised versus left local when this concept is replicated. It resolves the open framing question left in `docs/strategy/STRATEGIC-REPORT.md` (Table 1 vs Table 2) in the founder's own terms: 18/day is the target, 12 was never the intended ceiling.

---

## 2. Founder Direction

Treated as current direction for everything that follows, not re-litigated:

1. **18 GTT clients/day is the target operating capacity**, not guaranteed daily revenue — design for the higher end.
2. **GTT is the core business.** The premium experience exists to disrupt the standard GTT/pathology experience, not to decorate it.
3. **The ambition is Perth flagship → second Perth site → other Australian cities** — the flagship must be designed with eventual replication in mind, without over-engineering for it now.
4. **AM is GTT-constrained**; the exact AM service list is not locked — classify confirmed vs proposed vs future, don't invent to fill a menu.
5. **PM is a normal premium wellness/beauty business** with no GTT-related time restriction, serving both as a material secondary revenue stream and as the retention/lifetime-value engine for GTT clients.
6. **The experience is the product.** Not generic luxury language — specific, describable mechanisms.

---

## 3. Business Model

Per `docs/strategy/BRAND-ARCHITECTURE.md`, restated in commercial terms: one venue, two operating models sharing infrastructure and brand.

- **GTT (core):** the mandatory clinical visit, reframed as a premium hospitality experience. This is the business's reason to exist and its primary acquisition channel — referral-gated, capacity-capped, non-discretionary for the client.
- **PM (secondary + retention):** a standalone, fully discretionary wellness/beauty business, open to any woman. It exists both as its own P&L line and as the mechanism that converts AM's one-off referred traffic into a self-directed, repeat customer base — see §8.
- **AM add-on services (supporting):** the wellness/beauty layer delivered inside the GTT window itself — not a separate business, a value-add constrained entirely by the clinical clock.
- **Third-party retail (supporting, currently unvalidated):** Gaia/Weleda/Mustela resale, pregnancy/maternity/baby-adjacent, explicitly not a boutique concept. Per the founder's direction for this phase, the canonical financial model treats ancillary/retail revenue as **A$0 in baseline P&L** — the ~A$25,000/yr figure discussed elsewhere in this repository is a placeholder outside the canonical baseline, not a modelled revenue line. See §14.

---

## 4. Customer Segments

Two segments, fully profiled in `docs/strategy/BRAND-STRATEGY-NAME-AGNOSTIC.md` — summarised here in commercial terms, not re-derived:

- **AM / referred:** a woman referred for a GTT at 24–28 weeks. She did not choose this appointment. Her relationship to the business starts as a captive audience for a clinical necessity — the entire commercial opportunity is converting that captivity into preference and, later, choice.
- **PM / self-directed:** any woman booking massage, nails, hair, or beauty for herself, pregnant or not, GTT client or not. She has zero patience for anything that reads as medical. Two distinct entry paths into this segment: women who never had a GTT here at all, and AM alumni who return by choice (§8).

---

## 5. GTT Operating Model (18 Clients/Day, Conceptual)

Built directly from the verified, programmatically-checked Table 1 schedule (`docs/scenario-c-sync-timetables.md` §0.6a) — not re-derived, translated into operational terms.

**Structure:** 2 collection chairs (A/B), synchronized starts, 9 pairs/day, one new pair admitted every 25 minutes from 07:00 to 10:20. Each individual client's own journey, regardless of which pair she's in, follows the identical fixed shape:

```
Arrival/check-in → Draw 1 (5 min) → Service 1 (45-min slot) → 10-min transition/turnover buffer
→ Draw 2 (5 min, exactly +60 min from her own Draw 1) → Service 2 (45-min slot) → 10-min buffer
→ Draw 3 (5 min, exactly +120 min from her own Draw 1) → Departure
```

Total on-site time per client: ~125 minutes of structured clinical/service time, plus arrival and departure — consistent with the ~2.5-hour window described in `docs/business-plan.md`.

**Why this matters operationally:** because pairs stagger every 25 minutes, at any given moment the venue has clients simultaneously in different phases — one pair drawing blood, another in Service 1, another in the transition buffer, another in Service 2, another departing. This is a continuous overlapping flow, not a batch of 18 identical appointments — reception, treatment staff, and phlebotomists are each working a rolling queue, not a single wave.

**Reception flow:** each pair is greeted, checked in by first name (no clipboard model, per `docs/experience/CUSTOMER-JOURNEY.md`), and handed the welcome/itinerary card before their first draw — this has to happen inside a ~5-10 minute window per pair to keep the 25-minute cadence intact.

**Treatment room / station utilisation:** the 10-minute buffer built into every block (§0.6's canonical model) is what makes room turnover work — it is simultaneously a clinical-timing buffer and a cleaning/reset window for the room or station the previous client just vacated. This is a real, already-engineered feature of the schedule, not a gap that needs a separate turnover allowance layered on top.

**Staff movement:** the 4-person Massage+Beauty pool, 2 Nails, and 2 Hair lines each work a rolling sequence of bookings across the day (confirmed at 3 bookings/staff/day at the 12-client volume, scaling proportionally at 18/day) — staff are not idle between clients within the committed model; downtime that does occur is filled per the Staff Downtime Protocol (`financial-break-even-staff.md`), sellable via advance booking where possible.

**Customer departure:** see §8 — the departure interaction is a genuine design priority for the AM→PM flywheel, not just a clinical sign-off. **REMOVED 2026-08-19, per Anthony's explicit decision: the specific "leaving box"/physical parting-gesture concept previously described here is NOT approved and must not appear in any forward-facing material.** No replacement mechanism has been designed yet — this remains an open design question for §8, not a solved one.

**PM transition and overlap:** PM's shift begins at 12:00, while the last AM pairs (Table 1's clients 17/18, Draw 3 at 12:20-12:25) are still finishing. This means AM and PM operate simultaneously for roughly the first 20-25 minutes of the PM shift — reception and any shared spaces (the GTT Lounge) need to handle both an AM client's departure ritual and a PM client's arrival at the same time, on the same day, in the same room. This overlap is a real, currently undocumented operational detail — flagged in §15 as needing a specific handover protocol, not assumed to resolve itself.

**PM standalone appointments:** run independently from 12:00-18:00, booked exactly like any premium wellness/beauty appointment, with no GTT-related constraint on duration or sequencing (§7).

---

## 6. AM Experience

### 6.1 Service Classification

Built from `docs/services-pricing-locked.md` Part A (the existing GTT-window menu), classified per this document's own instruction rather than simply reproduced:

**CONFIRMED / FOUNDER-INTENDED (already in the locked GTT-window menu, fits the 45-min slot structure cleanly):**
- Pregnancy massage — Express (30 min) / Standard (45 min)
- Facials — Express glow (30 min) / Signature pregnancy facial (45 min), plus stackable add-ons (10-25 min each: LED therapy, scalp massage, décolletage, hand/arm massage, jade roller, eye mask, lymphatic drainage, HA infusion, collagen mask, aromatherapy, brow wax+tint)
- Brows & lashes — brow wax/reshape (20 min), brow wax+tint (25 min), brow thread (15 min), brow lamination (45 min), lash tint (20 min), brow+lash combo (35 min), lash lift+tint (45 min)
- Hairdressing (GTT-window subset) — blowdry short/medium (30 min), blowdry long (45 min), haircut excl. colour (30-45 min), pregnancy-safe hair mask+blowdry (45 min), braiding/hair up (30-45 min)
- Classic manicure (30 min), Express pedicure (30 min), Gel manicure (45 min), Spa pedicure (45 min)

**PROPOSED (real services in the menu, genuinely ambiguous fit — flagged, not silently resolved):**
- French gel manicure (50 min), Gel pedicure (50 min), French gel pedicure (55 min) — `services-pricing-locked.md`'s own nail-service table header states "GTT Window: Services under 60 min only," which is inconsistent with the 45-min slot structure every other GTT-window service in this document respects. This is a real, unresolved contradiction inside the existing source document, not introduced here — see §15.
- An AM-specific "push toward package" sales strategy analogous to PM's (§9) — PM has one, AM does not yet.

**NOT OFFERED DURING GTT (explicit, already decided):** spray tan (not on test day for pregnant clients), hair colour services (60 min+, chemical), eyelash extensions (90 min+), belly casting, cut+blowdry (60 min), scalp treatment+blowdry (50 min), mani+pedi combo (80+ min), acrylic/SNS nail sets (75-90 min) — all correctly routed to PM/standalone-only in the source document.

**FUTURE (explicit, not launch scope):** lactation consultant, GDM dietitian sessions, prenatal yoga, pelvic floor physiotherapy, hypnobirthing (all listed "not at launch" in `services-pricing-locked.md`); 3D keepsake ultrasound (`docs/business-plan.md` §7).

### 6.2 Package Logic, Not Just a List

**The operating logic, made explicit rather than assumed:** the canonical schedule (§5) gives every client two genuinely identical 45-minute service slots — this is a real structural fact, not a coincidence. Package 1 (A$250, fixed 2×30min) uses less than the full slot capacity in both windows; Package 2 (A$300, flexible 2×45min / 1×45+1×30 / 2×30) can fill either or both slots completely. Because both slots are equally sized under the current canonical model, there is no operational reason a 45-minute service must go in Slot 2 rather than Slot 1 — that constraint existed under an earlier, since-superseded scheduling model (`scenario-c-sync-timetables.md` §0.5) and does not apply to the current one. This is worth stating plainly because it removes a booking-system rule that would otherwise need to exist.

**Which services create the strongest perceived value in the AM window specifically:** the signature facial and standard massage (both fill a full 45-min slot, both are the highest-priced single items in their category, both align with the founder's "experience is the product" standard) — these are the services the AM package structure should be built to showcase, not the fastest or cheapest options.

---

## 7. PM Experience

### 7.1 Duration-to-Service Architecture

No GTT-related time constraint — durations map to service type, not to a clinical slot:

| Duration | Natural fit (from `services-pricing-locked.md` Part B and standalone-only notes in Part A) |
|---|---|
| 30 min | Express/entry services: classic manicure, express pedicure, brow services, short blowdry |
| 45 min | Standard-tier services: standard massage, signature facial, gel manicure/pedicure, long blowdry |
| 60 min | Cut+blowdry, single-process colour (lower end), belly cast, standalone 60-min massage |
| 90 min | Half foil highlights (lower end), classic lash set, PM Refresh-style two-service packages |
| 120+ min | Full foil highlights, balayage, volume lash sets |

### 7.2 Package vs. Standalone

**Should be packaged:** short, complementary two-service combinations deliverable by one cross-trained practitioner — this is exactly what the existing PM Duo/Refresh/Glow structure (`docs/pm-package-structure.md`) already does, and the operating logic behind it should be read as the template for any future PM package, not just those three: pair services within one practitioner's dual qualification (Massage+Beauty is the confirmed pairing) so a package adds revenue per visit without adding staff-coordination cost.

**Should remain standalone:** single-specialist, longer-duration services — hair colour, lash extensions, belly casting. These require one dedicated line for the full duration and don't naturally combine with a second service inside a single visit; packaging them would mostly just rename a booking, not add value.

### 7.3 Repeat Likelihood, Perceived Luxury, Margin, Retention Value

Distinguished explicitly rather than treated as one dimension:

- **Most likely repeat services:** manicure/pedicure (short natural refresh cycle), blowdry (event-driven, recurs independent of any single occasion), massage (habitual self-care pattern) — these are the services a PM booking cadence gets built around.
- **Highest perceived luxury:** signature facial, standard/extended massage, hair colour/balayage, lash extensions — the services most likely to be the subject of the "you HAVE to go there" sentence (`docs/strategy/STRATEGIC-REPORT.md`'s closing question).
- **Strongest margin potential (by service type, not by invented number):** brow/lash services and nail add-ons generally carry lower material cost relative to price than colour or extension services — a directional observation from the existing price/duration table, not a modelled margin figure.
- **Strongest GTT-retention value:** the services with the shortest natural repeat cycle (nails, blowdry) are structurally the best first re-booking candidates, because they ask the least of a woman who is testing whether this centre is worth returning to for something she chose herself (§8) — a large first standalone booking (colour, extensions) is a worse retention bet precisely because it asks for more commitment before trust is re-established outside the clinical context.

No pricing is proposed here beyond what already exists in `docs/services-pricing-locked.md` and `docs/pm-package-structure.md` — both cited, neither extended.

---

## 8. AM→PM Customer Flywheel

Per explicit instruction: no conversion percentage is assumed or invented here. This section builds the system, drawing on the mechanisms already established in `docs/experience/RETURN-LOOP.md` and `docs/experience/CUSTOMER-JOURNEY.md`, reframed against this brief's specific questions.

**REMOVED 2026-08-19, per Anthony's explicit decision:** the "leaving box"/physical parting-gesture concept previously described in this section (as the primary AM→PM conversion mechanism) is NOT approved and must not appear in any forward-facing material. The paragraphs below have been rewritten to remove that specific mechanic — the underlying question (why/how does a GTT customer return) remains open, without an invented replacement mechanism.

**Why would a GTT customer return?** Not because she was asked to — because the overall AM experience overturned her expectation of what this appointment would be, and something specific and describable she experienced created its own reason to come back on a day she chooses. **The exact mechanism for this (what happens at departure specifically) is an open design question, not yet solved — no specific concept is proposed here.**

**What would she remember?** One or two concrete, sensory-specific things, not a general impression — the welcome-card itinerary that meant she never had to ask "what happens next," and the specific service she had (a real massage, not "some pampering"). What else contributes to a memorable departure remains an open design question.

**What would she discover?** That the PM business exists on its own terms — not during her GTT visit as an upsell, and not via a later generic marketing message. Per `RETURN-LOOP.md`: upselling during the clinical visit itself undoes trust at exactly the point it's being built. Exactly when/how this discovery happens is not yet designed.

**What gives her a reason to book?** A single, specific line naming one thing she could book next — not a menu, not "come back soon." Specificity is what converts a pleasant memory into an action.

**When does that invitation occur, and who makes it?** Not yet designed — the prior framing (folded into a physical departure object) is removed. This needs a genuine design solution that does not rely on a physical gift/gesture mechanic.

**What does she receive?** One genuinely useful follow-up message once her results reach her doctor — real information, not marketing, with the PM mention riding alongside it once, briefly, per `RETURN-LOOP.md`'s explicit sequencing rule (usefulness first, invitation second). This is the one concrete mechanism that remains valid and approved.

**What service is most likely to become her first PM booking?** Per §7.3: a short, low-commitment, high-repeat-cycle service (nails, blowdry) — something that asks little and can be booked on impulse, not a 90-minute colour appointment.

**What creates a second PM booking?** Staff continuity and recognition on the first PM visit (`RETURN-LOOP.md`: "being remembered by name and treatment history... converts 'a nice business' into 'my place'") — this is an operations/rostering commitment, not a marketing one.

**Data needed before a real conversion assumption can be set (per this document's instruction, no percentage assigned):**
- Actual AM visit count and actual PM first-booking count, matched at the individual-client level (requires the booking system to track this relationship, which is not yet confirmed as built — see §13, §15).
- Time-to-first-PM-booking distribution (does she return in 2 weeks or 6 months — materially different retention economics).
- Which specific AM service (or none) precedes the first PM booking, to test the §7.3 hypothesis with real data rather than logic alone.
- Second-booking rate specifically among AM-converted PM clients, isolated from PM clients who never had a GTT here — needed to know whether the flywheel actually produces durable repeat customers or just a single bonus visit.

**Future model structure (bands only, per instruction — no percentages assigned to any band):** 0% / Conservative / Base / Strong / Exceptional — to be populated once the data above exists, not estimated now.

---

## 9. Service Architecture

Synthesised from §6/§7 rather than restated: AM's menu is a subset of the full service catalogue, filtered by a hard constraint (must fit inside a 45-minute slot, cannot require GTT-incompatible positioning or chemicals); PM's menu is the full catalogue plus longer-duration/higher-commitment services that have no reason to exist inside a clinical visit. The two menus share staff (dual-qualified treatment lines work both shifts) and share a brand voice/booking system, but are structurally different products sold to the same person at different points in her relationship with the centre — this dual-menu structure is itself one of the things worth standardising on replication (§16).

---

## 10. Venue Functional Requirements

A functional brief for a future floor plan, not a floor plan — cross-referenced against `docs/floor-plan-concept.md`'s existing Room Schedule (PARKED 2026-07-29, pending a real architect) rather than reinvented, and explicitly checked against the 18/day target's own peak-concurrency numbers.

**A genuine finding worth stating plainly:** the existing day-one committed floor plan (4 treatment rooms, 4 nail stations, 4 hair chairs) was sized independently of this specific 18-client analysis, but happens to match it closely. Table 1's own peak-concurrency figures (`scenario-c-sync-timetables.md` §0.3) show Massage, Beauty, Nails, and Hair each peak at 2 simultaneous clients in the 8-staff no-pooling structure — meaning up to 2 concurrent massage + 2 concurrent beauty clients need treatment-room capacity at once (4 rooms), alongside up to 2 concurrent nail clients (of 4 stations) and 2 concurrent hair clients (of 4 chairs). The existing room counts are not oversized for 18/day; they're the right order of magnitude for the model already in place — a genuine cross-check that hadn't been stated explicitly in either source document until now.

| Requirement | Classification | Basis |
|---|---|---|
| Blood Collection Room, solid walls, 2 chairs | **MUST HAVE** | The only genuinely clinical space; non-negotiable per `floor-plan-concept.md` |
| Reception with name-based (not clipboard) intake capability | **MUST HAVE** | `docs/experience/CUSTOMER-JOURNEY.md`'s reception model |
| GTT Lounge, capacity for overlapping AM/PM occupancy | **MUST HAVE** | §5's AM/PM transition overlap finding — not previously flagged as a room-capacity requirement |
| 4 treatment rooms, curtain-partitioned, each fit-out to support BOTH massage and facial/beauty delivery | **MUST HAVE** | Matches Table 1 peak concurrency (above); flexible fit-out needed because staff are pooled/dual-qualified, not room-specialist — see §15 for the labelling question this raises |
| 4 nail stations with LEV extraction | **MUST HAVE** | Matches Table 1 peak concurrency; mandatory WorkSafe WA compliance regardless of volume |
| 4 hairdressing chairs + 2-3 backwash | **MUST HAVE** | Matches Table 1 peak concurrency |
| Cafe/refreshments counter (glucose-drink dispensing) | **MUST HAVE** | Core GTT protocol function, not an amenity — `floor-plan-concept.md` |
| Staff room, clean linen/storage, dirty linen/biohazard, patient WC (accessible + standard), staff WC, circulation ≥1.5m | **MUST HAVE** | Baseline compliance/operational requirements, unaffected by 12 vs 18 client volume |
| Retail display (reception-adjacent, small footprint) | **SHOULD HAVE** | Retail is a supporting, currently-unvalidated revenue line (§3) — a footprint should exist, but not be over-invested given §3's A$0-baseline direction |
| Acoustic separation between the Blood Collection Room and guest-facing treatment/lounge areas | **SHOULD HAVE** | Not explicitly specified in `floor-plan-concept.md`; a reasonable inference from the "no clinical signalling outside the one room that needs it" principle (`docs/strategy/BRAND-ARCHITECTURE.md`) — flagged as a should-have, not asserted as already decided |
| A 5th/6th treatment-room, nail, or hair capacity buffer for days that exceed 18 or run two pairs behind schedule | **NICE TO HAVE** | Not required by the committed model; would only matter if real demand consistently exceeds the design target |
| Spray tan booth | **FUTURE** | Explicitly moved to Phase 2, `floor-plan-concept.md` |
| A 3rd phlebotomy chair / collection bay | **FUTURE** | Scenario D growth path, not committed |
| Growth-reservation Treatment Rooms 5/6 | **FUTURE** | Already reserved as shell space in `floor-plan-concept.md`, not staffed or costed day-one |

---

## 11. Staffing / Capacity

Using only already-modelled figures (`docs/CURRENT-STATE.md` §4/§5) — no new wage rates invented, missing inputs flagged explicitly.

**The central staffing finding, worth restating in this document's own terms:** headcount required for clinical/treatment delivery is **identical at 12 and 18 clients/day** — 2 phlebotomists + 8 dual-qualified treatment staff (4 Massage+Beauty pool + 2 Nails + 2 Hair). This is precisely why "design for 18" (the founder's direction, §2) does not require a different staffing commitment than the more conservative 12-client model — the AM Direct Labor figure (A$48,254.67/month, FTE-based) is unchanged either way. Saturday labor scales proportionally with the longer 18-client AM day (hours-based costing), a real but modest cost delta already captured in `docs/CURRENT-STATE.md` §5.

**Reception/hospitality:** 1 Receptionist/Manager, split shift covering AM open + PM administrative window (`docs/business-plan.md` §5).

**PM staff:** 4 dedicated casual hires (1 each: massage, hair, nail, beauty), cross-shift qualified with AM staff, hours-based costing (not blanket shift presence) — `docs/pm-staffing-roster.md`.

**Relief/backup pool:** 3 dual/cross-trained roles (Massage+Beauty, Nail, Hair) + 1 relief phlebotomist, added specifically to cover leave without reducing same-day capacity below the safe minimum.

**Venue Manager:** 1, critical-path hire, recruitment gated on venue confirmation — not yet begun.

**Overlapping shifts / peak periods:** AM runs 07:00-~12:48 (last departure, Table 1); PM runs 12:00-18:00 — meaning AM and PM staff overlap on-site for roughly the first 45-50 minutes of the PM shift (§5's transition finding). This overlap window is where reception/hospitality staffing needs the most careful rostering, since one person is unlikely to cover both an AM departure ritual and PM arrivals cleanly — flagged as a missing input, not yet resolved in any staffing document.

**Missing inputs, flagged rather than estimated:**
- Real, current wage rates — every figure in the model is 13+ months stale and two internal documents disagree on base rates (`docs/VERIFICATION-TRACKER.md` items 17-18).
- Award penalty-rate percentages (Saturday/Sunday/PH) — three internal documents disagree (item 16).
- Whether the AM/PM reception overlap (above) requires a second staff member during the transition window, or can be absorbed by existing rostering — not modelled anywhere.

---

## 12. Revenue Architecture

Per the founder's explicit structure for this phase:

- **CORE — GTT:** AM package sales (Package 1 A$250 / Package 2 A$300). At the 18-client target, modelled Total Revenue is A$157,792.16/month (historical/inherited methodology) or A$155,215.80/month (canonical days-based methodology, `docs/architecture/CANONICAL-REVENUE-METHODOLOGY.md`) — both already-modelled figures, neither restated as new.
- **SECONDARY — PM wellness/beauty:** individual a-la-carte (~A$95/session average, modelled, unvalidated by real bookings) plus set/fixed packages (PM Duo/Refresh/Glow, direction confirmed, final pricing not yet signed off).
- **SUPPORTING — AM add-on services:** priced in `docs/services-pricing-locked.md` (LED therapy, paraffin wax, nail art, etc.) but **no uptake/attach-rate assumption exists anywhere in the financial model** — these are real, priced, bookable items with zero revenue-line representation in the current P&L. Flagged as a genuine gap, not assumed to be immaterial.
- **SUPPORTING — Third-party retail:** Gaia/Weleda/Mustela resale. **Per founder direction for this phase, treated as A$0 in the canonical baseline P&L.** The ~A$25,000/yr figure discussed in `docs/VERIFICATION-TRACKER.md` item 10 remains outside the canonical baseline and unvalidated — not modified here, and not to be read as contradicting this section.

---

## 13. Financial Model Dependencies

Classified exactly as instructed — describing what exists and what's missing, not filling gaps:

| Assumption | Status |
|---|---|
| 18/day GTT target (schedule, headcount, capacity) | **ALREADY MODELLED** — `scenario-c-sync-timetables.md` §0.6a, `docs/CURRENT-STATE.md` §1/§5, solver-verified |
| Actual expected utilisation (real booking fill rate vs the 18/day ceiling) | **NEEDS VALIDATION** — no real trading data exists; referral pipeline (§4 of `docs/strategy/STRATEGIC-REPORT.md`) is the binding constraint, not modelled as a fill-rate probability |
| AM add-on uptake | **NEEDS NEW ASSUMPTION** — priced items exist, no attach-rate assumption exists anywhere (§12) |
| PM capacity | **ALREADY MODELLED** — ~16 sessions/day at ~50% utilisation of theoretical 4-line capacity, itself an unvalidated planning estimate, not real demand data |
| AM→PM conversion | **NEEDS NEW ASSUMPTION** — explicitly and deliberately not estimated in this document (§8); data collection prerequisites defined, no percentage assigned |
| PM repeat rate (beyond first conversion) | **NEEDS NEW ASSUMPTION** — no repeat-rate or lifetime-value modelling exists anywhere in this repository |
| Service mix (which services PM demand actually splits across) | **NEEDS VALIDATION** — `pm-staffing-roster.md` explicitly assumes an even split across the 4 PM lines "to be corrected once real booking data shows which services are more popular" |
| Appointment duration | **ALREADY MODELLED** — durations are documented per service in `services-pricing-locked.md`, used directly in §6/§7 above |
| Staff requirements | **ALREADY MODELLED** — fixed at 8 treatment + 2 phlebotomist across both 12 and 18-client volumes (§11) |
| Retail | **NOT YET RELEVANT** to the canonical baseline — treated as A$0 per founder direction (§3, §12); the unvalidated A$25,000/yr figure sits outside the model this document is built against |

No figure in `docs/CURRENT-STATE.md` or `docs/profit-loss-tables.md` is modified by this classification.

---

## 14. Scalability Architecture

Defined against what the flagship must prove, not a national rollout plan:

**STANDARDISE:**
- The GTT experience mechanics themselves — the welcome/itinerary card, the no-interrupt rule, the synchronized-chair scheduling logic (§5) as a transferable operating pattern, not just a Perth-specific solution.
- Service standards — the AM/PM dual-menu logic (§9): AM constrained by clinical timing, PM unconstrained, same underlying service catalogue split by duration/commitment rules.
- The customer journey stages and their emotional/design intent (`docs/experience/CUSTOMER-JOURNEY.md`).
- Hospitality principles — name-based reception, no clinical signalling outside the one room that needs it. (The departure interaction is a separate, currently unsolved design question — see §8; no specific "leaving gesture" concept is approved.)
- Staff hiring pattern — dual-qualification preference (Massage+Beauty) as the default recruiting model, not a Perth-specific workaround.
- Technology — the booking system's package/bundle configuration and (once built) the AM→PM tracking capability §8 depends on.
- Brand voice and positioning (`docs/strategy/BRAND-STRATEGY-NAME-AGNOSTIC.md`) — name-agnostic by design already.
- Package logic — the structural relationship between slot duration and package composition (§6.2), not the specific current prices.
- Operating procedures — booking-driven rostering (roster to confirmed bookings, not a calendar assumption), the Staff Downtime Protocol.

**FLEX:**
- The physical premises and room layout — local to each site's real floor plate.
- Local staffing — real wage rates, local award interpretation, local hire availability.
- Local service mix — regional demand may weight differently across massage/nails/hair/beauty.
- Local demand and referral pipeline strength.
- **Local pathology partnerships — the single most consequential replicability dependency.** The entire Option A clinical model (`docs/business-plan.md` §3) requires a NATA-accredited local partner willing to operate the rental-collection-room arrangement WDP is being asked to provide in Perth. This is not guaranteed to exist, on comparable terms, in every target city — a genuine, currently untested assumption behind the whole expansion ambition.

**FUTURE:**
- Centralised systems (shared booking/CRM/customer data across venues — the infrastructure §8's flywheel data needs would eventually feed).
- A training academy, once the dual-qualification hiring/training pattern is proven at one site.
- Membership (raised speculatively in both Claude Design explorations, not evaluated here).
- Additional service categories beyond the current four treatment lines.

**What the flagship must prove before any of the above is worth pursuing:** that the 18-client operating model delivers both its scheduling promise (zero collisions, on-time departures) and its emotional promise (the "unexpectedly lovely" reaction, §8) at real volume, not just in a solver; that the AM→PM flywheel produces measurable, durable repeat business once the data in §8 exists; that a local NATA-accredited pathology partnership is achievable on workable commercial terms somewhere other than the one relationship (WDP) currently being negotiated; and that unit economics hold up against real wage rates, real insurance costs, and real referral-pipeline fill rates (`docs/strategy/STRATEGIC-REPORT.md` §12) rather than the currently-modelled planning assumptions.

---

## 15. Unresolved Decisions

- **Nail-service duration conflict:** `services-pricing-locked.md`'s own GTT-window nail table header ("under 60 min only") contradicts the 45-min slot structure every other GTT-window service respects — French gel manicure (50 min), gel pedicure (50 min), and French gel pedicure (55 min) don't cleanly fit either rule as currently written. Needs a founder or Venue Manager decision: shrink these to fit 45 minutes, exclude them from the GTT window, or confirm the 60-minute framing is intentional and the slot structure should flex for nails specifically.
- **AM add-on revenue** is priced and bookable but has no uptake assumption anywhere in the financial model (§12, §13).
- **AM package-steering strategy** does not yet exist, unlike PM's explicit, documented "push toward package" approach (§6.2).
- **PM package pricing** remains unsigned-off (`docs/pm-package-structure.md`).
- **Treatment-room labelling vs. staff pooling:** the floor plan labels rooms "Massage" and "Facial/Beauty," but staff are hired and rostered as a pooled, dual-qualified group — rooms should probably be fit-out generically enough that any of the 4 pool staff can use any of the 4 rooms, rather than rigidly split 2/2 by label. Not yet decided.
- **AM/PM reception overlap** (§5, §11) — no staffing or process answer yet exists for the ~45-50 minute daily window where AM departures and PM arrivals happen simultaneously.
- **AM→PM data collection mechanism** — whether the booking system currently links an individual client's AM visit to her later PM bookings is not confirmed anywhere in this repository; §8's entire data-needs list depends on this existing or being built.
- **Multi-city pathology-partner replicability** (§14) — untested outside the current WDP relationship.
- **Venue location** remains the top blocking item across every strategic document produced so far — unaffected by this document's scope, restated here only because every other unresolved item is downstream of it.

---

## 16. Recommended Next Phase

- Resolve the nail-service duration conflict (§15) — cheap, fast, and currently a live contradiction in the client-facing menu logic.
- Define the AM/PM reception handover process for the daily overlap window (§5, §11) — an operational gap with real day-one consequences, independent of the venue timeline.
- Begin designing the specific data fields the booking system needs to capture to eventually answer §8's AM→PM conversion questions (which AM service preceded a PM booking, time-to-first-booking, second-booking rate) — this doesn't require real customers yet, only that the system is built to capture the right thing once they exist.
- Decide the AM add-on uptake and PM service-mix assumptions' priority for validation once real bookings exist — both currently unmodelled, both cheap to start tracking from day one.
- Continue venue search — still the single highest-leverage unblock across the whole venture, unchanged by this document.

---

## The Central Operating Challenge

**"How do we build a GTT centre capable of handling 18 clients a day while making each woman feel like she received a highly personal, premium experience rather than being processed through a high-volume medical service?"**

Working backwards from it, two things in this document do the actual work: first, the schedule itself is engineered so that no client experiences the venue as a batch — she has her own fixed 125-minute shape (§5), and the fact that eight other women are moving through the same building at staggered intervals never surfaces to her directly. Second, staffing capacity for 18/day is already identical to 12/day (§11) — meaning the "high-volume" side of the question is solved on paper without asking any single staff member to serve more people per hour than the schedule already assumes; nobody has to rush to make 18 work. The welcome/itinerary card (§6) is deliberately not volume-sensitive — it costs the same, personal amount whether she is client 1 or client 18 that day; the departure interaction (§8) remains an open design question, not yet solved (the previously-described "leaving gesture" concept is REMOVED, not approved). The honest remaining risk is not the schedule or the staffing model — both are already verified — it's whether the *feeling* of individual attention actually survives contact with a fully-booked real morning, which is precisely why §16's first two recommendations (the reception handover gap, the nail-duration conflict) matter now, before volume, rather than being discovered at it.
