# T1 自检结论 · monstrous-bitch-by-eleanor-johnson（2026-10-25）
抽样章：**ch01（首章）+ ch13（末章）**；理由：N=13 ⇒ ceil(13/8)=2，规则要求首末必含，两章正好覆盖首末（章号由公式先定，非读后挑选）。

## 一、阻断型（12 处，全部已修并复验）
- `ch05 3 roman witch bitches the persistence of lamia.md:109` ｜「随后**他**引入狄多」→「随后**她**引入狄多」｜作者 Eleanor Johnson 为女性（原文以 I/her 自述）
- `ch05…lamia.md:121` ｜「接着**他**给出全书式的判词」→「接着**她**给出…」｜同上
- `ch05…lamia.md:157` ｜「**他**用三个短语收尾」→「**她**用三个短语收尾」｜同上
- `ch12 10 monstrous bitches bite back.md:125` ｜「被**他**当成两种不同的传承语法」→「被**她**当成…」｜同上
- `ch12…bite back.md` 7 处（L18/L36×2/L46/L57/L60/L259）｜「埃里克托」→「**埃里赫托**」｜ch05、`00_概述.md`、`00_情感节点.md` 均作「埃里赫托」（原文 Erichtho）
- `ch12…bite back.md:18` ｜「第五部《地狱变体》（2018）」→「第五部《**苏斯皮莉亚**》（2018）」｜全书另 8 处 Suspiria 均作《苏斯皮莉亚》
- `00_概述.md:34` 与 `.overview_templates/ov_00_概述.md.tpl:34` ｜「而**维吉尔的《酒神的女信众》式收束**只有一个…」→「而维吉尔写**阿玛塔**的那一段，作者说听起来像《酒神的女信众》撞上《复仇女神》，她的判词只有一个…」｜The Bacchae 是欧里庇得斯的剧作；`text/ch05_3_roman_witch_bitches_the_persistence_of.txt:71` 原文只说维吉尔笔下阿玛塔段像 Bacchae 撞 Eumenides
- `ch10 8 possessed bitches…1970s.md:214` 与 `.overview_templates/ov_00_金句精选.md.tpl:230` ｜「这是**他们**见过的第一部作品」→「这是**我们**所见的第一部作品」｜引语原文 "the first literary or cultural work **we've** seen"；同文件 `:220` 已作「我们」
- `ch10…1970s.md:47` ｜「达妮埃拉**被**十三岁时遭强奸」→「达妮埃拉十三岁时遭强奸」｜病句；`text/ch10_8_possessed_bitches_of_the_1960s_and_197.txt:164` "she was raped at the age of thirteen"
- `ch13 11 back to babylon.md:251` ｜「**四百三十年前**女性可以崇拜母亲也可以畏惧她」→「**四千三百年前**女性可以同时崇拜又畏惧一个母亲」｜漏「千」；`text/ch13_11_back_to_babylon.txt:140` "forty-three hundred years ago"；同文件 `:81` 已作「四千三百年前…」
- `.overview_templates/ov_00_金句精选.md.tpl:54` ｜「**七十年后**的银幕上」→「**到七十年代**的银幕上」｜所指第 ⑳ 条为 ch11（1970s–80s 吸血鬼片），本条为 ch02（引言），二者间不存在 70 年年差
- `.overview_templates/ov_00_金句精选.md.tpl:78` ｜「与第 **⑮** 条同构：**三百多年后**，父权处置怪物母狗的路仍然只有杀死、驯服、遏制三条」→「与第 **㉑** 条呼应：**直到七十年代**，…」｜kill/tame/contain 出自 `text/ch11_9_sexy_vampire_bitches_of_the_1970s_and_.txt:182`；⑮ 为 ch08《卡米拉》，与 ch03 提亚马特不同构，且 300 年年差无出处

## 二、提示型（记录不修）
- 0 处：`gate.sh` 汇总「阻断型 0 ｜ 提示型 0」，`structure.py order` 0 缺陷 0 不可判定，`corruption_scan` FAIL 0。

## 三、工具侧发现
- `assertion_scan` ③类按「数字＋量词」命中，408 行中真含「岁」仅 6 行；归并出 93 种唯一表达式，其中约 41 种为纯量词套话 ⇒ 宜先聚类再人读（本次按此法归并后逐条回源）。
- ④类实际 57 行（首记 56，差 1）；⑥类 0 行。
- 引语含 `…` 会让 `structure.py order` 判「不可判定」⇒ 本书 184 条引语全部为同段连续、无省略号引语。
- facts 与素读产物在 `.memory/raw-gates/<slug>/production/`，**不在书目录下**（按书目录找过、失败一次）。
- `/tmp/mb_names_all.py` 传书目录会 `IsADirectoryError`，须无参运行。

## 四、覆盖
- 抽样章素读：ch01 **9/9 ✅**、ch13 **13/13 ✅**（改后重跑，rc=0）。
- 总览三篇全篇人判：`00_概述.md` 90 行/18 引语、`00_金句精选.md` 294 行/24 条、`00_情感节点.md` 96 行/9 节点 —— 引语全部逐字命中、章号标注全部对应，0 阻断。
- `assertion_scan` 670 行：①46 ②76 ③408 ④57 ⑤72 ⑥0。T1 全读 ①②③⑥；因阻断 ≥3 自动进 T2，**T2 已执行**：全量读 ③④⑤，③的 52 种载荷表达式逐条回 `text/` 核验（另核 ch02「九项形容词」=9、ch04「nor for」=4、ch12「playing at」=4、ch09 影片=6 部）。
- 复验：`chapter.sh` ch05/ch10/ch12/ch13 **rc=0**；`gate.sh` **RC=0**（184 块、密度 100%、夹杂 0%）；`overview.py` quotes/full/labels **三门 RC=0**（60/60 逐字、覆盖 13/13）；`structure.py order` 13 md/184 块 0/0；`corruption_scan` FAIL 0；`mb_batch_audit` 0 硬缺陷；`mb_vocab_hit` 13/13 章 0 未命中；`mb_names_all` 0 臆造专名。
- **升级：是（T1 查出 12 条阻断 ≥3 ⇒ 自动进 T2 断言全扫；T2 另查出 4 条并已修，即上表第 9–12 项。）**
- 本次共人读候选行 **670 行全量**（①46 ②76 ③408 ④57 ⑤72 ⑥0），另读总览三篇 480 行、抽样章素读事实 22 条。

**T1 为同会话自检，非异会话终审。**
