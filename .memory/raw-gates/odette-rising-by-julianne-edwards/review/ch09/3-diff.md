# 3-diff · ch09 double it（T3 深审 2026-11-18）

R1 来源：子代理盲读（8 条，区间/锚点 100% 验证）；R2：chapter.sh --json rc=0。

## 三单对账

| 单 | 项 | R1/原文 | md | 判 |
|---|---|---|---|---|
| 漏 | 轻微 | R1 提到 significant order（巴黎大单）与 "Double it. Please" 原句——md 导航「Double it」承担、精读块未引（原句让给抚恤与自伤线） | 取舍理由：7 块预算（短章）分配给知情权/抚恤/身体/孤独/社交五轴；订单与翻倍由导航与原句2（generous/Sizable sum）间接承载 | 提示（不修） |
| 漏 | 轻微 | R1 提到 governess「六岁来、十二岁走、无人接替」与 Feld 家「五年前搬来」——md 词汇表 hirsute 例句逐字承载 governess 句；five years 由原句7 场景上下文（决定去 Feld 家）承载 | 同上 | 提示（不修） |
| 漏 | 无 | 其余 6 条（Corot 付款单头回得知死讯/accidents inevitable+父亲慷慨/翻倍+地址+合礼/Polo 与父亲的注视量对比/孤立=进攻也是撤退/Feld 试一试决断）md 全覆盖 | — | 无关键漏 |
| 编 | 无 | — | — | 无编 |
| 错 | 无 | 说话人核：「Double it. Please」＝Odette；「As you wish」＝银行经理；「That is the father of the girl who was killed」＝银行经理；「not the offspring…」＝叙述——md 归对 ✅ | — | 无错 |

## 关键事实回源（R1 ↔ md）

- 大单：text "the Huré factory had received a significant order from the store in Paris"（59:132）↔ md 导航「巴黎大订单让她喜极欲泣」✅
- Corot 付款单：text "“That is the father of the girl who was killed.”"（442:490）↔ md 原句1 上下文 ✅
- 父亲慷慨：text "Your father was always generous to the bereaved families"（1713:1769）↔ md 原句2 ✅
- Double it：text "“Double it. Please,” she said"（1855:1884）↔ md 导航「Double it」＋文件名 ✅
- 注视量对比：text "She couldn’t recall her father ever having touched her"（3836:3890）↔ md 原句5 ✅
- governess：text "she had not arrived until she was six"（4644:4681）↔ md 词汇表 hirsute 例句 ✅
- 三级阶梯：text "taking up her blade when they were not enough"（5588:5633）↔ md 原句6 ✅
- Feld 五年：text "the family had moved in at least five years ago"（6377:6424）↔ md 原句7 场景上下文 ✅

## 取证命令示例

/usr/bin/grep -c "Double it. Please" notes/books/novels/odette-rising-by-julianne-edwards/text/ch09_chapter_9.txt → 1；退出码 0
/usr/bin/grep -c "taking up her blade when they were not enough" notes/books/novels/odette-rising-by-julianne-edwards/text/ch09_chapter_9.txt → 1；退出码 0
