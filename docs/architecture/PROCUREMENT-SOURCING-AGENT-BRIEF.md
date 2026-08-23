# Sourcing Agent Information Package

Status: current as of 2026-08-23. Self-contained: an external sourcing agent should be able to understand the project and begin a scoping conversation from this document alone, without access to the rest of this repository. Built entirely from existing repository research, no new claims are introduced here. **This is a preparation document. No sourcing agent has been contacted. No RFQ, sample request, or order has been sent.**

## 1. Business/Concept Summary

Western Australia's first venue built specifically around the mandatory Glucose Tolerance Test (GTT) wait, a routine pregnancy screening that requires a 2-3 hour on-site wait between blood draws. The venue turns that clinically necessary wait into a premium wellness experience (massage, beauty treatments, nail and hair services, a cafe, a keepsake 3D ultrasound scan for entertainment purposes only, never diagnostic) without pretending to be either a pathology lab or a day spa. Blood collection itself is provided by a pathology partner (WDP), not by this venture directly; the venue provides the space, the wellness/beauty services, and the waiting experience around it.

## 2. Brand Direction

Locked, usable today: a 7-colour palette (warm ivory, warm stone, deep brown, earthy terracotta, muted olive, dusty rose, warm brass; exact hex values in `outputs/brand/warm-stone-tokens.css` and `outputs/brand/brand-tokens.css`), a warm/restrained material language (timber tones, commercial-duty upholstery in wipe-clean vinyl, no high-gloss or overtly clinical finishes), and an explicit "what the venue must not look like" principle: not a clinical waiting room, not a budget nail bar, not an overtly glossy day-spa look. Final venture name is not yet confirmed; do not brief any signage or wordmark work until it is.

## 3. Venue Program

The venue has not yet been secured (site-dependent items below cannot be finalised until it is). The physical program is fixed regardless of which site is eventually chosen:

| Area | Physical build capacity | Key equipment | China-sourcing suitability |
|---|---|---|---|
| Blood Collection | 1 room, built/serviced for 3 chairs | Phlebotomy chairs, specimen fridge, sharps container | Australian-sourced (clinical/regulated) |
| Massage | 3 stations | Massage table/bed (format not yet decided) or chair, bolster set | Needs Australian verification on materials |
| Beauty | 3 stations | Treatment bed, storage, task lighting | Good sourcing candidate |
| Nail | 4 stations, open-plan | Nail table with dust collector, UV/LED lamp, tool trolley | Good OEM/ODM candidate |
| Pedicure | 4 chairs, same zone as Nail | Pipeless pedicure spa chair (hygiene-mandatory) | Good sourcing candidate, highest-confidence saving in the register |
| Hair Wash | 2 stations | Backwash basin, client chair | Good sourcing candidate |
| Hairdresser | 4 stations, open-plan | Styling chair, mirror, cabinetry, trolley | Good sourcing candidate (excludes named-brand hair dryers/straighteners, which remain Australian-sourced) |
| Reception | 2 workstations | Desk, payment terminal, storage | Australian-sourced furniture |
| Cafe | 1 counter zone | Fridge, coffee machine, chilled/boiling water tap, prep counter | Fixtures are good sourcing candidates; food itself is Australian-supplied |
| Lounge | 3-4 three-seat couches, final count site-dependent | Couches, kiosk-mounted tablets | Good OEM/ODM candidate |
| Staff area / Storage | 1 room each | Lockers, shelving, kitchenette | Australian-sourced |
| Toilets | Patient WC (accessible), patient WC (standard), staff WC | Standard fixtures | Australian-sourced preferred, accessibility-verification required |

Full detail: `docs/architecture/VENUE-PROGRAM-AUTHORITATIVE.md`.

## 4. Procurement Categories in Scope for a Sourcing Agent

China-suitable (per `docs/architecture/PROCUREMENT-CHINA-PACKAGE.md`, 10 sourcing groups): reception/cafe joinery-adjacent furniture, nail stations, hair styling stations, mirrors, decorative lighting, general furniture, treatment furniture, pedicure furniture, decorative hardware, other commercial fit-out items.

**Explicitly excluded from China sourcing** (Australian-only, clinical/regulated/fire-life-safety): phlebotomy chairs, centrifuge (WDP-dependent regardless of sourcing model), sharps containers, biohazard waste bins, TGA-listed disinfectant, AED, named-brand hair dryers and straightening irons (Dyson/GHD/Cloud Nine trade accounts, warranty-driven exclusion).

## 5. Quality Expectations

The brand positioning is premium, not budget. Sourcing must not become "buy the cheapest available version" of any item. Every item proceeding to procurement requires, at minimum: a named supplier specification, an approved drawing or reference image, a material sample, a finish sample, factory confirmation of the specification, pre-production approval, and pre-shipment inspection. Cheapest-compliant-option sourcing without these steps is not acceptable for this venture.

## 6. Compliance and Commercial-Use Requirements

Every item used in daily client-facing service (not occasional/domestic use) must be commercial-duty rated, not domestic-grade. Items with an electrical component require an Australian electrical safety mark (SAA) regardless of manufacturing origin; this must be confirmed even for China-manufactured items, ideally by an Australian-based sourcing agent or a licensed electrician before purchase. Pedicure chairs must be pipeless (no-jet) by design for hygiene, confirmed by factory documentation, not assumed from a product listing. Hair styling chairs require AS/NZS 4088 stability-standard compliance.

## 7. Inspection Requirements

Every China-manufactured item proceeding to procurement requires: a factory sample of material/finish before full production, pre-production approval, and independent pre-shipment inspection. Independent inspection services already researched in this venture's own sourcing-strategy work: SGS, Bureau Veritas, and QIMA, at a real, current, sourced market rate of US$149-350 per inspection-day (typically 3-4 days across pre-production, in-line, and pre-shipment checkpoints). Full detail: `docs/architecture/CHINA-AUSTRALIA-SOURCING-STRATEGY.md` §3.2/§7.

## 8. Freight and Landed-Cost Requirements

A real landed-cost figure cannot be produced until: (1) a venue is confirmed (for delivery/installation cost), (2) a finalised, locked item list exists (for freight volume/weight), (3) real quotes exist from at least one sourcing agent and one freight forwarder. The full cost-stack structure this venture uses (factory price, tooling, packaging, inspection, agent fee, inland transport, consolidation, international freight, marine/cargo insurance, customs duty under ChAFTA, GST, local delivery, unloading, installation, replacement/defect allowance) is set out in full in `docs/architecture/CHINA-AUSTRALIA-SOURCING-STRATEGY.md` §7. The existing per-parcel placeholder figure ("A$200-500 for a 100kg shipment") is explicitly inadequate for a whole-venue, container-scale order and should not be quoted to any agent as a real freight estimate. A real freight-forwarder quote is required (DB Schenker Perth or Toll Global Forwarding, both already identified as candidates, not yet contacted).

## 9. Installation and Interface Requirements

Every responding supplier or agent must itemise installation separately, not bundle it into the unit price. Installation cost and feasibility are site-dependent (venue floor plate affects complexity) and cannot be finalised before a venue is secured. Electrical, plumbing, and ventilation interfaces (GPO placement, LEV ducting, water supply/drain for pedicure and hair-wash stations) must be confirmed by licensed Australian trades, not by the sourcing agent.

## 10. Packaging Requirements

Export-grade packaging suitable for sea freight, typically included as a line item in agent/factory quotes; confirm this is included rather than assumed. No standalone repository figure exists for packaging cost in isolation from the overall quote.

## 11. Warranty and Replacement-Parts Requirements

Warranty and replacement-parts availability must be confirmed before order for every item, not assumed. This is flagged in this venture's own research as a genuine, previously unaddressed planning gap (no item in the register currently has a confirmed warranty term or replacement-parts commitment). For the pedicure spa chairs specifically, confirm local or importable availability of motor/plumbing fitting replacement parts before order (the pipeless design has no jets/pumps requiring replacement, but the chair's own mechanical parts still need a confirmed source).

## 12. Required Supplier Documentation

Certificate of Origin (for ChAFTA duty-free treatment where applicable, item-specific, not uniform across all items), factory test/compliance documentation for any electrical item, material composition documentation for any item claiming a specific grade or finish, and confirmation of MOQ (minimum order quantity) per item.

## 13. RFQ Response Format Required

Every RFQ response should itemise, per item: FOB/EXW unit price, MOQ, lead time, packaging method, whether export-grade packaging is included, inspection availability and cost, installation cost (separately itemised, not bundled), warranty term, and replacement-parts availability. This format has not yet been sent to any supplier or agent; it is stated here so that when it is used, comparisons across quotes are apples-to-apples.

## 14. Supplier Comparison Methodology

Once real quotes exist, compare on: total landed cost (not FOB price alone), inspection/QC provision, warranty term, replacement-parts availability, lead time, and evidence of genuine hospitality/commercial-furniture experience (case studies, references, prior projects of a comparable nature) rather than agent claims alone. Per this venture's own research, Epic Sourcing Australia is the closest candidate found to an end-to-end capable partner (Australian-based, furniture-specialised, in-house QC claim) but this has not been independently verified beyond their own public materials; no third-party review or salon/wellness-specific case study was found. FBM Sourcing (China-based) shows deeper hospitality-FF&E-specific evidence but carries a different accountability/communication risk profile as a China-based agent. Neither has been contacted.

## 15. Hard Boundary (Restated, Not Optional)

No sourcing agent, Australian or China-based, however capable, has any legal authority or competence to perform Australian architectural, engineering, building-certification, or regulated-clinical-design work. That work stays with Australian licensed professionals (architect, engineer, electrician, plumber, LEV/HVAC contractor) and the pathology partner (WDP) for anything touching the Blood Collection Room, regardless of which procurement model is used.

## 16. What Is Not Yet Locked (Do Not Brief These Categories Yet)

Massage station format (table/bed vs chair-based), final venture name (do not brief signage/wordmark work), exact final floor plate and room dimensions (site-dependent), Cafe upgrade decision (affects Cafe equipment spec). Full list: `docs/architecture/PROCUREMENT-FOUNDER-DECISIONS.md`.

## Sourcing

`docs/architecture/VENUE-PROGRAM-AUTHORITATIVE.md`, `docs/architecture/CHINA-AUSTRALIA-SOURCING-STRATEGY.md` (§3.2, §7, §8, §9, §10), `docs/architecture/PROCUREMENT-CHINA-PACKAGE.md`, `docs/architecture/BRAND-IDENTITY-FRAMEWORK.md` §2, `outputs/brand/warm-stone-tokens.css`.

## Changelog

**2026-08-23 (created):** Built as the self-contained sourcing-agent information package requested by the founder's governance instruction (Part 7), drawing entirely on existing repository research (no new claims introduced), covering business summary, brand direction, venue program, procurement categories, quality/compliance/inspection/freight/landed-cost/installation/packaging/warranty requirements, required documentation, RFQ format, and comparison methodology.
