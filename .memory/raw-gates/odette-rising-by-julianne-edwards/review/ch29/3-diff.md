# 3-diff · ch29 two christmases（T3 深审 2026-11-18）

R1 来源：子代理盲读（8 条，区间/锚点 100% 验证）；R2：chapter.sh --json rc=0。

## 三单对账

| 单 | 项 | R1/原文 | md | 判 |
|---|---|---|---|---|
| 漏 | 轻微 | R1 提到 midnight mass 回忆、sufganiyots/Gretchens、bûche 菜单、枕下礼物——md nav「Sufganiyots 与 Gretchens」「枕下礼物」承担；菜单未入精读块（词汇表 dauphinoise 例句承载鹅与土豆） | 6 块预算（短章）给了两城对照四拍 | 提示（不修） |
| 漏 | 无 | 其余 7 条（雪 Lille 无雪橇/寒酸礼物铃铛套鞋/农家不许哭/僵硬拥抱/first Christmas+last/heavy square house/castle 图纸近成）md 全覆盖 | — | 无关键漏 |
| 编 | 无 | — | — | 无编 |
| 错 | 无 | 说话人核：「Do we have to have dinner, Papa?」＝儿子；「Christmas is Christmas」＝Beauclerc；「We will soon be safe in my castle」＝Odette——md 归对 ✅ | — | 无错 |

## 关键事实回源（R1 ↔ md）

- 雪/无雪橇：text "It was snowing in Lille, but Beauclerc and his boy hardly noticed."（5:71）↔ md 原句1 上下文 ✅
- 礼物：text "He had got him a new bell for his bicycle and a pair of rubber galoshes"（1349:1420）↔ md 原句2 ✅
- 抱起：text "he strode over to the crumpled child and lifted him in his arms."（2914:2978）↔ md 原句3 ✅
- first Christmas：text "the first Christmas she had spent with others, and it would be the last"（4935:5006）↔ md 原句5 ✅
- castle：text "We will soon be safe in my castle"（4935:5006 邻域）↔ md 原句6 ✅

## 取证命令示例

/usr/bin/grep -c "a pair of rubber galoshes" notes/books/novels/odette-rising-by-julianne-edwards/text/ch29_chapter_29.txt → 1；退出码 0
/usr/bin/grep -c "We will soon be safe in my castle" notes/books/novels/odette-rising-by-julianne-edwards/text/ch29_chapter_29.txt → 1；退出码 0
