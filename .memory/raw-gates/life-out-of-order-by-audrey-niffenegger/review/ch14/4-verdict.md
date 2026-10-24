# ch14 Oliver Arrives · R5 判定

- 机器层：`chapter.sh` **rc=0**；块数 10 / 引语 10 / segment_miss 0 / 查无 0 / 空引号 0 / 结构缺项 0 / 关键词异常 0 / 字数 3054
- 素读：`1-suread.json`（12 条，先于 md 写定；全章 Alba 第一人称）
- 对账：`3-diff.md`

| # | 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|---|
| 1 | md 第 11/13/51/57 行把「攒满那间房」的人写成 Alba | `text/ch14_oliver_arrives.txt:73` `Oliver has been stuffing this room with possessions since the 1950s. For the first time I see it as he must have, as an egg…` | 主语与归属反向：攒房的是成年 Oliver 自己，她只是第一次用他的眼睛看；连带使 md:13「反转补给的方向」自相矛盾 | **阻断** |
| 2 | 信的内容（安全屋、`She will not lie to you`、`I’ll be terrified of you`）未进块也未进导航 | `text/ch14:142` `“Something like, ‘Dear Yang Qing, You are in a safe house in Chicago… She will not lie to you, so be careful what you ask her.’`；`:151` `“I’ll be terrified of you. Just feed me breakfast and look benevolent.”` | md:15 只提「讨论一封将要留在他桌上的信」，未给内容 | 提示 |
| 3 | 「找不到他的婚戒」未进块 | `text/ch14:83` `I look around for his wedding ring. It’s nowhere to be seen.`；`/usr/bin/grep -nE "婚戒\|wedding ring" md` → 无输出 **rc=1** | 与 ch13「他已戴婚戒」成对照，伏笔漏 | 提示 |
| 4 | 「没有电脑/电话/电视」只在词汇例句 | `text/ch14:83` `It’s conspicuously devoid of computers. No Apple product has ever entered this room. No telephone, no television, nothing digital.` | 否定式清单未进房间描写 | 提示 |
| 5 | md 第 13 行「坏掉的门廊灯」 | `text/ch14:38` `The porch light isn’t on, of course` | 原文只说灯没开，未说坏 | 提示 |
| 6 | md 第 14 行「读**体育版**连环画」 | `text/ch14:428` `settles back on his high stool with the Trib’s comics section` | comics section≠体育版 | 提示 |
| 7 | md 第 15 行「报纸日期」 | `text/ch14:428` `I peek at the date out of habit: May 12, 1999.` | 原文未点明载体，属可接受的推断 | 提示（可留） |

报数（四组）：

- **逐字**：0（10 条引语逐字全中，segment_miss=0；16 条词汇例句亦逐字）
- **对应**：1（第 4 块中文把 `Oliver has been stuffing` 的主语换成「她」，见阻断 1）
- **形态**：0（H1 `14. Oliver Arrives`、导航 5 项、子项 4 项齐全、块序与原文一致、有结尾总结）
- **断言**：1 阻断 + 6 提示

## 已核实为正确（防下一轮误修）

| 看着像错 | 回原文核对 | 结论 |
|---|---|---|
| 「Oliver 16、Alba 30」——她要大他 14 岁 | `text/ch14:18` `Wednesday, May 12, 1999 (Oliver is 16, Alba is 30)` | 原书抬头原文，勿改 |
| 「我还没出生」——她却已是这栋房子的主人 | `text/ch14:206` `“No, I haven’t been born yet.”`；`:210` `“I have not, also.”` | 两人在 1999 年都尚未出生（时间旅行者），md 第 11 行只写她、未写他，属节略不属错 |
| 「冰箱里摸出一盒伯爵茶」其实是橱柜 | `text/ch14:156` `I find a box of Earl Grey in the back of the cupboard.` | md 第 11 行「泡伯爵茶」、第 59 行引语均对（原句 5 照抄 cupboard） |
| 「他停在门槛像撞上看不见的栅栏」 | `text/ch14:545` `Oliver doesn’t come in; he stops at the threshold as though he’s encountered an invisible fence.` | 逐字有据，不是比喻原创 |
| 「她报出一百五十美元」 | `text/ch14:359` `“Yes, I have one hundred and fifty dollars.”` | 数字正确 |
| 「Adam 说 Oliver Junior」 | `text/ch14:392-396` `“Uncle,” I say. “His name is also Oliver.”` / `“Oliver Junior. That’s sweet.”` | 归属正确（她认作叔叔、Adam 接话） |
| 「蓝皮笔记本」 | `text/ch14:550` `“This green box has money. The blue box has notebooks.”` | 音「蓝盒里的笔记本」；md 写成蓝皮属近似，非硬错 |
| 词汇 16 条例句 | 逐条对 `text/ch14`：supersaturated 289 / indelicate 177 / benevolent 151 / conspicuously 83 / hypnotized 433 / Interstices 342 / cowering 47 / slouched 38 / appreciative 243 / abundance 78 / unrecognizable 190 / deposited 122 / doorbell 28 / afterthought 230 / bag boy 337 / old-fashioned 165 | 全部逐字命中 |
