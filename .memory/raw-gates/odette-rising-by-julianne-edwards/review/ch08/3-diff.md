# 3-diff · ch08 the golden city（T3 深审 2026-11-18）

R1 来源：子代理盲读（8 条，区间/锚点 100% 验证）；R2：chapter.sh --json rc=0。

## 三单对账

| 单 | 项 | R1/原文 | md | 判 |
|---|---|---|---|---|
| 漏 | 轻微 | R1 提到 Beauclerc 咖啡馆候场视角（邻桌 couple 十一点喝 absinthe、买手之约 twelve 点、掂量她 "Just twenty-one"、百货店 "Temples to excess"、"feed the beast"）——md 未设此块 | 取舍理由：12 块预算给到「她」的完整行程；Beauclerc 视角在 ch12/16/22 各有专块承接 | 提示（不修） |
| 漏 | 无 | 其余 7 条（corset 求助/首次离 Sèvres/乞丐嘲弄/Emile-Edouard 纠正+exceptional 讥讽/beginning of my life+Finally alive/Feld 大衣赠 Merry/衣柜分发+undertaker 疑伤）md 全覆盖 | — | 无关键漏 |
| 编 | 无 | — | — | 无编 |
| 错 | 无 | 说话人核：乞丐台词＝乞丐；「poor Emile」＝买手；纠正「Edouard」＝Beauclerc；「They are whores」→ch06 已核；宣言＝Odette——md 归对 ✅。日期数：eleven o'clock/twelve/Just twenty-one 均在 Beauclerc 咖啡馆段（未引，无冲突）✅ | — | 无错 |

## 关键事实回源（R1 ↔ md）

- corset 求助：text "“I need assistance. Help with the fastenings,” ventured Odette."（1586:1649）↔ md 原句1 ✅
- 首次离城：text "She was leaving Sèvres for the first time."（3139:3181）↔ md 原句2 上下文 ✅
- 乞丐：text "“A sous for a starving soldier, lady?”"（7722:7760）↔ md 原句3 ✅
- Edouard 纠正：text "“Edouard,” said Beauclerc. “He was Edouard Huré.”"（14492:14541）↔ md 原句6 上下文（droll fellow 块邻域）✅
- beginning of my life：text "this day might be the beginning of my life."（16635:16678）↔ md 原句7 ✅
- Finally alive：text "I am feeling. I feel alive. Finally alive."（同段尾）↔ md 原句9 ✅
- 大衣：text "pulled out a long gray wool coat, with gleaming brass buttons"（22882:22943）↔ md 原句11 ✅
- undertaker 疑伤：text "Secret scars that he took to his grave?"（23729:23776 邻域）↔ md 原句12 ✅

## 取证命令示例

/usr/bin/grep -c "this day might be the beginning of my life" notes/books/novels/odette-rising-by-julianne-edwards/text/ch08_chapter_8.txt → 1；退出码 0
/usr/bin/grep -c "He was Edouard Huré" notes/books/novels/odette-rising-by-julianne-edwards/text/ch08_chapter_8.txt → 1；退出码 0
