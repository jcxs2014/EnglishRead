# ch37 · R5 判定表（A Fatal Legacy / Charlotte Vassell）

- 章节：`ch37 robbie takes over the case`（原文章节号 37；场景题 `The Police Station`）
- 权威源：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch37_37.txt`
- 落盘：`.memory/raw-gates/a-fatal-legacy-by-charlotte-vassell/review/ch37/`
- 流程：R1 素读（先落 `1-suread.json`，未开任何 md）→ R2 机器层（`bash scripts/chapter.sh … --json`，退出码 **0**）→ R3（`3-diff.md`）→ R4（`4-correspondence.md`）→ R5（本文件）

## 一、四组数

| 组 | 口径 | 结果 |
|---|---|---|
| **逐字** | 7 个引语块是否与原文连续逐字串 + 词汇表 29 条例句是否逐字 | 引语 **6/7 通过、1 不通过**（原句 6 漏收尾右单引号 `’`，全书 391 块中唯一非逐字）；词汇例句 **29/29 通过**（表头 3 行不计）。**逐字缺陷 1 处（1/7）** |
| **对应** | 逐块回答「这段中文是不是在讲这句引语」 | **7/7 对应**。引语选短 0、跑题（讲全书主旨/作者生平）0、密度不足 0；块 3/4/6 的问题落在断言组，不计对应失分 |
| **形态** | H1 / 导航项名与项数 / 子项集 / 块数 vs 本书众数与 profile | H1 ✓、导航 5 项 ✓、子项集 4 项 ✓、块数 7＝众数 ✓；**偏离 1 处（分部名缺失，提示）** |
| **断言** | 漏/编/错/施事归属/事实断言逐条判定 | 断言条目 20 条：**阻断 3 / 提示 16 / 假红 0 / 跳过 1**（跳过项＝词汇档位注水，未逐条判档） |

**阻断型合计 3 条**：漏-1（Matt 的下一步报告与 Fenella 同意拆门全章无着落）、错-1（原句 3「作者不写安米的情绪」与原文矛盾）、错-2（原句 6 引语非逐字）。
**假红 0 条**（本章无工具口径错报）；**未核 1 条**（词汇档位注水）。

## 二、形态组细目

| 项 | md 实况 | 本书众数 / profile | 偏离与理由 |
|---|---|---|---|
| H1 | `# 37. The Police Station` | 本书 `# NN. 标题` 形；原文场景题 `text/ch37_37.txt:17` = `The Police Station` | 无偏离（`chapter.sh` `h1_shape_ok: true`） |
| 导航项名与项数 | 5 项：一句话概括 / 视角 / 线索结构 / 人物弧线 / 叙事手法 | 众数 5（`nav_count: 5`、`nav_count_ok: true`） | 无偏离 |
| 子项集 | 中文理解 / 关键词 / 为什么这样写 / 读者视角提示 | `subitems_modal`＝本书众数＝profile（mystery-thriller）4 项 | 无偏离 |
| 块数 | 7 | `block_median` 7.0（范围 5–10） | 无偏离 |
| **分部名** | md **未写**分部名 | 同属 epub `Part-008「FRIDAY」`（含 ch36–ch40）的 ch36 / ch38 / ch39 都在导航写了「A FRIDAY IN MAY」；本书 26/54 章写分部名 | **偏离（提示）**：分部名属可选信息（全书半数章写、半数不写），不构成硬性众数违规；但同一分部内 ch37 与 ch36/ch38/ch39 不一致，属体例不齐。若要补，按本书体例写「A FRIDAY IN MAY」。⚠️ 另注：epub 里「A FRIDAY IN MAY」是**另一个分部**（Part-001，只含 ch01）的标题，Part-008 的标题实为「FRIDAY」——ch36/ch38/ch39 的写法已把两者混名（属他章问题，ch37 未涉及） |

## 三、断言判定表

| # | 断言 | 证据（章:区间） | 结论 | 档位 |
|---|---|---|---|---|
| 1 | **交接指令原话与理由**＝「Caius 已向总警监 flag：罪案发生在其父持有租约的物业上」，md 未写成别的理由 | md `:19`（逐字引语）+ `:21` 中文理解「这些案子发生在他父亲持有租赁权的地皮上」+ `:59` 读者视角提示「一纸利益冲突」；原文 `text/ch37:23` [123,432]「as Caius has flagged with me that these crimes happened on property that his father owns the leasehold on」 | **成立**（本章专属判据通过：理由＝产权/利益冲突，非能力、非排班、非信任） | 提示 |
| 2 | 原句 3「为什么这样写」：作者不写安米的情绪 | 原文 `text/ch37:65` [2601,2652]「‘I’m …’ Amy let out an exasperated, guttural groan.」；md 自己的词汇表 `:92` 亦以该句为例句 | **不成立**：作者写了安米的情绪；md 自相矛盾 | **阻断** |
| 3 | 原句 6 引语为原文逐字 | md `:54` 结尾作「…a person. Matt got in the car.」；原文 `text/ch37:129` [6734,7553] 作「…a person.’ Matt got in the car.」 | **不成立**：漏 `’`，非连续逐字串（最长逐字前缀 796/817） | **阻断** |
| 4 | 原句 2「前喜剧红星 Jimmy Jones」＝ former comedy enfant terrible | 原文 `text/ch37:44` [1442,2116]；md 词汇表 `:80` 释 enfant terrible 为「被宠坏的麻烦人物／难缠角色」 | **不成立**（译法失真且与本文件词汇表冲突） | 提示 |
| 5 | 原句 6「被发现后还骂了他一句」＝ He called me a "chink" | 原文 `text/ch37:129` [6734,7553] | **定性降级**：种族辱称被写成一般斥骂，并丢掉「血统/来源」这条与第一条呼应的线索 | 提示 |
| 6 | 原句 6「你工作不行但你是个人」＝ Not because she's good at her job, but because she's a person | 原文 `text/ch37:129`；md 同块中文理解 `:56` 口径正确 | **不成立**（逻辑方向反转；同块两处口径不一致） | 提示 |
| 7 | 原句 4「作者让地貌本身变成作案动机」 | 原文 `text/ch37:89` [3393,4280] 只写传说与罗盘四方位点；作案动机在 `text/ch37:95` [4355,5350]；md 同块读者视角提示 `:45` 自己写的是「往后取证要走的那条路线」 | **越界**（属原句 5 的内容，且与同块自述不一致） | 提示 |
| 8 | 「警长离开办公室时…」＝ the Chief Superintendent | 原文 `text/ch37:32` [763,1032]；md `:21` 作「总警监」、`:75` 词汇表作「（英国警衔）总警监」 | **不一致**（同章两译名） | 提示 |
| 9 | 原句 1「他父亲持有租赁权」＝ his father | 原文 `text/ch37:23` [123,432] 先行词为 Caius；md `:21`「他」紧跟 Robbie 与「向他报告」 | 指代**歧义**（可能读成 Robbie 的父亲）；交接理由不得走样，建议写「凯厄斯的父亲」 | 提示 |
| 10 | 结尾「拆下那扇封了几十年的地下室门」 | 原文 `text/ch37:139` [7568,8407] 门上是百年的厚漆；`text/ch37:95` [4355,5350] sealed up for decades | 原文该从句先行词本身有歧义，md 属可接受压缩 | 提示 |
| 11 | 导航「他本人对凯厄斯、连带对这家博物馆，还带着一笔旧账与成见」 | 原文 `text/ch37:29` [565,760]（Robbie 对 Caius 的态度）、`:126` [6612,6731]（对 Billy 的袒护）；博物馆旧账全由 Amy 转述（`text/ch37:89`、`:95`）；Robbie 首次出现即本章 | **无据**：Robbie 在本书中此前从未出现（见下取证），他对博物馆无「自带旧账」 | 提示 |
| 12 | 导航「在 Matt 点破之后跟他僵持几秒」 | 原文 `text/ch37:74` [2916,3063]「Robbie stared at Amy. She stared back. They reached a stalemate.」 | 指代**歧义**（按最近先行词读成 Matt，则与原文不符；实为 Robbie 与 Amy） | 提示 |
| 13 | 导航「才低声连声道歉」 | 原文 `text/ch37:74` 该处一次道歉；另一次 `'Sorry, um.'` 在 `text/ch37:86` [3338,3390]，属另一轮对话 | **次数不符**（非连声） | 提示 |
| 14 | Matt 的下一步报告：35 号（黄房子）实地走访、状态机密的安保、申请进入 35 号地下室、拆下研究所地下室门的许可、**Fenella 今早同意**、Matt 即将前往并联络法证 | 原文 `text/ch37:101` [5438,6080]；md 七块引语无一覆盖该区间；导航五项、词汇表与结尾总结均无 | **缺环（漏）**：章末法证队拆门的授权来源与下一条现场线均无着落 | **阻断** |
| 15 | 白板颜色图例（红＝死亡、橙＝闯入、黄＝…）与「黄房子＝35 号」 | 原文 `text/ch37:53` [2389,2461]（Amy 的解说被 Robbie 打断、未讲完）、`:56`–`:62` [2464,2598]；md `:13` 仅写「Amy 再补上白板地图」 | **缺环（漏）**＋把被打断的解说写成完成态 | 提示 |
| 16 | Robbie 主动要求同去现场、Amy 如释重负；`He'd been told.` | 原文 `text/ch37:104`–`:107` [6083,6332] | **缺环（漏）**：本章「接手」的实际动作未进「人物弧线」 | 提示 |
| 17 | 导航以「Priory Square」称广场 | `text/` 全目录 19 章命中（ch31、ch33、ch34 等）；本章原文只写 the square | **成立**（书中确名，非杜撰） | 提示 |
| 18 | Robbie 是本书新人物 | `/usr/bin/grep -c "Robbie" text/ch0*.txt … text/ch3[0-6]*.txt \| /usr/bin/grep -v ":0$"` → 无输出，退出码 1（ch01–ch36 全 0 命中） | **成立** | 提示 |
| 19 | 导航「Amy 站着讲白板」 | 原文 `text/ch37:41` [1238,1439] 只写她指向白板，未言站/坐 | **无据（细节）**，不影响情节 | 提示 |
| 20 | 词汇表 29 条例句 | 独立脚本逐条比对 `text/ch37_37.txt`：**29/29 精确命中**（表头 3 行不计）；档位是否注水未逐条判 | 例句**成立**；档位注水未核 | 跳过 |

**断言组小计**：阻断 3、提示 16、假红 0、跳过 1。

## 四、零命中类断言的取证（命令 + 输出 + 退出码）

```
# (a) 「Robbie 在 ch37 之前全书未出现」
/usr/bin/grep -c "Robbie" text/ch0*.txt text/ch1*.txt text/ch2*.txt text/ch3[0-6]*.txt | /usr/bin/grep -v ":0$"
→ 无输出；cmd_exit=1（ch01–ch36 全部 0 命中）

# (b) 「text/ 里没有 FRIDAY IN MAY 这个串」（分部名只能来自 epub toc）
/usr/bin/grep -ri "FRIDAY IN MAY" text/
→ 无输出；cmd_exit=1

# (c) 分部归属：ch37 属于 epub Part-008「FRIDAY」（含 ch36–ch40）
python3 解析 library/…epub 的 OPS/toc.ncx（navPoint 树）→
PART: FRIDAY → ch36 s051 / ch37 s052 / ch38 s053 / ch39 s054 / ch40 s055
PART: A FRIDAY IN MAY → ch01 s009（另一个分部）

# (d) 「全书 391 个引语块中只有原句 6 非逐字」
python3 对 ch01–ch54 的 md 各正则取出全部引语块，逐条判断是否为对应 text/*.txt 的子串
→ total blocks: 391   non-exact: 1
   ch37 … 原句6: prefix_ok=796/817  md_next=' Matt got in the car.'  src_next='’ Matt got in the car.'
```

## 五、已核实为正确（防误修，勿再改）

1. **交接理由＝产权/利益冲突**（`text/ch37:23` [123,432]）——md 的「不是能力不够，而是『地』」「一纸利益冲突」成立，**不得改成别的理由**（本章专属判据）。
2. **「四正方位点围成一个 nexus」**（`text/ch37:89`）——原文 `form a nexus over the site`，`the site`＝该地点/遗址，md 作「在遗址之上」成立。
3. **「Jimmy Jones 被中断的直播画面里有个贼……正从地下室楼梯那一带走出来」**（`text/ch37:95`）——原文 `coming out of the area where the basement stairs are`，md 未把「地下室楼梯区域」写成「地下室」本身，成立。
4. **「Caius 认为那不是巧合」**（`text/ch37:95`）——施事是 Caius 不是 Amy，md 归属正确。
5. **「安米知道那栋楼里每个抽屉她都翻过」**（`text/ch37:95` `Amy knew she had gone through every drawer in that building.`）——成立。
6. **说话人未指性别**（`text/ch37:142` `their voice`）——md 未给那位法医编造性别，成立。
7. **「由面包店里的一个 incel 取走」/「他在店里对每个进门的女顾客都搭讪」**（`text/ch37:44`）——Scott 是在面包店**工作**的 incel、且对每个女客搭讪，md 未把面包店写成 Scott 所开，成立。
8. **「Robbie 先打破沉默道歉」**（`text/ch37:74` `Robbie broke the silence.`）——成立。
9. **词汇表 29 条例句全部是本章原句**（29/29 精确命中）——成立，勿改例句。

## 六、覆盖声明

- 本次**只审 ch37**；本书其余 53 章**未查**（不得写成「通过」）。
- 已跑：R1 素读（先落盘后开 md）→ R2 `chapter.sh --json`（退出码 0；7/7 引语门禁判绿、0 缺失、0 结构错、0 中文过薄）→ R3 三单 → R4 逐块 → R5。
- 第二实现：引语逐字与词汇例句逐字均用**独立脚本**（非 `chapter.sh` 路径）复核——原句 6 即由第二实现抓出，门禁口径为前缀窗口，未能发现结尾标点被吞。
- 未查项：词汇档位注水（跳过 1）；本书其余章节的同型问题。
- 本目录外**未写入任何文件**，未改动书目录任何 md，未执行 `git add` / `git commit`。
