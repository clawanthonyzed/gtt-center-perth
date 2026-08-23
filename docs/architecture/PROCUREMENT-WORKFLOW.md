# Procurement Workflow: Decision to Purchase

Status: current as of 2026-08-23. The actual process from identifying an item through to sign-off, so anyone running procurement (Venue Manager once hired, or Anthony in the interim) follows the same sequence for every item rather than improvising per purchase. This document does not invent an approval hierarchy the business has not decided; no named approval role beyond Anthony exists yet (the Venue Manager is a confirmed future hire, not yet in place, per `docs/HANDOFF.md` and this repo's own standing facts).

## The 17 Steps

**1. Identify item.** Look it up in `docs/architecture/MASTER-PROCUREMENT-SHOPPING-LIST.md` by Item ID, or find it via `docs/architecture/PROCUREMENT-SHOPPING-LIST-PLAIN-ENGLISH.md` or `docs/architecture/PROCUREMENT-ROOM-BY-ROOM-CHECKLIST.md` if the Item ID is not already known.

**2. Confirm required.** Check the item's Readiness classification and Required-at-Opening flag in `docs/architecture/PROCUREMENT-ITEM-SPECIFICATIONS-FULL.md`. Do not proceed on a Future/Optional (H) item without a deliberate decision to bring it forward.

**3. Confirm quantity.** The quantity is the master register's own Quantity column, not re-derived here. Where the Quantity Basis is SITE-DEPENDENT or STAFF-DEPENDENT, quantity is not yet fixed; do not guess a number, use the venue measurement or headcount confirmation instead (Step 5).

**4. Confirm specification.** Check `docs/architecture/PROCUREMENT-ITEM-SPECIFICATIONS-FULL.md` for the item's specification, dimensions (if known), material/finish (if known), and performance requirements. Where these read "Not yet determined", that is the actual state, not an oversight; resolve it before requesting a quote.

**5. Confirm venue/site dependency.** If the item's Readiness is C (SITE DEPENDENT), check `docs/architecture/PROCUREMENT-SITE-DEPENDENT-HOLD-LIST.md` for exactly what must be measured and who confirms it. Do not proceed to Step 6 until the site-dependent fact is resolved.

**6. Confirm compliance.** Check the Certification/Compliance field. If the item requires professional verification (Readiness D), engage the specific licensed professional named there (electrician, plumber, HVAC/LEV contractor, building surveyor, or access consultant, depending on the item) before proceeding.

**7. Determine China/Australia route.** Use the item's own Sourcing classification (CN/AU/HY/PRO/WDP/SITE). China-suitable items are grouped in `docs/architecture/PROCUREMENT-CHINA-PACKAGE.md`; Australian-only items are grouped in `docs/architecture/PROCUREMENT-AUSTRALIA-PACKAGE.md`. Hybrid items can go either way; compare quotes once both exist rather than picking one route by default.

**8. Obtain quote.** Send the RFQ using the format in `docs/architecture/FIT-OUT-SUPPLIER-RFQ-TEMPLATE.md` (unit price, MOQ, lead time, packaging, inspection availability, installation cost itemised separately, warranty term, replacement-parts availability). **No supplier or sourcing agent has been contacted for any item as of this document's creation.**

**9. Compare suppliers.** Compare on total landed cost (not FOB/unit price alone), inspection/QC provision, warranty term, replacement-parts availability, lead time, and evidence of genuine commercial/hospitality experience, per the methodology in `docs/architecture/PROCUREMENT-SOURCING-AGENT-BRIEF.md` §14.

**10. Confirm landed cost.** For China-sourced items, calculate the full cost stack (factory price, tooling if applicable, packaging, inspection, agent fee, freight, insurance, customs duty, GST, local delivery, installation, replacement/defect allowance) using the framework in `docs/architecture/CHINA-AUSTRALIA-SOURCING-STRATEGY.md` §7. Do not use the existing per-parcel freight placeholder ("A$200-500 for 100kg") for a whole-order calculation; it is explicitly flagged as inadequate at that scale.

**11. Approve purchase.** Anthony approves the purchase. No other approval role currently exists in this business; once a Venue Manager is hired, whether purchasing authority is delegated (and to what value threshold) is itself a future decision, not invented here.

**12. Order.** Place the order with the selected supplier once approved.

**13. Inspect.** For China-sourced items, an independent pre-shipment inspection is required (SGS, Bureau Veritas, or QIMA, at the researched US$149-350/inspection-day rate, per `docs/architecture/CHINA-AUSTRALIA-SOURCING-STRATEGY.md` §3.2/§7) before the item ships. For Australian-sourced items, inspect on delivery against the order specification.

**14. Receive.** Confirm the delivered item matches the order (quantity, specification, condition) before signing for delivery.

**15. Record warranty/documentation.** Record the warranty term, replacement-parts source, Certificate of Origin (where applicable for ChAFTA duty treatment), and any compliance certificate (SAA electrical mark, AS/NZS standard, TGA listing, or equivalent) against the Item ID. No central warranty register exists yet; this is a genuine gap already disclosed in `docs/architecture/PROCUREMENT-CHINA-PACKAGE.md` and should be built once the first orders are placed.

**16. Install.** Site-dependent and professional-verification items are installed by the relevant licensed trade (electrician, plumber, HVAC/LEV contractor) once delivered. Freestanding/portable items do not require this step.

**17. Sign off.** Confirm the item is in place, functional, and matches the specification before marking it complete in the master register.

## China-Sourced Items: Additional Steps Within 7 to 13

For any item routed through China (Step 7), the following must happen before Step 8 (obtaining a binding quote) proceeds to an actual order: RFQ sent with a full technical drawing or reference image, materials and finish samples reviewed and approved, factory confirmation of the specific design requirement in writing (e.g. pipeless pedicure chair design, dust-collector electrical safety), pre-production approval given before the factory begins the full run, independent pre-shipment inspection completed, export-grade packaging confirmed, freight arranged (container/consolidated, not the inadequate per-parcel placeholder), Australian compliance confirmed (SAA electrical mark regardless of manufacturing origin), landed cost calculated in full (Step 10), and a warranty/replacement-parts policy confirmed in writing. This sequence is already set out in full in `docs/architecture/PROCUREMENT-CHINA-PACKAGE.md`'s closing section; it is restated here in workflow order rather than duplicated with different wording.

## What This Workflow Deliberately Does Not Invent

A formal purchasing approval hierarchy beyond Anthony (no Venue Manager is hired yet, and no delegated purchasing authority or dollar-value threshold has been decided). A central warranty/documentation register (a genuine, disclosed gap, not yet built). A fixed number of supplier quotes required per purchase (not decided anywhere in this repository; 2-3 comparable quotes is common commercial practice but is not stated here as a rule since no such rule exists in this venture's own planning).

## Sourcing

`docs/architecture/MASTER-PROCUREMENT-SHOPPING-LIST.md`, `docs/architecture/PROCUREMENT-CHINA-PACKAGE.md`, `docs/architecture/PROCUREMENT-AUSTRALIA-PACKAGE.md`, `docs/architecture/PROCUREMENT-SOURCING-AGENT-BRIEF.md`, `docs/architecture/CHINA-AUSTRALIA-SOURCING-STRATEGY.md`, `docs/architecture/FIT-OUT-SUPPLIER-RFQ-TEMPLATE.md`, `docs/architecture/PROCUREMENT-SITE-DEPENDENT-HOLD-LIST.md`.

## Changelog

**2026-08-23 (created):** Built per direct founder instruction (Part 5) as the actual decision-to-purchase process, restating existing researched detail (China QC sequence, landed-cost framework, RFQ comparison methodology) in workflow order rather than duplicating it with new wording, and explicitly declining to invent an approval hierarchy the business has not decided.
