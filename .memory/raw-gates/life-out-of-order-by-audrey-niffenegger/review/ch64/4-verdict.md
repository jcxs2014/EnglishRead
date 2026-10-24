# ch64 All Souls Day — R5 判定

- md：`notes/books/novels/life-out-of-order-by-audrey-niffenegger/ch64 all souls day.md`
- text：`notes/books/novels/life-out-of-order-by-audrey-niffenegger/text/ch64_all_souls_day.txt`
- R1：`review/ch64/1-suread.json`｜R2：`review/ch64/2-machine.json`｜R3/R4：`review/ch64/3-diff.md`

## R2 机器层

`bash scripts/chapter.sh "…/ch64 all souls day.md" --json` → **rc=0**，`verdict=ok`，`issues=[]`，`blocks=4`，`cjk_ratio` 全部 >0.6。rc=0 不等于通过。

## R5 判定表

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 逐字：4 块引语 | `:23`「I’m nervous, and I arrive too early.」／`:42`「“We were so worried.” We sit on the only bench in the gallery.」／`:57`「The sense of time passing, the sense of being stared at, proprioception, pain, hunger and—empathy.」／`:183`「She stands and walks away, turning to wave goodbye just before she passes through the doors.」 | 4/4 逐字成立 | 通过 |
| 逐字：词汇 14 条例句 | 逐条 `in flat(text)`，含 `proprioception`／`incantation`（`:111`）／`laboriously`（`:125`）／`cyberimmortality`（`:116`）／`unconventional`（`:111`）／`delicate`／`manicured`（`:57`）／`relentless`／`anxiously`／`overjoyed`（`:174`）／`cheek`／`darling`（`:134`）／`notebook`（`:125`）／`doors`（`:183`） | 14/14 命中，miss=0 | 通过 |
| 对应：块 1 | 发慌→早到→狮子间→玻璃门/门厅/楼梯→索恩房间；md 未提前出现伊莎多拉 | 在讲这句引语 | 通过 |
| 对应：块 2 | 「我们一直很担心」是贝克接在「谢谢你救了她」之后说的；md 归属正确 | 在讲这句引语 | 通过 |
| 对应：块 3 | 时间流逝/被注视/本体感觉/痛/饿/共情＋松鼠；md 未把 empathy 提到最前 | 在讲这句引语 | 通过 |
| 对应：块 4 | 起身→走→过门前回头挥手→bereft（自由之喜与空落并存）→「跟我很久」 | 在讲这句引语 | 通过 |
| 形态：块数 | 4 块，`block_target [2,3]` → 超建议值 1 块（`block_limit` 内） | 提示 | 提示 |
| 断言：`:92`「万灵节次日」 | `:12`「All Souls Day」＋`:18`「Saturday, November 2, 2041 (Beck is 65, Isadora is 32)」——万灵节即 11 月 2 日，当天≠次日 | **阻断** | **阻断** |
| 断言：`:11`「天蓝羽绒服、长红裙」 | `:29`「She’s wearing a sky-blue puffer jacket over a long red dress and suede boots」 | 成立 | 已核 |
| 断言：`:11`「死亡像被删除、没有备份」 | `:102`「I think it’s like being deleted, with no backup. All the files are lost.」 | 成立 | 已核 |
| 断言：`:11`「博物馆只留得住过去的反光」 | `:66`「The Museum of Lost Souls is only made of the past—reflected light from before.」 | 成立 | 已核 |
| 断言：`:14`「我们永远会回到你身边」 | `:170`「“We’ll always come back to you.”」 | 成立 | 已核 |
| 断言：`:92`「收进保险箱」 | `:125`「I put the notebook back in my purse. I’ll lock it in our safe-deposit box.」 | 成立 | 已核 |
| 断言：`:92`「贾斯珀就在罗斯科教堂里」 | `:93`「I keep him in the Rothko Chapel. Contained.」 | 成立（「他想跟你说话」「他可以等」未进 md） | 提示 |
| 断言：出展厅时五个孩子涌进来 | `:174`「The doors open, and five children (obviously brothers and sisters) surge into the gallery.」 | md `:15` 以「写孩子」带过，未成事件 | 不成立 |
| 断言：露辛达想找卡拉洛拉 | `:138`「“Lucinda wants to find Caralora,” Isadora replies.」 | 素读有、md 无 | 提示（漏） |

## 报数（四组）

- **逐字**：引语 4/4、词汇 14/14，0 条。
- **对应**：4/4 块在讲引语，0 条。
- **形态**：块数超建议值 1 块，1 条（提示）。
- **断言**：导航/总结 10 条，8 条成立、1 条提示（贾斯珀两句）、1 条阻断（万灵节次日）。

| 章 | rc | 块数 | 漏 | 编 | 错 | 提示 |
|---|---|---|---|---|---|---|
| ch64 | 0 | 4 | 0 | 0 | 1 | 2 |

## 阻断明细（修法）

- 位置：`ch64 all souls day.md:92`（一句话总结首句）。
- 现文：「**万灵节次日**，贝克提早赶到芝加哥艺术学院」
- 建议：「**二〇四一年十一月二日（万灵节当天）**，贝克提早赶到…」——既补年份，又把「次日」改掉；`本章导航·一句话概括`（`:11`）只写「贝克提早赶到」不含日期，无需改。

## 已核实为正确（防下一轮误修）

1. **「天蓝羽绒服、长红裙」不是编的**：`:29`「a sky-blue puffer jacket over a long red dress and suede boots」逐字有据，别因为它是「现代服装」就当成穿越错。
2. **「收进保险箱」不是编的**：`:125`「I’ll lock it in our **safe-deposit box**」；上一轮我按 `safe|denosit` 措词没搜到，误记为「未核」——现已确证成立。
3. **「我们一直很担心」的主语是贝克（复数我们）**：`:42` 前一句是 `:38`「“We are amazing,” she says. “We’re happy. Lucinda is doing much better.”」＋他对答「Thank you for saving her」，所以「我们」＝贝克与阿尔芭/家人，不是伊莎多拉；别把这句话挂到伊莎多拉头上。
4. **「被删除、没有备份」不是双关误译**：`:102` 上文是他在问「那贾斯珀呢」，答句讲的是保存/备份，前后一致。
5. **「博物馆只由过去构成」是原文的 reflected light 比喻**：`:66` 同一句里既有 made of the past 也有 reflected light，md 两处说法（`:11` 反光、`:15` 只由过去构成）都出自这一句，不是两个矛盾说法。
6. **「她不再夸耀无限宇宙」**：`:174`「I thought I had an infinite universe in the Thorne Rooms」是过去时——她「曾经以为」，md `:13` 把它写成「曾」，正确。
