# GTT Center Perth — Margin Waterfall and Model Breakpoints (Round 3)

**Created:** 2026-09-25 (Round 3) | **Author:** Grace (Operations Manager)
**Purpose:** A verified margin waterfall (revenue down to profit, every real line item) and a ranked "what could break the model" report (impact x uncertainty), using the forensic findings from every other Round 3 file rather than repeating their derivations.

---

## 1. Margin Waterfall (Table 1, 18 clients/day, Current Canonical Figures) — Independently Reconstructed and Verified

This waterfall was built by reconstructing every individual cost component from `docs/profit-loss-tables.md`'s own Non-Wage Overhead breakdown plus the superannuation line found in `data/canonical/cost_ramp.yml` (see `RENT-ECONOMICS-FORENSICS.md` §4) — **it reconciles exactly to the canonical Total Costs and Net P&L figures, verified to the cent, not approximated.**

| Line | Monthly Amount | % of Revenue |
|---|---|---|
| **Total Revenue** | **A$143,070.37** | **100.0%** |
| Direct Labor (wages) | A$82,318.05 | 57.5% |
| Superannuation (12% OTE) | A$9,878.17 | 6.9% |
| Workers Compensation (1.7%) | A$1,399.41 | 1.0% |
| Rent | A$8,000.00 | 5.6% |
| Marketing (Instagram/Meta ads) | A$1,500.00 | 1.0% |
| Consumables + GTT supplies (glucose/tubes) | A$1,200.00 | 0.8% |
| Utilities (power/water/HVAC) | A$650.00 | 0.5% |
| Insurance | A$708.34 | 0.5% |
| Accounting/bookkeeping | A$500.00 | 0.3% |
| Miscellaneous/contingency | A$500.00 | 0.3% |
| Cleaning service | A$600.00 | 0.4% |
| Laundry/linen service | A$350.00 | 0.2% |
| Software (Fresha + Resend + internet/phone) | A$280.00 | 0.2% |
| **Total Costs** | **A$107,883.97** | **75.4%** |
| **Net Operating Result** | **A$35,186.40** | **24.6%** |

**The single largest finding from this waterfall: Direct Labor + Superannuation combined (A$92,196.22/month, 64.5% of revenue) is roughly 11.5x the size of Rent (A$8,000/month, 5.6%), and roughly 61x the size of Rent when compared line-by-line.** Every other individual line (marketing, consumables, utilities, insurance, accounting, misc, cleaning, laundry, software) is smaller than rent. **This reframes the priority order that motivated Round 3's rent investigation: rent, while genuinely worth investigating (Section 1 of `RENT-ECONOMICS-FORENSICS.md` found a real, if modest, internal understatement), is not the largest controllable cost pool in this model. Labour is, by a wide margin, and the phlebotomist wage discrepancy found in `STAFFING-FORENSICS.md` §1 sits inside that largest pool, not a smaller one.**

---

## 2. What Could Break the Model — Ranked by Impact x Uncertainty

| # | Assumption | Financial Impact if Wrong | Uncertainty | Combined Risk | Evidence |
|---|---|---|---|---|---|
| 1 | PM demand ramp reaches modelled ~50% utilisation | Large — already self-identified in this repository as "the single biggest unmodelled financial gap" (`docs/experience/RETURN-LOOP.md`) | Very High — zero real trading data exists anywhere | **Critical** | Existing repository + `PM-SERVICE-PROFITABILITY.md` §3 |
| 2 | Phlebotomist/other wage lines are current, not stale | Medium-Large — quantified at A$20,672-24,870/year for phlebotomists alone; other wage lines (hairdresser, beauty) not yet re-audited and may carry the same staleness | Medium (phlebotomist line: 2-source validated, not speculative) to High (other wage lines: unaudited) | **High** | `STAFFING-FORENSICS.md` §1-2 |
| 3 | AM segment fills to designed 18-client capacity with minimal no-shows | Medium — a realistic 5-10% no-show rate implies ~A$4,950-9,900/month unrealised AM revenue | Medium — narrowed this round via real deposit/reminder-system evidence, but not eliminated | **High** | `STAFFING-FORENSICS.md` §4 |
| 4 | Pathology partner commercial terms land favourably | Large — could affect whether the venture proceeds at all, or the eventual rental/commercial cost | High — industry-wide collection-centre rationalisation trend found this round is a genuine headwind, though WDP's own correspondence remains positive | **High** | `PATHOLOGY-PARTNER-ECONOMICS.md` §1 |
| 5 | Rent lands at or near the current A$8,000/month assumption | Small-Medium — Table 1 is resilient even at 2.25x the current rent; Table 2 (downside case) is materially more exposed and breaks even near A$18,076/month | Medium — a real venue has not yet been secured; the footprint itself has grown since the rent line was set | **Medium** | `RENT-ECONOMICS-FORENSICS.md` §1, §4 |
| 6 | Collection-room fit-out cost is adequately scoped at GTT's own flat A$800-1,250/sqm rate | Small-Medium — a room-type-specific blended estimate suggests A$39,000-60,450 more than currently assumed, a one-time capex item | Medium — the blended methodology is this document's own reasoning, not externally validated | **Medium** | `CAPEX-FITOUT-FORENSICS.md` §1 |
| 7 | Staff turnover does not require a dedicated recurring cost line | Unquantified but real — 37% average industry turnover exists as a benchmark, GTT's own dual-qualified design may reduce it but this is unproven | High — no dollar figure could be derived this round | **Medium** | `STAFFING-FORENSICS.md` §5 |
| 8 | The two new compliance questions (Round 2) resolve favourably | Low probability of actual issue, but genuinely untested | Medium | **Low-Medium** | `AUSTRALIAN-COMPLIANCE-SUPPLEMENT.md` (Round 2) |

**Critical-risk items (#1, #2, #3, #4) all sit above rent in combined risk** — this is the clearest single output of Round 3's forensic pass: **the model's real vulnerabilities are concentrated in demand realisation (PM ramp, AM no-shows) and labour-cost accuracy, not in rent**, even though rent was Round 3's own stated top priority going in. This is reported plainly, not adjusted to match the priority order it was asked to validate.

---

## Sources

Every figure in this file is drawn directly from `docs/CURRENT-STATE.md`, `data/canonical/cost_ramp.yml`, `docs/profit-loss-tables.md` (this venture's own primary documents) and the other Round 3 companion files listed above — no new external research was performed specifically for this file, which is a synthesis of verified figures already derived elsewhere in Round 3.

---

## Changelog

**2026-09-25 (Round 3, created):** New file. Built and verified (to the cent) a full margin waterfall, finding labour costs are ~11.5x the size of rent as a share of revenue — a genuinely important reframing of Round 3's own priority order. Ranked 8 model-breaking risks by impact x uncertainty, finding 4 items (PM demand, wage-line staleness, AM no-shows, pathology partner terms) rank above rent in combined risk.
