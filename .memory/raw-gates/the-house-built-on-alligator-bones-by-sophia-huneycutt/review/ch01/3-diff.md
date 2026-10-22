# ch01（Prologue｜文件号比书内章号大 1）R3/R4 对账

| # | 型 | 位置（md） | 现象 | 原文依据（逐字） |
|---|---|---|---|---|
| A1 | 阻断·漏 | 全章无位置（导航/精读/总结均未提） | 五年前那位 city inspector、让他「breath catch」的那张支票、以及「leaving the house to rot」这条判词，在全章 md 中彻底缺席 | text/ch01_prologue.txt:15 `...the city inspector...`（同句另见 text/ch48_chapter_forty_seven.txt:207 `as I watched the city inspector stare at his check in the rearview`） |
| A2 | 阻断·对应（语法别名用错） | :34 「为什么这样写」 | 写「同一句话里"her"滑了两次：**先指画像**」——`Her portrait` 的所有格先行词是画中人（Ida），不是「画像」这件物 | text/ch01_prologue.txt:39 `Her portrait still lies on the floor in front of it, the axe still stuck inside her, blade now dulled.` |
| A3 | 提示 | 全章无位置 | 「没有动物能不被关进笼子就进 Greer House；这屋子女主人不答应」这条规则句未落位（它是后文「鳄鱼怎么会自己在屋里」的世俗解释支点） | text/ch01_prologue.txt:54 `no animal could enter Greer House uncaged; the lady of the house wouldn’t allow it` |

取证命令与输出（零命中自证，`/usr/bin/grep` 显式路径，未用 git grep）：

```
$ cd notes/books/novels/the-house-built-on-alligator-bones-by-sophia-huneycutt && /usr/bin/grep -nE 'inspector|五年前|支票' "ch01 nature consumes greer house.md"
10:- **一句话概括**：……（该行只写「引擎盖」，无 inspector／支票）
（退出码 0，但命中行不含 inspector／支票语义；md 全篇 0 次 inspector、0 次 支票）
```
