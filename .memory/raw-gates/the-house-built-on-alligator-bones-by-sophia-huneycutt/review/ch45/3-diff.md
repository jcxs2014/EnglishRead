# ch45（Chapter Forty-Four）R3/R4 差异与定点核验

## 探针
- v45（引语前 6 词回源）：23 行全命中，MISS 0。
- ap45（直撇号）：md L56 `"pretending I didn't exist"` ＝ 直撇号 1 处；原文 text/ch45_chapter_forty_four.txt:93 为弯撇号 `didn’t`。
- in45（块内嵌英文）：未命中（仅模板 2 行）。
- span45（反引号自检）：模板 token MISS 为预期。

## 阻断
| # | 位置 | md 现状 | 原文 | 判型 |
|---|---|---|---|---|
| C-45-1 | md L56 | `"pretending I didn't exist"` | text/ch45_chapter_forty_four.txt:93 `pretending I didn’t exist`（弯撇号） | C 型（直撇号） |
| C-45-2 | md L10、L13 | 「Gazzie 手里有射钉枪」（两处） | text/ch45_chapter_forty_four.txt:168 `"I'm not going out there while she has the bolt gun."` —— bolt gun（击昏枪，与 ch43 Gazzie 手持同一件），全书 nail gun 0 命中 | C 型（事实错译） |

查无取证（C-45-2）：
```
$ /usr/bin/grep -n -i "nail\|gun" text/ch45_chapter_forty_four.txt
78:...several nails at the top sticking out...
168:A bitter laugh. “I’m not going out there while she has the bolt gun.”
```
（`nail gun` 连写 0 命中；`gun` 唯一命中即 bolt gun。）

## 提示
（无）

## 假红
（无）

## R4 定点核验（导航层断言逐条回源）
- 斧子在树桩上、属 Gazzie：text L114（`stuck in the tree stump—an axe`）、L120（`Gazzie’s axe was duller than Henri's`）✅
- 管家备餐门（butler's pantry）被锁、两人关在里面：L144 ✅
- "Open the door"：L81；"Let me in"：L87/L102 ✅
- "It's already over."（已结束了低语）：L192 ✅
- "She's at her worst when she's calm."（她 calm 的时候最坏）：L165 ✅
- 钥匙孔黑眼睛→"Ida?"→"No, I reassured myself. Gazzie."：L66/L69 ✅（先后顺序与 md 一致）
- 两个 Just because 残句：L189 ✅
- Hurricane Flora herself / temporary ally：L183 ✅
- 120 miles per hour：L93 ✅
- 砸破六扇前窗（six front-porch windows）：L135 ✅
- deadbolted：L60/L72/L78 ✅
- 上楼逐间隔窗顺序（Virginia's old room→Harrison's→Uncle Leon's→mine）：L183 ✅
- 开场电视节目 / 气象学家：L1 起 ✅

## 查无声明
- 导航「左脚在桥上踩刹车踩到剧痛」：`left foot` L64（`worked the brake with my left foot`）、`It was inches from the guardrail` L65 ✅命中。

## 快审护栏复核
- ch44 鳄鱼数与锁口径不涉本章；本章无新增冲突。

## 已核实为正确
- C-45-1、C-45-2 两条阻断证据如上，均为原文逐字级。
- 词汇表词头（deadbolted/silhouette/haphazardly/indestructible/projectiles/otherworldly 等）与例句均回源命中。
- 情感弧线、Tropes 层叙述与原文事件顺序一致（电视节目→桥→门前→尖叫→砸窗→备餐间偷听→上楼→办公室门）。
