# GTT Center Perth — Package Price-Increase Timing: Financial Comparison

**Compiled:** 2026-07-19 | **Compiled by:** Grace (Operations Manager)
**Purpose:** New deliverable requested by Anthony — compare "increase package price at Month X" vs "keep price the same," using existing financial-model figures, to support the Q4 open-question decision (package price-increase timing) in `docs/05_open_questions_for_founder.md`.
**This document does not make the decision for Anthony — it lays out the financial comparison so he can.**

---

## 1. Source Figures Used (and their status)

This comparison draws on three existing documents, at different levels of currency:

| Source | Status | What it provides |
|---|---|---|
| `profit-loss-tables.md` v2.0 (2026-07-17) | **Current canonical baseline** | Weekday/Saturday/monthly/yearly P&L at the current committed model: Scenario C (10 AM clients/day, 07:00 start), A$250 conservative package price, PM individual services, no Sunday. |
| `financial-break-even-staff.md` §Sensitivity | Older model (pre-Scenario-C, pre-PM-individual-services correction) | The only existing blended-price sensitivity table in the corpus — shows what price levels are needed for various margin targets. Structure (3-package system with an old A$200 tier) is **superseded** — GTT Center Perth now runs only Package 1 (A$250) and Package 2 (A$300), renamed 2026-07-20. Used here for **illustrative price-elasticity direction only**, not as a literal current figure. |
| `cash-flow.md` | Partially superseded (see its own banner) | Month-by-month ramp and break-even timing context (Month 4 marginal, Month 5+ steady state) — directionally consistent with `profit-loss-tables.md` v2.0 even though its own per-line figures are stale. |

**Important caveat:** No document in this corpus has run a full month-by-month re-forecast under an explicit "price increases at Month X" assumption using the *current* Scenario C / 2-package model. What follows is a comparison built from the current baseline figures plus the direction/magnitude implied by the existing sensitivity table — it is a reasoned estimate, not a re-verified new financial model. If Anthony wants a fully rebuilt month-by-month forecast under a specific price-increase scenario, that is a follow-up task, not something already sitting in the existing docs.

---

## 2. Current Baseline (No Price Change)

Per `profit-loss-tables.md`, using the conservative A$250 AM package price throughout (Package 1, deliberately the lower of the two current packages, per standing instruction):

| Period | Net P&L (conservative baseline, no price change) |
|---|---|
| Weekday | +A$808.00/day |
| Saturday (AM+PM combined) | +A$1,580.50/day |
| Weekly | +A$10,490.50 |
| Monthly | +A$25,087.07 |
| Quarterly | +A$75,261.21 |
| Half-Yearly | +A$150,522.42 |
| Yearly | +A$301,044.84 |

This is the "keep price the same" case for the remainder of this comparison — every scenario below is measured as a delta against this baseline.

---

## 3. What a Price Increase Would Change

There are two distinct ways a "price increase" could be implemented, and they have different financial mechanics:

**Option A — Raise the AM package prices themselves** (e.g., Package 1 A$250 → A$270, Package 2 A$300 → A$320, or similar). This directly raises the A$250 conservative-baseline figure used throughout `profit-loss-tables.md`.

**Option B — Shift the client mix toward Package 2** (encourage/upsell more clients into the higher-priced, flexible-composition package instead of the fixed 2×30-min Package 1) without changing either package's sticker price. This raises the *blended average* revenue per client without a headline price change — softer from a marketing perspective, same effect on revenue.

The existing sensitivity table in `financial-break-even-staff.md` (built on the older 3-package model) shows the general shape of this relationship even though its literal numbers use a superseded price structure:

| Target margin | Blended avg needed (old 3-package model) | Illustrative interpretation for the current 2-package structure |
|---|---|---|
| Breakeven (0%) | A$289 | Roughly a A$39/client increase over the current A$250 conservative baseline |
| 5% margin | A$306 | Roughly a A$56/client increase |
| 8% margin | A$317 | Roughly a A$67/client increase |
| 10% margin | A$325 | Roughly a A$75/client increase |

**Reading this table correctly:** the current Scenario C model (`profit-loss-tables.md` v2.0) is already profitable at the A$250 conservative baseline (+A$25,087/month), which the older sensitivity table above was not (it was built under a loss-making pre-correction model). The table's absolute numbers should not be read as "GTT needs to reach A$289 to break even" today — that was true of an older, different model. What the table still usefully shows is the **rate of change**: roughly every ~A$17 of blended-average increase moves the margin outcome by about 1.7 percentage points in that older model's structure. Applied directionally to the current model, a modest price increase (e.g., A$10-20/client blended average) would be expected to meaningfully add to the already-positive monthly figure, not rescue a loss-making one.

---

## 4. Timing Scenarios — Increase at Month 3 vs Month 4 vs Never (Hold Steady)

| Scenario | Mechanics | Estimated effect |
|---|---|---|
| **Hold steady (no increase)** | Baseline above continues indefinitely. | +A$25,087/month from Month 5+ steady state (per `profit-loss-tables.md` v2.0), +A$301,045/year. Simple, no customer-facing price-change risk, no re-marketing needed. Leaves margin upside on the table if demand can absorb a higher price. |
| **Increase at Month 3** | Price rises before the venue has reached its Month 4 marginal break-even point (per `cash-flow.md`'s ramp timeline — note this timeline uses the older PM/staffing model, so the exact month labels are directional, not exact under the current Scenario C figures). | Higher risk: raising price while still building initial demand/reputation could slow the waitlist-to-booking conversion Anthony is relying on for the ramp. Financial upside (extra margin per client) arrives earlier, but is a smaller base (fewer clients/day early in the ramp) than the Month 4+ scenario, so the absolute A$ benefit of an earlier increase is smaller than it looks — the percentage benefit is front-loaded onto a smaller volume. |
| **Increase at Month 4** (HANDOFF.md's leaning recommendation) | Price rises at the point the venue crosses into (marginal) profitability, per the existing ramp narrative. | Lower risk: the pricing is already proven to work (demand held up) at the point of increase, and the venue is already covering its costs, so this reads as "capturing more margin from success" rather than "changing price to survive." Matches the standing recommendation already in `HANDOFF.md`. |
| **Increase later (e.g., Month 6+, after PM/AM capacity ceiling reached)** | Price rises once both AM and PM capacity are fully booked (Month 5+ steady state, per `profit-loss-tables.md` and `cash-flow.md`). | This is arguably the *lowest-risk and highest-leverage* timing of all three, though not explicitly modelled as a separate scenario in any existing document: once the venue is capacity-constrained (fully booked AM + PM), a price increase captures pure margin without needing to attract more clients — demand is already exceeding supply at that point (a full booking calendar is itself evidence pricing has room to move). This scenario is flagged here as worth Anthony's direct consideration, not because any existing document already models it. |

---

## 5. What This Document Does NOT Do

- It does not produce a new month-by-month dollar forecast under a specific price and specific month — that would require rebuilding the ramp model with current Scenario C figures and a stated price-increase assumption, which is a follow-up task, not something derivable purely from re-reading existing docs.
- It does not recommend a specific month. `HANDOFF.md` already carries a lean toward Month 4; this document adds the "wait until capacity-constrained" option as a fourth possibility worth weighing, without picking one.
- It does not model customer churn/demand-sensitivity to a price increase — no market research in this corpus tests price elasticity at the specific package price points in play. `capacity-pricing-audit.md` and `market-research-findings.md` may have adjacent context (not re-checked in full for this document — worth a look before finalising a decision).

---

## 6. Recommendation for Next Step (Not a Decision)

If Anthony wants to move from "financial comparison" to "confirmed number," the next step would be: pick a target month or trigger condition (a specific month, or "once at capacity" as flagged in §4), then have Bruno (finance agent) rebuild the month-by-month cash-flow model with that specific assumption plugged in against the current Scenario C baseline — rather than working from the older sensitivity table's superseded price structure as this document has had to do.

See `docs/05_open_questions_for_founder.md` Q4 for the standing open question this document supports.

---

## Changelog

**2026-07-20 (package renumbering)** — Updated "Package 2/Package 3" references to "Package 1 (A$250)/Package 2 (A$300)" per `services-pricing-locked.md`'s renumbering.
