# 3-diff · ch36 here at last was her life（T3 深审 2026-11-18）

R1 来源：子代理盲读（8 条，区间/锚点 100% 验证）；R2：chapter.sh --json rc=0。

## 三单对账

| 单 | 项 | R1/原文 | md | 判 |
|---|---|---|---|---|
| 漏 | 轻微 | R1 提到 poker in honor of Berthe（小 Joseph bluffing）、Le Neptune undertow 回忆、望城全景——md nav（poker）/词汇表 undertow 例句承担 | 6 块预算（短章）给了补叙/信物/原谅/终句 | 提示（不修） |
| 漏 | 无 | 其余 7 条（truce/一枪穿心/magnificent flit+带蛇/Merry Christmas 卡/forgiven evaporated/Here at last）md 全覆盖 | — | 无关键漏 |
| 编 | 无 | — | — | 无编 |
| 错 | 无 | 说话人/叙述核：「She had shot Victor Gagnon.」＝叙述补叙（主语 Berthe）；「Here, at last, was her life.」＝叙述——md 归对 ✅。⚠️ R1 子代理把 truce 句的「beautiful pieces」转述为「漂亮瓷器」——md 无此错（md 分析作「美的作品」），属 R1 转述偏差，记录备查 | — | 无错 |

## 关键事实回源（R1 ↔ md）

- truce：text "For the workers in the factory, who had settled into a kind of truce with her"（140:212 邻域）↔ md 原句1 ✅
- 一枪穿心：text "A single bullet through the heart."（1308:1370）↔ md 原句2 ✅
- 潜逃：text "slipping out to a carriage via the back stairs, while Louis waited outside"（1588:1662）↔ md 原句3 ✅
- Merry 卡：text "“Merry Christmas” written carefully underneath"（2459:2506）↔ md 原句4 ✅
- 原谅：text "Her shame had evaporated in the heat of her happiness."（3467 邻域）↔ md 原句5 ✅
- 终句：text "Here, at last, was her life."（3467:3495）↔ md 原句6 ✅

## 取证命令示例

/usr/bin/grep -c "Here, at last, was her life." notes/books/novels/odette-rising-by-julianne-edwards/text/ch36_chapter_36.txt → 1；退出码 0
/usr/bin/grep -c "A single bullet through the heart." notes/books/novels/odette-rising-by-julianne-edwards/text/ch36_chapter_36.txt → 1；退出码 0
