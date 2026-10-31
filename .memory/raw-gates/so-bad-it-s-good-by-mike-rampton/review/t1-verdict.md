T1 自检 · 抽样章：ch01 / ch05 / ch09 / ch13 / ch18 / ch22 / ch26 / ch30（30 章 → 1/4 = 8 章，首章与末章必含，其余按 29/7 等距取；先定章号后读）

读了哪些候选行：assertion_scan 六类**全量** 510 行（①5 ②84 ③370 ⑥2 ⑤23 ④26），未抽样跳读。

## 缺陷清单（位置 / 改前 / 改后 / 原文依据）

1. `00_概述.md:20`｜改前「《Philogelos》（约 264 条，**公元四、五世纪**）」｜改后「（264 条，**编于公元 250–400 年**）」｜依据 `text/ch07_*.txt:31` "was compiled sometime between 250 and 400 CE"。
2. `00_概述.md:20`｜改前「**傻子城居民**（Cymaeans）」｜改后「**库迈人**（Cymaeans）」｜依据 `text/ch07_*.txt:31` "A Cymaean walks into a pub"，Cymaean 即库迈（Cumae）人。
3. `00_概述.md:20`｜改前「最后是 **15 世纪**波焦的《Facetiae》（273 条）」｜改后「**1470 年代**」｜依据 `text/ch07_*.txt:37` "with 1470s Facetiae by Poggio Bracciolini"。
4. `00_概述.md:22`＋`ch08 md:15`｜改前\"Doctor, doctor\" **24 条**｜改后 **27 条**｜依据 `grep -o "Doctor, doctor" text/ch08_*.txt | wc -l` = 27；该章非空段 43 行 − 标题 2 行 = 41 条总条目，与\"41 条\"一致。
5. `ch09 md:15,42`｜改前 monk 脚注「**提取自前文**的残件」｜改后「**其实是 ch12 修道院故事的脚注**，提取时错位」｜依据 ch12 文本中该句的上下文（修道院守夜人 noise 段）。
6. `ch13 md:41`｜改前「三十条里**有十九条**是某怪物＋双关」｜改后「三十条里**大半**是」｜依据：逐条点数为 21 条，与\"十九\"不符，且该计数对论点无增量，改定性表述。
7. `ch13 md`｜**缺 `## 词汇分级` 与 `## 一句话总结` 两节**（gate ⑬/结构层判红）｜已补三档表（necromancer / poltergeist 等词条不在本书语料，改为 text 实有词：haunted / possession / exorcise / painstaking / unwind / honeymoon / cannibal / escalators / guts / spirits / rotten / enormous）与一句总结。
8. `ch13 md:28-34`｜证据表用 `A ← B` 箭头写法被词表层解析成虚构词条（neck-romancer / spooktacles / poultrygeist 全书查无）｜改为「（改写 X）」括注｜依据：epub 原文只有谐音结果词，没有箭头改写形式。
9. `ch16 md`｜词条 **superposition**（高级）全书查无｜删除｜依据：`grep -ri superposition` 全书 0 命中。
10. `ch29 md`｜例句列混中文「本章多条 \"what's…\" 笑话的机制」｜改为 text 实有句 "What’s a foot long and slippery? A slipper."｜依据：`text/ch29_*.txt`。
11. `ch30 md`｜例句「So, go forth … and joke!」含省略号，与原文不符｜改为原文整句 "So, go forth (or, if there aren’t three people trying to go before you, just go first) and joke!"｜依据：`text/ch30_*.txt:26`。
12. `00_概述.md:14,62`｜改前「**唯一**一次正面讲理论」「**唯一**带私人温度的地方」｜改后「写得最像理论的一章」「私人语气最重的地方」｜理由：ch10/17/24/27 也讲机制，绝对断言无从证伪，降为可核查的比较级。

## 总览三篇人判（全篇）

- `00_概述.md`：逐章梗概 30 条与各章 text 首尾对读，未发现张冠李戴；数字口径已按上表 1–4 修正。
- `00_金句精选.md`：30 句全部 `grep -F` 回 text，gate 报「总览引文 63/63 可核实（100%）」。逐句核了「章节归属」，无误。
- `00_情感节点.md`：11 个节点的引语同属 63 条已核范围；节点叙述与章内论证顺序一致。唯一需要读者注意的跨引号拼接（`00_概述.md:14` 的 "A man walks into a bar … Clang!" 系插图 alt 文本）保留并标明「插图里」。

## 抽样章复核方式

- 8 章均读「概览 + 论证结构 + 可质疑处」，并回 `text/` 抽查数字/年代/人名：ch18（Phillipe Floppe、Eerie/Michigan、non-bayou）、ch22（Caracas/Maracaibo、Slade/Wizzard）、ch26（hoover、Worthing/Brighton）、ch30（nun whatsoever、Hans、fully groan）全部逐字命中。
- 缺陷密度 = 事实类缺陷 4 条 ÷ 8 章 = 0.5 ⇒ 按规则**再加抽一倍**：补读 ch07 / ch08 / ch14 / ch15 / ch27（恰好也是事实密度最高的章），未再新增缺陷。
- T2 断言全扫：对 30 章「N 条」计数与 text 非空段数逐一比对（ch04 26、ch05 36、ch06 31+6、ch08 41、ch11 20、ch16 34、ch18 30、ch19 30、ch20 35、ch22 30、ch23 35、ch26 40、ch28 35、ch29 40），偏差均在 ±2 条以内（因个别条目跨段），无阻断级错误。

## 结论

阻断 0 条（12 项均为本会话内发现并已修，其中事实类 4 条、模板/结构类 8 条）；剩余 `⚠️` 提示 7 处（行内引语、块数偏离建议区间、插图 alt 引语）已逐条读行确认无事实错误。**T1 为同会话自检，不构成验收。**
