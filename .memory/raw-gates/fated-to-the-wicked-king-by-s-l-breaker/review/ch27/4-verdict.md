# ch27 判定表（R4）

| # | 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|---|
| 1 | 原句1 记忆回灌 | text/ch27:31 | 一致 | — |
| 2 | 原句2 Eleanor 的「滑坡」逻辑 | text/ch27:55 | 一致 | — |
| 3 | 原句3 她认下全部罪 | text/ch27:160 | 一致 | — |
| 4 | 原句4 他要她留下 | text/ch27:169 | 一致 | — |
| 5 | 原句5 General 闯入 | text/ch27:187 | 一致 | — |
| 6 | 原句6 她质问他独自启动机器 | text/ch27:217 | 一致 | — |
| 7 | 原句7 冻住 General、子弹悬停 | text/ch27:289 区间 | 一致 | — |
| 8 | 原句8 午夜潮汐会抽干 Wünder | text/ch27:361 区间 | 一致 | — |
| 9 | 原句9 设过载 | text/ch27:379 | 一致 | — |
| 10 | 原句10 不能再自私 | text/ch27:391 | 一致 | — |
| 11 | 原句11 最后回望 | text/ch27:415 | 一致 | — |
| 12 | 原句12 他攥护身符起跳 | text/ch27:489 | 一致 | — |
| 13 | 原句13 Chez 收尾 | text/ch27:531 | 一致 | — |
| 14 | 「No cage will hold you…」未入 md | text/ch27:148 | 缺失 | **阻断（已修）** |
| 15 | 「you would have made a fine queen」未入 md | text/ch27:409 | 缺失 | **阻断（已修）** |
| 16 | 块序 13 块偏移递增 | 2-machine.json | 递增 | — |

## 已核实为正确（防误修）

1. **「would have made」是虚拟语气**：`text/ch27:409`——**不是**「你将会是王后」；改写必须保留「本可以」。
2. **手枪是 General 从原世界带来的**：`text/ch27:235` 区间 md 已写对；Wünder 本土无此类武器。
3. **护身符是 General 掉落的**：`text/ch27:486` 区间——不是国王自己的东西。
4. **钟面裂开坠落**：`text/ch27:500` 区间；`text/ch27:457` 章末的钟声停在 ch26，本章是钟楼被炸——两处不可混。
5. **正文边界**：`/usr/bin/grep -n "Thank you so much for reading" text/ch27_twenty_seven_jump.txt` → 539，exit 0；539 起全部非正文。
