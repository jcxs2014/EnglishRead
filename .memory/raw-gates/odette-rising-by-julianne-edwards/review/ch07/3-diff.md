# 3-diff · ch07 emilie corot（T3 深审 2026-11-18）

R1 来源：子代理盲读（8 条，区间/锚点 100% 验证）；R2：chapter.sh --json rc=0。

## 三单对账

| 单 | 项 | R1/原文 | md | 判 |
|---|---|---|---|---|
| 漏 | 轻微 | R1 提到量衣「一站 an hour 不肯求坐」与「mourning 已毕、三排褶边蕾丝」的行头拍板——md 原句1/2 覆盖其羞辱与代价逻辑，行头细节（三排蕾丝/草帽）未入精读块 | 取舍理由：7 块预算让给「shame and comfort」「price to pay」两主轴；行头由 ch08 出发段承接 | 提示（不修） |
| 漏 | 轻微 | R1 提到 corset 抗性时刻（"No! Use what you have, no more measuring. Please,"）——md 未引此句（corset 痛苦线由 ch08 原句1 承接） | 同上；抗性语义在 ch08 请求帮助的反差中兑现 | 提示（不修） |
| 漏 | 无 | 其余 6 条（黑发相片=巴黎人判断/Beauclerc 排练推销+disconcerting/Emilie 事故 sleeve-spindles/母亲抱尸/扫落样品）md 全覆盖 | — | 无关键漏 |
| 编 | 无 | — | — | 无编 |
| 错 | 无 | 说话人核：报告事故＝Dupont（"Her sleeve caught"）；「It was little Emilie Corot」＝叙述；摔样＝Beauclerc——md 归对 ✅。事故因果（sleeve→spindles）md 词汇表例句逐字承载 ✅ | — | 无错 |

## 关键事实回源（R1 ↔ md）

- 量衣之辱：text "She had been standing still for what felt like an hour"（965:1019）↔ md 原句1 上下文（refuge/comfort 块邻域）✅
- 相片=巴黎人：text "She picked up the photograph of the beautiful dark-haired woman"（3967:4030）↔ md 原句3 ✅
- disconcerting：text "the woman was physically disconcerting, and she knew nothing of the business"（5374:5450）↔ md 原句4 ✅
- sleeve/spindles：text "“Her sleeve caught,” said Dupont. “She was pulled into the spindles.”"（6345:6414）↔ md 词汇表 spindles 例句 ✅
- Emilie：text "It was little Emilie Corot. He picked up her hand, but it was limp"（6221:6287）↔ md 导航「Emilie Corot」＋原句6 场景 ✅
- 扫落样品：text "With a single lash of his arm, he swept the whole lot onto the floor."（8029:8098）↔ md 原句7 ✅

## 取证命令示例

/usr/bin/grep -c "It was little Emilie Corot" notes/books/novels/odette-rising-by-julianne-edwards/text/ch07_chapter_7.txt → 1；退出码 0
/usr/bin/grep -c "With a single lash of his arm" notes/books/novels/odette-rising-by-julianne-edwards/text/ch07_chapter_7.txt → 1；退出码 0
