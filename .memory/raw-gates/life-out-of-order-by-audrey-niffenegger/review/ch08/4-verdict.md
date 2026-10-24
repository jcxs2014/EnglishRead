# ch08 Election Day 2024 — 判定（R5）

- 机器层：`bash scripts/chapter.sh "…/ch08 election day 2024.md" --json` → **rc=0**，verdict=ok，块数 3、words 602、segments 4、查无 0、空引号 0、子项缺 0、关键词 0 缺、形态偏离 0，`issues` 全空。
- 素读锚点：8/8 命中。
- 报数：**逐字 0 / 对应 0 / 形态 0 / 断言 0 阻断、6 提示 + 1 形态提示**——漏 4、编 1、错 1。

## 判定表

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 漏：Zach 的两条边界（不吃人、不牵扯孩子）＋「你想保留多少选择的幻觉」/「一点也不要，我不想提前感到悔恨」 | `text/ch08_election_day_2024.txt:62` “Well. Not cannibalism. Nothing involving kids.”；`:66` “How much illusion of choice would you like to preserve?”；`:70` “None,” he says decisively. “I don’t want to feel the remorse in advance.” | 三块与导航均无；`cannibalism` 只作词汇行（md :56）。本章道德核心（他自愿交出选择权）无一字落地 | 提示 |
| 漏：观票派对在 Celia 与 Lucinda 家 | `:35` “Tonight there’s a watch party for the returns **at their place**. Mama and Beck are going.” | 导航 :11 只写「有一场为开票办的 watch party」，未交代地点与「Lucinda 家的场子」；她回避的对象因此悬空 | 提示 |
| 漏：清单第二类来源「你和 Gomez 自己做的、我只知道日期」 | `:74` “There are some that you and Gomez did on your own, all I know is the dates.” | 导航保留「只有日期」，丢掉行动主体 | 提示 |
| 漏：「这会是一段狂野的旅程」/「好」 | `:104` “It’s going to be a wild ride.”；`:108` “Okay.” | 零命中（轻） | 提示 |
| 编：md :13「**火很小，烟要用水冲走**」 | `:95` “I take the list from him, filch his lighter from his coat pocket, borrow his bathrobe, pad to the kitchen on my bare feet and burn the paper in the sink.” | 原文只有「在水槽里烧掉」，火势与烟的处理是加出来的物理细节 | 提示 |
| 错：md :12「哭不是为结果，是「poker face」**终于不必维持**」 | `:35` “…he pulls me into the house and embraces me. **So much for keeping a poker face.**” | 原文是「本想端着，当场破功」；md 读成「不必再演」，因果偏半格（可辩护，非事实冲突） | 提示 |
| 形态：112 行、8 条素读，精读只有 3 块，中段（缺席派对→门口哭→寿司夜→列清单→烧纸）无块 | md 结构：块 1 :19、块 2 :29、块 3 :39；导航 :9–:15；词汇 :49–:78 | 机器 `block_range [3,10]` 未报警，但本章信息密度与块数不匹配，中段全靠导航承载 | 提示 |
| 14 条词汇例句 | 脚本整串比对：`rows=14 miss=0` | 逐字无误、未跨章 | 假红（核后成立） |
| 抬头 `Alba is 23, Zach is 23` | `:18` “Tuesday, November 5, 2024 (Alba is 23, Zach is 23)” | 原书原文；md 未据此推算他章年龄 | 假红（按派工方口径延伸） |

## 处置建议（只报不改）

1. 建议补 1 块（`block_range` 上限 10，加块不会破形态）：以 `:66`–`:70` 为引语，中文落点是「他把选择权连同悔恨一起交出去」。
2. 导航 :11 补六字级信息：观票派对在 Celia 家（Lucinda 的场子）。
3. 改两处措辞：:12「不必维持」→「没能端住」；:13 删「火很小，烟要用水冲走」。

## 已核实为正确

- **两人同龄**：`text/ch08_election_day_2024.txt:18` “(Alba is 23, Zach is 23)”；md :11/:82 一致，未与 ch07 的 22/23 冲突（跨年）。
- **`Alba:` 声部标签**：`:23` 句首即 “Alba:”，md :15 的描述成立。
- **Lucinda 年龄**：`:29` “she’d just turned eighteen, this is the first election she can vote in”；md 未扩写成「生日就在这几天」。
- **结果不被说出**：md 全篇未写谁赢（`/usr/bin/grep -niE "won\|win \|trump\|harris\|当选\|赢了" "ch08 election day 2024.md"` 退出码 1、零输出），保住原文机关。
- **午夜脚步声的主语**：`:40` “I hear Charisse and Gomez come home around midnight.”；md :11 写「Charisse 和 Gomez 回家」，未误挂成 Celia/Lucinda。
- **「买枪」归属**：`:83` Zach 问 “What about offense?” → `:87` “I add a few things to the list. “Buy a gun and learn to use it,” I tell him.”；md :11「又添了一条」方向正确。
- **14 条词汇**：全部落本章（`miss=0`），`embraces` 例句即 `:35` 原句，`decisively`／`rhapsodizing` 亦为原句。
- **结尾三句**：`:112` “There’s no one in sight… no birdsong. We walk across the park, holding hands, into the mourning city, into the relentless future.”；md 原句 3 逐字采用，未改词、未并段。
