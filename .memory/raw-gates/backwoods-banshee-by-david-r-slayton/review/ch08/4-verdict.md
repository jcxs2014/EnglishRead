# R5 判定表 · ch08

- R1 素读：子代理独立素读 8 条，锚点 100% 命中 text/ch08_chapter_8.txt（先素读后开 md）。**素读条「愿望交换/天使已死之忧」不在 md 内 ⇒ 直接暴露漏尾**。
- R2 机器层：chapter.sh rc=0；块数 12（补尾后；⚠️ 偏离本书常见区间 3–9，理由=漏尾补全，见 3-diff）；fragments 250 片段 MISS 0（含新增段）。
- R3 对账：漏 1（漏尾，已修）/ 编 0 / 错 1（连带交接表述，已修）。
- R4 施事三问：块1 He didn't feel the need（Adam 自述）/块3 They'd captured his snarl（施事 Lost Ones 画者）/块5 the miner said（施事矿工）/块6 Vic said·You took away false hope（施事 Vic，中文一致）/块7 lay the banshee（受事位置句）/块9 one of the strands wrapped around his wrist（施事 strand，中文「缠上了他的手腕」一致）/块10 he asked·The tendril uncoiled（施事 he=Adam；tendril 释放 he）/块11 Vic asked·Adam shuddered（施事各归其位）/块12 Vic asked·he answered（施事对答分明；中文「维森特的回答只有三个词」指 “I'd save you.”，三个词逐字成立）。

| 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|
| 块9 读者提示「ch17 向 Argent 复述、ch22 降灵会再引」 | /usr/bin/grep -rn "door will be opened" text/ → ch08:636,664；ch17:691；ch22:331（退出码 0） | 回指成立（初稿误写 ch29，已当场修正 md 与本行） | 提示（已修） |
| 块10 中文「在此界活不成」 | text/ch08_chapter_8.txt:594 附近 "It can't survive here." | 成立 | 提示（措辞正当） |

## 已核实为正确

- 块1 中文「刀的耳语退了一格」——text/ch08_chapter_8.txt:49 "The whisper of the blade against his skin was more distant"
- 块3 中文「凶手本人站在自己的战利品前」——text/ch08_chapter_8.txt:143 "it looked angry, and fresh"
- 块6 中文「诈骗的破产不构成希望的被窃」——text/ch08_chapter_8.txt:342 附近 "He promised them wishes. You took away false hope, and you saved their lives."
- 新块9 预言四句——text/ch08_chapter_8.txt:636-664 逐字
- 新块12 "I'd save you."——text/ch08_chapter_8.txt:747
- 词汇表 nimbus/desiccated/possessive/translucence/scavenge 例句均在本章 text

以上各项回原文核对成立；后续不得以「读着不对」为由改动，除非给出反证。
