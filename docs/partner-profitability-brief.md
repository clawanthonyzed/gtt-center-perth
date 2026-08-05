# GTT Center Perth — The Case, For Imara

> **STALE FLAG, 2026-08-05 — NOT YET UPDATED for the 2026-08-05 financial rebase, do not present as-is.** Every 12-client-model dollar figure in this document (AM revenue, AM contribution, Monthly Net P&L, etc.) reflects the OLD, now-historical 12-client/23-min-cadence committed model. The new PRIMARY committed model (18-client/07:00, Monthly Net P&L +A$63,028.75) and SECONDARY reference (12-client/08:00, +A$27,084.69, numerically close to but not derived the same way as this document's figures) have not yet been propagated here — this specific client-facing rewrite was out of scope for this round's explicit file list (`docs/CURRENT-STATE.md`, `docs/profit-loss-tables.md`, `docs/VERIFICATION-TRACKER.md`). Flagged rather than left silently wrong — see `docs/CURRENT-STATE.md` for the current canonical figures before using this document with Imara.

*A plain-English summary of where this stood as of 2026-07-30 and why the numbers worked then. Every figure below traces back to a specific document in this repo — ask to see the source for anything. Updated 2026-07-30 (later same day — a true-maximum search was run and a higher volume was explored and rejected, 12 clients/day remains the committed model) — see `docs/CURRENT-STATE.md` for the canonical, tagged version of every figure here.*

> **Note:** a parallel session is independently rebuilding this same document for comparison, on purpose — this is not a redundant effort. This version is built from this repo's canonical `docs/CURRENT-STATE.md`, cross-checked directly, not copied from an earlier draft.

---

## What this actually is

Pregnant women getting the Glucose Tolerance Test (the standard gestational diabetes screening) spend up to 2.5 hours at a pathology clinic, mostly sitting around waiting between blood draws. GTT Center Perth turns that unavoidable wait into massage, nails, hair, and beauty services — the blood draw still happens, but instead of a waiting room, it's a day spa.

We don't run the lab side ourselves. A pathology partner (Western Diagnostics Pathology — WDP) handles the accreditation and reports results to the patient's doctor, same as any other collection centre. We currently plan to employ the phlebotomist and the treatment staff ourselves, and keep 100% of the wellness revenue — **though one open question could change that (see "What isn't locked down yet" below).**

## The morning (clinical) side pays for itself — and now by more than we thought

This was the open question: does the actual GTT/wellness pairing — the thing that makes this different from a normal day spa — make money on its own, or is it a loss the rest of the business has to carry?

**We now run 12 clients a day, not 10** — our pathology partner told us directly they wouldn't normally start a test after 10:30am, which is later than we'd assumed, so we extended the morning to fit one more client per chair. We tested the extended schedule the same way as before (actually simulating every booking slot, not estimating) and it holds up cleanly with our existing 8-person treatment team — no extra hires needed. At the lower of our two package prices, A$250:

| | Per day | Per month |
|---|---|---|
| Revenue | A$3,000 | A$66,000 |
| Staff wages (2 phlebotomists + 8 treatment staff, real award rates, super included) | A$2,193 | A$48,255 |
| **What's left over** | **A$807** | **A$17,745** |

That's the floor case — every client at the cheaper package, no upsells. If even some clients take the A$300 package instead, this number goes up, not down. **The wage cost didn't change when we added the 2 extra clients** — it's the same 8 people, same pay, just serving more people in a slightly longer morning (about 40 minutes later finish), so the extra revenue is close to pure profit.

**One important open question on this figure:** our pathology partner's actual proposal is an annual rental arrangement for the collection clinic space, and their email raises the possibility that *they* employ the phlebotomist under that arrangement, not us. If that turns out to be the case, the A$2,193/day wage line above would be replaced by a rental fee instead — a different, not-yet-modelled number. **Not decided yet — we need to ask them directly before assuming either way.**

**We also checked whether we could squeeze in even more than 12 (2026-07-30, later the same day)** — Anthony asked us to find the true maximum our 2 chairs can handle before 10:30am, not just confirm 12 works. The honest answer: mathematically, 14 is possible, but only by packing bookings into two tight clusters instead of an even rhythm, and it would need 4 more treatment staff (12 total, not 8) to keep up with those clusters. Once we ran the numbers, the extra 2 clients would bring in A$11,000 a month more revenue, but the extra staff would cost about A$20,538 a month more — a net loss of roughly A$9,538 a month compared to staying at 12. **So we're staying at 12 a day, not pushing to 14** — the "maximum" exists on paper but isn't a better business decision.

## The afternoon (day spa) side is where the real margin is

Same staff, same venue, open to anyone (not just GTT clients) from midday. Because afternoon staff are casual and only paid for booked hours, this side is cheaper to run per dollar of revenue than the morning side — at a conservative estimate of 16 sessions a day, it adds roughly **A$23,700 a month** on top of its own wage cost.

## Put together, at a steady, ongoing pace

| | Per month | Per year |
|---|---|---|
| Total revenue (mornings + afternoons) | A$118,297 | A$1,419,566 |
| Total costs (all wages, rent, insurance, admin, everything) | A$89,809 | A$1,077,705 |
| **Net profit (baseline)** | **A$28,488** | **A$341,861** |

This is the "running normally" figure, not day one — it assumes the booking calendar is full. Realistically it takes a few months to get there; the first year is closer to breakeven while bookings build up, which is normal for any new venue.

**Note on this figure vs earlier drafts:** the figure has moved twice this week, for two separate, deliberate reasons, not because we're guessing. First, we excluded cafe/retail revenue (roughly A$8,580/month) entirely from the headline — it's genuinely too uncertain to lean on, no real basis for the figure yet. That took the number from A$25,087/month to A$16,507/month. Second, we corrected the committed morning volume from 10 clients a day to 12 — the number above (A$28,488/month) reflects both changes together. If cafe/retail revenue does materialise once we're open, it's upside on top of this, not baked in.

## Two more upside numbers — real, but not counted in the A$28,488/month above

Staff have real gaps between their own appointments during the morning. We've worked out two separate ways to make use of that, and kept both **deliberately out of the baseline above** because neither has been tested with real demand yet. Both numbers below are recalculated for the new 12-client schedule, not carried over from the 10-client version — the extra client per chair changes the actual gap pattern, not just the totals:

| | Monthly figure | What it is |
|---|---|---|
| **Between-client bookings** (staff take an outside client during a genuine gap between two of their own GTT-client appointments, but only if that outside client booked in advance online — no walk-ins, no same-day) | **+A$12,679** | Extra revenue, if it happens |
| **Early release** (a staff member's day ends earlier than the standard shift once their last GTT client is done, rather than being paid to sit around) | **+A$16,511** | Wage cost avoided, if rostered this way |

Both are worked out from the actual verified 12-client schedule (not a guess), and both respect the legal minimum — casual staff can't be engaged for less than 3 hours at a time under the awards that apply here, which we checked directly against the real Fair Work rulebook, not just assumed. Together they're a meaningful upside (~A$29,000/month combined) but neither is guaranteed, so neither is folded into the "A$28,488/month" figure above. Treat them as what could be true once we're operating, not what we're planning around.

## What's already locked down

**Our pathology partner replied — by real email, not just a phone call — on two of the questions that had been hanging over this:**
- **Start time:** they said they wouldn't normally start a test after 10:30am. This is exactly why we extended to 12 clients a day — our last morning start is now 10:20am, still 10 minutes inside that guidance.
- **Specimen pickup timing:** this isn't a hard, fixed cutoff — samples can be stored overnight in some circumstances, and a late booking wouldn't automatically be turned away, though it does depend on specimen type and storage conditions on the day. That's a real, useful, **written** answer, even if it's not an unconditional "anytime works" — we're being careful not to overstate this one, since an earlier internal summary of a phone conversation had rounded it up to "no cutoff at all," which wasn't quite right.

We also know, because we tested it by actually simulating the schedule rather than guessing, that 12 clients a day fits cleanly with our existing 2 phlebotomist chairs and 8-person treatment team — no extra hiring needed for this volume, though our morning now finishes around 12:48pm instead of just after midday.

**How the second chair actually turns on — flagged as something we need to re-check:** the original plan was to open the second chair only once 2 people enquire about the same time slot, rather than running both chairs flat-out regardless of demand (roughly A$306 in unavoidable minimum-engagement wages to open a chair for a slot, which one client alone doesn't cover but two does). **Now that 12 clients a day — both chairs running together across the whole morning — is our committed model, this specific enquiry-by-enquiry approach may not fit anymore.** We haven't resolved this — it needs a direct decision, not a guess, on whether that gradual-opening approach still applies (maybe just before we're getting real demand) or whether we now plan for both chairs running from day one.

## What isn't locked down yet, and needs to happen before this becomes real

We haven't signed a venue lease. We haven't signed an agreement with our pathology partner (they're responsive and the conversation is live and has progressed well, but nothing's in writing yet, and their commercial terms — an annual rental arrangement — aren't quantified yet either). We haven't hired anyone. We haven't had an accountant check the numbers above or confirm the exact startup capital needed — estimates in our own planning have ranged from roughly A$145,000 to A$490,000 depending on which draft, which is exactly why that needs to be pinned down by someone qualified before we commit to a number, rather than picking one of the existing estimates.

**One specific open question that could change the numbers above:** whether we end up employing the phlebotomist ourselves (as modelled) or our pathology partner supplies one as part of their rental arrangement — genuinely undecided, needs a direct conversation with them.

None of that means the idea doesn't work — if anything, the numbers look stronger than they did a week ago. The next step isn't more planning, it's turning these specific unknowns into confirmed answers: a signed (or declined) pathology partnership (including who employs the phlebotomist and what the rental costs), a real venue offer, and an accountant's sign-off on the capital number.

## The honest risk list

The whole model depends on actually filling 12 morning slots a day (up from the 10 we'd been planning around) and a reasonable afternoon booking volume — we haven't tested real customer demand yet (no pre-sales, no deposits, just planning assumptions). Filling 2 more daily slots is a bigger ask than filling 10 was, even though the schedule itself can handle it. The A$200K funding this runs on is Anthony and Imara's joint savings, with no backup source if costs run over. And the profit margin, while real, isn't huge relative to revenue — it's a business that needs to actually run at its planned volume, not one with a lot of room to be sloppy.

---

*Every number in this brief comes directly from `profit-loss-tables.md`, `financial-break-even-staff.md`, `ivy-booking-system.md`, `scenario-c-sync-timetables.md`, and `docs/CURRENT-STATE.md` in the project repo — happy to pull up the underlying calculation for any of them.*
