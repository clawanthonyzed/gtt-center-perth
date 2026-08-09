# GTT Center Perth — Service Catalogue Audit

**Purpose:** completeness audit of `data/canonical/services.yml` against the repo's own known service references. Confirms what was canonicalised, what wasn't, and why — nothing found this pass was silently omitted. Companion to `data/canonical/services.yml` (structured data) and `data/canonical/pricing.yml` (canonical pricing for the subset of services already migrated there).

**Method:** every service reference in `docs/services-pricing-locked.md`, `docs/services-master-table.md`, `docs/extended-wellness-services.md`, `docs/pm-package-structure.md`, `docs/pm-staffing-roster.md`, and `docs/hire-purchase-china.md` §1C was checked against the other documents, not assumed correct from a single source.

---

## 1. Services Canonicalised

**99 total** (88 in `services.yml`'s `records` list, 6 in `historical_services`, 5 in `future_services`):

| Category | Count |
|---|---|
| GTT-window services (Part A core) | 23 |
| Facial add-ons | 11 |
| Nail add-ons | 4 |
| Belly-casting add-on | 1 |
| PM standalone/afternoon services (hair, massage, facial, nails, lash, hair colour, spray tan, belly casting) | 25 |
| AM packages | 2 |
| PM packages (proposed) | 3 |
| PM a-la-carte umbrella | 1 |
| Self-service/tablet (birth plan tiers) | 4 |
| Ancillary — café | 7 |
| Ancillary — retail | 5 |
| Ancillary — GDM info session | 1 |
| Future services | 5 |
| Historical/removed services | 6 |
| Future/Phase 2 (3D scan) | 1 |

**Of the 88 `records`, 13 reference `data/canonical/pricing.yml` by `pricing_ref`** (the AM packages, PM packages, PM a-la-carte average, and the 7 individual services Phase 1 already canonicalised) rather than restating a price — see `services.yml`'s own header for the full architecture rationale. **The remaining 75 records carry their price directly in `services.yml`**, as the first canonicalisation of that fact anywhere in this repo's machine-readable layer.

---

## 2. Current vs. Proposed vs. Historical Breakdown

| Lifecycle | Count | Notes |
|---|---|---|
| `current` | 82 | Actively offered/priced services, including 3 with a genuine, previously-undisclosed status question (spray tan — see §4) |
| `proposed` | 6 | PM Duo/Refresh/Glow (3), GDM info session (1), 3D keepsake scan (1), spray tan (1, reclassified this pass — see §4) |
| `historical` | 6 | Explicitly removed/rejected: hot stone massage, full body scrub, pregnancy body wrap, perinatal mental health screening, men's preconception health, maternity photography |
| (future_services list, separately tracked) | 5 | Lactation, GDM dietitian, prenatal yoga, pelvic floor physio, hypnobirthing — Month 3+ to Month 6+ |

**A service in an old document is not automatically current** — enforced directly: `svc_pm_spray_tan` is recorded `lifecycle: proposed`, not `current`, despite both pricing source documents (`services-pricing-locked.md`, `services-master-table.md`) still presenting it as an active, priced, current-scope service. `docs/equipment-costs.md`'s 2026-07-31 reclassification of the physical spray tan booth to "PHASE 2 / POST-LAUNCH EXPANSION" is treated as the more recent, more specific instruction and followed here — the pricing documents' own framing is flagged as stale, not followed. See `conflict_spraytan_status_and_price` in `services.yml`.

---

## 3. Services With Unresolved Pricing (12 `PLACEHOLDER` records)

| Service | Why unresolved |
|---|---|
| PM Duo, PM Refresh, PM Glow (proposed packages) | Two discount-tier options exist (10%/15% off), neither finalised by Anthony — see `pricing.yml`'s own `pm_package_*` records |
| Hybrid/volume lash infill | Price conflict (A$125 vs A$120) |
| Half foil highlights, Full foil highlights, Toner/gloss, Colour+blowdry | Price conflicts (see §4) |
| Spray tan (automated booth) | Price conflict AND lifecycle conflict (see §4) |
| GDM snack pack | Price conflict (A$20 point vs A$18-25 range) |
| GDM Information Session | Client-facing price genuinely undecided ("A$0 or A$20-30 optional") in the source itself — not a conflict between documents, a genuine open choice within one document |
| 3D Keepsake Ultrasound Scan | No client-facing price has ever been set anywhere in this repo — future/Phase 2, not committed |

None of these 12 was resolved by picking a value — every one is recorded with `price: null` and the competing options or the reason for the gap disclosed in the record's own `notes`.

---

## 4. Services With Conflicting Definitions (6 declared conflicts in `services.yml`)

1. **`conflict_spraytan_status_and_price`** — price (A$55/A$60 two-tier vs. flat A$60) AND lifecycle (current vs. Phase 2) both unresolved. The most consequential finding this pass — a service two source documents still present as active and priced was moved to Phase 2 nearly two weeks before this migration, undisclosed until now.
2. **`conflict_haircolour_prices`** — 4 of 7 hair colour services disagree between `services-pricing-locked.md`/`services-master-table.md` and `extended-wellness-services.md` (half foil highlights, full foil highlights, toner/gloss, colour+blowdry). The other 3 (single process colour, both balayage services) agree exactly across all 3 sources.
3. **`conflict_lash_infill_price`** — A$125 vs. A$120, the smallest-magnitude conflict found, retained regardless of size per the coordinator's explicit "do not silently pick one" instruction.
4. **`conflict_gdm_snack_pack_price`** — A$20 point price vs. A$18-25 range.
5. **`conflict_dietitian_service_status`** — the highest-materiality conflict relative to its size: `services-master-table.md`/`services-pricing-locked.md` both list "GDM dietitian consultation" as a planned Month 6+ future service, while `extended-wellness-services.md`'s own "Removed Services" section states dietary services are "deferred indefinitely." These are materially different framings of whether this revenue line should be planned for at all, not just its price.
6. **`conflict_locked_pricing_completeness_gap`** — not a disagreement between two sources, but a genuine completeness gap in the document titled "Locked Pricing": 6 services it describes as bookable have no price anywhere in that document, only in `services-master-table.md`.

---

## 5. Services Mentioned But Insufficiently Specified

- **Toner/gloss** — `services-pricing-locked.md`/`services-master-table.md` give a point price (A$65); `extended-wellness-services.md` gives a range (A$50-80) that contains it but isn't identical — genuinely unclear whether A$65 is meant to be a fixed price or a typical point within a real range.
- **SNS/dip powder full set** — duration itself disagrees slightly between sources (`services-pricing-locked.md`: 75-90 min; `services-master-table.md`: 60-75 min) in addition to the already-flagged missing price — a minor, undisclosed discrepancy noted in the record but not separately raised as its own conflict (duration-only, no price at stake).
- **GDM Information Session** — contractor fee to the venue (A$150-300/session) is stated, but this is a *cost*, not migrated to `data/canonical/opex.yml` this phase (out of scope) — flagged as a follow-up.
- **3D Keepsake Ultrasound Scan** — genuinely no client-facing price exists anywhere in this repo, only an equipment cost estimate (A$12,000-25,000) in `hire-purchase-china.md`, itself not migrated to `capex.yml` this phase since the service isn't committed.

---

## 6. Potential Duplicates

None found that represent the *same* service twice with different IDs — every apparent overlap resolved to either (a) a genuine price/definition conflict (§4, kept as separate records with the conflict disclosed) or (b) a legitimately distinct service (e.g. `addon_brow_wax_tint_during_facial`, a facial add-on, is a separate record from `svc_brow_wax_tint`, a standalone GTT-window service — same price, different duration when bundled, correctly kept as two records with the relationship noted). The closest thing to a duplicate is the Summary-Budget-vs-section-total pattern already found and tracked in `capex.yml` last phase (equipment costs, not services) — not re-litigated here.

---

## 7. Services Requiring Verification (Beyond the 6 Declared Conflicts)

- **Every hair colour price and duration range** — none of these is sourced to anything beyond market-research-style planning figures across all 3 documents; a real supplier/product-cost basis was not found for any of them.
- **The GDM Information Session's contractor fee (A$150-300/session)** — a round planning estimate, no quote.
- **Whether "Toner/gloss" A$65 (point) and A$50-80 (range) are meant to describe the same pricing decision at different precision, or genuinely different assumptions** — see §5.

---

## 8. What This Audit Does Not Do

It does not resolve any of the 6 declared conflicts, choose a PM package pricing tier, decide spray tan's committed lifecycle status, calculate any revenue figure, or build a pricing/revenue model. It does not migrate the GDM Information Session's contractor cost into `opex.yml` or the 3D scanner's equipment cost into `capex.yml` — both flagged as follow-ups, not attempted.
