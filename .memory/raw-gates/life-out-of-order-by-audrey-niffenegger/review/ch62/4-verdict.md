# ch62 The Empty Orchestra — R5 判定

- md：`notes/books/novels/life-out-of-order-by-audrey-niffenegger/ch62 the empty orchestra.md`
- text：`notes/books/novels/life-out-of-order-by-audrey-niffenegger/text/ch62_the_empty_orchestra.txt`
- R1：`review/ch62/1-suread.json`（先于 md 打开）｜R2：`review/ch62/2-machine.json`｜R3/R4：`review/ch62/3-diff.md`

## R2 机器层

`bash scripts/chapter.sh "…/ch62 the empty orchestra.md" --json` → **rc=0**，`verdict=ok`，`issues=[]`，`blocks=8`，`cjk_ratio` 最低 0.66。rc=0 不等于通过。

## R5 判定表

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 逐字：8 块引语 | `:30`「Her breath rages through her—」／`:35`「The smoke from the painted wood is sweet and probably toxic」／`:58`「I sit at the piano and wonder」／`:70`「The piece they played was so extraordinary」／`:87`「The fire is very low, and I can see my breath.」／`:192`「Clare always leaves her bag on one of the dining room chairs.」／`:283`「I expect him to yell at me, to beat me, but he doesn’t.」／`:320`「The Japanese word karaoke means “empty orchestra.”」 | 8/8 逐字成立 | 通过 |
| 逐字：词汇 14 条例句 | 逐条 `in flat(text)`：`poltergeists`／`encyclopedic`／`ramshackle`／`existential`／`distraught`／`subsides`／`dwindling`／`carcasses`／`engulfed`／`extricate`／`address book`／`aisles`／`bell`／`bedroom` | 14/14 命中，miss=0 | 通过 |
| 对应：块 1 | 空楼＋骚灵＋瘦＋减法；md 未把「我害臊」写成她的感受 | 在讲这句引语（`为什么这样写` 的「痰音」取自引语前一句 `:30` 开头，引语选短·提示） | 通过 |
| 对应：块 2 | 甜／有毒／没别的选择／只问过一次；md 的「穷与病互为因果」是解读，非新事实 | 在讲这句引语（「柴的来处」在 `:35` 引语之前被切掉·提示） | 通过 |
| 对应：块 3 | 「新＝她没听过」的解释链完整，未把它写成「世上没有」 | 在讲这句引语 | 通过 |
| 对应：块 4 | 听感飞升→转头→空衣服；md 未把「她」误认成别人 | 在讲这句引语 | 通过 |
| 对应：块 5 | 两次呼吸＋指背＋凉＋怕；「she is cool」译「是凉的」未夸成「冰凉」 | 在讲这句引语 | 通过 |
| 对应：块 6 | 主语＝扎克（`:122` 段内的「I」）；md 未把偷窃挂到奥利弗头上 | 归属正确 | 通过 |
| 对应：块 7 | 「I understand what I have done to him, what Alba and I have done」→ md「明白自己和阿尔芭对他做了什么」，责任主语未丢 | 在讲这句引语 | 通过 |
| 对应：块 8 | 词源→阿尔芭的说法→他的否定，三层对照；md 区分了「她说」与「他觉得」 | 在讲这句引语 | 通过 |
| 形态：块数／子项／标签 | 8 ∈ `block_target [7,12]`；四子项齐全；`Oliver:`×4／`Zach:`×2（`:23/:114/:122/:218/:235/:270/:295` 共 7 标签）与 md `:15`「靠标签分界」相符 | 合格 | 通过 |
| 断言：`:11`「扎克靠偷来的通讯录找上门」 | `:192`＋`:211`「I recognize Henry’s handwriting.」（在 `:122 Zach` 段内） | 成立 | 已核 |
| 断言：`:132`「在卧室里问一句『为什么』」 | `:270`「The bedroom door opens…」／`:277`「“Oliver.” He looks distraught. “Why?”」 | 成立 | 已核 |
| 断言：`:132`「母亲唱过的摇篮曲」 | `:60`「lullabies my mother once sang to me」 | 成立 | 已核 |
| 断言：`:132`「一场听不清的旧音乐会」 | `:76`「I barely remember it now」 | 原文是「记不清」不是「听不清」；且 `:70` 当场称那曲子 extraordinary | 提示 |
| 断言：`:70` 那场音乐会的年龄错位（他十几岁、阿尔芭五十多岁、1980s） | `:70`「when I was a teenager. Alba was in her fifties… It was winter in the 1980s」 | 素读有、md 无 | 提示（漏） |
| 断言：`:228` 笔记本与「she’s left him」 | `:228`「The last date Alba gives is October 14, 2041… think, she’s left him, and I am deeply sorry.」 | 素读有、md 无 | 提示（漏） |

## 报数（四组）

- **逐字**：引语 8/8、词汇 14/14，0 条。
- **对应**：8/8 块在讲引语；块 1、块 2 各有一处用到引语外的相邻句（提示）。
- **形态**：8 块落位、标签与 POV 对得上、块序与时间线一致，0 条。
- **断言**：导航 5 条 + 总结 0 条 + 抽查 4 条，其中 12 条成立、2 条提示（听不清、年龄错位），另 1 条提示（笔记本未进 md）。

| 章 | rc | 块数 | 漏 | 编 | 错 | 提示 |
|---|---|---|---|---|---|---|
| ch62 | 0 | 8 | 0 | 0 | 0 | 4 |

## 已核实为正确（防下一轮误修）

1. **偷通讯录的人是扎克，不是奥利弗**——本库下一轮最容易误改的一处。`:122` 起是 `Zach:` 段，`:192`「I open it, find her address book, zip it into the inside pocket of my coat」的主语是扎克；`:211`「I recognize Henry’s handwriting」也是扎克（他认得亨利的字）。md `:11`「扎克靠偷来的通讯录找上门」与 `:132`「扎克偷走克莱尔的通讯录」**均正确**，不要改成奥利弗。
2. **问「Why?」的人是扎克，答「I can’t explain」的是奥利弗**：`:277`「“Oliver.” He looks distraught. “Why?”」——扎克先叫名字再问；`:277` 下一段「“I can’t explain, even to myself. I’m sorry.”」是奥利弗。md `:132`「扎克…问一句『为什么』」方向正确。
3. **原句 6 的「他打开包」不必改成「我」**：引语是第一人称「I open it」，md 复述用第三人称「他」，指扎克，不是主语错乱。
4. **手机／笔记本别混**：`:228` 的「our notebook」是黄房子床板下的笔记本（阿尔芭与奥利弗共用），不是克莱尔的通讯录（`:192`）；两者在 2041 段里先后出现，md 只提通讯录，属取舍，不是把两物写成一物。
5. **`she’s left him` 的 him 是扎克**：`:228` 奥利弗读笔记本后想「她离开他了，我很抱歉」——「他」＝扎克（阿尔芭的丈夫），不是奥利弗自己。下一轮若把 him 读成奥利弗，整段认罪逻辑就会反过来。
6. **「空乐队」的翻译没错**：`:320`「karaoke means “empty orchestra”」→ md「日语里 karaoke 的意思是『空乐队』」，逐字。
7. **三段时间线不是倒叙笔误**：`:18` 2069 → `:109` 2041 → `:290` 2022，原文就是「越跳越年轻」，md `:15` 已说明。
