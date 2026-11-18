# 3-diff · ch34 light your lamp（T3 深审 2026-11-18）

R1 来源：子代理盲读（8 条，区间/锚点 100% 验证）；R2：chapter.sh --json rc=0。

## 三单对账

| 单 | 项 | R1/原文 | md | 判 |
|---|---|---|---|---|
| 漏 | 轻微 | R1 提到纽扣赌局、Cinderella 提议被拒、帝国包厢 commandeered、两千红丝绒座/four tiers、Comédie-Française 细节——md nav/词汇表外围承担（tiers 例句在词汇表） | 11 块预算给了告别式/信/接人三幕 | 提示（不修） |
| 漏 | 无 | 其余 7 条（leave-taking/盛装/合唱 wall+Laudi 泪/benediction/lioness 信/parting gift+救 Grace+light lamp/Gagnon dead+接 Merry no look-back）md 全覆盖 | — | 无关键漏 |
| 编 | 无 | — | — | 无编 |
| 错 | 无 | 说话人核：「You are a lioness」＝信（Berthe）；「Victor Gagnon is dead」＝Louis；「It has cost you too much」＝信——md 归对 ✅ | — | 无错 |

## 关键事实回源（R1 ↔ md）

- leave-taking：text "This, Odette, is the leave-taking of a colossus." ↔ md 原句1 ✅
- 盛装：text "strings of pearls pouring down her bodice, a thick rope of them around her neck" ↔ md 原句2 上下文（caryatids 块）✅
- Laudi：text "It was sung by just four women, without any instruments" ↔ md 原句5 ✅
- 信：text "You are a lioness and the most bravehearted woman I know." ↔ md 原句7 上下文 ✅
- parting gift：text "I have acted: one parting gift for this life, this city."（R1 邻域）↔ md suread 事实（1-suread.json）✅
- light lamp：text "Light your lamp, Odette. It's time." ↔ md 导航与金句 ㉔ 引语（金句卷）✅
- Gagnon dead：text "Victor Gagnon is dead." ↔ md suread 事实（1-suread.json）✅
- no look-back：text "He did not look back." ↔ md 原句11 上下文（hang in space 块）✅

## 取证命令示例

/usr/bin/grep -c "Light your lamp, Odette. It's time." notes/books/novels/odette-rising-by-julianne-edwards/text/ch34_chapter_34.txt → 1；退出码 0
/usr/bin/grep -c "Victor Gagnon is dead." notes/books/novels/odette-rising-by-julianne-edwards/text/ch34_chapter_34.txt → 1；退出码 0
