# GTT Center Perth — PM Package Structure (Committed)

**Status:** COMMITTED DIRECTION (2026-07-20). Anthony confirmed: PM will offer both individual standalone a-la-carte services (existing, unchanged) AND set/fixed PM packages (new), with an active strategy to steer/upsell clients toward the package option since it drives higher revenue per PM visit. **Dollar pricing below is proposed and modelled, not locked — every price figure in this document requires Anthony's sign-off before it goes live in Fresha or any client-facing material.**

**Version:** 2.0 | **Date:** 2026-07-20 (supersedes `pm-package-exploration.md`, renamed and elevated from exploratory to committed per Anthony's direct confirmation: *"add pm packaging into the pm structure. we will push pm clients to the package option for more revenue."*)

---

## What This Is Now

PM (12:00-18:00, no GTT test, no fasting requirement) offers **two booking tiers**:

1. **Individual a-la-carte services** (existing, unchanged) — one massage, one manicure, one blowdry, etc., each priced and booked separately (~A$95 avg/session, per `pm-staffing-roster.md`).
2. **Set/fixed PM packages** (new, committed direction) — a small number of specific, pre-defined 2-service combos at a set price, with an explicit sales strategy to present and steer clients toward this option first, since it generates materially more revenue per visit than a single standalone service.

**Reminder of the flexibility distinction (unchanged from the exploratory version, still important):** PM packages are the opposite of AM's Package 2 — **set/fixed combos, not client-choice.** A client picks from a short menu of named packages (e.g. "PM Duo," "PM Refresh"), each with a fixed, pre-defined service pairing — they do not build their own combination the way AM's Package 2 allows.

---

## Proposed Package Options — ANTHONY TO CONFIRM PRICING

**These are drafted, modelled proposals, not final prices.** Built from real service durations/prices in `services-master-table.md`, with the discount level chosen specifically to keep total package revenue meaningfully higher than the standalone average per visit (modelled below in §Revenue Modelling) — not just guessed at a round discount percentage.

| Package name | Fixed inclusions | Sum of individual prices | Proposed package price (10% off) | Proposed package price (15% off) | Duration |
|---|---|---|---|---|---|
| **PM Duo** | Blowdry (30min, A$65) + Express Glow Facial (30min, A$95) | A$160 | **A$144** | **A$136** | ~60-75 min |
| **PM Refresh** | Standard Pregnancy Massage (45min, A$120) + Signature Pregnancy Facial (45min, A$130) | A$250 | **A$225** | **A$212** | ~90-100 min |
| **PM Glow** | Gel Manicure (45min, A$75) + Express Glow Facial (30min, A$95) | A$170 | **A$153** | **A$144** | ~75-90 min |

**Recommendation (Anthony's call, not locked):** the 10% discount tier is the more conservative starting point — it preserves more margin per package while still being a genuine, visible saving vs booking separately. The 15% tier is a stronger upsell incentive if early package uptake is slow and needs a bigger nudge. Either could be tested against real bookings once live; this document does not pick one over the other.

**Service pairings above are illustrative proposals, not the only possible combos** — `services-master-table.md` has other plausible pairings (e.g. Brow Lamination + Express Facial, Blowdry + Gel Manicure); the 3 shown are a reasonable starting menu size (not too many choices to complicate rostering/Fresha setup) but Anthony may want different specific pairings.

---

## Revenue Modelling — Why This Increases Revenue Per PM Visit (Checked, Not Assumed)

**The mechanism:** a package converts what would otherwise be a single-service booking (~A$95 avg) into a two-service booking at a higher total price — even after the bundle discount, the package price is still well above the standalone average, because the discount is applied to the *sum of two services*, not used to make the package cheaper than one service.

| Comparison | Revenue per visit |
|---|---|
| Standalone visit (1 service, current average) | ~A$95 |
| PM Duo (10% off) | A$144 — **1.5x higher** |
| PM Refresh (10% off) | A$225 — **2.4x higher** |
| PM Glow (10% off) | A$153 — **1.6x higher** |

**Checked against staff capacity, not just per-visit revenue (the real trade-off):** a package visit takes longer than a standalone visit (60-100 min vs 30-45 min), so pushing every client toward packages means fewer total visits fit in a 6-hour PM shift. Modelled per single staff member's 6-hour shift, using `pm-staffing-roster.md`'s existing ~1.3 sessions/hr throughput assumption:

| Scenario | Sessions/packages per staff per 6hr shift | Revenue per staff per shift |
|---|---|---|
| All standalone (current model) | ~7.8 single-services | ~A$741 |
| All PM Refresh packages (10% off) | ~4.0 packages | ~A$900 |
| 50/50 mix (by time) | ~3.9 standalone + ~2.0 packages | ~A$795 |

**Finding: pushing toward packages increases total revenue per staff-hour, even though it reduces the total number of bookings served** — the higher price-per-booking more than offsets the lower booking count, at every discount level modelled (10% and 15%). This confirms Anthony's stated strategy is directionally sound, not just a hopeful assumption — but see the caveats below before treating the specific numbers as final.

**What this modelling does NOT prove:**
1. **Real client uptake is unknown.** This models "if X% of clients choose packages," not what X actually will be — no booking data exists yet. If clients don't take up the package option at a meaningful rate, none of this upside materialises; the "push toward package" sales strategy (see below) is what has to actually work for this to pay off.
2. **Two-therapist packages have a different, worse capacity trade-off** than the single-therapist packages priced above — see §Staffing Effect below, largely unchanged from the exploratory version's finding.
3. **Illustrative service pairings, prices, and discount levels are not final** — Anthony's confirmation required before anything goes live.

---

## Sales Strategy — "Push Toward Package" (Committed Direction, Practical Mechanics)

Per Anthony's direction to actively steer clients toward the package option, this needs to be reflected in both the booking flow and staff behaviour, not just exist as a priced menu option:

1. **Fresha booking flow:** when a client searches for or selects an individual service that has a package equivalent (e.g. selects "Standard Pregnancy Massage"), the booking flow should surface the relevant package (e.g. "PM Refresh — add a Signature Facial for just A$X more") as the first suggested option, with the standalone single-service booking still available but not the default-highlighted choice. This is standard upsell UX already supported by most booking platforms including Fresha — needs to be configured at setup, not assumed automatic.
2. **Reception/phone script:** the Receptionist/Manager, when taking a PM booking by phone or in person, should mention the relevant package option before confirming a single-service booking (e.g. "Would you like to add on a facial with that for A$X extra? It's a small saving versus booking them separately.") — a soft, value-framed upsell, not a hard sell.
3. **In-venue signage/menu:** PM package options should be listed above or more prominently than the individual a-la-carte menu on any printed or digital menu, consistent with the "steer toward package" direction.
4. **Staff incentive (flagged, not decided):** whether treatment staff have any commission/incentive tied to package uptake (vs standalone bookings) is a genuine open question this document does not resolve — a possible lever if uptake is slower than hoped, but a compensation-structure decision for Anthony, not assumed here.

---

## Staffing Effect (Carried Forward from the Exploratory Version, Still Applies)

- **Single-therapist packages (PM Duo/Refresh/Glow style, one practitioner delivers both services back-to-back):** works within the existing PM roster's cross-training pattern (`pm-staffing-roster.md` §Multi-Role Relief Hiring, Massage+Beauty cross-qualification) — lowest staffing complexity. All 3 proposed packages above can be delivered by a single cross-trained practitioner (Massage+Beauty pairing covers PM Refresh and PM Glow's facial component; a Hair+Nail cross-trained hire, if one exists, would be needed for PM Duo — otherwise PM Duo needs 2 staff members).
- **Two-therapist packages (different skill lines, e.g. PM Duo if no single practitioner covers both Blowdry and Facial):** requires coordinating two PM staff members for the same client — occupies 2 of the 4 PM lines simultaneously for one client, reducing how many separate single-service clients those 2 lines could otherwise serve in that window. This is a real capacity cost, not modelled as free.
- **Booking system:** Fresha supports package/bundle booking already (used for AM Package 1/2) — no new tooling required.
- **Recommendation:** prioritise single-therapist packages (PM Refresh, PM Glow) for the initial launch of this feature, since they don't add the 2-staff coordination cost — revisit PM Duo (or restructure it to a single-therapist pairing, e.g. swap in a Beauty-Beauty or Massage-Beauty combo) if a 2-staff package is wanted from Day 1.

---

## What Would Need to Happen Before This Goes Live

1. **Anthony confirms specific package names, service pairings, and pricing** (§Proposed Package Options above) — nothing here is final.
2. **Fresha configured** with the new package SKUs and the upsell-surfacing behaviour described in §Sales Strategy.
3. **Reception script updated** (`onboarding.md` or a dedicated script document) to include the package-mention step.
4. **Menu/signage updated** to list packages above individual services.
5. **Staff briefed** on the new package menu and the "mention the package option" expectation before launch.

---

## Related Documents

- `pm-staffing-roster.md` — current PM staffing model, cross-training pairings, hours-based costing method used in the revenue modelling above
- `services-master-table.md` — source service list, durations, and prices used to build the proposed package combos
- `services-pricing-locked.md` — AM package structure (client-choice model, the opposite of PM's set/fixed model)
- `cash-flow.md` — PM revenue line, updated to reference this committed package direction
- `business-plan.md` — Revenue Streams section, updated to reflect PM's two-tier (standalone + package) offering
- `poppy-marketing.md`, `afternoon-marketing-plan.md` — PM marketing content, updated to reflect the package-forward positioning

---

## Changelog

**2026-07-20** — Superseded `pm-package-exploration.md`. Elevated from exploratory to committed direction per Anthony's direct confirmation. Added: 3 proposed package options with modelled pricing (clearly marked as requiring Anthony's sign-off, not final); revenue modelling showing packages increase revenue per staff-hour despite fewer total bookings served (checked via the existing 1.3 sessions/hr throughput assumption, not guessed); an explicit sales-strategy section describing how the booking system, reception script, and signage should steer clients toward packages; carried forward the staffing-effect analysis from the exploratory version largely unchanged. Cascaded the committed-direction framing into `services-pricing-locked.md`, `services-master-table.md`, `business-plan.md`, `cash-flow.md`, `poppy-marketing.md`, `afternoon-marketing-plan.md`, `staff-plan.md`, `HANDOFF.md`, `reading-order.md`.
