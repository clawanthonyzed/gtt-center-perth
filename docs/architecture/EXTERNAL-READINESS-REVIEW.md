# External Readiness Review — Updated Assessment

**Phase:** Commercial Assumption Alignment & External Readiness — documentation only. Builds on `docs/architecture/COMMERCIAL-VALIDATION-FRAMEWORK.md` §4 (Investor/Lender Readiness Gap Report) and `docs/architecture/MVP-OPENING-DECISION-REVIEW.md` rather than starting from scratch — this document re-assesses those findings against what has genuinely changed since: the Canonical Startup Cost Adoption (a specific, founder-approved A$251,198 planning figure, replacing a broad range) and the narrowed funding-requirement planning case (A$336,198–361,198, shown alongside the previous A$357,390–577,180 bounded range).

**Date:** 2026-08-10
**Version used as source of truth:** commit `a2defba` (Canonical Startup Cost Adoption) and everything it built on.

---

## What Has Genuinely Changed Since the Prior Readiness Assessments

- A specific, itemised, founder-approved startup budget now exists (`data/canonical/startup_costs.yml#adopted_planning_scenarios`, A$251,198), replacing the broad A$357,390–577,180 range as the *primary* planning reference for internal purposes — though that broader range remains retained, unaltered, alongside it.
- The combined funding-requirement planning case narrowed to A$336,198–361,198.
- **Neither change resolves any of the underlying structural gaps** identified in the prior readiness assessments — no accountant engagement has occurred, no venue is confirmed, no debt/equity structure exists, and the new figure is explicitly a planning assumption, not a locked cost (`docs/VERIFICATION-TRACKER.md` item 49, OPEN).
- New this phase: the WDP client-volume mismatch has been precisely documented (`docs/architecture/WDP-COMMERCIAL-ALIGNMENT-REVIEW.md`) — a real, specific gap affecting WDP discussion readiness that was not previously isolated this precisely.

---

## A. Landlord Discussion

### Rating: Ready with conditions

**What's ready:** A genuinely strong business concept and occupancy story (staffing model, service structure, clientele profile — all well documented). The new founder-approved startup budget (A$251,198) gives a specific, credible answer to "what is this venture's capital position," materially stronger than presenting a wide A$357,390–577,180 range would be in a landlord conversation. The Venue First-Visit Checklist and full Venue Data Capture Template (`docs/architecture/VENUE-ACQUISITION-DUE-DILIGENCE.md`) are ready to use the moment a candidate property is found.

**Conditions still unmet — unchanged by this phase:**
1. **Proof-of-funds document** — does not exist anywhere in this repository. Likely the simplest gap to close (an accountant/bank-provided letter), but not yet produced.
2. **Public liability insurance certificate of currency** — not yet obtained (`docs/VERIFICATION-TRACKER.md` item 19, OPEN); `docs/financial-setup.md` STEP 8 itself notes many landlords want this before lease signing, not after.

**Verdict:** the venture could credibly walk into a landlord conversation today with a strong concept and a specific budget figure — but should close the two conditions above before a serious lease negotiation, not during one.

---

## B. WDP Discussion

### Rating: Ready with conditions

**What's ready:** A genuinely active, positive, real correspondence thread — Carole Rivers is engaged, has provided detailed staffing/scope/timing/room-spec information, and is actively progressing a commercial figure with WDP's own State Business Manager (`docs/VERIFICATION-TRACKER.md` item 1c). The underlying operational model (collector scope, wait-period supervision approach, room compliance) is well-developed and defensible against primary sources (NPAAC, RCPA — items 29/29b/29c).

**Condition that must be met before the next substantive commercial exchange:**
1. **The client-volume mismatch must be corrected.** `docs/architecture/WDP-COMMERCIAL-ALIGNMENT-REVIEW.md` (this phase) found that WDP has only ever been told 12 clients/day (the SECONDARY reference model) in any confirmed-sent communication — the correction to 18 clients/day (the PRIMARY committed model) was drafted but never sent. Since Carole's own stated pricing model depends explicitly on "expected pathology volume," any commercial figure WDP provides without this correction risks being calibrated against the wrong, lower volume.

**Also still open, lower priority:** three questions from the 07-31 email remain unanswered (staff continuity, placement-model threshold, observation-during-wait mechanism), and several questions have never been asked at all (exact room-spec dimensions, exclusivity, contract term/notice provisions, WDP's own insurance requirements) — see `docs/architecture/VENUE-ACQUISITION-DUE-DILIGENCE.md` §4.3 for the full gap list, unchanged by this phase.

**Verdict:** genuinely close to ready for a real commercial figure — but sending or receiving one before the volume correction is made risks a real, avoidable renegotiation later.

---

## C. Accountant Review

### Rating: Ready with conditions

**What's ready:** the financial package itself is genuinely strong and review-ready. The Master Financial Model (Excel/Word/PDF deliverables), the bottom-up startup cost reconstruction and its founder-approved MVP adoption, and the funding-requirement analysis are all professionally organised, internally traceable, and validated (114+ passing tests, 0 canonical validator errors throughout this whole effort). This is materially more complete than a typical pre-engagement financial package.

**Condition:** `docs/financial-setup.md` STEP 1 already flags accountant engagement as BLOCKING, Week 1 — that engagement has still not occurred (no evidence anywhere in this repo that it has). The condition is scheduling it, not further document preparation. When it does happen, `docs/architecture/COMMERCIAL-VALIDATION-FRAMEWORK.md` §2 already identified the specific, still-open accountant-confirmation items worth bundling into that single engagement rather than raising piecemeal: startup-capital sign-off, GST apportionment (item 7), ABN/GST registration scope (item 8), the proposed trust-distribution tax (items 9, 9b, 9c), and current Fair Work wage-rate confirmation (items 16–18).

**Verdict:** the package is ready; the action item is scheduling the engagement itself and bringing the already-compiled open-item list to it.

---

## D. Investor/Lender Discussion

### Rating: Not ready

**What's changed but doesn't move the rating:** the funding requirement is now more precise (A$336,198–361,198 vs. the previous A$357,390–577,180 range) — a genuine improvement in specificity, but it does not touch the structural reasons this remains not-ready:

- **Bank finance:** still no debt/repayment structure exists anywhere in this venture's model, by design (self-funded via joint savings, per `CLAUDE.md`'s own standing fact) — a structural gap, not a documentation gap, that no amount of further planning-figure precision resolves.
- **Private investor (equity):** still no equity structure, no return/exit modelling (explicitly out of scope per `data/models/master_financial_model.yml`'s own stated boundary) — the risk documentation remains unusually strong for a pre-revenue venture, but that alone does not constitute investor readiness.
- **Both:** no accountant sign-off has occurred (condition C above), no venue is confirmed (`docs/VERIFICATION-TRACKER.md` item 3, still BLOCKING), and the new A$251,198 figure is explicitly a planning assumption, not a locked cost (item 49, OPEN) — presenting it as final to an investor or lender would overstate its own certainty.

**Verdict:** unchanged from the prior assessment. The narrower funding-requirement range is a genuine, disclosed improvement in precision, not a change in readiness — the same structural and evidentiary gaps identified in `docs/architecture/COMMERCIAL-VALIDATION-FRAMEWORK.md` §4.1–4.2 remain fully open.

---

## Summary Table

| Audience | Rating | Primary remaining condition |
|---|---|---|
| A. Landlord discussion | Ready with conditions | Proof-of-funds document + public liability insurance certificate |
| B. WDP discussion | Ready with conditions | Correct the client-volume mismatch (18/day, not 12/day) before the next commercial exchange |
| C. Accountant review | Ready with conditions | Schedule the still-outstanding Week 1 engagement; bring the compiled open-item list |
| D. Investor/lender discussion | Not ready | Structural (no debt/equity structure by design) + no accountant sign-off + no confirmed venue + figure explicitly non-final |

---

## Validation — Confirmed No Model Changes Occurred

- No canonical YAML, financial model, or revenue/cost methodology was touched by this document.
- This is an assessment document only — no new financial figures were calculated; every figure referenced above is quoted directly from already-canonical, already-committed sources.
