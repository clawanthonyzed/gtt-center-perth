# GTT Center Perth — The Case, For Imara

*A plain-English summary of where this stands and why the numbers work. Every figure below traces back to a specific document in this repo — ask to see the source for anything. Rebuilt 2026-07-30 — see `docs/CURRENT-STATE.md` for the canonical, tagged version of every figure here.*

> **Note:** a parallel session is independently rebuilding this same document for comparison, on purpose — this is not a redundant effort. This version is built from this repo's canonical `docs/CURRENT-STATE.md`, cross-checked directly, not copied from an earlier draft.

---

## What this actually is

Pregnant women getting the Glucose Tolerance Test (the standard gestational diabetes screening) spend up to 2.5 hours at a pathology clinic, mostly sitting around waiting between blood draws. GTT Center Perth turns that unavoidable wait into massage, nails, hair, and beauty services — the blood draw still happens, but instead of a waiting room, it's a day spa.

We don't run the lab side ourselves. A pathology partner (Western Diagnostics Pathology — WDP) handles the accreditation and reports results to the patient's doctor, same as any other collection centre. We currently plan to employ the phlebotomist and the treatment staff ourselves, and keep 100% of the wellness revenue — **though one open question could change that (see "What isn't locked down yet" below).**

## The morning (clinical) side pays for itself

This was the open question: does the actual GTT/wellness pairing — the thing that makes this different from a normal day spa — make money on its own, or is it a loss the rest of the business has to carry?

At 10 clients a day (the model we've verified is schedulable with 2 phlebotomist chairs, checked by actually simulating every booking slot, not just estimated) and the lower of our two package prices, A$250:

| | Per day | Per month |
|---|---|---|
| Revenue | A$2,500 | A$55,000 |
| Staff wages (2 phlebotomists + 8 treatment staff, real award rates, super included) | A$2,193 | A$48,255 |
| **What's left over** | **A$307** | **A$6,745** |

That's the floor case — every client at the cheaper package, no upsells. If even some clients take the A$300 package instead, this number goes up, not down.

**One important open question on this figure:** our pathology partner's actual proposal is an annual rental arrangement for the collection clinic space, and their email raises the possibility that *they* employ the phlebotomist under that arrangement, not us. If that turns out to be the case, the A$2,193/day wage line above would be replaced by a rental fee instead — a different, not-yet-modelled number. **Not decided yet — we need to ask them directly before assuming either way.**

## The afternoon (day spa) side is where the real margin is

Same staff, same venue, open to anyone (not just GTT clients) from midday. Because afternoon staff are casual and only paid for booked hours, this side is cheaper to run per dollar of revenue than the morning side — at a conservative estimate of 16 sessions a day, it adds roughly **A$23,700 a month** on top of its own wage cost.

## Put together, at a steady, ongoing pace

| | Per month | Per year |
|---|---|---|
| Total revenue (mornings + afternoons) | A$105,132 | A$1,261,586 |
| Total costs (all wages, rent, insurance, admin, everything) | A$88,625 | A$1,063,501 |
| **Net profit (baseline)** | **A$16,507** | **A$198,085** |

This is the "running normally" figure, not day one — it assumes the booking calendar is full. Realistically it takes a few months to get there; the first year is closer to breakeven while bookings build up, which is normal for any new venue.

**Note on this figure vs an earlier draft:** an earlier version of this brief quoted A$25,087/month and A$301,045/year, which included roughly A$8,580/month of cafe/retail revenue (spray tan, snacks, products). We've since decided to exclude that entirely from the headline number — it's genuinely too uncertain to lean on (no real basis for the figure yet), so the number above is the honest one to plan around. If cafe/retail revenue does materialise once we're open, it's upside on top of this, not baked in.

## Two more upside numbers — real, but not counted in the A$16,507/month above

Staff have real gaps between their own appointments during the morning. We've worked out two separate ways to make use of that, and kept both **deliberately out of the baseline above** because neither has been tested with real demand yet:

| | Monthly figure | What it is |
|---|---|---|
| **Between-client bookings** (staff take an outside client during a genuine gap between two of their own GTT-client appointments, but only if that outside client booked in advance online — no walk-ins, no same-day) | **+A$9,509.50** | Extra revenue, if it happens |
| **Early release** (a staff member's day ends earlier than the standard shift once their last GTT client is done, rather than being paid to sit around) | **+A$14,647.05** | Wage cost avoided, if rostered this way |

Both are worked out from the actual verified schedule (not a guess), and both respect the legal minimum — casual staff can't be engaged for less than 3 hours at a time under the awards that apply here, which we checked directly against the real Fair Work rulebook, not just assumed. Together they're a meaningful upside (~A$24,000/month combined) but neither is guaranteed, so neither is folded into the "A$16,507/month" figure above. Treat them as what could be true once we're operating, not what we're planning around.

## What's already locked down

**Our pathology partner replied — by real email, not just a phone call — on two of the questions that had been hanging over this:**
- **Start time:** they said they wouldn't normally start a test after 10:30am. Our verified schedule finishes its last morning start at 9:40am — comfortably inside that. (We also checked: could we squeeze in a 6th client per chair — 12 a day instead of 10 — given this later cutoff? Yes, the schedule itself holds up with our current 8-person treatment team, though the day would run about 25-40 minutes later and it's not something we're doing yet — just confirmed it's possible if we ever want to.)
- **Specimen pickup timing:** this isn't a hard, fixed cutoff — samples can be stored overnight in some circumstances, and a late booking wouldn't automatically be turned away, though it does depend on specimen type and storage conditions on the day. That's a real, useful, **written** answer, even if it's not an unconditional "anytime works" — we're being careful not to overstate this one, since an earlier internal summary of a phone conversation had rounded it up to "no cutoff at all," which wasn't quite right.

We also know, because we tested it by actually simulating the schedule rather than guessing, that 10 clients a day fits cleanly with 2 phlebotomist chairs.

**How the second chair actually turns on:** rather than running both chairs flat-out every day regardless of demand, the plan is simpler and cheaper to start: a client enquires about a time slot, and it's confirmed on the first chair straight away. If a second person enquires about that same slot, that's when the second chair (and its own phlebotomist and treatment staff) actually opens for that slot. One person alone in a slot doesn't justify the added cost of opening a second chair (roughly A$306 in unavoidable minimum-engagement wages for that slot) — two people does.

## What isn't locked down yet, and needs to happen before this becomes real

We haven't signed a venue lease. We haven't signed an agreement with our pathology partner (they're responsive and the conversation is live and has progressed well, but nothing's in writing yet, and their commercial terms — an annual rental arrangement — aren't quantified yet either). We haven't hired anyone. We haven't had an accountant check the numbers above or confirm the exact startup capital needed — estimates in our own planning have ranged from roughly A$145,000 to A$490,000 depending on which draft, which is exactly why that needs to be pinned down by someone qualified before we commit to a number, rather than picking one of the existing estimates.

**One specific open question that could change the numbers above:** whether we end up employing the phlebotomist ourselves (as modelled) or our pathology partner supplies one as part of their rental arrangement — genuinely undecided, needs a direct conversation with them.

None of that means the idea doesn't work — it means the next step isn't more planning, it's turning these specific unknowns into confirmed answers: a signed (or declined) pathology partnership (including who employs the phlebotomist and what the rental costs), a real venue offer, and an accountant's sign-off on the capital number.

## The honest risk list

The whole model depends on actually filling 10 morning slots a day and a reasonable afternoon booking volume — we haven't tested real customer demand yet (no pre-sales, no deposits, just planning assumptions). The A$200K funding this runs on is Anthony and Imara's joint savings, with no backup source if costs run over. And the profit margin, while real, isn't huge relative to revenue — it's a business that needs to actually run at its planned volume, not one with a lot of room to be sloppy.

---

*Every number in this brief comes directly from `profit-loss-tables.md`, `financial-break-even-staff.md`, `ivy-booking-system.md`, and `docs/CURRENT-STATE.md` in the project repo — happy to pull up the underlying calculation for any of them.*
