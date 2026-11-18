# 3-diff · ch35 the castle on rue des binelles（T3 深审 2026-11-18）

R1 来源：子代理盲读（8 条，区间/锚点 100% 验证）；R2：chapter.sh --json rc=0。

## 三单对账

| 单 | 项 | R1/原文 | md | 判 |
|---|---|---|---|---|
| 漏 | 轻微 | R1 提到儿子一年的消沉（十一岁扛心重）、父丧于夏天/农场已卖/母依姐居、旅馆议论 visionary、圣诞夜菜单（blinis/oysters/champagne/无树/礼物只给小孩与狗）——md nav/原句上下文与词汇表部分承担 | 8 块预算给了归途/城堡/门口/邀请四幕 | 提示（不修） |
| 漏 | 无 | 其余 7 条（unmoored/fripperies 忏悔/fantastical beast+giggle/halo 天使/狼梦安慰/邀请+To return）md 全覆盖 | — | 无关键漏 |
| 编 | 无 | — | — | 无编 |
| 错 | 无 | 说话人核：「Is he a wizard?」＝男孩；「She. This is Mademoiselle Huré’s new house.」＝Beauclerc；「I have nightmares where I suffocate in blood.」＝男孩——md 归对 ✅。数字：eleven-year-old 逐字 ✅ | — | 无错 |

## 关键事实回源（R1 ↔ md）

- unmoored：text "He was unhappy. Unmoored." ↔ md 原句1 ✅
- 忏悔：text "dismissed Odette Huré as a fool" ↔ md 原句2 上下文 ✅
- 怪兽：text "She had built a fantastical beast." ↔ md 原句3 ✅
- 天使：text "She was an otherworldly being, an angel with a bright halo." ↔ md 原句4 ✅
- 狼梦：text "I was sometimes too scared to get out of bed. They stop eventually." ↔ md 原句5 ✅
- 邀请：text "we will have blinis, oysters, and champagne"（6947:7007 邻域）↔ md 原句6 ✅
- To return：text "If she would have him, he would come home."（9399:9441）↔ md 原句7 ✅

## 取证命令示例

/usr/bin/grep -c "She had built a fantastical beast." notes/books/novels/odette-rising-by-julianne-edwards/text/ch35_chapter_35.txt → 1；退出码 0
/usr/bin/grep -c "If she would have him, he would come home." notes/books/novels/odette-rising-by-julianne-edwards/text/ch35_chapter_35.txt → 1；退出码 0
