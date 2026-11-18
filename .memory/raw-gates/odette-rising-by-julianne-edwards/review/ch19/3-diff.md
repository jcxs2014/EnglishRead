# 3-diff · ch19 it was hope（T3 深审 2026-11-18）

R1 来源：子代理盲读（8 条，区间/锚点 100% 验证）；R2：chapter.sh --json rc=0。

## 三单对账

| 单 | 项 | R1/原文 | md | 判 |
|---|---|---|---|---|
| 漏 | 轻微 | R1 提到茶会的开场（Eugénie 抢开门）与 Berthe 的蛇皮烟盒、Gabriel 侍者、Comte 致意——md 原句1 为 Eugénie 抢门 ✅；烟盒/侍者名/Comte 由词汇表与导航外围承担 | 15 块预算覆盖全部主轴 | 提示（不修） |
| 漏 | 无 | 其余 7 条（teacup 香槟+敬逝者/家丑抖出+Guiche 提议/Beauclerc 突访+fire 审判+蛇袜/Gagnon 警告+hairbrush+find help/Beauclerc 辞职装箱/Dupont 报信+bank 承诺+foundryman/Arielle 拒绝+驱逐+方案+hope）md 全覆盖 | — | 无关键漏 |
| 编 | 无 | — | — | 无编 |
| 错 | 无 | 说话人核：「I thought you were dying」＝Berthe；「We were just toasting the dead」＝Odette；「Edouard told me about you」＝Berthe 转述；「No, madame, I'm not sure I have」＝Beauclerc——md 归对 ✅ | — | 无错 |

## 关键事实回源（R1 ↔ md）

- Eugénie 抢门：text "Eugénie, high on cake, jumped up, shouting, “I’ll go, I’ll go!”"（879:942）↔ md 原句1 ✅
- 茶杯香槟：text "he poured it into a teacup and thrust it at Berthe"（4848:4898）↔ md 原句2 ✅
- 敬逝者：text "we must salute those we have lost and never forget that we once were loved."（同段）↔ md 原句3 ✅
- fire 审判：text "“Huré needs someone with fire,” she said."（11301:11374）↔ md 原句4 ✅
- Gagnon 警告：text "Your father once gave him a large sum, and now, if he finds out that you exist"（14597:14675）↔ md 原句5 上下文（suread 事实）✅
- find help：text "He is unheroic. Find help."（同段）↔ md 原句6 上下文（suread）✅
- Beauclerc 辞职：text "He decided to quit, to leave; pack up the house and go."（19961:20016）↔ md 导航「携箱出走」✅
- hope：text "It was hope."（尾段）↔ md 原句15 ✅

## 取证命令示例

/usr/bin/grep -c "It was hope." notes/books/novels/odette-rising-by-julianne-edwards/text/ch19_chapter_19.txt → 1；退出码 0
/usr/bin/grep -c "Huré needs someone with fire" notes/books/novels/odette-rising-by-julianne-edwards/text/ch19_chapter_19.txt → 1；退出码 0
