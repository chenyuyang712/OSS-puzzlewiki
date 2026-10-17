# 角色文本集 · 索引

> 数据：en.subtitles（568 段）+ s-cn.subtitles（233 段），并集 585 段，台词块 5,727。
> 解析器：tools/extract_voices.py；生成器：tools/build_voices_md.py。
> 注意：34 个段落中英块数不一致（对齐按块序，个别行可能错位）；sailor_alt/trader_alt 等为变体录音。

| 文件 | 角色 | 台词块 | 英文词数 | 段落 | 中译覆盖 |
|---|---|---|---|---|---|
| [01_queen.md](01_queen.md) | 女王 The Queen | 61 | 368 | 23 | 45/61 |
| [02_director.md](02_director.md) | 总监 The Director | 1136 | 8714 | 47 | 672/1136 |
| [03_acting.md](03_acting.md) | 代理总监 The Acting Director | 951 | 6555 | 40 | 508/951 |
| [04_sokoban_leamington.md](04_sokoban_leamington.md) | Leamington（勘测员 / 后来的 Sokoban） | 446 | 4128 | 51 | 321/446 |
| [05_magistrate_reynard.md](05_magistrate_reynard.md) | 治安官 Reynard | 118 | 937 | 14 | 94/118 |
| [06_warrior_valens.md](06_warrior_valens.md) | 战士 Valens | 252 | 1549 | 105 | 177/252 |
| [07_thief_tif.md](07_thief_tif.md) | 盗贼 Tif | 249 | 1730 | 103 | 176/249 |
| [08_wizard_isidore.md](08_wizard_isidore.md) | 法师 Isidore | 210 | 1635 | 71 | 160/210 |
| [09_bard.md](09_bard.md) | 吟游诗人 The Bard | 89 | 577 | 45 | 66/89 |
| [10_druid.md](10_druid.md) | 德鲁伊 The Druid | 69 | 586 | 22 | 52/69 |
| [11_ratleigh.md](11_ratleigh.md) | Ratleigh | 4 | 14 | 4 | 4/4 |
| [12_priestess.md](12_priestess.md) | 女祭司 The Priestess | 12 | 8 | 7 | 8/12 |
| [13_dragons.md](13_dragons.md) | 龙与幼龙 Dragon & Baby Dragon | 122 | 450 | 38 | 61/122 |
| [14_sailor.md](14_sailor.md) | 水手 Sailor | 573 | 3040 | 116 | 338/573 |
| [15_boat_borraidus.md](15_boat_borraidus.md) | 船灵 Borraidus（船名 Vedessud） | 325 | 2161 | 70 | 214/325 |
| [16_trader.md](16_trader.md) | 商人 The Trader（及克隆体） | 329 | 1584 | 59 | 165/329 |
| [17_gemsman_caver.md](17_gemsman_caver.md) | 宝石匠人 Caver（?） | 190 | 785 | 66 | 96/190 |
| [18_jackays.md](18_jackays.md) | Jackays | 18 | 55 | 2 | 9/18 |
| [19_meta_credits.md](19_meta_credits.md) | 彩蛋与演员表（jon / misc） | 14 | 170 | 2 | 0/14 |
| [20_unattributed.md](20_unattributed.md) | 无归属文本（_） | 556 | 38 | 201 | 356/556 |

## 角色身份考据（文本证据）

- warrior=Valens：`thief_first` "Isidore! Valens!"；`heroes_warrior_mistrust` "good sir Valens"
- thief=Tif：`warrior_heroes1_call` "Tif! Isidore!"
- wizard=Isidore（Izzy）：同上；`heroes1_warrior_thief` "Where's Izzy?"
- magistrate=Reynard：`heroes_warrior_mistrust` "Magistrate Reynard felt slimy"
- sokoban=Leamington：`intro_1` "Mr. Quigley,"；`audiolog_g_crisis` 第三人称自指
- boat=Borraidus（船灵）/ Vedessud（船名）：`actor_credits` Jamieson Price 自述；`pals_meeting_vedessud`
- jackays/conroe=女王同伴：`intro_queen_callout_alt` "Jackays! Conroe! Are you here?"
- 职级序列：Sokoban → Implementor（`audiolog_sky_invocation`）；Magistrate 为头衔
- jon=片尾《失乐园》朗读者（`paradise_lost_invocation_credits`），疑为 Jonathan Blow 本人

## 配音演员表（游戏内 actor_credits 段）

- I'm Liam O'Brien and I am playing the Warrior.
- I'm Sabrina. I play the Thief.
- My name goes like this: Darin De Paul. And I am the voice of the Wizard.
- My name is Matthew Waterson and I am playing the Druid.
- I'm Anjali Bhimani and I am playing the Bard in Order of the Sinking Star.
- My name is Erica Luttrell and I play Sailor.
- I'm Jamieson Price. I'm the voice of Borraidus, the spirit of Sailor's ship.
- Hi, I'm Sean Rohani, I play Caver in Order of the Sinking Star.
- My name's Emily O'Brien, and I'm playing the Queen.
