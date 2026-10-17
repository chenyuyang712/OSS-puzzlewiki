# OSS-PuzzleWiki 沉星之序关卡图鉴

对 Steam 游戏《Order of the Sinking Star / 沉星之序》(r66830, 2026-10-08) 的**纯静态逆向研究**成果：
全部 **974 个关卡**的目录、**1,211,383 个实例**的空间布局、机制图谱与难度曲线。

> 声明：数据来自对自有游戏副本安装目录的离线静态分析，不涉及 DRM 规避，非官方资料。
> 游戏 © 其原作者。本仓库仅用于格式研究与攻略查阅。

## 🔭 快速浏览

- **`svg/highlights.html`** ← 用浏览器打开这个：6 张精选关卡的中文注释俯视图
- `svg/index.html` — 全部 974 关俯视图索引
- `book/LEVEL_CATALOG_book.md` — 关卡目录全书（66 组 / 974 关 / 83 区名 / 16 塔）

## 📦 交付物一览

| 文件 | 大小 | 内容 |
|---|---|---|
| `svg/` | 142 MB | 974 张人类可读俯视图（实心形状+标签+图例，可悬停查询） |
| `book/LEVEL_CATALOG_book.md` | 453 KB | 关卡目录全书（中文区名/塔门槛/关卡清单） |
| `book/difficulty_curve.md` | — | 难度曲线与机制图谱（16 机制首现/共现/塔门槛/34 组统计） |
| `book/story_and_themes.md` | — | 主题与剧情解读（游戏文本 × Blow 访谈互证） |
| `book/podcast_solo.md` | — | 播客解读稿（单人独白，九大主题题眼+解说） |
| **`book/plot_reconstruction.md`** | — | **剧情全梳理**（六条故事线/总时间线/结局序列/未解之谜，全带段落出处） |
| **`book/voices/`** | ~650 KB | **全角色文本集**：20 个角色分册 + 合订本（5,727 台词块，中英对照+导演注释，演员表） |
| `data/levels_catalog.json` | 906 KB | 目录结构化数据 |
| `data/mechanic_atlas.json` | — | 机制首现/共现/塔/难度代理 |
| `data/levels_layout.json.gz` | 46 MB | **全实例布局**（解压后 270MB，121 万实例：类型/坐标/旋转/包围盒/UI名/资产名/引用） |

## 🗺 俯视图图例

| 符号 | 含义 |
|---|---|
| 深蓝实心 | 岛面 / 地板 / 贴花 |
| 沙色实心 | 岩石 / 墙体（`*_Rock_*`、`Brick_*`、`ARCH_*`） |
| 金色 ● SUN | 太阳（主线收集物） |
| 紫色 ◆ TOWER | 塔（区域解锁门槛） |
| 青色 ○ | 传送门 Teleporter |
| 白色 ● | Guy / 主角出生点 |

坐标：俯视为世界 x/z 平面（y=高度，鼠标悬停任意形状可见），网格 10 单位。

## 🔬 `.entities` 格式速查（逆向成果）

```
'enty' | u16 ver=7 | u64 25 | u64 88
  → 88 × [u64 len][ascii 类名][u64 attr_count]   # 类注册表(全文件相同=schema)
  → u32 实例数
  → 实例记录流: [fd20 字符串数组(资产名)] [fd 字段...]
字段 = fd | u8 id | u8 kind | payload
  fd21/22/23 = 位置 xyz (f32)   fd06-09 = 旋转四元数
  fd16-18 / fd1a-1c = 包围盒 ext / ctr   fd1f = editorUI 名   fd31 = 资产串
  引用 = 21B [u16 tag][u16 类id][u32 目标idx][6B pad][f32 val]
```
88 类注册表（exe @0x72d038）：Rock=60, Sun=71, Teleporter=73, Tower=75, Wall_Set=84, Guy=34 …

## ⚠️ 已知边界

- 974 关中 **911 关实例计数精确匹配**；63 关含「无 fd20 头的隐藏记录」（少 1-2 个实例，已在 SVG 标题标注 PARTIAL），不影响浏览
- 88 类注册表是 schema 级（不含每实例类别 id），实例分类靠资产名/editorUI 启发式
- 关卡顺序取自 level_set DSL（设计者序列），非强制游玩顺序

## 🛠 复现工具

`tools/`（Python3 无三方依赖）：`enty_parse.py`(格式解析) → `build_catalog.py` → `build_layout.py` → `render_svg2.py` → `build_graph.py`
