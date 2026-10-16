#!/usr/bin/env python3
"""Rebuilds outputs/PRESENTATION/slides.html (internal deck, 23 slides, v0.5, 2026-10-16)
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
head = head.replace('GTT Center Perth - Pitch Deck (DRAFT v0.4, 2026-10-11)', 'GTT Center Perth - Pitch Deck (DRAFT v0.5, 2026-10-16)')
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

FOOT = '<div class="foot">GTT Center Perth | DRAFT 2026-10-16</div>'
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
  <div class="stamp">DRAFT 2026-10-16</div>
  <div class="foot">Working name. Pitch deck v0.5.</div>
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
    <li>2 certified phlebotomists on every testing morning. Who employs the collection staff is subject to written confirmation from the pathology partner and Medicare.</li>
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
      <div class="card dark"><div class="lab">Collection rooms</div><div class="big sm">2</div><div class="txt">2 chairs, 2 phlebotomists</div></div>
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
        <li>A steady morning stream of GTT patients at one site (up to 108 a week at capacity)</li>
        <li>Certified phlebotomists on every testing morning (employment arrangement to be confirmed in writing with the partner and Medicare)</li>
        <li>2 dedicated blood collection rooms built to national standards (NPAAC)</li>
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
  <p class="small warn" style="margin-top:8px">The pathology partner holds the Medicare collection centre approval and an occupation agreement for the collection room. Who employs the collectors is subject to written confirmation from the partner and Medicare.</p>
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
    <li style="font-size:34px">The pathology fee is billed by the lab, separate from our package. Out-of-pocket estimate A$0 to A$80, to be confirmed. Written fees are being requested from PathWest, WDP and Clinipath.</li>
    <li style="font-size:34px">Test Day Thank You (proposed): an exclusive discount on a standalone afternoon treatment booked within 14 days of the test. Discount level to be set.</li>
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
    <div class="card dark"><div class="lab">Break-even (morning clients a day)</div><div class="big sm">8.266</div><div class="txt">45.9% of the 18-a-day capacity</div></div>
  </div>
  <table>
    <tr><th>Morning clients a day</th><th>Roster</th><th>Revenue</th><th>Costs</th><th>Profit per month</th></tr>
    <tr><td>8.266 (break-even)</td><td>2 + 4</td><td>A$78,993.29</td><td>A$78,993.29</td><td>A$0</td></tr>
    <tr><td>9</td><td>2 + 4</td><td>A$83,827.87</td><td>A$78,993.29</td><td>+A$4,834.58</td></tr>
    <tr><td>10</td><td>2 + 6</td><td>A$90,410.37</td><td>A$93,438.63</td><td class="warn">-A$3,028.26</td></tr>
    <tr><td>12.6 (70% fill)</td><td>2 + 8</td><td>A$107,524.87</td><td>A$107,883.97</td><td class="warn">-A$359.10</td></tr>
    <tr><td>15.3 (85% fill)</td><td>2 + 8</td><td>A$125,297.62</td><td>A$107,883.97</td><td>+A$17,413.65</td></tr>
    <tr><td>18 (full capacity, planning case)</td><td>2 + 8</td><td>A$143,070.37</td><td>A$107,883.97</td><td>+A$35,186.40</td></tr>
  </table>
  <p class="small" style="margin-top:12px">Roster = phlebotomists + therapists. Staff are called in to match confirmed bookings. Margin of safety: 9.7 clients a day. If every booking stacks in pairs from 07:00, break-even rises to 12.655.</p>
  <div class="grid g2" style="margin-top:10px">
    <div class="card"><div class="lab">Why 8 therapists at about 12.6 clients?</div><div class="txt">Staffing follows overlap, not headcount. Each client has two services and pairs start 25 minutes apart. At about 12.6 booked clients neighbouring double-booked slots put four first services in the room at once, so 8 therapists are needed. If second-chair bookings fall in alternate slots, 6 are enough.</div></div>
    <div class="card"><div class="lab">Fill rate is the central risk</div><div class="txt">The plan assumes every released morning place fills. Each 1% of fill at capacity is worth about A$1,185 a month. At 85% fill profit is about +A$17.4k a month; at 70% GTT roughly breaks even. That is why the waitlist matters.</div></div>
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
    <tr><td>1</td><td>2</td><td>2</td><td>07:00</td><td>A$975.96</td><td>A$250</td><td class="warn">-A$725.96</td></tr>
    <tr><td>2 to 9 (one per slot)</td><td>2</td><td>4</td><td>07:25 to 10:20</td><td>A$1,482.90</td><td>A$500 to A$2,250</td><td>-A$982.90 to +A$767.10</td></tr>
    <tr><td>10</td><td>2</td><td>6</td><td>10:20</td><td>A$1,989.84</td><td>A$2,500</td><td>+A$510.16</td></tr>
    <tr><td>11 to 18</td><td>2</td><td>8</td><td>10:20</td><td>A$2,496.78</td><td>A$2,750 to A$4,500</td><td>+A$253.22 to +A$2,003.22</td></tr>
  </table>
  <p class="small" style="margin-top:10px">Weekday labour with 12% superannuation and 1.7% workers compensation. Saturday is 1.5 times. Staff are called in to match confirmed bookings. A morning with one booking runs 2 phlebotomists and 2 therapists, not a full team. Afternoons follow the pre-booked services; walk-ins are accepted only when staff are free.</p>
  <div class="grid g3" style="margin-top:12px">
    <div class="card dark"><div class="lab">No slow ramp-up</div><div class="txt">GTT uses launch marketing and a pre-launch waitlist to open at 18 bookings a morning.</div></div>
    <div class="card dark"><div class="lab">Book 2 to 4 weeks ahead</div><div class="txt">The standard for every time slot. The roster is published 1 to 2 weeks ahead from confirmed bookings.</div></div>
    <div class="card"><div class="lab">Phlebotomist minimum</div><div class="txt">2 on every testing morning, GTT's clinical standard, pending the pathology partner's answer.</div></div>
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
    <div class="card dark"><div class="lab">Baseline (headline)</div><div class="big">+A$35,186</div><div class="txt">A$8,000 rent, 18 clients a day, GST not deducted (subject to an ATO private ruling)</div></div>
    <div class="card"><div class="lab">Rent-adjusted (A$9,500 to A$10,500)</div><div class="big sm">+A$32,686 to +A$33,936</div><div class="txt">Gross ceiling A$10,500 all-in: +A$33,936. Prudent case (plus utilities and cleaning): +A$32,686</div></div>
    <div class="card"><div class="lab">GST-stress (prudent planning case)</div><div class="big">+A$23,443</div><div class="txt">Gross ceiling +A$22,306</div></div>
  </div>
  <div class="grid g2" style="margin-bottom:14px">
    <div class="card"><div class="lab">What is GST-stress?</div><div class="txt">The safety test that assumes the Australian Taxation Office treats the whole package as taxable, so one eleventh of every sale is paid away as GST. GTT still earns A$23,443 a month. First-year net under the test: A$254,038 (rent A$10,500) to A$281,311 (rent A$8,000). Any GST-free element the ATO confirms would be extra profit.</div></div>
    <div class="card"><div class="lab">What is the A$422k a year steady state?</div><div class="txt">At full capacity, 18 expecting mothers every morning, GTT earns A$35,186 a month in net operating profit (24.6% margin). Twelve months of that is A$422,237 a year.</div></div>
  </div>
  <div class="card dark"><div class="lab">Year 1 (no ramp-up, 12 full months)</div><div class="txt">Revenue A$1,716,844, costs A$1,294,608, net A$422,237 (GST-stress A$281,311). Earlier drafts showed A$322,015 (A$196,609 under GST-stress) because they assumed four months of build-up to full capacity. A pre-launch waitlist removes that build-up, so those figures are replaced.</div></div>
  <p class="small" style="margin-top:12px">Break-even 8.266 a day. Fill rate is the central risk: 85% fill is about +A$17.4k a month. GST: clinical pathology is billed by the lab; GTT's lounge, treatments and refreshments are taxable; our accountant will seek an ATO private ruling. Planning estimates, no trading data. Working shown: <a href="visual-financials.html">visual financials</a>.</p>
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
      <a href="floor-plan-concept.png"><img class="plan" src="floor-plan-concept-plan.png" alt="Concept floor plan, 18.5 m x 15.6 m"></a>
      <p class="cap">Concept layout, 18.5 m x 15.6 m (about 289 sqm). Concept only; subject to site survey, architect and NCC compliance. <a href="floor-plan-concept.png" style="color:#A9654E">Full drawing.</a></p>
    </div>
    <ol>
      <li>Two dedicated blood collection rooms, or one large room divided by a clinical privacy curtain.</li>
      <li>Open-plan luxury lounge beside collection, with a Private Refreshment Counter for GTT clients only.</li>
      <li>Massage and beauty bays with partition walls, privacy curtains and a handwash basin in every bay.</li>
      <li>Specimen fridge and clinical waste kept physically separate from the refreshment counter.</li>
      <li>Accessible toilet, staff room and storage, within the 257 to 290 sqm site range.</li>
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
  <p class="small" style="margin-top:6px">At the A$10,500 gross ceiling all-in: +A$33,936 a month, break-even 8.455, peak funding A$256,198. Prudent case (plus separate utilities and cleaning): +A$32,686, break-even 8.645. Lease bond and legal about A$19,600 to A$27,600 (modelled). No landlord contribution counted.</p>
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
    <tr><td>2</td><td>No signed lab agreement; fees unquoted; who employs the collectors for Medicare billing unresolved</td><td>High</td><td>Written fees from all three labs; written answer from the partner and Medicare before fit-out spend</td></tr>
    <tr><td>3</td><td>Funding gap: A$336k to A$361k need vs about A$200k. Peak funding A$251,198</td><td>High</td><td>Founder decision; accountant; staged fit-out</td></tr>
    <tr><td>4</td><td>Fill rate. Break-even 8.266. Each 1% of fill about A$1,185 a month; 85% about +A$17.4k; 70% roughly break-even</td><td>High</td><td>Pre-launch waitlist; referral network; book 2 to 4 weeks ahead; track fill weekly</td></tr>
    <tr><td>5</td><td>Courier arrangement unconfirmed</td><td>Med-High</td><td>Confirm in writing</td></tr>
    <tr><td>6</td><td>Model uses A$8,000 rent; ceiling is A$10,500 gross</td><td>Medium</td><td>Headline kept; rent-adjusted line shown</td></tr>
    <tr><td>7</td><td>Collection room approval and compliance; no architect yet</td><td>Medium</td><td>Brief architect after site pick; confirm with partner and WA Department of Health</td></tr>
    <tr><td>8</td><td>Proposed 30% minimum tax on discretionary trusts from 1 July 2028 (exposure draft, not law)</td><td>Low-Med</td><td>Accountant review</td></tr>
    <tr><td>9</td><td>GST treatment unsettled. GST-stress downside +A$23,443 a month</td><td>Medium</td><td>Accountant; ATO private ruling; plan on the taxable basis</td></tr>
    <tr><td>10</td><td>Pregnancy complications on site (liability)</td><td>Medium</td><td>Health declaration, emergency plan, incident register, insurance</td></tr>
  </table>
  <div class="foot">GTT Center Perth | DRAFT 2026-10-16 | Risks 1 to 3 are one single point of failure: no site and no partner means no revenue</div>
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
    'Baseline confirmed: +A$35,186 a month at full capacity; GST-stress downside +A$23,443',
    'Request written wholesale per-test and collection fees from WDP, PathWest and Clinipath; ask who must employ the collectors for Medicare billing',
    'Approve agent enquiries for the three shortlisted sites (nothing has been sent)',
    'Verify a site first: 257 to 290 sqm, 2 collection rooms, rent within the A$10,500 gross ceiling',
    'Decide how to cover the funding gap (A$336k to A$361k vs about A$200k)',
    'Accountant: GST ruling application and the trading entity (recommendation: a new dedicated company)',
    'Appoint an architect once a site is chosen; use the concept floor plan for fit-out quotes',
    'Decide the Test Day Thank You discount and the phlebotomist minimum',
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
  <p class="small">We are not asking for money in this draft. Tenant entity: to be confirmed. Full list of open items: Items to Confirm in the business plan.</p>
  {FOOT}
</section>''')

# 23 CLOSING
S('''
<!-- 23 CLOSING (both) -->
<section class="slide cover center" data-name="Draft notice">
  <h1><span>DRAFT</span></h1>
  <p style="font-size:56px; max-width:1400px">DRAFT for Anthony's approval. Not for distribution until approved.</p>
  <div class="foot">GTT Center Perth | Pitch deck v0.5 | 2026-10-16</div>
</section>''')

html = head + '<body>\n<noscript><p style="color:#33261E;padding:20px">JavaScript is off. Slides will not step. Use Print to PDF to see every slide.</p></noscript>\n<div id="stage">\n\n' + '\n\n'.join(slides) + '\n\n</div>\n\n<div id="hud"><span id="count">1 / 1</span><span id="mode"></span><span>Arrows / space: move | E: toggle internal / external | Print to PDF: one slide per page</span></div>\n\n' + script
open(os.path.join(PRES, 'slides.html'), 'w', encoding='utf-8').write(html)
print('slides', len(slides))

# ---------- visual-financials.html ----------
vold = subprocess.check_output(['git', '-C', REPO, 'show', '43b8f2b:outputs/PRESENTATION/visual-financials.html']).decode('utf-8')
vhead = vold[:vold.index('<body>')]
vhead = vhead.replace('</style>', EXTRA_CSS.replace('.slide ', '.vfpage ').replace('.slide.vfs', '.vfpage.vfs') + '\n.vf.vfbig{font-size:20px}.vf-svg{max-width:100%}\n</style>')
vbody = f'''<body>
<header class="top"><div class="in"><div><h1>GTT Center Perth: the working</h1><div class="sub">Capacity, break-even and cashflow, shown step by step. Financial model v0.5 (2026-10-16). DRAFT.</div></div><div class="badge">INTERNAL: contains financials</div></div></header>
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

<footer>GTT Center Perth | Visual financials DRAFT 2026-10-16 | Prepared by Theodore (CFO consultant) with Grace | Source: financial model v0.5. Planning estimates, no trading data.</footer>
</div>
</body>
</html>
'''
open(os.path.join(PRES, 'visual-financials.html'), 'w', encoding='utf-8').write(vhead + vbody)
print('vf ok')
