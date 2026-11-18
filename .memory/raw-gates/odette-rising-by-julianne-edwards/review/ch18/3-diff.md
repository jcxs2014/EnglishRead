# 3-diff · ch18 the rabbit pies（T3 深审 2026-11-18）

R1 来源：子代理盲读（8 条，区间/锚点 100% 验证）；R2：chapter.sh --json rc=0。

## 三单对账

| 单 | 项 | R1/原文 | md | 判 |
|---|---|---|---|---|
| 漏 | 无 | R1 8 条（额肿+Polo 安然/名册上没有她/被擦洗/三天份馅饼/厨房礼数/疤亮如腿疤/裂碗自判+Berthe 来过/herons 真相+夫妻戏）md 8 块全覆盖 | — | 无漏 |
| 编 | 无 | — | — | 无编 |
| 错 | 无 | 说话人核：「My mother is here」＝Merry；「It was Madame Marie-Sainte’s doing」＝Merry；「She’s deranged」＝Beauclerc；「You need each other」＝Beauclerc 之妻——md 归对 ✅ | — | 无错 |

## 关键事实回源（R1 ↔ md）

- 醒来清点：text "a large lump on her forehead, pain across her temples, and sores on her buttocks"（232:312）↔ md 原句1 上下文 ✅
- 名册：text "He had not mentioned her."（1567:1641 邻域）↔ md 原句2 ✅
- 擦洗：text "Someone had seen her bare flesh, had rolled her over, had scrubbed"（2809:2875）↔ md 原句3 ✅
- 馅饼：text "The others are for Friday and Saturday."（5409:5475）↔ md 原句4 ✅
- 厨房礼数：text "to eat in the kitchen was against some rule of etiquette"（7490 邻域）↔ md 原句5 ✅
- 疤亮：text "the scars of their disdain were as bright as those on her thighs"（9099:9170 邻域）↔ md 原句6 ✅
- 裂碗：text "a cracked bowl in this porcelain town, and be grateful for what she had"（9099:9170）↔ md 原句7 ✅
- herons 真相：text "the truth about the herons: that they might indeed have been a good idea."（10710:10783）↔ md 原句8 ✅

## 取证命令示例

/usr/bin/grep -c "It was Madame Marie-Sainte’s doing" notes/books/novels/odette-rising-by-julianne-edwards/text/ch18_chapter_18.txt → 1；退出码 0
/usr/bin/grep -c "a cracked bowl in this porcelain town" notes/books/novels/odette-rising-by-julianne-edwards/text/ch18_chapter_18.txt → 1；退出码 0
