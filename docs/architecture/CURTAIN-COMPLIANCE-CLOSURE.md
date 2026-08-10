# Curtain Compliance Closure — Tracker Item 51

**Phase:** Continued operational optimisation — closes the investigation opened in `docs/architecture/CHINA-ASIA-SUPPLIER-FEASIBILITY.md` §1 (`docs/VERIFICATION-TRACKER.md` item 51). **Does not wire a dollar figure into `data/canonical/startup_costs.yml`** — that remains a distinct, not-yet-authorised procurement step.

**Date:** 2026-08-10
**Research method:** direct web search of the applicable Australian standards and current commercial supplier landscape — not previously done in this repository before this pass.

---

## 1. Exact Compliance Requirement — Confirmed

**The applicable standards are AS 1530.2 (free-hanging curtains) and AS/NZS 1530.3 (wall-fixed fabric).** Both sit under the National Construction Code's fire-hazard-properties framework (Specification 7 in the current NCC edition, formerly Specification C1.10). AS 1530.2 tests a fabric's Flammability Index by exposing a vertically-mounted specimen to a radiant heat source; AS/NZS 1530.3 measures four indices — ignitability, flame spread, heat release, and smoke production. **For NCC/BCA compliance, the accepted threshold is a Flammability Index of 10 or below** (New Zealand's own standard is stricter, ≤6 — not the applicable jurisdiction here, but confirms this is a well-established, widely-used test regime, not an obscure one).

**Sources:** [Specification 7 Fire hazard properties | NCC](https://ncc.abcb.gov.au/editions/ncc-2022/adopted/volume-one/c-fire-resistance/7-fire-hazard-properties), [AS 1530 Flame Retardant Fabric Guide for Australian Projects](https://begoodtex.com/blog/as-1530-flame-retardant-fabric/), [AS/NZS 1530 requirements for fire resistance levels — Greenline](https://greenline.com.au/blog/as-1530).

---

## 2. Building Classification — Genuinely Relevant, Not Yet Determinable With Certainty

A material finding this closure surfaces: **GTT Center Perth is very unlikely to be a Class 9a (health-care) building**, the classification carrying the strictest fire-hazard requirements. Class 9a specifically applies where "the predominant treatment renders patients non-ambulatory... requires supervised on-site medical care after treatment" — describing patients rendered unconscious or unable to move (e.g. day surgery). **GTT clients are ambulatory throughout — venepuncture is a routine blood draw, not a procedure requiring post-treatment supervised medical recovery in this sense.** The far more likely classifications, based on comparable precedent already confirmed by direct search:
- **Class 5** (professional/commercial office) — the classification most private allied-health/ambulatory clinics (physiotherapy, podiatry, etc.) receive, where "patients arrive, receive treatment, and leave under their own capacity" — a close match to GTT's own model.
- **Class 6** (shops/services) — the classification a hairdresser/barber shop receives, directly relevant given GTT's substantial beauty/wellness component.

**This review cannot determine the exact classification with certainty** — that is a building surveyor/certifier determination, made against the specific venue's predominant use mix, not something resolvable from this repository alone. **What is confirmed: neither Class 5 nor Class 6 carries anything close to Class 9a's stricter regime** (which includes requirements like non-combustible curtain walls and external wall-wetting sprinkler systems, entirely inapplicable to a Class 5/6 tenancy). This materially de-risks the compliance question relative to how it might have looked if GTT were mistakenly assumed Class 9a.

**Sources:** [Building classifications | NCC](https://ncc.abcb.gov.au/ncc-navigator/building-classifications), [Allied Health Clinic Fitout: Design and Compliance Guide](https://designyard32.com.au/blog/allied-health-clinic-fitout).

---

## 3. A Genuine Nuance — Curtains May Be Formally Exempt From Building-Approval Testing, But Should Not Be Treated as Compliance-Free

Direct research surfaced a real, disclosed nuance not assumed away: **"curtains, blinds, or similar decor (other than proscenium curtains) and window treatments are excluded from certain [NCC] requirements... typically not included within building works approval."** This means the strict formal NCC building-approval process may not, on its own, mandate fire-tested curtain fabric as a line item for a Class 5/6 tenancy the way it would for wall linings.

**This finding does not change this review's recommendation.** Three independent reasons fire-rated fabric remains the right choice regardless of the formal exemption: (1) landlord lease conditions commonly require it as a matter of tenancy risk management, independent of building-approval formality; (2) public liability insurance underwriting for a health/beauty premises routinely expects fire-safe soft furnishings; (3) this is a pregnancy-focused, safety-conscious venture by its own stated brand positioning — using non-fire-rated fabric because a formal exemption technically exists would be a poor fit for that positioning, not a genuine cost-saving worth pursuing.

---

## 4. Acoustic Considerations — Tied to the MVP Review's Fabric Decision

`docs/architecture/MVP-OPENING-DECISION-REVIEW.md` §1 already established that the approved opening budget funds **acoustic-rated curtain fabric** (not basic curtain material) as a condition of the accepted opening strategy, addressing the AMT Massage Code's "impervious to sound" standard for the Massage/Facial-Beauty rooms specifically. This closure confirms fire-rating and acoustic performance are not competing requirements needing a trade-off — see §5.

---

## 5. Do Suitable Combined Fire + Acoustic Curtain Systems Exist? — Yes, Confirmed

Direct search of the current Australian commercial supplier market confirms **real, established suppliers already sell curtain products combining both AS 1530.2/1530.3 fire-retardancy and genuine acoustic/sound-absorbing performance in a single product line** — this is not a gap requiring a custom or compromise solution. Confirmed suppliers: Imported Theatre Fabrics (flame retardancy to AS/NZS 1530 Parts 2 & 3), Freedom's Halcyon Multi-Header Curtain range (fire-retardant rated under AS/NZS 1530.2 & 3), Blinds Plus, Lifestyle Curtains, eSafety Supplies (Noiseblock, fire-rated), and Creative Systems.

**Sources:** [Masking & Blackout Curtains Australia | Duvetyne & Molton Fabrics](https://www.importedtheatrefabrics.com.au/masking-acoustic-and-blackout-curtains/), [Buy 140x230cm Halcyon Multi-Header Curtain Slate Acoustic Online | Freedom](https://www.freedom.com.au/product/24517522), [Acoustic Curtains Sydney | Acoustic Curtains Supplier & Installer — Blinds Plus](https://blindsplus.com.au/acoustic-curtains-sydney/), [Acoustic Curtains Sydney | Soundproof Curtains — Lifestyle Curtains](https://www.lifestylecurtains.com.au/products/acoustic-curtains-sydney/), [Noise Reduction Acoustic Curtain Barrier — eSafety Supplies](https://esafetysupplies.com.au/products/noiseblock-noise-reduction-acoustic-curtain-barrier), [Acoustic Curtains | Creative Systems](https://www.creativesystems.net.au/products/acoustic-curtains).

---

## 6. Does Importing (China/Asia) Create Additional Compliance Risk on Top of the Base Fire-Rating Question?

**Yes, and this finding strengthens, not weakens, `docs/architecture/CHINA-ASIA-SUPPLIER-FEASIBILITY.md`'s original recommendation.** Given §5 confirms genuine, purpose-built, dual-compliant Australian products already exist at what is likely a modest total cost (this line item sits at roughly A$1,350–4,874 across the reconstruction/optimisation phases' own component breakdowns — a small fraction of total fit-out spend), the case for pursuing an imported curtain solution weakens further: the realistic saving available from importing generic curtain fabric is small in absolute dollar terms, while the verification burden (independently confirming a genuine, checkable AS 1530.2/3 test report from an overseas supplier, in a category where established Australian suppliers already sell exactly the right combined product) is real and disproportionate to the saving. **Recommendation, now more confident than the prior phase's flag: source curtain track and fabric from an established Australian acoustic-curtain supplier, not an import.**

---

## 7. Tracker Item 51 — Closure

Item 51 is closed as an **investigation** — the compliance question itself is now answered with genuine research, not left as an open flag. **The dollar figure is deliberately not wired into `data/canonical/startup_costs.yml` this phase** — that remains a distinct procurement action, once a specific Australian supplier/product is selected and quoted.

---

## Validation

No canonical YAML, financial model, or revenue/cost methodology was modified by this document (see full validation summary in this phase's combined report-back).
