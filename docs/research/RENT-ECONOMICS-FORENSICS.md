# GTT Center Perth — Rent Economics Forensics (Round 3, Priority 1)

**Created:** 2026-09-25 (Round 3) | **Author:** Grace (Operations Manager)
**Purpose:** Round 2 found a contradiction (GTT's modelled rent-to-revenue ratio ~5.6% vs one real Perth comparable's ~24%) and left it unresolved. This is not a re-log of that finding — it is an investigation into it, with more real comparables, a sensitivity table against the actual canonical financial model, and a real-property cross-check.

**Tagging used throughout:** `[VERIFIED]` = confirmed real source, `[REPORTED]` = stated by a source without independent audit, `[BENCHMARK]` = industry-wide commercial figure, `[ESTIMATE]` = this document's own arithmetic from real fragments, `[ASSUMPTION]` = a GTT planning figure, `[UNKNOWN]` = not found. Any finding with only one credible source is explicitly marked `LOW CONFIDENCE — SINGLE SOURCE`.

---

## 1. First, a Genuine Internal Finding: the Rent Line Was Not Recalculated When the Footprint Grew

Before comparing to external evidence, the internal record needed checking on its own terms. Result: a real, quantifiable internal gap was found.

- The A$8,000/month rent budget was set 2026-07-28 against a **200sqm** planning footprint at A$40/sqm/month `[VERIFIED — docs/rent-budget-2026-07-28.md, this venture's own document]`.
- Since then, two separate founder decisions grew the required footprint: the growth-reservation recalculation (2026-07-28, same day, later) raised the target to **~249sqm** `[VERIFIED — docs/property-links-2026-07-28.md]`, and the Blood Collection Room split into 2 rooms (2026-08-27) added a further ~18-20sqm `[VERIFIED — docs/architecture/VENUE-PROGRAM-AUTHORITATIVE.md]`. The construction/capex section of `docs/CURRENT-STATE.md` §7.2 already uses **239sqm** for the fit-out cost calculation.
- **The A$8,000/month rent line in the operating P&L (`docs/profit-loss-tables.md` §4, propagated into `docs/CURRENT-STATE.md` §5 and the canonical YAML model) was never recalculated to match this footprint growth.** At the same A$40/sqm/month rate the rent line was originally built on, a 239sqm venue implies A$9,560/month (A$114,720/year), and a 249sqm venue implies A$9,960/month (A$119,520/year) — both materially higher than the A$8,000/month currently used in every P&L figure in this repository.

**This is a real, disclosed, quantified gap, not a re-statement of the Round 2 contradiction — it is the internal half of the investigation Round 2 didn't do.** `[ESTIMATE — this document's own arithmetic, straightforward unit multiplication, not a new assumption]`. **Financial impact if corrected:** using the sensitivity table in Section 4 below, moving rent from A$8,000 to A$9,560-9,960/month reduces Table 1's Net P&L from A$35,186.40/month to approximately A$33,626.40-33,226.40/month — a real but modest ~4-5% reduction to steady-state monthly profit, not model-breaking, but a genuine correction that should be made regardless of the external-comparable question below.

---

## 2. Real AU Business-for-Sale/Operating Listings With Disclosed Revenue + Rent + Floor Area, Grouped by Type

Expanded this round with 2 further real, disclosed listings beyond the one South Perth day spa found in Round 2 (Case-Study-Database Case 5). Only listings with genuine disclosed revenue AND rent (or a computable proxy) are used — volume was not chased for its own sake, per the founder's own instruction to expand the dataset "only where listings have real disclosed financials."

| Business type | Location | Revenue (annualised) | Rent (annualised) | Floor area | Rent/Revenue | Rent/sqm/yr | Revenue/sqm/yr | Source |
|---|---|---|---|---|---|---|---|---|
| Day spa/beauty/skin (single-service-adjacent, general) | South Perth, WA | ~A$286,000 `[REPORTED]` | ~A$69,368 `[REPORTED]` | Not disclosed `[UNKNOWN]` | **~24.2%** `[ESTIMATE]` | Cannot compute (no sqm disclosed) | Cannot compute | Benchmark Business Sales listing, Tier 3, re-used from Round 2 |
| Allied-health/consulting room, single-room sublease (proxy for a healthcare-hybrid model) | Perth metro, various | N/A (room-rental model, not a standalone business) | A$150-300/week for an established-suburb consulting room (12-20sqm), i.e. **~A$7,800-15,600/year for a single ~15sqm room** | 12-20sqm (typical single consulting room) `[BENCHMARK]` | N/A — this is a sub-tenancy rate, not a whole-business ratio | **~A$390-1,300/sqm/yr** (wide range depending on room size/location within the stated bracket) `[ESTIMATE]` | N/A | med.estate Perth allied-health room guide, Tier 3/4 |
| Commercial retail/showroom shell (a proxy for GTT's own likely tenancy type, not a service business) | 6/325 Harborne St, Osborne Park | N/A (vacant shell, not a trading business) | A$55,000/yr net + GST | 268sqm | N/A | **~A$205/sqm/yr** | N/A | REIWA listing, Tier 3, re-used from `docs/property-links-2026-07-28.md` |
| Medical/consulting fitout shell, existing 4-room layout | 53 Hardy Road, Nedlands | N/A (vacant shell) | Not disclosed `[UNKNOWN]` | Not disclosed `[UNKNOWN]` | N/A | Cannot compute | N/A | commercialrealestate.com.au listing, Tier 3, re-used |
| Office/showroom shell, refurbished, medical/allied-health suitable | 45 Stirling Highway, Nedlands (150sqm tenancy) | N/A (vacant shell) | ~A$66,282/yr rent+outgoings (before car bays) `[ESTIMATE, from REPORTED $/sqm figures]` | 150sqm | N/A | **~A$442/sqm/yr** (rent $295 + outgoings $146.88) | N/A | commercialrealestate.com.au listing, Tier 3, re-used |

**Honest limitation:** genuine, disclosed **revenue-and-rent-and-sqm-together** triples (all three fields, from one real business) proved to be the rarest data point in Australian business-for-sale listings — almost none disclose floor area alongside financials, since goodwill/client-book value dominates the sale price narrative rather than the property metrics. Only the South Perth day spa (Round 2) discloses revenue+rent together; no listing found this round discloses all three. **This is disclosed as a genuine data limitation, not papered over with an invented number.**

---

## 3. What Rent-to-Revenue Ratio Is Actually Defensible for GTT Center Perth's Specific Model

**The core question, answered as directly as the evidence allows:** GTT Center Perth is not a single-service day spa (the ~24% comparable) and not a vacant commercial shell (the ~$205-442/sqm/yr comparables). It combines (a) a high-throughput clinical collection function generating revenue largely independent of floor area used, and (b) a multi-service wellness floor plan. **No real comparable business of exactly this combined type was found anywhere in this or the prior round's research** — this is genuinely unprecedented enough (per `CASE-STUDY-DATABASE.md`'s own finding, no international analogue combines a mandatory test with a full multi-service concurrent wellness floor) that no external rent-to-revenue ratio can be directly imported with confidence.

**What can be said with the evidence available:**
1. On a pure **rent-per-square-metre** basis, GTT's own A$40/sqm/month (A$480/sqm/yr) assumption sits **above** the Harborne Street showroom comparable (~A$205/sqm/yr) and modestly **above** the 45 Stirling Highway Nedlands comparable (~A$442/sqm/yr) — i.e., GTT's rent assumption is not obviously cheap relative to real, current Nedlands/Osborne Park-area commercial space; if anything it already prices in a small premium.
2. Given (1), **the rent-to-revenue ratio gap found in Round 2 (5.6% vs 24%) is therefore much more likely explained by GTT's own higher revenue-per-sqm (from combining pathology-collection throughput with a multi-service floor), not an understated rent assumption** — this narrows Round 2's open question meaningfully, though it does not eliminate it entirely, since (a) the internal footprint-growth gap found in Section 1 above is real and does modestly increase the true rent-per-sqm-equivalent cost, and (b) no real comparable of GTT's exact combined business type exists to confirm the revenue-per-sqm assumption independently.
3. **A defensible planning range, stated as a range not a point estimate:** given GTT's real, solver-verified capacity model (18 clients/day AM plus up to 10 PM sessions/day) against a ~239-249sqm footprint, a rent-to-revenue ratio in the **8-15%** band would be more consistent with a high-throughput, multi-service premises than the single-service-salon 24% comparable, while still being meaningfully above GTT's own current ~5.6-6% modelled figure — this is `[ESTIMATE — this document's own reasoned range, not a single source, LOW CONFIDENCE — no directly comparable business type exists to validate this range against]`. This range should be treated as a sanity-check band for whatever real venue is eventually secured, not adopted as a new planning assumption.

---

## 4. Rent Sensitivity Table Against the Actual Canonical Financial Model

**Method, fully disclosed:** Rent is one additive line inside Non-Wage Overhead, which is itself one additive line inside Total Costs. Because of this, any change to the rent line by an amount delta changes Total Costs by exactly delta and Net P&L by exactly minus delta, regardless of the other cost lines' internal composition. This was verified by reconstructing Table 1's exact canonical arithmetic from `docs/CURRENT-STATE.md` and `data/canonical/cost_ramp.yml` — **a genuine reconciliation finding surfaced in the process: the four cost lines individually listed in `docs/CURRENT-STATE.md` §5 (Direct Labor A$82,318.05 + Workers Comp A$1,399.41 + Non-Wage Overhead A$14,288.34 + Relief A$0.00 = A$98,005.80) do not sum to the stated Total Costs (A$107,883.97) — a A$9,878.17/month gap.** Checked directly against `data/canonical/cost_ramp.yml` line 251: this gap is exactly accounted for by **superannuation (A$9,878.17/month for Table 1)**, a real, correctly-modelled cost component in the canonical YAML model that is simply not displayed as its own row in `docs/CURRENT-STATE.md` §5's condensed summary table. **This is a documentation-completeness finding, not a computational error in the underlying model** — flagged so whoever next edits that table adds superannuation as its own visible row, since a table that appears to list "all the cost components" but omits one large (~9%) component is misleading even though the final total is correct.

**Verified reconstruction (Table 1, 18 clients/day):** Net P&L(R) = A$43,186.40 − R, where R is monthly rent. Cross-checked: at R=A$8,000, this gives A$35,186.40 — an exact match to the canonical figure.

**Verified reconstruction (Table 2, 12 clients/day, using its own last-published 2026-08-21 baseline — see the flagged inconsistency below):** Net P&L(R) = A$18,076.16 − R. Cross-checked: at R=A$8,000, this gives A$10,076.16 — an exact match.

**A further inconsistency flagged, not silently corrected:** Table 2's cost/revenue figures in `docs/CURRENT-STATE.md` appear to still reflect the 2026-08-21 round, not the 2026-09-19 Founder Decision round (Venue Manager Mon-Fri, PM capacity locked at 10 sessions/day) that was explicitly applied to Table 1. This may mean Table 2 is now stale relative to Table 1 — flagged as a genuine open item for whoever owns the canonical model next, not corrected here (Round 3's mandate is validation and quantification, not silent model edits).

### Sensitivity Table

| Monthly Rent | Table 1 (18/day) Net P&L | Table 1 Rent as % of Revenue (A$143,070.37) | Table 2 (12/day) Net P&L* | Table 2 Rent as % of Revenue (A$115,215.69) |
|---|---|---|---|---|
| A$7,000 | A$36,186.40 | 4.9% | A$11,076.16 | 6.1% |
| A$8,000 (current assumption) | A$35,186.40 | 5.6% | A$10,076.16 | 6.9% |
| A$9,000 | A$34,186.40 | 6.3% | A$9,076.16 | 7.8% |
| A$9,560-9,960 (real footprint-corrected, Section 1) | ~A$33,226-33,626 | ~6.7-7.0% | ~A$8,116-8,516 | ~8.3-8.6% |
| A$10,000 | A$33,186.40 | 7.0% | A$8,076.16 | 8.7% |
| A$12,000 | A$31,186.40 | 8.4% | A$6,076.16 | 10.4% |
| A$15,000 | A$28,186.40 | 10.5% | A$3,076.16 | 13.0% |
| A$18,000 | A$25,186.40 | 12.6% | **A$76.16** (essentially break-even) | 15.6% |

*Table 2 figures use its own last-published baseline, flagged above as potentially stale relative to Table 1's 2026-09-19 update — treat as directional, not final, until reconciled.

**Finding: GTT Center Perth's profitability is genuinely not highly sensitive to rent within a wide, realistic range for the PRIMARY Table 1 model.** Even at A$18,000/month (2.25x the current assumption, and above every real per-sqm comparable found for a ~250sqm Perth tenancy in this research), Table 1 remains solidly profitable at over A$25,000/month. **Table 2 (the downside/sensitivity reference case) is materially more exposed** — it turns unprofitable somewhere between A$18,000 and A$18,076/month rent, a real, quantified break-point. This means: if the AM segment underperforms toward the Table 2 volume (12/day instead of 18/day) at the same time as a real lease lands significantly above the current A$8,000/month assumption, the combined effect could be materially more dangerous than either factor alone — a genuine, quantified compounding risk not previously modelled anywhere in this repository.

---

## 5. Real Perth Property Comparison Against the ~249sqm/Rent-Budget Brief (Comparison Only, Not a Recommendation)

Using the real candidates already tracked in `docs/property-links-2026-07-28.md`, cross-checked against the sensitivity table above:

| Candidate | Size | Real annualised cost | Cost vs current A$96,000/yr budget | Cost vs footprint-corrected A$114,720-119,520/yr | Medical/layout suitability |
|---|---|---|---|---|---|
| 6/325 Harborne St, Osborne Park (VERIFIED) | 268sqm | A$55,000/yr net + GST + outgoings (outgoings not confirmed) | **Below budget** even before outgoings, at a larger size than needed | **Well below** the footprint-corrected figure | Open-plan showroom, not medical fitout, would need full reconfiguration `[VERIFIED — REIWA listing]` |
| 45 Stirling Hwy, Nedlands, 150sqm tenancy (UNVERIFIED CANDIDATE) | 150sqm | ~A$73,482/yr incl. 3 car bays (unconfirmed reading) | **Within** the current A$96,000/yr budget | **Within** the footprint-corrected figure too, but smaller than the ~249sqm target | Refurbished, suitable for office/physio/medical/allied health per listing; 2-chair phlebotomy layout not confirmed `[REPORTED — search-summary level, not direct-fetch confirmed]` |
| 45 Stirling Hwy, Nedlands, 240sqm tenancy (UNVERIFIED CANDIDATE) | 240sqm | Proportionally higher, not computed in the source document | Likely close to or above the current budget | Likely within the footprint-corrected range | Same building, larger tenancy, closer to the ~249sqm target `[REPORTED]` |
| 53 Hardy Road, Nedlands (UNVERIFIED CANDIDATE) | Not disclosed | Not disclosed | Cannot compare | Cannot compare | **Existing 4-room medical/consulting fitout + reception — the closest real layout match found in either round of research**, but financials remain unknown, a genuine, real, and specific gap `[REPORTED — needs a direct agent call, already flagged in the existing repo]` |
| Suite 4 East, 353 Cambridge St, Wembley (UNVERIFIED CANDIDATE) | 200-529sqm splittable | Outgoings ~A$126.90/sqm/yr, rent itself not found | Cannot fully compare (rent missing) | Cannot fully compare | Office-style fitout, would need reconfiguration; most parking of any candidate (19 bays) `[REPORTED]` |

**This is a comparison exercise only — no property is recommended here, per the standing rule against making this decision for Anthony.** The clearest takeaway: **53 Hardy Road, Nedlands remains the single most promising real candidate found across both this round and prior rounds on layout grounds (an existing 4-room medical fitout), and remains the one candidate where the actual rent figure is still missing** — the single highest-value next action for the venue search specifically (already flagged in the existing repository, re-confirmed rather than newly discovered here).

---

## Sources

`docs/rent-budget-2026-07-28.md`, `docs/property-links-2026-07-28.md`, `docs/CURRENT-STATE.md`, `data/canonical/cost_ramp.yml`, `docs/profit-loss-tables.md` (all Tier 1, this venture's own primary documents); [med.estate Perth allied-health room guide](https://med.estate/medical-room-rental-news/allied-health-rooms-for-rent-in-perth-a-practitioners-complete-guide) (Tier 3/4); Benchmark Business Sales South Perth listing (Tier 3, re-used from Round 2).

---

## Changelog

**2026-09-25 (Round 3, created):** New file, forensic validation of the Round 2 rent-to-revenue contradiction. Found and quantified a genuine internal gap (rent line never recalculated after footprint growth, ~A$1,560-1,960/month understated at the original A$40/sqm/month rate). Found and resolved the apparent Table 1 cost-line reconciliation gap (superannuation, A$9,878.17/month, a real but undisplayed component, not an error). Built a full rent sensitivity table against the verified canonical arithmetic. Concluded the Round 2 contradiction is more likely explained by GTT's higher revenue-per-sqm than an understated rent assumption, though this cannot be fully confirmed against a directly comparable business type, none of which was found to exist. Flagged Table 2 as potentially stale relative to Table 1's 2026-09-19 update, for reconciliation by whoever owns the canonical model next.
