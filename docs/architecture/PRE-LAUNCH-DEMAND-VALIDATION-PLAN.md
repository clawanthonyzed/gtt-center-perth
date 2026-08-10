# Pre-Launch Demand Validation Plan

**Phase:** Pre-Launch Validation — moving from internal planning into actual evidence collection before committing to a venue. **No financial/startup-cost/revenue model change made or requested this phase.** No WDP communication drafted or sent — tracker item 50 remains untouched. Builds directly on `docs/architecture/AM-STAFFING-RAMP-OPTIMISATION.md` (the Month 1 volume/break-even figures) and `docs/architecture/EARLY-DEMAND-VALIDATION-STRATEGY.md` (waitlist conversion as the primary Month 1 lever) — this document makes those findings decision-usable with a concrete, checkable threshold.

**Date:** 2026-08-10

---

## 1. The Target — Derived From Already-Canonical Figures, Not Invented

`docs/architecture/AM-STAFFING-RAMP-OPTIMISATION.md` established two real numbers: Month 1's canonical implied AM volume (**7.74 clients/day**, Table 1) and the AM-segment break-even band (**7.2–8.4 clients/day**, depending on which staffing configuration is confirmed). Converting to a whole-month total using the canonical operating-days figure (22 weekdays + 4.33 Saturdays = 26.33 days/month, `data/canonical/client_assumptions.yml`):

| Basis | Clients/day | Total AM clients across Month 1 |
|---|---|---|
| Break-even, low bound (7-staff option, unverified) | 7.2 | **190** |
| Canonical implied Month 1 (Table 1 ramp) | 7.74 | **204** |
| Break-even, high bound (8-staff, status quo) | 8.4 | **221** |

**This is the number Month 1 actually needs to hit — not an abstract "build a big waitlist" goal, but a specific total this document works backward from.**

---

## 2. Converting the Target Into a Waitlist Number — Assumptions Explicit, Not Hidden as Fact

**This venture has zero trading history — any conversion rate used here is a generic, non-GTT-specific planning assumption, not evidenced data. Flagged as such throughout, not presented as fact.**

Two genuinely unknown inputs are needed: (a) what share of Month 1 volume the pre-launch waitlist is expected to supply (vs. early referral trickle, launch-week organic reach, and paid marketing); (b) what share of waitlist signups actually convert to a real Month 1 booking. Neither has any repo-sourced or evidenced figure — both are presented as scenario ranges, not single numbers.

**Waitlist share of Month 1 volume:** scenarios at 50%, 65%, and 80% — reflecting `docs/architecture/EARLY-DEMAND-VALIDATION-STRATEGY.md`'s own finding that waitlist conversion is the primary, not sole, Month 1 lever.

**Conversion rate (waitlist signup → actual Month 1 booking):** scenarios at 10%, 20%, and 30% — generic small-business/service-launch planning ranges, not sourced to this venture or this repo in any way.

### Waitlist size needed, by scenario (using the mid target — 204 total clients, 7.74/day canonical implied Month 1):

| Waitlist share of Month 1 volume | Bookings needed from waitlist | At 10% conversion | At 20% conversion | At 30% conversion |
|---|---|---|---|---|
| 50% | 102 | 1,019 | 509 | 340 |
| **65% (primary planning case)** | **132** | **1,325** | **662** | **442** |
| 80% | 163 | 1,630 | 815 | 543 |

*(Full sensitivity across the break-even low/high bounds, not just the mid target, is available on request — the mid-target table above is the primary planning reference.)*

---

## 3. A Genuine, Important Finding — the Existing "300+" Waitlist Reference Is Likely Insufficient

`docs/business-plan.md` §8 references an unverified target of "300+ waitlist names before opening." Tested directly against the target above: **300 signups at even a generous 30% conversion rate produces only ~90 bookings — well short of the 190-221 total clients Month 1 needs**, and materially short of the 65%-share planning case's own 442-bookings-needed-from-waitlist figure at the same conversion rate. **This does not mean 300 is wrong as a number someone once used — it means it was never tested against the current (post-2026-08-05-rebase) Month 1 volume target, and does not hold up when tested now.** Flagged plainly, not smoothed over.

**Recommended planning range for the pre-lease evaluation checkpoint (§5): 500-700 waitlist signups**, corresponding to the 20% conversion / 65% waitlist-share planning case (662, rounded to a workable range) — presented as a reasoned planning midpoint, not a proven number, and explicitly subject to revision the moment real conversion data exists (see §6).

---

## 4. Target Customer Acquisition Channels

Directly reused from `docs/architecture/EARLY-DEMAND-VALIDATION-STRATEGY.md`, not re-derived — this document adds the checkable threshold, that document supplies the channel strategy:

- **Primary (Month 1 lever): direct-to-consumer waitlist**, via Instagram content and referral-card distribution, per `docs/brand-guide.md` §6 and `docs/poppy-marketing.md` §6.
- **Secondary (Month 2+ contributor, started early, not counted on for Month 1): midwife/OB-GYN referral outreach** — 22 named private practices already identified (12 midwifery, 10 OB/GYN, `docs/poppy-marketing.md` §1), none yet contacted.
- **Tertiary: community partnerships** (pregnancy photographers, prenatal yoga, maternity retail) and MCH nurse contacts — both flagged in the source document as needing a light research pass before outreach.

---

## 5. Timeline — Cross-Referenced Against the Existing Week-Based Schedule

`docs/grace-startup-plan.md`'s FINANCIAL GATES / Phase structure currently sequences waitlist-building AFTER lease signing (Week 9-10 lease, Week 9-10 "Set up Instagram and Facebook accounts"). **This document recommends inverting that sequence for the demand-validation purpose specifically:** a lightweight, address-agnostic "coming soon" waitlist presence (Instagram + a simple landing page, using the existing placeholder brand per `docs/brand-guide.md`'s own explicit "usable as working material" status) should begin **before** lease commitment, not after — since the entire purpose of this phase is evidence collection ahead of that capital commitment. This is a sequencing recommendation only; it does not change any dollar figure or the FINANCIAL GATES table itself.

| Stage | Timing (relative) | Action |
|---|---|---|
| Pre-lease validation window | Begins as soon as this plan is actioned, run for a defined evaluation period (recommend minimum 8-12 weeks to gather a meaningful signal) | Lightweight waitlist/interest capture, address-agnostic, no venue commitment implied to signups |
| Go/no-go checkpoint | End of the pre-lease validation window | Evaluate against §6's criteria |
| Lease signing (if go) | Existing Week 9-10 per `docs/grace-startup-plan.md` | Unchanged sequencing from here |
| Fit-out waitlist continuation | Week 9-20 | Existing plan continues — real venue-specific content, referral outreach begins in earnest (venue confirmed, per `docs/referral-partnership-plan.md`'s own gating condition) |
| Soft launch | Week 19 | Waitlist converts to real bookings, per `docs/grace-startup-plan.md` |

---

## 6. Measurable Go/No-Go Criteria — Concrete, Checkable, Not Vague

**GATE 1 — Demand signal:** pre-lease waitlist signups ≥ **500** (minimum) to **700** (comfortable), tracked via the actual landing page/Instagram funnel, by the end of the evaluation window (§5). **If tracking below 500 with no clear upward trend, this is a genuine signal to extend the validation window before committing to a lease, not a hard stop** — 500 is a planning threshold built on unevidenced conversion assumptions (§2), not a proven cutoff.

**GATE 2 — Referral engagement (a leading indicator, not a Month 1 volume source):** positive engagement (a response indicating willingness to refer, not just a delivered message) from at least **3-5 of the 22 named practices** (`docs/poppy-marketing.md` §1) contacted during the validation window. A low bar deliberately — `docs/architecture/EARLY-DEMAND-VALIDATION-STRATEGY.md` already establishes clinical referral relationships are a Month 2+ lever, not a Month 1 one; this gate exists to confirm the channel is viable at all, not to hit a volume target through it yet.

**GATE 3 — Dependency readiness (cross-referenced, not re-derived):** accountant engagement scheduled or underway (`docs/architecture/EXTERNAL-READINESS-REVIEW.md` — Ready with conditions), proof-of-funds documentation prepared (`docs/architecture/VENUE-ACQUISITION-READINESS-PACKAGE.md` §2, this phase), and WDP's commercial figure/room-spec dependency status unchanged or improved (`docs/VERIFICATION-TRACKER.md` items 1c, 49 — cross-referenced, not touched this phase).

**NO-GO condition:** if, at the end of the evaluation window, Gate 1 is materially below 500 (e.g. under 300, the same figure this document already found insufficient) **and** Gate 2 shows minimal engagement, the recommendation is to extend the validation window and/or revisit the committed volume scenario (Table 1 vs. Table 2, `docs/VERIFICATION-TRACKER.md` item 1m, still open) before signing a lease — not to proceed on the existing schedule regardless.

**This document does not itself decide go or no-go** — it defines the thresholds Anthony would check against once real data exists.

---

## Validation

No canonical YAML, financial model, or revenue/cost methodology was modified by this document. Every target figure is derived transparently from already-canonical data; every conversion/share assumption is explicitly flagged as a generic, unevidenced planning input, not fact (see full validation summary in this phase's combined report-back).
