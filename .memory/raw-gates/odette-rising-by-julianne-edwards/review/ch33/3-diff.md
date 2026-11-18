# 3-diff · ch33 living death（T3 深审 2026-11-18）

R1 来源：子代理盲读（8 条，区间/锚点 100% 验证）；R2：chapter.sh --json rc=0。

## 三单对账

| 单 | 项 | R1/原文 | md | 判 |
|---|---|---|---|---|
| 漏 | 轻微 | R1 提到 Louis 谈 Berthe「袭击＋马的意外」心事重重（他不知马伤真相）、别再封闭自己——md 原句3 上下文承担（Louis 提议歌剧） | 4 块预算（短章）给了动工/设计/包厢/泥陷四拍 | 提示（不修） |
| 漏 | 无 | 其余 7 条（水涝地基/锻铁铜绿/百合壁灯+海仙女/private box/Gagnon 城市/泥陷/living death）md 全覆盖 | — | 无关键漏 |
| 编 | 无 | — | — | 无编 |
| 错 | 无 | 说话人核：「We’re going to use wrought iron…」＝Louis；「I would like to design wall sconces…」＝Odette；「I would get a box. A private box.」＝Louis——md 归对 ✅ | — | 无错 |

## 关键事实回源（R1 ↔ md）

- 水涝地基：text "The foundations had been dug despite the waterlogged ground"（31:90）↔ md 原句1 ✅
- 铜绿：text "We’ll paint them with weathered brass to get a verdigris finish."（524:595）↔ md 原句2 ✅
- 百合壁灯：text "shaped to look like lilies growing from the walls"（884:933）↔ md 词汇表 sconces 例句 ✅
- private box：text "I would get a box. A private box."（2656:2689）↔ md 原句3 ✅
- Gagnon 城市：text "It seemed as if it belonged to Gagnon."（2156:2194）↔ md suread 事实（1-suread.json）✅
- 泥陷：text "her shoe shot out and she toppled backward into the mire"（3657:3713）↔ md 原句4 ✅
- living death：text "she could not survive the knowledge of what she’d done to Merry"（3798:3861）↔ md 原句4 ✅

## 取证命令示例

/usr/bin/grep -c "It seemed as if it belonged to Gagnon." notes/books/novels/odette-rising-by-julianne-edwards/text/ch33_chapter_33.txt → 1；退出码 0
/usr/bin/grep -c "a kind of living death" notes/books/novels/odette-rising-by-julianne-edwards/text/ch33_chapter_33.txt → 1；退出码 0
