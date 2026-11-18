# 3-diff · ch20 ned smith（T3 深审 2026-11-18）

R1 来源：子代理盲读（8 条，区间/锚点 100% 验证）；R2：chapter.sh --json rc=0。

## 三单对账

| 单 | 项 | R1/原文 | md | 判 |
|---|---|---|---|---|
| 漏 | 轻微 | R1 提到 woodland 系列图纸当天送 finishing room、Dupont 产能忧心、Madame Charcot 蛋白霜庆祝、Legrand 68 岁创业、儿子入学者授课、Marciac 月集相识、面试者惊骇笑场——md 导航/原句1 上下文与词汇表例句部分承担 | 12 块预算给了双城十二轴 | 提示（不修） |
| 漏 | 无 | 其余 7 条（bursting/慈善大火时尚风险/Mollard 午宴+rosehip/妻子 muslin+血迹/自行车钢架+充气胎/婚姻 contentment/fat one and a Jew+Ned Smith 揭晓+half English）md 全覆盖 | — | 无关键漏 |
| 编 | 无 | — | — | 无编 |
| 错 | 无 | 说话人核：「I am a farmer's daughter」＝Beauclerc 之妻；「Huré was being run by women. Worse, a fat one and a Jew.」＝叙述层（她的知晓）；「Ned Smith」＝Merry 说——md 归对 ✅ | — | 无错 |

## 关键事实回源（R1 ↔ md）

- woodland：text "This was to be their third collection together, for the autumn season"（644:713）↔ md 原句1 ✅
- 慈善大火：text "a fire that had recently engulfed a fashionable charity market"（2797:2859）↔ md 原句3 ✅
- Mollard：text "she who had suggested that they take the Printemps buyer to lunch instead"（3398:3471）↔ md 原句4 ✅
- muslin：text "pressing a ball of muslin hard to her mouth"（4944:4987）↔ md 原句5 ✅
- 自行车：text "Beauclerc was the manager of a business that manufactured bicycles"（6280:6346）↔ md 原句6 ✅
- 婚姻：text "He had assumed matrimony to be a necessary unhappiness"（同段）↔ md 原句7 ✅
- fat one and a Jew：text "Huré was being run by women. Worse, a fat one and a Jew."（11417:11473）↔ md 原句8 ✅
- Ned Smith：text "“Ned Smith,” said Merry."（13848:13872）↔ md 原句9 ✅

## 取证命令示例

/usr/bin/grep -c "If her life had been hollow, it was now bursting." notes/books/novels/odette-rising-by-julianne-edwards/text/ch20_chapter_20.txt → 1；退出码 0
/usr/bin/grep -c "Worse, a fat one and a Jew." notes/books/novels/odette-rising-by-julianne-edwards/text/ch20_chapter_20.txt → 1；退出码 0
