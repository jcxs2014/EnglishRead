# 3-diff · ch21 the pig shed（T3 深审 2026-11-18）

R1 来源：子代理盲读（8 条，区间/锚点 100% 验证）；R2：chapter.sh --json rc=0。

## 三单对账

| 单 | 项 | R1/原文 | md | 判 |
|---|---|---|---|---|
| 漏 | 轻微 | R1 提到 Corot 路费「亲手交到她本人手里」、Dupont 预先叫 Corot 保密、Charcot 把「Ned 认识 Odette 的母亲」误听为 Madame Huré——md 导航/原句5 上下文部分承担（保密与误听在 nav 与词汇表外围） | 13 块预算给了偷窃案→罢工→备战三幕 | 提示（不修） |
| 漏 | 无 | 其余 7 条（猪棚/巨人肩自嘲/带薪养病裁决/付钱让她好起来/罢工威胁/bon-bon 正义/半周工资奖金+演讲恐惧/马厩落泪+Ned 认母/obese 22/两块石头）md 全覆盖 | — | 无关键漏 |
| 编 | 无 | — | — | 无编 |
| 错 | 无 | 说话人核：「It's Madame Corot」＝Dupont；「I will pay her to get better」＝Odette；「Strike. Threatening to strike.」＝Dupont；「They stop eventually」＝Odette——md 归对 ✅ | — | 无错 |

## 关键事实回源（R1 ↔ md）

- 猪棚：text "she had enough in her pig shed to start her own factory"（3015:3070）↔ md 原句1 ✅
- 带薪养病：text "I will continue to pay her wages until she is well enough to return"（6985:7052）↔ md 原句3 ✅
- 路费：text "Give her the cost of the journey."（8582:8615）↔ md suread 事实（1-suread.json）✅
- 罢工：text "Strike. Threatening to strike. Even."（10498:10534）↔ md 原句5 上下文（suread 事实）✅
- bon-bon 正义：text "she doesn’t need bon-bons in order to feel that justice has been served."（10498 邻域）↔ md 原句6 ✅
- 半周工资：text "Equivalent to half a week’s wages."（13475:13509）↔ md 原句7 ✅
- 认母：text "“The one before you were born.”"（19309:19340）↔ md 原句10 上下文 ✅
- 两块石头：text "two stones, just large enough to fit into the palms of her hands"（20871:20913）↔ md 原句13 ✅

## 取证命令示例

/usr/bin/grep -c "pig shed to start her own factory" notes/books/novels/odette-rising-by-julianne-edwards/text/ch21_chapter_21.txt → 1；退出码 0
/usr/bin/grep -c "Equivalent to half a week’s wages" notes/books/novels/odette-rising-by-julianne-edwards/text/ch21_chapter_21.txt → 1；退出码 0
