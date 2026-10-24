# ch50 First Kiss — R5 判定

- 机器层：`bash scripts/chapter.sh "ch50 first kiss.md" --json` → rc=0，verdict `ok`
- 块数：8（本书上限 10，未触顶；71 章中位 6）
- 原文 3051 词 / 精读 132 行（Alba 第一人称；与 ch49 同名但为不同章）

## 一、判定表

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 八块引语逐字 | 与 `text/ch50_first_kiss.txt` L23/L34/L39/L61/L163/L216/L300/L453 逐字对齐，8/8 命中 | 真 | 跳过 |
| 抬头与年龄 | `:18` `Thursday, May 30, 1996 (Alba is 25, Oliver is 30)` | md「五月三十日」「二十五岁的阿尔芭」一致 | 跳过 |
| 导航「被人从车上追下来」 | `:39` `“A man chased me,” I begin. “He was in a car, and when I ran into someone's backyard he chased me on foot and I had to climb a fence…”` | 一致（车→步行追→翻栅栏） | 跳过 |
| 导航「脚上扎满了玻璃碴」 | `:61` `my feet are covered in cuts and tiny punctures. I must have run across glass.` | 一致 | 跳过 |
| 导航「他检查伤口」 | `:43` `“Your feet are a mess,” he informs me.` | 一致 | 跳过 |
| 导航「放洗澡水」 | `:61` `he stands up heavily and goes to the bathroom and runs the hot water for my bath` | 一致 | 跳过 |
| 导航「在楼下弹披头士和萨蒂」 | `:61` `he plays the beginning of The Beatles' “Good Day Sunshine” and then embarks upon Erik Satie's Vexations until I shout, “Oliver!” and he veers into The Gymnopédies` | 一致（三首均实有） | 跳过 |
| 导航「年长的她要求他去结识扎克」 | `:240` `the main task you assigned me was to meet Zach, ingratiate myself with him, become as intimate as possible without revealing anything much…` | 一致（施动者＝年长的 Alba） | 跳过 |
| 导航「承认自己像间谍」 | `:273` `My difficulty is to avoid slipping up and telling him anything about my real life, with you. I'm a spy.` | 一致 | 跳过 |
| 导航「她发现奥利弗对扎克有说不清的吸引」 | `:216` `I don't like it that the person he's problematically attracted to is Zach.` | 一致（吸引方向＝他对扎克） | 跳过 |
| 「他说那是他的初吻，在厨房洗碗时」 | `:157` `“That was my first kiss.” … “It was in the kitchen. We were washing dishes, and then you kissed me.”` | 一致；与 ch49 的洗碗场景互证 | 跳过 |
| 「No. Not yet.」 | `:168` `“No. Not yet.”` | 一致（她问是否已吻过他第一次） | 跳过 |
| 赌约收尾 | `:453` `He stubs out his cigarette and says, “I double dare you,” and this time I kiss him properly, and mean it. I knew I would, sooner or later.` | 一致（先「I dare you」后「double dare」） | 跳过 |
| 血脚印未收 | `:34` `There are bloody footprints on the rug, dark against the pale green wool.` | 未进块、导航未提 | 提示 |
| 章鱼之争未收 | `:90` `“No, it's really octopuses. I looked it up once.”` | 未收 | 提示 |
| 伊莎多拉是 AI（底特律出生、芝加哥一起长大、`guǐfù`） | `:352` `“Isadora was born in Detroit, and I grew up with her in Chicago.”`／`:360` `“No. She's an artificial intelligence.”`／`:364` `“Really?! She is guǐfù!”` | 未收（b7 只写「赞助人」） | 提示 |
| `His. And mine.` 未收 | `:256` `“His. And mine.”` | 未收 | 提示 |
| 玛德琳年近八十、2006 年前后停止 | `:406` `In Oliver's present, she's nearly eighty.`／`:407` `and then, around 2006, she just stopped` | 未收 | 提示 |
| b4 中文「他说，快有一道界线要到了」 | `:61` `There is a border coming soon, an invisible barrier between yes and no, but today he is yes and I am no` —— 该句**无引号**，是阿尔芭的叙述 | 把叙述归成他的话 | 提示 |

## 二、报数

- **逐字**：8/8 块引语逐字命中，0 偏差（b7 起于引号内 `She helped me to emigrate`，未吞前文）。
- **对应**：8/8 块中文在讲该块引语；b2 的 `compose yourself` 双关讲对，b8 两次吻的强弱对比讲对。
- **形态**：H1 `# 50. First Kiss`；导航 5 项；子项 4 项齐；块数 8（未触 10 块上限）。
- **断言**：导航 8 条事实性断言逐条有原文（见上表），0 编 0 错；5 条漏段与 1 条归属表述判提示。

## 三、已核实为正确（下一轮勿误改）

1. 本章是**阿尔芭**的第一人称（首句 `Alba:`），与 ch49 的 Oliver 视角不同；两章同名「First Kiss」但分属不同时间线（ch49＝1998 她 40 他 17；ch50＝1996 她 25 他 30）。
2. 「被人从车上追下来」——`:39` 原文先说车、再说下车步行追，md 未把顺序写反。
3. 「在楼下弹披头士和萨蒂」——`:61` 三首（`Good Day Sunshine`→`Vexations`→`Gymnopédies`）全在，不是编的。
4. 「年长的她要求他去结识扎克」——`:240` `the main task you assigned me was to meet Zach, ingratiate myself…`，指派者是他口中的「你」＝年长的 Alba。
5. 「他承认自己像间谍」——`:273` `I'm a spy.`；下一句她还回 `We're both spies.`（`:278`），若下一轮要补，可补这一句。
6. 「他记得她四十岁生日那天在厨房洗碗时被她吻过、那是他的初吻」——`:157` `“That was my first kiss.” … “It was in the kitchen. We were washing dishes, and then you kissed me.”`。本章**未**给出他当时的岁数：命令 `/usr/bin/grep -nE "seventeen" ch50_first_kiss.txt` 无命中（exit=1）；他当时 17 岁只能由 ch49 抬头 `:18` 推得，故本块引文不要补「十七岁」。
7. 「No. Not yet.」——`:168`，回答的是「我（按最早那一次算）是不是已经吻过你了」。
8. 「I dare you / I double dare you」的先后——`:453` 前有他先说的 `“I dare you,”`，她飞快吻一下，他才说 `I double dare you`；md「他两次说『我敢你』」的「两次」成立。
9. 「他 30 她 25，不同年代」——`:61` `“Ah. I'm thirty. We're in different eras.”`。
10. 「她注意破伤风疫苗，所以不太担心」——`:61` `I am careful about vaccinations, especially tetanus, so I'm not too concerned.`
