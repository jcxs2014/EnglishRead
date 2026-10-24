# ch02 判定表（R5）

章：`ch02 random driveway winter day.md`（155 行，10 块）
原文：`text/ch02_random_driveway_winter_day.txt`（691 行 / 5769 词）
机器：`2-machine.json` rc=0；块数 10；引语 11 段全 ok；空引号 0；子项缺 0；关键词 17 条全中；`block_hint` 仅提示块数（不判红）。
素读：`1-suread.json` 12 条，`quote in line` 校验 12/12。

## 判定表

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 本章应交代时间旅行的规则（像记忆／偏过去／可用人或物当锚点／多数是随机落点） | `text/ch02_random_driveway_winter_day.txt:119`「My doctor calls it a bias—the past is easier…**Time travel is like memory. It’s hard to remember forward**…Sometimes I can use an object or a person as a destination, but other times I just end up in a random time.」；md 10 块无一块讲，5 条导航无一处提，仅 md:151 词汇表收了 `bias` 例句 | 机制说明只以生词例句形式存在 | 提示（漏） |
| 追查 Nadia 的发起人、藏身处、接人者、唯一线索应至少各落一处 | `:447`「tasked with this by **Isadora**」；`:431`「a house in **Miller Beach**…on **Forest Avenue**」；`:441`「That’s Nadia’s father, **David Kendrick**」；`:526`「“**Flowers**,” I tell him. “Something about flowers.”」；`grep -nE "Isadora\|Miller\|Kendrick\|Flowers" "ch02 random driveway winter day.md"` → 0 命中 | 细节链全缺，主行动已进导航 | 提示（漏） |
| 世界观补丁（David 做基因/克隆、Clare 不许拿 Alba 做实验、满 18 岁她自己回去、政府压下知识） | `:597`「David has a whole lab working out the genetics, doing something with cloning…**Clare wouldn’t let him use Alba as a test subject**, but once Alba turned eighteen she jumped back into the study.」；`:606`「the powers that be moved to shut that knowledge down」 | md 全无（`grep -n "克隆"` = 0） | 提示（漏） |
| md:41「她站在自己二十一岁的房门口」是否把年龄搞错（她本章 27 岁） | 本章 `:18`「(Alba is 27, Zach is 28 and 22)」；ch01 `:18`「Alba is 21」；两抬头相隔 6 年半、年龄差 6 岁，生日落在 7 月底—12 月底之间即可自洽 | 「二十一岁」指房里那个年轻自己，不是笔误 | **假红** |
| md:11「她回 Mama 家借衣服」是否把「偷」写成「借」 | `:169`「filch one of Mama’s vintage winter coats from the front closet」＋同段「these things will be returned to my younger self tomorrow」；`:265`「please give my clothing to my younger self tomorrow」 | 原文自己就说会还，译「借」成立 | **假红** |

计数（只数阻断档）：漏 0 · 编 0 · 错 0；提示 3；假红 2。

## 已核实为正确

1. 日期与年龄：md:11「2022 年 12 月 30 日」「27 岁」= `:18` 抬头 + `:59`「December 2022」+ `:51`「the thirtieth」。
2. 车：md:11「旧黑色 Nash」= `:29`「Zach’s old black Nash Ambassador」（ch01 `:2072` 另给年份 1957，md 不必写）。
3. 手套箱信：md:11/49「宣告他未成年即「被解放」的旧公函」= `:224`「a five-year-old letter from Oklahoma Human Services…declaring Zach an emancipated minor」。
4. 六个月沙发客：md:59 引语自证 `:252`「I’ve been couch surfing for the last six months」。
5. 地址：md:11「Estes 街」= `:289`「the Gomolinskis’ house on Estes」。
6. 房间归属：md:11「Joe 的房间」= `:645`「I’d take Joe’s room because it has a bigger window」。
7. 午饭：md:71「烤奶酪三明治」= `:304`「toasted cheese sandwiches」（`:355` Zach 自己叫它 grilled cheese，两种叫法都在原文）。
8. 洗衣粉味道：md:11/155 = `:691`「“My mom used the same detergent,” I tell her.」
9. 两个声部：md:15「在「Zach:」处换成他」= `:533`「Zach: Alba stands up abruptly…」；Alba 声部 `:23`。
10. 机器层「引语逐字」11/11 ok（`2-machine.json` 第 4 块两段均 ok），片段间省略号由 md 自己加，不涉及改字。
