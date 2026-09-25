# GTT Center Perth — Startup Capex/Fit-Out Forensics (Round 3, Priority 7)

**Created:** 2026-09-25 (Round 3) | **Author:** Grace (Operations Manager)
**Purpose:** Real-world minimum-viable/premium/excessive fit-out ranges from real 2026 Australian sources, cross-checked against GTT's own A$800-1,250/sqm construction assumption.

**Tagging:** `[VERIFIED]` / `[REPORTED]` / `[BENCHMARK]` / `[ESTIMATE]` / `[ASSUMPTION]` / `[UNKNOWN]`.

---

## 1. GTT's Own Assumption vs Real 2026 Australian Medical/Allied-Health Fit-Out Benchmarks

**GTT's own figure:** A$800-1,250/sqm for the "raw-shell scenario" construction cost, applied to a 239sqm footprint (A$191,200-298,750 total) `[VERIFIED — docs/CURRENT-STATE.md §7.2]`.

**Real 2026 Australian benchmarks found this round (multiple independent sources, converging on a consistent range, not single-source):**
- General commercial fit-out (not medical-specific): commonly A$1,500-3,000/sqm overall `[BENCHMARK]`.
- **General practice/allied-health fit-out specifically: A$1,800-2,800/sqm** `[BENCHMARK — multiple independent 2026 Australian fit-out industry sources, converging on a consistent range]`.
- Basic/entry-level commercial fit-out: A$500-1,500/sqm; mid-spec: A$1,600-2,500/sqm; premium: A$2,600+/sqm `[BENCHMARK]`.
- Imaging/day-surgery/specialist procedure fit-outs (sterile environments, plant rooms): A$3,500-4,500+/sqm — **not applicable to GTT Center Perth**, whose collection rooms are a Tier 3B NPAAC collection centre, not a surgical/imaging facility, flagged explicitly to avoid misapplying a benchmark from a materially more complex facility type.

**Finding: GTT's own A$800-1,250/sqm assumption sits below the general allied-health fit-out benchmark (A$1,800-2,800/sqm) found this round, and even below the "basic" commercial tier's upper end (A$1,500/sqm).** This is a real, material, previously-unflagged gap. **However, this comparison needs an important caveat, not glossed over: GTT Center Perth's own footprint is predominantly a beauty/wellness salon fit-out (massage rooms, nail/hair stations, lounge, cafe) with only 2 small collection rooms carrying genuine clinical-grade requirements — applying a full allied-health-clinic rate (A$1,800-2,800/sqm) to the ENTIRE 239sqm footprint would likely overstate the true blended cost, since most of the space is salon-grade, not clinic-grade, fit-out.** A more defensible blended estimate, reasoned from the real fragments: if the ~38-40sqm collection-room component (2 rooms at ~18-20sqm each, per `docs/architecture/VENUE-PROGRAM-AUTHORITATIVE.md`) is costed at the real allied-health rate (A$1,800-2,800/sqm) and the remaining ~199-211sqm is costed at a general commercial/salon rate (closer to GTT's own existing A$800-1,250/sqm, which is more defensible for non-clinical salon space), the blended total would be:

- Collection rooms (~39sqm × A$1,800-2,800/sqm): **A$70,200-109,200**
- Remaining salon space (~200sqm × A$800-1,250/sqm): **A$160,000-250,000**
- **Blended total: A$230,200-359,200** `[ESTIMATE — this document's own blended calculation, combining GTT's own existing salon-space rate with a real external clinic-space rate, not previously calculated anywhere in this repository]`

This compares to GTT's own current flat-rate total of A$191,200-298,750 — **the blended, room-type-specific estimate is roughly A$39,000-60,450 higher than GTT's own current flat-rate assumption**, concentrated specifically in the collection-room component, which is the part of the venue most likely to actually require genuine clinical-grade fit-out (impervious surfaces, specific ventilation, plumbing for hand-hygiene stations — all already itemised in `docs/pathology-collection-room.md`, just not costed at a clinic-specific rate).

**Confidence:** Medium. The allied-health benchmark itself is well-sourced and consistent across multiple 2026 Australian fit-out industry publications. The blended-split methodology is this document's own reasonable approach, not externally validated, and the exact collection-room square-metreage (39sqm) is itself an estimate from `docs/architecture/VENUE-PROGRAM-AUTHORITATIVE.md`'s own stated "~18-20sqm" per room.

---

## 2. Minimum Viable vs Premium vs Excessive — Applied to GTT's Own Existing Optimisation Work

`docs/architecture/STARTUP-COST-OPTIMISATION.md` and the founder-approved A$251,198 planning figure (`docs/CURRENT-STATE.md` §6) already represent this venture's own "minimum viable opening" analysis — this round's external benchmarking does not find evidence this figure is unrealistic on the general-commercial-space portion, but does suggest the collection-room-specific component may be modestly underscoped relative to genuine allied-health fit-out standards, per Section 1 above.

**"Excessive" reference point, found this round:** the real Ingleburn hair salon business-for-sale listing (`CASE-STUDY-DATABASE.md` Case 6) shows a fit-out that cost ~A$280,000 only 3 years before selling the entire business for A$85,000 — a stark, real, quantified example of fit-out capital not being a recoverable asset. This reinforces, from an independent angle, why this venture's own cost-reduction work (`docs/architecture/STARTUP-COST-OPTIMISATION.md`) matters: fit-out spend should be sized to operational need, not maximised for its own sake, since it will not be recovered at exit value anywhere near cost.

---

## Sources

`docs/CURRENT-STATE.md`, `docs/architecture/VENUE-PROGRAM-AUTHORITATIVE.md`, `docs/pathology-collection-room.md`, `docs/architecture/STARTUP-COST-OPTIMISATION.md` (this venture's own primary documents); 2026 Australian medical/commercial fit-out cost sources (medicalsearch.com.au, finexfitouts.com.au, designyard32.com.au, soulmed.com.au — Tier 3, multiple independent sources converging on a consistent range); `CASE-STUDY-DATABASE.md` Case 6 (Round 2, this repository).

---

## Changelog

**2026-09-25 (Round 3, created):** New file. Found GTT's own flat-rate construction assumption (A$800-1,250/sqm) sits below real 2026 Australian allied-health fit-out benchmarks (A$1,800-2,800/sqm), then built a more defensible room-type-specific blended estimate (A$230,200-359,200) rather than either accepting GTT's figure uncritically or misapplying the full clinic rate to the entire footprint. Confidence explicitly stated as medium given the blended methodology is this document's own reasoning, not externally validated.
