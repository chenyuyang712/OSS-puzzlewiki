# -*- coding: utf-8 -*-
"""
build_layout.py - Task 2 deliverable: per-level object layout from .entities files.

Output report/levels_layout.json:
  { "<level>": {
       "decl": N, "found": N, "ok": bool,          # instance count match
       "types": {...},                              # 88-class table from header
       "instances": [ compact dict ... ] }

Compact instance dict:
  n   : non-empty names from fd20 group   (optional)
  p   : [x, y, z] position (fd21/22/23)
  q   : [x,y,z,w] rotation quaternion (fd06..09)
  d   : dims fd01..05
  b   : bbox extent fd16..18
  c   : bbox center fd1a..1c
  u   : editorUI string (fd1f)
  s   : other strings (asset names etc.)
  i   : {field_id: int/tag value}
  r   : [[field_id, type_id, idx], ...] references (val dropped)
  g   : fd20 group size (total strings incl. empty) when >1
"""
import sys, os, json, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import enty_parse


def compact(inst):
    o = {}
    f0 = inst[0] if inst else None
    if f0 is not None and f0['id'] == 0x20 and f0['t'] == 'arr':
        names = [s for s in f0['v'] if s]
        if len(f0['v']) > 1:
            o['g'] = len(f0['v'])
        if names:
            o['n'] = names[0] if len(names) == 1 else names
    p = [enty_parse.fget(inst, x) for x in (0x21, 0x22, 0x23)]
    if any(v is not None for v in p):
        o['p'] = [0.0 if v is None else round(v, 5) for v in p]
    q = [enty_parse.fget(inst, x) for x in (0x06, 0x07, 0x08, 0x09)]
    if all(v is not None for v in q):
        o['q'] = [round(v, 6) for v in q]
    d = [enty_parse.fget(inst, x) for x in (0x01, 0x02, 0x03, 0x04, 0x05)]
    if any(v is not None for v in d):
        o['d'] = [0.0 if v is None else round(v, 5) for v in d]
    b = [enty_parse.fget(inst, x) for x in (0x16, 0x17, 0x18)]
    if any(v is not None for v in b):
        o['b'] = [0.0 if v is None else round(v, 5) for v in b]
    c = [enty_parse.fget(inst, x) for x in (0x1a, 0x1b, 0x1c)]
    if any(v is not None for v in c):
        o['c'] = [0.0 if v is None else round(v, 5) for v in c]
    ui = next((f['v'] for f in inst if f['t'] == 'str' and f['id'] == 0x1f), None)
    if ui:
        o['u'] = ui
    strs = [f['v'] for f in inst if f['t'] == 'str' and f['id'] != 0x1f]
    if strs:
        o['s'] = strs[0] if len(strs) == 1 else strs
    ints = {f['id']: f['v'] for f in inst if f['t'] in ('i', 'tag')}
    if ints:
        o['i'] = ints
    refs = [[f['id'], f['v']['typ'], f['v']['idx']] for f in inst if f['t'] == 'ref']
    if refs:
        o['r'] = refs
    return o


def main():
    lvl_dir = sys.argv[1] if len(sys.argv) > 1 else 'extract/levels/data-common'
    out_path = sys.argv[2] if len(sys.argv) > 2 else 'report/levels_layout.json'
    files = sorted(glob.glob(os.path.join(lvl_dir, '*.entities')))
    result = {}
    stats = dict(files=0, ok=0, partial=0, parse_err=0, instances=0)
    for fp in files:
        name = os.path.basename(fp)[:-len('.entities')]
        try:
            res = enty_parse.parse_enty(fp)
        except Exception as e:
            stats['parse_err'] += 1
            result[name] = dict(error=str(e)[:200])
            continue
        stats['files'] += 1
        ok = (res['n_declared'] == res['n_found'])
        stats['ok' if ok else 'partial'] += 1
        stats['instances'] += res['n_found']
        insts = [compact(i) for i in res['insts']]
        result[name] = dict(decl=res['n_declared'], found=res['n_found'], ok=ok,
                            types=res['names'], instances=insts)
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, separators=(',', ':'))
    print(json.dumps(stats))


if __name__ == '__main__':
    main()
