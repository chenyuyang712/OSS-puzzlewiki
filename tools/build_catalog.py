#!/usr/bin/env python3
"""build_catalog.py - 《沉星之序》关卡目录全书构建器

Inputs:
  extract/levels/{data,data-common,data-pc}/*.entities        (type tables)
  extract/levels/{data,data-common,data-pc}/*.level_manifest  (asset counts)
  extract/levels/data/level_sets/*.level_set                  (DSL: levels/choice/glyphs/comments)
  <game>/data/strings/{s-cn,en}.localization                  (CN/EN names)
  <game>/logs/log_*.txt                                       (16-tower dump)

Outputs:
  report/levels_catalog.json
  report/LEVEL_CATALOG_book.md   (UTF-8, Chinese)
"""
import glob, json, os, re, struct, collections

CASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EX = os.path.join(CASE, 'extract', 'levels')
GAME = r"C:/Program Files (x86)/Steam/steamapps/common/Order of the Sinking Star"
OUT_JSON = os.path.join(CASE, 'report', 'levels_catalog.json')
OUT_MD = os.path.join(CASE, 'report', 'LEVEL_CATALOG_book.md')

# ---------- localization ----------
def load_loc(path):
    out, lines = {}, open(path, encoding='utf-8').read().split('\n')
    i = 0
    while i < len(lines):
        s = lines[i].strip()
        if s.startswith('`'):
            k = s[1:].strip()
            v = lines[i + 1].strip() if i + 1 < len(lines) else ''
            out[k] = v
            i += 2
        else:
            i += 1
    return out

cn = load_loc(os.path.join(GAME, 'data/strings/s-cn.localization'))
en = load_loc(os.path.join(GAME, 'data/strings/en.localization'))

# ---------- level_set DSL ----------
def parse_level_set(fp):
    name = os.path.basename(fp)[:-len('.level_set')]
    items, glyphs = [], []
    for raw in open(fp, encoding='utf-8', errors='replace'):
        line = raw.strip()
        if not line or line.startswith('[1]'):
            continue
        if line.startswith('#'):
            c = line[1:].strip()
            if c:
                items.append({'t': 'note', 'v': c})
            continue
        if line.startswith('*glyphs'):
            glyphs = line.split()[1:]
            items.append({'t': 'glyphs', 'v': glyphs})
            continue
        if line.startswith('*'):
            if line == '*choice' and items:
                for it in reversed(items):
                    if it['t'] == 'level':
                        it['choice'] = True
                        break
            continue
        lid = line.split()[0]
        items.append({'t': 'level', 'id': lid, 'choice': False})
    # collapse consecutive notes
    return {'name': name, 'glyphs': glyphs, 'items': items}

# ---------- entities type table ----------
def parse_entities(fp):
    d = open(fp, 'rb').read()
    if d[:4] != b'enty':
        return None
    ver, = struct.unpack_from('<H', d, 4)
    a, tc = struct.unpack_from('<QQ', d, 6)
    off = 22
    types = {}
    try:
        for _ in range(tc):
            (ln,) = struct.unpack_from('<Q', d, off); off += 8
            nm = d[off:off + ln].decode('latin-1'); off += ln
            (c,) = struct.unpack_from('<Q', d, off); off += 8
            if c:
                types[nm] = c
    except Exception:
        return None
    return {'ver': ver, 'a': a, 'types': types, 'total': sum(types.values()),
            'data_offset': off, 'size': len(d)}

# ---------- level_manifest ----------
def parse_manifest(fp):
    secs, cur = collections.OrderedDict(), None
    n = 0
    for ln in open(fp, encoding='utf-8', errors='replace'):
        s = ln.strip()
        if s.startswith(';;;;;'):
            cur = s.lstrip(';').strip()
            secs[cur] = 0
        elif s and cur:
            secs[cur] += 1
            n += 1
    return {'assets': n, 'sections': dict(secs)}

# ---------- towers from log ----------
def parse_towers():
    log = max(glob.glob(os.path.join(GAME, 'logs', 'log_*.txt')), key=os.path.getmtime)
    txt = open(log, encoding='utf-8', errors='replace').read()
    # only the LAST tower dump (log may contain multiple overworld loads)
    marker = txt.rfind('---- Towers:')
    towers, section = [], None
    for ln in txt[marker:].split('\n'):
        if 'Ground Floor Towers' in ln: section = 'ground'
        elif 'Upstairs Towers' in ln: section = 'upstairs'
        elif 'Downstairs Towers' in ln: section = 'downstairs'
        m = re.match(r'\[(\d+)\] (\d+) levels?: (\d+) normal, (\d+) dropdown; \((\d+)/(\d+) required, (\d+)%\) (.+): Tower #([\d-]+)', ln.strip())
        if m and section:
            g = m.groups()
            towers.append({'section': section, 'idx': int(g[0]), 'levels': int(g[1]),
                           'normal': int(g[2]), 'dropdown': int(g[3]),
                           'required_solved': int(g[4]), 'required_total': int(g[5]),
                           'required_pct': int(g[6]), 'glyphs': g[7].strip(), 'tid': g[8]})
    return towers

# ---------- build ----------
print('parsing level_sets ...')
sets = [parse_level_set(fp) for fp in sorted(glob.glob(os.path.join(EX, 'data', 'level_sets', '*.level_set')))]

print('parsing entities + manifests ...')
levels = {}
for sub in ('data', 'data-common', 'data-pc'):
    for fp in glob.glob(os.path.join(EX, sub, '*.entities')):
        lid = os.path.basename(fp)[:-len('.entities')]
        e = parse_entities(fp)
        if e is None:
            continue
        rec = {'dir': sub, 'entities': e}
        mfp = fp[:-len('.entities')] + '.level_manifest'
        if os.path.exists(mfp):
            rec['manifest'] = parse_manifest(mfp)
        levels[lid] = rec

# reverse index: level -> sets containing it
lvl_sets = collections.defaultdict(list)
for s in sets:
    for it in s['items']:
        if it['t'] == 'level':
            lvl_sets[it['id']].append(s['name'])

# per-set stats
for s in sets:
    slevels = [it['id'] for it in s['items'] if it['t'] == 'level']
    s['level_ids'] = slevels
    s['n_levels'] = len(slevels)
    s['n_choices'] = sum(1 for it in s['items'] if it['t'] == 'level' and it.get('choice'))
    s['cn'] = cn.get('area_g_' + s['name'], '') or cn.get('area_s_' + s['name'], '') or cn.get('area_' + s['name'], '')
    s['en'] = en.get('area_g_' + s['name'], '') or en.get('area_s_' + s['name'], '') or en.get('area_' + s['name'], '')
    known = [l for l in slevels if l in levels]
    s['levels_on_disk'] = len(known)

towers = parse_towers()

# global entity type totals
gtot = collections.Counter()
for lid, rec in levels.items():
    for t, c in rec['entities']['types'].items():
        gtot[t] += c

# mechanic fingerprint per level: gameplay-relevant types
GAMEPLAY_TYPES = ['Guy', 'Rock', 'Lily', 'Mirror', 'Gem', 'Door', 'Gate', 'Teleporter',
                  'Freezer', 'Monster', 'Rover', 'Friendly_Dragon', 'Promesst_Light',
                  'Spawner', 'Switch', 'Activator', 'Boat', 'Elevator_Platform', 'Statue']
for lid, rec in levels.items():
    types = rec['entities']['types']
    rec['fingerprint'] = {t: types[t] for t in GAMEPLAY_TYPES if t in types}
    rec['in_sets'] = lvl_sets.get(lid, [])

catalog = {
    'meta': {
        'game': 'Order of the Sinking Star (沉星之序)',
        'build': 'r66830, 2026-10-08',
        'n_level_sets': len(sets),
        'n_levels_entities': len(levels),
        'n_levels_in_sets': len(set(l for s in sets for l in s['level_ids'])),
        'n_area_names_cn': sum(1 for k in cn if k.startswith('area_')),
        'n_towers': len(towers),
        'entity_types': len(gtot),
    },
    'towers': towers,
    'area_names': [{'key': k, 'cn': cn[k], 'en': en.get(k, '')}
                   for k in sorted(cn) if k.startswith('area_')],
    'heroes': [{'key': k, 'cn': cn[k], 'en': en.get(k, '')}
               for k in sorted(cn) if k.startswith('campaign_name_h_')],
    'mechanics': [{'key': k, 'cn': cn[k], 'en': en.get(k, '')}
                  for k in sorted(cn) if k.startswith('campaign_name_m_')],
    'level_sets': sets,
    'levels': {lid: {'dir': r['dir'],
                     'total_instances': r['entities']['total'],
                     'fingerprint': r['fingerprint'],
                     'assets': r.get('manifest', {}).get('assets', 0),
                     'in_sets': r['in_sets']}
               for lid, r in sorted(levels.items())},
    'global_type_totals': dict(gtot.most_common()),
}
os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
with open(OUT_JSON, 'w', encoding='utf-8') as f:
    json.dump(catalog, f, ensure_ascii=False, indent=1)
print('json ->', OUT_JSON)

# ---------- markdown book ----------
md = []
md.append('# 《沉星之序》关卡目录全书\n')
md.append('> 数据来源：游戏本地 simp 包提取（static, offline）。构建脚本 `tools/build_catalog.py`；'
          '机器可读版 `levels_catalog.json`。所有关卡名/区域名/机制名取自官方简体中文本地化。\n')

md.append('\n## 一、世界结构：16 座塔楼\n')
md.append('| 层区 | # | 关卡数 | 普通/坠落 | 门槛(需解/要求) | 机制组合 | 塔编号 |')
md.append('|---|---|---|---|---|---|---|')
sec_cn = {'ground': '地面层', 'upstairs': '楼上', 'downstairs': '楼下'}
for t in towers:
    md.append(f"| {sec_cn.get(t['section'], t['section'])} | {t['idx']} | {t['levels']} | "
              f"{t['normal']}/{t['dropdown']} | {t['required_solved']}/{t['required_total']} ({t['required_pct']}%) | "
              f"{t['glyphs']} | #{t['tid']} |")

md.append('\n## 二、英雄与机制\n')
md.append('### 英雄（campaign_name_h_*）\n')
md.append('| 键 | 中文 | 英文 |')
md.append('|---|---|---|')
for h in catalog['heroes']:
    md.append(f"| {h['key']} | {h['cn']} | {h['en']} |")
md.append('\n### 机制（campaign_name_m_*）\n')
md.append('| 键 | 中文 | 英文 |')
md.append('|---|---|---|')
for m in catalog['mechanics']:
    md.append(f"| {m['key']} | {m['cn']} | {m['en']} |")

md.append('\n## 三、区域名对照（官方中文）\n')
md.append('| 键 | 中文 | 英文 |')
md.append('|---|---|---|')
for a in catalog['area_names']:
    md.append(f"| {a['key']} | {a['cn']} | {a['en']} |")

md.append('\n## 四、关卡集详解（%d 个 level_set）\n' % len(sets))
for s in sets:
    title = s['name']
    if s['cn']:
        title += f"（{s['cn']} / {s['en']}）" if s['en'] else f"（{s['cn']}）"
    md.append(f"\n### {title}\n")
    tags = ('机制标签: `' + ' '.join(s['glyphs']) + '`') if s['glyphs'] else '机制标签: （无）'
    md.append(f"- {tags}；关卡 {s['n_levels']} 个（其中分支 *choice {s['n_choices']} 处，磁盘命中 {s['levels_on_disk']}）")
    for it in s['items']:
        if it['t'] == 'level':
            line = f"  - `{it['id']}`"
            if it.get('choice'):
                line += ' ← *choice 分支'
            rec = levels.get(it['id'])
            if rec:
                fp = rec['fingerprint']
                fp_s = ', '.join(f'{k}×{v}' for k, v in sorted(fp.items(), key=lambda kv: -kv[1])[:5])
                line += f" ｜ 实体 {rec['entities']['total']}（{fp_s}）｜ 资源 {rec.get('manifest', {}).get('assets', 0)}"
            md.append(line)
        elif it['t'] == 'note':
            md.append(f"  > 💬 {it['v']}")
        elif it['t'] == 'glyphs':
            pass

md.append('\n## 五、全部关卡总表（%d 关，按名称排序）\n' % len(levels))
md.append('| 关卡 ID | 所在关卡集 | 实体总数 | 机制指纹 top5 | 资源数 |')
md.append('|---|---|---|---|---|')
for lid, rec in catalog['levels'].items():
    fp = rec['fingerprint']
    fp_s = ', '.join(f'{k}×{v}' for k, v in sorted(fp.items(), key=lambda kv: -kv[1])[:5])
    md.append(f"| `{lid}` | {', '.join(rec['in_sets']) or '—'} | {rec['total_instances']} | {fp_s} | {rec['assets']} |")

md.append('\n## 六、实体类型词汇表（88 种，按全游戏出现次数）\n')
md.append('| 类型 | 总数 | 类型 | 总数 |')
md.append('|---|---|---|---|')
items = list(catalog['global_type_totals'].items())
for i in range(0, len(items), 2):
    a = items[i]
    b = items[i + 1] if i + 1 < len(items) else ('', '')
    md.append(f"| {a[0]} | {a[1]} | {b[0]} | {b[1]} |")

md.append('\n---\n*本书由静态逆向自动生成，仅供学习研究；关卡设计版权归 Thekla, inc. 所有。*\n')

with open(OUT_MD, 'w', encoding='utf-8') as f:
    f.write('\n'.join(md))
print('md   ->', OUT_MD)
print('meta:', json.dumps(catalog['meta'], ensure_ascii=False))
