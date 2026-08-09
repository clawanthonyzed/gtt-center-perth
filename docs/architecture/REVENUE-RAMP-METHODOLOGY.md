# Revenue Ramp Methodology — Month 1-5+

**Date:** 2026-08-09 | **Type:** first bounded financial-model component, built on top of `docs/architecture/CANONICAL-REVENUE-METHODOLOGY.md` (adopted the same day, prior phase). **Not** the Master Financial Model, P&L, cash-flow forecast, Excel, or PDF — revenue ramp only.

---

## 1. What the Historical Ramp Was

Two historical ramp constructs exist in this repo, never previously cross-checked against each other's actual dollar figures:

1. **A blanket ramp-percentage shape (43%/64%/79%/93%/100%)**, applied identically to AM revenue and PM revenue, across Months 1-5+, in three separate documents: `docs/cash-flow.md`'s "18-Month Monthly Ramp" (10-client, A$55,000 AM ceiling), `docs/profit-loss-tables.md`'s "Year 1 Monthly Ramp" (12-client, A$66,000 AM ceiling), and `docs/investor-memorandum.md`'s "AM GTT Revenue — Monthly Ramp" (10-client, same as cash-flow.md). All three predate the 2026-08-05 Table 1/Table 2 rebase — none has ever been rebuilt against the current 18-client/12-client committed model.

2. **A PM session-count ramp (4/8/12/15/16 sessions/day)**, stated once, in `docs/pm-staffing-roster.md`'s "PM Revenue — Individual Services" table, with its own "Monthly PM Revenue" column.

Already canonical (Phase 6, unchanged this phase): `rev_ramp_pct_curve_historical` (the blanket shape, status SUPERSEDED, no replacement) and `rev_pm_session_ramp_historical` (the session-count ramp, status MODELLED) in `data/canonical/revenue_assumptions.yml`.

---

## 2. What It Appears to Have Meant

The blanket curve was applied as a **direct percentage multiplier on each month's steady-state ceiling**, separately for AM and separately for PM, then summed to a Total Revenue figure — not applied to client volume or session count directly, though (per §3 below) the arithmetic is mathematically identical either way for a linear revenue formula. No document states an underlying reason for the specific 5 numbers chosen (43/64/79/93/100) — no client-acquisition curve, referral-pipeline model, or external benchmark is cited anywhere.

---

## 3. What Was Tested

Per the coordinator's explicit instruction, five interpretations of "what does the ramp % apply to" were tested against the historical documents' own stated dollar figures:

| Interpretation | Tested against | Result |
|---|---|---|
| (A) Total revenue | 12-client model: 43% × (A$66,000+A$33,440) = A$42,760 | Matches `docs/profit-loss-tables.md`'s stated Month 1 Total (A$42,760) exactly |
| (B) AM revenue only | 43% × A$66,000 = A$28,380 | Matches the stated Month 1 AM figure (~A$28,380) exactly |
| (C) PM revenue only | 43% × A$33,440 = A$14,379 | Matches `docs/profit-loss-tables.md`'s stated Month 1 PM figure (~A$14,380) — but does NOT match `docs/pm-staffing-roster.md`'s own Month 1 PM figure (A$8,360) |
| (D) Client volume | 43% × 12 clients = 5.16, stated in `docs/investor-memorandum.md` as "~4-5 (43% of ceiling)" | Matches, and is mathematically identical to (B) since AM revenue is a linear function of client volume with fixed price/day-count |
| (E) AM/PM utilisation combination | — | Not separately meaningful — (A), (B), (D) are mathematically the *same* interpretation once (C) is confirmed to use the identical percentage, since scaling every additive component (AM, PM) by one common factor scales their sum by that same factor |

**Key mathematical finding, confirmed by direct arithmetic (not assumed):** because the blanket curve applies the *same* percentage to both AM and PM, interpretations (A), (B), (C), and (D) are not four competing hypotheses to choose between — they are algebraically equivalent, and all four reproduce `docs/profit-loss-tables.md`'s own historical Month 1-4 figures exactly (within normal rounding).

**The one genuine divergence found:** `docs/pm-staffing-roster.md`'s PM revenue figures do **not** match this blanket-curve interpretation — see §5.

---

## 4. What's Mathematically Valid

The blanket 43/64/79/93/100% curve, applied identically to AM and PM revenue, is internally coherent and exactly reproduces `docs/profit-loss-tables.md`'s own historical P&L ramp table (the document that actually feeds into a Net P&L calculation), `docs/cash-flow.md`'s equivalent table at the 10-client ceiling, and `docs/investor-memorandum.md`'s client-volume framing. This is the interpretation this document's new canonical ramp reuses (§6-8).

---

## 5. What Can't Be Determined — the PM Ramp Conflict

`docs/pm-staffing-roster.md`'s PM session-count ramp (4/8/12/15/16 sessions/day) is **also** internally coherent on its own terms — its "Monthly PM Revenue" column (A$8,360/16,720/25,080/31,350/33,440) matches `session_count × A$95 × 22 days` exactly at every month. But it does **not** match the blanket-curve PM figures used in the actual P&L ramp table (A$14,380/21,400/26,420/31,100/33,440) for Months 1-4 — only Month 5+ agrees, since both converge on the same 16-session/A$33,440 ceiling.

Expressed as a percentage of the 16-session steady state, the session-count ramp is **25%/50%/75%/93.75%/100%** — a materially different, slower-building curve than 43/64/79/93/100% for the first three months. Neither document cross-references the other or discloses this discrepancy anywhere. **This was not previously identified in this repo** — Phase 6's `rev_pm_session_ramp_historical` record flagged the two ramps as "a plausible distinction, not confirmed," but did not compute and compare their actual dollar outputs, which is what surfaced the conflict this phase.

**Cannot be determined:** which of the two PM ramps was "meant" to govern PM revenue specifically, or whether `pm-staffing-roster.md`'s table was intended only for staffing/payroll planning (session counts drive PM casual staff hours directly, per that same document's hours-based costing method) rather than as a revenue ramp at all. Both readings are plausible; this repo's saved working does not resolve it either way.

---

## 6. New Canonical Ramp Methodology

Built on top of `docs/architecture/CANONICAL-REVENUE-METHODOLOGY.md`'s formula (client volume × price × operating days, summed across AM/PM × weekday/Saturday). The ramp reuses the blanket 43/64/79/93/100% shape (§4's finding — the interpretation that actually matches the historical P&L revenue tables), applied identically to the canonical AM and PM steady-state totals for Table 1 and Table 2:

```
Month_Revenue(scenario, month) =
    (AM_steady_state(scenario) x ramp_pct[month] / 100)
  + (PM_steady_state x ramp_pct[month] / 100)     [PM is scenario-independent]
  + ancillary_monthly                              [currently A$0, does not ramp]
```

**Genuine extensions beyond the historical tables, disclosed:** (1) PM Saturday revenue (A$3,290.80/month at steady state) is included in the PM component and ramps by the same curve — the historical ramp tables never modelled PM Saturday at all, since Saturday trading and the canonical revenue methodology's PM Saturday line postdate them; (2) the base being scaled is the new canonical Table 1/Table 2 totals (A$155,215.80 / A$115,720.80), not either disputed historical ceiling (A$66,000 or A$55,000 AM-only) — this sidesteps, rather than resolves, `docs/VERIFICATION-TRACKER.md` item 37's base-ceiling mismatch (see §9).

**Status: MODELLED, not VERIFIED.** The ramp-percentage shape itself is reused, not re-derived — see `data/canonical/revenue_ramp.yml`'s `ramp_curve` record and `conflict_ramp_curve_origin_unknown` for full disclosure that this curve's own origin is undocumented anywhere in this repo.

---

## 7. Table 1 Results (18 clients/day)

Steady state: AM = A$118,485.00, PM = A$36,730.80, Total = **A$155,215.80/month**.

| Month | Ramp % | AM Revenue | PM Revenue | Ancillary | Total Revenue | % of Steady State |
|---|---|---|---|---|---|---|
| M1 | 43% | A$50,948.55 | A$15,794.24 | A$0.00 | A$66,742.79 | 43.00% |
| M2 | 64% | A$75,830.40 | A$23,507.71 | A$0.00 | A$99,338.11 | 64.00% |
| M3 | 79% | A$93,603.15 | A$29,017.33 | A$0.00 | A$122,620.48 | 79.00% |
| M4 | 93% | A$110,191.05 | A$34,159.64 | A$0.00 | A$144,350.69 | 93.00% |
| M5+ | 100% | A$118,485.00 | A$36,730.80 | A$0.00 | A$155,215.80 | 100.00% |

Implied client volume by month (informational, continuous-utilisation modelling, not a claim of a literal fractional headcount): M1 ≈7.74/day, M2 ≈11.52/day, M3 ≈14.22/day, M4 ≈16.74/day, M5+ = 18/day exactly.

---

## 8. Table 2 Results (12 clients/day)

Steady state: AM = A$78,990.00, PM = A$36,730.80 (identical to Table 1), Total = **A$115,720.80/month**.

| Month | Ramp % | AM Revenue | PM Revenue | Ancillary | Total Revenue | % of Steady State |
|---|---|---|---|---|---|---|
| M1 | 43% | A$33,965.70 | A$15,794.24 | A$0.00 | A$49,759.94 | 43.00% |
| M2 | 64% | A$50,553.60 | A$23,507.71 | A$0.00 | A$74,061.31 | 64.00% |
| M3 | 79% | A$62,402.10 | A$29,017.33 | A$0.00 | A$91,419.43 | 79.00% |
| M4 | 93% | A$73,460.70 | A$34,159.64 | A$0.00 | A$107,620.34 | 93.00% |
| M5+ | 100% | A$78,990.00 | A$36,730.80 | A$0.00 | A$115,720.80 | 100.00% |

Implied client volume by month: M1 ≈5.16/day, M2 ≈7.68/day, M3 ≈9.48/day, M4 ≈11.16/day, M5+ = 12/day exactly.

Both tables generated deterministically by `tools/revenue_ramp_model.py` and recorded in `data/canonical/revenue_ramp.yml`; reproducibility proven by `tests/test_revenue_ramp.py`.

---

## 9. Unresolved Assumptions

Per the coordinator's explicit "identify what remains genuinely unknown" instruction — none of the following are resolved by this phase:

1. **Real AM package mix** (Package 1 vs. Package 2) — unknown, `client_assumptions.yml#service_mix_am_package_split` remains PLACEHOLDER.
2. **PM package uptake** (Duo/Refresh/Glow) — not incorporated into any ramp figure.
3. **Saturday AM client volume assumption** — `saturday_volume_assumption` remains an inference (Saturday = weekday volume), not directly stated.
4. **PM Saturday sessions during ramp-up** — this phase assumes PM Saturday scales by the same blanket % as PM weekday; no source document states this explicitly (a new, disclosed extension, not a documented fact).
5. **Whether the ramp applies to clients, sessions, revenue, or utilisation** — mathematically equivalent for a linear formula (§3), so this specific ambiguity is resolved by the algebra, not by new evidence.
6. **Whether Table 1 and Table 2 should have different ramp curves** — not tested or assumed; both use the identical percentage shape, since nothing in this repo suggests otherwise.
7. **Whether the ramp should be linear/stepped/percentage-based** — the reused curve is percentage-based; no alternative shape was evaluated against real data (none exists — pre-launch venture).
8. **Whether ancillary revenue stays $0 in the ramp** — yes, per `rev_ancillary_excluded_from_baseline` (VERIFIED, unchanged), does not ramp.
9. **The PM 10% pre-booking discount** — not applied anywhere in the ramp, same treatment as the steady-state canonical methodology (`docs/architecture/CANONICAL-REVENUE-METHODOLOGY.md` §11).
10. **The origin of the 43/64/79/93/100% curve itself** — undocumented anywhere in this repo, at any point in its history (§10 conflict).

---

## 10. Conflicts

Both declared in `data/canonical/revenue_ramp.yml`'s `conflicts` list:

1. **`conflict_pm_ramp_two_interpretations`** (new finding this phase) — the blanket-curve PM ramp (used in this file) and `docs/pm-staffing-roster.md`'s session-count PM ramp are mutually inconsistent for Months 1-4, each correctly reproducing a different source document — see §5.
2. **`conflict_ramp_curve_origin_unknown`** (not new, but not previously logged as its own item) — no document states where the 43/64/79/93/100% shape came from.

Also relevant, not re-opened by this phase: `docs/VERIFICATION-TRACKER.md` item 37 (the pre-existing base-ceiling mismatch between `docs/profit-loss-tables.md`'s A$66,000 and `docs/cash-flow.md`'s A$55,000 AM ceilings) — this phase's canonical ramp sidesteps that conflict by using the new canonical Table 1/Table 2 totals instead of either disputed historical ceiling, but does not resolve which historical figure was "correct."

---

## 11. Relationship to the Eventual P&L / Cash-Flow Model

This document and `data/canonical/revenue_ramp.yml` supply the **revenue side only** of any future Month 1-5+ P&L. A real cash-flow/P&L model would still need: a matching cost ramp (fixed costs plus any genuinely variable costs, e.g. GTT supplies scaling with client volume per `docs/VERIFICATION-TRACKER.md` item 22), a marketing-spend ramp (already partially modelled in `docs/profit-loss-tables.md`'s "Marketing Spend Ramp" section, not yet canonicalised), and the resulting Net P&L per month. None of that is built here — this phase is revenue only, per the explicit scope limit.

---

## 12. Retained, Not Rejected

The 43/64/79/93/100% curve is **retained, not marked SUPERSEDED as a shape** — it is reused as-is for the new canonical ramp (§6), because it is the only ramp curve this repo has ever used, and it reproduces the actual historical P&L revenue ramp tables exactly. What **is** newly marked SUPERSEDED is its *base* — the old A$66,000/A$55,000 AM-only ceilings it was previously applied to, now replaced by the new canonical Table 1/Table 2 totals. `rev_pm_session_ramp_historical` (the 4/8/12/15/16 PM session ramp) remains SUPERSEDED, unchanged from Phase 6 — this phase did not elevate it to canonical, given the conflict found in §5.
