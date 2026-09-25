# GTT Center Perth — Financial Forensics: Reconstructing Real Economics From Fragments

**Created:** 2026-09-25 (Round 2, deeper pass) | **Author:** Grace (Operations Manager)
**Purpose:** Per the founder's explicit instruction — where no single public source discloses full day-spa/wellness economics, combine real fragments (rent, revenue, staffing, pricing, utilisation) from multiple independent sources into estimated ratios, clearly ranged and tagged, and cross-check them against GTT Center Perth's own modelled figures. This is deliberately a pressure-test document: it looks for contradictions between real external evidence and this venture's own assumptions, not just confirmations.

**Tagging convention used throughout:** `[VERIFIED]` = confirmed by a named real source, `[REPORTED]` = stated by a source without independent audit, `[BENCHMARK]` = an industry-wide figure from a commercial/consultant source, `[ESTIMATE]` = this document's own arithmetic combining two or more real fragments, `[ASSUMPTION]` = a planning figure this venture has already adopted, `[UNKNOWN]` = genuinely not found.

---

## 1. Rent-to-Revenue Ratio — A Real Contradiction Worth Flagging

**GTT Center Perth's own modelled figures:**
- Rent: A$8,000/month, A$96,000/year, based on 200sqm at A$40/sqm/month in Subiaco/Nedlands `[ASSUMPTION — docs/rent-budget-2026-07-28.md, no signed lease]`
- Current canonical Table 1 revenue: A$143,070.37/month, A$1,716,844.44/year `[CALCULATED — docs/CURRENT-STATE.md §5, 2026-09-19 Founder Decision round]`
- **Implied rent-to-revenue ratio: ~5.6%** `[ESTIMATE — this document's own arithmetic: 96,000 / 1,716,844.44]`

**Real external fragment found this round:** the South Perth day spa/beauty/skin business-for-sale listing (`docs/research/CASE-STUDY-DATABASE.md` Case 5) discloses turnover ~A$5,500/week (~A$286,000/year) and rent ~A$1,334/week (~A$69,368/year) `[REPORTED — real business-for-sale listing, Tier 3]` — **an implied rent-to-revenue ratio of ~24.2%** `[ESTIMATE — this document's own arithmetic: 69,368 / 286,000]`.

**The contradiction, stated plainly:** GTT Center Perth's own modelled rent-to-revenue ratio (~5.6%) is roughly **4x lower** than the one real, current, comparable Perth day-spa data point found this round (~24.2%). Two genuinely different explanations are both plausible, and this document does not pick one:
1. **GTT Center Perth's revenue-per-square-metre assumption is materially higher than a typical single-service Perth day spa**, because it combines a high-throughput pathology collection component (18 AM clients/day, a fundamentally different volume driver to a standard day spa) with a materially larger multi-service PM offering (4 treatment rooms + 4 nail stations + 4 hair stations) in the same footprint — i.e., GTT Center Perth may genuinely earn more revenue per square metre than a typical day spa, which would make a lower rent-to-revenue ratio a real feature of the model, not an error.
2. **GTT Center Perth's A$40/sqm/month rent assumption may be understated for a 200sqm premium commercial space in Subiaco/Nedlands specifically** — this figure has never been checked against a real current Perth commercial-lease listing in this venture's own documents (flagged as `[VERIFICATION NEEDED]` in `docs/rent-budget-2026-07-28.md` itself already, this document does not newly discover that gap, only quantifies how large the resulting ratio discrepancy could be if the rent assumption is too low).

**Recommendation, not a decision:** when a specific venue candidate is identified (the current #1 blocking gate per `docs/risk-register.md`), sanity-check the actual quoted rent against both this venture's own A$40/sqm/month planning assumption and the ~24% rent-to-revenue ratio found in this real comparable listing — if the real revenue ramp undershoots the committed model in the first 1-2 years (a genuine, already-flagged open risk, `docs/CURRENT-STATE.md`'s PM ramp-validation item), a rent commitment sized against the optimistic 5.6% ratio rather than the real-world 24% comparable could leave less margin for error than currently assumed. This is a pressure-test finding for awareness, not a reason to change the locked A$8,000/month planning figure before a real lease exists.

---

## 2. Labour Cost as a Percentage of Revenue — A Genuine Validation, Not a Contradiction

**GTT Center Perth's own modelled figures (Table 1, current, 2026-09-19):**
- Total Direct Labor + Opening Costs: A$82,318.05/month `[CALCULATED — docs/CURRENT-STATE.md §5]`
- Total Revenue: A$143,070.37/month `[CALCULATED — same source]`
- **Implied labour-cost-as-percentage-of-revenue: ~57.5%** `[ESTIMATE — this document's own arithmetic: 82,318.05 / 143,070.37]`

**Real external benchmark found this round:** multiple independent spa-industry commercial sources (Vagaro, Optimantra, industry KPI trackers) converge on labour representing **40-60% of spa department revenue**, with some sources citing a narrower 50-60% band as "the biggest cost driver" `[BENCHMARK — Tier 4, commercial sources, directionally consistent across multiple independent sources rather than a single claim]`.

**Finding: GTT Center Perth's own modelled labour percentage (~57.5%) sits comfortably within, and toward the higher end of, this real industry benchmark range — this is a genuine validation of the existing financial model, not a contradiction.** This is a meaningful cross-check because this venture's labour figure was built entirely bottom-up (position-by-position, first-principles, `docs/architecture/FIRST-PRINCIPLES-FINANCIAL-MODEL.md`) with no reference anywhere in its own derivation to this external industry ratio — the fact that it independently lands inside the real benchmark band is reassuring evidence the bottom-up build is realistic, not a coincidence to be dismissed.

---

## 3. Room/Session Utilisation — A Partial Validation With One Open Flag

**GTT Center Perth's own modelled figures:**
- PM segment capacity utilisation: "~50% utilisation of theoretical 4-line capacity" `[ASSUMPTION — docs/CURRENT-STATE.md §3, explicitly stated as "no real demand data exists yet"]`

**Real external benchmark found this round:** ISPA (International Spa Association) data on full-service hotel spas shows treatment-room utilisation of **50-65%** `[BENCHMARK — Tier 2/3, ISPA is a genuine industry body, though the specific figure could not be traced to a current, dated primary ISPA publication this round — see the note below]`; a separate commercial source cites a "75-80% sweet spot" as the target band, with above 85% flagged as over-stretched `[BENCHMARK — Tier 4, different source, not reconciled with the ISPA figure]`.

**Finding: GTT Center Perth's own ~50% PM utilisation assumption sits at the very bottom edge of the ISPA 50-65% band, and below the alternative 75-80% "sweet spot" figure.** This is not a contradiction requiring action — it is arguably a **conservative, defensible planning assumption** (safer to under-plan utilisation pre-launch than over-plan it), consistent with this venture's own explicit statement that it has no real demand data yet. It does mean there may be real, currently unmodelled upside if PM utilisation tracks toward the middle or top of the real industry range once trading begins — a genuine, evidence-based opportunity to flag for the PM ramp-validation review already scheduled once real booking data exists (`docs/CURRENT-STATE.md`'s existing open item), not a new decision needed now.

**Data-quality caveat, disclosed rather than hidden:** a search this round specifically for the ISPA figure's primary source found that "the only per-treatment-room figure ISPA has published is from 2004" (per a secondary source's own honest disclosure) — i.e., the commonly-cited "50-65%" and "$52,163 per treatment room" figures trace back to a **20+ year old** ISPA data point, not a current one. The 50-65% band is used here only as a rough directional cross-check, not treated as a precise or current authority.

---

## 4. Single-Service Salon Resale Multiples vs Multi-Service Day-Spa Multiples — A New, Specific Finding

**Real fragments combined from `docs/research/CASE-STUDY-DATABASE.md` Cases 5-6:**
- Multi-service/branded day-spa sector (general): reported valuation multiples of **1.4x-3.5x SDE** for independent operator-run businesses, up to 2.78x+ for spas earning over A$800K/year `[BENCHMARK — Tier 3, BizBuySell/CT Acquisitions valuation-multiple research]`
- 8 real single-service hair/beauty salon listings found this round (Campbelltown, Sydney South, Inner West Sydney, South West Sydney, Cronulla, Tweed Heads, Ingleburn, Brisbane): asking prices consistently **A$55,000-A$200,000**, with the two listings disclosing a profit figure showing an **implied multiple of roughly 1.0-1.4x annual profit** `[ESTIMATE — this document's own arithmetic from real disclosed EBITDA/profit and asking-price pairs]`

**Finding, genuinely new this round:** single-service salons (hair-only or beauty-only) appear to trade at a materially lower multiple than the broader "day spa" sector average, even accounting for the wide range in the day-spa figure. **This is directional support, from an independent financial-forensics angle, for GTT Center Perth's own multi-service (massage + beauty + nails + hair, all under one roof) design choice** — not because GTT Center Perth is being built to be resold, but because a business model that commands a higher exit multiple in this specific industry is also generally evidence of a more resilient, less single-point-of-failure revenue base while trading, which is directly relevant to this venture's own risk profile.

---

## 5. What Could Not Be Reconstructed, Disclosed Rather Than Guessed

- **Revenue per available AM chair-hour specifically for a pathology-collection-plus-wellness model** — no source (Australian or international) discloses this combined figure; GTT Center Perth's own solver-verified capacity model (`docs/scenario-c-sync-timetables.md`) remains the only real basis for this figure, and this document does not attempt to manufacture an external comparison where none exists.
- **A precise, current (not 20-year-old) per-treatment-room revenue benchmark** — genuinely not found; flagged in Section 3 above rather than substituted with the stale 2004 figure presented as current.
- **PathWest/WDP/Clinipath's own internal cost-per-collection or margin-per-referred-test economics** — as already found in `docs/research/PATHOLOGY-OPERATIONS-DEEP-DIVE.md` §2, this is commercially sensitive information no pathology company publishes anywhere, and no fragment-reconstruction approach can substitute for it; direct negotiation (already underway with WDP) remains the only real path to this specific number.

---

## Sources

All source citations for the real fragments used in this document are in `docs/research/CASE-STUDY-DATABASE.md` (Cases 5, 6) and `docs/research/PATHOLOGY-OPERATIONS-DEEP-DIVE.md` §1, cross-referenced rather than repeated here. GTT Center Perth's own figures are cited directly to `docs/CURRENT-STATE.md` and `docs/rent-budget-2026-07-28.md` throughout.

---

## Changelog

**2026-09-25 (Round 2, created):** New file, built specifically in response to the founder's instruction to reconstruct economics from fragments where no single source discloses them, and to deliberately hunt for contradictions rather than only confirmations. Found one genuine, material contradiction worth flagging (rent-to-revenue ratio, Section 1), one genuine validation (labour percentage, Section 2), one partial validation with a data-quality caveat disclosed (utilisation, Section 3), and one new supporting finding for an existing design choice (multi-service resale multiples, Section 4). No locked figure changed; all findings presented as evidence for awareness or future venue-specific verification.
