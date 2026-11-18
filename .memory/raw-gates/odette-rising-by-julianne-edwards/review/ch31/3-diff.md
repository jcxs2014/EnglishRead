# 3-diff · ch31 the stake in napoleon（T3 深审 2026-11-18）

R1 来源：子代理盲读（8 条，区间/锚点 100% 验证）；R2：chapter.sh --json rc=0。

## 三单对账

| 单 | 项 | R1/原文 | md | 判 |
|---|---|---|---|---|
| 漏 | 轻微 | R1 提到 Dupont 焦急打听小姐何时回厂、两份不宜应征、Louis 不解新宅冷落——md nav/原句3 上下文部分承担 | 10 块预算给了追童/两难/夜袭/解雇四幕 | 提示（不修） |
| 漏 | 无 | 其余 7 条（钱付无音信/Eugénie 被追/defiance 引用/木桩钉马/Gagnon 之人判定/必须停止/假解雇+footman/Polo 转赠）md 全覆盖 | — | 无关键漏 |
| 编 | 无 | — | — | 无编 |
| 错 | 无 | 说话人核：「No, we love it here, with you」＝Arielle；「It is not your choice」＝Odette；「May God keep them safe」＝她内心——md 归对 ✅ | — | 无错 |

## 关键事实回源（R1 ↔ md）

- 二月末猎屋：text "At the end of February, the household had moved into an old hunting lodge"（5:78）↔ md nav「二月末迁入 Saint-Cloud 猎舍」✅
- 钱付无音信：text "She had sent the money but had heard nothing"（313:389）↔ md 原句1 上下文（suread）✅
- Eugénie 被追：text "a man was standing at the bottom of the garden. A frightening man."（1642:1708）↔ md 原句1 ✅
- 木桩：text "she saw the wooden stake protruding from the flank"（8444:8494）↔ md 原句4 ✅
- footman：text "I have arranged a position for you as a footman in a house in Paris."（11846:11914）↔ md 原句7 ✅
- Polo 转赠：text "took out Polo, who sat on her hand, nose up, whiskers twitching"（13904:13967）↔ md 原句9 ✅

## 取证命令示例

/usr/bin/grep -c "a man was standing at the bottom of the garden" notes/books/novels/odette-rising-by-julianne-edwards/text/ch31_chapter_31.txt → 1；退出码 0
/usr/bin/grep -c "I have arranged a position for you as a footman" notes/books/novels/odette-rising-by-julianne-edwards/text/ch31_chapter_31.txt → 1；退出码 0
