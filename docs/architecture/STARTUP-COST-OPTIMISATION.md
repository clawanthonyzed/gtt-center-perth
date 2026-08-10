# Startup Cost Optimisation & Minimum Viable Opening Model

**Phase:** Startup Cost Optimisation — a bounded analysis phase. This document reclassifies every item from `docs/architecture/startup-cost-reconstruction.md` by timing (mandatory before first revenue / required within 3-6 months / optional-growth) and builds a genuine Minimum Viable Opening scenario. **It does not modify `data/canonical/startup_costs.yml`, the financial model, or the funding requirement calculation.** Anthony reviews this analysis before anything is wired into the canonical layer.

**Date:** 2026-08-10
**Version used as source of truth:** commit `c1ef066` (Startup Cost Reconstruction) and everything it built on.

**Hard constraint honoured throughout:** no compliance, safety, or legal requirement is reduced anywhere in this document. This optimises *spend*, never *standard*. Every item classified Mandatory-before-revenue for compliance/safety reasons is explicitly protected and never appears in the deferred schedule.

---

## Executive Summary

Three headline figures (Pre-Opening Capital scope only, same scope as the reconstruction — excludes the untouched Working Capital Reserve):

| Scenario | Total | Relationship to the reconstruction |
|---|---|---|
| **Minimum Viable Opening** | **A$243,912** | New — genuinely below the reconstruction's Scenario A (Lean), by A$39,210 (~13.9%) |
| **Expected Opening** | **A$450,494** | Maps to the reconstruction's Scenario B (Expected/Realistic), with one disclosed correction (see §0) |
| **Full Build** | **A$644,832** | Maps to the reconstruction's Scenario C (Higher-Cost), unchanged |

The Minimum Viable Opening scenario achieves its reduction through two distinct, separately-disclosed levers: (1) **deferring** specific non-essential line items entirely (~A$14,000–20,000 worth, itemised in §5), and (2) **more aggressive but still fully compliant sourcing assumptions** on several fit-out trades, beyond the reconstruction's own Scenario A low-end pricing (~A$24,000 reduction in the fit-out category alone, §3.1). Both are disclosed separately below, never blended into an unexplained number.

---

## §0. One Disclosed Correction to the Prior Reconstruction

While reviewing whether pre-opening staffing costs were "actually required" (per this phase's own brief), a genuine inconsistency was found in `startup-cost-reconstruction.md`'s Category H: the treatment-staff trial/induction line modelled headcount as scaling 4→6→8 across Scenario A→B→C. This does not match the actual committed financial model, which fixes treatment-staff headcount at **8** (4 Massage+Beauty, 2 Nails, 2 Hair) identically for both Table 1 and Table 2 — headcount is not a startup-budget-scenario variable, it is a financial-model given. Reducing headcount would be an actual change to the financial model, explicitly out of scope this phase.

**Correction applied in this document only** (the reconstruction document itself is not edited retroactively, per this repo's disclose-don't-silently-fix convention): treatment-staff trial/induction now uses 8 staff in all three tiers (MVP, Expected, Full Build), with only the *training duration* varying. This raises the reconstruction's Scenario B (Expected) total by A$2,610 (Category H: A$32,373 → A$34,983) and its downstream contingency by A$391, moving the Expected total from A$447,493 to **A$450,494**. Scenario C (Full Build) was already correctly using 8 staff and is unchanged at A$644,832.

---

## §1. Item-by-Item Timing Reclassification

**Timing legend:** **A** = Mandatory before first revenue (legally required, compliance-required, or operationally impossible without it) | **B** = Required within first 3–6 months (useful, not day-one) | **C** = Optional/growth (deferrable until revenue exists).

### Category A — Premises Acquisition

| Item | Timing | Confidence | Rationale | Source |
|---|---|---|---|---|
| Lease bond | A | HIGH | Cannot sign a commercial lease without it | Reconstruction §A |
| Advance rent | A | HIGH | Cannot occupy the venue without it | Reconstruction §A |
| Legal fees (lease review + entity paperwork) | A | HIGH | `grace-startup-plan.md`'s own FINANCIAL GATES table treats this as a Week 1 blocking item | Reconstruction §A |
| Tenant-side agent/application fees | C | LOW | Genuinely optional — WA market convention is landlord pays agent commission | Reconstruction §A |

### Category B — Design and Approvals

| Item | Timing | Confidence | Rationale | Source |
|---|---|---|---|---|
| Architect/interior designer drawings | A | LOW | Required in principle before fit-out per `floor-plan-concept.md`'s own instruction; scope (not necessity) is reducible — see §3.1 | Reconstruction §B |
| WA Skin Penetration Code/NPAAC compliance consulting | A | LOW | Compliance is mandatory; the MVP satisfies it at A$0 via self-management using existing repo research (`standards-floorplan-crosscheck-2026-07-28.md`), not by lowering the standard | Reconstruction §B |
| Council planning-zone / building-permit fees | A | LOW | Cannot legally operate without confirmed use-class | Reconstruction §B |
| Food Business Notification (FSS cert) | A | HIGH | Legally required before serving any food/drink, per `financial-setup.md` STEP 9 | Reconstruction §B |
| WorkSafe WA nail LEV pre-application | A | LOW | Compliance-mandatory, nails are a day-one service | Reconstruction §B |
| WDP/pathology collection-room compliance review | A | HIGH | Cannot open the Blood Collection Room without it; already free, already in progress | Reconstruction §B |

### Category C — Fit-Out (see §3.1 for the full trade-level review)

| Item | Timing | Confidence | Rationale | Source |
|---|---|---|---|---|
| Demolition/strip-out | A | MEDIUM | Unavoidable for any fit-out | Reconstruction §C |
| Walls/partitions (Blood Collection Room only) | A | MEDIUM | Already at design-minimum — only the one clinically-necessary enclosed room | Reconstruction §C |
| Doors | A | MEDIUM | Collection room door + entry, both required | Reconstruction §C |
| Electrical (base) | A | MEDIUM | Core power/data/lighting circuits required to operate | Reconstruction §C |
| Electrical (premium/decorative circuits, e.g. dimmer zones) | B | MEDIUM | Nice-to-have ambiance beyond functional lighting | This document, §3.1 |
| Plumbing (Code-required wet areas) | A | MEDIUM | Already at the design-established minimum (2 sinks Nail/Facial-Beauty, 1 Massage, no further reducible) | Reconstruction §C |
| Lighting (clinical/task) | A | MEDIUM | Required to see/work safely, Ra>90 clinical requirement in Collection Room | Reconstruction §C |
| Lighting (ambiance/decorative, e.g. warm dimmable Lounge feature lighting) | B | MEDIUM | Genuine experience upgrade, not required to open | This document, §3.1 |
| Flooring (standard commercial-grade) | A | MEDIUM | Required, Code-mandated impervious surface in wet zones | Reconstruction §C |
| Flooring (premium finish upgrade) | C | MEDIUM | Aesthetic upgrade over standard-grade | This document, §3.1 |
| Painting (basic finish) | A | MEDIUM | Walls must be finished before opening | Reconstruction §C |
| Painting (feature walls/premium finish) | C | MEDIUM | Aesthetic upgrade | This document, §3.1 |
| Cabinetry/joinery (functional storage, reception counter) | A | MEDIUM | Secure consumable/sharps storage is a compliance-adjacent need (NPAAC C1.1(iv)); reception counter is operationally required | Reconstruction §C |
| Cabinetry/joinery (custom/premium finish beyond functional storage) | C | MEDIUM | Standard flat-pack storage is functionally equivalent | This document, §3.1 |
| Privacy curtain systems | A | HIGH | The privacy mechanism itself for Massage/Facial-Beauty — non-negotiable given the open-plan design, already the cost-saving option vs. walls | Reconstruction §C |
| HVAC (basic split system) | A | MEDIUM | Climate control required for a 2+ hour client wait | Reconstruction §C |
| HVAC (fully zoned premium system) | B | MEDIUM | A basic system is compliant and sufficient at opening | This document, §3.1 |
| Reception build | A | MEDIUM | Required to check in/process clients | Reconstruction §C |
| Staff area fit-out | A | MEDIUM | WHS requires staff amenities (staff room, WC) | Reconstruction §C |
| Acoustic treatment for curtain bays | **B** | MEDIUM | Not a legal mandate confirmed anywhere in this repo — `floor-plan-concept.md` itself flags it as "not resolved," a real but non-blocking quality investment. **Flagged tension, not hidden:** this sits uneasily against this venture's own stated design principle ("pregnancy modesty is non-negotiable") — see §6 Risks | This document, §3.1 |

### Category D — Furniture, Fixtures and Fittings

| Item | Timing | Confidence | Rationale | Source |
|---|---|---|---|---|
| Lounge & common-area furniture (functional minimum) | A | HIGH | Clients need somewhere to sit for 2+ hours | Reconstruction §D |
| Lounge extras (extra side tables, decorative lamps) | C | LOW | Upgrade beyond functional seating | This document, §3.3 |
| Reception furniture | A | LOW | Operationally required | Reconstruction §D |
| Treatment beds/tables (2 massage + 2 facial/beauty) | A | HIGH | Cannot deliver these services without them; tied to committed room count, not station count — not reducible | Reconstruction §D |
| Styling/manicure/pedicure chairs — first 2 of each (matches solver-verified headcount) | A | HIGH | `equipment-costs.md`'s own finding: only 2 Nails/2 Hair staff are needed at committed volume | Reconstruction §D, §3.3 |
| Styling/manicure/pedicure chairs — additional 2 of each | **B** | HIGH | `equipment-costs.md`'s own words: "extra stations provide rostering flexibility... not a mandatory extra hire" — genuinely deferrable, already disclosed in this repo | This document, §3.3 |
| Staff room furniture | A | LOW | WHS-adjacent requirement | Reconstruction §D |
| Signage (basic, compliant) | A | HIGH | Needed to be found; typically a lease condition | Reconstruction §D |
| Signage (premium/oversized upgrade) | C | LOW | Beyond functional wayfinding/shopfront presence | This document, §3.3 |
| Decorations/branding elements | **C** | LOW | Already flagged in the reconstruction as addable post-opening | Reconstruction §D |
| Storage hamper | A | HIGH | Functional necessity | Reconstruction §D |

### Category E — Medical and Operational Equipment

| Item | Timing | Confidence | Rationale | Source |
|---|---|---|---|---|
| Pathology/phlebotomy equipment (full) | A | HIGH | **Protected — no reduction.** WDP requirement, clinical safety-critical | Reconstruction §E |
| Nail LEV unit | A | HIGH | Compliance-mandatory; sized for eventual capacity, not staged (see §3.2 risk) | Reconstruction §E |
| Nail portable equipment — 2 stations | A | HIGH | Matches solver-verified 2-technician headcount | Reconstruction §E, §3.2 |
| Nail portable equipment — additional 2 stations | **B** | HIGH | Deferrable — same rostering-flexibility rationale as Category D | This document, §3.2 |
| Hair backwash basin+chair hardware (2 units, already minimum) | A | HIGH | Already at design-minimum, not further reducible | Reconstruction §E |
| Hair portable equipment — 2 chairs | A | HIGH | Matches solver-verified 2-technician headcount | Reconstruction §E, §3.2 |
| Hair portable equipment — additional 2 chairs | **B** | HIGH | Deferrable, same rationale | This document, §3.2 |
| Beauty/brows equipment | A | HIGH | Only 2 rooms exist; no further staging possible without cutting a committed room | Reconstruction §E |
| Massage-room equipment | A | HIGH | Required for service delivery | Reconstruction §E |
| Technology — core (2 iPads, POS, B&W printer, router, computer) | A | HIGH | Core operational technology | Reconstruction §E, §3.2 |
| Technology — 3rd iPad + colour inkjet printer | **B** | HIGH | Explicitly flagged "premium birth plan prints" in the source — a genuine upgrade, not core | This document, §3.2 |
| Emergency/safety equipment (full) | A | HIGH | **Protected — no reduction.** AED, first aid, panic buttons are safety-critical | Reconstruction §E |
| General cleaning equipment | A | LOW | Required for basic hygiene operations | Reconstruction §E |

### Category F — Opening Inventory and Consumables

| Item | Timing | Confidence | Rationale | Source |
|---|---|---|---|---|
| Pathology consumables | A | HIGH | **Protected — full stock, no reduction.** Patient-safety-adjacent | Reconstruction §F |
| All other opening consumables (gel polish, hair/facial products, lounge snacks, printed forms, cleaning supplies) — reduced initial order | A | MEDIUM | A smaller opening order, restocked from early revenue, is still a genuine day-one requirement — quantity reduced, not the requirement itself | This document, §3.2 |

### Category G — Technology and Systems

| Item | Timing | Confidence | Rationale | Source |
|---|---|---|---|---|
| Basic web presence (waitlist/landing page) | A | LOW | Some web presence is needed for the referral/booking funnel | This document, §3.4 |
| Full professional website build | **B** | LOW | A venture opening primarily via referral partnerships (not organic search) can defer the full build | This document, §3.4 |
| Domain registration | A | LOW | Cheap, needed for basic web presence/email | Reconstruction §G |
| IT setup/installation | A | LOW | Network needed for booking/payments from Day 1 | Reconstruction §G |
| Booking system (Fresha) configuration | A | HIGH | No setup fee; needed before opening | Reconstruction §G |
| Xero configuration | A | HIGH | Bundled with the mandatory accountant engagement | Reconstruction §G |

### Category H — Staffing Before Opening

| Item | Timing | Confidence | Rationale | Source |
|---|---|---|---|---|
| Recruitment — Venue Manager, Phlebotomist, Receptionist (paid ads) | A | LOW | Higher-stakes/credentialed roles, paid channels retained | This document, §3.5 |
| Recruitment — Massage, Nails, Beauty/Brows (organic/referral-network channels) | A | LOW | `reed-partnerships.md`'s own named professional-network channels can substitute for paid ads — genuine risk if organic sourcing underperforms, see §6 | This document, §3.5 |
| Venue Manager pre-opening salary | A | HIGH (rate) / MEDIUM (duration) | **Protected role** — `hr-framework.md`'s own words: "the venue cannot safely open without it." Duration compressed (8wk→6wk) by overlapping early admin with Anthony directly, not by removing the role | Reconstruction §H, this document §3.5 |
| Phlebotomist credentialing (1 week) | A | HIGH (rate) / LOW (duration) | **Not further reducible** — WDP credentialing requirement, patient-safety-adjacent, held at Scenario A's original duration | Reconstruction §H |
| Receptionist training | A | HIGH (rate) / MEDIUM (duration) | Compressed from `staff-plan.md`'s own explicit "3 weeks" to 1.5 weeks for MVP — **a real, flagged deviation from the source document's own stated requirement**, see §6 Risks | Reconstruction §H, this document §3.5 |
| Treatment staff trial/induction (8 staff, compressed duration) | A | HIGH (rate) / MEDIUM (duration) | Full committed headcount trained in all scenarios (§0 correction); MVP compresses duration to 4 days — a real risk against the tightly-choreographed 25-min AM cadence, see §6 | This document, §0 and §3.5 |
| First Aid / Fire Warden course | A | HIGH | **Protected — no reduction.** Legally required per `emergency-plan.md` | Reconstruction §H |

### Category I — Marketing and Launch

| Item | Timing | Confidence | Rationale | Source |
|---|---|---|---|---|
| Professional photography | **B** | LOW | Deferred to post-opening — smartphone/organic content sufficient for launch, per this phase's explicit "what can be organic instead of paid" instruction | This document, §3.6 |
| Paid pre-launch marketing push | **C** | LOW | Near-eliminated for MVP — relies on the already-named, real referral-practice list (`poppy-marketing.md`, `referral-partnership-plan.md`), a A$0 channel | This document, §3.6 |
| Basic promotional materials for referral outreach | A | LOW | Something is needed to hand OB/midwife practices during outreach conversations — minimised, not eliminated | This document, §3.6 |

### Category J — Professional Services

| Item | Timing | Confidence | Rationale | Source |
|---|---|---|---|---|
| Accountant engagement | A | HIGH | **Protected.** `financial-setup.md` STEP 1 is explicitly BLOCKING | Reconstruction §J |
| ASIC registration | A | HIGH | Fixed government fee, legally required | Reconstruction §J |
| Solicitor (lease review) | A | HIGH | Bundled with Category A legal fees, mandatory | Reconstruction §J |
| Insurance brokerage setup | A | HIGH | **Protected.** Quotes are free; the premium itself remains an operating cost, untouched | Reconstruction §J |
| Compliance consulting | A | LOW | Bundled with Category B, mandatory but achievable at A$0 via self-management | Reconstruction §J |

---

## §2. Three Scenario Totals

| Category | Minimum Viable Opening | Expected Opening | Full Build |
|---|---|---|---|
| A. Premises acquisition | A$19,000 | A$28,500 | A$47,500 |
| B. Design and approvals | A$4,100 | A$11,650 | A$20,700 |
| C. Fit-out | A$138,328 | A$234,241 | A$306,029 |
| D. Furniture, fixtures and fittings | A$14,160 | A$35,530 | A$51,800 |
| E. Medical and operational equipment | A$19,280 | A$33,900 | A$45,220 |
| F. Opening inventory and consumables | A$2,585 | A$4,706 | A$6,030 |
| G. Technology and systems | A$820 | A$3,935 | A$7,550 |
| H. Staffing before opening | A$18,717 | A$34,983 (corrected, §0) | A$45,492 |
| I. Marketing and launch | A$250 | A$3,250 | A$5,500 |
| J. Professional services | A$539 | A$1,039 | A$1,539 |
| **Subtotal (A–J)** | **A$217,779** | **A$391,734** | **A$537,360** |
| K. Contingency | A$26,133 (12%) | A$58,760 (15%) | A$107,472 (20%) |
| **TOTAL** | **A$243,912** | **A$450,494** | **A$644,832** |

**Contingency rationale for MVP (12%, above the reconstruction's original 10% for Scenario A):** the MVP scenario has less discretionary buffer remaining to absorb surprises, having already deferred or minimised most non-essential spend — a construction cost overrun represents a larger percentage hit on a smaller, leaner base. A slightly higher contingency percentage protects against this, rather than compounding the risk of an under-buffered lean budget.

**Difference between the three scenarios, explained:**
- **Minimum Viable Opening (A$243,912)** achieves compliance and safe operation at the lowest defensible cost — every mandatory/compliance item is fully funded; every deferrable item is deferred, not cut.
- **Expected Opening (A$450,494)** is the realistic mid-point — matches this venture's own existing bottom-up figures (`equipment-costs.md`, `floor-plan-concept.md`) most closely, with all items funded at typical market rates and no deferrals.
- **Full Build (A$644,832)** funds every item at the high end of sourced ranges with generous specification and a 20% contingency — the most conservative, best-buffered scenario.

---

## §3. Specific Area Reviews

### §3.1 Fit-Out

**Challenged directly, per instruction:** internal walls, joinery, decorative finishes, non-essential construction.

- **Internal walls:** already minimised by the venue's own current design (only the Blood Collection Room is fully walled) — no further reduction possible without either (a) removing a required clinical enclosure, which is not on the table, or (b) converting the Blood Collection Room itself to a curtain bay, which would breach the WA Skin Penetration Code's privacy/acoustics requirements for venepuncture. **No further reduction recommended here.**
- **Joinery/cabinetry:** the reconstruction's 10% trade allocation includes both functionally-required storage (secure consumable/sharps cabinets, per NPAAC C1.1(iv)) and discretionary finish quality. MVP retains full functional storage but assumes standard flat-pack/off-the-shelf units instead of custom joinery — a genuine ~35% reduction on this trade, with no loss of required storage capacity.
- **Decorative finishes:** premium flooring, feature paint walls, and ambiance/decorative lighting circuits are all deferred or reduced in MVP — standard commercial-grade finishes satisfy every compliance requirement identically to premium finishes.
- **Acoustic treatment for the curtain-partitioned Massage/Facial-Beauty bays** is the one genuinely finely-balanced call in this category: it is not a confirmed legal requirement anywhere in this repo, but `floor-plan-concept.md` itself already flags the curtain-partition sound-insulation trade-off as a real, unresolved concern, and this venture's own design principles state "pregnancy modesty is non-negotiable." MVP defers this to the first 3–6 months rather than cutting it entirely — see §6 Risks for the honest framing of this trade-off.
- **What can be delayed:** the additional HVAC zoning beyond a basic split system, and the acoustic treatment above, are the two fit-out items genuinely deferrable to post-opening without touching compliance.

### §3.2 Equipment

- **Absolutely required day-one:** all pathology/phlebotomy equipment (full, protected), all emergency/safety equipment (full, protected), the nail LEV system (compliance-mandatory, not stageable — see below), 2 nail stations' and 2 hair chairs' worth of portable equipment (matches the solver-verified 2-technician headcount at committed volume), all beauty/brows and massage equipment (tied to committed rooms, not stations).
- **Can be staged/purchased later:** the additional 2 nail stations' and 2 hair chairs' worth of *portable* equipment (tables, lamps, dryers, straighteners, trolleys) — `equipment-costs.md`'s own words describe these extra stations as providing "rostering flexibility... not a mandatory extra hire." The extra iPad and colour inkjet printer (explicitly "premium birth plan prints" in the source) are also stageable.
- **Genuinely not stageable, flagged honestly:** the nail LEV extraction system itself. Shared extraction systems are typically sized and installed once, during the fit-out pass — retrofitting a system later to cover 2 additional stations would likely cost more than installing full-capacity capability now. MVP retains full LEV capacity even though only 2 stations open day-one, at genuine extra cost relative to a "true minimum," because deferring it creates a larger future cost, not a smaller one — a disclosed judgment call, not an oversight.
- **Can lease vs. purchase:** no leasing option is sourced anywhere in this repository for any equipment category (the AED note in `equipment-costs.md` §11 does mention "some AEDs come with leasing options at A$40–60/month" as the one exception found). This is a genuine gap — leasing was not modelled further, flagged as UNKNOWN rather than assumed unavailable.

### §3.3 Furniture

- **Operational requirement vs. aesthetic upgrade, separated explicitly:** functional seating for the Lounge (clients need somewhere to sit for 2+ hours) is protected in full; extra side tables and decorative floor lamps are an aesthetic upgrade, deferred. Treatment beds/tables are tied to committed rooms (not reducible). The additional 2 nail/2 hair chairs (beyond the solver-verified 2-headcount minimum) are the single largest furniture-category deferral opportunity, matching the same repo-disclosed rostering-flexibility framing as the equipment side.
- **Decorations/branding elements** are wholly aesthetic and deferred entirely (already flagged as addable post-opening in the reconstruction).
- **Signage** is split: basic, compliant, functional signage is retained in full; any premium/oversized upgrade is deferred.

### §3.4 Technology and Systems

- A basic waitlist/landing page substitutes for a full professional website build at opening — this venture's primary client-acquisition channel is referral partnerships (named midwifery/OB practices, per `referral-partnership-plan.md`), not organic web search, making a full website build a genuinely deferrable investment rather than a day-one necessity.
- Core booking/payment/network infrastructure (Fresha, domain, basic IT setup) is retained in full — none of this is discretionary.

### §3.5 Staffing Before Opening

Reviewed directly against this phase's own question: **are all pre-opening wages actually required, and can recruitment/training overlap with the opening timeline?**

- **Venue Manager:** the role itself is protected (critical-path, cannot open without it, per `hr-framework.md`'s own words). The *duration* of pre-opening salary is compressed from 8 to 6 weeks by overlapping the earliest administrative work (accountant briefing, entity setup) directly with Anthony, deferring Venue Manager onboarding until there is genuine on-site fit-out/operational work for the role to do. This is a scheduling optimisation, not a role reduction.
- **Phlebotomist credentialing:** held at its original 1-week estimate — this is patient-safety-adjacent (WDP credentialing) and was not further compressed, a deliberate choice not to cut into this specific timeline.
- **Receptionist training:** compressed from `staff-plan.md`'s own explicitly stated "3 weeks" to 1.5 weeks. **This is a real, flagged deviation from an existing repo document's own stated requirement** — not a silent override. See §6 Risks.
- **Treatment staff trial/induction:** the full 8-person committed headcount is trained in every scenario (§0 correction) — headcount is never reduced. Only the trial *duration* is compressed (from 1 week to 4 days for MVP), a real risk against the tightly-choreographed 25-minute AM cadence this venture's entire capacity model depends on.
- **Recruitment channel mix:** MVP shifts 3 of 5 roles (Massage, Nails, Beauty/Brows) to organic/referral-network sourcing (already-named professional channels in `reed-partnerships.md`), retaining paid advertising only for the 3 higher-stakes/credentialed roles (Venue Manager, Phlebotomist, Receptionist).

### §3.6 Marketing

**Minimum viable launch spend determined:** near-zero. This venture already has a real, named, unpaid channel — direct outreach to the specific midwifery/OB/GYN practices and public-sector maternal-child-health contacts listed in `poppy-marketing.md` and `referral-partnership-plan.md` — that costs nothing beyond basic printed materials for those conversations. Professional photography and any paid pre-launch advertising push are deferred to the first 3–6 months, once early revenue and real client photos/testimonials exist to make paid content more effective. **This directly compounds an already-disclosed uncertainty** (see §6): no conversion-rate evidence exists anywhere in this repo for the referral channel, so an MVP launch with near-zero paid marketing has less of a fallback lever if referral conversion underperforms.

---

## §4. Reconciliation Against the Funding Requirement — Not Replaced This Phase

The current bounded range (A$357,390–A$577,180, `docs/architecture/FUNDING-REQUIREMENT-INVESTIGATION.md`) combines Pre-Opening Capital (A$272,390–467,180) with the separate, **untouched** Working Capital Reserve (A$85,000–110,000). This phase's three totals (§2) are Pre-Opening-Capital-scoped only, directly comparable to the A$272,390–467,180 figure, not the full combined range, unless the untouched Working Capital Reserve is added back for an all-in comparison.

**Potential revised range, if this analysis were adopted (informational only — not a construct this phase authorises):**

| | Pre-Opening Capital only | + untouched Working Capital Reserve (A$85,000–110,000) |
|---|---|---|
| Minimum Viable Opening | A$243,912 | A$328,912 – A$353,912 |
| Expected Opening | A$450,494 | A$535,494 – A$560,494 |
| Full Build | A$644,832 | A$729,832 – A$754,832 |

**What changed:** if Minimum Viable Opening were adopted as the new low-end planning basis, the funding requirement's low end could reasonably move from A$357,390 toward approximately **A$328,912** — a reduction of **A$28,478 (~8%)**. This is a real, evidence-based potential reduction, achieved entirely through the deferrals and lean-but-compliant sourcing decisions itemised in §1 and §5, without touching any compliance or safety requirement.

**What assumptions drove the reduction:** (1) deferring the additional 2 nail/2 hair stations' furniture and portable equipment, acoustic treatment, full website build, professional photography, and most paid marketing (§5); (2) more aggressive but still compliant sourcing on several fit-out trades (standard vs. premium finishes, basic vs. fully-zoned HVAC); (3) a compressed but not eliminated pre-opening staffing timeline.

**What still requires confirmation before this could replace the canonical figure:**
1. **Anthony's own review and risk-acceptance of every deferred/compressed item** — this document is explicitly submitted for that review, not a decision already made.
2. **Real builder quotes** to confirm the fit-out trade-percentage reductions are achievable against an actual venue (same conclusion `STARTUP-COST-RECONCILIATION.md` §4 already reached — unchanged by this phase).
3. **Confirmation that 2-station (not 4-station) nail/hair equipment is genuinely operationally sufficient** at committed volume, or that the "rostering flexibility" value of the extra 2 stations is not more load-bearing than the pure headcount-solver finding suggests — see new tracker item 48.
4. **Confirmation the compressed Venue Manager/Receptionist/treatment-staff training timelines are operationally safe** — genuinely unverified, flagged not assumed.
5. **Formal wiring into `data/canonical/startup_costs.yml`** — explicitly not done this phase.

---

## §5. Deferred Expenditure Schedule

Items deferred to **B (required within first 3–6 months)**, funded from early operating revenue rather than startup capital, in the Minimum Viable Opening scenario:

| Item | Estimated cost | Funded from |
|---|---|---|
| Additional 2 nail stations (furniture + portable equipment) | ~A$3,000 | Early operating revenue |
| Additional 2 hair chairs (furniture + portable equipment) | ~A$2,600 | Early operating revenue |
| Acoustic treatment for curtain bays | ~A$4,874 | Early operating revenue |
| Full professional website build (upgrade from basic landing page) | ~A$1,200 | Early operating revenue |
| Professional photography | ~A$1,000 | Early operating revenue |
| 3rd iPad + colour inkjet printer | ~A$700 | Early operating revenue |
| Electrical/lighting/HVAC premium upgrades (if desired post-opening) | Variable, not quantified | Early operating revenue |
| **Approximate total, B-tier** | **~A$13,000–14,000** | |

Items deferred to **C (optional/growth, indefinite)**:

- Decorations/branding elements (A$500–2,000)
- Any premium/decorative fit-out finish beyond MVP baseline (flooring, feature paint, custom joinery)
- Tenant-side agent/application fees
- Phase 2 equipment (spray tan booth, hire fleet, China-sourced stock) — already excluded from every scenario, unchanged from the reconstruction phase

---

## §6. Risks Introduced by Cost Reduction — Honest Assessment

Deferring or reducing spend is never risk-free. Each risk below is a genuine, disclosed trade-off, not glossed over:

1. **Staged equipment (2 of 4 nail/hair stations deferred).** If demand ramps faster than expected, or if peak-day bookings cluster in ways that strain the reduced station count even at fixed committed headcount, the venue loses the rostering flexibility `equipment-costs.md` itself describes these extra stations as providing. This is a real scheduling-friction risk in the early months, most acute if referral-driven demand is lumpier than the smooth ramp curve assumes.
2. **Compressed Venue Manager pre-opening period (6 weeks vs. 8).** Less buffer for unexpected fit-out delays, less time to fully embed WHS/HR systems before the first hire, more schedule risk if anything slips.
3. **Compressed Receptionist training (1.5 weeks vs. `staff-plan.md`'s own explicit "3 weeks").** A real, flagged deviation from an existing source document's own stated requirement — genuine risk of front-of-house errors (booking mistakes, payment processing issues) in the earliest operating days.
4. **Compressed treatment-staff trial (4 days vs. 1–2 weeks).** Less rehearsal time for the synchronised AM scheduling model (25-minute cadence) this venture's entire capacity model depends on — a real risk given how tightly choreographed the Table 1/Table 2 schedules already are.
5. **Deferred acoustic treatment.** `floor-plan-concept.md` already discloses the curtain-partition sound-insulation trade-off as "genuinely weakened... not resolved." Deferring the fix further compounds an already-disclosed risk, and sits in real tension with this venture's own stated design principle that "pregnancy modesty is non-negotiable" — flagged prominently, not treated as a purely cosmetic deferral.
6. **Reduced recruitment spend (organic/referral channels for 3 of 5 roles).** A real risk of slower time-to-hire if organic channels underperform, potentially forcing a late, more expensive pivot back to paid advertising anyway — a possible false economy.
7. **Near-zero launch marketing, referral-dependent.** No conversion-rate evidence exists anywhere in this repository for the referral channel (`docs/architecture/COMMERCIAL-VALIDATION-FRAMEWORK.md`'s own Revenue Ramp Evidence Framework already flags this gap). An MVP launch with minimal paid marketing has less of a fallback lever if referral conversion underperforms than a scenario with real ad spend budgeted from Day 1.
8. **Smaller opening consumables order.** If a supplier's lead time is longer than expected, a smaller initial buffer increases stock-out risk in the first weeks — bounded (pathology consumables are explicitly protected, not reduced), but real for non-clinical consumables.
9. **Reduced design/architect scope.** A lighter-touch design brief could miss coordination issues (e.g., the already-flagged LEV-vs-open-plan tension in `floor-plan-concept.md`) that a fuller architect engagement might catch before construction begins — a real quality-of-outcome risk traded against upfront cost.

---

## §7. Unresolved Assumptions

- Whether 2-station nail/hair equipment genuinely suffices operationally at committed volume, or whether the "rostering flexibility" the extra 2 stations provide is more load-bearing than the pure headcount-solver finding suggests.
- Whether organic/referral-based recruitment can realistically fill 3 of 5 roles within the required timeline without falling back to paid advertising anyway.
- Whether the compressed Venue Manager/Receptionist/treatment-staff training windows are operationally safe — genuinely unverified, flagged not assumed.
- The fit-out trade cost reductions (electrical/lighting/flooring/cabinetry/HVAC) remain MEDIUM/LOW confidence estimates, unconfirmed against real quotes — same conclusion as the reconstruction phase, unchanged.
- This document has not been reviewed or approved by Anthony — it is submitted for that review, not a decision already made.

---

## Tracker Update

One new item added, per this phase's own genuinely new evidence gap (not noise) — continuing the sequential numbering from item 47:

**Item 48 (new) — MVP Opening Scenario: deferred/reduced items requiring founder risk-acceptance before adoption.** Who can confirm: Anthony (risk-acceptance decision) / Venue Manager, once hired (operational validation). Status: OPEN. Detail: `docs/architecture/STARTUP-COST-OPTIMISATION.md` proposes deferring 2 of 4 nail/hair stations' equipment and furniture (rostering-flexibility trade-off), compressing Venue Manager pre-opening salary from 8 to 6 weeks, compressing Receptionist training from `staff-plan.md`'s own explicit "3 weeks" to 1.5 weeks, compressing treatment-staff trial from 1-2 weeks to 4 days, deferring acoustic treatment for curtain-partitioned rooms, and shifting 3 of 5 recruitment channels to organic/referral sourcing. None of these touch compliance or safety requirements, all are explicitly disclosed trade-offs (§6 Risks) — but none has been confirmed operationally safe or accepted as a real risk by Anthony. Required action: Anthony's explicit review and risk-acceptance (or rejection) of each deferred/compressed item before the Minimum Viable Opening scenario could be adopted as a planning basis. Impact if unconfirmed: the A$243,912 Minimum Viable Opening figure and the associated ~A$28,478 potential funding-requirement reduction (§4) remain a proposal, not a confirmed basis for any real funding conversation.

---

## Validation — Confirmed No Model Changes Occurred

- `git status --short` before this phase: clean.
- File created this phase: `docs/architecture/STARTUP-COST-OPTIMISATION.md`. `docs/VERIFICATION-TRACKER.md` updated with one new item (48).
- Full pytest suite: **114 passed**, 0 failed.
- `tools/validate_canonical_data.py`: **13 files checked, 0 errors, 27 warnings** — identical to every prior phase.
- `tools/check_consistency.py`: **0 findings** — identical to every prior phase.
- `git diff --stat` against `data/canonical/`, `data/models/`, and `tools/*.py`: zero changes.
- `data/canonical/startup_costs.yml` was **not modified**. The financial model and funding requirement calculation were **not touched**.

## Recommended Next Step

Anthony reviews §1 (item-by-item classification), §5 (deferred schedule), and §6 (risks) directly, and makes an explicit risk-acceptance decision on each deferred/compressed item flagged in the new tracker item 48. Only after that review would wiring any part of this analysis into `data/canonical/startup_costs.yml` become an appropriately-authorised next phase — not attempted here.
