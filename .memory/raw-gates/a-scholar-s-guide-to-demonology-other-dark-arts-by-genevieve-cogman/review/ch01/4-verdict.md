# ch01 R5 判定（Prophecy / Prologue，书信体）

机器层：`2-machine.json` rc=0（空引号 0｜子项缺 0｜关键词不成立 0｜中文过薄 0｜模板套话 0｜残句 0｜引语长度全部 ≤100 词）；形态 H1 ✅ `01. Prologue`、导航 5 项 ✅、块数 4（本书中位 12，范围 4–15，⚠️ 偏离建议区间不判红）。

## R4 逐块对应（4 块）

| 块 | 引语首 6 词 | 字数 | 中文理解 ↔ 引语 | 关键词在引语内 | 为什么这样写 ↔ 引语 | 施事三问 | 档位 |
|---|---|---|---|---|---|---|---|
| 1 | May I first say what | 61 | ✅ 逐句对应（夸纸笔信 / 现代世界忘了动笔 / 仍有人记得） | ✅ formal letter、forgotten how to apply pen to paper | ✅ 讲「先夸无用的小事立价值标准」+ 反现代底色 | 主语＝校长（I / my），受事＝那封申请信；无归属歧义 | 通过 |
| 2 | I have noticed certain deficiencies | 31 | ✅ | ✅ deficiencies、paperwork and references、at your interview | ✅ 只讲「先立威再留余地」，未越出引语 | 主语＝校长（I have noticed）；受事＝芬的材料与推荐信；「查过底细」由 `I have noticed` 直接支撑 | 通过 |
| 3 | I for one would far rather | 62 | ✅ | ✅ enthusiast、pallid disciplinarian、a dozen certificates、no true burning desire | ✅ 对立结构讲透；**已修**：原句把缺材料说成「苍白管束者」的典型特征（原文无此关联），改依据为 `Your letter speaks of a lifelong interest in Latin` | 主语＝校长（I would rather have）；受事＝enthusiast / disciplinarian 两类人 | 通过（修后） |
| 4 | many of our alumnae choose | 65 | ✅ **已修**：引语起点前移，`this` 的指代（校友不自夸）进块内 | ✅ maidenly modesty、secure a commanding position、don’t see you coming、military historians | ✅ 把「低调」重解为「战略隐蔽」 | 主语＝Some（校友）/ I（校长）；受事＝commanding position；「谁在自夸」回 `:25` 核＝alumnae 不夸耀 antecedents | 通过（修后） |

**逐字**：4/4 逐字命中（`quotes.py verbatim --full` 全书 356/356，本章 4/4）。

## 断言清单（阻断 3 / 提示 3）

| 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|
| 「后面每出现一次现代事物（维基百科、电邮、外卖）都会与这句形成对照」 | `text/ch01_chap1.txt:16/25`（两个词都在本章）；`/usr/bin/grep -c -i -E "takeaway\|delivery\|pizza" text/*.txt` → 仅 `ch15:280` 一处 | 无据的全书断言 | 阻断（已改） |
| 「材料缺失正是『苍白管束者』那一类的典型特征」 | `:19` 与 `:22` 两段之间原文无因果；`:22` 明写判断依据是 `Your letter speaks of…` | 因果错置 | 阻断（已改） |
| 块 4 引语 `this` 指代块外 | `:25` 前一句 `many of our alumnae choose not to boast of their antecedents.` | 引语截短 | 阻断（已补前移） |
| 「暗示学校不在维基百科上」 | `:25` `I fear we do not feature on Wikipedia` | 明说非暗示；与 `:99` 口径不一 | 提示（已改） |
| 「芬小姐自己也不知道缺的是哪一项」 | 全章仅信件，`/usr/bin/grep -c "Fen" text/ch01_chap1.txt` = 1（称呼行） | 对人物心理无据 | 提示（已改） |
| 「全章唯一出场者」 | 书信体，无场景 | 用词与文本形态不符 | 提示（已改） |

## 已核实为正确

- **「北约克郡荒原、约克郡」**（`ch01 prologue.md:21`）：原文 `text/ch01_chap1.txt:4-7` `North Yorkshire Moors, / Yorkshire` —— 两个地名分列两行，md 并列写成立。
- **「2003 年 10 月 10 日」**（`:21`）：原文 `:10` `10th October 2003`，日/月/年顺序与原文一致。
- **「旧生立下大功却从不声张」**（`:10`、`:99`）：原文 `:25` `many of our Old Girls have played vital parts in our nation’s history, many of our alumnae choose not to boast of their antecedents`。
- **「学校不在维基百科上的封闭之地」**（`:99`）：原文 `:25` `I fear we do not feature on Wikipedia, or other modern sources of information. We are somewhat exclusive.`
- **「信里只有『若你有这些品质，你在这里会顺利』的招聘标准，没有预言或点名」**（`:17`）：原文 `:22` `If you have all these things, then you will do well here.` —— 全信无预言、无点名，判断成立。
- **「信头以公文格式前置，仿档案卷宗的开卷方式」**（`:21`）：原文 `:1-10` 依次为校名、郡、日期，确为公文抬头格式。
- **词表 12 条例句**：逐条 `grep -F` 各命中 1 次，全部出自本章（deficiencies `:19`、antecedents `:25`、historians `:25`、tradition `:16`、interview `:19`、exclusive `:25`、classical/military/advanced `:25`、paperwork/enclosed documents `:19`、association `:28`）。
