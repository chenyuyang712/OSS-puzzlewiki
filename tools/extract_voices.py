#!/usr/bin/env python3
# extract_voices.py -- parse en.subtitles + s-cn.subtitles into per-character Markdown collections.
# Format: headers '::+ name'; markers '= <tag> <time> [dur] [! ref]' PRECEDE their text;
# '++' = director notes (attach to next spoken block); '[' lines skipped.
# CN file mirrors markers; blocks aligned by index per segment.
import re, os, sys
from collections import Counter, defaultdict

BASE = 'C:/Program Files (x86)/Steam/steamapps/common/Order of the Sinking Star/data/strings/subtitles/'
OUT = 'report/voices'

MARKER = re.compile(r'^= ([\w?]+) ([+-]?\d+(?:\.\d+)?)(?:\s+(\d+(?:\.\d+)?))?(?:\s+! (\S+))?\s*$')
HEADER = re.compile(r'^::+ (\S+)\s*$')

def parse(path):
    txt = open(path, encoding='utf-8').read()
    segs = []  # (name, [blocks]) block = {speaker, texts[], notes[], ref}
    cur_name, cur = None, None
    pending_notes = []
    def flush():
        nonlocal cur
        if cur is not None and (cur['texts'] or cur['notes']):
            segs[-1][1].append(cur)
        cur = None
    for line in txt.split('\n'):
        line = line.rstrip('\r')
        h = HEADER.match(line)
        if h:
            if cur_name is not None: flush()
            segs.append((h.group(1), []))
            cur_name = h.group(1)
            pending_notes = []
            continue
        if cur_name is None: continue
        m = MARKER.match(line)
        if m:
            flush()
            cur = {'speaker': m.group(1), 'texts': [], 'notes': pending_notes, 'ref': m.group(4)}
            pending_notes = []
            continue
        s = line.strip()
        if not s: continue
        s = re.sub(r'^\+ instant_duration \d+(?:\.\d+)?\s*', '', s)  # 内联时间指令
        if not s: continue
        if s.startswith('++'):
            pending_notes.append(s[2:].strip())
            continue
        if s.startswith('[') or s.startswith('!'): continue
        if cur is None:
            cur = {'speaker': '_', 'texts': [], 'notes': pending_notes, 'ref': None}
            pending_notes = []
        cur['texts'].append(s)
    if segs: flush()
    return dict(segs), segs

def main():
    en_map, en_order = parse(BASE + 'en.subtitles')
    cn_map, cn_order = parse(BASE + 's-cn.subtitles')
    names = [n for n,_ in en_order] + [n for n,_ in cn_order if n not in en_map]
    # per character: char -> [ (segname, [(spk,en,cn,notes,has_cn)] ) ]
    chars = defaultdict(list)
    mismatch = 0
    for name in names:
        en_blocks = en_map.get(name, [])
        cn_blocks = cn_map.get(name, [])
        has_cn = name in cn_map
        if has_cn and len(en_blocks) != len(cn_blocks): mismatch += 1
        rows = []
        n = max(len(en_blocks), len(cn_blocks))
        for i in range(n):
            eb = en_blocks[i] if i < len(en_blocks) else None
            cb = cn_blocks[i] if i < len(cn_blocks) else None
            spk = (eb or cb)['speaker']
            en_t = ' '.join(eb['texts']) if eb else ''
            cn_t = ' '.join(cb['texts']) if cb else ''
            notes = (eb or cb)['notes']
            if not en_t and not cn_t: continue
            rows.append((spk, en_t, cn_t, notes, has_cn))
            chars[spk].append((name, len(rows)-1, rows))
        # store rows back? simpler: keep per-seg rows in chars entries
    # rebuild chars as spk -> list of (segname, row)
    chars2 = defaultdict(list)
    for name in names:
        en_blocks = en_map.get(name, []); cn_blocks = cn_map.get(name, [])
        has_cn = name in cn_map
        n = max(len(en_blocks), len(cn_blocks))
        for i in range(n):
            eb = en_blocks[i] if i < len(en_blocks) else None
            cb = cn_blocks[i] if i < len(cn_blocks) else None
            spk = (eb or cb)['speaker']
            en_t = ' '.join(eb['texts']) if eb else ''
            cn_t = ' '.join(cb['texts']) if cb else ''
            notes = list((eb or cb)['notes'])
            if not en_t and not cn_t and not notes: continue
            chars2[spk].append({'seg': name, 'en': en_t, 'cn': cn_t, 'notes': notes, 'has_cn': has_cn})
    os.makedirs(OUT, exist_ok=True)
    import json
    json.dump({s: v for s, v in chars2.items()}, open(OUT + '/voices.json', 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    # stats (ascii only for console)
    total_blocks = sum(len(v) for v in chars2.values())
    print('segments EN', len(en_map), 'CN', len(cn_map), 'union', len(names))
    print('block-count mismatches:', mismatch)
    print('total spoken blocks:', total_blocks)
    for spk, v in sorted(chars2.items(), key=lambda kv: -len(kv[1])):
        words = sum(len(r['en'].split()) for r in v)
        print(f'{spk:18s} blocks={len(v):5d} en_words={words:6d} segs={len(set(r["seg"] for r in v))}')

if __name__ == '__main__':
    main()
