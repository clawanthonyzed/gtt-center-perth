#!/usr/bin/env python3
"""Builds outputs/PRESENTATION/floor-plan-v2.html (self-contained) from the v2 SVG, the v1 SVG (archive) and the circulation check output.
Run from the repo root after make_concept_floor_plan.py."""
import html, json, re, sys, pathlib

root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")
svg2 = (root / "outputs/DESIGN/CONCEPT-FLOOR-PLAN.svg").read_text(encoding="utf-8")
svg1 = (root / "outputs/DESIGN/CONCEPT-FLOOR-PLAN-v1.svg").read_text(encoding="utf-8")
chk = json.loads((root / "outputs/DESIGN/CIRCULATION-CHECK-v2.json").read_text(encoding="utf-8"))
A = chk["areas"]

def strip_dims(s):
    return re.sub(r'<svg ([^>]*?)width="\d+" height="\d+"', r'<svg \1', s, count=1)

svg2i = strip_dims(svg2); svg1i = strip_dims(svg1)

esc = html.escape
checks_html = "\n".join(esc(m) for m in chk["checks"])

changes = [
    ("1. Poorly placed walls blocked access to rooms",
     "Every room now has a clear door or open front onto the clinical corridor, the back-of-house corridor, the arrival lobby or the lounge. No room is reached only through another room. The two collection rooms each have a door to the clinical corridor and a second door to the back-of-house corridor. The four massage and beauty bays open to the lounge or lobby through a curtain, never through each other. The storage room is reached through the staff room on purpose (staff only).",
     "Whole plan. Clinical corridor (1.5 m) runs full width between the rear rooms and the lounge; doors are drawn with swings; circulation check below proves it."),
    ("2. Hair and nail zones far too big",
     f"Hair cut from 45.0 to {A['hair']:.1f} sqm (4 chairs, 2 backwash, about 6 sqm per chair including aisles and back bar). Nails cut from 30.0 to {A['nails']:.1f} sqm (4 stations with pedicure chairs, about 5.6 sqm per station). Together 75.0 sqm became {A['hair']+A['nails']:.1f} sqm, freeing {75.0-A['hair']-A['nails']:.1f} sqm. The open luxury lounge grew from 34.5 to {A['lounge']:.1f} sqm. The rest went to reception (11.8 to {A['recep']:.1f}), the massage and beauty bays (10.2 to {A['m1']:.1f} each), the staff room, the equal collection rooms and a separate service entry.",
     "East side of the plan: hairdressing along the north end, nails at the south end; the lounge now fills the centre."),
    ("3. No separate fridge room wanted",
     "The 4.8 sqm specimen fridge and centrifuge bay is gone. Each collection room has its own under-counter clinical specimen fridge (red box on the bench). Clinical waste and dirty linen stay in their own small room at the service end, 9.6 m from the refreshment counter with no shared wall (decision of 2026-09-04 kept).",
     "Inside each collection room, north bench (red fridge box). Dirty linen and clinical waste room, top-left corner."),
    ("4. Collection rooms differed (17.6 and 19.4 sqm)",
     "Both rooms are 19.0 sqm (4.75 m x 4.0 m), the middle of the 18 to 20 sqm range in the venue documents. Same layout in both: chair, stool, recovery recliner, handwash basin, bench with fridge, centrifuge position and documentation bench, sharps. Option B uses the same logic: 2 x 19.0 = 38.0 sqm.",
     "Top row, two rooms side by side. Option B inset, bottom right."),
    ("5. Staff walked through the service and linen zone to reach the staff room",
     "The dirty zone (service door, dirty linen and clinical waste) is a separate room group at the far west end of the back-of-house corridor, shaded red. The staff room has its own entry door from outside (north wall), a door to the back-of-house corridor and a door to the clinical corridor. Staff never need to enter the dirty zone. The clinical waste route runs from the collection rooms along the staff-only corridor to the service door and does not cross any client area.",
     "Top row, east of the collection rooms. Green route = staff, red route = waste."),
    ("6. Staff toilet redundant",
     "Staff WC removed (4.0 sqm reclaimed). The accessible WC and one standard WC are shared by clients and staff. Sanitary provision needs architect confirmation (see open questions).",
     "Top right, two WCs off the clinical corridor."),
]
changes_html = "\n".join(f"<tr><td><strong>{esc(a)}</strong></td><td>{esc(b)}</td><td>{esc(c)}</td></tr>" for a, b, c in changes)

before_after = [
    ("Blood Collection Room 1", "17.6", f"{A['cr1']:.1f}"), ("Blood Collection Room 2", "19.4", f"{A['cr2']:.1f}"),
    ("Specimen fridge and centrifuge bay (separate)", "4.8", "removed (fridge in each room)"),
    ("Clinical waste and dirty linen", "4.8", f"{A['dirty']:.1f}"),
    ("Massage and beauty bays (each)", "10.2", f"{A['m1']:.1f}"), ("Open-plan lounge", "34.5", f"{A['lounge']:.1f}"),
    ("Reception", "11.8", f"{A['recep']:.1f}"), ("Hairdressing", "45.0", f"{A['hair']:.1f}"), ("Nails and pedicure", "30.0", f"{A['nails']:.1f}"),
    ("Staff room (with lockers)", "9.8", f"{A['staff']:.1f}"), ("Staff WC", "4.0", "removed"),
    ("Accessible WC / standard WC", "7.0 / 4.1", f"{A['accwc']:.1f} / {A['stdwc']:.1f}"),
    ("Total gross internal", "288.6", f"{chk['total']:.1f}"),
]
ba_html = "\n".join(f"<tr><td>{esc(a)}</td><td class='n'>{esc(b)}</td><td class='n'>{esc(c)}</td></tr>" for a, b, c in before_after)

refs = [
    ("AusHFG Health Planning Unit 0550 Pathology Unit, Revision 7.0 (May 2022)", "https://healthfacilityguidelines.com.au/sites/default/files/HPU_B.0550_7.pdf",
     "Collection bay 9 m2 and optional enclosed collection room 12 m2 with basin (may need dual egress); patient toilet 4 m2 (6 m2 if accessible); staff amenities in a staff-only zone reached by corridor; glucose tolerance patients wait about two hours and need staff oversight.",
     "Room size comparison, two doors per collection room, staff route, lounge beside the corridor."),
    ("AusHFG Health Planning Unit 0270 Day Surgery / Procedure Unit, Revision 7.0 (March 2022)", "https://healthfacilityguidelines.com.au/sites/default/files/HPU_B.0270_7.pdf",
     "Separation of clean and dirty flows; logical orderly patient flow from reception; staff able to monitor patients at all times.",
     "Separate dirty route and one-direction client flow."),
    ("Pathology collection centre fit-out, Warrnambool VIC, 80 m2 (MedicalSearch listing)", "https://www.medicalsearch.com.au/pathology-collection-centre-interior-fitout/p/284031",
     "A real collection centre: waiting and reception, 2 collection rooms, staff room, disabled toilet, store room (no plan or dimensions published).",
     "Confirms the room set."),
    ("Standard Salon Size and Dimensions (Salon Business)", "https://thesalonbusiness.com/?p=787",
     "Styling 35 sq ft, shampoo 36 sq ft, manicure 16 sq ft, pedicure 32 sq ft; at least 40 inches between chairs.",
     "Hair and nail station sizes."),
    ("Styling station space guide (Kaemark)", "https://kaemark.com/blogs/news/styling-station-ideal-space",
     "Minimum styling station about 3.25 sqm (5 ft by 7 ft).", "Chair spacing along the mirror wall."),
    ("Beauty salon floor plan guide (Pabau, overseas)", "https://pabau.com/templates/beauty-salon-floor-plan/",
     "Wet units placed first to follow drainage; one-direction client flow that never crosses stockrooms or laundry; enclosed rooms where clients undress.",
     "Shared wet wall (backwash and refreshment counter); client route clear of the service zone."),
    ("Relinque Urban Spa, Studio Tate, 800 m2 (Dezeen)", "https://www.dezeen.com/?p=1868883",
     "Central reception with treatment rooms either side; privacy increases deeper into the plan.",
     "Public front, private rear (sequence only; larger scale)."),
    ("Beauty salon layout guide (salon.life)", "https://www.salon.life/en/post/beauty-salon-layout",
     "Minimum passage for wheelchairs and trolleys; staff room accessible but discreet; group hair wash with cutting.",
     "Staff room off the corridor; backwash behind chairs."),
    ("NCC 2022 Volume One, Part F4 Sanitary and other facilities (ABCB)", "https://ncc.abcb.gov.au/editions/ncc-2022/adopted/volume-one/f-health-and-amenity/part-f4-sanitary-and-other-facilities",
     "Sanitary provisions F4D4 and F4D5, including employees and the public sharing facilities in a Class 6 building if the combined requirement is met.",
     "Staff WC removed; marked TO CONFIRM."),
]
refs_html = "\n".join(f"<tr><td><a href='{u}'>{esc(t)}</a></td><td>{esc(w)}</td><td>{esc(ap)}</td></tr>" for t, u, w, ap in refs)

questions = [
    "Collection room size: the plan uses 19.0 sqm each (middle of the 18 to 20 sqm range). Please confirm with the pathology partner. The venue documents note the recovery recliner allowance of about 2 to 3 sqm may sit on top of 18 sqm, which would mean 20 to 21 sqm. The pathology partner room specifications (WDP, PathWest) have not been seen in full. TO CONFIRM.",
    "Sanitary facilities: the plan has one accessible unisex WC and one standard WC, shared by clients and staff (about 10 treatment and collection staff plus a venue manager, and clients and companions). The National Construction Code Part F4 (Table F4D4a and the sharing rule in F4D4) decides the count and whether separate male and female facilities or unisex facilities are acceptable. The building class (5, 6 or 9b) must be set by the building surveyor. TO CONFIRM.",
    "Dual egress: the public hospital guideline notes enclosed collection rooms may need two exits depending on jurisdictional policy. Each room has two doors (client side and back-of-house). Confirm whether the pathology partner or WA Health requires this.",
    "Second centrifuge, second recovery recliner and second specimen fridge: the plan shows one fridge and one recliner in each room (two of each) and space for a centrifuge in each room. The procurement register carried one of each, so the second units are quantity changes to be priced. TO CONFIRM.",
    "Massage and beauty bays are drawn 2.2 m wide by 4.8 m (10.7 sqm), below the 12 and 11 sqm in the room schedule. Confirm this is acceptable or trade lounge area for bay size.",
    "Nails sit beside reception on the east wall with a local exhaust duct to the outside wall; the open-plan fume control method needs the ventilation engineer and WorkSafe.",
    "Accessible WC: door swing, clear floor space and grab rails to be set to AS 1428.1 by the architect. Doors drawn at 1.0 m.",
    "Fire exits, travel distances and the use of the service and staff doors as exits need the building surveyor.",
    "Reception is drawn open-plan; the venue documents describe it with solid walls. Confirm.",
    "The plan is a typical 18.5 m x 15.6 m rectangle. A real site will change room positions; the principles (separate dirty route, equal collection rooms, staff route not through the dirty zone) should carry over.",
]
q_html = "\n".join(f"<li>{esc(q)}</li>" for q in questions)

page = """<!doctype html>
<html lang="en-AU"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>GTT Center Perth: Concept Floor Plan v2</title>
<style>
 body{margin:0;background:#FBF8F3;color:#3A322B;font-family:Helvetica,Arial,'Noto Sans',sans-serif;line-height:1.5}
 .wrap{max-width:1280px;margin:0 auto;padding:28px 24px 60px}
 h1{font-size:30px;margin:4px 0 6px} h2{font-size:15px;letter-spacing:2px;color:#B58B2A;text-transform:uppercase;margin:40px 0 10px;border-top:2px solid #E6D7B5;padding-top:14px}
 .eyebrow{color:#B58B2A;letter-spacing:3px;font-weight:700;font-size:13px}
 .stamp{display:inline-block;border:2px solid #B5483A;color:#B5483A;border-radius:6px;padding:6px 14px;font-weight:700;margin:8px 0}
 .plan{background:#FBF8F3;border:1px solid #E6D7B5;margin:12px 0} .plan svg{width:100%;height:auto;display:block}
 table{border-collapse:collapse;width:100%;font-size:14px;margin:8px 0} th{background:#3A322B;color:#fff;text-align:left;padding:7px 9px}
 td{padding:7px 9px;border-bottom:1px solid #E8E0D3;vertical-align:top} tr:nth-child(even) td{background:#F6F0E6} td.n{text-align:right;white-space:nowrap}
 pre{background:#fff;border:1px solid #E6D7B5;padding:12px;font-size:12.5px;overflow-x:auto;white-space:pre-wrap}
 .two{display:grid;grid-template-columns:1fr 1fr;gap:18px} .two .plan{margin:0} .cap{font-size:13px;color:#8A7F73;margin-top:4px}
 a{color:#2F6A92} li{margin:6px 0} .note{font-size:13px;color:#6f6458}
 @media(max-width:800px){.two{grid-template-columns:1fr}}
 @media print{.wrap{padding:0} h2{break-after:avoid} table{break-inside:auto}}
</style></head><body><div class="wrap">
<div class="eyebrow">GTT CENTER PERTH</div>
<h1>Concept Floor Plan and Layout Schematic, version 2</h1>
<div class="stamp">CONCEPT ONLY. NOT FOR CONSTRUCTION. Subject to site survey, architect and NCC compliance.</div>
<p>Typical rectangle 18.5 m x 15.6 m, 288.6 sqm gross internal, inside the 257 to 290 sqm site range. Version 2 corrects the access, size, fridge, staff flow and toilet faults found in version 1 (dated 2026-10-16). Drawing date 2026-10-17.</p>

<h2>The plan</h2>
<div class="plan">__SVG2__</div>

<h2>What changed: one row per fault</h2>
<table><tr><th style="width:22%">Fault in version 1</th><th>Fix in version 2</th><th style="width:24%">Where on the plan</th></tr>
__CHANGES__</table>

<h2>Before and after</h2>
<div class="two"><div><div class="plan">__SVG1__</div><div class="cap">Version 1 (archived, 2026-10-16)</div></div>
<div><div class="plan">__SVG2B__</div><div class="cap">Version 2 (this page)</div></div></div>
<table style="max-width:760px"><tr><th>Zone (sqm)</th><th>Version 1</th><th>Version 2</th></tr>__BA__</table>

<h2>Circulation notes</h2>
<ul>
<li><strong>Client route:</strong> main entry, arrival lobby, reception and lounge, then the clinical corridor to a collection room door. Toilets, massage, beauty, hair and nails all open from the lounge or the clinical corridor.</li>
<li><strong>Staff route:</strong> staff entry (north wall) straight into the back-of-house corridor and staff room; the staff room also opens to the clinical corridor, so staff can reach clients without using the back-of-house corridor.</li>
<li><strong>Dirty route:</strong> collection room back doors, along the staff-only corridor, into the dirty zone and out through the service door. It never crosses the lounge, reception or the clinical corridor.</li>
<li><strong>Refreshments and specimens:</strong> the Private Refreshment Counter (glucose drink service) is 3.6 m from the nearest collection room wall and 9.6 m from the clinical waste room, with no shared wall. Each collection room has its own under-counter specimen fridge.</li>
<li><strong>Supervision:</strong> the lounge sits beside the clinical corridor so staff can see clients waiting after the glucose drink (the public hospital guideline stresses staff oversight of glucose tolerance waiting areas).</li>
<li><strong>Shared amenities:</strong> one accessible WC and one standard WC serve clients and staff. Number and type are subject to NCC Part F4 and the building surveyor (TO CONFIRM).</li>
</ul>

<h2>Circulation check (run in code from the plan data)</h2>
<pre>__CHECK__</pre>
<p class="note">The check builds a graph of rooms, doors and open boundaries from the same data that draws the plan. It also confirms that each door sits on a wall shared by the two rooms it joins, that rooms do not overlap and that the room areas add up to the 288.6 sqm shell. Short names in the output: boh_m = back-of-house corridor, boh_d = service entry, dirty = dirty linen and clinical waste room, cr1 and cr2 = collection rooms, gallery = clinical corridor, OUT_MAIN, OUT_STAFF and OUT_SVC = outside at the main, staff and service doors.</p>

<h2>Area schedule</h2>
<p class="note">Drawn sqm against the reference target. Both collection rooms: 19.0 sqm, the middle of the 18 to 20 sqm range in the venue room schedule and pathology partner brief (partner floor 9 to 10 sqm; the public hospital guideline shows 12 sqm for one enclosed room). Hair and nails: 5 to 6 sqm per station.</p>
<div class="plan" style="padding:0">__SCHED__</div>

<h2>Reference layouts and sizing sources</h2>
<table><tr><th style="width:28%">Reference</th><th>What it shows</th><th style="width:24%">Used for</th></tr>__REFS__</table>
<p class="note">Pinterest boards could not be retrieved (the pages return no readable pins). No architect plan of a 250 to 300 sqm wellness lounge was found that could be cited as a plan, so none is claimed. The two public hospital planning guides are the strongest sources.</p>

<h2>Open questions for the architect</h2>
<ol>__Q__</ol>
<p class="note">Concept only, not for construction. Nobody has been contacted. Nothing has been ordered, signed or paid.</p>
</div></body></html>
"""

# area schedule as html table
sched = [
    ("Blood Collection Room 1", f"{A['cr1']:.1f}", "19 (middle of 18 to 20)", "Pathology partner brief; venue room schedule"),
    ("Blood Collection Room 2", f"{A['cr2']:.1f}", "19 (equal to Room 1)", "Venue room schedule; public guideline 12 sqm minimum for one enclosed room"),
    ("Massage 1 and 2 (each)", f"{A['m1']:.1f}", "12", "Venue room schedule"),
    ("Beauty 1 and 2 (each)", f"{A['b1']:.1f}", "11", "Venue room schedule"),
    ("Open-plan luxury lounge", f"{A['lounge']:.1f}", "35", "Venue room schedule (exceeded)"),
    ("Private Refreshment Counter", f"{A['counter']:.1f}", "8", "Venue room schedule"),
    ("Reception", f"{A['recep']:.1f}", "15", "Venue room schedule"),
    ("Hairdressing (4 chairs, 2 backwash)", f"{A['hair']:.1f}", "20 to 24 (5 to 6 per chair)", "Brief of 2026-10-17; salon sizing guides"),
    ("Nails and pedicure (4 stations)", f"{A['nails']:.1f}", "20 to 24 (5 to 6 per station)", "Brief of 2026-10-17; salon sizing guides"),
    ("Accessible WC", f"{A['accwc']:.1f}", "7", "Venue room schedule"),
    ("Standard WC", f"{A['stdwc']:.1f}", "4", "Venue room schedule"),
    ("Staff room and lockers", f"{A['staff']:.1f}", "10", "Venue room schedule"),
    ("Clean linen", f"{A['clean']:.1f}", "6", "Venue room schedule"),
    ("Dirty linen and clinical waste", f"{A['dirty']:.1f}", "4", "Venue room schedule"),
    ("Storage (consumables, retail stock)", f"{A['storage']:.1f}", "not separately scheduled", "Procurement list shelving items"),
    ("Service entry (dirty route)", f"{A['boh_d']:.1f}", "not separately scheduled", "New in version 2"),
    ("Circulation (clinical corridor, staff corridor, arrival lobby)", f"{A['gallery']+A['boh_m']+A['lobby']:.1f}", "16", "Venue room schedule (hallway only; the lounge also carries walking traffic)"),
    ("Total gross internal", f"{chk['total']:.1f}", "257 to 290 range", "Site Brief"),
]
rows = "".join(f"<tr><td>{esc(a)}</td><td class='n'>{esc(b)}</td><td>{esc(c)}</td><td>{esc(d)}</td></tr>" for a, b, c, d in sched)
sched_html = "<table style='margin:0'><tr><th>Zone</th><th>Drawn sqm</th><th>Reference target</th><th>Source of target</th></tr>" + rows + "</table>"

page = (page.replace("__SVG2__", svg2i).replace("__SVG1__", svg1i).replace("__SVG2B__", svg2i)
        .replace("__CHANGES__", changes_html).replace("__BA__", ba_html).replace("__CHECK__", checks_html)
        .replace("__SCHED__", sched_html).replace("__REFS__", refs_html).replace("__Q__", q_html))
assert "—" not in page and "–" not in page, "dash found"
out = root / "outputs/PRESENTATION/floor-plan-v2.html"
out.write_text(page, encoding="utf-8")
print("wrote", out, len(page))
