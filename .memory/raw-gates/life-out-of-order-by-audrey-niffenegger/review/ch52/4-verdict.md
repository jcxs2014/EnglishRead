# ch52 Perfect Day — R5 判定

- 机器层：`bash scripts/chapter.sh "ch52 perfect day.md" --json` → rc=0，verdict `ok`
- 块数：4（未触 10 块上限）
- 原文 977 词 / 精读 92 行（Alba 第一人称）

## 一、判定表

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 四块引语逐字 | 与 `text/ch52_perfect_day.txt` L23/L49/L62/L157 逐字对齐，4/4 命中 | 真 | 跳过 |
| 抬头与年龄 | `:18` `Wednesday, June 25, 1980, and Thursday, June 26, 1980 (Alba is 25, Oliver is 17)` | md「六月末」一致；未写两处年龄，不构成错 | 跳过 |
| 导航「六月末的暖夜」 | `:23` `We have the windows open because it's a warm evening` | 一致 | 跳过 |
| 「他停下问她当初同他做爱时是几岁」 | `:36` `“How old were you when you made love with me the first time?”` | 一致（问者是他） | 跳过 |
| 「两人都说那件事对各自还没发生」 | `:44` `“That also has not happened. To me. I wish it would happen.”` | 一致 | 跳过 |
| 「她按住他的肩」 | `:44` `I place my hands on his shoulders.` | 一致；`:53` `Oliver reaches up and gently dislodges my hands` 证明是她按住、他挪开 | 跳过 |
| 「他说这样便扯平了」 | `:91` `“Good,” Oliver says. “Then things will be even.”` | 一致 | 跳过 |
| 「每次以为在选，其实早选好了」 | `:103` `“Every time I think I have a choice, it turns out I've already made it.”` | 一致 | 跳过 |
| 「凌晨三点三十五分」 | `:129` `Down in the kitchen, the noisy little electric clock says 3:35.` | 一致 | 跳过 |
| 「枫糖浆一滴不浪费」 | `:137` `He pours the maple syrup slowly, not wasting a drop.` | 一致 | 跳过 |
| 「唱到『种什么收什么』便停下，只弹」「雨大了去关窗」 | `:157` `At the end, Lou sings, You're going to reap just what you sow… I stop singing, and just play. Outside, the rain intensifies, and we jump up to close all the windows.` | 一致 | 跳过 |
| 「这是完美的一天」 | `:155` `“This is a perfect day. Have sex with you, and drink orange juice.”` | 一致 | 跳过 |
| `Oh, you are a good woman` 未收 | `:137` `“Oh, that is nice. Oh, you are a good woman.”` | 未收（grep 见 3-diff，exit=1） | 提示 |
| 他没听出 Lou Reed 未收 | `:156` `I didn't think he'd recognize it, and he doesn't.` | 未收（grep exit=1） | 提示 |
| 最尖锐的一句只作摘要 | `:83` `“Will you think of me when he fucks you?”` | 以「问得直接又坦白」概括 | 提示 |

## 二、报数

- **逐字**：4/4 块引语逐字命中。
- **对应**：4/4 块在讲该块引语；b2 的两重后果（向未来所有 Oliver 打开／对 Zach 关上）没有颠倒。
- **形态**：H1 `# 52. Perfect Day`；导航 5 项；子项 4 项齐；块数 4（原文 977 词，非短章下限问题）。
- **断言**：md 内可核断言 11 条全对（暖夜、问句内容、按住肩、扯平、3:35、糖浆、停唱、关窗、完美的一天、一八一四年的格拉斯、雨）；3 条漏段为提示。

## 三、已核实为正确（下一轮勿误改）

1. 「暖夜」——`:23` `a warm evening`；不是「夏夜闷热」一类可自由加戏的描写，**不要**改写成雷雨前。
2. 「凌晨三点三十五分」——`:129` 原文 `the noisy little electric clock says 3:35`；md 的「凌晨」对（三点半）。
3. 「她按住他的肩」——`:44` `I place my hands on his shoulders`，接着 `:53` 他 `gently dislodges my hands`；**是她按、他挪开**，别写成他按住她。
4. 「他问得直接又坦白」——`:83` `“Will you think of me when he fucks you?”`；问者是他、被问者是她。
5. 「这样事情就扯平了」是他的话——`:91` `“Good,” Oliver says. “Then things will be even.”`，不是她的判断；她的问句在 `:83`。
6. 「她唱到那句便停」——`:157` `I stop singing, and just play.`；是唱不下去而止，**不是**「不肯唱给他听」。
7. 「雨大了，两人跳起身去关所有的窗」——`:157` `we jump up to close all the windows`。
8. 「天亮后他称这是完美的一天」——`:155`；说话人是他，被她后来用同名歌反照。
9. 「一八一四年」——`:23` `as though Philip Glass had manifested briefly in 1814`，格拉斯是 20 世纪作曲家，md 的「短暂现身」是原文的幽默，不是史实错误。
10. 「她弹卢·里德的《完美的一天》」——`:156` `the opening chords of Lou Reed's “Perfect Day”`；曲名与作者对。
