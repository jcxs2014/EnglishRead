# ch57 A Failed Surprise —— R5 判定

- 章：ch57（`text/ch57_a_failed_surprise.txt`，318 行 / 2141 词；抬头 `:18` 2041-09-06 与 09-07，Zach 40、Alba 40）
- md：`ch57 a failed surprise.md`，113 行，**6 块**
- 机器层：`bash scripts/chapter.sh` → **rc=0**，verdict=ok；6 引语全逐字；empty_quote=0；struct_bad=0；block_target=[4,7]

## 判定表

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| **转折点对质段无块**：承认因果闭环、追问名字、physically cannot、why did you lie、「我走你留下」「你必须留在这里」全缺；6 块未触上限 10，导航未写取舍 | `text/ch57_a_failed_surprise.txt:221` "“Alba, where do you go? Who do you go to? There’s someone that you’re traveling to, isn’t there?”"；`:239` "“What’s his name?” Zach’s hands are pressed flat against the table."；`:243` "I try to tell him and I can’t, I physically cannot."；`:247` "“Why did you lie to me?” Zach says this quietly, which somehow makes it worse."；`:260` "“No,” I say. “I’ll go. You stay here.”"；`:284` "“There’s more going on than you and me.”" | 漏 | **阻断** |
| **「她没有回答，句子就停在她的沉默里」——她答了「我不知道」** | `:217` "“I don’t know,” I reply." | 编（虚构沉默并据此发议论） | **阻断** |
| 「随后提箱离开」——收拾箱子的是扎克 | `:255` "He’s in the bedroom, packing a suitcase."；`:260` "“No,” I say. “I’ll go. You stay here.”" | 错（主体） | 提示 |
| 块 5「几乎从不走向他」软化（引语作 never） | `:212` "Why is it that you’re always traveling away from me, never to me?" | 错（强度） | 提示 |
| 块 4 译文首句在引语之外 | `:158` "The remains of the surprise party clutter all the tables." | 对应偏移 | 提示 |
| 露辛达失联线（纽约、助手、忧郁、只想找 Isadora、机场告别语） | `:33` "She lives in New York now, modeling occasionally and working as an assistant for a very demanding, very famous performance artist whose name I always forget." | 正确 | 跳过 |
| 群像（Clare 风湿、Nell、Rosa 当选、Mark/Sharon 的孩子因野火没来） | `:29` 段；`:66` "Clare has arthritis in her hands, so I open both our beers and pour." | 正确（多数在词汇例句里落地） | 跳过 |
| 恐慌「觉得她死了」 | `:132` "I have a panicky feeling that Alba is dead, even though I know for a fact that she isn’t." | 正确 | 跳过 |
| 剩蛋糕「Happy birthday to me」 | `:158` "A plate with a half-eaten piece of carrot cake is tucked neatly under a chair. I’m hungry, so I eat it. Happy birthday to me." | 正确 | 跳过 |
| 结尾喊 Isadora、留条、走黄房子 | `:317` "I call out for Isadora and get no answer, then remember that Isadora is gone. I leave a note to say I was here, then I lock up and walk to the Yellow House. It isn’t home, but it will have to do for now." | 正确 | 跳过 |

## 报数（四组）

| 组 | 数 | 说明 |
|---|---|---|
| 逐字 | 6/6 ✅ | segment_miss=0；人工 grep 六条块首全部命中（`:23 :33 :132 :158 :212 :317`） |
| 对应 | 5/6 ⚠️ | 块 4 译文首句（「残局摊在每张桌上」）落在引语之外，应把 `:158` 首句纳入引语 |
| 形态 | 6 块（target 4–7）；子项四件齐；导航 5 条 | 通过 |
| 断言 | 阻断 2 · 提示 3 · 跳过 6 | 见上表 |

## 判词

ch57 **2 阻断**。这一章是全书的分水岭，md 的群像与日期线都稳，块 1–4 选句（冒险的赌注、露辛达的失联、无蜡烛的生日歌、椅下那半块蛋糕）几乎无可替代。两处硬伤正好都在转折点上：①真正的对质（她承认「他是因果闭环的一部分」「我走，你留下」）没有块承载，只在总结里留一句；②块 5 的解说「她没有回答」与原文相反——她答了「我不知道」。前者让本章最重要的一次夫妻对话只剩半句，后者让沉默读起来像沉默，实则不是。

## 已核实为正确（防下一轮误修）

命令：`/usr/bin/grep -nE "I don’t know,” I reply|where do you go|What’s his name|physically cannot|Why did you lie to me|You stay here|There’s more going on" text/ch57_a_failed_surprise.txt`，命中 `:217 / :221 / :239 / :243 / :247 / :260 / :284`，**退出码 0**。

- 原句 1 ＝ `:23` "I knew it was a risky idea to throw a surprise party for Alba’s fortieth birthday. I figured if she didn’t know about it, she was more likely to be here. But she disappeared this morning while she was taking a shower, and I haven’t seen her since."
- 原句 2 ＝ `:33` "The only person unaccounted for—besides Alba—is Lucinda. She lives in New York now, modeling occasionally and working as an assistant for a very demanding, very famous performance artist whose name I always forget. The last time Alba and I saw Lucinda, around the Christmas holidays, she seemed unhappy—not quite her shy, sweet self, but an exhausted, depressed woman who deflected all personal questions."
- 原句 3 ＝ `:132` "Beck made carrot cake, Alba’s favorite. We skip the candles, but we sing happy birthday to Alba. I have a panicky feeling that Alba is dead, even though I know for a fact that she isn’t."
- 原句 4 ＝ `:158` "The remains of the surprise party clutter all the tables. When Zach and I throw a party, we always stay up and wash all the dishes. Last night, they collected the empties and stacked the plates by the kitchen sink, but there are glasses, balled-up napkins and a sprinkling of toothpicks everywhere. A plate with a half-eaten piece of carrot cake is tucked neatly under a chair."
- 原句 5 ＝ `:212` "“Alba,” Zach says, “you know how your father time traveled to your mother’s childhood, over and over? Why is it that you’re always traveling away from me, never to me?”"
- 原句 6 ＝ `:317` "I call out for Isadora and get no answer, then remember that Isadora is gone. I leave a note to say I was here, then I lock up and walk to the Yellow House. It isn’t home, but it will have to do for now."
- 「她有回答」＝ `:217` "“I don’t know,” I reply." → **凡写「她没有回答 / 停在她的沉默里」皆错，勿改回**
- 「causal loop 指另一个男人」＝ `:231` "“Later,” I admit. “You’re the one I chose. He’s part of a causal loop. With him, there was no beginning. Or if there was, I haven’t found it yet.”" → 正确
- 「提箱者是 Zach」＝ `:255` "He’s in the bedroom, packing a suitcase." → **勿把提箱主语写成阿尔芭**
- 「never to me」＝ `:212` → 勿软化成「几乎从不」
