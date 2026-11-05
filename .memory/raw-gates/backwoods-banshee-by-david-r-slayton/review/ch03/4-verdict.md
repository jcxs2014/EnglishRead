# R5 判定表 · ch03

- R1 素读：子代理独立素读 8 条，7 条一次命中；1 条（displacement）锚点首词误抄，回原文本章 :355 纠正后 8/8 全命中（先素读后开 md；md 无此错）。
- R2 机器层：chapter.sh rc=0；块数 6（建议 4–7）；fragments MISS 0。
- R3 对账：漏 0（2 提示取舍）/ 编 0 / 错 0（1 处为素读锚点笔误，非 md 缺陷）。
- R4 施事三问：块1 Juan had dropped a wrench（施事 Juan，中文「Juan 掉了把扳手」一致）/块3 A nurse was talking to him（施事 nurse，中文「护士在同他说话」一致）/块4 The man's spirit had been ripped out（受事 spirit，中文「灵魂被扯走」方向一致）/块5 Bobby made a nervous expression（施事 Bobby）/块6 Dautre had figured out smartphones（施事 Dautre）。

| 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|
| 读者提示「六名患者由此与 ch01 的灾难对上账」 | text/ch03_chapter_3.txt:268 "We have five more just like him." | Tristan+5=6，与 ch01 受害集合一致 | 提示（措辞正当） |
| 一句话总结「六名患者睁眼空壳」 | 同上 | 计数成立 | 提示（措辞正当） |

## 已核实为正确

- 块1 读者提示「数到五的自救」——text/ch03_chapter_3.txt:31 "he counted backward from five"
- 块2 中文「自旅馆 Erythraean 事件以来一直是他的避难所」——text/ch03_chapter_3.txt:52 "had been his escape since the events at the Hotel Erythraean"
- 块4 读者提示引 "The Underworld?"——text/ch03_chapter_3.txt:417
- 块6 读者提示引 "Would you like to watch a film?"——text/ch03_chapter_3.txt:528
- 词汇表「weird cases」例句——text/ch03_chapter_3.txt:470 "I catch all the weird cases."

以上各项回原文核对成立；后续不得以「读着不对」为由改动，除非给出反证。
