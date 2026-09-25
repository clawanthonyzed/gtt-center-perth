# GTT Center Perth — Staffing Forensics (Round 3, Priority 4, With AM Capacity/Bottleneck Cross-Check, Priority 6)

**Created:** 2026-09-25 (Round 3) | **Author:** Grace (Operations Manager)
**Purpose:** Where GTT's own labour assumptions are conservative vs dangerously optimistic, using real wage/turnover data; plus an AM capacity/bottleneck stress-test folded in here since phlebotomist availability is fundamentally a staffing question.

**Tagging:** `[VERIFIED]` / `[REPORTED]` / `[BENCHMARK]` / `[ESTIMATE]` / `[ASSUMPTION]` / `[UNKNOWN]`, `LOW CONFIDENCE — SINGLE SOURCE` flagged explicitly.

---

## 1. The Phlebotomist Wage Figure — a Material, Multi-Source-Validated Discrepancy

**This is the most financially material staffing finding of Round 3.**

**GTT's own canonical figure:** A$43,068/year per phlebotomist (A$86,136/year for 2), used throughout `docs/CURRENT-STATE.md`, `docs/financial-break-even-staff.md`'s payroll table, and every P&L figure in this repository `[VERIFIED — this venture's own primary document]`.

**GTT's own document already flags this figure as stale:** `docs/financial-break-even-staff.md` itself states, in its own text: *"Annual salary figures (A$56,237/A$62,774/A$60,456/A$43,068 etc.) above are NOT yet recomputed against these new casual rates... Do not silently blend an old annual figure with a new hourly rate."* The same document's own updated hourly-rate research gives the phlebotomist role (MA000027, Health Professionals Award, SS Level 1-2) a current casual rate of **A$33.71-35.04/hour** `[VERIFIED — this venture's own document, already researched, just not yet propagated to the annual figure]`.

**Independent cross-check performed this round (Tier 3, Glassdoor Perth data):** the average salary for a Pathology Collector in Perth is reported at **A$65,640/year** full-time-equivalent, with an hourly range of **A$27-33/hour** reported across submissions `[REPORTED — Glassdoor Perth salary aggregator, real submitted-data aggregator, not a single anecdote]`.

**Reconstructing the real annualised cost:** at the venture's own already-researched MA000027 casual rate (A$33.71-35.04/hour) for a 6-hour/day, 22-day/month AM-only role (1,584 hours/year, per `docs/financial-break-even-staff.md`'s own stated shift structure): **A$53,404-55,503/year per phlebotomist** `[ESTIMATE — this document's own arithmetic on the venture's own already-researched hourly rate, cross-validated directionally by the independent Glassdoor figure]` — **materially higher than the A$43,068/year figure currently baked into every canonical P&L figure**, a gap of roughly **A$10,336-12,435/year per phlebotomist, or A$20,672-24,870/year for both**.

**Confidence: Medium-High, not single-source.** Two independent sources (this venture's own MA000027 award research, and a fresh external Glassdoor check) converge on a materially higher figure than the A$43,068 currently used. This is not `LOW CONFIDENCE — SINGLE SOURCE` — it clears the hard rule's bar for a finding that materially affects the model.

**Financial impact, quantified:** applying the low end of the gap (A$20,672/year, A$1,722.67/month) directly reduces Table 1's steady-state Net P&L from A$35,186.40/month to approximately **A$33,463.73/month** (before any Workers Comp/superannuation flow-through recalculation, which would modestly widen the gap further) — a real, material, but not model-breaking reduction (roughly 5% of monthly profit). Applying the high end (A$24,870/year, A$2,072.50/month) reduces it to approximately **A$33,113.90/month**.

**Recommendation, not a decision:** this venture's own repository already has an outstanding, self-identified action item ("full payroll recompute") to propagate the updated MA000027 rate research into the annual salary figures — this Round 3 finding adds real, independent, cross-validated confirmation that this recompute is not a low-priority housekeeping item, it has a genuine, quantified ~A$20,700-24,900/year impact on the canonical model, concentrated in a single line item that has already been flagged as stale by the venture's own document but apparently not yet actioned through to `docs/CURRENT-STATE.md`.

---

## 2. Other Wage Lines — Spot-Checked, Not Fully Re-Audited

A full re-audit of every wage line (hairdresser, beauty therapist, PM service therapist) was out of scope for the time available this round — the phlebotomist line was prioritised because it was the one already self-flagged as stale in the venture's own document, making it the highest-value single line to validate. **Not re-checked this round, flagged as a remaining gap:** whether the hairdresser (A$60,456/yr) and beauty therapist (A$62,774/yr) annual figures carry the same "not yet recomputed against new casual rates" staleness — `docs/financial-break-even-staff.md`'s own disclaimer applies to "A$56,237/A$62,774/A$60,456/A$43,068 etc." as a set, suggesting all of them may carry the same gap, not just the phlebotomist line. This is a genuine, larger, unquantified remaining risk — see `MODEL-BREAKPOINTS.md`.

---

## 3. Real Australian Employee vs Contractor Considerations for Phlebotomists

**Finding, Tier 1 (ATO/Fair Work general guidance, not case-specific legal advice):** this venture's own 2026-09-19 founder decision confirms GTT Center Perth employs both phlebotomists directly (not as contractors, and not partner-supplied) `[VERIFIED — docs/CURRENT-STATE.md §0]`. This round did not find any new information suggesting this employment classification carries contractor-vs-employee misclassification risk (the role is directly analogous to any other casual/permanent salon employee, not a genuinely independent contracting arrangement) — **no new compliance concern identified here**, this section exists to confirm the question was checked, not to raise a new flag.

---

## 4. AM Capacity/Bottleneck Stress-Test (Priority 6, Folded In Here)

**GTT's own existing work is already extremely deep on this question** (`docs/scenario-c-sync-timetables.md`, `docs/architecture/AM-DEMAND-DRIVEN-STAFFING-TIERS-2026-09.md`) — solver-verified, zero-collision scheduling at both 12 and 18 clients/day. This round's contribution is narrower: cross-checking the **real-world attendance/no-show risk** against that theoretical model, using this round's own research.

**Theoretical capacity (already verified):** 18 clients/day, zero scheduling collisions, 8 treatment staff + 2 phlebotomists `[VERIFIED — existing repository solver work]`.

**Practical capacity, accounting for a real no-show rate:** Round 2 found general Australian medical no-show rates of 12-18%, but flagged that this may not apply directly to a mandatory GTT screening appointment. **This round's new evidence narrows that uncertainty meaningfully, without fully resolving it:** real industry sources found this round state that **collecting payment in advance (a deposit, or in GTT Center Perth's case, the full package price) is "the single most effective no-show prevention strategy,"** and that manual/no-reminder booking systems see 18-25% no-shows, while deposit-plus-automated-reminder systems (Fresha, which GTT Center Perth already uses, sends automated SMS/email reminders) see under 10% `[BENCHMARK — Phorest 2025 data, Zenoti 2026 data, both Tier 3/4 commercial sources, converging on a consistent range]`. **Because GTT Center Perth already collects full payment at booking (a stronger commitment device than a partial deposit) and already uses Fresha (which sends automated reminders), a more realistic practical no-show rate for the AM segment is likely in the 5-10% band, not the 18% general-medical average** — `[ESTIMATE — this document's own reasoning, combining GTT's own already-locked payment/booking-system choices with real external no-show-reduction benchmarks, LOW CONFIDENCE — no source directly measures no-show rates for a fully-prepaid mandatory medical test specifically]`.

**Stress capacity vs comfortable capacity, in the real-world sense (not the scheduling-collision sense already solved):** at 18 clients/day with a 5-10% real no-show rate, GTT Center Perth would realistically see **16-17 clients/day attend** on an average day, with occasional full-18 days and occasional lower days — this does not break the scheduling model (fewer arrivals loosens the solver's constraints, it does not tighten them) but it does mean **realised AM revenue is likely to run 5-10% below the designed-capacity revenue figure on an ongoing basis**, a real, quantifiable, previously unmodelled gap between designed and realised revenue. At Table 1's AM revenue contribution, a 5-10% shortfall represents roughly **A$4,950-9,900/month** in unrealised AM revenue at steady state `[ESTIMATE — this document's own arithmetic on GTT's own AM revenue figure]`.

**Phlebotomist single-point-of-failure economics:** `UNASKED-QUESTIONS-LOG.md` Q1 (Round 2) already flagged that relief/locum phlebotomist roles are real and advertised in the WA market. This round adds the real cost data point: at the corrected wage figure (Section 1 above, ~A$33.71-35.04/hour), a full-day relief phlebotomist shift (6 hours) costs approximately **A$202-210/day** `[ESTIMATE]` — a small, absorbable cost if a casual relief pool exists, but this venture's own model does not currently show a specific budgeted relief line for phlebotomists distinct from the general A$15,000/year Casual Relief Pool line, which covers all roles, not phlebotomists specifically. **Genuinely unconfirmed, flagged not assumed:** whether A$15,000/year is sufficient to cover realistic relief needs across all roles including phlebotomists, given the real turnover/absence rates found in `OWNER-OPERATOR-FAILURE-INTELLIGENCE.md` §5 (37% average industry turnover). This is a real, quantifiable gap worth a closer look once real staffing data exists, not resolved here.

---

## 5. Staff Turnover — Recurring Cost, Now Partially Quantified

Round 2 found real Australian beauty-industry turnover figures (37% average, 61% leave within first year) but did not attempt a dollar estimate. This round attempts a bounded estimate: if even 2-3 of GTT Center Perth's ~12-16 total staff turn over in a typical year (a conservative fraction of the 37% industry average, chosen because GTT's own dual-qualified/cross-trained role design may reduce turnover somewhat, per `OWNER-OPERATOR-FAILURE-INTELLIGENCE.md` §5's own hypothesis), and each replacement costs a conservative estimate of 2-4 weeks of reduced productivity plus recruitment/training time (no specific Australian recruitment-cost-per-hire figure was found this round for the beauty industry specifically, so this cannot be precisely dollarised) `[UNKNOWN — a specific per-hire cost figure for this industry was not found, flagged rather than invented]`. **This remains a genuinely unquantified, real, ongoing cost risk, not resolved this round** — logged in `MODEL-BREAKPOINTS.md` as a real but currently un-dollarised risk.

---

## Sources

`docs/financial-break-even-staff.md`, `docs/CURRENT-STATE.md`, `docs/scenario-c-sync-timetables.md` (this venture's own primary documents); Glassdoor Perth pathology collector salary data (Tier 3/4); Phorest 2025 and Zenoti 2026 no-show-reduction data (Tier 3/4, commercial booking-software research); `OWNER-OPERATOR-FAILURE-INTELLIGENCE.md` (Round 2, this repository).

---

## Changelog

**2026-09-25 (Round 3, created):** New file. Found and cross-validated (2 independent sources, not single-source) a material phlebotomist wage discrepancy (~A$20,672-24,870/year impact) already self-flagged as stale in the venture's own document but not yet propagated to the canonical model. Narrowed the AM no-show uncertainty range using real deposit/reminder-system benchmarks, without fully resolving it. Quantified the practical revenue gap between designed and realised AM capacity (~A$4,950-9,900/month). Left staff-turnover dollar cost genuinely unquantified, disclosed as unknown rather than invented.
