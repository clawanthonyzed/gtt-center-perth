# GTT Center Perth — Pricing & Billing Strategy

**Version:** 1.0 | **Date:** 2026-07-19 (Phase 7 new deliverable)
**Purpose:** Private billing vs bulk billing vs hybrid model and rationale, referencing `services-pricing-locked.md`. **Medicare billing specifics are flagged as "requires verification" throughout — none of the below should be treated as settled Medicare policy or billing advice.**

---

## Two Separate Billing Streams — Do Not Conflate Them

GTT Center Perth's revenue model has two entirely separate billing streams that must not be confused with each other:

1. **The pathology/GTT test itself** — billed by the pathology partner (WDP priority, PathWest/Clinipath contingency), not by GTT Center Perth. GTT Center Perth earns zero revenue from this stream (`pathology-partnership-brief.md`: "GTT Center Perth earns zero from pathology billing. All revenue comes from packages and services.")
2. **The wellness package (Package 1/2) and any standalone/afternoon services** — billed entirely by GTT Center Perth, privately, at the locked prices in `services-pricing-locked.md`. This is where 100% of GTT Center Perth's own revenue comes from.

---

## Stream 1: Pathology/GTT Test Billing — Bulk Billing (Model, Requires Verification)

**Current working model, per this venture's own documents:**

| Patient situation | Billing model | Out-of-pocket cost |
|---|---|---|
| Medicare card holder, valid GP/midwife referral | Bulk-billed by the pathology partner | $0, per `onboarding.md`'s draft confirmation email content |
| No Medicare card / overseas visitor | Charged privately by the pathology partner | Approximately A$40-60, per `onboarding.md` draft — **this specific figure has not been independently confirmed with WDP or any partner** |
| No valid referral form | Cannot be processed under Medicare | Patient must obtain a referral before the test can proceed |

**Requires verification — do not treat as settled:**
- This bulk-billing arrangement (Medicare card holders = $0 out of pocket) is the standard expectation for a Licensed Collection Centre model, and appears consistently across this venture's planning documents, but **has not been confirmed in writing by WDP or any pathology partner for this specific venture.** `pathology-partnership-brief.md` itself notes "Pathology fee billed by PathWest/WDP to Medicare (out-of-pocket TBC — contact before pricing)."
- The A$40-60 non-Medicare figure is a planning estimate in draft patient-facing copy (`onboarding.md`), not a confirmed fee schedule from any pathology partner.
- **GTT Center Perth's own Medicare provider registration status:** under the confirmed Option A model, GTT Center Perth does not bill Medicare itself — the pathology partner does. This should be explicitly confirmed with an accountant and the pathology partner before being treated as settled (see `docs/regulatory-accreditation-tracker.md` §2).

---

## Stream 2: Wellness Package Billing — Private, Full-Price, Prepaid (Confirmed Model)

**This is fully within GTT Center Perth's own control and is the confirmed, locked model** — no Medicare involvement, no bulk-billing ambiguity.

- **Model:** private billing, no health-insurance rebate pathway involved (wellness services — massage, nails, hair, brows — are not Medicare or private-health-fund rebateable in this context)
- **Pricing:** Package 1 (A$250) and Package 2 (A$300) — flat, locked prices per `services-pricing-locked.md`, renamed 2026-07-20 (same 2 price points as before, the old A$200 tier remains dropped).
- **Payment timing:** per `onboarding.md`'s current draft policy, full payment is collected at time of booking (no deposit-only model) — this is a stricter policy than some competitor models (e.g., MIWM's booking structure was not independently verified for its own payment timing) and should be confirmed as the final policy before publishing, since `financial-setup.md` elsewhere describes an A$30 deposit model rather than full prepayment. **This is an internal inconsistency, not a Medicare-related item** — flagged here since it's directly relevant to billing strategy, and logged in `docs/01_conflicts_log.md` as a new finding.
- **GST treatment:** wellness services are standard-rated (10% GST); the pathology/GTT component is GST-free (medical supply) — this is a mixed-supply business requiring split GST accounting in Xero from Day 1 (`cash-flow.md`, `financial-setup.md`). **Requires verification:** the exact apportionment method when a single package price bundles a GST-free component (venue/lounge access, arguably attributable to the GTT visit) with GST-taxable wellness services — flagged in `financial-setup.md` as needing accountant confirmation, not yet resolved.

---

## Is a Hybrid Model (Bulk Billing + Private Billing) the Right Approach?

**Yes, and this is already the confirmed model, not a choice still being evaluated** — the "hybrid" here isn't GTT Center Perth choosing between bulk billing and private billing for the same service; it's that two genuinely separate services (the mandatory clinical test vs the optional wellness experience) naturally fall into different billing models:

- The clinical test is billed the way Australian pathology has always billed GTTs (bulk-billed to Medicare where eligible) — this isn't a strategic choice GTT Center Perth is making, it's simply how the existing pathology system already works, inherited via the partnership model
- The wellness experience is billed privately because it is, by definition, an elective add-on with no Medicare rebate pathway — there's no bulk-billing option available for a massage or manicure regardless of what GTT Center Perth might prefer

**This means GTT Center Perth is not actually setting pricing/billing *strategy* for the clinical component at all** — that's inherited from the pathology partner's existing Medicare arrangement. The only pricing/billing decisions genuinely within GTT Center Perth's control are the wellness package prices themselves (`services-pricing-locked.md`) and the payment-timing policy, **now confirmed: full package price collected at time of booking, no deposit (resolved 2026-07-20, see Open Items below).**

---

## Rationale Summary

1. **No incentive or ability to alter the pathology billing model** — it's inherited from the partner, not a GTT Center Perth decision, and any attempt to change it would require renegotiating the entire Option A partnership structure.
2. **Private billing for wellness services is the only available option** — there is no Medicare or private-health-fund rebate pathway for massage/nails/hair/brows in this context, so "private billing" isn't a strategic preference, it's the only mechanism that exists.
3. **The locked Package 1/2 structure (`services-pricing-locked.md`) already reflects the pricing decision** — this document exists to explain the billing *mechanics* around that pricing, not to re-litigate the price points themselves. See `docs/price-increase-comparison.md` for the separate analysis of whether/when to change the price points.

---

## Open Items

1. ~~Payment timing inconsistency~~ **RESOLVED 2026-07-20:** Anthony confirmed full package price is collected at time of booking, not a deposit. Corrected in `financial-setup.md`, `operations-manual.md`, `ivy-booking-system.md`, and `website-spec.md` — all now match `onboarding.md`'s originally-correct draft copy. See `docs/01_conflicts_log.md` CONFLICT-09.
2. **Pathology out-of-pocket figures:** the A$40-60 non-Medicare estimate needs direct confirmation with the pathology partner once the partnership is finalised. Not resolved.
3. **GST apportionment method:** needs accountant confirmation before the first taxable transaction (`financial-setup.md` Step 1). Not resolved.

---

## Changelog

**2026-07-19** — Created as a new Phase 7 deliverable. Referenced `services-pricing-locked.md` for the confirmed wellness pricing. Flagged all Medicare/pathology billing specifics as "requires verification," per the ground rule that this is a healthcare venture and clinical/regulatory/billing claims should not be asserted as settled. Found and logged a new internal inconsistency (payment-timing: prepayment vs deposit model) while researching this document — added to `docs/01_conflicts_log.md`.

**2026-07-20 (CONFLICT-09 resolved)** — Anthony confirmed full payment at booking, not a deposit. Updated this document and cross-referenced the four other documents corrected to match (`financial-setup.md`, `operations-manual.md`, `ivy-booking-system.md`, `website-spec.md`).

**2026-07-20 (package renumbering)** — Updated "Package 2/Package 3" references to "Package 1 (A$250)/Package 2 (A$300)" per `services-pricing-locked.md`'s renumbering.
