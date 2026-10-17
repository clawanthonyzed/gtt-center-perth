#!/usr/bin/env python3
"""GTT Center Perth concept floor plan v2 (concept only, 18.5 m x 15.6 m shell).

Usage: make_concept_floor_plan_v2.py out.svg [--json out.json]

The room rectangles and the door / opening list below drive BOTH the drawing and the
circulation check (graph of rooms and doors). The script asserts:
  * rooms do not overlap and fill the shell exactly,
  * every door / opening lies on a boundary shared by the two rooms it joins,
  * every room is reachable from the main entry,
  * staff room -> entry, lounge -> collection rooms and staff room -> collection rooms avoid the dirty zone,
  * the clinical waste route (collection rooms -> service door) uses back-of-house nodes only,
  * both collection rooms have the same area,
  * the refreshment counter is physically apart from the collection rooms and dirty zone.
"""
import sys, html, json
from collections import deque

S = 44.0
OX, OY = 90, 250
W, D = 18.5, 15.6
CANVAS_W, CANVAS_H = 1840, 1330

BG = "#FBF8F3"; INK = "#3A322B"; MUTE = "#8A7F73"; WALL = "#3A322B"
FILL = {
    "clinical": "#DCE7E3", "bay": "#F3DDD2", "lounge": "#EFE4D4", "counter": "#F6E7BE",
    "reception": "#EAD9C0", "hair": "#EADFCF", "nail": "#F1DED6", "staff": "#E3DDD4",
    "wc": "#E1E7EC", "circ": "#F7F3EC", "waste": "#E9C9C2", "store": "#E9E2D6",
}
BLUE = "#3E7EA6"; RED = "#B5483A"; GOLD = "#B58B2A"; GREEN = "#3F7D4E"

# ---------------------------------------------------------------- geometry (metres, origin top-left, y down = south)
BAY_H = 8.9 / 4
R = {
    "dirty":   [(0, 1.2, 2.6, 1.6)],
    "clean":   [(0, 2.8, 2.6, 2.4)],
    "boh_d":   [(0, 0, 2.6, 1.2)],
    "boh_m":   [(2.6, 0, 9.5, 1.2)],
    "cr1":     [(2.6, 1.2, 4.75, 4.0)],
    "cr2":     [(7.35, 1.2, 4.75, 4.0)],
    "staff":   [(12.1, 0, 2.5, 5.2)],
    "storage": [(14.6, 0, 3.9, 2.2)],
    "accwc":   [(14.6, 2.2, 2.4, 3.0)],
    "stdwc":   [(17.0, 2.2, 1.5, 3.0)],
    "gallery": [(0, 5.2, 18.5, 1.5)],
    "m1": [(0, 6.7 + 0 * BAY_H, 4.8, BAY_H)],
    "m2": [(0, 6.7 + 1 * BAY_H, 4.8, BAY_H)],
    "b1": [(0, 6.7 + 2 * BAY_H, 4.8, BAY_H)],
    "b2": [(0, 6.7 + 3 * BAY_H, 4.8, BAY_H)],
    "lounge":  [(4.8, 6.7, 5.3, 6.2), (10.1, 6.7, 3.2, 2.1), (10.1, 11.3, 3.2, 1.6)],
    "counter": [(10.1, 8.8, 3.2, 2.5)],
    "lobby":   [(4.8, 12.9, 2.8, 2.7)],
    "recep":   [(7.6, 12.9, 5.7, 2.7)],
    "hair":    [(13.3, 6.7, 5.2, 4.6)],
    "nails":   [(13.3, 11.3, 5.2, 4.3)],
}
NAMES = {
    "dirty": "Dirty linen / clinical waste", "clean": "Clean linen", "boh_d": "Service entry (dirty route)",
    "boh_m": "Back-of-house corridor", "cr1": "Blood Collection Room 1", "cr2": "Blood Collection Room 2",
    "staff": "Staff room + lockers", "storage": "Storage (consumables, retail stock)", "accwc": "Accessible WC",
    "stdwc": "Standard WC", "gallery": "Clinical corridor", "m1": "Massage 1", "m2": "Massage 2",
    "b1": "Beauty 1", "b2": "Beauty 2", "lounge": "Open-plan luxury lounge", "counter": "Private Refreshment Counter",
    "lobby": "Arrival lobby", "recep": "Reception", "hair": "Hairdressing", "nails": "Nails + pedicure",
}
DIRTY_ZONE = {"dirty", "boh_d", "OUT_SVC"}
CLIENT_NODES = {"lobby", "lounge", "recep", "counter", "gallery", "m1", "m2", "b1", "b2", "hair", "nails", "accwc", "stdwc"}

def area(k): return sum(w * h for (_, _, w, h) in R[k])

# doors: (a, b, x, y, w, orient, swing, label)  orient h = door in horizontal wall at y spanning x..x+w; v = vertical wall at x spanning y..y+w
# swing: h: +1 opens south, -1 opens north ; v: +1 opens east, -1 opens west ; 0 = sliding / no swing drawn
DOORS = [
    ("OUT_MAIN", "lobby", 5.4, 15.6, 1.8, "h", 0),
    ("boh_m", "cr1", 3.3, 1.2, 1.0, "h", +1),
    ("boh_m", "cr2", 8.05, 1.2, 1.0, "h", +1),
    ("cr1", "gallery", 5.6, 5.2, 1.0, "h", -1),
    ("cr2", "gallery", 10.35, 5.2, 1.0, "h", -1),
    ("boh_d", "dirty", 0.8, 1.2, 0.9, "h", -1),
    ("boh_m", "staff", 12.1, 0.1, 1.0, "v", +1),
    ("staff", "gallery", 12.8, 5.2, 0.9, "h", -1),
    ("staff", "storage", 14.6, 0.2, 0.9, "v", +1),
    ("gallery", "accwc", 15.3, 5.2, 1.0, "h", -1),
    ("gallery", "stdwc", 17.3, 5.2, 0.9, "h", -1),
    ("gallery", "clean", 0.9, 5.2, 0.9, "h", -1),
    ("OUT_SVC", "boh_d", 0.0, 0.1, 1.0, "v", +1),
    ("OUT_STAFF", "boh_m", 10.4, 0.0, 1.0, "h", +1),
]
# open connections (no wall, drawn as dotted boundary or curtain): (a, b, x1, y1, x2, y2, kind)
OPENINGS = [
    ("boh_d", "boh_m", 2.6, 0.0, 2.6, 1.2, "open"),
    ("lobby", "lounge", 4.8, 12.9, 7.6, 12.9, "open"),
    ("lobby", "recep", 7.6, 12.9, 7.6, 15.6, "open"),
    ("recep", "lounge", 7.6, 12.9, 10.1, 12.9, "open"),
    ("recep", "lounge", 10.1, 12.9, 13.3, 12.9, "open"),
    ("counter", "lounge", 10.1, 9.1, 10.1, 11.0, "open"),
    ("lounge", "gallery", 4.8, 6.7, 10.1, 6.7, "open"),
    ("lounge", "gallery", 10.1, 6.7, 13.3, 6.7, "open"),
    ("hair", "lounge", 13.3, 6.7, 13.3, 8.8, "open"),
    ("hair", "nails", 13.3, 11.3, 18.5, 11.3, "open"),
    ("nails", "lounge", 13.3, 11.3, 13.3, 12.9, "open"),
    ("m1", "lounge", 4.8, 6.7, 4.8, 6.7 + BAY_H, "curtain"),
    ("m2", "lounge", 4.8, 6.7 + BAY_H, 4.8, 6.7 + 2 * BAY_H, "curtain"),
    ("b1", "lounge", 4.8, 6.7 + 2 * BAY_H, 4.8, 12.9, "curtain"),
    ("b1", "lobby", 4.8, 12.9, 4.8, 6.7 + 3 * BAY_H, "curtain"),
    ("b2", "lobby", 4.8, 6.7 + 3 * BAY_H, 4.8, 15.6, "curtain"),
]

# ---------------------------------------------------------------- geometry checks
TOL = 1e-6
def inter(a, b):
    ax, ay, aw, ah = a; bx, by, bw, bh = b
    ox = min(ax + aw, bx + bw) - max(ax, bx); oy = min(ay + ah, by + bh) - max(ay, by)
    return max(0, ox) * max(0, oy)

def on_boundary(k, seg):
    """segment (x1,y1,x2,y2) lies on an outer edge of one of room k's rectangles"""
    x1, y1, x2, y2 = seg
    for (x, y, w, h) in R[k]:
        if abs(y1 - y2) < TOL:  # horizontal
            if (abs(y1 - y) < TOL or abs(y1 - (y + h)) < TOL) and min(x1, x2) >= x - TOL and max(x1, x2) <= x + w + TOL: return True
        if abs(x1 - x2) < TOL:  # vertical
            if (abs(x1 - x) < TOL or abs(x1 - (x + w)) < TOL) and min(y1, y2) >= y - TOL and max(y1, y2) <= y + h + TOL: return True
    return False

def on_shell(seg):
    x1, y1, x2, y2 = seg
    if abs(y1 - y2) < TOL and (abs(y1) < TOL or abs(y1 - D) < TOL): return True
    if abs(x1 - x2) < TOL and (abs(x1) < TOL or abs(x1 - W) < TOL): return True
    return False

def check_geometry():
    msgs = []
    rects = [(k, r) for k, rs in R.items() for r in rs]
    for i in range(len(rects)):
        for j in range(i + 1, len(rects)):
            ov = inter(rects[i][1], rects[j][1])
            assert ov < 1e-6, f"overlap {rects[i][0]} {rects[j][0]} {ov}"
    total = sum(area(k) for k in R)
    assert abs(total - W * D) < 1e-6, f"rooms {total} != shell {W*D}"
    msgs.append(f"geometry: no overlaps; rooms sum {total:.2f} sqm = shell {W*D:.2f} sqm")
    for (a, b, x, y, w, o, sw) in DOORS:
        seg = (x, y, x + w, y) if o == "h" else (x, y, x, y + w)
        for n in (a, b):
            if n.startswith("OUT_"): assert on_shell(seg), f"door {a}-{b} not on shell"
            else: assert on_boundary(n, seg), f"door {a}-{b} not on boundary of {n}"
    for (a, b, x1, y1, x2, y2, kind) in OPENINGS:
        for n in (a, b): assert on_boundary(n, (x1, y1, x2, y2)), f"opening {a}-{b} not on boundary of {n}"
    msgs.append(f"geometry: all {len(DOORS)} doors and {len(OPENINGS)} openings sit on a boundary shared by both rooms")
    return msgs

def graph():
    g = {}
    def add(a, b):
        g.setdefault(a, set()).add(b); g.setdefault(b, set()).add(a)
    for (a, b, *_r) in DOORS: add(a, b)
    for (a, b, *_r) in OPENINGS: add(a, b)
    return g

def bfs_path(g, s, t, banned=frozenset(), allowed=None):
    q = deque([[s]]); seen = {s}
    while q:
        p = q.popleft()
        if p[-1] == t: return p
        for n in sorted(g.get(p[-1], ())):
            if n in seen or n in banned: continue
            if allowed is not None and n not in allowed and n != t: continue
            seen.add(n); q.append(p + [n])
    return None

def check_circulation():
    g = graph(); out = []
    rooms = [k for k in R]
    # entry node = main exterior door
    reach = set(); q = deque(["OUT_MAIN"])
    while q:
        n = q.popleft()
        if n in reach: continue
        reach.add(n); q.extend(g.get(n, ()))
    missing = [k for k in rooms if k not in reach]
    assert not missing, f"unreachable from main entry: {missing}"
    out.append(f"reachability: all {len(rooms)} rooms reachable from the main entry (graph of {len(g)} nodes, {sum(len(v) for v in g.values())//2} connections)")
    def need(label, s, t, banned=DIRTY_ZONE, allowed=None):
        p = bfs_path(g, s, t, banned=banned, allowed=allowed)
        assert p, f"FAIL {label}"
        assert not (set(p) & DIRTY_ZONE), f"FAIL {label} touches dirty zone: {p}"
        out.append(f"PASS {label}: " + " > ".join(p))
        return p
    need("staff room to main entry (no dirty zone)", "staff", "OUT_MAIN")
    need("staff room to collection room 1 (no dirty zone)", "staff", "cr1")
    need("staff room to collection room 2 (no dirty zone)", "staff", "cr2")
    need("staff entry door to staff room (no dirty zone)", "OUT_STAFF", "staff")
    need("lounge to collection room 1 (no dirty zone)", "lounge", "cr1")
    need("lounge to collection room 2 (no dirty zone)", "lounge", "cr2")
    need("main entry to accessible WC (no dirty zone)", "OUT_MAIN", "accwc")
    # waste route: must use back-of-house nodes only (no client area)
    BOH = {"cr1", "cr2", "boh_m", "boh_d", "dirty", "OUT_SVC"}
    for c in ("cr1", "cr2"):
        p = bfs_path(g, c, "OUT_SVC", allowed=BOH)
        assert p and not (set(p) & CLIENT_NODES), f"FAIL waste route {c}"
        out.append(f"PASS clinical waste route from {c} to service door (back-of-house only): " + " > ".join(p))
    p = bfs_path(g, "dirty", "OUT_SVC", allowed=BOH)
    assert p; out.append("PASS dirty room to service door: " + " > ".join(p))
    # every room has a door or opening
    for k in rooms:
        assert g.get(k), f"{k} has no connection"
    # no collection room is reached only through another room
    for c in ("cr1", "cr2"):
        assert len(g[c]) >= 2 and "cr2" not in g[c] and "cr1" not in g[c]
    out.append("PASS collection rooms each have a client-side door (corridor) and a back-of-house door, and neither opens into the other")
    for k in ("m1", "m2", "b1", "b2"):
        assert not ({"m1", "m2", "b1", "b2"} & g[k]), "bays must not connect to each other"
    out.append("PASS massage and beauty bays open onto the lounge or lobby, never through each other")
    # equal collection rooms
    assert abs(area("cr1") - area("cr2")) < 1e-9
    out.append(f"PASS collection rooms equal: {area('cr1'):.2f} sqm and {area('cr2'):.2f} sqm")
    # counter separation
    def dist(k1, k2):
        best = 1e9
        for (a, b, c, d) in R[k1]:
            for (e, f, g_, h) in R[k2]:
                dx = max(e - (a + c), a - (e + g_), 0); dy = max(f - (b + d), b - (f + h), 0)
                best = min(best, (dx * dx + dy * dy) ** 0.5)
        return best
    d_cr = min(dist("counter", "cr1"), dist("counter", "cr2")); d_dirty = dist("counter", "dirty")
    assert d_cr > 3.0 and d_dirty > 8.0
    out.append(f"PASS refreshment counter is {d_cr:.1f} m from the nearest collection room and {d_dirty:.1f} m from the dirty linen / clinical waste room (no shared wall)")
    return out

# ---------------------------------------------------------------- drawing helpers
out = []
def a(s): out.append(s)
def X(m): return OX + m * S
def Y(m): return OY + m * S

def rect(x, y, w, h, fill, stroke=WALL, sw=2.2, extra=""):
    a(f'<rect x="{X(x):.1f}" y="{Y(y):.1f}" width="{w*S:.1f}" height="{h*S:.1f}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" {extra}/>')

def line(x1, y1, x2, y2, stroke=WALL, sw=2.2, dash=None, cap="butt", op=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    o = f' opacity="{op}"' if op else ""
    a(f'<line x1="{X(x1):.1f}" y1="{Y(y1):.1f}" x2="{X(x2):.1f}" y2="{Y(y2):.1f}" stroke="{stroke}" stroke-width="{sw}"{d}{o} stroke-linecap="{cap}"/>')

def text(x, y, s, size=11, weight="400", fill=INK, anchor="middle", px=False, style=""):
    xx, yy = (x, y) if px else (X(x), Y(y))
    a(f'<text x="{xx:.1f}" y="{yy:.1f}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" {style}>{html.escape(s)}</text>')

def vtext(x, y, s, size=8, weight="400", fill=INK):
    a(f'<text transform="translate({X(x):.1f},{Y(y):.1f}) rotate(-90)" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="middle">{html.escape(s)}</text>')

def gap(x1, y1, x2, y2, w=6):
    a(f'<line x1="{X(x1):.1f}" y1="{Y(y1):.1f}" x2="{X(x2):.1f}" y2="{Y(y2):.1f}" stroke="{BG}" stroke-width="{w}" />')

def door(x, y, w, orient, swing):
    if orient == "h":
        gap(x, y, x + w, y)
        if swing:
            yy = y + swing * w
            a(f'<path d="M {X(x):.1f} {Y(y):.1f} L {X(x):.1f} {Y(yy):.1f} A {w*S:.1f} {w*S:.1f} 0 0 {1 if swing<0 else 0} {X(x+w):.1f} {Y(y):.1f}" fill="none" stroke="{MUTE}" stroke-width="1"/>')
    else:
        gap(x, y, x, y + w)
        if swing:
            xx = x + swing * w
            a(f'<path d="M {X(x):.1f} {Y(y):.1f} L {X(xx):.1f} {Y(y):.1f} A {w*S:.1f} {w*S:.1f} 0 0 {1 if swing>0 else 0} {X(x):.1f} {Y(y+w):.1f}" fill="none" stroke="{MUTE}" stroke-width="1"/>')

def basin(x, y, w=0.55, h=0.42):
    a(f'<rect x="{X(x):.1f}" y="{Y(y):.1f}" width="{w*S:.1f}" height="{h*S:.1f}" rx="4" fill="#fff" stroke="{BLUE}" stroke-width="1.4"/>')
    a(f'<circle cx="{X(x+w/2):.1f}" cy="{Y(y+h/2):.1f}" r="{h*S*0.28:.1f}" fill="none" stroke="{BLUE}" stroke-width="1.2"/>')

def item(x, y, w, h, fill="#fff", stroke=MUTE, rx=3, sw=1.1, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    a(f'<rect x="{X(x):.1f}" y="{Y(y):.1f}" width="{w*S:.1f}" height="{h*S:.1f}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>')

def circ(x, y, r, fill="#fff", stroke=MUTE, sw=1.1):
    a(f'<circle cx="{X(x):.1f}" cy="{Y(y):.1f}" r="{r*S:.1f}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')

def arrow_path(pts, color, sw=2.0, dash="6 4", op=0.9):
    d = "M " + " L ".join(f"{X(px):.1f} {Y(py):.1f}" for px, py in pts)
    a(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{sw}" stroke-dasharray="{dash}" opacity="{op}" stroke-linejoin="round"/>')
    (x1, y1), (x2, y2) = pts[-2], pts[-1]
    import math
    ang = math.atan2((Y(y2) - Y(y1)), (X(x2) - X(x1)))
    L = 9
    for da in (2.6, -2.6):
        a(f'<line x1="{X(x2):.1f}" y1="{Y(y2):.1f}" x2="{X(x2)+L*math.cos(ang+da):.1f}" y2="{Y(y2)+L*math.sin(ang+da):.1f}" stroke="{color}" stroke-width="{sw}" opacity="{op}"/>')

def fill_room(k, key):
    for (x, y, w, h) in R[k]:
        a(f'<rect x="{X(x):.1f}" y="{Y(y):.1f}" width="{w*S:.1f}" height="{h*S:.1f}" fill="{FILL[key]}" stroke="none"/>')

def wall_room(k, sw=3.0):
    for (x, y, w, h) in R[k]:
        a(f'<rect x="{X(x):.1f}" y="{Y(y):.1f}" width="{w*S:.1f}" height="{h*S:.1f}" fill="none" stroke="{WALL}" stroke-width="{sw}" stroke-linejoin="miter"/>')

def label2(x, y, name, sqm, size=10.5, color=INK):
    text(x, y, name, size, "700", color)
    text(x, y + 0.34, f"{sqm:.1f} sqm", size - 2, "400", MUTE)

# ---------------------------------------------------------------- build
def build():
    assert not out
    a(f'<svg xmlns="http://www.w3.org/2000/svg" width="{CANVAS_W}" height="{CANVAS_H}" viewBox="0 0 {CANVAS_W} {CANVAS_H}" font-family="Helvetica, Arial, \'Noto Sans\', \'DejaVu Sans\', sans-serif">')
    a(f'<rect width="{CANVAS_W}" height="{CANVAS_H}" fill="{BG}"/>')
    text(70, 70, "GTT CENTER PERTH", 15, "700", GOLD, "start", px=True, style='letter-spacing="3"')
    text(70, 112, "Concept Floor Plan and Layout Schematic, version 2", 34, "700", INK, "start", px=True)
    text(70, 142, "Option A shown: two equal blood collection rooms, each with its own specimen fridge. Option B (one large room with clinical privacy curtain) is in the inset.", 14, "400", MUTE, "start", px=True)
    text(70, 168, f"Typical rectangle {W} m x {D} m = {W*D:.1f} sqm gross internal. Site Brief range about 257 to 290 sqm. Scale 1:100 at A1 (see scale bar).", 14, "400", INK, "start", px=True)
    a(f'<rect x="70" y="190" width="1700" height="2" fill="{GOLD}" opacity="0.6"/>')
    a(f'<rect x="1050" y="40" width="720" height="48" rx="6" fill="#fff" stroke="{RED}" stroke-width="2"/>')
    text(1410, 61, "CONCEPT ONLY. NOT FOR CONSTRUCTION.", 15, "700", RED, "middle", px=True)
    text(1410, 80, "Subject to site survey, architect and NCC compliance.", 13, "400", RED, "middle", px=True)
    a(f'<rect x="{X(0)-6:.1f}" y="{Y(0)-6:.1f}" width="{W*S+12:.1f}" height="{D*S+12:.1f}" fill="none" stroke="{WALL}" stroke-width="1" opacity="0.35"/>')

    # fills
    fmap = {"dirty": "waste", "clean": "store", "boh_d": "waste", "boh_m": "circ", "cr1": "clinical", "cr2": "clinical",
            "staff": "staff", "storage": "store", "accwc": "wc", "stdwc": "wc", "gallery": "circ", "m1": "bay", "m2": "bay",
            "b1": "bay", "b2": "bay", "lounge": "lounge", "counter": "counter", "lobby": "circ", "recep": "reception",
            "hair": "hair", "nails": "nail"}
    for k, f in fmap.items(): fill_room(k, f)

    # open-plan dotted boundaries (drawn first, walls over them)
    for (n1, n2, x1, y1, x2, y2, kind) in OPENINGS:
        if kind == "open": line(x1, y1, x2, y2, MUTE, 1.3, "3 5")
    line(0, 5.2, 18.5, 5.2, MUTE, 0.8, "2 6", op=0.0)

    # solid walls
    for k in ("dirty", "clean", "cr1", "cr2", "staff", "storage", "accwc", "stdwc", "counter", "boh_d", "boh_m"):
        wall_room(k, 3.0 if k not in ("boh_d", "boh_m") else 2.0)
    # bays: walls on north, south, west; curtain on east
    for k in ("m1", "m2", "b1", "b2"):
        (x, y, w, h), = R[k]
        line(x, y, x + w, y, WALL, 3.0); line(x, y + h, x + w, y + h, WALL, 3.0); line(x, y, x, y + h, WALL, 3.0)
    # reception east wall (against nails, fumes) and reception south
    line(13.3, 12.9, 13.3, 15.6, WALL, 3.0)
    # hair / nails: east wall + nails north-west wall segment
    # mirror wall along north edge of hair
    line(13.4, 6.82, 18.45, 6.82, "#7FAFC7", 5.0, cap="round")
    text(15.95, 6.64, "mirror wall (free-standing, 1.8 m)", 8, "400", BLUE)
    # shell
    line(0, 0, W, 0, WALL, 5.5); line(W, 0, W, D, WALL, 5.5); line(W, D, 0, D, WALL, 5.5); line(0, D, 0, 0, WALL, 5.5)
    # curtains on bay openings
    for (n1, n2, x1, y1, x2, y2, kind) in OPENINGS:
        if kind == "curtain": line(x1, y1 + 0.04, x2, y2 - 0.04, GOLD, 2.6, "7 4")

    # doors
    for (n1, n2, x, y, w, o, sw) in DOORS:
        door(x, y, w, o, sw)
    # main entry marker (sliding double door)
    a(f'<line x1="{X(5.4):.1f}" y1="{Y(15.6):.1f}" x2="{X(7.2):.1f}" y2="{Y(15.6):.1f}" stroke="{GOLD}" stroke-width="4"/>')
    text(6.3, 16.2, "MAIN ENTRY", 11, "700", GOLD)
    # service and staff exterior markers
    a(f'<line x1="{X(0):.1f}" y1="{Y(0.1):.1f}" x2="{X(0):.1f}" y2="{Y(1.1):.1f}" stroke="{RED}" stroke-width="4"/>')
    a(f'<text x="{X(0)-8:.1f}" y="{Y(0.65):.1f}" font-size="9" font-weight="700" fill="{RED}" text-anchor="end">service</text><text x="{X(0)-8:.1f}" y="{Y(0.65)+11:.1f}" font-size="9" font-weight="700" fill="{RED}" text-anchor="end">door</text>')
    a(f'<line x1="{X(10.4):.1f}" y1="{Y(0):.1f}" x2="{X(11.4):.1f}" y2="{Y(0):.1f}" stroke="{GREEN}" stroke-width="4"/>')
    text(10.9, -0.2, "staff entry", 9, "700", GREEN)
    # shopfront glazing
    line(0.3, 15.6, 5.2, 15.6, BLUE, 1.4); line(7.3, 15.6, 13.2, 15.6, BLUE, 1.4)
    text(14.9, 16.2, "shopfront glazing (assumed)", 9, "400", MUTE)

    # ---- labels + furniture
    # dirty zone
    text(1.05, 1.85, "Dirty linen /", 8.5, "700", RED); text(1.05, 2.15, "clinical waste", 8.5, "700", RED); text(1.05, 2.5, f"{area('dirty'):.1f} sqm", 7.5, "400", MUTE)
    item(2.05, 1.4, 0.4, 0.4, "#F3D36B", MUTE, rx=2); item(2.05, 1.95, 0.4, 0.4, "#D95F4B", MUTE, rx=2)
    text(1.3, 3.4, "Clean linen", 9, "700"); text(1.3, 3.72, "+ shelving", 8, "400", MUTE); text(1.3, 4.0, f"{area('clean'):.1f} sqm", 7.5, "400", MUTE)
    text(6.4, 0.69, "back-of-house corridor, staff and service only, 1.2 m", 7.5, "400", MUTE)

    # collection rooms
    for k, ox_ in (("cr1", 2.6), ("cr2", 7.35)):
        oy_ = 1.2; n = k[-1]
        item(ox_ + 1.85, oy_ + 0.08, 2.7, 0.6, "#fff", MUTE)                              # bench
        item(ox_ + 1.95, oy_ + 0.14, 0.55, 0.48, "#fff", INK, dash=(None if k == "cr1" else "3 2")); text(ox_ + 2.22, oy_ + 0.46, "C", 8.5, "700")  # centrifuge
        text(ox_ + 3.0, oy_ + 0.45, "doc. bench", 7.5)                                   # doc bench
        item(ox_ + 3.5, oy_ + 0.14, 0.2, 0.2, "#F3D36B", MUTE, rx=2)                      # sharps
        item(ox_ + 3.8, oy_ + 0.1, 0.72, 0.56, "#fff", RED, sw=1.8)                      # under-counter fridge
        text(ox_ + 4.16, oy_ + 0.45, "fridge", 7.5, "700", RED)
        item(ox_ + 1.9, oy_ + 1.35, 0.85, 1.7, "#fff", INK); text(ox_ + 2.32, oy_ + 2.25, "Chair " + ("A" if n == "1" else "B"), 8)
        circ(ox_ + 3.25, oy_ + 2.2, 0.22)
        item(ox_ + 0.12, oy_ + 1.3, 0.85, 1.85, "#fff", MUTE); vtext(ox_ + 0.58, oy_ + 2.25, "recovery recliner", 7.5)
        basin(ox_ + 4.1, oy_ + 2.95); text(ox_ + 3.85, oy_ + 3.0, "HB", 8, "700", BLUE)
        label2(ox_ + 1.8, oy_ + 3.6, f"Blood Collection Room {n}", area(k), 9.5)
    # staff room
    item(12.45, 1.9, 1.2, 0.9, "#fff"); circ(12.6, 1.75, 0.11); circ(13.5, 1.75, 0.11); circ(12.6, 2.95, 0.11); circ(13.5, 2.95, 0.11)
    item(14.12, 1.35, 0.38, 3.4, "#E6D7BF", MUTE); vtext(14.31, 3.05, "lockers", 7.5, "400", MUTE)
    pass
    text(13.1, 3.35, "Staff room", 9.5, "700"); text(13.1, 3.65, "+ lockers", 8, "400", MUTE); text(13.1, 3.93, f"{area('staff'):.1f} sqm", 7.5, "400", MUTE)
    # storage
    for i in range(3): item(14.9, 0.3 + i * 0.6, 0.0, 0.0)
    item(17.9, 0.2, 0.45, 1.8, "#fff", MUTE); item(15.9, 0.2, 0.4, 0.4, "#fff", MUTE)
    label2(16.7, 1.1, "Storage", area("storage"), 9.5)
    text(16.7, 1.75, "consumables, retail stock", 7.5, "400", MUTE)
    # WCs
    circ(16.45, 2.85, 0.2); basin(14.75, 2.3, 0.45, 0.35)
    line(14.65, 4.1, 14.65, 3.2, BLUE, 1.2); line(15.4, 2.28, 16.1, 2.28, BLUE, 1.2)
    text(15.8, 4.5, "Accessible WC", 8.5, "700"); text(15.8, 4.8, f"{area('accwc'):.1f} sqm", 7.5, "400", MUTE)
    circ(18.0, 2.75, 0.2); basin(17.2, 3.7, 0.4, 0.3)
    text(17.75, 4.45, "WC", 8.5, "700"); text(17.75, 4.75, f"{area('stdwc'):.1f}", 7.5, "400", MUTE)
    text(2.4, 6.0, "clinical corridor, 1.5 m clear", 9, "400", MUTE)

    # bays
    for k in ("m1", "m2", "b1", "b2"):
        (x, y, w, h), = R[k]
        n = NAMES[k]
        item(1.35, y + 0.62, 1.95, 0.75, "#fff", INK); text(2.33, y + 1.08, "bed", 8)
        circ(0.9, y + 1.0, 0.17)
        basin(0.1, y + 0.15)
        if k.startswith("b"):
            a(f'<rect x="{X(0.1):.1f}" y="{Y(y+1.15):.1f}" width="{0.5*S:.1f}" height="{0.4*S:.1f}" rx="4" fill="#fff" stroke="{BLUE}" stroke-width="1.4"/>')
            text(0.35, y + 1.43, "IS", 7.5, "700", BLUE)
        text(3.95, y + 0.78, n, 9.5, "700"); text(3.95, y + 1.1, f"{area(k):.1f} sqm", 8, "400", MUTE)
        text(3.95, y + 1.5, "curtain", 7.5, "400", GOLD)
    # lounge
    def couch(x, y, w=1.9, h=0.85):
        item(x, y, w, h, "#fff", MUTE, rx=7); item(x + 0.05, y + 0.05, w - 0.1, 0.22, "#EBDDC8", MUTE, rx=5, sw=0.6)
    couch(5.8, 7.55); couch(8.0, 7.55); couch(5.8, 10.55); couch(8.0, 10.55)
    item(5.85, 9.15, 0.5, 0.5, "#fff", MUTE, rx=25)
    item(11.2, 7.1, 0.9, 0.9, "#fff", MUTE, rx=40); circ(10.55, 7.55, 0.22); circ(12.4, 7.5, 0.22)
    circ(12.6, 12.35, 0.28, "#DCE7D3", "#7F9A6F", 1.2)
    for (px_, py_) in [(7.6, 8.5), (9.0, 8.7)]: circ(px_, py_, 0.13, "#F6E7BE", GOLD, 1)
    text(8.4, 9.3, "Open-plan luxury lounge", 11, "700"); text(8.4, 9.62, f"{area('lounge'):.1f} sqm", 9, "400", MUTE)
    text(8.4, 9.9, "seating for 8+, TV, natural light", 7.5, "400", MUTE)
    # counter
    item(10.3, 8.95, 2.9, 0.45, "#fff", INK); text(11.75, 9.28, "bench", 7.5)
    basin(12.55, 10.6, 0.5, 0.4); item(10.35, 10.55, 0.7, 0.55, "#fff", MUTE); text(10.7, 10.9, "mini fridge", 6)
    item(11.2, 10.6, 0.6, 0.5, "#fff", MUTE); text(11.5, 10.92, "coffee", 7)
    text(11.65, 9.75, "Private Refreshment", 8.5, "700"); text(11.65, 10.05, "Counter (GTT clients)", 8, "700"); text(11.65, 10.28, f"{area('counter'):.1f} sqm", 7.5, "400", MUTE)
    # lobby + reception
    text(5.65, 14.0, "Arrival", 9, "700"); text(5.65, 14.28, "lobby", 9, "700"); text(5.65, 14.58, f"{area('lobby'):.1f} sqm", 7.5, "400", MUTE)
    item(8.1, 13.3, 3.6, 0.62, "#fff", INK); text(9.9, 13.67, "desk, 2 POS", 8.5)
    item(12.85, 13.2, 0.3, 1.9, "#E6D7BF", MUTE)
    label2(10.4, 14.65, "Reception", area("recep"), 11)
    # hair
    for i in range(4):
        circ(13.98 + i * 1.3, 7.55, 0.32, "#fff", INK)
    for i in range(2):
        bx = 14.0 + i * 2.75
        item(bx, 10.1, 1.1, 0.9, "#fff", BLUE, rx=14); text(bx + 0.55, 10.62, "backwash", 7.5, "400", BLUE)
    label2(15.9, 8.85, "Hairdressing (open plan)", area("hair"), 10.5)
    text(15.9, 9.55, "4 chairs, 2 backwash", 8, "400", MUTE)
    # nails
    for i in range(4):
        nx = 13.55 + i * 1.28
        item(nx, 11.65, 1.0, 0.55, "#fff", INK); circ(nx + 0.5, 12.5, 0.17)
        item(nx, 14.35, 0.95, 0.95, "#fff", MUTE, rx=10)
    label2(15.9, 13.2, "Nails + pedicure (open plan)", area("nails"), 10.5)
    text(15.9, 13.92, "4 stations, 4 pedicure chairs", 8, "400", MUTE)
    # LEV
    a(f'<path d="M {X(18.5)-2:.1f} {Y(12.2):.1f} L {X(18.5)+34:.1f} {Y(12.2):.1f}" stroke="{RED}" stroke-width="3"/>')
    a(f'<path d="M {X(18.5)+26:.1f} {Y(12.2)-6:.1f} L {X(18.5)+36:.1f} {Y(12.2):.1f} L {X(18.5)+26:.1f} {Y(12.2)+6:.1f}" fill="none" stroke="{RED}" stroke-width="2.5"/>')
    text(18.5 + 0.9, 12.55, "LEV exhaust", 9, "700", RED, "start"); text(18.5 + 0.9, 12.82, "to outside", 9, "400", RED, "start")

    # ---- route overlays
    arrow_path([(6.65, 15.3), (6.65, 13.3), (5.3, 13.3), (5.3, 6.4), (6.1, 6.4), (6.1, 5.4)], BLUE, 2.0, "2 5")
    arrow_path([(6.1, 6.4), (10.85, 6.4), (10.85, 5.4)], BLUE, 2.0, "2 5")
    arrow_path([(13.25, 5.4), (13.25, 6.05), (9.95, 6.05), (9.95, 12.45), (7.0, 12.45), (7.0, 15.2)], GREEN, 2.0, "6 4")
    arrow_path([(12.15, 0.85), (3.55, 0.85), (3.55, 1.25)], GREEN, 2.0, "6 4")
    arrow_path([(8.3, 0.85), (8.3, 1.25)], GREEN, 2.0, "6 4")
    arrow_path([(8.8, 1.3), (8.8, 0.4), (4.05, 0.4), (0.25, 0.4)], RED, 2.0, "4 3")
    arrow_path([(4.05, 1.3), (4.05, 0.4)], RED, 2.0, "4 3")
    arrow_path([(1.25, 0.4), (1.25, 1.25)], RED, 2.0, "4 3")
    arrow_path([(10.9, -0.1), (10.9, 0.8)], GREEN, 2.0, "6 4")

    # dimensions
    def dim_h(x1, x2, y, s):
        line(x1, y, x2, y, MUTE, 1); line(x1, y - 0.12, x1, y + 0.12, MUTE, 1); line(x2, y - 0.12, x2, y + 0.12, MUTE, 1)
        text((x1 + x2) / 2, y - 0.2, s, 10.5, "700", MUTE)
    def dim_v(x, y1, y2, s):
        line(x, y1, x, y2, MUTE, 1); line(x - 0.12, y1, x + 0.12, y1, MUTE, 1); line(x - 0.12, y2, x + 0.12, y2, MUTE, 1)
        a(f'<text transform="translate({X(x)-8:.1f},{Y((y1+y2)/2):.1f}) rotate(-90)" font-size="10.5" font-weight="700" fill="{MUTE}" text-anchor="middle">{s}</text>')
    dim_h(0, W, -0.7, f"{W} m"); dim_v(-1.5, 0, D, f"{D} m")

    # north arrow placeholder + scale bar
    nx, ny = X(W) - 60, Y(D) + 95
    a(f'<g transform="translate({nx:.1f},{ny:.1f})"><circle r="26" fill="#fff" stroke="{INK}" stroke-width="1.5"/><path d="M0 -20 L8 10 L0 5 L-8 10 Z" fill="{INK}"/><text y="-30" font-size="14" font-weight="700" text-anchor="middle" fill="{INK}">N</text><text y="44" font-size="8.5" text-anchor="middle" fill="{MUTE}">placeholder, true</text><text y="55" font-size="8.5" text-anchor="middle" fill="{MUTE}">north per site</text></g>')
    sx, sy = X(0), Y(D) + 62
    a('<g>' + "".join(f'<rect x="{sx+i*S:.1f}" y="{sy:.1f}" width="{S:.1f}" height="8" fill="{INK if i%2==0 else "#fff"}" stroke="{INK}"/>' for i in range(5)) + '</g>')
    for i in range(6): a(f'<text x="{sx+i*S:.1f}" y="{sy+24:.1f}" font-size="10" text-anchor="middle" fill="{INK}">{i}</text>')
    a(f'<text x="{sx+5*S+14:.1f}" y="{sy+24:.1f}" font-size="10" fill="{INK}">metres</text>')
    text(sx, sy - 8, "Scale bar", 10, "700", INK, "start", px=True)

    # routes key under the plan
    ky = Y(D) + 140
    text(70, ky, "CIRCULATION ROUTES", 13, "700", GOLD, "start", px=True, style='letter-spacing="2"')
    keys = [(BLUE, "2 5", "Client route: entry, lounge, clinical corridor, collection room door"),
            (GREEN, "6 4", "Staff route: staff entry and staff room to clinical and back-of-house corridors"),
            (RED, "4 3", "Dirty route: clinical waste and soiled linen to the service door (staff only)")]
    for i, (c, d, t) in enumerate(keys):
        yy = ky + 22 + i * 22
        a(f'<line x1="70" y1="{yy-4}" x2="104" y2="{yy-4}" stroke="{c}" stroke-width="2.4" stroke-dasharray="{d}"/>')
        text(114, yy, t, 11.5, "400", INK, "start", px=True)
    text(70, ky + 22 + 3 * 22 + 4, "Staff reach the staff room from the clinical corridor or the back-of-house corridor, never through the dirty zone (red tint).", 11, "400", MUTE, "start", px=True)

    # ---- right panel legend
    PX = 1030
    text(PX, 262, "LEGEND", 14, "700", GOLD, "start", px=True, style='letter-spacing="2"')
    leg = [("clinical", "Blood collection (solid walls)"), ("waste", "Dirty zone: service entry, clinical waste, dirty linen"),
           ("bay", "Massage / beauty bay (partition walls + curtain)"), ("lounge", "Open-plan lounge / open plan zones"),
           ("counter", "Private Refreshment Counter (GTT clients only)"), ("reception", "Reception"),
           ("staff", "Staff room"), ("store", "Storage and clean linen"), ("wc", "Toilets (accessible + standard)"), ("circ", "Circulation")]
    for i, (k, n) in enumerate(leg):
        col = i // 5; row = i % 5
        lx = PX + col * 420; ly = 280 + row * 26
        a(f'<rect x="{lx}" y="{ly}" width="26" height="16" fill="{FILL[k]}" stroke="{WALL}" stroke-width="1.2"/>')
        text(lx + 36, ly + 13, n, 12, "400", INK, "start", px=True)
    ly = 280 + 5 * 26 + 6
    a(f'<line x1="{PX}" y1="{ly+8}" x2="{PX+26}" y2="{ly+8}" stroke="{GOLD}" stroke-width="2.4" stroke-dasharray="7 4"/>'); text(PX + 36, ly + 12, "Privacy curtain track", 12, "400", INK, "start", px=True)
    a(f'<rect x="{PX+210}" y="{ly}" width="22" height="16" rx="4" fill="#fff" stroke="{BLUE}" stroke-width="1.4"/><circle cx="{PX+221}" cy="{ly+8}" r="3.5" fill="none" stroke="{BLUE}" stroke-width="1.2"/>'); text(PX + 242, ly + 12, "HB handwash basin (IS = instrument sink)", 12, "400", INK, "start", px=True)
    a(f'<line x1="{PX}" y1="{ly+34}" x2="{PX+26}" y2="{ly+34}" stroke="{WALL}" stroke-width="3.2"/>'); text(PX + 36, ly + 38, "Solid partition wall", 12, "400", INK, "start", px=True)
    a(f'<line x1="{PX+210}" y1="{ly+34}" x2="{PX+236}" y2="{ly+34}" stroke="{MUTE}" stroke-width="1.4" stroke-dasharray="3 5"/>'); text(PX + 246, ly + 38, "Open-plan boundary (no wall)", 12, "400", INK, "start", px=True)
    a(f'<line x1="{PX}" y1="{ly+60}" x2="{PX+26}" y2="{ly+60}" stroke="{RED}" stroke-width="3"/>'); text(PX + 36, ly + 64, "LEV exhaust to outside (nails)", 12, "400", INK, "start", px=True)
    a(f'<rect x="{PX+210}" y="{ly+52}" width="22" height="16" fill="#fff" stroke="{RED}" stroke-width="1.8"/>'); text(PX + 242, ly + 64, "Under-counter clinical specimen fridge", 12, "400", INK, "start", px=True)
    text(PX, ly + 92, "C = centrifuge. Dashed C in Room 2 = space kept for a second unit (quantity TO CONFIRM with the pathology partner).", 11, "400", MUTE, "start", px=True)

    # ---- area schedule
    ty = 575
    text(PX, ty - 10, "AREA SCHEDULE (drawn sqm against reference target)", 14, "700", GOLD, "start", px=True, style='letter-spacing="2"')
    circ_area = area("gallery") + area("boh_m") + area("lobby")
    rows = [
        ("Blood Collection Room 1", f"{area('cr1'):.1f}", "19 (mid of 18 to 20)", "Pathology partner brief; venue room schedule"),
        ("Blood Collection Room 2", f"{area('cr2'):.1f}", "19 (equal to Room 1)", "Venue room schedule; AusHFG room 12 min"),
        ("Massage 1 and 2", f"{area('m1'):.1f} each", "12 each", "Venue room schedule"),
        ("Beauty 1 and 2", f"{area('b1'):.1f} each", "11 each", "Venue room schedule"),
        ("Open-plan luxury lounge", f"{area('lounge'):.1f}", "35", "Venue room schedule (exceeded)"),
        ("Private Refreshment Counter", f"{area('counter'):.1f}", "8", "Venue room schedule"),
        ("Reception", f"{area('recep'):.1f}", "15", "Venue room schedule"),
        ("Hairdressing (4 chairs, 2 backwash)", f"{area('hair'):.1f}", "20 to 24 (5 to 6 per chair)", "Brief 2026-10-17; salon sizing guides"),
        ("Nails + pedicure (4 stations)", f"{area('nails'):.1f}", "20 to 24 (5 to 6 per station)", "Brief 2026-10-17; salon sizing guides"),
        ("Accessible WC", f"{area('accwc'):.1f}", "7", "Venue room schedule"),
        ("Standard WC", f"{area('stdwc'):.1f}", "4", "Venue room schedule"),
        ("Staff room + lockers", f"{area('staff'):.1f}", "10", "Venue room schedule"),
        ("Clean linen", f"{area('clean'):.1f}", "6", "Venue room schedule"),
        ("Dirty linen / clinical waste", f"{area('dirty'):.1f}", "4", "Venue room schedule"),
        ("Storage (consumables, retail stock)", f"{area('storage'):.1f}", "not separately scheduled", "Procurement list: shelving items"),
        ("Service entry (dirty route)", f"{area('boh_d'):.1f}", "not separately scheduled", "New in v2"),
        ("Circulation (clinical corridor, staff corridor, arrival lobby)", f"{circ_area:.1f}", "16", "Venue room schedule (corridor only)"),
    ]
    # header
    a(f'<rect x="{PX-8}" y="{ty}" width="760" height="24" fill="{INK}"/>')
    text(PX, ty + 17, "Zone", 11.5, "700", "#fff", "start", px=True); text(PX + 330, ty + 17, "Drawn", 11.5, "700", "#fff", "end", px=True)
    text(PX + 342, ty + 17, "Reference target", 11.5, "700", "#fff", "start", px=True); text(PX + 505, ty + 17, "Source of target", 11.5, "700", "#fff", "start", px=True)
    yy = ty + 24
    tot = 0.0
    for i, (n, d_, tgt, src) in enumerate(rows):
        a(f'<rect x="{PX-8}" y="{yy}" width="760" height="21" fill="{"#fff" if i%2==0 else "#F3EDE3"}"/>')
        text(PX, yy + 15, n, 11, "400", INK, "start", px=True)
        text(PX + 330, yy + 15, d_, 11, "700", INK, "end", px=True)
        text(PX + 342, yy + 15, tgt, 10, "400", MUTE, "start", px=True)
        text(PX + 505, yy + 15, src, 9, "400", MUTE, "start", px=True)
        yy += 21
    a(f'<rect x="{PX-8}" y="{yy}" width="760" height="24" fill="{GOLD}"/>')
    all_area = sum(area(k) for k in R)
    text(PX, yy + 17, f"Total gross internal ({W} m x {D} m)", 12, "700", "#fff", "start", px=True)
    text(PX + 330, yy + 17, f"{all_area:.1f}", 12, "700", "#fff", "end", px=True)
    text(PX + 342, yy + 17, "257 to 290 range", 11.5, "700", "#fff", "start", px=True)
    yy += 38
    for n in ("Both collection rooms are drawn at 19.0 sqm, the middle of the pathology partner brief range of 18 to 20 sqm (the 9 sqm figure is the partner's",
              "minimum floor, and AusHFG shows 12 sqm for a single enclosed collection room). Each room carries its own specimen fridge, handwash basin, bench,",
              "chair, recovery recliner and documentation bench. Hair and nails are drawn at 5 to 6 sqm per station. All areas are indicative."):
        text(PX, yy, n, 10, "400", MUTE, "start", px=True); yy += 14

    # ---- Option B inset
    IX, IY, IS_ = PX, 1125, 34.0
    text(IX, IY - 40, "OPTION B INSET: ONE LARGE COLLECTION ROOM WITH CLINICAL PRIVACY CURTAIN", 13, "700", GOLD, "start", px=True, style='letter-spacing="1"')
    def ix(m): return IX + m * IS_
    def iy(m): return IY + m * IS_
    a(f'<rect x="{ix(0):.1f}" y="{iy(0):.1f}" width="{9.5*IS_:.1f}" height="{4.0*IS_:.1f}" fill="{FILL["clinical"]}" stroke="{WALL}" stroke-width="3"/>')
    a(f'<line x1="{ix(4.75):.1f}" y1="{iy(0.1):.1f}" x2="{ix(4.75):.1f}" y2="{iy(3.9):.1f}" stroke="{GOLD}" stroke-width="3.2" stroke-dasharray="8 4"/>')
    a(f'<text x="{ix(4.75):.1f}" y="{iy(-0.2):.1f}" font-size="10" font-weight="700" fill="{GOLD}" text-anchor="middle">clinical privacy curtain (ceiling track, floor to ceiling)</text>')
    for k, o in enumerate((0.0, 4.75)):
        nm = "Chair A" if k == 0 else "Chair B"
        a(f'<rect x="{ix(o+1.85):.1f}" y="{iy(1.35):.1f}" width="{0.85*IS_:.1f}" height="{1.7*IS_:.1f}" rx="3" fill="#fff" stroke="{INK}" stroke-width="1.2"/>')
        a(f'<text x="{ix(o+2.27):.1f}" y="{iy(2.25):.1f}" font-size="8" text-anchor="middle">{nm}</text>')
        a(f'<rect x="{ix(o+1.85):.1f}" y="{iy(0.08):.1f}" width="{2.7*IS_:.1f}" height="{0.6*IS_:.1f}" fill="#fff" stroke="{MUTE}"/>')
        a(f'<rect x="{ix(o+3.8):.1f}" y="{iy(0.1):.1f}" width="{0.72*IS_:.1f}" height="{0.56*IS_:.1f}" fill="#fff" stroke="{RED}" stroke-width="1.6"/>')
        a(f'<text x="{ix(o+4.16):.1f}" y="{iy(0.45):.1f}" font-size="7" font-weight="700" fill="{RED}" text-anchor="middle">fridge</text>')
        a(f'<text x="{ix(o+2.8):.1f}" y="{iy(0.45):.1f}" font-size="7" text-anchor="middle">doc. bench</text>')
        a(f'<rect x="{ix(o+0.12):.1f}" y="{iy(1.3):.1f}" width="{0.85*IS_:.1f}" height="{1.85*IS_:.1f}" rx="3" fill="#fff" stroke="{MUTE}"/>')
        a(f'<text transform="translate({ix(o+0.58):.1f},{iy(2.25):.1f}) rotate(-90)" font-size="7" text-anchor="middle">recliner</text>')
        a(f'<rect x="{ix(o+4.0):.1f}" y="{iy(2.95):.1f}" width="{0.55*IS_:.1f}" height="{0.42*IS_:.1f}" rx="4" fill="#fff" stroke="{BLUE}" stroke-width="1.4"/>')
        a(f'<text x="{ix(o+2.3):.1f}" y="{iy(3.75):.1f}" font-size="10" font-weight="700" text-anchor="middle">Bay {k+1}, 19.0 sqm</text>')
    a(f'<text x="{ix(10.0):.1f}" y="{iy(0.4):.1f}" font-size="11" font-weight="700" fill="{INK}">One room, 38.0 sqm (2 x 19.0)</text>')
    tx = ["Same equal-size logic as Option A: each bay keeps the 19.0 sqm,", "its own under-counter specimen fridge, handwash basin, recovery",
          "recliner and documentation bench; the dividing wall is replaced", "by a full-height clinical curtain on a ceiling track. Doors to",
          "the clinical corridor and the back-of-house corridor are as in", "Option A. Curtain gives visual privacy only. Sound privacy is lower",
          "than two walled rooms (to confirm with the pathology partner)."]
    for i, t in enumerate(tx):
        a(f'<text x="{ix(10.0):.1f}" y="{iy(0.85)+i*14:.1f}" font-size="10" fill="{MUTE}">{html.escape(t)}</text>')

    a(f'<rect x="70" y="{CANVAS_H-42}" width="1700" height="1.5" fill="{GOLD}" opacity="0.6"/>')
    text(70, CANVAS_H - 18, "Concept only, not for construction; subject to site survey, architect and NCC compliance.   GTT Center Perth.   Drawing date 2026-10-17, version 2.", 12, "700", RED, "start", px=True)
    a('</svg>')

if __name__ == "__main__":
    msgs = check_geometry() + check_circulation()
    for m in msgs: print(m)
    build()
    open(sys.argv[1], "w", encoding="utf-8").write("\n".join(out))
    rows = {k: round(area(k), 2) for k in R}
    print("areas", json.dumps(rows))
    if "--json" in sys.argv:
        jp = sys.argv[sys.argv.index("--json") + 1]
        json.dump({"areas": rows, "checks": msgs, "total": round(sum(rows.values()), 2)}, open(jp, "w"), indent=1)
