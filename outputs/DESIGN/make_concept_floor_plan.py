#!/usr/bin/env python3
"""Generates outputs/DESIGN/CONCEPT-FLOOR-PLAN.svg (concept only, 18.5 m x 15.6 m)."""
import sys, html

S = 44.0           # px per metre (main plan)
OX, OY = 70, 250   # plan origin
W, D = 18.5, 15.6

# palette (warm neutral)
BG = "#FBF8F3"; INK = "#3A322B"; MUTE = "#8A7F73"; WALL = "#3A322B"
FILL = {
    "clinical": "#DCE7E3", "bay": "#F3DDD2", "lounge": "#EFE4D4", "counter": "#F6E7BE",
    "reception": "#EAD9C0", "hair": "#EADFCF", "nail": "#F1DED6", "staff": "#E3DDD4",
    "wc": "#E1E7EC", "circ": "#F7F3EC", "waste": "#E9C9C2", "fridge": "#CFE0DB",
}
BLUE = "#3E7EA6"; RED = "#B5483A"; GOLD = "#B58B2A"

out = []
def a(s): out.append(s)

def X(m): return OX + m * S
def Y(m): return OY + m * S

def rect(x, y, w, h, fill, stroke=WALL, sw=2.2, extra=""):
    a(f'<rect x="{X(x):.1f}" y="{Y(y):.1f}" width="{w*S:.1f}" height="{h*S:.1f}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" {extra}/>')

def line(x1, y1, x2, y2, stroke=WALL, sw=2.2, dash=None, cap="butt"):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    a(f'<line x1="{X(x1):.1f}" y1="{Y(y1):.1f}" x2="{X(x2):.1f}" y2="{Y(y2):.1f}" stroke="{stroke}" stroke-width="{sw}"{d} stroke-linecap="{cap}"/>')

def text(x, y, s, size=11, weight="400", fill=INK, anchor="middle", px=False, style=""):
    xx, yy = (x, y) if px else (X(x), Y(y))
    a(f'<text x="{xx:.1f}" y="{yy:.1f}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" {style}>{html.escape(s)}</text>')

def label(x, y, name, sqm, size=11.5):
    text(x, y, name, size, "700")
    text(x, y + 0.36, f"{sqm:.1f} sqm", size - 2, "400", MUTE)

def gap(x1, y1, x2, y2):
    """Door opening: white-ish break in a wall."""
    a(f'<line x1="{X(x1):.1f}" y1="{Y(y1):.1f}" x2="{X(x2):.1f}" y2="{Y(y2):.1f}" stroke="{BG}" stroke-width="5" />')

def door(x, y, w, orient, swing):
    """orient 'h' door in horizontal wall at y spanning x..x+w; swing +1 down, -1 up."""
    if orient == "h":
        gap(x, y, x + w, y)
        yy = y + swing * w
        a(f'<path d="M {X(x):.1f} {Y(y):.1f} L {X(x):.1f} {Y(yy):.1f} A {w*S:.1f} {w*S:.1f} 0 0 {1 if swing<0 else 0} {X(x+w):.1f} {Y(y):.1f}" fill="none" stroke="{MUTE}" stroke-width="1"/>')
    else:
        gap(x, y, x, y + w)
        xx = x + swing * w
        a(f'<path d="M {X(x):.1f} {Y(y):.1f} L {X(xx):.1f} {Y(y):.1f} A {w*S:.1f} {w*S:.1f} 0 0 {1 if swing>0 else 0} {X(x):.1f} {Y(y+w):.1f}" fill="none" stroke="{MUTE}" stroke-width="1"/>')

def basin(x, y, w=0.55, h=0.42):
    a(f'<rect x="{X(x):.1f}" y="{Y(y):.1f}" width="{w*S:.1f}" height="{h*S:.1f}" rx="4" fill="#fff" stroke="{BLUE}" stroke-width="1.4"/>')
    a(f'<circle cx="{X(x+w/2):.1f}" cy="{Y(y+h/2):.1f}" r="{h*S*0.28:.1f}" fill="none" stroke="{BLUE}" stroke-width="1.2"/>')

def item(x, y, w, h, fill="#fff", stroke=MUTE, rx=3, sw=1.1):
    a(f'<rect x="{X(x):.1f}" y="{Y(y):.1f}" width="{w*S:.1f}" height="{h*S:.1f}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')

def circ(x, y, r, fill="#fff", stroke=MUTE, sw=1.1):
    a(f'<circle cx="{X(x):.1f}" cy="{Y(y):.1f}" r="{r*S:.1f}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')

def curtain(x1, y1, x2, y2):
    """Curtain track: dashed line with scallop ticks."""
    line(x1, y1, x2, y2, stroke=GOLD, sw=2.4, dash="7 4")

AREAS = {}
def zone(key, name, x, y, w, h, fill, lab=True, lx=None, ly=None, size=11.5, wall=True):
    AREAS[key] = (name, w * h)
    rect(x, y, w, h, FILL[fill], stroke=WALL if wall else "none", sw=1.6)
    if lab:
        label(lx if lx is not None else x + w / 2, ly if ly is not None else y + h / 2, name, w * h, size)

# ---------------------------------------------------------------- header
a(f'<svg xmlns="http://www.w3.org/2000/svg" width="1840" height="1400" viewBox="0 0 1840 1400" font-family="Helvetica, Arial, \'Noto Sans\', \'DejaVu Sans\', sans-serif">')
a(f'<rect width="1840" height="1400" fill="{BG}"/>')
text(70, 70, "GTT CENTER PERTH", 15, "700", GOLD, "start", px=True, style='letter-spacing="3"')
text(70, 112, "Concept Floor Plan and Layout Schematic", 34, "700", INK, "start", px=True)
text(70, 142, "Option A shown: two dedicated blood collection rooms.  Option B (one large room with clinical privacy curtain) shown in the inset.", 14, "400", MUTE, "start", px=True)
text(70, 168, f"Typical rectangle {W} m x {D} m = {W*D:.1f} sqm gross internal. Site Brief range about 257 to 290 sqm. Scale 1:100 at A1 (see scale bar).", 14, "400", INK, "start", px=True)
a(f'<rect x="70" y="190" width="1700" height="2" fill="{GOLD}" opacity="0.6"/>')

# stamp
a(f'<rect x="1050" y="40" width="720" height="48" rx="6" fill="#fff" stroke="{RED}" stroke-width="2"/>')
text(1410, 61, "CONCEPT ONLY. NOT FOR CONSTRUCTION.", 15, "700", RED, "middle", px=True)
text(1410, 80, "Subject to site survey, architect and NCC compliance.", 13, "400", RED, "middle", px=True)

# ---------------------------------------------------------------- shell
a(f'<rect x="{X(0)-6:.1f}" y="{Y(0)-6:.1f}" width="{W*S+12:.1f}" height="{D*S+12:.1f}" fill="none" stroke="{WALL}" stroke-width="1" opacity="0.35"/>')

# Row A (rear, y 0-4.4)
zone("staff", "Staff room", 0, 0, 4.1, 2.4, "staff", ly=1.75, size=10)
zone("svc", "Service / linen", 0, 2.4, 2.1, 2.0, "staff", size=9, ly=3.2)
zone("swc", "Staff WC", 2.1, 2.4, 2.0, 2.0, "wc", size=9, ly=3.3)
zone("bcr1", "Blood Collection Room 1", 4.1, 0, 4.0, 4.4, "clinical", ly=3.75, size=10)
zone("spec", "Specimen bay", 8.1, 0, 2.2, 2.2, "fridge", lab=False)
text(9.2, 1.75, "specimen bay", 8.5, "700"); text(9.2, 2.05, "4.8 sqm", 7.5, "400", MUTE)
zone("waste", "Clinical waste + dirty linen", 8.1, 2.2, 2.2, 2.2, "waste", lab=False)
text(9.2, 3.65, "clinical waste", 8.5, "700"); text(9.2, 3.9, "+ dirty linen", 8, "700"); text(9.2, 4.2, "4.8 sqm", 7.5, "400", MUTE)
zone("bcr2", "Blood Collection Room 2", 10.3, 0, 4.4, 4.4, "clinical", ly=3.75, size=10)
zone("awc", "Accessible WC", 14.7, 0, 2.4, 2.9, "wc", size=9, ly=2.35)
zone("swc2", "WC", 17.1, 0, 1.4, 2.9, "wc", size=9, ly=2.3)
AREAS["lobby"] = ("WC lobby", 3.8 * 1.5)
rect(14.7, 2.9, 3.8, 1.5, FILL["circ"], stroke="none")
# Spine + circulation
AREAS["spine"] = ("Rear circulation spine", 18.5 * 1.2)
rect(0, 4.4, 18.5, 1.2, FILL["circ"], stroke="none")
# Front: bays (west strip)
bays = [("m1", "Massage 1", 5.6, "bay"), ("m2", "Massage 2", 8.1, "bay"), ("b1", "Beauty 1", 10.6, "bay"), ("b2", "Beauty 2", 13.1, "bay")]
for k, n, y0, f in bays:
    zone(k, n, 0, y0, 4.1, 2.5, f, lab=False)
# mid block
zone("lounge", "Open-plan luxury lounge", 4.1, 5.6, 6.9, 5.0, "lounge", lx=7.55, ly=7.95, size=12.5)
zone("counter", "Private Refreshment Counter", 4.1, 10.6, 3.2, 2.5, "counter", size=8.6, ly=11.55, wall=True)
AREAS["approach"] = ("Lounge approach", 3.7 * 2.5)
rect(7.3, 10.6, 3.7, 2.5, FILL["lounge"], stroke="none")
zone("recep", "Reception", 4.1, 13.1, 4.7, 2.5, "reception", lx=6.2, ly=14.7, size=11)
AREAS["vest"] = ("Entry vestibule", 2.2 * 2.5)
rect(8.8, 13.1, 2.2, 2.5, FILL["circ"], stroke=WALL, sw=1.6)
# east column
zone("hair", "Hairdressing (open plan)", 11.0, 5.6, 7.5, 6.0, "hair", lab=False)
zone("nail", "Nails + pedicure (open plan)", 11.0, 11.6, 7.5, 4.0, "nail", lab=False)

# ---------------------------------------------------------------- walls (re-stroke key walls thicker)
def W_(x1, y1, x2, y2, sw=3.2): line(x1, y1, x2, y2, WALL, sw)
# external envelope
W_(0, 0, W, 0, 5.5); W_(W, 0, W, D, 5.5); W_(W, D, 0, D, 5.5); W_(0, D, 0, 0, 5.5)
# rear row partitions
W_(0, 4.4, 4.1, 4.4); W_(4.1, 4.4, 14.7, 4.4); W_(4.1, 0, 4.1, 4.4)
W_(14.7, 0, 14.7, 4.4); W_(14.7, 2.9, 18.5, 2.9, 2.2); W_(14.7, 4.4, 14.7, 2.9)
# openings for lobby: no wall at y=4.4 for x 14.7..18.5
# bays: solid partitions between bays, back wall of bay row
for yy in (5.6, 8.1, 10.6, 13.1):
    W_(0, yy, 4.1, yy, 3.0)
# spine edge north line (rear row south wall) already drawn; lounge boundary
W_(4.1, 5.6, 4.1, 15.6, 1.2)  # faint line under curtains drawn later
# counter room walls
W_(4.1, 10.6, 4.1, 13.1, 3.0); W_(4.1, 13.1, 8.8, 13.1, 3.0); W_(7.3, 10.6, 7.3, 13.1, 3.0)
# vestibule walls
W_(8.8, 13.1, 8.8, 15.6, 3.0); W_(11.0, 13.1, 11.0, 15.6, 3.0); W_(8.8, 13.1, 11.0, 13.1, 1.6)
# open-plan lines (dotted)
line(11.0, 5.6, 11.0, 13.1, MUTE, 1.4, "3 5")
line(11.0, 11.6, 18.5, 11.6, MUTE, 1.2, "3 5")
line(4.1, 10.6, 11.0, 10.6, MUTE, 1.0, "2 6")

# curtain tracks at bay openings (x=4.1) and spine ends
for k, n, y0, f in bays:
    curtain(4.1, y0 + 0.05, 4.1, y0 + 2.45)

# ---------------------------------------------------------------- doors
door(5.1, 4.4, 0.9, "h", +1)            # BCR1 -> spine
door(11.3, 4.4, 0.9, "h", +1)           # BCR2 -> spine
gap(8.1, 0.8, 8.1, 1.7); gap(8.1, 2.9, 8.1, 3.8)     # BCR1 <-> bays
gap(10.3, 0.8, 10.3, 1.7); gap(10.3, 2.9, 10.3, 3.8) # BCR2 <-> bays
door(0.5, 4.4, 0.9, "h", +1)            # service entry -> spine
door(2.6, 4.4, 0.8, "h", +1)            # staff WC -> spine
gap(0, 2.9, 0, 3.8)                     # exterior service door
text(-0.25, 3.35, "service door", 8.5, "400", MUTE, "end")
gap(0.6, 2.4, 1.5, 2.4)                 # staff room <-> service
door(15.2, 2.9, 0.9, "h", +1)           # accessible WC door
door(17.4, 2.9, 0.7, "h", +1)           # std WC door
# entry (shopfront) in south wall
gap(9.05, 15.6, 10.75, 15.6)
a(f'<line x1="{X(9.05):.1f}" y1="{Y(15.6):.1f}" x2="{X(10.75):.1f}" y2="{Y(15.6):.1f}" stroke="{GOLD}" stroke-width="4"/>')
text(9.9, 16.2, "MAIN ENTRY", 11, "700", GOLD)
# shopfront glazing marker along south wall nail side/lounge
line(11.0, 15.6, 18.5, 15.6, BLUE, 1.4)
line(0.3, 15.6, 8.8, 15.6, BLUE, 1.4)
text(14.7, 16.2, "shopfront glazing (assumed)", 9, "400", MUTE)
# openings: reception to vestibule
gap(8.8, 13.6, 8.8, 15.0)
# counter open to lounge
gap(4.5, 10.6, 7.0, 10.6)
# staff passage to hair zone
# lobby opens to spine (no wall) ; spine open to lounge
gap(4.5, 5.6, 10.8, 5.6)
a(f'<text x="{X(7.7):.1f}" y="{Y(5.08):.1f}" font-size="9" fill="{MUTE}" text-anchor="middle">clinical corridor (1.2 m)</text>')
text(16.6, 3.8, "lobby", 8.5, "400", MUTE)

# ---------------------------------------------------------------- furniture
# BCR1
item(5.0, 1.4, 0.85, 1.7, "#fff", INK); text(5.42, 2.3, "Chair A", 8.5)    # phlebotomy chair A
circ(6.4, 2.3, 0.22)                                                         # stool
basin(7.2, 0.15); text(7.5, 0.95, "HB", 8, "700", BLUE)
item(4.3, 0.15, 2.4, 0.6, "#fff", MUTE); text(5.5, 0.55, "bench + sharps", 8)
item(7.1, 0.9, 0.85, 1.3, "#fff", MUTE); text(7.52, 1.5, "recovery", 7.5); text(7.52, 1.78, "recliner", 7.5)
# BCR2
item(11.4, 1.4, 0.85, 1.7, "#fff", INK); text(11.82, 2.3, "Chair B", 8.5)
circ(12.9, 2.3, 0.22)
basin(13.7, 0.15); text(13.97, 0.95, "HB", 8, "700", BLUE)
item(10.5, 0.15, 2.5, 0.6, "#fff", MUTE); text(11.75, 0.55, "doc. bench + sharps", 8)
# Specimen bay
item(8.35, 0.25, 0.7, 0.55, "#fff", INK); text(8.7, 0.62, "C", 9, "700")
item(9.2, 0.25, 0.9, 1.2, "#fff", RED, sw=1.6); text(9.65, 0.98, "fridge", 8, "700", RED)

# Waste bay
item(8.35, 2.45, 0.55, 0.55, "#F3D36B", MUTE); item(9.0, 2.45, 0.55, 0.55, "#F3D36B", MUTE); item(9.65, 2.45, 0.45, 0.55, "#D95F4B", MUTE)
# Staff room
item(0.5, 0.45, 1.6, 0.8, "#fff"); circ(0.8, 0.3, 0.12); circ(1.8, 0.3, 0.12)
item(2.5, 0.2, 1.4, 0.4, "#E6D7BF"); text(3.2, 0.5, "lockers", 7.5, "400", MUTE)
# Staff WC
circ(3.8, 4.1, 0.2); basin(2.3, 2.5, 0.4, 0.3)
# Accessible WC
circ(16.5, 0.45, 0.22); basin(15.0, 0.25, 0.45, 0.35)

# Std WC
circ(17.8, 0.5, 0.2); basin(17.2, 1.8, 0.4, 0.3)
# Beds / bays
for k, n, y0, f in bays:
    by = y0 + 0.45
    item(1.3, by, 1.95, 0.75, "#fff", INK); text(2.28, by + 0.47, "bed", 8)
    circ(0.9, by + 0.37, 0.2)
    basin(0.15, y0 + 0.1)
    text(2.05, y0 + 1.75, n, 11, "700")
    text(2.05, y0 + 2.1, f"{4.1*2.5:.1f} sqm", 9, "400", MUTE)
    if n.startswith("Beauty"):
        a(f'<rect x="{X(3.35):.1f}" y="{Y(y0+0.1):.1f}" width="{0.5*S:.1f}" height="{0.4*S:.1f}" rx="4" fill="#fff" stroke="{BLUE}" stroke-width="1.4"/>')
        text(3.6, y0 + 0.65, "IS", 7.5, "700", BLUE)
# Lounge furniture
def couch(x, y, w=2.0, h=0.85):
    item(x, y, w, h, "#fff", MUTE, rx=7); item(x + 0.05, y + 0.05, w - 0.1, 0.22, "#EBDDC8", MUTE, rx=5, sw=0.6)
couch(4.5, 6.0); couch(7.2, 6.0, 1.9)
couch(4.5, 9.4, 2.0, 0.85); couch(7.2, 9.4, 1.9, 0.85)
item(4.8, 7.55, 0.8, 0.8, "#fff", MUTE, rx=40); item(10.1, 7.55, 0.7, 0.7, "#fff", MUTE, rx=40)
circ(10.6, 6.3, 0.2); circ(10.6, 9.7, 0.2)
for (px_, py_) in [(6.35, 7.0), (6.35, 9.15), (9.5, 7.0), (9.5, 9.15), (4.3, 6.4)]:
    circ(px_, py_, 0.14, "#F6E7BE", GOLD, 1)

# Refreshment counter
item(4.4, 10.7, 2.7, 0.5, "#fff", INK); text(5.75, 11.07, "bench", 7.5)
basin(4.35, 12.4, 0.5, 0.4); item(5.0, 12.35, 0.7, 0.55, "#fff", MUTE); text(5.35, 12.7, "mini fridge", 6)
item(5.85, 12.4, 0.6, 0.5, "#fff", MUTE); text(6.15, 12.72, "coffee", 7)

# Reception
item(4.6, 13.35, 3.2, 0.75, "#fff", INK); text(6.2, 13.82, "desk, 2 POS", 8.5)
item(8.05, 13.4, 0.5, 1.9, "#E6D7BF", MUTE)
item(4.15, 14.4, 0.3, 1.0, "#E6D7BF", MUTE)
# Hairdressing
for i in range(4):
    cx = 12.0 + i * 1.7
    item(cx - 0.35, 6.15, 0.7, 0.7, "#fff", INK, rx=35)
item(11.3, 5.65, 6.9, 0.18, "#CFE3EA", BLUE, rx=1)
text(14.7, 5.5, "", 6)
for i in range(2):
    bx = 12.4 + i * 3.0
    item(bx, 9.2, 1.1, 0.9, "#fff", BLUE, rx=14); text(bx + 0.55, 9.7, "backwash", 7.5, "400", BLUE)
text(14.75, 7.5, "Hairdressing (open plan)", 12, "700"); text(14.75, 7.86, f"{7.5*6.0:.1f} sqm  (4 chairs, 2 backwash)", 9.5, "400", MUTE)
text(14.75, 8.2, "mirror wall along rear", 8.5, "400", MUTE)
# Nails
for i in range(4):
    nx = 11.4 + i * 1.8
    item(nx, 11.9, 1.2, 0.6, "#fff", INK); circ(nx + 0.6, 12.8, 0.2); circ(nx + 0.6, 11.7, 0.0)
for i in range(4):
    nx = 11.45 + i * 1.8
    item(nx, 14.2, 0.9, 1.1, "#fff", MUTE, rx=10)
text(14.75, 13.5, "Nails + pedicure (open plan)", 12, "700"); text(14.75, 13.86, f"{7.5*4.0:.1f} sqm  (4 stations, 4 pedicure chairs)", 9.5, "400", MUTE)
# LEV duct
a(f'<path d="M {X(18.5)-2:.1f} {Y(12.2):.1f} L {X(18.5)+34:.1f} {Y(12.2):.1f}" stroke="{RED}" stroke-width="3"/>')
a(f'<path d="M {X(18.5)+26:.1f} {Y(12.2)-6:.1f} L {X(18.5)+36:.1f} {Y(12.2):.1f} L {X(18.5)+26:.1f} {Y(12.2)+6:.1f}" fill="none" stroke="{RED}" stroke-width="2.5"/>')
text(18.5 + 0.9, 12.55, "LEV exhaust", 9, "700", RED, "start")
text(18.5 + 0.9, 12.82, "to outside", 9, "400", RED, "start")

# room name labels for zones that had lab=False
for k in ("staff", "svc", "swc", "bcr1", "bcr2", "spec", "waste", "awc", "swc2", "lounge", "counter", "recep"):
    pass

text(9.15, 11.55, "Clinical areas are", 8.5, "700", RED); text(9.15, 11.85, "physically separate from", 8.5, "700", RED); text(9.15, 12.15, "the refreshment counter", 8.5, "700", RED)
text(9.9, 14.3, "Entry", 9, "700", GOLD); text(9.9, 14.6, "vestibule", 8.5, "400", MUTE)

# ---------------------------------------------------------------- dimensions, north arrow, scale bar
# overall dims
def dim_h(x1, x2, y, s):
    line(x1, y, x2, y, MUTE, 1); line(x1, y - 0.12, x1, y + 0.12, MUTE, 1); line(x2, y - 0.12, x2, y + 0.12, MUTE, 1)
    text((x1 + x2) / 2, y - 0.2, s, 10.5, "700", MUTE)
def dim_v(x, y1, y2, s):
    line(x, y1, x, y2, MUTE, 1); line(x - 0.12, y1, x + 0.12, y1, MUTE, 1); line(x - 0.12, y2, x + 0.12, y2, MUTE, 1)
    a(f'<text transform="translate({X(x)-8:.1f},{Y((y1+y2)/2):.1f}) rotate(-90)" font-size="10.5" font-weight="700" fill="{MUTE}" text-anchor="middle">{s}</text>')
dim_h(0, W, -0.7, f"{W} m")
dim_v(-0.9, 0, D, f"{D} m")

# north arrow placeholder
nx, ny = X(W) - 60, Y(D) + 85
a(f'<g transform="translate({nx:.1f},{ny:.1f})"><circle r="26" fill="#fff" stroke="{INK}" stroke-width="1.5"/><path d="M0 -20 L8 10 L0 5 L-8 10 Z" fill="{INK}"/><text y="-30" font-size="14" font-weight="700" text-anchor="middle" fill="{INK}">N</text><text y="44" font-size="8.5" text-anchor="middle" fill="{MUTE}">placeholder, true</text><text y="55" font-size="8.5" text-anchor="middle" fill="{MUTE}">north per site</text></g>')

# scale bar (0-5 m)
sx, sy = X(0), Y(D) + 62
a(f'<g><rect x="{sx:.1f}" y="{sy:.1f}" width="{S:.1f}" height="8" fill="{INK}"/><rect x="{sx+S:.1f}" y="{sy:.1f}" width="{S:.1f}" height="8" fill="#fff" stroke="{INK}"/><rect x="{sx+2*S:.1f}" y="{sy:.1f}" width="{S:.1f}" height="8" fill="{INK}"/><rect x="{sx+3*S:.1f}" y="{sy:.1f}" width="{S:.1f}" height="8" fill="#fff" stroke="{INK}"/><rect x="{sx+4*S:.1f}" y="{sy:.1f}" width="{S:.1f}" height="8" fill="{INK}"/></g>')
for i in range(6):
    a(f'<text x="{sx+i*S:.1f}" y="{sy+24:.1f}" font-size="10" text-anchor="middle" fill="{INK}">{i}</text>')
a(f'<text x="{sx+5*S+14:.1f}" y="{sy+24:.1f}" font-size="10" fill="{INK}">metres</text>')
text(sx, sy - 8, "Scale bar", 10, "700", INK, "start", px=True)

# ---------------------------------------------------------------- right panel: legend
PX = 1010
text(PX, 262, "LEGEND", 14, "700", GOLD, "start", px=True, style='letter-spacing="2"')
leg = [("clinical", "Blood collection (solid walls)"), ("fridge", "Specimen fridge + centrifuge bay"), ("waste", "Clinical waste + dirty linen"),
       ("bay", "Massage / beauty bay (partition walls + curtain)"), ("lounge", "Open-plan lounge / open plan zones"),
       ("counter", "Private Refreshment Counter (GTT clients only)"), ("reception", "Reception"), ("staff", "Staff, back of house"),
       ("wc", "Toilets (accessible + standard)"), ("circ", "Circulation")]
for i, (k, n) in enumerate(leg):
    col = i // 5; row = i % 5
    lx = PX + col * 420; ly = 280 + row * 26
    a(f'<rect x="{lx}" y="{ly}" width="26" height="16" fill="{FILL[k]}" stroke="{WALL}" stroke-width="1.2"/>')
    text(lx + 36, ly + 13, n, 12, "400", INK, "start", px=True)
ly = 280 + 5 * 26 + 6
# symbol legend
a(f'<line x1="{PX}" y1="{ly+8}" x2="{PX+26}" y2="{ly+8}" stroke="{GOLD}" stroke-width="2.4" stroke-dasharray="7 4"/>'); text(PX + 36, ly + 12, "Privacy curtain track", 12, "400", INK, "start", px=True)
a(f'<rect x="{PX+210}" y="{ly}" width="22" height="16" rx="4" fill="#fff" stroke="{BLUE}" stroke-width="1.4"/><circle cx="{PX+221}" cy="{ly+8}" r="3.5" fill="none" stroke="{BLUE}" stroke-width="1.2"/>'); text(PX + 242, ly + 12, "HB handwash basin (IS = instrument sink)", 12, "400", INK, "start", px=True)
a(f'<line x1="{PX}" y1="{ly+34}" x2="{PX+26}" y2="{ly+34}" stroke="{WALL}" stroke-width="3.2"/>'); text(PX + 36, ly + 38, "Solid partition wall", 12, "400", INK, "start", px=True)
a(f'<line x1="{PX+210}" y1="{ly+34}" x2="{PX+236}" y2="{ly+34}" stroke="{MUTE}" stroke-width="1.4" stroke-dasharray="3 5"/>'); text(PX + 246, ly + 38, "Open-plan boundary (no wall)", 12, "400", INK, "start", px=True)
a(f'<line x1="{PX}" y1="{ly+60}" x2="{PX+26}" y2="{ly+60}" stroke="{RED}" stroke-width="3"/>'); text(PX + 36, ly + 64, "LEV exhaust to outside (nails)", 12, "400", INK, "start", px=True)

# ---------------------------------------------------------------- area schedule
ty = 540
text(PX, ty - 10, "AREA SCHEDULE (drawn, sqm)", 14, "700", GOLD, "start", px=True, style='letter-spacing="2"')
rows = [("Blood Collection Room 1", "bcr1", "18"), ("Blood Collection Room 2", "bcr2", "18 to 20"),
        ("Specimen fridge + centrifuge bay", "spec", "in rooms"), ("Clinical waste + dirty linen", "waste", "4"),
        ("Massage 1 and 2", ("m1", "m2"), "12 each"), ("Beauty 1 and 2", ("b1", "b2"), "11 each"),
        ("Open-plan lounge", "lounge", "35"), ("Private Refreshment Counter", "counter", "8"),
        ("Reception", "recep", "15"), ("Hairdressing (4 chairs, 2 backwash)", "hair", "52"),
        ("Nails + pedicure (4 stations)", "nail", "32"), ("Accessible WC", "awc", "7"), ("Standard WC", "swc2", "4"),
        ("Staff room", "staff", "10"), ("Staff WC", "swc", "4"), ("Service entry / clean linen", "svc", "6 (linen)")]
a(f'<rect x="{PX-8}" y="{ty}" width="760" height="24" fill="{INK}"/>')
text(PX, ty + 17, "Zone", 11.5, "700", "#fff", "start", px=True); text(PX + 420, ty + 17, "Drawn", 11.5, "700", "#fff", "end", px=True)
text(PX + 560, ty + 17, "Room schedule target", 11.5, "700", "#fff", "end", px=True)
yy = ty + 24
tot = 0
for i, (n, k, tgt) in enumerate(rows):
    ar = sum(AREAS[kk][1] for kk in k) if isinstance(k, tuple) else AREAS[k][1]
    if isinstance(k, tuple): ar_s = f"{ar/2:.1f} each"
    else: ar_s = f"{ar:.1f}"
    a(f'<rect x="{PX-8}" y="{yy}" width="760" height="21" fill="{"#fff" if i%2==0 else "#F3EDE3"}"/>')
    text(PX, yy + 15, n, 11.5, "400", INK, "start", px=True)
    text(PX + 420, yy + 15, ar_s, 11.5, "700", INK, "end", px=True)
    text(PX + 560, yy + 15, tgt, 11.5, "400", MUTE, "end", px=True)
    yy += 21
circ_total = AREAS["spine"][1] + AREAS["lobby"][1] + AREAS["approach"][1] + AREAS["vest"][1]
room_total = sum(v[1] for kk, v in AREAS.items() if kk not in ("spine", "lobby", "approach", "vest"))
a(f'<rect x="{PX-8}" y="{yy}" width="760" height="21" fill="#F3EDE3"/>')
text(PX, yy + 15, "Circulation (spine, WC lobby, lounge approach, vestibule)", 11.5, "400", INK, "start", px=True)
text(PX + 420, yy + 15, f"{circ_total:.1f}", 11.5, "700", INK, "end", px=True); text(PX + 560, yy + 15, "16", 11.5, "400", MUTE, "end", px=True)
yy += 21
a(f'<rect x="{PX-8}" y="{yy}" width="760" height="24" fill="{GOLD}"/>')
text(PX, yy + 17, f"Total gross internal ({W} m x {D} m)", 12, "700", "#fff", "start", px=True)
text(PX + 420, yy + 17, f"{room_total+circ_total:.1f}", 12, "700", "#fff", "end", px=True)
text(PX + 560, yy + 17, "257 to 290 range", 11.5, "700", "#fff", "end", px=True)
yy += 36
note = [
    "Room targets come from the venue room schedule. Hair, nails, reception and the four bays are drawn slightly",
    "below target (a 1.2 m clinical corridor and an entry vestibule use the difference). A real site and architect",
    "may need about 300 sqm for the full schedule with no compromise. Treat all areas as indicative.",
]
for n in note:
    text(PX, yy, n, 10.5, "400", MUTE, "start", px=True); yy += 15

# ---------------------------------------------------------------- Option B inset
IX, IY, IS_ = PX, 1090, 34.0
text(IX, IY - 22, "OPTION B INSET: ONE LARGE COLLECTION ROOM WITH CLINICAL PRIVACY CURTAIN", 13, "700", GOLD, "start", px=True, style='letter-spacing="1"')
def ix(m): return IX + m * IS_
def iy(m): return IY + m * IS_
# merged room 8.4 x 4.4 = 36.96
a(f'<rect x="{ix(0):.1f}" y="{iy(0):.1f}" width="{8.4*IS_:.1f}" height="{4.4*IS_:.1f}" fill="{FILL["clinical"]}" stroke="{WALL}" stroke-width="3"/>')
a(f'<rect x="{ix(8.4):.1f}" y="{iy(0):.1f}" width="{2.2*IS_:.1f}" height="{2.2*IS_:.1f}" fill="{FILL["fridge"]}" stroke="{WALL}" stroke-width="2"/>')
a(f'<rect x="{ix(8.4):.1f}" y="{iy(2.2):.1f}" width="{2.2*IS_:.1f}" height="{2.2*IS_:.1f}" fill="{FILL["waste"]}" stroke="{WALL}" stroke-width="2"/>')
# curtain divider
a(f'<line x1="{ix(4.2):.1f}" y1="{iy(0.15):.1f}" x2="{ix(4.2):.1f}" y2="{iy(4.25):.1f}" stroke="{GOLD}" stroke-width="3.2" stroke-dasharray="8 4"/>')
a(f'<text x="{ix(4.2):.1f}" y="{iy(-0.2):.1f}" font-size="10" font-weight="700" fill="{GOLD}" text-anchor="middle">clinical privacy curtain (ceiling track, floor to ceiling)</text>')
for cx, nm in ((1.6, "Chair A"), (6.0, "Chair B")):
    a(f'<rect x="{ix(cx):.1f}" y="{iy(1.4):.1f}" width="{0.85*IS_:.1f}" height="{1.7*IS_:.1f}" rx="3" fill="#fff" stroke="{INK}" stroke-width="1.2"/>')
    a(f'<text x="{ix(cx+0.42):.1f}" y="{iy(2.3):.1f}" font-size="8" text-anchor="middle">{nm}</text>')
    a(f'<circle cx="{ix(cx+1.4):.1f}" cy="{iy(2.3):.1f}" r="{0.2*IS_:.1f}" fill="#fff" stroke="{MUTE}"/>')
for bx in (0.2, 4.5):
    a(f'<rect x="{ix(bx+0.1):.1f}" y="{iy(0.15):.1f}" width="{0.55*IS_:.1f}" height="{0.42*IS_:.1f}" rx="4" fill="#fff" stroke="{BLUE}" stroke-width="1.4"/>')
    a(f'<text x="{ix(bx+0.9):.1f}" y="{iy(0.45):.1f}" font-size="8" font-weight="700" fill="{BLUE}">HB</text>')
a(f'<rect x="{ix(3.0):.1f}" y="{iy(3.2):.1f}" width="{0.85*IS_:.1f}" height="{1.0*IS_:.1f}" rx="3" fill="#fff" stroke="{MUTE}"/>')
a(f'<text x="{ix(3.42):.1f}" y="{iy(3.75):.1f}" font-size="7.5" text-anchor="middle">recliner</text>')
a(f'<text x="{ix(4.2):.1f}" y="{iy(1.0):.1f}" font-size="11" font-weight="700" text-anchor="middle" fill="{INK}"></text>')
a(f'<text x="{ix(2.1):.1f}" y="{iy(4.1):.1f}" font-size="10.5" font-weight="700" text-anchor="middle">Bay 1</text>')
a(f'<text x="{ix(6.3):.1f}" y="{iy(4.1):.1f}" font-size="10.5" font-weight="700" text-anchor="middle">Bay 2</text>')
a(f'<text x="{ix(9.5):.1f}" y="{iy(1.25):.1f}" font-size="8.5" font-weight="700" text-anchor="middle">specimen</text><text x="{ix(9.5):.1f}" y="{iy(1.6):.1f}" font-size="8.5" text-anchor="middle">fridge bay</text>')
a(f'<text x="{ix(9.5):.1f}" y="{iy(3.35):.1f}" font-size="8.5" font-weight="700" text-anchor="middle">clinical waste</text>')
a(f'<line x1="{ix(2.8):.1f}" y1="{iy(4.4):.1f}" x2="{ix(3.7):.1f}" y2="{iy(4.4):.1f}" stroke="{BG}" stroke-width="5"/>')
a(f'<text x="{ix(10.9):.1f}" y="{iy(0.4):.1f}" font-size="11" font-weight="700" fill="{INK}">One room, 37.0 sqm</text>')
tx = [ "Same footprint as Option A with the dividing wall removed.", "Two chairs, one curtain-separated bay each, a handwash", "basin in every bay, recovery recliner shared, specimen",
       "fridge bay and clinical waste kept apart from the", "Private Refreshment Counter (physical separation", "decided 2026-09-04 is unchanged).", "Curtain gives visual privacy only. Sound privacy is",
       "lower than two walled rooms (to confirm with the", "pathology partner before choosing Option B)."]
for i, t in enumerate(tx):
    a(f'<text x="{ix(10.9):.1f}" y="{iy(0.85)+i*14:.1f}" font-size="10" fill="{MUTE}">{html.escape(t)}</text>')

# footer
a(f'<rect x="70" y="1358" width="1700" height="1.5" fill="{GOLD}" opacity="0.6"/>')
text(70, 1382, "Concept only, not for construction; subject to site survey, architect and NCC compliance.   GTT Center Perth.   Drawing date 2026-10-16.", 12, "700", RED, "start", px=True)
a('</svg>')

open(sys.argv[1], "w", encoding="utf-8").write("\n".join(out))
print("room total", round(room_total, 1), "circ", round(circ_total, 1), "sum", round(room_total + circ_total, 1), "shell", W * D)
for k, v in AREAS.items():
    print(k, v[0], round(v[1], 2))
