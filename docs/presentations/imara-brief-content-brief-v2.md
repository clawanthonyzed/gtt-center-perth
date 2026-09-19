# GTT Center Perth — Content Brief v2 for the Imara Presentation (Financial/Factual Rebuild)

**Prepared:** 2026-09-19 | **Prepared by:** Grace (Operations Manager), for the separate session rebuilding the Imara presentation from reconciled numbers
**Purpose:** Anthony reviewed the v1 presentation and sent back corrections that are real operating-model and financial-model decisions, not wording changes. This file resolves them properly in the repo's underlying model (canonical YAML + tools, not just prose), then restates every affected fact and number in one place. **This is not presentation prose, slide copy, or page design — facts and numbers only, same convention as v1.**

**Tagging convention (unchanged from v1, per `rules/CLAUDE.md`'s hard rule):**
- `[VERIFIED — source, date]` — confirmed by an external party or an independent programmatic check that is itself the primary source.
- `[MODELED — assumption: X]` — internally calculated from other modeled or verified inputs.
- `[PLACEHOLDER — not yet known]` — still a guess, or genuinely unreconciled.

**Pre-flight checks run before compiling this brief:** `pytest` → **168 passed** (0 failed). `python tools/check_consistency.py` → **0 findings**. See the "Tooling Flag" note at the end — the same pre-existing limitation flagged in v1 still applies (the checker's own hardcoded stale-pattern list does not include this round's new figures either way, so a clean run is not independent proof every figure is current — every figure below was cross-checked directly against a fresh run of the actual canonical tools, not against the checker's verdict alone).

**What changed in the underlying repo this round (real model work, not documentation-only):** `tools/cost_ramp_model.py` (Venue Manager Mon-Fri, PM session ramp corrected to 10/day, removed the now-unneeded PM M5plus anchor, added a parameterized AM-treatment-headcount function), `tools/revenue_ramp_model.py`'s inputs (`data/canonical/revenue_assumptions.yml`, `data/canonical/client_assumptions.yml`), two new tools (`tools/am_volume_tier_staffing_solver.py`, `tools/am_demand_tier_financial_ladder.py`) with their own test files, `data/canonical/cost_ramp.yml` and `data/canonical/revenue_ramp.yml` (all 10 records each, both scenarios), `data/canonical/revenue_assumptions.yml` (Model E PM transaction records, old Model C records superseded not deleted), `docs/CURRENT-STATE.md` (§0 new founder-decision banner, §4, §5, new §10 ladder section), `docs/VERIFICATION-TRACKER.md` (item 1d closed), two new architecture docs (`docs/architecture/PM-SESSION-CAPACITY-MODEL-E-2026-09.md`, `docs/architecture/AM-DEMAND-DRIVEN-STAFFING-TIERS-2026-09.md`), and 6 existing test files updated to match the recomputed figures (`tests/test_cost_ramp.py`, `tests/test_master_financial_model.py`, `tests/test_revenue_ramp.py`, `tests/test_revenue_methodology.py`, `tests/test_demand_scenario_financial_model.py`, plus `tools/demand_scenario_financial_model.py` itself).

---

## 1. Phlebotomist Employment Model — CLOSED

**SOLENA employs both phlebotomists directly (Option A, in-house) and performs the blood collection itself.** The external pathology partner's role is limited to lab transport and processing only — never blood collection, never a GTT Center Perth staff role. This closes the "in-house vs partner-supplied" question that was open from 2026-07-30 through this repo's last several rounds (Carole Rivers' WDP email had raised the possibility WDP might supply/employ the collector instead under a rental-clinic model — that possibility is now settled in favour of in-house employment). `[VERIFIED/DECIDED — Anthony's direct instruction, 2026-09-19]`

**No dollar change** — this was already the costed baseline in every prior financial model round; only the status tag moves from "contingent on an open question" to `[VERIFIED/DECIDED]`. AM weekday phlebotomist Direct Labor: **A$9,075.00/month** (2 phlebotomists × A$34.375/hr × 6hrs × 22 days), unchanged. AM Saturday phlebotomist Direct Labor: **A$2,679.19/month** (2 × A$51.5625/hr × 6hrs × 4.33 Saturdays), unchanged.

Updated in the repo: `docs/CURRENT-STATE.md` §0/§4, `docs/VERIFICATION-TRACKER.md` item 1d (closed).

---

## 2. Venue Manager Hours — Monday to Friday (was Monday to Saturday)

Recomputed on a 5-day week, per Anthony's direct instruction. `[DECIDED — Anthony's direct instruction, 2026-09-19]`

| | Was (Mon–Sat) | Now (Mon–Fri) |
|---|---|---|
| Weekday cost | A$320.00/day × 22 days = A$7,040.00/month | A$7,040.00/month (unchanged) |
| Saturday cost | A$480.00/day (×1.5 penalty) × 4.33 Saturdays = A$2,078.40/month | **A$0.00/month** |
| **Total Venue Manager monthly cost** | **A$9,118.40** | **A$7,040.00** |

**A$2,078.40/month direct-labor saving** (before super/workers comp; the full downstream saving after super/workers comp is folded into the payroll totals in §5 below).

**Genuine open gap, not resolved by this change and not papered over:** Table 1 trades Monday through Saturday — a full committed 6th trading day. This change does not say who covers Venue Manager duties (opening, reception oversight, rostering escalation) on Saturday. The existing "emergency fallback" cross-training rule (`docs/architecture/DEMAND-DRIVEN-STAFFING-MODEL.md` §4) is explicitly scoped to *"Monday–Friday, if VM01 is unexpectedly unavailable"* — it is not a standing answer for a routine, every-Saturday gap. No new role or cost is invented here to fill it. `[PLACEHOLDER — genuine operational gap, flagged not resolved]`

Updated in the repo: `tools/cost_ramp_model.py` (`VENUE_MANAGER_SATURDAY_DAILY`), `docs/CURRENT-STATE.md` §0/§4/§5.

---

## 3. Demand-Driven AM Staffing — Solver-Verified at 5 Volumes

Full method: `docs/architecture/AM-DEMAND-DRIVEN-STAFFING-TIERS-2026-09.md`. `tools/am_volume_tier_staffing_solver.py` extends the already-published, calibrated concurrency solver (`tools/demand_driven_staffing_solver.py`) to support odd client counts and to sweep pair cadence for each target volume, checking the widest cadence that still clears the WDP guidance window (last Draw 1 ≤ 10:30am). Calibrated against the already-published N=12/N=18 figures (8 staff) before being trusted on the new tiers — confirmed exactly.

### Rostered headcount by role and cadence, at each target volume

| AM clients/day | Rostered for (whole clients) | Pair cadence | Massage+Beauty | Nail Technician | Hairdresser | **Total treatment** | Phlebotomists |
|---|---|---|---|---|---|---|---|
| 9.00 | 9 | 45min (widened — **not yet a founder decision**) | 2 | 1 | 1 | **4** | 2 |
| 11.29 | 12 | 25min (committed) | 4 | 2 | 2 | **8** | 2 |
| 13.50 | 14 | 25min (committed) | 4 | 2 | 2 | **8** | 2 |
| 15.50 | 16 | 25min (committed) | 4 | 2 | 2 | **8** | 2 |
| 18.00 | 18 | 25min (committed) | 4 | 2 | 2 | **8** | 2 |

**Genuine, disclosed finding, not forced to fit expectations: only the lowest tier (9.00/day) can actually reduce treatment headcount below the committed 8.** The mathematics: reducing to 4 requires widening the pair cadence to 45 minutes or more (an already-published finding at 6 clients/day, now confirmed to extend up to 9 clients/day specifically). The WDP guidance window (last Draw 1 ≤ 210 minutes after a 07:00 start) caps how many pair-slots can fit at a 45-minute cadence at 5 (10 clients) — 11.29/day rounds up to 12 clients (6 pair-slots), whose own maximum feasible cadence is only 40 minutes, below the 45-minute threshold the reduction needs. This is a direct mathematical consequence of the synchronized-pair schedule and the fixed 60/120-minute clinical marks, not a modelling choice. **Phlebotomist headcount (2) is unaffected at every tier tested — structural, 2 collection chairs.**

**The 45-minute widened cadence at 9.00/day is a genuine finding, presented for Anthony's decision, not adopted as policy** — same status as the already-published 6-client/day finding. Requires: (a) confirming a 45-minute pair spacing is acceptable client-wait experience (per-client clinical timing is unaffected, only inter-pair spacing widens); (b) a real day-ahead rostering mechanism to know in advance a given day will be a genuinely low-volume day; (c) Anthony's explicit sign-off.

### Full financial ladder — revenue, wage cost, total operating cost, operating profit

| AM clients/day | Monthly payroll total | Monthly total revenue | Monthly total operating cost | **Monthly Operating Profit** |
|---|---|---|---|---|
| 9.00 | A$64,705.01 | A$83,827.87 | A$78,993.30 | **+A$4,834.57** |
| 11.29 | A$93,595.63 | A$98,901.79 | A$107,883.97 | **-A$8,982.18** (loss-making) |
| 13.50 | A$93,595.63 | A$113,449.12 | A$107,883.97 | **+A$5,565.15** |
| 15.50 | A$93,595.63 | A$126,614.12 | A$107,883.97 | **+A$18,730.15** |
| **18.00** | **A$93,595.63** | **A$143,070.37** | **A$107,883.97** | **+A$35,186.40 (planning case)** |

**Rounding convention:** each fractional volume (a continuous average daily-booking planning figure, the same convention this repo has always used for revenue) is rounded UP to the nearest whole client for STAFFING purposes only — you cannot roster a fractional client, and rounding up avoids understaffing risk. Revenue continues to use the exact fractional volume.

**A genuinely counter-intuitive result, disclosed rather than smoothed over: 9.00 clients/day (+A$4,834.57) is MORE profitable than 11.29 clients/day (-A$8,982.18).** This is real, not an error — 11.29 requires the full 8-staff headcount step-up while 9.00 does not, creating a real "valley" in the profitability ladder between roughly 9 and 12.655 clients/day (see break-even, §9). Below that valley or above it, the venue is profitable; inside it, at the currently-committed always-8-staff model, it is not.

**Role-by-role payroll breakdown at each volume:** see §5.

Source tools: `tools/am_volume_tier_staffing_solver.py`, `tools/am_demand_tier_financial_ladder.py`, tests in `tests/test_am_volume_tier_staffing_solver.py` and `tests/test_am_demand_tier_financial_ladder.py` (calibrated to match `data/canonical/cost_ramp.yml`'s and `revenue_ramp.yml`'s own Table 1 M5plus records exactly at the HIGH-headcount tier).

---

## 4. PM Model Rebuild — 10 Sessions/Day, Session-Consumption Reconciled, Pricing Locked

Full method: `docs/architecture/PM-SESSION-CAPACITY-MODEL-E-2026-09.md`. PM operates 13:00–18:00, the same Monday–Saturday operating days as the AM model.

**PM session capacity is now a directly-specified planning input: exactly 10 sessions/day (was 16), per Anthony's instruction.** A "session" is one treatment-staff appointment-slot. Each transaction type consumes a whole number of sessions — the resolved rule, not an open caveat:

| Transaction type | Sessions consumed | Why |
|---|---|---|
| Individual a-la-carte | 1 | One therapist, one continuous booking |
| PM Refresh (Massage 45min + Mini facial 30min) | 1 | ONE dual-qualified Massage+Beauty-pool therapist delivers both components sequentially — the venue's own established common-pool design |
| PM Restore (Gel manicure 45min + Blow-dry 30min) | 2 | TWO different specialists (Nail Technician + Hairdresser) — no confirmed dual Nails+Hair qualification anywhere in this repo |

Using the same disclosed 60% individual / 25% Refresh / 15% Restore mix assumption (still a planning estimate, not real booking data — the venue has not opened):

**Weighted sessions/transaction = 0.60(1) + 0.25(1) + 0.15(2) = 1.15.** **Weekday transaction capacity = 10 ÷ 1.15 = 8.6957/day** (was 12.8128 under the prior minutes-weighted method). **Saturday transaction capacity = 4.3478/day** (50% of weekday, same convention as before).

### PM pricing — locked as the resolved planning figure, not left unresolved

| Package/service | Duration | Price | Tag |
|---|---|---|---|
| PM Refresh (Massage 45min + Mini facial 30min) | 75 min | **A$185** (13% bundle discount vs A$212 bought separately) | `[MODELED — estimate, real Perth-comparable bundle pricing research, best current defensible planning figure]` |
| PM Restore (Gel manicure 45min + Blow-dry 30min) | 75 min | **A$135** (10% bundle discount vs A$150 bought separately) | `[MODELED — estimate, same basis]` |
| Individual a-la-carte average | — | A$84.11 (average of 9 representative catalogue midpoints) | `[CALCULATED — docs/architecture/SERVICE-CATALOGUE.md]` |
| **Blended PM average transaction value** (60/25/15 mix) | — | **A$116.97 ≈ A$117** | `[MODELED — estimate, unchanged by this round's session-count correction]` |

**Per Anthony's explicit instruction, this is presented as the resolved planning figure with a plain estimate label — not as "may be X% high" or unresolved.** Anthony's own final sign-off on the exact A$185/A$135 numbers has not been separately re-confirmed this round; they are the same figures already proposed and carried forward as the best current defensible planning prices.

### PM revenue

| | Transactions/day | Revenue/day | Days/month | Revenue/month |
|---|---|---|---|---|
| Weekday | 8.6957 | A$1,017.40 | 22 | **A$22,382.73** |
| Saturday | 4.3478 | A$508.69 | 4.33 | **A$2,202.64** |
| **TOTAL** | | | | **A$24,585.37** |

**PM revenue: was A$36,225.69/month (16-session, minutes-weighted method) → now A$24,585.37/month, a decrease of A$11,640.32/month (-32.1%)** — a genuine, direct consequence of Anthony's lower session target, not an error, and not framed as uncertain.

### PM labour cost

The existing labour-hours formula (`hours/role/day = sessions ÷ 4 roles ÷ 1.3 throughput`, floored at 3 hours) is unchanged, just fed the new 10-session input. **Genuine, disclosed finding: at 10 sessions/day, `10÷4÷1.3 = 1.923hrs/role` is now BELOW the 3-hour floor for every one of the 5 ramp months, including the former steady-state month** (the old 16-session target cleared the floor at 3.08hrs/role). **PM weekday labour is therefore now flat at A$9,808.92/month across the entire ramp — no more month-to-month increase, and no more special-cased "anchor" figure is needed in the model.** PM Saturday labour is unaffected (A$668.78/day, already floor-bound before this change). **PM labour total: A$12,704.78/month** (was A$12,966.32, a small A$261.54/month decrease — the floor was already absorbing most of the labour-cost effect; the revenue effect above is far larger).

---

## 5. Total Payroll Reconciliation — Role-by-Role, at Every Volume Tested

**At the 18-client/day committed volume (the headline figure):**

| Role | Monthly wage cost |
|---|---|
| Venue Manager (Mon-Fri) | A$7,040.00 |
| Phlebotomists (×2) | A$11,754.19 |
| Massage+Beauty pool (4 staff) | A$25,645.50 |
| Nail Technician (2 staff) | A$12,586.81 |
| Hairdresser (2 staff) | A$12,586.81 |
| PM dedicated casuals (Massage/Beauty/Nail/Hair, combined) | A$12,704.78 |
| **SUM (Direct Labor + Opening)** | **A$82,318.09** |
| + Superannuation (12%) | A$9,878.17 |
| + Workers Compensation (1.7%) | A$1,399.41 |
| **= PAYROLL TOTAL** | **A$93,595.67*** |

*\*A$0.04 rounding difference from the exact canonical figure (A$93,595.63, `data/canonical/cost_ramp.yml#cost_table1_m5plus`) — the canonical figure rounds each role's own weekday/Saturday sub-total once before summing; this table's role-level figures are individually correct, the cent-level gap is a disclosed rounding-order artefact, not a second, disagreeing calculation. Use A$93,595.63 as the authoritative figure.*

**At the other 4 volumes:**

| Role | 9.00/day (LOW, 4 treatment staff) | 11.29 / 13.50 / 15.50/day (HIGH, 8 treatment staff — identical to 18.00's own figures) |
|---|---|---|
| Venue Manager (Mon-Fri) | A$7,040.00 | A$7,040.00 |
| Phlebotomists (×2) | A$11,754.19 | A$11,754.19 |
| Massage+Beauty pool | A$12,822.75 (2 staff) | A$25,645.50 (4 staff) |
| Nail Technician | A$6,293.41 (1 staff) | A$12,586.81 (2 staff) |
| Hairdresser | A$6,293.41 (1 staff) | A$12,586.81 (2 staff) |
| PM dedicated casuals (combined) | A$12,704.78 | A$12,704.78 |
| **SUM (Direct Labor + Opening)** | **A$56,908.54** | **A$82,318.09** |
| + Superannuation (12%) | A$6,829.02 | A$9,878.17 |
| + Workers Compensation (1.7%) | A$967.45 | A$1,399.41 |
| **= PAYROLL TOTAL** | **A$64,705.01** | **A$93,595.63** |

Every role-by-role table above sums exactly to its own displayed total (confirmed programmatically, `tests/test_am_demand_tier_financial_ladder.py::PayrollAdditivityTests`).

---

## 6. Depreciation — Indicative

Basis: the A$251,198 Pre-Opening Capital planning figure's own itemised component breakdown (`data/canonical/startup_costs.yml#adopted_planning_scenarios`, see §8 below) — the fitout, equipment, furniture/fixtures/fittings, and technology-systems components specifically (not premises acquisition, opening inventory consumables, staffing-before-opening, marketing, professional services, or contingency, none of which are depreciable capital assets).

**Useful-life assumptions used (indicative, not independently confirmed with an accountant or the ATO's own effective-life determinations):**
- **Fit-out (leasehold improvement): 10 years, straight-line.** A common planning assumption for commercial fit-out; the actual figure depends on the eventual lease term and a proper accountant/ATO effective-life determination, neither of which exists yet.
- **Equipment, furniture/fixtures/fittings, and technology systems (combined): 5 years, straight-line.** A common planning assumption for salon/clinical equipment and furniture; same caveat.
- No residual/salvage value assumed (conservative — a real residual value would lower the depreciation charge slightly).

| Component | Base (A$) | Useful life | Annual depreciation |
|---|---|---|---|
| Fit-out | 139,678 | 10 years | A$13,967.80 |
| Equipment + Furniture/Fixtures/Fittings + Technology | 34,260 (19,280 + 14,160 + 820) | 5 years | A$6,852.00 |
| **TOTAL** | **173,938** | | **A$20,819.80/year** |

**Indicative monthly depreciation: A$1,734.98/month. Indicative annual depreciation: A$20,819.80/year.** `[MODELED — INDICATIVE, requires professional advice — accountant/ATO effective-life confirmation not yet obtained]`

---

## 7. Indicative Income Tax

**Entity structure is genuinely not settled** — `docs/architecture/ENTITY-STRUCTURE-INVESTIGATION.md` (2026-09-04) documents 3 live options (trust-direct, a new operating PTY LTD under the trust, or a fixed-distribution election under the 2026-09-03 draft federal trust-tax legislation), none decided, all requiring an accountant conversation.

**Indicative assumption used, stated plainly: the current small-business/base-rate-entity company tax rate of 25%** (aggregated turnover under A$50m, applicable to Option (b) — a new operating company — from the 3 live options). **Why this one:** it is the single most easily-stated, sanity-checkable rate of the three options. The trust-direct default (Option a) would instead flow to Anthony's and Imara's own personal marginal tax rates (which vary by person and are not modelled here — outside this repo's scope, Anthony's own adviser's territory) and, from 1 July 2028, potentially the new 30% discretionary-trust minimum tax unless Option (b) or (c) is also taken. Neither of those alternatives reduces to a single clean indicative rate the way the company rate does. **This is an indicative planning assumption only, not a claim about which entity structure will actually be used — that decision sits with Anthony and his accountant.**

| | Annual (18-client committed) |
|---|---|
| Operating Profit (Revenue − Operating Costs, before depreciation/tax) | A$422,236.80 |
| − Indicative depreciation (§6) | A$20,819.80 |
| = Indicative taxable base | A$401,417.00 |
| − Indicative income tax @ 25% | A$100,354.25 |
| **= Indicative after-tax result** | **A$301,062.75/year ≈ A$25,088.56/month** |

`[MODELED — INDICATIVE, requires professional advice — entity structure not settled, tax rate is an illustrative assumption only, not a determination]`

---

## 8. Return on Startup Capital

**Is A$251,198 still the current authoritative planning startup figure?** Yes — confirmed, no newer figure supersedes it in the repo (`data/canonical/startup_costs.yml#adopted_planning_scenarios`, approved "in principle" by Anthony 2026-08-10, Pre-Opening Capital scope). It sits alongside, not replacing, the older unreconciled ranges in `docs/CURRENT-STATE.md` §6 — this remains the newest planning-specific figure.

**Component breakdown — already itemised in the canonical data, sums exactly to A$251,198:**

| Component | A$ |
|---|---|
| Premises acquisition | 19,000 |
| Design and approvals | 4,100 |
| Fitout | 139,678 |
| Furniture, fixtures, fittings | 14,160 |
| Equipment | 19,280 |
| Opening inventory/consumables | 2,585 |
| Technology systems | 820 |
| Staffing before opening | 22,872 |
| Marketing and launch | 1,250 |
| Professional services | 539 |
| Subtotal before contingency | 224,284 |
| Contingency (12%) | 26,914 |
| **TOTAL** | **251,198** |

`[DECIDED — Anthony's own "in principle" approval, 2026-08-10, explicitly a planning figure, not a locked final cost, pending venue confirmation and final supplier/quote validation — docs/VERIFICATION-TRACKER.md item 49, still OPEN]`

**Indicative annual operating return** (Anthony's own specified measure — labelled exactly as this, not ROI, not IRR, not investment yield):

**Annual Operating Profit ÷ Startup Capital = A$422,236.80 ÷ A$251,198.00 = 168.09% (indicative annual operating return)**

`[CALCULATED — a simple ratio of two already-established figures, not a discounted or risk-adjusted return measure of any kind]`

---

## 9. Break-Even — Recomputed

**The previously-quoted 11.290 clients/day break-even figure is now stale and should not be quoted** — it predates this rebuild's demand-driven staffing and PM/Venue Manager changes. Because headcount now genuinely flexes by volume, break-even is not one number — it is two, segment-specific figures:

| Metric | LOW segment (4-staff, 45min cadence, not yet a founder decision) | **HIGH segment (8-staff, 25min cadence — the standing committed model)** |
|---|---|---|
| Break-even AM clients/day | 8.266 | **12.655** |
| Break-even clients/week (×6 trading days) | 49.59 | 75.93 |
| Break-even clients/month (×26.33 trading days/month) | ≈217.6 | ≈333.2 |
| % of the 18-client/day committed target | 45.9% | **70.3%** |

**Approximate share of the addressable market:** Perth metro GTT tests ≈515/week `[VERIFIED — KPMG analysis of ABS Births, Australia 2024]`, ≈2,231.7/month (515 × 52 ÷ 12). Break-even as a share of that: **≈9.75%** (LOW segment) or **≈14.93%** (HIGH segment). This comparison is responsible to make — both figures use the same already-verified ABS/KPMG-derived market-size basis this repo has used since 2026-07-31, not a new or unsupportable claim.

**Which to quote:** the **HIGH-segment figure (12.655 clients/day, ~70.3% of the 18-client committed target, ~14.93% of the addressable market)** is the correct figure to present as "the" break-even under the currently-committed operating model (always 8 treatment staff, no cadence widening adopted). The LOW-segment figure (8.266/day) is a real, solver-verified, secondary finding that applies only if Anthony separately adopts the widened-cadence, demand-flexed staffing approach for genuinely low-volume days — disclosed here as a distinct, conditional finding, not blended into a single misleading average.

**Margin of safety at the 18.00-client planning case:** 18.00 − 12.655 = **5.345 clients/day (≈29.7% of committed volume)** — narrower than the pre-rebuild margin (6.710 clients/day, ≈37.3%), a real, disclosed consequence of the lower PM revenue that is not offset by the smaller Venue Manager cost.

**Table 2 (12-client/day secondary reference), post-rebuild:** Net Operating Result is now **+A$1,096.40/month** (was +A$10,076.16) — thin but still positive; break-even 11.833/day, margin of safety 0.167 clients/day (~1.4%).

---

## 10. Pathology Partner Status — Current Position, All 4 Candidates

No new correspondence exists in this repo for any of the 4 candidates since the position recorded in the v1 brief (2026-09-12) — confirmed by checking the commit history of every pathology-related document; the most recent relevant commit is dated 2026-09-08. Current state only, no internal email history restated:

| Candidate | Status | What's confirmed | What's open | Next step |
|---|---|---|---|---|
| **WDP (Western Diagnostic Pathology) — PRIMARY** | In discussion, tone of the most recent reply is closing-sounding | Courier collection conditionally viable (fluoride oxalate tubes, ~24hr stable); GTT start-time guidance (not normally after 10:30am); no GP-on-site requirement | The commercial/rental figure; whether medical waste disposal is covered under WDP's setup | Awaiting a substantive reply to Anthony's 2026-09-08 follow-up |
| **PathWest — SECONDARY, progressing** | In discussion, most advanced of the 4 on courier confirmation specifically | PathWest can accommodate courier pickups for fluoride-oxalate tubes and will supply tubes/biohazard bags free | Cost (courier + lab testing); shape of any arrangement (contract/partnership/fee-for-service) | Awaiting Meera Bennett's answers to Anthony's 2026-09-03 email. **Anthony has explicitly deferred progressing this until WDP's outstanding follow-up is answered** |
| **Clinipath — CONTINGENCY** | Not yet confirmed — no engagement despite 3 contact attempts | Nothing confirmed | Everything — pure outreach status | Awaiting any reply to the 2026-09-07 send (3 addresses). Contingency only |
| **Australian Clinical Labs (ACL) — 4th candidate** | Awaiting reply, no engagement yet | Nothing confirmed | Everything | No follow-up planned yet — this venture's pattern is to wait ~3-4 weeks of silence before following up (first contact 2026-08-29) |

**Do not imply any of the 4 has a signed partnership.** The most advanced position of any candidate is PathWest's unconditional courier confirmation — a real, concrete step, but not a commercial agreement, and Anthony has explicitly chosen not to progress it further until WDP replies.

---

## 11. Current PM/AM Service Pricing — Actual Ranges

**Source:** `docs/services-pricing-locked.md` (canonical for the individual a-la-carte menu and AM package prices) and `docs/architecture/PM-PACKAGES.md` (PM package build, see §4 above for the two locked package prices).

**AM packages (only 2 tiers, no others):**
- Package 1 (fixed 2×30min): **A$250**
- Package 2 (flexible 2×45min / 1×45+1×30min / 2×30min): **A$300**

**AM GTT-window a-la-carte menu, actual price ranges (not an average):**

| Service category | Price range |
|---|---|
| Pregnancy massage (30/45min) | A$75 – A$120 |
| Pregnancy-safe facials (30/45min) | A$95 – A$130 |
| Nail services (under 60min) | A$55 – A$90 |
| Brows & lashes | A$30 – A$95 |
| Hairdressing (30/45min) | A$60 – A$85 |

**PM afternoon/standalone a-la-carte menu, actual price ranges (individual services longer than 45min, not available in the AM window):**

| Service category | Price range |
|---|---|
| Hairdressing extras (cut+blowdry, scalp treatment+blowdry) | A$90 – A$95 |
| Spray tan (automated booth) | A$55 – A$60 |
| Hair colour services | A$65 – A$400 (toner at the low end; full-head balayage/colour+blowdry at the high end) |
| Eyelash extensions | A$99 – A$280 |
| Belly casting | A$250 – A$330 (+A$75 for a return-visit decoration upgrade) |

**PM fixed packages (locked, see §4):** PM Refresh A$185, PM Restore A$135.

**Cafe (post-test-only):** A$3 – A$12. **Retail:** A$18 – A$105.

---

## What's Genuinely Unresolved — Read Before Presenting

- **PM package pricing (A$185/A$135):** presented as the resolved planning figure per Anthony's explicit instruction, but his own final line-by-line sign-off on these two exact numbers has not been separately re-confirmed this round.
- **Saturday Venue Manager coverage:** the Mon-Fri change creates a real, disclosed gap on who covers VM duties on Saturday — not answered by this brief, no cost invented to cover it.
- **The 45-minute widened-cadence staffing model (9.00/day tier, and the LOW-segment break-even of 8.266/day that depends on it):** a genuine, solver-verified finding, but explicitly not yet a founder decision — do not present it as the committed operating model.
- **Depreciation and indicative tax (§6, §7):** both genuinely indicative, using stated but not professionally-confirmed assumptions (useful life, entity structure/tax rate) — both explicitly require an accountant before being used in any real funding conversation.
- **A$251,198 startup capital:** Anthony's own "in principle" approval, not a locked final cost — still pending venue confirmation and final supplier/quote validation (`docs/VERIFICATION-TRACKER.md` item 49, OPEN).
- **Entity structure:** genuinely a live, 3-way, undecided question (`docs/architecture/ENTITY-STRUCTURE-INVESTIGATION.md`) — the 25% company tax rate used in §7 is illustrative only, not a claim about which structure will be chosen.
- **Final pathology partner:** none of the 4 candidates has a signed agreement (§10).
- **PM revenue mix (60/25/15 individual/Refresh/Restore split):** still a planning estimate, no real booking data exists — the venue has not opened.

---

## Tooling Flag — Read Before Trusting Any "Clean" Consistency Check

`tools/check_consistency.py` was run for this brief and returned **0 findings**, same as v1. This should **not** be read as proof every figure in this repo is current — the script's own hardcoded stale-value patterns were written to catch specific old, already-known-stale figures (e.g. the old A$63,028.75/A$27,084.69 Net P&L pair, the old A$200 package price, the old 8-client/10-client capacity figures). It does **not** have this round's new figures (A$35,186.40, A$143,070.37, A$107,883.97, etc.) in its pattern list either as canonical or as stale — a genuinely clean run is expected regardless of whether this round's changes were applied correctly or not. **Every figure in this brief was instead cross-checked directly against a fresh run of `tools/cost_ramp_model.py`, `tools/revenue_ramp_model.py`, `tools/master_financial_model.py`, `tools/am_volume_tier_staffing_solver.py`, and `tools/am_demand_tier_financial_ladder.py` — not against the consistency checker's verdict alone.** `pytest` (168 tests) provides the stronger guarantee here: every hardcoded expectation in the test suite was updated to match the recomputed figures and now passes, and several tests specifically cross-check the new demand-tier ladder against the canonical `cost_ramp.yml`/`revenue_ramp.yml` records to confirm they agree exactly at the committed 18-client tier.

---

## Sources Consulted (primary documents/tools this brief is built from)

`docs/CURRENT-STATE.md` (§0, §4, §5, §10), `docs/VERIFICATION-TRACKER.md` (item 1d), `docs/architecture/PM-SESSION-CAPACITY-MODEL-E-2026-09.md`, `docs/architecture/AM-DEMAND-DRIVEN-STAFFING-TIERS-2026-09.md`, `docs/architecture/DEMAND-DRIVEN-STAFFING-MODEL.md`, `docs/architecture/PM-CAPACITY-RECONCILIATION.md`, `docs/architecture/PM-PACKAGES.md`, `docs/architecture/ENTITY-STRUCTURE-INVESTIGATION.md`, `docs/services-pricing-locked.md`, `docs/reed-partnerships.md`, `data/canonical/cost_ramp.yml`, `data/canonical/revenue_ramp.yml`, `data/canonical/revenue_assumptions.yml`, `data/canonical/client_assumptions.yml`, `data/canonical/startup_costs.yml`, `data/models/master_financial_model.yml`, `tools/cost_ramp_model.py`, `tools/revenue_ramp_model.py`, `tools/master_financial_model.py`, `tools/am_volume_tier_staffing_solver.py`, `tools/am_demand_tier_financial_ladder.py`, `tools/demand_scenario_financial_model.py`.
