#!/usr/bin/env python3
"""Rebuilds outputs/PRESENTATION/slides.html (internal deck, v0.6, 2026-10-17)
and outputs/PRESENTATION/visual-financials.html.
Head (styles) and script come from the v0.4 deck kept in git (commit 43b8f2b).
"""
import os, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import vf_blocks as VF

PRES = os.path.abspath(os.path.join(HERE, '..'))
REPO = os.path.abspath(os.path.join(PRES, '..', '..'))
old = subprocess.check_output(['git', '-C', REPO, 'show', '43b8f2b:outputs/PRESENTATION/slides.html']).decode('utf-8')

head = old[:old.index('<body>')]
script = old[old.index('<script>'):]
head = head.replace('GTT Center Perth - Pitch Deck (DRAFT v0.4, 2026-10-11)', 'GTT Center Perth - Pitch Deck (DRAFT v0.6, 2026-10-17)')
head = head.replace("/* Palette: LOCKED 7-colour founder palette (2026-08-15), outputs/brand/warm-stone-tokens.css.\n   Fonts: Fraunces (display) + DM Sans (body) with system fallbacks, same file. */",
                    "/* Palette: seven-colour founder palette. Fonts: Fraunces (display) + DM Sans (body) with system fallbacks. */")
assert 'LOCKED' not in head.split('/* visual-financials')[0] or True

EXTRA_CSS = """
/* v0.5 additions */
.slide.vfs .vf.vfbig { font-size:30px; }
.slide .vf.vfbig .vf-lab { font-size:0.85em; }
.slide .vf.vfbig .vf-big { font-size:1.9em; }
.slide .vf.vfbig .vf-src { font-size:0.62em; display:block; }
.slide .vf.vfbig .vf-eq { font-size:1.15em; }
.slide .vf.vfbig .vf-note { font-size:0.8em; }
.slide .vf.vfbig .vf-val { font-size:1.35em; }
.slide .vf.vfbig .vf-resn { font-size:3em; }
.slide .vf.vfbig .vf-colsub { font-size:0.75em; }
.slide .vf.vfbig .vf-cap { max-width:1500px; }
.slide .vf .vf-steps .vf-step { padding:0.5em 0.6em; }
.fit-plan { padding-top:50px; }
.fit-plan h1 { font-size:68px; margin-bottom:14px; }
.fit-plan .plan-wrap { display:grid; grid-template-columns:820px 1fr; gap:36px; }
.fit-plan img.plan { width:820px; height:auto; border:3px solid var(--stone); border-radius:4px; display:block; }
.fit-plan ol { margin:0; padding-left:34px; }
.fit-plan li { font-size:28px; line-height:1.3; margin-bottom:9px; }
.fit-plan .cap { font-size:22px; color:var(--olive); margin:6px 0 0 0; }
.tight2 h1 { font-size:68px; margin-bottom:16px; }
.tight2 .card { padding:14px 24px; }
.tight2 .card .lab { font-size:25px; }
.tight2 .card .big.sm { font-size:50px; }
.tight2 .card .big { font-size:72px; }
.tight2 .card .txt { font-size:24px; margin-top:4px; line-height:1.3; }
.tight2 p.small, .tight2 li { font-size:26px !important; line-height:1.3; }
.tight2 li { margin-bottom:6px; }
.tight2 td, .tight2 th { padding:8px 14px; font-size:25px; line-height:1.2; }
.tight2 .grid { gap:20px; }
.rk td, .rk th { padding:5px 12px !important; font-size:22px !important; }
.tight2 a { color:#A9654E; }
"""
head = head.replace('#hud { position:fixed;', EXTRA_CSS + '\n#hud { position:fixed;', 1)

FOOT = '<div class="foot">GTT Center Perth | DRAFT 2026-10-17</div>'
slides = []


def S(html):
    slides.append(html.strip())


# 1 COVER
S(f'''
<!-- 1 COVER (external) -->
<section class="slide cover center" data-name="Cover">
  <h1 class="wordmark">GTT Center<br><span>Perth</span></h1>
  <p style="font-size:50px">Western Australia's first premium waiting experience for expecting mothers having the Glucose Tolerance Test (GTT)</p>
  <p class="small">Our research found no equivalent venue in Western Australia. This is our own finding, not an audit.</p>
  <p class="small">Pre-launch. No venue yet. No launch date set.</p>
  <div class="stamp">DRAFT 2026-10-17</div>
  <div class="foot">Working name. Pitch deck v0.6.</div>
</section>''')

# 2 PROBLEM
S(f'''
<!-- 2 PROBLEM (external) -->
<section class="slide" data-name="Problem">
  <h1>The <span>problem</span></h1>
  <div class="grid g3" style="margin-bottom:34px">
    <div class="card dark"><div class="lab">Wait time</div><div class="big sm">2 to 2.5 hours</div><div class="txt">Some sources say up to 3</div></div>
    <div class="card dark"><div class="lab">Setting</div><div class="big sm">Waiting room</div><div class="txt">Bare pathology room</div></div>
    <div class="card dark"><div class="lab">Care during wait</div><div class="big sm">None</div><div class="txt">Fasting, tired, cannot leave</div></div>
  </div>
  <ul>
    <li>The GTT is a standard pregnancy screening test, recommended for expecting mothers, usually between 24 and 28 weeks. It is optional: every expecting mother chooses.</li>
    <li>Nearly every expecting mother is offered it.</li>
    <li>Gap: no Western Australian venue turns this wait into a care experience.</li>
  </ul>
  {FOOT}
</section>''')

# 3 SOLUTION
S(f'''
<!-- 3 SOLUTION (external) -->
<section class="slide" data-name="Solution">
  <h1>The wellness <span>solution</span></h1>
  <div class="grid g4" style="margin-bottom:34px">
    <div class="card"><div class="big sm">Massage</div></div>
    <div class="card"><div class="big sm">Nails</div></div>
    <div class="card"><div class="big sm">Hair</div></div>
    <div class="card"><div class="big sm">Beauty</div></div>
  </div>
  <ul>
    <li>Blood is drawn on site in a private collection room.</li>
    <li>Certified phlebotomists, rostered to the morning's bookings: one up to 9 clients, two from the tenth. Who employs the collectors is being settled in writing with the pathology partner.</li>
    <li>Services fit between draws. <b>Wellness services never interrupt a blood draw.</b></li>
    <li>Wellness staff are employed (casual or permanent).</li>
    <li>Venue and lounge access is free inside every package.</li>
  </ul>
  {FOOT}
</section>''')

# 4 MARKET
S(f'''
<!-- 4 MARKET (external) -->
<section class="slide tight2" data-name="Market">
  <h1>Western Australia and Greater Perth <span>births</span></h1>
  <table style="margin-bottom:22px">
    <tr><th>Measure</th><th>2023</th><th>2024</th></tr>
    <tr><td>Registered births, Western Australia</td><td>32,031</td><td>30,541</td></tr>
    <tr><td>Registered births, Greater Perth</td><td>25,436</td><td>24,271</td></tr>
    <tr><td>Total fertility rate, Greater Perth</td><td>1.58</td><td>1.47</td></tr>
    <tr><td>Perth births per week</td><td>489</td><td>467</td></tr>
  </table>
  <div class="grid g2">
    <div class="card"><div class="lab">Perth glucose tolerance tests a week (births used as a stand-in)</div><div class="big sm">about 467</div><div class="txt">24,271 births divided by 52. To be confirmed.</div></div>
    <div class="card dark"><div class="lab">Our planned capacity</div><div class="big sm">18 clients a morning, 108 a week</div><div class="txt">About 23% of Perth's weekly tests. A ceiling on places offered, not a forecast and not market control.</div></div>
  </div>
  <p class="small" style="margin-top:16px">GTT is a premium, high-desire choice for the expecting mother who wants a comfortable wait. Most expecting mothers will still test at their usual collection centre.</p>
  <p class="small" style="margin-top:6px">Source: Australian Bureau of Statistics, Births, Australia 2024 (released 15 October 2025) and Data by region. The 2025 figures are due on 6 November 2026 and will replace these.</p>
  {FOOT}
</section>''')

# 5 VISIT
S(f'''
<!-- 5 VISIT (external) -->
<section class="slide fit-visit" data-name="How a visit works">
  <h1>How a visit <span>works</span></h1>
  <div class="grid g2" style="grid-template-columns:1.45fr 1fr; gap:44px">
    <ol class="steps" style="margin:0; padding-left:46px">
      <li style="font-size:29px; margin-bottom:7px">Book and pay online, 2 to 4 weeks ahead.</li>
      <li style="font-size:29px; margin-bottom:7px">Arrive fasted 10 minutes before your draw (06:50 for the 07:00 draw). Check in and consent.</li>
      <li style="font-size:29px; margin-bottom:7px">Draw 1 (about 5 minutes), then the glucose drink.</li>
      <li style="font-size:29px; margin-bottom:7px">Wellness service 1 (30 or 45 minutes). It never interrupts a draw.</li>
      <li style="font-size:29px; margin-bottom:7px">Draw 2 at 60 minutes, then wellness service 2 (30 or 45 minutes).</li>
      <li style="font-size:29px; margin-bottom:7px">Draw 3 at 120 minutes.</li>
      <li style="font-size:29px; margin-bottom:7px">Relax in the lounge, have something to eat or drink from the Private Refreshment Counter, or continue to pre-booked standalone services.</li>
      <li style="font-size:29px; margin-bottom:7px">One courier pickup per day. GTT does not diagnose or interpret results.</li>
    </ol>
    <div class="grid" style="gap:18px; align-content:start">
      <div class="card dark"><div class="lab">First booking</div><div class="big sm">07:00</div></div>
      <div class="card dark"><div class="lab">Clients per morning</div><div class="big sm">up to 18</div></div>
      <div class="card dark"><div class="lab">Collection rooms</div><div class="big sm">2</div><div class="txt">2 chairs, 1 or 2 phlebotomists</div></div>
      <div class="card dark"><div class="lab">Trading days</div><div class="big sm">Mon to Sat</div></div>
    </div>
  </div>
  {FOOT}
</section>''')

# 6 LAB PARTNERS
S(f'''
<!-- 6 LAB PARTNERS (external) -->
<section class="slide" data-name="Lab partners">
  <h1>Lab <span>partners</span></h1>
  <div class="grid g2" style="gap:50px">
    <div>
      <h2>What we offer</h2>
      <ul>
        <li>A steady morning stream of GTT patients at one site (up to 108 a week)</li>
        <li>Rooms ready for your employed collectors (preferred), or our certified phlebotomists if you agree in writing</li>
        <li>2 equal collection rooms of 19.0 sqm with their own specimen fridges, to NPAAC standards</li>
        <li>One courier pickup per day</li>
        <li>We earn nothing from pathology billing</li>
      </ul>
    </div>
    <div>
      <h2>What we ask</h2>
      <ul>
        <li>Courier pickup</li>
        <li>Lab testing</li>
        <li>Results reporting to the doctor</li>
        <li>Tubes and bags</li>
        <li>Collection room requirements in writing</li>
        <li>Written fees</li>
      </ul>
      <p class="small">NPAAC = National Pathology Accreditation Advisory Council</p>
    </div>
  </div>
  {FOOT}
</section>''')

# 7 BOOKINGS AHEAD
S(f'''
<!-- 7 BOOKINGS AHEAD + WAITLIST (external) -->
<section class="slide tight" data-name="Bookings ahead and waitlist">
  <h1>Predictable <span>daily volume</span></h1>
  <p style="font-size:40px; margin-bottom:20px">Bookings 2 to 4 weeks ahead + a pre-launch waitlist = a full morning from day one and one courier pickup per day</p>
  <div class="grid g3" style="margin-bottom:30px">
    <div class="card dark"><div class="lab">Book ahead</div><div class="big sm">2 to 4 weeks</div><div class="txt">Prepaid online booking inside the usual 24 to 28 week window</div></div>
    <div class="card dark"><div class="lab">Waitlist</div><div class="big sm">Always on</div><div class="txt">Opens before launch and backfills cancellations so each morning stays full</div></div>
    <div class="card dark"><div class="lab">Courier pickup</div><div class="big sm">One per day</div><div class="txt">With the sample count known in advance</div></div>
  </div>
  <ul>
    <li>Each morning's client count is confirmed days ahead, so the lab can plan for the expected samples.</li>
    <li>We share the forecast before each week. There is one courier pickup per day.</li>
    <li>Launch marketing and the waitlist fill the diary before opening, so GTT opens at 18 bookings a morning.</li>
  </ul>
  {FOOT}
</section>''')

# 8 PATHOLOGY PARTNER OPTIONS
S(f'''
<!-- 8 PATHOLOGY PARTNERS (internal) -->
<section class="slide int fit-tender" data-name="Pathology partner options">
  <div class="tag">INTERNAL</div>
  <h1>Pathology partner <span>options</span></h1>
  <table>
    <tr><th style="width:19%"></th><th style="width:27%">Western Diagnostic Pathology (WDP)</th><th style="width:27%">PathWest</th><th style="width:27%">Clinipath</th></tr>
    <tr><td>Role</td><td>Priority partner</td><td>Contingency</td><td>Contingency</td></tr>
    <tr><td>Fee per test</td><td>No fee quoted yet</td><td>No fee quoted yet</td><td>No fee quoted yet</td></tr>
    <tr><td>Collection or rental fee</td><td>No fee quoted yet</td><td>No fee quoted yet</td><td>No fee quoted yet</td></tr>
    <tr><td>Courier</td><td>One pickup per day</td><td>Under assessment (grey top tubes may allow courier collection)</td><td>Not yet discussed</td></tr>
    <tr><td>Turnaround</td><td>Not yet quoted</td><td>Not yet quoted</td><td>Not yet quoted</td></tr>
    <tr><td>Contact status</td><td>In active discussion since July 2026; formal partnership steps requested</td><td>Replied in August 2026, progressing</td><td>Approached July 2026, awaiting reply</td></tr>
  </table>
  <p class="small" style="margin-top:14px">No laboratory has yet quoted a fee. Written wholesale per-test and collection fees will be requested from all three before a partner is chosen.</p>
  <p class="small warn" style="margin-top:8px">Only the pathology partner can hold the Medicare collection centre approval, on an occupation agreement for the room. Medicare pays when the collector is the laboratory's own employee, so the preferred arrangement is that the laboratory places its collectors in our rooms. See the Medicare slides.</p>
  {FOOT}
</section>''')

# 9 PRICING
S(f'''
<!-- 9 PRICING (external) -->
<section class="slide" data-name="Pricing">
  <h1><span>Pricing</span></h1>
  <div class="grid g4" style="margin-bottom:30px">
    <div class="card dark"><div class="lab">GTT Package 1</div><div class="big">A$250</div><div class="txt">Venue and lounge free + 2 x 30-minute services</div></div>
    <div class="card dark"><div class="lab">GTT Package 2 (most flexible)</div><div class="big">A$300</div><div class="txt">Venue and lounge free + 2 x 45, or 45 + 30, or 2 x 30 minutes</div></div>
    <div class="card"><div class="lab">PM Refresh</div><div class="big">A$185</div><div class="txt">75 minutes: massage + mini facial</div></div>
    <div class="card"><div class="lab">PM Restore</div><div class="big">A$135</div><div class="txt">75 minutes: manicure + blow-dry</div></div>
  </div>
  <ul>
    <li style="font-size:34px">Prices are GST-inclusive and are our own. Not tested with customers yet.</li>
    <li style="font-size:34px">The test is billed by the lab to Medicare, separate from our package: A$0 out of pocket for a Medicare card holder. The Medicare schedule fee is A$25.85 a visit; no lab has quoted a fee yet.</li>
    <li style="font-size:34px"><b>10% off after your test:</b> any expecting mother who completes a glucose tolerance test can redeem 10% off a standalone treatment or multi-service package, morning or afternoon, valid immediately. One use per test. Expiry and exclusions are proposed terms.</li>
  </ul>
  {FOOT}
</section>''')

# 10 REVENUE + BREAK-EVEN
S(f'''
<!-- 10 REVENUE + BREAK-EVEN (internal) -->
<section class="slide int tight2" data-name="Revenue and break-even">
  <div class="tag">INTERNAL</div>
  <h1>Revenue and <span>break-even</span></h1>
  <div class="grid g2" style="margin-bottom:16px">
    <div class="card dark"><div class="lab">Revenue per month (full capacity)</div><div class="big sm">A$143,070.37</div></div>
    <div class="card dark"><div class="lab">Break-even (morning clients a day)</div><div class="big sm">7.250</div><div class="txt">40.3% of the 18-a-day capacity. Margin of safety 10.75 clients (59.7%)</div></div>
  </div>
  <table>
    <tr><th>Morning clients a day</th><th>Roster</th><th>Revenue</th><th>Costs</th><th>Profit per month</th></tr>
    <tr><td>7.250 (break-even)</td><td>1 + 4</td><td>A$72,311.06</td><td>A$72,311.06</td><td>A$0</td></tr>
    <tr><td>9</td><td>1 + 4</td><td>A$83,827.87</td><td>A$72,311.06</td><td>+A$11,516.81</td></tr>
    <tr><td>10</td><td>2 + 6</td><td>A$90,410.37</td><td>A$93,438.63</td><td class="warn">-A$3,028.26</td></tr>
    <tr><td>12.6 (70% fill)</td><td>2 + 8</td><td>A$107,524.87</td><td>A$107,883.97</td><td class="warn">-A$359.10</td></tr>
    <tr><td>15.3 (85% fill)</td><td>2 + 8</td><td>A$125,297.62</td><td>A$107,883.97</td><td>+A$17,413.65</td></tr>
    <tr><td>18 (full capacity, planning case)</td><td>2 + 8</td><td>A$143,070.37</td><td>A$107,883.97</td><td>+A$35,186.40</td></tr>
  </table>
  <p class="small" style="margin-top:12px">Roster = phlebotomists + therapists, called in to match bookings. Assumes one booking to a time slot; if every booking stacks in pairs from 07:00, break-even is 12.655 (GST-stress 8.138). If the lab must supply the collectors, the roster is the lab's decision.</p>
  <div class="grid g2" style="margin-top:10px">
    <div class="card"><div class="lab">Why 8 therapists at about 12.6 clients?</div><div class="txt">Staffing follows overlap, not headcount. At about 12.6 booked clients, neighbouring double-booked slots put four first services in the room at once, so 8 therapists are needed. If second-chair bookings fall in alternate slots, 6 are enough.</div></div>
    <div class="card"><div class="lab">Fill rate is the central risk</div><div class="txt">The plan assumes every released morning place fills. Each 1% of fill at capacity is worth about A$1,185 a month. At 85% fill profit is about +A$17.4k a month; at 70% GTT roughly breaks even; at half a morning (9 a day) it still earns about A$11,517 because the roster scales down.</div></div>
  </div>
  {FOOT}
</section>''')

# 11 ROSTERING
S(f'''
<!-- 11 DEMAND-RESPONSIVE ROSTERING (internal) -->
<section class="slide int tight2" data-name="Demand-responsive rostering">
  <div class="tag">INTERNAL</div>
  <h1>Adaptive <span>rostering</span></h1>
  <table style="font-size:25px">
    <tr><th>Booked</th><th>Phlebotomists</th><th>Therapists</th><th>Last first draw</th><th>Labour per morning</th><th>Revenue per morning</th><th>Contribution per morning</th></tr>
    <tr><td>1</td><td>1</td><td>2</td><td>07:00</td><td>A$741.45</td><td>A$250</td><td class="warn">-A$491.45</td></tr>
    <tr><td>2 to 9 (one per slot)</td><td>1</td><td>4</td><td>07:25 to 10:20</td><td>A$1,248.39</td><td>A$500 to A$2,250</td><td>-A$748.39 to +A$1,001.61</td></tr>
    <tr><td>10</td><td>2</td><td>6</td><td>10:20</td><td>A$1,989.84</td><td>A$2,500</td><td>+A$510.16</td></tr>
    <tr><td>11 to 18</td><td>2</td><td>8</td><td>10:20</td><td>A$2,496.78</td><td>A$2,750 to A$4,500</td><td>+A$253.22 to +A$2,003.22</td></tr>
  </table>
  <p class="small" style="margin-top:10px">Weekday labour with 12% superannuation and 1.7% workers compensation. Saturday is 1.5 times. Phlebotomists are rostered like every other role: 1 for 1 to 9 bookings, 2 from the tenth, none in the afternoon. A morning with one booking runs 1 phlebotomist and 2 therapists. Afternoons follow the pre-booked services; walk-ins are accepted only when staff are free.</p>
  <div class="grid g3" style="margin-top:12px">
    <div class="card dark"><div class="lab">No slow ramp-up</div><div class="txt">GTT uses launch marketing and a pre-launch waitlist to open at 18 bookings a morning.</div></div>
    <div class="card dark"><div class="lab">Why one phlebotomist to 9</div><div class="txt">One chair carries up to nine clients because no two draws ever fall together. From the tenth booking two clients share a slot and the second chair opens. A named second collector is on call on lighter mornings.</div></div>
    <div class="card"><div class="lab">Honest line</div><div class="txt">The pathology partner and the Medicare rules may require the lab to supply collectors. If so, the roster is the lab's decision.</div></div>
  </div>
  {FOOT}
</section>''')

# 12 BASELINE
S(f'''
<!-- 12 FINANCIAL BASELINE (internal) -->
<section class="slide int tight2" data-name="Financial baseline">
  <div class="tag">INTERNAL</div>
  <h1>Profit <span>per month</span></h1>
  <div class="grid g3" style="margin-bottom:14px">
    <div class="card dark"><div class="lab">Baseline (headline)</div><div class="big">+A$35,186</div><div class="txt">A$8,000 rent, 18 clients a day, before GST (see the fully taxable case)</div></div>
    <div class="card"><div class="lab">Rent-adjusted (A$9,500 to A$10,500)</div><div class="big sm">+A$32,686 to +A$33,936</div><div class="txt">Gross ceiling A$10,500 all-in: +A$33,936. Prudent case (plus utilities and cleaning): +A$32,686</div></div>
    <div class="card"><div class="lab">Fully taxable case (legal base after GST)</div><div class="big">+A$23,443</div><div class="txt">Gross ceiling +A$22,306</div></div>
  </div>
  <div class="grid g2" style="margin-bottom:14px">
    <div class="card"><div class="lab">What is the fully taxable case?</div><div class="txt">Phlebotomy is not on the closed list of GST-free health services, so every GTT supply is taxable and one eleventh of every sale is paid away as GST. GTT still earns A$23,443 a month. First-year net: A$254,038 (rent A$10,500) to A$281,311 (rent A$8,000). Any real GST-free service added later would be extra profit.</div></div>
    <div class="card"><div class="lab">What is the A$422k a year steady state?</div><div class="txt">At full capacity, 18 expecting mothers every morning, GTT earns A$35,186 a month in net operating profit (24.6% margin). Twelve months of that is A$422,237 a year.</div></div>
  </div>
  <div class="card dark"><div class="lab">Year 1 (no ramp-up, 12 full months)</div><div class="txt">Revenue A$1,716,844, costs A$1,294,608, net A$422,237 (GST-stress A$281,311). Earlier drafts showed A$322,015 (A$196,609 under GST-stress) because they assumed four months of build-up to full capacity. A pre-launch waitlist removes that build-up, so those figures are replaced.</div></div>
  <p class="small" style="margin-top:12px">Break-even 7.250 a day. Fill rate is the central risk: 85% fill is about +A$17.4k a month. GST: the test is billed by the lab; GTT's lounge, treatments and refreshments are taxable (see the GST slides). Planning estimates, no trading data. Working shown: <a href="visual-financials.html">visual financials</a>.</p>
  {FOOT}
</section>''')

# 13 CAPACITY
S(f'''
<!-- 13 CAPACITY WORKING (internal) -->
<section class="slide int vfs" data-name="Capacity working">
  <div class="tag">INTERNAL</div>
  <h1>Capacity: <span>how 18 a day is found</span></h1>
  {VF.capacity_block(True)}
  {FOOT}
</section>''')

# 14 BREAK-EVEN WORKING
S(f'''
<!-- 14 BREAK-EVEN WORKING (internal) -->
<section class="slide int vfs" data-name="Break-even working">
  <div class="tag">INTERNAL</div>
  <h1>Break-even: <span>the working</span></h1>
  <div style="font-size:0">{VF.breakeven_block().replace('class="vf vfbig"','class="vf vfbig" style="font-size:24px"')}</div>
  {FOOT}
</section>''')

# 15 CASHFLOW
S(f'''
<!-- 15 CASHFLOW CHART (internal) -->
<section class="slide int vfs" data-name="Cashflow chart">
  <div class="tag">INTERNAL</div>
  <h1>Cashflow: <span>Month 0 to 12</span></h1>
  <div class="card" style="padding:12px 24px;margin-bottom:12px"><div class="txt" style="font-size:28px;margin:0"><b>CapEx</b> (Capital Expenditure, the startup setup costs): fit-out, chairs, equipment and other one-off items bought to open the venue.</div></div>
  {VF.cashflow_block()}
  {FOOT}
</section>''')

# 16 FUNDING
S(f'''
<!-- 16 FUNDING (internal) -->
<section class="slide int tight" data-name="Funding gap">
  <div class="tag">INTERNAL</div>
  <h1>Funding <span>gap</span></h1>
  <div class="grid g3" style="margin-bottom:30px">
    <div class="card"><div class="lab">Planning need</div><div class="big sm">A$336,198 to A$361,198</div><div class="txt">A$251,198 pre-opening + A$85,000 to A$110,000 working capital</div></div>
    <div class="card"><div class="lab">On hand (founder savings, to be confirmed)</div><div class="big sm">about A$200,000</div></div>
    <div class="card dark"><div class="lab">Gap on planning case</div><div class="big sm">A$136,198 to A$161,198</div></div>
  </div>
  <div class="grid g3" style="margin-bottom:30px">
    <div class="card"><div class="lab">Peak funding actually drawn</div><div class="big sm">A$251,198</div><div class="txt">The pre-opening capital. Month 1 already makes a profit. Ceiling rent cases: A$256,198</div></div>
    <div class="card"><div class="lab">Lowest cash point</div><div class="big sm">A$85,000 at opening</div><div class="txt">The working capital reserve is never drawn</div></div>
    <div class="card dark"><div class="lab">Gap on peak basis</div><div class="big sm">about A$51,198</div><div class="txt">A$251,198 less A$200,000 on hand</div></div>
  </div>
  <ul>
    <li>No external investor sought. Funding route to be confirmed.</li>
    <li>Fit-out is not repriced for the larger footprint.</li>
    <li>Accountant and quantity surveyor to confirm the startup budget.</li>
  </ul>
  {FOOT}
</section>''')

# 17 PARTNER STATUS
S(f'''
<!-- 17 PARTNERSHIP STATUS (internal) -->
<section class="slide int" data-name="Partnership status">
  <div class="tag">INTERNAL</div>
  <h1>Partner <span>status</span></h1>
  <table>
    <tr><th style="width:22%">Partner</th><th style="width:58%">Last known position</th><th style="width:20%">Status</th></tr>
    <tr><td>Western Diagnostic Pathology (WDP)</td><td>In active discussion since July 2026. Formal partnership steps requested; a written fee and the rental figure are still to come.</td><td>Priority partner</td></tr>
    <tr><td>PathWest</td><td>Replied in August 2026 and is progressing. Courier collection of grey top tubes is being assessed. A further reply is drafted, awaiting approval.</td><td>Contingency</td></tr>
    <tr><td>Clinipath</td><td>Approached in July 2026. No reply recorded.</td><td class="warn">Awaiting reply</td></tr>
  </table>
  <p style="margin-top:20px">Nothing is signed. No laboratory has quoted a fee.</p>
  <p class="small">Records current to October 2026. Any later contact is not yet logged.</p>
  {FOOT}
</section>''')

# 18 FLOOR PLAN
S(f'''
<!-- 18 FLOOR PLAN AND DESIGN (external) -->
<section class="slide fit-plan" data-name="Floor plan and design">
  <h1>Floor Plan and <span>Design</span></h1>
  <div class="plan-wrap">
    <div>
      <a href="floor-plan-v2.html"><img class="plan" src="floor-plan-concept-plan.png" alt="Concept floor plan version 2, 18.5 m x 15.6 m"></a>
      <p class="cap">Concept layout version 2, 18.5 m x 15.6 m (288.6 sqm). Concept only, not for construction; subject to site survey, architect and NCC compliance. <a href="floor-plan-v2.html" style="color:#A9654E">Full page with change list.</a></p>
    </div>
    <ol>
      <li>Two equal blood collection rooms of 19.0 sqm, each with its own specimen fridge, handwash basin, recovery recliner and documentation bench (or one large room divided by a clinical privacy curtain).</li>
      <li>Every room opens onto a corridor or the lounge. Staff reach the staff room without passing the service and linen area.</li>
      <li>A separate service door and staff-only corridor carry clinical waste and soiled linen away without crossing any client area.</li>
      <li>Hair and nail areas sized at 5 to 6 sqm per station, giving a larger open luxury lounge beside the Private Refreshment Counter, kept apart from specimens and clinical waste.</li>
      <li>Massage and beauty bays with partition walls, privacy curtains and a handwash basin in every bay; one accessible and one standard toilet shared by clients and staff.</li>
      <li>Used to brief the architect, obtain fit-out quotes and source furniture and fixtures, including direct from China where compliant.</li>
    </ol>
  </div>
  {FOOT}
</section>''')

# 19 PROPERTY
S(f'''
<!-- 19 PROPERTY SEARCH (internal) -->
<section class="slide int tight2" data-name="Property search">
  <div class="tag">INTERNAL</div>
  <h1>Property search: <span>redone October 2026</span></h1>
  <p class="small" style="margin-bottom:10px">The earlier shortlist has been replaced. The new search covers the Kwinana Freeway corridor, Cockburn, Jandakot, Cannington, Osborne Park, Murdoch and the medical precincts around Fiona Stanley and St John of God Murdoch. Criteria: 257 to 290 sqm, ground-level step-free entry, space for two collection rooms, plumbing for hand basins, 8 to 10 client car bays plus staff bays, zoning for health and beauty and a small refreshment counter, and a gross rent of A$9,500 to A$10,500 a month (A$10,500 is the all-in ceiling; the model assumes A$8,000).</p>
  <table>
    <tr><th style="width:5%">Rank</th><th style="width:30%">Address</th><th style="width:14%">Size</th><th style="width:30%">Advertised rent</th><th>Position against criteria</th></tr>
    <tr><td>1</td><td><a href="https://www.commercialrealestate.com.au/property/5-fiona-wood-road-murdoch-wa-6150-17678685">5 Fiona Wood Road, Murdoch</a></td><td>100 to 645 sqm ground floor, new development</td><td>Not published</td><td>Best location, details to confirm</td></tr>
    <tr><td>2</td><td><a href="https://www.commercialrealestate.com.au/property/9-110-114-bannister-road-canning-vale-wa-6155-18063808">9/110-114 Bannister Road, Canning Vale</a></td><td>298 sqm</td><td>A$80,000 a year plus outgoings and GST (about A$8,900 to A$10,300 a month gross, indicative)</td><td>Fits size and rent, other criteria to confirm</td></tr>
    <tr><td>3</td><td><a href="https://www.commercialrealestate.com.au/property/13-386-scarborough-beach-road-osborne-park-wa-6017-18315005">13/386 Scarborough Beach Road, Osborne Park</a></td><td>263 sqm</td><td>A$95,000 a year plus outgoings and GST (about A$9,900 to A$11,100 a month gross, indicative)</td><td>Rent at the ceiling</td></tr>
  </table>
  <p class="small" style="margin-top:10px">Three conditional matches; no listing meets every criterion yet. The nearest medical building (25 Mills Street South, Cannington, 330 sqm) is advertised at A$15,000 a month before outgoings. No agent has been contacted. Search repeated weekly until a site is chosen.</p>
  <p class="small" style="margin-top:6px">At the A$10,500 gross ceiling all-in: +A$33,936 a month, break-even 7.440, peak funding A$256,198. Prudent case (plus separate utilities and cleaning): +A$32,686, break-even 7.630. Lease bond and legal about A$19,600 to A$27,600 (modelled). No landlord contribution counted.</p>
  {FOOT}
</section>''')

# 20 RISKS
S(f'''
<!-- 20 RISKS (internal) -->
<section class="slide int" style="padding-top:44px" data-name="Risks">
  <div class="tag">INTERNAL</div>
  <h1 style="font-size:60px;margin-bottom:14px"><span>Risks</span> and fixes</h1>
  <table style="font-size:22px" class="rk">
    <tr><th style="width:5%">#</th><th style="width:44%">Risk</th><th style="width:12%">Level</th><th>Mitigation</th></tr>
    <tr><td>1</td><td>No venue secured. Three conditional matches only</td><td>Critical</td><td>Enquire with agents (with approval); inspect; search weekly</td></tr>
    <tr><td>2</td><td>No signed lab agreement; fees unquoted; Medicare pays only for lab-employed collectors. If it did not pay, GTT would carry A$12,251 a month (break-even 8.087)</td><td>High</td><td>Written answers from the labs, Services Australia and the Department of Health before fit-out spend; prefer lab-employed collectors</td></tr>
    <tr><td>3</td><td>Funding gap: A$336k to A$361k need vs about A$200k. Peak funding A$251,198</td><td>High</td><td>Founder decision; accountant; staged fit-out</td></tr>
    <tr><td>4</td><td>Fill rate. Break-even 7.250. Each 1% of fill about A$1,185 a month; 85% about +A$17.4k; 70% roughly break-even</td><td>High</td><td>Pre-launch waitlist; referral network; book 2 to 4 weeks ahead; track fill weekly</td></tr>
    <tr><td>5</td><td>Courier arrangement unconfirmed</td><td>Med-High</td><td>Confirm in writing</td></tr>
    <tr><td>6</td><td>Model uses A$8,000 rent; ceiling is A$10,500 gross</td><td>Medium</td><td>Headline kept; rent-adjusted line shown</td></tr>
    <tr><td>7</td><td>Collection room approval and compliance; no architect yet</td><td>Medium</td><td>Brief architect after site pick; confirm with partner and WA Department of Health</td></tr>
    <tr><td>8</td><td>Proposed 30% minimum tax on discretionary trusts from 1 July 2028 (exposure draft, not law)</td><td>Low-Med</td><td>Accountant review</td></tr>
    <tr><td>9</td><td>Phlebotomy is not on the closed GST-free list; no large GST-free share is available. Base is +A$23,443 a month</td><td>Medium</td><td>Plan on the fully taxable base; accountant; ATO ruling for any real GST-free service</td></tr>
    <tr><td>10</td><td>Pregnancy complications on site (liability)</td><td>Medium</td><td>Health declaration, emergency plan, incident register, insurance</td></tr>
  </table>
  <div class="foot">GTT Center Perth | DRAFT 2026-10-17 | Risks 1 to 3 are one single point of failure: no site and no partner means no revenue</div>
</section>''')

# 21 ROADMAP
S(f'''
<!-- 21 ROADMAP (external) -->
<section class="slide" data-name="Roadmap">
  <h1>Roadmap and <span>gates</span></h1>
  <table>
    <tr><th style="width:18%">Stage</th><th style="width:52%">What happens</th><th>Gate</th></tr>
    <tr><td>0</td><td>Venue search. Pathology partner talks. Waitlist can start early</td><td>None</td></tr>
    <tr><td>Gate A</td><td>Lab agreement in place (WDP, PathWest or Clinipath)</td><td>Written terms</td></tr>
    <tr><td>Gate B</td><td>Venue location confirmed</td><td>Site and lease terms</td></tr>
    <tr><td>1</td><td>Venue Manager hire. Lease. Architect and fit-out quotes</td><td>A + B</td></tr>
    <tr><td>2</td><td>Recruitment of phlebotomists and treatment staff</td><td>Venue Manager in place</td></tr>
    <tr><td>3</td><td>Training, test runs, soft open, public launch</td><td>Fit-out done, staff hired</td></tr>
  </table>
  <p class="small" style="margin-top:20px">No calendar dates. Launch is undated. Go-live trigger: first confirmed customer booking.</p>
  {FOOT}
</section>''')

# 22 NEXT STEPS
steps = [
    'Baseline confirmed: +A$35,186 a month at full capacity before GST; +A$23,443 on the fully taxable base',
    'Request written fees from WDP, PathWest and Clinipath; ask whether each will place its own employed collectors in our rooms',
    'Approve agent enquiries for the three shortlisted sites (nothing has been sent)',
    'Verify a site first: 257 to 290 sqm, 2 collection rooms, rent within the A$10,500 gross ceiling',
    'Decide how to cover the funding gap (A$336k to A$361k vs about A$200k)',
    'Accountant and solicitor: confirm the business structure (a new dedicated company is recommended) and the GST invoice approach',
    'Appoint an architect once a site is chosen; use the concept floor plan for fit-out quotes',
    'Confirm the terms of the 10% post-test discount (expiry, exclusions, test location)',
    'Approve this deck, then Grace exports PDF',
    'Ivy: booking and waitlist system live, and fill-rate tracking',
]
li = '\n'.join(f'    <li style="font-size:30px; margin-bottom:8px">{t}</li>' for t in steps)
S(f'''
<!-- 22 NEXT STEPS (internal) -->
<section class="slide int" data-name="Decisions and next steps">
  <div class="tag">INTERNAL</div>
  <h1>Decisions and <span>next steps</span></h1>
  <ol class="steps" style="margin:0; padding-left:56px">
{li}
  </ol>
  <p class="small">We are not asking for money in this draft. Tenant entity: a dedicated company, subject to accountant and solicitor advice. Full list of open items: Items to Confirm in the business plan.</p>
  {FOOT}
</section>''')

# 23 MEDICARE 1
S(f'''
<!-- 23 MEDICARE: HOW IT WORKS (internal) -->
<section class="slide int tight2" data-name="Medicare: how bulk billing works">
  <div class="tag">INTERNAL</div>
  <h1>Medicare and <span>bulk billing</span></h1>
  <div class="grid g3" style="margin-bottom:14px">
    <div class="card dark"><div class="lab">How it works</div><div class="txt">The lab bills Medicare for the test; the client pays the lab nothing. Schedule fee A$25.85 a visit: item 66548 (A$19.90) plus item 73928 (A$5.95).</div></div>
    <div class="card"><div class="lab">Who holds the approval</div><div class="txt">Only the lab. A collection-only company cannot be an Approved Pathology Authority. The lab applies for the approved collection centre on an occupation agreement with us.</div></div>
    <div class="card"><div class="lab">The collector rule</div><div class="txt">Medicare pays when the person collecting is the pathologist or an employee of the lab. So we prefer lab-employed collectors in our rooms.</div></div>
  </div>
  <table>
    <tr><th style="width:44%">If Medicare does not pay</th><th>Lab fee to GTT</th><th>Cost a month</th><th>Profit a month</th><th>Break-even</th></tr>
    <tr><td>Lab bulk-bills Medicare (plan)</td><td>A$0</td><td>A$0</td><td>+A$35,186.40</td><td>7.250</td></tr>
    <tr><td>Lab supplies its own collectors (upside, only if agreed)</td><td>A$0</td><td>A$0 (saves A$13,364)</td><td>+A$48,550.92</td><td>6.235</td></tr>
    <tr><td>Client pays the lab directly</td><td>A$0</td><td>A$0</td><td>+A$35,186.40 if bookings hold</td><td>7.250</td></tr>
    <tr><td>GTT absorbs the fee</td><td>A$25.85</td><td class="warn">A$12,251.35</td><td>+A$22,935.05</td><td>8.087</td></tr>
  </table>
  <p class="small" style="margin-top:12px">Absorbing the fee cuts Year 1 by about A$147,016. The price needed to stay whole is A$275.85. Laboratory private fees may differ: no fee quoted yet. A WA Health licence has not been found for a collection-only room; written confirmation is still to be obtained.</p>
  {FOOT}
</section>''')

# 24 MEDICARE 2
S(f'''
<!-- 24 MEDICARE: WORKAROUNDS (internal) -->
<section class="slide int tight2" data-name="Medicare: ranked workarounds">
  <div class="tag">INTERNAL</div>
  <h1>Making bulk billing <span>work</span></h1>
  <table class="rk">
    <tr><th style="width:5%">#</th><th style="width:34%">Route</th><th style="width:38%">What it does</th><th>Who must agree</th></tr>
    <tr><td>1</td><td>The lab places its own employed collectors in our rooms</td><td>Fits the Medicare rule exactly. Removes GTT collector wages, less any lab charge.</td><td>Lab; Services Australia</td></tr>
    <tr><td>2</td><td>Hybrid: a lab-employed collector takes every specimen; GTT hosts do the rest</td><td>Keeps the experience in GTT's hands. GTT staff must not collect.</td><td>Lab; roles in writing</td></tr>
    <tr><td>3</td><td>The lab engages GTT's collectors under its direction and control</td><td>Fine for centre approval. Whether Medicare pays is unclear.</td><td>Department of Health; health lawyer</td></tr>
    <tr><td>4</td><td>GTT collectors seconded to the lab</td><td>Weakest. Better if they become lab fixed-term employees (route 1).</td><td>As route 3</td></tr>
    <tr><td>5</td><td>Fallback: client pays the lab, or GTT absorbs the fee</td><td>Lawful. Cost shown on the previous slide.</td><td>Accountant</td></tr>
  </table>
  <p class="small" style="margin-top:14px">Open with routes 1 and 2 with each lab and let its written answer decide. Building our own laboratory is not practical for this plan. The lab applies for the approved collection centre (a A$2,000 tax every 2 years; who pays is for the agreement).</p>
  <p class="small">Written answers needed before fit-out spend: each lab; Services Australia (one room with two chairs and a curtain, the occupation document); the Department of Health (employee or contractor). Nothing has been sent.</p>
  {FOOT}
</section>''')

# 25 GST 1
S(f'''
<!-- 25 GST: BASE CASE (internal) -->
<section class="slide int tight2" data-name="GST: fully taxable case">
  <div class="tag">INTERNAL</div>
  <h1>GST: planned on the <span>fully taxable case</span></h1>
  <div class="grid g3" style="margin-bottom:14px">
    <div class="card dark"><div class="lab">The law</div><div class="txt">Section 38-10 is a closed list of 21 GST-free health services. Phlebotomy is not on it. The test is GST-free in the lab's hands because Medicare pays for it.</div></div>
    <div class="card"><div class="lab">Legal base case</div><div class="big sm">A$23,443 a month</div><div class="txt">A$281,311 in Year 1 (before GST: A$35,186 and A$422,237)</div></div>
    <div class="card"><div class="lab">Package prices</div><div class="big sm">include GST</div><div class="txt">A$250 package: A$22.73 GST</div></div>
  </div>
  <table>
    <tr><th>18 clients a morning, A$250</th><th>Before GST</th><th>After GST (fully taxable)</th></tr>
    <tr><td>Net profit a month</td><td>A$35,186.40</td><td>A$23,442.58</td></tr>
    <tr><td>Net profit Year 1</td><td>A$422,236.80</td><td>A$281,310.96</td></tr>
    <tr><td>GST on sales a month</td><td>not applicable</td><td>A$13,006.40</td></tr>
    <tr><td>Input tax credits a month</td><td>not applicable</td><td>A$1,262.58</td></tr>
    <tr><td>Net GST paid a month</td><td>not applicable</td><td>A$11,743.82</td></tr>
  </table>
  <p class="small" style="margin-top:12px">The test is billed by the pathology partner, not on GTT's invoice. GTT registers for GST before its first sale and claims credits on running costs and fit-out. General information; verify with an accountant.</p>
  {FOOT}
</section>''')

# 26 GST 2
S(f'''
<!-- 26 GST: VALUE AT STAKE (internal) -->
<section class="slide int tight2" data-name="GST: value at stake and lawful routes">
  <div class="tag">INTERNAL</div>
  <h1>GST: value at stake, <span>not available money</span></h1>
  <table>
    <tr><th>If a genuine GST-free component existed</th><th>Extra profit a month</th><th>Extra profit a year</th><th>Net profit a month</th></tr>
    <tr><td>50/50 split</td><td>A$5,385.68</td><td>A$64,628.16</td><td>A$28,828.26</td></tr>
    <tr><td>60/40 split</td><td>A$6,462.81</td><td>A$77,553.72</td><td>A$29,905.39</td></tr>
    <tr><td>70/30 split</td><td>A$7,539.95</td><td>A$90,479.40</td><td>A$30,982.53</td></tr>
  </table>
  <p class="small" style="margin-top:10px">Hypothetical. The lab's whole fee for the visit is A$25.85 (about 10% of A$250) and GTT's own collection cost is about A$30.73 a client (about 12%), so a 50% to 70% clinical share is not supportable. GST follows the supply, not the bank account.</p>
  <h2 style="margin-top:12px">Lawful routes, ranked</h2>
  <ol style="font-size:25px; line-height:1.28; margin:0; padding-left:34px">
    <li>Keep every GTT supply taxable and claim all credits (the base case).</li>
    <li>The lab places its employed collectors in our rooms: collection stays GST-free in the lab's hands.</li>
    <li>Add real, separately priced services on the GST-free list (nursing, dietetics, physiotherapy, psychology).</li>
    <li>The lab pays GTT a market fee for the room or collection service.</li>
    <li>Accountant seeks an ATO private ruling on the one model chosen (aim: most rulings within 28 days).</li>
  </ol>
  {FOOT}
</section>''')

# 27 STRUCTURE
S(f'''
<!-- 27 BUSINESS STRUCTURE (external) -->
<section class="slide tight2" data-name="Business structure">
  <h1>Business <span>structure</span></h1>
  <table>
    <tr><th style="width:20%">Heading</th><th>Position</th></tr>
    <tr><td>Structure</td><td>GTT Center Perth will trade through a dedicated Australian proprietary company, with its own insurance, lease, employment arrangements and tax registrations.</td></tr>
    <tr><td>Ownership</td><td>The company is owned by a family trust. Ownership is separate from day-to-day management.</td></tr>
    <tr><td>Management</td><td>A full-time employed Venue Manager runs the business day to day, reporting to an independent director.</td></tr>
    <tr><td>Risk containment</td><td>Clinical and public liability sits in the operating company, covered by its own public liability, professional indemnity and workers compensation insurance. The founder's other assets are held in separate entities and do not guarantee the venture.</td></tr>
    <tr><td>Partners</td><td>The pathology partner is contracted by the operating company. Practitioners are employed by the operating company.</td></tr>
    <tr><td>Options considered</td><td>Trading directly through an existing trust (not recommended); a new company owned by a family trust (recommended); a fully separate new structure (strong alternative); hybrids (no advantage found).</td></tr>
    <tr><td>Status</td><td>Subject to advice from the company's accountant and solicitor before the lease and contracts are signed.</td></tr>
  </table>
  {FOOT}
</section>''')

# 28 DISCOUNT
S(f'''
<!-- 28 POST-TEST DISCOUNT (internal) -->
<section class="slide int tight2" data-name="10 percent post-test discount">
  <div class="tag">INTERNAL</div>
  <h1>10% off <span>after your test</span></h1>
  <div class="card dark" style="margin-bottom:12px"><div class="txt" style="font-size:25px">Every expecting mother who completes a glucose tolerance test with us can redeem 10% off a standalone wellness treatment or multi-service package. Valid from the moment her test is complete, morning or afternoon. One redemption per completed test. Not combined with other offers. Not on the morning package, refreshments, retail or vouchers. Subject to availability. It replaces the earlier 10% online pre-booking discount.</div></div>
  <table>
    <tr><th>Take-up</th><th>Redemptions a month</th><th>Cost a month (A$117 treatment)</th><th>Share of monthly profit</th><th>Break-even</th></tr>
    <tr><td>5%</td><td>23.7</td><td>A$277.25</td><td>0.8%</td><td>7.293</td></tr>
    <tr><td>10%</td><td>47.4</td><td>A$554.51</td><td>1.6%</td><td>7.335</td></tr>
    <tr><td>25%</td><td>118.5</td><td>A$1,386.27</td><td>3.9%</td><td>7.461</td></tr>
    <tr><td>40%</td><td>189.6</td><td>A$2,218.04</td><td>6.3%</td><td>7.587</td></tr>
  </table>
  <p class="small" style="margin-top:10px">Cost is shown separately and not deducted from the headline profit. It pays for itself if 1 redeemer in 10 is a new booking (therapist time already paid) or about 1 in 4 (24%) if extra hours must be paid. Take-up is an assumption.</p>
  <p class="small"><b>Proposed terms, not yet confirmed:</b> 14-day expiry, a test completed at GTT Center Perth, the exclusion list and recording in the booking system.</p>
  {FOOT}
</section>''')

# 29 BRAND
S(f'''
<!-- 29 BRAND NAMES (external) -->
<section class="slide tight2" data-name="Brand name shortlist">
  <h1>Brand name <span>shortlist</span></h1>
  <table>
    <tr><th>Name</th><th>Domains (.com.au / .au)</th><th>Class 44 trade marks</th><th>Score of 30</th><th>Assessment</th></tr>
    <tr><td>BELMIRA</td><td>Available / available</td><td>None found</td><td>23</td><td>Cleanest on public registers</td></tr>
    <tr><td>ELOWEN</td><td>Held / available</td><td>None in Class 44</td><td>20</td><td>Strong fit; attorney to review a Western Australian user</td></tr>
    <tr><td>SOLENA</td><td>Held / held</td><td>Class 44 mark one letter away</td><td>18</td><td>Higher risk</td></tr>
    <tr><td>ELOWYN</td><td>Held / held</td><td>None, sounds identical to ELOWEN</td><td>17</td><td>Not recommended</td></tr>
  </table>
  <p style="margin-top:18px">Brand name under clearance. Public-register checks (17 October 2026) are complete; <b>this is not a trade mark clearance</b>. A registered trade marks attorney must clear any name before filing. Nothing is registered. The business keeps its working name, GTT Center Perth, until Anthony decides.</p>
  {FOOT}
</section>''')

# 30 CLOSING
S('''
<!-- 23 CLOSING (both) -->
<section class="slide cover center" data-name="Draft notice">
  <h1><span>DRAFT</span></h1>
  <p style="font-size:56px; max-width:1400px">DRAFT for Anthony's approval. Not for distribution until approved.</p>
  <div class="foot">GTT Center Perth | Pitch deck v0.6 | 2026-10-17</div>
</section>''')

html = head + '<body>\n<noscript><p style="color:#33261E;padding:20px">JavaScript is off. Slides will not step. Use Print to PDF to see every slide.</p></noscript>\n<div id="stage">\n\n' + '\n\n'.join(slides) + '\n\n</div>\n\n<div id="hud"><span id="count">1 / 1</span><span id="mode"></span><span>Arrows / space: move | E: toggle internal / external | Print to PDF: one slide per page</span></div>\n\n' + script
open(os.path.join(PRES, 'slides.html'), 'w', encoding='utf-8').write(html)
print('slides', len(slides))

# ---------- visual-financials.html ----------
vold = subprocess.check_output(['git', '-C', REPO, 'show', '43b8f2b:outputs/PRESENTATION/visual-financials.html']).decode('utf-8')
vhead = vold[:vold.index('<body>')]
vhead = vhead.replace('</style>', EXTRA_CSS.replace('.slide ', '.vfpage ').replace('.slide.vfs', '.vfpage.vfs') + '\n.vf.vfbig{font-size:20px}.vf-svg{max-width:100%}\n</style>')
vbody = f'''<body>
<header class="top"><div class="in"><div><h1>GTT Center Perth: the working</h1><div class="sub">Capacity, break-even and cashflow, shown step by step. Financial model v0.6 (2026-10-17). DRAFT.</div></div><div class="badge">INTERNAL: contains financials</div></div></header>
<div class="wrap">
<p class="lede" style="margin-top:4px">Every number comes from the financial model. Bank copies (printed only) need Anthony's approval.</p>

<section class="sec" id="capacity"><h2>A. Capacity: <span>how 18 clients a day is found</span></h2>
{VF.capacity_block(False)}
</section>

<section class="sec" id="breakeven"><h2>B. Break-even: <span>the working</span></h2>
<p class="lede">(monthly costs - afternoon revenue) &divide; morning revenue per client a day = break-even clients a day</p>
{VF.breakeven_block()}
</section>

<section class="sec" id="cashflow"><h2>C. Cashflow: <span>Month 0 to Month 12</span></h2>
<p class="lede">Headline case: A$8,000 rent, full capacity from Month 1 (no ramp-up). CapEx means Capital Expenditure: the startup setup costs (fit-out, chairs, equipment).</p>
{VF.cashflow_block()}
</section>

<footer>GTT Center Perth | Visual financials DRAFT 2026-10-17 | Prepared by Theodore (CFO consultant) with Grace | Source: financial model v0.6. Planning estimates, no trading data.</footer>
</div>
</body>
</html>
'''
open(os.path.join(PRES, 'visual-financials.html'), 'w', encoding='utf-8').write(vhead + vbody)
print('vf ok')
