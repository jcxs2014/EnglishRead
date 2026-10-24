# ch12 The Yellow House · R5 判定

- 机器层：`chapter.sh` **rc=0**；块数 10 / 引语 10 / 查无 0 / 空引号 0 / 结构缺项 0 / 关键词异常 0 / CJK 低 0 / 字数 2607 / 块数区间 [2,15] 内（10 触本书上限）
- 素读：`1-suread.json`（先于 md 写定）
- 对账：`3-diff.md`

| # | 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|---|
| 1 | md 第 14 行：「这一天她做的事几乎都是「不」——…**不肯读便条**…」 | `text/ch12_the_yellow_house.txt:238-241`：`“Can I read it?” I asked.` / `“Later,” she said.`（Alba 主动要求读，被母亲推到以后） | 意愿方向颠倒；且被用作「她做的都是不」的论据 | **阻断** |
| 2 | md 第 45 行：「末句短得只有**四个词**」 | `text/ch12_the_yellow_house.txt:39`：`The cake said, Welcome, Alba!`；`python3 -c "print(len('The cake said, Welcome, Alba!'.split()))"` → `5` | 句长计数差 1，不影响理解 | 提示 |
| 3 | md 第 14 行：「**不肯留下手套**」 | `text/ch12_the_yellow_house.txt:255-263`：`I suddenly loved them—I didn’t want to leave them there.` … `I pulled off the mittens and carefully arranged them by her note` | 原文是舍不得但照做；与同章第 12 行「她开始留下东西」自相矛盾 | 提示 |
| 4 | md 第 11 行：「像 Blue Teddy 兄弟的熊，**取名** Other Teddy」 | `text/ch12_the_yellow_house.txt:176`：`The bear’s name was Other Teddy.`（未写命名者） | 补出了原文没有的施动者 | 提示 |
| 5 | md 第 13 行：「**后院**攒着空酒瓶和麦片盒」 | `text/ch12_the_yellow_house.txt:72`：`There was a small back porch full of empty liquor bottles and cereal boxes waiting to be recycled.` | 后廊误作后院 | 提示 |
| 6 | 素读第 8 条（提琴+挂锁房间，`text/ch12:181-195`）在 md 无对应块 | `/usr/bin/grep -nE "提琴｜violin｜挂锁｜padlock" "ch12 the yellow house.md"` → 无输出，**rc=1**；`text/ch12:181` `We found a violin in the last bedroom.`、`:190` `A large, ominous-looking padlock had been installed above the doorknob.` | 覆盖缺口；非转折，10 块已满，取舍可理解 | 提示 |

报数（四组）：

- **逐字**：0（10 条引语全部与 `text/` 逐字一致，机器层 segment_miss=0）
- **对应**：0（10 块中文都与所贴引语同层，见 `3-diff.md` 第四节）
- **形态**：0（H1 `12. The Yellow House`、导航 5 项、子项 4 项齐全、块序与原文一致）
- **断言**：1 阻断 + 5 提示（上表）

## 已核实为正确（防下一轮误修）

| 看着像错 | 回原文核对 | 结论 |
|---|---|---|
| 抬头 2007-02-27「Alba is 5」与 2007-03-07「Alba is 25」同年不同龄 | `text/ch12:21` `Tuesday, February 27, 2007 (Alba is 5, Clare is 35)`；`text/ch12:288` `Wednesday, March 7, 2007 (Alba is 25, Oliver is 44)` | 原书抬头原文即如此，md 第 15 行「同一个 2007 年同时装着五岁和二十五岁的 Alba，一句解释都不给」是对原文的忠实描述，**不是错误**，勿改年份 |
| 「壁橱里是 where they keep all the monsters」 | `text/ch12:195` `“That’s where they keep all the monsters,” I said.` | 引语与归属（五岁 Alba 说）正确 |
| 「母亲去市政厅查房契，发现她从 1947 年起就是业主」 | `text/ch12:46-47` `When she looked up the deed at City Hall she found that I had been the owner of the Yellow House since 1947.` | 正确 |
| 原句 6 说落点衣柜就是发现紫色衣裙的衣柜 | `text/ch12:158` `we found a closet full of girl’s clothing` … `text/ch12:176` `landing on the rug in front of that closet` | 同一柜，正确 |
| 「求婚/押金」式解读：Mama 收下手套 | `text/ch12:255-263` `Mama said, “How about your mittens?”` … `Mama gave me her leather gloves.` | 方向正确（Alba 给、Mama 收并回赠） |
| 词汇例句 11 条 | 逐条对 `text/ch12`：reverential 111 / discordant 185 / vestiges 181 / inconspicuous 308 / neglected 26 / menacing 57 / sparsely 32 / gleaming 77 / back door 37 / grown-up 128 / bright 57 | 全部逐字命中 |
