# 3-diff · ch32 goods to trade（T3 深审 2026-11-18）

R1 来源：子代理盲读（8 条，区间/锚点 100% 验证）；R2：chapter.sh --json rc=0。

## 三单对账

| 单 | 项 | R1/原文 | md | 判 |
|---|---|---|---|---|
| 漏 | 轻微 | R1 提到 Nanette 倒吸气与 Berthe 追问、Merry 只回望 Nanette 一眼、Smith 过渡帮忙——md nav/词汇表外围部分承担 | 5 块预算（短章）给了谎言/离场/自判三拍 | 提示（不修） |
| 漏 | 无 | 其余 7 条（dead voice 谎言/Polo ran away 谎言/Gagnon 派人接走/只回望 Nanette/惊觉残忍/复刀不停/no better than Gagnon）md 全覆盖 | — | 无关键漏 |
| 编 | 无 | — | — | 无编 |
| 错 | 无 | 说话人核：「he has left us, moved on to a position in Paris」＝Odette（谎）；「He ran away, I’m afraid.」＝Odette（谎）；「She was no better than Gagnon.」＝叙述层——md 归对 ✅ | — | 无错 |

## 关键事实回源（R1 ↔ md）

- dead voice：text "he has left us, moved on to a position in Paris. Footman."（325:382）↔ md 原句1 ✅
- Polo 谎言：text "He ran away, I’m afraid."（1032:1056）↔ md nav ✅
- 接走：text "Gagnon had sent a man to fetch him"（1540:1574）↔ md 原句2 ✅
- 回望 Nanette：text "He had turned only to look at Nanette, who leaned on the door frame"（1646:1713）↔ md 原句2 上下文 ✅
- 惊觉：text "She was stunned by her own capacity for cruelty and reeled backward"（视段）↔ md 原句3 ✅
- 复刀：text "She had not cut herself for months but now could not stop"（2362:2419）↔ md 原句4 ✅
- 自判：text "She was no better than Gagnon."（3228:3258）↔ md 原句5 ✅

## 取证命令示例

/usr/bin/grep -c "Gagnon had sent a man to fetch him" notes/books/novels/odette-rising-by-julianne-edwards/text/ch32_chapter_32.txt → 1；退出码 0
/usr/bin/grep -c "She was no better than Gagnon." notes/books/novels/odette-rising-by-julianne-edwards/text/ch32_chapter_32.txt → 1；退出码 0
