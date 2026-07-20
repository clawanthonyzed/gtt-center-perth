# GTT Center Perth — PM Standalone Package Exploration

**Status:** EXPLORATORY ONLY — not committed, not a decision. Anthony asked for this to be explored and written down, not adopted.

**Version:** 1.0 | **Date:** 2026-07-20

---

## What This Is

Currently, the PM shift (12:00-18:00, no GTT test attached) sells **individual a-la-carte services only** — one massage, one manicure, one blowdry, etc., each priced and booked separately (~A$95 avg/session, per `pm-staffing-roster.md`). This document explores whether PM should **also** offer a bundled package option (2+ services booked together at a modest discount vs booking them separately) for standalone wellness clients who are not doing a GTT test.

This is the same idea already flagged as a lever in `pm-staffing-roster.md` §Levers to Close the Remaining Gap ("Introduce a modest PM package option... Lifting PM avg from A$95 to ~A$115/session adds ~A$7,040/month at 352 sessions") — that mention was written when the PM model still showed a small loss and needed upside levers. The gap has since closed on its own (see `profit-loss-tables.md` v2.0, +A$25,087/month), so this is no longer a "needed to survive" lever — it is now purely an optional revenue-growth idea worth thinking through properly before deciding either way.

**This document does not recommend adopting PM packages.** It lays out the positioning logic, rough pricing math, and staffing effect so the idea can be evaluated later against real PM booking data, not launch-day guesswork.

---

## 1. Positioning — Why This Might Make Sense

- **AM already has a package structure** (Package 2 A$250, Package 3 A$300 — `services-pricing-locked.md`) built around 2 services bundled with the GTT wait. PM clients have no GTT wait to fill, so the "why bundle" logic is different — it would need to stand on its own value (convenience + modest discount), not "something to do while you wait."
- **Some standalone wellness clients naturally want 2+ services anyway** (e.g. a blowdry + gel manicure before an event) — a package makes this an easier single booking decision and a slightly better deal than pricing each service separately, which can nudge average spend up per visit.
- **Risk:** PM package clients take longer per visit (2 services back-to-back, ~75-90 min vs ~30-45 min for a single service), which uses more staff-hours per client at a lower effective hourly staff-cost recovery than 2 separate single-service clients booked back-to-back with a different staff member each — this needs checking against actual PM capacity, not assumed as free upside.

## 2. Rough Pricing Logic (Illustrative Only — Not a Proposal)

Individual PM service prices average ~A$95/session (`pm-staffing-roster.md`, `services-master-table.md`). A simple package model, purely illustrative:

| Package idea | Inclusions | Sum of individual prices (illustrative) | Package price (illustrative ~10-15% discount) | Effective avg/session within package |
|---|---|---|---|---|
| PM Duo | 1× 30-min service + 1× 45-min service | ~A$95 + A$120 = A$215 | ~A$185-195 | ~A$92.50-97.50/session |
| PM Refresh | 2× 45-min services | ~A$120 + A$120 = A$240 | ~A$205-215 | ~A$102.50-107.50/session |

**Important caveat:** these are illustrative arithmetic only, built from the same rough service-price figures already in the corpus — not independently re-verified against a real PM service-price list, and not tested with any actual customer. The A$115 "lifted avg" figure quoted in `pm-staffing-roster.md`'s original lever discussion assumed a specific volume/mix that was never validated either.

## 3. Staffing Effect

- **Single-therapist package (2 services, same practitioner, e.g. massage + facial cross-trained skillset):** works within the existing PM roster's cross-training pattern (`pm-staffing-roster.md` §Multi-Role Relief Hiring already establishes Massage+Beauty cross-qualification) — lowest staffing complexity, since one practitioner delivers both services back-to-back to one client.
- **Two-therapist package (e.g. blowdry + manicure, different skill lines):** requires coordinating two PM staff members' schedules for the same client at overlapping/sequential times — same concurrency logic already modelled for AM in `operations-manual.md`, but PM currently has only 1 dedicated hire per line, so a 2-therapist package would occupy 2 of the 4 PM lines simultaneously for one client, reducing how many separate single-service clients those 2 lines could otherwise serve in that window. This is the main real staffing cost of the idea and needs modelling against actual PM demand patterns, not assumed neutral.
- **Booking system:** Fresha supports package/bundle booking already (used for AM Package 2/3) — no new tooling required if adopted.

## 4. What Would Need to Happen Before Adopting This

1. At least 4-6 weeks of real PM standalone booking data post-launch, showing which individual services clients already tend to book together informally (i.e. do people already book a manicure + blowdry back to back on their own, suggesting latent bundling demand).
2. A genuine price-test — offer a package to a subset of bookings (or via a promo) and compare uptake/avg spend against continuing individual pricing, rather than assuming the illustrative discount above is right.
3. Confirmation that 2-therapist packages don't meaningfully reduce total PM sessions served per day at current 1-per-line headcount (see §3) — may need to wait until PM lines scale to 2 per line (`pm-staffing-roster.md` Locked Decision #2, targeted Month 3-4) before 2-therapist packages make sense without cannibalising single-service capacity.

## 5. Bottom Line

**Worth exploring once real PM booking data exists — not something to build or price now.** No pricing, staffing, or Fresha configuration change is proposed as a result of this document. Revisit alongside the Month 3-6 PM headcount scale-up decision already planned in `pm-staffing-roster.md`.

---

## Related Documents

- `pm-staffing-roster.md` — current PM staffing model and the original (now-closed) gap-closing lever this idea was first mentioned under
- `services-pricing-locked.md` — AM package structure and individual PM service pricing
- `profit-loss-tables.md` — current P&L showing the PM gap has already closed without this lever
- `05_open_questions_for_founder.md` — see also Open Question tracker for anything that needs Anthony's decision before this could move from exploration to a real product change

---

## Changelog

**2026-07-20** — Created as a new exploratory document per Anthony's request: explore (not commit to) a PM standalone package option alongside the existing individual-service model. Positioning, illustrative pricing, and staffing effect covered; explicitly flagged as not a recommendation or decision.
