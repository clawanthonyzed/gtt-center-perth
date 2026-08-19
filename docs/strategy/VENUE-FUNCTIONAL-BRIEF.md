# Venue Functional Brief

**Date:** 2026-08-14 | **Status:** Current. Single consolidated document, per instruction. Translates the verified 18-client business model (`docs/strategy/OPERATING-COMMERCIAL-ARCHITECTURE.md`, `docs/strategy/18-CLIENT-OPERATIONAL-STRESS-TEST.md`, `docs/strategy/18-CLIENT-COMMERCIAL-STRESS-TEST.md`) into physical venue requirements. This is a **functional business brief**, not an architectural drawing, a locked venue, a Perth suburb choice, or a regulatory determination. No financial model, pricing, business plan, naming, service menu, or `CURRENT-STATE.md` figure is modified here.

**Classification used throughout:** every requirement below is tagged **A. CONFIRMED**, **B. STRONGLY IMPLIED**, **C. DESIGN RECOMMENDATION**, or **D. UNKNOWN/REQUIRES VALIDATION**. Where clinical, pathology, building, accessibility, fire, plumbing, waste, or infection-control requirements need professional confirmation, this is stated explicitly — nothing here is legal or regulatory advice.

---

## 1. Founder Decisions — Locked, Not Reopened

18 clients/day is the design target (12/day downside only); every AM service is 45 minutes or less, absolute; PM standard bookings begin 12:30, with 12:00-12:30 a soft (not closed) transition; GTT is the core business, PM is the secondary revenue + retention engine; the venue must read as a premium women's wellness destination that happens to deliver an exceptional GTT experience, not a clinic with beauty services attached.

---

## 2. Source Basis

This brief is built from a fresh read of: `docs/business-plan.md`, `docs/CURRENT-STATE.md`, `docs/strategy/STRATEGIC-REPORT.md`, `docs/strategy/OPERATING-COMMERCIAL-ARCHITECTURE.md`, `docs/strategy/18-CLIENT-OPERATIONAL-STRESS-TEST.md`, `docs/strategy/18-CLIENT-COMMERCIAL-STRESS-TEST.md`, `docs/experience/CUSTOMER-JOURNEY.md`, `docs/experience/RETURN-LOOP.md`, `docs/strategy/BRAND-ARCHITECTURE.md`, `docs/strategy/PREMIUM-POSITIONING.md`, `docs/scenario-c-sync-timetables.md`, `docs/floor-plan-concept.md` (the existing room-schedule/compliance document — **PARKED 2026-07-29**, pending a real architect, but its room counts, compliance findings, and sqm figures remain valid inputs), and relevant `data/canonical/` records. Existing room counts and compliance findings are validated against the current model, not rebuilt from scratch.

**CORRECTION, 2026-08-14 — a real source document was missing from the list above.** `docs/location-scouting.md` was not read when this brief was originally written, and it contains an explicit, existing parking requirement ("Ample parking — non-negotiable... Minimum 8–10 dedicated or immediately adjacent off-street parking spaces") that directly contradicts this brief's original §13/§18/§22 claims that no source document addresses parking. Corrected in place at each of those three locations — see §13, §18, §22.

---

## 3. Functional Program

Organised by the guest and staff journey, cross-referencing `docs/experience/CUSTOMER-JOURNEY.md` rather than re-deriving it.

**Entry/Arrival:** street-visible but deliberately under-signed entrance (**C**, per `docs/strategy/PREMIUM-POSITIONING.md`'s restraint principle) → reception with sightline to the door (**A**, `floor-plan-concept.md`) → orientation/welcome (name-based, no clipboard, **A**, `CUSTOMER-JOURNEY.md`) → GTT Lounge/waiting (**A**) → accessible arrival path for prams/mobility aids (**A**, see §13).

**GTT:** check-in → Lounge wait/preparation → Blood Collection Room (Draw 1/2/3) → AM treatment service (massage/beauty/nails/hair, ≤45min, **A**, locked rule) → post-draw hospitality/departure ritual (**A**, `CUSTOMER-JOURNEY.md`'s highest-leverage moment) → clinical storage/waste handling (**A**, `floor-plan-concept.md`).

**AM wellness/beauty:** delivered inside the same treatment rooms/nail/hair stations used for GTT-window services — not a separate physical zone (**A**, confirmed by the existing room schedule and validated against Table 1's peak concurrency in `docs/strategy/18-CLIENT-OPERATIONAL-STRESS-TEST.md` §9).

**PM wellness/beauty:** same physical spaces, longer/varied durations (30-120+min, no ceiling), independent booking flow from 12:30 (**A**, locked rule).

**Staff:** arrival/changing, staff room (break, handover, lunch), lockers, staff WC, administration — largely as already specified in `floor-plan-concept.md`, revisited in §5/§13 against the 18-client staffing model.

**Back of house:** clean linen, dirty linen/biohazard, consumables storage, retail stock (small), deliveries — as already specified.

---

## 4. Room Requirements — Validated Against 18/Day, Not Redesigned

The existing day-one room schedule (`floor-plan-concept.md`) specifies 4 treatment rooms, 4 nail stations, 4 hairdressing chairs. This brief does not redesign these — it validates them.

**Validation finding (A, confirmed by cross-reference to already-completed analysis):** `docs/strategy/18-CLIENT-OPERATIONAL-STRESS-TEST.md` §9 already established that peak concurrency per line (Massage, Beauty, Nails, Hair) is 2 concurrent clients at the 18-client target — identical to the 12-client model, because treatment/phlebotomist headcount doesn't change with volume. **The existing 4/4/4 fixture counts remain appropriate for 18/day** — they were sized independently of this specific volume, but happen to sit at almost exactly the right order of magnitude (roughly 2x the actual peak-concurrency requirement per line), which is genuinely useful slack, not waste (see §11).

| Category | Minimum | Preferred | Ideal | Basis |
|---|---|---|---|---|
| Blood Collection Room | 1, 2 chairs, solid walls | Same, +vasovagal recliner space | Same, + confirmed room-level wheelchair accessibility | **A** — `floor-plan-concept.md`, 2026-08-06 gap findings |
| Treatment rooms (massage/beauty) | 4, curtain-partitioned | 4 + 2 growth-reservation shells | 4 + 2 growth reservations, fit out generically (not labelled Massage vs Beauty) | **A** minimum count; **C** generic fit-out — see §5 flexibility discussion |
| Nail stations | 4, open-plan, LEV | Same | Same, LEV method confirmed by contractor pre-fit-out | **A** count; **D** LEV method — genuine open item, `floor-plan-concept.md` |
| Hair chairs | 4, open-plan, 2 backwash | 4, 3 backwash | Same | **A** count; **C** 3rd backwash |
| GTT Lounge seating | 8 reclining chairs (existing design principle) | Re-checked against real peak occupancy — see below | Sized to the re-checked figure | **A** existing spec; **D** — see the new finding immediately below |
| Reception | 2 workstations | + small back-office/admin nook | Dedicated Venue Manager work area | **A** workstations; **C** back-office — not itemised anywhere in the existing floor plan |
| Staff room | 1, 10sqm | Re-checked against transition-period break load | Larger if the AM/PM reception-overlap mitigation (§8) requires a second body on-site | **A** existing; **D** — see §8 |

**A genuinely new finding this brief surfaces, not previously computed anywhere in this repository:** the existing GTT Lounge design principle ("seats 8 simultaneously... at minimum, all originally-specified 8 in the lounge at once") itself flags this as unresolved against the 18-client model. Working through Table 1's actual pair-overlap timing (`docs/scenario-c-sync-timetables.md` §0.6a — each client is on-site roughly 125-133 minutes; pairs enter every 25 minutes) shows **up to 5 pairs (10 clients) can be simultaneously on-site at the mid-morning peak** (e.g. around 09:30-09:55), materially more than the 6 found in the operational stress test's 11:30-13:00 tail-window analysis, and more than the Lounge's original 8-seat assumption. **However, most of that on-site time is spent in the Blood Collection Room or a treatment/nail/hair station, not the Lounge itself** — the Lounge's actual peak occupancy (arrival wait plus the two 10-minute buffer transitions per client) is very likely lower than the full 10-person on-site peak, but this brief cannot state a precise figure without a proper occupancy-timeline simulation. **Flagged as D — requires validation** before Lounge seating count is finalised; treat "8" as a floor, not a confirmed ceiling.

---

## 5. Room Flexibility

- **Could a treatment room serve massage + beauty?** Yes, and should — staff are hired and rostered as a dual-qualified pool (`docs/CURRENT-STATE.md` §4), not room-specialists. The existing floor plan labels rooms "Massage" and "Facial/Beauty" with slightly different fixtures (1 sink vs 2, per the Skin Penetration Code findings, §12) — this brief recommends (**C**) fitting all 4 rooms to the more conservative 2-sink Facial/Beauty spec where cost allows, so any of the 4 pool staff can use any room, removing a real constraint flagged but not resolved in `docs/strategy/OPERATING-COMMERCIAL-ARCHITECTURE.md` §15.
- **Could a hair area support multiple service types?** Already the case — hair chairs are a single-purpose, open-plan zone; no change recommended.
- **Could PM use areas differently from AM?** Yes — PM's longer/varied durations (§16) use the identical physical rooms/stations, just booked for longer blocks; no separate PM-only zone is implied anywhere in the source documents.
- **Could rooms be dual-purpose across AM/PM?** Already the model — same spaces, different booking rules by time of day.
- **Could future services be accommodated?** The 2 growth-reservation shells (Massage/Beauty) already exist for this purpose (**A**, `floor-plan-concept.md`); no additional space is recommended beyond that without a specific new service being confirmed first.

---

## 6. Floor Area

Not an arbitrary number — derived from the existing, itemised room schedule (`floor-plan-concept.md`), validated against the 18-client model, with this brief's own additions clearly separated and labelled as new.

| Tier | Area | Basis |
|---|---|---|
| **MINIMUM FUNCTIONAL** | **~239-242sqm** | Day-one committed room schedule (`floor-plan-concept.md`), already validated against 18/day peak concurrency (§4). The +3sqm allows for the vasovagal recliner gap found 2026-08-06, not yet incorporated into the original 18sqm Blood Collection Room target. |
| **PREFERRED** | **~262sqm** | Day-one + the 2 Massage/Beauty growth-reservation shells — space only, not staffed/costed, but present from Day 1 so a second Perth site or added treatment capacity doesn't require relocating the flagship (directly serves the replication ambition, §17). |
| **IDEAL FLAGSHIP** | **~280-290sqm** (business-planning estimate, not architectural) | Preferred (262sqm) + a dedicated Venue Manager back-office/admin nook (~6-8sqm, not itemised anywhere in the existing plan) + Lounge seating headroom pending the §4 occupancy-validation finding (~8-10sqm allowance) + modest staff-room headroom for transition-period breaks (~4-6sqm). |

**Component breakdown (day-one, ~239sqm basis):** Reception 15sqm, GTT Lounge 35sqm, Blood Collection Room 18sqm, 4 treatment rooms 46sqm, Nail Station Area 32sqm, Hairdressing Area 52sqm, Cafe/Refreshments 8sqm, Staff Room 10sqm, WCs (accessible + standard + staff) 15sqm, Linen/waste storage 10sqm, Circulation 16sqm — full detail in `floor-plan-concept.md`'s Room Schedule, not reproduced line-by-line here to avoid drift between two copies of the same figures.

**Explicit assumptions:** this estimate assumes the existing per-room sqm figures remain valid (they were independently re-derived from `floor-plan-v3.svg`'s dimensioned figures, per that document's own changelog); it does not account for tenancy shape inefficiency (an irregular floor plate could require more gross leasable area than this net-functional estimate); and it is a business-planning estimate, explicitly not a substitute for a real architect's assessment of any specific candidate property.

---

## 7. Customer Flow

**GTT customer:** Arrive → Check in (name-based) → Orient (welcome/itinerary card, `CUSTOMER-JOURNEY.md`) → Wait/prepare (Lounge) → Draw 1 → Service 1 → Draw 2 → Service 2 → Draw 3 → Recovery/hospitality (departure experience — mechanism not yet designed, the previously-described departure-gesture concept is REMOVED, not approved) → Depart. Then, separately, on her own timeline: Discovers PM (at departure, not during the clinical visit, `docs/experience/RETURN-LOOP.md`) → Books PM → Returns.

**PM customer:** Arrive → Reception → Lounge (shorter wait, different register) → Treatment → Refresh/depart → Rebook.

**Can these coexist without feeling clinical or chaotic?** Largely yes, per the existing brand principle that only the Blood Collection Room is permitted to look clinical (`docs/strategy/BRAND-ARCHITECTURE.md`) — an AM guest in the open-plan Lounge already reads as "a woman in a nice space," not as a patient, so AM/PM co-presence in shared zones is not inherently a flow problem (a finding already established in `docs/strategy/18-CLIENT-OPERATIONAL-STRESS-TEST.md` §7, restated here because it directly bears on whether AM and PM need physically separated circulation — **they do not**, per that analysis).

---

## 8. AM/PM Physical Transition (12:00-12:30)

Per the locked operating rule, this is what physically needs to happen, not a new decision:

- **Cleaning/room reset:** each treatment room/station used in the AM's final pairs needs its normal reset (already built into the schedule's 10-minute buffers, per `docs/strategy/18-CLIENT-OPERATIONAL-STRESS-TEST.md` §4) plus a fuller reset for the PM shift specifically (fresh linen, restocked consumables).
- **Linen/waste/replenishment:** clean linen store and dirty linen/biohazard room (both already in the room schedule) need to be positioned for quick staff access during this window — no new room implied, a workflow/positioning note (**C**).
- **Reception reset:** the single shared reception role (`docs/business-plan.md` §5, confirmed in the operational stress test as the actual transition bottleneck) needs a physical space to reset — the reception counter itself, no separate room implied.
- **Atmosphere reset (lighting/music/environmental):** **C, design recommendation, not confirmed anywhere in the source documents** — a deliberate lighting or audio shift at 12:00-12:30 (subtle, not theatrical) could reinforce the "this is now a different kind of afternoon" feeling without any client-visible "shift change," consistent with the founder's own concern about the venue feeling like "a busy clinic changing shifts." Worth testing, not yet decided.
- **Staff handover/lunch:** per `docs/strategy/18-CLIENT-OPERATIONAL-STRESS-TEST.md` §6, this genuinely benefits from — but does not strictly require — a small break/lunch area; the existing 10sqm Staff Room is the assumed venue for this, sized for the 12-client-era model, not independently re-checked against the 18-client transition-period load (**D**, flagged in §4 above).

**Physically, the goal is that none of the above is visible to a guest still in the venue** — the Lounge/circulation zones stay calm and populated-but-quiet; the reset activity happens in staff-only zones (Staff Room, linen store, BOH) or discreetly at reception, not as a visible operational scramble in guest-facing space.

---

## 9. Premium Experience Requirements

Translating "the experience is the product" (`docs/strategy/PREMIUM-POSITIONING.md`) into physical terms — name-agnostic, no colour palette or identity chosen:

| Requirement | Classification | Note |
|---|---|---|
| Natural light, especially in the Lounge | **A** | Existing design principle, `floor-plan-concept.md` |
| Warm, dimmable lighting; no harsh clinical downlights outside the Collection Room | **A** | Existing spec |
| Sound insulation in treatment rooms | **B, genuinely weakened by the curtain-partition decision** | Already disclosed as a real trade-off, not resolved — see §12 |
| Blood-draw privacy (visual and acoustic) | **A** | Solid-walled Collection Room, existing spec |
| Treatment privacy (visual) | **A** | Curtain-track bays, existing spec |
| Scent | **D** | Not addressed anywhere in the source documents — a genuine open item for design development, not this brief |
| Temperature control | **B** | Implied by "pregnant women sitting 2+ hours" comfort requirement; no specific HVAC spec exists yet (§12) |
| Materials (restraint over decoration) | **C** | `PREMIUM-POSITIONING.md`'s own evidenced finding — one or two consistently-executed material choices outperform many mediocre ones |
| Seating built for a genuine wait, not a transactional lobby | **A** | `CUSTOMER-JOURNEY.md` |
| Hospitality (refreshments, welcome ritual) | **A** | See §15 |
| Bathrooms — cleanliness, accessibility | **A**/**D** for compliance specifics — see §13 |
| Staff visibility where reassurance is needed, invisibility elsewhere | **C** | Reception sightline is confirmed (**A**); a broader "staff choreography" principle is a design recommendation, not a physical spec |
| Circulation ease, especially for a fasting/anxious guest | **A** | 1.5m-minimum hallway, existing spec |

---

## 10. Clinical vs. Wellness Balance

The existing floor plan already embodies the correct principle — this section confirms and extends it, doesn't redesign it.

**Only the Blood Collection Room should read as clinical** — genuinely clinical fittings (elbow taps, sharps disposal, medical fridge, Ra>90 lighting) belong there and nowhere else (**A**). Everywhere else, medical credibility should be communicated through **competence and process** (on-time draws, a clear itinerary, credentialed staff), not through visible medical signalling — consistent with `docs/strategy/BRAND-ARCHITECTURE.md`'s "named experience, not department" principle.

**Where the venue should feel:**
- **Clinical:** Blood Collection Room only.
- **Neutral/transitional:** Reception, circulation.
- **Warm/hospitality-led:** GTT Lounge, the leaving/departure moment.
- **Wellness-led:** Treatment rooms, Nail Station, Hairdressing Area — for both AM and PM alike.

No regulatory claim is made about what "counts" as sufficient clinical credibility for compliance purposes — that is a matter for the professional validations named throughout §12/§13.

---

## 11. Open-Plan Strategy

The existing floor plan already commits to this (Lounge/Hairdressing/Nails open-plan, only the Collection Room solid-walled, treatment rooms curtain-partitioned) — validated, not redesigned.

| Zone | Open-plan appropriate? | Basis |
|---|---|---|
| Reception, Lounge, Hairdressing, Nails | Yes — already the committed model | **A** |
| Blood Collection Room | No — solid walls required | **A** |
| Treatment rooms (massage/beauty) | Partial — curtain-partitioned, not fully open, not fully walled | **A**, with the disclosed sound-insulation trade-off (§9, §12) |
| Staff areas, BOH | No — must remain inaccessible to clients | **A** |

**The genuine open tension, already flagged and not resolved by this brief either:** the Nail Station's LEV/fume-containment requirement was originally specified as "must not be adjacent to the Lounge," which directly conflicts with the now-committed open-plan Lounge/Hairdressing/Nails zone. `floor-plan-concept.md` itself already flags this as unresolved, pending a WorkSafe WA-familiar contractor's confirmation that per-station downdraft LEV can substitute for room-level air separation. **This brief carries the same open item forward (D) rather than assuming it's resolved.**

---

## 12. Plumbing / Services / Building Infrastructure

| Requirement | Status |
|---|---|
| Clinical (elbow-tap) sink, medical-grade refrigeration, centrifuge bench, sharps disposal — Blood Collection Room | **KNOWN (A)** — `floor-plan-concept.md`, WDP-sourced |
| 2-sink/hands-free-tap fit-out — Facial/Beauty rooms and Nail Station | **KNOWN (A), conservative interpretation of the WA Skin Penetration Code, not a confirmed legal determination — requires professional/regulatory validation** |
| Single clinical sink — Massage rooms | **KNOWN (A)** — massage does not trigger the Code |
| No Code-mandated sink requirement — Hairdressing | **KNOWN (A)** |
| Plumbed hot/cold backwash basins — Hairdressing (2-3 for 4 chairs) | **KNOWN (A)** |
| LEV extraction — Nail Station, method for open-plan layout | **LIKELY, method UNKNOWN (D)** — requires LEV contractor/WorkSafe WA confirmation |
| Bathrooms — accessible + standard + staff, AS 1428.1 for accessible | **KNOWN (A) for existence; compliance specifics require professional validation** |
| Laundry — off-site or on-site not specified anywhere in the source documents | **UNKNOWN (D)** |
| Electrical load — minimum 2x 10A GPOs per nail station (specified); other zones not itemised | **PARTIAL — KNOWN for nails, UNKNOWN elsewhere (D)** |
| Data/power in the Blood Collection Room (centrifuge, medical fridge, booking terminal) | **GAP, identified 2026-08-06, still open (D)** |
| Wi-Fi/data throughout | **STRONGLY IMPLIED (B)** — a modern booking system (Fresha) and any future AM→PM tracking capability (`docs/strategy/OPERATING-COMMERCIAL-ARCHITECTURE.md` §15) requires reliable connectivity, not independently specified anywhere |
| HVAC — general comfort implied; no zoning spec exists | **B for general comfort; D for zoning/acoustic treatment specifics** |
| Acoustic treatment for curtain-partitioned treatment rooms | **UNRESOLVED, flagged not hidden (D)** — see §9 |

**None of the above is an engineering specification** — each is a business-planning flag for what a future architect/engineer needs to confirm, not a substitute for that confirmation.

---

## 13. Accessibility / Customer Practicalities

- **Mobility/pregnancy accessibility:** accessible WC (AS 1428.1), low reception counter section (750mm), 1.5m-minimum circulation, pram/mobility-aid-compatible pathways — all **A**, existing spec.
- **Blood Collection Room-specific wheelchair accessibility** (doorway width, turning circle, chair positioning) — **GAP, identified 2026-08-06, not yet confirmed (D)**, distinct from the building-level provisions above.
- **Companions:** **CORRECTION, 2026-08-14 — existing guidance was missed.** `docs/extended-wellness-services.md` §6 ("Women-Focused Space Policy") and `docs/research.md` (both CURRENT status per `docs/00_document_inventory.md`) already specify: partners/visitors are welcomed in a **separate cafe/reception-area seating zone**, explicitly **not** the treatment rooms or main GTT Lounge ("Service areas (treatment rooms, lounge): Women only... Partners and visitors: Welcome in the cafe/partner seating area near the entrance only"). **A**, existing guidance — this means companions do **not** add to the GTT Lounge seat count the way this brief originally assumed; they add to the Reception/Cafe zone's seating instead, a separate and smaller design question. Genuinely open (**D**): whether the existing Reception/Cafe footprint (§4, 15sqm + 8sqm) was ever sized with dedicated companion seating in mind, or only staff/retail/refreshment function — not addressed in either source document.
- **Parking:** **CORRECTION, 2026-08-14 — this brief's original claim that no source document addresses parking was wrong.** `docs/location-scouting.md` (not in this brief's original §2 source list, now added) states explicitly: "Ample parking — non-negotiable... Minimum 8–10 dedicated or immediately adjacent off-street parking spaces. Street parking alone is not acceptable." **A**, existing guidance. Genuinely open (**D**): whether 8-10 spaces remains sufficient at the 18-client design target with possible companion/support-person vehicles (§13 item above) — `location-scouting.md` predates both the 18-client rebase and the companion-seating question, so this specific re-validation is a real gap, distinct from "no guidance exists at all."
- **Requires professional/regulatory validation, explicitly, not asserted as compliant here:** AS 1428.1 compliance, fire egress, food-handling notification (Cafe/Refreshments counter, already flagged in `floor-plan-concept.md` as requiring WA Food Act 2008 council notification), and the Blood Collection Room's WDP/NPAAC compliance sign-off.

---

## 14. Retail

Per the founder's direction: third-party resale (Gaia, Weleda, Mustela), supporting/convenience, not a proprietary boutique concept — consistent with every prior strategic document's treatment of retail (`docs/strategy/STRATEGIC-REPORT.md` §7, `docs/strategy/OPERATING-COMMERCIAL-ARCHITECTURE.md` §3/§10).

- **Footprint:** wall-mounted shelving within the Reception zone, visible from the Lounge — already specified in `floor-plan-concept.md`'s Reception fittings, no separate room. **A.**
- **Stock storage:** minor allowance within existing back-of-house storage (Clean Linen/Storage room already includes "shelving, locked consumable cabinet" — retail stock can share this, not a new room). **C, reasonable inference, not independently specified.**
- **Checkout integration:** the existing reception POS/EFTPOS spec already covers this — no separate retail checkout implied. **A.**
- **Explicitly not required:** a standalone retail room, a boutique-style fitting-room/display concept, or dedicated retail staff — none of these are supported anywhere in the business plan or this repository's retail treatment, and none are recommended here.

---

## 15. Hospitality

Grounded in what the business plan and services documentation actually specify — no invented cafe.

- **Refreshments (water, herbal tea, snacks, the glucose drink itself):** the Cafe/Refreshments Counter (8sqm, kitchenette, mini fridge) is already specified as a **day-one core function**, not an ancillary amenity — glucose-drink dispensing is part of the GTT protocol itself. **A.**
- **Seating:** covered by the GTT Lounge's own seating requirement (§4). **A.**
- **Storage/refrigeration:** a mini fridge is already specified for the Cafe counter — sufficient for the documented items (water, tea, snacks, glucose drink), no larger cold-storage requirement is implied by anything in the business plan. **A.**
- **Cleaning:** standard kitchenette hygiene, no special provision beyond what's already specified. **A.**
- **Explicitly not required:** a full commercial kitchen, an expanded cafe/food-service concept, or any hospitality footprint beyond the existing 8sqm counter — nothing in `docs/business-plan.md` supports building a larger food-service operation, and this brief does not recommend one.

---

## 16. PM as a Real Wellness Centre

**Can the venue transition from GTT centre to premium wellness centre without a second premises?** Yes, per every document reviewed for this brief — PM uses the identical physical rooms/stations as AM, just with different (and unrestricted) durations and no clinical time pressure. No source document anywhere in this repository proposes or requires a second premises for PM. **A.**

**Duration support (30/45/60/90/120+ min):** already addressed structurally — treatment rooms, nail stations, and hair chairs have no inherent duration limit; the 45-minute ceiling is an AM *scheduling* rule (driven by the clinical draw clock), not a physical constraint of the rooms themselves (`docs/strategy/18-CLIENT-COMMERCIAL-STRESS-TEST.md` §2's own finding that AM timing is clock-invariant to service selection applies in reverse for PM — the room doesn't care how long the booking is, only the calendar does). **A.**

**Room flexibility enabling this:** already covered in §5 — the same dual-qualified staff and generically-fit-out treatment rooms that serve AM in the morning serve PM's longer bookings in the afternoon, no redesign implied.

---

## 17. Future Scale

Extending `docs/strategy/OPERATING-COMMERCIAL-ARCHITECTURE.md` §14's replicability framework specifically to the physical venue:

**STANDARDISE across future sites:** the room-count philosophy (4 treatment/4 nail/4 hair as the validated ratio for an 18-client target, §4); the open-plan-except-Collection-Room construction logic; the AM/PM shared-space model (§16); the customer flow sequence (§7); the Collection Room's clinical-fit-out spec (WDP/NPAAC-derived, though the specific pathology partner will differ by city, §12 of `OPERATING-COMMERCIAL-ARCHITECTURE.md`); the growth-reservation principle itself (build in near-term expansion shells from Day 1, §6).

**VARY by site:** exact floor area (tenancy shape will differ), frontage/street presence, parking provision, local building/council requirements, the specific pathology partner and their room-spec preferences, local trade/fit-out costs.

**The flagship's job as a prototype:** prove the room-count-to-client-volume ratio holds in practice (not just in the solver), prove the open-plan/curtain construction approach delivers the calm-not-clinical experience it's designed for, and produce a real, costed fit-out reference that a second site's budget can be built from — rather than each future site re-deriving these answers independently.

---

## 18. Property Search Checklist

| Category | MUST HAVE | SHOULD HAVE | PREFERRED | DEAL BREAKER |
|---|---|---|---|---|
| Floor area | ~239-242sqm net usable | ~262sqm (growth-reservation-ready) | ~280-290sqm | Below ~230sqm net usable without a credible path to the minimum functional program |
| Configuration | Single, contiguous tenancy | Regular (non-fragmented) floor plate | Flexible internal layout, minimal structural columns | A floor plate that cannot fit the Blood Collection Room + 4 treatment rooms + 4 nail + 4 hair within a one-way flow |
| Access | Street-level or lift access for pregnant/mobility-aid clients | Separate or discreet service/staff entry | Dedicated entry visibility | No step-free access achievable within reasonable fit-out cost |
| Parking | **8-10 dedicated or immediately adjacent off-street spaces, non-negotiable (A, `docs/location-scouting.md`, correcting this brief's original "not specified anywhere" claim — see §13)** | Validated against the 18-client design target + possible companion vehicles (**D** — not yet re-checked at this volume, §22) | Ample, close, easy | Street parking only, or effectively no accessible parking option for a fasting, possibly-anxious pregnant client base |
| Plumbing | Capacity for the Collection Room's clinical sink, 2 backwash basins, multiple treatment-room sinks | Capacity for the full 2-sink Facial/Beauty spec across all 4 treatment rooms (§5's flexibility recommendation) | Generous existing plumbing reducing fit-out cost | Plumbing capacity that cannot support the Collection Room and backwash basins at all |
| Electrical | Capacity for nail LEV, hair equipment, general commercial load | Capacity without major supply upgrade | Existing 3-phase or easily upgradable | Electrical supply requiring a disproportionately expensive upgrade |
| Bathrooms | Existing WCs to build from (accessible + standard + staff) | Existing WC count close to the 3-WC requirement | Fully compliant, ready to use | No feasible path to an AS 1428.1-compliant accessible WC |
| Ceiling height | Not specified anywhere in the source documents — **D** | — | — | — |
| Tenancy layout | Supports a one-way-flow-compatible arrangement | Supports the open-plan zones without excessive internal structure | Naturally suits the Collection-Room-as-only-enclosed-room concept | A layout requiring the Collection Room to be centrally exposed with no privacy option |
| Infrastructure install capacity | Can accommodate LEV, medical fridge, centrifuge, HVAC as needed | Can accommodate without major building-services work | Existing services already close to spec | Building/landlord restrictions prohibiting medical-adjacent fit-out (LEV, clinical waste, etc.) |
| Staff facilities | Room for the existing Staff Room spec | Room for the §4/§8-flagged headroom | Generous staff amenity | No feasible staff-room/WC provision separated from client areas |
| Storage | Room for clean/dirty linen, consumables, retail stock | Generous BOH storage | Dedicated loading/delivery access | No BOH storage path at all |
| Landlord/building constraints | Landlord open to a health/beauty tenancy, LEV installation, clinical waste collection | Landlord contribution to fit-out (A$20,000-60,000 range referenced in `floor-plan-concept.md`, not guaranteed) | Favourable lease terms, fit-out period | Landlord prohibits medical/clinical use, LEV installation, or after-hours fit-out access |
| Expansion potential | None required at minimum | Room for the 2 growth-reservation shells (§6) | Adjacent tenancy or clear future-expansion path | — |

---

## 19. Property Scoring Framework

A framework to be weighted once real candidate properties exist — no arbitrary weights assigned here, per instruction:

| Dimension | What it measures |
|---|---|
| Clinical suitability | Can the Blood Collection Room's full spec (§12, §13) be achieved at reasonable cost |
| Customer experience potential | Natural light, street presence, sense of arrival, avoidance of a "strip mall clinic" read |
| PM suitability | Does the space feel credible as a standalone premium wellness venue in the afternoon, independent of its morning use |
| Floor-plan efficiency | Ratio of net usable/functional area to gross leasable area; regularity of the floor plate |
| Infrastructure readiness | Plumbing, electrical, HVAC capacity relative to what's needed vs. what requires new install |
| Parking/access | Proximity and ease for a fasting, potentially anxious, possibly-companioned pregnant client |
| Visibility | Street frontage, signage rights, findability |
| Expansion potential | Room for the growth-reservation shells, or a credible path to a second Perth site's learnings |
| Fit-out complexity | How much of the existing space already suits the open-plan/curtain-partition model vs. requires demolition/rebuild |
| Estimated fit-out cost/risk | Against the existing `floor-plan-concept.md` cost bands, adjusted for the specific tenancy's condition |
| Location quality | Proximity to the target demographic, existing obstetric/midwifery referral geography |
| Brand/environment potential | Whether the shell supports the "premium women's house" read without extraordinary intervention |

---

## 20. Venue Cost Discipline

Extending `docs/strategy/PREMIUM-POSITIONING.md`'s existing cost-discipline framework to venue selection specifically — no new fit-out budget invented here, existing figures cited as-is.

**Spend HIGH:** the Blood Collection Room's genuine clinical requirements (this is the one place underfunding directly threatens both safety and the brand's core credibility claim); natural light where the tenancy allows it (a real, low-cost-if-chosen-well, high-impact lever per `PREMIUM-POSITIONING.md`).

**Spend MEDIUM:** the treatment-room fit-out (one consistent, well-executed material choice, per the existing evidence-based finding); considered signage over standard vinyl.

**Spend LOW:** anything that reads as decoration rather than restraint — per `PREMIUM-POSITIONING.md`'s own findings, this includes avoiding both an underfunded "trying too hard" palette and an overspent, decoratively excessive one. The luxury proposition, as already established elsewhere in this repository, comes from space, light, service, and consistency — **not from an expensive venue alone.** A well-chosen, structurally simple tenancy that already suits the open-plan/curtain model (§18, §19) is a better spend than a more expensive space that requires extensive rebuilding to fit the concept.

**No fit-out budget is created here** — `floor-plan-concept.md`'s existing A$228,142-457,559 day-one estimate (mid A$341,851) remains the reference figure; this brief does not revise it.

---

## 21. Flagship vs. Minimum Viable Centre

**Minimum Viable GTT + Wellness Centre:** the ~239-242sqm minimum functional program (§6) — 4 treatment rooms, 4 nail, 4 hair, one Blood Collection Room, Reception, Lounge, Cafe counter, Staff Room, WCs, BOH. Capable of running the full 18-client/day model profitably (`docs/strategy/18-CLIENT-COMMERCIAL-STRESS-TEST.md`), but with no built-in room to grow without a future relocation or disruptive refit.

**Perth Flagship:** the ~262-290sqm preferred-to-ideal range (§6) — everything in the minimum viable centre, plus the 2 growth-reservation shells (a 3rd massage/beauty line without relocating), a proper back-office for the Venue Manager, and Lounge/staff-room headroom validated against the real 18-client peak-occupancy finding (§4) rather than the older 8-seat assumption. **The additional physical capability is entirely about not having to relearn or rebuild the concept when a second site is justified** — the flagship's role is to be the reference a second Perth location and eventual other-city sites are copied from, not merely to be one profitable venue.

---

## 22. Open Questions Requiring Founder Input

Only items that materially affect property requirements, floor area, fit-out, operations, customer experience, or economics:

1. **Companion/support-person provision — CORRECTED, 2026-08-14: guidance already exists, question is narrower than originally stated.** `docs/extended-wellness-services.md` §6 and `docs/research.md` already specify partners/visitors use a separate cafe/reception-area seating zone, not the main GTT Lounge — this brief's original claim of "no source document" was a source-list gap, now corrected (see §13). The remaining genuine founder question: **is the existing 15sqm Reception + 8sqm Cafe footprint (§4, §6) actually sized with dedicated companion seating in mind, or does it need a small explicit allowance added** — narrower than the original Lounge-seat-count question, and does not affect the Lounge sizing itself.
2. **Parking provision expectation — CORRECTED, 2026-08-14: guidance already exists.** `docs/location-scouting.md` states a minimum of 8-10 dedicated/adjacent off-street spaces, "non-negotiable." This brief's original claim of "zero existing guidance" was a source-list gap (that document wasn't in this brief's original §2 list), now corrected. The remaining genuine founder question is narrower: **does 8-10 spaces (set before the 18-client rebase and before the companion-seating question above) still hold, or does the higher design-target volume plus possible companion vehicles warrant more?**
3. **Whether the §4 Lounge peak-occupancy finding (up to 10 clients on-site at once, though not all in the Lounge simultaneously) should trigger a larger Lounge than the existing 35sqm/8-seat spec.** Matters directly for floor area (§6) and fit-out cost.
4. **Whether the AM/PM reception-overlap mitigation (already recommended as a scheduling fix — PM opening at 12:30 — in the operational stress test) is considered sufficient, or whether a second reception body should be planned for at all, even as a contingency.** Matters for the Staff Room sizing (§4, §8) and total headcount at the venue.
5. **Whether the Massage/Beauty treatment rooms should be fit out generically (2-sink spec across all 4) rather than split 2/2 by label (§5).** A real, modest cost decision (2 additional sinks) that materially improves AM/PM room-allocation flexibility — worth deciding before, not after, fit-out.

---

## 23. Contradiction Check

Performed explicitly against the repository, per instruction — none silently resolved:

1. **Nail Station open-plan vs. LEV/fume-containment adjacency rule.** `floor-plan-concept.md` itself already flags this: the Nail Station's original "must not be adjacent to the Lounge" fume-containment rule directly conflicts with the now-committed open-plan Lounge/Hairdressing/Nails zone. Not resolved by `floor-plan-concept.md`, and not resolved by this brief either — carried forward as an open item (§11).
2. **GTT Lounge's "seats 8 simultaneously" design principle vs. this brief's own computed peak of up to 10 clients on-site simultaneously (5 pairs) at the 18-client target.** A genuinely new contradiction surfaced by this brief, not previously reconciled anywhere — the existing 8-seat assumption may understate real Lounge demand, though the true Lounge-specific (not whole-venue) peak is likely lower than 10 and requires further validation (§4, §22 item 3).
3. **Curtain-partition sound insulation vs. the brand's "calm, private, premium" standard.** Already disclosed in `floor-plan-concept.md` as a real trade-off of the 2026-07-31 cost-reduction decision, not resolved there, and not resolved here — restated because it directly touches this brief's own §9 premium-experience requirements.
4. **Staff Room sizing (10sqm) was set independently of the 18-client model and the AM/PM transition-period staffing findings from the operational stress test.** Not a contradiction in the strict sense, but a genuine gap between two documents that were never cross-checked against each other until this brief — flagged in §4/§8 as requiring validation, not assumed adequate.
5. **The existing floor-plan target (~239-262sqm) predates the founder's most recent operating decisions** (18-client Table 1 as the explicit design target, the 12:30 PM start, the absolute 45-minute AM ceiling) — `floor-plan-concept.md` itself is marked PARKED as of 2026-07-29, before any of these decisions were made. This brief's validation work (§4) confirms the existing room counts still hold under the newer decisions, but this is the first time that cross-check has actually been performed and documented, not an assumption carried over silently.
6. **The Blood Collection Room's 18sqm target does not yet include the ~2-3sqm needed for the vasovagal recliner/couch**, a gap identified 2026-08-06 and still not incorporated into any sqm figure anywhere in this repository, including this brief's own §6 minimum-tier estimate, which adds it as a separate allowance rather than folding it into a revised room-schedule figure (which this brief does not have the authority to edit, per the "do not modify" instruction).

---

## 24. Property Search Brief — Summary

**Business:** GTT Centre Perth flagship.
**Design target:** 18 GTT clients/day (12/day downside scenario only).
**AM:** GTT + wellness/beauty, every service ≤45 minutes, absolute rule.
**PM:** Premium women's wellness/beauty, bookings begin 12:30pm, no duration ceiling (30-120+ min).
**Transition:** 12:00-12:30, soft reset/handover, not a closure.
**Core spaces:** 1 solid-walled Blood Collection Room (2 chairs); 4 curtain-partitioned treatment rooms (massage/beauty, ideally fit generically); 4 open-plan nail stations with LEV; 4 open-plan hair chairs with 2-3 backwash; open-plan GTT Lounge/reception/hairdressing/nails zone; Cafe/refreshments counter; Staff Room; 3 WCs (accessible, standard, staff); clean/dirty linen and BOH storage; small third-party retail display at reception.
**Floor area:** Minimum ~239-242sqm; Preferred ~262sqm (growth-reservation-ready); Ideal flagship ~280-290sqm (business-planning estimate, not architectural).
**Customer experience:** premium, calm, spacious, hospitality-led, clinically credible only where it needs to be (one room, not the whole venue).
**Clinical:** WDP/NPAAC-informed Blood Collection Room spec, professional validation required before fit-out.
**PM:** must feel like an independent, credible premium wellness operation in the same physical footprint, no second premises required.
**Retail:** small, supporting, third-party — a display wall, not a store.
**Staff:** sized to the existing 18-client headcount model (8 treatment + 2 phlebotomists + 1 reception + 4 PM dedicated + relief pool + Venue Manager), with the transition-period reception/staff-room adequacy flagged for validation.
**Future:** designed as the standardisable prototype for a second Perth location and eventual other-city expansion, not a one-off.
