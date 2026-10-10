# 《沉星之序》关卡目录全书

> 数据来源：游戏本地 simp 包提取（static, offline）。构建脚本 `tools/build_catalog.py`；机器可读版 `levels_catalog.json`。所有关卡名/区域名/机制名取自官方简体中文本地化。


## 一、世界结构：16 座塔楼

| 层区 | # | 关卡数 | 普通/坠落 | 门槛(需解/要求) | 机制组合 | 塔编号 |
|---|---|---|---|---|---|---|
| 地面层 | 0 | 12 | 8/4 | 6/8 (75%) | SKIPPING | PROMESST | #83-7084 |
| 地面层 | 1 | 13 | 11/2 | 8/11 (72%) | HEROES | MIRRORS | #83-7074 |
| 地面层 | 2 | 11 | 8/3 | 6/8 (75%) | MIRRORS | PROMESST | #110-3954 |
| 地面层 | 3 | 10 | 10/0 | 7/10 (70%) | HEROES | SKIPPING | #83-7076 |
| 地面层 | 4 | 14 | 12/2 | 10/12 (83%) | HEROES | PROMESST | #83-7078 |
| 地面层 | 5 | 11 | 10/1 | 7/10 (70%) | MIRRORS | SKIPPING | #83-7080 |
| 楼上 | 0 | 14 | 14/0 | 12/14 (85%) | HEROES | UPSTAIRS | #110-5121 |
| 楼上 | 1 | 7 | 7/0 | 6/7 (85%) | SKIPPING | UPSTAIRS | #110-5110 |
| 楼上 | 2 | 12 | 12/0 | 10/12 (83%) | PROMESST | UPSTAIRS | #110-5113 |
| 楼上 | 3 | 7 | 7/0 | 6/7 (85%) | MIRRORS | UPSTAIRS | #110-5117 |
| 楼下 | 0 | 8 | 8/0 | 7/8 (87%) | HEROES | MIRRORS | DOWNSTAIRS | #110-5211 |
| 楼下 | 1 | 8 | 8/0 | 7/8 (87%) | MIRRORS | PROMESST | DOWNSTAIRS | #110-29812 |
| 楼下 | 2 | 12 | 12/0 | 10/12 (83%) | SKIPPING | PROMESST | DOWNSTAIRS | #110-5184 |
| 楼下 | 3 | 9 | 9/0 | 8/9 (88%) | HEROES | PROMESST | DOWNSTAIRS | #110-5226 |
| 楼下 | 4 | 6 | 6/0 | 5/6 (83%) | HEROES | SKIPPING | DOWNSTAIRS | #110-29827 |
| 楼下 | 5 | 7 | 7/0 | 6/7 (85%) | MIRRORS | SKIPPING | DOWNSTAIRS | #110-5194 |

## 二、英雄与机制

### 英雄（campaign_name_h_*）

| 键 | 中文 | 英文 |
|---|---|---|
| campaign_name_h_0 | 战士 | Warrior |
| campaign_name_h_1 | 盗贼 | Thief |
| campaign_name_h_2 | 法师 | Wizard |
| campaign_name_h_3 | 吟游诗人 | Bard |
| campaign_name_h_4 | 德鲁伊 | Druid |
| campaign_name_h_5 | 哥布林 | Goblin |
| campaign_name_h_6 | 龙 | Dragon |
| campaign_name_h_7 | 水晶 | Crystal |
| campaign_name_h_8 | 界门 | Gate |

### 机制（campaign_name_m_*）

| 键 | 中文 | 英文 |
|---|---|---|
| campaign_name_m_0 | 镜 | Mirror |
| campaign_name_m_1 | 石头 | Rock |
| campaign_name_m_2 | 反射 | Reflect |
| campaign_name_m_3 | 成双 | Duplicate |
| campaign_name_m_4 | 岛 | Isle |
| campaign_name_m_5 | 海洋 | Ocean |

## 三、区域名对照（官方中文）

| 键 | 中文 | 英文 |
|---|---|---|
| area_g_antipode | 对映之地 | The Antipode |
| area_g_beamcaster | 光束发射器 | Beamcaster |
| area_g_crossroads | 交汇之地 | Crossroads |
| area_g_exit | 出口 | The Exit |
| area_g_extended_promise_south | 项环 | Torc |
| area_g_heroes_2 | 英雄2：怪物 | Heroes 2: Monsters |
| area_g_heroes_3 | 英雄3：吟游诗人与德鲁伊 | Heroes 3: Bard, Druid |
| area_g_heroes_and_artifacts | 英雄与神器 | Heroes and Artifacts |
| area_g_heroes_and_light | 英雄与光 | Heroes and Light |
| area_g_heroes_and_light_extended | 英雄与光：进阶 | Heroes and Light, Advanced |
| area_g_heroes_and_mirrors | 英雄与魔镜 | Heroes and Mirrors |
| area_g_heroes_and_stones_east | 英雄与飞石：东部 | Heroes and Stones, East |
| area_g_heroes_and_stones_west | 英雄与飞石：西部 | Heroes and Stones, West |
| area_g_heroes_and_water | 英雄与水 | Heroes and Water |
| area_g_heroes_and_water_north | 英雄与水：北部 | Heroes and Water, North |
| area_g_heroes_duplicated | 英雄，成双 | Heroes, Duplicated |
| area_g_heroes_initial | 搬运英雄 | Heroes of Hauling |
| area_g_heroes_together | 英雄齐聚 | Heroes Together |
| area_g_mirror_isles | 镜之群岛 | The Mirror Isles |
| area_g_mirrorable_mirrors | 镜中之镜 | Mirrorable Mirrors |
| area_g_mirrors_and_light_north | 映照之光 | Beams Reflected |
| area_g_mirrors_and_light_south | 反射光束 | Reflected Beams |
| area_g_mirrors_and_stones | 魔镜与飞石 | Mirrors and Stones |
| area_g_mm | 光随镜转 | Beams, Mirrorably |
| area_g_promise_1 | 光束发射器之库 | Vault of the Beamcasters |
| area_g_promise_3 | 变形光束 | Alter Beam |
| area_g_promise_extended_north | 推车与短杖 | Cart, Rod |
| area_g_skipping_stones | 飞石成径 | Skipping Stones |
| area_g_stones_illuminated | 光照之石 | Stones Illuminated |
| area_g_stones_illuminated_3 | 巨龙挤一挤 | Squeeze, Dragon |
| area_s_antipode_high | 对映之地：高处 | Antipode High |
| area_s_archways | 拱门 | Archways |
| area_s_bard_stacks | 魅惑与堆叠 | Charmed Stacks |
| area_s_beam_way | 光束之路 | The Beam Way |
| area_s_falls | 飞跃与坠落 | Skipping and Falling |
| area_s_heroes_3d | 英雄与第三维度 | Heroes and Depth |
| area_s_heroes_way | 英雄之路 | The Heroic Way |
| area_s_highgrounds | 双倍光束坠落 | Double Beam Falling |
| area_s_mines | 升降机 | Elevators |
| area_s_mirror_rotation | 头顶一面镜 | Mirror on Head |
| area_s_mirror_way | 镜之路 | The Mirror Way |
| area_s_mirrors_and_buttons | 魔镜与按钮 | Mirrors and Buttons |
| area_s_porphyry | 竖直端点 | Vertical Endpoints |
| area_s_skipping_stacks | 堆叠与飞跃 | Skipping Stacks |
| area_s_skipping_way | 飞跃之路 | The Skipping Way |
| area_s_spinning_beams | 旋转光束 | Spinning Beams |
| area_s_stacks | 堆叠与水 | Stacks and Water |
| area_s_startle_reflex | 转身的哥布林 | Goblin Turning |
| area_s_strength | 力量 | Strength |
| area_s_top | 世界之巅 | Top of the World |
| area_s_towers | 坠落之镜 | Mirror Falling |
| area_s_upper_crossroads | 交汇之地：高处 | Crossroads High |
| area_s_vertical_mirror_skipping | 竖直之镜与飞跃 | Vertical Mirror Skipping |
| area_s_vertical_mirrors | 竖直之镜 | Vertical Mirrors |
| area_s_vertical_priestess | 防护与支撑 | Protection and Support |
| area_u_3wc | 三者齐上阵 | Three at Once |
| area_u_4wc | 四方共合力 | Four Together |
| area_u_alter_smash | 变形与粉碎 | Alter-Smash |
| area_u_antipode_low | 对映之地：低处 | Antipode Low |
| area_u_bard_and_water | 吟游诗人与水 | Bard and Water |
| area_u_beam_rotation_on_lilies | 睡莲上的旋转光束 | Lily Beam Rotation |
| area_u_crossroads_low | 交汇之地：低处 | Crossroads Low |
| area_u_crystal_carts | 水晶推车 | Crystal Carts |
| area_u_double_beams | 双倍光束 | Doubling Beams |
| area_u_endpoint_falling | 端点坠落 | Endpoint Falling |
| area_u_endpoint_skipping | 端点飞跃 | Endpoint Skipping |
| area_u_exit_low | 出口：低处 | Exit Low |
| area_u_gate_opening | 开启界门 | Gate Opening |
| area_u_gem_beams | 宝石光束 | Gem Beams |
| area_u_gems_as_obstacles | 宝石挡道 | Gems as Obstacles |
| area_u_heterogeneous_stacks | 混合堆叠 | Heterogeneous Stacks |
| area_u_lemonade | 镜中之镜：集锦 | Mirrorable Mirror Medley |
| area_u_mirrors_and_artifacts | 魔镜与神器 | Mirrors and Artifacts |
| area_u_mirrors_and_rivers | 魔镜与河流 | Mirrors and Rivers |
| area_u_mirrors_as_obstacles | 魔镜挡道 | Mirrors as Obstacles |
| area_u_monsters_through | 怪物穿行 | Monsters, Through |
| area_u_moving_flat_things | 扁平物件挪一挪 | Moving the Flat Things |
| area_u_partial_resets | 局部重置 | Partial Resets |
| area_u_river | 无尽飞跃 | Endless Skipping |
| area_u_skipping_misc_beams | 飞跃与各式光束 | Skipping, Misc Beams |
| area_u_wrapping_mirrors | 环绕镜子 | Wrapping Mirrors |
| area_u_wrapping_wizard | 环绕法师 | Wrapping Wizard |
| area_u_zachtronics | 光束演算 | Beam Computation |

## 四、关卡集详解（66 个 level_set）


### advanced_bard_and_water

- 机制标签: `heroes stones`；关卡 10 个（其中分支 *choice 9 处，磁盘命中 10）
  > 💬 Bard + skipping stones - located north
  - `rowboat_wizard_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 320
  - `rowboat` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 328
  - `boat_priest_v3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 392
  - `front_side_bus2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 318
  - `front_side_bus3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 249
  - `drop_off` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 300
  > 💬 rowboat_self
  > 💬 self_propelled
  > 💬 *choice
  > 💬 get_close # Daily Challenge potential
  > 💬 *choice
  > 💬 Moved to Underworld because this is a sequence
  > 💬 and the 2nd one is pretty hard, and the first one
  > 💬 involves structural observation, which is maybe
  > 💬 a subtle underworld thing.
  - `bard_movable_island` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 292
  - `bard_movable_island2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 296
  - `pole_vault` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 338
  > 💬 carpet_bomb # Daily challenge potential
  - `missile_command` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 314
  > 💬 Daily Challenge...
  > 💬 bard_gated_platform
  > 💬 boat_skip

### beam_carrying

- 机制标签: `beams`；关卡 3 个（其中分支 *choice 3 处，磁盘命中 3）
  > 💬 Room about carrying objects interacting with beams
  - `crystal_logistics` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 260
  - `beam_sisters` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 220
  - `corner_trick_easier` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 237

### beaming_objects

- 机制标签: `heroes beams`；关卡 9 个（其中分支 *choice 7 处，磁盘命中 9）
  > 💬 Levels that focus on beams affecting things besides the characters.
  > 💬 This section teaches more about what stuff is beamable & explores it further.
  > 💬 There is already a fair of this in other ground-floor beams+heroes level sets,
  > 💬 but Orsi and I decided to just keep this on its own and not merge them.
  > 💬 There was a note to possibly move those levels here, but they already got arted,
  > 💬 so it's a bit too late. And also this set has its own identity. -Patrick
  > 💬 See "Puzzles" spreadsheet for more info on which levels were cut, organization notes, etc. for this level set.
  > 💬 https://docs.google.com/spreadsheets/d/1M4-IlEWzCdMbLSjEv-r10ut--MSl3qPT1LepsuAkNdk/edit#gid=810785867
  > 💬 Double
  - `boxes_vs_crystals` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 285
  - `pushing_crystal_near_orange_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 287
  - `safety_gloves` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 298
  > 💬 Endpoint
  - `endpoint_object` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 254
  > 💬 Through
  - `through_maze_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 333
  > 💬 Smash
  - `middle_smash` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 338
  > 💬 Open
  - `accidentally_unlock_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 239
  > 💬 Torc
  - `torc_blocked_easier` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 328
  - `torc_blocked` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 245
  > 💬 double_block_v3 # Patrick cut
  > 💬 1d_sokoban # Patrick removed from this level set, to be improved and expanded upon, maybe in underworld?
  > 💬 the_wall # Patrick cut
  > 💬 endpoint_two_objects # Patrick cut
  > 💬 crystal_clear # Broken. Kind of redundant with some of these orange-beam-combo-lock levels I did anyway. -jblow, 10 May 2023
  > 💬 accidentally_unlock_harder # harder but probably worse.
  > 💬 comment for pushing_crystal_near_orange_v2 --- similar to pushing_near_orange and pushing_orange... but I think this level is justified in its own existence. Only question is ordering?
  > 💬 Endpoint
  > 💬 (I put the contents of endpoint_trials here. There's a lot of levels, but a lot of these aren't that great or are sort of redundant so it's probably not as many as it seems)
  > 💬 endpoint_push_intro_v3
  > 💬 endpoint_push_intro_v2
  > 💬 endpoint_push_1_v2
  > 💬 endpoint_push_druid
  > 💬 end_mowers
  > 💬 end_mowers_v3
  > 💬 *choice
  > 💬 end_dragon_mowers_0
  > 💬 end_dragon_mowers_v2
  > 💬 *choice
  > 💬 end_dragon_mowers_1
  > 💬 end_dragon_mowers_v3
  > 💬 *choice
  > 💬 monster_endpoint
  > 💬 monster_endpoint_madness_0
  > 💬 monster_endpoint_madness
  > 💬 *choice

### beams_and_basic_heroes

- 机制标签: `heroes beams`；关卡 62 个（其中分支 *choice 49 处，磁盘命中 62）
  > 💬 These will be the first levels outside of Promesst in which the players use beams, which means we need to introduce things like lasers being movable, crystals being laserable, how abilities are affected by beams.
  > 💬 Should not have anything too fancy in here, probably just heroes and beams. It's separated by beam type, because (for the most part) the beams have pretty separate ideas.
  > 💬 Might even be good to start off even simpler with a couple heroes + beams levels in which the beams are fixed in place.
  > 💬 Strength
  - `oneway_beam` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 238
  > 💬 Through beam
  > 💬 heroes_beam_intro
  > 💬 strafe
  - `through_intro` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 254
  - `through_push` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 235
  - `binary_maze` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 196
  - `thief_through` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 232
  - `wall_sneak` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 285
  - `bypass_gates` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 201
  > 💬 Both of these are decent levels, but commented out because there's already a lot of levels in this part:
  > 💬 leave_behind
  > 💬 gem_through
  > 💬 *choice
  - `corner_loop` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 222
  > 💬 green_beam_fun
  > 💬 *choice
  - `through_sokoban` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 255
  > 💬 Double beam
  - `double_team` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 162
  > 💬 pushing_near_orange, pushing_orange, pushing_crystal_near_orange and pulling_near_orange are compact levels with a lot of steps (hopefully doesn't feel excessive.) Hoping that helps give the player a good feel for pushing lasers, boxes, and crystals while doubling
  - `pushing_near_orange` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 180
  - `pulling_near_orange_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 257
  - `pushing_orange` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 209
  - `jump_the_fence_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 218
  - `orange_beam_deal` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 186
  > 💬 Commented out because it uses the sailor:
  > 💬 orange_beam_deal_double
  > 💬 In the style of orange_beam_deal, this time using the doubled double beam.
  > 💬 priest_hop
  > 💬 beam_problems
  > 💬 Hmm... could use some more changing. The idea of putting the orange laser in the gate is not enforcable, because you can just put it behind the gate and it will be blocked. Also, could just be a bit smaller than it is now.
  > 💬 Misc level about smashing a beam emitter. Doesn't use water though.
  - `beam_shatter` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 233
  > 💬 Endpoint beam (not in promesst 1)
  - `simple_trap` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 238
  - `untrap` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 250
  - `pushback` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 254
  - `endpoint_team` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 227
  - `purple_haze` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 211
  - `purple_perpendicular` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 247
  - `endpoint_gates` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 260
  - `slide_rows` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 255
  - `pull_together` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 221
  - `purple_push_pal` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 206
  > 💬 vault
  > 💬 find_platform
  > 💬 Open beam
  - `red_handed` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 206
  - `lock_picky` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 167
  > 💬 With water (3-world-combo)
  > 💬 Thief+rover+water
  - `help_drop` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 214
  > 💬 Water + Wizard + Gems
  - `gem_transport` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 173
  - `gem_transport_2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 168
  > 💬 Cleric fly + wand + water
  - `cleric_isles` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 240
  > 💬 Wand + water + twins
  - `friendly_nudges` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 170
  > 💬 Warrior combo-lock mechanism
  - `shunt2_alt` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 208
  > 💬 Druid + wand + water
  - `plus_signs_v3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 191
  > 💬 With rovers
  > 💬 pet_roomba
  > 💬 *choice
  > 💬 robot_assistant
  > 💬 *choice
  > 💬 monster_proof
  > 💬 *choice
  > 💬 (help_drop moved to the "with water" section)
  > 💬 Old rover stuff:
  > 💬 rover_square
  > 💬 rover_square2
  > 💬 death_by_rover
  > 💬 rover_goblin_party
  > 💬 rover_and_thief
  > 💬 rover_and_wizard
  > 💬 Some more complicated beam interactions in here.
  > 💬 Wizard + Purple
  > 💬 purple_wizard_intro
  - `wizard_finesse_1` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 273
  - `wizard_finesse_2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 270
  - `wizard_finesse_3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 282
  - `wizard_finesse_4` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 289
  > 💬 Note: All of the above are in wizard_finesse_all, not sure if that's better than individually.
  - `purple_wizard_maze` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 372
  - `be_aggro_alt_2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 347
  > 💬 Wizard + Double
  - `orange_wizard_intro` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 302
  - `learning_double` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 252
  > 💬 beam_blocker_zach
  > 💬 *choice
  - `magic_square` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 268
  > 💬 beam_blocker_simple
  - `magic_shield` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 306
  > 💬 Wizard + Through
  - `see_through` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 320
  - `mini_green_maze` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 248
  - `safe_returns` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 289
  - `two_through_alt_2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 294
  > 💬 Through + Trees/Druid
  > 💬 minefield
  > 💬 tree_sneak_intro
  > 💬 tree_sneak
  > 💬 *choice
  > 💬 dungeon_escape
  > 💬 *choice
  > 💬 Bard charming something in a beam
  > 💬 (e.g. that the charmed thing is doubled when the charmed object is in a double beam)
  > 💬 Double beam
  - `double_tempo` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 293
  - `button_playground` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 289
  > 💬 bard_offset
  > 💬 build_platformv2
  > 💬 bard_escape
  - `matching_purple` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 261
  - `immobilize` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 285
  - `endpoint_weapon` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 357
  > 💬 arms_lengthv2
  - `invisible_hand` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 250
  > 💬 P3 stuff with Heroes and whoever:
  - `snipperclips_0_square` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 237
  - `snipperclips_square` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 240
  - `snipperclips_diagonal` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 240
  - `druid_multismash_v3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 151
  > 💬 Has Warrior and crystals
  - `gem_beam_placement` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 360
  > 💬 Smash beam and monsters:
  - `smash_grid_kill` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 225
  - `smash_grid_4` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 217

### beams_and_mirrors

- 机制标签: `mirrors beams`；关卡 39 个（其中分支 *choice 33 处，磁盘命中 39）
  > 💬 Promesst + Mirror Isles
  > 💬 Some levels with just normal mirrors
  > 💬 Open
  - `tempered_glass_red` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 265
  - `red_rooms_v5` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 320
  - `wrapping_mirror_red_v4` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 307
  > 💬 Smash
  - `smash_or_dash_vs2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 248
  > 💬 Through
  - `break_through_focused` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 302
  > 💬 Strong
  - `cyan_counter_med3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 294
  - `fun_house` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 283
  - `cyan_torc_maze_vs` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 368
  - `top_green_purple_v3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 277
  > 💬 Endpoint
  - `sidetrack` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 247
  - `purple_wall_around_easier_vp` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 221
  - `across_the_fence_vtrader_m_p` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 277
  > 💬 Double
  - `orange_doubleback` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 208
  - `orange_doubledoubleback` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 211
  > 💬 Rooms
  - `protrusions` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 180
  - `dual_screen` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 136
  > 💬 over_the_edge
  > 💬 screencheat
  - `mirror_promesst` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 306
  > 💬 Wand + magic mirror
  - `mirror_non_turner_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 186
  - `adjust_explorer_v4` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 166
  > 💬 Torc + mirror + beam:
  - `green_torq_mirror_vs4` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 341
  > 💬 Merging clones using beams
  - `purple_clm_v4` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 248
  - `orange_clm_s` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 245
  > 💬 Rovers
  - `rover_water_purple_v9` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 187
  - `rover_water_purple_sequel_v3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 249
  - `magic_rover` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 173
  - `remote_work` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 226
  > 💬 Orange water walking dropdown
  > 💬 orange_rescue
  - `double_sideways` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 149
  - `floating_orange_purple` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 195
  - `orange_predicament` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 144
  > 💬 Crystal rovers dropdown:
  - `green_crystal_rover` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 172
  - `mirror_rover_orange_2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 202
  > 💬 mirror_rover_green is the same level as mirror_rover_orange...
  > 💬 mirror_rover_green
  > 💬 *choice
  > 💬 P3 + Mirrors
  - `red_yellow_alter_with_intro_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 222
  - `purple_corner_gem` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 302
  - `gem_clg_v4` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 326
  > 💬 Metamirrors + other base games (but no 3D)
  - `the_spiral` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 258
  > 💬 Metamirrors + Promesst
  > 💬 green_one_river
  > 💬 green_two_rivers
  - `green_metamirror` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 334
  > 💬 green_mountain
  > 💬 *choice
  > 💬 green_purple_mountain
  > 💬 *choice
  - `orange_floaty_reflect_v3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 247
  > 💬 purple_mirror_endpoint
  > 💬 *choice
  - `meta_orange_purple` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 209
  - `meta_orange_purple_2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 210
  > 💬 double_sideways_meta
  > 💬 *choice
  > 💬 skip_orange_corner_meta
  > 💬 *choice
  > 💬 mirror_mirror_v2
  > 💬 *choice

### beams_and_stones

- 机制标签: `stones beams`；关卡 36 个（其中分支 *choice 31 处，磁盘命中 36）
  > 💬 Skipping Stones + Promesst
  > 💬 Beams + Stones
  > 💬 Orange easy level
  - `skip_orange_block_c` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 203
  > 💬 Through + Strong and lilypads group
  - `through_way` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 196
  - `sp_crystal_tuto` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 225
  - `stonewalled` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 165
  - `frantic_factory_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 211
  - `skipping_cyan_precise_c_v3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 236
  > 💬 Open + Smash group
  - `doorstop` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 232
  - `doorstop_reprise_easier` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 206
  - `glass_beach` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 224
  - `break_send_lily_c` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 192
  > 💬 Endpoint
  - `purple_beam_intro_v2_alt` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 205
  - `faster_than_stone` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 158
  - `hustle_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 159
  > 💬 Big level
  - `skipping_near_beams_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 404
  > 💬 Other
  > 💬 Wrapping
  - `skipping_wrapping_v3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 220
  > 💬 Wand
  - `skip_or_sink_r` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 165
  - `skip_wand_v6` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 238
  > 💬 Big level
  - `skipping_promesst` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 206
  > 💬 Rover
  - `rover_impulse_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 221
  - `rover_advance_c_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 215
  - `rover_shift_p` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 188
  - `submarine` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 193
  - `submarine_far_away` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 219
  > 💬 Orange water walking dropdown
  - `skip_orange_maze_v3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 220
  - `orange_skip_place_v3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 172
  - `skip_orange_wall_v3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 200
  > 💬 Promesst 3 lock:
  > 💬 P3 + Skipping + Skinny Beam
  - `security_checkpoints_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 158
  - `ocean_blue` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 138
  > 💬 Alter smash
  - `rsmash` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 195
  > 💬 Friendly Dragon on the ground floor:
  - `endpoint1_skipping` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 201
  - `narrow_passage` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 199
  > 💬 dragons_den
  > 💬 *choice
  - `close_circuit` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 194
  - `double_door` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 214
  - `free_ride` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 225
  - `swap_seats` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 202
  > 💬 stuck_in_the_middle
  > 💬 *choice
  - `dragon_drag` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 167
  > 💬 Skipping Stones to Lonely Homes + Beams
  > 💬 Skipping focused
  > 💬 Skipping + Beams mostly uses double or endpoint beams
  > 💬 skipping_near_beams
  > 💬 skipping_near_beams_basement
  > 💬 *choice
  > 💬 tricky_endpoint
  > 💬 *choice
  > 💬 Some levels probably obsolete because of skipping_near_beams:
  > 💬 helpage00
  > 💬 *choice
  > 💬 helpage0_easier_timing # The original had IMO too tricky timing (for this early in the level set, at least)
  > 💬 helpage0
  > 💬 helpage # May also be trickier than it should be, with a few rabbit holes. (just because the sailor can get to the trader's island as a first step, but that's not the right path.)
  > 💬 hurtage
  > 💬 *choice
  > 💬 YELLOW
  > 💬 These are simplified / lighter-weight versions of smash_midskip.
  > 💬 They have removed the "smash a stone at the beginning" that happened in that level though.
  > 💬 I think I prever 4, but, not totally sure.  -jblow
  > 💬 We decided in a previous design call to move this interaction to the underworld. -Patrick 2024-05-10
  > 💬 smash_midskip_simpler3
  > 💬 smash_midskip_simpler2
  > 💬 smash_midskip_simpler4
  > 💬 *choice
  > 💬 BLUE
  > 💬 Note: The BLUE are in the Underworld; we could put them into a different Level_Set.
  > 💬 turn_control
  > 💬 *choice
  > 💬 security_checkpoints
  > 💬 ocean_blue # Not too exciting, just trying to make a level with the squeeze beam.
  > 💬 *choice
  > 💬 ORANGE
  > 💬 skip_miss # Here's one specifically designed to not allow double-floating over the ocean.
  > 💬 bon_voyage
  > 💬 *choice
  > 💬 RAINBOW
  > 💬 get_through
  > 💬 *choice

### clones

- 机制标签: `heroes mirrors`；关卡 10 个（其中分支 *choice 9 处，磁盘命中 10）
  > 💬 Levels that focus on syncing clones without 3D.
  > 💬 Also different hero types with the same input ID.
  > 💬 I think it would be good if the first level or two involved generating the clones yourself with mirrors, sort of as a reminder that you've seen clones before and it's not just an arbitrary new mechanic, so here are some clones levels that involve making the clones yourself
  - `clone_adjust_mirror` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 164
  - `clone_maze` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 159
  > 💬 Managing the offset, with bottomless pits along the edges
  > 💬 We *must* go out after any level inside the clone area, otherwise the player can mess things up by exiting mid-level...  -jblow, 11 November 2023
  - `clone_adjust` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 168
  - `clone_adjust_two_rocks` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 150
  - `pull_line` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 197
  > 💬 clone_adjust_dock
  > 💬 *choice
  > 💬 Arcadia sequence
  - `arcadiav2_big` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 177
  - `arcadia_surprise_big` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 183
  - `arcadia_surprise_big2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 202
  - `button_clone_journey` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 176
  - `pugo` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 194
  > 💬 clone_adjust_* level comment:
  > 💬 These levels that involve managing the offset, and notably not being able to walk into the edges freely because a clone will fall into the water, should probably resemble the cliffs levels in which the bard pushes people into the water. I even think it should maybe mean the clones levels should go after the cliffs levels (though right now clones is on earth and cliffs is in heaven) or maybe a separate subsection clones_cliffs that can only be accessed after both clones and cliffs
  > 💬 Arcadia sequence comment:
  > 💬 There is a not-currently-used level called 'arcadia' that was my first attempt,
  > 💬 then I did arcadiav2, which is set up so that you can't win if you desync your guys
  > 💬 (since this involves pushing a block to a wall, and all the pressure plates are off
  > 💬 walls). I am not sure if this made it less fun, so 'arcadia' is still sitting around
  > 💬 just in case. But also, the door is open to make this into a sequence, say, a second
  > 💬 level that continues the pattern but a bit harder somehow, then a 3rd level that
  > 💬 involves a surprise desync. (If a level were over water, it would provide a surprise
  > 💬 way to get into another guy's chamber, via pushing a boulder into the water, etc).
  > 💬 -jblow, 4 May 2017
  > 💬 arcadiav3 # Patrick cut
  > 💬 arcadiav4 # Patrick cut
  > 💬 arcadiav5 # Patrick cut
  > 💬 Patrick cut
  > 💬 mirror_14_reprise # This is identical in layout to mirror_14, except the clones can fall off the edge now, and this makes it interesting. There are actually two ways to solve this! One way to change the offset is by using the fact that the guy gets blocked if he tries to push both mirrors, and the other is that you can change which diagonal line you are on if your reflected path hits the second mirror. You could force the second solution by making the characters warriors, but forcing the first seems hard.
  > 💬 dont_merge # Patrick cut
  > 💬 clone_adjust_2 # Patrick cut
  > 💬 clone_duet # Patrick cut
  > 💬 clone_flying2 # Moved to heroes_and_mirrors, near fly_and_flip, for simpler overworld gating, since it requires heroes_and_water. This is a bad time to first see priest flying.
  > 💬 Patrick cut because I don't think we want this mechanic?
  > 💬 clone_sacrifice # Clone level, not great. could be simplified/focused.
  > 💬 clone_protection # Patrick cut

### design_illustrations

- 机制标签: `star`；关卡 24 个（其中分支 *choice 10 处，磁盘命中 24）
  > 💬 Note that all the *choice are ignored for gameplay, in this level_set only,
  > 💬 because in the code we always return back after every level if coming from Intro.
  - `heroes1_7` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 68
  - `heroes1_7_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 389
  - `lily_wearing_intro` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 90
  - `tiger_lily_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 238
  - `torcher` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 82
  - `quad_torch_v1` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 88
  - `quad_torch` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 342
  - `worlds_collide_heroes_and_promesst` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 96
  - `worlds_collide_heroes_and_promesst_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 96
  - `worlds_collide_heroes_and_promesst_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 81
  - `worlds_collide_heroes_and_promesst_v4` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 457
  - `across_the_fence_old` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 61
  - `across_the_fence_vtrader_m_p` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 277
  - `sender` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 85
  - `sender_simplified` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 73
  - `sender_simplified_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 214
  - `push_down_a_lot` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 55
  - `push_down_a_lot_small` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 188
  - `catching_up_v0` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 63
  - `catching_up_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 246
  - `strategic_stack` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 62
  - `triple_gate` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 299
  - `height_chooser` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 79
  - `height_chooser_v0` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 214
  > 💬 i_beam_pre_revision
  > 💬 i_beam
  > 💬 i_beam2
  > 💬 i_beam_v2
  > 💬 *choice
  > 💬 bridgey3_old
  > 💬 bridgey3_abstract_art
  > 💬 *choice
  > 💬 purple_wall_around
  > 💬 purple_wall_around_easier_vp
  > 💬 *choice
  > 💬 retvrn
  > 💬 retvrn0
  > 💬 retvrn0b
  > 💬 *choice
  > 💬 drop_operation_v2
  > 💬 drop_operation_v3
  > 💬 *choice

### double_beam_falling

- 机制标签: `beams`；关卡 18 个（其中分支 *choice 15 处，磁盘命中 18）
  > 💬 Double beam falling
  > 💬 (comments and commented-out levels have been moved to spreadsheet)
  - `sky_double_intro0` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 178
  - `sky_double_intro1` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 183
  - `into_the_water_3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 238
  - `air_skating_v6` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 171
  - `monster_drop` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 202
  - `thin_ice_rooms` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 181
  - `through_the_table_e` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 186
  - `through_the_table_f` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 199
  - `dragons_layer` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 204
  - `the_sky_is_falling_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 193
  - `laser_stop_surprise` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 186
  > 💬 fire_from_above_small
  - `fire_from_above_2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 198
  - `hat_maker` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 199
  - `double_up` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 192
  - `annoying_orange_v3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 175
  > 💬 Side sub
  - `side_sub_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 244
  - `side_sub_back` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 210
  - `orange_snake` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 214

### double_beam_falling_dropdown

- 机制标签: `stones beams`；关卡 3 个（其中分支 *choice 3 处，磁盘命中 3）
  > 💬 Dropdown, for orange beams and water:
  - `first_flight` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 131
  - `double_trouble` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 123
  - `orange_cross` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 145

### drafts_arted

- 机制标签: （无）；关卡 787 个（其中分支 *choice 0 处，磁盘命中 786）
  - `rowboat_wizard_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 320
  - `rowboat` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 328
  - `boat_priest_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 392
  - `front_side_bus2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 318
  - `front_side_bus3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 249
  - `drop_off` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 300
  - `bard_movable_island` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 292
  - `bard_movable_island2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 296
  - `pole_vault` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 338
  - `missile_command` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 314
  - `boxes_vs_crystals` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 285
  - `pushing_crystal_near_orange_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 287
  - `safety_gloves` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 298
  - `endpoint_object` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 254
  - `through_maze_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 333
  - `middle_smash` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 338
  - `accidentally_unlock_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 239
  - `limited_offsets` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 217
  - `limited_offsets_surprise_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 277
  - `torc_blocked_easier` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 328
  - `torc_blocked` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 245
  - `oneway_beam` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 238
  - `through_intro` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 254
  - `through_push` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 235
  - `binary_maze` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 196
  - `thief_through` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 232
  - `wall_sneak` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 285
  - `bypass_gates` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 201
  - `corner_loop` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 222
  - `through_sokoban` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 255
  - `double_team` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 162
  - `pushing_near_orange` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 180
  - `pushing_orange` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 209
  - `pulling_near_orange_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 257
  - `jump_the_fence_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 218
  - `orange_beam_deal` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 186
  - `beam_shatter` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 233
  - `simple_trap` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 238
  - `untrap` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 250
  - `pushback` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 254
  - `endpoint_team` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 227
  - `purple_haze` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 211
  - `purple_perpendicular` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 247
  - `endpoint_gates` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 260
  - `slide_rows` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 255
  - `pull_together` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 221
  - `purple_push_pal` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 206
  - `red_handed` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 206
  - `lock_picky` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 167
  - `help_drop` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 214
  - `gem_transport` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 173
  - `gem_transport_2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 168
  - `cleric_isles` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 240
  - `friendly_nudges` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 170
  - `shunt2_alt` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 208
  - `plus_signs_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 191
  - `wizard_finesse_1` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 273
  - `wizard_finesse_2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 270
  - `wizard_finesse_3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 282
  - `wizard_finesse_4` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 289
  - `purple_wizard_maze` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 372
  - `be_aggro_alt_2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 347
  - `orange_wizard_intro` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 302
  - `learning_double` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 252
  - `magic_square` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 268
  - `magic_shield` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 306
  - `see_through` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 320
  - `mini_green_maze` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 248
  - `safe_returns` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 289
  - `two_through_alt_2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 294
  - `double_tempo` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 293
  - `button_playground` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 289
  - `matching_purple` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 261
  - `immobilize` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 285
  - `endpoint_weapon` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 357
  - `invisible_hand` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 250
  - `snipperclips_0_square` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 237
  - `snipperclips_square` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 240
  - `snipperclips_diagonal` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 240
  - `druid_multismash_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 151
  - `zachtronics` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 327
  - `smash_grid_kill` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 225
  - `smash_grid_4` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 217
  - `tempered_glass_red` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 265
  - `red_rooms_v5` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 320
  - `wrapping_mirror_red_v4` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 307
  - `smash_or_dash_vs2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 248
  - `break_through_focused` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 302
  - `cyan_counter_med3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 294
  - `fun_house` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 283
  - `cyan_torc_maze_vs` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 368
  - `top_green_purple_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 277
  - `sidetrack` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 247
  - `purple_wall_around_easier_vp` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 221
  - `across_the_fence_vtrader_m_p` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 277
  - `orange_doubleback` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 208
  - `orange_doubledoubleback` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 211
  - `protrusions` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 180
  - `dual_screen` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 136
  - `mirror_promesst` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 306
  - `mirror_non_turner_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 186
  - `adjust_explorer_v4` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 166
  - `green_torq_mirror_vs4` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 341
  - `purple_clm_v4` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 248
  - `orange_clm_s` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 245
  - `rover_water_purple_v9` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 187
  - `rover_water_purple_sequel_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 249
  - `magic_rover` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 173
  - `remote_work` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 226
  - `double_sideways` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 149
  - `floating_orange_purple` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 195
  - `orange_predicament` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 144
  - `green_crystal_rover` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 172
  - `mirror_rover_orange_2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 202
  - `red_yellow_alter_with_intro_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 222
  - `purple_corner_gem` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 302
  - `gem_clg_v4` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 326
  - `the_spiral` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 258
  - `green_metamirror` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 334
  - `orange_floaty_reflect_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 247
  - `meta_orange_purple` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 209
  - `meta_orange_purple_2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 210
  - `skip_orange_block_c` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 203
  - `through_way` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 196
  - `zachtronics_xor` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 328
  - `stonewalled` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 165
  - `frantic_factory_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 211
  - `skipping_cyan_precise_c_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 236
  - `doorstop` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 232
  - `doorstop_reprise_easier` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 206
  - `glass_beach` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 224
  - `break_send_lily_c` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 192
  - `purple_beam_intro_v2_alt` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 205
  - `faster_than_stone` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 158
  - `hustle_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 159
  - `skipping_near_beams_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 404
  - `skipping_wrapping_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 220
  - `skip_or_sink_r` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 165
  - `skip_wand_v6` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 238
  - `skipping_promesst` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 206
  - `rover_impulse_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 221
  - `rover_advance_c_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 215
  - `rover_shift_p` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 188
  - `submarine` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 193
  - `submarine_far_away` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 219
  - `skip_orange_maze_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 220
  - `orange_skip_place_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 172
  - `skip_orange_wall_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 200
  - `security_checkpoints_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 158
  - `ocean_blue` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 138
  - `rsmash` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 195
  - `endpoint1_skipping` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 201
  - `narrow_passage` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 199
  - `close_circuit` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 194
  - `double_door` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 214
  - `free_ride` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 225
  - `swap_seats` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 202
  - `dragon_drag` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 167
  - `crystal_logistics` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 260
  - `beam_sisters` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 220
  - `corner_trick_easier` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 237
  - `wizards_true_nature` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 233
  - `clone_adjust_mirror` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 164
  - `clone_maze` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 159
  - `clone_adjust` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 168
  - `clone_adjust_two_rocks` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 150
  - `pull_line` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 197
  - `arcadiav2_big` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 177
  - `arcadia_surprise_big` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 183
  - `arcadia_surprise_big2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 202
  - `button_clone_journey` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 176
  - `pugo` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 194
  - `zachtronics_or` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 331
  - `zachtronics_identity` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 315
  - `worlds_collide_heroes_and_promesst_v4` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 457
  - `swapwiz_harder` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 319
  - `ortho2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 172
  - `duality_condensed` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 303
  - `bridgey3_abstract_art` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 212
  - `worlds_collide_mirrors_and_stones_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 228
  - `across_the_fence_vtrader_m_p` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 277
  - `worlds_collide_ps` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 364
  - `purple_wall_around_easier_vp` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 221
  - `worlds_collide_heroes_and_mirrors_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 414
  - `worlds_collide_heroes_and_promesst_v4` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 457
  - `sender_simplified_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 214
  - `worlds_collide_heroes_and_stones` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 476
  - `push_down_a_lot_small` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 188
  - `worlds_collide_alt` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 277
  - `height_chooser_v0` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 214
  - `volcano_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 255
  - `retvrn0` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 254
  - `flamestrike_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 250
  - `catching_up_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 246
  - `height_chooser_v0` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 214
  - `beam_jail_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 272
  - `tiger_lily_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 238
  - `suspend_swapper_hard` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 224
  - `triple_gate` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 299
  - `suspend_directions_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 237
  - `drop_operation_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 228
  - `sky_double_intro0` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 178
  - `sky_double_intro1` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 183
  - `into_the_water_3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 238
  - `air_skating_v6` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 171
  - `monster_drop` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 202
  - `thin_ice_rooms` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 181
  - `through_the_table_e` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 186
  - `through_the_table_f` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 199
  - `dragons_layer` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 204
  - `the_sky_is_falling_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 193
  - `laser_stop_surprise` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 186
  - `fire_from_above_2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 198
  - `hat_maker` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 199
  - `double_up` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 192
  - `annoying_orange_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 175
  - `side_sub_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 244
  - `side_sub_back` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 210
  - `orange_snake` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 214
  - `first_flight` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 131
  - `double_trouble` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 123
  - `orange_cross` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 145
  - `sokobridge_v4` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 172
  - `double_the_fun` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 214
  - `taking_the_lift` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 174
  - `trick_landing` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 217
  - `drop_sokoban` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 184
  - `elevator_cyan` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 177
  - `end1` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 817
  - `suspend_heterogeneous` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 301
  - `suspend_block_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 303
  - `suspend_intro` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 272
  - `one_floor_down_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 278
  - `pink_platforms` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 171
  - `vacuum` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 276
  - `seeing_red` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 284
  - `vertical_promesst_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 240
  - `pachinko_rescue_w` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 276
  - `end2_mirror_3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 202
  - `pachinko` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 243
  - `falling_down` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 237
  - `retro_hooks` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 179
  - `retro` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 252
  - `lily_pull` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 166
  - `lily_pull_intro` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 171
  - `tandem` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 204
  - `escape_bridge` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 236
  - `all_out_goblin_war` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 250
  - `bridgey3_abstract_art` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 212
  - `bridgey2b` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 189
  - `bridgey2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 177
  - `sidestone_zach_2_end2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 284
  - `bridgey` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 180
  - `wolf_boat_carry` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 257
  - `juggle` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 318
  - `vertical_unclone_3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 282
  - `chasm_3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 257
  - `bottom_adjust` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 252
  - `tall_stack` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 214
  - `to_kill_a_goblin` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 389
  - `quick_redirect_v5` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 163
  - `catching_up_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 246
  - `implausible_bridge_2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 270
  - `new_way_mirror_later` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 257
  - `repel` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 138
  - `mission_impossible` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 263
  - `make_shoreline` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 209
  - `bottom_bridge_tall` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 248
  - `bottom_bridge_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 228
  - `overwrite` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 255
  - `implausible_bridge` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 198
  - `drawbridge` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 197
  - `portable_stairs` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 309
  - `vert_mirror_intro` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 264
  - `sender_simplified_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 214
  - `shower` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 164
  - `landmines_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 272
  - `chain_reaction` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 208
  - `end2_mirror1` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 203
  - `end2_mirror_4_islands_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 211
  - `smash_midskip_simpler4` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 195
  - `juggalos` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 222
  - `defender` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 361
  - `retvrn0` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 254
  - `drop_operation_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 228
  - `tricky_endpoint` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 216
  - `hover_corner_4` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 164
  - `hover_corner_3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 197
  - `movable_button` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 242
  - `movable_buttons` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 318
  - `gem_slot_on_lily` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 240
  - `lily_switch_p` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 294
  - `sombreros` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 355
  - `gem_trap` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 286
  - `gem_trap2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 307
  - `negative_space` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 242
  - `numberlink_alt` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 302
  - `breaking_bread` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 279
  - `orange_gem_instant` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 200
  - `boot_cycle_warrior` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 190
  - `goblin_below_intro_same_z` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 235
  - `aggro_which0` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 209
  - `aggro_maze` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 184
  - `chain_gang` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 201
  - `chain_gang3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 207
  - `pass_through_v2_same_z` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 207
  - `heroes1_1` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 296
  - `heroes1_2_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 268
  - `heroes1_3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 330
  - `heroes1_4` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 246
  - `heroes1_4.5` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 287
  - `heroes1_5_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 274
  - `heroes1_7_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 389
  - `heroes1_6` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 240
  - `heroes1_7.5` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 284
  - `heroes1_8_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 272
  - `heroes1_10_inv_v4_b` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 337
  - `heroes1_9` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 241
  - `heroes1_11_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 208
  - `heroes1_13_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 288
  - `heroes1_12_v2_alt` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 272
  - `heroes1_15` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 235
  - `heroes1_16_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 267
  - `heroes1_17` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 278
  - `heroes1_18` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 278
  - `mobile_cover_2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 239
  - `endpoint_holder4` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 234
  - `heroes2_2b` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 250
  - `heroes2_2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 224
  - `heroes2_thief_goblin` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 242
  - `heroes2_3_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 224
  - `heroes2_5_altE` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 372
  - `heroes2_5_no_crystal` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 280
  - `heroes2_5.5v5` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 265
  - `heroes2_6_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 264
  - `heroes2_9` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 295
  - `heroes2_10a_intro` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 253
  - `heroes2_10a` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 248
  - `heroes2_3monster` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 235
  - `heroes2_10` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 273
  - `heroes2_11_v2_easier` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 234
  - `heroes2_12_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 226
  - `heroes2_11_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 203
  - `heroes2_10.5` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 235
  - `one_fire_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 240
  - `heroes2_13` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 176
  - `heroes2_14` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 200
  - `heroes2_15` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 261
  - `heroes2_reprise` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 295
  - `heroes2_16v4` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 219
  - `heroes2_18` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 213
  - `mosh_pit_small` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 198
  - `heroes2_17_intro` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 249
  - `heroes2_17` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 249
  - `heroes2_20` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 205
  - `heroes2_21b` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 188
  - `heroes2_22_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 225
  - `heroes3_10` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 248
  - `heroes3_11_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 282
  - `endpoint_holder3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 175
  - `skip_purple_drop_alt` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 219
  - `heroes3_15_v2`
  - `heroes3_13_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 292
  - `bon_voyage` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 243
  - `3wcn_purple_goblin` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 313
  - `heroes3_1_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 242
  - `heroes3_2_v4` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 260
  - `heroes3_3_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 253
  - `heroes3_4` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 209
  - `heroes3_5` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 304
  - `heroes3_8_thief` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 368
  - `half_journey_vh` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 274
  - `perch_3_rovers` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 144
  - `heroes3_8_v4_alt` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 336
  - `crystal_rover_bridge` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 162
  - `heroes3_14_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 326
  - `crystal_rover_rush` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 152
  - `mirror_crystal_rover` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 133
  - `two_half_togglers` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 234
  - `purple_heart` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 269
  - `victory_lap` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 475
  - `thief_wand` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 232
  - `flame_wand` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 240
  - `swap_and_spin` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 215
  - `wizard_with_a_gun` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 245
  - `bug_spray` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 178
  - `flip_flop_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 234
  - `two_for_one` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 182
  - `gate_shatter` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 186
  - `iodine_clock_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 241
  - `mirror_clocks` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 228
  - `mirror_hallway_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 188
  - `reattachment` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 247
  - `detachment` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 269
  - `blocking_issue` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 218
  - `greenhouse` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 235
  - `bitstring_small` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 241
  - `holes` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 246
  - `double_break` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 230
  - `drop_tool` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 263
  - `wizard_mirror_intro` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 223
  - `regular_mirror_v4` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 238
  - `moving_a_mirror` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 232
  - `moving_three_mirrors` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 195
  - `mirror_dweller` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 254
  - `the_swappers` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 222
  - `tricky_swappers_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 257
  - `close_to_button` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 287
  - `goblin_parity` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 273
  - `clone_goblin` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 416
  - `two_dragon_rooms` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 369
  - `quad_torch` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 342
  - `trick_kills` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 425
  - `fuse` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 292
  - `fly_and_flip` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 284
  - `fire_and_flip` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 314
  - `elope` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 268
  - `walk_the_plank` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 286
  - `red_cross` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 308
  - `oneway_dragon_toast` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 301
  - `crystals_not_stones` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 223
  - `stones_not_crystals` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 227
  - `one_of_each` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 189
  - `one_bird_two_stones` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 200
  - `breath_skip` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 220
  - `indirect_skip` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 188
  - `indirect_skip_2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 203
  - `indirect_skip_3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 237
  - `druids_stone_0_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 158
  - `druid_stone_p` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 145
  - `druids_stone_alt` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 177
  - `druids_stone_2_v4` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 192
  - `island_friends` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 216
  - `wizard_with_a_capital_w` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 190
  - `wizard_with_a_capital_w_2_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 229
  - `slot_machine_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 158
  - `push_against` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 204
  - `come_closer` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 218
  - `useful_stone` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 207
  - `trick_shot` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 223
  - `bard_range4` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 179
  - `bard_range5` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 203
  - `bard_range6` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 182
  - `pull_it_v4` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 192
  - `pull_teamwork_alt` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 223
  - `sprint_skip0` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 222
  - `watergate` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 218
  - `stone_stopper_intro` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 222
  - `another_stone_stopper` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 228
  - `stone_stopper3_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 273
  - `stone_stopper5` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 232
  - `skipping_with_dragon` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 240
  - `walk_into_fire` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 245
  - `hot_swap` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 241
  - `toggler00` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 225
  - `pull_skip_twins_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 297
  - `dipping_your_toes_in` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 271
  - `crystal_bridges` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 297
  - `push_and_pull_zach` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 238
  - `quadrants_follow_up` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 355
  - `quadrants` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 339
  - `drowner` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 329
  - `surrounded` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 378
  - `dont_push_the_button` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 288
  - `detonator` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 294
  - `a_wiz_out_of_water` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 295
  - `island_hopping` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 260
  - `dunk_tank_alt` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 258
  - `floating_gardens` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 204
  - `four_horsemen` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 203
  - `put_down_roots_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 278
  - `prisoners_dilemma_alt` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 239
  - `beam_me_up_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 292
  - `gully_alt` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 281
  - `easy_situation_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 270
  - `one_vs_three` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 254
  - `synchronized_swimmers` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 285
  - `dragon_compass` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 243
  - `new_cleric_fly` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 243
  - `little_faith_alt` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 193
  - `both_ways` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 250
  - `flamethrower` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 210
  - `killer_wizard` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 229
  - `partial_pull` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 255
  - `cleric_fly_intro3_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 228
  - `monster_mover` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 259
  - `team_building_exercise` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 228
  - `tug_boat` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 261
  - `on_command` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 265
  - `bard_stack_intro` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 236
  - `goblin_express` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 295
  - `baby_steps_line` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 303
  - `surfing_lesson_alt` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 247
  - `bard_range3_with_intro` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 291
  - `gated_twice_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 263
  - `gated_twice_thief_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 259
  - `connect_the_dots_v5` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 235
  - `pulling_pedestals` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 248
  - `thief_stack` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 277
  - `zombie_graves_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 211
  - `dragon_bridge` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 225
  - `loading_docks_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 227
  - `assassins_creed` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 223
  - `high_horse` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 323
  - `personal_assistant_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 203
  - `push_down_a_lot_small` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 188
  - `my_first_stack` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 241
  - `single_out` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 131
  - `jenga_shortstack_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 157
  - `jenga_easier` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 186
  - `archways_2_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 192
  - `archways_4` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 189
  - `hat_chain_vp` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 220
  - `cliff_duo` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 139
  - `going_up_v4` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 225
  - `automatic_door_v5` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 182
  - `magicians_assistant_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 181
  - `falloff_intro` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 170
  - `falloff_4` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 203
  - `falloff_kill_goblins_v6` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 207
  - `falloff_dragons` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 203
  - `erosion_alt` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 245
  - `magic_tower` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 240
  - `mountain_music` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 260
  - `out_of_range_v4` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 281
  - `musical_staircase_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 158
  - `sticky` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 291
  - `tippy_intro` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 382
  - `tippy_towers_1` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 226
  - `tippy_towers_4` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 227
  - `high_shelf_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 229
  - `jump_to_pillar_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 267
  - `i_beam_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 285
  - `bard_must_stack4_fix` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 267
  - `bard_triangle` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 245
  - `no_charm` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 191
  - `stones_below_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 199
  - `sky_druid_kill` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 209
  - `sky_druid_kill_tall_2_goblins` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 209
  - `weaklings_bard_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 184
  - `stopper_topper_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 154
  - `sky_druid_tree_ex` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 208
  - `druid_3d_beam` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 194
  - `sky_druid_maze` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 203
  - `sky_druid_one` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 210
  - `priest_descent_simpler` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 145
  - `priest_button_3d_revised` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 199
  - `priest_3d_goblin_pass` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 140
  - `fire_stairs_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 209
  - `fire_stairs_part_2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 255
  - `priest_3d_intro_dragon_v4` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 236
  - `priest_warrior_descent` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 288
  - `priest_bottom_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 319
  - `from_the_depths` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 276
  - `priest_two_warriors_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 227
  - `monster_stack` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 200
  - `catching_fire_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 235
  - `frame_advance_v5` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 229
  - `priest_traverse_e_fence` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 266
  - `stuck_up_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 217
  - `intro` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 1534
  - `jenga_dispenser` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 219
  - `wizards_true_nature` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 233
  - `mega_merge_v5` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 190
  - `push_down_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 183
  - `mega_clone_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 229
  - `water_bender_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 218
  - `double_sided_skip` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 190
  - `wrapping_magic_mirror_2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 185
  - `torus_mirrors` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 107
  - `raft_corners_4x4` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 174
  - `raft_corners_2_small` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 190
  - `raft_corners_alt_3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 143
  - `zach_lilies_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 318
  - `mirror_u` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 368
  - `mirror_flip_donut` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 293
  - `in_a_flash_alt` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 331
  - `in_a_flash_alt_back` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 334
  - `river_maze_clear_tenacious_race_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 340
  - `river_rates_button` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 385
  - `river_rates_jagged` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 397
  - `metamirror_same_dir_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 138
  - `metamirror_same_dir_2_alt_2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 142
  - `metamirror_same_dir_3_alt_2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 115
  - `metamirror_same_dir_5_alt` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 150
  - `metamirror_different_dir_alt` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 150
  - `metamirror_different_dir_3_alt` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 189
  - `metamirror_different_dir_2_alt` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 144
  - `metamirror_block_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 153
  - `metamirror_c_alt` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 140
  - `two_metamirrors` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 107
  - `mirror_1` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 156
  - `mirror_2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 143
  - `mirror_3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 179
  - `mirror_4` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 170
  - `mirror_5` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 152
  - `mirror_6_alt` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 173
  - `mirror_7` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 152
  - `mirror_8_v5` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 158
  - `mirror_11` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 151
  - `mirror_12` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 136
  - `mirror_13` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 153
  - `mirror_14` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 137
  - `mirror_15` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 166
  - `mirror_19` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 144
  - `mirror_17` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 146
  - `mirror_sink` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 133
  - `mirror_20` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 137
  - `mirror_18` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 116
  - `mirror_21` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 150
  - `mirror_22_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 148
  - `mirror_factory_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 127
  - `mirror_pals` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 143
  - `walk_it_over` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 163
  - `mirror_10_alt2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 125
  - `mundane_mirror` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 115
  - `mirror_10_b_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 151
  - `mirror_10_d` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 128
  - `3wc_into_forest_v7` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 248
  - `mirror_stone_intro` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 159
  - `catch_and_drop` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 284
  - `catch_and_throw` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 209
  - `reflect_momentum` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 284
  - `sidestone_zach_1` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 308
  - `sidestone_zach_2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 239
  - `sidestone_zach_3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 167
  - `sidestone_zach_4` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 162
  - `launch_and_collect` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 312
  - `lilyruga_simpler` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 235
  - `bad_aim_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 286
  - `multipurpose` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 283
  - `wide_ocean` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 230
  - `zig_zag` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 232
  - `ricochet_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 429
  - `run_the_clock_alt` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 366
  - `wider_ocean` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 382
  - `reel_it_in` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 183
  - `make_it_happen_v6` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 338
  - `new_new_new_slam` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 185
  - `airmail` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 161
  - `thats_my_ride` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 167
  - `place_to_stand` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 159
  - `emergency_brake` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 175
  - `short_ride_option_b` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 178
  - `highway` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 162
  - `cancel_out` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 178
  - `mirror_motion` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 166
  - `diag_slide` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 189
  - `the_long_way` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 220
  - `ride_together` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 166
  - `two_bounce_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 221
  - `first_diversions` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 280
  - `far_river` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 247
  - `ditching_cargo` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 287
  - `unblock_block_alt` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 271
  - `there_and_back` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 209
  - `sink_together` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 202
  - `in_the_way_alt_3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 252
  - `river_dictionary_alt_up` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 356
  - `river_push_v4` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 313
  - `coax_a_lot` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 252
  - `already_dropped_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 219
  - `two_step` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 218
  - `moving_bridge` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 249
  - `square_dance` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 214
  - `use_and_remove` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 250
  - `infinite_crystal_hack_v5` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 253
  - `river_plinko_v2_actual` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 383
  - `trader_descend` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 175
  - `cliff_hopping` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 223
  - `make_a_right_simpler` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 202
  - `make_a_right` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 260
  - `learn_to_catch_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 228
  - `trust_falls` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 221
  - `falling_blocker_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 196
  - `pillars` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 242
  - `long_platform_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 342
  - `triple_gate` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 299
  - `blind_spot_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 246
  - `bothersome_mirror` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 264
  - `hat_tricks_0_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 258
  - `omnimirror_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 285
  - `goblin_parity_3d` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 261
  - `no_murder_weapon_wizard` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 209
  - `no_murder_weapon_0` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 222
  - `dragonsweeper` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 226
  - `green_goblins` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 266
  - `en_root_alt` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 226
  - `button_and_beam_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 237
  - `thief_dragger_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 232
  - `open_monster` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 215
  - `monster_promesst_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 152
  - `goblin_two_rovers_alt` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 168
  - `rotating_cavalry_spaced` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 178
  - `simultaneous_x` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 274
  - `simultaneous_x_surprise` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 317
  - `lazy_susan_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 364
  - `fail_to_mirror_sequence_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 442
  - `three_artifacts_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 427
  - `magnitudes_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 682
  - `quadruple_skip` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 102
  - `triple_skip` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 183
  - `wand_reintro` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 318
  - `battle_royale_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 379
  - `orange_mirror_walk_button` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 218
  - `ice_climbers` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 227
  - `orange_water_button_vdouble_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 212
  - `orange_water_button_vfour_alter` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 207
  - `how_to_train_your_dragon` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 190
  - `promesst1_streamlined` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 444
  - `promesst2_streamlined` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 345
  - `beam_rooms` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 192
  - `pushy` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 381
  - `forbidden_room` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 291
  - `gem_pushers` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 297
  - `target_practice_gem` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 222
  - `right_hand_man` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 298
  - `green_revolution` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 309
  - `torcoban_2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 264
  - `blue_revolution_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 268
  - `promesst2.5_deeper` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 306
  - `jenga_assorted` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 205
  - `grid_hopping0` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 139
  - `far_cl_no_walls_pit` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 239
  - `crystal_rover_intro` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 264
  - `side_slide_intro_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 310
  - `multipush_for_me2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 263
  - `side_kick` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 273
  - `dragon_on_the_wall` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 262
  - `lily_falls_intro_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 242
  - `many_falls` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 271
  - `delay_time_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 319
  - `pool_pal_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 259
  - `sunk_cost_2_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 238
  - `on_the_rocks` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 351
  - `button_shut_in` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 362
  - `tiger_lily_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 238
  - `carry_lily` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 142
  - `removal_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 171
  - `skip_stack_1` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 273
  - `skip_stack_2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 291
  - `skip_stack_3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 252
  - `depositor_thief` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 307
  - `depositor_bard` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 288
  - `turn_control_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 214
  - `spin_heroes` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 253
  - `spray_and_pray` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 202
  - `rotator` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 200
  - `spin_doctors_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 243
  - `the_waterfall_v4` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 274
  - `priest_water_back_goblin` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 257
  - `priest_water_back_place_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 228
  - `skipping_stones` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 387
  - `time_tutorial` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 191
  - `skipping_pals` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 531
  - `skipping_shores_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 351
  - `green_hat` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 211
  - `its_a_tall_order` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 275
  - `stasis_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 234
  - `bard_metamirror` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 162
  - `mirror_the_unmirrorable_mirror` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 222
  - `druid_metamirror` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 166
  - `moving_through_mirrors_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 387
  - `busy_beaver` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 212
  - `hanoi_3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 340
  - `pigeonhole_squished` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 277
  - `goblin_hat_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 257
  - `special_move` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 192
  - `buff_explorer` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 209
  - `stay_lit` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 180
  - `cyan_bridge_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 215
  - `under_pressure` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 209
  - `strong_monsters_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 233
  - `floorhands_v5` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 244
  - `druid_vertical_mirror` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 282
  - `crystal_island` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 209
  - `army_v5` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 222
  - `base_jump` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 221
  - `hyper_jump` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 226
  - `hyper_jump_2c` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 326
  - `self_teleporting` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 162
  - `wrapping_mirror0` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 160
  - `wrapping_mirror0_relatively_prime` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 151
  - `the_line_must_be_drawn_HERE` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 117
  - `wrapping_mirror_alt` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 155
  - `lemonade_tng_stages_towers_no_float` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 289
  - `lemonade` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 389

### drafts_good_looking

- 机制标签: （无）；关卡 92 个（其中分支 *choice 0 处，磁盘命中 92）
  - `hyper_jump` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 226
  - `goblin_hat_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 257
  - `purple_heart` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 269
  - `no_murder_weapon_0` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 222
  - `green_revolution` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 309
  - `pugo` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 194
  - `goblin_hat_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 257
  - `dragon_on_the_wall` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 262
  - `base_jump` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 221
  - `mirror_the_unmirrorable_mirror` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 222
  - `priest_3d_intro_dragon_v4` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 236
  - `fire_stairs_part_2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 255
  - `to_kill_a_goblin` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 389
  - `hat_maker` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 199
  - `orange_snake` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 214
  - `cliff_hopping` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 223
  - `vacuum` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 276
  - `bottom_bridge_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 228
  - `sky_druid_tree_ex` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 208
  - `falloff_kill_goblins_v6` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 207
  - `stuck_up_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 217
  - `breaking_bread` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 279
  - `mission_impossible` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 263
  - `orange_doubledoubleback` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 211
  - `dragonsweeper` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 226
  - `busy_beaver` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 212
  - `new_cleric_fly` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 243
  - `button_shut_in` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 362
  - `pass_through_v2_same_z` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 207
  - `crystal_bridges` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 297
  - `air_skating_v6` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 171
  - `dragons_layer` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 204
  - `bard_range3_with_intro` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 291
  - `pulling_pedestals` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 248
  - `spin_heroes` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 253
  - `monster_stack` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 200
  - `aggro_maze` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 184
  - `oneway_beam` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 238
  - `priest_traverse_e_fence` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 266
  - `numberlink_alt` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 302
  - `grid_hopping0` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 139
  - `removal_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 171
  - `hanoi_3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 340
  - `under_pressure` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 209
  - `cyan_bridge_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 215
  - `high_shelf_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 229
  - `push_down_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 183
  - `open_monster` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 215
  - `skip_orange_maze_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 220
  - `priest_button_3d_revised` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 199
  - `chain_gang` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 201
  - `double_break` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 230
  - `archways_2_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 192
  - `falling_down` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 237
  - `team_building_exercise` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 228
  - `monster_mover` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 259
  - `synchronized_swimmers` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 285
  - `endpoint_gates` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 260
  - `through_maze_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 333
  - `pool_pal_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 259
  - `many_falls` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 271
  - `heroes2_5_no_crystal` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 280
  - `gem_trap2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 307
  - `thin_ice_rooms` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 181
  - `surfing_lesson_alt` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 247
  - `priest_bottom_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 319
  - `pachinko_rescue_w` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 276
  > 💬 Ethan List
  - `bard_stack_intro` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 236
  - `falloff_intro` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 170
  - `metamirror_same_dir_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 138
  - `goblin_parity_3d` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 261
  - `goblin_below_intro_same_z` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 235
  - `bard_must_stack4_fix` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 267
  - `boxes_vs_crystals` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 285
  - `all_out_goblin_war` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 250
  - `skip_stack_3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 252
  - `mountain_music` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 260
  - `sky_druid_kill` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 209
  - `fire_stairs_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 209
  - `sky_double_intro1` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 183
  - `orange_doubleback` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 208
  - `fuse` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 292
  - `jenga_easier` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 186
  - `lily_pull_intro` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 171
  - `bottom_bridge_tall` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 248
  - `orange_predicament` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 144
  - `zachtronics` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 327
  - `duality_condensed` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 303
  - `torus_blocks_alt_v4` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 152
  - `tall_stack` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 214
  - `weaklings_bard_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 184
  - `pigeonhole_squished` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 277

### drafts_story

- 机制标签: （无）；关卡 230 个（其中分支 *choice 0 处，磁盘命中 225）
  - `through_intro` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 254
  - `through_push` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 235
  - `binary_maze` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 196
  - `beam_shatter` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 233
  - `red_handed` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 206
  - `gem_transport` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 173
  - `gem_transport_2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 168
  - `friendly_nudges` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 170
  - `orange_wizard_intro` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 302
  - `learning_double` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 252
  - `magic_square` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 268
  - `magic_shield` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 306
  - `see_through` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 320
  - `mini_green_maze` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 248
  - `safe_returns` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 289
  - `two_through_alt_2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 294
  - `double_tempo` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 293
  - `button_playground` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 289
  - `matching_purple` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 261
  - `through_way` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 196
  - `stonewalled` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 165
  - `purple_beam_intro_v2_alt` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 205
  - `skipping_near_beams_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 404
  - `skipping_wrapping_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 220
  - `rover_impulse_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 221
  - `rover_advance_c_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 215
  - `rover_shift_p` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 188
  - `submarine` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 193
  - `submarine_far_away` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 219
  - `worlds_collide_heroes_and_promesst_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 81
  - `bridgey3_abstract_art` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 212
  - `triple_gate` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 299
  - `monster_drop` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 202
  - `dragons_layer` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 204
  - `the_sky_is_falling_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 193
  - `end2_heroes_1_2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 293
  - `end2_heroes_1_5` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 303
  - `heroes1_1` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 296
  - `heroes1_2_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 268
  - `heroes1_3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 330
  - `heroes1_4` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 246
  - `heroes1_4.5` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 287
  - `heroes1_5_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 274
  - `heroes1_7_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 389
  - `heroes1_6` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 240
  - `heroes1_7.5` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 284
  - `heroes1_8_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 272
  - `heroes1_10_inv_v4_b` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 337
  - `heroes1_9` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 241
  - `heroes1_11_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 208
  - `heroes1_13_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 288
  - `heroes1_12_v2_alt` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 272
  - `heroes1_15` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 235
  - `heroes1_16_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 267
  - `heroes1_17` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 278
  - `heroes1_18` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 278
  - `heroes1_19_jail` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 297
  - `heroes1_21_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 305
  - `heroes2_2b` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 250
  - `heroes2_2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 224
  - `heroes2_thief_goblin` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 242
  - `heroes2_3_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 224
  - `heroes2_5_altE` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 372
  - `heroes2_5_no_crystal` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 280
  - `heroes2_5.5v5` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 265
  - `heroes2_6_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 264
  - `heroes2_9` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 295
  - `heroes2_10a_intro` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 253
  - `heroes2_10a` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 248
  - `heroes2_3monster` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 235
  - `heroes2_10` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 273
  - `heroes2_11_v2_easier` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 234
  - `heroes2_12_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 226
  - `heroes2_11_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 203
  - `heroes2_10.5` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 235
  - `one_fire_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 240
  - `heroes2_14` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 200
  - `heroes2_15` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 261
  - `heroes2_reprise` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 295
  - `heroes2_16v4` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 219
  - `heroes2_18` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 213
  - `heroes2_21b` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 188
  - `mosh_pit_small` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 198
  - `heroes2_17_intro` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 249
  - `heroes2_17` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 249
  - `heroes2_20` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 205
  - `heroes2_22_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 225
  - `heroes3_10` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 248
  - `heroes3_11_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 282
  - `druid_and_dragon` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 241
  - `wizard_and_druid_alt` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 302
  - `heroes3_15_v2`
  - `heroes3_13_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 292
  - `heroes3_druid_b_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 231
  - `heroes3_druid_a` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 326
  - `heroes3_1_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 242
  - `heroes3_2_v4` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 260
  - `heroes3_3_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 253
  - `heroes3_4` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 209
  - `heroes3_5` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 304
  - `heroes3_8_thief` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 368
  - `heroes3_6_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 405
  - `heroes3_7_v4` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 328
  - `heroes3_8_v4_alt` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 336
  - `heroes3_8_v3_alt3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 381
  - `heroes3_14_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 326
  - `heroes3_16_v4_alt` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 233
  - `compactor_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 243
  - `gatekeeping_v2`
  - `heroes3_21_condensed` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 243
  - `victory_lap` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 475
  - `thief_wand` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 232
  - `flame_wand` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 240
  - `bug_spray` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 178
  - `crystals_not_stones` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 223
  - `stones_not_crystals` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 227
  - `one_bird_two_stones` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 200
  - `breath_skip` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 220
  - `indirect_skip` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 188
  - `indirect_skip_2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 203
  - `druids_stone_0_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 158
  - `druids_stone_alt` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 177
  - `druids_stone_2_v4` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 192
  - `island_friends` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 216
  - `wizard_with_a_capital_w` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 190
  - `wizard_with_a_capital_w_2_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 229
  - `pull_it_v4` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 192
  - `pull_teamwork_alt` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 223
  - `sprint_skip0` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 222
  - `watergate` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 218
  - `dipping_your_toes_in` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 271
  - `crystal_bridges` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 297
  - `push_and_pull_zach` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 238
  - `quadrants_follow_up` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 355
  - `drowner` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 329
  - `surrounded` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 378
  - `dont_push_the_button` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 288
  - `detonator` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 294
  - `gated_twice_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 263
  - `gated_twice_thief_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 259
  - `connect_the_dots_v5` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 235
  - `intro` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 1534
  - `3d_intro_vanilla` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 196
  - `push_down_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 183
  - `sister_staircase_harder` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 165
  - `carry_simplified` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 181
  - `3d_intro_mirrors` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 208
  - `metamirror_same_dir_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 138
  - `metamirror_same_dir_2_alt_2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 142
  - `metamirror_same_dir_3_alt_2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 115
  - `metamirror_same_dir_5_alt` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 150
  - `metamirror_different_dir_alt` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 150
  - `metamirror_different_dir_3_alt` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 189
  - `metamirror_different_dir_2_alt` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 144
  - `metamirror_block_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 153
  - `metamirror_c_alt` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 140
  - `two_metamirrors` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 107
  - `mirror_0`
  - `mirror_1` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 156
  - `mirror_2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 143
  - `mirror_3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 179
  - `mirror_4` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 170
  - `mirror_5` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 152
  - `mirror_6_alt` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 173
  - `mirror_7` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 152
  - `mirror_8_v5` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 158
  - `mirror_11` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 151
  - `mirror_12` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 136
  - `mirror_13` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 153
  - `mirror_14` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 137
  - `mirror_15` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 166
  - `mirror_19` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 144
  - `mirror_17` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 146
  - `mirror_sink` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 133
  - `mirror_20` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 137
  - `mirror_18` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 116
  - `mirror_21` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 150
  - `mirror_22_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 148
  - `mirror_factory_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 127
  - `mirror_pals` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 143
  - `walk_it_over` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 163
  - `mirror_finale`
  - `mirror_stone_intro` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 159
  - `catch_and_drop` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 284
  - `catch_and_throw` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 209
  - `sidestone_zach_1` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 308
  - `sidestone_zach_2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 239
  - `sidestone_zach_3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 167
  - `sidestone_zach_4` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 162
  - `new_new_new_slam` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 185
  - `airmail` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 161
  - `thats_my_ride` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 167
  - `place_to_stand` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 159
  - `emergency_brake` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 175
  - `short_ride_option_b` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 178
  - `highway` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 162
  - `in_the_way_alt_3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 252
  - `river_dictionary_alt_up` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 356
  - `trader_descend` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 175
  - `cliff_hopping` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 223
  - `learn_to_catch_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 228
  - `trust_falls` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 221
  - `falling_blocker_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 196
  - `long_platform_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 342
  - `triple_gate` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 299
  - `blind_spot_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 246
  - `magnitudes_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 682
  - `promesst1_streamlined` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 444
  - `depositor_bard` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 288
  - `turn_control_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 214
  - `spin_heroes` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 253
  - `spray_and_pray` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 202
  - `rotator` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 200
  - `spin_doctors_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 243
  - `skipping_stones` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 387
  - `new_way_mirror_later` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 257
  - `quick_redirect_v5` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 163
  - `to_kill_a_goblin` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 389
  - `bridgey` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 180
  - `bridgey2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 177
  - `bridgey2b` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 189
  - `bridgey3_abstract_art` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 212
  - `all_out_goblin_war` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 250
  - `tandem` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 204
  - `worlds_collide_alt` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 277
  - `worlds_collide_heroes_and_stones` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 476
  - `worlds_collide_heroes_and_promesst_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 81
  - `worlds_collide_heroes_and_mirrors_v2_flip`
  - `worlds_collide_ps` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 364
  - `worlds_collide_mirrors_and_stones_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 228

### drafts_trailer

- 机制标签: （无）；关卡 3 个（其中分支 *choice 0 处，磁盘命中 3）
  - `quad_torch` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 342
  - `break_send_lily_c` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 192
  - `reflect_momentum` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 284

### elevators

- 机制标签: `beams`；关卡 6 个（其中分支 *choice 6 处，磁盘命中 6）
  > 💬 Elevators as a 3D gameplay element
  > 💬 (comments and commented-out levels have been moved to spreadsheet)
  - `sokobridge_v4` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 172
  - `double_the_fun` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 214
  - `taking_the_lift` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 174
  > 💬 no_call
  > 💬 *choice
  - `trick_landing` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 217
  - `drop_sokoban` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 184
  - `elevator_cyan` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 177
  > 💬 gap
  > 💬 *choice

### endgame1

- 机制标签: `end1`；关卡 1 个（其中分支 *choice 1 处，磁盘命中 1）
  - `end1` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 817
  > 💬 3wc_into_forest_v7
  > 💬 *choice
  > 💬 3wc_purple_goblin_v4
  > 💬 *choice
  > 💬 3wc_stonehenge_v3
  > 💬 *choice
  > 💬 3wc_smp_parade_v3
  > 💬 *choice
  > 💬 4wc_dragon_cyan_s_v2
  > 💬 *choice

### endgame2

- 机制标签: `end2`；关卡 27 个（其中分支 *choice 15 处，磁盘命中 27）
  > 💬 Heroes
  - `allocate_heroes_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 357
  - `end2_heroes_1_2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 293
  - `end2_heroes_1_5` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 303
  - `prelude_priest_water_goblins_only` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 331
  - `see_no_evil` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 277
  > 💬 Stones
  - `place_lily_pushstyle_v6` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 284
  - `three_birds_push` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 342
  - `stones_prelude` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 223
  - `end2_river_place` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 404
  > 💬 Mirrors
  - `end2_mirror_3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 202
  - `mirror_prelude_v2_fix` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 138
  - `peak_toggle` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 279
  > 💬 Promesst
  - `place_slot_4x4_pushstyle` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 283
  - `color_picker` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 251
  - `place_promesst_rooms` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 276
  - `promesst_prelude_pushstyle` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 301
  - `elevator_mechanic` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 263
  > 💬 #
  > 💬 # HM:
  > 💬 #
  - `floor_plan_v3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 464
  > 💬 #
  > 💬 # HS:
  > 💬 #
  - `who_you_gonna_call` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 256
  - `end2_monster_connect` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 285
  > 💬 #
  > 💬 # HP:
  > 💬 #
  - `end2_prism_hp` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 344
  > 💬 #
  > 💬 # MS:
  > 💬 #
  - `chart_a_course` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 222
  - `sidestone_zach_2_end2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 284
  > 💬 #
  > 💬 # MP:
  > 💬 #
  - `stack_prelude_pushstyle` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 213
  - `laser_pointer` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 212
  > 💬 #
  > 💬 # SP:
  > 💬 #
  - `stone_economy` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 248
  - `all_together_now` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 448
  > 💬 ####
  > 💬 #### Finale:
  > 💬 ####
  > 💬 end2_finale
  > 💬 *choice

### endgame3

- 机制标签: `end3`；关卡 40 个（其中分支 *choice 27 处，磁盘命中 40）
  > 💬 Section 1: 2-3 intro levels for each of the 4 games.
  > 💬 Needs judging:
  - `allocate_heroes_end3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 312
  - `end3_heroes_1` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 372
  - `end3_mirror_1_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 219
  - `end3_mirror_2_alt2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 231
  - `end3_skipping_1` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 190
  - `end3_skipping_red` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 221
  - `best_beam_colors` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 332
  - `end3_promesst_red` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 869
  > 💬 Section 2: Topics (as if it were developer commentary; a room per topic probably):
  > 💬 Implementing an Idea: The intro to really designing more-complex levels.
  > 💬 Clarity of Central Idea: Do you know what this puzzle was about? How strong is the idea?
  > 💬 Readability: How well does the geometry and framing communicate the idea? Focuses on nuances and whether they clarify or make more confusing.
  > 💬 Focus / On-Topicness (any preliminary or contributing puzzles must be on-topic; remove excess Sokobanning.)
  > 💬 Lightweightness (don't use more geometry or objects than is necessary).
  > 💬 Exploits (and how to mess up your level by the least amount to fix an exploit;
  > 💬 minimize the amount by which it is made more ugly).
  > 💬 (This list of topics is provisional, To Be Revised depending on how well these come out)
  > 💬 --- Implementing an Idea ---
  > 💬 --- Lightweightness ---
  > 💬 make_sokoban is about, make sure all the geometry is used... if a room is not needed,
  > 💬 it should not be there. (But it is kind of in reverse where the rooms are given).
  - `design_corner` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 330
  - `make_sokoban` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 382
  - `make_shoreline` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 209
  - `design_fts` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 257
  - `make_oneway` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 268
  - `make_thief_goblin_maze_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 315
  > 💬 --- Exploits ---
  - `river_exploit_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 238
  > 💬 fix_exploit is a very nice level. We want to add some text to it, saying
  > 💬 "Hey, first understand the level and how it's *meant* to be solved, then
  > 💬 figure out why it's exploitable..."
  > 💬 (original Zach level).
  - `fix_exploit` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 189
  > 💬 fix_exploit_simplify_skipping
  - `wizard_jailbreak_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 335
  - `fix_exploit_promesst_overworld` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 453
  - `end2_clone_divergence` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 174
  - `end2_clone_divergence_2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 170
  > 💬 Same here ... making sure all sides of the pond are used.
  > 💬 shape_pond
  > 💬 --- Clarity of the Central Idea ---
  - `simplify_wizard` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 328
  - `simplify_skipping` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 321
  > 💬 --- Readability of Level ---
  - `end2_mirror1` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 203
  - `end2_mirror_4_islands_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 211
  - `end3_denoise_pool` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 317
  - `end3_redundant_beams` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 355
  > 💬 --- Focus / On-Topicness ---
  > 💬 use_druid      # Old level. "If the Druid is in a level, make sure his ability makes sense and is necessary."
  > 💬 use_abilities  # Old level. A more-complex version of use_druid. This is too hard and gnarly; we should consider a version where at least one block is already fixed in place, to reduce the dimensionality of the puzzle and also provide an anchor for thinking about the puzzle: in what part of the map are we talking about, what general shape are we talking about, etc. (But first we have to solve Zach's puzzle since the solution was not ever written down?? The hard part seems to be figuring out how to make the Warrior necessary.) *** OR *** we could just remove the constraint of things being in columns, which is not really germane to the central idea (thus increases focus??), and just let players drop 5+ blocks wherever they want in the grid (though this might be harder to judge from the code......)
  - `end3_off_topic_alt` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 458
  - `end3_off_topic_mirror` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 327
  - `end3_off_topic_heroes` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 433
  - `end3_reorder_skipping_fix` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 311
  - `end3_reorder_mirror` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 493
  > 💬 Aesthetics
  > 💬 environment_art
  - `environment_art_grid` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 173
  - `environment_art_background` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 349
  - `environment_art_objects` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 279
  > 💬 Pipeline
  - `end3_pipeline_setup` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 116
  - `end3_pipeline_design` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 149
  - `end3_pipeline_cleanup` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 145
  - `end3_pipeline_cut` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 144
  - `end3_pipeline_reorder` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 145
  > 💬 end3_pipeline_exploit # deprecated
  - `end3_pipeline_aesthetics` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 332
  > 💬 Extra / Junk Levels that don't seem good enough, but we might use
  > 💬 for ideas:

### flat_things

- 机制标签: `mirrors stones`；关卡 5 个（其中分支 *choice 5 处，磁盘命中 5）
  - `movable_button` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 242
  - `movable_buttons` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 318
  - `gem_slot_on_lily` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 240
  - `lily_switch_p` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 294
  - `sombreros` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 355
  > 💬 goal_kick
  > 💬 *choice
  > 💬 From Nachama:
  > 💬 lily_switch # Good! -Patrick
  > 💬 lily_switch_v2
  > 💬 lily_switch_2
  > 💬 lily_switch_2_v2
  > 💬 lily_switch_3
  > 💬 lily_switch_4

### gems

- 机制标签: `heroes beams`；关卡 7 个（其中分支 *choice 6 处，磁盘命中 7）
  > 💬 Underworld piled-up gems room and related areas
  > 💬 In a lot of levels, gems are completely ignored. Here are some levels that use gems.
  > 💬 Actually has no beams! But relies pickily on the rule that Explorer guy can't just drop gems anywhere.
  > 💬 Let's put it in the underworld since it is weird that way:
  > 💬 tricky_wizard
  > 💬 *choice
  > 💬 Currently in underworld, but, maybe not that good of a level?
  > 💬 Marked broken currently:
  > 💬 two_laser_traps
  - `gem_trap` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 286
  - `gem_trap2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 307
  > 💬 Walk on gems
  - `negative_space` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 242
  - `numberlink_alt` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 302
  > 💬 Weird promesst guy gem duplication level
  - `breaking_bread` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 279
  > 💬 Gem beams
  - `orange_gem_instant` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 200
  - `boot_cycle_warrior` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 190
  > 💬 Promesst dragon
  > 💬 baby_dragon_rooms
  > 💬 *choice

### goblin_rotation

- 机制标签: `beams`；关卡 6 个（其中分支 *choice 5 处，磁盘命中 6）
  > 💬 Goblin rotation
  > 💬 (comments + commented-out levels have been moved to spreadsheet)
  - `goblin_below_intro_same_z` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 235
  - `aggro_which0` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 209
  - `aggro_maze` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 184
  - `chain_gang` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 201
  - `chain_gang3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 207
  > 💬 aggro_thief5_same_z
  > 💬 *choice
  - `pass_through_v2_same_z` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 207

### heroes1

- 机制标签: `heroes`；关卡 21 个（其中分支 *choice 7 处，磁盘命中 21）
  > 💬 # Magistrate introes Ratley, says he will leave him duties, such as handling prisoners like... this guy.
  - `heroes1_1` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 296
  > 💬 # Got to find Tif, she'll know where the Magistrate is fleeing to. She likes to eavesdrop.
  - `heroes1_2_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 268
  - `heroes1_3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 330
  - `heroes1_4` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 246
  > 💬 # Magistrate introes Thief, says different characters have their different talents and tendencies. You must watch that they don't get the best of you.
  - `heroes1_4.5` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 287
  - `heroes1_5_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 274
  - `heroes1_7_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 389
  - `heroes1_6` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 240
  > 💬 # Magistrate introes Wizard, tauntingly... look, he can't get out from here. Understand your opponents' weaknesses!
  > 💬 # "You still haven't paid us for the appraisal!"
  - `heroes1_7.5` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 284
  - `heroes1_8_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 272
  - `heroes1_10_inv_v4_b` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 337
  - `heroes1_9` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 241
  > 💬 # Warrior + Wizard
  - `heroes1_11_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 208
  - `heroes1_13_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 288
  > 💬 # Wizard + Thief
  - `heroes1_12_v2_alt` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 272
  > 💬 # Warrior + Wizard
  - `heroes1_15` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 235
  > 💬 # Warrior, Thief, Wizard
  - `heroes1_16_v3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 267
  > 💬 # Warrior, Thief, Wizard
  - `heroes1_17` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 278
  > 💬 # Warrior, Thief, Wizard
  - `heroes1_18` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 278
  - `heroes1_19_jail` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 297
  > 💬 # Warrior, Thief, Wizard
  - `heroes1_21_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 305
  > 💬 # "Ratleigh, I delegate: stop them, then meet me on the barge."
  > 💬 # heroes1_npc

### heroes2

- 机制标签: `heroes`；关卡 30 个（其中分支 *choice 10 处，磁盘命中 30）
  > 💬 #
  > 💬 # Magistrate + Ratleigh, "travel through the countryside where I grew up"...
  > 💬 # Warrior on his tail
  > 💬 # Warrior + Some Monsters
  - `heroes2_2b` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 250
  > 💬 # Warrior + Many Monsters
  - `heroes2_2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 224
  > 💬 # Thief + Many Monsters
  - `heroes2_thief_goblin` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 242
  > 💬 # Wizard + Many Monsters
  - `heroes2_3_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 224
  > 💬 # Warrior + Dragons
  > 💬 # "There are many dangers out here, Ratleigh, of which a city-born child like yourself knows not. Observe, and learn."
  - `heroes2_5_altE` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 372
  > 💬 # Thief + Dragons
  - `heroes2_5_no_crystal` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 280
  > 💬 # Thief + Dragons
  - `heroes2_5.5v5` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 265
  > 💬 # Thief + Dragons
  - `heroes2_6_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 264
  > 💬 # Warrior, Thief, Wizard + Dragons
  - `heroes2_9` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 295
  > 💬 # Warrior + Monsters + Gate
  - `heroes2_10a_intro` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 253
  - `heroes2_10a` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 248
  - `heroes2_3monster` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 235
  > 💬 # Thief + Monsters + Gate
  > 💬 # Magistrate and Ratleigh on the usefulness of Monster Gates.
  > 💬 # "These were developed as part of an automated defense scheme against monsters;
  > 💬 # The other parts are quite expensive, mostly reserved for the King's own defense,
  > 💬 # but these are common and cheap, and I find them
  > 💬 # quite useful to slow down unwanted pursuers."
  - `heroes2_10` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 273
  > 💬 # Warrior + Monsters + Gate
  - `heroes2_11_v2_easier` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 234
  > 💬 # Wizard + Monsters + Gate
  > 💬 # Magistrate and Ratleigh are on the same level at the same time
  > 💬 #
  - `heroes2_12_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 226
  > 💬 Per-Turn Dragon Breath (totally optional):
  > 💬 # Warrior + Dragons and Goblins
  - `heroes2_11_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 203
  > 💬 # Wizard + Dragons and Goblins
  - `heroes2_10.5` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 235
  > 💬 # Warrior, Thief + Dragons and Goblins
  - `one_fire_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 240
  > 💬 #
  > 💬 # *** Priestess Intro *** (what to do?)
  > 💬 #
  - `heroes2_13` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 176
  > 💬 # Wizard + Priestess (bashful not sure how to talk to her)
  - `heroes2_14` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 200
  > 💬 # Warrior + Priestess (positive attitude and happy to have help)
  - `heroes2_15` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 261
  - `heroes2_reprise` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 295
  > 💬 # Thief + Priestess (new friend!)
  - `heroes2_16v4` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 219
  - `heroes2_18` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 213
  > 💬 # Wizard + Priestess
  - `mosh_pit_small` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 198
  - `heroes2_17_intro` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 249
  - `heroes2_17` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 249
  > 💬 # Wizard, Thief, Priestess
  - `heroes2_20` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 205
  > 💬 # Thief, Wizard, Priestess
  - `heroes2_21b` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 188
  > 💬 # Warrior, Thief, Wizard, Priestess
  - `heroes2_22_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 225
  > 💬 #
  > 💬 # -- or --
  > 💬 # skip the previous level, and just come up with heroes2_npc_finale
  > 💬 #

### heroes3

- 机制标签: `heroes`；关卡 25 个（其中分支 *choice 8 处，磁盘命中 25）
  > 💬 Druid levels:
  > 💬 # *** Druid Intro ***
  > 💬 # Thief, Druid
  - `heroes3_10` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 248
  > 💬 # *** Discuss Druid history ***
  > 💬 # Warrior, Druid
  - `heroes3_11_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 282
  - `druid_and_dragon` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 241
  > 💬 # Wizard, Druid
  - `wizard_and_druid_alt_5` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 233
  - `heroes3_15_v4` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 217
  > 💬 # Warrior, Priestess, Druid
  > 💬 # ** Uncertainty of trust between Druid and Priestess ** -- "We don't usually work with them. Don't quite see eye to eye. Historical differences."
  - `heroes3_13_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 292
  - `heroes3_druid_b_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 231
  > 💬 # Warrior, Thief, Wizard, Druid
  - `heroes3_druid_a` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 326
  > 💬 Optional:
  - `wizard_and_druid_alt` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 302
  > 💬 Bard levels:
  > 💬 # *** Bard Intro ***
  > 💬 # Bard + Goblins
  - `heroes3_1_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 242
  - `heroes3_2_v4` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 260
  > 💬 # Bard + Crystals (crystals move with life force!)
  - `heroes3_3_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 253
  > 💬 # Bard + Goblins
  - `heroes3_4` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 209
  > 💬 # *** Warrior meets Bard ***
  - `heroes3_5` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 304
  > 💬 # *** Thief meets Bard ***
  - `heroes3_8_thief` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 368
  > 💬 # Warrior, Thief, Bard
  - `heroes3_6_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 405
  > 💬 # Wizard, Bard
  - `heroes3_7_v4` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 328
  > 💬 # Bard + Dragon
  - `heroes3_8_v4_alt` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 336
  > 💬 # Bard, Priestess
  - `heroes3_8_v3_alt3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 381
  > 💬 heroes3_9
  > 💬 Bard and Druid:
  > 💬 # Bard, Druid
  - `heroes3_14_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 326
  - `heroes3_16_v4_alt` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 233
  > 💬 # Warior, Thief, Druid, Bard
  - `compactor_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 243
  > 💬 # Wizard, Druid, Bard
  - `gatekeeping_v3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 232
  - `heroes3_21_condensed` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 243
  > 💬 #
  > 💬 # Level where Ratleigh is defeated,
  > 💬 # "But lo! You may think you have failed yet again,
  > 💬 # poor Ratleigh, but you have succeeded at least in
  > 💬 # getting me where I needed to go."
  > 💬 #
  > 💬 #
  > 💬 # Strictly bonus, later:
  > 💬 #
  - `victory_lap` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 475

### heroes_and_artifacts（英雄与神器 / Heroes and Artifacts）

- 机制标签: `heroes beams`；关卡 5 个（其中分支 *choice 5 处，磁盘命中 5）
  > 💬 Wand/Torc + Heroes of Sokoban
  > 💬 I'm unsure if the torc+heroes levels should be colocated with all the wand+heroes levels,
  > 💬 but this seems like an alright place to put them if we keep them? -Patrick 2023-11-19
  > 💬 Thief, intro
  - `thief_wand` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 232
  > 💬 Warrior - UNSURE. maybe just 1? but I'm not ultra confident in any of these levels. -Patrick
  - `flame_wand` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 240
  > 💬 great_wall
  > 💬 great_wall_v2
  > 💬 roommates
  > 💬 roommates2
  > 💬 wand_multipush
  > 💬 target_practice
  > 💬 Wizard
  - `swap_and_spin` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 215
  - `wizard_with_a_gun` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 245
  > 💬 Bard
  - `bug_spray` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 178
  > 💬 Torc
  > 💬 (todo?)
  > 💬 torc_team # Improvable. Also doesn't have to be Heroes. Hm.
  > 💬 torc_blocked # Maybe better in underworld? Also doesn't have to be Heroes. Hm.

### heroes_and_mirrors（英雄与魔镜 / Heroes and Mirrors）

- 机制标签: `heroes mirrors`；关卡 34 个（其中分支 *choice 30 处，磁盘命中 34）
  > 💬 Heroes of Sokoban + Mirror Isles
  > 💬 except for cloning/clones, that's in "clones" level set
  > 💬 Gates
  - `flip_flop_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 234
  - `two_for_one` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 182
  - `gate_shatter` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 186
  - `iodine_clock_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 241
  - `mirror_clocks` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 228
  > 💬 Warrior
  - `mirror_hallway_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 188
  > 💬 Bard
  - `reattachment` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 247
  - `detachment` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 269
  > 💬 Priest and Druid blocking and deflecting
  - `blocking_issue` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 218
  - `greenhouse` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 235
  - `bitstring_small` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 241
  > 💬 Thief
  - `holes` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 246
  - `double_break` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 230
  - `drop_tool` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 263
  > 💬 Wizard
  - `wizard_mirror_intro` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 223
  - `regular_mirror_v4` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 238
  - `moving_a_mirror` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 232
  - `moving_three_mirrors` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 195
  - `mirror_dweller` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 254
  > 💬 ######### Art phase 2 ##########
  > 💬 Swap mechanic
  - `the_swappers` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 222
  - `tricky_swappers_v3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 257
  > 💬 Goblins
  - `close_to_button` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 287
  - `goblin_parity` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 273
  - `clone_goblin` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 416
  > 💬 Dragons
  - `two_dragon_rooms` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 369
  - `quad_torch` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 342
  - `trick_kills` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 425
  - `fuse` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 292
  > 💬 Cleric fly + monsters
  - `fly_and_flip` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 284
  - `fire_and_flip` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 314
  - `elope` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 268
  - `walk_the_plank` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 286
  - `red_cross` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 308
  - `oneway_dragon_toast` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 301
  > 💬 bard_metamirror and druid_metamirror moved to metamirrors_combo.level_set in underworld
  > 💬 Commented-out levels
  > 💬 bottleneck # Warrior
  > 💬 Notes that were here before Patrick revisions:
  > 💬 First:
  > 💬 Levels that use one hero & mirrors.
  > 💬 Each of these are pretty independent from the rest, so can be in separate unlock branches.
  > 💬 Priest/druid go together (because they both can't move crystals), and wizard feels a bit fancier than the rest (because he has mechanics with regular mirrors too)
  > 💬 Thief
  > 💬 Warrior
  > 💬 Wizard
  > 💬 Priest/Druid (not trivial!)
  > 💬 reflection_deflection_v3 doesn't have all the superfluous trees, and reflection_deflection_druid_v2 has the fewest amount of trees that keeps the puzzle the same, but I sort of like having the full forest for some reason.
  > 💬 Bard
  > 💬 Gates
  > 💬 Second: mirroring multiple things/characters at once
  > 💬 Also learning about when mirrors are blocked and puzzles about that?
  > 💬 Remove the v2's to get back the original version (same layout, no fire)
  > 💬 (Maya is super on board with the fire update! -Matt)
  > 💬 fuse_v2 # Patrick cut
  > 💬 fuse2_v2 # Patrick cut
  > 💬 fuse3_v2 # Patrick cut
  > 💬 fuse4_v2
  > 💬 fuse4_v3 # Minor change. I think v2 might have been too easy to accidentally win without realizing the parity change. Might still be a problem.
  > 💬 (P.S. Commented out fuse4 for now)
  > 💬 mirror_trolls
  > 💬 clone_flying2
  > 💬 mirror_line
  > 💬 diagonal
  > 💬 A nice level where the focus is having more than one character
  > 💬 mirror_slide
  > 💬 *choice
  > 💬 Teaching that mirroring multiple characters happens simultaneously.
  > 💬 two_for_one
  > 💬 mirror_together
  > 💬 doppeldanger
  > 💬 *choice
  > 💬 Levels with blocked mirrors
  > 💬 unblock_all
  > 💬 swap_limit # disfavored
  > 💬 *choice
  > 💬 one_fire
  > 💬 mirror_clone_dragons_v0 # This and the next feel like they are distinct enough solves to be a good pair of levels, not sure _2 adds much on
  > 💬 mirror_clone_dragons
  > 💬 mirror_clone_dragons_2_v2
  > 💬 *choice

### heroes_and_stones

- 机制标签: `heroes stones`；关卡 41 个（其中分支 *choice 27 处，磁盘命中 41）
  > 💬 Levels that just require heroes of sokoban + skipping stones and show interactions between the two
  > 💬 Twists that don't get revealed here:
  > 💬 Normal stones vs crystal stones (may change all stones to crystal stones at some point)
  > 💬 Bard stacking moves
  > 💬 Dragons on lilies rotate
  > 💬 Interesting intro thing (a little hard for an intro, but probably ok)
  - `crystals_not_stones` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 223
  - `stones_not_crystals` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 227
  - `one_of_each` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 189
  > 💬 ## WARRIOR
  - `one_bird_two_stones` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 200
  - `breath_skip` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 220
  - `indirect_skip` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 188
  - `indirect_skip_2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 203
  - `indirect_skip_3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 237
  > 💬 ## DRUID
  - `druids_stone_0_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 158
  - `druid_stone_p` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 145
  - `druids_stone_alt` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 177
  - `druids_stone_2_v4` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 192
  > 💬 Druid and water, but the big star is flagged heroes+stones not heroes+mirrors
  - `floating_gardens` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 204
  - `four_horsemen` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 203
  - `put_down_roots_v3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 278
  - `prisoners_dilemma_alt` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 239
  - `dragon_garden` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 262
  > 💬 ## WIZARD
  > 💬 warrior_and_wizard
  - `island_friends` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 216
  - `wizard_with_a_capital_w` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 190
  - `wizard_with_a_capital_w_2_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 229
  > 💬 ## BARD (have to be careful not to reveal the bard_stacking "twist")
  - `slot_machine_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 158
  - `push_against` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 204
  - `come_closer` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 218
  - `useful_stone` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 207
  - `trick_shot` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 223
  > 💬 These levels involve the aforementioned bard_stacking twist.
  > 💬 But, this area has since been moved to be a sky dropdown.
  > 💬 -Patrick 2024-10-16
  - `bard_range4` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 179
  - `bard_range5` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 203
  - `bard_range6` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 182
  > 💬 ## Thief
  - `pull_it_v4` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 192
  - `pull_teamwork_alt` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 223
  > 💬 ## GATES (These two are pretty unrelated... don't feel like a full sequence)
  - `sprint_skip0` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 222
  > 💬 Level where a stone on a lily blocks the dragon for a second.
  - `watergate` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 218
  > 💬 ## All the remaining levels are priest levels. This is gated by knowledge of priest walking on water (every single level here is probably going to use it.):
  - `stone_stopper_intro` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 222
  - `another_stone_stopper` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 228
  > 💬 stone_stopper0
  > 💬 stone_stopper #commented out for now because mirror (but also there were too many stone stopper levels anyway, and it doesn't add much)
  > 💬 stone_stopper2 #also mirror, it seems like these mirrors are really not necessary to the idea anyways though so we'll be able to remake them with no mirror easily enough if we like them.
  - `stone_stopper3_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 273
  > 💬 stone_stopper4
  - `stone_stopper5` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 232
  - `skipping_with_dragon` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 240
  - `walk_into_fire` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 245
  > 💬 scrape_off # Uses lily rotation, which I think we want to save for the underworld (lily_rotation.level_set). -Patrick 2024-06-25
  - `hot_swap` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 241
  > 💬 hot_swap_part_deux (very exploitable)
  > 💬 swapwiz_double_v2
  > 💬 This is over on the Priestess Highway:
  - `monster_gate_in_water` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 229
  - `pull_skip_twins_v3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 297

### heroes_and_water（英雄与水 / Heroes and Water）

- 机制标签: `heroes mirrors`；关卡 33 个（其中分支 *choice 23 处，磁盘命中 33）
  > 💬 The heroes sets don't have water so this set will show the
  > 💬 basic interactions heroes can have with water. Some things with
  > 💬 crystals/gates/drowning, but the biggest point of interest
  > 💬 is the cleric walking on water.
  > 💬 Warrior:
  > 💬 Showing that crystals can be pushed into water
  - `dipping_your_toes_in` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 271
  > 💬 And then that they can be walked on too
  - `crystal_bridges` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 297
  > 💬 Warrior and Thief:
  - `push_and_pull_zach` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 238
  - `quadrants_follow_up` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 355
  - `quadrants` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 339
  > 💬 Drowning monsters
  - `drowner` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 329
  - `surrounded` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 378
  - `dont_push_the_button` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 288
  - `detonator` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 294
  - `a_wiz_out_of_water` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 295
  - `island_hopping` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 260
  - `dunk_tank_alt` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 258
  > 💬 Bard
  - `gully_alt` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 281
  - `easy_situation_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 270
  - `one_vs_three` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 254
  > 💬 Bard with Priestess
  - `synchronized_swimmers` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 285
  - `dragon_compass` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 243
  > 💬 Introduction of priest walking on water, only has heroes & water.
  - `new_cleric_fly` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 243
  > 💬 cleric_fly_intro0 # Won't make sense if the player hasn't seen perspective shifts
  - `little_faith_alt` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 193
  > 💬 cleric_fly_intro1 # Doesn't seem to really add anything on top of little_faith. I think little_faith is slightly better, though mostly the same.
  - `both_ways` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 250
  - `flamethrower` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 210
  - `killer_wizard` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 229
  - `partial_pull` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 255
  - `cleric_fly_intro3_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 228
  - `monster_mover` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 259
  > 💬 tiny_islands
  > 💬 cleric_fly_intro2
  > 💬 cleric_fly_intro3 # Sort of broken. Top part isn't needed. See v2
  > 💬 cleric_fly_intro3_v2
  > 💬 goblin_pusher1
  > 💬 jack_and_rose
  - `team_building_exercise` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 228
  - `tug_boat` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 261
  - `on_command` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 265
  > 💬 impossible_gap
  > 💬 pool_party # Broken by druid revive
  > 💬 Bard sunken crystal manipulation
  > 💬 (The few bard levels from above would also be moved down here. See spreadsheet for which ones - currently highlighted in yellow in Patrick Notes.)
  - `bard_stack_intro` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 236
  - `goblin_express` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 295
  - `baby_steps_line` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 303
  > 💬 bard_range0
  > 💬 bard_range
  > 💬 bard_range2
  - `surfing_lesson_alt` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 247
  > 💬 jazz_trio_alt
  > 💬 swing_trio # Hard!
  - `bard_range3_with_intro` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 291

### heroes_in_3d

- 机制标签: `heroes`；关卡 66 个（其中分支 *choice 58 处，磁盘命中 66）
  > 💬 Heroes of Sokoban in 3D
  > 💬 (comments and commented-out levels have been moved to spreadsheet)
  > 💬 North thief+warrior+goblins path
  - `gated_twice_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 263
  - `gated_twice_thief_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 259
  - `connect_the_dots_v5` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 235
  - `pulling_pedestals` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 248
  - `thief_stack` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 277
  - `zombie_graves_v3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 211
  - `dragon_bridge` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 225
  - `loading_docks_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 227
  - `assassins_creed` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 223
  - `high_horse` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 323
  > 💬 East warrior stacks path
  - `personal_assistant_v3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 203
  - `push_down_a_lot_small` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 188
  - `my_first_stack` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 241
  - `single_out` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 131
  - `jenga_shortstack_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 157
  - `jenga_easier` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 186
  - `archways_2_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 192
  - `archways_4` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 189
  - `hat_chain_vp` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 220
  - `cliff_duo` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 139
  > 💬 Vertical gates (merge this back into the warrior+thief place?)
  - `going_up_v4` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 225
  - `automatic_door_v5` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 182
  > 💬 Wizard
  - `magicians_assistant_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 181
  - `falloff_intro` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 170
  - `falloff_4` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 203
  - `falloff_kill_goblins_v6` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 207
  - `falloff_dragons` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 203
  - `erosion_alt` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 245
  - `magic_tower` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 240
  > 💬 Bard 3D Range
  - `mountain_music` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 260
  - `out_of_range_v4` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 281
  - `musical_staircase_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 158
  - `sticky` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 291
  > 💬 Main bard stacks area
  - `tippy_intro` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 382
  - `tippy_towers_1` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 226
  - `tippy_towers_4` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 227
  - `high_shelf_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 229
  - `jump_to_pillar_v3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 267
  - `i_beam_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 285
  - `bard_must_stack4_fix` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 267
  - `bard_triangle` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 245
  - `no_charm` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 191
  - `stones_below_v3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 199
  > 💬 Sky Druid:
  - `sky_druid_kill` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 209
  - `sky_druid_kill_tall_2_goblins` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 209
  - `weaklings_bard_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 184
  - `stopper_topper_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 154
  - `sky_druid_tree_ex` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 208
  - `druid_3d_beam` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 194
  - `sky_druid_maze` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 203
  - `sky_druid_one` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 210
  > 💬 sky_druid_pro
  > 💬 Priest
  - `priest_descent_simpler` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 145
  - `priest_button_3d_revised` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 199
  - `priest_3d_goblin_pass` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 140
  - `fire_stairs_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 209
  - `fire_stairs_part_2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 255
  - `priest_3d_intro_dragon_v4` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 236
  - `priest_warrior_descent` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 288
  - `priest_bottom_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 319
  - `from_the_depths` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 276
  - `priest_two_warriors_v3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 227
  - `monster_stack` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 200
  - `catching_fire_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 235
  - `frame_advance_v5` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 229
  - `priest_traverse_e_fence` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 266
  - `stuck_up_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 217
  > 💬 Meh?
  > 💬 priest_two_warriors_path# Warrior Holding Goblin to Make Priest Path (2 Warriors)
  > 💬 Deprecated:
  > 💬 angel
  > 💬 fallen_angel
  > 💬 monster_stack_2_v3
  > 💬 priest_spiral_2
  > 💬 Crush goblin
  > 💬 death_from_above
  > 💬 *choice
  > 💬 These levels were moved to the intersection between priest fly and skipping stones. The are in the skipping_in_3d level set. -Patrick
  > 💬 priest_water_back       # Warrior helping Priestess. Simple, kinda planar.
  > 💬 *choice
  > 💬 3 priest + skipping stones levels moved to skipping_in_3d. -Patrick 2024-10-15
  > 💬 the_waterfall_v4        # Skipping characters into dragon breath.
  > 💬 *choice
  > 💬 priest_water_back_goblin
  > 💬 *choice
  > 💬 priest_water_back_place
  > 💬 *choice
  > 💬 backfire_v2 is currently over near Dressing Room:
  > 💬 backfire_v2
  > 💬 *choice

### intro

- 机制标签: `star`；关卡 1 个（其中分支 *choice 0 处，磁盘命中 1）
  - `intro` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 1534

### intro_hard_puzzles

- 机制标签: `heroes`；关卡 2 个（其中分支 *choice 2 处，磁盘命中 2）
  > 💬 Levels in the "hard puzzles" room in the intro level post-credits.
  - `jenga_dispenser` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 219
  - `wizards_true_nature` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 233

### intro_to_3d

- 机制标签: `star`；关卡 8 个（其中分支 *choice 5 处，磁盘命中 8）
  > 💬 The first levels you play in the sky.
  > 💬 (comments and commented-out levels have been moved to spreadsheet)
  - `3d_intro_vanilla` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 196
  - `push_down_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 183
  - `sister_staircase_harder` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 165
  - `carry_simplified` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 181
  - `3d_intro_heroes` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 312
  - `3d_intro_mirrors` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 208
  - `3d_intro_skipping` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 231
  - `3d_intro_promesst_v5` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 239

### lily_highway_heroes_and_stones

- 机制标签: `heroes stones`；关卡 4 个（其中分支 *choice 3 处，磁盘命中 4）
  > 💬 H+S
  > 💬 Beginning
  - `stone_rescue_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 145
  - `wrap_music` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 198
  - `wrap_music_2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 137
  > 💬 Not wrapping levels, but located along the wrapping river highway.
  - `swapwiz_harder` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 319

### lily_highway_mirrors_and_stones

- 机制标签: `mirrors stones`；关卡 12 个（其中分支 *choice 10 处，磁盘命中 12）
  > 💬 M+S
  > 💬 Wrapping skipping island 1
  - `infinite_looping_skipper0_alt` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 253
  - `infinite_looping_skipper_alt` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 236
  - `infinite_looping_skipper_far` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 201
  - `infinite_looping_skipper_mirrored_ikaruga_alt` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 230
  > 💬 Wrapping skipping island 2
  > 💬 upstream_alt
  > 💬 *choice
  - `sick_270_small` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 220
  - `layered_alt` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 280
  - `yars_revenge_setup_v3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 243
  > 💬 Not on the lily highway at all, but makes sense to put here becuase they are the same crossover type and nearby
  > 💬 Advanced Skipping Stones
  > 💬 I really liked odd_pop but it does not work with the new rules. Sad.
  > 💬 odd_pop
  - `mirror_180` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 286
  - `reroute_3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 241
  > 💬 reroute_v2
  > 💬 reroute_2_v2
  > 💬 Diagonal Skipping
  > 💬 I thought maybe the level shape is a giveaway, but on second thought it probably
  > 💬 makes it nicer since it becomes obvious in hindsight:
  - `before_wings` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 267
  - `far_wings` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 259
  - `after_wings` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 218
  > 💬 Note: Diagonal-skipping stones also kick lilies 45 degrees backward (which is about the only thing
  > 💬 that makes sense?) and this could be a wings2 level...

### lily_highway_stones_and_promesst

- 机制标签: `stones beams`；关卡 9 个（其中分支 *choice 6 处，磁盘命中 9）
  > 💬 S+P
  > 💬 Axes intersection island
  - `duality_condensed` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 303
  - `duality_2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 279
  > 💬 Wand
  - `zap_bridge` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 143
  - `zap_bridge_perp` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 92
  - `frontier` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 245
  > 💬 Advanced Skipping Stones w/ Heroes
  > 💬 Funny level. For underworld. Needs probably a bit more
  > 💬 movement tuning.
  > 💬 Not technically a skipping+promesst level, but is along the path to a S+P star
  - `skybridge` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 175
  > 💬 Wand, Elevator
  - `ortho` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 264
  - `ortho2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 172
  - `ortho3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 223
  > 💬 ortho3a

### lily_rotation

- 机制标签: `mirrors stones`；关卡 7 个（其中分支 *choice 6 处，磁盘命中 7）
  > 💬 Levels which involve rotating things by putting them on a rotating lily.
  > 💬 If there are not many levels in here, could be grouped with some other advanced skipping stones concept
  > 💬 Rotating mirrors
  - `mirror_u` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 368
  - `mirror_flip_donut` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 293
  - `in_a_flash_alt` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 331
  > 💬 Putting this back for now to see if I can reproduce Cameron's undo bug
  - `in_a_flash_alt_back` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 334
  > 💬 mirror_choice
  > 💬 river_maze_redivert
  > 💬 *choice
  > 💬 mirror_u2
  > 💬 *choice
  > 💬 mirror_moment
  > 💬 *choice
  > 💬 Moved here from heroes_and_stones because it uses lily rotation. -Patrick 2024-06-25
  > 💬 scrape_off
  > 💬 *choice
  > 💬 Advanced river diversion
  > 💬 This doesn't involve lily rotation, but it is a small chunk of levels that is located next to lily rotation,
  > 💬 so I put it in this level set for now just because of locality. -Patrick 2025-06-11
  - `river_maze_clear_tenacious_race_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 340
  - `river_rates_button` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 385
  - `river_rates_jagged` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 397
  > 💬 procrastination_alt
  > 💬 blockade_alt
  > 💬 This level is maybe harder than it needs to be, but I was also doing that
  > 💬 to constrain the level and make it less messy and more solvable...
  > 💬 irreversible
  > 💬 *choice

### metamirrors

- 机制标签: `mirrors`；关卡 10 个（其中分支 *choice 5 处，磁盘命中 10）
  > 💬 Metamirrors
  > 💬 Levels with one regular mirror and one mirrorable mirror:
  > 💬 First, both have mirrors facing in the same direction.
  - `metamirror_same_dir_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 138
  - `metamirror_same_dir_2_alt_2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 142
  - `metamirror_same_dir_3_alt_2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 115
  - `metamirror_same_dir_5_alt` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 150
  > 💬 metamirror_same_dir_2
  > 💬 metamirror_same_dir_3
  > 💬 metamirror_same_dir_4
  > 💬 metamirror_same_dir_5
  > 💬 Then with different directions (Surprise, reflecting a mirror can change it's direction!)
  - `metamirror_different_dir_alt` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 150
  - `metamirror_different_dir_3_alt` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 189
  - `metamirror_different_dir_2_alt` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 144
  > 💬 metamirror_different_dir
  > 💬 metamirror_different_dir_3
  > 💬 metamirror_different_dir_2
  > 💬 Then other concepts can happen
  > 💬 bring back boxes, mirrorable boxes, clones, etc...
  - `metamirror_block_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 153
  - `metamirror_c_alt` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 140
  > 💬 metamirror_clone # This level is unfair without having more levels involving double mirror before it. So far I think only one level before it used this concept.
  > 💬 Multiple mirrorable mirrors
  - `two_metamirrors` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 107
  > 💬 flip
  > 💬 NOTE: see level "flip" when revising this set. It may be a better (or worse) version of one of these levels. -Patrick 2023-12-17

### mirror

- 机制标签: `mirrors`；关卡 27 个（其中分支 *choice 14 处，磁盘命中 27）
  > 💬 Just mirrors, no rocks
  - `mirror_1` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 156
  - `mirror_2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 143
  > 💬 Now rocks as well
  - `mirror_3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 179
  - `mirror_4` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 170
  - `mirror_5` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 152
  - `mirror_6_alt` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 173
  - `mirror_7` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 152
  - `mirror_8_v5` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 158
  > 💬 Clones
  - `mirror_11` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 151
  - `mirror_12` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 136
  - `mirror_13` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 153
  - `mirror_14` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 137
  > 💬 Mirrorable crystals
  > 💬 Dry land manipulation
  - `mirror_15` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 166
  - `mirror_19` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 144
  - `mirror_17` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 146
  > 💬 Sinking them from a mirror
  - `mirror_sink` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 133
  - `mirror_20` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 137
  - `mirror_18` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 116
  - `mirror_21` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 150
  - `mirror_22_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 148
  - `mirror_factory_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 127
  > 💬 Optional levels:
  - `mirror_pals` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 143
  - `walk_it_over` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 163
  > 💬 Two-mirror bouncing...
  > 💬 This is a nonlinear branch that opens up after mirror_sink.
  > 💬 Unlocks the H+M Mirror:
  - `mirror_10_alt2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 125
  - `mundane_mirror` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 115
  - `mirror_10_b_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 151
  - `mirror_10_d` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 128
  > 💬 mirror_finale

### mirrorable_stones

- 机制标签: `mirrors stones`；关卡 20 个（其中分支 *choice 13 处，磁盘命中 20）
  > 💬 Intro to mirrorable stones.
  > 💬 These first levels generally have a single fixed mirror, and not too many options.
  - `mirror_stone_intro` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 159
  - `catch_and_drop` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 284
  - `catch_and_throw` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 209
  > 💬 landlock
  - `reflect_momentum` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 284
  > 💬 skipping_around
  > 💬 bridge_builder
  > 💬 *choice
  > 💬 The sidestone puzzles can be annoying to have to draw long diagonal lines with your eyes. I'm hoping there will somehow be a way to help the player with this like diagonal lines drawn in the ocean.
  > 💬 Maybe we like sidestone_alt1 better than sidestone... not sure.
  > 💬 sidestone_stop_and_drop_intro
  > 💬 sidestone_stop_and_drop # I might like this one better if the bottom right island were more open (so the puzzle is about choosing where to skip rocks rather than having it feel claustrophobic)
  > 💬 sidestone_corner_fill
  > 💬 ikaruga
  > 💬 sidestone # Seems very broken. The island on the top isn't even needed!*
  > 💬 sidestone_stop_and_drop_gates # I think that the intended idea is to realize you have to do the bottom stone last, or else you don't have a stone for the button. However if you tried to do the bottom stone not last, the mirror would get stuck anyways. Also it's exploitable by mirroring the guy onto the top and then moving him.
  > 💬 sidestone_stop_and_drop_bananas_small
  - `sidestone_zach_1` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 308
  - `sidestone_zach_2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 239
  - `sidestone_zach_3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 167
  - `sidestone_zach_4` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 162
  > 💬 stone_redirection
  > 💬 stone_redirection2
  - `launch_and_collect` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 312
  - `lilyruga_simpler` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 235
  > 💬 lilyruga # Love the core idea of this level, but it feels like it has some distractions that make it harder than it has to be.
  > 💬 mirror_spiral_v3
  > 💬 mirror_spiral_v2 # Long mazelike level, sort of a test of what the player has learnt so far.
  > 💬 Moved into drafts_disfavored...
  > 💬 mirror_spiral # My experience with this level was that it's possible to put the crystal in the wrong place very early and not clear why that is bad until much later on.
  > 💬 Two mirror ideas:
  > 💬 u_turn
  > 💬 *choice
  - `bad_aim_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 286
  - `multipurpose` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 283
  - `wide_ocean` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 230
  - `zig_zag` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 232
  - `ricochet_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 429
  - `run_the_clock_alt` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 366
  > 💬 Mirror on a lily
  - `wider_ocean` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 382
  - `reel_it_in` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 183
  - `make_it_happen_v6` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 338
  > 💬 retrieve
  > 💬 coaxer is currently broken due to a gameplay code bug.
  > 💬 coaxer
  > 💬 coaxer_different # same solution as make_it_happen
  > 💬 coaxer_harder # Almost the exact same as coaxer, with no meaningful change to the solution
  > 💬 rescuer0
  > 💬 Interesting but it's so big that theories take a long time to try out (and it's hard too!) Hopefully can be made more compact.
  > 💬 coordinates
  > 💬 rescuer # Also very big with slow moving lilies. Things take a long time to try. (and it's very hard)
  > 💬 The slam levels are pretty advanced
  > 💬 slam_bridge # Currently test is broken. I don't see how it's supposed to work.
  > 💬 slam
  > 💬 Orange currently unneeded.
  > 💬 clone_thrown_stone
  > 💬 new_slam
  > 💬 new_new_slam is currently marked as broken because you just clone the skipping stones.
  > 💬 new_new_slam
  - `new_new_new_slam` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 185

### mirrors_and_stones（魔镜与飞石 / Mirrors and Stones）

- 机制标签: `mirrors stones`；关卡 29 个（其中分支 *choice 21 处，磁盘命中 29）
  > 💬 Normal mirrors + stones + crystals
  > 💬 wheels_within_wheels_v2 # Pretty slow without using time manipulation powers.
  - `airmail` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 161
  > 💬 airmail_v2 is an adjusted version of airmail, but airmail was already arted, and it's fine if the adjustment doesn't make it in.
  > 💬 horseshoe
  - `thats_my_ride` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 167
  - `place_to_stand` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 159
  - `emergency_brake` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 175
  - `short_ride_option_b` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 178
  - `highway` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 162
  - `cancel_out` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 178
  > 💬 clone_lilies
  > 💬 Put mirror on a lily
  - `mirror_motion` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 166
  > 💬 place_mirror
  - `diag_slide` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 189
  - `the_long_way` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 220
  - `ride_together` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 166
  - `two_bounce_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 221
  > 💬 knock_stones # Feels bad right now, due to awkward stone timing.
  > 💬 stream_to_stream
  > 💬 lily_to_lily
  > 💬 Would be nice to have a couple of levels with rivers, that don't involve diversion
  > 💬 River levels
  - `first_diversions` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 280
  - `far_river` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 247
  - `ditching_cargo` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 287
  - `unblock_block_alt` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 271
  - `there_and_back` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 209
  - `sink_together` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 202
  - `in_the_way_alt_3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 252
  > 💬 mirror_epicycle
  > 💬 river_maze_loop
  > 💬 river_maze_loop_2
  > 💬 river_maze_upper_friend_v2 # It's 3D. Commented out for now, a similar idea could be made that doesn't require 3d by putting the crystal one space further out from the mirror so you mirror the person first, and the crystal second.
  > 💬 A lot of concepts with skipping stones + mirror isles mechanics
  > 💬 skipping_isles
  > 💬 The rest of the levels are about diverting the path of rivers
  > 💬 Important learning level, levels before this shouldn't rely on which direction the river turns.
  - `river_dictionary_alt_up` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 356
  > 💬 river_push_v3
  - `river_push_v4` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 313
  - `coax_a_lot` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 252
  > 💬 coax_a_lot_2 and do_not_coax_a_lot make a kinda cool sequence
  > 💬 with coax_a_lot, but are marked as disfavored currently since
  > 💬 maybe we do not want to do that with this game. If we do, we'd
  > 💬 put them all in the underworld.
  > 💬 coax_a_lot_2
  > 💬 do_not_coax_a_lot
  > 💬 teleport_onto_lily_pad
  > 💬 The following river_maze levels are new and hopefully better than the old ones. -jblow, 8 August 2022
  > 💬 river_maze_easy
  > 💬 river_maze_strut
  > 💬 river_maze_two_diversions_revised
  > 💬 river_maze_two_diversions_b
  > 💬 river_maze_cycle_attempt_2
  > 💬 river_maze_cycle_reach
  > 💬 The following river_maze levels I have phased out because they are not good.  -jblow, 8 August 2022
  > 💬 river_maze
  > 💬 river_maze_two_diversions
  > 💬 river_maze_two_diversions_need_to_make_space
  > 💬 river_maze_clear_one seemed kinda redundant with what came before. Maybe it could be revised in a way that maintains continuity of the sequence. I revised river_maze_clear_two and was able to preserve the idea but it got much bigger!
  > 💬 level
  > 💬 dragon doesn't belong in this set
  > 💬 river_maze_dragon
  > 💬 river_maze_clear_two
  > 💬 river_maze_clear_or_gate
  > 💬 river_maze_clear_or_gate_combiner
  > 💬 commented out because buttons (it's a nice level though. should go somewhere later.)
  > 💬 toggle
  > 💬 to_and_fro
  > 💬 coax_a_lot_2 # Good but it's 3D so for now seems like shouldn't be here; broken unless modified for new river rules.
  > 💬 coax_a_lot_2d # Draft of making it 2d which doesn't work :/
  > 💬 This was about stopping a river but it's just not that hard to stop a river.
  > 💬 @Incomplete: Work on this one to see if I can make it make sense.
  > 💬 river_maze_clear_tenacious
  > 💬 This one was cooler with its lead-in level; by itself, I dunno, it is redundant with pulse?
  > 💬 river_maze_clear_tenacious_race
  > 💬 pulse
  > 💬 pulse2
  > 💬 pulse3
  > 💬 Mirrors in the water!
  - `already_dropped_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 219
  - `two_step` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 218
  - `moving_bridge` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 249
  - `square_dance` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 214
  - `use_and_remove` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 250
  - `infinite_crystal_hack_v5` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 253
  > 💬 Underwater cloning?
  > 💬 Underwater diversion, do rivers go back to how they had been?
  > 💬 River Polarity
  - `river_plinko_v2_actual` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 383

### mirrors_in_3d

- 机制标签: `mirrors`；关卡 16 个（其中分支 *choice 13 处，磁盘命中 16）
  > 💬 Magic mirrors interfacing with 3D. (Note: no vertical mirrors.)
  > 💬 (comments and commented-out levels have been moved to spreadsheet)
  > 💬 Intro - "vanilla mirror isles + 3D" and ground-to-air mirroring.
  - `trader_descend` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 175
  - `cliff_hopping` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 223
  > 💬 Misc
  - `make_a_right_simpler` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 202
  - `make_a_right` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 260
  > 💬 Catch
  - `learn_to_catch_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 228
  - `trust_falls` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 221
  - `falling_blocker_v3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 196
  - `pillars` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 242
  - `long_platform_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 342
  - `triple_gate` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 299
  - `blind_spot_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 246
  > 💬 Misc
  - `bothersome_mirror` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 264
  > 💬 Mirrors + carrying
  - `hat_tricks_0_v3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 258
  - `omnimirror_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 285
  - `goblin_parity_3d` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 261
  - `mirror_carry_duo` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 296

### monsters_and_beams

- 机制标签: `heroes beams`；关卡 11 个（其中分支 *choice 10 处，磁盘命中 11）
  > 💬 Monsters in walls with Through Beam
  - `no_murder_weapon_wizard` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 209
  - `no_murder_weapon_0` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 222
  > 💬 no_murder_weapon
  - `dragonsweeper` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 226
  - `green_goblins` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 266
  > 💬 Druid 3D roots + Squeeze Beam
  - `en_root_alt` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 226
  > 💬 Monsters + Rooms and Monsters + Open Beam
  - `button_and_beam_v3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 237
  - `thief_dragger_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 232
  - `open_monster` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 215
  - `monster_promesst_v3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 152
  > 💬 Goblin water room
  - `goblin_two_rovers_alt` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 168
  - `rotating_cavalry_spaced` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 178
  > 💬 Dropping turns
  > 💬 rapid_fire
  > 💬 *choice

### orange_beam_highway_mirrors_and_promesst

- 机制标签: `mirrors beams`；关卡 6 个（其中分支 *choice 5 处，磁盘命中 6）
  > 💬 Mirrors+Promesst Levels along the orange beam highway in the underworld.
  > 💬 Artifacts + mirrors
  - `simultaneous_x` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 274
  - `simultaneous_x_surprise` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 317
  - `lazy_susan_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 364
  > 💬 fail_to_mirror
  - `fail_to_mirror_sequence_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 442
  > 💬 wand_wand
  > 💬 *choice
  - `three_artifacts_v3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 427
  > 💬 Along the highway:
  > 💬 Magnitudes
  - `magnitudes_v3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 682
  > 💬 Requires orange beam water walking, which may not be permissible on the ground floor. -Patrick 2023-11-19
  > 💬 Currently in the Underworld but doesn't seem spicy enough, so maybe we reconsider and put it on
  > 💬 the ground floor?
  > 💬 These levels are sort of superseded by green_torq_mirror_vs4. -Patrick 2024-04-02
  > 💬 torc_midair
  > 💬 torc_midair_2 # uses warrior
  > 💬 torc_midair_2_vtrader
  > 💬 *choice
  > 💬 double_beam_with_mirror0
  > 💬 *choice
  > 💬 double_beam_with_mirror
  > 💬 *choice
  > 💬 double_beam_with_mirror2
  > 💬 *choice

### orange_beam_highway_stones_and_promesst

- 机制标签: `stones beams`；关卡 4 个（其中分支 *choice 3 处，磁盘命中 4）
  > 💬 Skipping+Promesst Levels along the orange beam highway in the underworld.
  > 💬 Double beam water walking + skipping
  - `orange_mirror_walk_button` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 218
  - `orange_water_button_vslow` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 203
  - `orange_water_button_vdouble_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 212
  - `orange_water_button_vfour_alter` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 207
  > 💬 Orange_beam_skipper is currently in drafts_jon and needs fixing,
  > 💬 but it might go here when fixed.
  > 💬 orange_beam_skipper

### orange_beam_highway_worlds_collide

- 机制标签: `star`；关卡 4 个（其中分支 *choice 3 处，磁盘命中 4）
  > 💬 3 and 4 Worlds Collide Levels along the orange beam highway in the underworld.
  > 💬 3 worlds collide H+M+S
  - `3wcn_shm_dragon_lily` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 331
  > 💬 3 worlds collide M+S+P
  - `3wcn_purple_mirror_skip` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 299
  > 💬 4 worlds collide
  - `4wcn_all_fast` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 385
  - `4wc_dragon_cyan_s_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 532

### overworld

- 机制标签: （无）；关卡 1 个（其中分支 *choice 0 处，磁盘命中 1）
  - `overworld` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 3890

### promesst1_and_2

- 机制标签: `beams`；关卡 12 个（其中分支 *choice 12 处，磁盘命中 12）
  > 💬 Promesst 1
  - `promesst1_streamlined` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 444
  > 💬 Promesst 2
  - `promesst2_streamlined` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 345
  > 💬 Individual levels with only P1 and P2
  - `beam_rooms` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 192
  - `pushy` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 381
  - `forbidden_room` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 291
  - `gem_pushers` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 297
  - `target_practice_gem` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 222
  - `right_hand_man` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 298
  - `green_revolution` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 309
  - `torcoban_2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 264
  - `blue_revolution_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 268
  - `cyan_overlap_intro_longer` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 342
  > 💬 gem_endpointing_2
  > 💬 *choice

### promesst3

- 机制标签: `beams`；关卡 5 个（其中分支 *choice 5 处，磁盘命中 5）
  > 💬 Promesst 2.5
  - `promesst2.5_deeper` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 306
  > 💬 Promesst 3
  - `promesst3_streamlined` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 301
  > 💬 Promesst 3 tutorial levels. Not sure if these would be presented before or after p2.5/p3. -Patrick 2023-12-22
  > 💬 half_tutorial  # Moved this to the other half beam levels, which means it is not an intro to p3 at this time. We could move it if we decide that would be better. -jblow, 23 December 2023.
  - `half_tutorial` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 280
  - `monkey_in_the_midpoint` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 226
  > 💬 Crystal rovers dropdown
  - `crystal_rover_intro` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 264

### sideways_gates

- 机制标签: `heroes`；关卡 4 个（其中分支 *choice 4 处，磁盘命中 4）
  > 💬 Sideways gates
  > 💬 (comments and commented-out levels have been moved to spreadsheet)
  - `side_slide_intro_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 310
  - `multipush_for_me2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 263
  > 💬 gate_nudge
  > 💬 *choice
  - `side_kick` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 273
  - `dragon_on_the_wall` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 262

### skipping_in_3d

- 机制标签: `stones`；关卡 28 个（其中分支 *choice 27 处，磁盘命中 28）
  > 💬 Skipping Stones to Lonely Homes in 3D
  > 💬 Lily falling
  - `lily_falls_intro_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 242
  - `many_falls` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 271
  - `delay_time_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 319
  > 💬 Elevated pools + skipping stones
  - `pool_pal_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 259
  - `sunk_cost_2_v3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 238
  - `on_the_rocks` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 351
  - `button_shut_in` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 362
  > 💬 Lilies on solid objects
  - `tiger_lily_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 238
  - `carry_lily` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 142
  - `removal_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 171
  > 💬 Basic stone stacks
  - `skip_stack_1` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 273
  - `skip_stack_2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 291
  - `skip_stack_3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 252
  - `depositor_thief` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 307
  - `depositor_bard` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 288
  > 💬 Skipping stone rotation
  - `turn_control_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 214
  - `spin_heroes` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 253
  - `spray_and_pray` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 202
  - `rotator` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 200
  - `spin_doctors_v3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 243
  > 💬 Priest fly
  - `the_waterfall_v4` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 274
  - `priest_water_back_goblin` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 257
  - `priest_water_back_place_v3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 228
  > 💬 Vertical mirror skipping
  > 💬 (moved to another area!)
  - `falling_down` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 237
  - `lily_pull_intro` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 171
  - `lily_pull` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 166
  - `retro` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 252
  - `retro_hooks` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 179

### skipping_stones（飞石成径 / Skipping Stones）

- 机制标签: `stones`；关卡 4 个（其中分支 *choice 4 处，磁盘命中 4）
  - `skipping_stones` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 387
  - `time_tutorial` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 191
  > 💬 Replaced all the levels in this set with this one big level:
  - `skipping_pals` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 531
  - `skipping_shores_v3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 351
  > 💬 send_and_receive_2
  > 💬 send_and_receive
  > 💬 Old comments moved here from advanced_stones.level_set:
  > 💬 Any levels which are almost completely just SSTLH mechanics
  > 💬 Vanilla skipping stones mechanics (but with interactions not seen in skipping stones)
  > 💬 need_multipush
  > 💬 *choice
  > 💬 backpedal
  > 💬 double_backpedal
  > 💬 *choice
  > 💬 ocean_square
  > 💬 *choice
  > 💬 hit_midflight # Could be better. I feel like some sort of level like this is good to lead you to the right place in the next level.
  > 💬 Wait haha I just played through hit_midflight again and realized it's _super_ trivial. Just going to comment out for now.
  > 💬 hit_midflight_bridge
  > 💬 *choice
  > 💬 Skipping stones levels that are possible with multiple characters but not with only one
  > 💬 skip_team_intro
  > 💬 stonecross
  > 💬 *choice
  > 💬 skip_team_rescue
  > 💬 skip_team_strand # There are two solutions at the end of this one, but both solutions feel intended/interesting so I don't think it's a problem.
  > 💬 *choice
  > 💬 skip_team_block
  > 💬 skip_team_ocean
  > 💬 *choice
  > 💬 skip_team_river

### sky_promesst_misc

- 机制标签: `beams`；关卡 3 个（其中分支 *choice 2 处，磁盘命中 3）
  > 💬 A few misc 3D Promesst topics
  - `green_hat` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 211
  - `its_a_tall_order` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 275
  - `high_endpoint_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 209
  > 💬 Rovers in 3D
  > 💬 rover_hat
  > 💬 rover_stack
  > 💬 skip_rover_move_t
  > 💬 *choice

### spawners

- 机制标签: `stones beams`；关卡 9 个（其中分支 *choice 9 处，磁盘命中 9）
  > 💬 These are "exploit via Activator" levels, 1 for each world.
  > 💬 Could be structured better in the usual 4-way cross to grant
  > 💬 access to the rest of Endgame 2.
  > 💬 For what they are, I like them, but:
  > 💬 'recycling' was harder than the other ones and less clear,
  > 💬 so I made a design revision for increased clarity.  -jblow, 1 January 2025
  - `easy_reset_small` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 292
  - `reset_mirror` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 287
  - `wrong_reset` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 288
  - `recycling` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 295
  - `falling_button` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 162
  > 💬 draft:fall_reset
  > 💬 draft: rover_uses
  - `treadmill` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 175
  > 💬 leapfrog is ***VERY HARD***. It's essentially a maze where
  > 💬 there's not much clue which way to go and it's easy to go
  > 💬 way down a route thinking about the wrong thing. It should
  > 💬 not be in endgame2; maybe on a "very hard challenge" screen
  > 💬 for Underworld. Or Daily Challenge????
  > 💬 I don't think leapfrog_version is really better, just smaller.
  > 💬 But it's hard to know since I had to spoil myself on leapfrog
  > 💬 in order to solve it at all.
  > 💬 For now I am going to move it to daily_challenge.
  > 💬 leapfrog # even smaller version: leapfrog_version
  > 💬 monster_spawn should be rotated 90 degrees probably...
  > 💬 Very cool level though.
  - `monster_spawn` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 288
  - `fall_reset_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 288
  - `reset_trio` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 141

### strength（力量 / Strength）

- 机制标签: `beams`；关卡 6 个（其中分支 *choice 5 处，磁盘命中 6）
  > 💬 Strength in 3D
  > 💬 (comments and commented-out levels have been moved to spreadsheet)
  - `buff_explorer` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 209
  - `cyan_bridge_v3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 215
  - `under_pressure` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 209
  - `strong_monsters_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 233
  - `floorhands_v5` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 244
  - `stay_lit` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 180

### underworld_crossroads

- 机制标签: `star`；关卡 1 个（其中分支 *choice 1 处，磁盘命中 1）
  - `push_down_chain` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 185
  > 💬 Very misc levels with beams and advanced things
  > 💬 Mostly just beams puzzles I don't know where to put yet
  > 💬 Almost all of these have wrapping or 3d or artifacts which are concepts I haven't touched much yet so that's why they're here.
  > 💬 Most of these came from what used to be advanced_beams
  > 💬 3D
  > 💬 gem_field
  > 💬 gem_field2
  > 💬 gem_field2b
  > 💬 gem_field2c
  > 💬 *choice
  > 💬 multipurpose_security_beam
  > 💬 escape_tunnel
  > 💬 *choice
  > 💬 There were some rule changes since build_wall and build_wall2
  > 💬 were designed, so maybe they are simpler. At least one of them
  > 💬 doesn't need both blocks in order to be completed.
  > 💬 Maybe we should tighten them up.  -jblow, 5 November 2018
  > 💬 build_wall
  > 💬 build_wall2
  > 💬 .. now in drafts_maya.

### underworld_heroes_and_mirrors

- 机制标签: `heroes mirrors`；关卡 25 个（其中分支 *choice 21 处，磁盘命中 25）
  > 💬 Beginning path
  - `crystal_island` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 209
  - `army_v5` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 222
  > 💬 companion_cube
  > 💬 Mirror hyper jumping:
  > 💬 high_skip_v3
  > 💬 *choice
  > 💬 3D, mirrorable mirror, simple / easy.
  > 💬 A little bit like the 'fallible' wizard bounce falling level, but much simpler construction-wise...
  - `base_jump` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 221
  - `hyper_jump` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 226
  - `hyper_jump_2c` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 326
  > 💬 hyper_jump3  # Currently broken (code-wise) but I want to fix it.
  > 💬 *choice
  > 💬 Wrapping metamirrors:
  > 💬 I am not sure which of self_teleporting and self_teleporting_small
  > 💬 is best, so I am leaving them both in here for now. We'll decide
  > 💬 later. self_teleporting makes the exit seem much farther away,
  > 💬 but self_teleporting_small has the elegance of compactness.
  > 💬 There is no other size in-between that works, because the world
  > 💬 size in X has to be a multiple of 3, and X - Y mod 3 must be 2.
  > 💬 -jblow, 1 May 2019
  > 💬 Update, 20 December 2023: My hunch is to go with the big one, even
  > 💬 though it is in principle the wrong one. Not sure why. We'll see.
  - `self_teleporting` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 162
  > 💬 self_teleporting_small
  > 💬 wrapping with mirrorable mirrors (and cool sleds).
  > 💬 I think there is still some more interesting stuff that can be done here,
  > 💬 and/or these levels improved:
  - `wrapping_mirror0` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 160
  - `wrapping_mirror0_relatively_prime` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 151
  > 💬 It is what it is...
  - `the_line_must_be_drawn_HERE` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 117
  > 💬 wrapping with mirrorable vertical mirror:
  - `wrapping_mirror_alt` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 155
  > 💬 wrapping_mirror2 # Daily challenge potential
  > 💬 Mirrorable mirrors, 3D.
  - `lemonade_tng_stages_towers_no_float` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 289
  > 💬 Mirrorable mirror, kinda like wrapping_mirror but without wrapping
  > 💬 and more about the state machine kinda behavior that the mirrors
  > 💬 go through. Maybe messy because you can clone the rock a bunch
  > 💬 but this doesn't necessarily lead to a solution (but might make
  > 💬 the level confusing?)
  - `lemonade` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 389
  > 💬 Druid mirroring crystalized characters underwater
  - `druid_vertical_mirror` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 282
  - `special_move` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 192
  > 💬 Two extreme goblin + mirrors situations
  - `goblin_hat_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 257
  - `pigeonhole_squished` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 277
  > 💬 Extrene mirror mechanisms
  - `bottleneck` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 275
  > 💬 hanoi_intro
  - `hanoi_3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 340
  > 💬 hanoi_4
  - `busy_beaver` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 212
  - `moving_through_mirrors_v3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 387
  > 💬 the_cloud_from_braid
  > 💬 *choice
  > 💬 Hero abilities + Metamirrors
  - `druid_metamirror` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 166
  - `mirror_the_unmirrorable_mirror` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 222
  - `bard_metamirror` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 162
  > 💬 Lily, Mirrors, Monsters
  > 💬 stasis0 and stasis are meant to be later-game levels (underground?)
  > 💬 stasis0
  - `stasis_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 234
  - `far_cl_no_walls_pit` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 239

### underworld_heroes_and_promesst

- 机制标签: `heroes beams`；关卡 23 个（其中分支 *choice 21 处，磁盘命中 23）
  > 💬 Heroes dense wrapping
  - `torus_goblins` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 132
  - `wasteland` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 127
  - `torus_blocks_alt_v4` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 152
  - `torus_bard` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 154
  - `grid_hopping0` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 139
  > 💬 careful_smashing
  > 💬 wrapping_wizard
  > 💬 grid_hopping
  > 💬 drill
  > 💬 swap_smash
  > 💬 swap_smash2
  > 💬 swap_smash3
  > 💬 torus_sokoban # Daily challenge potential
  > 💬 torus_wizard
  > 💬 equator
  > 💬 equator2
  > 💬 equator3
  > 💬 equator_and_prime_meridian_alt
  > 💬 Jengas, kind of
  - `jenga_assorted` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 205
  - `how_to_train_your_dragon` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 190
  > 💬 stacker_v2
  > 💬 crowded
  > 💬 crowded_assorted
  > 💬 Heroes and tall cliffs
  - `ice_climbers` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 227
  - `battle_royale_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 379
  > 💬 Advanced wand, with only Promesst elements
  - `wand_reintro` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 318
  > 💬 Dense wrapping with *some* heroes elements
  - `endpoint_wrap_druid_alt` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 201
  - `endpoint_maze` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 261
  - `pat_on_the_back_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 166
  > 💬 Extrapolations off of a sokoban level
  > 💬 priest_wizard_wrapping
  > 💬 stone_teleport_v2
  > 💬 test_the_waters
  > 💬 *choice
  > 💬 end_lily_bridge2 # Daily challenge potential
  > 💬 *choice
  > 💬 H+S+P
  - `triple_skip` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 183
  - `quadruple_skip` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 102
  - `3wc_into_forest_v7` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 248
  - `3wcn_stonehenge` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 243
  - `limited_offsets` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 217
  - `limited_offsets_surprise_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 277
  > 💬 Crystal Rovers room:
  - `mirror_crystal_rover` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 133
  - `crystal_rover_rush` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 152
  - `crystal_rover_bridge` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 162
  - `perch_3_rovers` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 144

### underworld_lilies

- 机制标签: `heroes stones`；关卡 4 个（其中分支 *choice 4 处，磁盘命中 4）
  > 💬 Beginning path
  - `zach_lilies_v3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 318
  > 💬 Lily rafts screen
  - `raft_corners_alt_3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 143
  - `raft_corners_2_small` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 190
  - `raft_corners_4x4` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 174

### underworld_mirrors_and_promesst

- 机制标签: `mirrors beams`；关卡 19 个（其中分支 *choice 19 处，磁盘命中 19）
  > 💬 Wrapping non-meta mirrors:
  - `torus_mirrors` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 107
  - `wrapping_magic_mirror_2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 185
  - `double_sided_skip` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 190
  > 💬 Diverting in preferred directions forced by mirrors:
  - `water_bender_v3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 218
  > 💬 Mega clone and merge
  - `mega_clone_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 229
  - `mega_merge_v5` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 190
  > 💬 Alter-Smash Room:
  - `nowhere_to_smash_combo` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 312
  - `get_through_alt` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 203
  - `get_through_depths` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 229
  - `save_for_later` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 302
  - `rubble_chain` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 348
  - `do_not_want` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 293
  - `smartbomb_combo_v3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 381
  > 💬 Endpoint Toggler Room:
  - `beam_me_up_v3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 292
  - `toggler00` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 225
  - `two_half_togglers` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 234
  - `purple_heart` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 269
  > 💬 half_toggler
  > 💬 Probably not necessary given half_toggler. half_toggler0
  > 💬 toggler0  # Redundant, not worth including.
  > 💬 toggler
  > 💬 endpoint_levitation
  > 💬 *choice
  > 💬 Advanced endpoint beam located at the world border
  - `half_journey_vh` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 274
  - `3wcn_purple_goblin` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 313

### underworld_skipping_and_promesst

- 机制标签: `stones beams`；关卡 17 个（其中分支 *choice 17 处，磁盘命中 17）
  - `bon_voyage` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 243
  > 💬 Hover technique:
  > 💬 Endpointing stones
  > 💬 These feel like a fun-nish advanced surprise.
  > 💬 This level set was split off from advanced_mirrorable_stones because
  > 💬 it seems pretty different, especially with regard to what the overworld
  > 💬 puzzle would be.  -jblow, 19 December 2023
  > 💬 endpoint_holder0
  > 💬 *choice
  - `skip_purple_drop_alt` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 219
  > 💬 endpoint_holder1 # This feels almost the same as the previous, the box doesn't even need to be move#d so I think it's an exploit.
  > 💬 endpoint_holder2
  > 💬 endpoint_holder
  > 💬 *choice
  - `endpoint_holder3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 175
  - `endpoint_holder4` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 234
  - `mobile_cover_2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 239
  - `hover_corner_3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 197
  - `hover_corner_4` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 164
  > 💬 Not hover technique:
  - `tricky_endpoint` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 216
  - `drop_operation_v3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 228
  - `retvrn0` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 254
  - `defender` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 361
  - `juggalos` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 222
  - `smash_midskip_simpler4` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 195
  - `chain_reaction` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 208
  > 💬 sprint2 is in here and not beams_and_stones because it involves wrapping.
  > 💬 We could make a version that does not involve wrapping, but it requires another
  > 💬 object to block the beam. I am not sure if that's better.  -jblow, 19 December 2023
  > 💬 sprint2
  > 💬 *choice
  > 💬 Skipping with endpoint beam; may be redundant with some other endpoint beam skipping
  > 💬 level I did, but if so, maybe this one is simpler?
  > 💬 [ Update on the above note: We decided to consolidate these levels, and we deprecated this sequence in favor of using only other levels. see advanced_beams_and_stones.level_set. -Patrick 2025-01-27 ]
  > 💬 delayed_endpoint_slot_intro
  > 💬 delayed_endpoint_slot
  > 💬 delayed_endpoint_slot2
  > 💬 *choice
  > 💬 mobile_cover
  > 💬 *choice
  > 💬 duckling
  > 💬 *choice
  > 💬 Rotating beams on lillies
  - `river_rotate_beams_gr` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 246
  - `kick` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 281
  - `lily_two_cyan` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 241
  > 💬 red_light_green_light # Slightly worried that if this is grouped in with exclusively other lily rotation levels, it will ruin some of the surprise. (It's not that hard of a level, just a cute moment.)
  > 💬 red_light_green_light_v2
  > 💬 Goes with spin_doctors and rotator; maybe not interesting enough to ship without further improvements.
  > 💬 odd_stop0
  > 💬 odd_stop

### vertical_endpoint

- 机制标签: `beams`；关卡 3 个（其中分支 *choice 2 处，磁盘命中 3）
  > 💬 Vertical endpointing without mirrors
  - `landmines_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 272
  - `shower` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 164
  - `sender_simplified_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 214

### vertical_mirrors（竖直之镜 / Vertical Mirrors）

- 机制标签: `mirrors`；关卡 31 个（其中分支 *choice 23 处，磁盘命中 31）
  > 💬 Vertical magic mirrors.
  > 💬 (comments and commented-out levels have been moved to spreadsheet)
  > 💬 Climbing the pyramid
  > 💬 Intro to vertical mirrors, mostly planar levels
  - `vert_mirror_intro` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 264
  - `portable_stairs` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 309
  - `drawbridge` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 197
  - `implausible_bridge` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 198
  - `overwrite` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 255
  - `bottom_bridge_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 228
  - `bottom_bridge_tall` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 248
  - `mission_impossible` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 263
  - `repel` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 138
  > 💬 Pool above
  - `new_way_mirror_later` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 257
  - `implausible_bridge_2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 270
  > 💬 Timing with warrior
  - `catching_up_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 246
  - `quick_redirect_v5` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 163
  - `to_kill_a_goblin` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 389
  - `tall_stack` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 214
  - `bottom_adjust` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 252
  > 💬 Down again
  > 💬 Clones
  - `chasm_3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 257
  - `vertical_unclone_3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 282
  > 💬 Misc
  - `juggle` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 318
  - `wolf_boat_carry` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 257
  > 💬 The next 5 levels form something of a mini narrative-adventure starring
  > 💬 the Thief, with a DARING RESCUE at the end.
  > 💬 Vertical mirrors:
  - `bridgey` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 180
  - `bridgey2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 177
  - `bridgey2b` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 189
  - `bridgey3_abstract_art` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 212
  - `all_out_goblin_war` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 250
  - `escape_bridge` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 236
  > 💬 We rescued Priest from All Out Goblin War. Or something. A more difficult, later level. Involves vertical mirrors.
  - `tandem` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 204
  > 💬 Now in the Vertical Mirror Upward area heading into end2:
  > 💬 Reflecting dragon breath
  - `flamestrike_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 250
  - `volcano_v3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 255
  > 💬 Vertical Mirrors and the Promesst guy
  - `pachinko` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 243
  - `pachinko_rescue_w` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 276

### vertical_promesst

- 机制标签: `beams`；关卡 1 个（其中分支 *choice 1 处，磁盘命中 1）
  - `vertical_promesst_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 240

### vertical_reflection

- 机制标签: `beams`；关卡 11 个（其中分支 *choice 10 处，磁盘命中 11）
  > 💬 Vertical non-magic mirrors reflecting beams
  > 💬 (comments and commented-out levels have been moved to spreadsheet)
  - `seeing_red` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 284
  - `vacuum` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 276
  - `pink_platforms` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 171
  - `one_floor_down_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 278
  > 💬 Vertical endpoint suspend series:
  - `suspend_intro` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 272
  - `suspend_block_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 303
  - `suspend_heterogeneous` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 301
  - `suspend_directions_v2` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 237
  - `suspend_swapper_hard` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 224
  > 💬 endpoint_suspend_1_alt1
  > 💬 *choice
  > 💬 block_suspend_alt1
  > 💬 *choice
  > 💬 endpoint_suspend_heterogeneous2
  > 💬 endpoint_suspend_directions
  > 💬 endpoint_suspend_directions_swapper
  > 💬 *choice
  - `beam_jail_v3` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 272
  > 💬 With a magic vertical mirror.
  - `height_chooser_v0` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 214

### worlds_collide

- 机制标签: `star`；关卡 6 个（其中分支 *choice 0 处，磁盘命中 6）
  > 💬 Every level here mixes a different pair of worlds, so the transition glyphs are given per level
  > 💬 with *level_glyphs. *glyphs star is the fallback if a level is missing its override.
  > 💬 collide_ms
  > 💬 collide_hm
  > 💬 collide_mp
  > 💬 collide_ps
  > 💬 collide_hp
  > 💬 collide_hs
  > 💬 Would have been named worlds_collide_promesst_and_mirrors, but predates this organization.
  - `worlds_collide_alt` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 277
  - `worlds_collide_heroes_and_stones` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 476
  > 💬 Unlike some of the other worlds_collide levels, in this level the heroes don't have a lot of individual
  > 💬 puzzling to do initially; it's more about working together right away. Maybe that's fine for variety,
  > 💬 though.
  - `worlds_collide_heroes_and_promesst_v4` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 457
  - `worlds_collide_heroes_and_mirrors_v3` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 414
  > 💬 worlds_collide_promesst_and_stones_v3
  - `worlds_collide_ps` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 364
  > 💬 worlds_collide_mirrors_and_stones
  - `worlds_collide_mirrors_and_stones_v2` ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 228
  > 💬 These are the main levels from the trailer,
  > 💬 so people can use the 'level' command to go there.
  > 💬 heroes_for_trailer_v3
  > 💬 mirror1_for_trailer_v3
  > 💬 promesst_for_trailer_v3
  > 💬 skipping_stones_for_trailer
  > 💬 invisible_hand_for_trailer

### zachtronics

- 机制标签: `heroes beams`；关卡 4 个（其中分支 *choice 4 处，磁盘命中 4）
  > 💬 Zachtronics
  > 💬 These Become Pretty Advanced.
  - `zachtronics_identity` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 315
  > 💬 zachtronics_or is more complicated than necessary; see zachtronics_or_simplified
  > 💬 (but that simplification makes it work differently than the other levels, which is
  > 💬 bad for the sequence and also bad for the surprise of the level, since we are
  > 💬 then adding multiple other basic differences not having to do with the surprise).
  - `zachtronics_or` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 331
  - `zachtronics_xor` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 328
  > 💬 zachtronics_or_simplified   # There is no valid solution here I think, as it would need to be redesigned a bit for the same 'trick' to work, probably with having too many stones instead of too many crystals.
  - `zachtronics` ← *choice 分支 ｜ 实体 845（Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16）｜ 资源 327

## 五、全部关卡总表（974 关，按名称排序）

| 关卡 ID | 所在关卡集 | 实体总数 | 机制指纹 top5 | 资源数 |
|---|---|---|---|---|
| `3d_intro_heroes` | intro_to_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 312 |
| `3d_intro_mirrors` | drafts_story, intro_to_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 208 |
| `3d_intro_promesst_v5` | intro_to_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 239 |
| `3d_intro_skipping` | intro_to_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 231 |
| `3d_intro_vanilla` | drafts_story, intro_to_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 196 |
| `3wc_into_forest_v7` | drafts_arted, underworld_heroes_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 248 |
| `3wcn_purple_goblin` | drafts_arted, underworld_mirrors_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 313 |
| `3wcn_purple_mirror_skip` | orange_beam_highway_worlds_collide | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 299 |
| `3wcn_shm_dragon_lily` | orange_beam_highway_worlds_collide | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 331 |
| `3wcn_stonehenge` | underworld_heroes_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 243 |
| `4wc_dragon_cyan_s_v2` | orange_beam_highway_worlds_collide | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 532 |
| `4wcn_all_fast` | orange_beam_highway_worlds_collide | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 385 |
| `a_wiz_out_of_water` | drafts_arted, heroes_and_water | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 295 |
| `accidentally_unlock_v2` | beaming_objects, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 239 |
| `across_the_fence_old` | design_illustrations | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 61 |
| `across_the_fence_vtrader_m_p` | beams_and_mirrors, design_illustrations, drafts_arted, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 277 |
| `adjust_explorer_v4` | beams_and_mirrors, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 166 |
| `after_wings` | lily_highway_mirrors_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 218 |
| `aggro_maze` | drafts_arted, drafts_good_looking, goblin_rotation | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 184 |
| `aggro_which0` | drafts_arted, goblin_rotation | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 209 |
| `air_skating_v6` | double_beam_falling, drafts_arted, drafts_good_looking | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 171 |
| `airmail` | drafts_arted, drafts_story, mirrors_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 161 |
| `all_out_goblin_war` | drafts_arted, drafts_good_looking, drafts_story, vertical_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 250 |
| `all_together_now` | endgame2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 448 |
| `allocate_heroes_end3` | endgame3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 312 |
| `allocate_heroes_v2` | endgame2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 357 |
| `already_dropped_v2` | drafts_arted, mirrors_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 219 |
| `annoying_orange_v3` | double_beam_falling, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 175 |
| `another_stone_stopper` | drafts_arted, heroes_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 228 |
| `arcadia_surprise_big` | clones, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 183 |
| `arcadia_surprise_big2` | clones, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 202 |
| `arcadiav2_big` | clones, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 177 |
| `archways_2_v2` | drafts_arted, drafts_good_looking, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 192 |
| `archways_4` | drafts_arted, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 189 |
| `army_v5` | drafts_arted, underworld_heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 222 |
| `assassins_creed` | drafts_arted, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 223 |
| `automatic_door_v5` | drafts_arted, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 182 |
| `baby_steps_line` | drafts_arted, heroes_and_water | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 303 |
| `bad_aim_v2` | drafts_arted, mirrorable_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 286 |
| `bard_metamirror` | drafts_arted, underworld_heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 162 |
| `bard_movable_island` | advanced_bard_and_water, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 292 |
| `bard_movable_island2` | advanced_bard_and_water, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 296 |
| `bard_must_stack4_fix` | drafts_arted, drafts_good_looking, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 267 |
| `bard_range3_with_intro` | drafts_arted, drafts_good_looking, heroes_and_water | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 291 |
| `bard_range4` | drafts_arted, heroes_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 179 |
| `bard_range5` | drafts_arted, heroes_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 203 |
| `bard_range6` | drafts_arted, heroes_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 182 |
| `bard_stack_intro` | drafts_arted, drafts_good_looking, heroes_and_water | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 236 |
| `bard_triangle` | drafts_arted, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 245 |
| `base_jump` | drafts_arted, drafts_good_looking, underworld_heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 221 |
| `battle_royale_v2` | drafts_arted, underworld_heroes_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 379 |
| `be_aggro_alt_2` | beams_and_basic_heroes, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 347 |
| `beam_jail_v3` | drafts_arted, vertical_reflection | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 272 |
| `beam_me_up_v3` | drafts_arted, underworld_mirrors_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 292 |
| `beam_rooms` | drafts_arted, promesst1_and_2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 192 |
| `beam_shatter` | beams_and_basic_heroes, drafts_arted, drafts_story | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 233 |
| `beam_sisters` | beam_carrying, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 220 |
| `before_wings` | lily_highway_mirrors_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 267 |
| `best_beam_colors` | endgame3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 332 |
| `binary_maze` | beams_and_basic_heroes, drafts_arted, drafts_story | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 196 |
| `bitstring_small` | drafts_arted, heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 241 |
| `blind_spot_v2` | drafts_arted, drafts_story, mirrors_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 246 |
| `blocking_issue` | drafts_arted, heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 218 |
| `blue_revolution_v2` | drafts_arted, promesst1_and_2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 268 |
| `boat_priest_v3` | advanced_bard_and_water, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 392 |
| `bon_voyage` | drafts_arted, underworld_skipping_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 243 |
| `boot_cycle_warrior` | drafts_arted, gems | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 190 |
| `both_ways` | drafts_arted, heroes_and_water | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 250 |
| `bothersome_mirror` | drafts_arted, mirrors_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 264 |
| `bottleneck` | underworld_heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 275 |
| `bottom_adjust` | drafts_arted, vertical_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 252 |
| `bottom_bridge_tall` | drafts_arted, drafts_good_looking, vertical_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 248 |
| `bottom_bridge_v2` | drafts_arted, drafts_good_looking, vertical_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 228 |
| `boxes_vs_crystals` | beaming_objects, drafts_arted, drafts_good_looking | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 285 |
| `break_send_lily_c` | beams_and_stones, drafts_arted, drafts_trailer | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 192 |
| `break_through_focused` | beams_and_mirrors, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 302 |
| `breaking_bread` | drafts_arted, drafts_good_looking, gems | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 279 |
| `breath_skip` | drafts_arted, drafts_story, heroes_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 220 |
| `bridgey` | drafts_arted, drafts_story, vertical_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 180 |
| `bridgey2` | drafts_arted, drafts_story, vertical_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 177 |
| `bridgey2b` | drafts_arted, drafts_story, vertical_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 189 |
| `bridgey3_abstract_art` | drafts_arted, drafts_arted, drafts_story, drafts_story, vertical_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 212 |
| `buff_explorer` | drafts_arted, strength | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 209 |
| `bug_spray` | drafts_arted, drafts_story, heroes_and_artifacts | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 178 |
| `busy_beaver` | drafts_arted, drafts_good_looking, underworld_heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 212 |
| `button_and_beam_v3` | drafts_arted, monsters_and_beams | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 237 |
| `button_clone_journey` | clones, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 176 |
| `button_playground` | beams_and_basic_heroes, drafts_arted, drafts_story | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 289 |
| `button_shut_in` | drafts_arted, drafts_good_looking, skipping_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 362 |
| `bypass_gates` | beams_and_basic_heroes, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 201 |
| `cancel_out` | drafts_arted, mirrors_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 178 |
| `carry_lily` | drafts_arted, skipping_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 142 |
| `carry_simplified` | drafts_story, intro_to_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 181 |
| `catch_and_drop` | drafts_arted, drafts_story, mirrorable_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 284 |
| `catch_and_throw` | drafts_arted, drafts_story, mirrorable_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 209 |
| `catching_fire_v2` | drafts_arted, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 235 |
| `catching_up_v0` | design_illustrations | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 63 |
| `catching_up_v2` | design_illustrations, drafts_arted, drafts_arted, vertical_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 246 |
| `chain_gang` | drafts_arted, drafts_good_looking, goblin_rotation | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 201 |
| `chain_gang3` | drafts_arted, goblin_rotation | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 207 |
| `chain_reaction` | drafts_arted, underworld_skipping_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 208 |
| `chart_a_course` | endgame2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 222 |
| `chasm_3` | drafts_arted, vertical_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 257 |
| `cleric_fly_intro3_v2` | drafts_arted, heroes_and_water | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 228 |
| `cleric_isles` | beams_and_basic_heroes, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 240 |
| `cliff_duo` | drafts_arted, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 139 |
| `cliff_hopping` | drafts_arted, drafts_good_looking, drafts_story, mirrors_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 223 |
| `clone_adjust` | clones, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 168 |
| `clone_adjust_mirror` | clones, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 164 |
| `clone_adjust_two_rocks` | clones, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 150 |
| `clone_goblin` | drafts_arted, heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 416 |
| `clone_maze` | clones, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 159 |
| `close_circuit` | beams_and_stones, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 194 |
| `close_to_button` | drafts_arted, heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 287 |
| `coax_a_lot` | drafts_arted, mirrors_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 252 |
| `color_picker` | endgame2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 251 |
| `come_closer` | drafts_arted, heroes_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 218 |
| `compactor_v2` | drafts_story, heroes3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 243 |
| `connect_the_dots_v5` | drafts_arted, drafts_story, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 235 |
| `corner_loop` | beams_and_basic_heroes, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 222 |
| `corner_trick_easier` | beam_carrying, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 237 |
| `crystal_bridges` | drafts_arted, drafts_good_looking, drafts_story, heroes_and_water | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 297 |
| `crystal_island` | drafts_arted, underworld_heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 209 |
| `crystal_logistics` | beam_carrying, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 260 |
| `crystal_rover_bridge` | drafts_arted, underworld_heroes_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 162 |
| `crystal_rover_intro` | drafts_arted, promesst3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 264 |
| `crystal_rover_rush` | drafts_arted, underworld_heroes_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 152 |
| `crystals_not_stones` | drafts_arted, drafts_story, heroes_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 223 |
| `cyan_bridge_v3` | drafts_arted, drafts_good_looking, strength | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 215 |
| `cyan_counter_med3` | beams_and_mirrors, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 294 |
| `cyan_overlap_intro_longer` | promesst1_and_2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 342 |
| `cyan_torc_maze_vs` | beams_and_mirrors, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 368 |
| `defender` | drafts_arted, underworld_skipping_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 361 |
| `delay_time_v2` | drafts_arted, skipping_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 319 |
| `depositor_bard` | drafts_arted, drafts_story, skipping_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 288 |
| `depositor_thief` | drafts_arted, skipping_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 307 |
| `design_corner` | endgame3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 330 |
| `design_fts` | endgame3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 257 |
| `detachment` | drafts_arted, heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 269 |
| `detonator` | drafts_arted, drafts_story, heroes_and_water | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 294 |
| `diag_slide` | drafts_arted, mirrors_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 189 |
| `dipping_your_toes_in` | drafts_arted, drafts_story, heroes_and_water | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 271 |
| `ditching_cargo` | drafts_arted, mirrors_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 287 |
| `do_not_want` | underworld_mirrors_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 293 |
| `dont_push_the_button` | drafts_arted, drafts_story, heroes_and_water | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 288 |
| `doorstop` | beams_and_stones, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 232 |
| `doorstop_reprise_easier` | beams_and_stones, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 206 |
| `double_break` | drafts_arted, drafts_good_looking, heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 230 |
| `double_door` | beams_and_stones, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 214 |
| `double_sided_skip` | drafts_arted, underworld_mirrors_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 190 |
| `double_sideways` | beams_and_mirrors, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 149 |
| `double_team` | beams_and_basic_heroes, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 162 |
| `double_tempo` | beams_and_basic_heroes, drafts_arted, drafts_story | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 293 |
| `double_the_fun` | drafts_arted, elevators | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 214 |
| `double_trouble` | double_beam_falling_dropdown, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 123 |
| `double_up` | double_beam_falling, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 192 |
| `dragon_bridge` | drafts_arted, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 225 |
| `dragon_compass` | drafts_arted, heroes_and_water | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 243 |
| `dragon_drag` | beams_and_stones, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 167 |
| `dragon_garden` | heroes_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 262 |
| `dragon_on_the_wall` | drafts_arted, drafts_good_looking, sideways_gates | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 262 |
| `dragons_layer` | double_beam_falling, drafts_arted, drafts_good_looking, drafts_story | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 204 |
| `dragonsweeper` | drafts_arted, drafts_good_looking, monsters_and_beams | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 226 |
| `drawbridge` | drafts_arted, vertical_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 197 |
| `drop_off` | advanced_bard_and_water, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 300 |
| `drop_operation_v3` | drafts_arted, drafts_arted, underworld_skipping_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 228 |
| `drop_sokoban` | drafts_arted, elevators | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 184 |
| `drop_tool` | drafts_arted, heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 263 |
| `drowner` | drafts_arted, drafts_story, heroes_and_water | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 329 |
| `druid_3d_beam` | drafts_arted, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 194 |
| `druid_and_dragon` | drafts_story, heroes3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 241 |
| `druid_metamirror` | drafts_arted, underworld_heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 166 |
| `druid_multismash_v3` | beams_and_basic_heroes, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 151 |
| `druid_stone_p` | drafts_arted, heroes_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 145 |
| `druid_vertical_mirror` | drafts_arted, underworld_heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 282 |
| `druids_stone_0_v2` | drafts_arted, drafts_story, heroes_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 158 |
| `druids_stone_2_v4` | drafts_arted, drafts_story, heroes_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 192 |
| `druids_stone_alt` | drafts_arted, drafts_story, heroes_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 177 |
| `dual_screen` | beams_and_mirrors, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 136 |
| `duality_2` | lily_highway_stones_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 279 |
| `duality_condensed` | drafts_arted, drafts_good_looking, lily_highway_stones_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 303 |
| `dunk_tank_alt` | drafts_arted, heroes_and_water | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 258 |
| `easy_reset_small` | spawners | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 292 |
| `easy_situation_v2` | drafts_arted, heroes_and_water | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 270 |
| `elevator_cyan` | drafts_arted, elevators | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 177 |
| `elevator_mechanic` | endgame2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 263 |
| `elope` | drafts_arted, heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 268 |
| `emergency_brake` | drafts_arted, drafts_story, mirrors_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 175 |
| `en_root_alt` | drafts_arted, monsters_and_beams | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 226 |
| `end1` | drafts_arted, endgame1 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 817 |
| `end2_clone_divergence` | endgame3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 174 |
| `end2_clone_divergence_2` | endgame3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 170 |
| `end2_heroes_1_2` | drafts_story, endgame2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 293 |
| `end2_heroes_1_5` | drafts_story, endgame2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 303 |
| `end2_mirror1` | drafts_arted, endgame3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 203 |
| `end2_mirror_3` | drafts_arted, endgame2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 202 |
| `end2_mirror_4_islands_v2` | drafts_arted, endgame3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 211 |
| `end2_monster_connect` | endgame2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 285 |
| `end2_prism_hp` | endgame2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 344 |
| `end2_river_place` | endgame2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 404 |
| `end3_denoise_pool` | endgame3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 317 |
| `end3_heroes_1` | endgame3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 372 |
| `end3_mirror_1_v3` | endgame3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 219 |
| `end3_mirror_2_alt2` | endgame3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 231 |
| `end3_off_topic_alt` | endgame3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 458 |
| `end3_off_topic_heroes` | endgame3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 433 |
| `end3_off_topic_mirror` | endgame3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 327 |
| `end3_pipeline_aesthetics` | endgame3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 332 |
| `end3_pipeline_cleanup` | endgame3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 145 |
| `end3_pipeline_cut` | endgame3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 144 |
| `end3_pipeline_design` | endgame3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 149 |
| `end3_pipeline_reorder` | endgame3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 145 |
| `end3_pipeline_setup` | endgame3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 116 |
| `end3_promesst_red` | endgame3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 869 |
| `end3_redundant_beams` | endgame3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 355 |
| `end3_reorder_mirror` | endgame3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 493 |
| `end3_reorder_skipping_fix` | endgame3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 311 |
| `end3_skipping_1` | endgame3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 190 |
| `end3_skipping_red` | endgame3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 221 |
| `endpoint1_skipping` | beams_and_stones, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 201 |
| `endpoint_gates` | beams_and_basic_heroes, drafts_arted, drafts_good_looking | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 260 |
| `endpoint_holder3` | drafts_arted, underworld_skipping_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 175 |
| `endpoint_holder4` | drafts_arted, underworld_skipping_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 234 |
| `endpoint_maze` | underworld_heroes_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 261 |
| `endpoint_object` | beaming_objects, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 254 |
| `endpoint_team` | beams_and_basic_heroes, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 227 |
| `endpoint_weapon` | beams_and_basic_heroes, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 357 |
| `endpoint_wrap_druid_alt` | underworld_heroes_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 201 |
| `env_corral` | — | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 18 |
| `environment_art_background` | endgame3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 349 |
| `environment_art_grid` | endgame3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 173 |
| `environment_art_objects` | endgame3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 279 |
| `erosion_alt` | drafts_arted, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 245 |
| `escape_bridge` | drafts_arted, vertical_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 236 |
| `fail_to_mirror_sequence_v2` | drafts_arted, orange_beam_highway_mirrors_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 442 |
| `fall_reset_v2` | spawners | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 288 |
| `falling_blocker_v3` | drafts_arted, drafts_story, mirrors_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 196 |
| `falling_button` | spawners | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 162 |
| `falling_down` | drafts_arted, drafts_good_looking, skipping_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 237 |
| `falloff_4` | drafts_arted, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 203 |
| `falloff_dragons` | drafts_arted, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 203 |
| `falloff_intro` | drafts_arted, drafts_good_looking, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 170 |
| `falloff_kill_goblins_v6` | drafts_arted, drafts_good_looking, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 207 |
| `far_cl_no_walls_pit` | drafts_arted, underworld_heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 239 |
| `far_river` | drafts_arted, mirrors_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 247 |
| `far_wings` | lily_highway_mirrors_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 259 |
| `faster_than_stone` | beams_and_stones, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 158 |
| `fire_and_flip` | drafts_arted, heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 314 |
| `fire_from_above_2` | double_beam_falling, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 198 |
| `fire_stairs_part_2` | drafts_arted, drafts_good_looking, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 255 |
| `fire_stairs_v2` | drafts_arted, drafts_good_looking, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 209 |
| `first_diversions` | drafts_arted, mirrors_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 280 |
| `first_flight` | double_beam_falling_dropdown, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 131 |
| `fix_exploit` | endgame3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 189 |
| `fix_exploit_promesst_overworld` | endgame3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 453 |
| `flame_wand` | drafts_arted, drafts_story, heroes_and_artifacts | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 240 |
| `flamestrike_v3` | drafts_arted, vertical_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 250 |
| `flamethrower` | drafts_arted, heroes_and_water | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 210 |
| `flip_flop_v2` | drafts_arted, heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 234 |
| `floating_gardens` | drafts_arted, heroes_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 204 |
| `floating_orange_purple` | beams_and_mirrors, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 195 |
| `floor_plan_v3` | endgame2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 464 |
| `floorhands_v5` | drafts_arted, strength | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 244 |
| `fly_and_flip` | drafts_arted, heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 284 |
| `forbidden_room` | drafts_arted, promesst1_and_2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 291 |
| `four_horsemen` | drafts_arted, heroes_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 203 |
| `frame_advance_v5` | drafts_arted, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 229 |
| `frantic_factory_v2` | beams_and_stones, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 211 |
| `free_ride` | beams_and_stones, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 225 |
| `friendly_nudges` | beams_and_basic_heroes, drafts_arted, drafts_story | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 170 |
| `from_the_depths` | drafts_arted, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 276 |
| `front_side_bus2` | advanced_bard_and_water, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 318 |
| `front_side_bus3` | advanced_bard_and_water, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 249 |
| `frontier` | lily_highway_stones_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 245 |
| `fun_house` | beams_and_mirrors, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 283 |
| `fuse` | drafts_arted, drafts_good_looking, heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 292 |
| `gate_shatter` | drafts_arted, heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 186 |
| `gated_twice_thief_v2` | drafts_arted, drafts_story, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 259 |
| `gated_twice_v2` | drafts_arted, drafts_story, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 263 |
| `gatekeeping_v3` | heroes3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 232 |
| `gem_beam_placement` | beams_and_basic_heroes | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 360 |
| `gem_clg_v4` | beams_and_mirrors, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 326 |
| `gem_pushers` | drafts_arted, promesst1_and_2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 297 |
| `gem_slot_on_lily` | drafts_arted, flat_things | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 240 |
| `gem_transport` | beams_and_basic_heroes, drafts_arted, drafts_story | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 173 |
| `gem_transport_2` | beams_and_basic_heroes, drafts_arted, drafts_story | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 168 |
| `gem_trap` | drafts_arted, gems | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 286 |
| `gem_trap2` | drafts_arted, drafts_good_looking, gems | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 307 |
| `get_through_alt` | underworld_mirrors_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 203 |
| `get_through_depths` | underworld_mirrors_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 229 |
| `glass_beach` | beams_and_stones, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 224 |
| `goblin_below_intro_same_z` | drafts_arted, drafts_good_looking, goblin_rotation | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 235 |
| `goblin_express` | drafts_arted, heroes_and_water | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 295 |
| `goblin_hat_v2` | drafts_arted, drafts_good_looking, drafts_good_looking, underworld_heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 257 |
| `goblin_parity` | drafts_arted, heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 273 |
| `goblin_parity_3d` | drafts_arted, drafts_good_looking, mirrors_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 261 |
| `goblin_two_rovers_alt` | drafts_arted, monsters_and_beams | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 168 |
| `going_up_v4` | drafts_arted, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 225 |
| `green_crystal_rover` | beams_and_mirrors, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 172 |
| `green_goblins` | drafts_arted, monsters_and_beams | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 266 |
| `green_hat` | drafts_arted, sky_promesst_misc | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 211 |
| `green_metamirror` | beams_and_mirrors, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 334 |
| `green_revolution` | drafts_arted, drafts_good_looking, promesst1_and_2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 309 |
| `green_torq_mirror_vs4` | beams_and_mirrors, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 341 |
| `greenhouse` | drafts_arted, heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 235 |
| `grid_hopping0` | drafts_arted, drafts_good_looking, underworld_heroes_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 139 |
| `gully_alt` | drafts_arted, heroes_and_water | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 281 |
| `half_journey_vh` | drafts_arted, underworld_mirrors_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 274 |
| `half_tutorial` | promesst3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 280 |
| `hanoi_3` | drafts_arted, drafts_good_looking, underworld_heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 340 |
| `hat_chain_vp` | drafts_arted, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 220 |
| `hat_maker` | double_beam_falling, drafts_arted, drafts_good_looking | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 199 |
| `hat_tricks_0_v3` | drafts_arted, mirrors_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 258 |
| `height_chooser` | design_illustrations | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 79 |
| `height_chooser_v0` | design_illustrations, drafts_arted, drafts_arted, vertical_reflection | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 214 |
| `help_drop` | beams_and_basic_heroes, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 214 |
| `heroes1_1` | drafts_arted, drafts_story, heroes1 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 296 |
| `heroes1_10_inv_v4_b` | drafts_arted, drafts_story, heroes1 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 337 |
| `heroes1_11_v2` | drafts_arted, drafts_story, heroes1 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 208 |
| `heroes1_12_v2_alt` | drafts_arted, drafts_story, heroes1 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 272 |
| `heroes1_13_v2` | drafts_arted, drafts_story, heroes1 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 288 |
| `heroes1_15` | drafts_arted, drafts_story, heroes1 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 235 |
| `heroes1_16_v3` | drafts_arted, drafts_story, heroes1 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 267 |
| `heroes1_17` | drafts_arted, drafts_story, heroes1 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 278 |
| `heroes1_18` | drafts_arted, drafts_story, heroes1 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 278 |
| `heroes1_19_jail` | drafts_story, heroes1 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 297 |
| `heroes1_21_v3` | drafts_story, heroes1 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 305 |
| `heroes1_2_v2` | drafts_arted, drafts_story, heroes1 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 268 |
| `heroes1_3` | drafts_arted, drafts_story, heroes1 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 330 |
| `heroes1_4` | drafts_arted, drafts_story, heroes1 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 246 |
| `heroes1_4.5` | drafts_arted, drafts_story, heroes1 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 287 |
| `heroes1_5_v2` | drafts_arted, drafts_story, heroes1 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 274 |
| `heroes1_6` | drafts_arted, drafts_story, heroes1 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 240 |
| `heroes1_7` | design_illustrations | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 68 |
| `heroes1_7.5` | drafts_arted, drafts_story, heroes1 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 284 |
| `heroes1_7_v2` | design_illustrations, drafts_arted, drafts_story, heroes1 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 389 |
| `heroes1_8_v2` | drafts_arted, drafts_story, heroes1 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 272 |
| `heroes1_9` | drafts_arted, drafts_story, heroes1 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 241 |
| `heroes2_10` | drafts_arted, drafts_story, heroes2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 273 |
| `heroes2_10.5` | drafts_arted, drafts_story, heroes2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 235 |
| `heroes2_10a` | drafts_arted, drafts_story, heroes2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 248 |
| `heroes2_10a_intro` | drafts_arted, drafts_story, heroes2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 253 |
| `heroes2_11_v2` | drafts_arted, drafts_story, heroes2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 203 |
| `heroes2_11_v2_easier` | drafts_arted, drafts_story, heroes2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 234 |
| `heroes2_12_v2` | drafts_arted, drafts_story, heroes2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 226 |
| `heroes2_13` | drafts_arted, heroes2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 176 |
| `heroes2_14` | drafts_arted, drafts_story, heroes2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 200 |
| `heroes2_15` | drafts_arted, drafts_story, heroes2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 261 |
| `heroes2_16v4` | drafts_arted, drafts_story, heroes2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 219 |
| `heroes2_17` | drafts_arted, drafts_story, heroes2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 249 |
| `heroes2_17_intro` | drafts_arted, drafts_story, heroes2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 249 |
| `heroes2_18` | drafts_arted, drafts_story, heroes2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 213 |
| `heroes2_2` | drafts_arted, drafts_story, heroes2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 224 |
| `heroes2_20` | drafts_arted, drafts_story, heroes2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 205 |
| `heroes2_21b` | drafts_arted, drafts_story, heroes2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 188 |
| `heroes2_22_v2` | drafts_arted, drafts_story, heroes2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 225 |
| `heroes2_2b` | drafts_arted, drafts_story, heroes2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 250 |
| `heroes2_3_v2` | drafts_arted, drafts_story, heroes2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 224 |
| `heroes2_3monster` | drafts_arted, drafts_story, heroes2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 235 |
| `heroes2_5.5v5` | drafts_arted, drafts_story, heroes2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 265 |
| `heroes2_5_altE` | drafts_arted, drafts_story, heroes2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 372 |
| `heroes2_5_no_crystal` | drafts_arted, drafts_good_looking, drafts_story, heroes2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 280 |
| `heroes2_6_v3` | drafts_arted, drafts_story, heroes2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 264 |
| `heroes2_9` | drafts_arted, drafts_story, heroes2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 295 |
| `heroes2_reprise` | drafts_arted, drafts_story, heroes2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 295 |
| `heroes2_thief_goblin` | drafts_arted, drafts_story, heroes2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 242 |
| `heroes3_10` | drafts_arted, drafts_story, heroes3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 248 |
| `heroes3_11_v2` | drafts_arted, drafts_story, heroes3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 282 |
| `heroes3_13_v2` | drafts_arted, drafts_story, heroes3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 292 |
| `heroes3_14_v3` | drafts_arted, drafts_story, heroes3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 326 |
| `heroes3_15_v4` | heroes3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 217 |
| `heroes3_16_v4_alt` | drafts_story, heroes3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 233 |
| `heroes3_1_v3` | drafts_arted, drafts_story, heroes3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 242 |
| `heroes3_21_condensed` | drafts_story, heroes3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 243 |
| `heroes3_2_v4` | drafts_arted, drafts_story, heroes3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 260 |
| `heroes3_3_v2` | drafts_arted, drafts_story, heroes3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 253 |
| `heroes3_4` | drafts_arted, drafts_story, heroes3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 209 |
| `heroes3_5` | drafts_arted, drafts_story, heroes3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 304 |
| `heroes3_6_v3` | drafts_story, heroes3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 405 |
| `heroes3_7_v4` | drafts_story, heroes3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 328 |
| `heroes3_8_thief` | drafts_arted, drafts_story, heroes3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 368 |
| `heroes3_8_v3_alt3` | drafts_story, heroes3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 381 |
| `heroes3_8_v4_alt` | drafts_arted, drafts_story, heroes3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 336 |
| `heroes3_druid_a` | drafts_story, heroes3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 326 |
| `heroes3_druid_b_v2` | drafts_story, heroes3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 231 |
| `high_endpoint_v2` | sky_promesst_misc | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 209 |
| `high_horse` | drafts_arted, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 323 |
| `high_shelf_v2` | drafts_arted, drafts_good_looking, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 229 |
| `highway` | drafts_arted, drafts_story, mirrors_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 162 |
| `holes` | drafts_arted, heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 246 |
| `hot_swap` | drafts_arted, heroes_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 241 |
| `hover_corner_3` | drafts_arted, underworld_skipping_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 197 |
| `hover_corner_4` | drafts_arted, underworld_skipping_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 164 |
| `how_to_train_your_dragon` | drafts_arted, underworld_heroes_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 190 |
| `hustle_v2` | beams_and_stones, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 159 |
| `hyper_jump` | drafts_arted, drafts_good_looking, underworld_heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 226 |
| `hyper_jump_2c` | drafts_arted, underworld_heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 326 |
| `i_beam_v2` | drafts_arted, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 285 |
| `ice_climbers` | drafts_arted, underworld_heroes_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 227 |
| `immobilize` | beams_and_basic_heroes, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 285 |
| `implausible_bridge` | drafts_arted, vertical_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 198 |
| `implausible_bridge_2` | drafts_arted, vertical_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 270 |
| `in_a_flash_alt` | drafts_arted, lily_rotation | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 331 |
| `in_a_flash_alt_back` | drafts_arted, lily_rotation | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 334 |
| `in_the_way_alt_3` | drafts_arted, drafts_story, mirrors_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 252 |
| `indirect_skip` | drafts_arted, drafts_story, heroes_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 188 |
| `indirect_skip_2` | drafts_arted, drafts_story, heroes_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 203 |
| `indirect_skip_3` | drafts_arted, heroes_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 237 |
| `infinite_crystal_hack_v5` | drafts_arted, mirrors_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 253 |
| `infinite_looping_skipper0_alt` | lily_highway_mirrors_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 253 |
| `infinite_looping_skipper_alt` | lily_highway_mirrors_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 236 |
| `infinite_looping_skipper_far` | lily_highway_mirrors_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 201 |
| `infinite_looping_skipper_mirrored_ikaruga_alt` | lily_highway_mirrors_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 230 |
| `ingame_glyphs` | — | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 9 |
| `ingame_particles` | — | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 144 |
| `into_the_water_3` | double_beam_falling, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 238 |
| `intro` | drafts_arted, drafts_story, intro | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 1534 |
| `invisible_hand` | beams_and_basic_heroes, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 250 |
| `iodine_clock_v2` | drafts_arted, heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 241 |
| `island_friends` | drafts_arted, drafts_story, heroes_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 216 |
| `island_hopping` | drafts_arted, heroes_and_water | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 260 |
| `its_a_tall_order` | drafts_arted, sky_promesst_misc | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 275 |
| `jenga_assorted` | drafts_arted, underworld_heroes_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 205 |
| `jenga_dispenser` | drafts_arted, intro_hard_puzzles | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 219 |
| `jenga_easier` | drafts_arted, drafts_good_looking, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 186 |
| `jenga_shortstack_v2` | drafts_arted, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 157 |
| `juggalos` | drafts_arted, underworld_skipping_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 222 |
| `juggle` | drafts_arted, vertical_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 318 |
| `jump_the_fence_v2` | beams_and_basic_heroes, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 218 |
| `jump_to_pillar_v3` | drafts_arted, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 267 |
| `kick` | underworld_skipping_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 281 |
| `killer_wizard` | drafts_arted, heroes_and_water | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 229 |
| `landmines_v3` | drafts_arted, vertical_endpoint | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 272 |
| `laser_pointer` | endgame2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 212 |
| `laser_stop_surprise` | double_beam_falling, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 186 |
| `launch_and_collect` | drafts_arted, mirrorable_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 312 |
| `layered_alt` | lily_highway_mirrors_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 280 |
| `lazy_susan_v2` | drafts_arted, orange_beam_highway_mirrors_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 364 |
| `learn_to_catch_v2` | drafts_arted, drafts_story, mirrors_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 228 |
| `learning_double` | beams_and_basic_heroes, drafts_arted, drafts_story | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 252 |
| `lemonade` | drafts_arted, underworld_heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 389 |
| `lemonade_tng_stages_towers_no_float` | drafts_arted, underworld_heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 289 |
| `lily_falls_intro_v2` | drafts_arted, skipping_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 242 |
| `lily_pull` | drafts_arted, skipping_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 166 |
| `lily_pull_intro` | drafts_arted, drafts_good_looking, skipping_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 171 |
| `lily_switch_p` | drafts_arted, flat_things | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 294 |
| `lily_two_cyan` | underworld_skipping_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 241 |
| `lily_wearing_intro` | design_illustrations | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 90 |
| `lilyruga_simpler` | drafts_arted, mirrorable_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 235 |
| `limited_offsets` | drafts_arted, underworld_heroes_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 217 |
| `limited_offsets_surprise_v2` | drafts_arted, underworld_heroes_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 277 |
| `little_faith_alt` | drafts_arted, heroes_and_water | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 193 |
| `loading_docks_v2` | drafts_arted, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 227 |
| `lock_picky` | beams_and_basic_heroes, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 167 |
| `long_platform_v2` | drafts_arted, drafts_story, mirrors_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 342 |
| `magic_rover` | beams_and_mirrors, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 173 |
| `magic_shield` | beams_and_basic_heroes, drafts_arted, drafts_story | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 306 |
| `magic_square` | beams_and_basic_heroes, drafts_arted, drafts_story | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 268 |
| `magic_tower` | drafts_arted, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 240 |
| `magicians_assistant_v2` | drafts_arted, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 181 |
| `magnitudes_v3` | drafts_arted, drafts_story, orange_beam_highway_mirrors_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 682 |
| `make_a_right` | drafts_arted, mirrors_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 260 |
| `make_a_right_simpler` | drafts_arted, mirrors_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 202 |
| `make_it_happen_v6` | drafts_arted, mirrorable_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 338 |
| `make_oneway` | endgame3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 268 |
| `make_shoreline` | drafts_arted, endgame3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 209 |
| `make_sokoban` | endgame3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 382 |
| `make_thief_goblin_maze_v2` | endgame3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 315 |
| `many_falls` | drafts_arted, drafts_good_looking, skipping_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 271 |
| `matching_purple` | beams_and_basic_heroes, drafts_arted, drafts_story | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 261 |
| `mega_clone_v2` | drafts_arted, underworld_mirrors_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 229 |
| `mega_merge_v5` | drafts_arted, underworld_mirrors_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 190 |
| `menu_combo_heroes_light_a` | — | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 162 |
| `menu_combo_heroes_mirrors_a` | — | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 199 |
| `menu_combo_heroes_stones_a` | — | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 81 |
| `menu_combo_heroes_water_a` | — | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 170 |
| `menu_combo_mirrors_stones_a` | — | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 136 |
| `menu_combo_prom_skip_a` | — | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 147 |
| `menu_combo_reflected_beams_a` | — | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 186 |
| `menu_demo_startup` | — | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 94 |
| `menu_heroes_a` | — | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 312 |
| `menu_intro_a` | — | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 59 |
| `menu_mirror_isles_a` | — | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 83 |
| `menu_promesst_a` | — | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 244 |
| `menu_skipping_a` | — | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 84 |
| `menu_skipping_b` | — | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 303 |
| `menu_sky_double_a` | — | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 131 |
| `menu_sky_goblin_a` | — | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 109 |
| `menu_sky_heroes_a` | — | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 176 |
| `menu_sky_mirror_a` | — | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 63 |
| `menu_sky_prommest_a` | — | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 138 |
| `menu_sky_skipping_a` | — | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 117 |
| `menu_under_beam_computation_a` | — | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 127 |
| `menu_under_crossroads_a` | — | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 53 |
| `menu_under_endless_skipping_a` | — | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 258 |
| `menu_under_endpoint_falling_a` | — | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 175 |
| `menu_under_gems_obstacles_a` | — | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 150 |
| `menu_under_lily_beam_a` | — | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 160 |
| `menu_under_mirror_obstacle_a` | — | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 160 |
| `menu_under_mirror_stone_reversion_a` | — | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 180 |
| `menu_under_mirrors_artifacts_a` | — | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 129 |
| `menu_under_mirrors_rivers_a` | — | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 286 |
| `menu_under_monsters_through_a` | — | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 128 |
| `menu_under_skipping_misc_beams_a` | — | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 106 |
| `menu_under_tricky_mirrors_a` | — | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 143 |
| `meta_orange_purple` | beams_and_mirrors, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 209 |
| `meta_orange_purple_2` | beams_and_mirrors, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 210 |
| `metamirror_block_v2` | drafts_arted, drafts_story, metamirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 153 |
| `metamirror_c_alt` | drafts_arted, drafts_story, metamirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 140 |
| `metamirror_different_dir_2_alt` | drafts_arted, drafts_story, metamirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 144 |
| `metamirror_different_dir_3_alt` | drafts_arted, drafts_story, metamirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 189 |
| `metamirror_different_dir_alt` | drafts_arted, drafts_story, metamirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 150 |
| `metamirror_same_dir_2_alt_2` | drafts_arted, drafts_story, metamirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 142 |
| `metamirror_same_dir_3_alt_2` | drafts_arted, drafts_story, metamirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 115 |
| `metamirror_same_dir_5_alt` | drafts_arted, drafts_story, metamirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 150 |
| `metamirror_same_dir_v2` | drafts_arted, drafts_good_looking, drafts_story, metamirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 138 |
| `middle_smash` | beaming_objects, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 338 |
| `mini_green_maze` | beams_and_basic_heroes, drafts_arted, drafts_story | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 248 |
| `mirror_1` | drafts_arted, drafts_story, mirror | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 156 |
| `mirror_10_alt2` | drafts_arted, mirror | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 125 |
| `mirror_10_b_v2` | drafts_arted, mirror | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 151 |
| `mirror_10_d` | drafts_arted, mirror | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 128 |
| `mirror_11` | drafts_arted, drafts_story, mirror | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 151 |
| `mirror_12` | drafts_arted, drafts_story, mirror | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 136 |
| `mirror_13` | drafts_arted, drafts_story, mirror | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 153 |
| `mirror_14` | drafts_arted, drafts_story, mirror | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 137 |
| `mirror_15` | drafts_arted, drafts_story, mirror | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 166 |
| `mirror_17` | drafts_arted, drafts_story, mirror | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 146 |
| `mirror_18` | drafts_arted, drafts_story, mirror | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 116 |
| `mirror_180` | lily_highway_mirrors_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 286 |
| `mirror_19` | drafts_arted, drafts_story, mirror | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 144 |
| `mirror_2` | drafts_arted, drafts_story, mirror | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 143 |
| `mirror_20` | drafts_arted, drafts_story, mirror | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 137 |
| `mirror_21` | drafts_arted, drafts_story, mirror | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 150 |
| `mirror_22_v2` | drafts_arted, drafts_story, mirror | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 148 |
| `mirror_3` | drafts_arted, drafts_story, mirror | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 179 |
| `mirror_4` | drafts_arted, drafts_story, mirror | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 170 |
| `mirror_5` | drafts_arted, drafts_story, mirror | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 152 |
| `mirror_6_alt` | drafts_arted, drafts_story, mirror | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 173 |
| `mirror_7` | drafts_arted, drafts_story, mirror | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 152 |
| `mirror_8_v5` | drafts_arted, drafts_story, mirror | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 158 |
| `mirror_carry_duo` | mirrors_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 296 |
| `mirror_clocks` | drafts_arted, heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 228 |
| `mirror_crystal_rover` | drafts_arted, underworld_heroes_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 133 |
| `mirror_dweller` | drafts_arted, heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 254 |
| `mirror_factory_v2` | drafts_arted, drafts_story, mirror | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 127 |
| `mirror_flip_donut` | drafts_arted, lily_rotation | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 293 |
| `mirror_hallway_v2` | drafts_arted, heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 188 |
| `mirror_motion` | drafts_arted, mirrors_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 166 |
| `mirror_non_turner_v3` | beams_and_mirrors, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 186 |
| `mirror_pals` | drafts_arted, drafts_story, mirror | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 143 |
| `mirror_prelude_v2_fix` | endgame2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 138 |
| `mirror_promesst` | beams_and_mirrors, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 306 |
| `mirror_rover_orange_2` | beams_and_mirrors, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 202 |
| `mirror_sink` | drafts_arted, drafts_story, mirror | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 133 |
| `mirror_stone_intro` | drafts_arted, drafts_story, mirrorable_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 159 |
| `mirror_the_unmirrorable_mirror` | drafts_arted, drafts_good_looking, underworld_heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 222 |
| `mirror_u` | drafts_arted, lily_rotation | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 368 |
| `missile_command` | advanced_bard_and_water, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 314 |
| `mission_impossible` | drafts_arted, drafts_good_looking, vertical_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 263 |
| `mobile_cover_2` | drafts_arted, underworld_skipping_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 239 |
| `monkey_in_the_midpoint` | promesst3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 226 |
| `monster_drop` | double_beam_falling, drafts_arted, drafts_story | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 202 |
| `monster_gate_in_water` | heroes_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 229 |
| `monster_mover` | drafts_arted, drafts_good_looking, heroes_and_water | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 259 |
| `monster_promesst_v3` | drafts_arted, monsters_and_beams | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 152 |
| `monster_spawn` | spawners | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 288 |
| `monster_stack` | drafts_arted, drafts_good_looking, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 200 |
| `mosh_pit_small` | drafts_arted, drafts_story, heroes2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 198 |
| `mountain_music` | drafts_arted, drafts_good_looking, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 260 |
| `movable_button` | drafts_arted, flat_things | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 242 |
| `movable_buttons` | drafts_arted, flat_things | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 318 |
| `moving_a_mirror` | drafts_arted, heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 232 |
| `moving_bridge` | drafts_arted, mirrors_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 249 |
| `moving_three_mirrors` | drafts_arted, heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 195 |
| `moving_through_mirrors_v3` | drafts_arted, underworld_heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 387 |
| `multipurpose` | drafts_arted, mirrorable_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 283 |
| `multipush_for_me2` | drafts_arted, sideways_gates | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 263 |
| `mundane_mirror` | drafts_arted, mirror | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 115 |
| `musical_staircase_v2` | drafts_arted, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 158 |
| `my_first_stack` | drafts_arted, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 241 |
| `narrow_passage` | beams_and_stones, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 199 |
| `negative_space` | drafts_arted, gems | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 242 |
| `new_cleric_fly` | drafts_arted, drafts_good_looking, heroes_and_water | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 243 |
| `new_new_new_slam` | drafts_arted, drafts_story, mirrorable_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 185 |
| `new_way_mirror_later` | drafts_arted, drafts_story, vertical_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 257 |
| `no_charm` | drafts_arted, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 191 |
| `no_murder_weapon_0` | drafts_arted, drafts_good_looking, monsters_and_beams | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 222 |
| `no_murder_weapon_wizard` | drafts_arted, monsters_and_beams | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 209 |
| `nowhere_to_smash_combo` | underworld_mirrors_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 312 |
| `numberlink_alt` | drafts_arted, drafts_good_looking, gems | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 302 |
| `ocean_blue` | beams_and_stones, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 138 |
| `omnimirror_v2` | drafts_arted, mirrors_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 285 |
| `on_command` | drafts_arted, heroes_and_water | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 265 |
| `on_the_rocks` | drafts_arted, skipping_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 351 |
| `one_bird_two_stones` | drafts_arted, drafts_story, heroes_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 200 |
| `one_fire_v2` | drafts_arted, drafts_story, heroes2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 240 |
| `one_floor_down_v2` | drafts_arted, vertical_reflection | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 278 |
| `one_of_each` | drafts_arted, heroes_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 189 |
| `one_vs_three` | drafts_arted, heroes_and_water | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 254 |
| `oneway_beam` | beams_and_basic_heroes, drafts_arted, drafts_good_looking | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 238 |
| `oneway_dragon_toast` | drafts_arted, heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 301 |
| `open_monster` | drafts_arted, drafts_good_looking, monsters_and_beams | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 215 |
| `orange_beam_deal` | beams_and_basic_heroes, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 186 |
| `orange_clm_s` | beams_and_mirrors, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 245 |
| `orange_cross` | double_beam_falling_dropdown, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 145 |
| `orange_doubleback` | beams_and_mirrors, drafts_arted, drafts_good_looking | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 208 |
| `orange_doubledoubleback` | beams_and_mirrors, drafts_arted, drafts_good_looking | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 211 |
| `orange_floaty_reflect_v3` | beams_and_mirrors, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 247 |
| `orange_gem_instant` | drafts_arted, gems | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 200 |
| `orange_mirror_walk_button` | drafts_arted, orange_beam_highway_stones_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 218 |
| `orange_predicament` | beams_and_mirrors, drafts_arted, drafts_good_looking | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 144 |
| `orange_skip_place_v3` | beams_and_stones, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 172 |
| `orange_snake` | double_beam_falling, drafts_arted, drafts_good_looking | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 214 |
| `orange_water_button_vdouble_v2` | drafts_arted, orange_beam_highway_stones_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 212 |
| `orange_water_button_vfour_alter` | drafts_arted, orange_beam_highway_stones_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 207 |
| `orange_water_button_vslow` | orange_beam_highway_stones_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 203 |
| `orange_wizard_intro` | beams_and_basic_heroes, drafts_arted, drafts_story | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 302 |
| `ortho` | lily_highway_stones_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 264 |
| `ortho2` | drafts_arted, lily_highway_stones_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 172 |
| `ortho3` | lily_highway_stones_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 223 |
| `out_of_range_v4` | drafts_arted, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 281 |
| `overworld` | overworld | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 3890 |
| `overwrite` | drafts_arted, vertical_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 255 |
| `pachinko` | drafts_arted, vertical_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 243 |
| `pachinko_rescue_w` | drafts_arted, drafts_good_looking, vertical_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 276 |
| `partial_pull` | drafts_arted, heroes_and_water | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 255 |
| `pass_through_v2_same_z` | drafts_arted, drafts_good_looking, goblin_rotation | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 207 |
| `pat_on_the_back_v2` | underworld_heroes_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 166 |
| `peak_toggle` | endgame2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 279 |
| `perch_3_rovers` | drafts_arted, underworld_heroes_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 144 |
| `personal_assistant_v3` | drafts_arted, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 203 |
| `pigeonhole_squished` | drafts_arted, drafts_good_looking, underworld_heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 277 |
| `pillars` | drafts_arted, mirrors_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 242 |
| `pink_platforms` | drafts_arted, vertical_reflection | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 171 |
| `place_lily_pushstyle_v6` | endgame2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 284 |
| `place_promesst_rooms` | endgame2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 276 |
| `place_slot_4x4_pushstyle` | endgame2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 283 |
| `place_to_stand` | drafts_arted, drafts_story, mirrors_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 159 |
| `plus_signs_v3` | beams_and_basic_heroes, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 191 |
| `pole_vault` | advanced_bard_and_water, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 338 |
| `pool_pal_v2` | drafts_arted, drafts_good_looking, skipping_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 259 |
| `portable_stairs` | drafts_arted, vertical_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 309 |
| `prelude_priest_water_goblins_only` | endgame2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 331 |
| `priest_3d_goblin_pass` | drafts_arted, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 140 |
| `priest_3d_intro_dragon_v4` | drafts_arted, drafts_good_looking, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 236 |
| `priest_bottom_v2` | drafts_arted, drafts_good_looking, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 319 |
| `priest_button_3d_revised` | drafts_arted, drafts_good_looking, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 199 |
| `priest_descent_simpler` | drafts_arted, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 145 |
| `priest_traverse_e_fence` | drafts_arted, drafts_good_looking, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 266 |
| `priest_two_warriors_v3` | drafts_arted, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 227 |
| `priest_warrior_descent` | drafts_arted, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 288 |
| `priest_water_back_goblin` | drafts_arted, skipping_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 257 |
| `priest_water_back_place_v3` | drafts_arted, skipping_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 228 |
| `prisoners_dilemma_alt` | drafts_arted, heroes_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 239 |
| `promesst1_streamlined` | drafts_arted, drafts_story, promesst1_and_2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 444 |
| `promesst2.5_deeper` | drafts_arted, promesst3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 306 |
| `promesst2_streamlined` | drafts_arted, promesst1_and_2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 345 |
| `promesst3_streamlined` | promesst3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 301 |
| `promesst_prelude_pushstyle` | endgame2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 301 |
| `protrusions` | beams_and_mirrors, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 180 |
| `pugo` | clones, drafts_arted, drafts_good_looking | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 194 |
| `pull_it_v4` | drafts_arted, drafts_story, heroes_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 192 |
| `pull_line` | clones, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 197 |
| `pull_skip_twins_v3` | drafts_arted, heroes_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 297 |
| `pull_teamwork_alt` | drafts_arted, drafts_story, heroes_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 223 |
| `pull_together` | beams_and_basic_heroes, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 221 |
| `pulling_near_orange_v2` | beams_and_basic_heroes, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 257 |
| `pulling_pedestals` | drafts_arted, drafts_good_looking, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 248 |
| `purple_beam_intro_v2_alt` | beams_and_stones, drafts_arted, drafts_story | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 205 |
| `purple_clm_v4` | beams_and_mirrors, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 248 |
| `purple_corner_gem` | beams_and_mirrors, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 302 |
| `purple_haze` | beams_and_basic_heroes, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 211 |
| `purple_heart` | drafts_arted, drafts_good_looking, underworld_mirrors_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 269 |
| `purple_perpendicular` | beams_and_basic_heroes, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 247 |
| `purple_push_pal` | beams_and_basic_heroes, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 206 |
| `purple_wall_around_easier_vp` | beams_and_mirrors, drafts_arted, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 221 |
| `purple_wizard_maze` | beams_and_basic_heroes, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 372 |
| `push_against` | drafts_arted, heroes_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 204 |
| `push_and_pull_zach` | drafts_arted, drafts_story, heroes_and_water | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 238 |
| `push_down_a_lot` | design_illustrations | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 55 |
| `push_down_a_lot_small` | design_illustrations, drafts_arted, drafts_arted, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 188 |
| `push_down_chain` | underworld_crossroads | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 185 |
| `push_down_v2` | drafts_arted, drafts_good_looking, drafts_story, intro_to_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 183 |
| `pushback` | beams_and_basic_heroes, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 254 |
| `pushing_crystal_near_orange_v2` | beaming_objects, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 287 |
| `pushing_near_orange` | beams_and_basic_heroes, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 180 |
| `pushing_orange` | beams_and_basic_heroes, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 209 |
| `pushy` | drafts_arted, promesst1_and_2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 381 |
| `put_down_roots_v3` | drafts_arted, heroes_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 278 |
| `quad_torch` | design_illustrations, drafts_arted, drafts_trailer, heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 342 |
| `quad_torch_v1` | design_illustrations | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 88 |
| `quadrants` | drafts_arted, heroes_and_water | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 339 |
| `quadrants_follow_up` | drafts_arted, drafts_story, heroes_and_water | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 355 |
| `quadruple_skip` | drafts_arted, underworld_heroes_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 102 |
| `quick_redirect_v5` | drafts_arted, drafts_story, vertical_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 163 |
| `raft_corners_2_small` | drafts_arted, underworld_lilies | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 190 |
| `raft_corners_4x4` | drafts_arted, underworld_lilies | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 174 |
| `raft_corners_alt_3` | drafts_arted, underworld_lilies | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 143 |
| `reattachment` | drafts_arted, heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 247 |
| `recycling` | spawners | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 295 |
| `red_cross` | drafts_arted, heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 308 |
| `red_handed` | beams_and_basic_heroes, drafts_arted, drafts_story | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 206 |
| `red_rooms_v5` | beams_and_mirrors, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 320 |
| `red_yellow_alter_with_intro_v2` | beams_and_mirrors, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 222 |
| `reel_it_in` | drafts_arted, mirrorable_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 183 |
| `reflect_momentum` | drafts_arted, drafts_trailer, mirrorable_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 284 |
| `regular_mirror_v4` | drafts_arted, heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 238 |
| `remote_work` | beams_and_mirrors, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 226 |
| `removal_v2` | drafts_arted, drafts_good_looking, skipping_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 171 |
| `repel` | drafts_arted, vertical_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 138 |
| `reroute_3` | lily_highway_mirrors_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 241 |
| `reset_mirror` | spawners | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 287 |
| `reset_trio` | spawners | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 141 |
| `retro` | drafts_arted, skipping_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 252 |
| `retro_hooks` | drafts_arted, skipping_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 179 |
| `retvrn0` | drafts_arted, drafts_arted, underworld_skipping_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 254 |
| `ricochet_v2` | drafts_arted, mirrorable_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 429 |
| `ride_together` | drafts_arted, mirrors_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 166 |
| `right_hand_man` | drafts_arted, promesst1_and_2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 298 |
| `river_dictionary_alt_up` | drafts_arted, drafts_story, mirrors_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 356 |
| `river_exploit_v2` | endgame3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 238 |
| `river_maze_clear_tenacious_race_v2` | drafts_arted, lily_rotation | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 340 |
| `river_plinko_v2_actual` | drafts_arted, mirrors_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 383 |
| `river_push_v4` | drafts_arted, mirrors_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 313 |
| `river_rates_button` | drafts_arted, lily_rotation | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 385 |
| `river_rates_jagged` | drafts_arted, lily_rotation | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 397 |
| `river_rotate_beams_gr` | underworld_skipping_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 246 |
| `rotating_cavalry_spaced` | drafts_arted, monsters_and_beams | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 178 |
| `rotator` | drafts_arted, drafts_story, skipping_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 200 |
| `rover_advance_c_v2` | beams_and_stones, drafts_arted, drafts_story | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 215 |
| `rover_impulse_v2` | beams_and_stones, drafts_arted, drafts_story | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 221 |
| `rover_shift_p` | beams_and_stones, drafts_arted, drafts_story | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 188 |
| `rover_water_purple_sequel_v3` | beams_and_mirrors, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 249 |
| `rover_water_purple_v9` | beams_and_mirrors, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 187 |
| `rowboat` | advanced_bard_and_water, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 328 |
| `rowboat_wizard_v2` | advanced_bard_and_water, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 320 |
| `rsmash` | beams_and_stones, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 195 |
| `rubble_chain` | underworld_mirrors_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 348 |
| `run_the_clock_alt` | drafts_arted, mirrorable_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 366 |
| `safe_returns` | beams_and_basic_heroes, drafts_arted, drafts_story | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 289 |
| `safety_gloves` | beaming_objects, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 298 |
| `save_for_later` | underworld_mirrors_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 302 |
| `security_checkpoints_v2` | beams_and_stones, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 158 |
| `see_no_evil` | endgame2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 277 |
| `see_through` | beams_and_basic_heroes, drafts_arted, drafts_story | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 320 |
| `seeing_red` | drafts_arted, vertical_reflection | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 284 |
| `self_teleporting` | drafts_arted, underworld_heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 162 |
| `sender` | design_illustrations | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 85 |
| `sender_simplified` | design_illustrations | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 73 |
| `sender_simplified_v2` | design_illustrations, drafts_arted, drafts_arted, vertical_endpoint | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 214 |
| `short_ride_option_b` | drafts_arted, drafts_story, mirrors_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 178 |
| `shower` | drafts_arted, vertical_endpoint | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 164 |
| `shunt2_alt` | beams_and_basic_heroes, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 208 |
| `sick_270_small` | lily_highway_mirrors_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 220 |
| `side_kick` | drafts_arted, sideways_gates | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 273 |
| `side_slide_intro_v2` | drafts_arted, sideways_gates | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 310 |
| `side_sub_back` | double_beam_falling, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 210 |
| `side_sub_v2` | double_beam_falling, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 244 |
| `sidestone_zach_1` | drafts_arted, drafts_story, mirrorable_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 308 |
| `sidestone_zach_2` | drafts_arted, drafts_story, mirrorable_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 239 |
| `sidestone_zach_2_end2` | drafts_arted, endgame2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 284 |
| `sidestone_zach_3` | drafts_arted, drafts_story, mirrorable_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 167 |
| `sidestone_zach_4` | drafts_arted, drafts_story, mirrorable_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 162 |
| `sidetrack` | beams_and_mirrors, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 247 |
| `simple_trap` | beams_and_basic_heroes, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 238 |
| `simplify_skipping` | endgame3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 321 |
| `simplify_wizard` | endgame3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 328 |
| `simultaneous_x` | drafts_arted, orange_beam_highway_mirrors_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 274 |
| `simultaneous_x_surprise` | drafts_arted, orange_beam_highway_mirrors_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 317 |
| `single_out` | drafts_arted, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 131 |
| `sink_together` | drafts_arted, mirrors_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 202 |
| `sister_staircase_harder` | drafts_story, intro_to_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 165 |
| `skip_or_sink_r` | beams_and_stones, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 165 |
| `skip_orange_block_c` | beams_and_stones, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 203 |
| `skip_orange_maze_v3` | beams_and_stones, drafts_arted, drafts_good_looking | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 220 |
| `skip_orange_wall_v3` | beams_and_stones, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 200 |
| `skip_purple_drop_alt` | drafts_arted, underworld_skipping_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 219 |
| `skip_stack_1` | drafts_arted, skipping_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 273 |
| `skip_stack_2` | drafts_arted, skipping_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 291 |
| `skip_stack_3` | drafts_arted, drafts_good_looking, skipping_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 252 |
| `skip_wand_v6` | beams_and_stones, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 238 |
| `skipping_cyan_precise_c_v3` | beams_and_stones, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 236 |
| `skipping_near_beams_v2` | beams_and_stones, drafts_arted, drafts_story | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 404 |
| `skipping_pals` | drafts_arted, skipping_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 531 |
| `skipping_promesst` | beams_and_stones, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 206 |
| `skipping_shores_v3` | drafts_arted, skipping_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 351 |
| `skipping_stones` | drafts_arted, drafts_story, skipping_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 387 |
| `skipping_with_dragon` | drafts_arted, heroes_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 240 |
| `skipping_wrapping_v3` | beams_and_stones, drafts_arted, drafts_story | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 220 |
| `sky_double_intro0` | double_beam_falling, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 178 |
| `sky_double_intro1` | double_beam_falling, drafts_arted, drafts_good_looking | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 183 |
| `sky_druid_kill` | drafts_arted, drafts_good_looking, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 209 |
| `sky_druid_kill_tall_2_goblins` | drafts_arted, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 209 |
| `sky_druid_maze` | drafts_arted, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 203 |
| `sky_druid_one` | drafts_arted, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 210 |
| `sky_druid_tree_ex` | drafts_arted, drafts_good_looking, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 208 |
| `skybridge` | lily_highway_stones_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 175 |
| `slide_rows` | beams_and_basic_heroes, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 255 |
| `slot_machine_v2` | drafts_arted, heroes_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 158 |
| `smartbomb_combo_v3` | underworld_mirrors_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 381 |
| `smash_grid_4` | beams_and_basic_heroes, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 217 |
| `smash_grid_kill` | beams_and_basic_heroes, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 225 |
| `smash_midskip_simpler4` | drafts_arted, underworld_skipping_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 195 |
| `smash_or_dash_vs2` | beams_and_mirrors, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 248 |
| `snipperclips_0_square` | beams_and_basic_heroes, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 237 |
| `snipperclips_diagonal` | beams_and_basic_heroes, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 240 |
| `snipperclips_square` | beams_and_basic_heroes, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 240 |
| `sokobridge_v4` | drafts_arted, elevators | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 172 |
| `sombreros` | drafts_arted, flat_things | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 355 |
| `sp_crystal_tuto` | beams_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 225 |
| `special_move` | drafts_arted, underworld_heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 192 |
| `spin_doctors_v3` | drafts_arted, drafts_story, skipping_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 243 |
| `spin_heroes` | drafts_arted, drafts_good_looking, drafts_story, skipping_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 253 |
| `spray_and_pray` | drafts_arted, drafts_story, skipping_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 202 |
| `sprint_skip0` | drafts_arted, drafts_story, heroes_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 222 |
| `square_dance` | drafts_arted, mirrors_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 214 |
| `stack_prelude_pushstyle` | endgame2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 213 |
| `stasis_v2` | drafts_arted, underworld_heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 234 |
| `stay_lit` | drafts_arted, strength | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 180 |
| `sticky` | drafts_arted, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 291 |
| `stone_economy` | endgame2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 248 |
| `stone_rescue_v3` | lily_highway_heroes_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 145 |
| `stone_stopper3_v2` | drafts_arted, heroes_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 273 |
| `stone_stopper5` | drafts_arted, heroes_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 232 |
| `stone_stopper_intro` | drafts_arted, heroes_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 222 |
| `stones_below_v3` | drafts_arted, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 199 |
| `stones_not_crystals` | drafts_arted, drafts_story, heroes_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 227 |
| `stones_prelude` | endgame2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 223 |
| `stonewalled` | beams_and_stones, drafts_arted, drafts_story | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 165 |
| `stopper_topper_v2` | drafts_arted, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 154 |
| `strategic_stack` | design_illustrations | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 62 |
| `strong_monsters_v2` | drafts_arted, strength | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 233 |
| `stuck_up_v2` | drafts_arted, drafts_good_looking, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 217 |
| `submarine` | beams_and_stones, drafts_arted, drafts_story | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 193 |
| `submarine_far_away` | beams_and_stones, drafts_arted, drafts_story | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 219 |
| `sunk_cost_2_v3` | drafts_arted, skipping_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 238 |
| `surfing_lesson_alt` | drafts_arted, drafts_good_looking, heroes_and_water | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 247 |
| `surrounded` | drafts_arted, drafts_story, heroes_and_water | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 378 |
| `suspend_block_v2` | drafts_arted, vertical_reflection | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 303 |
| `suspend_directions_v2` | drafts_arted, vertical_reflection | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 237 |
| `suspend_heterogeneous` | drafts_arted, vertical_reflection | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 301 |
| `suspend_intro` | drafts_arted, vertical_reflection | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 272 |
| `suspend_swapper_hard` | drafts_arted, vertical_reflection | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 224 |
| `swap_and_spin` | drafts_arted, heroes_and_artifacts | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 215 |
| `swap_seats` | beams_and_stones, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 202 |
| `swapwiz_harder` | drafts_arted, lily_highway_heroes_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 319 |
| `synchronized_swimmers` | drafts_arted, drafts_good_looking, heroes_and_water | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 285 |
| `taking_the_lift` | drafts_arted, elevators | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 174 |
| `tall_stack` | drafts_arted, drafts_good_looking, vertical_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 214 |
| `tandem` | drafts_arted, drafts_story, vertical_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 204 |
| `target_practice_gem` | drafts_arted, promesst1_and_2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 222 |
| `team_building_exercise` | drafts_arted, drafts_good_looking, heroes_and_water | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 228 |
| `tempered_glass_red` | beams_and_mirrors, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 265 |
| `thats_my_ride` | drafts_arted, drafts_story, mirrors_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 167 |
| `the_line_must_be_drawn_HERE` | drafts_arted, underworld_heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 117 |
| `the_long_way` | drafts_arted, mirrors_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 220 |
| `the_sky_is_falling_v2` | double_beam_falling, drafts_arted, drafts_story | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 193 |
| `the_spiral` | beams_and_mirrors, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 258 |
| `the_swappers` | drafts_arted, heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 222 |
| `the_waterfall_v4` | drafts_arted, skipping_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 274 |
| `there_and_back` | drafts_arted, mirrors_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 209 |
| `thief_dragger_v2` | drafts_arted, monsters_and_beams | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 232 |
| `thief_stack` | drafts_arted, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 277 |
| `thief_through` | beams_and_basic_heroes, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 232 |
| `thief_wand` | drafts_arted, drafts_story, heroes_and_artifacts | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 232 |
| `thin_ice_rooms` | double_beam_falling, drafts_arted, drafts_good_looking | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 181 |
| `three_artifacts_v3` | drafts_arted, orange_beam_highway_mirrors_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 427 |
| `three_birds_push` | endgame2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 342 |
| `through_intro` | beams_and_basic_heroes, drafts_arted, drafts_story | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 254 |
| `through_maze_v2` | beaming_objects, drafts_arted, drafts_good_looking | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 333 |
| `through_push` | beams_and_basic_heroes, drafts_arted, drafts_story | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 235 |
| `through_sokoban` | beams_and_basic_heroes, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 255 |
| `through_the_table_e` | double_beam_falling, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 186 |
| `through_the_table_f` | double_beam_falling, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 199 |
| `through_way` | beams_and_stones, drafts_arted, drafts_story | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 196 |
| `tiger_lily_v2` | design_illustrations, drafts_arted, drafts_arted, skipping_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 238 |
| `time_tutorial` | drafts_arted, skipping_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 191 |
| `tippy_intro` | drafts_arted, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 382 |
| `tippy_towers_1` | drafts_arted, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 226 |
| `tippy_towers_4` | drafts_arted, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 227 |
| `to_kill_a_goblin` | drafts_arted, drafts_good_looking, drafts_story, vertical_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 389 |
| `toggler00` | drafts_arted, underworld_mirrors_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 225 |
| `top_green_purple_v3` | beams_and_mirrors, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 277 |
| `torc_blocked` | beaming_objects, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 245 |
| `torc_blocked_easier` | beaming_objects, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 328 |
| `torcher` | design_illustrations | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 82 |
| `torcoban_2` | drafts_arted, promesst1_and_2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 264 |
| `torus_bard` | underworld_heroes_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 154 |
| `torus_blocks_alt_v4` | drafts_good_looking, underworld_heroes_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 152 |
| `torus_goblins` | underworld_heroes_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 132 |
| `torus_mirrors` | drafts_arted, underworld_mirrors_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 107 |
| `trader_descend` | drafts_arted, drafts_story, mirrors_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 175 |
| `treadmill` | spawners | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 175 |
| `trick_kills` | drafts_arted, heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 425 |
| `trick_landing` | drafts_arted, elevators | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 217 |
| `trick_shot` | drafts_arted, heroes_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 223 |
| `tricky_endpoint` | drafts_arted, underworld_skipping_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 216 |
| `tricky_swappers_v3` | drafts_arted, heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 257 |
| `triple_gate` | design_illustrations, drafts_arted, drafts_arted, drafts_story, drafts_story, mirrors_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 299 |
| `triple_skip` | drafts_arted, underworld_heroes_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 183 |
| `trust_falls` | drafts_arted, drafts_story, mirrors_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 221 |
| `tug_boat` | drafts_arted, heroes_and_water | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 261 |
| `turn_control_v2` | drafts_arted, drafts_story, skipping_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 214 |
| `two_bounce_v2` | drafts_arted, mirrors_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 221 |
| `two_dragon_rooms` | drafts_arted, heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 369 |
| `two_for_one` | drafts_arted, heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 182 |
| `two_half_togglers` | drafts_arted, underworld_mirrors_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 234 |
| `two_metamirrors` | drafts_arted, drafts_story, metamirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 107 |
| `two_step` | drafts_arted, mirrors_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 218 |
| `two_through_alt_2` | beams_and_basic_heroes, drafts_arted, drafts_story | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 294 |
| `unblock_block_alt` | drafts_arted, mirrors_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 271 |
| `under_pressure` | drafts_arted, drafts_good_looking, strength | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 209 |
| `untrap` | beams_and_basic_heroes, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 250 |
| `use_and_remove` | drafts_arted, mirrors_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 250 |
| `useful_stone` | drafts_arted, heroes_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 207 |
| `vacuum` | drafts_arted, drafts_good_looking, vertical_reflection | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 276 |
| `vert_mirror_intro` | drafts_arted, vertical_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 264 |
| `vertical_promesst_v2` | drafts_arted, vertical_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 240 |
| `vertical_unclone_3` | drafts_arted, vertical_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 282 |
| `victory_lap` | drafts_arted, drafts_story, heroes3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 475 |
| `volcano_v3` | drafts_arted, vertical_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 255 |
| `walk_into_fire` | drafts_arted, heroes_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 245 |
| `walk_it_over` | drafts_arted, drafts_story, mirror | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 163 |
| `walk_the_plank` | drafts_arted, heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 286 |
| `wall_sneak` | beams_and_basic_heroes, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 285 |
| `wand_reintro` | drafts_arted, underworld_heroes_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 318 |
| `wasteland` | underworld_heroes_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 127 |
| `water_bender_v3` | drafts_arted, underworld_mirrors_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 218 |
| `watergate` | drafts_arted, drafts_story, heroes_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 218 |
| `weaklings_bard_v2` | drafts_arted, drafts_good_looking, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 184 |
| `who_you_gonna_call` | endgame2 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 256 |
| `wide_ocean` | drafts_arted, mirrorable_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 230 |
| `wider_ocean` | drafts_arted, mirrorable_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 382 |
| `wizard_and_druid_alt` | drafts_story, heroes3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 302 |
| `wizard_and_druid_alt_5` | heroes3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 233 |
| `wizard_finesse_1` | beams_and_basic_heroes, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 273 |
| `wizard_finesse_2` | beams_and_basic_heroes, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 270 |
| `wizard_finesse_3` | beams_and_basic_heroes, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 282 |
| `wizard_finesse_4` | beams_and_basic_heroes, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 289 |
| `wizard_jailbreak_v2` | endgame3 | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 335 |
| `wizard_mirror_intro` | drafts_arted, heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 223 |
| `wizard_with_a_capital_w` | drafts_arted, drafts_story, heroes_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 190 |
| `wizard_with_a_capital_w_2_v2` | drafts_arted, drafts_story, heroes_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 229 |
| `wizard_with_a_gun` | drafts_arted, heroes_and_artifacts | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 245 |
| `wizards_true_nature` | drafts_arted, drafts_arted, intro_hard_puzzles | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 233 |
| `wolf_boat_carry` | drafts_arted, vertical_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 257 |
| `worlds_collide_alt` | drafts_arted, drafts_story, worlds_collide | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 277 |
| `worlds_collide_heroes_and_mirrors_v3` | drafts_arted, worlds_collide | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 414 |
| `worlds_collide_heroes_and_promesst` | design_illustrations | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 96 |
| `worlds_collide_heroes_and_promesst_v2` | design_illustrations | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 96 |
| `worlds_collide_heroes_and_promesst_v3` | design_illustrations, drafts_story, drafts_story | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 81 |
| `worlds_collide_heroes_and_promesst_v4` | design_illustrations, drafts_arted, drafts_arted, worlds_collide | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 457 |
| `worlds_collide_heroes_and_stones` | drafts_arted, drafts_story, worlds_collide | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 476 |
| `worlds_collide_mirrors_and_stones_v2` | drafts_arted, drafts_story, worlds_collide | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 228 |
| `worlds_collide_ps` | drafts_arted, drafts_story, worlds_collide | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 364 |
| `wrap_music` | lily_highway_heroes_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 198 |
| `wrap_music_2` | lily_highway_heroes_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 137 |
| `wrapping_magic_mirror_2` | drafts_arted, underworld_mirrors_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 185 |
| `wrapping_mirror0` | drafts_arted, underworld_heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 160 |
| `wrapping_mirror0_relatively_prime` | drafts_arted, underworld_heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 151 |
| `wrapping_mirror_alt` | drafts_arted, underworld_heroes_and_mirrors | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 155 |
| `wrapping_mirror_red_v4` | beams_and_mirrors, drafts_arted | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 307 |
| `wrong_reset` | spawners | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 288 |
| `yars_revenge_setup_v3` | lily_highway_mirrors_and_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 243 |
| `zach_lilies_v3` | drafts_arted, underworld_lilies | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 318 |
| `zachtronics` | drafts_arted, drafts_good_looking, zachtronics | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 327 |
| `zachtronics_identity` | drafts_arted, zachtronics | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 315 |
| `zachtronics_or` | drafts_arted, zachtronics | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 331 |
| `zachtronics_xor` | drafts_arted, zachtronics | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 328 |
| `zap_bridge` | lily_highway_stones_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 143 |
| `zap_bridge_perp` | lily_highway_stones_and_promesst | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 92 |
| `zig_zag` | drafts_arted, mirrorable_stones | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 232 |
| `zombie_graves_v3` | drafts_arted, heroes_in_3d | 845 | Guy×34, Rock×32, Lily×19, Friendly_Dragon×17, Gate×16 | 211 |

## 六、实体类型词汇表（88 种，按全游戏出现次数）

| 类型 | 总数 | 类型 | 总数 |
|---|---|---|---|
| Particle_Source | 83764 | Settings | 54544 |
| Ocean_Map | 51622 | Guy | 33116 |
| Fog_Of_War | 32142 | Rock | 31168 |
| Camera_Control | 25324 | Level_Entry | 24350 |
| Lily | 18506 | View_Giver | 17532 |
| Friendly_Dragon | 16558 | Group | 16558 |
| Gate | 15584 | Point_Light | 15584 |
| Spawner | 15584 | Gem | 14610 |
| Monster | 14610 | Door | 13636 |
| Mirror | 13636 | Sign | 13636 |
| Camera_Marker | 12662 | Tree | 12662 |
| Rover | 11688 | Marker | 10714 |
| Promesst_Light | 10714 | Teleporter | 10714 |
| Fog_Volume | 9740 | Freezer | 9740 |
| Level_State | 9740 | Checkpoint | 8766 |
| Fog | 8766 | Activator | 7792 |
| Flow_Updater | 7792 | Animating | 6818 |
| Fence | 6818 | Gem_Slot | 6818 |
| Judge | 6818 | Audio_Marker | 5844 |
| Fog_Of_War_Clear | 5844 | Global_Effects_Settings | 5844 |
| Tower | 5844 | Artifact | 4870 |
| Inanimate | 4870 | Voice_Log | 4870 |
| Light_Probe | 3896 | Particle_Force | 3896 |
| Sun | 3896 | Turbulence | 3896 |
| Wall_Set | 3896 | Wardrobe | 3896 |
| Wind | 3896 | Annihilator | 2922 |
| Baby_Dragon | 2922 | Boat | 2922 |
| Decal | 2922 | Elevator_Platform | 2922 |
| Entity_Issued_Sound | 2922 | Fog_Of_War_Z | 2922 |
| Level_Connector | 2922 | Note | 2922 |
| Npc | 2922 | Per_Screen_Audio | 2922 |
| Rubble | 2922 | Sky | 2922 |
| Stairs | 2922 | Statue | 2922 |
| Switch | 2922 | Treasure | 2922 |
| Egg | 1948 | Hedron | 1948 |
| Outline_Override | 1948 | Overworld_Unlock | 1948 |
| Procedurally_Animating | 1948 | Ripples | 1948 |
| Translucent_Shadow | 1948 | Treasure_Display | 1948 |
| Area_Pin | 974 | Arrow | 974 |
| Combiner_Display | 974 | Flat_Decoration | 974 |
| Glyph_Radical | 974 | Impeller | 974 |
| Playtest_Note | 974 | Roots | 974 |
| Shadow_Decal | 974 | Temporary_Splash | 974 |
| Wall | 974 | Wrapping_Mask | 974 |

---
*本书由静态逆向自动生成，仅供学习研究；关卡设计版权归 Thekla, inc. 所有。*
