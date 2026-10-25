# ch07 · T3 判定表

- 章：Chapter Six（md：`ch07 the death cards.md`；原文 `text/ch07_chapter_six.txt`）
- R1 素读：`1-suread.json`（**独立代理**，只读 `text/`，禁开任何 md；8 条事实 + 转折点；锚点经中央脚本 `t3_suread_fix.py` fail-closed 核验：逐字命中且全文唯一）
- R2 机器层：`2-machine.json`（第二实现，verdict=ok；11 块 / 20 片段 / segment_miss=0 / struct_bad=0）
- R3 对账：`3-diff.md`
- 覆盖：**全章 11 块逐块 R4 ＋ R5**；无「只有机器层」的块

## R4 逐块对应（唯一不可机械化的一步）

| 块 | 词数 | 关键词 | 引语逐字 | 中文是否在讲这句引语 | 施事/受事 | 档位 |
|---|---|---|---|---|---|---|
| 1 | 42 | training sessions / stricken expressions | ✓ | ✓ 两位收割者离开、老板心情糟 | ✓ | 通过（读者指引另见提示 1） |
| 2 | 60 | Chief Executive Officer / hawklike | ✓ | ✓ 三高管等他、敌意 | ✓ | 通过 |
| 3 | 69 | never grant them / one direction | ✓ | ✓ 不可逆＝单向路线 | ✓ | 通过 |
| 4 | 32 | wishes to be brought back / six weeks | ✓ | ✓ 请求＋理由＋时限 | ✓ | 通过 |
| 5 | 68 | The Reaper Handbook / sacrosanct | ✓ | ✓ 手册宣读禁令 | ✓ | 通过 |
| 6 | 72 | One hundred thirty-five / forty-seven days | ✓ | ✓ 资历被一笔带过 | ✓ | 通过 |
| 7 | 78 | less earth-shattering / I am a marshmallow | ✓ | ✓ 一次触碰推翻百年冷漠 | ✓ | 通过 |
| 8 | 72 | Not since 1623 / customers and also our product | ✓ | ✓ 数据过期、指标下滑 | ✓ | 通过 |
| 9 | 80 | fifth consecutive year / pinball machines | ✓ | ✓ 连续五年不达标 | ✓ | 通过 |
| 10 | 50 | eight-week extension / Mid-Level Two | ✓ | ✓ 合同条款（八周／交回／Upgrade） | ✓ | 通过（引语层缺「观察差事」这一半，见 R3 提示 1） |
| 11 | 72 | anything but benevolent / Lower quotas | ✓ | ✓ 「你。」＋配额下滑 | ✓ | 通过（分析层引语外，见提示 2） |

## R5 判定表

| 断言 | 证据（text/ 文件:行 ＋ 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 原句 1 读者视角提示：「两位同事一个在配额上没达标，一个则是『态度不达标』」 | `text/ch07_chapter_six.txt:19`："Behind quota?"；`:25`："I've hit quota," the other says. "But my attitude isn't up to par." | **事实成立**（两条绩效信息逐字在原文），但**不在本块引语内**（在本块之后正文）；库内同类「分析层回引同章别处」全书仅 2 处 ⇒ 非库内惯例 | **提示**（引语选短；不改：属「读者视角提示」层的前瞻功能） |
| 原句 11「为什么这样写」：「Daniel 随后那句『像病毒一样被隔离』……只有两个字：我懂」 | `text/ch07_chapter_six.txt:270`："So he's isolating me like a virus they don't want spreading. This shouldn't rankle as much as it does. "I see."" | **事实成立**（逐字可回溯），但不在本块引语内 | **提示**（分析层引语外；不改） |
| 原句 6「为什么这样写」：「他先纠正数字（首席人事官说的是一百年）」 | 本块引语逐字："One hundred thirty-five," I correct. | 成立：既有「我纠正」的动作，被纠正的旧值（一百年）由「correct」隐含；同章原句 8 的 "Centuries, then." 与 "more than a century" 佐证量级 | 提示（已核实为正确） |
| 原句 4「为什么这样写」：「这个长度正好落在后来那份延寿合同能够覆盖的范围里」 | 原句 10 逐字："At the end of this eight-week extension…"；原句 4 逐字："in six weeks" | 成立（六周 ⊂ 八周） | 提示（已核实为正确） |
| 原句 9 读者视角提示：「降职的终点是去撒旦的地下室办公室上班」 | 本章词汇层例句逐字（已由 `t3_vocab_check.py` 核过）："demoted Reapers are sent to work in Lucifer's basement office for eternity." | 成立（同章别处，事实正确） | 提示 |
| 导航「早上醒来还是厌倦死亡的收割者，现在是一颗棉花糖」 | 原句 7 逐字："When I woke up this morning, I was a disgruntled and disinterested Reaper… Now, apparently, I am a marshmallow." | 成立 | 提示（已核实为正确） |
| 导航「三位高管」 | 原句 2 逐字："the Agency's Chief Executive Officer, Chief People Officer, and Head of Inhuman Resources" | 成立 | 提示（已核实为正确） |

## 分组计数（只报四组）

- **逐字**：11/11 块整串命中，查无 0（`2-machine.json` verdict=ok；20 片段逐条回查，segment_miss=0）
- **对应**：阻断 0，提示 3（引语选短 2 · 引语层缺块承载 1）；11 块的中文均在讲本块引语，施事/受事逐块核过，无反转
- **形态**：阻断 0（H1 `07. Chapter Six` 合本书形态 · 导航 5 项齐 · 4 子项齐备 · 11 块在本书众数区间 3–12 内 · 编号连续无撞车 · 词数 32–80 全落库内常见区间）
- **断言**：阻断 0，提示 6，未核 0

## 阻断

（无）

## 提示（只记不改）

- **[对应]** 原句 1 读者视角提示引用了本块引语外的两条绩效信息（`text/ch07:19`、`:25`）——事实成立，属「读者视角提示」层的前瞻功能，库内此类仅 2 处，非惯例但不成缺陷
- **[对应]** 原句 11「为什么这样写」引用了本块引语外的 `text/ch07:270`（"isolating me like a virus… I see."）——事实成立，属分析层的全章回望
- **[对应/漏]** R1 fact 5 的后半「由 Agency 雇员观察她」这一交换项，**引语层无块承载**（只在导航「一句话概括」与原句 11 读者视角提示里）⇒ 按 lifeguard T3 判据「导航层承载 ≠ 取舍理由」，记提示型漏；补救可向后扩原句 10 的引语（需验「原文连续一段」）或拆块
- **[R1 工件]** `1-suread.json` fact 2 把 Lucy 的**妹妹**写成「姐姐」——md 原句 4 写「她妹妹六周后结婚」是对的，不修 md；此条作为审查工件缺陷留档

## 已核实为正确（后续不得以「读着不对」为由改动）

| 表面像错的写法 | 为何成立 | 原文逐字 | 出处 |
|---|---|---|---|
| 原句 6「他先纠正数字（首席人事官说的是一百年）」 | 引语是 "One hundred thirty-five," I correct.，动作本身就是纠正；旧值由 correct 隐含 | "One hundred thirty-five," I correct. And forty-seven days. | `text/ch07_chapter_six.txt` |
| 原句 4「六周正好落在后来那份延寿合同能覆盖的范围里」 | 六周 ⊂ 八周延寿 | "Her sister is getting married in six weeks." / "At the end of this eight-week extension…" | 同上 |
| 原句 9 读者视角提示「降职的终点是撒旦的地下室办公室」 | 本章词汇层例句逐字（已机器核过） | "demoted Reapers are sent to work in Lucifer's basement office for eternity." | 同上 |
