# -*- coding: utf-8 -*-
"""
render_svg2.py - human-readable top-down maps: solid shapes + labels + legend.

Key fixes vs v1:
  - terrain drawn as FILLED RECTS from bbox (fd16-18 ext, fd1a-1c / fd21 center)
  - bbox garbage filter (some ext values are 1e18!) -> sane range [0.02, 150]
  - center = position p (99.9% coverage); bbox ctr c only if |c-p| < 50
  - gameplay markers (Sun/Tower/Teleporter/Guy) bigger + text labels
  - grid, scale bar, legend, title
"""
import sys, os, json, math

IN = sys.argv[1] if len(sys.argv) > 1 else 'report/levels_layout.json'
OUTDIR = sys.argv[2] if len(sys.argv) > 2 else 'report/svg2'
MAX_SHAPES = 60000
EXT_MIN, EXT_MAX = 0.02, 150.0

C_FLOOR = '#31506e'   # decal / island floor
C_TERRAIN = '#a89880' # rock / wall / brick
C_OTHER = '#4d7099'
C_SUN = '#ffd54a'
C_TOWER = '#c060ff'
C_TELE = '#35e0ff'
C_GUY = '#ffffff'

def klass(inst):
    n = inst.get('n', '')
    n = ' '.join(n) if isinstance(n, list) else (n or '')
    u = inst.get('u') or ''
    t = (n + ' ' + u).lower()
    if 'editorui_sun' in t or 'sun' in t and len(t) < 30: return 'sun'
    if 'tower' in t: return 'tower'
    if 'teleport' in t: return 'tele'
    if 'guy' in t or 'editorui_guy' in t or 'hero' in t: return 'guy'
    if 'editorui_decal' in t or 'decal' in t: return 'floor'
    if 'rock' in t or 'wall' in t or 'brick' in t or 'arch_' in t or 'isle' in t: return 'terrain'
    return 'other'

def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

def render(name, rec):
    insts = rec.get('instances', [])
    shapes = []      # (z_order, kind, data...)
    stride = max(1, math.ceil(len(insts) / MAX_SHAPES))
    dropped = len(insts) - (len(insts) // stride) * stride
    n_bad = 0
    markers = []
    for inst in insts[::stride]:
        p = inst.get('p')
        if not p:
            continue
        k = klass(inst)
        cx, cy, cz = p
        ext = None
        b = inst.get('b')
        if b and all(EXT_MIN <= abs(v) <= EXT_MAX for v in b):
            c = inst.get('c')
            if c and all(abs(c[i] - p[i]) < 50 for i in range(3)):
                cx, cz = c[0], c[2]
            ext = (abs(b[0]), abs(b[2]))          # x, z half-extents
        w = ext[0] if ext else 0.35
        h = ext[1] if ext else 0.35
        if k in ('sun', 'tower', 'tele', 'guy'):
            markers.append((k, cx, cz, inst.get('u') or ''))
        else:
            zord = 0 if k == 'floor' else 1
            shapes.append((zord, k, cx, cz, w, h, cy))
    shapes.sort(key=lambda s: s[0])
    # world bounds
    allx = [s[2] for s in shapes] + [m[1] for m in markers]
    allz = [s[3] for s in shapes] + [m[2] for m in markers]
    if not allx:
        return None, 0
    x0, x1 = min(allx), max(allx); z0, z1 = min(allz), max(allz)
    W = H = 1100; PAD = 60
    scale = (H - 2*PAD) / max(z1 - z0, x1 - x0, 1e-3)
    def X(x): return PAD + (x - x0) * scale
    def Y(z): return PAD + (z - z0) * scale

    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" font-family="sans-serif">' % (W, H),
           '<rect width="%d" height="%d" fill="#0d1117"/>' % (W, H),
           '<text x="14" y="26" fill="#e6edf3" font-size="20" font-weight="bold">%s</text>' % esc(name),
           '<text x="14" y="48" fill="#8b949e" font-size="13">top-down (x/z) | %s | insts=%s | stride=%s</text>'
           % ('OK' if rec.get('ok') else 'PARTIAL', len(insts), stride)]
    # grid every 10 world units
    gx = math.floor(x0/10)*10
    while gx <= x1:
        out.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="#21262d" stroke-width="1"/>'
                   % (X(gx), PAD, X(gx), H-PAD))
        gx += 10
    gz = math.floor(z0/10)*10
    while gz <= z1:
        out.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="#21262d" stroke-width="1"/>'
                   % (PAD, Y(gz), W-PAD, Y(gz)))
        gz += 10
    # terrain shapes
    for _, k, cx, cz, w, h, cy in shapes:
        col = C_FLOOR if k == 'floor' else (C_TERRAIN if k == 'terrain' else C_OTHER)
        op = 0.55 if k == 'floor' else 0.9
        out.append('<rect x="%.2f" y="%.2f" width="%.2f" height="%.2f" fill="%s" fill-opacity="%s">'
                   '<title>%s y=%.2f</title></rect>'
                   % (X(cx-w), Y(cz-h), max(2*w, 1.2), max(2*h, 1.2), col, op, esc(k), cy))
    # gameplay markers on top
    for k, mx, mz, label in markers[:200]:
        if k == 'sun':
            out.append('<circle cx="%.1f" cy="%.1f" r="6" fill="%s" stroke="#a87b00"><title>%s</title></circle>'
                       % (X(mx), Y(mz), C_SUN, esc(label or 'sun')))
            out.append('<text x="%.1f" y="%.1f" fill="%s" font-size="11">SUN</text>' % (X(mx)+8, Y(mz)+4, C_SUN))
        elif k == 'tower':
            out.append('<rect x="%.1f" y="%.1f" width="10" height="10" fill="%s" transform="rotate(45 %.1f %.1f)">'
                       '<title>%s</title></rect>' % (X(mx)-5, Y(mz)-5, C_TOWER, X(mx), Y(mz), esc(label or 'tower')))
            out.append('<text x="%.1f" y="%.1f" fill="%s" font-size="11">TOWER</text>' % (X(mx)+8, Y(mz)+4, C_TOWER))
        elif k == 'tele':
            out.append('<circle cx="%.1f" cy="%.1f" r="5" fill="none" stroke="%s" stroke-width="2"><title>%s</title></circle>'
                       % (X(mx), Y(mz), C_TELE, esc(label or 'teleporter')))
        else:
            out.append('<circle cx="%.1f" cy="%.1f" r="4" fill="%s"><title>%s</title></circle>'
                       % (X(mx), Y(mz), C_GUY, esc(label or 'guy')))
    # legend + scale bar
    ly = H - 34
    out.append('<rect x="%d" y="%d" width="14" height="10" fill="%s"/><text x="%d" y="%d" fill="#8b949e" font-size="12">island/floor</text>'
               % (PAD, ly-9, C_FLOOR, PAD+20, ly))
    out.append('<rect x="%d" y="%d" width="14" height="10" fill="%s"/><text x="%d" y="%d" fill="#8b949e" font-size="12">rock/wall</text>'
               % (PAD+130, ly-9, C_TERRAIN, PAD+150, ly))
    out.append('<circle cx="%d" cy="%d" r="5" fill="%s"/><text x="%d" y="%d" fill="#8b949e" font-size="12">Sun</text>'
               % (PAD+250, ly-4, C_SUN, PAD+260, ly))
    out.append('<rect x="%d" y="%d" width="8" height="8" fill="%s" transform="rotate(45 %d %d)"/><text x="%d" y="%d" fill="#8b949e" font-size="12">Tower</text>'
               % (PAD+320, ly-8, C_TOWER, PAD+324, ly-4, PAD+340, ly))
    # scale bar: 10 world units
    out.append('<rect x="%d" y="%d" width="%.1f" height="4" fill="#e6edf3"/><text x="%d" y="%d" fill="#e6edf3" font-size="12">10 units</text>'
               % (W-140, ly-6, 10*scale, W-140, ly-12))
    out.append('</svg>')
    return '\n'.join(out), len(shapes) + len(markers)


def main():
    os.makedirs(OUTDIR, exist_ok=True)
    data = json.load(open(IN, encoding='utf-8'))
    total = 0
    n = 0
    for name in sorted(data):
        rec = data[name]
        if 'instances' not in rec:
            continue
        svg, cnt = render(name, rec)
        if svg is None:
            continue
        with open(os.path.join(OUTDIR, name + '.svg'), 'w', encoding='utf-8') as f:
            f.write(svg)
        total += cnt; n += 1
    print(json.dumps(dict(rendered=n, shapes=total)))

if __name__ == '__main__':
    main()
