# GTT Center Perth — Property Search Framework

**Date:** 2026-08-14
**Status:** Framework only — precedes and governs the property search in `docs/strategy/PERTH-PROPERTY-SHORTLIST.md`
**Primary source:** `docs/strategy/VENUE-FUNCTIONAL-BRIEF.md` (verified, commit e2aa09b) — this framework translates that document's requirements into a scoring and screening tool for real properties. It does not restate the venue brief's reasoning; it applies it.
**Secondary source:** `docs/location-scouting.md` (v2.0, 2026-07-28) — existing suburb shortlist, rent budget, lease-term targets. Preserved and built on, not re-derived.
**Name-agnostic:** nothing below depends on or implies any naming decision.

---

## A. Hard Requirements

A property that fails any of these is not a candidate, regardless of how good it looks otherwise.

| Requirement | Threshold | Why |
|---|---|---|
| Ground floor | Yes, no exceptions | `location-scouting.md` Primary Location Criteria; pregnant clients, prams, mobility considerations rule out upper floors without dedicated lift access as a "nice to have" — this is a MUST per the venue brief's accessibility section. |
| Minimum floor area | ~239-242sqm (day-one build) | `VENUE-FUNCTIONAL-BRIEF.md` §6, derived from `floor-plan-concept.md`'s Room Schedule (4 treatment rooms, 4 nail stations, 4 hair chairs, Blood Collection Room, Reception, Lounge, BOH). Below this, the confirmed 18-client room configuration does not fit without cutting a room the operational stress test relies on. |
| Zoning permits health/beauty/wellness use | Confirmed or realistically achievable | A property in the wrong zone is not usable regardless of layout. Zoning classification itself is a **council/planning-authority confirmation item**, not something this framework can verify from a listing — see §E. |
| Minimum 2 plumbed wet areas | Existing or feasible to install | `location-scouting.md` Venue Specification checklist; `floor-plan-concept.md`'s WA Skin Penetration Code sink analysis requires plumbed sinks in the Blood Collection Room and (per that document's 2-sink-per-treatment-room recommendation) ideally all 4 treatment rooms. A property with no existing plumbing and no feasible path to add it fails this. |
| 3-phase power available or feasible | Confirmed or realistically achievable | `location-scouting.md` Venue Specification checklist — hair equipment (dryers, potentially backwash pump systems) and future equipment load require this; single-phase-only buildings with no upgrade path fail. |
| Accessible WC feasible | Existing or buildable within the space | AS1428.1 compliance is a design requirement in `floor-plan-concept.md`; a property physically too small or too constrained to fit one fails. |

---

## B. Strong Preferences

These are not automatic rejects, but a property lacking several of them needs to compensate elsewhere to stay competitive.

| Preference | Why |
|---|---|
| Located in one of the 4 priority suburbs from `location-scouting.md` (Osborne Park > Joondalup > Cannington > Myaree/Murdoch) | Those rankings were built on freeway/arterial access, demographic catchment, and parking stock — not arbitrary. See §Location Strategy below for how this framework treats candidates outside the 4. |
| 8-10+ dedicated or immediately adjacent off-street parking spaces | `location-scouting.md`'s "ample parking — non-negotiable" language, and the founder's own scoring framework in §Parking Treatment below. Treated as a strong preference with a graduated scoring effect, not a binary filter this round — see below. |
| Existing health/medical/beauty fitout (any prior wet-area or clinical layout) | Materially reduces fit-out cost and time versus a bare shell — the difference between adapting existing plumbing and installing it from scratch is real money, not cosmetic. |
| Floor area in the 260-290sqm band | `VENUE-FUNCTIONAL-BRIEF.md`'s Preferred (~262sqm) and Ideal Flagship (~280-290sqm) tiers — room to build the 2-shell growth reservation (2nd Massage/Beauty room) without a second move. |
| Prominent street frontage / signage rights | Brand visibility for a premium, appointment-driven service — supports the "flagship" ambition without being load-bearing for day-one viability. |
| Former or current allied-health, medical, or beauty tenancy | Same logic as fitout above — reduces the list of unknowns a fresh commercial/retail shell carries. |

---

## C. Flexible Variables

These matter, but the business model does not depend on any specific answer — they are genuinely negotiable or solvable with a fit-out budget.

| Variable | Why it's flexible |
|---|---|
| Exact room configuration on day one | `floor-plan-concept.md`'s room schedule is a design target, not a fixed floor plan — curtain-partitioned treatment rooms, an open-plan nail/hair zone, and a separate Blood Collection Room can be built inside many different shell shapes. |
| Building age / construction type | Tilt-panel light-industrial (common in Osborne Park), A-grade office, or retail shell can all work if the internal fit-out is achievable — `floor-plan-concept.md` doesn't require a specific building typology. |
| Landlord fit-out contribution | Desirable (the existing fit-out cost estimate assumes A$30,000-60,000 of landlord contribution) but the business case doesn't collapse without it — it shifts net capex, not feasibility. |
| Lease length within reason | `location-scouting.md` targets 3yr+3yr option — a 2yr+3yr or 5yr straight lease is a negotiation point, not a screening filter. |
| Existing signage / branding on-site | Removable, replaceable. |

---

## D. Deal Breakers

Distinct from Hard Requirements: these are conditions that would disqualify an otherwise-compliant property, usually discovered mid-search rather than screened for upfront.

| Deal breaker | Why | Confirmation path |
|---|---|---|
| Upper floor with no ground-floor-equivalent access | Same reasoning as Hard Requirement above — restated here because upper-floor space sometimes gets shortlisted for price before this is checked. | Listing description / site visit |
| Fewer than 2 dedicated or immediately-adjacent parking spaces, in a location with no meaningful street/public parking alternative | Not "any parking below 8-10" (see graduated treatment below) — this is the genuine floor: effectively no parking option at all, for a service where clients arrive for 45-120+ minute appointments, often visibly pregnant. | Listing + site visit |
| Confirmed zoning that prohibits health/beauty/wellness use with no rezoning or use-class pathway | A property that cannot legally operate the business, full stop. | **Requires council/planning authority confirmation — not inferable from a listing.** |
| Structural inability to install plumbing (e.g., slab-on-grade with no accessible service routing, heritage-listed with hard fabric restrictions) | Fails Hard Requirement B (plumbed wet areas) with no feasible remedy. | **Requires a builder/architect site assessment — not inferable from a listing.** |
| True occupancy cost (rent + outgoings + GST) more than ~25-30% over the A$7,000-9,000/month budget band from `location-scouting.md`, with no offsetting factor (e.g., landlord contribution, below-market fitout) | This framework does not invent a new budget. A property can be functionally excellent and still fail on cost — that's a real deal breaker, not a soft preference, because it directly threatens the commercial model tested in `18-CLIENT-COMMERCIAL-STRESS-TEST.md`. | Listing figures; agent confirmation for outgoings/GST treatment |

---

## E. Information to Verify With the Leasing Agent

Not determinable from a listing page — requires a phone call or email before a property can move past Tier 2.

- Exact current asking rent, outgoings, and whether GST is included or additional (listings are inconsistent about this)
- Current lease term on offer and whether a 3yr+3yr option structure is negotiable
- Landlord fit-out contribution, if any, and rent-free fit-out period
- Zoning / permitted use class, and whether a health/beauty/wellness use has been approved at this address before
- Whether the quoted parking count is exclusive to this tenancy or shared with other tenants in the building
- Whether 3-phase power is already connected or would require an upgrade
- Existing plumbing points — how many, where, and whether the existing configuration is usable or would need to be relocated
- Current condition of HVAC and whether it's shared or tenancy-specific

## F. Information Only Determinable Through Site Inspection

- True internal layout feel (a floor plan doesn't convey natural light, ceiling height, acoustic separation, or how "clinical vs. wellness" the space feels on arrival — a genuine theme running through the venue brief)
- Actual condition of existing plumbing, drainage, and any wet areas (age, functionality, capacity)
- Real-world parking behavior at the actual times GTT would operate (early morning arrivals from ~06:45, a scenario listing photos never show)
- Noise from neighboring tenancies (relevant for an open-plan Lounge/Nail/Hair zone with LEV extraction running)
- Wheelchair/pram accessibility in practice — door widths, threshold height, path of travel from parking to entrance
- Whether the ceiling/structure can accommodate LEV ductwork for the Nail Station without a costly reroute
- Signal/mobile reception and NBN/internet infrastructure quality (needed for booking systems, EFTPOS, pathology data transmission)

---

## Property Size Classification Guidance

Per `VENUE-FUNCTIONAL-BRIEF.md`'s three-tier floor area model. This is a fit-to-purpose scale, not a "bigger is better" scale — a property well above the Ideal Flagship tier is not automatically preferred, since it likely carries occupancy cost the model doesn't support.

| Band | Range | Assessment |
|---|---|---|
| Below minimum | <239sqm | **Fails Hard Requirement** unless a specific room can be legitimately deferred (e.g., 2nd Massage/Beauty growth shell was always future-phase, not day-one — so a property landing just under 239sqm because it can't fit *that* shell is not automatically disqualified; a property that can't fit the confirmed day-one 4-treatment/4-nail/4-hair configuration is). |
| Minimum (day-one viable) | 239-260sqm | Meets the confirmed day-one room schedule. No spare room for the 2-shell growth reservation without a future move or reconfiguration. |
| Preferred | 260-280sqm | Fits day-one plus meaningful circulation/storage margin. |
| Ideal flagship | 280-290sqm | Fits day-one plus the 2-shell growth reservation from `floor-plan-concept.md`. |
| Above ideal | >290sqm | Not automatically better — evaluate specifically on whether the extra area is usable (e.g., splittable tenancies, dead space in an oversized single-use floor) and whether occupancy cost still clears the Deal Breaker threshold in §D. A 994sqm whole-floor listing is not "more flagship," it's a different, probably unaffordable, category of property. |

---

## Perth Commercial Property Type Research

Evaluated against: customer experience fit, plumbing/wet-area feasibility, room configuration flexibility, accessibility, parking, frontage, fit-out cost, and PM/wellness suitability.

| Property type | Typical stock | Assessment for GTT |
|---|---|---|
| Medical/consulting suite (existing fitout) | Common in Osborne Park, Joondalup, Cannington (near Bentley Health Campus), Nedlands, Ardross | **Best fit-out starting point.** Existing consulting rooms, reception, plumbing, disabled WC already solve several Hard Requirements. Downside: layout is optimised for GP/allied-health consult rooms (small, closed), which suits Treatment Rooms and the Blood Collection Room well but needs reconfiguration for the open-plan Nail/Hair/Lounge zone. |
| Retail/showroom shell | Common in Osborne Park (tilt-panel light industrial converted to retail) | Good floor area and frontage, usually open-plan (suits Lounge/Nail/Hair well), but typically **no existing wet areas** — full plumbing build-out required, raising fit-out cost and time versus a medical shell. |
| A-grade multi-tenant office building | Osborne Park (20 Parkland Road type), Joondalup CBD | Professional presentation and good building services (HVAC, NABERS ratings, end-of-trip facilities), but often priced per sqm at a premium reflecting whole-building amenity GTT doesn't need, and floor plates can be larger than useful (whole-floor listings well above the Ideal Flagship band). Only worth pursuing if a right-sized sub-tenancy is available, not a whole floor. |
| Wellness/day spa (existing fitout) | Rare in general commercial listings — most existing day spas are in shopping centres or hospitality precincts, not typically advertised as standalone commercial leases | Would be the closest functional analogue to the full AM+PM model, but none surfaced as an available candidate in this search — noted as a gap, not fabricated. |
| Office/medical hybrid (business park) | Myaree/Murdoch, parts of Cannington | Similar profile to standalone medical suites; worth the same evaluation. |
| Hospitality-adjacent (cafe/restaurant shell) | Scattered | Would solve some Lounge/cafe-counter aesthetic goals but working against, not with, the plumbing and room-partition requirements — not pursued as a category unless a specific compelling listing appears. |

---

## Location Strategy

Sourced directly from `docs/location-scouting.md` — **preserved, not re-derived.**

The existing 4-priority shortlist:

1. **Osborne Park** — Mitchell Freeway access, best parking stock of any Perth location for this use type (10-40 dedicated spaces typical per tenancy), tilt-panel/light-industrial building stock at the lowest A$/sqm of the 4 priority suburbs after Cannington, target streets Hutton St / Scarborough Beach Rd / Balcatta Rd / Warrick St-Odin Drive / Joseph Banks.
2. **Joondalup** — Mitchell Freeway northern terminus, 400,000+ population northern-corridor catchment, CBD precinct with 2,000+ public parking spaces as a backstop, proximity to Joondalup Health Campus (a genuine positive for a health-adjacent service — clients and referral pathways both plausible), target streets Boas Ave / Lakeside Drive-Grand Blvd / Shenton Ave / Davidson Tce-Joondalup Dr.
3. **Cannington/East Cannington** — Albany Hwy/Roe Hwy interchange, Carousel Shopping Centre 500+ free spaces nearby, lowest A$/sqm of the 4, proximity to Bentley Health Campus (same logic as Joondalup Health Campus above), target areas Manning Rd-George St / Albany Hwy / Welshpool Rd East.
4. **Myaree/Murdoch** — Kwinana Freeway/Leach Hwy access.

This framework does not add or substitute suburbs. Where the live search below surfaces a credible candidate outside these 4 (this round found genuine candidates in Nedlands, Mount Lawley, and Wembley), it is reported honestly in the shortlist with an explicit note that it falls outside the founder-reviewed priority list — not silently ranked alongside the 4, and not excluded outright either. That is a founder decision, not one this framework makes unilaterally.

### Destination-Based Customer Location Logic

GTT is not a walk-in, foot-traffic-driven business — it is 100% appointment-based (GTT bookings are scheduled well in advance; PM bookings are scheduled). This changes what "good location" means versus a conventional retail-siting model:

- **Visibility and passing foot traffic matter far less** than for a retail tenancy — clients are coming specifically for this business, not discovering it by walking past.
- **Freeway/arterial accessibility from across the metro area matters more** than hyperlocal walkability, because clients are drawn from a catchment defined by "will a pregnant woman drive here for a scheduled appointment," not "who walks past this door." This is precisely why `location-scouting.md` weighted freeway access so heavily and why it remains the right lens.
- **Parking at the point of arrival matters more than street presence**, because every client is arriving by car (a near-certainty for pregnant women attending a morning appointment involving blood draws) and needs a low-friction, close, safe place to park — this is the direct link between the destination-based model and why parking gets a Strong Preference weighting (not a Hard Requirement veto) in this framework.
- **Proximity to existing health infrastructure (hospitals, health campuses) is a soft positive**, not because of foot traffic, but because it reinforces the clinical-credibility half of the brand positioning (GTT is a real pathology service, not just a spa) — both Joondalup Health Campus and Bentley Health Campus proximity are noted as a plus for candidates near them in the shortlist.

### Parking Treatment (Graduated, Not Binary)

Per this round's founder instruction: parking is not a binary hard-reject filter. This framework scores it on a graduated scale instead:

| Parking situation | Treatment |
|---|---|
| Known ≥10 dedicated/immediately-adjacent spaces | Full marks — meets or exceeds `location-scouting.md`'s stated ideal. |
| Known 8-9 dedicated/immediately-adjacent spaces | Strong — meets the stated minimum band. |
| Known <8 dedicated spaces | Below preference, **not an automatic reject** — assess specifically: is there meaningful street parking or a nearby public parking facility that realistically substitutes? Is the shortfall small (6-7) or severe (0-2)? A property with 6 dedicated bays plus genuinely ample uncontrolled street parking is a different proposition than one with 2 bays and no alternative (the latter crosses into the Deal Breaker in §D). |
| Not disclosed in the listing | Treated as an item to verify with the agent (§E) — not scored negatively until confirmed. |
| Street/shared/public parking only, no dedicated bays | Flagged explicitly as higher-risk — evaluate the specific street's realistic capacity and competition from neighboring businesses at GTT's actual operating hours, rather than assuming it is unusable. |

---

## Property Scoring Model (14 Dimensions)

Weights are shown only where directly derivable from the business model documents already in this repository. Where no document supports a specific weight, the dimension is scored but left **unweighted, flagged for founder confirmation** rather than assigned an invented number.

| # | Dimension | Weight | Source for weight |
|---|---|---|---|
| 1 | Floor area (fit to size-classification bands above) | High | Hard Requirement — a property that fails this isn't a candidate at all, so among candidates that pass, closeness to the Preferred/Ideal band is a strong differentiator. |
| 2 | Ground floor access | Pass/fail | Hard Requirement. |
| 3 | Zoning / permitted use | Pass/fail (pending confirmation) | Hard Requirement, confirmation-gated. |
| 4 | Parking (graduated scale above) | High | Founder-specified graduated framework this round; `location-scouting.md`'s "non-negotiable" language for the 8-10 band. |
| 5 | True occupancy cost vs. A$7,000-9,000/month budget | High | Deal Breaker threshold directly tied to the commercial model in `18-CLIENT-COMMERCIAL-STRESS-TEST.md`. |
| 6 | Existing plumbing / wet areas | Medium-High | Directly reduces fit-out cost, a real and large line item (`floor-plan-concept.md`'s A$228,142-457,559 range). **Not formally weighted against the other Medium-High items** — flagged for founder confirmation of relative priority vs. items 7 and 9. |
| 7 | Existing medical/beauty/allied-health fitout | Medium-High | Same logic as #6. **Weight relative to #6 and #9 not derivable from existing documents — flagged for founder confirmation.** |
| 8 | Suburb priority (per `location-scouting.md`'s 4-tier list) | Medium | Directly sourced ranking, but this framework treats it as an input alongside others, not an automatic filter, per this round's explicit instruction not to exclude genuine out-of-list candidates. |
| 9 | Freeway/arterial accessibility | Medium | Destination-based customer logic above. **Weight relative to #6/#7 flagged for founder confirmation** — no document ranks "accessibility" against "fitout condition" numerically. |
| 10 | 3-phase power availability | Pass/fail | Hard Requirement. |
| 11 | Room configuration flexibility (can the confirmed day-one schedule fit) | High | Directly gates whether the venue brief's validated room schedule is achievable at all. |
| 12 | Growth-reservation headroom (280-290sqm ideal band) | Low-Medium | Desirable, not load-bearing for day-one viability — `VENUE-FUNCTIONAL-BRIEF.md` treats this as a "nice to have now, need later" tier. |
| 13 | Frontage / signage visibility | Low | Explicitly secondary given the destination-based, appointment-only model above — included because it supports the flagship ambition, not because it drives bookings. |
| 14 | Landlord fit-out contribution / lease terms | Low-Medium | Flexible Variable in §C — affects capex, not feasibility. |

**Founder confirmation needed:** dimensions 6, 7, and 9 are all reasonably "Medium-High" or "Medium" by qualitative logic, but no repository document establishes their relative order or numeric weights against each other. Until confirmed, this framework scores each dimension independently in the shortlist (as a rating, not a single weighted composite score) rather than manufacturing a false-precision total.

---

## Genuine Deal-Breakers List (Consolidated)

Restated from §D for clarity, with confirmation authority noted:

1. Upper floor, no ground-level equivalent — self-confirming from listing.
2. Effectively zero viable parking (< 2 dedicated bays, no meaningful alternative) — listing + site visit.
3. Zoning that prohibits the intended use with no realistic pathway — **requires council/planning authority confirmation.**
4. Structural inability to add required plumbing — **requires builder/architect assessment.**
5. True occupancy cost >25-30% over the A$7,000-9,000/month budget band with no offsetting factor — listing + agent confirmation.

No deal-breaker in this list is invented for this round — all five trace directly to either a Hard Requirement above or the existing rent-budget figure in `location-scouting.md`.

---

## What This Framework Deliberately Does Not Do

- Does not create a new rent budget, floor-area target, or room schedule — all three are cited from existing, founder-reviewed documents.
- Does not treat parking as a binary filter, per this round's explicit instruction.
- Does not exclude candidates outside the 4-priority-suburb list — it flags them for founder review instead.
- Does not assign invented numeric weights where no source document supports one — flagged instead.
- Does not make or imply any naming decision.

This framework is now applied to real, current Perth listings in `docs/strategy/PERTH-PROPERTY-SHORTLIST.md`.
