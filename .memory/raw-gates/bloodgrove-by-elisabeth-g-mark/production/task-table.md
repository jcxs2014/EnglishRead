# 任务表 · Bloodgrove（Elisabeth G. Mark）· novels 言情长篇

- 语料：`text/ch01–ch58`，58 件零偏移（TOC 对齐：Trigger Warning + Ch1–58 + Ack + Also-by）
- 总词数 ~105k；章词数 516–4,088；装置件（titlepage/contents/copyright/maps/dedication/trigger warning/ack/also-by）已剔除；ch58 尾部 end-matter（The End/book2 promo/newsletter）已剥离
- 形态：H1 `# NN. Chapter N`（text/ 首行即 Chapter N）；导航 5 项；子项 4 项；新书块数 2–15
- 批次节奏：约 1 章/次（长篇）；每章 rc=0 立刻 commit（pathspec）；每批 gate.sh 后回填 hash
- 完工定义：全书 + 总览三篇 + T1 自检三件套（t1-verdict.md / t1-candidates.txt / 台账一行）

| 章 | 词数 | 状态 | commit |
|---|---|---|---|
| ch01 | 2152 | 试产 rc=0 | b60fc95d7 |
| ch02 | 2720 | rc=0 | 5d530d1df |
| ch03 | 1987 | rc=0 | d91d4ed54 |
| ch04 | 516 | rc=0 | 4f5fc04d5 |
| ch05 | 1688 | rc=0 | 4a26c6ce4 |
| ch06 | 1141 | rc=0 | c6395b35e |
| ch07 | 2372 | rc=0 | cd8540995 |
| ch08 | 2242 | rc=0 | b78622624 |
| ch09 | 1369 | rc=0 | a776ead8d |
| ch10 | 2091 | rc=0 | 6a037890e |
| ch11 | 1690 | rc=0 | a791acc99 |
| ch12 | 1671 | rc=0 | 45cb8913d |
| ch13 | 1210 | rc=0 | 5ab8f3056 |
| ch14 | 1487 | rc=0 | 0794b0b48 |
| ch15 | 1090 | rc=0 | 26aedae57 |
| ch16 | 2091 | rc=0 | 4a5043364 |
| ch17 | 2722 | rc=0 | 8a01d4172 |
| ch18 | 1100 | rc=0 | ebceda289 |
| ch19 | 663 | rc=0 | d98be44c8 |
| ch20 | 1651 | rc=0 | 3b79b3acc |
| ch21 | 2254 | rc=0 | 1ad10544c |
| ch22 | 1196 | rc=0 | 55a049f33→267f2533a |
| ch23 | 1678 | rc=0 | 89bb04fca→3e26862c5 |
| ch24 | 996 | rc=0 | 009867bd2 |
| ch25 | 1125 | rc=0 | 89d266451 |
| ch26 | 2459 | rc=0 | 5cc0845d6 |
| ch27 | 3476 | rc=0 | 6d308bf5a |
| ch28–ch58 | — | 进行中 | |

**批次收口 3（ch19–27）**：gate EXIT=0（vocab FAIL=0、拼接 0、405 块逐字）。整改：虚构词条（attestation/sulking/templated→真实词形）、跨章例句（ch22 demo、ch24 hesitation）、ch20/21/26 拼接红线（片段连续化）。**词表教训：例句须整段收尾且无弯直撇号混用，例句中的所有格一律照抄原文弯撇号。** 露骨章（ch26/27）引语选段避写器官细节，以对白与姿态承载弧线。

**批次收口 1（ch01–05）**：gate 无内容阻断；素读 100% 命中。
**批次收口 2（ch06–18）**：gate EXIT=0（vocab FAIL=0、structure 阻断 0、206/206 逐字）。整改 3 轮：ch02 关键词不在本块引语 / ch10、ch14、ch17 共 6 处跨段拼接红线（片段须原文连续）/ ch12 gutter 例句跨章错挂。教训：①块内多 `>` 片段必须在原文中字符连续（间隔句子/段落即红）；②写 vocab 例句必须当场 grep 本章。
