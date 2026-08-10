# Waitlist Validation Framework

**Phase:** feeds directly into `docs/architecture/MVP-BRAND-LAUNCH-PACKAGE.md` — this document does not duplicate that doc's asset list. It tightens the measurement criteria that package's waitlist mechanism will be measured against. **Does not change the existing 500-700 raw-signup target** (`docs/architecture/PRE-LAUNCH-DEMAND-VALIDATION-PLAN.md`) — it refines and qualifies that target with a quality dimension it currently lacks. No canonical data or financial model touched. No WDP communication — tracker item 50 untouched.

**Date:** 2026-08-10

---

## 1. High-Quality vs. Low-Quality Signup — Measurable Factors

Six factors, each independently measurable from data the lean signup form (`docs/architecture/MVP-BRAND-LAUNCH-PACKAGE.md` §1.4) and its optional follow-up survey (§1.8) already capture — no new data collection invented beyond what that document already specifies.

### 1.1 Due Date / GTT-Window Timing Alignment — the single most important factor

**A genuinely sobering, load-bearing finding this framework surfaces for the first time:** given the realistic lead time to opening — an 8-12 week pre-lease validation window (`docs/architecture/PRE-LAUNCH-DEMAND-VALIDATION-PLAN.md` §5) plus the existing ~20-week lease-to-opening schedule (`docs/grace-startup-plan.md`, lease Week 9-10, soft launch Week 19) — the realistic gap from "waitlist campaign starts" to "venue opens" is approximately **28-32 weeks (~7 months)**, a planning estimate, not a promised date. **A woman who is already in her 20-27th week of pregnancy at signup will, in almost every case, need to complete her actual GTT test elsewhere before this venue can open** — pregnancy is 40 weeks total, and 28-32 weeks from now she will likely have already delivered or be well past the 24-28-week GTT window. The women most likely to still be genuinely in-window near the realistic opening date are those who are **not yet pregnant, or very early in pregnancy (first trimester) at the time of signup** — a real, counter-intuitive finding directly relevant to how this factor should be scored.

**Scoring (0-30 points, the highest-weighted factor):**
- **30 pts:** not yet pregnant/actively planning, or currently weeks 1-10 — most likely to land in the 24-28-week window near the realistic opening horizon
- **15 pts:** currently weeks 11-20 — plausible, genuinely uncertain given opening-date variability
- **5 pts:** currently weeks 21-27 — will very likely need to test elsewhere before this venue opens; valuable for brand loyalty/future pregnancies, not a realistic Month 1 candidate
- **0 pts:** currently 28+ weeks, or has already indicated (via the survey question already specified in `docs/architecture/MVP-BRAND-LAUNCH-PACKAGE.md` §1.8) that she has already had her GTT test

### 1.2 Suburb/Location Relevance — Explicitly Provisional Pre-Venue

**Flagged plainly: this factor cannot be scored against a real catchment yet, since no venue is confirmed.** Provisional proxy only, to be re-scored once a venue exists: full points for a suburb within reasonable drive-time of any of the search zones already identified in `docs/location-scouting.md` (Osborne Park, Joondalup, Cannington, Myaree/Murdoch, and the widened metro-wide search since); partial points for other Perth-metro suburbs; low points for outside-metro signups. **This whole factor should be recalculated retrospectively once a venue is confirmed** — a provisional score now is better than no signal at all, but should not be treated as settled.

**Scoring (0-15 points):** 15 (within an identified search zone or reasonable drive-time) / 8 (other Perth metro) / 2 (outside metro, genuinely low priority for a physical-visit service).

### 1.3 Engagement Level

**Scoring (0-20 points):** 20 (opened the welcome email AND at least one further engagement — a follow-up email open, an Instagram interaction, a landing-page return visit) / 10 (opened the welcome email only) / 0 (no engagement recorded beyond the initial form submission).

### 1.4 Willingness to Book / Explicit Intent Signal

**Scoring (0-20 points):** 20 (completed the optional validation follow-up survey, `docs/architecture/MVP-BRAND-LAUNCH-PACKAGE.md` §1.8 — a genuine, voluntary extra-effort signal) / 10 (responded positively to a future priority-access invitation, once one exists) / 0 (signup only, no further voluntary action).

### 1.5 Service/Package Interest Alignment

**Scoring (0-10 points):** 10 (selected interest in current launch-scope services only — massage, nails, hair, brows) / 5 (selected a mix including out-of-scope items, e.g. 3D scan/dietitian, alongside in-scope ones) / 0 (selected only out-of-scope services, or none at all) — a genuine mismatch signal at 0, not just a scoring formality.

### 1.6 Referral Source Quality

**Scoring (0-5 points):** 5 (referred by one of the 22 named practices or a confirmed community partner, `docs/poppy-marketing.md` §1) / 3 (organic social/search discovery) / 0 (unknown or unspecified source).

**Maximum possible score: 100 points.**

---

## 2. Scoring System — Bridging Raw Signups to Estimated Month 1 Volume

### 2.1 Quality Tiers

- **High-Quality:** total score ≥ 70
- **Medium-Quality:** total score 40-69
- **Low-Quality:** total score < 40

### 2.2 Weighted Qualified Size (WQS)

Not every quality tier converts to a booking at the same rate — a Low-quality signup is not worthless (word-of-mouth, future pregnancies, referral value), but should not be counted at face value against a Month 1 target. **Weighting, disclosed as a reasoned judgement, not evidenced data (this venture has zero trading history):**

**WQS = (High-quality count × 1.0) + (Medium-quality count × 0.5) + (Low-quality count × 0.1)**

### 2.3 From WQS to Estimated Month 1 Bookings

Apply the same conversion-rate scenarios already established in `docs/architecture/PRE-LAUNCH-DEMAND-VALIDATION-PLAN.md` §2 (10%/20%/30%, generic and unevidenced) — but now applied to the **quality-weighted** count, a more defensible base than raw signups:

**Estimated Month 1 bookings from waitlist = WQS × conversion rate**

### 2.4 Illustrative Worked Example — Hypothetical Numbers, Not Real Data

To show the mechanics only, not to assert a real outcome: 600 raw signups, with an illustrative (not evidenced) quality mix of 20% High / 40% Medium / 40% Low:

| | Count | Weight | Weighted contribution |
|---|---|---|---|
| High | 120 | 1.0 | 120 |
| Medium | 240 | 0.5 | 120 |
| Low | 240 | 0.1 | 24 |
| **WQS** | | | **264** |

At 10%/20%/30% conversion: **26 / 53 / 79 estimated Month 1 bookings** from this illustrative mix — a genuinely sobering result against the 132-booking target (§3), included precisely to show why quality mix matters as much as raw count, not to predict a real outcome.

### 2.5 Channel Performance Measurement

Because referral source (§1.6) is one of the six scored factors, per-channel quality can be measured directly: average total score, and average WQS-per-signup, computed separately for each referral-source category (named-practice referral, community partner, organic social, direct search, other). This lets Anthony see which acquisition channel is producing not just volume but *quality* — a genuinely more useful signal than raw signup count by channel alone, and directly answers the "channel performance" measurement this framework was asked to support.

---

## 3. Refined Go/No-Go Thresholds — Qualifying, Not Replacing, the Existing 500-700 Target

**The 500-700 raw signup target from `docs/architecture/PRE-LAUNCH-DEMAND-VALIDATION-PLAN.md` §3/§6 is unchanged.** This section adds a quality qualifier alongside it, using the same already-established 65%-waitlist-share planning case and the Month 1 target (190-221 total AM clients, mid 204):

- **Bookings needed from the waitlist specifically (65% share, mid target): 132.**
- **Weighted Qualified Size needed, by conversion scenario:** 1,325 (at 10%) / **662 (at 20%, the primary planning case)** / 442 (at 30%).

**Refined Gate 1 (replaces the raw-count-only version of this gate from the prior document with a two-part qualifier):**
1. Raw signups ≥ 500-700 (unchanged).
2. **AND** at least 40% of those signups score Medium-or-High quality on this framework (i.e., at least 200-280 of the 500-700 are genuinely plausible, not merely any signup) — a new, disclosed, judgement-based qualifier, not evidenced.

**Why 40%, disclosed honestly:** this is a reasoned planning threshold, not a proven cutoff — it is set deliberately modest, since §1.1's own finding (most currently-pregnant signups will not remain in-window by opening) means a genuinely high-quality-majority waitlist is unlikely to be achievable from a cold, pre-lease audience. **This qualifier exists to catch a genuinely poor-quality waitlist (e.g. mostly Low-tier, heavily skewed toward already-pregnant/already-tested signups) before it is mistaken for real demand validation, not to set an unrealistically high bar.**

---

## 4. Evidence Thresholds for What Happens Next

**Proceed toward lease discussions if:**
- Gate 1 (§3) is met — raw signups ≥ 500-700 AND ≥ 40% Medium/High quality — **and**
- The computed WQS, at the observed real conversion signal (once any real booking-intent data exists, e.g. from the priority-access follow-up), is trending toward or above the 442-662 range (§3) — not required to be conclusively proven, but showing a credible trajectory.

**Continue validation longer if:**
- Raw signups are tracking below 500 with no clear plateau, **or**
- Raw signups reach 500-700 but quality mix is materially below the 40% Medium/High qualifier (e.g. heavily skewed Low, per §1.1's own timing-alignment risk) — extend the window and intensify the "not yet pregnant / early pregnancy" messaging specifically, since §1.1 identifies this as the highest-value, currently-least-targeted segment.

**Genuinely reconsider the operating assumptions (Table 1 vs. Table 2, or the launch timeline) if:**
- The validation window has already been extended once (per the prior bullet) and the quality-weighted signal still does not credibly approach the 442-662 WQS range even at the more optimistic 30% conversion scenario — this is the point at which the honest conclusion is not "try harder at the same plan" but a genuine re-examination of whether the committed 18-client/day Table 1 volume (`docs/VERIFICATION-TRACKER.md` item 1m, still open) is realistic, or whether the launch timeline itself needs to shift to capture a later, more naturally-aligned cohort of signups (per §1.1's own timing-alignment finding, a later launch could plausibly draw from women who are further along in pregnancy today but would only just be entering their GTT window when a delayed opening occurs).
- **This document does not make this decision** — it defines the evidence threshold at which the decision becomes genuinely warranted, for Anthony to act on.

---

## Validation

No canonical YAML, financial model, or revenue/cost methodology was modified by this document. The 500-700 signup target itself is unchanged — only qualified with a new quality dimension (see full validation summary in this phase's combined report-back).
