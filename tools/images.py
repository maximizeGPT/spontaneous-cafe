#!/usr/bin/env python3
"""Generate responsive variants for every photo in src/assets/img: <name>-{480,800,1200}.jpg and .webp
plus <name>.webp at full size. Originals stay as the 1600-wide fallback. Idempotent."""
import os, sys
from PIL import Image
D = os.path.join(os.path.dirname(__file__), '..', 'src', 'assets', 'img')
WIDTHS = (480, 800, 1200)
made = 0
for f in sorted(os.listdir(D)):
    if not f.endswith('.jpg') or any(f.endswith(f'-{w}.jpg') for w in WIDTHS):
        continue
    base = f[:-4]; src = os.path.join(D, f)
    im = Image.open(src).convert('RGB')
    targets = [(w, os.path.join(D, f'{base}-{w}.jpg'), 'JPEG') for w in WIDTHS if w < im.width]
    targets += [(w, os.path.join(D, f'{base}-{w}.webp'), 'WEBP') for w in WIDTHS if w < im.width]
    targets += [(im.width, os.path.join(D, f'{base}.webp'), 'WEBP')]
    for w, out, fmt in targets:
        if os.path.exists(out) and os.path.getmtime(out) >= os.path.getmtime(src):
            continue
        r = im.copy(); r.thumbnail((w, w * 4), Image.LANCZOS)
        r.save(out, fmt, quality=76, optimize=True, method=6) if fmt == 'WEBP' else r.save(out, fmt, quality=76, optimize=True, progressive=True)
        made += 1
print(f'{made} variants written')
