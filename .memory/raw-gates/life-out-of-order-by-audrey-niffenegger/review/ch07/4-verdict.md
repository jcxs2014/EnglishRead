# ch07 Mayday — 判定（R5）

- 机器层：`bash scripts/chapter.sh "…/ch07 mayday.md" --json` → **rc=0**，verdict=ok，块数 10、words 3593、segments 11、查无 0、空引号 0、子项缺 0、关键词 0 缺、形态偏离 0；`block_hint` 记「块数 10 偏离本书常见区间 3–9」（提示型，`issues.block_count` 空）。
- 素读锚点：8/8 命中。
- 报数：**逐字 0 / 对应 0 / 形态 0 / 断言 2**（2 阻断、4 断言级提示 + 1 形态提示）——漏 4（含 2041 段）、编 0、错 2（握手、后门）。

## 判定表

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 漏：Caralora「2041 年要空着」这条时间旅行揭示（含 Alba 的愤怒、十八年、Beast in the Jungle、You saved my life） | `text/ch07_mayday.txt:109` “You basically said, go ahead and live your life, but be available in 2041.”；`:113` “That’s eighteen years from now.”；`:122` “That’s some serious Beast in the Jungle shit right there.”；`:127` “You saved my life; you didn’t tell me frivolously.” | md 四个块、导航全部零命中（`grep -n "2041\|十八\|18 年" "ch07 mayday.md"` 退出码 1）。这是本章唯一的时间旅行揭示，也是 Alba「不肯说未来」律法的反例；未写取舍理由 ⇒ 应补一块 | **阻断** |
| md :11「两人**只是**互相搭把手」／:13「不是恋情公布」 | `:85` ““I thought you meant you were in a relationship,” I say, disappointed.”；`:89` ““Oh, we are, kind of,” Caralora says.” | 原文明确「算是在一起」；md 用「只是」抹掉，且与本书原句 3 中文理解（:41）自相矛盾。改「两人算搭伙，也算在一起（kind of）」 | **阻断** |
| 漏：派对临时顶上的原因（Charisse 母亲摔断髋骨，Charisse/Max/Joe/Rosa 去马尼拉） | `:23` “But last week Charisse’s mom fell and broke her hip, and Charisse, Max, Joe and Rosa have gone to Manila to help her out, leaving the rest of us scrambling.” | 零命中；缺它则「五个人」的构成与 Rosa 等人的缺席无来处 | 提示 |
| 漏：Caralora 拒饭局的行程（今晚开回 Ann Arbor、周三搬家、没打包完） | `:50` “I would love to, but I should hit the road. I’m driving back to Ann Arbor tonight.”；`:57` “but I’m moving to a new place on Wednesday.” | 零命中；人物弧线只留「愿意为 Bette 挪地方」 | 提示 |
| 漏：清单由来（11 岁与 Rosa 争吵→Gomez 追问→「你让我变得谨慎」）与「答案没有步骤」 | `:275` “When I was eleven I was trying to win an argument with Rosa…”；`:340` “That list is just the answers, without the steps.” | 「答案」只在词汇表 :146 作例句；11 岁段零命中 | 提示 |
| md 原句 2 中文理解 :31「到了…**后门**，Lucinda…穿过**院门**」 | `:69` “We’ve arrived at the Gomolinskis’ **back gate**. … Lucinda sails through and skips to the **back door**.” | 到达点是院门，穿过院门才到后门；md 顺序颠倒 | 提示 |
| md :15「厨房散场之后换由『Zach:』领起」 | `:230` “Zach: I can feel Alba watching me.” 起至章末（含床戏段 `:509` 起 “Later, Alba and I are dozing…”）全为 Zach 第一人称 | 切换方向对，但「厨房散场之后」的定位含糊，且床戏段未切回 Alba；属表述问题 | 提示 |
| 15 条词汇例句 | 脚本整串比对 `text/ch07_mayday.txt`：`rows=15 miss=0` | 逐字无误、未跨章 | 假红（核后成立） |
| 抬头 `Alba is 22, Zach is 23`（2024-05-01） | `:18` “Wednesday, May 1, 2024 (Alba is 22, Zach is 23)” | 原书原文，非缺陷；md 未据此刻算其他章年龄 | 假红（按派工方口径延伸） |

## 处置建议（只报不改）

1. 必补 1 块：2041 揭示（建议以 `:109` 或 `:113` 为引语，中文交代「年长的 Alba 报出年份」＋Alba 的愤怒，落点是 Alba 自己也在用未来干预别人的人生）。
2. 必改 1 处：:11/:13 的「只是互相搭把手／不是恋情公布」。
3. 可选 4 处提示（马尼拉、Ann Arbor、11 岁由来、gate/door、视角定位）。

## 已核实为正确

- **抬头年龄**：`text/ch07_mayday.txt:18` 原文 `Alba is 22, Zach is 23`；与 ch06 的 `Alba is 42` 并存，属原书自相矛盾，不作为本书缺陷。
- **Lucinda 十七岁**：`:196` “I thought you were seventeen now?”；与「只差五岁」（Caralora 22）自洽。
- **视角切换**：`:230` 起确为 Zach 第一人称，md「前半是 Alba 的第一人称」成立。
- **15 条词汇**：全部落在本章原文，无跨章搬句、无改写（`miss=0`）。
- **「All of it has happened」**：`:312` 原文；md 译「全都已经发生、谁也改不了」，未加码。
- **Bette 四要素**（premed／一个小孩／又怀一个／丈夫走了）：`:79` 原文齐全，md 未添原文没有的措辞。
