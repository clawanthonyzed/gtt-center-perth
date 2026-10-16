#!/usr/bin/env python3
"""Builds BUSINESS-PLAN.pdf, PROFIT-AND-LOSS.pdf and CASHFLOW-FORECAST.pdf with headless Chromium
(the same engine that produced the original PDFs: Chromium / Skia PDF).
Usage: build_pdfs.py [plan|pl|cf|all]
The plan has a two-pass table of contents so each entry carries a clickable link and its real page number.
"""
import os, re, subprocess, sys, html as H
import markdown
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
PRES = os.path.abspath(os.path.join(HERE, '..'))
FIN = os.path.abspath(os.path.join(PRES, '..', 'FINANCIALS'))
OUT = os.path.join(HERE, 'out')
os.makedirs(OUT, exist_ok=True)

CSS = """
@page { size: A4; margin: 16mm 16mm 18mm 16mm; }
* { box-sizing: border-box; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { font-family: 'Carlito','Calibri','Liberation Sans',Arial,sans-serif; font-size: 10pt; line-height: 1.38; color: #33261E; margin: 0; }
h1 { font-family: 'Gentium Basic','Liberation Serif',Georgia,serif; font-size: 30pt; margin: 0 0 4pt 0; color: #33261E; border-bottom: 2px solid #9C7A46; padding-bottom: 6pt; }
h2 { font-family: 'Gentium Basic','Liberation Serif',Georgia,serif; font-size: 17pt; color: #A9654E; margin: 0 0 8pt 0; padding-bottom: 3pt; border-bottom: 1px solid #E8DAC5; break-after: avoid; }
h1 + h2 { font-size: 15pt; border: none; }
h3 { font-family: 'Gentium Basic','Liberation Serif',Georgia,serif; font-size: 12.5pt; color: #5E5F45; margin: 12pt 0 4pt 0; break-after: avoid; }
p { margin: 0 0 6pt 0; }
ul, ol { margin: 0 0 6pt 0; padding-left: 18pt; }
li { margin-bottom: 2pt; }
a { color: #A9654E; text-decoration: underline; }
table { width: 100%; border-collapse: collapse; margin: 4pt 0 8pt 0; font-size: 8.8pt; line-height: 1.28; }
th { background: #33261E; color: #FAF6EE; text-align: left; padding: 3.5pt 6pt; font-weight: 700; }
td { padding: 3pt 6pt; border-bottom: 1px solid #E8DAC5; vertical-align: top; }
tr:nth-child(even) td { background: #F6EEE0; }
tr { break-inside: avoid; }
thead { display: table-header-group; }
.tblock { break-inside: avoid; page-break-inside: avoid; }
.tblock table { margin-top: 2pt; }
.tblock.fit table { font-size: 8.4pt; line-height: 1.22; }
.tblock.fit td { padding: 2.4pt 5pt; }
.tcap { font-weight: 700; color: #A9654E; margin: 8pt 0 2pt 0; font-size: 10.5pt; break-after: avoid; }
.pagebreak { break-after: page; page-break-after: always; height: 0; }
img { max-width: 100%; height: auto; display: block; margin: 6pt auto; border: 1px solid #E8DAC5; }
em { color: #5E5F45; }
strong { color: #33261E; }
/* cover table */
h1 + h2 + p + table td:first-child, h1 + h2 + p + table th:first-child { width: 24%; }
/* table of contents */
.toc h2 { font-size: 24pt; margin-bottom: 16pt; border-bottom: 2px solid #9C7A46; }
.toc .lead { font-size: 11.5pt; color: #5E5F45; margin-bottom: 18pt; }
.toc a.row { display: flex; align-items: baseline; text-decoration: none; color: #33261E; font-size: 15.5pt; padding: 6pt 0; border-bottom: 1px solid #E8DAC5; }
.toc a.row .n { width: 30pt; color: #A9654E; font-family: 'Gentium Basic','Liberation Serif',serif; font-weight: 700; }
.toc a.row .t { flex: 1; }
.toc a.row .pg { width: 34pt; text-align: right; color: #A9654E; font-weight: 700; }
.toc a.row.sub { font-size: 12.5pt; padding: 4pt 0 4pt 30pt; color: #5E5F45; }
.toc a.row.sub .n { width: 22pt; }
/* financial statements */
.fin table { font-size: 7.6pt; }
.fin.wide table.wide { font-size: 6.4pt; }
.fin.wide table.wide th, .fin.wide table.wide td { padding: 2pt 2.5pt; }
"""

COMMON_SUBS = [
    # plain business wording for the financial statements (sources and internal wording removed)
    (r' Source: model[^\n|]*', ''),
]


def md_to_html(md_text):
    md = markdown.Markdown(extensions=['tables', 'sane_lists'])
    return md.convert(md_text)


def wrap_tables(body, fit_ids=()):
    """Wrap each table with the caption paragraph before it so it never splits across pages."""
    # caption paragraphs: <p><strong>Table x.y: ...</strong></p> directly before <table>
    def cap_repl(m):
        cap, tbl = m.group(1), m.group(2)
        num = re.search(r'Table (\d+\.\d+)', cap)
        fit = ' fit' if num and num.group(1) in fit_ids else ''
        cap_clean = re.sub(r'^<p>(.*)</p>$', r'<div class="tcap">\1</div>', cap.strip(), flags=re.S)
        return f'<div class="tblock{fit}">{cap_clean}{tbl}</div>'
    body = re.sub(r'(<p><strong>Table \d+\.\d+[^<]*</strong></p>)\s*(<table>.*?</table>)', cap_repl, body, flags=re.S)
    # remaining uncaptioned tables of moderate size also kept together
    def plain(m):
        t = m.group(0)
        rows = t.count('<tr>')
        return f'<div class="tblock">{t}</div>' if rows <= 14 else t
    parts = re.split(r'(<div class="tblock.*?</div>)', body, flags=re.S)
    out = []
    for p in parts:
        if p.startswith('<div class="tblock'):
            out.append(p)
        else:
            out.append(re.sub(r'<table>.*?</table>', plain, p, flags=re.S))
    return ''.join(out)


def headings(body):
    items = []
    for m in re.finditer(r'<h([23])[^>]*>(.*?)</h\1>', body):
        lvl, txt = int(m.group(1)), re.sub(r'<.*?>', '', m.group(2))
        items.append((lvl, txt))
    return items


def slug(t):
    return 'sec-' + re.sub(r'[^a-z0-9]+', '-', t.lower()).strip('-')


def add_ids(body):
    def r(m):
        return f'<h{m.group(1)} id="{slug(re.sub("<.*?>", "", m.group(2)))}">{m.group(2)}</h{m.group(1)}>'
    return re.sub(r'<h([23])>(.*?)</h\1>', r, body)


def render_pdf(html_text, out_pdf, footer_label, base_dir):
    path = os.path.join(OUT, os.path.basename(out_pdf) + '.html')
    open(path, 'w', encoding='utf-8').write(html_text)
    # keep relative image paths working: place the html next to the images via base tag
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page()
        pg.goto('file://' + path)
        pg.wait_for_timeout(500)
        footer = ('<div style="font-size:8px;width:100%;padding:0 16mm;color:#5E5F45;display:flex;justify-content:space-between;font-family:Arial,sans-serif">'
                  f'<span>{footer_label}</span><span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span></div>')
        pg.pdf(path=out_pdf, format='A4', print_background=True, display_header_footer=True,
               header_template='<div></div>', footer_template=footer,
               margin={'top': '16mm', 'bottom': '18mm', 'left': '16mm', 'right': '16mm'}, prefer_css_page_size=False)
        b.close()


def pdf_pages(pdf):
    n = int(re.search(r'Pages:\s+(\d+)', subprocess.check_output(['pdfinfo', pdf]).decode()).group(1))
    texts = []
    for i in range(1, n + 1):
        texts.append(subprocess.check_output(['pdftotext', '-f', str(i), '-l', str(i), '-layout', pdf, '-']).decode('utf-8', 'ignore'))
    return texts


def build_plan():
    md_text = open(os.path.join(PRES, 'BUSINESS-PLAN.md'), encoding='utf-8').read()
    body = md_to_html(md_text)
    body = wrap_tables(body, fit_ids=('5.3', '5.5', '6.3', '8.3', '9.3'))
    body = add_ids(body)
    hs = headings(body)
    toc_items = []
    for lvl, t in hs:
        if t.startswith('Business Plan') or t == 'Table of Contents':
            continue
        if lvl == 2 or t.startswith('Appendix '):
            toc_items.append((lvl, t))

    def toc_html(pages):
        rows = []
        for lvl, t in toc_items:
            m = re.match(r'(\d+)\.\s+(.*)', t)
            num, title = (m.group(1), m.group(2)) if m else ('', t)
            if lvl == 3:
                mm = re.match(r'(Appendix [A-D])\.\s+(.*)', t)
                num, title = mm.group(1)[-1], mm.group(2)
            cls = 'row sub' if lvl == 3 else 'row'
            pg = pages.get(t, '')
            rows.append(f'<a class="{cls}" href="#{slug(t)}"><span class="n">{num}</span><span class="t">{H.escape(title)}</span><span class="pg">{pg}</span></a>')
        return ('<div class="toc"><h2>Table of Contents</h2><p class="lead">Select any entry to jump to that section.</p>' + ''.join(rows) + '</div>')

    def full(pages):
        b = body.replace('<div id="toc-placeholder"></div>', toc_html(pages))
        return f'<!DOCTYPE html><html lang="en-AU"><head><meta charset="utf-8"><title>GTT Center Perth Business Plan</title><base href="file://{PRES}/"><style>{CSS}</style></head><body>{b}</body></html>'

    pdf = os.path.join(OUT, 'BUSINESS-PLAN.pdf')
    footer = 'GTT Center Perth | Business Plan v0.5 | DRAFT 2026-10-16'
    render_pdf(full({}), pdf, footer, PRES)
    texts = pdf_pages(pdf)
    pages = {}
    for lvl, t in toc_items:
        key = t
        for i, tx in enumerate(texts):
            if i < 2:
                continue
            lines = [re.sub(r'\s+', ' ', l).strip() for l in tx.splitlines()]
            if key in lines:
                pages[t] = i + 1
                break
    print('pages', pages)
    render_pdf(full(pages), pdf, footer, PRES)
    return pdf


def fin_md(name):
    t = open(os.path.join(FIN, name), encoding='utf-8').read()
    return t


def clean_fin(t):
    """Presentation-only wording changes for the PDF copy of a financial statement."""
    subs = [
        (r'\(repo basis\)', '(before GST timing)'), (r'repo basis', 'before GST timing'), (r'Repo basis', 'Before GST timing'),
        (r'Cumulative \(repo basis\)', 'Cumulative (before GST timing)'),
        (r'\bthe repo\'s own\b', 'the model\'s own'), (r'\brepo\b', 'model'),
        (r'Model §[\w\d, §.]*', 'Financial model'), (r'model §[\w\d, §.]*', 'financial model'),
        (r'\(model §[^)]*\)', ''), (r'; CURRENT-STATE §\d+', ''),
        (r'CURRENT-STATE[^|;)]*', 'the plan'), (r'profit-loss-tables\.md v3\.0', 'the financial model'),
        (r'\bTO CONFIRM\b', 'to be confirmed'), (r'\bNot in model\b', 'Not in the model'), (r'\bnot in model\b', 'not in the model'),
        (r'\.md\b', ''),
    ]
    for a, b in subs:
        t = re.sub(a, b, t)
    return t


def build_fin(name, title, out_name, wide=False):
    t = clean_fin(fin_md(name))
    body = md_to_html(t)
    cls = 'fin wide' if wide else 'fin'
    if wide:
        body = body.replace('<table>', '<table class="wide">', 1) if False else body
    html_text = f'<!DOCTYPE html><html lang="en-AU"><head><meta charset="utf-8"><title>{title}</title><style>{CSS}\n@page {{ size: A4 landscape; margin: 12mm; }}</style></head><body class="{cls}">{body}</body></html>'
    pdf = os.path.join(OUT, out_name)
    path = pdf + '.html'
    open(path, 'w', encoding='utf-8').write(html_text)
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page()
        pg.goto('file://' + path)
        pg.wait_for_timeout(400)
        footer = ('<div style="font-size:8px;width:100%;padding:0 12mm;color:#5E5F45;display:flex;justify-content:space-between;font-family:Arial,sans-serif">'
                  f'<span>GTT Center Perth | {title} | DRAFT 2026-10-16</span><span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span></div>')
        pg.pdf(path=pdf, format='A4', landscape=True, print_background=True, display_header_footer=True,
               header_template='<div></div>', footer_template=footer, margin={'top': '12mm', 'bottom': '14mm', 'left': '12mm', 'right': '12mm'})
        b.close()
    return pdf


if __name__ == '__main__':
    what = sys.argv[1] if len(sys.argv) > 1 else 'all'
    if what in ('plan', 'all'):
        print(build_plan())
    if what in ('pl', 'all'):
        print(build_fin('PROFIT-AND-LOSS.md', 'Projected Profit and Loss', 'PROFIT-AND-LOSS.pdf', True))
    if what in ('cf', 'all'):
        print(build_fin('CASHFLOW-FORECAST.md', 'Cashflow Forecast', 'CASHFLOW-FORECAST.pdf', True))
