# Fit-Out Program — Decision Analysis (Blood Collection Rooms, Beauty Stations, Consolidated Program, Procurement Readiness)

**Status: analysis complete, no decision made, no external contact made.** This document performs the formal decision-analysis requested for the two genuinely open station/room-count questions identified in `FIT-OUT-DESIGN-PROCUREMENT-BRIEF.md` §3.2 and traced with evidence in `CHINA-AUSTRALIA-SOURCING-STRATEGY.md` §2. It does not resolve either decision — both remain **FOUNDER DECISION REQUIRED**. It also consolidates the current venue program into one authoritative table, reviews the brief for over-specification, and summarises procurement readiness. No supplier, sourcing agent, manufacturer, or WDP contact was made in producing this document.

Source basis: `docs/architecture/CHINA-AUSTRALIA-SOURCING-STRATEGY.md` (primary evidence trail), `docs/architecture/FIT-OUT-DESIGN-PROCUREMENT-BRIEF.md`, `docs/architecture/FIT-OUT-EQUIPMENT-SCHEDULE.md`, `docs/floor-plan-concept.md`, `docs/scenario-d-investigation.md`, `docs/architecture/ITEMISED-PURCHASE-LIST.md` §1, `docs/am-capacity-weekend.md`, `docs/VERIFICATION-TRACKER.md`, `docs/DECISION-LOG.md`, Chapter 34 of `outputs/master-dossier-v2/index.html`.

---

## Part B — Blood Collection Room Count: Decision Analysis

**Question:** does the venue genuinely require 2 physical Blood Collection Rooms, or does it remain 1 room with capacity for the required chairs (with a documented precedent for a 3rd chair via Scenario D)?

**Governance check performed first:** searched `VERIFICATION-TRACKER.md`, `DECISION-LOG.md`, Chapter 34, `scenario-d-investigation.md`, `am-capacity-weekend.md`, `floor-plan-concept.md` — no document anywhere in this repository, at any point in its history, proposes a second physical Blood Collection Room. Every existing reference to growth capacity in this function (Scenario D) describes adding a 3rd chair to the one room, never adding a room. This is not a stale source being misread; it is the absence of any prior basis for "2 rooms" anywhere except the fit-out brief's own §3.1 program line, which restates Anthony's instruction for that specific document without independent derivation.

| | **Option 1 — One room, appropriate chair capacity (2 chairs now, 3rd chair via Scenario D if needed)** | **Option 2 — Two physical Blood Collection Rooms** |
|---|---|---|
| **Operational case** | Matches every clinical/staffing/financial model built to date. 2 phlebotomists, 1 solid-walled room, Chair A/B, 18 clients/day at 25-min cadence (`docs/CURRENT-STATE.md`). Scenario D adds a 3rd chair inside the same room to reach ~15 clients in the AM block if volume grows further, at labour cost only — no new lease footprint, reception, or Venue Manager overhead. | No operational model has ever been built around 2 rooms. Would presumably let two clients be drawn fully privately in parallel rather than two chairs in one shared room, or separate the AM high-volume flow from a lower-volume PM/overflow flow. Neither rationale is stated anywhere in the repository — this is a plausible interpretation, not a documented one. |
| **Space impact** | Currently-costed room: 18sqm (`CURRENT-STATE.md` changelog 2026-08-07), plus ~2-3sqm allowance for a vasovagal recliner not yet folded in. Fits the existing floor-plan concept without re-derivation. | A second room at the same ~18-20sqm minimum floor area (`FIT-OUT-DESIGN-PROCUREMENT-BRIEF.md` §4.2, itself A-tagged from `pathology-collection-room.md`) would add roughly 18-20sqm to the venue's required footprint — a material change to total leasable area required, not yet tested against either Tier-1 venue candidate's floor plate. |
| **Fit-out impact** | Already the basis for the current costed fit-out range (A$228,142-457,559, `FIT-OUT-DESIGN-PROCUREMENT-BRIEF.md` §24). Solid walls, door, soundproofing, lighting, ventilation (6 ACH), hand hygiene, sharps/waste, power/data — one instance of each. | Doubles every clinical-room fit-out line item: a second solid-walled enclosure, second door, second full lighting/ventilation/hand-hygiene/sharps-and-waste/power-data build-out, second WDP room-spec sign-off. Not costed anywhere — `FIT-OUT-EQUIPMENT-SCHEDULE.md` explicitly marks the phlebotomy-chair quantity "PENDING §3.2 RECONCILIATION" rather than assuming doubled quantities. |
| **Advantages** | Financially and operationally proven; no re-derivation of the P&L, staffing model, or lease-size requirement needed; matches WDP's own room-spec correspondence to date (`docs/pathology-collection-room.md`, Carole Rivers' 2026-08-06 reply). | Could offer greater privacy/separation if that is genuinely the intent (e.g. two clients never share a room even briefly); could allow independent scheduling of two draws without any shared-room coordination. |
| **Disadvantages** | If "2 rooms" was intended to mean materially more privacy or genuinely doubled physical capacity, Option 1 alone does not deliver that. | Unbudgeted, unstaffed (no model exists with more than 2 phlebotomists), unrequested by WDP in any correspondence to date, and expands the venue's required floor plate before a venue is even secured — directly conflicts with the "do not over-specify before the venue" principle (Part E below). |
| **Evidence** | `docs/scenario-d-investigation.md`, `docs/am-capacity-weekend.md`, `docs/floor-plan-concept.md`, `docs/CURRENT-STATE.md` §1/§3/§4/§5/§7/§8, `docs/pathology-collection-room.md`. All internally consistent with each other. | `FIT-OUT-DESIGN-PROCUREMENT-BRIEF.md` §3.1 only — a single instruction line in a single document, with no supporting operational, staffing, or WDP-correspondence basis found anywhere else. |
| **Outstanding confirmation needed** | Whether Scenario D's 3rd-chair lever is even needed yet — gated on WDP's specimen-cutoff/window confirmation for a 15-client AM schedule (a pre-existing, still-open third-party dependency, not new). | Whether "2 rooms" was shorthand for wanting more phlebotomy capacity (in which case Scenario D already answers it) or a genuinely new, doubled-capacity intent, and if the latter, what operational/financial case supports it. |

**RECOMMENDATION — FOUNDER DECISION STILL REQUIRED.** The evidence weighs toward Option 1 (one room, Scenario D as the documented growth lever) being the interpretation consistent with everything else built for this venture, but this document does not lock that reading. Anthony's own §3.1 instruction says "2 rooms" in a live, current document, and a founder instruction is not overridden by the absence of prior paperwork. This is presented as an evidenced choice, not decided here.

---

## Part C — Beauty Station Count: Decision Analysis

**Question:** is 4 Beauty stations correct, or 3 — and is there any basis for the 4th, or does Beauty share rooms with Massage?

**Governance check performed first:** searched `floor-plan-concept.md`'s Room Schedule, `ITEMISED-PURCHASE-LIST.md`, service-catalogue and staffing documents, Chapter 34, `VERIFICATION-TRACKER.md`, `DECISION-LOG.md`. No document proposes a 4th Beauty station or room. This was not assumed to be a typo — it was searched for directly and not found.

| | **Option 1 — 3 Beauty stations** | **Option 2 — 4 Beauty stations** |
|---|---|---|
| **Operational case** | Matches `floor-plan-concept.md`'s Room Schedule exactly: day-one committed (Treatment Room 3, Treatment Room 4 — Facial/Beauty = 2) plus one Growth Reservation (Treatment Room 6 — Facial/Beauty = 1), total 3. This is the same day-one-plus-reservation logic that independently explains Massage's figure of 3 in the fit-out brief (2 day-one + 1 reservation = 3, an exact match). Applying identical logic to Beauty predicts 3, not 4. | No document anywhere proposes a 4th Beauty room, station, or reservation. Staffing model (`CURRENT-STATE.md`) uses 4 dual-qualified Massage+Beauty pool staff sharing rooms via curtain partitions, not 4 dedicated Beauty-only stations — headcount does not independently support a 4th physical station either. |
| **Space impact** | Fits the existing floor-plan concept and its already-documented growth reservation — no new floor area beyond what is already planned for the venue's own full build-out. | Would require an additional treatment-room footprint beyond what `floor-plan-concept.md`'s Room Schedule currently reserves for Beauty — not modelled in that document. |
| **Fit-out impact** | Consistent with the currently-costed model (`FIT-OUT-EQUIPMENT-SCHEDULE.md`: 2 facial/beauty treatment beds currently costed, "up to 4 PENDING §3.2 RECONCILIATION" only because the brief's own §3.1 asked for 4, not because a 4th is independently evidenced). | Adds one facial/beauty treatment bed and associated fit-out (partition curtain run, power/data, lighting) beyond the day-one-plus-reservation total — a genuine incremental cost with no documented rationale. |
| **Advantages** | Internally consistent with every other planning document; uses the exact same evidentiary logic that already explains Massage's figure; no unexplained cost added. | If genuinely intended (e.g. Anthony wants a larger long-term Beauty capacity than Massage), it front-loads that ambition into the current brief rather than requiring a second reconciliation exercise later. |
| **Disadvantages** | If 4 was a deliberate, considered instruction (not a slip), Option 1 under-builds against that intent. | No repository evidence supports it; risks being carried forward into supplier-facing documents as though it were confirmed, when it is not. |
| **Evidence** | `docs/floor-plan-concept.md` Room Schedule, `docs/architecture/CHINA-AUSTRALIA-SOURCING-STRATEGY.md` §2.3 (side-by-side Massage/Beauty reconciliation). | None found. `FIT-OUT-DESIGN-PROCUREMENT-BRIEF.md` §3.1 only. |
| **Outstanding confirmation needed** | None beyond the founder decision itself — the day-one-plus-reservation figure is already fully documented elsewhere. | Whether Anthony intends a genuinely larger Beauty capacity than Massage, and if so, on what operational or demand basis (service-catalogue mix, projected Beauty-vs-Massage booking split, or similar) — no such basis currently exists in any document. |

**Beauty sharing rooms with Massage:** already the current, costed model for day-one (4 combined, curtain-partitioned "treatment rooms" usable by any of the 4 pool staff, per `FIT-OUT-DESIGN-PROCUREMENT-BRIEF.md` §3.2's own comparison table) — this is not a new option, it is the status quo interpretation, and is compatible with either 3 or 4 as a total dedicated-Beauty count once the room-schedule reservation question is settled.

**RECOMMENDATION — FOUNDER DECISION REQUIRED.** Evidence points to 3 (day-one + growth reservation, matching the same logic that explains Massage), with no traceable basis anywhere for a 4th. This is not manufactured into a false certainty — it is reported as the strongest evidenced reading, pending Anthony's confirmation.

---

## Part D — Consolidated Current Venue Program (Single Authoritative Version)

One table, replacing any impression that multiple station-count versions are equally current. Classification: **Confirmed** (matches costed/staffed model, no open question) / **Founder decision** (genuinely unresolved, evidence stated above) / **Professional verification** (dimension/compliance figure needs an Australian specialist) / **Site-dependent** (cannot be finalised until a venue is secured) / **Procurement-dependent** (depends on the China/Australia sourcing decision, Part G).

| Area | Current program | Classification | Basis |
|---|---|---|---|
| Blood Collection Room(s) | 1 room, 2 chairs (Chair A/B), Scenario D 3rd chair as documented growth lever | **Founder decision** (brief's §3.1 says 2 rooms — see Part B) | `CURRENT-STATE.md`, `scenario-d-investigation.md` |
| Massage stations | 3 (2 day-one + 1 growth reservation) | **Confirmed** — figure reconciled with evidence this round | `floor-plan-concept.md`, `CHINA-AUSTRALIA-SOURCING-STRATEGY.md` §2.3 |
| Massage station format (table/bed vs chair-based) | Not decided | **Founder decision** | `FIT-OUT-DESIGN-PROCUREMENT-BRIEF.md` §6 |
| Beauty stations | 3 by the same evidenced logic as Massage; brief's "4" has no traceable basis | **Founder decision** (see Part C) | `floor-plan-concept.md`, `CHINA-AUSTRALIA-SOURCING-STRATEGY.md` §2.3 |
| Nail stations | 4 | **Confirmed** | `ITEMISED-PURCHASE-LIST.md` §1 |
| Pedicure chairs | 4, same zone as the 4 nail stations, not a separate expansion | **Confirmed** — reconciled with evidence this round | `ITEMISED-PURCHASE-LIST.md` §1, `CHINA-AUSTRALIA-SOURCING-STRATEGY.md` §2.4 |
| Hair Wash stations | 2 | **Confirmed** | `FIT-OUT-DESIGN-PROCUREMENT-BRIEF.md` §8 |
| Hairdresser stations | 4 | **Confirmed** | `FIT-OUT-DESIGN-PROCUREMENT-BRIEF.md` §8 |
| Construction type (solid walls vs curtain partition per area) | Confirmed regardless of station-count outcome | **Confirmed** | `FIT-OUT-DESIGN-PROCUREMENT-BRIEF.md` §3.3 |
| Blood Collection Room clinical dimensions/finishes/lighting/ventilation | Ranges and standards stated, exact figures not locked | **Professional verification** | `FIT-OUT-DESIGN-PROCUREMENT-BRIEF.md` §4 |
| Café/F&B model | Pre-made vs on-site assembly, not decided | **Founder decision** | Chapter 34, `FIT-OUT-DESIGN-PROCUREMENT-BRIEF.md` §28 item 16 |
| Total leasable floor area required | Depends on Blood Collection Room and Beauty outcomes above | **Site-dependent** (also gated on Part B/C) | Derived |
| Which items are China-sourced vs Australia-only | Category A/B/C classification exists, no supplier selected | **Procurement-dependent** | `CHINA-AUSTRALIA-SOURCING-STRATEGY.md` §6 |
| Fit-out total cost | A$228,142-457,559 currently costed against the currently-costed model only, not the expanded §3.1 program | **Founder decision + site-dependent** (moves once Part B/C are resolved) | `FIT-OUT-DESIGN-PROCUREMENT-BRIEF.md` §24 |

No station-count figure above is presented as simultaneously "confirmed" in one place and "open" in another within this repository as of this update — the brief's §3.1 figures for Blood Collection Rooms and Beauty remain visibly flagged as founder decisions in §3.2/§28, not silently superseded by this document.

---

## Part E — Over-Specification Review

Reviewed `FIT-OUT-DESIGN-PROCUREMENT-BRIEF.md` specifically for false architectural certainty. Finding: the brief is already highly disciplined on this point.

- **Dimensions** — every room/clearance figure is tagged A (confirmed), B (strongly implied), C (design recommendation), or "AUSTRALIAN [DISCIPLINE] VERIFICATION REQUIRED." No dimension is stated as final without a tag (§4.2, §16-19 spot-checked).
- **Cabinetry/joinery** — described at the level of function and material language (§2, §17), not shop-drawing detail; no joinery dimensions invented.
- **Plumbing/electrical/HVAC/LEV routing** — explicitly not routed. §16-19 state requirements (circuit counts, ACH targets, LEV pre-application need) without claiming to route services, consistent with "not manufacture-ready" status (§F below).
- **Drainage** — sink/handwash requirements stated per the WA Skin Penetration Code's 2-sink interpretation; no drainage layout invented.
- **Accessibility circulation** — AS 1428.1 referenced by name, exact clearances flagged "AUSTRALIAN ACCESSIBILITY VERIFICATION REQUIRED" rather than guessed (§4.2).
- **Toilet configuration, BOH, equipment clearances** — described functionally (§10-13), not dimensioned to shop-drawing precision.

No changes required to the brief as a result of this review — it was already built to avoid this failure mode, per its own §30 "What This Document Does Not Do."

---

## Part F — Procurement Readiness (Ready vs Remaining Gaps)

From `CHINA-AUSTRALIA-SOURCING-STRATEGY.md` §8-9, reported without new research.

**Ready today:** brand/design direction (7-colour palette, typography, material language), Hair area (the one area with no open item), construction-type philosophy (§3.3), Nail/Pedicure program, the compliance-standard names that apply (even where exact figures need verification), the landed-cost framework's known components (inspection fee US$149-350/day, agent commission 3-10%).

**Remaining gaps before an RFQ could realistically be issued:**
1. Blood Collection Room count (Part B) and Beauty station count (Part C) — both founder decisions, directly change quantities on every affected line item.
2. Massage station format (table/bed vs chair-based) — changes the entire product spec for that category.
3. A confirmed venue with a measured floor plate — nothing above can be finalised as a floor plan until a venue is secured (site-dependent).
4. Exact Australian compliance figures currently flagged "VERIFICATION REQUIRED" (accessibility clearances, LEV pre-application outcome, electrical circuit certification detail).
5. A procurement model decision (Part G) — determines who (if anyone) is approached for quoting, and what information package they need.
6. Full freight/landed-cost modelling beyond the existing FOB×1.55 placeholder, which is explicitly flagged inadequate for a whole-project shipment.

This is a "prepare for the next stage" gap list, not a blocker list — none of these gaps require external contact to close except the venue search itself (already in motion separately) and the two founder decisions.

---

## Part G — China/Australia Procurement Strategy (Summary, No New Research, No Contact)

Restating `CHINA-AUSTRALIA-SOURCING-STRATEGY.md` §5 and §9-11 — not repeating the underlying research.

**Recommendation on record (a recommendation, not a founder decision):** Model C, Hybrid — an Australian-based sourcing agent for China-sourceable categories, independent third-party pre-shipment inspection (SGS/Bureau Veritas/Intertek/QIMA/V-Trust, all evidenced with real day-rate figures), and Australian sourcing retained unchanged for clinical/regulated items. **Epic Sourcing Australia** (Alexandria NSW, furniture-specific, explicit hospitality-sector claim) is the strongest candidate found to date, with FBM Sourcing (Guangzhou, real hospitality FF&E evidence, no local AU entity) as an alternative. Neither has been contacted. Ali Baba Furniture (Adelaide) is confirmed, this round, to be a retail store, not a commercial sourcing partner — the earlier characterisation in `ASIA-SOURCING-INVESTIGATION.md` is a superseded source on this specific point, not new evidence of anything having changed.

**Minimum information package needed before any agent could realistically quote** (per §9 of the sourcing strategy, restated, not re-derived): a secured venue, a measured floor plan, the final station/room program (Parts B-D above resolved), design intent per area, a materials/finish schedule, firm quantities per item, equipment specifications for clinical items, applicable Australian compliance requirements per item, installation-responsibility split (supplier vs local trades), freight assumptions, and landed-cost requirements (duty/GST/ChAFTA treatment). None of this package is assembled yet in a form ready to send, and nothing has been sent.

**Recommended sequencing** (from §11's 15-stage pathway, restated): lock the station/room program first (Parts B-D), then venue selection, then measure/survey, then Australian compliance review, then room-by-room design finalisation, then China/Australia classification, then Australian benchmark pricing obtained first, then a scoping conversation with a sourcing agent — in that order. No step beyond "lock the program" has been actioned.

---

## Addendum (2026-08-21, Round 2) — Growth-First Venue Philosophy

Anthony has since stated a governing principle that changes how Parts B-D above should be read, though it does not silently resolve either founder decision: **the initial venue must be built for the full planned operating model from day one, not renovated later.** Day-one utilisation being lower than eventual capacity is not, on its own, a reason to shrink the station program — the question is what physical capacity the venue needs on day one so growth (larger client base, AM-to-PM conversion, increased PM staffing) does not require a second fit-out. This changes the *interpretation* of the evidence in Parts B and C, not the *facts*.

**Blood Collection Room, reframed:** the existing evidence (no document proposes a literal 2nd room; Scenario D documents a 3rd-chair-in-one-room growth path) is still accurate, but under the growth-first principle it supports a **third option not previously presented**: build the single Blood Collection Room from day one sized, serviced, and wired/plumbed for 3 chairs (the Scenario D configuration), rather than installing only 2-chair capacity and needing to retrofit power/data/space later. This satisfies "no future renovation" without requiring a literal second enclosed room, and is consistent with every operational document reviewed. It does not resolve whether Anthony's "2 rooms" instruction means this (a bigger single room, future-proofed) or a genuinely separate second enclosed space — that remains the founder decision. Anthony's own brain-dump also raises a related, genuinely open construction question: whether the Blood Collection area's required privacy/compliance can be met with a properly constructed partition wall within a larger space rather than two fully independent rooms (separate doors, separate HVAC zones) — this is a real cost-and-space-efficiency question that has not been evaluated by an Australian building/compliance professional and is flagged here as **AUSTRALIAN COMPLIANCE VERIFICATION REQUIRED**, not decided.

**Beauty stations, reframed:** the growth-first principle explains *when* to build the existing, already-documented Growth Reservation tier (build it day-one rather than waiting) but does not, by itself, supply a basis for a *4th* station beyond what `floor-plan-concept.md` already reserves (day-one 2 + reservation 1 = 3). If Anthony intends 4 Beauty stations from day one, that requires the Growth Reservation tier itself to be expanded from 1 additional station to 2 — a genuinely new quantity decision, not just a timing decision, and still not evidenced anywhere in this repository. The finding in Part C stands: 3 is the evidenced figure, 4 remains unexplained, growth-first philosophy notwithstanding.

**Net effect on the recommendation:** both items remain **FOUNDER DECISION REQUIRED**. The growth-first principle sharpens the Blood Collection Room question into a genuine three-way choice (2-chair room / 3-chair-ready single room / two separate rooms) rather than a binary one, and confirms the Beauty question is about quantity, not timing. Neither is resolved here.

---

## Addendum (2026-08-22, Round 3): Real Recommendations, Not a Repeated "No Precedent" Deflection

Anthony has directly instructed that repeating "no historical precedent" is not sufficient once the growth-first principle has been stated: the physical venue must be evaluated from opening on workflow, privacy, clinical requirements, staffing requirements, floor-area/fit-out cost, and ability to scale without construction, not on what an old document happened to say. He has also clarified that a landlord-provided "2 rooms" condition is not required: walls can be constructed inside the venue regardless of the lease's existing configuration. Both items below are now given a genuine recommendation.

**Blood Collection Rooms, RECOMMENDATION: one room, built and serviced from day one for 3 chairs, not two separate rooms.**

Reasoning, not precedent-counting:
- Every operating scenario this venture has ever modelled (18-client committed AM model, the 12-client secondary model, and Scenario D's higher-volume growth case) tops out at 3 simultaneous phlebotomy chairs. No scenario anywhere in this repository's history, including the growth-focused ones, calls for more than 3 concurrent draws. A second physically separate room would only earn its cost if a 4th+ simultaneous chair, or a genuinely distinct second clinical stream, were part of the actual growth plan; neither is.
- Workflow: 2 phlebotomists work as a synchronised pair on a 25-minute cadence (Chapter 8). A 3rd chair added later extends that same synchronised model; it does not require a second, separately supervised clinical space. Splitting into two rooms would instead require either a 3rd phlebotomist supervising a fully separate space alone (a staffing and clinical-supervision change with its own cost and safety implications, not evidenced as needed) or awkward back-and-forth supervision across two rooms by the same 2-person team.
- Privacy: privacy is a per-chair curtain/partition and appointment-scheduling matter (no two clients are drawn while a third is present in the same chair-position), not a function of the number of enclosed rooms. One larger, correctly serviced room with 3 chair positions and adequate partitioning between them meets the same privacy standard as two smaller rooms, at materially lower floor-area and fit-out cost (one set of solid walls, one door, one ventilation/lighting/hand-hygiene/sharps-and-waste build-out instead of two).
- Growth-without-renovation: building the room's walls, power, data, and plumbing sized for 3 chairs from day one, while only installing and staffing 2 chairs initially, satisfies "no future renovation" completely. Adding the 3rd chair later becomes a furniture and staffing decision, not a construction one, exactly the physical-capacity-versus-staffing-capacity distinction the growth-first principle asks for.
- Cost: a second full room roughly doubles every clinical-room fit-out line (second solid wall, door, ventilation, hand-hygiene, sharps/waste, power/data, and a second WDP room-spec sign-off), for a capacity increase (a theoretical 4th chair) that no operating model calls for. That is over-building relative to the venture's own evidenced growth path, not growth-first design.

**This is now the recommendation, not an open coin-flip: one Blood Collection Room, built and serviced for 3 chairs from day one.** Final sign-off still requires an Australian building/compliance professional to confirm the specific partition/privacy arrangement between chair positions meets the WA Skin Penetration Code and any WDP-specific collection-room requirement for a specific floor plate once a venue is secured; that verification step is real and still open, not a founder decision.

**Beauty stations, RECOMMENDATION: 3 stations (2 day-one + 1 growth reservation), matching Massage exactly, not 4.**

Reasoning: Massage and Beauty draw from one shared, dual-qualified staff pool (Chapter 9/14), not two independent pools. Every AM staffing model built for this venture, including the committed 18-client model, caps that shared pool's peak simultaneous concurrency at 4 people. Building 3 Massage stations plus 4 Beauty stations would give the combined pool 7 physical stations to grow into against a peak modelled demand of 4, over-provisioning relative to the venue's own real growth lever, which is the shared pool's headcount, not a fixed per-service station count. The already-committed day-one-plus-growth-reservation figure of 3 (matching Massage) already gives the combined pool 6 stations against a peak of 4: genuine headroom for growth, without inventing an unevidenced 4th station. No operating scenario, demand case, or staffing model anywhere in this repository supports a Beauty station count independent of and larger than Massage's. If Anthony specifically wants Beauty capacity to be able to run independently of Massage's own staffing at a scale beyond the shared pool's current peak, that is a distinct, new demand assumption that would need its own case; it is not evidenced today, so it is not adopted here.

**Net effect:** Blood Collection Room count and Beauty station count are no longer presented as open, unweighted founder decisions. Both now carry a specific, reasoned recommendation. Anthony's confirmation is still the final step before either becomes a committed program (this is a real capital-cost decision, appropriately isolated as one), but this document no longer asks him to choose between two equally-weighted options with no stated preference.

## Changelog

**2026-08-22 (Round 3):** Replaced the Round 2 "growth-first sharpens the question but doesn't resolve it" framing with an actual recommendation for both open items, per direct founder instruction not to repeat a "no precedent" deflection. Blood Collection Rooms: recommend one room, built/serviced for 3 chairs from day one, not two separate rooms, reasoned from the venue's own real growth lever (Scenario D's 3rd chair), workflow, privacy-via-partitioning, and cost, not from precedent-counting. Beauty stations: recommend 3, matching Massage, reasoned from the shared Massage+Beauty staffing pool's own modelled peak concurrency (4), not from "no document mentions a 4th." Both still require Anthony's final sign-off as real capital-cost decisions, and the Blood Collection Room recommendation still requires an Australian building/compliance professional to verify the specific partition arrangement against the WA Skin Penetration Code once a venue is secured.

**2026-08-21 (Round 2 — growth-first venue philosophy addendum)** — Anthony stated a governing principle (venue built for the full planned operating model from day one, no future renovation) that reframes but does not resolve the Blood Collection Room and Beauty station decisions. Added a 3-way Blood Collection Room framing (2-chair room / 3-chair-ready single room / two separate rooms) and clarified that Beauty's open question is a quantity decision, not a timing decision. Both remain founder decisions.

**2026-08-21 (created)** — Written to persist the Part B-G decision-analysis work (blood collection room decision table, beauty station evidence trail, consolidated venue program, over-specification review, procurement readiness summary, procurement strategy summary) that had previously only been produced in-session and not committed to the repository, per the standing project rule that nothing stays session-only. Draws entirely on evidence already gathered in `CHINA-AUSTRALIA-SOURCING-STRATEGY.md`, `FIT-OUT-DESIGN-PROCUREMENT-BRIEF.md`, `FIT-OUT-EQUIPMENT-SCHEDULE.md`, and independently-verified prior reading of `floor-plan-concept.md`, `scenario-d-investigation.md`, and `ITEMISED-PURCHASE-LIST.md` §1 — no new research performed, no supplier/agent/WDP contact made. Both founder decisions (Blood Collection Room count, Beauty station count) remain open; this document does not resolve either.
