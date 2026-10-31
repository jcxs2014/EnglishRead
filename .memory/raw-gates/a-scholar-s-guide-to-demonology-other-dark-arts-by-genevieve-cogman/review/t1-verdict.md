# T1 自检 · a-scholar-s-guide-to-demonology-other-dark-arts-by-genevieve-cogman

**抽样章号（先定后读）：ch01、ch05、ch10、ch14、ch18、ch23、ch27（7 章 = ceil(27/4)，首末必含，其余按 (27-1)/6≈4.33 等距取）**
自检人：写作方本人（同会话）。**未经异会话复核，有效率未校准。** 全书 27 章 332 块。

## 一、机器层（全部 rc=0）
`bash scripts/gate.sh` → **EXIT=0 / 0 条阻断型**；`chapter.sh` 27/27 rc=0；总览三篇 quotes 81/81、full 命中 81 查无 0、labels 52/52 ✅；`check_vocab` 913 行 FAIL 0 / WARN 0；`structure.py keywords` 阻断 0；引语块 332 行前缀完整、编号连续。

## 二、抽样章人判（7 章，先读 text/ 再读 md）
| 章 | 章内查出 | 处置 |
|---|---|---|
| ch01 | **1 阻断**：`ch01 prologue.md:16` 写「校长不写『亲爱的』」，原文 `text/ch01_chap1.txt:13` 是 `Dear Miss Fen,` | 改为「先夸肯用纸笔写信，紧接点出材料有欠缺」 |
| ch05 | **4 阻断**：`:15`/`:22`/`:201` 三处「布伦登的死因」，原文只写 `a sad loss`/`left us without warning`（`text/ch05:61`，且 `text/ch26:4` 她还活着）；`:15` 虚构「拿人体当楼梯扶手装饰」（全库 grep 零命中） | 死因→「突然离开」；装饰→「墙角《屠杀无辜者》复制品」（`text/ch05:91`） |
| ch10 | 0 阻断（2 提示：`前同事`→`前任拉丁文教师`；中文理解删块外句） | 已修 |
| ch14 | 0 阻断（1 提示：`:92`「把校长请来掌权」主语含糊） | 改为「指挥链直接通到王座，不经过政府或首相」 |
| ch18 | 0 阻断（1 提示：六参观地点的「王宫」，原文 `text/ch18:487` Royal Pavilion） | 改「行宫」 |
| ch23 | 0 阻断 | — |
| ch27 | **1 阻断**：`:10`/`:29`/`:33`/`:167` 写「下午四点半」，原文 `text/ch27:13` 是 `quarter to five in the afternoon` | 全部改「四点四十五分」 |

## 三、T2 触发与执行（全书断言全扫）
抽样密度 = 6 阻断 / 7 章 ≈ **0.86 ≥ 0.5**，且**合并阻断 ≥3** ⇒ 按 §0.3 / §0.7 **自动进入 T2**；T2 的覆盖本来就是全书，因此「再抽一倍」由全书扫描满足。
`python3 scripts/assertion_scan.py` → `review/t1-candidates.txt` **381 条候选行**，六类分布 ①2 / ②73 / ③192 / ⑥19 / ⑤83 / ④12。**已逐行读完 381/381**，疑点均回原文 grep 取证。

**T2 新查出并已修（4 条阻断级 + 4 条提示级）**
| 位置 | 类别 | 问题 | 依据 |
|---|---|---|---|
| `ch15 chapter fourteen.md:86` | ④身份 | 把 Jupiter 说成那条蛇的名字 | Jupiter 是**猫**的名字：`text/ch15:58` 给猫取名并要买 basket/brush；`:127` 蛇在盒里另说 |
| `ch20 chapter nineteen.md:150` | ③数字 | 「一个十六岁的学生」（Casey） | Casey 是 **Upper Sixth**（`text/ch20:4`/`:22`） |
| `ch07 chapter six.md:18` | ②绝对断言 | 「布伦登小姐从未露面」 | 全书不成立（ch10 起她本人出场），改「在本章始终没有露面」 |
| `ch14 chapter thirteen.md:92` | ⑤施受 | 「把校长请来掌权」主语与动作错位 | 已重写为指挥链直通王座 |
| `ch18 chapter seventeen.md:188` | ⑥场景 | 六地点里的「王宫」 | 原文 Royal Pavilion，改「行宫」 |
| `ch01:27/43/99`、`ch05:10/18/22/38/184`、`ch10:63/226` | 提示 | 块外引语、「英文与推荐信」误译、词头单复数、说话人归属 | 均按原文改 |

**逐条回源核过、判为无缺陷的高危候选（举证）**：`ch02:51`「倒数第二」＝`Last person but one`（`text/ch02:19`）；`ch09:148`「十五六岁」＝`Girls of fifteen or sixteen`（`text/ch09:265`）；`ch12:106`「死了十年」＝`Mine died ten years ago`（`text/ch12:142`）；`ch15:176`「十二三岁」＝`twelve, or thirteen at most`（`text/ch15:397`）；`ch22:82`「十名女生、五名二年级」＝`Ten girls. Five second-formers`（`text/ch22:115`）；`ch22:134`「十一岁上下」＝`barely eleven years old`；`ch24:101`「三次走正门」＝`not once, not twice, but three times running`（`text/ch24:115`）；`ch23:153` Melicent Pomphrey 确有其人（`text/ch04:238`）；`ch23:185` Jane 的银行账户宣言（`text/ch23:337`）；`ch04:104` 1970 年初版课本；`ch07:10`「四、五年级」＝`fourth and fifth years`（`text/ch07:31`）；`ch18:160` 真名套索规则（`text/ch18:385`）。
**判为可接受的修辞型绝对断言（不改）**：各章「第一次/唯一/全章唯一」类读者视角提示，均在本章范围内成立。

## 四、总览三篇人判（全篇）
概述 7 段梗概 + 3 主题 + 4 人物弧光；金句 25 条 × 4 子项；情感节点 9 节点 × 3 引语。
**生产期已修的事实错误**：概述把 Black Spot 归给 Miss Grending（实为 `text/ch08:55` Dr Tregennis）、把 BLACKMAIL 归给校长（实为 `text/ch09:181` 姑婆 Belinda 的信）；情感节点把「野餐伞下填字游戏」（ch16 场景）错挂到 ch17–ch19 节点。金句说话人 25/25 已 grep 确认；「呼应关系」编号互指逐条回查、修 9 处指错。

## 五、结论
- 阻断合计 **10 条**（抽样 6 + T2 新增 4），**全部就地修复并复验**：`gate.sh` 复跑 EXIT=0，`check_vocab` FAIL 0 / WARN 0，改动的 7 章 `chapter.sh` 全 rc=0。
- T2 已实质完成：候选行 **381/381 已读**，非抽样兜底。
- **T1 为同会话自检，不是「已通过审查」**；异会话复核未做，需用户另行发起。

**读了哪些候选行、共几行**：`review/t1-candidates.txt` 全 **381 行**（①相对章号 2、②绝对断言 73、③年龄数字 192、④亲属身份 12、⑤方向施受 83、⑥场景方位 19）；另抽样 7 章逐块人判 **79 块**（ch01 4 / ch05 13 / ch10 13 / ch14 14 / ch18 14 / ch23 15 / ch27 6）。
