# China/Asia Supplier Feasibility Review — Startup Cost Categories

**Phase:** Commercial Assumption Alignment & External Readiness, focus area 3 of 4 — investigation only. **`data/canonical/startup_costs.yml` is NOT modified this phase.** Potential cost reductions are identified as findings for a future, separately-authorised phase to formally wire in, if adopted — not adopted here.

**Date:** 2026-08-10
**Primary existing source:** `docs/hire-purchase-china.md` (dated 2026-06-09, predates the 2026-07-31 open-plan/curtain redesign — its existing findings for furniture/treatment beds/salon equipment are reused, not re-derived; categories that document does not cover — cabinetry, reception, lighting, curtains/privacy systems, décor — are assessed fresh below, clearly flagged as new, general-market estimates where no repo source exists).

---

## 1. Category-by-Category Assessment

### Recommended for Import

| Category | Existing repo finding | Savings potential |
|---|---|---|
| **Pedicure spa chairs (Nail Station)** | `hire-purchase-china.md` §1D: China A$500-1,500 vs. AU A$800-2,000 (basic) or A$1,200-3,500 (with massage). Requires pipeless/no-jet design (hygiene) and CE/SAA electrical certification. | Up to ~A$1,500-2,000/unit — a real, already-identified saving across up to 4 units (2 day-one, 2 staged per the MVP decision review). |
| **Backwash basin + chair (Hair Station)** | `hire-purchase-china.md` §1F lists "AU beauty supply or China," A$800-2,500/unit — not further differentiated in the source, but the same pipeless/electrical-certification logic as pedicure chairs applies. | Plausible, not separately quantified in the source — flagged as needing a direct quote comparison, not assumed at the same ratio as pedicure chairs without confirmation. |
| **Non-electrical décor/soft-furnishing accessories** (throw blankets, decorative cushions, eye masks, small display items) | No direct repo finding for décor specifically, but the same general China-bulk-goods logic already applied to hire-fleet items (`hire-purchase-china.md` §2/§3) transfers cleanly — these carry no TGA/electrical-safety complexity. | Likely material on a per-unit basis, low absolute dollar impact given these are small-ticket items. |

### Possible With Compliance Checks

| Category | What's needed before importing | Repo basis |
|---|---|---|
| **Treatment beds/massage tables** | `hire-purchase-china.md` §1E: "Good quality pregnancy massage tables available from Chinese manufacturers... at A$300-800 vs A$800-2,500 locally. Risk: shipping damage; weight and size make returns difficult. Buy at least one Australian brand as reference quality." A genuine saving, with a real, already-disclosed logistics/quality-assurance risk, not glossed over. | Existing repo finding, reused directly. |
| **General furniture (lounge chairs, side tables, reception seating)** | No TGA/electrical concern for non-electrical furniture, but Australian Consumer Law product safety standards still apply (stability, flammability of upholstery foam per AS/NZS 4088 for public-seating furniture). No repo source directly addresses lounge-chair sourcing from China specifically — `hire-purchase-china.md` §1G lists only Australian/commercial-fitout sources for lounge chairs, flagging this as a genuinely new assessment, not previously researched. | New assessment this phase, flagged LOW confidence — no existing repo quote comparison exists. |
| **Salon equipment — nail tables, UV/LED lamps, hair dryers/straighteners** | `hire-purchase-china.md` covers nail tables and UV lamps only via the general "AU beauty supply" line, without a China cost comparison specifically for these smaller items (only the pedicure chairs get a direct China quote). Electrical items require SAA/electrical-safety certification (equivalent to CE, Australian-specific) — a real, standard compliance step, not unusually burdensome for established Alibaba beauty-equipment suppliers, but must be checked per supplier. | Plausible but unquantified in this repo — flagged, not assumed. |
| **Lighting fixtures (general commercial LED, non-clinical)** | No repo source. General commercial LED lighting from China is a very mature, low-risk import category (Australian retailers themselves commonly resell China-manufactured fixtures) — but must carry SAA approval marks for any mains-connected fitting, a standard, verifiable requirement, not a genuine barrier. **Clinical-grade lighting (Ra>90 in the Blood Collection Room specifically) should be treated more cautiously** — colour-rendering-index claims on budget import fittings are a known area where cheaper suppliers understate real performance; a reputable, verifiable-spec supplier matters more here than for general ambiance lighting. | New assessment this phase, flagged LOW confidence. |
| **Cabinetry/joinery components (flat-pack storage units, non-custom)** | No repo source. Standard flat-pack commercial storage (already the MVP-scenario's own preferred lower-cost option over custom joinery, per `docs/architecture/STARTUP-COST-OPTIMISATION.md` §3.1) is a mature China/Asia-sourced category (many Australian flat-pack retailers themselves resell China-manufactured units) — genuinely low compliance complexity for non-electrical storage furniture. The custom-built reception counter itself, however, is a local trades job (cabinetmaker/shopfitter), not an import candidate. | New assessment this phase — flat-pack storage plausible for import, the reception counter *build* itself is not (it is a site-installed joinery job, not a shippable product). |

### Should Remain Australian-Sourced

| Category | Reason |
|---|---|
| **TENS machines** | `hire-purchase-china.md` §2 is explicit and absolute: "TENS machines are TGA-regulated (Class IIa) medical devices... Do NOT source TENS machines from Alibaba/China for commercial hire — TGA registration required." Not applicable to this venture's day-one startup scope regardless (Phase 2/post-launch item), but the compliance rule itself is unconditional. |
| **Phlebotomy chairs and centrifuge** | `hire-purchase-china.md` §1A treats the centrifuge specifically as "critical for GDM accuracy — do not compromise," recommending an established brand (Hettich) via an Australian distributor even for the backup unit, only conditionally noting a China-sourced backup "if NATA accepts" — never proposed as the primary unit. The phlebotomy chairs themselves are lower-risk (not TGA-regulated) but sit inside the one room this venture's entire clinical credibility depends on — this review does not recommend disturbing an already-conservative, already-disclosed decision. |
| **Curtain/privacy systems** | **New compliance flag this phase, not previously addressed anywhere in this repo.** Commercial soft furnishings — including privacy curtains, especially any near an egress path or close to the Blood Collection Room — are typically subject to fire-retardancy requirements under the National Construction Code / AS 1530 series (flammability/fire-hazard properties of materials). **This applies regardless of sourcing country** — the requirement is that the fabric itself carries verifiable, tested fire-rating certification (commonly "IFR" — inherently flame retardant — with a test report against the applicable AS 1530 standard), not that China-sourced fabric is automatically non-compliant. **The risk with China/Asia sourcing specifically is verification, not the country of origin** — a generic Alibaba curtain-fabric listing is far less likely to carry a genuine, checkable Australian-standard fire-test report than an established Australian commercial-curtain supplier who routinely certifies for this exact use case. Given the acoustic-treatment work from the prior phase already established these curtains as the primary (non-deferrable) privacy mechanism for two treatment rooms, this review recommends **Australian-sourced curtain track and fabric specifically**, or, if a China supplier is genuinely considered, only with an independently verified, English-language AS 1530-equivalent test report in hand before purchase — not a general China-import recommendation. |
| **3D keepsake ultrasound scanner** | Not applicable to this review's scope (explicitly Phase 2/future, not startup capital, per `hire-purchase-china.md` §1C) — retained here only to confirm its own existing TGA-registered-distributor-only rule is unaffected by this review. |

---

## 2. Import Lead Times Against the Opening Timeline

`docs/hire-purchase-china.md`'s own Equipment Purchase Timeline (via `docs/equipment-costs.md`) allows "4-8 weeks delivery for China-sourced items," scheduled for Month 2-3 of the fit-out sequence — **before** the Month 3-4 consumables/emergency-equipment purchases and well ahead of the Week 19-20 launch target (`docs/grace-startup-plan.md`). This existing buffer is genuinely adequate for the items already assessed as import-feasible (pedicure chairs, treatment beds) — no timeline risk identified for those specifically. **New items flagged this phase (lighting, cabinetry, general furniture) have not been checked against this same buffer** — if pursued, they should be sequenced into the same Month 2-3 window, not treated as a separate, later purchase that could compress the fit-out schedule.

---

## 3. Compliance/Certification Requirements Summary

- **Electrical items (pedicure/backwash chairs with massage function, lighting):** SAA approval mark required for any mains-connected fitting sold/installed in Australia — a standard, verifiable requirement, not a unique barrier to China sourcing specifically.
- **Curtains/soft furnishings:** fire-rating certification (AS 1530 series or equivalent), verification-dependent regardless of source country — see §1's Australian-sourced recommendation above.
- **Furniture (public seating):** AS/NZS 4088 stability and upholstery-flammability considerations apply to any commercial lounge/waiting-area seating, regardless of source.
- **TGA-regulated items (TENS, ultrasound):** confirmed hard exclusions, already established in `hire-purchase-china.md`, unaffected by this review.

## 4. Warranty/Support Implications

`docs/hire-purchase-china.md` already discloses the core trade-off honestly for massage tables: "Risk: shipping damage; weight and size make returns difficult." This applies generally across every furniture/equipment category assessed here — China-sourced items typically carry weaker, harder-to-action local warranty support than an Australian-distributed brand, a real ongoing operational risk (a broken pedicure chair mid-week with a multi-week replacement-parts lead time is a genuine service-disruption risk this venture has not previously modelled). **Recommendation, consistent with the existing massage-table guidance:** for any category recommended for import, purchase at least one Australian-sourced reference/backup unit where the item is operationally critical (a spare pedicure chair, a spare massage table), mirroring the existing centrifuge-backup logic already established in `hire-purchase-china.md` §1A.

---

## 5. Potential Startup Cost Reduction — Finding Only, Not Adopted

Using the already-established China-vs-Australian price gaps for the items this repo has already researched (pedicure chairs, massage/treatment tables), a rough, directional saving is identifiable across the equipment lines in `data/canonical/startup_costs.yml#adopted_planning_scenarios`'s Category E (equipment) — **not quantified into a specific dollar figure this phase**, since doing so would require re-deriving the exact unit counts already committed in that record and is explicitly out of scope ("do NOT change canonical figures this phase, this is investigation only"). The directionally clearest opportunities, in priority order: pedicure chairs (largest known per-unit gap, already researched), massage/treatment tables (second-largest known gap, already researched, with a disclosed logistics caveat), and — newly flagged this phase, unquantified — flat-pack cabinetry/storage as a substitute for custom joinery, which the MVP scenario already assumes uses "standard flat-pack" pricing without specifying a sourcing country.

---

## 6. Risks Identified

- **Curtain fire-rating verification is a genuine, previously-unflagged compliance gap** — not specific to China sourcing, but the verification burden is real regardless of source and has never been addressed anywhere in this repo before this document.
- **Shipping damage/return difficulty for large furniture items** (already disclosed for massage tables, extends logically to any bulky lounge furniture considered for import) is a real, underweighted risk if pursued at scale without the same "buy one Australian reference unit" mitigation already applied to the centrifuge.
- **Warranty/support gap** — no China-sourced equipment category assessed here has a clear local support pathway; a mid-operation equipment failure could create a real service disruption this venture has not previously planned around.

## 7. Recommended Next Decisions

1. **If cost reduction is a genuine priority, formally quantify the pedicure-chair and treatment-table savings against the actual committed unit counts** in a future, separately-authorised phase — this review only confirms the categories are worth pursuing, it does not re-derive the canonical figures.
2. **Obtain a genuine AS 1530-equivalent fire-test report requirement into any future curtain/fabric procurement brief**, regardless of source country, before the Concept Design Preparation brief (`docs/architecture/CONCEPT-DESIGN-BRIEF.md`, this phase) is handed to a designer/architect.

---

## Validation

No canonical YAML, financial model, or revenue/cost methodology was modified by this document. `data/canonical/startup_costs.yml` was not touched — every cost figure above is either quoted directly from `docs/hire-purchase-china.md` or presented as a new, LOW-confidence, clearly-flagged general-market observation (see full validation summary in this phase's combined report-back).
