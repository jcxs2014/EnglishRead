# ch53 Tattoo — R5 判定

- 机器层：`bash scripts/chapter.sh "ch53 tattoo.md" --json` → rc=0，verdict `ok`
- 块数：4（未触 10 块上限；原文 1086 词）
- 原文 1086 词 / 精读 92 行（Alba 第一人称、几乎全现在时）

## 一、判定表

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 四块引语逐字 | 与 `text/ch53_tattoo.txt` L23/L62/L111/L116 逐字对齐，4/4 命中 | 真 | 跳过 |
| 抬头与年龄 | `:18` `Saturday, December 29, 1979 (Alba is 74, Oliver is 17)` | md「十二月二十九日」「七十四岁」「十七岁」一致 | 跳过 |
| 「她要扶着水池站稳」 | `:67` `I have to hold on to the sink for balance.` | 一致 | 跳过 |
| 「他坐在盖着的马桶上」 | `:40` `the closed toilet seat` | 一致 | 跳过 |
| 「抹乳液」 | `:86` `Oliver squirts lotion on his hand and rubs it into the arch of my foot` | 一致（施动者是他） | 跳过 |
| 纹身在她脚心、可有衣物遮住 | `:72` `if it was on the bottom of my foot I could cover it` | 「脚心」＝`bottom of my foot`，一致 | 跳过 |
| 「四岁那年被麻醉纹上」 | `:62` `I was four. I sat on my daddy's lap in the tattoo parlor.`／`:62` `They had to sedate me` | 一致 | 跳过 |
| 「他来自二〇四六年」 | `:86` `“May 2046.”` | 一致 | 跳过 |
| 「她来自二〇七六年」 | `:91` `“2076.”` | 一致 | 跳过 |
| 「她问他有过几次，他答一次」 | `:107` `“Once.”` | 一致 | 跳过 |
| 「她说在黑暗里两人都是最好的自己」 | `:133` `“Here in the dark, we'll be our best selves.” I turn toward him.` | 一致 | 跳过 |
| 「他问她可不可以」 | `:121` `“Alba,” he says, very quietly. “May I . . . ? Do you mind . . . ?”` | 一致（开口的是他） | 跳过 |
| 「他说不想看见世界结束，因为世界太美」 | `:165` `“I don't want to see the world end, Alba. It's too beautiful.”` | 一致 | 跳过 |
| 开门对答未收 | `:30` `I say, “Come in, I'm decent.”` ／`:31` `“I'm not,” Oliver says.` | 未收：`/usr/bin/grep -nE "decent" "ch53 tattoo.md"` 零命中 | 提示 |
| 「若不是时间旅行者不会成为情人」未收 | `:92` `If we weren't time travelers we'd never have become lovers.` | 未收：`grep -nE "时间旅行者"` 零命中 | 提示 |
| 「你会是我的大作曲家，我是你的缪斯」未收 | `:137` `“You'll be my great composer, and I'll be your muse.”` | 未收：`grep -nE "作曲家|缪斯"` 零命中 | 提示 |
| 「别告诉我任何事」未收 | `:153` `“Don't tell me anything, Alba.”` | 未收；同段 `:149` `“Not yet. Not for a long time yet. Not tonight.”` 导航第 12 行已交代「只留一句「今晚不会」」 | 提示（部分已交代） |
| 导航「失序与失去都没有被提起」 | `:116` `In his present, his parents are still alive, though he'll never see them again.` | 与 b4 及导航第 15 行自述「他的父母还活着、他的世界已是废墟」冲突 | 提示 |

## 二、报数

- **逐字**：4/4 块引语逐字命中。
- **对应**：4/4 块在讲该块引语；「冻掉双脚」归属于**她父亲**未错；「父母还活着」归属于**他的时代**未错写成已死。
- **形态**：H1 `# 53. Tattoo`；导航 5 项；子项 4 项齐；块数 4（≥ 短章下限 3；本章 1086 词 > 800，不受短章下限约束）。
- **断言**：md 内可核断言 12 条全对（日期、两处年龄、水池、马桶、乳液、脚心、四岁麻醉、二〇四六、二〇七六、只有一次、最好的自己、不愿看世界结束）；4 条漏段＋1 条导航自述冲突判提示。

## 三、已核实为正确（下一轮勿误改）

1. 「他喊名字的方式让她断定他很年轻」——`:24` `I hear Oliver shouting my name and I know he'll be very young—he used to bellow like that at first and then he quieted down.`；是**她**的判断，不是他的自述。`:111` 又有 `No wonder he came bellowing up the stairs` 与之呼应。
2. 「坐在盖着的马桶上」——`:40` `the closed toilet seat`；盖子**盖着**，不是掀开。
3. 「她让他擦脚」——`:49` `“But then I wouldn't have gotten any exercise,” I say. “Will you dry my feet?”`；她请求、他动手。
4. 「chrono-displaced 的孩子都有这种纹身」——`:61` `“That's a relic. All the chrono-displaced children used to have these tattoos.”`；「遗物」指旧时代的做法，不是「她身上的遗物」。
5. 「四岁、坐在爸爸腿上、被麻醉」——`:62`；醒来哭在 `:62` 同段，父说是「魔法数字」。
6. 「脚心而非手腕」——`:72` `He figured if it was on the bottom of my foot I could cover it; he didn't want it on my wrist where anyone could see it.`；**纹在脚底**，md 的「脚心」同义。
7. 「爸爸反对写名字地址」——`:72` `My dad objected to putting my name or address on me. He worried that I might need to lie to the police occasionally.`；理由是不必对警察说谎，不是怕被坏人利用。
8. 「他的时代扫眼睛」——`:77` `“In my time they scan your eye,”`；不是刷指纹、也不是查身份证。
9. 「他来自二〇四六年五月」——`:86` `“May 2046.”`；此前 `:86` 同段他正替她抹乳液，时间为 1979 年冬。
10. 「她来自二〇七六年」——`:91` `“2076.”`；两人年龄差被「放大」的说法紧接在 `:91`–`:92`。
11. 「她父亲冻掉双脚、她一生怕冬天」——`:111` `I think about my dad, who lost his feet to frostbite. All my life I have been frightened of winter.`；**是她父亲**，不是奥利弗的父亲。
12. 「他的父母在他自己的时代还活着，只是他再也见不到」——`:116` `In his present, his parents are still alive, though he'll never see them again.`；**没有**写成「父母已死」。
13. 「他问她可不可以」——`:121` `“Alba,” he says, very quietly. “May I . . . ? Do you mind . . . ?”`；开口的是他。接着 `:125` `My eyes fill with tears. “I didn’t think you’d want me.”` 是**她**说的（她怕自己太老），`:129` 他的回答是 `“No, it is the opposite; I must seem like a child to you. I was ashamed.”`——**两极各一句，勿把两句都归给同一人**。
14. 「在黑暗里两人都是最好的自己」——`:133` `“Here in the dark, we'll be our best selves.” I turn toward him.`；说话人是她（Alba）。
15. 「你会是我的大作曲家，我是你的缪斯」——`:137` 说话人是**他**（Oliver，接在她「你手真凉」之后）；而 `:141` `“You’ll be the brilliant pianist who makes sure there’s music at the end of the world.”` 是**她**的回应。两句各归一人，勿混。
16. 「只有一次」——`:107` `“Once.”`；问句在她（`:102`–`:107`），答句是他。
17. 「今晚不」——`:149` `“Not yet. Not for a long time yet. Not tonight.”`；说话人是她；紧接 `:153` `“Don't tell me anything, Alba.”` 是他。
18. 「不愿看世界结束」——`:165`；说话人是他，理由是「世界太美」。
