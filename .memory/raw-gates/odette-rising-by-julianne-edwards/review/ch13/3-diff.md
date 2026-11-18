# 3-diff · ch13 le neptune（T3 深审 2026-11-18）

R1 来源：主会话现读补做（子代理配额失败；先 text 后 md）＋生产期 suread。R2：chapter.sh --json rc=0。

## 三单对账

| 单 | 项 | R1/原文 | md | 判 |
|---|---|---|---|---|
| 漏 | 轻微 | 门房盘问、独坐半小时、Comte de Mâcon 名片、买手催单等外围事件——md 导航/原句1 上下文承担，未入精读块 | 块预算给了 14 个核心块 | 提示（不修） |
| 编 | 无 | — | — | 无编 |
| 错 | 无 | 说话人核：「You are here.」＝Berthe；「here's a truth: you are living in my father's house」＝Odette；「The law has no eyes」＝Berthe；「stolen their hope」转述方向＝Gagnon 偷走希望——md 归对 ✅ | — | 无错 |

## 关键事实回源（R1 ↔ md）

- 焦糖落座：text "she lowered herself, like poured caramel, into her chair." ↔ md 原句3 ✅
- 以真相回敬：text "here’s a truth: you are living in my father’s house." ↔ md 原句4 ✅
- 法律无眼：text "The law has no eyes. It is blind." ↔ md 原句5 分析（「几句话之前她刚说」同章定位 ✅）
- 债单：text "She read the columns and saw that along with costs for coal, new roof tiles..." ↔ md 原句10 ✅
- 烟蒂：text "She stubbed out a cigarette in Odette’s salad" ↔ md 原句12 ✅
- 匿名付账：text "“The gentleman wishes not to be known.”" ↔ md 原句13 上下文＋导航 ✅

## 取证命令示例

/usr/bin/grep -c "like poured caramel" notes/books/novels/odette-rising-by-julianne-edwards/text/ch13_chapter_13.txt → 1；退出码 0
/usr/bin/grep -c "The gentleman wishes not to be known" notes/books/novels/odette-rising-by-julianne-edwards/text/ch13_chapter_13.txt → 1；退出码 0
