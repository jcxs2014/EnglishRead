# 3-diff · ch16 the english maid（T3 深审 2026-11-18）

R1 来源：子代理盲读（8 条，区间/锚点 100% 验证）；R2：chapter.sh --json rc=0。

## 三单对账

| 单 | 项 | R1/原文 | md | 判 |
|---|---|---|---|---|
| 漏 | 无 | R1 8 条（债付清无音信/Feld 茶请求+insinuate/工厂关门/Beauclerc 家对峙/半薪+Lyons/herons 谎言/Jews 摊牌/英国女仆核弹+掌掴）md 10 块全覆盖 | — | 无漏 |
| 编 | 无 | — | — | 无编 |
| 错 | 无 | 说话人核：「We can't make stockings…」＝Beauclerc；「No, they did not care for herons」＝Beauclerc（谎言）；「I don't think we should be having Jews in our home」＝Dendron；「Twenty-one years of serving you」＝Dendron；「slimed caul」段＝Dendron——md 归对 ✅。数字：twenty-one years（服侍年限）与 half-wages/two weeks/Lyons 逐字 ✅ | — | 无错 |

## 关键事实回源（R1 ↔ md）

- 债付清：text "Berthe's debts had been paid in full, but Odette had heard nothing."（72:139）↔ md nav ✅
- 工厂关门：text "Gates locked. The man said the workers had been sent home."（3183:3241）↔ md 原句2 ✅
- 咆哮：text "All you've done is nearly bankrupt us by not transferring funds"（7838:7906 邻域）↔ md 原句3 ✅
- 半薪/Lyons：text "I have put the workers on half-wages. But for another two weeks only"（7838 邻域）↔ md 原句4 分析 ✅
- herons 谎言：text "No, they did not care for herons," he said."（8445:8488）↔ md 词汇表 intol…（原句5 邻域）✅
- Jews：text "I don't think we should be having Jews in our home."（10871:10922）↔ md 原句8 ✅
- Dreyfus：text "Through his treatment, France had revealed a black heart"（同段）↔ md 原句9 ✅
- 英国女仆：text "the result of your poor father seduced by an English slut, a visiting maid"（13808:13882）↔ md 原句10 ✅

## 取证命令示例

/usr/bin/grep -c "I don't think we should be having Jews in our home" notes/books/novels/odette-rising-by-julianne-edwards/text/ch16_chapter_16.txt → 1；退出码 0
/usr/bin/grep -c "seduced by an English slut, a visiting maid" notes/books/novels/odette-rising-by-julianne-edwards/text/ch16_chapter_16.txt → 1；退出码 0
