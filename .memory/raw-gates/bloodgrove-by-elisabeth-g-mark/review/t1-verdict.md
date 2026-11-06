# T1 自检 · bloodgrove-by-elisabeth-g-mark

抽样章（先写后读，按 >40 章规则取 1/5 且 ≥10，首末必含）：ch01, ch06, ch12, ch17, ch23, ch28, ch34, ch39, ch45, ch51, ch58（11/58 = 19%）。
理由：规则档位（1/5），等距取样覆盖「启程—血价—博弈—教堂—决斗—订婚—救援—公开战—雪夜—兽化—终局」十一个结构节点。

| 位置 | 改前 | 改后 | 原文依据 |
|---|---|---|---|
| ch51 全章分析子项 | 威尔被写成「她」（约 20 处：她不再想跑／她的脚踝／她想被捉／她拿他的招牌词…） | 全部改为「他」，Elodie 处保留「她」 | ch51 原文本：主角为 Will（"No. He did not want to run anymore."） |
| 26 个章节 md 的分析字段 | 中文句子里残留英文充当句子成分：venom／accept／mandate／threat／challenge／butcher／milky／gasping／armor／candidacy／consent／haunted／cord／reacting／hope／flag／imagery／gleam／gaze／dead／letters／sad／fairy tale／rivalry／species／dynasty／insult／energy／quiet+command／choreography／innocuous 等 | 逐条汉化（括注式英文释义与引文保留） | 中文层判据：分析字段须为中文 |
| ch28 叙事手法 | 「三连『为什么』」 | 「连串的『为什么』」 | ch28 原文本实为 5 处 why（"Why this?" + 4 连问） |
| ch30 读者视角提示 | 「三百只眼睛」裙 | 「数百只眼睛」裙 | ch29 "Hundreds of eyes covered the sweeping skirt"；ch57 "embroidered with hundreds of eyes" |
| ch34 读者视角提示 | 「第一次喝『人』的血」 | 「第一次被人主动喂血」 | ch20 已舔过她指尖的血，ch25 喝过自己的血；ch34 是首次被喂 |
| ch23 叙事手法 | 「第一次主动施法（月光球）」 | 「第一次开口祈求，换来月光球」 | ch23 同章前段五烛齐燃亦由他的魔法引发，故非首次施法 |
| ch45 读者视角提示 | 「第一次主动说『我会输心』」+ 引「你还有两周」 | 改为「ch41 已说『我可能把心输给你』」+ 引原文 "In two weeks, I will be gone" | ch41 "I may lose my heart to you"；ch45 原文本 |
| ch46 一句话总结 | 「她吃过妹妹死胎的父亲」 | 「她父亲吃掉妹妹死胎」 | ch46 "I was there when he ate my sister's stillborn child" |
| ch48 读者视角提示 | 「ch14『四个月』」 | 「ch01『四个月』」 | 四个月出自 ch01 "When I return in four months" |
| 00_概述 / 00_情感节点 | 「十八岁的朋友 Saint」 | 「十八岁上下」 | ch07 "perhaps eighteen at most" |
| ch28 读者视角提示 | 「所有Feed 他人者」 | 「所有以他人为食者」 | 中文层判据 |

- 素读复验：11/11 抽样章 `suread.py --check` 锚点零 MISS；抽 3 条事实回源（ch28 面具真相、ch51 兽化告白的「火车」、ch58 王的一二七岁判决语境）全部命中。
- 总览三篇全篇人判：`overview.py quotes` 63/63（100%）、`full` 章节标签 59/59 对、H1 语义 0 错配；中文叙述断言逐条回源（年龄/亲属/谁做的/数字四类）。
- 断言预筛：`assertion_scan.py` 输出 697 行 → ①相对章号 20 行全读、⑥场景方位 9 行全读、③年龄数字 311 行按「数字↔英文数词」程序化对账（命中 118 行为修辞性计数，非事实断言）、②绝对断言 225 行与⑤方向施受 54 行按抽样+关键词复核。
- 合计：12 条整改（阻断级 4 类：代词错置、中文层英文残留、施受颠倒、虚构数字；其余为章号错指与绝对化断言）。