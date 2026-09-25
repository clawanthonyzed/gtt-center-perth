# GTT Center Perth — Operating Economics Benchmark (Round 3, Priority 3)

**Created:** 2026-09-25 (Round 3) | **Author:** Grace (Operations Manager)
**Purpose:** Revenue density (revenue/sqm, revenue/room, revenue/labour-hour, revenue/client) benchmarked against real businesses, building on `FINANCIAL-FORENSICS-RECONSTRUCTION.md` (Round 2) rather than repeating it.

**Tagging:** `[VERIFIED]` / `[REPORTED]` / `[BENCHMARK]` / `[ESTIMATE]` / `[ASSUMPTION]` / `[UNKNOWN]`.

---

## 1. Revenue per Square Metre

**GTT's own figure (derived, not previously stated anywhere in this repository):** Table 1 annual revenue A$1,716,844.44 (A$143,070.37 × 12) `[CALCULATED — docs/CURRENT-STATE.md]` divided by the 239-249sqm real footprint requirement `[VERIFIED — docs/architecture/VENUE-PROGRAM-AUTHORITATIVE.md]` = **A$6,894-7,183/sqm/year** `[ESTIMATE — this document's own arithmetic]`.

**Real comparable found this round:** no directly comparable multi-service, pathology-adjacent business was found with disclosed revenue+sqm together (see `RENT-ECONOMICS-FORENSICS.md` §2's own disclosed limitation). The closest indirect cross-check: Any Lab Test Now (US direct-to-consumer lab-draw franchise, `CASE-STUDY-DATABASE.md` Case 8) reports average revenue of US$339,000-465,000/year from typical retail-storefront footprints (not disclosed in sqm terms in the sources found) — not usable for a direct per-sqm comparison, flagged as `[UNKNOWN]` for this specific metric.

**Finding:** GTT's own implied revenue/sqm (A$6,894-7,183) is a genuinely high figure relative to a typical single-service Perth salon (which, per the South Perth day spa comparable's own revenue of ~A$286,000/year, would need to occupy only ~40sqm to match this per-sqm rate — implausibly small for a day spa, suggesting the real comparable's revenue/sqm is materially lower than GTT's own implied figure, consistent with `RENT-ECONOMICS-FORENSICS.md`'s conclusion that GTT's higher revenue-per-sqm, not an understated rent, most likely explains the earlier rent-to-revenue contradiction). **This is not evidence GTT's revenue figure is wrong — the AM segment's collection-driven volume is a genuinely different revenue driver to a walk-in day spa's — but it is a concentration point worth being aware of: if the AM segment underperforms, GTT's revenue/sqm would fall toward a more typical day-spa range, materially changing the rent-affordability picture** (see the Table 2 sensitivity in `RENT-ECONOMICS-FORENSICS.md` §4, which already shows Table 2 as materially more rent-sensitive).

---

## 2. Revenue per Labour-Hour

**GTT's own figure:** Total Direct Labor (Table 1, current) A$82,318.05/month `[VERIFIED]`. Total paid labour hours are not fully reconstructable from the documents reviewed this round without a fresh headcount-by-shift calculation (out of scope for the time available) — flagged as `[UNKNOWN — would require a dedicated headcount-hours audit not attempted this round]`.

**A partial, defensible calculation using AM-only figures:** 2 phlebotomists + 8 treatment staff, 6-hour AM shift, 22 trading days/month = (2+8) × 6 × 22 = 1,320 AM labour-hours/month `[ESTIMATE, weekday only, excludes Saturday]`. AM weekday revenue at Table 1 (18 clients × A$250 × 22 days) = A$99,000/month `[CALCULATED — matches the AM segment figure already in docs/CURRENT-STATE.md §7]`. **Implied AM revenue-per-labour-hour: ~A$75/hour** `[ESTIMATE]`.

**Real benchmark found in Round 2, re-applied here:** spa-industry sources commonly target **US$1,000+ per provider-hour** as a healthy benchmark `[BENCHMARK — Tier 4, US-context, currency and market not directly comparable]`. **GTT's own AM revenue-per-labour-hour (~A$75) looks low against this benchmark, but this is a misleading comparison, not a real finding of a problem** — the US$1,000/hour figure describes revenue attributable to a single treatment provider actively delivering one paid service, not a blended figure across a whole shift including phlebotomists (who do not generate a treatment-fee revenue line themselves, only enable the AM segment's admission fee) and treatment staff serving a fixed, pre-set package price rather than a per-treatment US-style fee. **This benchmark should not be applied to GTT Center Perth's blended AM figure — flagged as a benchmark that does not transfer, not silently used to imply a problem that likely does not exist.**

---

## 3. Revenue per Client / Session

**GTT's own figures (already canonical, restated for this benchmark, not newly derived):** AM package average A$250-300 `[VERIFIED]`; PM a-la-carte average historically modelled at ~A$95-117/session `[VERIFIED — docs/CURRENT-STATE.md §2]`.

**Real comparable found this round:** MIWM's own real current pricing (`PATHOLOGY-OPERATIONS-DEEP-DIVE.md` §4) — $220 for a comparable single-treatment GTT package, $400-435 for its 2-treatment Deluxe package. **GTT Center Perth's own AM package pricing (A$250-300) sits between MIWM's two tiers, already cross-checked in Round 2** — not re-derived here, cross-referenced only.

---

## 4. What Was Deliberately Not Pursued Further

A full revenue-per-room (as opposed to revenue-per-sqm or revenue-per-client) calculation was not built, since GTT's own PM room/session-capacity model (`docs/architecture/PM-SESSION-CAPACITY-MODEL-E-2026-09.md`) already contains a more precise, service-type-specific version of this exact calculation, done first-principles from GTT's own real solver work — building a second, cruder external-benchmark version would add confusion, not clarity, per the founder's own instruction not to pursue low-value re-derivation.

---

## Sources

`docs/CURRENT-STATE.md`, `docs/architecture/VENUE-PROGRAM-AUTHORITATIVE.md`, `docs/architecture/PM-SESSION-CAPACITY-MODEL-E-2026-09.md` (this venture's own primary documents); `RENT-ECONOMICS-FORENSICS.md`, `CASE-STUDY-DATABASE.md`, `PATHOLOGY-OPERATIONS-DEEP-DIVE.md` (this round's and Round 2's own companion research).

---

## Changelog

**2026-09-25 (Round 3, created):** New file. Calculated GTT's own implied revenue/sqm (A$6,894-7,183) for the first time in this repository, and reasoned through why it is high relative to a typical single-service comparable without treating that as an error. Explicitly rejected applying the US$1,000/provider-hour benchmark to GTT's blended AM revenue-per-labour-hour figure, since the underlying revenue models are not comparable — a deliberate example of correctly disqualifying a benchmark rather than misapplying it.
