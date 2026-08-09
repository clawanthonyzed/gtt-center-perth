# GTT Center Perth — Startup-Capital Reconciliation

**Purpose:** reconstruct every "total startup capital" figure found anywhere in this repo, verify each directly against its stated source (not assumed still correct), and explain **why** they differ — not just list them side by side. This document does **not** resolve which figure is correct. Per the coordinator's explicit instruction for this phase: *"The startup-capital reconciliation problem must stay visible until evidence actually supports reconciling it."* Structured-data counterparts to most figures below live in `data/canonical/startup_costs.yml`'s `historical_total_estimates` list — this document is the narrative companion, not a duplicate.

**Method:** every figure below was re-read directly from its cited source document this session (not carried over from a prior session's summary), per the coordinator's explicit instruction not to assume the 4 figures flagged in the prior audit are still correct.

---

## 1. The Figures, Verified Directly

| # | Figure | Source | Date/Version | Status |
|---|---|---|---|---|
| 1 | A$363,000 mid / A$292,000-493,000 | `investor-memorandum.md` (original itemised build) | Pre-2026-07-29 rewrite | **SUPERSEDED — and untraceable.** Confirmed this session: the itemisation behind this figure **no longer exists anywhere in `investor-memorandum.md`'s current content.** The document was rewritten 2026-07-29 after an external review found a banner/body contradiction elsewhere in the same file — the rewrite replaced the original fit-out/equipment/IT/working-capital/legal breakdown with a paragraph stating the figure is "now known to be one of three different, never-reconciled ranges" and pointing to `CURRENT-STATE.md` instead. **The original component build cannot be re-derived from this repo's current content at all** — only the summary mid/range numbers survive, as a historical reference. |
| 2 | ~A$144,500-242,500 | `HANDOFF.md` (2026-07-17) | 2026-07-17 | **SUPERSEDED — no itemised build, never had one.** Confirmed this session: `HANDOFF.md`'s own text gives this range with zero component breakdown — it is presented as "realistic," down from the A$363,000 original, with no line items shown. **New finding this pass:** this figure is remarkably close to `grace-startup-plan.md`'s own "Total pre-revenue capital" bottom line (A$140,000-260,000, see #9 below) — plausibly the same underlying estimate, restated, or a closely related calculation done independently. Not confirmed either way; the two documents never cross-reference each other. |
| 3 | Low A$209,000 / Mid A$305,000 / High A$431,000 | `business-plan.md` §9, attributed to `cash-flow.md` | 2026-07-20 rebuild era | **PLACEHOLDER — citation confirmed broken this session, not just suspected.** `cash-flow.md`'s own current content was read in full this pass: its "Pre-Launch Capital Deployment" section explicitly states *"Not rebuilt in this round"* and lists only category **names** (entity setup, lease bond, fit-out, equipment, WDP setup, pre-launch marketing, staff training, pre-open operating costs, contingency) — **no dollar figures at all, anywhere in that document.** `business-plan.md`'s citation to `cash-flow.md` for this specific range cannot be substantiated from `cash-flow.md`'s actual content. |
| 4 | A$228,142-457,559 (mid A$341,851; net after landlord contribution ~A$311,851) | `floor-plan-concept.md` Fit-Out Cost Estimate | 2026-07-31 recompute | **CURRENT, but narrower scope — not directly comparable to the others.** This is the most recently and most rigorously re-derived figure in the whole list (independent bottom-up build, itemised construction/equipment/furniture/signage/IT-AV). But it covers **fit-out only** — it excludes working capital, legal/entity setup, and lease costs entirely. Comparing it to the "full startup capital" ranges above requires adding those categories on top, which no document in this repo does explicitly. |
| 5 | A$268,142-583,559 | `CURRENT-STATE.md` §7, "original same-day rebuild" | 2026-07-31 (retired same day) | **SUPERSEDED, explicitly and immediately.** `CURRENT-STATE.md` states this figure "is retired, not left standing alongside" its own reconciled replacement (#6/#7 below) — Anthony reviewed it directly the same day and required two corrections (landlord contribution removed from the headline; insurance relabelled `[PLACEHOLDER]`). Retained in this repo for trace only. |
| 6 | A$276,635-554,900 | `CURRENT-STATE.md` §7.4, "the original reference range this whole Section 7 exercise started from" | Pre-2026-07-31 | **SUPERSEDED — a starting point, not a destination.** `CURRENT-STATE.md` itself frames both 2026-07-31 corrections (landlord contribution removed, construction recomputed at a higher established rate) as pushing this starting range **up**, arriving at #7/#8 below. |
| 7 | A$357,390-577,180 | `CURRENT-STATE.md` §7.4, this agent's own 7.1+7.2+7.3 component sum | 2026-07-31 | **CURRENT, but explicitly disclosed as not matching #8.** A straightforward arithmetic sum of `CURRENT-STATE.md`'s own three component ranges (Equipment/Furniture/Signage A$61,190-140,430; Construction A$191,200-298,750; Working Capital & Pre-Launch A$105,000-138,000). `CURRENT-STATE.md` itself states this sum does **not** land exactly on #8 — "a few percent gap on both ends," attributed to unspecified reconciliation choices Anthony made that aren't fully visible in this repo. |
| 8 | **A$292,335-594,900** | `CURRENT-STATE.md` §7.4, "Anthony's own reconciliation, adopted as instructed" | 2026-07-31 | **The most recent figure this repo's own governance points to for current use** — but `CURRENT-STATE.md` itself continues to frame the overall §6/§7 question as UNRECONCILED at the file level, retaining every historical range rather than declaring this the single canonical figure for all purposes. See §3 below for why this document does not elevate it further. |
| 9 | **A$140,000-260,000** ("Total pre-revenue capital") | `grace-startup-plan.md` FINANCIAL GATES table | 2026-06-05 | **NEW FINDING THIS PASS — not previously counted in this repo's own "3 unreconciled ranges" framing.** `CURRENT-STATE.md` §6 and `investor-memorandum.md` §8 both describe "three different, never-reconciled ranges" — but this fourth, fully itemised range (legal/professional fees A$3,000-6,000 + lease deposit/first month A$5,000-15,000 + fit-out deposit Stage 1 A$50,000-80,000 + fit-out completion Stage 2 A$50,000-100,000 + equipment/FF&E/stock A$30,000-60,000) exists in this repo, undisclosed by that framing. It carries **no staleness banner** despite being dated 2026-06-05 — before every subsequent client-volume rebase (8→10→12→18/day) and fit-out rebase (2→4 hair chairs, 2→4 nail stations, wall-to-curtain construction). Treated as superseded by inference in `data/canonical/startup_costs.yml`, not by an explicit marker in the source. |

**This repo's own governance undercounts the unreconciled range problem.** `CURRENT-STATE.md` §6 says "three different ranges exist" (figures #1, #2, #3 above); `investor-memorandum.md` §8 repeats the same "three ranges" framing. Counting the fit-out-only figure (#4), the two Section 7 build stages (#5, #7/#8), the pre-2026-07-31 starting point (#6), and the newly-found `grace-startup-plan.md` figure (#9), there are **at least 6-9 distinct, non-identical dollar ranges** across this repo's own documents, depending on how finely the Section 7 build's internal stages are counted separately. This is itself a finding worth surfacing plainly, not smoothed into "three."

---

## 2. Why the Figures Differ (Not Just That They Differ)

Six distinct, disclosed drivers explain the spread — not a single unexplained inconsistency:

### 2.1 Scope differences — what's actually being totalled
- **Full startup capital** (legal, lease, fit-out, equipment, working capital) — figures #1, #2, #3, #5, #6, #7, #8, #9.
- **Fit-out only** (construction + equipment + furniture + signage + IT/AV, no legal/lease/working-capital) — figure #4. Materially narrower scope; not apples-to-apples with the others without addition.
- **A different decomposition entirely** — figure #9 (`grace-startup-plan.md`) splits fit-out into a 2-stage deposit schedule (Stage 1/Stage 2) rather than a single construction line, and does not appear to include a working-capital reserve at all (see §2.4).

### 2.2 Methodology differences — how the construction figure itself is derived
Two genuinely different, independently-run methodologies coexist for construction cost alone, both retained in `CURRENT-STATE.md` §7.2 and `data/canonical/startup_costs.yml`, deliberately not forced to agree:
- **Reverse-derived rate:** `floor-plan-concept.md`'s figure reverse-derives a base shell A$/sqm rate from this document's own 2026-07-19 prior figures, applies it to the new 239sqm footprint, then subtracts a itemised, confirmed wall-to-curtain/open-plan saving (A$10,736-17,256).
- **Established-rate reapplication:** `CURRENT-STATE.md` §7.2 instead applies its own previously-established A$800-1,250/sqm rate directly to the same 239sqm, with no landlord-contribution deduction.

Both are legitimate, disclosed, and land "close but not identical" (`CURRENT-STATE.md`'s own words) — A$162,452-306,029 vs. A$191,200-298,750.

### 2.3 Temporal drift — the underlying model kept changing
Every earlier figure in the list predates at least one, and usually several, of the following real changes to what's actually being built: the AM client-volume rebase (8→10→12→18 clients/day), the fixture-count expansion (2→4 hairdressing chairs, 2-3→4 nail stations), and the construction-type change (walled rooms → open-plan/curtain partitions for everything except the Blood Collection Room). `grace-startup-plan.md` (#9, 2026-06-05) predates **all** of these. `investor-memorandum.md`'s original build (#1) and `HANDOFF.md` (#2) predate most of them. Only figures #4, #7, and #8 postdate the full 2026-07-31 fixture-count/construction-type correction — and none of them yet reflects the 2026-08-05 client-volume rebase to Table 1/Table 2 (client volume does not directly drive fit-out cost, so this specific drift is lower-impact for startup capital than for the operating P&L, but is not independently confirmed as zero-impact either).

### 2.4 Working-capital inclusion/exclusion
`CURRENT-STATE.md` §7.3 explicitly includes a Working Capital Reserve (A$85,000-110,000) inside its startup-capital range. `grace-startup-plan.md`'s FINANCIAL GATES table (#9) shows no working-capital line at all — its "Total pre-revenue capital" appears to be startup **expenditure** only, not the fuller "opening funding requirement" concept the coordinator's Part 5 distinguishes. This alone could explain a meaningful share of the gap between #8 (A$292,335-594,900, includes working capital) and #9 (A$140,000-260,000, apparently does not) — a plausible, not confirmed, explanation.

### 2.5 Landlord-contribution treatment
`floor-plan-concept.md` (#4) nets a landlord fit-out contribution (A$20,000-60,000) against its headline, producing a "net mid-range" figure of ~A$311,851. `CURRENT-STATE.md` §7 (#5 through #8) explicitly **removes** this deduction from the headline entirely, per Anthony's direct instruction ("skeptical a landlord will actually contribute"). Comparing #4's net figure to #7/#8's gross figures without adjusting for this is a like-for-like error waiting to happen.

### 2.6 Contingency — present in principle, absent in practice
Exactly one contingency assumption exists anywhere in this repo: `investor-memorandum.md`'s risk table states "Mid-range budget includes 15% contingency" for fit-out cost blowout risk. **No other document states a competing percentage — but no document's own build methodology (including `investor-memorandum.md`'s own, since its original itemisation no longer exists) shows this 15% actually being applied as a calculation step.** Whether any of figures #4, #7, or #8 already has an implicit 15% buffer baked in, or whether all of them would need an additional 15% uplift on top, is genuinely unknown from this repo's content. See `data/canonical/startup_costs.yml`'s `contingency_fitout_15pct` record.

---

## 3. New Findings This Pass (Beyond the 4 Figures the Coordinator Asked to Re-Verify)

1. **`grace-startup-plan.md`'s own A$140,000-260,000 range** (§1, figure #9) — not previously counted anywhere in this repo's "3 unreconciled ranges" framing.
2. **`equipment-costs.md`'s Summary Budget table does not exactly match its own per-section itemised totals**, for at least 4 categories (Pathology Collection Room — already disclosed by the source itself; Massage Rooms, Lounge, Technology — not previously flagged anywhere). See `data/canonical/capex.yml`'s `conflict_summary_budget_vs_section_totals`.
3. **A possible IT/AV double-count** — `floor-plan-concept.md`'s Fit-Out Cost Estimate carries its own standalone "IT / AV (POS, booking tablets, TVs, music system)" line (A$5,000-12,000) separate from its "Equipment" line, which itself sources from `equipment-costs.md`'s Technology section (which already includes iPads and a POS terminal). Whether this is genuinely additional spend (TVs, music system — not itemised anywhere else) or a partial double-count is not resolved by either document. See `data/canonical/capex.yml`'s `conflict_it_av_overlap`.
4. **`grace-startup-plan.md`'s staged fit-out payments (Stage 1 + Stage 2 = A$100,000-180,000) are materially lower than every current construction estimate** (A$162,452-306,029 or A$191,200-298,750) at both ends — most plausibly explained by §2.3's temporal-drift finding, not confirmed.
5. **Potential overlap between `CURRENT-STATE.md` §7.3's "Legal/entity setup, lease bond" line and `grace-startup-plan.md`'s separate "Legal and professional fees" + "Lease deposit + first month" lines** — neither document cross-references the other, and it's not clear whether these describe the same cash requirement twice or are genuinely additive.

---

## 4. What Would Actually Be Needed to Reconcile This (Not Attempted Here)

`CURRENT-STATE.md` §6 already states the answer, and this pass found nothing to change it: **"a fresh, itemised fit-out/equipment/legal/working-capital build against the current model... Anthony and an accountant/quantity surveyor should confirm before this figure is used in any real funding conversation."** Specifically, that fresh build would need to:

1. Start from a confirmed venue (none exists yet — `docs/VERIFICATION-TRACKER.md` item 3, still `BLOCKING`), since sqm-rate-based construction estimates are inherently provisional without a real tenancy.
2. Reconcile the `floor-plan-concept.md` vs. `CURRENT-STATE.md` §7.2 construction methodologies into one, or explicitly keep both with a stated reason.
3. Decide whether the 15% contingency (§2.6) applies on top of, or is already inside, the current headline ranges.
4. Resolve whether `grace-startup-plan.md`'s legal/lease lines are additive to or the same as `CURRENT-STATE.md` §7.3's legal/lease-bond line.
5. Get real quotes (3 builder quotes, an insurance broker, a QS) rather than market-research estimates for every major line.

**None of this was performed in this canonical-data phase**, per the coordinator's explicit scope limit ("resolve startup-capital conflicts unless the repo already has definitive evidence" — it does not).

---

## 5. What This Document Does Not Do

It does not pick a single authoritative startup-capital figure. It does not build the Master Financial Model, an Excel workbook, or any funding-requirement calculation. It does not resolve any of the conflicts listed in `data/canonical/startup_costs.yml`'s or `data/canonical/capex.yml`'s own `conflicts` lists. It does not obtain real quotes or engage an accountant/quantity surveyor. It does not choose Table 1 vs. Table 2 as primary (startup capital is not scenario-dependent on AM client volume in any document reviewed this pass, so this question does not directly arise here — flagged as an assumption, not independently proven).
