# 3-diff · ch26 the exiled thief（T3 深审 2026-11-18）

R1 来源：子代理盲读（8 条，区间/锚点 100% 验证）；R2：chapter.sh --json rc=0。

## 三单对账

| 单 | 项 | R1/原文 | md | 判 |
|---|---|---|---|---|
| 漏 | 轻微 | R1 提到 altar-boy 回忆、Pierre 帮忙救火、Beauclerc 请她克制（街头啜泣失体）——md nav/原句上下文部分承担 | 5 块预算（短章）给了教堂/流放/天谴/反犹/发夹五拍 | 提示（不修） |
| 漏 | 无 | 其余 7 条（四个月未进教堂/独自在 Lille/被流放+欠我/devilment+God has spoken/lick of madness/无经理+Jews going to the dogs/想家恨城/发夹圣物）md 全覆盖 | — | 无关键漏 |
| 编 | 无 | — | — | 无编 |
| 错 | 无 | 说话人核：「I have been exiled here, by her?」＝Corot；「God has spoken」＝Corot；「it’s people who are brutal」＝Corot；「That is beneath you」＝Beauclerc——md 归对 ✅ | — | 无错 |

## 关键事实回源（R1 ↔ md）

- 四个月：text "He had not set foot in a church for four months. Not since burying his wife."（406:482）↔ md 原句1 上下文 ✅
- 流放：text "you do not know that I have been exiled here, by her?"（1921:1974）↔ md 原句2 ✅
- 天谴：text "Burned the place down during an evening of devilment and debauchery."（2212:2280）↔ md 原句3 ✅
- 疯气：text "a lick of madness"（2351:2389）↔ md 原句4 分析（疯话与真情同体）✅
- 反犹：text "She’s Jewish, you know? It’s going to the dogs."（3355:3384）↔ md 原句5 ✅
- beneath you：text "that is beneath you"（同段）↔ md 原句5 分析（Beauclerc 护她）✅
- 发夹：text "He had found one of her hairpins yesterday."（5027:5070）↔ md 原句6 ✅

## 取证命令示例

/usr/bin/grep -c "a lick of madness" notes/books/novels/odette-rising-by-julianne-edwards/text/ch26_chapter_26.txt → 1；退出码 0
/usr/bin/grep -c "He had found one of her hairpins yesterday." notes/books/novels/odette-rising-by-julianne-edwards/text/ch26_chapter_26.txt → 1；退出码 0
