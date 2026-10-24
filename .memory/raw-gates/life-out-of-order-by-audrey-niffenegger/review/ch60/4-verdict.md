# ch60 The Return of the Darling — R5 判定

- md：`notes/books/novels/life-out-of-order-by-audrey-niffenegger/ch60 the return of the darling.md`
- text：`notes/books/novels/life-out-of-order-by-audrey-niffenegger/text/ch60_the_return_of_the_darling.txt`
- R1：`review/ch60/1-suread.json`（10 条，先于 md 打开）｜R2：`review/ch60/2-machine.json`｜R3/R4：`review/ch60/3-diff.md`

## R2 机器层

`bash scripts/chapter.sh "notes/books/novels/life-out-of-order-by-audrey-niffenegger/ch60 the return of the darling.md" --json` → **rc=0**，`verdict=ok`，`issues=[]`，`blocks=4`，`cjk_ratio` 最低 0.74。**rc=0 不等于通过**，以下为人判。

## R5 判定表

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 逐字：4 块引语是否原文原句 | `:23`「More than anyone else I care for, it’s Lucinda I’ve tried to protect」／`:41`「When Lucinda arrives, I see her immediately, walking south on Clark Street」／`:89`「She said I had to get the new bioware」／`:124`「At first we had to take turns, but now I can be with her」 | 4/4 逐字成立（机器层与人工抽查一致；仅原句 3、4 在断句处跨了原文的段落内换行，未改字） | 通过 |
| 逐字：词汇表例句 | 13 条例句逐条与 text 比对（脚本逐串 `in flat(text)`，miss=0）：`I’m sitting in Washington Square Park, aka Bughouse Square,`／`Lucinda sees me, pauses, then walks toward me, diagonalling`／`She seems ebullient, and I realize that it’s been a long time`／`She’s my backup, and I’m hers.`／`I help her up and we start toward the coffee shop on Clark` | 13/13 逐字成立，0 miss | 通过 |
| 对应：块 1 | 引语讲「我一直想护住她／给她留空／少知未来」；md 中文亦只讲这三件，主语＝阿尔芭，受事＝露辛达 | 在讲这句引语 | 通过 |
| 对应：块 2 | 引语讲「一眼看见／拖箱／红雨衣太薄／失踪一个多月」；md 四句一一对应 | 在讲这句引语 | 通过 |
| 对应：块 3 | 引语里三个声音分得清：伊莎多拉「必须装」（She said）、阿尔芭「你一直说不该装」（you always told me）、露辛达「要么装要么死」 | 主语与归属方向正确 | 通过 |
| 对应：块 4 | 引语「先轮流、现在能同时在场、重叠融合、我几乎欣喜」；md 按序复述 | 在讲这句引语 | 通过 |
| 形态：块数／子项／H1／导航 | `2-machine.json` form 段：`h1_ok`、`nav_count=5`、四子项齐全 | 形态合格 | 通过 |
| 断言：导航「救她的是另一个人」 | `:144`「If Isadora can hold her in this world by offering her another, I can learn to be grateful for that.」 | 成立 | 已核 |
| 断言：导航「露辛达前所未有地平静快乐」 | `:67`「Lucinda looks serene, somehow—happier than I’ve seen her in a long time.」＋`:135`「She seems ebullient」 | 成立（serene＝平静、happier/ebullient＝快乐；两词都在原文，md 合写非错） | 假红（见下节） |
| 断言：「反复犹豫了很久」 | `:80`「for a while we went around and around about it」 | 「we」两人来回，md 收成一个人的犹豫；方向未反，丢一层语境 | 提示 |
| 断言：Newberry／父亲未进 md | `:36`「…I think of my father, who was a special collections librarian there for years…」 | 素读有、md 无；非事件/转折，但这是本章地点的由来 | 提示 |

## 报数（四组）

- **逐字**：引语 4/4、词汇例句 13/13，全绿，0 条。
- **对应**：4/4 块「在讲这句引语」，1 条引语选短（块 1 的「未必做到」用到句外「But I have failed her」），提示。
- **形态**：块数 4 ∈ [3,4]、四子项齐全、H1/导航合格，0 条。
- **断言**：导航+总结共 11 条断言，10 条成立、1 条提示（「反复犹豫」）。

| 章 | rc | 块数 | 漏 | 编 | 错 | 提示 |
|---|---|---|---|---|---|---|
| ch60 | 0 | 4 | 0 | 0 | 0 | 2 |

## 已核实为正确（防下一轮误修）

1. **「平静」不是错，不要改成「兴奋」**。md `:12`「露辛达前所未有地平静快乐」、`:91`「神情却比很久以来都平静」看着与该章后文 `:135`「She seems ebullient」冲突，但 `:67` 原文就写着「Lucinda looks serene, somehow—happier than I’ve seen her in a long time.」——**serene 正是「平静」**，且同一句里还有「happier」。md 把 serene 与 ebullient 两处并读成「平静快乐」，是合理合并，**不是错**。下一轮若只搜到 ebullient 就判错，属误修。
2. **「失踪一个多月」与「三十四天」并存不算矛盾**：`:41` 是旁白（more than a month），`:58` 是阿尔芭当面给的准数（Thirty-four days），md 两处都保留，与原文层次一致。
3. **「三人一起回家」不算编造**：「Let’s go home」有两处——`:149` 阿尔芭先说、`:157` 新声音附和（「I’m ready, too」），md 写「三人一起回家时，另一个熟悉的声音借露辛达的嘴应了声」，顺序与说话人归属均正确。
4. **原句 4 的「almost delighted」译成「几乎欣喜」是对的**：原文 `:125`「Lucinda looks pleased about this, almost delighted.」，不是「欣喜若狂」，md 的「几乎」保留了原句的克制。
5. **块 3 里「劝阻」归给阿尔芭没错**：`:80`「I remembered that you always told me I shouldn’t do that」中的 you＝阿尔芭（露辛达在对她说话），不要因为句子里出现 Isadora 就把劝阻改挂到她名下。
