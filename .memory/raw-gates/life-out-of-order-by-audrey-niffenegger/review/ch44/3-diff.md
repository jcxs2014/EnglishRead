# ch44 life indoors — 对账单（R3）

- 原文：`text/ch44_life_indoors.txt`（148 行，实际正文即一场厨房对话）
- 精读：`ch44 life indoors.md`（81 行）
- 机器层：`2-machine.json` rc=0，verdict=ok，3 块 / 3 段引语全逐字，empty_quote 0，struct_bad 0，keyword_bad 0，cjk_low 0，nav 5 条，H1 `44. Life Indoors`，words 735，block_hint 目标 2 块、实写 3 块（未超上限）

## 一、漏（素读有、md 无）

| # | 素读条目 | 原文 | md 侧 | 档 |
|---|---|---|---|---|
| L1 | 鸽子段整段未进正文：他们把鸽子叫「长翅膀的老鼠」；Oliver 说他们老鼠多得是、庆幸老鼠没长翅膀；「鸽子很美，我很遗憾它们没了」；Alba 追问「那么多怎么会全没了」 | `:100` ““We call pigeons ‘rats with wings,’” I tell him.”；`:104` ““We have plenty of rats. I’m glad they don’t have wings.” Oliver frowns. “The pigeons were beautiful. I’m sorry they’re gone.””；`:108` ““All gone? There are so many of them. How can they all be gone?”” | `grep -c "鸽子"`→0、`grep -c "老鼠"`→0；导航只有一句「伦敦消失的鸟」（`md:11`）、「承认自己怀念鸟」（`md:14`） | 提示（本章最有分量的一段哀悼被压成一句概括） |
| L2 | 「AI 变成了我们」那三句未落地 | `:139` “Robots are everywhere. Some of them are so small you can’t see them, some of them are inside our bodies. AIs became us. We fell in love with them. We forgot to defend ourselves. They do what they please with us now.” | `grep -c "AI"`→0、`grep -c "人工智能"`→0；`md:11` 只写「机器人无处不在，合成体验压过真实」 | 提示（未来衰败的因果链被省略，只剩结论） |
| L3 | 年龄三锚点全无：自称「该是六十五」/「七十几吧」/「今年八月我才会出生」 | `:121` ““I don’t know. I ought to be sixty-five. But I’ve spent so much time out of my own time . . . it’s impossible to say. Seventysomething? It’s funny to be in 2028. I will be born this coming August.”” | `grep -c "六十五"`→0、`grep -c "七十几"`→0、`grep -c "八月"`→0；`md:11` 只留「说不清自己多少岁」 | 提示（全书年龄表的关键锚点，ch45 的 1975/2041 双线全靠它对齐；建议补数字） |
| L4 | 方舟细节（佛罗里达大沼泽地、装的不是鳄鱼是孩子、结局不好） | `:41-58` “A man in Florida, in the Everglades…”“No, children.”“Did it end well?”…“No.” | 未进引语块，但 `md:13`「方舟这个意象也被兑现——船里装的是孩子，结局不好」与 `md:81` 一句话总结都已写对 | 跳过（导航已覆盖，非关键事件） |
| L5 | 「四天前到黄房子」与「这场雨把想冒头的植物都淹了」 | `:23` “It was raining when I arrived at the Yellow House four days ago”；`:67` “This rain is drowning any vegetation that might have been trying to emerge.” | `grep -c "四天"`→0；vegetation 只作词汇例句入选（`md:56`） | 跳过（氛围细节，`md:81`「雨从…那天起就没停过」已承接） |
| L6 | 「那是个多事的世纪」（It’s been an eventful century） | `:130` | 未收 | 跳过（过场应答） |

## 二、编（md 有、原文无）

无。逐项回查：`md:11`「他说起小时候看过的方舟新闻」有 `:41` “It happened when I was a kid, I remember watching it on TV.”；`md:12`「他先推拒」有 `:112` “You usually say you don’t want to know, Alba.”；`md:13`「船里装的是孩子，结局不好」有 `:50`/`:58`；`md:14`「承认自己怀念鸟」有 `:104`。

## 三、错（两边都有但不一致）

无对照级错。三处需记账的近似点：

| # | 断言位置 | md 写法 | 原文 | 判 |
|---|---|---|---|---|
| E1 | `md:11` 一句话概括 | 「阿尔芭打电话到图书馆，**确认年份是二〇二八年**」 | `:24` “April 18 of what year? I asked, timidly. 2028, she said, sounding more alert.”——年份是她**追问**出来的，不是对方主动报的；且原文刻意先给「四月十八日」不给年 | 假红（md:11「确认」、`md:25`「时间…是要去打听的消息」、`md:27`「确认年份之外」都已写明追问性质；块 1 的中文理解略去追问，但导航补上了） |
| E2 | `md:12` 情感弧线 | 「阿尔芭…最后**用一个直觉判断逼出回答**」 | 次序是 `:134` ““Tell me about it,” I ask.”（她先请求）→ `:139` Oliver 全段讲述 → `:144` “It sounds like the end of the world”（她事后判断） | 假红（「逼出回答」指的是 `:148` 他接下这句判断作答，与原文不冲突；仅措辞偏紧） |
| E3 | `md:15` 叙事手法 | 「阿尔芭用第一人称**现在时**记录」 | `:23` “It’s raining. It was raining when I arrived…”；`:24` “I called… asked…”（过去时） | 假红（现在时与过去时交替，是回忆式现在时；不作错判） |

## 四、归属方向复核（R4 三问）

- 块 1 “I called the library reference desk…” ⇄ `:24`：施事＝**阿尔芭**（I called），受事＝图书馆参考咨询台；md `:21`「阿尔芭早上给图书馆的参考咨询台打电话」——方向正确。
- 块 2 “In my time, people long for escape.” ⇄ `:139`：说话人是**奥利弗**（对阿尔芭讲他的时代），不是阿尔芭转述；md `:31`「奥利弗说」——正确。
- 块 3 “It’s the end of one world…” ⇄ `:148`：回答者是**奥利弗**，提问/判断者是阿尔芭（`:144` “It sounds like the end of the world”）；md `:41`「阿尔芭说这听起来像世界末日，奥利弗回答」——方向正确，未把两句并作一人。
- 「他伸出手，她把手交给他」⇄ `:148` “He offers me his hand, and I give him mine.”——施动方向正确（Oliver 先伸）。
- 「奥利弗昨天才到」⇄ `:23` “still raining when Oliver showed up yesterday”——正确。
- 「他点起一支烟，承认算不清多少岁」⇄ `:112`（first cigarette of the day）→ `:121`（年龄）——先后正确。
