# -*- coding: utf-8 -*-
"""
build_graph.py v2 - Task 4: difficulty curve & mechanic atlas.

Fix vs v1: catalog 'fingerprint' was SCHEMA attr-counts (identical across all
levels = garbage). Now derives per-level mechanic presence from
levels_layout.json instance data:
  - ref typ ids (88-class registry)  -> direct class evidence
  - instance name/ui strings         -> keyword evidence

Outputs: report/mechanic_atlas.json, report/difficulty_curve.md
"""
import sys, os, json, statistics, struct
from collections import Counter

CASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAT = json.load(open(os.path.join(CASE, 'report', 'levels_catalog.json'), encoding='utf-8'))
LAY = json.load(open(os.path.join(CASE, 'report', 'levels_layout.json'), encoding='utf-8'))

# 88-class registry from any entities header
def type_names():
    d = open(os.path.join(CASE, 'extract', 'levels', 'data-common',
                          '3d_intro_heroes.entities'), 'rb').read()
    off = 22
    names = []
    for _ in range(88):
        (ln,) = struct.unpack_from('<Q', d, off); off += 8
        names.append(d[off:off+ln].decode('ascii')); off += ln
        off += 8
    return names
TNAMES = type_names()
TID = {n: i for i, n in enumerate(TNAMES)}

# mechanic -> (type ids, name keywords)
MECHS = {
    'Mirror':    ([TID['Mirror']], ['mirror']),
    'Rock':      ([TID['Rock']], ['_rock', 'rock_']),
    'Promesst':  ([TID.get('Promesst_Light', -1), TID.get('Promesst_Dark', -1)],
                  ['promesst']),
    'Heroes':    ([TID['Guy']], ['guy', 'hero']),
    'Lily':      ([TID.get('Lily', -1)], ['lily']),
    'Skipping':  ([TID.get('Skippable_Stone', -1), TID.get('Skippable', -1)],
                  ['skipp']),
    'Water':     ([TID.get('Ocean_Map', -1)], ['ocean', 'water', 'boat']),
    'Gems':      ([TID.get('Gem', -1)], ['gem']),
    'Monsters':  ([TID.get('Monster', -1)], ['monster', 'goblin']),
    'Spawner':   ([TID.get('Spawner', -1)], ['spawner']),
    'Elevator':  ([TID.get('Elevator_Platform', -1), TID.get('Elevator', -1)],
                  ['elevator']),
    'Teleport':  ([TID['Teleporter']], ['teleport']),
    'Rover':     ([TID['Rover']], ['rover']),
    'Dragon':    ([TID.get('Friendly_Dragon', -1), TID.get('Baby_Dragon', -1)],
                  ['dragon']),
    'Sun':       ([TID['Sun']], ['editorUI_sun', 'sun_']),
    'Tower':     ([TID.get('Tower', -1)], ['tower']),
}
MECHS = {k: (set(t for t in v[0] if t >= 0), v[1]) for k, v in MECHS.items()}

def level_mech(lid, rec):
    typs = Counter()
    words = Counter()
    for inst in rec.get('instances', []):
        for _, typ, _ in inst.get('r', []):
            typs[typ] += 1
        for key in ('n', 'u', 's'):
            v = inst.get(key)
            if not v:
                continue
            vs = ' '.join(v) if isinstance(v, list) else str(v)
            for w in vs.replace('~', ' ').replace('_', ' ').split():
                words[w.lower()] += 1
    wl = ' '.join(words)
    found = []
    for mech, (ids, kws) in MECHS.items():
        if any(typs[t] for t in ids) or any(k in wl for k in kws):
            found.append(mech)
    return found

# ---- play sequence (level_set DSL order) ----
order = []
for s in CAT['level_sets']:
    for it in s['items']:
        if it['t'] == 'level':
            order.append((s['name'], it['id'], it.get('choice', False)))
seen = set(); seq = []
for sn, lid, ch in order:
    if lid not in seen:
        seen.add(lid); seq.append((sn, lid, ch))

first = {}; co = Counter(); rows = []
for i, (sn, lid, ch) in enumerate(seq):
    rec = LAY.get(lid, {})
    ms = level_mech(lid, rec)
    for m in ms:
        first.setdefault(m, dict(seq_pos=i, level=lid, set=sn))
    for a in range(len(ms)):
        for b in range(a + 1, len(ms)):
            co[tuple(sorted((ms[a], ms[b])))] += 1
    n = rec.get('decl', 0)
    rows.append(dict(seq=i, set=sn, level=lid, choice=ch, instances=n,
                     n_mech=len(ms), mechs=ms))

setstats = {}
for r in rows:
    s = setstats.setdefault(r['set'], dict(n=0, inst=[], mech=[]))
    s['n'] += 1; s['inst'].append(r['instances']); s['mech'].append(r['n_mech'])
for sn, s in setstats.items():
    s['inst_avg'] = round(statistics.mean(s['inst']), 1)
    s['inst_max'] = max(s['inst'])
    s['mech_avg'] = round(statistics.mean(s['mech']), 2)
    del s['inst']; del s['mech']

out = dict(
    n_levels_seq=len(seq),
    mech_first=[dict(mech=m, **first[m]) for m in sorted(first, key=lambda m: first[m]['seq_pos'])],
    co_occurrence=[dict(a=k[0], b=k[1], n=v) for k, v in co.most_common(25)],
    set_stats=[dict(set=k, **v) for k, v in setstats.items()],
    towers=CAT['towers'],
)
with open(os.path.join(CASE, 'report', 'mechanic_atlas.json'), 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=1)

md = []
md.append('# 第六章 难度曲线与机制图谱（静态数据推断）\n')
md.append('数据源：levels_layout.json 实例数据（引用 typ + 名字串）+ level_set DSL 顺序。\n')
md.append('注意：关卡顺序为设计者 set 顺序，非强制游玩顺序；难度代理=实例数与机制多样性。\n')
md.append('\n## 6.1 机制首现（按 set 序）\n')
md.append('| 机制 | 首现序号 | 关卡 | 所属 set |')
md.append('|---|---|---|---|')
for m in sorted(first, key=lambda m: first[m]['seq_pos']):
    f = first[m]
    md.append('| %s | %d | %s | %s |' % (m, f['seq_pos'], f['level'], f['set']))
md.append('\n## 6.2 机制共现 Top25\n')
md.append('| A | B | 同关次数 |')
md.append('|---|---|---|')
for k, v in co.most_common(25):
    md.append('| %s | %s | %d |' % (k[0], k[1], v))
md.append('\n## 6.3 塔（16 座）规模与门槛\n')
md.append('| 区 | 编号 | 关卡数 | 必解/必须 | 要求% | Glyph 门槛 |')
md.append('|---|---|---|---|---|---|')
for t in CAT['towers']:
    md.append('| %s | %d | %d | %d/%d | %d%% | %s |'
              % (t['section'], t['idx'], t['levels'], t['required_solved'],
                 t['required_total'], t['required_pct'], t['glyphs']))
md.append('\n## 6.4 各 set 规模与复杂度 Top25（实例均值=难度代理）\n')
md.append('| set | 关卡数 | 实例均值 | 实例峰值 | 机制类型均值 |')
md.append('|---|---|---|---|---|')
for k, v in sorted(setstats.items(), key=lambda kv: -kv[1]['inst_avg'])[:25]:
    md.append('| %s | %d | %.1f | %d | %.2f |' % (k, v['n'], v['inst_avg'], v['inst_max'], v['mech_avg']))
with open(os.path.join(CASE, 'report', 'difficulty_curve.md'), 'w', encoding='utf-8') as f:
    f.write('\n'.join(md))
print(json.dumps(dict(mech_first=len(out['mech_first']),
                      first=[(m['mech'], m['seq_pos'], m['level']) for m in out['mech_first']][:10],
                      co=len(out['co_occurrence']), sets=len(setstats))))
