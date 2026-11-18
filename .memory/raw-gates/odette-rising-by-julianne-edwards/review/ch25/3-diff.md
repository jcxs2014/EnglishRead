# 3-diff · ch25 the burning chrysanthemum（T3 深审 2026-11-18）

R1 来源：子代理盲读（8 条，区间/锚点 100% 验证）；R2：chapter.sh --json rc=0。

## 三单对账

| 单 | 项 | R1/原文 | md | 判 |
|---|---|---|---|---|
| 漏 | 轻微 | R1 提到警察局长 Lallement 派人、Armand Martin 看守烟花却醉跳吉格舞、Arielle 携子女将被拦截、警察仅三名转救火、Louis 勘灾+Victor Horta 引荐——md nav/原句上下文部分承担（Martin 跳舞在原句5 邻域未引；Horta 未提） | 12 块预算给了 riot→fire→razor→rebuild 四幕主轴 | 提示（不修） |
| 漏 | 无 | 其余 7 条（斗殴群殴/锁厂/圣所/菊花烟花/火箭穿窗+画稿同焚+Polo 坠落/Ned 拖救+救活 Polo/象牙剃刀+恨屋/不该让 Beauclerc 走+重建）md 全覆盖 | — | 无关键漏 |
| 编 | 无 | — | — | 无编 |
| 错 | 无 | 说话人核：「The police chief…」＝Dupont；「Her sleeve caught」＝ch07（不涉）；「No, madame, I’m not sure I have」＝ch19（不涉）；扫落样品＝ch07（不涉）——本章说话人：「What has happened?」＝Odette；「We can’t make stockings」＝ch16（不涉）——本章 md 归对 ✅ | — | 无错 |

## 关键事实回源（R1 ↔ md）

- 群殴：text "A fight had broken out near the stone arch"（169:211）↔ md 原句1 ✅
- 锁厂：text "throwing the bolt on the outside and locking it"（3617:3681 邻域）↔ md 原句2 ✅
- 圣所：text "the girl breaching her father’s sanctuary"（视段）↔ md 原句3 ✅
- 菊花：text "like a vast, burning chrysanthemum"（8896:8955 邻域）↔ md 原句4 ✅
- 火箭穿窗：text "the rocket smashed through the window, sending glass flying"（8896:8955）↔ md 原句5 上下文＋词汇表 skittered 例句 ✅
- Polo 坠落：text "felt Polo fly, watching the blur of his little body fall to the burning floor"（视段）↔ md 原句7 ✅
- 剃刀：text "The ivory handle of the razor in her hand felt warm and smooth."（16472:16535）↔ md 原句10 ✅
- 重建：text "I will start anew. I want something that is exciting and modern."（24126 邻域）↔ md 导航（拆翼重建）✅

## 取证命令示例

/usr/bin/grep -c "the rocket smashed through the window" notes/books/novels/odette-rising-by-julianne-edwards/text/ch25_chapter_25.txt → 1；退出码 0
/usr/bin/grep -c "I should never have made Monsieur Beauclerc leave." notes/books/novels/odette-rising-by-julianne-edwards/text/ch25_chapter_25.txt → 1；退出码 0
