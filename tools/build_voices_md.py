#!/usr/bin/env python3
# build_voices_md.py -- voices.json -> per-character Markdown files + README index + combined file.
import json, os
from collections import OrderedDict

OUT = 'report/voices'
V = json.load(open(OUT + '/voices.json', encoding='utf-8'))

# tag-group -> (文件名, 标题, 身份考据)
GROUPS = [
    (['queen'], '01_queen', '女王 The Queen',
     '无名女王，框架叙事的起点（"这里……是来世吗？"）。配音：Emily O\u2019Brien（游戏内演员表自述）。'),
    (['director'], '02_director', '总监 The Director',
     '沉星会正任总监，出门"调查"多年未归；在 audiolog_u_* 系列亲自面试 Leamington。片尾 Milton《失乐园》祈愿由 jon（疑为 Jonathan Blow 本人）朗读，与此角呼应。'),
    (['acting'], '03_acting', '代理总监 The Acting Director',
     'Director 外出期间代掌沉星会；audiolog_sky_* 创教史独白的主要讲述者；自述从 Sokoban 升至 Implementor 再到代理总监。'),
    (['sokoban'], '04_sokoban_leamington', 'Leamington（勘测员 / 后来的 Sokoban）',
     '玩家的前任。audiolog_g_* 录音日志（致 Quigley）与全部主线对话的主人翁；通关后获仓房管辖权，职级 Sokoban、头衔 Magistrate。证据：intro_1 "Mr. Quigley,"；crisis 日志第三人称自指 "Leamington was rash, you\'d say"。'),
    (['magistrate'], '05_magistrate_reynard', '治安官 Reynard',
     'Heroes 线大反派，后为仓房前任守门人（"按我的固有时间算，整整十四年了"）。证据：warrior 台词 "Magistrate Reynard felt slimy from the beginning"。'),
    (['warrior', 'warrior_alt'], '06_warrior_valens', '战士 Valens',
     'Heroes 三主角之一。证据：thief_first "Isidore! Valens!"；magistrate 称 "good sir Valens"。配音：Liam O\u2019Brien。'),
    (['thief'], '07_thief_tif', '盗贼 Tif',
     'Heroes 三主角之一。证据：warrior_heroes1_call "Tif! Isidore!"；被称 "Izzy" 的是 Isidore。配音：Sabrina。'),
    (['wizard'], '08_wizard_isidore', '法师 Isidore',
     'Heroes 三主角之一，"肉汁法师"梗当事人。配音：Darin De Paul。'),
    (['bard'], '09_bard', '吟游诗人 The Bard', 'Heroes 线配角。配音：Anjali Bhimani。'),
    (['druid'], '10_druid', '德鲁伊 The Druid', 'Heroes 线配角。配音：Matthew Waterson。'),
    (['ratleigh'], '11_ratleigh', 'Ratleigh',
     'Reynard 的学徒/随从（"Come, Ratleigh. If you\'re to assume my duties here…"）。台词极少。'),
    (['priestess'], '12_priestess', '女祭司 The Priestess', 'Heroes 线配角，几乎只有省略号。'),
    (['dragon', 'baby_dragon'], '13_dragons', '龙与幼龙 Dragon & Baby Dragon', 'Heroes 线生物角色。'),
    (['sailor', 'sailor_alt'], '14_sailor', '水手 Sailor',
     'Pals 线主角之一，与船灵同行；给自己的船起名 Vedessud（"Veddy"）。配音：Erica Luttrell。sailor_alt 为同场景替代录音/变体（与 sailor 有 25 段重叠）。'),
    (['boat', 'vedessud'], '15_boat_borraidus', '船灵 Borraidus（船名 Vedessud）',
     '"会自己操帆的船"。证据：演员表 "Jamieson Price — Borraidus, the spirit of Sailor\u2019s ship"；sailor 台词 "Here is my boat, Vedessud"；pals_borrie "Ought I call you Borrie from here out?"。配音：Jamieson Price。'),
    (['trader', 'trader_alt', 'trader_clone_1', 'trader_clone_2'], '16_trader', '商人 The Trader（及克隆体）',
     'trader_clone_1/2 证实商人存在克隆体；trader_alt 为变体录音。'),
    (['gemsman', 'gemsman_alt'], '17_gemsman_caver', '宝石匠人 Caver（?）',
     '宝石世界角色。演员表有 Sean Rohani 饰 "Caver"，疑即此角（未完全确证）。'),
    (['jackays'], '18_jackays', 'Jackays',
     '女王的同伴（intro_queen_callout_alt："Jackays! Conroe! Are you here?"）。仅出现于开发用段落 audiolog_di_tiger_lily_v2，文本为空——疑似未实装或仅音效。'),
    (['jon', 'misc'], '19_meta_credits', '彩蛋与演员表（jon / misc）',
     'jon：片尾朗读 Milton《失乐园》祈愿的声音，疑为 Jonathan Blow 本人。misc：游戏内演员表自报家门段落（actor_credits），含 9 位配音演员真名。'),
    (['_'], '20_unattributed', '无归属文本（_）',
     '未标注说话者的行：旁白、环境音、第二人称提示等。多为空标记哨兵，此处仅收录有实际文字的行。'),
]

def stats(rows):
    blocks = len(rows)
    words = sum(len(r['en'].split()) for r in rows)
    segs = len(set(r['seg'] for r in rows))
    cn_ok = sum(1 for r in rows if r['cn'])
    return blocks, words, segs, cn_ok

def render_file(title, desc, rows):
    L = [f'# {title}\n', f'> {desc}\n']
    b, w, s, cn = stats(rows)
    cov = f'{cn}/{b}' if b else '0'
    L.append(f'**统计**：台词块 {b} · 英文词数 {w} · 涉及段落 {s} · 官方中译覆盖 {cov}\n')
    L.append('---\n')
    cur = None
    for r in rows:
        if r['seg'] != cur:
            cur = r['seg']
            cn_tag = '' if r['has_cn'] else ' （无官方中译）'
            L.append(f'\n### `{cur}`{cn_tag}\n')
        if not r['en'] and not r['cn']:
            continue
        L.append(f'- **EN** {r["en"]}')
        if r['cn']:
            L.append(f'  **CN** {r["cn"]}')
        for n in r['notes']:
            L.append(f'  *导演注释：{n}*')
    return '\n'.join(L) + '\n'

def main():
    os.makedirs(OUT, exist_ok=True)
    index_rows = []
    combined = ['# 《沉星之序》全角色文本集\n',
                '> 来源：data/strings/subtitles/en.subtitles + s-cn.subtitles（官方简体中译）。',
                '> 共 585 个段落、5,727 个台词块、31 个说话人标签。英文为原文，CN 行为官方中译；标注"无官方中译"的段落官方简体字幕文件未收录。',
                '> 斜体"导演注释"为字幕文件内嵌的作者备注（非游戏内可见内容）。\n', '---\n']
    for tags, fname, title, desc in GROUPS:
        rows = []
        for t in tags:
            rows.extend(V.get(t, []))
        # 保持文件顺序：按首次出现排序（voices.json 已有序，合并多 tag 时按 seg 顺序混合即可，简单按原顺序拼接后按 seg 首次出现排序）
        seen = {}
        for r in rows:
            seen.setdefault(r['seg'], len(seen))
        rows.sort(key=lambda r: list(seen).index(r['seg']) if r['seg'] in seen else 0)
        # 上面的 sort 不对（list(seen) 每次重建）；改为稳定排序键：
        order = {n: i for i, n in enumerate(seen)}
        rows.sort(key=lambda r: order[r['seg']])
        if not rows: continue
        md = render_file(title, desc, rows)
        with open(f'{OUT}/{fname}.md', 'w', encoding='utf-8') as f:
            f.write(md)
        b, w, s, cn = stats(rows)
        first = next((r['en'] for r in rows if r['en']), '')
        index_rows.append((fname, title, b, w, s, cn, first[:70]))
        combined.append(f'\n<!-- ================= {fname} ================= -->\n')
        combined.append(md)
    with open(f'{OUT}/CHARACTERS_ALL.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(combined))
    # README
    R = ['# 角色文本集 · 索引\n',
         '> 数据：en.subtitles（568 段）+ s-cn.subtitles（233 段），并集 585 段，台词块 5,727。',
         '> 解析器：tools/extract_voices.py；生成器：tools/build_voices_md.py。',
         '> 注意：34 个段落中英块数不一致（对齐按块序，个别行可能错位）；sailor_alt/trader_alt 等为变体录音。\n',
         '| 文件 | 角色 | 台词块 | 英文词数 | 段落 | 中译覆盖 |', '|---|---|---|---|---|---|']
    for fname, title, b, w, s, cn, _ in index_rows:
        R.append(f'| [{fname}.md]({fname}.md) | {title} | {b} | {w} | {s} | {cn}/{b} |')
    R.append('\n## 角色身份考据（文本证据）\n')
    R.append('- warrior=Valens：`thief_first` "Isidore! Valens!"；`heroes_warrior_mistrust` "good sir Valens"')
    R.append('- thief=Tif：`warrior_heroes1_call` "Tif! Isidore!"')
    R.append('- wizard=Isidore（Izzy）：同上；`heroes1_warrior_thief` "Where\'s Izzy?"')
    R.append('- magistrate=Reynard：`heroes_warrior_mistrust` "Magistrate Reynard felt slimy"')
    R.append('- sokoban=Leamington：`intro_1` "Mr. Quigley,"；`audiolog_g_crisis` 第三人称自指')
    R.append('- boat=Borraidus（船灵）/ Vedessud（船名）：`actor_credits` Jamieson Price 自述；`pals_meeting_vedessud`')
    R.append('- jackays/conroe=女王同伴：`intro_queen_callout_alt` "Jackays! Conroe! Are you here?"')
    R.append('- 职级序列：Sokoban → Implementor（`audiolog_sky_invocation`）；Magistrate 为头衔')
    R.append('- jon=片尾《失乐园》朗读者（`paradise_lost_invocation_credits`），疑为 Jonathan Blow 本人')
    R.append('\n## 配音演员表（游戏内 actor_credits 段）\n')
    for r in V.get('misc', []):
        if r['en']: R.append(f'- {r["en"]}')
    with open(f'{OUT}/README.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(R) + '\n')
    tot = os.path.getsize(f'{OUT}/CHARACTERS_ALL.md')
    print('done. files:', len(index_rows), 'combined bytes:', tot)

if __name__ == '__main__':
    main()
