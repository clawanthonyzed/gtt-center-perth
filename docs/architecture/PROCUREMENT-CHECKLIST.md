# Procurement Checklist — Recommended-Import Categories

**Phase:** Commercial Launch Preparation, focus area 3 of 4. Continues directly from `docs/architecture/PROCUREMENT-STRATEGY.md`'s category recommendations. **`data/canonical/startup_costs.yml` is NOT modified this phase** — Anthony's approval of the underlying procurement strategy is still pending from the prior phase. This is a practical, fillable checklist for whoever executes the procurement once approved, not a purchase authorisation.

**Date:** 2026-08-10
**Scope:** the categories `docs/architecture/PROCUREMENT-STRATEGY.md` recommended for import or hybrid-with-import — treatment beds/massage tables, pedicure chairs, and selected furniture/equipment sub-items (flat-pack cabinetry, ancillary furniture, décor, general lighting). **Privacy/curtain systems are explicitly excluded** — `docs/architecture/CURTAIN-COMPLIANCE-CLOSURE.md` already confirmed Australian sourcing for that category, not a candidate for this checklist.

---

## 1. Supplier Verification

- [ ] Confirm supplier's business registration/legitimacy (Alibaba Verified Supplier badge, or equivalent for Made-in-China.com/1688.com per `docs/hire-purchase-china.md` §3's platform guide)
- [ ] Request Trade Assurance (Alibaba) or equivalent buyer-protection mechanism — do not pay outside a protected payment channel for a first order
- [ ] Request and review the supplier's own product certifications directly, in English, before ordering — not a generic listing claim (per `docs/architecture/CHINA-ASIA-SUPPLIER-FEASIBILITY.md`'s own core finding: "the risk is verification, not the country of origin")
- [ ] Request a sample before any bulk order — `docs/hire-purchase-china.md` §3 budgets A$50-200 for sample shipping as standard practice
- [ ] Check for existing reviews/trading history on the platform (order volume, response rate, dispute history)
- [ ] Confirm minimum order quantity (MOQ) matches this venture's actual day-one unit counts (2 of each nail/hair station-driven item per the MVP staffing timing, not a bulk quantity beyond real need)

## 2. Full Landed Cost — Not Just Unit Price

**Formula, already established in this repo, reused not re-derived:** `docs/hire-purchase-china.md` §3's own landing-cost calculation: **FOB price × 1.55** (freight A$200-500 for a 100kg shipment + 5% customs duty + 10% GST on import value + clearing agent fee ~A$200-400). Use this as the starting multiplier, refined per shipment once real quotes exist:

- [ ] Unit price (FOB — Free On Board, the price quoted by the supplier before shipping)
- [ ] Freight cost — get a real quote from a freight forwarder (`docs/hire-purchase-china.md` §6: DB Schenker Perth, Toll Global Forwarding), not the generic A$200-500/100kg placeholder, once actual shipment weight/volume is known
- [ ] Customs duty — confirm the applicable rate under ChAFTA (China-Australia Free Trade Agreement); many consumer goods are duty-free with a supplier-provided Certificate of Origin, per `docs/hire-purchase-china.md` §6 — **do not assume 5% duty applies without checking the specific HS code's actual ChAFTA treatment**
- [ ] Correct HS (customs) code for each item — `docs/hire-purchase-china.md` §6 already provides several: pedicure chairs (electrical) = 9402.10; general furniture would need its own confirmed code, not assumed identical
- [ ] GST on import value (10%) — confirm this is reclaimable as a business GST credit on the next BAS, per `docs/hire-purchase-china.md` §6, not a sunk cost
- [ ] Customs clearing agent fee (~A$200-400 per `docs/hire-purchase-china.md` §6, or the freight forwarder's own bundled clearance service)
- [ ] **Insurance** — cargo/transit insurance for the shipment, not previously itemised anywhere in this repo's own landing-cost formula. Flagged as a genuine, real cost to add to the total landed-cost calculation, not assumed included in freight by default — confirm with the freight forwarder whether it is bundled or a separate line.
- [ ] Total landed cost per unit = (Unit price × exchange rate) + (freight ÷ units in shipment) + duty + GST + (clearing fee ÷ units) + (insurance ÷ units) — **compare this total, not the FOB unit price alone, against the Australian-sourced alternative price before deciding**

## 3. Compliance Checks

**Per category, cross-referencing `docs/architecture/PROCUREMENT-STRATEGY.md`'s own findings:**

- [ ] **Treatment beds/massage tables:** non-electrical, no TGA trigger — confirm general Australian Consumer Law product-safety compliance only (stability, materials safety); no certification body approval required beyond standard consumer-goods obligations.
- [ ] **Pedicure chairs (electrical/massage function):** SAA electrical-safety approval mark required for the mains-connected component — request the supplier's test report and confirm the mark is genuine (checkable against the regulator's own compliance database, not just trusted on the supplier's word). Confirm pipeless/no-jet design for hygiene, per `docs/hire-purchase-china.md` §1D's own explicit checklist.
- [ ] **General furniture/cabinetry:** AS/NZS 4088 (public-seating stability/upholstery flammability) applies to any client-facing seating regardless of source — confirm compliance documentation exists, don't assume it by default for an import item.
- [ ] **Lighting (non-clinical, general):** SAA approval mark required for any mains-connected fitting — standard, verifiable requirement per `docs/architecture/PROCUREMENT-STRATEGY.md` §6.
- [ ] **Décor/non-electrical accessories:** minimal compliance complexity — Australian Consumer Law general product-safety standards only.

## 4. Warranty/Support Considerations

- [ ] Confirm what warranty period (if any) the supplier offers, and what it actually covers (manufacturing defect only, or also shipping damage — these are often different)
- [ ] Confirm the realistic process and lead time for a warranty claim from an overseas supplier — `docs/hire-purchase-china.md` §1E's own disclosed risk applies here: "shipping damage; weight and size make returns difficult"
- [ ] **For every category recommended for import where the item is operationally critical (a pedicure chair, a treatment table), purchase at least one Australian-sourced reference/backup unit** — the same discipline already applied to the centrifuge in `docs/hire-purchase-china.md` §1A, and explicitly recommended again in `docs/architecture/CHINA-ASIA-SUPPLIER-FEASIBILITY.md` §4. This is a standing requirement for this checklist, not optional.
- [ ] Confirm spare-parts availability and realistic replacement lead time for electrical/mechanical items (pedicure chair massage mechanisms specifically) — a mid-operation failure with a multi-week parts wait is a genuine, previously-flagged service-disruption risk.

## 5. Timing Checklist Against the Opening Sequence

- [ ] Confirm the order is placed within the existing Month 2-3 China-sourcing window (`docs/equipment-costs.md`'s own Equipment Purchase Timeline), not left to a later, more compressed window.
- [ ] For treatment beds/tables specifically: build in extra buffer ahead of the Week 15 fit-out-completion milestone (`docs/grace-startup-plan.md`) to allow for a damaged-unit replacement cycle, per the shipping-damage risk already disclosed — **not currently built into the existing purchase timeline**, a genuine scheduling refinement this checklist recommends adopting if the import approach is approved.
- [ ] Confirm the 4-8 week delivery estimate (`docs/hire-purchase-china.md`) against the specific supplier's own quoted lead time before committing — the generic window is a planning estimate, not a guarantee from any specific supplier.

---

## What This Checklist Does Not Do

It does not approve any purchase. It does not update `data/canonical/startup_costs.yml`. It does not select a specific supplier. It exists to be filled out once Anthony approves the underlying procurement strategy and a real supplier is being evaluated.

---

## Validation

No canonical YAML, financial model, or revenue/cost methodology was modified by this document. `data/canonical/startup_costs.yml` was not touched (see full validation summary in this phase's combined report-back).
