# 第六章 难度曲线与机制图谱（静态数据推断）

数据源：levels_layout.json 实例数据（引用 typ + 名字串）+ level_set DSL 顺序。

注意：关卡顺序为设计者 set 顺序，非强制游玩顺序；难度代理=实例数与机制多样性。


## 6.1 机制首现（按 set 序）

| 机制 | 首现序号 | 关卡 | 所属 set |
|---|---|---|---|
| Rock | 0 | rowboat_wizard_v2 | advanced_bard_and_water |
| Heroes | 0 | rowboat_wizard_v2 | advanced_bard_and_water |
| Water | 0 | rowboat_wizard_v2 | advanced_bard_and_water |
| Monsters | 0 | rowboat_wizard_v2 | advanced_bard_and_water |
| Sun | 0 | rowboat_wizard_v2 | advanced_bard_and_water |
| Tower | 1 | rowboat | advanced_bard_and_water |
| Mirror | 6 | bard_movable_island | advanced_bard_and_water |
| Skipping | 7 | bard_movable_island2 | advanced_bard_and_water |
| Promesst | 10 | crystal_logistics | beam_carrying |
| Gems | 10 | crystal_logistics | beam_carrying |
| Elevator | 10 | crystal_logistics | beam_carrying |
| Dragon | 10 | crystal_logistics | beam_carrying |
| Lily | 15 | safety_gloves | beaming_objects |
| Rover | 50 | help_drop | beams_and_basic_heroes |
| Spawner | 289 | end2_mirror1 | drafts_arted |
| Teleport | 566 | intro | drafts_arted |

## 6.2 机制共现 Top25

| A | B | 同关次数 |
|---|---|---|
| Heroes | Water | 585 |
| Heroes | Rock | 524 |
| Rock | Water | 512 |
| Mirror | Water | 433 |
| Heroes | Mirror | 403 |
| Heroes | Sun | 367 |
| Sun | Water | 366 |
| Mirror | Rock | 361 |
| Rock | Sun | 306 |
| Heroes | Monsters | 303 |
| Gems | Promesst | 282 |
| Gems | Heroes | 277 |
| Mirror | Sun | 263 |
| Monsters | Water | 251 |
| Heroes | Promesst | 248 |
| Gems | Water | 248 |
| Heroes | Tower | 228 |
| Gems | Rock | 217 |
| Promesst | Water | 216 |
| Monsters | Rock | 215 |
| Promesst | Rock | 201 |
| Tower | Water | 195 |
| Mirror | Monsters | 174 |
| Monsters | Sun | 169 |
| Gems | Mirror | 165 |

## 6.3 塔（16 座）规模与门槛

| 区 | 编号 | 关卡数 | 必解/必须 | 要求% | Glyph 门槛 |
|---|---|---|---|---|---|
| ground | 0 | 12 | 6/8 | 75% | SKIPPING | PROMESST |
| ground | 1 | 13 | 8/11 | 72% | HEROES | MIRRORS |
| ground | 2 | 11 | 6/8 | 75% | MIRRORS | PROMESST |
| ground | 3 | 10 | 7/10 | 70% | HEROES | SKIPPING |
| ground | 4 | 14 | 10/12 | 83% | HEROES | PROMESST |
| ground | 5 | 11 | 7/10 | 70% | MIRRORS | SKIPPING |
| upstairs | 0 | 14 | 12/14 | 85% | HEROES | UPSTAIRS |
| upstairs | 1 | 7 | 6/7 | 85% | SKIPPING | UPSTAIRS |
| upstairs | 2 | 12 | 10/12 | 83% | PROMESST | UPSTAIRS |
| upstairs | 3 | 7 | 6/7 | 85% | MIRRORS | UPSTAIRS |
| downstairs | 0 | 8 | 7/8 | 87% | HEROES | MIRRORS | DOWNSTAIRS |
| downstairs | 1 | 8 | 7/8 | 87% | MIRRORS | PROMESST | DOWNSTAIRS |
| downstairs | 2 | 12 | 10/12 | 83% | SKIPPING | PROMESST | DOWNSTAIRS |
| downstairs | 3 | 9 | 8/9 | 88% | HEROES | PROMESST | DOWNSTAIRS |
| downstairs | 4 | 6 | 5/6 | 83% | HEROES | SKIPPING | DOWNSTAIRS |
| downstairs | 5 | 7 | 6/7 | 85% | MIRRORS | SKIPPING | DOWNSTAIRS |

## 6.4 各 set 规模与复杂度 Top25（实例均值=难度代理）

| set | 关卡数 | 实例均值 | 实例峰值 | 机制类型均值 |
|---|---|---|---|---|
| overworld | 1 | 205313.0 | 205313 | 16.00 |
| underworld_heroes_and_mirrors | 1 | 2922.0 | 2922 | 5.00 |
| promesst3 | 3 | 2482.0 | 4544 | 5.67 |
| beam_carrying | 3 | 2329.7 | 4628 | 7.67 |
| promesst1_and_2 | 1 | 2237.0 | 2237 | 9.00 |
| endgame3 | 37 | 1803.8 | 4903 | 6.32 |
| mirrors_in_3d | 1 | 1729.0 | 1729 | 4.00 |
| endgame2 | 23 | 1696.2 | 5264 | 6.17 |
| intro_to_3d | 3 | 1570.7 | 2057 | 6.67 |
| underworld_mirrors_and_promesst | 7 | 1499.7 | 4520 | 7.71 |
| beaming_objects | 9 | 1403.6 | 1818 | 5.67 |
| double_beam_falling | 18 | 1368.4 | 3348 | 6.44 |
| spawners | 9 | 1366.3 | 3354 | 6.11 |
| advanced_bard_and_water | 10 | 1227.2 | 2466 | 4.40 |
| beams_and_basic_heroes | 62 | 1095.0 | 4170 | 5.18 |
| orange_beam_highway_worlds_collide | 4 | 1030.0 | 1782 | 7.50 |
| drafts_arted | 577 | 1013.4 | 24695 | 4.75 |
| orange_beam_highway_stones_and_promesst | 1 | 974.0 | 974 | 6.00 |
| sky_promesst_misc | 1 | 937.0 | 937 | 6.00 |
| beams_and_mirrors | 39 | 869.6 | 2665 | 5.87 |
| beams_and_stones | 36 | 834.4 | 7118 | 7.00 |
| lily_highway_mirrors_and_stones | 12 | 830.6 | 2107 | 4.92 |
| underworld_crossroads | 1 | 828.0 | 828 | 3.00 |
| double_beam_falling_dropdown | 3 | 787.7 | 894 | 5.33 |
| drafts_story | 22 | 782.1 | 1550 | 3.86 |