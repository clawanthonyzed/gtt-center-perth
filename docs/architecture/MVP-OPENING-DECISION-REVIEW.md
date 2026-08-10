# Founder Risk Acceptance Review — MVP Opening Decision

**Phase:** Founder Risk Acceptance Review — decision review only. This document determines which MVP cost reductions from `docs/architecture/STARTUP-COST-OPTIMISATION.md` are acceptable, unacceptable, or need further validation, directly addressing `docs/VERIFICATION-TRACKER.md` item 48. **It does not modify `data/canonical/startup_costs.yml`, the funding requirement calculation, or the financial model.** Anthony still needs to sign off on the recommendation below before anything is wired into the canonical layer.

**Date:** 2026-08-10
**Version used as source of truth:** commit `600794b` (Startup Cost Optimisation) and everything it built on.

---

## Executive Summary

This review examined every deferred or compressed item in the MVP Opening scenario (A$243,912) against operational, compliance, customer-experience, and revenue-risk impact. **No compliance or legal requirement was found to be at risk anywhere in the MVP proposal** — that constraint held throughout the prior phase and is confirmed again here. Several items, however, were found to carry real operational or customer-experience risk that the pure cost-minimisation lens of the prior phase did not fully weigh, and are **not recommended for acceptance as originally proposed**.

**The single most important finding is a precise, not a blanket, one:** the venture's own stated "pregnancy modesty is non-negotiable" design principle is about **visual** privacy ("no client sees another client") — and that is **not at risk anywhere in the MVP scenario**, since the privacy curtain systems themselves were never deferred (fully funded in every scenario, unchanged). The item genuinely at risk is a **different, narrower** concern — **conversational/acoustic** privacy in the four curtain-partitioned rooms (Massage 1–2, Facial/Beauty 3–4) — governed by the AMT Massage Code's own practice standard, not the venture's literally-stated visual-modesty principle. This review recommends **Accept with condition**: fund acoustic-rated curtain fabric now (a modest, non-deferrable upgrade to a line item already being purchased), defer the remainder of the full acoustic-treatment package (sound-masking, additional padding) pending real client feedback. See §1 for the full reasoning.

**Revised Recommended Opening Strategy: A$251,198** — A$7,286 above the pure MVP figure (A$243,912), and A$199,296 (~44%) below the Expected Opening figure (A$450,494). This is the lowest-cost opening strategy this review can defend without leaving a genuine, avoidable risk unaddressed.

---

## MVP Assumptions Reviewed — Summary Table

| # | Item | Cost saving vs. Expected | Operational impact | Compliance impact | Customer experience impact | Revenue risk impact | Recommendation |
|---|---|---|---|---|---|---|---|
| 1a | Full acoustic treatment for curtain bays deferred entirely | A$4,874 | Low | None found — AMT Code is a professional-practice standard, not confirmed WA law | **Real** — conversational privacy weakened in Massage/Facial-Beauty rooms | Low-moderate — repeat-visit/word-of-mouth risk if clients feel overheard | **Accept with condition** — see §1 |
| 2 | One-off pre-launch marketing near-eliminated | A$3,000 | Low | None | None | **Real, but not new** — ramp curve's own origin is already undocumented (item 42), unaffected by this specific reduction | **Accept with condition** — see §2 |
| 3a | Receptionist training compressed 3wk→1.5wk | A$1,201 | **Real** — directly contradicts `staff-plan.md`'s own explicit "3 weeks" requirement, no new evidence justifies the change | None directly | **Real** — front-of-house errors in first days | Low-moderate | **Reject** — restore to 3 weeks, see §3 |
| 3b | Venue Manager pre-opening period compressed 8wk→6wk | A$3,124 | **Real, larger than previously assessed** — VM's own start date is the root of the entire downstream hiring cascade (Phlebotomist Wk7, Receptionist/Massage/Nails Wk12, Beauty Wk14, all sequenced FROM VM start per `staff-plan.md` §7) | None directly | Indirect, via cascading hire delays | Moderate — launch-date risk | **Accept with condition** — partial restoration to 7 weeks, see §3 |
| 3c | Treatment staff trial compressed 1wk→4 days | A$1,392 | **Real** — the tightly-choreographed 25-min AM cadence is solver-verified, not simple; `staff-plan.md`/`grace-startup-plan.md` both imply a full "test operations week" | None directly | **Real** — under-rehearsed synchronized schedule risks early-days errors | Moderate | **Accept with condition** — restore to 1 week minimum, see §3 |
| 3d | 3 of 5 recruitment channels shifted to organic/referral | A$1,700 | Low-moderate — real risk if organic sourcing underperforms | None | None | Low | **Accept with condition** — set a fallback checkpoint, see §3 |
| 4a | 2 of 4 nail stations' equipment/furniture deferred | ~A$3,000 | None for AM/Table 1/Table 2 GTT capacity (solver-confirmed) | None | None for AM | **Needs validation** for PM standalone-booking capacity specifically | **Accept, with a ramp-aligned purchase trigger** — see §4 |
| 4b | 2 of 4 hair stations' equipment/furniture deferred | ~A$2,600 | Same as 4a | None | None for AM | Same as 4a | **Accept, with a ramp-aligned purchase trigger** — see §4 |
| 4c | Full professional website build deferred | A$1,200 | Low | None | Low — referral-driven launch doesn't depend on a full site | Low | **Accept** |
| 4d | Professional photography deferred | ~A$1,000 | Low | None | Low | Low | **Accept** |
| 4e | Decorations/branding elements deferred | A$500–2,000 | None | None | Low | None | **Accept** |
| 4f | Nail LEV system — full capacity retained despite staged stations | A$0 change | None — already correctly not staged in the prior phase | None | None | None | **Accept (no change proposed)** |

---

## §1. Privacy and Acoustic Treatment — Highest Priority

### 1.1 The design principle, read precisely

`floor-plan-concept.md`'s Design Principle 3 states: *"Treatment rooms are private — no client sees another client in mid-treatment. Pregnancy modesty is non-negotiable."* This is explicitly a **visual** privacy standard. The document's own Critical Design Requirements section separately specifies the mechanism for meeting it: *"Use a full-length, opaque, lockable-track privacy curtain (curtain cannot be pulled open from outside once closed) as the equivalent privacy mechanism"* for Massage and Facial/Beauty rooms, since only the Blood Collection Room retains solid walls.

**Finding: this visual-privacy requirement is not at risk anywhere in the MVP scenario.** The privacy curtain systems themselves (Category C, `startup-cost-reconstruction.md`) were never deferred, reduced, or downgraded in the optimisation phase — they remain fully funded, at the same specification, in the MVP, Expected, and Full Build scenarios alike. **Can curtains meet the intended patient privacy standard? Yes, for visual privacy, as designed** — a full-length, opaque, lockable-track curtain is a genuine equivalent to a locked door for the specific purpose the design principle states (preventing one client from seeing another).

### 1.2 The item genuinely at risk — acoustic, not visual, privacy

`floor-plan-concept.md`'s own Critical Design Requirements section separately, honestly discloses a different, narrower gap: *"Sound insulation — genuinely weakened by the curtain-partition change, flagged not hidden. Matches AMT Massage Code's 'clinic rooms should be impervious to sound' requirement, which a curtain cannot achieve to the same standard as a solid wall."* `standards-floorplan-crosscheck-2026-07-28.md` confirms the exact source: the AMT (Association of Massage Therapists) Massage Code of Practice's Privacy and Confidentiality standard states *"Clinic rooms should be impervious to sound so that conversations cannot be overheard."* This was assessed as **MEETS directly** when rooms were fully walled (before the 2026-07-31 open-plan/curtain redesign) — the redesign genuinely weakened this specific standard, a real, disclosed trade-off, not newly discovered by this review.

**Important distinction for this decision:** the AMT Code is a professional-body practice standard (relevant to the massage therapists' own professional registration/insurance standing and to genuine client trust), not a WA government legal mandate in the way the Skin Penetration Code is. This does not make it dismissible — massage and facial/beauty treatments routinely involve clients discussing sensitive personal and pregnancy-related health information, and being overheard is a real trust and repeat-visit risk for a wellness venue whose entire value proposition is a restorative, private experience — but it is a different category of requirement than a hard legal mandate, and this review treats it accordingly (a real risk to manage, not an absolute blocker).

### 1.3 Which areas genuinely require acoustic treatment vs. which can use curtains as-is

- **Blood Collection Room:** unaffected by this question entirely — it retains solid walls and its own already-specified sound insulation requirement ("Collection Room must not allow sound to pass to adjacent treatment rooms"), never converted to curtain, never part of the MVP's acoustic deferral.
- **Massage Rooms 1–2, Facial/Beauty Rooms 3–4:** the four curtain-partitioned rooms — this is where the AMT Code gap genuinely applies. **All four**, not a subset — the Code's standard applies to clinic rooms generally, and nothing distinguishes these four rooms' privacy needs from one another.
- **GTT Lounge, Hairdressing Area, Nail Station Area:** open-plan by explicit design, with no privacy expectation ever claimed for these zones (they are shared social/service spaces by intent) — the acoustic question does not apply here at all.

### 1.4 Is partial treatment sufficient? What's the minimum acceptable opening solution?

**Yes — partial treatment is sufficient and is this review's recommendation.** The full "acoustic treatment for curtain bays" line item costed in the optimisation phase (A$4,874) bundles two genuinely different things: (a) **acoustic-rated curtain fabric** — a heavier, sound-dampening curtain material used in place of a standard curtain, which is a modest cost delta on a line item already being purchased regardless (the curtains themselves are non-negotiable and already fully funded); and (b) **additional acoustic mitigation** — ambient sound-masking systems, extra spacing between bays, or supplementary padding, which are real but separable additions.

**Recommendation: fund (a) now, as a condition of accepting the MVP scenario. Defer (b), pending real client feedback in the first 3 months.** Estimated cost of acoustic-rated curtain fabric over standard fabric: **~A$1,350** (≈28% of the full A$4,874 line, a reasonable proportion given fabric/hardware is typically the smaller share of a full acoustic-treatment budget relative to sound-masking systems and structural padding). This is the minimum acceptable opening solution: it does not fully close the AMT Code gap (a curtain, even acoustic-rated, will never equal a solid wall), but it is a genuine, real, non-token improvement over a standard curtain, funded before opening rather than deferred entirely, and proportionate to a professional-practice standard rather than a hard legal mandate.

**Condition attached:** if real client feedback in the first 3 months indicates the acoustic-rated curtain alone is insufficient (e.g., complaints about being overheard, or staff-reported discomfort), the remaining ~A$3,524 sound-masking/padding package should be actioned immediately from early operating revenue, not deferred further.

---

## §2. Launch Marketing Reduction

### 2.1 Minimum viable launch marketing actually required

The venture already has a real, named, zero-cost channel: direct outreach to the specific midwifery/OB-GYN practices and public-sector maternal-child-health contacts listed in `poppy-marketing.md` and `referral-partnership-plan.md`. This review agrees the MVP's shift toward this channel is directionally sound — but "near-eliminated" (A$250) leaves no buffer if the channel underperforms in the critical opening weeks.

### 2.2 Does the revenue ramp curve justify — or get undercut by — reduced marketing spend?

**Answer: neither, precisely — and this is an important distinction to hold onto.** Two separate things must not be conflated:

1. **The ONGOING Month 1–4 marketing ramp** (A$600 → A$800 → A$1,000 → A$1,200 → A$1,500/month, already in `data/canonical/cost_ramp.yml` as an **operating cost**, funded from Month 1 revenue) is **completely untouched by the MVP startup-capital scenario** — it is not a startup-capital line at all, and remains identically funded in MVP, Expected, and Full Build alike. This ramp is what the 43/64/79/93/100% revenue ramp curve's cost side, if it has one at all, would actually correspond to.
2. **The ONE-OFF pre-launch marketing push** the MVP scenario reduced (Category I of the startup-cost taxonomy) was always a **separate, additional** line, disclosed explicitly in the optimisation phase as "distinct from the ongoing Month 1 ramp figure." It was never part of the revenue ramp curve's own embedded cost assumption.

Given `docs/architecture/REVENUE-RAMP-METHODOLOGY.md` itself confirms the 43/64/79/93/100% curve's own origin is genuinely undocumented anywhere in this repo (no external benchmark, referral-pipeline model, or client-acquisition curve is cited — item 42, still open) — **the curve does not "justify" any particular marketing spend level, because no causal mechanism between marketing spend and the curve's shape is stated anywhere in this repository.** The MVP's one-off marketing reduction therefore does not create a *new* mismatch with the ramp assumption that did not already exist — but it also does nothing to *resolve* the pre-existing, still-open uncertainty about whether referral-only demand generation can actually achieve the ramp's implied volumes.

### 2.3 Recommendation

**Accept with condition.** Reduce the one-off pre-launch marketing push, but not to near-zero. Restore a **A$1,000 marketing contingency reserve** — held, not necessarily spent immediately, released only if early bookings underperform. **Condition:** track real Week 1–4 bookings against the ramp's own implied volumes (Table 1 ≈7.74 clients/day at Month 1, Table 2 ≈5.16/day — both already stated in `REVENUE-RAMP-METHODOLOGY.md` §7–8) as an explicit go/no-go trigger for releasing the reserve, rather than waiting passively for a full month to pass.

---

## §3. Staffing Compression

### 3.1 Receptionist onboarding — REJECT the compression

`staff-plan.md` §7 states, explicitly and specifically: *"Receptionist... Train 3 weeks before soft open."* The MVP scenario compressed this to 1.5 weeks with no new evidence offered to justify overriding an existing, specifically-sourced repo requirement — this is exactly the category of change this engagement's own standing rule prohibits ("do not resolve unknowns without evidence," "do not change assumptions without evidence"). **This review rejects the compression and restores the full 3 weeks** (cost: A$2,403, matching the Expected scenario's own figure — Receptionist training was never actually compressed in the Expected/Full Build scenarios, only in MVP). Added cost vs. MVP: **A$1,201**.

### 3.2 Venue Manager pre-opening period — Accept with condition, partial restoration

The prior phase's reasoning (overlap early admin with Anthony directly) is not unreasonable on its own, but this review identifies a **larger, previously under-weighted risk**: the Venue Manager's own start date is the root of the entire downstream hiring cascade. `staff-plan.md` §7's Hiring Timeline sequences every subsequent hire relative to the Venue Manager's own start (Phlebotomist Week 7, Receptionist/Massage/Nails Week 12, Beauty Week 14) — compressing the Venue Manager's start by 2 weeks risks compressing every downstream hire's own available runway too, not just the Venue Manager's own admin buffer. This is a compounding, not merely additive, risk.

**Recommendation: partial restoration to 7 weeks** (not the full original 8, not the MVP's compressed 6) — a defensible middle path. Added cost vs. MVP: **A$1,562**. **Condition:** confirm the two-gate recruitment condition (`staff-plan.md`'s own policy: recruitment does not begin until BOTH a pathology partnership and a physical venue are confirmed) is fully cleared *before* the Venue Manager's clock starts, so no part of the compressed timeline is spent waiting on external gates.

### 3.3 Treatment staff trial — Accept with condition, restore to 1 week minimum

`staff-plan.md` and `grace-startup-plan.md` both frame this period as a "test operations week" (Phase 4, Week 17–18 in the latter) — the 4-day MVP compression falls short of what the source documents themselves already imply. Given the AM schedule this staff must execute is a solver-verified, tightly-choreographed 25-minute cadence (not a simple walk-in service), and given the full committed 8-person headcount is trained in every scenario (§0 correction from the prior phase, unchanged), **this review recommends restoring the trial period to a minimum of 1 week.** Added cost vs. MVP: **A$1,392**.

### 3.4 Recruitment channel mix — Accept with condition

Shifting Massage, Nails, and Beauty/Brows recruitment to organic/referral-network channels (already-named professional networks in `reed-partnerships.md`) is a low-risk, reasonable optimisation — it costs nothing extra to attempt, and paid advertising remains available as a fallback. **Recommendation: accept, with an explicit checkpoint** — if no qualified candidate is identified via organic channels by a defined point ahead of the role's needed start date, fall back to paid advertising immediately rather than waiting indefinitely and risking a late scramble. No cost change from MVP's existing figure.

---

## §4. Deferred Equipment/Furniture

### 4.1 Does staged purchasing affect Table 1/Table 2 client capacity from Day 1?

**No — confirmed, not assumed.** `equipment-costs.md`'s own solver-verified finding (independently re-confirmed by this review, not re-derived) is that peak concurrent AM demand for both Nails and Hair is exactly 2 technicians at committed volume, for **both** Table 1 (18/day) and Table 2 (12/day) — station count above 2 provides rostering flexibility and PM standalone-booking capacity, not AM/GTT throughput. **The core committed revenue capacity this venture's financial model depends on is unaffected by staging 2 of 4 nail/hair stations.**

### 4.2 What does create a genuine, unresolved question

The extra stations are explicitly described in `equipment-costs.md` as also providing **PM standalone-booking capacity** — a separate revenue stream from AM GTT revenue. No solver analysis exists anywhere in this repository specifically testing whether 2 stations suffice for **PM** concurrent demand (only the AM peak-concurrency question was solved). `pm-staffing-roster.md`'s own PM volume assumption (16 sessions/day combined across all treatment types at Month 5+ steady state, itself only ~50% of theoretical 4-line capacity) suggests 2 stations is *likely* adequate even for PM throughput, since total PM demand is well below theoretical maximum and spread across sequential (not necessarily simultaneous) bookings — but this is a reasoned inference, not a confirmed solver result, and this review does not present it as one.

### 4.3 Recommendation — Accept, with a ramp-aligned purchase trigger, not a fixed calendar date

**Accept staging 2 of 4 nail/hair stations for the opening period**, but attach a more precise condition than the prior phase's vague "3–6 months": **tie the stations 3–4 purchase to the already-modelled PM revenue ramp itself**, not an arbitrary calendar window. The revenue ramp reaches 93% of steady-state PM volume by Month 4 and 100% by Month 5 (`REVENUE-RAMP-METHODOLOGY.md` §7–8) — **stations 3–4 for both Nails and Hair should be purchased and installed by Month 4**, ahead of PM volume reaching its steady-state level, rather than left to an unanchored "3–6 months" placeholder. This directly ties a deferred-equipment decision to evidence already inside this venture's own financial model, rather than an independent guess.

### 4.4 Website, photography, decorations — Accept as proposed

These carry low operational and customer-experience risk, and were already reasonably scoped in the prior phase — no change recommended.

### 4.5 Nail LEV system — Accept, no change proposed

The prior phase already correctly identified the LEV extraction system as not stageable (a shared system typically sized/installed once during fit-out) and retained full capacity even in MVP. This review confirms that reasoning and proposes no change.

---

## Revised Recommended Opening Strategy

Applying every "Accept with condition" restoration above to the MVP baseline:

| Adjustment | Amount |
|---|---|
| MVP baseline (Categories A–J subtotal) | A$217,779 |
| + Acoustic-rated curtain fabric (§1.4) | +A$1,350 |
| + Marketing contingency reserve (§2.3) | +A$1,000 |
| + Receptionist training restored to 3 weeks (§3.1) | +A$1,201 |
| + Venue Manager restored to 7 weeks (§3.2) | +A$1,562 |
| + Treatment staff trial restored to 1 week (§3.3) | +A$1,392 |
| **Revised subtotal (A–J)** | **A$224,284** |
| Contingency (12%, unchanged rationale from the optimisation phase) | A$26,914 |
| **REVISED RECOMMENDED OPENING STRATEGY — TOTAL** | **A$251,198** |

**Comparison across all four figures:**

| Scenario | Total | vs. MVP | vs. Expected |
|---|---|---|---|
| Minimum Viable Opening (prior phase, unmodified) | A$243,912 | — | -45.9% |
| **Revised Recommended Opening Strategy (this review)** | **A$251,198** | **+A$7,286 (+3.0%)** | **-44.2%** |
| Expected Opening | A$450,494 | +84.7% | — |
| Full Build | A$644,832 | +164.4% | +43.2% |

This answers the question this review was asked to answer: **the lowest-cost opening strategy that still protects the GTT customer experience and operational viability is A$251,198** — a genuine A$199,296 saving against the Expected scenario, achieved by accepting every low-risk MVP deferral (staged equipment, deferred photography/website/decorations, organic recruitment) while restoring the small number of items where the pure cost-minimisation lens of the prior phase created real, avoidable customer-experience or operational risk (acoustic treatment, receptionist training, treatment-staff rehearsal time, and the Venue Manager's cascading start date).

### Funding requirement reconciliation (informational only, not adopted this phase)

Adding the untouched Working Capital Reserve (A$85,000–110,000): the Revised Recommended Opening Strategy brackets to **A$336,198–361,198** — very close to, and in the low-reserve case slightly below, the existing bounded range's low end (A$357,390). This is a more conservative, better-evidenced improvement claim than the pure MVP figure's (~A$28,478 reduction), reflecting this review's decision to restore several genuinely risk-bearing items rather than accept every deferral at face value.

---

## Accepted, Rejected, and Conditional Reductions — Summary

**Accepted as proposed (no change):** deferred professional photography, deferred full website build, deferred decorations/branding, organic recruitment channel shift (with checkpoint condition), staged 2-of-4 nail/hair stations for the opening period (with ramp-aligned purchase trigger), retained full LEV capacity.

**Accepted with condition (partial restoration, cost added):** acoustic treatment (fund acoustic-rated curtain fabric now, +A$1,350), launch marketing (restore a A$1,000 reserve), Venue Manager pre-opening period (restore to 7 weeks, +A$1,562), treatment staff trial (restore to 1 week, +A$1,392).

**Rejected (full restoration):** Receptionist training compression — restored to the full 3 weeks `staff-plan.md` already specifies, +A$1,201.

**No item in this review required a genuinely new "Needs venue validation" classification held open indefinitely** — the one candidate for that category (PM standalone-booking capacity at 2 stations, §4.2) was resolved into an "Accept, with a ramp-aligned purchase trigger" recommendation instead, since sufficient evidence already exists in this repo's own PM volume modelling to make a reasoned, disclosed judgement rather than leaving the question fully open.

---

## Tracker Item 48 — Status Update

**Updated from OPEN to IN PROGRESS.** This review provides the founder-facing risk analysis item 48 called for, with an explicit recommendation (A$251,198, the Revised Recommended Opening Strategy above) — but **Anthony's own sign-off has not yet occurred**, so the item is not marked RESOLVED. Status remains open for Anthony's explicit acceptance or override of: the acoustic-treatment partial-fund decision (§1.4), the marketing reserve amount (§2.3), the three staffing-timeline restorations (§3.1–3.3), and the ramp-aligned equipment purchase trigger (§4.3).

---

## Validation — Confirmed No Model Changes Occurred

- `git status --short` before this phase: clean.
- File created this phase: `docs/architecture/MVP-OPENING-DECISION-REVIEW.md`. `docs/VERIFICATION-TRACKER.md` item 48 updated (status change only, from OPEN to IN PROGRESS, with this document's findings appended).
- Full pytest suite: **114 passed**, 0 failed.
- `tools/validate_canonical_data.py`: **13 files checked, 0 errors, 27 warnings** — identical to every prior phase.
- `tools/check_consistency.py`: **0 findings** — identical to every prior phase.
- `git diff --stat` against `data/canonical/`, `data/models/`, and `tools/*.py`: zero changes.
- `data/canonical/startup_costs.yml` was **not modified**. The funding requirement calculation and the financial model were **not touched**.

## Recommended Next Step

Anthony reviews this document's recommendation directly and either (a) accepts the Revised Recommended Opening Strategy (A$251,198) and its attached conditions as the new planning basis, in which case a future, separately-authorised phase would wire the accepted figure into `data/canonical/startup_costs.yml` alongside (not replacing) the existing historical ranges, or (b) overrides specific recommendations in this document, in which case the figure would be recalculated accordingly before any canonical update is considered.
