# ch10 Tabula Rasa — 对账（R3）

素读：`1-suread.json`（8 条，锚点脚本核对 8/8 命中，`facts= 8 bad= 0`）
机器层：`2-machine.json`，rc=0，verdict=ok，3 块 / 691 words / segments 3 / 查无 0 / 空引号 0 / 子项缺 0 / 关键词缺 0 / 形态偏离 0；`block_target [2,2]`、`block_range [3,10]`、`issues` 全空
精读：`ch10 tabula rasa.md`（80 行，3 个引语块，词汇 12 行）

## 一、漏（素读有 / md 无）

| # | 素读条目 | 原文（text/ch10_tabula_rasa.txt） | md 对应 | 判 |
|---|---|---|---|---|
| L1 | 第 4 条前半：他旧日的口味——主要听摇滚，喜欢 rockabilly，还有英伦入侵乐队、朋克、早期乡村、Dylan | 38: “I used to listen mostly to rock and roll. I liked rockabilly, but I liked a lot of other stuff, too: British Invasion bands, punk, early country music, Dylan.” | 全缺。`grep -c -F "rockabilly"/"Dylan"` = 0／0；`grep -nE "摇滚\|朋克\|乡村"` 零命中，退出码 1。:11 只写「他『无意间』成了 Alba 那个无词的音乐世界的学徒」 | 提示：「意外当上学徒」的前提是**他有过另一套耳朵**（摇滚／rockabilly），没有这个落差，「accidently apprenticed」就只是一个词。建议 :11 补半句「他从前只听摇滚」 |
| L2 | 第 7 条前半：收藏名单——Terry Riley、Philip Glass、Arvo Pärt、Pauline Oliveros、Steve Reich，再往回跳到勋伯格、贝尔格、韦伯恩，直到 Thomas Tallis | 68: “spending whole days listening to Terry Riley, Philip Glass, Arvo Pärt, Pauline Oliveros, Steve Reich, and then skipping backward to Schoenberg, Berg, Webern, then early composers like Thomas Tallis.” | 全缺。`grep -c -F` 七个名字（Terry Riley/Philip Glass/Arvo/Oliveros/Reich/Schoenberg/Tallis）全为 0；:11 仅「整天听极简主义与更早的作曲家」 | 提示：名单型信息，允许压缩（选两三个名字即可），但一个都没有时，读者看不出这条听觉路线的方向（美国极简 → 第二维也纳乐派 → 文艺复兴复调），而这正是本章「声音把他洗空」的实物证据。本章词汇表也未收其中任何一个 |
| L3 | 第 2 条尾：「水停了，她还在唱」 | 28: “The water stops. Alba continues to sing.” | 无（:11 只写「她反复唱同样的乐句」） | 跳过：单句细节，且「怕吵醒他」的体贴已由 reassuring／soft 覆盖 |

## 二、编（md 有 / 原文无）

| # | md 断言 | 原文 | 判 |
|---|---|---|---|
| — | 未发现凭空出现的情节、人物、数字、曲名 | — | 无 |

> 说明：`:13`「他却在其中放松下来」一句，原文只到「I realized that I liked it, a lot.」（`:63`）——没有「放松」这个词，也没有任何身体状态描写。因它是对「喜欢」的引申而非新增事实，记作提示（见 E1），不判编。

## 三、错（两边都有 / 不一致）

| # | md 断言 | 原文逐字 | 判 |
|---|---|---|---|
| E1 | :13「极简主义的『宁静』被写成工业嗡鸣加指甲刮黑板，**他却在其中放松下来**」 | 63: “I surprised myself: I realized that I liked it, a lot.”；67–68: “Alba smiled. ‘Oh, yeah.’” 全章无 relax／relaxed／settle 类词（`grep -nE "relax\|settle"` 零命中，退出码 1） | 提示：把「喜欢」写成「放松」，是本章唯一一处比原文更软的引申；「宁静」被写成噪音这一层（:47 的 industrial／droning／fingernails-on-chalkboard）完全准确 |
| E2 | :15「句子长短跟着内容走——**写声音时句子被分号和逗号一路推长**，**写身份崩塌时反而短促**」 | 实测句长（按 . ! ? ” 切分，Python 计数）：`:33` 身份段 7 句、均值 **16.7** 词、最长 29 词；`:47` 声音段 7 句、均值 **8.4** 词、最长 23 词 | 提示：方向与实测相反——身份段平均句长是声音段的两倍。站得住的只有「分号把声音串成一条」（:47 用 `String instruments; long low stacks…` 一个句子装下整段音色），「短促」的那一半应改挂到 :78–79 的收尾（`It took time to find out.` / `I am still finding out` 才是全章最短的句子） |

## 四、R4 逐块对应（人判）

| 块 | 引语 | 中文是否在讲这句 | 三问 | 判 |
|---|---|---|---|---|
| 1 | 28 行 笔记本／取笔／写她的声音 | 是（开头两句「凌晨三点多，他先听见水声和歌声，然后开灯、摸眼镜」取自相邻的 :23，属铺垫，随后即回到本句） | 主语＝I（retrieve/find/start）；受事＝notebook、a description of Alba's voice；「被吵醒这件事，被他写成了被安抚」点的是叙述态度，未改写事实 | 通过（附注：铺垫句请与 :23 对齐，勿被读者当成引语内容） |
| 2 | 29 行 不是有意放弃／习惯丢了／Maybe I never had been? | 是 | 主语＝I（didn't mean／lost／stopped thinking）；「people asked，that got awkward」施事换人这一点抓得准；问句归属＝他自问，未误挂在 Alba | 通过 |
| 3 | 39 行 她答问／缠在沙发上／数月后想要语言 | 是 | 主语＝she（would answer）／we（listened）／a part of me（woke up）；受事＝language；「他想要的不是写得好，是 language 本身」与 desperately 的位置分析一致 | 通过 |

> 密度：3 块均做到「先拆句法再谈效果」，块 1 的 puzzle piece 一段（「反复出现的同一块乐句是还没嵌进去的一角」）是全章最好的一处细读。

## 五、已核实为正确（防下一轮误修）

1. **日期与年龄**：`:18` “Saturday, October 25, 2025 (Zach is 24, Alba is 24)”；2025-10-25 确为星期六。md :11／:80 的「2025 年 10 月 25 日」「凌晨 3:13」均对；本章抬头 Zach 在前，md :15 也把「我」判给 Zach，正确。
2. **「Alba 没有对他说过一句关于写作的话」**（:13，负向断言）：她的全部台词只有 4 处——`:47` “You probably won’t like it.”、`:48` “So?”、`:57–58` “La Monte Young, Trio for Strings…What did you make of it?”、`:67` “Oh, yeah.”；无一句涉及写作。断言成立。
3. **曲名与年份**：`:57` “La Monte Young, Trio for Strings. It’s from 1958.”；md :11／:80「La Monte Young 的 Trio for Strings」「1958」无误，且未把作曲家写成 La Monte Young 之外的任何人。
4. **「极简主义原点」的译法**：`:57` “It’s kind of ground zero for minimalism.”；md :13「标题的拉丁语（擦净的书写板）」与「ground zero」分属两处，未混为一谈。
5. **停笔原因的三层**：`:33` 怕笔记本落到别人手里／`:73` uncertainty 与「为别人的认可而写」；md :11 与 :12 分层叙述，未把「怕」（外部）说成「倦」（内部）。
6. **「她是被听见的人」**（:14）：依据 `:68` “She would answer questions if I asked, but mostly we listened together” 与 `:58` “What did you make of it?”；「把他当成能给出判断的听者」有原文支撑。
7. **12 条词汇**：脚本逐条整串命中（`rows=12 miss=0`），含 `fingernails-on-chalkboard`（:47 原句）、`headphone jack`（:47 原句）、`entwined`（:68 原句）、`approval`（:73 原句）；`accidently` 的拼写错误已在释义里注明「原文拼写如此」，处理正确。
8. **`Alba is 42` 不涉本章**：本章年龄 24/24，md 未做任何年龄推算（`grep -nE "42\|四十二"` 零命中，退出码 1），与 ch06 的瑕疵无传导。
