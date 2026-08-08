# GTT Center Perth — The Case, For Imara

*A plain-English summary of where this stands and why the numbers work. Every figure below traces back to a specific document in this repo — ask to see the source for anything. Updated 2026-08-08 — fully rebased to the current committed model (18 clients a day, not 12) — see `docs/CURRENT-STATE.md` for the canonical, tagged version of every figure here.*

---

## What this actually is

Pregnant women getting the Glucose Tolerance Test (the standard gestational diabetes screening) spend up to 2.5 hours at a pathology clinic, mostly sitting around waiting between blood draws. GTT Center Perth turns that unavoidable wait into massage, nails, hair, and beauty services — the blood draw still happens, but instead of a waiting room, it's a day spa.

We don't run the lab side ourselves. A pathology partner (Western Diagnostics Pathology — WDP) handles the accreditation and reports results to the patient's doctor, same as any other collection centre. We currently plan to employ the phlebotomist and the treatment staff ourselves, and keep 100% of the wellness revenue — **though one open question could change that (see "What isn't locked down yet" below).**

## The morning (clinical) side pays for itself — and now by a lot more than we thought

This was the open question: does the actual GTT/wellness pairing — the thing that makes this different from a normal day spa — make money on its own, or is it a loss the rest of the business has to carry?

**We now run 18 clients a day, not 12** — we rebuilt the morning schedule around our pathology partner's exact requirements (precise 1-hour and 2-hour blood-draw marks, not a flexible window) and, once we did that properly, found we could fit far more clients into the same morning than we'd assumed, using the exact same 8-person treatment team — no extra hires needed. This was checked the same way as before (actually simulating every booking slot, not estimating). At the lower of our two package prices, A$250:

| | Per day | Per month |
|---|---|---|
| Revenue | A$4,500 | A$99,000 |
| Staff wages (2 phlebotomists + 8 treatment staff, real award rates, super included) | A$2,193 | A$48,255 |
| **What's left over** | **A$2,307** | **A$50,745** |

That's the floor case — every client at the cheaper package, no upsells. If even some clients take the A$300 package instead, this number goes up, not down. **The wage cost didn't change when we added the extra clients** — it's the same 8 people, same pay, just serving 50% more people in the same morning, so almost all of the extra revenue is pure profit.

**One important open question on this figure:** our pathology partner's actual proposal is an annual rental arrangement for the collection clinic space, and their email raises the possibility that *they* employ the phlebotomist under that arrangement, not us. If that turns out to be the case, the A$2,193/day wage line above would be replaced by a rental fee instead — a different, not-yet-modelled number. **Not decided yet — we've asked them directly and are waiting on a commercial figure; they've confirmed they're actively chasing it internally.** In the meantime, we've worked out what that rental figure would need to be below for WDP-supplied staffing to actually be the cheaper option: roughly **A$105,000-107,000 a year** is the break-even point on wages alone (the 2 phlebotomists' full annual cost, weekday and Saturday combined). Below that, WDP-supplied is cheaper; above it, doing it ourselves is cheaper — though there's a separate, real value in WDP carrying the employment/liability burden instead of us, which isn't captured in that number and is a judgement call, not something we can put a dollar figure on ourselves.

**We also double-checked there wasn't an even bigger number hiding in the schedule.** The uniform, easy-to-communicate 25-minute rhythm between client pairs holds the staffing at exactly 8 people all the way to 18 clients a day — a genuinely better finding than our earlier, tighter-cadence exploration, which needed a 9th treatment staff member just to handle 14 clients. We also tested whether one more pair of clients could be squeezed in at the very end of a later-starting version of the schedule (08:00 start instead of 07:00) — it doesn't work without raising the treatment team to 11 people, so we didn't adopt it.

## The afternoon (day spa) side is where the real margin is

Same staff, same venue, open to anyone (not just GTT clients) from midday. Because afternoon staff are casual and only paid for booked hours, this side is cheaper to run per dollar of revenue than the morning side — at a conservative estimate of 16 sessions a day, it adds roughly **A$23,700 a month** on top of its own wage cost.

## Put together, at a steady, ongoing pace

| | Per month | Per year |
|---|---|---|
| Total revenue (mornings + afternoons, weekdays + Saturday) | A$157,792 | A$1,893,506 |
| Total costs (all wages, rent, insurance, admin, everything) | A$94,763 | A$1,137,161 |
| **Net profit (baseline)** | **A$63,029** | **A$756,345** |

This is the "running normally" figure, not day one — it assumes the booking calendar is full. Realistically it takes a few months to get there; the first year is closer to breakeven while bookings build up, which is normal for any new venue. This figure has moved up materially from the previous version of this brief (A$28,488/month) — not because of a pricing change or a new assumption, but because rebuilding the schedule properly around our pathology partner's exact requirements revealed genuine extra capacity we didn't know we had, at zero extra staffing cost.

**A secondary, more conservative version of this schedule also exists** — starting the morning at 08:00 instead of 07:00, which only fits 12 clients rather than 18 (less room before our pathology partner's 10:30am guidance). It uses the identical 8-person team and lands at **A$27,085/month**, numerically the same as our old committed figure. We're recommending the 18-client, 07:00-start version as the plan, since it uses the same people and the same hours-worked cost but earns 50% more — but we're flagging the alternative explicitly in case there's a reason (demand risk, staff comfort with an earlier start, etc.) to prefer starting smaller.

## Two more upside numbers — real, but not counted in the A$63,029/month above

Staff have real gaps between their own appointments during the morning. We've worked out two separate ways to make use of that, and kept both **deliberately out of the baseline above** because neither has been tested with real demand yet. Both numbers below are recalculated for the new 18-client schedule, not carried over from the 12-client version — the extra clients change the actual gap pattern, not just the totals:

| | Monthly figure | What it is |
|---|---|---|
| **Between-client bookings** (staff take an outside client during a genuine gap between two of their own GTT-client appointments, but only if that outside client booked in advance online — no walk-ins, no same-day) | **+A$3,623** | Extra revenue, if it happens |
| **Early release** (a staff member's day ends earlier than the standard shift once their last GTT client is done, rather than being paid to sit around) | **+A$14,167** | Wage cost avoided, if rostered this way |

Both are worked out from the actual verified 18-client schedule (not a guess), and both respect the legal minimum — casual staff can't be engaged for less than 3 hours at a time under the awards that apply here, which we checked directly against the real Fair Work rulebook, not just assumed. Together they're a meaningful upside (~A$17,800/month combined) but neither is guaranteed, so neither is folded into the "A$63,029/month" figure above. **Note: the between-client bookings figure is smaller than it was under the 12-client schedule** (was A$12,679/month) — a genuine, disclosed side-effect of packing the morning more tightly. The tighter schedule leaves less "dead time" between a given staff member's own appointments, which is good for the headline profit figure but slightly reduces this specific upside line. Treat both figures as what could be true once we're operating, not what we're planning around.

## What's already locked down

**Our pathology partner has replied multiple times now — by real email, not just a phone call — on the questions that had been hanging over this:**
- **Start time:** they said they wouldn't normally start a test after 10:30am. Our morning schedule is built directly around that guidance.
- **Specimen pickup timing:** this isn't a hard, fixed cutoff — samples can be stored overnight in some circumstances, and a late booking wouldn't automatically be turned away, though it does depend on specimen type and storage conditions on the day.
- **Room requirements:** they sent a full list of what our collection room needs to meet accreditation standards. We checked our floor plan against every item — mostly already covered, with a handful of small additions identified (a recovery chair for anyone who feels faint after a blood draw, a couple of minor accessibility/services details) — nothing structural, nothing that changes the numbers above.
- **The "stay at the collection centre" requirement:** they'd asked that clients remain in a specific area for the full two hours. We checked the actual accreditation rulebook directly and found it doesn't set that requirement itself — it turns out to be our partner's own internal policy, which they've since confirmed themselves. The two things that actually matter, in their words, are that the client doesn't leave the building and isn't doing anything strenuous — which our model already satisfies, since the client moves straight from the blood draw to a low-activity treatment (massage, nails) with one staff member responsible for her the whole time. They've taken this internally to their own Quality team to confirm how it applies to a venue like ours — not resolved yet, but progressing, and nothing about it threatens the wellness-during-wait model.
- **Site-assessment criteria:** they'd mentioned things like GPs on-site and referral volumes as part of how they normally assess a location. We flagged that our model doesn't fit that pattern — we're not a GP practice, our volume comes from a dedicated venue built around a mandated test. They've confirmed directly that the absence of doctors on-site isn't an operational concern for them.

We also know, because we tested it by actually simulating the schedule rather than guessing, that 18 clients a day fits cleanly with our existing 2 phlebotomist chairs and 8-person treatment team — no extra hiring needed for this volume.

**How the second chair actually turns on:** both chairs now run together across the whole morning as the committed model — this is baked into the 18-client figure above, not a separate on/off decision.

## What isn't locked down yet, and needs to happen before this becomes real

We haven't signed a venue lease. We haven't signed an agreement with our pathology partner (they're responsive and the conversation is live, detailed, and progressing well — including an internal escalation on our behalf — but nothing's in writing yet, and their commercial terms — an annual rental arrangement — aren't quantified yet either, though they're actively working on that figure with us). We haven't hired anyone. We haven't had an accountant check the numbers above or confirm the exact startup capital needed — our own current, not-yet-verified working estimate, reconciled (not settled — several older, since-superseded planning drafts quoted different ranges) across every planning document we have, is roughly **A$292,000 to A$595,000**, which is exactly why that needs to be pinned down by someone qualified before we commit to a number, rather than treating our own estimate as final.

**One specific open question that could change the numbers above:** whether we end up employing the phlebotomist ourselves (as modelled) or our pathology partner supplies one as part of their rental arrangement — genuinely undecided, actively being discussed with them directly.

None of that means the idea doesn't work — if anything, the numbers look substantially stronger than they did even a week ago. The next step isn't more planning, it's turning these specific unknowns into confirmed answers: a signed (or declined) pathology partnership (including who employs the phlebotomist and what the rental costs), a real venue offer, and an accountant's sign-off on the capital number.

## The honest risk list

The whole model depends on actually filling 18 morning slots a day (up from the 12 we'd been planning around most recently, and 10 before that) and a reasonable afternoon booking volume — we haven't tested real customer demand yet (no pre-sales, no deposits, just planning assumptions). Filling 18 daily slots is a meaningfully bigger ask than filling 12 was, even though the schedule itself can handle it — this is the single biggest open risk in this brief, worth being direct about rather than letting the improved headline number obscure it. A more conservative 12-client version of this same schedule exists as a fallback (see above) if demand doesn't support the full 18. The A$200K funding this runs on is Anthony and Imara's joint savings, with no backup source if costs run over. And the profit margin, while real and now larger, still depends on actually running at the planned volume, not one with a lot of room to be sloppy.

---

*Every number in this brief comes directly from `profit-loss-tables.md`, `financial-break-even-staff.md`, `equipment-costs.md`, `scenario-c-sync-timetables.md`, `docs/VERIFICATION-TRACKER.md`, and `docs/CURRENT-STATE.md` in the project repo — happy to pull up the underlying calculation for any of them.*

## Changelog

**2026-08-08 (fully rebased to the current 18-client committed model, per Anthony's/the coordinator's direct instruction)** — This document previously carried a STALE FLAG (added 2026-08-05) after the venture-wide financial rebase moved past it. Full rewrite this round, not a spot-patch: every dollar figure updated from the old 12-client/23-min-cadence model to the current 18-client/07:00/25-min-cadence Table 1 primary model (Monthly Net P&L A$63,029, was A$28,488), the 12-client secondary reference added as an explicit fallback option (A$27,085/month, numerically unchanged from the old figure), the downtime-fill/early-release upside lines recomputed fresh against the 18-client schedule's actual gap pattern (including disclosing that the between-client-bookings figure is smaller than under the 12-client model — a genuine, not hidden, side-effect), the startup-capital estimate updated to the current reconciled range (A$292,000-595,000, was "A$145,000 to A$490,000"), and the "What's already locked down" section rewritten to reflect Carole's full correspondence through 2026-08-08 (room-spec cross-check, the "stay at the collection centre" policy-not-accreditation finding, the site-assessment-criteria resolution). The old N_max=14 "squeeze in more clients" exploration section (specific to the superseded 12-client model) was removed as no longer relevant — replaced with a brief note on the 18-client model's own headroom testing (25-min cadence holds 8 staff to 18 clients; a 7th-pair test on the 08:00-start variant was tried and rejected). Break-even rental figure for WDP-supplied staffing added as new content (not in any prior version of this brief). Sourced from `docs/CURRENT-STATE.md`, `docs/profit-loss-tables.md`, `docs/VERIFICATION-TRACKER.md` items 1c/1d/1d-be/29/29b/29c/29d/30, and `docs/equipment-costs.md` — cross-checked directly, not copied from an earlier draft.
