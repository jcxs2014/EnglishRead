# 3-diff · ch27 the night she stopped（T3 深审 2026-11-18）

R1 来源：子代理盲读（8 条，区间/锚点 100% 验证）；R2：chapter.sh --json rc=0。

## 三单对账

| 单 | 项 | R1/原文 | md | 判 |
|---|---|---|---|---|
| 漏 | 轻微 | R1 提到厨房群像开场（W.G./账目/Ned 门边）、Eiffel 灯火与独身女性街上自信行走、鸦片注射细节、Pequin 拒问缘由——md nav/原句上下文与 suread 承担，未入精读块 | 8 块预算给了急报/红屋/缝脸/止刀四幕 | 提示（不修） |
| 漏 | 无 | 其余 7 条（急报+药篮/红屋熄灭/伤情/no one but you+Pequin/伤口实体/mediating/裹刀收瓶）md 全覆盖 | — | 无关键漏 |
| 编 | 无 | — | — | 无编 |
| 错 | 无 | 说话人核：「You must come. It’s Madame Marie-Sainte.」＝Merry；「No. She said no one but you.」＝Nanette；「We have opium」＝Nanette；「as if she were hemming a skirt」＝叙述（Pequin 缝合）——md 归对 ✅ | — | 无错 |

## 关键事实回源（R1 ↔ md）

- 急报：text "A cab arrived when I was getting coal. A message from Nanette."（1587:1649）↔ md 原句1 上下文 ✅
- 红屋熄灭：text "nothing glittered, nothing moved"（4492:4547 邻域）↔ md 原句2 ✅
- 伤情：text "A wound ran from her eyebrow to the corner of her mouth"（4492:4547）↔ md 原句3 ✅
- no one but you：text "She said no one but you. No one else."（5541:5578）↔ md suread 事实（1-suread.json）✅
- hemming：text "as if she were hemming a skirt"（10474:10504）↔ md suread 事实（1-suread.json）✅
- wounded creature：text "stripped of her fire, had never seemed more real."（同段邻域）↔ md 原句4 ✅
- mediating：text "as if her body was mediating between her and her life"（视段）↔ md 原句6 ✅
- 裹刀：text "She trembled as she wrapped her blade back in its cloth"（视段）↔ md 原句7 ✅

## 取证命令示例

/usr/bin/grep -c "as if she were hemming a skirt" notes/books/novels/odette-rising-by-julianne-edwards/text/ch27_chapter_27.txt → 1；退出码 0
/usr/bin/grep -c "She said no one but you. No one else." notes/books/novels/odette-rising-by-julianne-edwards/text/ch27_chapter_27.txt → 1；退出码 0
