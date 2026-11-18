# 3-diff · ch03 the faerie queen desk（T3 深审 2026-11-18）

R1 来源：子代理盲读（8 条，区间/锚点 100% 验证）；R2：chapter.sh --json rc=0。

## 三单对账

| 单 | 项 | R1/原文 | md | 判 |
|---|---|---|---|---|
| 漏 | 轻微 | R1 提到「绣房得知丝袜销往 Paris」——md 导航人物弧线有「问袜子去向」（事实在 text/ch03 "Where are these stockings bound for?" "Paris."），但精读块未引此对话 | 取舍理由：对话两行各自成段无法成块引，信息由导航层承担 | 提示（不修，理由如上） |
| 漏 | 无 | 其余 7 条事实（周三点到/斗篷/百英尺+Huré Hosiery+三百英尺/scowler+嫌恶/Paris 袜样/仙后巢+Who did these/勇气问/卧室三帧+牡蛎+交换眼神）md 全覆盖 | — | 无关键漏 |
| 编 | 无 | — | — | 无编 |
| 错 | 无 | 说话人核：「They're his. Your father's.」＝Beauclerc；「poisoned by an oyster」＝Dendron；「That one?」＝厨娘——md 全部归对 | — | 无错 |

## 关键事实回源（R1 ↔ md）

- 约 Wednesday two o'clock：text "suggesting that she arrive at the factory at two o'clock on Wednesday"（87:156）↔ md 原句1「拜访那天」背景 ✅
- Huré Hosiery：text "an edifice standing some hundred feet tall"（2642:2684）↔ md 原句3 ✅
- scowler：text "she recognized him from the funeral and her heart sank"（3808:3862）↔ md 原句5 ✅
- Who did these：text "“Who?” he replied. “They're his. Your father's.”"（11254:11302）↔ md 原句8 上下文 ✅
- 牡蛎：text "poisoned by an oyster. They have never been served in this house since."（18693:18764）↔ md 原句11 ✅
- 交换眼神：text "But Odette hadn't missed the look that passed between them."（19201:19260）↔ md 原句12 ✅

## 取证命令示例

/usr/bin/grep -c "Where are these stockings bound for" notes/books/novels/odette-rising-by-julianne-edwards/text/ch03_chapter_3.txt → 1；退出码 0
/usr/bin/grep -c "Huré Hosiery" notes/books/novels/odette-rising-by-julianne-edwards/text/ch03_chapter_3.txt → 1；退出码 0
