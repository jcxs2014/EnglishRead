# ch11 Thanksgiving — 判定（R5）

- 机器层：`bash scripts/chapter.sh "…/ch11 thanksgiving.md" --json` → **rc=0**，verdict=ok，块数 9、words 3570、segments 9、查无 0、空引号 0、子项缺 0、关键词缺 0、形态偏离 0，`issues` 全空。
- 素读锚点：8/8 命中（`facts= 8 bad= 0`）。
- 报数：**逐字 0 / 对应 0 / 形态 0 / 断言 0 阻断、11 提示**（漏 7、错 4）。

## 判定表

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 漏：Beck「一夜没睡，Isadora 闹脾气」这处最早的伏笔 | `text/ch11_thanksgiving.txt:119` “When we arrived at eleven she was still wearing pajamas and had her hair wrapped… Beck quietly said, I’ve been up all night, Isadora’s being a brat” | `grep -c -F "Isadora 闹脾气"` = **0**；`grep -c -F "brat"` 唯一命中是 :59 引语里 `celebrated` 的字母串，非原词。:14 只有「疲惫」 | 提示 |
| 漏：无酒精蔓越莓 shrub（生蛋白／玫瑰果利口酒／替 Lucinda 留不含酒的份） | `:103` “a nonalcoholic cranberry shrub (made by Gomez and Charisse… using raw egg whites, plus rose hip liqueur and vodka for anyone who isn’t Lucinda)” | `grep -c -F "shrub"` = **0**、`"蔓越莓"` = **0** | 提示 |
| 漏：敬酒词点名 Henry；Rosa 回忆 Henry（七岁丧父、刻南瓜、把小孩当 short adults） | `:210` ““To Henry,” says Charisse, raising her glass, “and all our absent friends and family.””；`:206` “I was seven when he died. I remember we used to carve pumpkins here every year… He always treated us like short adults.” | `grep -c -F "Rosa"` = **0**；`grep -c -F "Henry"` = **1**，唯一命中在 :133 词汇例句。正文无 Henry 之名 | 提示 |
| 漏：Clare 拿出 Kimy 的旧食谱笔记本（另有一本 Henry 母亲的、’60 年代罐头汤与 Jell-O） | `:201` “then returns with a battered composition notebook. “These were Kimy’s,” Clare says.” | `grep -c -F "食谱"` = **0** | 提示 |
| 漏：车里摊牌后的斗嘴（Pandora／nemesis／spanking／「she actually sounds kind of fun」） | `:305` “I’m going to start calling you Pandora.”；`:311` “Maybe Isadora should be wary of me.”；`:319` “I could become Isadora’s nemesis.”；`:323` “Isadora doesn’t need a nemesis, she needs a spanking.”；`:327` “She actually sounds kind of fun,” | `grep -c -F "Pandora"` = **0**、`"nemesis"` = **0** | 提示 |
| 漏：Alba 当众把他拽进旧卧室、Beck「Oh, to be young」 | `:224` “she leads me into her old bedroom—behind us there is a delayed reaction, nervous laughter; Beck says, “Oh, to be young,”” | `grep -c -F "to be young"` = **0**、`"旧卧室"` = **0** | 提示 |
| 漏：地下室唱的曲子是「Wild thing, you make my heart sing」，用 Ella 的爵士腔唱车库摇滚 | `:210` “I hear a radio playing in the basement, an uncanny voice that reminds me of Ella Fitzgerald singing with her big band: Wild thing, you make my heart sing” | `grep -c -F "Wild thing"` = **0**；:13 只写「像 Ella Fitzgerald 的歌声」（曲名错配这层丢失） | 提示 |
| 错：:14「说出口的诉求只有一句」 | `:265` “Why do you keep secrets from me?”；`:274` “What’s in your parents’ basement?”；`:282` “Why am I the only person you know who thought Isadora was a human being?”；`:344` “I just hate being the last to know.” | 一路问了四句，最后那句只是收束；「只有一句」削得太狠 | 提示 |
| 错：:12「她要他别问，他就真的不问，然后自己去收拾那张案板上的派皮」 | `:72` “I fold the piecrust gently over itself… “Do you do that a lot?” I ask her.”；`:85` “I can tell that she just wants me to let it drop, so I do.” | 顺序颠倒：他是**一边擀第四张派皮一边问**，等她答完才放过；「她要他别问」也是转述（warily／small voice），她并未开口要求 | 提示 |
| 错：:15「每一段都从一个具体动作切入（擀派皮、抱柴、熄火）」 | `:23` “Zach: Alba and I have been teaching ourselves to cook.”（习惯陈述）；`:147` “Caralora comes in the back door with a bundle of firewood.”（第二段中腰，且是别人进来） | 三段只有第三段（`:291` 熄火）符合 | 提示 |
| 错：「a couple of weeks」被放宽成「几个星期」 | `:67` “I was there for a **couple of weeks** just now” | md 四处同源：:11「撑了几个星期」、:140 同、:51「待了几个星期」、:55「她说『几个星期』」、:57「几个星期对上几分钟」；`grep -n -F "几个星期"` 共 7 行命中共 4 行属此错（:101／:105 指 Berg 协奏曲 “for weeks”，正确，勿改） | 提示 |
| 9 块 R4 对应 | `3-diff.md` 第四节 | 三问全过；块 7 的「三条件分层」、块 9 的 retreat 判断为全章最佳 | 假红（核后成立） |
| 12 条词汇 | 脚本整串比对 `rows=12 miss=0` | 逐字无误、未跨章 | 假红（核后成立） |
| 抬头 `Alba is 24, Zach is 25` | `:18` “Wednesday, November 26, 2025, and Thursday, November 27, 2025 (Alba is 24, Zach is 25)” | 原书原文；2025-11-26 确为周三、11-27 为周四；md「11 月 26 日深夜」指午夜烤派，正确；未做年龄外推 | 假红（按派工方口径延伸） |

## 处置建议（只报不改，按性价比排序）

1. **E4 量词**：四处「几个星期」改「两个星期左右」；:57 改后「两周对上几分钟」比原句更狠。
2. **E1 与 L5 一起修**：:14 的「诉求只有一句」改「他问了一路」，并把车里那段斗嘴压成一句（「Alba 说要开始叫他 Pandora，他说也许该反过来、让 Isadora 提防他」）——这一改同时把 :14 的断言和 L5 的空白补上，且是下一章他去见 Isadora 的动机。
3. **L7**：:13 补曲名半句「唱的是 Wild thing, you make my heart sing」——诡异感全在「爵士嗓音唱车库摇滚」，不补这句，「没什么不对却让人发毛」就悬空。
4. **L3／L4 合并成一句**：在 :13 的「一家人举杯敬不在场的人」后面接「敬的是 Henry——那天 Rosa 说起他七岁时教他们刻南瓜、把小孩当大人；Clare 还翻出 Kimy 的食谱本」。Henry 与 Kimy 是这本书前几章的两条根，本章正是收口处。
5. **E2／E3**：改两处时序与断句即可，不动结论。
6. **L1／L2／L6** 可不动；若要省字数，优先保 L1（一句话）、舍 L2（酒水单）。

## 已核实为正确

- **日期与年龄**：`:18` “Wednesday, November 26, 2025, and Thursday, November 27, 2025 (Alba is 24, Zach is 25)”；2025-11-26 是周三，11-27 是周四；与 ch10（24/24）自洽。
- **四个派与时序**：`:23` “two pies in the oven and two under construction”；`:28` “pumpkin, apple, sweet potato and rhubarb”；md「四个派」及四种口味全对。
- **「带派去 Alba 家」的方向**：`:23` “bringing pies to Alba’s family’s Thanksgiving”；md 未把方向反过来。
- **Isadora 的命名**：`:156` “She’s named after Beck’s daughter, who was stillborn.”；md 三处一致，未写成「Beck 的女儿还活着」。
- **禁令的两层**：`:165` “offline, top secret, not allowed to meet any new people… especially not allowed to meet you”；md :11／:14 分层正确。
- **Beck 的三重身份**：`:113` “an artist, computer programmer and professor”；与 :14「守门人」不冲突。
- **Clare 的两句台词**：`:237` “She’s trying to protect you,”；`:245` “In my experience, things happen anyway.”；说话人未调换（不是 Alba 说的）。
- **「lies by omission」出处**：`:186` “Alba mostly lies by omission.”（Caralora 语，:175 还有 “she probably never told you any actual untruths”）；md :13 用作判断而非 Zach 的结论，正确。
- **派的三次移动**：`:85` cooling racks → `:129` “We put the pies on the sideboard” → `:249` “divvy them up into Tupperware”；md :15 的路线与原文一致。
- **12 条词汇**：全部落本章（`miss=0`），含 `cumulatively`／`inculcated`／`diffident`／`heirlooms`／`crisscrossing`／`alarming clink`（原文为 alarming clink）。
- **未与 `Alba is 42` 相涉**：本章 24/25，md 无年龄推算。
