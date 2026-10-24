# ch61 A Lady in a Burnt Garden — R3 差异 / R4 逐块

- md：`notes/books/novels/life-out-of-order-by-audrey-niffenegger/ch61 a lady in a burnt garden.md`
- text：`notes/books/novels/life-out-of-order-by-audrey-niffenegger/text/ch61_a_lady_in_a_burnt_garden.txt`（仅 31 行，全章逐字读完）
- 素读底稿：`review/ch61/1-suread.json`；机器层：`review/ch61/2-machine.json`（rc=0, 4 块）
- 章首：`text/ch61_a_lady_in_a_burnt_garden.txt:18`「Friday, May 1, 2065 (Alba is 40)」——md `:11` 写「二〇六五年五月一日，四十岁的阿尔芭」，相符

## R3-1 漏（素读有、md 无）

| # | 素读事实 | 原文（逐字 + 位置） | md 侧 | 判定 |
|---|---|---|---|---|
| L1 | 全章只有一处情感判断句夹在残骸清单里：「So much loss.」（这么多失去） | `:31`「I didn’t know I loved the Yellow House until it was gone. So much loss. I kneel in the grass and wait to disappear.」 | 引语 `:49` 用省略号跳过这句：「…until it was gone. … I kneel in the grass」，中文理解 `:51` 也只译「直到它没了」→「随后她跪进草里」；`为什么这样写` `:55` 未提 | **提示**（省略号是显式标记，不犯逐字；但这句是全章唯一一句直白的哀悼词，跳过后读者的情绪落点只剩「等她消失」，语气比原文轻） |
| L2 | 地下室的洞：黑水、半烧过、认不出原形的漂浮物 | `:24`「The hole that was the basement is full of black water and half burned, unrecognizable floating objects.」 | 导航 `:11` 写「地下室灌满黑水」✓；但四个块内无此句（`unrecognizable` 只出现在词汇表 `:65`） | 不成立（导航已交代，属概述层） |

> 结论：本章**无阻断级漏**。原文正文只有 4 个自然段（`:23`／`:24`／`:25`／`:30–31`），md 的四个块＋导航把每一段的要点都收进了：没有房子→往里塌的残骸清单→街区废墟与树桩送葬人→雨声与自白。

## R3-2 编（md 有、原文无）

| # | md 断言（逐字） | 原文核对 | 判定 |
|---|---|---|---|
| B1 | `:47` 读者视角提示「也留意雨越下越大，她一直站在雨里，没躲；**冷是后来才轮到她去感觉的**。」 | 全文检索无任何冷觉词：`/usr/bin/grep -nEi "cold|chill|freez" text/ch61_a_lady_in_a_burnt_garden.txt` → **无输出，EXIT=1** | **提示（编）**：原文既没写她冷，也没写「冷要等到后来」；这是 md 自己补的物理感受。不升阻断，因为它是读者提示层的推测、不构成情节/关系/数字的虚构 |
| B2 | `:15` 叙事手法「中间插进一句琴声的碎片，**声音刚回来就被雨声盖掉**」 | `:30`「Fragments of music here and there. The rain makes a hissing sound as it touches the embers.」 | 提示：原文是并置两句，没有「被盖掉」的因果；且「Fragments of music」在原句 4 的引语之外，属分析用到句外 |
| B3 | `:27`「而她认出的头一件大东西是琴，声音这条线从这里就接上了」 | `:23`「here is Oliver’s piano, collapsed and all the wires sprung loose」——琴之前还点了 bowl、clock | 提示（轻）：「头一件**大东西**」说法成立（小物件在前），但「声音这条线」是 md 的连线，原文无此意 |

> 结论：本章**无编造级情节**，两条提示均为分析/提示层的越界，不是事实虚构。

## R3-3 错（两边都有但不一致）

| # | md 侧（逐字） | 原文（逐字 + 位置） | 不一致点 | 判定 |
|---|---|---|---|---|
| E1 | `:89` 一句话总结「只剩焦木、烧化的电器、奥利弗玩具的残骸和**塌成一堆的钢琴**」 | `:23`「here is Oliver’s piano, collapsed and all the wires sprung loose, the ivory blackened, the case charred, **its shape almost intact but the legs gone**」 | 原文是「轮廓几乎完好、只是腿没了」，md 收成「塌成一堆」。二者都含 collapsed，但「一堆」把它写成不成形，与 `its shape almost intact` 相反的印象 | 提示（轻；不涉及人物/原因/时序，属描写强度偏移） |
| E2 | `:11`「四十岁的阿尔芭落进后院」 | `:23`「I don’t know when or at first where I am. I’m in the backyard」 | 章程内没有写「落进」，是 md 对穿越方式的推断；本章原文只给她「不知何时何地」 | 提示（轻，且与全书设定一致） |
| E3 | `:12`「整章没有对话，只有一个人在灰烬里认东西」 | 全章 31 行确无引号对话 | 相符 | 已核 |
| E4 | `:13`「这一次没有可重逢的人，只有物件的残骸和一场雨」 | `:25`「no one is left here to see it」／`:24`「No one came to save the Yellow House.」 | 相符 | 已核 |

## R4 逐块对应

| 块 | 引语首句 | 这段中文是不是在讲这句引语 | 判断 |
|---|---|---|---|
| 原句1 | "I don’t know when or at first where I am. I’m in the backyard…" | 是。失向→后院→房子没了→赤身→焦木/布/碗/钟→钢琴与松脱琴弦，顺序与引语一致 | 对应成立 |
| 原句2 | "The house is not even a shell, it has imploded—…" | 是。「连空壳都不是」→imploded→烟囱→家电→玩具→电视→建材清单→余烬，逐项咬合；md 未把「黏软塑料」误挂给别人（引语里是「must be Oliver’s」推测语气，md 也写「该是」） | 对应成立 |
| 原句3 | "The trees that crowded around the house are tall stump silhouettes…" | 是。树桩→送葬人比喻→花园绿→雨更大→No birds，四层全在引语内 | 对应成立 |
| 原句4 | "The rain makes a hissing sound as it touches the embers.…" | 是。但引语用「…」跳过「So much loss.」，中文理解随之跳过（见 L1） | 对应成立（提示：引语省略了全章唯一的哀悼句） |

## 形态

- 4 块四子项齐全；块数 4、本书 `block_target [2,2]` —— **超出建议值 2 块**，但仍在 `block_limit hi=15` 内，且原文 31 行/9 段确实只够 4 个引语，不判红。
- `cjk_ratio` 最低 0.64（原句 2 的`为什么这样写`），高于 0.6 门限；词汇 11 条例句逐条比对 text，miss=0。
