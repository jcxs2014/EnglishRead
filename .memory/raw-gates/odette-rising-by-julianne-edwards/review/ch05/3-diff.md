# 3-diff · ch05 the bank and the bridge（T3 深审 2026-11-18）

R1 来源：子代理盲读（8 条，区间/锚点 100% 验证）；R2：chapter.sh --json rc=0。

## 三单对账

| 单 | 项 | R1/原文 | md | 判 |
|---|---|---|---|---|
| 漏 | 轻微 | R1 提到 Feld 先生当街倒下、Merry 扛送、死于心脏（text "“No, his heart,” said Merry"）、家有孩子——md 导航有人物弧线「Feld：以一次倒下完成授课」与原句9 上下文，但倒下/扛送的动作细节未入精读块 | 取舍理由：5 块预算让给「旁观者无用」与「shape the hours」两条主轴；事件本身导航层已承担 | 提示（不修） |
| 漏 | 无 | 其余 7 条（两周字条无回音/逼款清单/摔门+兴奋/银行 Thursday+centime/浮尸+绕河/Could I cross/shape the hours）md 全覆盖 | — | 无关键漏 |
| 编 | 无 | — | — | 无编 |
| 错 | 无 | 说话人核：逼款台词＝Beauclerc（all but spat）；「Should I assume you will come each Thursday?」＝银行经理；「No, his heart」＝Merry——md 归对 ✅ | — | 无错 |

## 关键事实回源（R1 ↔ md）

- 两周无回音：text "he had received no replies to his notes sent over the last two weeks"（289:357）↔ md 原句1 ✅
- 逼款三连：text "it's your factory. You must pay your workers."（2291:2336）↔ md 原句2 ✅
- 兴奋：text "The front door was slammed with some might."（3462:3505）↔ md 原句3 上下文 ✅
- Thursday/centime：text "Should I assume you will come each Thursday?"（6790:6834）↔ md 原句5 上下文（walnut 面孔段）✅
- 浮尸：text "there had been another bloated corpse floating past last week"（7783:7844）↔ md 原句6 分析「她的巴黎体验」背景 ✅
- Could I cross：text "Could I? she thought. Could I cross?"（9489:9525）↔ md 导航「巴黎之谜推到眼前」＋素读事实（未入精读块，导航层承担）✅
- shape the hours：text "you could shape the hours in which you lived"（12060:12104）↔ md 原句9 ✅

## 取证命令示例

/usr/bin/grep -c "Could I? she thought. Could I cross?" notes/books/novels/odette-rising-by-julianne-edwards/text/ch05_chapter_5.txt → 1；退出码 0
/usr/bin/grep -c "you could shape the hours in which you lived" notes/books/novels/odette-rising-by-julianne-edwards/text/ch05_chapter_5.txt → 1；退出码 0
