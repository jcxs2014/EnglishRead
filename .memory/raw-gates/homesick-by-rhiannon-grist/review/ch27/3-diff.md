# ch27 对账（R3）：`ch27 either mad or a murderer.md` ↔ `text/ch27_chapter_27.txt`

取证命令统一为 `/usr/bin/grep -n -F '<串>' text/ch27_chapter_27.txt`（禁 git grep）。

## 一、五条「原句」逐字核对

| # | md 位置 | 核对结果 | text 行 |
|---|---|---|---|
| 原句1 | md:24 `That’s what I thought over and over, lying in bed, watching the dawn creep round the blue horizon…climbing up the ceiling beams of my bedroom.` | ✅ 逐字一致（弯撇 `That’s` 保留） | text:8 |
| 原句2 | md:34 `If it wasn’t madness…It’s not like the place was actually built on a fairy hill.` | ✅ 逐字一致 | text:29 |
| 原句3 | md:44 `…a penchant for illusions. It is debated whether they are benign or malicious, but in Scotland faeries are said to be feared—` | ✅ 逐字一致，破折号结尾未自补 `”` | text:47 |
| 原句4 | md:54 `…all the porcelain houses she liked to collect—stained with cigarette smoke over the years.` | ✅ 逐字一致（`collect—stained` 无空格） | text:71 |
| 原句5 | md:64 `…climbing over the dressing gown I used as a bedsheet, clutching at my toes—` | ✅ 逐字一致 | text:83 |

五条引文均落在自然段内、无跨段拼接，句首词与句末标点齐全。

## 二、词汇表 24 条例句

逐条 grep，全部命中（text:8/14/17/26/29/35/38/47/62/71/74/83/92/95 等行），无一条改写、无一条张冠李戴。
抽查最易错的四条：

- `screed`（md:82）→ text:35 `…so I got a screed of “Scottish monsters” and “Scottish mythical creatures”.` ✅ 弯引号一对完整
- `mementos`（md:86）→ text:74 `All her things, the collected mementos of her life…` ✅
- `raft`（md:107）→ text:92 `I’d cling to anyone like a life raft in that moment.` ✅
- `stillness`（md:98）→ text:26 `I lay there in the stillness of late morning…` ✅

## 三、叙述/事实性表述核对

| 位置 | md 表述 | text 依据 | 判定 |
|---|---|---|---|
| md:12 导航一句话 | 「天刚亮她就给自己定了案」 | text:8 天亮（dawn）→ text:26 仍是 `the stillness of late morning` → text:62 才落到 `Either I was mad, or I was a murderer` | ⚠️ 时序提前 |
| md:114 一句话总结 | 「她在天亮之前就把自己判了」 | 同上：定案发生在 late morning 之后，不在天亮之前 | ⚠️ 时序错 |
| md:18 人物弧线 | 「她这一章没有任何外在行动」 | text:26 `I threw my phone out of the bed`、text:95 `quickly threw on some clothes and headed downstairs`，同一条 bullet 自己又写「章末她下楼开门」 | ⚠️ 自相矛盾 |
| md:18 人物弧线 | 「章末她下楼开门」 | text:95 只到 `headed downstairs`，本章无开门动作 | ⚠️ 越界到 ch28 |
| md:20 叙事手法 | 「整段百科式条目原文被直接贴进来」 | text:41 / text:47 确为词条体两段 | ✅ 成立 |
| md:50 为什么这样写 | 「作者一个字没动」 | 无法从 `text/` 核实（看不到作者所据底稿） | ⚠️ 不可核表述 |
| md:32 / md:72 | 开篇的光与结尾的黑走同一条路线（升 vs 朝她） | text:8 `creep round…climbing up the ceiling beams` ↔ text:83 `inching up from the foot of my bed, climbing over…` | ✅ 成立，且对得准 |
| md:20 叙事手法 | 中途冒出第二人称「你」 | text:23 `When was the last time you messaged anyone? No one knows what’s going on with you.` | ✅ 成立 |
| md:70 | 第三句「用三个分词一路推下去」 | text:83 实为四个 -ing：`creeping` / `inching up` / `climbing over` / `clutching at` | ⚠️ 计数少一 |

## 四、判定汇总

判定汇总：**阻断 0 / 提示 4**
