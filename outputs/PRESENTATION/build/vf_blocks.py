#!/usr/bin/env python3
"""Draws the three working diagrams (capacity, break-even, cashflow) used on the
internal slides and in visual-financials.html. Figures come from the financial
model v0.5 documents (outputs/FINANCIALS/CASHFLOW-FORECAST.md is parsed for the
cash rows); nothing here is a new calculation.
"""
import re, os

HERE = os.path.dirname(os.path.abspath(__file__))
FIN = os.path.join(HERE, '..', '..', 'FINANCIALS')


def money(v, d=2):
    s = f"{abs(v):,.{d}f}"
    return ("-A$" if v < 0 else "A$") + s


def cash_rows():
    """Parse the Month 0 to 12 cash table in CASHFLOW-FORECAST.md."""
    txt = open(os.path.join(FIN, 'CASHFLOW-FORECAST.md'), encoding='utf-8').read()
    rows = {}
    for line in txt.splitlines():
        m = re.match(r'\|\s*M(\d+)\s*\|', line)
        if not m:
            continue
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        def num(c):
            c = c.split('◄')[0].replace('**', '').replace(',', '').strip()
            return float(c)
        rows[int(m.group(1))] = dict(
            funding=num(cells[2]), receipts=num(cells[3]), opex=num(cells[4]),
            capex=num(cells[5]), deferred=num(cells[6]), gst=num(cells[7]),
            net=num(cells[8]), close=num(cells[9]), cum_gst=num(cells[10]), cum_repo=num(cells[11]))
    assert len(rows) == 13, rows.keys()
    return rows


def capacity_block(slide=False):
    fs = 'font-size:26px' if slide else ''
    steps = [
        ('1', '07:00', 'first booking (expecting mothers arrive fasted at 06:50)'),
        ('2', '2', 'chairs, synchronised pairs'),
        ('3', '25 min', 'pair cadence'),
        ('4', '0 / 60 / 120', 'draw marks (minutes after the first draw)'),
        ('5', '10:30', 'latest first draw, 210 minutes after 07:00 (pathology partner guidance window)'),
    ]
    html = ['<div class="vf vfbig"><div class="vf-steps">']
    for n, big, lab in steps:
        html.append(f'<div class="vf-step"><div class="vf-sn">{n}</div><div class="vf-big">{big}</div><div class="vf-lab">{lab}</div></div>')
    html.append('</div>')
    html.append('<div class="vf-math"><div class="vf-eq"><span class="vf-k">slots</span> = floor(210 &divide; 25) + 1 = 8 + 1 = <b>9</b> pairs &nbsp;x 2 chairs = <b class="vf-hl">18</b> expecting mothers a morning</div>'
                '<span class="vf-src">Rule: (pairs - 1) x cadence must not pass 210 minutes. The last first draw is 10:20. Full-capacity time slots are booked 2 to 4 weeks ahead.</span></div>')
    # one-row timeline, large type
    x0, x1 = 90, 1000
    span = 210.0
    def X(t):
        return x0 + (x1 - x0) * t / span
    s = ['<svg class="vf-svg vf-cap" viewBox="0 0 1200 250" role="img" aria-label="Pair start times every 25 minutes between 07:00 and 10:20">']
    s.append(f'<rect x="{x0}" y="50" width="{X(210)-x0}" height="110" fill="#E8DAC5" opacity="0.45"/>')
    s.append(f'<line x1="{X(210)}" y1="40" x2="{X(210)}" y2="175" stroke="#A9654E" stroke-width="4" stroke-dasharray="10 6"/>')
    s.append(f'<text x="{X(210)}" y="30" text-anchor="middle" font-size="26" font-weight="700" fill="#A9654E">10:30 latest first draw</text>')
    s.append(f'<line x1="{x0}" y1="110" x2="{X(200)}" y2="110" stroke="#33261E" stroke-width="4"/>')
    for i in range(9):
        t = i * 25
        hh, mm = divmod(7 * 60 + t, 60)
        s.append(f'<circle cx="{X(t):.1f}" cy="110" r="24" fill="#33261E"/>')
        s.append(f'<text x="{X(t):.1f}" y="118" text-anchor="middle" font-size="24" font-weight="700" fill="#D9A08C">2</text>')
        s.append(f'<text x="{X(t):.1f}" y="82" text-anchor="middle" font-size="24" font-weight="700" fill="#33261E">{hh:02d}:{mm:02d}</text>')
    s.append(f'<text x="1180" y="120" text-anchor="end" font-size="72" font-family="Fraunces,Georgia,serif" fill="#33261E">18</text>')
    s.append(f'<text x="1180" y="152" text-anchor="end" font-size="24" font-weight="700" fill="#5E5F45">9 pairs x 2 chairs</text>')
    s.append(f'<text x="{(x0+X(210))/2}" y="205" text-anchor="middle" font-size="24" font-weight="700" fill="#33261E">210 minute window, one pair of clients every 25 minutes</text>')
    s.append('</svg></div>')
    html.append(''.join(s))
    return '\n'.join(html)


def breakeven_block():
    def row(op, val, lab, src=''):
        return (f'<div class="vf-row"><div class="vf-op">{op}</div><div><div class="vf-val">{val}</div>'
                f'<div class="vf-lab">{lab}</div>' + (f'<span class="vf-src">{src}</span>' if src else '') + '</div></div>')
    left = ('<div class="vf-col vf-b"><div class="vf-colhead">Adaptive rostering</div>'
            '<div class="vf-colsub">25 minute cadence, staff called in to match bookings</div>'
            + row('', 'A$36,738.11', 'fixed costs a month: rent, overhead, cost of goods, afternoon team and Venue Manager, with on-costs')
            + row('+', 'A$42,255.18', 'morning roster for up to 9 clients: 2 phlebotomists + 4 therapists, with on-costs')
            + row('=', 'A$78,993.29', 'total costs at that roster')
            + row('-', 'A$24,585.37', 'afternoon revenue')
            + row('&divide;', 'A$6,582.50', 'one morning client a day for a month: A$250 x 26.33 trading days')
            + '<div class="vf-res"><div class="vf-op">=</div><div><div class="vf-resn">8.266</div>'
              '<div class="vf-lab">morning clients a day, 45.9% of the 18 a day capacity</div></div></div></div>')
    right = ('<div class="vf-col vf-a"><div class="vf-colhead">If every booking stacks in pairs</div>'
             '<div class="vf-colsub">all bookings placed in pairs from 07:00 (the full 2 + 8 roster is needed)</div>'
             + row('', 'A$107,883.97', 'monthly costs with the full roster')
             + row('-', 'A$24,585.37', 'afternoon revenue')
             + row('&divide;', 'A$6,582.50', 'one morning client a day for a month')
             + '<div class="vf-res"><div class="vf-op">=</div><div><div class="vf-resn">12.655</div>'
               '<div class="vf-lab">morning clients a day, 70.3% of capacity</div></div></div></div>')
    note = ('<div class="vf-note">Margin of safety at the planning case: 9.7 clients a day below capacity. The two columns differ only in the cost line: '
            'with one booking per time slot at most two first services overlap, so 4 therapists cover up to 9 clients. '
            'Two phlebotomists are kept on every testing morning as GTT\'s clinical standard, pending the pathology partner\'s answer.</div>')
    return f'<div class="vf vfbig"><div class="vf-be">{left}{right}</div>{note}</div>'


def cashflow_svg(compact=False):
    R = cash_rows()
    W, H = 1200, 525
    left, right = 110, 1110
    top, bot = 70, 440
    vmax, vmin = 180000.0, -270000.0
    def Y(v):
        return top + (vmax - v) / (vmax - vmin) * (bot - top)
    n = 13
    step = (right - left) / n
    def CX(m):
        return left + step * (m + 0.5)
    s = [f'<svg class="vf-svg" viewBox="0 0 {W} {H}" role="img" aria-label="Cashflow Month 0 to 12" style="font-size:20px">']
    # peak funding line
    py = Y(-251198.0)
    s.append(f'<line x1="{left}" y1="{py:.1f}" x2="{right}" y2="{py:.1f}" stroke="#A9654E" stroke-width="2.5" stroke-dasharray="9 6"/>')
    s.append(f'<text x="{right}" y="{py+24:.1f}" text-anchor="end" font-size="22" font-weight="700" fill="#A9654E">Peak funding A$251,198 (Month 0)</text>')
    # zero line
    zy = Y(0)
    s.append(f'<line x1="{left}" y1="{zy:.1f}" x2="{right}" y2="{zy:.1f}" stroke="#33261E" stroke-width="2"/>')
    s.append(f'<text x="{left-8}" y="{zy+6:.1f}" text-anchor="end" font-size="20" font-weight="500" fill="#33261E">A$0</text>')
    for v in (100000, -100000, -200000):
        yy = Y(v)
        s.append(f'<line x1="{left}" y1="{yy:.1f}" x2="{right}" y2="{yy:.1f}" stroke="#E8DAC5" stroke-width="1.5"/>')
        s.append(f'<text x="{left-8}" y="{yy+6:.1f}" text-anchor="end" font-size="18" fill="#5E5F45">{"-" if v<0 else ""}A${abs(v)//1000}k</text>')
    bw = step * 0.5
    for m in range(13):
        r = R[m]
        cx = CX(m)
        if m == 0:
            h = Y(r['capex']) - zy
            s.append(f'<rect x="{cx-bw/2:.1f}" y="{zy:.1f}" width="{bw:.1f}" height="{h:.1f}" fill="#33261E"/>')
        else:
            h = zy - Y(r['net'] if r['net'] > 0 else 0)
            s.append(f'<rect x="{cx-bw/2:.1f}" y="{zy-(zy-Y(35186.40)):.1f}" width="{bw:.1f}" height="{zy-Y(35186.40):.1f}" fill="#5E5F45"/>')
            if r['deferred']:
                dh = Y(r['deferred']) - zy
                s.append(f'<rect x="{cx-bw/2:.1f}" y="{zy:.1f}" width="{bw:.1f}" height="{max(dh,6):.1f}" fill="#33261E"/>')
        s.append(f'<text x="{cx:.1f}" y="{bot+30}" text-anchor="middle" font-size="22" font-weight="500" fill="#33261E">M{m}</text>')
    # lines
    def poly(key):
        return ' '.join(f'{CX(m):.1f},{Y(R[m][key]):.1f}' for m in range(13))
    s.append(f'<polyline points="{poly("cum_repo")}" fill="none" stroke="#9C7A46" stroke-width="4" stroke-dasharray="2 7" stroke-linecap="round"/>')
    s.append(f'<polyline points="{poly("cum_gst")}" fill="none" stroke="#A9654E" stroke-width="4"/>')
    for m in range(13):
        s.append(f'<circle cx="{CX(m):.1f}" cy="{Y(R[m]["cum_repo"]):.1f}" r="6" fill="#9C7A46" stroke="#FAF6EE" stroke-width="2"/>')
        s.append(f'<circle cx="{CX(m):.1f}" cy="{Y(R[m]["cum_gst"]):.1f}" r="6" fill="#A9654E" stroke="#FAF6EE" stroke-width="2"/>')
    # payback markers
    x8, x11 = CX(8), CX(11)
    s.append(f'<line x1="{x8:.1f}" y1="{top}" x2="{x8:.1f}" y2="{bot}" stroke="#9C7A46" stroke-width="2" stroke-dasharray="4 4"/>')
    s.append(f'<text x="{x8-8:.1f}" y="{top-14}" text-anchor="end" font-size="22" font-weight="700" fill="#9C7A46">Payback Month 8 (before GST timing)</text>')
    s.append(f'<line x1="{x11:.1f}" y1="{top+30}" x2="{x11:.1f}" y2="{bot}" stroke="#A9654E" stroke-width="2" stroke-dasharray="4 4"/>')
    s.append(f'<text x="{x11-8:.1f}" y="{top+14}" text-anchor="end" font-size="22" font-weight="700" fill="#A9654E">Payback Month 11 (after GST)</text>')
    # point labels
    s.append(f'<text x="{CX(12)+14:.1f}" y="{Y(R[12]["cum_repo"])+6:.1f}" text-anchor="start" font-size="20" font-weight="700" fill="#9C7A46">+157,665</text>')
    s.append(f'<text x="{CX(12)+14:.1f}" y="{Y(R[12]["cum_gst"])+6:.1f}" text-anchor="start" font-size="20" font-weight="700" fill="#A9654E">+28,483</text>')
    # legend
    ly = 505
    s.append(f'<rect x="{left}" y="{ly-14}" width="18" height="18" fill="#33261E"/><text x="{left+26}" y="{ly}" font-size="20" fill="#33261E">capex (setup costs)</text>')
    s.append(f'<rect x="{left+250}" y="{ly-14}" width="18" height="18" fill="#5E5F45"/><text x="{left+276}" y="{ly}" font-size="20" fill="#33261E">monthly net profit A$35,186</text>')
    s.append(f'<circle cx="{left+560}" cy="{ly-5}" r="7" fill="#9C7A46"/><text x="{left+576}" y="{ly}" font-size="20" fill="#33261E">cumulative, before GST timing</text>')
    s.append(f'<circle cx="{left+700}" cy="{ly-5}" r="7" fill="#A9654E"/><text x="{left+716}" y="{ly}" font-size="20" fill="#33261E">after GST</text>')
    s.append('</svg>')
    return ''.join(s)


def cashflow_block():
    return ('<div class="vf" style="max-width:1480px">' + cashflow_svg() +
            '<div class="vf-note" style="font-size:22px">Funding in at Month 0: A$336,198. Pre-opening capital spent: A$251,198. The A$85,000 reserve is never drawn: Month 1 already makes a profit. '
            'Headline case: A$8,000 rent, full capacity from Month 1, no ramp-up.</div></div>')


if __name__ == '__main__':
    print(len(capacity_block()), len(breakeven_block()), len(cashflow_block()))
