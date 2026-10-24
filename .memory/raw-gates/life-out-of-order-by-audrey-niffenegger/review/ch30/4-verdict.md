# ch30 chance encounter — 判定表（R5）

- 原文 230 行 / 精读 101 行；机器层 `2-machine.json` rc=0（verdict=ok，5 块 5 引语全逐字，零 issue）
- 报数四组：**逐字 5/5 通 · 对应 5/5 通 · 形态 通（H1 `30. Chance Encounter`／导航 5 条／子项四件齐）· 断言 漏 1 提示 · 编 0 · 错 0 阻断、1 提示**

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 块 1 引语逐字、且「琴声先于看见人」的顺序未被改写 | `text/ch30_chance_encounter.txt:24` “As I walk toward the house, I realize that many of the windows are open; intricate music spills into the garden. I see a man sitting at the piano in the living room. I don’t think he notices me.” | 成立 | 已核实 |
| 块 2 的「十几岁的阿尔芭」有原文支点，非改写年龄 | `text/ch30_chance_encounter.txt:41` “…one of Henry’s old CBGB’s T-shirts that teenage Alba likes to sleep in” | 成立（原文自身与 `:105` “Eight.” 冲突，md 按原文写「十几岁」是对的） | 假红（若下一轮以「与八岁矛盾」报错，即误修） |
| 块 3 中文理解掺入引语外的「在男厕刮胡子」 | 引语见 `:109` “Then the police came and asked him…he said no…covered in blood.”；「刮胡子」在同段前句 `:109` “He was in the men’s room, shaving…” | 引语选短一格，事实无误 | 提示 |
| 块 4 的「她更年长、他更年轻」方向 | `text/ch30_chance_encounter.txt:171` “It’s only that I’ve met you before, when you were much older, and I was somewhat younger.” | 成立（方向未颠倒） | 已核实 |
| 块 5「贝克必须是教纳迪娅的那个人」的施受关系 | `text/ch30_chance_encounter.txt:207` “lives depend on Beck being the one to teach Nadia” | 成立（施事 Beck／受事 Nadia） | 已核实 |
| 导航与一句话总结称「他握过她的手就消失了」 | `text/ch30_chance_encounter.txt:225` “He holds out his hand and I hurry to take it—I tread on some of the sheet music—and he vanishes.” | 成立 | 已核实 |
| 章末「读完《Harriet the Spy》问女儿有没有见过叫 Oliver 的人」未进块、未进导航 | `text/ch30_chance_encounter.txt:229` “In the evening, after we’ve read a few chapters from Harriet the Spy, as Alba is falling asleep, I ask her if she’s ever met anyone named Oliver, and she grumpily reminds me that there are two boys in her class with that name. I leave it at that.” | 非转折，属余味；md 未收 | 提示 |
| 「他本名不是这个」这一身份信息未进块／导航 | `text/ch30_chance_encounter.txt:184` ““Is that your real name?” … “It wasn’t, originally, but it is now.”” | 未收，属取舍 | 提示 |
| 情感弧线「直到『有人命系于此』，她笑不出来了」 | `text/ch30_chance_encounter.txt:193` “This is so unexpected that I laugh, but Oliver doesn’t.”；`:212` “I don’t want to know whose lives he means.” | 原文未写「笑不出来」，属解读 | 跳过 |
| 词汇表 13 条例句逐字 | `:50` shelf-stable／`:72` asymmetrical／`:207` facilitate／`:117` self-absorbed／`:24` intricate·back door·discretion／`:97` unearned／`:109` stranded／`:145` premature／`:127` housemates／`:24` grocery store／`:41` friendly | 全部逐字命中 | 已核实 |
| 抬头日期「八月二日」落进导航与总结 | `text/ch30_chance_encounter.txt:18` “Monday, August 2, 2010 (Clare is 39, Oliver is 59)” | 成立 | 已核实 |

## 已核实为正确（防下一轮误修）

1. 「十几岁的阿尔芭」不是缺陷。`text/ch30_chance_encounter.txt:41` 原文逐字为 “that teenage Alba likes to sleep in”；同章 `:105` Clare 又说 “Eight.”。⇒ 原文自相矛盾，精读照 `:41` 写字面，**不得改成「八岁」也不得删掉「十几岁」**。
2. 块 2「他穿楼上壁橱的亚麻长裤」= 原文 “linen trousers from the closet upstairs”（`:41`），不是「衣柜里的旧衣」泛写。
3. 块 4「别把这次见面告诉阿尔芭」是 **Oliver 求 Clare**，不是 Clare 求 Oliver（`:171` “I hope you won’t mention this to Alba?”）。
4. 托付的路径方向：**Oliver 要 Clare 去促成 Beck 教 Nadia**，且明说「由阿尔芭转达也可以，但由你开口更自然」（`:207`），未写成「Clare 替 Alba 答应」。
5. 结尾「事情兜了一圈回到原处」有原文支点：`:230` “Things have come full circle.”（原文此句为 Clare 心理独白，非 Oliver 台词）。
6. 机器层 rc=0 是真通过：`bash scripts/chapter.sh "…/ch30 chance encounter.md" --json` 退出码 0，counts 全零。
