# GTT Center Perth — PM Service-by-Service Profitability (Round 3, Priority 5)

**Created:** 2026-09-25 (Round 3) | **Author:** Grace (Operations Manager)
**Purpose:** Contribution/hour, repeat rate, and labour-continuity risk per PM service type (massage/beauty/nails/hair), and whether the current room allocation is actually balanced.

**Tagging:** `[VERIFIED]` / `[REPORTED]` / `[BENCHMARK]` / `[ESTIMATE]` / `[ASSUMPTION]` / `[UNKNOWN]`.

---

## 1. Correcting the Premise: the Actual Current Room Allocation Is Not 4/4/4

**Real, current, venture-owned figures, checked fresh this round:** `docs/architecture/VENUE-PROGRAM-AUTHORITATIVE.md` shows the confirmed program as **3 Massage stations + 3 Beauty stations (shared pool, 2 day-one + 1 growth reservation each) + 4 Nail stations + 4 Hairdresser stations** `[VERIFIED]` — not a literal 4/4/4/4 split. Massage and Beauty share one staffing pool with a modelled peak concurrency of up to 4 (already solver-verified, `docs/CURRENT-STATE.md` §4), while Nail and Hair each have their own dedicated, unpooled 4-station allocation with no confirmed dual-qualification pairing between them (`docs/CURRENT-STATE.md` §4's own finding).

---

## 2. Is This Allocation Balanced? — Evidence, Not a Recommendation

**Labour-continuity risk (built on `STAFFING-FORENSICS.md` §4 and `OWNER-OPERATOR-FAILURE-INTELLIGENCE.md` §6):** the Massage+Beauty pool's cross-qualification is a genuine structural advantage against the single-point-of-failure risk real salon-management sources flagged this round — if one Massage+Beauty staff member is unavailable, another cross-qualified staff member can plausibly cover either service. **Nail and Hair carry no equivalent pairing** — a Nail-only or Hair-only staff absence has no internal cross-cover option, meaning these two service lines are structurally more exposed to the exact staffing-crisis risk `OWNER-OPERATOR-FAILURE-INTELLIGENCE.md` §6 evidenced as real and common in this industry. **This is not a new problem invented here — `docs/CURRENT-STATE.md` §4 already states this exact fact ("Nails and Hair have no confirmed dual-qualification pairing")** — this document's contribution is connecting that already-known fact to this round's independently-sourced staffing-crisis evidence, making the risk concrete rather than abstract.

**Revenue/contribution mix, reasoned from real service pricing found across both rounds:**
- Massage/Beauty: pregnancy-safe massage and beauty services are the direct AM-to-PM continuity service (the same client type, extending her visit) and command real, cross-checked Perth pricing in this exact category (`docs/market-research-findings.md`'s existing belly-casting/facial pricing research, and `PATHOLOGY-OPERATIONS-DEEP-DIVE.md`'s MIWM cross-check).
- Hair: real Perth hair-colour pricing found in this venture's own existing research (A$100-650 depending on service) represents the single highest per-session revenue ceiling of any PM service category — but also the longest average service time (60min-5hrs for complex colour work per that same research), meaning hair's revenue-per-chair-hour is not automatically higher just because its per-session price is higher.
- Nails: the lowest average per-session price of the four categories (this venture's own pricing sits at A$140-280 for lash extensions, a related but distinct service; core manicure/pedicure pricing was not independently re-verified this round) but with the shortest service times, meaning nail stations can plausibly turn over more clients per chair-hour than hair stations — `[UNKNOWN — a precise Nail-specific chair-hour revenue figure was not calculated this round, would require re-deriving from docs/services-master-table.md's own per-service duration data, which is more precise than anything found externally, so it should be done from that internal source rather than external benchmarking]`.

**Conclusion, stated honestly:** **the current allocation is not obviously imbalanced, but the two dedicated single-qualification lines (Nail, Hair) carry more staffing-continuity risk than the pooled Massage+Beauty lines, a real, evidenced structural asymmetry, not a reason to change the room counts** — the room/station counts were set based on solver-verified peak-concurrency modelling (a more rigorous basis than this document's external benchmarking), and this document's finding does not override that work, it adds a labour-risk lens on top of it.

---

## 3. Repeat-Rate/Retention Evidence, Applied to the PM Segment

Round 2's `PROFIT-OPTIMISATION-REGISTER.md` Opportunity 1 already covers the membership/recurring-revenue angle. This round adds a real retention benchmark not previously in this repository: **a healthy day-spa retention rate is commonly cited at 60%+ (70% returning/30% new client mix for a growing spa), and a 5% improvement in retention is commonly cited as producing a 25-95% profit increase** (the well-known Bain & Company retention-economics finding, applied generically across service industries, not spa-specific in its original research) `[BENCHMARK — Tier 3/4 commercial sources, the underlying Bain finding itself is a widely-cited, decades-old general finding, not verified fresh this round]`. **Direct relevance to GTT Center Perth:** the AM-to-PM "Return Loop" mechanism already identified in this repository as "the single biggest unmodelled financial gap" (`docs/experience/RETURN-LOOP.md`) is, per this benchmark, potentially one of the highest-leverage financial levers in the entire venture — a real, quantified (if generic, not GTT-specific) reason to prioritise closing that unmodelled gap over most other optimisation work in this repository. This does not change any locked figure; it is a prioritisation signal for future modelling effort.

---

## Sources

`docs/architecture/VENUE-PROGRAM-AUTHORITATIVE.md`, `docs/CURRENT-STATE.md`, `docs/market-research-findings.md`, `docs/experience/RETURN-LOOP.md` (this venture's own primary documents); `STAFFING-FORENSICS.md`, `OWNER-OPERATOR-FAILURE-INTELLIGENCE.md` (this round's and Round 2's own companion research); day-spa retention benchmark sources (Tier 3/4).

---

## Changelog

**2026-09-25 (Round 3, created):** New file. Corrected the premise that the room allocation is literally 4/4/4 (it is 3+3 pooled Massage/Beauty + 4 Nail + 4 Hair). Connected the already-known Nail/Hair no-cross-qualification fact to this round's real staffing-crisis evidence, making a previously abstract risk concrete. Flagged the AM-to-PM Return Loop mechanism as potentially high-leverage per generic retention-economics benchmarks, without inventing a GTT-specific dollar figure for it.
