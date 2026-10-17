#!/usr/bin/env python3
"""Writes EXECUTIVE-PITCH-DECK.md as a plain-text version of slides.html (same wording, same numbers),
so the two documents cannot drift apart. Run after build_slides.py."""
import os, re
from bs4 import BeautifulSoup

HERE = os.path.dirname(os.path.abspath(__file__))
PRES = os.path.abspath(os.path.join(HERE, '..'))
soup = BeautifulSoup(open(os.path.join(PRES, 'slides.html'), encoding='utf-8').read(), 'html.parser')

def clean(s):
    return re.sub(r'\s+', ' ', s).strip()

def table_md(tb):
    rows = []
    for tr in tb.find_all('tr'):
        cells = [clean(c.get_text(' ')) for c in tr.find_all(['th', 'td'])]
        if cells:
            rows.append(cells)
    if not rows:
        return ''
    n = max(len(r) for r in rows)
    rows = [r + [''] * (n - len(r)) for r in rows]
    out = ['| ' + ' | '.join(rows[0]) + ' |', '|' + '---|' * n]
    out += ['| ' + ' | '.join(r) + ' |' for r in rows[1:]]
    return '\n'.join(out)

lines = []
lines.append('# GTT Center Perth: Executive Pitch Deck (DRAFT v0.6, 2026-10-17)')
lines.append('')
lines.append('**Status:** DRAFT for Anthony\'s approval. Nothing here has been sent or published.')
lines.append('**Prepared by:** Grace (Operations Manager). All figures in Australian dollars (A$). Planning estimates: the business has not opened and has no trading data.')
lines.append('This text is the same as the slide deck (slides.html, 30 slides). Slides marked INTERNAL contain financials and are not for external use.')
lines.append('')
for i, sl in enumerate(soup.select('.slide'), 1):
    name = sl.get('data-name', '')
    internal = 'int' in sl.get('class', [])
    lines.append('---')
    lines.append('')
    lines.append(f'## SLIDE {i}: {name} ({"INTERNAL" if internal else "external"})')
    lines.append('')
    for el in sl.find_all(['h1', 'h2', 'p', 'li', 'table', 'div'], recursive=True):
        if el.name == 'div':
            cls = el.get('class', [])
            if 'card' in cls:
                lab = el.select_one('.lab'); big = el.select_one('.big'); txt = el.select_one('.txt')
                parts = [clean(x.get_text(' ')) for x in (lab, big, txt) if x]
                if parts:
                    lines.append('- ' + ': '.join(parts))
            elif 'stamp' in cls or 'foot' in cls:
                pass
            continue
        if el.name == 'table':
            lines.append(table_md(el)); lines.append(''); continue
        if el.find_parent('table') or el.find_parent(class_='card'):
            continue
        txt = clean(el.get_text(' '))
        if not txt or txt == 'INTERNAL':
            continue
        if el.name == 'h1':
            lines.append('**' + txt + '**'); lines.append('')
        elif el.name == 'h2':
            lines.append('**' + txt + '**'); lines.append('')
        elif el.name == 'li':
            lines.append('- ' + txt)
        else:
            lines.append(txt); lines.append('')
    lines.append('')
open(os.path.join(PRES, 'EXECUTIVE-PITCH-DECK.md'), 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
print('exec deck md written')
