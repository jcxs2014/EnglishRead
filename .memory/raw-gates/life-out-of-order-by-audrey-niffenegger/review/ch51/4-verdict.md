# ch51 Random Acts of Randomness — R5 判定

- 机器层：`bash scripts/chapter.sh "ch51 random acts of randomness.md" --json` → rc=0，verdict `ok`
- 块数：6（未触 10 块上限）
- 原文 2144 词 / 精读 112 行；双第一人称接力（前半 `Oliver:`，后半 `Zach:`）

## 一、判定表

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 六块引语逐字 | 与 `text/ch51_random_acts_of_randomness.txt` L23/L29/L112/L119/L135/L287 逐字对齐，6/6 命中 | 真 | 跳过 |
| 抬头与年龄 | `:18` `Monday, September 1, 2036 (Zach is 35, Oliver is 31)` | md「二〇三六年九月一日」一致 | 跳过 |
| 导航「前半由奥利弗讲…后半由扎克接着讲」 | `:23` 以 `Oliver:` 起头；`:190` 起以 `Zach:` 起头 | 一致 | 跳过 |
| 「枪击过去几个月」 | `:23` `the shooting at the Haymarket memorial was just a few months ago` | 一致 | 跳过 |
| 「提着空购物袋去超市」「半路被扎克叫住」 | `:29` `Now I'm walking down Lincoln Avenue with my empty shopping bags, headed for Trader Joe's, when I hear someone call out “Oliver!”` | 一致 | 跳过 |
| 「街角酒吧坐下喝酒」（橡树下、天热） | `:44` `There's a bar on the corner, and we are led to an outdoor table under the shade of a huge oak` | 一致 | 跳过 |
| 「扎克为戈麦斯的死追问天意，说宇宙不过是些随机事件」 | `:112` `the universe consists of random acts of randomness`；`:94` `“It seemed too providential to be random,” Zach says` | 一致（立场归扎克，未归给奥利弗） | 跳过 |
| 「奥利弗答以音乐，说艺术增加的是喜悦的总量」 | `:119` `“It's like music—people ask what art is for; I think it adds to the sum total of joy, and joy is good. Music offsets evil…”` | 一致 | 跳过 |
| 「卡萝拉随后到场」「同桌三人合起来就是阿尔芭全部的情爱」 | `:124` `“Caralora, there you are.”`；`:135` `the three of us at this table represent Alba's entire erotic life` | 一致 | 跳过 |
| 「几周后扎克不再追问，把这个查无此人的人留在身边当朋友」 | `:332` `She says she got nowhere: Oliver is officially a phantom.`；章末 `He's my friend. I want that to be enough.` | 一致 | 跳过 |
| 阿尔芭预先告知枪击全过程、他像照本的演员 | `:23` `Alba told me exactly how the shooting would unfold, told me what to say, what to do, what to expect`／`:24` `I moved through it as an unhappy actor, with my dialogue and actions laid out for me like immutable laws of nature` | md 全无：命令 `/usr/bin/grep -nE "预先|演员|告诉他会|照本|unfold" "ch51 random acts of randomness.md"` 仅命中「预先表态」一处（无关），exit=0 | 提示（建议补） |
| `You look familiar` 未收 | `:140` `She squints at me, gives me the once-over. “You look familiar.”` | 未收 | 提示 |
| 派对邀约＋他谎称烧烤带 coleslaw 未收 | `:171` `“We're having a Labor Day party at the ward office tonight, you should come by…”` | md 全无：命令 `/usr/bin/grep -nE "冷冻|冰淇淋|派对|coleslaw|烧烤|选中" "ch51 random acts of randomness.md"` 无命中，exit=1 | 提示 |
| 冷冻柜前站到「实体稳固」未收 | `:185` `I arrive at the grocery store panting and panicked, and spend a long time in the frozen food aisle` | 同上 grep（exit=1） | 提示 |
| 扎克梦见戈麦斯转身不理 | `:75` `“He won't talk to me. He turns his back.”` | 未收 | 提示 |
| 一句话概括「几周后又替扎克去查」 | `:309` `“You're going to get us all killed, mister… Let me try.”`／`:332` `She says she got nowhere` | 去查由卡萝拉自请，非扎克委托 | 提示 |
| b3 引语起于 `“Exactly,”` | `:112` 该句为扎克对奥利弗上一问的应答（`:94`） | 引语选短，上文未交代 | 提示 |

## 二、报数

- **逐字**：6/6 块引语逐字命中，0 偏差。
- **对应**：6/6 块在讲该块引语；随机/音乐两方立场未对调；扎克段与奥利弗段的归属正确（章末「朋友」是扎克的话）。
- **形态**：H1 `# 51. Random Acts of Randomness`；导航 5 项；子项 4 项齐；块数 6。
- **断言**：导航与总结中可核断言 9 条全对（日期、两处年龄、酒吧/橡树、Pimm's、救命名谢、三人关系、查无此人、妻子住此、几年之交）；6 条漏段＋2 条表述判提示。

## 三、已核实为正确（下一轮勿误改）

1. 本章「前半 Oliver、后半 Zach」的接力结构——`:23` 与 `:190` 的说话人标记；**不要合并成单一叙述者**。
2. 「二〇三六年九月一日」是**劳动节**——`:18` 后文 `:171` 有 `Labor Day party`，节日名成立。
3. 「扎克 35、奥利弗 31」——`:18`；md 摘要未写具体年龄，不构成错。
4. 「戈麦斯」是那位市议员，被枪杀——`:75` `“He won't talk to me. He turns his back.”`（梦）与 `:23` `save both Zach and Gomez`；**不是奥利弗的亲人**。
5. 「音乐抵消恶，我们把喜悦储存起来对付坏日子」——`:119` `Music offsets evil. We store up joy against bad times.`，因果方向正确。
6. 「卡萝拉金发、宽檐帽、像 Dorothy Lamour」——`:124`；**她是阿尔芭的情人，不是扎克的妻子**（`:135` 三人＝她的情爱生活）。
7. 「查无此人（officially a phantom）」——`:332`，说话人卡萝拉、转述者扎克。
8. 「他住伦敦、妻子住在这里」——`:297` `“London. His wife lives here, he just visits.”`；「妻子」＝阿尔芭，md 未点破，不算错。
9. 「他离开得快，是为避免在原地留下一堆衣服」——`:152`；这是本章唯一的解释性旁白，md 的「再一次练习对熟人隐瞒」并未与之冲突。
