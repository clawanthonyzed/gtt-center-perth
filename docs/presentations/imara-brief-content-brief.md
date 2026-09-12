# GTT Center Perth — Content Brief for the Imara Presentation

**Prepared:** 2026-09-12 | **Prepared by:** Grace (Operations Manager), for the separate session building the Imara presentation PDF
**Purpose:** One reconciled, sourced, single-source-of-truth file to build the presentation from. Not presentation copy — facts and numbers only, tagged per this repo's own governance convention.

**Tagging convention used throughout (per `rules/CLAUDE.md`'s hard rule, this repo's own — not the 4-label scheme originally proposed for this brief, corrected per the coordinator's mid-task note):**
- `[VERIFIED — source, date]` — confirmed by an external party or an independent programmatic check that is itself the primary source.
- `[MODELED — assumption: X]` — internally calculated from other modeled or verified inputs.
- `[PLACEHOLDER — not yet known]` — still a guess, or genuinely unreconciled.

**Canonical sourcing used for this brief, per direct correction from the coordinator mid-task:**
- `docs/CURRENT-STATE.md` — single canonical source for package prices, client capacity, headcount, monthly P&L, startup capital range. Used first; not re-reconciled against `financial-model.md`/`break-even-sensitivity-analysis.md`/`scenario-comparison-master-2026-08.md` myself.
- `docs/VERIFICATION-TRACKER.md` — single running list of what's open/unconfirmed. Used as-is, not rebuilt.
- `data/models/master_financial_model.yml` and `data/canonical/cost_ramp.yml` — the deterministic outputs `CURRENT-STATE.md` itself points to for its most recent (2026-08-21) recompute; used to get exact current break-even/sensitivity figures that `CURRENT-STATE.md`'s prose doesn't spell out line-by-line.
- Architecture-layer docs (`docs/architecture/*.md`, `docs/experience/*.md`, `docs/strategy/*.md`) used only for narrative/methodology detail, never to override a `CURRENT-STATE.md` figure.

**Pre-flight checks run before compiling this brief, per repo rule:** `python tools/check_consistency.py` → **0 findings** across all `docs/*.md`. `pytest` → **141 passed**. See the "Tooling Flag" note at the very end of this document — the consistency checker's own hardcoded "canonical" P&L figure is itself stale and does not catch the most recent staleness; do not rely on a clean check_consistency.py run alone as proof a figure is current.

---

## 0. Is `docs/gtt-center-perth-overview-for-imara.md` current? Should it be the starting point?

**No. It is confirmed stale — do not use it as a starting point for anything.** Dated 2026-07-20, it describes:
- The old 10-client/day AM model (not 18/day) — capacity language "~220 visits/month," "10/day."
- Old monthly profit figure "~A$25,000/month" and "~A$301,000/year" (both far below the current reconciled figures).
- Old startup-cost range "A$209,000-431,000."
- The old A$88,600/month cost-coverage framing.

This document has not been touched since 2026-07-20 while the operating model, financials, staffing, venue program, and brand have all moved substantially since. It should not be read, cited, or used as a scaffold for the new presentation — this brief supersedes it entirely for content purposes.

---

## 1. The Concept — Plain Language, No Medical Claims

**What a GTT is:** every pregnant woman in Australia undergoes a mandatory gestational glucose tolerance test around 24–28 weeks' gestation. In its ordinary form this is a 2–2.5 hour appointment involving three blood draws at fixed clinical intervals, with the patient waiting between draws in a standard pathology waiting room.

**What the current typical experience looks like:** an ordinary pathology clinic waiting room — fluorescent lighting, plastic chairs, no service beyond the test itself. Nothing about the wait itself is designed for the person going through it.

**Why that's an opportunity:** the test is mandatory and recurring — this is not a business that has to create demand from nothing; it is built around a stream of women who must attend, for medical reasons, regardless of the economy or marketing spend. `[MODELED — market-opportunity framing, not itself a figure requiring a tag]`. As far as this venture's research has found, no directly comparable business exists in WA; one comparable business exists in Melbourne `[MODELED — market-research-findings.md, not independently re-verified this session]`.

**What GTT Center Perth changes:** the wait itself becomes a wellness visit. While the pathology partner's collection process runs on its own required clinical schedule, the same time is filled with massage, beauty, nails, and hair services delivered by the venue's own employed staff. The clinical blood draws and lab processing are handled entirely by an external pathology partner operating under its own accreditation; GTT Center Perth's own staff never perform or interpret the test itself.

**Model discipline, non-negotiable for the presentation:** beauty/wellness practitioners and phlebotomists are **employed staff** (casual or part-time), not subtenants and not independent contractors renting space. `docs/workflow.md`'s older "subtenant" framing is superseded and must not be used — see §12 below.

**No diagnostic or regulatory claims to make in this document or the presentation without a current WA Health/AHPRA citation.** Nothing in this brief asserts NATA accreditation, clinical certification, or a regulatory guarantee beyond what is explicitly sourced below (§10).

---

## 2. AM + PM Operating Model — What Actually Happens, Not the Simplified Version

**Flag, addressed directly per the coordinator's brief:** the AM/PM description given in the original task brief ("AM = GTT collection, ≤45 min... PM starts ~12:30pm") does not match this repo's actual, current, solver-verified operating model. The real model is more specific and is given below — use this version, not the simplified one.

### AM window (07:00–13:00, Monday–Saturday)

- **18 clients/day, 9 synchronised pairs, 2 collection chairs, 07:00 start, 25-minute pair cadence.** `[VERIFIED — scenario-c-sync-timetables.md §0.6a, hard-constraint solver, zero chair/phlebotomist collisions across all 153 pairwise checks]`
- Each client's own visit: **Draw 1 (5 min) → Service 1 (45 min) → 10-min buffer → Draw 2 at exactly +60 min (5 min) → Service 2 (45 min) → 10-min buffer → Draw 3 at exactly +120 min (5 min) → depart.** Total per-client visit ≈ 2 hours 5 minutes of clinical/service time. `[VERIFIED — docs/architecture/OPERATING-MODEL-18-CLIENTS.md §2, sourced from the same solver-verified timetable actually sent to WDP]`
- Last Draw 1 of the day: 10:20am — 10 minutes inside WDP's own "not normally after 10:30am" guidance. Last departure ≈12:33pm. `[VERIFIED — same source]`
- **This is NOT a "≤45-minute GTT collection" model** — each of the two wellness service slots is ≤45 minutes; the clinical process itself spans the full ~2-hour draw interval, exactly as the real test requires. Correcting this in the brief avoids a factual error appearing in the presentation.
- Phlebotomy is **employed, in-house staff** in the current modelled baseline (2 phlebotomists, one per chair) — see §10 for the still-open question of whether the eventual pathology partner instead supplies/employs the collector under a rental model.
- The pathology partner's role is limited to sample transport and lab testing/reporting under GTT's proposed self-collection model (see §10) — GTT Center Perth's own revenue never includes the pathology fee itself, which is billed separately.
- **No AM gap-fill capacity exists at full 18-client volume** — every treatment slot is already allocated to a GTT client's Service 1 or Service 2. `[VERIFIED — docs/architecture/OPERATING-MODEL-18-CLIENTS.md §2]`

### PM window (13:00–18:00, Monday–Saturday)

- Standalone/self-booked wellness clients — no clinical test in the afternoon (fasting requirement is AM-only).
- Individual a-la-carte services (30/45/50/55/60/75/90+ minute slots depending on service — see §5) plus two fixed PM packages (PM Refresh, PM Restore, both 75 minutes) `[MODELED — docs/architecture/PM-PACKAGES.md, pricing not yet signed off by Anthony, see §5]`.
- PM capacity basis: 16 treatment-staff sessions/day across 4 lines (Massage, Beauty, Nails, Hair), ~50% utilisation of theoretical capacity `[MODELED — no real booking data yet]`. **A genuine, quantified open item exists on how many actual client transactions this converts to once package bookings (which consume 2 sessions per 1 transaction) are accounted for — see §7's note on PM revenue.**
- PM Reception is **not** a separate paid role in the current committed model — rostered PM treatment staff handle check-in/payment/Fresha administration during natural gaps in their own paid bookings (Model C), per Anthony's direct 2026-08-21 decision, overriding an earlier recommendation for a dedicated PM Reception hire. `[VERIFIED — Anthony's direct instruction, 2026-08-21, docs/CURRENT-STATE.md §5]`

### AM-to-PM transition

Not a formal handover — different people, different shift patterns, no scheduled handover meeting, per Anthony's explicit instruction. `[VERIFIED — Anthony's direct instruction, docs/architecture/OPERATING-MODEL-18-CLIENTS.md §1]` AM treatment staff may be rostered into the PM window on a given day if booking demand supports it, but this is a day-to-day rostering choice, not a structural double-shift.

---

## 3. Customer Journey — Step by Step

Two journeys exist in parallel and share a physical space and brand: **AM (GTT, referred)** and **PM (standalone, self-booked)**. `[VERIFIED — docs/experience/CUSTOMER-JOURNEY.md, current, name-agnostic]`

1. **Referral / Discovery** — AM clients arrive via a midwife/OB referral (a low-control brand moment: the referrer's own description does real work). PM clients discover the venue independently (social, word of mouth, search).
2. **Website / Booking** — Two clearly separated entry paths (book a morning / book an afternoon), not one undifferentiated flow. Minimal-friction booking, first name collected early.
3. **Confirmation / Pre-arrival** — A reassuring, specific reminder the night before for AM guests (the single highest-leverage pre-arrival touchpoint identified in this venture's own experience research); practical reminder only for PM guests.
4. **Arrival** — AM: nervous, possibly fasting since the prior night; reception recognises her by name, no clinical intake-style questioning. PM: expects a normal premium salon arrival.
5. **GTT clinical process (AM only)** — Draw 1, glucose drink, then the two wellness service slots interleaved with Draw 2 and Draw 3 exactly as described in §2. A physical welcome/itinerary card is handed over at arrival listing her personal timetable by clock time, the staff member assigned to each treatment, her selected post-test food/drink choice, and a Google review QR code. `[VERIFIED — docs/experience/CUSTOMER-JOURNEY.md, card contents confirmed by founder instruction, 2026-08-16]`
6. **Optional AM-to-PM transition** — an AM client may, subject to availability, extend her visit into a PM booking, but this is not built into the committed AM schedule as spare capacity (see §2 — the AM day is fully allocated at 18 clients).
7. **Departure** — Food/drink service is post-test-only (the client remains fasting until the final draw completes). **A previously-described "leaving box"/parting-gift concept was explicitly REMOVED by Anthony's direct decision, 2026-08-19 — do not include any gift/parting-item mechanic in the presentation.** `[VERIFIED — Anthony's direct instruction, 2026-08-19]` The departure moment remains a genuinely open design question, not a locked feature.
8. **Follow-up** — Results are communicated to the referring doctor by the pathology partner, not to GTT Center Perth (no medical role for venue staff). A follow-up touchpoint tells the client what happens next rather than pushing a rebooking upsell.
9. **Rebooking / long-term relationship** — the AM guest discovers the PM standalone business on its own terms afterward, not as an in-visit upsell.

---

## 4. Venue Requirements — Conceptual Zones Only (No Addresses, No Sizes)

Per the hard constraint on this brief: no property addresses, no comparison tables, no square-metre figures. The table below is the physical **program** the venue must accommodate — what each zone needs, not where or how big. `[VERIFIED/CONFIRMED — docs/architecture/VENUE-PROGRAM-AUTHORITATIVE.md, current as of 2026-08-22, updated 2026-09-04]`

| Zone | What it needs | Status |
|---|---|---|
| Blood Collection | **2 separate rooms, one per phlebotomist** (each with its own solid walls, one door, no public-facing window) — a founder decision for extra client privacy, overriding an earlier evidence-based recommendation for a single shared room | Confirmed (founder decision, closed 2026-08-27) |
| Massage | Stations for the shared Massage+Beauty treatment pool; table/bed format (not chair-based); curtain-partitioned | Confirmed count and format |
| Beauty | Stations shared with the Massage pool; curtain-partitioned | Recommended |
| Nail | Open-plan stations with dust/LEV extraction | Confirmed count; ventilation needs professional verification |
| Pedicure | Same zone as Nail, hygiene-mandatory pipeless chairs | Confirmed |
| Hair Wash | Backwash stations, open-plan | Confirmed |
| Hairdresser | Open-plan styling stations | Confirmed |
| Reception | Workstations, Fresha/payment terminal | Confirmed |
| Cafe | A counter zone, adjacent to the Lounge, post-test-only service, WA Food Business Risk Classification researched at Low risk | Confirmed model; council notification still outstanding |
| Lounge | Seated waiting area (couches, not reclining chairs), kiosk-mounted tablets | Site-dependent on final seat count |
| Staff area | Back-of-house room — lockers, table, kitchenette | Confirmed |
| Storage | Clean linen, dirty linen/biohazard, general storage, physically segregated from the Cafe's food/drink storage (NPAAC requirement) | Confirmed; biohazard waste-disposal arrangement still open with the pathology partner |
| Toilets | Accessible patient WC, standard patient WC, staff WC | Professional verification required (AS 1428.1 accessibility) |
| Circulation | Corridor/circulation space | Confirmed |

**Genuinely still open, not resolved here:** the growth path if a 3rd collection room or a 2nd chair in an existing room is needed later; whether the centrifuge, specimen fridge, and reclining chair are shared or duplicated between the 2 collection rooms.

---

## 5. Services and Pricing — Reconciled

**Reconciliation note:** `docs/services-pricing-locked.md` (CURRENT/CANONICAL for pricing) and `docs/architecture/PM-PACKAGES.md` (the PM package build) do not conflict — they cover different parts of the menu and are combined below. `docs/services-master-table.md` is the durations/service-list companion to the same pricing, also current, no discrepancy found.

### AM (GTT-window) packages — the only revenue model financial figures should use

| Package | Composition | Price | Tag |
|---|---|---|---|
| Package 1 | Fixed: 2 × 30-minute services from the GTT-window menu | **A$250** | `[MODELED — Anthony's locked launch price, not externally market-tested]` |
| Package 2 | Flexible: 2×45min, or 1×45min+1×30min, or 2×30min | **A$300** | `[MODELED — same basis]` |

Venue + lounge access (water, herbal tea, GTT coordination, welcome/itinerary card) is bundled free into both packages — no separate venue fee. Financial modelling uses Package 1's A$250 price as a deliberate conservative safety price, not a blended average. `[MODELED — standing instruction]`

**GTT-window a-la-carte menu (all ≤45 min, available inside the two service slots):** pregnancy massage (30/45 min, A$75/A$120), pregnancy-safe facials (30/45 min, A$95/A$130, extensive add-on menu), nail services under 60 min (manicure/pedicure A$55–A$90), brows and lashes (A$30–A$95), hairdressing 30/45 min (blowdry/haircut/braiding, A$60–A$85).

### PM (afternoon/standalone) — individual services + 2 fixed packages

- **Individual a-la-carte:** the full afternoon menu including longer services not available in the AM window (60-min massage, 60/75-min facials, mani+pedi combos, acrylics, hair colour 60–240 min, lash extensions, belly casting). Individual a-la-carte average price A$84.11, calculated from 9 representative services' catalogue midpoints. `[CALCULATED — docs/architecture/PM-PACKAGES.md §5, from docs/architecture/SERVICE-CATALOGUE.md]`
- **PM Refresh** (Massage 45min + Mini facial 30min, 75 min total): **A$185** (13% bundle discount vs buying separately). `[MODELED — real Perth-comparable bundle pricing research, not yet signed off]`
- **PM Restore** (Gel manicure 45min + Blow-dry/styling 30min, 75 min total): **A$135** (10% bundle discount). `[MODELED — same basis]`
- **Blended PM average transaction value: A$117** (60% individual / 25% PM Refresh / 15% PM Restore mix assumption). `[MODELED — planning estimate, no real booking data]`
- **PM package pricing itself still requires Anthony's final sign-off** — direction is confirmed, exact prices are not yet locked. `[PLACEHOLDER — docs/CURRENT-STATE.md §2, docs/architecture/PM-PACKAGES.md §6]`
- 10% online pre-booking discount applies to afternoon/standalone services booked at the same time as a GTT reservation; full price applies to same-day/in-centre upsells.

**Cafe (post-test-only):** water, sparkling water, herbal tea, protein bars, fruit cups, snack packs, A$3–A$12. **Retail:** CGM sensors, low-GI recipe books, GDM snack packs, take-home nail polish, A$18–A$105.

---

## 6. Staffing Model — Roles, Headcount, Hours, Wages

**Source:** `docs/architecture/STAFF-POSITION-REGISTER.md` (current as of 2026-08-23, the single authoritative position-ID register) reconciled against `docs/CURRENT-STATE.md` §4 (committed headcount) and the 2026-08-18 audit-round wage correction. Where the register's "recommended" pool size (including relief) differs from the **committed** headcount actually costed in the P&L, both are shown — do not present the recommended relief-pool total as if it were the costed headcount.

| Role | Committed headcount (costed in the P&L) | Recommended full pool (incl. relief, not all costed) | Hours | Wage rate | Tag |
|---|---|---|---|---|---|
| Venue Manager | 1 (new hire, not yet in place) | 1, no relief pool — single point of failure, disclosed | 07:00–15:00, Mon–Sat | **A$40.00/hr**, Hair & Beauty Industry Award MA000005 Level 6 ("salon manager" classification) | `[MODELED — researched-best-evidenced, corrected 2026-08-18 from an earlier Clerks Award misclassification]` |
| Phlebotomist (Chair A / Chair B) | 2 | 4 recommended (2 committed + 2 relief; 3 is the disclosed lower bound) | 07:00–13:00, Mon–Sat | **A$33.71–35.04/hr** (A$34.375/hr midpoint), Health Professionals Award MA000027 | `[MODELED — researched 2026-08-16, not yet propagated through every legacy annual-salary figure in this repo]`. **Critically, this whole line is contingent on the still-open in-house-vs-partner-supplied employment question — see §10.** |
| Massage+Beauty pool (dual-qualified) | 4 simultaneous (of a 6-recommended full pool incl. 2 relief) | 6 recommended | 07:00–13:00, Mon–Sat, staggered starts (07:05/07:30) | **A$37.50/hr**, MA000005 Level 4 | `[VERIFIED headcount — sweep-line + greedy first-fit, exact agreement, same 4-person peak concurrency at both 12 and 18 clients/day]` |
| Nail Technician | 2 simultaneous (of a 3-recommended pool) | 3 recommended | 07:00–13:00, Mon–Sat, staggered start (07:30) | **A$36.81/hr**, MA000005 Level 3 | `[MODELED]` |
| Hairdresser | 2 simultaneous (of a 3-recommended pool) | 3 recommended | 07:00–13:00, Mon–Sat, staggered start (07:30) | **A$36.81/hr**, MA000005 Level 3 | `[MODELED]` |
| PM Massage Therapist, PM Beauty Therapist, PM Nail Technician, PM Hairdresser | 1 each committed; 2–3 on demand only during a solver-verified real peak cluster, not a standing increase | — | 13:00–18:00, hours-based costing (not a fixed shift length) | Same MA000005 rates as the AM equivalents | `[MODELED — covers PM reception during own booking gaps, Fresha training required]` |
| **Total committed headcount (AM 8 treatment + 2 phlebotomists + Venue Manager)** | **~11 committed core roles**, plus PM dedicated-casuals | ~16-17 including full relief pools | | | `[MODELED — sum of above, per docs/CURRENT-STATE.md §4]` |

**Superannuation:** 12% on ordinary time earnings, confirmed current for FY2026-27. `[VERIFIED — hr-framework.md, 2026-08-16 research]` Payday Super (paying super within 7 business days, not quarterly) becomes mandatory from 1 July 2026 — a timing change, not a rate change.

**Workers compensation:** 1.7% of payroll, applied as a modelling convention. **The rate itself remains `[PLACEHOLDER — not upgraded to VERIFIED]`** — mandatory coverage itself is confirmed, but this venture's exact classification/premium is not.

**Penalty rates:** Saturday 1.33×, Sunday 2.0×, Public Holiday 2.5× — unconfirmed against a primary source; a 3-way conflict remains unresolved in the canonical wage data. `[PLACEHOLDER]`

**Genuinely still open, not resolved here:** whether 4 phlebotomists (with 2 relief) vs the 3-person lower bound is the right hire target; same open question for the 6- vs 5-person Massage+Beauty pool. Both are founder decisions outstanding, not blocking the current P&L (which costs only the 2/8 simultaneous-committed figures).

**Recruiting collateral exists but is NOT ready to post:** `docs/venue-manager-job-posting.md` is explicitly marked "ON HOLD — NOT READY FOR APPROVAL" as of 2026-07-29 — do not present it in the deck as an active/live posting.

---

## 7. Full Financial Model at 18 Clients/Day

**Source: `docs/CURRENT-STATE.md` §5 (2026-08-21, Founder Decision round — the current, authoritative figures) and `data/models/master_financial_model.yml` (the deterministic model those figures are computed from). This is the most recent recompute; earlier rounds (2026-08-05 rebase, 2026-08-09 super correction, 2026-08-17 wage recompute, 2026-08-18 audit/finalisation rounds) are all superseded by this one and should NOT be quoted in the presentation.**

### Revenue

| Line | Formula | Monthly | Tag |
|---|---|---|---|
| AM GTT (Package 1, weekday + Saturday) | 18 clients/day × A$250 × 22 weekdays/month, plus the Saturday-volume equivalent (Saturday = same AM volume as weekday, per the settled operating model) | **A$118,485.00** | `[CALCULATED]` |
| AM gap-fill/standalone | None available — AM window fully allocated at 18 clients/day | A$0.00 | `[VERIFIED — no idle AM capacity exists at full committed volume]` |
| PM (blended individual + PM Refresh + PM Restore) | 16 sessions/day capacity × A$117 blended average × operating days | **A$36,225.69** | `[MODELED — see the flagged transaction-vs-session reconciliation note below]` |
| Ancillary (cafe/retail) | Excluded from baseline entirely — pure upside if it materialises | A$0.00 | `[MODELED — deliberate exclusion, not an oversight]` |
| **TOTAL REVENUE** | | **A$154,710.69/month** | `[CALCULATED]` |

**Flag on the PM revenue line, not resolved, disclosed rather than hidden:** a dedicated reconciliation (`docs/architecture/OPERATING-MODEL-18-CLIENTS.md` §3b) found that PM packages consume 2 treatment-staff "sessions" per 1 client transaction, while the current canonical PM revenue figure multiplies the A$117 average directly against the 16-sessions/day capacity figure as if every session were 1 transaction. This makes the current A$36,225.69/month PM revenue figure a likely **overestimate, bounded between 0% and ~28.6%**, depending on an operational decision (concurrent vs sequential package delivery) that has not yet been made. **This is not corrected in the canonical model — it is a genuine open item requiring Anthony's decision, not something this brief resolves unilaterally.**

### Operating costs

| Line | Monthly | Tag |
|---|---|---|
| Total payroll (all wages, all roles, incl. super + workers comp) | **A$96,256.18** | `[CALCULATED — data/canonical/cost_ramp.yml, deterministic]` |
| Non-wage overhead (rent A$8,000, utilities A$650, insurance A$708.34, GTT supplies A$400, consumables A$800, laundry A$350, marketing A$1,500, software A$280, cleaning A$600, accounting A$500, misc/contingency A$500) | **A$14,288.34** | `[MODELED/BALLPARK-ESTIMATE — insurance corrected 2026-08-18, real broker quotes still in motion]` |
| Relief/Absence Coverage Allowance | **A$0.00** — reverted per direct founder instruction; normal payroll/rostering treated as already absorbing absence coverage | `[DECIDED — founder instruction, 2026-08-21]` |
| **TOTAL OPERATING COSTS** | **A$110,544.52/month** | `[CALCULATED]` |

**Note on the payroll figure's composition:** the A$96,256.18 total reflects the 2026-08-21 removal of a previously-modelled dedicated PM Reception role (Position 06/RCO01, ~A$4,802.83/month) — PM Reception is now covered by rostered PM treatment staff during their own booking gaps, at no extra cost. A full per-role dollar breakdown re-published after this removal does not exist as a single document; the last full itemised breakdown (`docs/architecture/FINANCIAL-POSITION-CURRENT.md`, 2026-08-18) still includes the now-removed PM Reception line and should not be quoted as current without netting that line out. **This agent has not attempted to re-derive a full post-removal per-role breakdown beyond the two headline totals above (payroll subtotal, non-wage overhead) — flagged as a genuine gap in this brief, not fabricated.**

### Operating result

| Metric | Monthly | Annualised | Tag |
|---|---|---|---|
| **Operating Result (Revenue − Operating Costs)** | **A$44,166.17** | **A$529,994.04** | `[CALCULATED — data/models/master_financial_model.yml#outputs.steady_state_summary, 2026-08-21]` |
| Quarterly | A$132,498.51 | | `[CALCULATED]` |
| Half-yearly | A$264,997.02 | | `[CALCULATED]` |

**Terminology, use precisely in the presentation:** this is an **Operating Result**, not a full accounting "net profit." It explicitly excludes depreciation/amortisation of startup capex, income tax, interest on financing, and any allocation of startup capital cost — none of these are modelled anywhere in the canonical layer yet. `[VERIFIED — docs/architecture/FINANCIAL-POSITION-CURRENT.md §4, definitional note still valid even though that document's dollar figures are stale]`

### Weekly / daily equivalents

| | Value |
|---|---|
| Weekly Operating Result (Monthly ÷ 4.33) | ≈ A$10,200/week `[CALCULATED by this agent from the monthly figure — presentation-convenience conversion, not a separately modelled figure]` |
| Daily Operating Result (Monthly ÷ 22 weekdays, illustrative only — real daily result varies by weekday/Saturday mix) | ≈ A$2,007/day `[CALCULATED, same caveat]` |

---

## 8. Break-Even and Profitability Ladder

**Source: `data/models/master_financial_model.yml` (2026-08-21 run) — this is the most current break-even computation and supersedes `docs/architecture/FINANCIAL-POSITION-CURRENT.md`'s own break-even figure (13.051 clients/day), which predates the 2026-08-21 PM Reception removal and is explicitly marked stale by the model file's own changelog note.** `break-even-sensitivity-analysis.md`, `financial-model.md`, and `scenario-comparison-master-2026-08.md` are not separately re-reconciled here, per the coordinator's instruction — this YAML output is the authoritative current computation `docs/CURRENT-STATE.md` itself defers to.

| Metric | Value | Tag |
|---|---|---|
| **Break-even AM client volume** | **11.290 clients/day** | `[CALCULATED — compute_breakeven(scenario_table_1), 2026-08-21]` |
| Break-even monthly revenue | A$110,542.11 | `[CALCULATED]` |
| Committed (planning) volume | 18.000 clients/day | `[VERIFIED — solver-confirmed capacity]` |
| Margin of safety | 6.710 clients/day above break-even (≈37.3% of committed volume) | `[CALCULATED]` |

### Profitability ladder — AM client volume vs Operating Result (payroll held fixed at the committed 18-client design, per this model's own disclosed limitation that headcount does not flex down with lower booking volume)

| AM clients/day | % of committed (18/day) | Monthly revenue | Monthly Operating Result | Tag |
|---|---|---|---|---|
| 9.00 | 50% | A$95,468.19 | **-A$15,076.33** (loss-making) | `[CALCULATED]` |
| 11.29 | ~63% | A$110,542.11 | **A$0** (break-even point) | `[CALCULATED]` |
| 13.50 | 75% | A$125,089.44 | **+A$14,544.92** | `[CALCULATED]` |
| **18.00** | **100% (planning case)** | **A$154,710.69** | **+A$44,166.17** | `[CALCULATED]` |
| 22.50 | 125% (above physical 9-pair capacity ceiling — illustrative only, not a real achievable schedule at current headcount) | A$184,331.94 | +A$73,787.42 | `[CALCULATED, illustrative]` |

**Reading this plainly for the presentation:** the venue clears break-even at just under 11.3 AM clients/day — well below the 18-client committed target — and the 18-client case carries a genuine margin of safety of almost 7 clients/day above that. The 22.5/day row is a pure sensitivity extrapolation (the actual solver-verified physical ceiling at the current 8-treatment-staff/2-phlebotomist headcount is 18/day for the 25-minute-cadence model) and should be labelled as such if shown, not implied as an achievable near-term step.

**On the 12/day figure:** per the hard constraint on this brief, 12 clients/day does not appear anywhere above as a live scenario. It exists in the source documents only as a historical/retired committed model (superseded 2026-08-05) and, separately, as a permanently-retained downside/sensitivity reference point (Table 2) that is explicitly never presented as an alternative plan anywhere in this venture's own documents. Neither use case belongs in this presentation per Anthony's instruction.

---

## 9. Start-Up Costs

**Source: `docs/CURRENT-STATE.md` §6 — genuinely unreconciled across this repo's own history, flagged plainly rather than forced to a single false-precision number.**

| Component | Range | Tag |
|---|---|---|
| Equipment, furniture, fixtures, expendables (day-one) | A$61,190 – A$140,430 | `[MODELED — itemised bottom-up build, equipment-costs.md + floor-plan-concept.md]` |
| Fit-out/construction | A$191,200 – A$298,750 | `[MODELED — 239sqm × A$800–1,250/sqm established rate; landlord fit-out contribution deliberately excluded from this figure per Anthony's instruction, since he is skeptical a landlord will actually contribute]` |
| Working capital & pre-launch costs (legal/entity setup, lease bond, working-capital reserve for Months 1–3 operating losses) | A$105,000 – A$138,000 | `[MODELED — from Anthony's own partner-brief working session; the A$400/month insurance sub-component within this range is itself `[PLACEHOLDER]`, never an actual quote]` |
| **Adopted total range (Anthony's own reconciliation, the figure to quote)** | **A$292,335 – A$594,900** | `[MODELED — Anthony's reconciled figure, adopted as instructed; this agent's own independent component sum lands a few percent higher on both ends (A$357,390–577,180) — both are shown in the source document rather than silently forced to agree]` |
| **Newer planning figure, alongside (not replacing) the range above** | **A$251,198** (Pre-Opening Capital scope), approved "in principle" by Anthony, 2026-08-10 | `[MODELED — planning figure, not a locked final cost, pending venue confirmation and final supplier/quote validation]` |

**Do not present any single one of these numbers as "the" startup cost without the range/estimate caveat** — this is explicitly flagged in the source document as the clearest example of this venture's financial model having moved multiple times across different planning sessions, not yet fully reconciled against the current 18-client committed model.

**Working capital reserve specifically:** A$85,000–110,000, sized to fund the ramp period. Per the 2026-08-21 cash-flow model, the actual operating cash trough is **-A$76,532.52 at Month 2**, turning cumulatively positive from **Month 6**, reaching **+A$598,232.91 by Month 24**. `[CALCULATED — data/models/master_financial_model.yml, 2026-08-21]` Note this cash-flow figure was computed before the same-day PM Reception removal fully propagated through every downstream cash-flow row in some source documents — the headline Operating Result above (A$44,166.17/month) is the correct, fully-current figure to use; the exact monthly cash-flow trajectory shown in `docs/architecture/FINANCIAL-POSITION-CURRENT.md` predates that removal and should be treated as directionally correct but not cited as an exact current figure.

---

## 10. Pathology Partner Status — All 4 Candidates

**Field size, confirmed:** 4 genuine WA pathology candidates exist — WDP, PathWest, Clinipath, and Australian Clinical Labs (ACL), the last identified via a fresh 2026-08-28 re-verification after the field was initially (and incorrectly) treated as 3. `[VERIFIED — docs/reed-partnerships.md §1c]` **No partnership is signed with any of the 4 as of this writing.**

### WDP (Western Diagnostic Pathology) — PRIMARY

| | |
|---|---|
| **Status** | In discussion, active back-and-forth, but the tone of the most recent reply is closing-sounding |
| **What's been discussed** | A documented Licensed Collection Centre program; GTT's operating model (18/day, Mon–Sat); a full ACC/NPAAC collection-room spec and site-assessment criteria; whether courier/GTT collection is feasible with the correct specimen tubes (confirmed viable "in some circumstances" — fluoride oxalate tubes stable ~24hrs, `[VERIFIED — Carole Rivers, WDP, email, 2026-07-30]`); the GTT start-time guidance ("would not normally commence a GTT after 10:30am," `[VERIFIED — same source]`); whether a GP/doctor needs to be on-site (resolved favourably — "the absence of doctors on site would not present an operational concern," `[VERIFIED — Carole Rivers, 2026-08-07]`) |
| **Have they responded?** | Yes, multiple times (2026-08-06, 08-08, 09-08). Most recent (2026-09-08) reply, in full: *"Hi Anthony, I think I have provided all the information I can as a Customer and Commercial Manager. Many thanks."* — fairly closing-sounding, does not update on the two items she said she was chasing internally |
| **Confirmed vs still proposed** | Confirmed: courier collection conditionally viable; GTT start-time guidance; no GP-on-site requirement. Still proposed/unconfirmed: the actual commercial/rental figure (item 1c); whether WDP or GTT employs the phlebotomist (item 1d, deliberately not yet asked); whether medical waste disposal is covered under WDP's own setup |
| **Next step** | Awaiting a substantive reply to Anthony's 2026-09-08 follow-up, which asked whether her Quality Department/State Business Manager got back to her, an in-principle willingness question, and next steps toward a formal contract — deliberately did not re-raise the rental figure, the Quality Department boundary question, or the employment-model question this round, a strategic choice given her closing tone |

### PathWest — SECONDARY, genuinely progressing

| | |
|---|---|
| **Status** | In discussion, the most advanced of the 4 on one specific point (unconditional courier confirmation) |
| **What's been discussed** | Venue concept, wellness services overview, testing operation, expected volume (18/day, Mon–Sat), timeframe; courier collection feasibility for grey-top (fluoride oxalate) tubes; tube/consumables supply |
| **Have they responded?** | Yes, multiple substantive replies (2026-08-27 through 2026-09-03), from Meera Bennett, Medical Liaison Officer |
| **Confirmed vs still proposed** | Confirmed: PathWest "can definitely accommodate courier pick ups for Fluoro ox tubes" and will supply tubes/biohazard bags at no cost `[VERIFIED — Meera Bennett email, 2026-09-01]`; PathWest does **not** supply the glucose drink. Still proposed/unconfirmed: cost (courier + lab testing), the shape of any arrangement (contract/partnership/fee-for-service), PathWest's own next steps |
| **Next step** | Awaiting Meera's answers to Anthony's 2026-09-03 email (cost ballpark, arrangement shape, next steps). **Anthony has explicitly decided not to lock anything in with PathWest until WDP's outstanding follow-up is answered** — this is exploratory/information-gathering only, not a commitment |

### Clinipath — CONTINGENCY

| | |
|---|---|
| **Status** | Not yet confirmed — awaiting reply, no engagement yet despite 3 contact attempts |
| **What's been discussed** | Original enquiry (2026-07-27, generic cutoff-time/overnight-storage questions); a follow-up nudge (2026-08-27); a 3rd contact (2026-09-07, sent to 3 addresses simultaneously) that for the first time states GTT's actual self-collection/lab-processing-only model plainly, with 2 explicit operating-model options |
| **Have they responded?** | **No response from any of the 3 contacted addresses as of 2026-09-07** |
| **Confirmed vs still proposed** | Nothing confirmed — pure outreach status |
| **Next step** | Awaiting any reply to the 2026-09-07 send. Contingency only — proceed if WDP and PathWest both decline or terms are unfavourable |

### Australian Clinical Labs (ACL) — 4th candidate

| | |
|---|---|
| **Status** | Awaiting reply, no engagement yet |
| **What's been discussed** | First-contact email (sent 2026-08-29) presenting both staffing/operating options (GTT self-collects, ACL limited to transport/lab-testing; or ACL supplies collection staff and runs collection end-to-end) |
| **Have they responded?** | **No response received as of the latest repository update** |
| **Confirmed vs still proposed** | Nothing confirmed |
| **Next step** | No follow-up planned yet — per this venture's own established pattern, follow-ups go out only after roughly 3–4 weeks of silence |

**Do not imply any of the 4 has a signed partnership.** The most advanced position of any candidate is PathWest's unconditional courier confirmation (tubes/biohazard bags supplied free) — this is a real, concrete step, but it is not a commercial agreement, and Anthony has explicitly chosen not to progress it further until WDP replies.

---

## 11. Research Depth Summary — What's Actually Been Investigated

One line each, categories only, not a self-congratulatory list:

- **Customer experience:** full before/arrival/GTT/after journey map built and reconciled across two independent design explorations; departure-gift concept explicitly tested and rejected by the founder.
- **GTT clinical workflow:** exact minute-by-minute AM schedule solver-verified for zero chair/phlebotomist collisions at 18 clients/day; the schedule actually sent to WDP for review.
- **Pathology relationships:** all 4 genuine WA candidates identified and contacted; live, evolving correspondence tracked message-by-message with 3 of the 4.
- **Staffing:** headcount solver-verified via two independent methods (sweep-line + greedy first-fit) at the committed volume; a single authoritative position register built with wage/hours/eligibility per role.
- **Wages:** current award rates researched via two independent third-party payroll calculators (2026-08-16); one misclassification (Venue Manager) found and corrected via an independent audit.
- **Pricing:** AM packages locked by the founder; PM packages designed against real Perth comparable bundle pricing, average transaction value derived from the actual service catalogue, not assumed.
- **Venue requirements:** a single authoritative venue-program table separating physical build capacity from staffing, reconciled against multiple prior fit-out documents.
- **Capacity:** 3 successive capacity models (10 → 12 → 18 clients/day) each independently solver-verified before being adopted or retired.
- **Financial modelling:** a fully deterministic, YAML-driven model with 8+ successive correction rounds, each disclosed rather than silently overwritten, down to the current 2026-08-21 figures.
- **Branding:** a full name-agnostic brand/experience strategy layer plus a founder-locked colour palette, built to work identically regardless of which of the 2 remaining candidate names is chosen.
- **Legal/regulatory:** NPAAC collection-centre standards researched and cross-checked against all 4 pathology candidates' own public accreditation pages; a new September 2026 federal trust-tax development researched and written up for the entity-structure decision.
- **Market opportunity:** WA GTT test volume estimated from real ABS births data (~515/week Perth metro), corrected once already after an earlier unsourced estimate.
- **Risks:** a standing risk register and open-conflicts log maintained throughout, with each flagged item tracked to resolution or explicitly left open rather than quietly dropped.

---

## 12. Current Position vs Open Items

### Decided / locked

- Operating model: 18 clients/day AM (Table 1), 07:00 start, 25-min cadence — settled 2026-08-17, not a live framing question.
- AM packages: A$250 / A$300, only 2 tiers.
- Employment model for wellness/beauty staff and (in the current baseline) phlebotomists: **employed staff, not subtenants.**
- PM Reception: no dedicated role — covered by PM treatment staff during booking gaps (Model C), founder decision 2026-08-21.
- Blood Collection Room count: 2 separate rooms, one per phlebotomist, for privacy — founder decision 2026-08-27.
- Massage station format: table/bed, not chair-based — founder decision 2026-08-26.
- Departure "leaving box" gift concept: rejected — must not appear in any forward-facing material.
- Retail strategy: third-party resale (Gaia, Weleda, Mustela), not a name-branded product line — closed 2026-08-14.
- Brand colour palette: founder-locked 2026-08-15 (Warm Ivory #FAF6EE, Warm Stone #E8DAC5, Deep Brown #33261E, Earthy Terracotta #A9654E, Muted Olive #5E5F45, Soft Dusty Rose #D9A08C, Warm Brass #9C7A46 for fine-line/hardware detail only) — matches the palette given in the original task brief exactly (the brief's "Soft Blush" is the same hex as the canonical "Soft Dusty Rose," name variance only). **`docs/brand-guide.md` (the older sage/terracotta/June-2026 document) is superseded and must not be used as a colour or naming reference — see the flag below.**
- Typography/logo territory: Fraunces (serif) + DM Sans (sans), wordmark-led (no symbolic mark) — current, name-agnostic.

### Still open

- **Final brand name:** SOLENA currently leads a weighted three-way comparison (71.6% vs ELOWEN's 68.8%), but this is explicitly a **conditional, not locked** decision — trademark attorney clearance is deliberately deferred to a later funding milestone, and the legal status is "KNOWN RISK — NOT YET PROFESSIONALLY CLEARED." State it in the presentation as "SOLENA (conditional leader), final name still being resolved," not as decided.
- **Final pathology partner:** none of the 4 candidates has a signed agreement — see §10.
- **Phlebotomist employment model:** in-house (current costed baseline) vs pathology-partner-supplied under a rental model — deliberately not yet asked of WDP.
- **Final venue site:** no property secured — kept fully out of scope for this presentation per the hard constraint on property content.
- **Entity structure:** trust-direct (status quo) vs a new operating PTY LTD under the trust vs a new fixed-distribution election under September 2026 draft federal legislation — a live 3-way question for Anthony's accountant conversation, not decided anywhere in this repo. Imara's position under each option is described neutrally (funding partner / possible trust beneficiary — status not yet confirmed against the actual trust deed) with **no operational role assigned to her under any option.**
- **PM package pricing:** direction confirmed, exact A$185/A$135 prices not yet signed off by Anthony.
- **Startup capital:** a genuinely unreconciled range across multiple planning sessions (§9) — present as a range/estimate, not a single number.
- **PM revenue methodology:** the session-vs-transaction reconciliation flagged in §7 is unresolved, pending an operational decision on how PM packages are actually delivered (concurrent vs sequential staffing).
- **Staffing pool size:** whether to hire to the full recommended relief pool (e.g., 4 phlebotomists, 6 Massage+Beauty staff) or the disclosed lower bound (3 and 5 respectively) — a founder decision outstanding, not blocking the current committed P&L.
- **Workers compensation rate:** mandatory coverage confirmed, exact premium for this venture's classification not yet quoted.

---

## Tooling Flag — Read Before Trusting Any "Clean" Consistency Check

`tools/check_consistency.py` was run for this brief and returned **0 findings**. This should **not** be read as proof every figure in the repo is current. The script's own hardcoded "canonical" display values for Monthly Net P&L (+A$63,028.75/month) and AM GTT capacity commentary reflect the **2026-08-05 rebase**, not the many subsequent correction rounds through 2026-08-21 (superannuation, wage-rate recompute, first-principles rebuild, audit-round correction, PM capacity reconciliation, financial finalisation, and the final founder-decision round that produced today's actual figure of A$44,166.17/month). The script's stale-pattern regex list only catches much older figures (e.g., -A$9,684, +A$25,087) — it would not flag a document that quoted A$63,028.75 or A$32,576.80 as if still current, because neither of those intermediate figures is in its stale-pattern list. **This is a genuine tool limitation in the repository, not something this brief's content relies on** — every figure in this brief was cross-checked directly against `docs/CURRENT-STATE.md`'s own most recent (2026-08-21) prose and `data/models/master_financial_model.yml`'s underlying computed output, not against the consistency checker's verdict alone.

---

## Sources Consulted (primary documents this brief is built from)

`docs/CURRENT-STATE.md`, `docs/VERIFICATION-TRACKER.md`, `docs/DECISION-LOG.md`, `docs/gtt-center-perth-overview-for-imara.md` (confirmed stale), `docs/workflow.md` (confirmed stale/superseded), `docs/brand-guide.md` (confirmed stale/superseded), `docs/strategy/VISUAL-BRAND-DIRECTION.md`, `docs/00_document_inventory.md`, `docs/experience/CUSTOMER-JOURNEY.md`, `docs/architecture/OPERATING-MODEL-18-CLIENTS.md`, `docs/architecture/VENUE-PROGRAM-AUTHORITATIVE.md`, `docs/architecture/STAFF-POSITION-REGISTER.md`, `docs/financial-break-even-staff.md`, `docs/services-pricing-locked.md`, `docs/architecture/PM-PACKAGES.md`, `docs/architecture/FINANCIAL-POSITION-CURRENT.md` (flagged partially stale), `data/models/master_financial_model.yml`, `data/canonical/cost_ramp.yml`, `docs/lab-outreach-2026-07-28.md`, `docs/pathwest-clinipath-outreach-2026-07-27.md`, `docs/reed-partnerships.md`, `docs/architecture/PARTNER-ACCREDITATION-STANDARDS-COMPARISON.md`, `docs/naming/NAMING-DECISION-STATE.md`, `docs/architecture/ENTITY-STRUCTURE-INVESTIGATION.md`.
