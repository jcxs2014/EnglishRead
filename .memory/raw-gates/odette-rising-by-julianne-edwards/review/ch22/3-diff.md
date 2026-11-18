# 3-diff · ch22 the macabre rose garland（T3 深审 2026-11-18）

R1 来源：子代理盲读（8 条，区间/锚点 100% 验证）；R2：chapter.sh --json rc=0。

## 三单对账

| 单 | 项 | R1/原文 | md | 判 |
|---|---|---|---|---|
| 漏 | 轻微 | R1 提到儿子反常拥抱（此前被叮嘱远离病母）、Legrands 慰问火腿、L 'Athlète 阅读、父亲来信——md 原句上下文与词汇表部分承担（父亲来信在原句6 邻域未引） | 7 块预算给了病榻与婚姻两主轴 | 提示（不修） |
| 漏 | 无 | 其余 7 条（鼠与气味/血手绢花环/疗养院僵局/welds 汇报+Well done/I'll stay here/consumption 确认/孤 Lille+盼她惨败）md 全覆盖 | — | 无关键漏 |
| 编 | 无 | — | — | 无编 |
| 错 | 无 | 说话人核：「She needs to go to a sanatorium」＝医生；「I'll stay here. I won't leave you.」＝妻；「How was the factory today?」＝妻；「Good. Well done.」＝妻——md 归对 ✅ | — | 无错 |

## 关键事实回源（R1 ↔ md）

- 儿子拥抱：text "his son raced toward him and flung two thin arms around his waist"（439:504）↔ md nav「反常拥抱」✅
- 花环：text "bloodied handkerchiefs discarded about her like a macabre rose garland"（847:914）↔ md 原句2 ✅
- 疗养院：text "The Sanatorium d’Agincourt can take her."（2560:2623）↔ md 原句3 ✅
- welds：text "We have found a way to strengthen the welds in the frame."（4362:4419）↔ md suread 事实（1-suread.json）✅
- 僵局：text "“I’ll stay here. I won’t leave you.”"（4556:4592）↔ md 原句5 上下文 ✅
- 确诊：text "it was indeed consumption that was eating her lungs"（4931:4982）↔ md 原句5 分析 ✅
- 火腿：text "sending a note and a cured ham"（6888:6959）↔ md 词汇表 echelons 例句邻域 ✅
- 盼她惨败：text "he hoped she’d failed, dismally and publicly, forced back to her wretched house"（7621:7700）↔ md 原句7 ✅

## 取证命令示例

/usr/bin/grep -c "like a macabre rose garland" notes/books/novels/odette-rising-by-julianne-edwards/text/ch22_chapter_22.txt → 1；退出码 0
/usr/bin/grep -c "he hoped she’d failed, dismally and publicly" notes/books/novels/odette-rising-by-julianne-edwards/text/ch22_chapter_22.txt → 1；退出码 0
