# -*- coding: utf-8 -*-
from pathlib import Path
from PIL import Image

HUB = Path(r"C:\AndroidStudioProjects\batch20-hubs\fairgocasino")

def compress_jpg(p, max_w=1600, q=78):
    im = Image.open(p).convert("RGB")
    if im.width > max_w:
        h = int(im.height * max_w / im.width)
        im = im.resize((max_w, h), Image.Resampling.LANCZOS)
    im.save(p, "JPEG", quality=q, optimize=True, progressive=True)

def compress_logo():
    p = HUB / "assets" / "brand" / "logo.png"
    im = Image.open(p)
    if im.mode != "RGBA":
        im = im.convert("RGBA")
    im.thumbnail((512, 512), Image.Resampling.LANCZOS)
    im.save(p, "PNG", optimize=True)
    # If still huge, quantize
    if p.stat().st_size > 160_000:
        im = im.convert("P", palette=Image.ADAPTIVE, colors=64)
        im.save(p, "PNG", optimize=True)

def favicons():
    src = Image.open(HUB / "assets" / "brand" / "logo.png").convert("RGBA")
    # gold map on forest green plate for tiny favicons
    def make(size, name, bg=True):
        canvas = Image.new("RGBA", (size, size), (20, 83, 45, 255) if bg else (0, 0, 0, 0))
        mark = src.copy()
        pad = max(2, size // 10)
        mark.thumbnail((size - pad * 2, size - pad * 2), Image.Resampling.LANCZOS)
        x = (size - mark.width) // 2
        y = (size - mark.height) // 2
        canvas.paste(mark, (x, y), mark)
        out = HUB / name
        canvas.save(out, "PNG", optimize=True)
    make(32, "favicon-32x32.png")
    make(48, "favicon-48x48.png")
    make(96, "favicon-96x96.png")
    make(192, "favicon-192x192.png")
    make(180, "apple-touch-icon.png")
    # ico from 32
    Image.open(HUB / "favicon-32x32.png").save(HUB / "favicon.ico", sizes=[(32, 32)])

for p in HUB.rglob("*.jpg"):
    compress_jpg(p)
    print("jpg", p.name, p.stat().st_size)
compress_logo()
print("logo", (HUB / "assets/brand/logo.png").stat().st_size)
favicons()
print("favicons ok")
