# GTT locked facts preamble (topic-tagged; the builder pastes only the lines a brief needs)

Source: docs/FINANCIAL-CENTER-OF-TRUTH.md (Theodore R21, 2026-10-26), docs/CURRENT-STATE.md section 000 and the Round 21 files in docs/overhaul-2026-10-26/L16-r21/ (GRACE-R21-BOOKING-FLOW-PART-1.md, PART-2.md, MIDWIFE-SLOTS.md, WAITLIST-AND-LATE.md, COMPUTER-FILING.md). If this block and those files ever differ, the files win: fix this block the same day and run `python3 tools/factcheck_locked_facts.py playbooks/GTT-LOCKED-FACTS-PREAMBLE.md`.

## How the tags work (8,000 character rule)

Every line between BEGIN and END starts with `@topic-id` and one space. The builder (tools/build_overnight_brief.py) drops the tag and pastes the line. A spec lists the ids it needs in `"facts": [...]`; the builder adds every `@core-*` line to every brief on top. The core lines together must stay at 1,200 characters or fewer (the builder fails if not). A whole brief over 8,000 characters is refused. Add a new fact as a new tagged line; never paste the whole block into a brief by hand.

| Id | What the line holds |
|---|---|
| core-rules, core-style, core-what, core-money, core-stops | Always included: use-exactly rule, style, what it is, money result, hard stops |
| prices | Step 1 question, Path A and Path B prices, package contents |
| split-b, split-a, checkout | Money split Path B, money split Path A, lab billing and checkout display |
| medicare-b, medicare-open | Medicare rebate lines (Path B), what is confirmed and what is open |
| order, slots | Order of events; midwife slots, priority, same-morning rule |
| morning, late | Test morning timings; the late wording |
| people, midwives, results, mealbreak | Venue and service staff; midwife roster; results messages; meal break flag |
| rooms, filing, changes | Rooms; computer filing; change window, waitlist, illness, refunds |
| structure, outreach, money-notes | Companies and lab term; outreach order; what the profit figure leaves out |

--- BEGIN PREAMBLE ---
@core-rules LOCKED FACTS FOR GTT CENTER PERTH (Anthony, 2026-10-25 and 2026-10-26). Use them exactly. A fact you need that is not in this brief: write NOT IN REPO and move on. Never guess or invent a figure, name, address or date.
@core-style STYLE: Australian dollars (A$). Plain English a 16 year old can read. No em dashes. No square-bracket slots. No floor plans or drawings, words only. Nothing is sent or published; this is a draft for Anthony. Always say client. Sign off Regards.
@core-what WHAT IT IS: a pregnancy-only glucose tolerance test (GTT) lounge in Perth. Luxury day spa and maternal sanctuary feel, not clinical. Working name only (brand names are on hold).
@core-money MONEY RESULT (Theodore R21, locked case, GTT clients on Path B only): profit A$26,631.97 a month before company tax, A$19,973.98 after. Do not recompute. Quote no other profit figure.
@core-stops HARD STOPS: no legal or medical advice (write "lawyer to check"; Catherine owns the legal library); no floor plans; no invented figures; no external sending; no health lawyer cost in any financial figure.
@prices BOOKING STEP 1 is 'Do you have a referral?'. Path B (package with GTT midwife consult): Package 1 A$320, Package 2 A$370, both including the A$27.85 lab fee, GST inside the GTT part. Path A (client keeps her own outside referral, no GTT consult): Package 1 A$265, Package 2 A$315, all in including the A$27.85 lab fee. Plan on 100 percent Package 1. Package 1 has 2 services of 30 minutes; Package 2 has 2 services of up to 45 minutes; both include lounge access and approved drinks.
@split-b MONEY SPLIT, Path B (Package 1): the lab test A$27.85 is paid by the client straight to the lab (the lab bills her) and is never GTT money. GTT receives A$292.15 = consult A$130.00 (GST-free) + lounge and service A$162.15 (GST inside). Package 2: GTT receives A$342.15 = consult A$130.00 + A$212.15. The standalone midwife consult is also A$130.00 GST-free.
@split-a MONEY SPLIT, Path A: GTT receives A$237.15 (Package 1) or A$287.15 (Package 2), A$55.00 less than Path B, all GST-taxable (OPEN until Anthony confirms the Path A price).
@checkout The lab bills the client after it receives the paperwork and samples; GTT never passes booking details to the lab. Checkout shows the full price and the breakdown, shows rebates as 'about', and charges only the GTT amount.
@medicare-b MEDICARE (Structure B only: private all-inclusive, the client claims her own rebate; do not discuss any other billing model): consult is 20 minutes, item 82105, rebate A$32.95. Lab test item 66548 rebate A$16.95 plus collection item 73928 rebate A$5.10 = lab rebate A$22.05 (AskMBS to confirm 73928 or 73938; always say 'about'). Total rebate A$55.00 for consult plus lab together. Never say 'A$55 for the consult'. Client's own cost after Medicare A$265 (Package 1) or A$315 (Package 2), lab fee included. Rebates apply to Path B only. Path A: an outside request gets no Medicare benefit for a test done at GTT and the screen says so (Catherine to confirm wording). Every rebate line is 'about, subject to confirmation'.
@medicare-open Confirmed: item 82105 fee A$38.75 benefit A$32.95; item 66548 fee A$19.90 benefit A$16.95. OPEN: collection item 73928 (A$5.10 benefit) or 73938 (A$6.80); lab rebate and total are 'about A$22 to A$24' and 'about A$55 to A$57'.
@order ORDER OF EVENTS: the client books the TEST first, then the CONSULT (Path B). The consult produces the request and must end before her draw. The client has up to 28 days to book the consult. No consult, no test (Path B). Path A: no consult; her outside request is checked at the door; if unsuitable on the day there is no draw.
@slots MIDWIFE SLOTS: test clients get priority access to midwife slots; a same-morning consult is offered only when it ends before her draw (draw pairs 08:40 and later, one per pair) with a fasting warning. Pairs 07:00 to 08:15 need an earlier-day consult. Midwife on site 08:00, first appointment 08:15, 25-minute blocks. Standalone midwife consults are upside only and are never counted in money.
@morning TEST MORNING: 18 clients a morning, Monday to Saturday, Sunday closed. First draw 07:00, draws 07:00 to 10:30, pairs every 25 minutes (the only cadence). Water only until the final draw. Hard 60 and 120 minute marks from the first draw unless the lab says otherwise. Stand for draw follows the pathology governing bodies and the partner lab. Services fit between draws and never interrupt a draw. Doors shut by 18:00.
@late LATE RULE: arrive at least 10 minutes before the appointment. LATE means from the appointment time onwards: we cannot fit a first blood draw in after that. Use this wording everywhere.
@people PEOPLE: venue manager starts 06:30 (Monday to Friday 06:30 to 15:00) and does reception and welcome; there is no separate front-of-house role; the venue manager sees booking flags only. 8 morning service staff (4 massage and beauty, 2 nails, 2 hair), 07:00 to 13:00. 2 phlebotomists, employed by GTT Medical. 4 casual afternoon service staff. Saturday cover is a senior staff member already rostered. Roles are only those listed here.
@midwives MIDWIVES: 2 permanent part-time (22.5 paid hours each, 45 a week between them) plus 1 casual for leave; fortnightly block, one works Monday to Wednesday and the other Thursday to Saturday, then they swap; they work 08:00 to 16:00 and also take standalone private pregnancy consults when time allows (upside only).
@results RESULTS: the midwife phones only abnormal results; normal results get a generic text or email saying the result is ready, no health detail.
@mealbreak OPEN: a 30 minute unpaid meal break leaves fewer than 18 blocks of 25 minutes; do not state 18 blocks a day.
@rooms ROOMS: 2 collection rooms with 1 chair each; 1 consult room, same size as a collection room. Room sizes in square metres: NOT IN REPO.
@filing FILING: the paper folder is replaced by a secure computer record per test day for referral copies (midwife files, phlebotomists see Today, backups).
@changes CHANGES: OPEN, change window 1 week or 48 hours; waitlist with an automatic email when a slot opens; illness asks for the least proof; the 50 percent lounge-refund idea stands pending Anthony, a delivered consult stays earned.
@structure STRUCTURE: Structure B. Three companies: GTT Holdings (owned directly by Anthony and his partner), GTT Medical Services, GTT Lounge Sanctuary. One partner lab on a 3-year term matching the 3-year lease. Payroll tax is accepted as a cost. Company tax 25 percent.
@outreach OUTREACH: government bodies first, then all 4 labs at once (PathWest, WDP, Saturn, Australian Clinical Labs), starting fresh. Nothing is sent without Anthony's approval of the exact text.
@money-notes MONEY RESULT NOTES: Anthony accepted the profit figure as the starting point. Path A clients are not in it. Interest, standalone consults, Package 2 take-up, retail and card quotes are NOT in it.
--- END PREAMBLE ---
