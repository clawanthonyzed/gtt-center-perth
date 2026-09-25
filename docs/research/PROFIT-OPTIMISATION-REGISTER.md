# GTT Center Perth — Profit Optimisation Register (External Research Supplement)

**Created:** 2026-09-25 | **Research completed by:** Grace (Operations Manager), external-research mission
**Purpose:** New margin/revenue opportunities identified this session, in the format the mission specified: CURRENT / EVIDENCE / POTENTIAL CHANGE / FINANCIAL EFFECT / CONFIDENCE / DECISION. This supplements, and does not replace, the extensive existing optimisation work already in this repository (`docs/architecture/STARTUP-COST-OPTIMISATION.md`, `docs/architecture/STARTUP-COST-REDUCTION-ACTIONS.md`, the Downtime-Fill Revenue line already quantified in `docs/CURRENT-STATE.md` §8, and the Lever 0 AM-capacity finding already adopted into the current model). **No figure below has been added to the canonical financial model — every one of these is a recommendation only, tagged for Anthony's decision, per the mission's hard rule against silently altering the locked financial model.**

---

## Opportunity 1: PM Membership / Recurring-Revenue Product

**CURRENT:** PM revenue is modelled entirely as one-off session/package transactions (`docs/CURRENT-STATE.md` §2, §5) — no recurring-revenue or membership product exists anywhere in this venture's plan.

**EVIDENCE:** Australia's largest day-spa franchise network, endota spa, operates a formal "endota Retreat Membership" recurring-revenue product (confirmed via its own website, `COMPETITOR-ANALOGUE-DATABASE.md` Section 3) — a real, current Australian industry precedent that membership models are viable in this exact industry. General spa-industry commercial sources (Tier 4, not independently verified) commonly frame membership/recurring-revenue programs as a retention and predictable-cash-flow tool, directly relevant given the cash-flow-fragility evidence in `OWNER-OPERATOR-FAILURE-INTELLIGENCE.md`.

**POTENTIAL CHANGE:** Explore a simple PM membership tier (e.g., a monthly fee entitling the member to a discounted or bundled recurring treatment, positioned for postpartum/ongoing clients returning after their GTT visit) as a Phase 2 addition, not a launch-day feature — this aligns with the existing `experience/RETURN-LOOP.md` mechanism (already identified in this repository as "the single biggest unmodelled financial gap") by giving the AM-to-PM return loop a concrete recurring-revenue product to convert into, rather than leaving repeat PM visits as one-off transactions.

**FINANCIAL EFFECT:** Not quantifiable without real trading data (repeat-visit rate, willingness-to-pay for a membership tier are both unknown pre-launch) — genuinely `[PLACEHOLDER]`, not modelled here. Directionally, even a modest membership uptake among the PM segment's existing ~10 sessions/day capacity (`docs/CURRENT-STATE.md` §3, post-2026-09-19 Model E figure) would improve revenue predictability, which has a real (if unquantified) value given the cash-flow-fragility evidence above, independent of any change to average revenue per session.

**CONFIDENCE:** Low-Medium — the endota precedent proves viability in the industry generally, not in GTT Center Perth's specific single-venue, 6-hour-afternoon-window PM operating base, which is a materially smaller and more time-constrained model than a full-day multi-location franchise network.

**DECISION:** Anthony approval required. Recommend logging as a Phase 2 consideration alongside the existing 3D-scan and spray-tan Phase 2 deferrals, not a launch-day commitment.

---

## Opportunity 2: Referral-Courtesy Model Review (Compliance-Driven, But With a Real Profit Angle)

**CURRENT:** The referral-partnership plan (`docs/referral-partnership-plan.md`) offers referring practices complimentary staff visits and possible "partner-specific pricing" as a referral-relationship tool.

**EVIDENCE:** `AUSTRALIAN-COMPLIANCE-SUPPLEMENT.md` Finding 1 flags a genuine, previously-unidentified legal question (Health Insurance Act s129AA) about whether these referral-courtesy mechanics could be read as inducement. Separate from the compliance question, complimentary visits and discounted referred-client pricing are a real, direct cost/margin item that has not been quantified anywhere in this venture's plan (the 22-practice first-wave outreach plan does not model the cost of the complimentary visits it proposes giving to up to 22 practices' staff).

**POTENTIAL CHANGE:** Once the compliance question in Finding 1 is resolved, quantify the actual cost of the complimentary-visit offer (up to 22 initial recipients, each consuming one PM session slot at zero revenue) against the referral-channel revenue it is expected to generate, and consider capping the number of complimentary visits per practice or per quarter, rather than leaving it open-ended.

**FINANCIAL EFFECT:** At current a-la-carte PM pricing (`docs/CURRENT-STATE.md` §2, ~A$95-117/session historically modelled), 22 complimentary visits would represent an unmodelled opportunity cost in the order of A$2,000-2,600 in forgone PM session revenue if all 22 practices take up the offer in the same period as a fully-booked PM day — genuinely small relative to the overall model, but currently entirely unquantified anywhere in this repository. `[MODELED — this document's own estimate, not previously calculated elsewhere]`.

**CONFIDENCE:** Medium — the arithmetic is simple and the practice count is already fixed in `docs/referral-partnership-plan.md`; the real uncertainty is how many of the 22 practices actually take up the offer, which is unknown pre-launch.

**DECISION:** No founder decision strictly required (this is a documentation/quantification gap, not a locked-model change) — recommend adding this cost line to whichever document eventually costs out the referral-outreach program, once outreach is closer to actually starting.

---

## Opportunity 3: Prepaid-Package Cash-Flow Segregation (Risk-Mitigation, Not Revenue, But Directly Protects Existing Profit Model)

**CURRENT:** Full package price is collected at booking (`docs/CURRENT-STATE.md` §2); the working-capital reserve (§7.3) already covers Months 1-3 operating losses as a buffer, but no document in this repository discusses whether prepaid client funds are tracked/segregated separately from general operating cash.

**EVIDENCE:** The real Adytum case (`OWNER-OPERATOR-FAILURE-INTELLIGENCE.md` Section 1) shows a concrete, sourced example of a comparable Australian wellness business continuing to sell prepaid vouchers while insolvent, leaving customers and staff as unsecured creditors. This is not a claim that GTT Center Perth is at similar risk — its financial model is far more rigorously built than what that case suggests Adytum had — but it is real evidence that pre-collected client cash needs deliberate handling discipline, not just a general working-capital reserve.

**POTENTIAL CHANGE:** No change to the pricing/payment model (locked, out of scope). Recommend a simple internal practice once trading begins: track prepaid-but-not-yet-delivered package liability as its own line in whatever bookkeeping/Xero setup is used (`docs/financial-setup.md`), so the Venue Manager and Anthony always know the dollar value of services already paid for but not yet delivered, distinct from the venue's own operating cash. This is a bookkeeping/process recommendation, not a financial-model change.

**FINANCIAL EFFECT:** Not a revenue or cost line — a risk-mitigation practice. No dollar effect on the P&L; protects the existing model's own cash position and reputation from the specific failure mode evidenced in Section 1.

**CONFIDENCE:** High that the practice itself is sound (this is standard accounting practice for any business collecting payment in advance of service delivery, "deferred revenue" or "unearned revenue" in standard accounting terms) — low uncertainty here, this is closer to a confirmed good practice than a speculative opportunity.

**DECISION:** Recommend to accountant as a standard bookkeeping setup item, not a founder decision — flagged here because it was directly evidenced by this session's failure-intelligence research, not because it requires Anthony's judgement call.

---

## What Was Deliberately Not Pursued Further

- **Re-deriving AM capacity/staffing levers** — `docs/CURRENT-STATE.md` §0 and §10 already contain an extremely recent (2026-09-19), solver-verified set of findings on this exact question (demand-driven staffing tiers, Lever 0). Nothing found this session would add to or contradict that work.
- **Startup-cost reduction** — `docs/architecture/STARTUP-COST-OPTIMISATION.md` and `STARTUP-COST-REDUCTION-ACTIONS.md` already cover this in detail with a founder-approved outcome (A$251,198 planning figure). No new supplier/cost evidence was found this session that would add to it.

---

## Changelog

**2026-09-25 (created):** New file, external-research mission deliverable. 3 new opportunities identified, none applied to the canonical financial model, all tagged for Anthony's decision or standard professional/bookkeeping practice as appropriate. Cross-references `COMPETITOR-ANALOGUE-DATABASE.md` (endota membership precedent) and `OWNER-OPERATOR-FAILURE-INTELLIGENCE.md` (Adytum cash-flow evidence) and `AUSTRALIAN-COMPLIANCE-SUPPLEMENT.md` (referral-inducement question) rather than repeating their content.
