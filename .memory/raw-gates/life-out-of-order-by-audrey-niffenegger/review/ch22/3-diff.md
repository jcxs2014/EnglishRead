# ch22 Russian Tea — 三单对账（漏 / 编 / 错）

> 素读底稿：`1-suread.json`（10 条）；机器层：`2-machine.json`（rc=0，9 块，9 段引语全 ok，3581 词，查无 0 / 空引号 0 / 子项缺 0）。
> 素读先落盘，之后才打开 md（`notes/books/novels/life-out-of-order-by-audrey-niffenegger/ch22 russian tea.md`）。

## 素读补充句（作业单要求）

本章的转折点进没进这几条？——**两个转折，一个进了、一个没进**。①裸体的 Alba 从旋转门跌进来（素读第 5 条）进了，且是九块里最重的一块；②**碰杯那句「To life, out of order」与「To world enough, and time」**（素读第 10 条）——它是整章的收束，也是"失序"这个题眼的落点——**没有进任何一块，也没进导航**，这是本章最大的一处漏。

## 一、漏（素读有、md 无）

| # | 素读条目 | md 情况 | 档 |
|---|---|---|---|
| 1 | 碰杯：Beck「To life, out of order」；Clare 回「'To world enough, and time'」——"It was Henry's favorite toast, but it seems appropriate tonight."（`text/ch22_russian_tea.txt:395、399`） | md 全文搜 `杯` / `敬` / `world enough` / `out of order` **全为 0**（`/usr/bin/grep -nE "杯\|敬\|world enough\|toast\|干杯"` 退出码 1）；9 块从"Less/random"直接跳到"她过马路"，**全章题眼被整段跳过** | **阻断** |
| 2 | Beck 的女儿出生即死：「We had a daughter. She died at birth.」（`text/ch22_russian_tea.txt:141`）；Jasper「seems so lost」，她仍与他远程合作，MacArthur 奖是两人共同的（`:149、:172`） | md 搜 `婴儿`=0、`Jasper`=0、`MacArthur`=0；导航只有「互换伤口」四字，**Jasper 这个人物在本章 md 里完全不存在** | 提示 |
| 3 | Clare 低声讲 2016 年大选，Beck 说「No. That's horrible」「How do we stop—」，Clare 答「We don't. We can't.」（`text/ch22_russian_tea.txt:364-369`） | 只在 md:13 的 Tropes 里以"包括一场选举"一笔带过，无块覆盖 | 提示 |
| 4 | 宗教对照：贵格会/废奴/地下铁道、Clare 母亲死后"像断了电"（`text/ch22_russian_tea.txt:299、312`） | md 无（`贵格`=0） | 提示 |
| 5 | 基因治疗明年宣布："Gene therapy works. They announce it next year."（`text/ch22_russian_tea.txt:387`） | md 无（`基因`=0） | 提示 |
| 6 | 年龄坐标：Alba 八岁、Henry 死于 Alba 五岁；抬头 Clare 38 / Beck 34 / Alba 36（`text/ch22_russian_tea.txt:18、85、93`） | md 未给任何年龄；"Alba 36"这一关键（裸体 Alba 来自 2038 年）完全没交代 | 提示 |

## 二、编（md 有、原文无）

**未发现凭空情节。** 专名与数字核过：Adams El stop、South Haven、Cranbrook、MIT、SAIC、David Kendrick、Malbec、Wabash、Charisse/Celia/Kimy，均在 `text/ch22_russian_tea.txt` 有原文。

## 三、错（两边都有但不一致）

| # | md 位置 | 原文 | 判 | 档 |
|---|---|---|---|---|
| 1 | md:11「两个刚失去**丈夫**的女人」；md:13「两人各自带着**亡夫**」 | `text/ch22_russian_tea.txt:127` "Jasper and I met in grad school, at MIT."；`:149` "Jasper would have been a good father. Losing the baby was hard for both of us, but I'm not sure he will recover. **He seems so lost.**"；`:172` "He's been incredibly erratic lately." —— **Jasper 活着**，只是"lost"（精神状况坏、两人分居/离婚中） | 关系状态错：把"丈夫失踪/病着"写成"亡夫"，抹掉了本章与上一章的结构性对称（两个 lost 的丈夫） | **阻断** |
| 2 | md:21「一顿**午饭**被写成需要下决心的事」 | `text/ch22_russian_tea.txt:25` "watching **rush-hour** crowds"；`:67` 点伏特加；`:373` 上主菜、`:395` 上酒；`:443` 分手后"walk east, to the parking garage" —— 是**晚饭** | 时序/场合错（且与 md:12 自己写的"私密的晚饭"矛盾） | 提示 |

## 四、R4 逐块对应（人判）

| 块 | 引语 | 中文是否在讲这句引语 | 主语/受事/归属 | 档 |
|---|---|---|---|---|
| 原句 1 | 挑衣服挑到迟到 | 是（"午饭"见错 2） | 主语：她；受事：衣服/打扮 | 通过（附提示） |
| 原句 2 | 雨棚下等、手机没消息 | 是 | 主语：她；受事：无（等） | 通过 |
| 原句 3 | 满屋红 + 唯一的黑人 | 是；"被看的人只是抬了抬眼"是合理外推 | 归属："她是唯一的黑人"是 **Clare 的发现**，md 明确归给 Clare，未错 | 通过 |
| 原句 4 | 说不出口的两件事 | 是 | 主语：她（不知道怎么说）；受事：Alba 见 Henry 这件事 | 通过 |
| 原句 5 | "show all our damage" | 是 | 主语：Beck（问）；"我们"含 Clare | 通过 |
| 原句 6 | 湿透脏污、灰发、披外套 | 是 | 主语：Clare（动作）；受事：Alba | 通过 |
| 原句 7 | 凉汤、被围观、经理换热汤 | 是 | 主语：经理（给）；受事：汤 | 通过 |
| 原句 8 | 更不信神 | 是 | 主语：她（答）；受事：无 | 通过 |
| 原句 9 | 过马路、未来开花 | 是 | 主语：她（明白）；受事：未来 | 通过 |

**结论**：九块对应全部成立，无"讲引语之外的上下文"；问题不在块内，在**块与块之间被跳过的两段**（死婴/丈夫 lost 的自述、碰杯）。
