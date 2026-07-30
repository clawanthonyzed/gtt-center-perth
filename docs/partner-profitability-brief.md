# GTT Center Perth — The Case, For Imara

*A plain-English summary of where this stands and why the numbers work. Every figure below traces back to a specific document in this repo — ask to see the source for anything. Current as of 2026-07-30 — see `docs/CURRENT-STATE.md` for the canonical, tagged version of every figure here.*

> **Adopted 2026-07-30** from an earlier parallel session's draft, rewritten to correct the funding-source wording (was "personal savings," corrected to joint savings) and updated against this session's most current figures (ancillary revenue excluded, Carole Rivers' actual WDP email integrated, phlebotomist employment model flagged open). Do not treat the earlier draft (if it resurfaces elsewhere) as current — this version supersedes it.

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
| **Net profit** | **A$16,507** | **A$198,085** |

This is the "running normally" figure, not day one — it assumes the booking calendar is full. Realistically it takes a few months to get there; the first year is closer to breakeven while bookings build up, which is normal for any new venue.

**Note on this figure vs an earlier draft:** an earlier version of this brief quoted A$25,087/month and A$301,045/year, which included roughly A$8,580/month of cafe/retail revenue (spray tan, snacks, products). We've since decided to exclude that entirely from the headline number — it's genuinely too uncertain to lean on (no real basis for the figure yet), so the number above is the honest one to plan around. If cafe/retail revenue does materialise once we're open, it's upside on top of this, not baked in.

## What's already locked down

**Our pathology partner replied — by real email, not just a phone call — on two of the questions that had been hanging over this:**
- **Start time:** they said they wouldn't normally start a test after 10:30am. Our verified schedule finishes its last morning start at 9:40am — comfortably inside that.
- **Specimen pickup timing:** this isn't a hard, fixed cutoff — samples can be stored overnight in some circumstances, and a late booking wouldn't automatically be turned away, though it does depend on specimen type and storage conditions on the day. That's a real, useful answer, even if it's not an unconditional "anytime works."

We also know, because we tested it by actually simulating the schedule rather than guessing, that 10 clients a day fits cleanly with 2 phlebotomist chairs.

## What isn't locked down yet, and needs to happen before this becomes real

We haven't signed a venue lease. We haven't signed an agreement with our pathology partner (they're responsive and the conversation is live and has progressed well, but nothing's in writing yet, and their commercial terms — an annual rental arrangement — aren't quantified yet either). We haven't hired anyone. We haven't had an accountant check the numbers above or confirm the exact startup capital needed — estimates in our own planning have ranged from roughly A$145,000 to A$490,000 depending on which draft, which is exactly why that needs to be pinned down by someone qualified before we commit to a number, rather than picking one of the existing estimates.

**One specific open question that could change the numbers above:** whether we end up employing the phlebotomist ourselves (as modelled) or our pathology partner supplies one as part of their rental arrangement — genuinely undecided, needs a direct conversation with them.

None of that means the idea doesn't work — it means the next step isn't more planning, it's turning these specific unknowns into confirmed answers: a signed (or declined) pathology partnership (including who employs the phlebotomist and what the rental costs), a real venue offer, and an accountant's sign-off on the capital number.

## The honest risk list

The whole model depends on actually filling 10 morning slots a day and a reasonable afternoon booking volume — we haven't tested real customer demand yet (no pre-sales, no deposits, just planning assumptions). The A$200K funding this runs on is Anthony and Imara's joint savings, with no backup source if costs run over. And the profit margin, while real, isn't huge relative to revenue — it's a business that needs to actually run at its planned volume, not one with a lot of room to be sloppy.

---

*Every number in this brief comes directly from `profit-loss-tables.md`, `financial-break-even-staff.md`, and `docs/CURRENT-STATE.md` in the project repo — happy to pull up the underlying calculation for any of them.*
