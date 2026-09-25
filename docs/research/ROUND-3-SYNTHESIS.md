# GTT Center Perth — Round 3 Synthesis: Forensic Validation and Commercial Optimisation

**Created:** 2026-09-25 (Round 3) | **Author:** Grace (Operations Manager)
**Mission:** Not more breadth-first discovery (Round 2 already delivered that). For the highest-stakes findings so far: validate, narrow the uncertainty range, or prove the information genuinely cannot be obtained, and quantify what a wrong assumption would cost. Worked top-down through the given priority order, spending real time on 1-2, lighter but still substantive treatment on 3-9.

**A note on file structure:** the requested `VENUE-ECONOMICS-RESEARCH.md` was folded into `RENT-ECONOMICS-FORENSICS.md` §5 rather than built as a separate file — the real Perth property comparison against the rent budget is inseparable from the rent-economics investigation itself, and a second file would have duplicated the same 5 real candidates rather than adding new organisation. This is a deliberate deviation from the literal file list, in service of the standing "don't pad file count" instruction, disclosed here rather than silently done.

---

## Priority 1: Rent/Venue Economics — VALIDATED AND NARROWED, NOT FULLY RESOLVED

Full detail: `RENT-ECONOMICS-FORENSICS.md`.

- **Found a real, internal, quantified gap:** the A$8,000/month rent line was never recalculated after the venue footprint grew from 200sqm to 239-249sqm across two later founder decisions — a real ~A$1,560-1,960/month understatement at GTT's own originally-assumed rate, reducing Table 1's Net P&L by roughly 4-5% if corrected.
- **Resolved an apparent internal arithmetic gap:** the four cost lines shown in `docs/CURRENT-STATE.md` §5 don't sum to the stated Total Costs — traced this to a real, correctly-modelled but undisplayed superannuation line (A$9,878.17/month), not a computational error. Flagged as a documentation-completeness issue.
- **Narrowed, not resolved, the Round 2 rent-to-revenue contradiction:** GTT's own rent-per-sqm assumption is not obviously cheap relative to real current Nedlands/Osborne Park listings found this round — the 5.6% vs 24% gap is more likely explained by GTT's genuinely higher revenue-per-sqm (multi-service, pathology-throughput model) than an understated rent figure, though no directly comparable business type exists to confirm this with certainty.
- **Built a full rent sensitivity table** against the verified canonical arithmetic: Table 1 remains solidly profitable even at 2.25x the current rent assumption; Table 2 (downside case) breaks even near A$18,076/month, a real, quantified, previously unmodelled compounding risk if AM demand underperforms at the same time as a higher-than-expected lease lands.
- **Real property comparison, no recommendation made:** 53 Hardy Road, Nedlands remains the best layout match found across both research rounds, and remains the one candidate still missing real financial figures — the single highest-value next action for the venue search itself.

## Priority 2: Pathology Partnership Economics — ONE MATERIAL NEW FINDING, MULTI-SOURCE VALIDATED

Full detail: `PATHOLOGY-PARTNER-ECONOMICS.md`.

- **The Australian pathology industry, at the level of its two largest ASX-listed operators (ACL, Sonic Healthcare), is currently in an active collection-centre rationalisation phase** — driven by wage inflation, government-funding pressure, and margin protection, evidenced via real investor disclosures and earnings-call commentary, cross-checked across 2 independent companies. This is genuinely new, previously unidentified anywhere in this repository, and it materially changes the negotiating context for any new site proposal, including GTT Center Perth's.
- **Explicitly flagged as low-confidence when extrapolated to WDP specifically** — WDP is privately held, has no public disclosures, and its own direct, positive, progressing correspondence with this venture remains the more reliable evidence of WDP's own posture.
- **Built a ranged specimen-volume model** (9,500-14,000 specimens/year at Table 1 volume) from GTT's own real capacity data, reframing "what makes a site attractive" correctly as a volume/logistics question for the partner, not a per-visit fee question — GTT Center Perth does not pay the partner per test; the partner's revenue comes from the Medicare-rebated test itself.

## Priority 3: Real Operating Economics (Revenue Density) — CALCULATED FOR THE FIRST TIME, ONE BENCHMARK CORRECTLY REJECTED

Full detail: `OPERATING-ECONOMICS-BENCHMARK.md`.

- Calculated GTT's own implied revenue/sqm (A$6,894-7,183/year) for the first time anywhere in this repository.
- Deliberately rejected applying a US$1,000/provider-hour spa-industry benchmark to GTT's blended AM revenue-per-labour-hour figure, since the underlying revenue models (US per-treatment fee vs GTT's fixed package price across a mixed phlebotomist/treatment-staff shift) are not comparable — an example of correctly disqualifying a benchmark rather than misapplying it to manufacture a false finding.

## Priority 4: Staffing/Labour Productivity — THE SECOND MOST MATERIAL FINDING OF ROUND 3

Full detail: `STAFFING-FORENSICS.md`.

- **Found and cross-validated (2 independent sources, clears the "not single-source" bar) that GTT's own phlebotomist wage figure (A$43,068/year) is materially understated** relative to both the venture's own already-researched, not-yet-propagated MA000027 award rate and an independent Glassdoor Perth check — a real ~A$20,672-24,870/year gap, already self-flagged as stale in `docs/financial-break-even-staff.md` but apparently not yet corrected in `docs/CURRENT-STATE.md`.
- Other wage lines (hairdresser, beauty therapist) were not fully re-audited this round — flagged as a real, larger, unquantified remaining risk, since the venture's own staleness disclaimer applies to all of them as a set, not just the phlebotomist line.

## Priority 5: PM Service Mix Profitability — PREMISE CORRECTED, RISK ASYMMETRY EVIDENCED

Full detail: `PM-SERVICE-PROFITABILITY.md`.

- Corrected the working assumption that the room allocation is 4/4/4 — it is actually 3+3 pooled Massage/Beauty + 4 Nail + 4 Hair, per the venture's own current program.
- Connected the already-known fact that Nail and Hair have no cross-qualification pairing to this round's real evidence that staffing crises are a genuine, common industry risk — a real, evidenced structural asymmetry, not a reason to change the room counts (which were set by more rigorous solver work).

## Priority 6: AM GTT Capacity/Bottlenecks — REAL-WORLD ATTENDANCE RISK NARROWED

Full detail: folded into `STAFFING-FORENSICS.md` §4 (a staffing/capacity intersection, not a separate file, per the "don't pad file count" instruction).

- The scheduling-collision question is already solved by the venture's own solver work; this round's contribution was narrowing the real-world no-show risk (likely 5-10%, not the generic 18% medical average) using real deposit/reminder-system evidence, and quantifying the resulting realised-vs-designed revenue gap (~A$4,950-9,900/month).

## Priority 7: Startup Capex/Fit-Out — A REAL, MODERATE, ROOM-TYPE-SPECIFIC GAP FOUND

Full detail: `CAPEX-FITOUT-FORENSICS.md`.

- GTT's own flat construction-cost assumption (A$800-1,250/sqm) sits below real 2026 Australian allied-health fit-out benchmarks (A$1,800-2,800/sqm) for the collection-room-specific portion of the venue. Built a blended, room-type-specific estimate (A$230,200-359,200 total) that is a real but moderate A$39,000-60,450 above GTT's current flat-rate figure, concentrated in the genuinely clinical-grade portion of the fit-out.

## Priority 8-9: Customer Economics / Technology-Automation — UPSIDE ALREADY LATENT IN EXISTING DECISIONS

Full detail: `PROFIT-OPPORTUNITIES-ROUND-3.md`.

- No GTT-specific CAC/CLV figure exists or could be estimated pre-launch — genuinely unknown, not invented.
- Found that GTT's own already-locked decisions (full payment at booking, Fresha's automated reminders, referral-driven acquisition) already carry real, evidenced upside (lower no-shows, lower CAC than paid-channel acquisition) not yet explicitly modelled or messaged internally — the opportunity is measurement and awareness, not new spend.

---

## Margin Waterfall and Ranked Model Breakpoints

Full detail: `MODEL-BREAKPOINTS.md`. **The single most important structural finding of Round 3:** Direct Labor + Superannuation (64.5% of revenue) is roughly 11.5x the size of Rent (5.6% of revenue) in the verified margin waterfall. **This means the priority order Round 3 was given (rent first) does not match the priority order the evidence itself supports once quantified** — the ranked "what could break the model" list places PM demand realisation, wage-line staleness, AM no-shows, and pathology-partner terms all above rent in combined impact x uncertainty. This is reported plainly, as the evidence requires, not adjusted to match the brief.

---

## If Anthony Had to Make the Final Investment Decision Tomorrow: What From Round 3 Would Materially Change That Decision vs What Was Already Known?

**Nothing found this round changes the fundamental investment case.** The venture remains, on its own extensively-modelled numbers, solidly profitable at steady state under the committed Table 1 model, with real resilience to rent variation specifically. No locked figure was altered, and no finding this round constitutes a reason to pause or reconsider the venture.

**What genuinely would, and should, change how Anthony reads the model before signing anything major:**

1. **The phlebotomist wage correction (~A$20,672-24,870/year) should be actioned before any final financial commitment** — it is a real, cross-validated, already-partially-self-identified gap sitting in the single largest cost line in the entire model. This is the highest-value, cheapest-to-fix finding of the round: it requires an internal document update, not new research or negotiation.
2. **The pathology-industry rationalisation context should inform how the WDP commercial negotiation is approached** — not as a reason for concern about WDP specifically (whose own correspondence remains genuinely positive), but as context for why GTT Center Perth's own real specimen volume and appointment-scheduled predictability should be used explicitly as a negotiating asset, not left implicit.
3. **The rent line should be recalculated against the real, current footprint (239-249sqm) before the rent budget is used again as a comparison basis for any new property lead** — a small, mechanical correction, not a reason to reconsider the venture's viability, but one that should happen before, not after, a lease is signed.
4. **The collection-room fit-out cost should be re-scoped at a room-type-specific rate, not the flat salon-wide rate**, once a real venue exists — a real but moderate, one-time capex adjustment, not a reason to delay.
5. **The single most consequential unmodelled question remains unchanged from before this round: real PM demand.** Nothing in Round 3 narrows this uncertainty, because no external research can substitute for real trading data on a genuinely novel business model. This remains the one item where "we genuinely cannot know yet" is the correct, honest answer, not a research gap to keep chasing.

**In short: Round 3 sharpens and de-risks the existing plan meaningfully (two real, cheap corrections; two negotiating/awareness improvements) without surfacing anything that should change whether Anthony proceeds.**

---

## Full File List, This Round

`RENT-ECONOMICS-FORENSICS.md` (includes the venue-property comparison), `PATHOLOGY-PARTNER-ECONOMICS.md`, `OPERATING-ECONOMICS-BENCHMARK.md`, `STAFFING-FORENSICS.md` (includes the AM-capacity real-world cross-check), `PM-SERVICE-PROFITABILITY.md`, `CAPEX-FITOUT-FORENSICS.md`, `MODEL-BREAKPOINTS.md`, `PROFIT-OPPORTUNITIES-ROUND-3.md`, and this file.

---

## Changelog

**2026-09-25 (Round 3, created):** Final synthesis file for the forensic-validation-and-commercial-optimisation round. Structured around the given priority order, ending with an explicit, honest answer to the "would this change tomorrow's investment decision" question: no, but it identifies two cheap corrections (wage line, rent-footprint reconciliation) and two negotiating/awareness improvements (pathology volume leverage, no-show/CAC awareness) worth actioning before any major commitment. Explicitly reports that the evidence-ranked risk order does not match the given priority order (labour and demand risk outrank rent), rather than adjusting the finding to fit the brief.
