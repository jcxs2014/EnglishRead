# ch11 Thanksgiving — 对账（R3）

素读：`1-suread.json`（8 条，锚点脚本核对 8/8 命中，`facts= 8 bad= 0`）
机器层：`2-machine.json`，rc=0，verdict=ok，9 块 / 3570 words / segments 9 / 查无 0 / 空引号 0 / 子项缺 0 / 关键词缺 0 / 形态偏离 0；`block_target [6,11]`、`block_range [3,10]`、`issues` 全空
精读：`ch11 thanksgiving.md`（140 行，9 个引语块，词汇 12 行）

## 一、漏（素读有 / md 无）

| # | 素读条目 | 原文（text/ch11_thanksgiving.txt） | md 对应 | 判 |
|---|---|---|---|---|
| L1 | 第 6 条尾：Beck 到十一点还穿着睡衣、头发包着，说「我一夜没睡，Isadora 闹脾气」 | 119: “When we arrived at eleven she was still wearing pajamas and had her hair wrapped… Beck quietly said, I’ve been up all night, Isadora’s being a brat” | :14 只写「Beck 是这一章的守门人，疲惫」；`grep -c -F "Isadora 闹脾气"` = 0；`grep -c -F "brat"` 唯一命中的是 `celebrated` 里的字母串（:59 引语内），不是原词 | 提示：这是全章最早的伏笔——Isadora 先在 Beck 的睡眠里出场，比地下室那一幕早了两个小时。一句话即可补：「她一夜没睡，因为 Isadora 在闹」 |
| L2 | 第 5 条菜单末项：Gomez 与 Charisse 摇的无酒精蔓越莓 shrub（生蛋白、玫瑰果利口酒，伏特加只给不喝给 Lucinda 的人） | 103: “a nonalcoholic cranberry shrub (made by Gomez and Charisse with much theatrical shaking and straining, using raw egg whites, plus rose hip liqueur and vodka for anyone who isn’t Lucinda)” | `grep -c -F "shrub"` = 0、`"蔓越莓"` = 0；:13 只列到「tofurkey、披萨、羽衣甘蓝、通心粉焗菜」 | 提示：这一项是全场唯一「照顾未成年人」的细节（替 Lucinda 留不含酒的份），比菜名本身有意思，可压成一句 |
| L3 | 第 7 条前半：敬酒「To Henry, and all our absent friends and family」＋ Rosa 谈 Henry（七岁丧父、每年在此刻南瓜、教他们洗南瓜子再烤、把小孩当「short adults」） | 210: ““To Henry,” says Charisse, raising her glass, “and all our absent friends and family.””；:206: “I was seven when he died. I remember we used to carve pumpkins here every year… He always treated us like short adults.” | 正文零覆盖：`grep -c -F "Rosa"` = 0；`grep -c -F "Henry"` = 1，唯一命中在 :133 词汇例句里（`absent friends`）。:13 只写「一家人举杯敬不在场的人」 | 提示：Henry 是这顿感恩节真正被敬的人，也是 Alba 那条「时间旅行者家属」线的源头；现在他只在词汇表里出现过一次。Rosa 的南瓜回忆可压成半句 |
| L4 | 第 7 条中段：Clare 从厨房拿出 Kimy 的旧食谱笔记本（「These were Kimy's」），另有一本是 Henry 母亲的、’60 年代的罐头蘑菇汤与 Jell-O | 201: “then returns with a battered composition notebook. “These were Kimy’s,” Clare says. “I’ve got one that belonged to Henry’s mother, but most of those recipes involve canned mushroom soup or Jell-O, they’re from the ’60s.”” | `grep -c -F "食谱"` = 0 | 提示：这一段把「家宴」接回「Kimy 的厨房」（与 :23 的 Nanna Kimy 首尾相应），缺了之后第一章那段的师承就没有落点 |
| L5 | 第 8 条中段：车里摊牌之后的斗嘴——「我要开始叫你 Pandora」、「也许该反过来，Isadora 该提防我」、「我可以当 Isadora 的宿敌」、「她需要的不是宿敌，是一顿打屁股」、「听起来她挺有意思」 | 305: “I’m going to start calling you Pandora.”；:311: “Maybe it’s the other way around. Maybe Isadora should be wary of me.”；:319: “I could become Isadora’s nemesis.”；:323: “Isadora doesn’t need a nemesis, she needs a spanking.”；:327: “She actually sounds kind of fun,” | `grep -c -F "Pandora"` = 0、`"nemesis"` = 0；:11 只写「把话摊开」，:14 写「诉求只有一句」 | 提示：这是本章唯一的调笑段，也是 Zach 第一次对 Isadora 表现出兴趣而不是恐惧（下一章他会去找它）；全抹掉后，车里的对话只剩控诉 |
| L6 | 第 8 条前段：Alba 当着全家跳起来、把他拽进自己的旧卧室，Beck 说「Oh, to be young」 | 224: “when she jumps up and darts down the hall I am out of my chair following her before I think—she leads me into her old bedroom—behind us there is a delayed reaction, nervous laughter; Beck says, “Oh, to be young,”” | `grep -c -F "to be young"` = 0、`"旧卧室"` = 0 | 提示：全桌从「敬死者」转到「笑年轻人」的一口气，被省掉了；这也是本章唯一一处 Zach 被拉出自己心事的地方 |
| L7 | 第 8 条：地下室收音机唱的具体是「Wild thing, you make my heart sing」，用 Ella Fitzgerald 与大乐队的腔调唱一首车库摇滚 | 210: “I hear a radio playing in the basement, an uncanny voice that reminds me of Ella Fitzgerald singing with her big band: Wild thing, you make my heart sing” | `grep -c -F "Wild thing"` = 0；:13 写了「像 Ella Fitzgerald 的歌声」与「It’s about time—」，唯独没有曲名 | 提示：诡异感恰恰来自**曲目错配**（爵士嗓音唱 60 年代摇滚金曲）；只留「像 Ella」就丢了这个错配，读者不知道它「没什么不对，却让人发毛」到底指什么 |

## 二、编（md 有 / 原文无）

| # | md 断言 | 原文 | 判 |
|---|---|---|---|
| — | 未发现凭空出现的情节、人物、数字 | — | 无 |

## 三、错（两边都有 / 不一致）

| # | md 断言 | 原文逐字 | 判 |
|---|---|---|---|
| E1 | :14「结尾他是那个要求知情的人，**说出口的诉求只有一句**「I just hate being the last to know」」 | 265: ““Why do you keep secrets from me?” I ask Alba.”；274: ““What’s in your parents’ basement?””；282: ““Why am I the only person you know who thought Isadora was a human being?””；344: ““I just hate being the last to know.”” | 提示：他一路问了四句，最后那句只是收尾。「只有一句」把这一章的质问削成了一句台词；建议改「他问了一路，落点只有一句」 |
| E2 | :12「**她要他别问，他就真的不问**，然后自己去收拾那张案板上的派皮」 | 72: “I fold the piecrust gently over itself, scoop it up and transfer it to the waiting rhubarb pie… “Do you do that a lot?” I ask her.”；85: “I can tell that she just wants me to let it drop, so I do.” | 提示：顺序反了——他是**一边擀第四张派皮一边问**「你经常这样吗」，等她答完（:85）才放过；「收拾派皮」不是不问之后的动作，而是提问时的动作。「她要他别问」也是转述（原文是 warily／small voice／只想让他放过），不是她开口要求 |
| E3 | :15「每一段都从一个具体动作切入（擀派皮、抱柴、熄火）」 | 23: “Zach: Alba and I have been teaching ourselves to cook.”（第一段以习惯陈述开头）；147: “Caralora comes in the back door with a bundle of firewood.”（抱柴在第二段中腰，且是别人进来，不是段首） | 提示：三段里只有第三段（熄火，:291）符合；建议改成「第二段从 Beck 的睡衣与一夜没睡切入，第三段从熄火切入」 |
| E4 | 引语把「两周」放宽成「几个星期」：:11「省着吃撑了**几个星期**」、:140 同、:51「在那里待了**几个星期**」、:55 甚至写成「她说『几个星期』时用的还是同一副平调子」、:57「**几个星期**对上几分钟」 | 67: “I was there for a **couple of weeks** just now” | 提示：a couple of weeks 是「约两周」，不是「几个星期」（3–9 周）。四处同源，属量词放宽，且 :55／:57 把它当成她的原话在分析，等于替她改了口径；改「两个星期左右」，:57 的量词对照（两周 vs 几分钟）反而更刺人。注：:101／:105「练了几个星期」指 Berg 协奏曲，原文 “She’s been working on it for weeks”，用法正确，不要跟着改 |

## 四、R4 逐块对应（人判）

| 块 | 引语 | 中文是否在讲这句 | 三问 | 判 |
|---|---|---|---|---|
| 1 | 23 行 shadowing／feral／没学到本事 | 是 | 主语＝Alba（grew up shadowing）／I（have been accustomed／haven't picked up）；受事＝厨房里的本事；「几乎算野生的」对 feral 的降级处理恰当，未译成「没教养」 | 通过 |
| 2 | 34 行 切奶酪／手更细／颧骨／宽松衣服 | 是（「Alba 喊饿」出自同一行的前一句，非别行） | 主语＝she（takes／cuts）／I（notice）；受事＝她的手与身上的变化；md :35 说「baggy 是旁证——衣服没换，人小了」，未反过来写成「她换了宽衣服」 | 通过 |
| 3 | 42 行 希望你没发现／走了又回来／几分钟 | 是 | 主语＝I（was hoping／went／got dressed）；受事＝那半小时；「half an hour」与「a few minutes」两个时长并置这点抓住了，未擅自换算 | 通过 |
| 4 | 67 行 往前去／被弃置／两个星期／罐头／ration | 是（前半「有一栋房子她有时会落到那里」出自同一行更早处） | 主语＝I（went forward／was there）；受事＝那栋房子与罐头；ration 译「算着吃」准确；仅「几个星期」量词放宽（见 E4） | 通过（附 E4） |
| 5 | 98–99 行 三年都在 Gomolinski 家／三个 love／今年翻修 | 是 | 主语＝Charisse 与 Gomez（love to fill／cook）；受事＝他们的房子；「random constituents」译「连主人也未必认识的人」是合理引申，未写成「陌生人」 | 通过 |
| 6 | 69 行 我能下去吗／三重门禁／密码指纹眼睛 | 是 | 主语＝Lucinda（asks／walks／keys in）；受事＝那扇门；「glances at me」被读成「破例是当着他的面做的」，归属正确（看的是 Zach） | 通过 |
| 7 | 79 行 离线绝密／不许见新人／着迷／monkey see | 是 | 主语＝Alba（has been adamant）／Isadora（fixated）；受事＝新认识的人；md :87 把「offline 对世界设防／不许见新人 只对一个人设防」分开，是本章最准的一处判断 | 通过 |
| 8 | 89 行 界定与分开／一切都混／与死人往来 | 是 | 主语＝I（try to keep）；受事＝人与事；「staring straight ahead」被读成「不是看他」，与下文「不道歉」接得上 | 通过 |
| 9 | 99 行 Berg／尖利重复／为早死女孩／退回卧室 | 是 | 主语＝Alba（is playing）；受事＝那首协奏曲；md 点出「死去的年轻女孩」与死产女儿同名不点破，未说成「她就是为 Isadora 拉的」 | 通过 |

> 密度：9 块全部做到「先看句法再看效果」，块 7 的三条件分层、块 9 的 retreat（军事用语）是全章最好的两处。

## 五、已核实为正确（防下一轮误修）

1. **日期**：`:18` “Wednesday, November 26, 2025, and Thursday, November 27, 2025 (Alba is 24, Zach is 25)”；2025-11-26 确为周三、11-27 为周四。md :11／:140「11 月 26 日深夜」正确（午夜烤派属 26 日夜里）。
2. **四个派**：`:23` “we have two pies in the oven and two under construction” + `:28` “We are making pumpkin, apple, sweet potato and rhubarb”；md「四个派——南瓜、苹果、红薯、大黄」完全正确。
3. **「带派去 Alba 家」的方向**：`:23` “We are bringing pies to Alba’s family’s Thanksgiving tomorrow”；md 未写成「Alba 家带派给我们」。
4. **AI 项目的命名来源**：`:156` “She’s named after Beck’s daughter, who was stillborn.”；md :11／:140「名字取自 Beck 死产的女儿」准确，未写成「Beck 的女儿叫 Isadora、还活着」。
5. **禁令的范围**：`:165` “she is offline, top secret, not allowed to meet any new people… Isadora is especially not allowed to meet you.”；md :11「严禁它见任何新认识的人」＋:14「不许知道 Zach」两层都对。
6. **Beck 的三重身份**：`:113` “she is an artist, computer programmer and professor”；md :14「守门人」不与之冲突。
7. **Clare 的两句台词**：`:237` “She’s trying to protect you,” ；`:245` “In my experience, things happen anyway.”；md :14 引用无误、未调换说话人（不是 Alba 说的）。
8. **「lies by omission」的出处**：`:186` “Alba mostly lies by omission.”（Caralora 语）；md :13 归给这一判断而未写成 Zach 的结论，正确。
9. **派的三次移动**：`:85` cooling racks → `:129` “We put the pies on the sideboard” → `:249` “divvy them up into Tupperware”；md :15「案板→冷却架→餐具柜→保鲜盒」的路线与原文一致。
10. **12 条词汇**：脚本逐条整串命中（`rows=12 miss=0`），含 `cumulatively`（:67）、`inculcated`（:190）、`diffident`（:103）、`heirlooms`（:108）、`crisscrossing`（:34）、`alarming clink`（:231）。
11. **未与 `Alba is 42` 相涉**：本章年龄 24/25，md 未做年龄推算。
