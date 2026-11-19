# 任务表 · public-access-afterworld-by-jane-schoenbrun

- 书：Public Access Afterworld — Jane Schoenbrun（Hogarth / Random House，© 2026），奇幻/酷儿小说长篇；**电视剧集结构**：正文按 10 个 Episode 编排，集内章号从 1 重开
- 语料：`text/` 78 件零偏移（ch01=Foreword；ch02–09=Ep1 章1–8；ch10–17=Ep2 章1–8；ch18–25=Ep3 章1–8；ch26=Ep4「Chicago」**整集单件**；ch27–33=Ep5 章1–7；ch34=[Midseason Hiatus] 正文；ch35–40=Ep6 章1–6；ch41–49=Ep7 章1–9；ch50–54=Ep8 五部虚构电影条目；ch55–64=Ep9 时间戳小节 ×10；ch65=Ep9 末无标题 coda；ch66=Postscript: The Video Store；ch67–77=Ep10 章1–11；ch78=Postscript: Five Years Later）
- 三方对齐 PASS：版权页（Hogarth 2026, ISBN 9780593978405）+ 目录页 78 篇正文 + 提取实测 78 件（另跳过：Ep 分集页 ×11、Dedication/Epigraph、p009_sup「click here」提示页、致谢/作者页/推广页）
- verify_corpus：**PASS**（expect 78 / FAIL 0 / WARN 1）——WARN=ch42、ch61 疑似页码 bleed，**选句与例句避开粘连点**；锚点 13 件 + shared=Erin,Bethany,Willa,David,Chimotera（人物跨集复现为本书设定）
- 体裁 profile：novels（导航 5 项 / 4 子项 / 新书前 3 章块数 2–15 / 总览 3 篇）
- 章词数：374–3,735（中位 ~1,900）；**ch26=13,278 词**（Episode Four 为书内无子章的单件中篇：按 2–15 硬门写满 15 块，跨全篇选段；用户试产验收时可改判拆分）
- ⚠️ ch71 仅 374 词 / ch09 581 / ch65 582 / ch62 610 / ch49 687 / ch34 715 / ch64 716 / ch17 763 / ch24 789——均按 2 块下限写
- H1 形态（多分部章号重复，按 german-wife 先例）：`# NN. Chapter N（Episode X: 部名）`；特殊件 `# 01. Foreword` / `# 26. Episode Four: Chicago` / `# 34. [Midseason Hiatus]` / `# 50. Chimotera! (1944)` / `# 55. 2:49 a.m.`（跟 text 首行形态）/ `# 66. Postscript: The Video Store` / `# 78. Postscript: Five Years Later` / ch65 无书内标题（落笔时定，倾向 `# 65. （无标题）`）
- 生成批节奏：约 1 章/次；每章 suread → 写 → chapter.sh → pathspec commit → 每批 gate
- 完工定义：总览三篇 + T1 自检三件套（t1-verdict.md / t1-candidates.txt / 台账一行，审查方填 `自检`）

| 章 | 书内标题 | 词数 | 状态 | commit |
|---|---|---|---|---|
| ch01 | Foreword | 1,339 | 试产中 | |
| ch02 | Ep1 Ch1 | 2,545 | 待写 | |
| ch03 | Ep1 Ch2 | 2,372 | 待写 | |
| ch04 | Ep1 Ch3 | 2,301 | 待写 | |
| ch05 | Ep1 Ch4 | 1,497 | 待写 | |
| ch06 | Ep1 Ch5 | 2,076 | 待写 | |
| ch07 | Ep1 Ch6 | 2,575 | 待写 | |
| ch08 | Ep1 Ch7 | 1,416 | 待写 | |
| ch09 | Ep1 Ch8 | 581 | 待写 | |
| ch10 | Ep2 Ch1 | 2,865 | 待写 | |
| ch11 | Ep2 Ch2 | 1,230 | 待写 | |
| ch12 | Ep2 Ch3 | 1,659 | 待写 | |
| ch13 | Ep2 Ch4 | 2,209 | 待写 | |
| ch14 | Ep2 Ch5 | 1,960 | 待写 | |
| ch15 | Ep2 Ch6 | 1,419 | 待写 | |
| ch16 | Ep2 Ch7 | 2,381 | 待写 | |
| ch17 | Ep2 Ch8 | 763 | 待写 | |
| ch18 | Ep3 Ch1 | 3,515 | 待写 | |
| ch19 | Ep3 Ch2 | 2,464 | 待写 | |
| ch20 | Ep3 Ch3 | 2,106 | 待写 | |
| ch21 | Ep3 Ch4 | 2,010 | 待写 | |
| ch22 | Ep3 Ch5 | 899 | 待写 | |
| ch23 | Ep3 Ch6 | 2,491 | 待写 | |
| ch24 | Ep3 Ch7 | 789 | 待写 | |
| ch25 | Ep3 Ch8 | 1,150 | 待写 | |
| ch26 | Episode Four: Chicago（单件） | 13,278 | 待写 | |
| ch27 | Ep5 Ch1 | 2,056 | 待写 | |
| ch28 | Ep5 Ch2 | 2,499 | 待写 | |
| ch29 | Ep5 Ch3 | 3,130 | 待写 | |
| ch30 | Ep5 Ch4 | 3,117 | 待写 | |
| ch31 | Ep5 Ch5 | 2,847 | 待写 | |
| ch32 | Ep5 Ch6 | 2,296 | 待写 | |
| ch33 | Ep5 Ch7 | 3,635 | 待写 | |
| ch34 | [Midseason Hiatus] | 715 | 待写 | |
| ch35 | Ep6 Ch1 | 3,670 | 待写 | |
| ch36 | Ep6 Ch2 | 1,516 | 待写 | |
| ch37 | Ep6 Ch3 | 3,735 | 待写 | |
| ch38 | Ep6 Ch4 | 2,466 | 待写 | |
| ch39 | Ep6 Ch5 | 1,432 | 待写 | |
| ch40 | Ep6 Ch6 | 1,040 | 待写 | |
| ch41 | Ep7 Ch1 | 1,016 | 待写 | |
| ch42 | Ep7 Ch2（页码 bleed 避粘连） | 2,677 | 待写 | |
| ch43 | Ep7 Ch3 | 1,705 | 待写 | |
| ch44 | Ep7 Ch4 | 1,436 | 待写 | |
| ch45 | Ep7 Ch5 | 3,389 | 待写 | |
| ch46 | Ep7 Ch6 | 2,599 | 待写 | |
| ch47 | Ep7 Ch7 | 1,255 | 待写 | |
| ch48 | Ep7 Ch8 | 2,771 | 待写 | |
| ch49 | Ep7 Ch9 | 687 | 待写 | |
| ch50 | Ep8: Chimotera! (1944) | 2,506 | 待写 | |
| ch51 | Ep8: The Bride of Chimotera! (1946) | 2,497 | 待写 | |
| ch52 | Ep8: Son of Chimotera! (1948) | 2,514 | 待写 | |
| ch53 | Ep8: Chimotera! Meets Abbott and Costello (1949) | 2,026 | 待写 | |
| ch54 | Ep8: Chimotera! '99 (1999) | 2,150 | 待写 | |
| ch55 | Ep9: 2:49 a.m. | 1,504 | 待写 | |
| ch56 | Ep9: 2010 | 3,017 | 待写 | |
| ch57 | Ep9: 5:31 a.m. | 1,372 | 待写 | |
| ch58 | Ep9: 2012 | 1,936 | 待写 | |
| ch59 | Ep9: 8:11 a.m. | 2,397 | 待写 | |
| ch60 | Ep9: 2018 | 1,022 | 待写 | |
| ch61 | Ep9: 9:41 a.m.（页码 bleed 避粘连） | 2,328 | 待写 | |
| ch62 | Ep9: 2026 | 610 | 待写 | |
| ch63 | Ep9: 11:51 a.m. | 976 | 待写 | |
| ch64 | Ep9: In the Years to Come… | 716 | 待写 | |
| ch65 | Ep9 末无标题 coda | 582 | 待写 | |
| ch66 | Postscript: The Video Store | 2,135 | 待写 | |
| ch67 | Ep10 Ch1 | 1,767 | 待写 | |
| ch68 | Ep10 Ch2 | 1,632 | 待写 | |
| ch69 | Ep10 Ch3 | 1,369 | 待写 | |
| ch70 | Ep10 Ch4 | 1,635 | 待写 | |
| ch71 | Ep10 Ch5 | 374 | 待写 | |
| ch72 | Ep10 Ch6 | 1,478 | 待写 | |
| ch73 | Ep10 Ch7 | 2,137 | 待写 | |
| ch74 | Ep10 Ch8 | 1,728 | 待写 | |
| ch75 | Ep10 Ch9 | 1,034 | 待写 | |
| ch76 | Ep10 Ch10 | 2,288 | 待写 | |
| ch77 | Ep10 Ch11 | 2,588 | 待写 | |
| ch78 | Postscript: Five Years Later | 3,142 | 待写 | |
| — | 总览三篇（00_概述 / 00_金句精选 / 00_情感节点） | | 待写 | |
| — | T1 自检三件套 | | 待跑 | |
