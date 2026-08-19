# Lounge Device Spec — Tablets/iPads

**Date:** 2026-08-19 | **Status:** PROPOSED DESIGN REQUIREMENT, not yet formally approved — created fresh per Anthony's explicit instruction, since no prior document in this repository specified this. **This is the single canonical document for this topic — other chapters/documents should reference this one, not restate or vary the spec independently.**

**Certainty label for this entire document: MODELLED (proposed design requirement)** — reasoned from the actual Lounge design, client demographic, and premium positioning already established elsewhere, but not yet costed, procured, or approved.

---

## 1. Purpose

The GTT Lounge (35sqm, open-plan, 8 reclining/comfort chairs, `docs/floor-plan-concept.md`) is where clients wait between draws and services during a multi-hour AM visit (`docs/architecture/OPERATING-MODEL-18-CLIENTS.md` §2), and where companions/children wait for the duration of the visit (`docs/architecture/CHILDREN-COMPANION-POLICY.md`). A shared device (or devices) in this space serves two genuinely different possible purposes, not yet decided between:

1. **Client-facing amenity** — light entertainment/information during a wait that, per §2's operating-model finding, has almost no idle dwell time built into the current schedule (see the honest finding already logged in `OPERATING-MODEL-18-CLIENTS.md` §2: "the AM lounge is used for two 10-minute transition buffers, not a long relaxed wait" — meaning a client-facing device would mostly be used during those short buffer windows, not an extended sit-and-browse period).
2. **Companion/child-facing amenity** — since companions and any accompanying children may be in the Lounge for the client's ENTIRE visit (up to ~2 hours for the AM structure), a device serving them specifically has a much clearer, longer usage window than one aimed at the client herself.

**Proposed conclusion, not yet decided by Anthony:** given finding #1 above (the AM schedule leaves little client dwell time), a lounge device is **more likely to be primarily useful for companions/children** than for the client herself — but this is a proposed inference from the existing operating-model finding, not a settled design decision. Flagged for Anthony's confirmation.

## 2. Proposed Specification

| Aspect | Proposed spec | Certainty |
|---|---|---|
| Device count | 2 (matches the 2-chair synchronized AM model's typical simultaneous-pair pattern, plus general PM lounge use) | BALLPARK-ESTIMATE — not costed or confirmed |
| Device type | Consumer tablet (iPad or equivalent Android tablet) | MODELLED |
| Mounting/storage | Wall or table-mounted secure stand (theft/damage deterrent, consistent with a hospitality-not-clinical Lounge aesthetic — a bare tablet on a low table in a premium space is a real damage/theft risk) | MODELLED |
| Charging | Dedicated charging dock/cable integrated into the mount, not a visible loose cable (aesthetic requirement, per the premium/restraint brand principle, `docs/strategy/PREMIUM-POSITIONING.md`) | MODELLED |
| Content/use restrictions | Curated content only — no open internet browser, no app-store access, no social media login capability. Suggested content: a simple welcome/orientation screen (what happens next in the visit, reinforcing the physical welcome/itinerary card), light entertainment (age-appropriate games/videos if primarily companion/child-facing per §1), NOT medical/clinical information (avoids any appearance of self-diagnosis or clinical advice being dispensed via an unsupervised device) | MODELLED — content curation itself not yet built |
| Hygiene/cleaning | Wipeable case, included in the existing daily-turn/weekly-deep-clean cleaning service (`docs/architecture/FINANCIAL-FIGURE-REFERENCE.md` §4 cleaning line) — no new cleaning cost line proposed, folded into the existing service | MODELLED |
| Privacy | No client account login, no browsing history retained between uses, device resets to a home/welcome screen after each session (a kiosk-mode configuration) — a real, buildable requirement, not yet implemented | MODELLED |
| Security | Kiosk-mode device management (a standard, low-cost tablet-management software category) to prevent app installation, settings changes, or browsing outside curated content | MODELLED — specific software/vendor not researched this round |
| Supervision | No venue staff supervision of device use is proposed — self-service, consistent with a hospitality (not childcare) positioning; parents/companions remain responsible for supervising any child's device use, consistent with `CHILDREN-COMPANION-POLICY.md`'s supervision-responsibility framing | MODELLED, cross-referenced |
| Client-facing vs companion/child-facing | Primarily companion/child-facing, per §1's reasoning — proposed, not confirmed | **FOUNDER DECISION REQUIRED** |

## 3. What This Document Does NOT Cover

- Exact device brand/model/cost (not researched this round — a procurement task, would sit in `docs/architecture/ITEMISED-PURCHASE-LIST.md` once specified).
- Content licensing (if entertainment content beyond a simple welcome screen is proposed, e.g. a video-streaming service, licensing/subscription cost is not modelled here or anywhere in the current financial model).
- Any tablet use INSIDE a treatment room or the Blood Collection Room — this document is scoped to the Lounge only.

## 4. Cross-References — This Is the Canonical Document

- `docs/architecture/OPERATING-MODEL-18-CLIENTS.md` §2 (the AM dwell-time finding this spec's core reasoning depends on)
- `docs/architecture/CHILDREN-COMPANION-POLICY.md` (supervision responsibility)
- `docs/floor-plan-concept.md` (Lounge dimensions/layout)
- The future Master Dossier's Lounge/Customer Experience chapter

---

## Changelog

**2026-08-19** — Created fresh, per Anthony's explicit instruction, since no prior document in this repository specified lounge devices. Reasoned from the existing AM dwell-time finding (`OPERATING-MODEL-18-CLIENTS.md` §2) to propose the devices are primarily companion/child-facing, not client-facing — flagged explicitly as a proposed inference requiring Anthony's confirmation, not a settled decision.
