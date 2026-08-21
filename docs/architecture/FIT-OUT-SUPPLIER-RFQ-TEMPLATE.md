# Fit-Out Supplier RFQ Template — Overseas OEM/ODM Commercial Interior Suppliers

**Date:** 2026-08-21 | **Companion document to:** `docs/architecture/FIT-OUT-DESIGN-PROCUREMENT-BRIEF.md` §22, §23, §26. **Status:** Draft template, not yet sent to any supplier. **No supplier has been contacted. No purchase authorised. No manufacturing authorised.**

**Purpose:** a fillable RFQ (Request for Quotation) checklist to send alongside the main design brief, so a supplier's response can be compared apples-to-apples against another supplier's response — including the two suppliers that triggered this brief (Guangzhou XERA Display, Guangzhou Brutalist Store Display Products), neither of which is assumed suitable or pre-approved.

---

## Part 1 — Supplier Profile

| # | Required from supplier | Response |
|---|---|---|
| 1 | Company profile (legal name, years trading, ownership structure) | |
| 2 | Factory location(s) | |
| 3 | Manufacturing capabilities (in-house vs subcontracted, per category) | |
| 4 | Relevant completed projects (with photos/references, verifiable) | |
| 5 | Salon/beauty/medical/wellness project experience specifically (not just general retail fit-out) | |
| 6 | Design capability (in-house design team size/qualifications) | |
| 7 | 3D rendering capability (software used, sample output) | |
| 8 | CAD capability (file formats supported) | |
| 9 | Shop-drawing capability (sample provided) | |

## Part 2 — Materials and Finishes

| # | Required from supplier | Response |
|---|---|---|
| 10 | Material samples (physical, shipped, not photographs) | |
| 11 | Finish samples matching the locked palette (`outputs/brand/warm-stone-tokens.css` — 7 exact hex values, no substitution) | |
| 12 | Hardware specifications (brand, finish, warm brass/bronze only per the brief's §2.5 material schedule) | |
| 13 | Furniture specifications (frame material, upholstery, joinery method) | |

## Part 3 — Technical Specifications

| # | Required from supplier | Response |
|---|---|---|
| 14 | Electrical specifications — voltage/frequency compatibility with Australia (230V/50Hz), plug type, SAA certification status for every mains-connected item | |
| 15 | Plumbing specifications — for any plumbed item (backwash basins, pedicure chairs) | |
| 16 | Fire-rating information — for any soft furnishing/curtain fabric proposed (AS 1530.2/1530.3), if the supplier is asked to quote this category at all (see the brief's §21 Category C — Australian-sourced is the standing recommendation for curtain fabric specifically) | |
| 17 | Material safety information (upholstery foam flammability, general product safety documentation) | |

## Part 4 — Logistics

| # | Required from supplier | Response |
|---|---|---|
| 18 | Packaging method | |
| 19 | Export packaging (shock/moisture protection for a long sea freight to Australia) | |
| 20 | Shipping terms offered | |
| 21 | Incoterms (FOB, EXW, CIF, DDP — state which is quoted) | |
| 22 | Minimum order quantities (MOQ) per item — confirm against this venture's actual day-one unit counts, not a bulk quantity beyond real need | |
| 23 | Production lead time | |
| 24 | Sample lead time | |
| 25 | Installation support — remote guidance only, or genuine on-site capability | |
| 26 | On-site installation options, if any — realistic given the distance to Perth, WA | |

## Part 5 — Quality, Warranty, Commercial Terms

| # | Required from supplier | Response |
|---|---|---|
| 27 | Warranty terms (duration, what's covered — manufacturing defect only, or also shipping damage) | |
| 28 | Spare parts availability | |
| 29 | Replacement-component lead time | |
| 30 | Quality-control process (in-house QC, 3rd-party inspection, at what production stages) | |
| 31 | Pre-shipment inspection process | |
| 32 | Certifications held (list all, with copies) | |
| 33 | Australian compliance documentation where applicable (SAA marks, AS 1530 test reports, ARTG registration for any TGA-adjacent item — though per the brief's §21, TGA-regulated items should not be sourced from this channel at all) | |
| 34 | Payment terms | |
| 35 | Revision policy (how many design revisions included before additional cost applies) | |
| 36 | Design ownership/IP terms (who owns the final design if this venture doesn't proceed to production) | |

---

## Part 6 — Required Deliverables Before Any Production Authorisation

Per the brief's §23, no production is authorised from renders alone. A responding supplier must produce, at their own cost or an agreed design-fee stage, before any purchase order is issued:

- [ ] Concept boards
- [ ] Material boards
- [ ] Floor-plan proposal (against the brief's §3 station program, with §3.2's ambiguity resolved first)
- [ ] Furniture layout
- [ ] 3D renders
- [ ] Elevations
- [ ] Joinery drawings
- [ ] Furniture drawings
- [ ] Equipment schedule (matching `FIT-OUT-EQUIPMENT-SCHEDULE.md`'s format)
- [ ] Lighting proposal
- [ ] Electrical load schedule
- [ ] Plumbing schedule
- [ ] Ventilation/extraction proposal
- [ ] Colour schedule (matching the locked 7-colour palette exactly)
- [ ] Finish schedule
- [ ] Packing schedule
- [ ] Itemised quotation (per Part 7 below — not a single lump-sum figure)

---

## Part 7 — Itemised Quotation Requirement

**A supplier must not be permitted to respond with a single vague "US$XX,XXX complete shop" figure.** The quotation must itemise, per the brief's §24:

| Cost component | Required |
|---|---|
| FOB/EXW unit price, per line item | Mandatory |
| Packaging cost | Mandatory |
| Freight estimate | Mandatory, against actual shipment weight/volume once known |
| Cargo/transit insurance | Mandatory — do not assume bundled into freight by default |
| Customs duty | Mandatory, with the correct HS code and applicable ChAFTA treatment stated per item — do not assume a flat rate |
| GST on import value (10%) | Stated separately — reclaimable as a business GST credit, not a sunk cost |
| Clearing agent fee | Mandatory |
| Australian delivery cost | Mandatory |
| Installation cost | Mandatory, with local-trades inclusions/exclusions stated explicitly |
| Design fees | Mandatory, if not folded into unit pricing |
| Tooling costs | Mandatory, if any custom tooling is required |
| Sample costs | Mandatory |
| Revision costs beyond the included allowance | Mandatory |
| Spare parts pricing | Mandatory |
| Explicit exclusions | Mandatory — anything not covered by the quoted price must be listed, not left implicit |

**Landed-cost sanity-check formula (starting point only, to be refined against the real quote above):** FOB price × ~1.55 (freight + duty + GST + clearing-agent-fee approximation), per `docs/hire-purchase-china.md` §3/§6.

---

## Part 8 — Supplier Comparison Matrix (Blank Template)

To be filled once real RFQ responses exist from more than one supplier — including, but not limited to, Guangzhou XERA Display and Guangzhou Brutalist Store Display Products. **No ranking exists yet — insufficient evidence, neither supplier contacted.**

| Dimension | Supplier A | Supplier B | Supplier C |
|---|---|---|---|
| Design capability | | | |
| Manufacturing capability | | | |
| Relevant completed projects | | | |
| Quality (sample assessment) | | | |
| Customisation (exact palette match) | | | |
| Australian export experience | | | |
| Compliance documentation (genuine, checkable) | | | |
| Communication quality | | | |
| Lead time | | | |
| Full landed-cost pricing | | | |
| Warranty | | | |
| Installation support | | | |
| Logistics track record | | | |
| Whole-project coordination ability | | | |
| Ability to work from Australian drawings | | | |
| Shop-drawing quality | | | |
| Willingness to sample before bulk order | | | |

---

## What This Template Does Not Do

Does not approve any purchase. Does not select a supplier. Does not rank Guangzhou XERA Display or Guangzhou Brutalist Store Display Products, or any other supplier — neither has been contacted, evaluated, or assumed suitable. Does not authorise sending this RFQ to any supplier — that remains Anthony's decision. Does not commit to any manufacturing.

---

## Changelog

**2026-08-21 (created)** — Built per the fit-out design/procurement brief's §22/§23/§26 requirements, as a fillable companion checklist rather than folding a 36-item table and a full comparison matrix into the narrative brief itself. No supplier contacted, no figures invented — every requirement traces to an existing repository procurement-research finding (`docs/architecture/PROCUREMENT-CHECKLIST.md`, `docs/hire-purchase-china.md`) or is a standard RFQ-hygiene item this venture had not previously formalised into one document.
