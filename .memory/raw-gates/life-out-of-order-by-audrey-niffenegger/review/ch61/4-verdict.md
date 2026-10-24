# ch61 A Lady in a Burnt Garden — R5 判定

- md：`notes/books/novels/life-out-of-order-by-audrey-niffenegger/ch61 a lady in a burnt garden.md`
- text：`notes/books/novels/life-out-of-order-by-audrey-niffenegger/text/ch61_a_lady_in_a_burnt_garden.txt`
- R1：`review/ch61/1-suread.json`（先于 md 打开）｜R2：`review/ch61/2-machine.json`｜R3/R4：`review/ch61/3-diff.md`

## R2 机器层

`bash scripts/chapter.sh "…/ch61 a lady in a burnt garden.md" --json` → **rc=0**，`verdict=ok`，`issues=[]`，`blocks=4`，`cjk_ratio` 最低 0.64。rc=0 不等于通过。

## R5 判定表

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 逐字：4 块引语 | `:23`「I don’t know when or at first where I am.」／`:24`「The house is not even a shell, it has imploded」／`:25`「The trees that crowded around the house are tall stump silhouettes」／`:30`「The rain makes a hissing sound as it touches the embers.」 | 4/4 逐字成立（原句 4 含显式省略号「…」，被跳过的「So much loss.」见下条） | 通过 |
| 逐字：词汇 11 条例句 | 逐条 `in flat(text)`：`unrecognizable floating objects`／`It burned uninterrupted`／`The whole neighborhood is in ruins.`／`Fragments of music here and there.` 等 | 11/11 命中，miss=0 | 通过 |
| 对应：块 1 | 引语讲失向→后院→房子没了→赤身→点名碎件→钢琴与琴弦；md 中文同序，未加「她为什么回来」 | 在讲这句引语 | 通过 |
| 对应：块 2 | 引语主语是房子（imploded/fallen/collapsed/melted），md 中文主语一致；玩具一句原文是「must be Oliver’s」，md 译「该是奥利弗的玩具」保留了推测 | 归属方向正确 | 通过 |
| 对应：块 3 | 树桩＝送葬人（like mourners around a grave），md 译「像围在坟边的送葬人」，本体/喻体方向未反 | 在讲这句引语 | 通过 |
| 对应：块 4 | 引语拆自 `:30–31`，md 译「雨落在余烬上，发出嘶嘶的声响」＋「从前不知道爱着黄房子」＋「跪进草里等自己消失」 | 在讲这句引语（省略句见档位表下条） | 通过 |
| 形态：H1／导航／子项 | `2-machine.json` form：`h1_ok`、`nav_count=5`、四子项齐全 | 合格 | 通过 |
| 形态：块数 | 实有 4 块，本书该章 `block_target [2,2]` | 超建议值但原文足够撑 4 块，`block_limit` 内 | 提示 |
| 断言：导航「露辛达…」无——导航「整章没有对话」 | 全章 31 行无引号对话（`:23`–`:31` 全为叙述） | 成立 | 已核 |
| 断言：`：47`「冷是后来才轮到她去感觉的」 | `/usr/bin/grep -nEi "cold|chill|freez" text/ch61_a_lady_in_a_burnt_garden.txt` → 无输出，**EXIT=1**；全文无冷觉描写 | md 补了原文没有的物理感受 | **提示（编）** |
| 断言：`:15`「声音刚回来就被雨声盖掉」 | `:30`「Fragments of music here and there. The rain makes a hissing sound as it touches the embers.」 | 原文是并置，无「盖掉」的因果 | 提示 |
| 断言：`:89`「塌成一堆的钢琴」 | `:23`「its shape almost intact but the legs gone」 | 描写强度超出原文（原文强调轮廓完好） | 提示 |
| 断言：引语 4 省略「So much loss.」 | `:31`「I didn’t know I loved the Yellow House until it was gone. So much loss. I kneel in the grass and wait to disappear.」 | 省略有显式标记，不犯逐字；但跳过全章唯一哀悼句 | 提示 |

## 报数（四组）

- **逐字**：引语 4/4、词汇 11/11，0 条。
- **对应**：4/4 块在讲引语；块 4 引语省略一句（提示）。
- **形态**：块数超 `block_target`（提示），其余合格。
- **断言**：导航 5 条 + 块内提示 4 条 = 9 条，其中 6 条已核成立、3 条提示（冷觉、雨声盖掉、钢琴形态）。

| 章 | rc | 块数 | 漏 | 编 | 错 | 提示 |
|---|---|---|---|---|---|---|
| ch61 | 0 | 4 | 0 | 0 | 0 | 4 |

## 已核实为正确（防下一轮误修）

1. **「连空壳都算不上」不是译错**：原文 `:24`「The house is not even a shell, it has imploded」——md 译「房子连空壳都算不上，是往里塌的」是逐字直译，不要改成「只剩空壳」。
2. **「该是奥利弗的玩具」的推测语气必须保留**：原文是「that mess of glutinous plastic **must be** Oliver’s toy collection」，不是肯定句；下一轮若改成「是奥利弗的玩具收藏」，反而把原文的不确定抹掉。
3. **「围在坟边的送葬人」方向正确**：原文 `:25`「they stand over the devastation like mourners around a grave」——树桩是送葬人、废墟是坟；不要改成「像坟一样围着树桩」。
4. **「花园四周却是绿的」不是笔误**：原文 `:25`「All around the garden is green; it is raining」——绿是原文的对照，不要因为「烧成废墟」就改成「焦黑」。
5. **「没有鸟」的独立短句不能并进上一句**：原文 `:25` 末「No birds.」本身就是独立句，md 译「没有鸟。」保留独立，与原文的断句意图一致。
6. **本章无对话是原文事实**，不是 md 漏记：`:23`–`:31` 全为第一人称叙述，无一处引号台词。
