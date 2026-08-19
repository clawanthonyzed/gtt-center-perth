# 18-Client/Day Commercial + Capacity Stress Test

**Date:** 2026-08-14 | **Status:** Current. Single analysis document, per instruction. Builds on the accepted operational stress test (`docs/strategy/18-CLIENT-OPERATIONAL-STRESS-TEST.md`) to ask the commercial question: does 18 GTT clients/day make money, and does it stay premium while doing so. Every figure below is sourced to `data/canonical/` or `data/models/master_financial_model.yml` — nothing here recalculates the model with a new methodology, and no financial-model file, pricing document, or the business plan is modified.

**Locked rules treated as settled, not re-litigated:** 18 clients/day is the design target, 12/day is the downside case only. Every AM service is 45 minutes or less, absolute, no exceptions. PM standard bookings begin at 12:30; 12:00-12:30 is a soft transition, not a closure.

---

## 1. GTT Economics at 18/Day

Sourced directly from `data/models/master_financial_model.yml`'s `scenario_table_1` outputs — the canonical (days-based) methodology, per `docs/architecture/CANONICAL-REVENUE-METHODOLOGY.md`.

| Line | Value | Status |
|---|---|---|
| AM revenue (monthly) | **A$118,485.00** | CALCULATED, canonical |
| PM revenue (monthly) | **A$36,730.80** | CALCULATED, canonical |
| **Total revenue (monthly)** | **A$155,215.80** | CALCULATED, canonical |
| Net operating result (monthly, includes 12% superannuation) | **+A$56,581.70** | CALCULATED, canonical, recalculated 2026-08-09 |
| Annualised net operating result (steady state) | **A$678,980.40** | CALCULATED |
| 24-month total net operating result | **A$1,172,971.91** | CALCULATED |
| Break-even monthly revenue | A$98,632.63 | CALCULATED |
| Break-even AM client volume | 9.404 clients/day | CALCULATED |
| Margin of safety | 8.596 clients/day (~48% of the 18-client target) | CALCULATED |

**AM revenue, derived from already-canonical unit facts (not a new calculation methodology):** 18 clients/day × A$250 (Package 1, the deliberate conservative-floor price used for all revenue calculations, `pricing.yml#am_price_used_for_revenue`) = **A$4,500/weekday**, before Saturday's separately-scaled contribution. The real Package 1/Package 2 mix is unknown (`client_assumptions.yml#service_mix_am_package_split`, PLACEHOLDER) — every canonical revenue figure in this repository already prices AM conservatively low, meaning real AM revenue could be higher than shown here if clients choose Package 2 (A$300) at any real rate, never lower.

**A genuine, disclosed conflict — not silently resolved:** this repository carries two different Total Revenue figures for Table 1, and two different Net P&L figures, from two different methodologies:

| | Canonical (current) | Historical/inherited (superseded) | Gap |
|---|---|---|---|
| Total Revenue (monthly) | A$155,215.80 | A$157,792.16 | A$2,576.36, origin unresolved per `docs/VERIFICATION-TRACKER.md` item 36 |
| Net P&L (monthly) | A$56,581.70 (includes superannuation) | A$63,028.75 (does not include superannuation) | Not the same figure for two disclosed reasons: different revenue base, and superannuation was never in the historical figure at all |

This document uses the **canonical** figures throughout (A$155,215.80 revenue / A$56,581.70 net result) as instructed. Where the historical figure (A$63,028.75) is referenced elsewhere in this repository's other strategy documents, that is the older, superseded methodology — not a contradiction of this document, a disclosed and already-logged conflict.

---

## 2. AM Service Economics

Stress-tested against three uptake scenarios, using only real, already-priced, VERIFIED add-ons from `data/canonical/services.yml` — nothing invented. Every AM add-on listed there is already 10-25 minutes, sits inside the 45-minute ceiling with room to spare in most cases, and is delivered by the same staff member already booked for the base service (no extra headcount implied).

**Scenario A — Minimal AM uptake:** clients take the base package only (Package 1's fixed 2×30min, or Package 2's chosen composition), no add-ons. Revenue is exactly the AM package price already modelled in §1 — no additional revenue, no additional operational load.

**Scenario B — Moderate AM uptake:** roughly one add-on per client on one of their two service slots (e.g. a facial + LED therapy add-on, A$35, or a manicure + paraffin wax, A$30). At 18 clients/day, illustrative additional revenue = 18 × ~A$30 (a representative mid-range add-on price) × 22 days ≈ **A$11,880/month**, explicitly illustrative, not a forecast — no uptake-rate assumption exists in this repository to make this a real modelled figure (§15, item 2).

**Scenario C — High AM uptake:** two or more stacked add-ons per client where duration allows (e.g. a 30-minute facial plus two 10-15 minute add-ons, still inside the 45-minute slot). Illustrative additional revenue roughly doubles Scenario B's, but this is where the schedule's fixed 10-minute buffer becomes the real constraint, not the 45-minute ceiling itself — see below.

**Does AM add-on uptake create operational pressure?** Per `docs/strategy/18-CLIENT-OPERATIONAL-STRESS-TEST.md` §8, the schedule's *timing* is invariant to service selection — the clock doesn't change whether a client takes zero or three add-ons, provided the total fits inside 45 minutes. The real risk under Scenario C is **pacing**, not throughput: the same fixed 10-minute buffer has to absorb a more complex, multi-step service regardless of how many add-ons were stacked into it, which is a soft, staff-experienced pressure rather than a scheduling failure. **Verdict: AM add-ons enhance the proposition (real, already-priced upside, delivered by staff already on the clock) without threatening the 18-client throughput — but Scenario C specifically should be watched for staff pacing feedback, not just revenue upside, once real bookings exist.**

**A genuine, currently-missing control:** nothing in the booking system validates that a chosen base service plus its add-ons stays under 45 minutes at time of booking — flagged in the operational stress test, restated here because it's exactly the mechanism Scenario C depends on holding.

---

## 3. PM Capacity at 12:30

Using existing canonical capacity figures — none invented, one clearly-labelled illustrative adjustment made explicit below.

| Figure | Value | Status |
|---|---|---|
| PM theoretical maximum capacity (4-line, unconstrained, back-to-back) | 31 sessions/day | MODELLED |
| PM current planning capacity | 16 sessions/day | MODELLED, "no real demand data exists yet" |
| PM utilisation implied by the planning figure | 51.6% (16/31) | CALCULATED |
| PM Saturday sessions | 8 sessions/day | MODELLED |

**A disclosed gap this stress test surfaces, not previously flagged anywhere in the repository:** both the 31-session theoretical ceiling and the 16-session planning figure were built against a PM operating window that predates the founder's 12:30 PM-start decision — the source documents describe PM as 12:00-18:00 (6 hours), not the now-locked 12:30-18:00 (5.5 hours). Proportionally rescaling (5.5/6 = 91.7%) gives an **illustrative** theoretical ceiling of ~28 sessions/day and an **illustrative** planning capacity of ~14-15 sessions/day. `[MODELED — illustrative proportional scaling only, not a new canonical figure; the real fix is for the model owner to recompute both figures against the new 12:30 start]`.

**Utilisation required to materially contribute to profitability:** PM's canonical monthly revenue (A$36,730.80) is already what's driving roughly a quarter of Table 1's total modelled revenue (A$36,730.80 / A$155,215.80 ≈ 23.7%) at the current 16-session/day (or ~51.6%) planning assumption — PM is already material to the model as it stands, not a rounding error. It does not need to approach its theoretical ceiling to matter; it already does at less than 52% utilisation of its own theoretical maximum.

---

## 4. PM Service Mix

Drawn directly from `data/canonical/services.yml`'s real, priced PM catalogue — no menu finalised here, every price cited is already VERIFIED or MODELLED in the canonical layer, none invented.

| Duration | Real examples (price) | Commercial character |
|---|---|---|
| 30 min | Classic manicure (A$55), express pedicure (A$55), express facial, short blowdry | **High-frequency** — short natural repeat cycle, low-commitment first-booking candidates |
| 45 min | Standard massage (A$120), signature facial (A$130), gel manicure (A$75), gel pedicure (A$80) | **High-frequency + margin potential** — the AM package's own two "strongest perceived value" services, equally strong standalone |
| 60 min | Cut+blowdry (A$95), full massage (A$145), hydration facial (A$145), single-process colour (A$130-200) | **Repeat-capable, higher AOV** |
| 75 min | Signature facial-75 (A$175), belly cast + painted finish (A$310) | **Premium/hero-tier candidates** |
| 80-90 min | Mani+pedi combo (A$140), half foil highlights (A$200, price conflict disclosed in `services.yml`), classic lash extensions (A$140) | **Destination services** — longer commitment, lower frequency, higher single-visit value |
| 120+ min | Full foil highlights (A$280-350), balayage full head (A$360-400), hybrid/volume lash extensions (A$200-280) | **Hero/destination services** — the highest single-transaction value in the whole catalogue, genuinely long-duration, low-frequency |

**Proposed, explicitly labelled as proposed, not decided:**
- **High-frequency backbone:** manicure/pedicure and blowdry (30-45min) — these are the natural candidates for the first AM→PM conversion booking (§5), consistent with `docs/strategy/OPERATING-COMMERCIAL-ARCHITECTURE.md` §7.3's reasoning.
- **Margin-potential candidates:** brow/lash/nail add-ons generally carry lower material cost relative to price than colour or extension services — a directional read of the price/duration table, not a modelled margin figure (no cost-of-goods data exists in this repository for any service).
- **Premium/hero services:** the signature facial (75min), balayage, and lash extensions — long enough and priced high enough to be genuinely "destination" bookings, the kind of service that anchors a woman's choice to return specifically for that appointment.
- **Repeat services:** manicure/pedicure, blowdry, standard massage — short natural cycles.
- **Longer destination services:** hair colour, balayage, lash extensions, belly casting — infrequent but high single-visit value.

A real, disclosed data-quality note: `services.yml` itself flags several PM prices as unresolved conflicts across source documents (hybrid lash infill: A$120 vs A$125; several hair colour prices differ by A$20-30 between `services-pricing-locked.md` and `extended-wellness-services.md`) — not resolved here, cited as-is.

---

## 5. AM→PM Conversion — Sensitivity, Not a Forecast

Per instruction, no conversion rate is asserted as real. The structure below multiplies three already-canonical inputs — 18 clients/day, 22 trading days/month (the convention already used throughout `docs/CURRENT-STATE.md`), and the PM a-la-carte average (A$95/session) — against illustrative conversion rates.

**AM visit volume:** 18 × 22 = 396 visits/month (matches `docs/CURRENT-STATE.md` §3's own AM capacity ceiling figure exactly — a genuine internal consistency check, not a new number).

| Conversion rate | Converted PM sessions/month | Illustrative additional PM revenue/month | Status |
|---|---|---|---|
| 0% | 0 | A$0 | Baseline — no flywheel effect assumed |
| 5% | ~19.8 | ~A$1,881 | **Sensitivity scenario, not a forecast** |
| 10% | ~39.6 | ~A$3,762 | **Sensitivity scenario, not a forecast** |
| 15% | ~59.4 | ~A$5,643 | **Sensitivity scenario, not a forecast** |
| 20% | ~79.2 | ~A$7,524 | **Sensitivity scenario, not a forecast** |
| 25% | ~99.0 | ~A$9,405 | **Sensitivity scenario, not a forecast** |

**A real capacity tension this sensitivity model surfaces, not previously connected anywhere in this repository:** at the higher end (20-25%), converted volume alone (79-99 sessions/month) is a meaningful fraction of the existing ~352-session/month PM planning capacity (16/day × 22 days) — meaning a genuinely successful flywheel would need to be checked against whether it's *additive* to the current PM baseline or already partially embedded within the existing, undifferentiated 16-session/day planning assumption. **The current PM revenue figure does not distinguish organic PM demand from AM-converted demand at all** — this is the same data-capture gap flagged in `docs/strategy/OPERATING-COMMERCIAL-ARCHITECTURE.md` §8/§15, restated here because it directly limits how much confidence can be placed in any of the sensitivity figures above as *incremental* revenue.

---

## 6. Customer Lifetime Value — Conceptual Model, Missing Inputs Named

| Customer type | Revenue shown | Basis |
|---|---|---|
| GTT-only customer | A$250 (Package 1 floor) — up to A$300 (Package 2) | Already-canonical AM pricing |
| GTT + one PM visit | A$250 + A$95 (a-la-carte average) = **A$345**, or A$250 + a PM package (A$144 PM Duo / A$153 PM Glow / A$225 PM Refresh) = **A$394-475** | Already-canonical AM + PM pricing, no new assumption |
| GTT + recurring PM customer | **Cannot be computed — see missing inputs below** | — |

**Missing inputs, named rather than guessed at, per instruction:**
- **Repeat-visit frequency** (how many PM visits per year a converted customer makes) — does not exist anywhere in this repository.
- **Customer tenure/churn** (how many years a converted customer keeps booking before stopping) — does not exist.
- **Service-mix evolution over time** (does a repeat customer trend toward higher-value services, packages, or stay at the initial a-la-carte level) — does not exist.
- **AM→PM conversion rate itself** (§5) — the gating input before any of the above can even be applied to a cohort.

**Why this matters economically, even unquantified:** the simple two-row comparison above already shows a GTT-only customer is worth a fixed, one-time A$250-300, while a single PM conversion adds 38-90% more revenue from the same acquisition event (referral pipeline cost is already sunk once she's in the building). A *recurring* PM customer compounds that multiple times per year, for multiple years — the return loop's entire economic argument (`docs/experience/RETURN-LOOP.md`) rests on this compounding effect being real, but this document cannot quantify it without the four missing inputs above. This is precisely why §15 ranks AM→PM conversion data collection as a top commercial risk, not a nice-to-have.

---

## 7. Customer Experience vs. Utilisation

Cross-referencing `docs/strategy/18-CLIENT-OPERATIONAL-STRESS-TEST.md` rather than re-deriving: the operational stress test already found the schedule has genuine built-in slack (a 20-minute phlebotomist idle window, treatment staff fully free 10-20 minutes before the last draw, ~50% spare room/station capacity at peak) and that PM's own planning assumption already runs at only ~51.6% of its theoretical ceiling.

**This is not incidental — it's the model's actual operating philosophy, made explicit here for the first time:** the business is not designed to run near 100% utilisation anywhere. The AM side has slack built into every buffer; the PM side is planned at roughly half its theoretical capacity. Pushing either toward its ceiling would directly threaten the calm, unhurried standard the founder has set (§12 of the operational stress test) and would very likely require *additional* staff to sustain safely, undermining the "same headcount at 12 or 18/day" finding that currently makes 18/day cost-neutral.

**Target utilisation philosophy, stated directly:** sufficient utilisation to sit comfortably above break-even with a real margin of safety (§1's ~48% margin), without compressing the AM schedule's built-in buffers or pushing PM meaningfully past its current ~50% planning assumption. **Profitable, premium, and repeatable is the objective — not maximum throughput.**

---

## 8. 18 Clients — Downside Case (12/Day)

Both figures are already fully canonical — no interpolation needed.

| | Table 1 (18/day, target) | Table 2 (12/day, downside) | Difference |
|---|---|---|---|
| AM revenue (monthly) | A$118,485.00 | A$78,990.00 | -A$39,495.00 |
| PM revenue (monthly) | A$36,730.80 | A$36,730.80 | **No difference — see note below** |
| Total revenue (monthly) | A$155,215.80 | A$115,720.80 | -A$39,495.00 |
| Net operating result (monthly) | +A$56,581.70 | +A$21,056.64 | -A$35,525.06 |
| Annualised net operating result | A$678,980.40 | A$252,679.68 | -A$426,300.72 |
| Treatment/phlebotomist headcount | 8 + 2 | 8 + 2 (identical) | No staffing cost difference |
| Break-even AM client volume | 9.404/day | 8.801/day | Table 2's break-even volume is nearly as high in absolute terms |
| **Margin of safety (% of own target)** | **~48% (8.596 of 18)** | **~27% (3.199 of 12)** | **Table 2 is structurally less resilient, not more** |

**Note on PM revenue being identical across both scenarios:** this is a direct consequence of §5/§6's flagged gap — PM revenue is currently modelled as entirely decoupled from AM client volume in this repository's canonical layer. This is convenient for a downside comparison (PM doesn't degrade if AM volume falls) but it's an assumption, not a proven fact — real PM demand may partially depend on AM-driven foot traffic and word-of-mouth, in which case a genuine AM downside would likely drag PM down somewhat too, an interaction this model does not currently capture.

**The non-obvious finding worth stating plainly:** because treatment/phlebotomist headcount doesn't change between 12 and 18 clients/day, the *same* fixed labor cost is spread across a larger revenue base at 18/day — which is exactly why Table 1's margin of safety (~48%) is nearly double Table 2's (~27%), even though Table 2 is the "safer-sounding," lower-volume scenario. **The 18-client design target is not just more revenue — it is structurally more resilient than 12/day**, precisely because of the headcount-neutrality finding already established in the operational stress test. This document does not recommend changing the design target (already locked); it demonstrates why the target the founder chose is the financially sounder one on the evidence, not merely the more ambitious one.

---

## 9. Break-Even / Resilience

- **Approximate GTT utilisation required to cover the existing fixed structure:** 9.404 clients/day at Table 1's cost base — **52.2% of the 18-client target**. This is the single most important resilience number in this document: the business does not need anywhere near full 18-client bookings to survive.
- **Impact of lower GTT utilisation:** per §8's sensitivity table (`master_financial_model.yml#sensitivity_client_volume`), 50% of committed volume (9/day) already produces a small **loss** (-A$2,660.80/month) — consistent with the 9.404/day break-even figure above (9/day sits just below break-even). 75% of committed volume (13.5/day) is solidly profitable (+A$26,960.45/month). The business is loss-making only in a genuinely severe under-booking scenario (below ~52% of target), and comfortably profitable well before reaching full capacity.
- **How PM revenue changes resilience:** because PM revenue is currently modelled as AM-volume-independent (§8's flagged gap), it acts as a real financial floor under every AM scenario in this model — A$36,730.80/month exists in the P&L regardless of how many GTT clients are actually booked, as currently modelled. This makes PM look like a stabiliser by construction. Whether that holds in reality depends entirely on the untested assumption above.
- **Is PM a meaningful stabiliser or merely incremental?** Both, simultaneously, and this document does not pick one: it is a real ~24% share of total modelled revenue (§3) and a genuine buffer against AM under-booking *as currently modelled* — but the model's own decoupling of PM from AM volume is itself unvalidated, so PM's true stabilising power in a real downside is unknown, not proven.

---

## 10. Top 5 Commercial Risks

Determined from the evidence in this document, not assumed in advance:

| # | Risk | Evidence | Financial consequence | Operational consequence | What needs validation | When |
|---|---|---|---|---|---|---|
| 1 | Real GTT referral-volume fill rate against the 18/day target | Only one pathology partner (WDP) is in active dialogue; PathWest/Clinipath remain unreplied-to (`docs/strategy/STRATEGIC-REPORT.md` §4). Break-even sits at 52.2% of target (§9), so this is the single largest swing factor in the entire model. | The whole revenue range in §8/§9's sensitivity table hinges on this | Referral pipeline maturity directly determines real daily volume | Real, sustained booking data once operating; interim proxy: confirmed referring-practice count and their stated volume | Immediately, ongoing — this is the top blocking item across every strategic document produced so far |
| 2 | AM package mix (Package 1 vs Package 2) is entirely unknown | `client_assumptions.yml#service_mix_am_package_split` is PLACEHOLDER; every canonical figure uses the conservative Package 1 floor | Real AM revenue could be materially higher than shown here, but this is an upside risk (unvalidated, not a downside) | None | Real booking-mix data | Once bookings open |
| 3 | AM→PM conversion is entirely unvalidated, and current PM revenue doesn't distinguish organic from converted demand | §5, §6 — no conversion rate, no CLV inputs exist anywhere | The entire "PM as retention engine" economic thesis is currently invisible in the P&L | The flywheel mechanism (`docs/experience/RETURN-LOOP.md`) may or may not be working — no way to tell without new data capture | Booking-system-level AM→PM client linking (flagged repeatedly, not yet built) | Should begin capturing from Day 1, even before real conversion data exists |
| 4 | PM utilisation/service-mix assumption is itself a planning estimate with no real demand data | `pm-staffing-roster.md`'s own "no real demand data exists yet" caveat on the 16-session/50% figure; PM package revenue explicitly excluded from every current revenue figure pending real uptake | PM's true revenue could be meaningfully higher (packages) or lower (if 51.6% utilisation doesn't materialise) than modelled | Staffing levels are built around this planning assumption | Real PM booking volume and package uptake once operating | Post-launch, ongoing |
| 5 | Real, current wage rates and insurance costs are stale/underestimated | `docs/VERIFICATION-TRACKER.md` items 17-19 — wage rates 13+ months stale and internally contradictory; insurance modelled at A$400/month vs an itemised A$500-916.66/month range | Insurance sensitivity alone moves Table 1's net result by ~0.9% and Table 2's by ~2.45% (`master_financial_model.yml#sensitivity_insurance`) — real wage-rate correction could be materially larger and is not yet quantified | None directly, but every margin-of-safety figure in this document is built on these rates | 3 real insurance quotes; a real wage-rate/award-penalty check — both flagged as cheap, fast fixes in prior strategic reports | Before any funding conversation, ideally now |

---

## 11. What We Should NOT Optimise For

Explicit, not implied:

- **Maximum room/station utilisation.** §7 and the operational stress test both show the model's real strength is its built-in slack, not tight packing — pushing rooms/stations toward their peak-concurrency ceiling threatens the calm-and-personal standard for no proven financial gain, since headcount (the actual cost driver) doesn't change either way.
- **Maximum appointment count beyond 18/day.** The 18-client target is already the headcount-neutral ceiling (§8's finding) — going beyond it would require new staff, breaking the exact cost-neutrality that makes 18/day attractive in the first place.
- **Maximum AM add-on stacking (Scenario C, §2) as a default sales push.** Real, priced upside exists, but treating "stack every add-on" as a target risks the pacing pressure flagged in §2, for revenue that isn't even quantified as a real assumption yet.
- **Maximum PM occupancy toward its ~28-31 session theoretical ceiling.** PM is already materially contributing to revenue at roughly half that ceiling (§3, §7) — chasing the ceiling is chasing a number the model doesn't need to hit, at direct cost to the calm PM experience the return-loop thesis depends on.
- **Aggressive same-visit AM upselling.** Already flagged in `docs/experience/RETURN-LOOP.md`: upselling during the clinical visit itself undoes trust at exactly the point it's being built — the add-on revenue in §2 should be offered, not pushed, and never at the cost of the departure experience the whole flywheel depends on (see `CUSTOMER-JOURNEY.md`'s Departure Experience stage — the specific mechanism there is still an open design question, not yet solved).

---

## 12. Scale Test

Not a national model — a classification of which parts of this commercial architecture travel and which don't, extending `docs/strategy/OPERATING-COMMERCIAL-ARCHITECTURE.md` §14's replicability framework with this document's commercial specifics.

**Location-specific:** real local wage rates and award interpretation; local lease/fit-out cost; local GTT referral-volume market size; and — the single biggest scale dependency, already flagged in the operating architecture — a local NATA-accredited pathology partner willing to run an equivalent rental-collection arrangement to WDP's, which is not guaranteed to exist on comparable terms in every target city.

**Scalable/standardisable:** the headcount-to-client-volume ratio itself (8 treatment + 2 phlebotomists holds flat across a 12-18 client range at this venue's configuration — a genuinely transferable operating fact, not a Perth-specific coincidence); the 45-minute AM ceiling and its underlying "clock-invariant to service selection" property (§2); the 12:30 PM-start logic and its rationale (a natural schedule lull, not an arbitrary Perth choice); the AM/PM decoupled-but-linked commercial structure itself (core + secondary + retention engine); the break-even-as-%-of-target framing (§9) as a standard resilience check for any future site's own volume target.

**Dependent on local demand:** the real AM→PM conversion rate (§5) may vary by market and needs local data, not an assumed constant; PM's organic (non-GTT-driven) demand will depend on local competitive density and brand awareness, unlike the AM side which is referral-gated by design everywhere.

**What the flagship must prove before this scale test means anything:** real (not modelled) AM fill-rate against 18/day, a real (not assumed) AM→PM conversion signal, and confirmation that a local pathology partnership on WDP-equivalent terms is achievable — all three are prerequisites this document's numbers assume, not facts this document has established.

---

## 13. Final Verdict

**1. Is 18 GTT clients/day commercially viable under the current model?** Yes, on the canonical figures: +A$56,581.70/month net operating result, break-even at just 52.2% of the target volume, and a ~48% margin of safety — the strongest resilience position of any scenario modelled in this repository.

**2. How much does AM service uptake potentially add?** A real, already-priced revenue line (individual add-ons A$15-45 each) with no operational throughput cost within the 45-minute ceiling — illustratively several thousand dollars/month at moderate uptake (§2), though no real uptake-rate assumption exists yet to convert this into a forecast.

**3. How important could PM realistically become?** Already material as modelled — roughly 24% of total revenue at only ~51.6% of its own theoretical capacity (§3, §7) — with real, unexploited headroom if package uptake or utilisation increases, though neither is currently validated.

**4. What AM→PM conversion rate would make a material difference?** Not determinable with confidence from this repository's current data (§5, §6) — the sensitivity table shows even a modest 10-15% conversion adds meaningful incremental revenue (~A$3,700-5,600/month, illustrative only), but the more important finding is that the current model can't tell whether any of that is already happening inside the existing PM baseline or would be genuinely new.

**5. What is the biggest commercial uncertainty?** Real GTT referral-volume fill rate against the 18/day target (§10, risk #1) — every other figure in this document is downstream of actual bookings materialising, and the referral pipeline is the least mature input in the whole venture.

**6. What data do we need to validate before committing significant capital?** Real referring-practice commitments and early booking signals; AM package-mix data; AM→PM linked booking data (requires building the capability first, not just collecting it); real current wage rates and insurance quotes (§10, risk #5) — the cheapest and fastest of these to close.

**7. Does the 12:30 PM opening create a commercially acceptable balance?** Yes — it costs only 30 minutes of PM capacity relative to a 12:00 opening (§3's capacity table shows the delta is modest, ~2 of ~22-24 theoretical staff-hours) while resolving the single reception-role congestion risk the operational stress test identified as the actual bottleneck, not room or staff capacity.

**8. Does the business remain attractive if GTT utilisation is materially below 18/day?** Yes, down to roughly 52% of target (§9) before the model turns unprofitable — and even the 12-client downside scenario remains solidly profitable (+A$21,056.64/month), just with a structurally thinner margin of safety than the 18-client target (§8).

**9. What should we optimise first?** Closing the AM→PM data-capture gap (§5, §6, §10 risk #3) — it's the one input that would let this document's most speculative section (CLV, conversion) become a real, evidence-based number, and it costs nothing to start building before real customers exist.

**10. What should we deliberately NOT optimise?** Utilisation itself, in any dimension — room, PM occupancy, add-on stacking, or same-visit upselling (§11). The model's real financial strength comes from its resilience margin and headcount-neutral capacity, not from running any part of the business near its ceiling.

---

## How the 18-Client Flagship Makes Money Without Sacrificing the Experience

Working backward from that question, the evidence in this document converges on one answer: **it doesn't need to run near capacity anywhere to be highly profitable.** AM headcount is fixed regardless of volume between 12 and 18 clients/day, so the 18-client target is pure operating leverage on an already-committed cost base — the same money buys more revenue, not more risk. PM is already materially contributing at roughly half its theoretical ceiling, meaning there's real headroom to grow PM's contribution through service mix and package uptake without ever crowding the calm, spacious standard the brand depends on. And the business survives a genuine downside (52% of target) without becoming unprofitable, which means neither AM nor PM has to be pushed hard on any single day to protect the year's numbers. The actual commercial risk isn't in the schedule or the unit economics — both are sound, on paper — it's in the two things this document could not quantify: whether real referral volume shows up, and whether the AM→PM flywheel is real. Both are data questions, not design questions, and both can start being answered without spending a dollar more than what's already committed.
