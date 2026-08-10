# Startup Cost Reconstruction — Bottom-Up, First-Principles Rebuild

**Phase:** Startup Cost Reconstruction — documentation only. This document builds a new, itemised, bottom-up startup-capital budget from first principles. It does **not** start from the existing A$357,390–A$577,180 bounded range or any of the 6–9 historical ranges (`docs/architecture/STARTUP-COST-RECONCILIATION.md`) — those are used only as comparison references in §4, at the end. It does **not** modify `data/canonical/startup_costs.yml`, the revenue model, the cost model, the Master Financial Model, or any canonical operating assumption. Wiring this reconstruction into the canonical layer (formally replacing `startup_costs.yml`) is explicitly a separate, future, not-yet-authorised phase.

**Date:** 2026-08-10
**Version used as source of truth:** commit `cc492ad` (Venue Acquisition & Commercial Due Diligence) and everything it built on.

---

## Design Context — What This Reconstruction Models

This reconstruction models GTT Center Perth's **current** intended design, confirmed 2026-07-31 (`docs/floor-plan-concept.md`): a predominantly **open-plan** centre, not a traditional fully-partitioned medical fit-out.

- **Only the Blood Collection Room is fully enclosed** with solid walls and a locking door — the one genuinely clinical/privacy-critical space (venepuncture).
- **GTT Lounge, Hairdressing Area, and Nail Station Area are open plan** — no internal walls between them.
- **Massage Rooms and Facial/Beauty Rooms use partition-curtain bays**, not stud-wall-and-door construction — full-length, opaque, lockable-track privacy curtains as the privacy mechanism.
- Day-one footprint: **~239sqm** (the figure the fit-out cost estimate below is built against). A separate, larger **~262sqm** figure exists in `floor-plan-concept.md` for day-one + un-costed growth-reservation space (extra massage/beauty capacity, space-only, not staffed or budgeted here) — not used in this reconstruction, since growth reservations are explicitly not part of the day-one committed budget.

This open-plan design **meaningfully reduces** the walls/partitions/doors trade cost relative to a traditional enclosed-room medical fit-out (reflected explicitly in §C.1 below), at the cost of a real, disclosed trade-off in acoustic privacy for the curtain-partitioned rooms (also priced explicitly, not hidden).

---

## Methodology

- **Confidence levels**, applied per item:
  - **HIGH** — directly sourced from an existing, itemised figure already in this repository.
  - **MEDIUM** — derived from an existing sourced figure using a disclosed reallocation or percentage-split methodology (e.g. decomposing a single construction total into trades).
  - **LOW** — a new estimate using general Australian market knowledge (job-board pricing, typical service-industry rates), not a GTT-specific quote and not previously stated anywhere in this repository. Flagged explicitly, never presented as more certain than it is.
- **Three scenarios**, none selected as preferred:
  - **Scenario A (Lean/open-plan implementation)** — the low end of sourced ranges, a compressed pre-opening timeline, minimal discretionary spend.
  - **Scenario B (Expected/realistic implementation)** — the mid-point of sourced ranges, matching this repo's own existing bottom-up figures (`floor-plan-concept.md`, `equipment-costs.md`) most closely.
  - **Scenario C (Higher-cost implementation)** — the high end of sourced ranges, a longer pre-opening timeline, more conservative contingency.
- Every item states: description, category, cost (A/B/C), confidence, source/evidence, required-before-opening, required-day-one, optional.
- **No cost is invented without a source or an explicitly disclosed general-market basis.** Where a genuinely unknown item exists, it is flagged UNKNOWN rather than estimated with false confidence.

---

## A. Premises Acquisition

| Item | Scenario A | Scenario B | Scenario C | Confidence | Source/Evidence | Before Opening | Day-One | Optional |
|---|---|---|---|---|---|---|---|---|
| Lease bond (1/2/3 months' rent, at the established A$8,000/month planning rent) | A$8,000 | A$16,000 | A$24,000 | HIGH (rent figure) / MEDIUM (months multiplier) | `docs/rent-budget-2026-07-28.md` (A$8,000/month); months-multiplier per `docs/CURRENT-STATE.md` §7.3's own "~2 months' rent" convention, varied across scenarios | Yes | Yes | No |
| Advance rent (first month, paid at signing) | A$8,000 | A$8,000 | A$16,000 (2 months upfront, conservative landlord) | HIGH | `docs/rent-budget-2026-07-28.md` | Yes | Yes | No |
| Legal fees (lease review + entity paperwork, bundled) | A$3,000 | A$4,500 | A$6,000 | HIGH | `docs/grace-startup-plan.md` FINANCIAL GATES table ("Legal and professional fees, A$3,000–6,000") | Yes | Yes | No |
| Tenant-side agent/application fees | A$0 | A$0 | A$1,500 | LOW | WA commercial-market convention: landlord typically pays agent commission, not tenant — Scenario C allows for an optional buyer's-agent engagement | Yes | No | Yes (Scenario C only) |
| **Category A subtotal** | **A$19,000** | **A$28,500** | **A$47,500** | | | | | |

---

## B. Design and Approvals

| Item | Scenario A | Scenario B | Scenario C | Confidence | Source/Evidence | Before Opening | Day-One | Optional |
|---|---|---|---|---|---|---|---|---|
| Architect/interior designer concept + construction drawings | A$5,000 | A$9,000 | A$15,000 | LOW | `docs/floor-plan-concept.md`'s own instruction that a professional architect is needed once a venue is confirmed — no fee stated in this repo; general AU commercial fit-out design-fee benchmark used, disclosed | Yes | Yes | No |
| WA Skin Penetration Code / NPAAC compliance consulting | A$0 (self-managed, existing research) | A$1,500 | A$3,000 | LOW | No repo figure — general estimate for an external compliance consultant, if engaged | Yes | Yes | Yes (self-managed is viable per Scenario A, given `docs/standards-floorplan-crosscheck-2026-07-28.md`'s existing research) |
| Council planning-zone / building-permit application fees | A$500 | A$1,000 | A$2,000 | LOW | `docs/location-scouting.md`'s requirement to confirm planning zone before committing — no specific WA council fee sourced in this repo | Yes | Yes | No |
| Food Business Notification — Food Safety Supervisor certificate | A$100 | A$150 | A$200 | HIGH | `docs/financial-setup.md` STEP 9 ("~4 hours, A$100–200") | Yes | Yes | No |
| WorkSafe WA nail LEV pre-application | A$0 | A$0 | A$500 | LOW | `docs/floor-plan-concept.md`'s Critical Design Requirements ("pre-application to WorkSafe WA must be submitted") — typically free/nominal; Scenario C allows for a possible assessment fee | Yes | Yes | No |
| WDP/pathology collection-room compliance review | A$0 | A$0 | A$0 | HIGH | `docs/wdp-reply-carole-2026-07-30.md` — WDP's own review process, already engaged via Carole Rivers, no GTT-side fee identified anywhere in the correspondence | Yes | Yes | No |
| **Category B subtotal** | **A$5,600** | **A$11,650** | **A$20,700** | | | | | |

---

## C. Fit-Out — Trade-by-Trade Breakdown

The **total** construction envelope (A$162,452 / A$234,241 / A$306,029) is anchored to `docs/floor-plan-concept.md`'s own already-computed, itemised bottom-up build for the 239sqm open-plan/curtain design — not re-invented. That document derives the total via (base shell rate × 239sqm) minus a confirmed A$10,736–17,256 wall-to-curtain/open-plan saving. **This reconstruction decomposes that same total into individual trades**, using standard Australian commercial fit-out percentage splits (a general industry rule-of-thumb, disclosed as MEDIUM confidence, not a fresh independent total) — directly reflecting the open-plan-with-enclosed-phlebotomy-rooms design in the trade weighting itself (walls/partitions weighted low; an explicit acoustic-treatment line prices the curtain-privacy trade-off `floor-plan-concept.md` itself flags as a real, unresolved cost).

| Trade | % of total | Scenario A | Scenario B | Scenario C | Confidence | Notes |
|---|---|---|---|---|---|---|
| Demolition / strip-out | 4% | A$6,498 | A$9,370 | A$12,241 | MEDIUM | Assumes a raw-shell or lightly-fitted tenancy; a former-tenancy strip-out could shift this, not modelled without a confirmed venue |
| Walls/partitions | 8% | A$12,996 | A$18,739 | A$24,482 | MEDIUM | Deliberately low — reflects only the Blood Collection Room needing solid walls, per the design context above |
| Doors | 2% | A$3,249 | A$4,685 | A$6,121 | MEDIUM | One solid clinical door (Blood Collection Room) + entry door |
| Electrical (power, data, lighting circuits) | 18% | A$29,241 | A$42,163 | A$55,085 | MEDIUM | Largest single trade — 4 nail stations at min. 2×10A GPOs each, technology points throughout |
| Plumbing (clinical sink, nail/facial/beauty wet areas, backwash, staff kitchenette, WCs) | 15% | A$24,368 | A$35,136 | A$45,904 | MEDIUM | Reflects the WA Skin Penetration Code's 2-sink requirement for Nail Station + Facial/Beauty rooms specifically (not Massage or Hairdressing — see design context) |
| Lighting fixtures | 8% | A$12,996 | A$18,739 | A$24,482 | MEDIUM | Clinical LED Ra>90 in Blood Collection Room; warm dimmable in Lounge; task lighting elsewhere |
| Flooring | 10% | A$16,245 | A$23,424 | A$30,603 | MEDIUM | Impervious vinyl/tile in Code-triggering wet zones; washable/soft finish in Lounge/Hairdressing |
| Painting / wall finishes | 5% | A$8,123 | A$11,712 | A$15,301 | MEDIUM | |
| Cabinetry / joinery (reception counter build, storage, staff lockers, nail dust cabinets) | 10% | A$16,245 | A$23,424 | A$30,603 | MEDIUM | |
| **Privacy curtain systems** (curtain track + medical-grade privacy curtain, 4 bays) | 1% | A$1,625 (within total) | A$2,342 (within total) | A$3,060 (within total) | HIGH-basis | Called out for visibility per the design context — already included within the total above (matches `floor-plan-concept.md`'s own A$600–1,400 4-bay itemisation), not additive on top |
| HVAC | 10% | A$16,245 | A$23,424 | A$30,603 | MEDIUM | Shared open-plan air handling, cheaper than per-room zoning — `floor-plan-concept.md` itself flags this saving as likely understated, not modelled further here |
| Reception build (counter structure, low-section) | 3% | A$4,874 | A$7,027 | A$9,181 | MEDIUM | |
| Staff area fit-out (solid-wall room, kitchenette plumbing) | 3% | A$4,874 | A$7,027 | A$9,181 | MEDIUM | |
| **Acoustic treatment for curtain bays** | 3% | A$4,874 | A$7,027 | A$9,181 | MEDIUM | Prices the real sound-insulation trade-off `floor-plan-concept.md` itself discloses as "genuinely weakened by the curtain-partition change... not resolved" — not hidden, an explicit line |
| **Category C subtotal (= total construction cost)** | **100%** | **A$162,452** | **A$234,241** | **A$306,029** | | Matches `floor-plan-concept.md`'s own low/mid/high construction figures exactly |

**All items:** required before opening, required day-one, not optional (the fit-out is the venue itself).

---

## D. Furniture, Fixtures and Fittings

Built from `docs/equipment-costs.md`'s existing itemised lines, re-bucketed into genuinely furniture-type items — **a real overlap was found and resolved**: `docs/floor-plan-concept.md`'s Fit-Out Cost Estimate carries its own separate "Furniture and fittings (lounge chairs, reception counter, styling chairs)" line (A$15,000–35,000) that duplicates items already itemised inside `equipment-costs.md`'s Lounge (§6) and Hair (§5) sections. **This reconstruction uses only `equipment-costs.md`'s granular item-level figures**, not `floor-plan-concept.md`'s separate summary line, to avoid double-counting — the reception counter *structure* is priced once, in Category C's cabinetry trade above.

| Item | Scenario A | Scenario B | Scenario C | Confidence | Source/Evidence | Before Opening | Day-One | Optional |
|---|---|---|---|---|---|---|---|---|
| Lounge & common-area furniture (chairs, side tables, coffee tables, lamps) | A$5,000 | A$10,000 | A$15,000 | HIGH | `equipment-costs.md` §6 | Yes | Yes | No |
| Reception furniture (desk chair, drawer units, waiting bench — not the built-in counter, see Category C) | A$800 | A$1,400 | A$2,000 | LOW | Not itemised anywhere in this repo — general estimate | Yes | Yes | No |
| Treatment beds/tables (2 massage tables + 2 facial/beauty beds) | A$2,400 | A$4,600 | A$6,800 | HIGH | `equipment-costs.md` §4, §5A | Yes | Yes | No |
| Styling chairs (×4) + manicure chairs (×4) + pedicure spa chairs (×4) | A$6,000 | A$10,200 | A$14,400 | HIGH | `equipment-costs.md` §3, §5 | Yes | Yes | No |
| Staff room furniture (lockers, table, shelving) | A$1,500 | A$2,500 | A$3,500 | LOW | Not separately itemised in this repo — general estimate; the staff room's own build (walls, kitchenette plumbing) is in Category C | Yes | Yes | No |
| Signage (shopfront + internal wayfinding) | A$3,000 | A$5,500 | A$8,000 | HIGH | `equipment-costs.md` Summary Budget / `floor-plan-concept.md` | Yes | Yes | No |
| Decorations / branding elements (artwork, plants, wall graphics) | A$500 | A$1,250 | A$2,000 | LOW | Not itemised anywhere in this repo — a genuinely new line, flagged as unsourced | No (can be added post-opening) | No | Yes |
| Storage hamper/lidded bins (×2, massage linen) | A$60 | A$80 | A$100 | HIGH | `equipment-costs.md` §4 | Yes | Yes | No |
| **Category D subtotal** | **A$19,260** | **A$35,530** | **A$51,800** | | | | | |

---

## E. Medical and Operational Equipment

Day-one required equipment, re-bucketed from `equipment-costs.md`'s room-by-room lists — this category explicitly excludes each room's own embedded "opening stock" consumable lines (moved to Category F, see the de-duplication note there) and the furniture items already counted in Category D.

| Item | Scenario A | Scenario B | Scenario C | Confidence | Source/Evidence | Before Opening | Day-One | Optional |
|---|---|---|---|---|---|---|---|---|
| Pathology/phlebotomy equipment (2 phlebotomy chairs, vasovagal recovery chair, centrifuge, sharps/blood-spill kit, specimen transport, documentation) | A$6,330 | A$8,285 | A$10,240 | HIGH | `equipment-costs.md` §1 | Yes | Yes | No |
| Nail equipment (4 nail tables w/ dust collector, LEV unit, UV/LED lamps, tool trolleys) | A$4,500 | A$6,850 | A$9,200 | HIGH | `equipment-costs.md` §3 | Yes | Yes | No |
| Hair equipment (dryers, straighteners, backwash basin+chair hardware, mirror, trolleys) | A$4,400 | A$7,150 | A$9,900 | HIGH | `equipment-costs.md` §5 | Yes | Yes | No |
| Beauty/brows equipment (magnifying lamp, wax heater, brow/lash tools, facial steamer, trolley) | A$750 | A$1,145 | A$1,540 | HIGH | `equipment-costs.md` §5A | Yes | Yes | No (facial steamer itself is flagged optional within §5A) |
| Massage-room equipment (bolster/pillow, heated blanket, oil warmer, diffuser) | A$700 | A$1,000 | A$1,300 | HIGH | `equipment-costs.md` §4 | Yes | Yes | No |
| Technology (iPads, POS terminals, printers, WiFi router, admin computer) | A$3,240 | A$5,580 | A$7,920 | HIGH | `equipment-costs.md` §8 | Yes | Yes | No |
| Emergency/safety equipment (first aid kits, AED, panic buttons, fire extinguisher) | A$2,360 | A$3,340 | A$4,320 | HIGH | `equipment-costs.md` §11 | Yes | Yes | No |
| General cleaning equipment (vacuum, mop system, waste bins) | A$300 | A$550 | A$800 | LOW | Not previously itemised anywhere in this repo — a genuine gap, filled with a disclosed general estimate | Yes | Yes | No |
| **Category E subtotal (day-one required)** | **A$22,580** | **A$33,900** | **A$45,220** | | | | | |

**Optional / Phase 2 equipment — NOT included in any scenario total above, carrying forward Anthony's own existing decision (`equipment-costs.md`, 2026-07-31), not re-litigated here:**

| Item | Range | Status |
|---|---|---|
| Spray tan booth | A$2,750–6,550 | Phase 2 / post-launch expansion |
| Hire fleet (TENS units, birth balls, etc.) | A$3,610–5,630 | Phase 2 / post-launch expansion |
| China-sourced branded retail/hire-buffer stock | A$3,550–8,400 | Phase 2 / post-launch expansion |

---

## F. Opening Inventory and Consumables

**De-duplication finding:** `equipment-costs.md` §12 (consolidated "Opening Consumables Stock," A$2,035–3,650) and the embedded "opening stock" sub-lines inside §3 (Nail), §4 (Massage), §5 (Hair), and §5A (Beauty) contain at least one confirmed identical duplicate (massage oil, A$125–250, appears identically in both §4's own total and §12) and several near-duplicates (gel polish, hair products, facial products) that §5A's own note claims are not double-counted but does not actually reconcile for the massage-oil case. **This reconstruction resolves the overlap by using §12 as the single primary source**, adding only the per-section consumable items §12 does not otherwise cover.

| Item | Scenario A | Scenario B | Scenario C | Confidence | Source/Evidence | Before Opening | Day-One | Optional |
|---|---|---|---|---|---|---|---|---|
| Consolidated opening consumables stock (massage oil, gel polish, hair/facial products, pathology consumables, spray-tan-kit consumables excluded per Phase 2, lounge snacks, printed forms, cleaning/disinfection supplies) | A$2,035 | A$2,843 | A$3,650 | HIGH | `equipment-costs.md` §12 | Yes | Yes | No |
| Nail-specific consumables not in §12 (files/buffers/tools, disinfection solution, dust masks) | A$280 | A$380 | A$480 | HIGH | `equipment-costs.md` §3 | Yes | Yes | No |
| Beauty/brows-specific consumables not in §12 (brow tint, wax, disposable brow/wax consumables) | A$350 | A$500 | A$650 | HIGH | `equipment-costs.md` §5A | Yes | Yes | No |
| Hair-specific consumables not in §12 (colour gowns + towels) | A$150 | A$200 | A$250 | HIGH | `equipment-costs.md` §5 | Yes | Yes | No |
| Massage-specific consumables not in §12 (essential oils, linen set) | A$565 | A$782 | A$1,000 | HIGH | `equipment-costs.md` §4 | Yes | Yes | No |
| **Category F subtotal** | **A$3,380** | **A$4,706** | **A$6,030** | | | | | |

**PPE and uniforms:** not itemised anywhere in this repo as a distinct line — the AED/first-aid kit (Category E) and general cleaning/disinfection supplies (above) are the only PPE-adjacent items found. **Flagged UNKNOWN** — staff uniform policy and cost has no source in this repository.

---

## G. Technology and Systems

Distinct from Category E's technology **hardware** (already priced above) — this category covers software setup, subscriptions' one-off configuration, and IT installation labour.

| Item | Scenario A | Scenario B | Scenario C | Confidence | Source/Evidence | Before Opening | Day-One | Optional |
|---|---|---|---|---|---|---|---|---|
| Website setup/build (Squarespace DIY through to a professional build) | A$1,500 | A$3,000 | A$6,000 | LOW | `docs/poppy-marketing.md` §4 recommends Squarespace (A$23–33/month ongoing, not a build cost) — the one-off build cost itself is not stated in this repo, general estimate | Yes | Yes | No |
| Domain name registration | A$20 | A$35 | A$50 | LOW | `docs/grace-startup-plan.md` Week 9–10 lists domain registration as an action, no fee stated — general market rate | Yes | Yes | No |
| IT setup / installation (network cabling, WiFi configuration, POS system setup labour) | A$500 | A$900 | A$1,500 | LOW | Not itemised anywhere in this repo — general estimate; the WiFi router **hardware** itself is already in Category E | Yes | Yes | No |
| Booking system (Fresha) configuration | A$0 | A$0 | A$0 | HIGH | `docs/ivy-booking-system.md` — Fresha has no setup fee; the A$14.95/user/month Team plan (1–2 admin seats) is an ongoing operating cost, already reflected in the canonical opex layer, not a startup capital line | Yes | Yes | No |
| Xero accounting software configuration | A$0 (bundled) | A$0 (bundled) | A$0 (bundled) | HIGH | Bundled into the accountant engagement, Category J below — not double-counted here | Yes | Yes | No |
| **Category G subtotal** | **A$2,020** | **A$3,935** | **A$7,550** | | | | | |

---

## H. Staffing Before Opening

**Ongoing wages once revenue starts are explicitly excluded.** Every item below is pre-opening only — recruitment, training/credentialing, and the Venue Manager's critical-path pre-opening working period.

| Item | Scenario A | Scenario B | Scenario C | Confidence | Source/Evidence | Before Opening | Day-One | Optional |
|---|---|---|---|---|---|---|---|---|
| Recruitment/job-ad costs (Venue Manager, Phlebotomist ×2, Receptionist, Massage, Nails, Beauty/Brows — ~5 postings) | A$2,000 | A$2,900 | A$3,750 | LOW | Not itemised anywhere in this repo — general AU job-board (Seek-equivalent) pricing benchmark, disclosed | Yes | N/A | No |
| Venue Manager pre-opening salary (critical-path hire, working through fit-out/setup) | A$12,496 (8 wks) | A$17,182 (11 wks) | A$21,868 (14 wks) | HIGH (rate) / MEDIUM (duration) | `docs/venue-manager-job-posting.md` (A$72,500/yr + 12% super ≈ A$81,200/yr ≈ A$1,562/week); duration modelled against `docs/grace-startup-plan.md`'s Week 9–20 fit-out-to-launch span, varied by scenario | Yes | N/A | No |
| Phlebotomist credentialing/pre-opening training (×2, before WDP sign-off) | A$1,225 (1 wk) | A$1,838 (1.5 wks) | A$2,450 (2 wks) | HIGH (rate) / LOW (duration, unstated in this repo) | `data/canonical/wages.yml#wage_phlebotomist` (A$24.50/hr × 25hr/wk); duration not stated anywhere in this repo — flagged, estimated | Yes | N/A | No |
| Receptionist training | A$1,602 (2 wks) | A$2,403 (3 wks) | A$3,204 (4 wks) | HIGH | `docs/staff-plan.md` §7 explicitly states "train 3 weeks before soft open" — Scenario B matches this exactly; `data/canonical/wages.yml#wage_receptionist_manager` (A$26.70/hr × 30hr/wk) | Yes | N/A | No |
| Treatment staff trial/induction (massage, nails, beauty/brows) | A$3,480 | A$7,830 | A$13,920 | HIGH (rate) / MEDIUM (headcount/duration ramp) | `docs/staff-plan.md` §7 ("trial run during test operations week"); blended treatment-staff rate ≈A$29/hr × 30hr/wk, headcount and duration scaled by scenario | Yes | N/A | No |
| First Aid / Fire Warden course (Venue Manager) | A$150 | A$220 | A$300 | LOW | `docs/emergency-plan.md` requires current First Aid before opening — no fee stated in this repo, general WA course-fee estimate | Yes | Yes | No |
| Payroll setup labour | A$0 (bundled) | A$0 (bundled) | A$0 (bundled) | HIGH | Bundled into the Venue Manager's own pre-opening time above and the accountant engagement (Category J) — not double-counted | Yes | N/A | No |
| **Category H subtotal** | **A$20,953** | **A$32,373** | **A$45,492** | | | | | |

---

## I. Marketing and Launch

**Signage is not repeated here** — it is priced once, in Category D. Printed forms/referral cards already in Category F's opening-stock consumables are not repeated either. This category covers the genuinely pre-opening, one-off launch push, distinct from the ongoing Month 1–4 marketing ramp already modelled in `data/canonical/cost_ramp.yml` (an operating cost, not touched by this reconstruction).

| Item | Scenario A | Scenario B | Scenario C | Confidence | Source/Evidence | Before Opening | Day-One | Optional |
|---|---|---|---|---|---|---|---|---|
| Professional photography (venue + launch content) | A$800 | A$1,400 | A$2,000 | LOW | `docs/grace-startup-plan.md` Week 17–18 lists "professional photography of venue" as an action — no fee stated, general Perth commercial photography rate | Yes | No | No |
| One-off pre-launch marketing push (beyond the ongoing Month 1 ramp) | A$600 | A$1,500 | A$3,000 | LOW | Distinct from `cost_ramp.yml`'s existing Month 1 ramp figure (A$600/month, ongoing from first revenue) — this is a separate, one-off pre-opening push, disclosed as a new estimate | Yes | No | No |
| Promotional materials for referral-practice outreach (branded flyers/business cards, beyond the printed forms already in Category F) | A$200 | A$350 | A$500 | LOW | Not itemised anywhere in this repo — general estimate | Yes | No | Yes |
| **Category I subtotal** | **A$1,600** | **A$3,250** | **A$5,500** | | | | | |

---

## J. Professional Services

| Item | Scenario A | Scenario B | Scenario C | Confidence | Source/Evidence | Before Opening | Day-One | Optional |
|---|---|---|---|---|---|---|---|---|
| Accountant (initial brief + structure confirmation) | A$500 | A$1,000 | A$1,500 | HIGH | `docs/financial-setup.md` STEP 1 ("A$500–1,500 for initial brief and structure confirmation") | Yes | N/A | No |
| ASIC business name registration | A$39 | A$39 | A$39 | HIGH | `docs/financial-setup.md` STEP 2 (fixed government fee) | Yes | N/A | No |
| Solicitor (lease review) | A$0 (bundled) | A$0 (bundled) | A$0 (bundled) | HIGH | Already counted in Category A's "Legal fees" line — not double-counted here | Yes | N/A | No |
| Insurance brokerage/setup fee | A$0 | A$0 | A$0 | HIGH | BizCover-style quotes are free; the annual **premium** itself (A$4,800–19,000/yr depending on modelled-vs-itemised treatment, `docs/VERIFICATION-TRACKER.md` item 19) is an ongoing operating cost, already in the canonical opex layer — not re-counted here as startup capital, to avoid double-counting against `data/canonical/opex.yml` | Yes (setup) | N/A | No |
| Compliance consulting (WA Skin Penetration Code / NPAAC) | A$0 (bundled) | A$0 (bundled) | A$0 (bundled) | HIGH | Already counted in Category B — not double-counted here | Yes | N/A | No |
| **Category J subtotal** | **A$539** | **A$1,039** | **A$1,539** | | | | | |

---

## K. Contingency — Separate, Explicit, Not Hidden

| Scenario | Contingency % | Basis | Amount |
|---|---|---|---|
| A (Lean) | 10% | Lower relative risk — the simpler open-plan design carries fewer trade interfaces and unknowns than a fully-partitioned fit-out | A$25,738 |
| B (Expected) | 15% | Reuses the one contingency percentage that already exists anywhere in this repo (`docs/investor-memorandum.md`'s risk table) — `docs/VERIFICATION-TRACKER.md` item 27 flags that document never actually shows this percentage being calculated into any total, so applying it explicitly here (rather than leaving it ambiguous) is a genuine methodological improvement, not a re-use of a resolved figure | A$58,369 |
| C (Higher-cost) | 20% | A more conservative buffer for the higher-uncertainty scenario | A$107,472 |

---

## Three Scenario Totals

| Category | Scenario A (Lean) | Scenario B (Expected) | Scenario C (Higher-Cost) |
|---|---|---|---|
| A. Premises acquisition | A$19,000 | A$28,500 | A$47,500 |
| B. Design and approvals | A$5,600 | A$11,650 | A$20,700 |
| C. Fit-out | A$162,452 | A$234,241 | A$306,029 |
| D. Furniture, fixtures and fittings | A$19,260 | A$35,530 | A$51,800 |
| E. Medical and operational equipment | A$22,580 | A$33,900 | A$45,220 |
| F. Opening inventory and consumables | A$3,380 | A$4,706 | A$6,030 |
| G. Technology and systems | A$2,020 | A$3,935 | A$7,550 |
| H. Staffing before opening | A$20,953 | A$32,373 | A$45,492 |
| I. Marketing and launch | A$1,600 | A$3,250 | A$5,500 |
| J. Professional services | A$539 | A$1,039 | A$1,539 |
| **Subtotal (A–J)** | **A$257,384** | **A$389,124** | **A$537,360** |
| K. Contingency | A$25,738 (10%) | A$58,369 (15%) | A$107,472 (20%) |
| **TOTAL (A–K)** | **A$283,122** | **A$447,493** | **A$644,832** |

**No scenario is selected as preferred.** All three remain live, disclosed alternatives.

---

## 4. Reconciliation Against the Existing Funding Range

### 4.1 What this reconstruction is directly comparable to — and what it isn't

The existing bounded range (A$357,390–A$577,180, `docs/architecture/FUNDING-REQUIREMENT-INVESTIGATION.md`) combines two components: **Pre-Opening Capital** (A$272,390–467,180 — equipment/furniture/signage + construction + legal/lease-bond only) and a separate **Working Capital Reserve** (A$85,000–110,000 — funds Months 1–3 operating losses). **This reconstruction (Categories A–K) is scoped identically to the Pre-Opening Capital component only** — it does not include, model, or touch the Working Capital Reserve, which remains an untouched, separate, existing concept.

**Like-for-like comparison:**

| | Old Pre-Opening Capital | New bottom-up reconstruction (A–K) |
|---|---|---|
| Low end | A$272,390 | A$283,122 (Scenario A) |
| High end | A$467,180 | A$644,832 (Scenario C) |

The low ends are close (≈4% higher). The high ends diverge materially (≈38% higher) — explained below, not forced to reconcile.

### 4.2 Which historical assumptions were removed

- The old Pre-Opening Capital figure was a **decomposition** of `docs/CURRENT-STATE.md` §7.1+§7.2+§7.3's own existing component sum — not an independent rebuild. This reconstruction is genuinely independent, built category-by-category from first principles, not reverse-engineered from any existing total.
- The old figure's construction cost and equipment/furniture cost are **retained, not removed** — this reconstruction deliberately anchors Category C (fit-out) to `floor-plan-concept.md`'s own already-computed construction total, and Categories D+E (furniture+equipment) closely track `equipment-costs.md`'s own day-one total (A$43,190–97,430 vs. this reconstruction's A$41,840–A$97,020 combined) — confirming the re-bucketing methodology reconstructs the same overall equipment/furniture envelope where the two overlap.

### 4.3 Which costs were reduced

- Nothing in the fit-out/construction cost itself was reduced relative to the existing figure — it was **decomposed**, not cut. The open-plan design's cost reduction (vs. a traditional fully-partitioned layout) was already captured by `floor-plan-concept.md` before this reconstruction began (A$10,736–17,256 wall-to-curtain/open-plan saving) — this reconstruction inherits that saving, it does not create a new one.

### 4.4 Which costs remain uncertain

- **Fit-out trade percentage splits (Category C)** — MEDIUM confidence, a general industry rule-of-thumb, not confirmed against a real quote for this specific fit-out. Only real builder quotes (per `docs/architecture/STARTUP-COST-RECONCILIATION.md` §4's own existing recommendation) would firm this up.
- **Recruitment costs, website build, photography, IT setup, general cleaning equipment, decorations** (Categories D, G, H, I) — all LOW confidence, genuinely new estimates using general Australian market knowledge, not previously priced anywhere in this repository.
- **Pre-opening staffing durations** (Category H) — the Venue Manager's and treatment staff's actual pre-opening working periods are modelled against `grace-startup-plan.md`'s week-based schedule, not independently confirmed; the phlebotomist credentialing duration specifically has no source anywhere in this repo and is flagged LOW confidence.
- **PPE/uniforms** — flagged UNKNOWN, no source exists anywhere in this repository for this line.

### 4.5 Why the new bottom-up number differs materially at the high end — explained, not forced to match

Three genuine, disclosed reasons, not an error in either figure:

1. **Scope was genuinely narrower in the old figure.** The old Pre-Opening Capital component never included staffing-before-opening (Category H, A$20,953–45,492), marketing/launch (Category I, A$1,600–5,500), technology/software setup (Category G, A$2,020–7,550), or opening consumables (Category F, A$3,380–6,030) at all — these four categories alone add A$27,953–64,572 across the three scenarios, accounting for a substantial share of the divergence.
2. **Contingency was ambiguous in the old figure, explicit here.** `docs/VERIFICATION-TRACKER.md` item 27 already flags that the only contingency percentage in this repo (15%, `investor-memorandum.md`'s risk table) was never confirmed as actually applied to any total. This reconstruction applies contingency explicitly and separately (Category K, 10–20%) — a genuine methodological improvement, not a inflated re-statement of an existing number.
3. **Scenario C is deliberately conservative**, using high-end sourced ranges across every category simultaneously plus a 20% contingency — the old figure's own high end (A$467,180) does not stack every high-end assumption together with an explicit contingency layered on top the way Scenario C does here.

### 4.6 Comparison to Anthony's adopted total

Anthony's own adopted, reconciled total (`docs/CURRENT-STATE.md` §7.4) is **A$292,335–594,900**, which includes the Working Capital Reserve, unlike this reconstruction. Adding the existing, untouched A$85,000–110,000 Working Capital Reserve to this reconstruction's Scenario A/C totals for an informational, all-in comparison (not a construct of this phase, shown for context only): **A$368,122 (Scenario A + low reserve) to A$754,832 (Scenario C + high reserve)** — bracketing Anthony's adopted range at the low end, materially exceeding it at the high end, for the same three reasons in §4.5.

---

## Confidence and Evidence Gaps Found

- **Recruitment advertising costs** — no source anywhere in this repository.
- **Website build cost** — only the ongoing subscription cost (`poppy-marketing.md`) is sourced; the one-off build/design cost is not.
- **Professional photography cost** — the action is sourced (`grace-startup-plan.md`), the cost is not.
- **Pre-opening training/credentialing durations** — Receptionist's 3-week figure is explicitly sourced; every other role's pre-opening duration (Venue Manager, phlebotomists, treatment staff) is modelled against the general week-based schedule, not independently confirmed per role.
- **PPE/uniforms** — flagged UNKNOWN, no source exists.
- **Fit-out trade percentage splits** — a disclosed general industry benchmark, not a GTT-specific quote; only real builder quotes against a confirmed venue would firm this up (same conclusion `STARTUP-COST-RECONCILIATION.md` §4 already reached).
- **Demolition/strip-out cost** — assumes a raw-shell or lightly-fitted tenancy; a confirmed venue with an existing incompatible fit-out could change this materially, not modellable without one.

---

## Validation — Confirmed No Model Changes Occurred

- `git status --short` before this phase: clean.
- File created this phase: `docs/architecture/startup-cost-reconstruction.md` only.
- Full pytest suite: **114 passed**, 0 failed.
- `tools/validate_canonical_data.py`: **13 files checked, 0 errors, 27 warnings** — identical to every prior phase.
- `tools/check_consistency.py`: **0 findings** — identical to every prior phase.
- `git diff --stat` against `data/canonical/`, `data/models/`, and `tools/*.py`: zero changes.
- `data/canonical/startup_costs.yml` was **not modified** — this reconstruction is not wired into the canonical layer this phase, per explicit instruction.

## Recommended Next Step

Two paths forward, neither actioned here: (1) if Anthony wants this reconstruction formally adopted, a separate future phase would wire it into `data/canonical/startup_costs.yml` alongside (not replacing) the existing historical ranges, following this repo's established "disclose, don't silently overwrite history" convention; (2) independently of that decision, the single highest-value action to firm up the largest genuine uncertainty in this reconstruction — the fit-out trade percentage splits (Category C, ~57-64% of every scenario's total) — is the same one `docs/architecture/STARTUP-COST-RECONCILIATION.md` and the Commercial Validation Framework's venue dependency plan already identified: 3 real builder quotes against a confirmed venue floor plate.
