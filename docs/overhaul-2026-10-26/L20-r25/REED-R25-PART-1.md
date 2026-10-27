# Reed R25 Part 1: Rent and the room licence (Gap 1)

Reed, Commercial Consultant. 2026-10-27. Draft for Anthony. Nothing sent. Four parts: 1 rent and licence, 2 insurance, 3 broker draft and refund wording, 4 start-up fees.

## READ-FIRST CHECK
- Venue manager: a hired person, starts 06:30 (Mon to Fri 06:30 to 15:00). First draw 07:00. Anthony is owner and director, 0 operational hours.
- Path A = package WITH the GTT midwife consult (preferred). Path B = outside referral, no GTT consult (not preferred, not limited).
- Prices: Path A A$320 / A$370 advertised, GTT charges A$292.15 / A$342.15. Path B A$300 / A$350, GTT charges A$272.15 / A$322.15.
- Rebates used: about A$32.95 consult + A$22.05 lab = A$55.00.
- Midwives on site 08:00 to 16:00, first consult 08:15.
- Late rule: blood draws no wiggle room; consults 10 minute grace window.
- Tags: R repo, V verified source (URL and date), E estimate, U unverified. The locked profit (A$26,631.97 before company tax) is NOT changed by anything here.

## 1. What the repo assumes about rent

| Item | Value | Tag | Where |
|---|---|---|---|
| Rent in the model | A$8,000 a month. Set on 200 sqm at A$40 per sqm per month. Anthony said "leave rent as is" on 2026-10-03 | R | docs/CURRENT-STATE.md (rent budget item), DECISION-LOG.md |
| Floor area now planned | 239 to 249 sqm | R | CURRENT-STATE.md, HUMAN-READABLE-STARTUP-COSTS.md |
| Rent ceiling to confirm at lease | A$9,500 to A$10,500 a month gross (base plus outgoings), still OPEN | R | ITEMS-TO-CONFIRM.md, ITC-02 |
| Outgoings on top of base rent | usually 15 to 25 percent | R | data/canonical/opex.yml |
| Room fee Medical pays Lounge | NOT IN REPO | R | FINANCIAL-CENTER-OF-TRUTH.md section 4A |
| Room sizes | NOT IN REPO yet. Grace's file GRACE-R25-ROOM-SIZES.md did not exist when I checked (folder empty) | R | L20-r25 folder |

The repo itself already admits that A$8,000 was built for 200 sqm and the plan grew to 239 to 249 sqm (CURRENT-STATE.md). Anthony chose to keep it.

## 2. Rent per square metre: what the model and the ceiling mean

Simple maths (E): monthly rent x 12, divided by floor area.

| Case | Per sqm per year, gross | Tag |
|---|---|---|
| Model A$8,000 a month, 249 sqm / 239 sqm | A$386 / A$402 | E |
| Ceiling A$9,500 a month, 249 sqm / 239 sqm | A$458 / A$477 | E |
| Ceiling A$10,500 a month, 249 sqm / 239 sqm | A$506 / A$527 | E |

## 3. Current Perth benchmarks (asking rents, not signed deals)

Honest note: the big listing sites blocked me from opening the pages (error 403), so the listing rates below come from search-result summaries on 2026-10-27. Treat each as "seen, page not opened". Ask an agent to confirm.

| Area and property | Type | Rate | Tag | Source |
|---|---|---|---|---|
| Osborne Park, 165 Main St | Ground floor medical or consulting | A$295 per sqm + outgoings + GST. Page updated 17 Feb 2026 | V (search summary) | [commercialrealestate.com.au](https://www.commercialrealestate.com.au/property/165-main-street-osborne-park-wa-6017-17992517) | <!-- factcheck:ok -->
| Osborne Park, 128 Main St | First floor office, marked leased | from A$360 per sqm. Date unclear | U | [realcommercial.com.au](https://realcommercial.com.au/leased/property-unit-3-first-floor-128-main-street-osborne-park-wa-6017-5734270) |
| Cannington, 25 Mills St | 300 sqm medical centre | A$400 per sqm + outgoings + GST. Date not shown | U | [mmj.com.au](https://www.mmj.com.au/properties/25-mills-street-cannington-wa) (page gave 404 when opened) |
| Cannington, 2/7-9 Pattie St | Suite, marked leased 2023 | about A$325 per sqm (my division of the quoted rent) | U, old | [realcommercial.com.au](https://www.realcommercial.com.au/leased/property-2-7-9-pattie-street-cannington-wa-6107-504237808) |
| East Perth, Royal St | Turnkey medical or allied health | A$525 per sqm + GST + outgoings; car bay A$230 a month | U (not a target suburb) | [commercialrealestate.com.au](https://www.commercialrealestate.com.au/property/26-108-112-royal-street-east-perth-wa-6004-2020766658) |
| Perth CBD, prime office (context only) | Net face rent | A$749 (Knight Frank Q2 2026) and A$674 (JLL Q1 2026) | V | [Knight Frank](https://content.knightfrank.com/research/2910/documents/en/australian-office-indicators-q2-2026-12987.pdf), [JLL](https://research.jllapsites.com/appd-market-report/q1-2026-office-perth/) |
| Joondalup, Victoria Park, Subiaco, Myaree | any | no published rate found | U | none |
| Repo location scouting, net per year | Osborne Park 200-350, Joondalup 250-400, Cannington 180-320, Myaree/Murdoch 220-380 | R, undated, not verified | R | docs/location-scouting.md |

## 4. Plausibility verdict: the repo rent is PLAUSIBLE, but at the low end

- Net A$295 to A$400 per sqm, plus 15 to 25 percent outgoings (R), on 239 to 249 sqm gives about A$6,760 to A$10,380 a month (E). <!-- factcheck:ok -->
- The model A$8,000 sits inside that range, below the middle (about A$8,570). It holds if net rent is about A$335 or less with 20 percent outgoings (E maths).
- The ceiling A$9,500 to A$10,500 covers net rates up to roughly A$400 to A$440, so it covers every target-suburb benchmark found.
- East Perth style medical fit-out rents (A$525 net) would break the ceiling. Not a target.
- Cost of being wrong: at the top of the ceiling rent is A$2,500 a month above the model, which would lower profit by about that much before GST credits and company tax (E). The locked profit stays as it is until a real lease exists.
- Check at inspection: these are medical or office asking rents. A day spa with a lounge may be priced as retail, and a change of use needs council approval.

## 5. The room licence from Lounge to Medical: a planning method

Lounge holds the lease. Medical uses the consult and draw rooms under a licence (R, L19-r24 licence outline). Amount: NOT IN REPO, so it stays E.

Recommended method (E): area share.
1. Fee a month = total monthly rent plus outgoings, ex GST, x Medical's share.
2. Medical's share = (Medical's own rooms + a fair slice of shared space such as the front desk and corridors) / total lettable area.
3. Grace's measured room areas fill in the numbers. Until then the amount is E.

Other methods, in order of preference: (b) a fixed percentage of rent that Anthony and the accountant pick; (c) an area share adjusted for hours of use (Medical's rooms are mainly used 07:00 to 16:00 Monday to Saturday).

Sizing aid (maths, E): each 1 percent of share is about A$80 a month at A$8,000 rent and A$105 at A$10,500.

Why it does not change group profit (general knowledge, accountant and lawyer to check): inside a tax consolidated group, payments between the companies are ignored for company tax, and inside a GST group there is no GST on them (R, licence outline item 7). The fee only moves profit between Lounge and Medical.

Why still write it down: it shows an arm's length price if a company is ever sold or the group is split; the landlord must consent to the licence (lease checklist point 9); and it must never be linked to Medicare benefits, test numbers or client numbers (R).

Regards.
