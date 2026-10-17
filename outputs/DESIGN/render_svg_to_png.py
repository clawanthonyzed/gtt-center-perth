import sys
from playwright.sync_api import sync_playwright
svg, png, scale = sys.argv[1], sys.argv[2], float(sys.argv[3]) if len(sys.argv)>3 else 1.5
w,h = int(sys.argv[4]) if len(sys.argv)>4 else 1840, int(sys.argv[5]) if len(sys.argv)>5 else 1500
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width":w,"height":h}, device_scale_factor=scale)
    pg.goto("file:///"+svg.replace("\\","/")); pg.screenshot(path=png, full_page=False); b.close()
