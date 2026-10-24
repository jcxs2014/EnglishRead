# ch00 对账（R3）

素读：`1-suread.json`（10 条，均带 `text/ch00_life_out_of_order.txt:行` + 逐字）。
机器：`2-machine.json`（rc=0，块数 4，引语 4 段全 ok，查无 0，空引号 0，子项缺 0）。
本文件在**素读落盘之后**才打开 md，逐条贴两侧原文。

## 一、漏（素读有、md 无）

素读 10 条 → md 覆盖 9 条半。**无阻断级漏项**（无「关键事件/转折未进任何一块或导航」）。

唯一细节缺口：

| 素读条目 | 原文 | md 侧 |
|---|---|---|
| 两个丈夫的**名字** | `text/ch00_life_out_of_order.txt:42`「I might look at Zach out in the backyard, mowing our mossy grass」；`:46`「instead of two at once」 | md 只在导航写「她说自己「同时有两个丈夫」」（`ch00 prologue life out of order.md:11`），**Zach / Oliver 两名字全章 0 次**：「他说自己」之外的识别信息丢失 |

判：事件本身已进导航，属**细节缺失**，不判阻断 → 提示。

## 二、编（md 有、原文无）

逐条回原文核 md 的每一处「原文里没有的说法」，结论：**无捏造情节/关系/数字**。

| md 断言 | 回原文核对 | 结论 |
|---|---|---|
| 「兑现「遗传的诅咒」（父亲的时间旅行传给了女儿）」（md:13） | 原文只说「A few genes have gone wrong in me」（`:16`）+「Time travel killed him」（`:21`），**没有一句说这病是从父亲传下来的** | 属**合理推断**（父亲显然也旅行才被判死因），但「传给了女儿」是 md 加的因果。记提示，不算编造情节 |
| 「母亲」= 母亲身份（md:11 等） | 原文用 `Mama`（`:26`「Mama’s hair is streaked with a little gray now」） | 成立 |
| 「她替父母互相传话」（md:11） | `:26`「My parents ask for news of each other, and I tell them what I can safely admit」 | 成立 |

## 三、错（两边都有但不一致）

两处都是**形态断言**（对原文句子形状的描述），不是情节错，故判提示：

1. md:15「结尾三句都以 I 开头」
   - md 原文：「结尾三句都以 I 开头，视野从「看前—看后—只做一件事」逐步收窄」
   - 原文 `:46` 三句为：`I look back and regret all the lies.` / `I try not to hurt people.` / **`But mostly, I just try not to panic.`**
   - 第三句以 **But** 开头，不是 I。核实命令见 `4-verdict.md`。

2. md:35「三个句子连着来，一句比一句短，最后一句最长」
   - 引用的正是 `:21` 三句。实测词数（`len(s.split())`）：**22 / 6 / 14**
   - 「一句比一句短」不成立（第三句比第二句长）；「最后一句最长」也不成立（第一句最长）。作者想说的「把死和回来压在同一行里」这个观察本身对，但支撑它的长度判断反了。

## 四、R4 逐块对应（4 块）

| 块 | 引语（text 行） | 这段中文是不是在讲这句引语 | 主语/受事/归属 |
|---|---|---|---|
| 原句1 | `:16` 首二句 | 是。中文把「所有人都在旅行」摊平成常态，再收到「她的单行道被扯断」 | 主语 Alba；受事＝她自己的时间；无归属歧义 |
| 原句2 | `:21` 前三句 | 是。爱与恨同句、killed 的归因、keeps throwing 的习惯动作，全部对应 | 凶手＝time travel（原文主语确实是 time travel），md 没把凶手写成「她」 |
| 原句3 | `:37` 前三句 | 是。antidote 定性 → 列举 → disciplines/grants 双向作用 | 主语 music；受事＝her mind / her（freedom）；md「把爱、注意力与在场都交出去」对应 `command my love and attention and my presence` |
| 原句4 | `:46` 末三句 | 是。三句收窄的读法与原文一致（唯一问题是块外导航把它说成「都以 I 开头」） | 主语 I；md「多数时候只是努力别慌」对应 `But mostly` |

密度：中文理解 87 / 99 / 105 / 83 字（`2-machine.json` `blocks[].cjk`），无一块只复述字面。
