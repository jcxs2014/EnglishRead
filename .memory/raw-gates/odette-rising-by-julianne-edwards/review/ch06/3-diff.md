# 3-diff · ch06 polo eats the note（T3 深审 2026-11-18）

R1 来源：子代理盲读（8 条，区间/锚点 100% 验证）；R2：chapter.sh --json rc=0。

## 三单对账

| 单 | 项 | R1/原文 | md | 判 |
|---|---|---|---|---|
| 漏 | 轻微 | R1 提到 Beauclerc 家中婚事背景（妻父撮合、Marine 擦铜器、婚后「她偏要看他的脸」）——md 导航人物弧线有「妻子一句安慰都被他当冒犯」覆盖其婚姻线，细节未入精读块 | 取舍理由：6 块预算（短章）让给「谁的事情谁去巴黎」主线 | 提示（不修） |
| 漏 | 轻微 | R1 提到 Odette 吩咐 Dendron「请他回客厅等我」与问 Dendron 马车去向的对话——md 导航「Dendron：incredulous 的传话人」承担，未入精读块 | 同上 | 提示（不修） |
| 漏 | 无 | 其余 6 条（两周无流失但设计断档/以厂货为耻+猴蜥蜴/替她赴巴黎+pro formas/whores+Next time/字条被吃/delinquents 向往）md 全覆盖 | — | 无关键漏 |
| 编 | 无 | — | — | 无编 |
| 错 | 无 | 说话人核：「They are whores.」＝Beauclerc；「Next time, I will come with you.」＝Odette；「the little mouse had eaten it」＝叙述——md 归对 ✅ | — | 无错 |

## 关键事实回源（R1 ↔ md）

- 两周无流失：text "he’d not lost any workers for two weeks"（498:537）↔ md 原句1 上下文 ✅
- 猴与蜥蜴：text "stockings that titillated, designed to the tastes of the fast set in Paris"（986:1060）↔ md 原句2 ✅
- 替她赴巴黎：text "I went on your behalf, mademoiselle. To arrange the orders for the quarter"（5310:5384）↔ md 原句3 ✅
- Next time：text "Next time, I will come with you."（6100:6132）↔ md 原句4 ✅
- 字条被吃：text "the little mouse had eaten it"（6953:6982）↔ md 原句5 ✅
- She did indeed：text "Did she want to see them, these delinquents...? She did indeed."（尾段）↔ md 原句6 ✅

## 取证命令示例

/usr/bin/grep -c "Next time, I will come with you" notes/books/novels/odette-rising-by-julianne-edwards/text/ch06_chapter_6.txt → 1；退出码 0
/usr/bin/grep -c "the little mouse had eaten it" notes/books/novels/odette-rising-by-julianne-edwards/text/ch06_chapter_6.txt → 1；退出码 0
