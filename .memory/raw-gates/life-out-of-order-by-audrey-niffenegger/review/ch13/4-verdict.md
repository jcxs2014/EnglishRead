# ch13 Coming Attractions · R5 判定

- 机器层：`chapter.sh` **rc=0**；块数 10 / 引语 10 / segment_miss 0 / 查无 0 / 空引号 0 / 结构缺项 0 / 关键词异常 0 / 字数 3947（块数 10＝本书上限，机器提示「偏离常见区间 3–9」但不判红）
- 素读：`1-suread.json`（10 条，先于 md 写定）
- 对账：`3-diff.md`

| # | 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|---|
| 1 | md 全章缺 Oliver「信息不足」警告与「我存在于他不知道的空间」主题句 | `text/ch13_coming_attractions.txt:478` `“Most of the difficulties in Zach’s life will stem from a lack of information. You won’t tell him things he needs to know.”`；`:494` `“I exist in the space he doesn’t know about.”`；`:637` `I exist in the space he doesn’t know about.`；`/usr/bin/grep -nE "space he doesn|lack of information|信息不足" md` → 无输出 **rc=1** | 关键交锋未进块也未进导航，无取舍说明 | **阻断** |
| 2 | md 第 11 行导航把「弹琴—问曲—点曲」写成倒序 | `text/ch13:384` `“Anything in particular?”` → `:388` `“That étude. The Chopin.”` → `:393` `Then he plays.` | 时序倒，抹掉「她点的正是他刚讲的那首」的呼应 | 提示 |
| 3 | md 第 99 行「说明 Oliver 不是新出现的人」 | `text/ch13:626` `Because Oliver has suddenly become part of the Yellow House` | 原文只说「刚成为房子的一部分」，未说他不是新出现的人 | 提示 |
| 4 | 老年夫妇蓝狐披肩/巨大耳朵未进块 | `text/ch13:23` `She has a blue fox stole; he is wearing a cashmere overcoat. They must be immensely old, they both have freakishly enormous ears.` | 非关键，时代质感已由他物承担；`freakishly` 例句保留原句（md:132） | 提示 |

报数（四组）：

- **逐字**：0（10 条引语逐字全中，segment_miss=0；11 条词汇例句亦逐字）
- **对应**：0（10 块均讲所贴引语，见 `3-diff.md` 第四节）
- **形态**：0（H1 `13. Coming Attractions`、导航 5 项、子项 4 项齐全、块序与原文一致、结尾有一句话总结）
- **断言**：1 阻断 + 3 提示（上表）

## 已核实为正确（防下一轮误修）

| 看着像错 | 回原文核对 | 结论 |
|---|---|---|
| 同一个「Alba 24」出现在 1964 与 2025 两个抬头 | `text/ch13:18` `Thursday, November 19, 1964 (Alba is 24, Oliver is 36)`；`text/ch13:560` `Sunday, December 28, 2025 (Alba is 24, Zach is 25)` | 原书抬头原文如此，md 第 19 行「同一个二十四岁被放在相隔六十一年的一天里」是忠实描述，**勿按年份推算改岁数** |
| Oliver 1964 年 36 岁，却在 2044 年自称 16 岁 | `text/ch13:18` `Oliver is 36`；`text/ch13:151-152` `“I was sixteen. It was October 12, 2044. We met in my present. You were seventy-three years old.”` | 原书两个岁数不能按年份换算（时间旅行者年龄不随年份走），md 两面照抄，**不是 md 的错** |
| 1960 年出现的梳妆台上摆「肯尼迪竞选徽章」 | `text/ch13:54` `A dresser appeared in that bedroom in 1960, and on it there are … a campaign button for JFK` | JFK 1960 年竞选，年份成立，md 第 39 行「把年份钉在 1960 年前后」正确 |
| 「衣柜攒了十几年男装」 | `text/ch13:54` `Since the early 1950s there has been a steadily increasing collection of men’s clothes` → 1964 年约 14 年 | 「十几年」成立，勿改 |
| 「婚戒说明这人有妻子」是 md 添加的推断 | `text/ch13:81` `he’s wearing … the wedding ring`；`text/ch13:359` `I can feel his wedding ring against my palm.` | 原文后文坐实他戴婚戒，md 的推断有据，不算编 |
| 章题 Coming Attractions 被读成「预告片」 | `text/ch13:143` `“Shall I tell you how we met? How I met you, that is? It’s quite far in your future.”` | 他讲的正是「未来的片子」，md 第 15 行 Tropes 的读法成立 |
| 词汇 11 条例句 | 逐条对 `text/ch13`：sluicing 28 / intimation 183 / enervated 398 / freakishly 23 / monogrammed 54 / indifferently 54 / reverberate 398 / painlessly 380 / taxi line 23 / back door 565 / bedroom 75 | 全部逐字命中 |
