# ch44 life indoors — 判定表（R5）

- 原文：`text/ch44_life_indoors.txt`（148 行）
- 精读：`ch44 life indoors.md`（81 行）
- 机器层：`2-machine.json` rc=0（verdict=ok，3 块，segment_miss 0，empty_quote 0，struct_bad 0，keyword_bad 0，cjk_low 0，nav 5）
- 结论：**无阻断**；漏 3（提示）· 编 0 · 错 0（3 条假红）· 跳过 3

| # | 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|---|
| 1 | 3 块引语逐字、均属本章 | `2-machine.json` segments=3, segment_miss=0；回捞 `:24` `:139` `:148` 全命中 | 引语层干净 | 假红 |
| 2 | 3 块 × 四子项齐全，块 3–10 行，中位 6 | `2-machine.json` form.subitems_modal / block_range | 形态合规（本章短，3 块属正常） | 假红 |
| 3 | 日期与场景锚点正确 | `:18` “Tuesday, April 18, 2028 (Alba is 24, Oliver is 65)”；`:23` “It was raining when I arrived at the Yellow House four days ago and still raining when Oliver showed up yesterday.”；md:11「四月十八日，阴雨的黄房子」「奥利弗昨天才到」 | 正确 | 已核实为正确 |
| 4 | 「确认年份」写成对方主动报年份 | `:24` “April 18 of what year? I asked, timidly. 2028, she said, sounding more alert.” | 措辞偏松，但 md:25/27 已写明「要去打听」「确认年份之外」，块 1 略去追问属压缩 | 假红 |
| 5 | 鸽子段（「长翅膀的老鼠」/「鸽子很美，我很遗憾它们没了」）全无 | `:100` ““We call pigeons ‘rats with wings,’” I tell him.”；`:104` “The pigeons were beautiful. I’m sorry they’re gone.”；`/usr/bin/grep -c "鸽子" "ch44 life indoors.md"` → 0，rc=1 | **漏**：本章唯一的哀悼段，只余导航一句「消失的鸟」 | 提示 |
| 6 | 「AI 变成了我们／我们忘了自卫／它们对我们为所欲为」全无 | `:139` “AIs became us. We fell in love with them. We forgot to defend ourselves. They do what they please with us now.”；`grep -c "AI"`→0 | **漏**：未来衰败只剩「机器人无处不在」这一句结论，因果链丢掉 | 提示 |
| 7 | 年龄三锚点（六十五／七十几／今年八月才出生）全无 | `:121` “I ought to be sixty-five… Seventysomething? It’s funny to be in 2028. I will be born this coming August.”；`grep -c "六十五"`→0、`grep -c "八月"`→0 | **漏**：全书年龄表的关键锚点（ch45 的 1975/2041 双线靠它对齐） | 提示 |
| 8 | 方舟段（佛罗里达大沼泽地／装的是孩子／结局不好） | `:41` “A man in Florida, in the Everglades,”；`:50` ““No, children.””；`:58` ““No.””；md:13 与 md:81 已写对 | 导航已覆盖，未进块 | 跳过 |
| 9 | 「四天前到」「雨淹掉要冒头的植物」 | `:23`；`:67` “This rain is drowning any vegetation that might have been trying to emerge.” | 未收 | 跳过 |
| 10 | 「那是个多事的世纪」 | `:130` ““It’s been an eventful century.”” | 未收 | 跳过 |
| 11 | 「她先请求讲述，事后才下判断」 | `:134` ““Tell me about it,” I ask.” → `:139` 全段 → `:144` “It sounds like the end of the world” | md:12「用一个直觉判断逼出回答」指 `:148` 他接判断作答，不构成时序错 | 假红 |
| 12 | 「现在时记录」 | `:23` “It’s raining. It was raining when I arrived…” | 回忆式现在时与过去时交替，写法成立 | 假红 |
| 13 | 块 3 的两句话归属没混 | `:144` 阿尔芭：“It sounds like the end of the world”；`:148` 奥利弗：“It’s the end of one world, and the beginning of the next… Nothing ever ends, it just gives way.” | 谁判末日、谁改口为「让位」，分工正确 | 已核实为正确 |
| 14 | 「他伸出手，她把手交给他」的施动方向 | `:148` “He offers me his hand, and I give him mine.” | 正确（Oliver 先伸） | 已核实为正确 |
| 15 | 「你通常说不想知道」的推拒属奥利弗 | `:112` ““You usually say you don’t want to know, Alba.” Oliver lights a cigarette, his first of the day.” | 正确 | 已核实为正确 |
| 16 | 词汇 13 条例句逐字 | 例：`:139` “The pandemics, the fighting over resources, the change from democracies to autocracies in the West.”；`:56` “This rain is drowning any vegetation…”；`:58` “A man in Florida, in the Everglades,”；`:68` “I’ve never noticed before how long his eyelashes are.” | 全命中，无改写 | 已核实为正确 |

## 已核实为正确（防下一轮误修）

1. **「他说起小时候在电视上看到的方舟新闻」不是编的**：`:41` “It happened when I was a kid, I remember watching it on TV.” **勿删。**
2. **方舟里装的是「孩子」，不是动物**：`:50` ““No, children.””——这是本章黑色幽默的核心（诺亚装动物、这个人装孩子），**勿按常识改成动物**。
3. **「结局不好」是原文**：`:58` “Oliver looks as though he’s sorry he brought it up. “No.”” **勿改成「结局不明」。**
4. **年龄「该是六十五」是奥利弗自述的账面年龄，不是叙述者判定**：`:121` “I ought to be sixty-five.” 头部信息 `:18` 也写 “Oliver is 65”。**两处都成立，勿以一处改另一处**；他本人随后又说「七十几吧」（因常年不在自己时代）。
5. **「今年八月我才会出生」是原文**：`:121` “I will be born this coming August.”——2028 年 4 月他尚未出生，此行是回溯。**勿改成「他 2028 年 65 岁」。**
6. **「伦敦没有鸟，连鸽子也没有」是原文**：`:88` ““No.””（birds）、`:96` ““Sorry, no.””（pigeons）。**勿改成「鸟变少了」。**
7. **「卡拉 OK 意为空乐队」的释义与原文一致**：`:139` “The Japanese word karaoke means ‘empty orchestra.’”→ md:31「空荡荡的乐队」。**勿改译「空管弦乐」。**
8. **「一个世界结束、另一个开始，没有东西真的结束，只是让位」是奥利弗说的**：`:148`。**勿把这句转给阿尔芭。**
9. **「雨势在减弱」是结尾最后一句**：`:148` “Look, I think the rain is letting up a bit.”——它是全章唯一一处「转好」的信号，md:15 说「结尾不写结论，只写…一句关于雨势的话」是对的。**勿删。**
