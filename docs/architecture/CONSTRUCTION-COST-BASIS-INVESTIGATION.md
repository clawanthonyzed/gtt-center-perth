# Construction Cost Per SqM — What the A$800-1,250/m² Estimate Actually Includes

**Date:** 2026-08-16 | **Purpose:** C5 — investigate the basis of the current A$800-1,250/sqm construction estimate: what it includes/excludes, what assumptions generated it, whether it's appropriate for a predominantly open-plan fit-out, and whether the open-plan concept materially changes it. Not carried forward blindly.

---

## 1. Where This Rate Actually Comes From

Per `docs/CURRENT-STATE.md` §7.2, the A$800-1,250/sqm rate is **`CURRENT-STATE.md`'s own established rate** — not independently sourced to a Perth builder, quantity surveyor, or published commercial-construction cost guide anywhere in this repository. It sits alongside a second, independently-derived figure — `docs/floor-plan-concept.md`'s itemised bottom-up build (A$162,452-306,029, same 239sqm) — which "lands close but not identical" to the A$800-1,250/sqm figure (A$191,200-298,750 at the same footprint), both retained side by side per this repo's own disclosure practice, neither picked as more authoritative.

**Genuine finding: neither figure traces to an external, cited construction-cost benchmark.** Both are internally-generated planning estimates, cross-checked against each other for directional agreement, not against a real market rate.

## 2. What the Rate Includes (Per `floor-plan-concept.md`'s Own Itemisation)

The itemised bottom-up build breaks construction into: demolition/strip-out, walls/partitions (Blood Collection Room only, curtain-partitioned elsewhere), doors, electrical, plumbing (Code-required wet areas), lighting (clinical/task + ambiance), flooring, painting, cabinetry/joinery, privacy curtain systems, HVAC, reception build, staff area fit-out. This is a genuine, itemised trade breakdown — not a single opaque per-sqm number pulled from nowhere.

## 3. What the Rate Does NOT Include, Disclosed Explicitly

Per `floor-plan-concept.md`'s own stated limitation: **"this bottom-up estimate covers wall/door/curtain costs only — it does NOT separately reduce electrical (fewer circuits/switches per enclosed room) or HVAC zoning (shared open-plan air handling vs per-room diffusers/returns), both of which typically also drop when converting enclosed rooms to open-plan/curtain bays."** The source document's own honest assessment: **"this estimate likely understates the true saving, not overstates it"** — i.e. the open-plan conversion may be cheaper than either current figure reflects, not more expensive.

Also not included in either figure: landlord-specific variables (existing services condition, whether the tenancy is a raw shell or has a compatible prior health/beauty fit-out — explicitly flagged in `CURRENT-STATE.md` §7.2 as "needs a fresh assessment once a specific venue candidate exists," not fabricated), and any contingency uplift (a separate 15% fit-out-blowout contingency figure exists in `data/canonical/startup_costs.yml#contingency_fitout_15pct`, itself flagged as "not resolved... whether this 15% is actually incorporated into any of the current headline fit-out figures").

## 4. Is This Rate Appropriate for a Predominantly Open-Plan Fit-Out?

**Directionally yes, but likely still conservative (too high), for a real, disclosed reason.** The venue's current design already minimises walled construction to a single room (the Blood Collection Room — the only clinically-necessary enclosure), with everything else (Lounge, Hairdressing, Nails, and even the Massage/Facial-Beauty rooms) using curtain partitions instead of stud walls. The A$10,736-17,256 wall-to-curtain saving is already itemised and applied in `floor-plan-concept.md`'s own build. But per §3 above, the flow-on savings from open-plan on electrical circuit count and HVAC zoning have NOT been separately quantified in either figure — meaning **both current construction estimates plausibly still carry some walled-room-era electrical/HVAC assumptions baked in**, even though the wall/curtain saving itself was captured.

## 5. Does the Open-Plan Concept Materially Change the Rate?

**Yes, directionally downward, but by an unquantified amount — a genuine open question, not resolved here.** The two already-known savings (wall-to-curtain conversion, ~A$10,736-17,256; and the unquantified electrical/HVAC flow-on from §3) both point the same direction. No new dollar figure is proposed here — quantifying the electrical/HVAC flow-on would require either a real builder's trade-by-trade breakdown (not available without a confirmed venue) or a further bottom-up estimate this document deliberately does not attempt, to avoid inventing precision this repo's own standards don't support.

## 6. Conclusion

The A$800-1,250/sqm rate (and its itemised counterpart, A$679.72-1,280.46/sqm) are **internally-generated planning estimates, not externally benchmarked against a real Perth builder or published construction-cost guide** — a genuine gap, disclosed here for the first time explicitly as its own finding. Both are plausibly still slightly conservative (higher than a real open-plan build would cost) because the electrical/HVAC flow-on savings from the open-plan conversion were identified as real but never quantified. **This does not mean the current figures should be reduced** — per this repo's own standing practice, no dollar figure is invented without a real basis. It means: (1) the current range remains the correct planning figure to use until real quotes exist, and (2) real builder quotes against a confirmed venue, once available, may plausibly land at or below the current range's low end, not above it — worth flagging as a directional expectation for whoever negotiates those quotes, not a promise.

---

## Changelog

**2026-08-16** — Created per C5. Investigates the actual basis of the A$800-1,250/sqm construction rate (internally-generated, not externally benchmarked), what it includes/excludes (a real itemised trade breakdown, missing the electrical/HVAC open-plan flow-on saving), and whether open-plan materially changes it (plausibly yes, downward, unquantified). No new dollar figure invented — the current range remains the correct planning figure pending real quotes.
