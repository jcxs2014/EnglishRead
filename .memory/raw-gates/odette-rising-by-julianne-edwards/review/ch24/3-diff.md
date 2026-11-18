# 3-diff · ch24 the death certificate（T3 深审 2026-11-18）

R1 来源：子代理盲读（8 条，区间/锚点 100% 验证）；R2：chapter.sh --json rc=0。

## 三单对账

| 单 | 项 | R1/原文 | md | 判 |
|---|---|---|---|---|
| 漏 | 轻微 | R1 提到 Elise 与医生守床、儿子被叮嘱远离病母、L 'Athlète 等外围——md 导航/词汇表部分承担 | 5 块预算（短章）给了死亡证明/临终/团灭/父子祷四拍 | 提示（不修） |
| 漏 | 无 | 其余 7 条（midnight 死亡/clean by six/our loss/血沫 rattle/不知如何告别/站街女烟蒂+怜悯/Gone to God+撞墙+同祷）md 全覆盖 | — | 无关键漏 |
| 编 | 无 | — | — | 无编 |
| 错 | 无 | 说话人核：「I'm sorry for your loss, sir」＝Elise；「our loss」＝Beauclerc；「Have you prayed yet?」＝男孩；「It's more powerful if we do it together」＝Beauclerc——md 归对 ✅。时间：three o'clock/midnight/six 逐字 ✅ | — | 无错 |

## 关键事实回源（R1 ↔ md）

- 三点/午夜：text "It was three o’clock. His wife had died at midnight."（311:363）↔ md 原句1 ✅
- clean by six：text "make sure she looked clean and calm by six, when the boy would wake"（567:634）↔ md 原句2 上下文 ✅
- our loss：text "“I think it is our loss, is it not?” He smiled."（1539:1586）↔ md 原句3 上下文（suread）✅
- rattle：text "It was a terrible, bloody rattle, and her body had convulsed"（2163:2223）↔ md 原句4 ✅
- 烟蒂怜悯：text "He felt a rush of compassion; she was someone’s daughter"（2666:2722）↔ md 原句5 上下文（suread）✅
- Gone to God：text "Your mother has passed away. She’s…that’s to say, she’s gone to God.”"（3538:3607）↔ md 原句7 上下文 ✅
- 同祷：text "She will need our prayers when she crosses the bridge to the land of the dead"（4690:4767）↔ md 原句8 上下文（suread）✅

## 取证命令示例

/usr/bin/grep -c "His wife had died at midnight." notes/books/novels/odette-rising-by-julianne-edwards/text/ch24_chapter_24.txt → 1；退出码 0
/usr/bin/grep -c "the bridge to the land of the dead" notes/books/novels/odette-rising-by-julianne-edwards/text/ch24_chapter_24.txt → 1；退出码 0
