# ch06 · R5 判定表

> 审查对象：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch06 callie goes to the richmond party.md`
> 唯一权威源：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch06_6.txt`（13,073 字符 / 327 行）
> 读取顺序：先素读 `text/ch06_6.txt`（落盘 `1-suread.json`）→ 后开 md → 再跑 R2 机器层。
> 区间记法：`text/ch06_6.txt:<字符起-字符止>`（0-based 半开，Python `str.find` 实测值）。
>
> **覆盖声明**：本次受派范围**仅 ch06 一章**，其余 53 章**只有机器层**（`scripts/chapter.sh` 逐章重跑），
> **未做人判**，不得据本报告推断全书质量。本章抽查理由：人物线切换章（与命案现场无关），
> 按 `docs/rules/生产-审查对照.md`「按章型加权」，对话密集 + 视角切换，双倍权重。

---

## 四组数（只报这四组）

| 组 | 口径 | 数 | 说明 |
|---|---|---|---|
| **逐字** | 9 条引语逐字命中原文 | **9 / 9** | 每条在 ch06 内**唯一命中**、在**全书 54 个 text 文件**内也唯一命中；**无 `…` 拼接**（9 条引语均不含省略号），无跨章搬句。R2 `scripts/chapter.sh --json` 退出码 **0**、`verdict=ok`、`segment_miss=0` |
| **对应** | 逐块「这段中文是不是在讲这句引语」 | **8 / 9** | 8 块对应成立；1 块（block 8）**说话人/施事归属反转** ⇒ 不对应。引语选短 0 块；密度不足 0 块（九块均有「为什么这样写」；机器层中文理解 21–90 字、为什么这样写 85–110 字，全部达标） |
| **形态** | H1 / 导航 / 子项集 / 块数 vs 本书众数与 profile | **4 项全部一致（块数偏高但在区间内）** | 详见下方「形态组」 |
| **断言** | md 对原文的事实性断言逐条回原文核对 | **20 条已核 · 17 成立 · 3 与原文冲突** | 冲突 3 条全为阻断型（W1 兔耳、W2 丈夫、W3 说话人），见下方「断言组」 |

**阻断型条数：3**（断言组 W1 / W2 / W3；对应组 1 条与 W3 同源，不重复计数）。

---

## 形态组（对照本书众数）

众数来源：`python3 scripts/bookform.py "<书目录>" --json`（本书 54 章、391 块）。

| 项 | ch06 实际 | 本书众数 | profile（mystery-thriller） | 判定 |
|---|---|---|---|---|
| H1 | `# 6. Richmond` | `N.` 形态 **54/54 章** | — | ✅ 一致 |
| 导航项名 | 一句话概括 / 视角 / 线索结构 / 人物弧线 / 叙事手法 | 同上 5 项 **54/54 章** | — | ✅ 一致（项数 **5**） |
| 子项集 | 中文理解 / 关键词 / 为什么这样写 / 读者视角提示（**4**） | 同集合 **391/391 块** | 同集合（可选第 5 项「句子结构」未用） | ✅ 一致 |
| 块数 | **9** | 中位 **7**，区间 **[5, 10]** | [3, 10] | ⚠️ 高于中位 2 块，未越书内区间上限 |

**偏离理由（一行）**：本章为「人物线切换」章，需同时覆盖**赴会路上（车内/公汽/房产查询）→ 派对中（礼物、客人、Dotty 的八卦、Nell 与凯乌斯）→ 派对后段（来电、歌手邀约、身体不适）** 三段场景，故取 9 块（中位 7、上限 10），未越界。

**另记形态提示（提示档）**：ch06 的导航**未写出所属分部「A SATURDAY IN MAY」**（本章确实是周六晚，原文 `text/ch06_6.txt` 行 215：`'Christ, what does anyone want me for on a Saturday evening.'`）。
取证：`/usr/bin/grep -c "分部" "ch06 … .md"` → **0 命中，退出码 1**；全书 54 章中 **26 章**在导航里写出分部、**28 章**未写（ch01、ch05、ch06、ch07… 同属未写的一组）。
⇒ **不判阻断**：导航 5 项是本书固定形态，没有「分部」子项位；此为**全书性不一致**，非 ch06 独有缺陷。

---

## 断言组（md 断言 → 回原文核对）

| # | 断言（md） | 证据（章:区间 / 行） | 结论 | 档位 |
|---|---|---|---|---|
| W1 | block 2 读者视角提示：卡莉买的是「白袜子和带**兔耳**的连帽开衫」（md:37） | `text/ch06_6.txt:1187-1248`（行 50）：`‘And a little cardigan thing with **teddy bear ears** on the hood.’` | 原文是 **teddy bear（小熊）耳朵**，md 写成兔耳——逐字级事实改写，且此句是「礼物＝她与圈子关系」这一解读的物证 | **阻断** |
| W2 | 一句话总结：「……打**丈**着房子、客人和**丈夫凯乌斯**的工作」（md:156） | `text/ch06_6.txt` 行 116：`‘Your boyfriend’s calling,’ Callie said to Caius…`；`/usr/bin/grep -n -iE "husband\|wife\|married\|marriage" text/ch06_6.txt` → **0 命中，退出码 1**；旁证 ch38 行 56 的 "your husband" 是 Callie 谈**别人**的丈夫，ch54 行 20 凯乌斯口袋里是 **ring box**（未成婚） | 本章明写 boyfriend；md 升级为「丈夫」 | **阻断** |
| W3 | block 8「为什么这样写」：「**多蒂转述时**用的是娱乐圈那种夸张口吻」（md:95） | `text/ch06_6.txt:11054-11172`（行 269）Caius 问 `‘And what does Eulalia want from you?’`；`text/ch06_6.txt:11175-11543`（行 272）引语本体含 `she has asked **yours truly** to help develop the whole concept`（yours truly = 说话人自称） | 说话人 = **卡莉自己**，不是多蒂；Dotty 全章从未谈过头套（只有行 230/239/254 三句：`‘Eulalia as in the singer?’`、`‘Eulalia!’`、`‘Come on, spill, Cal.’`）。R4 三问之「谁说的」答错 | **阻断** |
| A4 | 导航「身体线：饿、恶心、**发空**」（md:13）、block 9「饿、恶心、**发空**」（md:107） | `text/ch06_6.txt:829-918`（行 38）：`‘I am bloody starving and yet also a little nauseous. I mustn’t have eaten enough today.’` | 原文只有「饿 / 恶心 / 没吃够」，无「发空」；属措辞过度概括 | 提示 |
| A5 | 导航「视角」：「她看房子、看客人穿戴、盯凯乌斯与旧识的互动、**记下每个人的话**」（md:12） | `text/ch06_6.txt:8356-8744`（行 215）`Callie, who had watched the whole vignette unfold…` | Callie 只是**看、听、回想**，无任何「记录」动作；措辞不确 | 提示 |
| A6 | 导航「叙事手法」：「**章末**用两处悬置收束——一通未接的陌生来电，和她自己说不清的身体反应」（md:15） | `text/ch06_6.txt:8541-8590`（行 215）三通未接电话；其后仍有 block 8 整段（行 272–278）与不适感（行 302） | 来电在全文 327 行中位于约 2/3 处，**不在章末**；「两处悬置都在后半段」成立，「章末」偏松 | 提示 |
| A7 | block 5：「头巾与紧身短裤是**伦敦东区**的旧派讲究」（md:65） | `text/ch06_6.txt` 行 74：`‘I mean, **Georgie’s** low-key one of the East London mandem.’` | 原文 East London 修饰的是 **Georgie**（人），md 把它安到头巾/短裤上 ⇒ 归属外推（原文并未这么说） | 提示 |
| A8 | block 5：「泡泡糖电子乐却是**当下正流行的消费音乐**」（md:65） | `text/ch06_6.txt:4680-5045`（行 113）只写 `Bubblegum electro-pop was blasting out of a speaker system that Georgie had set up.` | 原文无「正流行/消费音乐」的评价，属 md 自加的时代判断 | 提示 |
| A9 | block 7：「作者把『被找』的时刻放在她**刚刚放松下来**的场合」（md:85） | `text/ch06_6.txt:8424-8540`（行 215）：`The creeping feeling that Caius’s career was one day soon going to seriously impact their social life fell over her.` | 紧接来电前写的是**不安压下来**，无「放松」；情境断言无据 | 提示 |
| A10 | block 9：「……而**她自己或许还没想到**」（md:105） | `text/ch06_6.txt:12551-12594`（行 308）：`‘At least you didn’t say it was my hormones.’` → 行 311 才是 `‘Is it though? Your body runs like clockwork…’` | 原文是**卡莉自己先提「荷尔蒙」**、凯乌斯随后接；md 的先后说反（原文用「或许」软化，故只判提示） | 提示 |
| A11 | 导航「视角」：第三人称限知、紧贴卡莉（md:12） | `text/ch06_6.txt:8006-8072`（行 209）：`Georgie was secretly thrilled by this apparent proximity to death.` | 原文本身有一句短暂越出卡莉视角进入乔治内心；md 说「紧贴」略绝对（**原文如此，非 md 的错**） | 提示 |
| A12 | 导航「人物弧线」：接受戴头套歌手邀约时「有点出神」（md:14） | `text/ch06_6.txt` 行 296：`‘Yeah.’ Callie looked a little spaced out.` | ✅ 与原文一致 | 通过 |
| A13 | 导航「一句话概括」：Dotty 办「不是婴儿洗礼的洗礼加乔迁聚会」（md:11） | `text/ch06_6.txt:459-667`（行 32）：`Dotty was having a non-baby shower-cum-housewarming.` | ✅ 一致 | 通过 |
| A14 | block 6「为什么这样写」：多蒂因怀孕不喝酒，是全场唯一清醒者（md:75） | `text/ch06_6.txt:4545-4647`（行 110）：`They’ve been drinking since lunchtime and predictably everyone is plastered. Except for me, of course.’ She patted her growing bump.` | ✅ 有原文支撑（推论） | 通过 |
| A15 | block 4：房子「看上去像一所牧师住宅」／卡莉担心「都铎复兴式的仿古建筑」（md:51） | `text/ch06_6.txt:2592-2911`（行 86）：`It looked like a vicarage. For a moment there Callie had worried it was going to be mock Tudor.` | ✅ 一致 | 通过 |
| A16 | block 3：查房价要用 Rightmove 无痕模式，「查朋友家的房产让我觉得挺脏」（md:41） | `text/ch06_6.txt:1598-1811`（行 59） | ✅ 一致 | 通过 |
| A17 | block 1「读者视角提示」：派对上说「有点不对劲」是开场紧绷的回响（md:27） | `text/ch06_6.txt:12361-12382`（行 302）：`‘No. I feel a bit off.’` | ✅ 一致 | 通过 |
| A18 | 词汇表 28 条例句均为本章原句 | 逐条 `str.count` 实测：**28/28 各命中 1 次**（表头行除外）；`scripts/check_vocab.py "<书目录>"` → ch06 **0 条报警**，退出码 0 | ✅ 通过 |
| A19 | 九块「关键词」均在引语内 | R2 `keyword_bad=0`；抽查 block 5（bemulletted / rosemary-marinated / electro-pop）、block 9（clockwork / full moon）均在引语原文内 | ✅ 通过 |
| A20 | 引语未跨章搬句 | 9 条引语在**全书 54 个 text 文件**中各命中 **1 次**（均在 ch06_6.txt 内），无第二处 | ✅ 通过 |

---

## 假红（工具口径，非 md 缺陷）

| 报警 | 证据 | 结论 | 档位 |
|---|---|---|---|
| `2-machine.json` 里每条引语的 `pos` 与我在原文中实测的字符位不一致（如 block 1：机器 `pos=13`，实测 `29`；block 8：机器 `pos=10711`，实测 `11175`） | 差值随引语内弯引号/单引号数量变化 | `scripts/bookform.py` 先把 `‘’` 归一化为 `'` 再做 `find`，**`pos` 是归一化串上的下标**，不是原文字符位 | **假红**——不改 md；引用原文位置请用 `str.find` 实测值（本报告全部区间均为实测值） |

---

## 跳过（未查 / 不建议查）

| 项 | 原因 | 档位 |
|---|---|---|
| 其余 53 章 | 受派范围仅 ch06；这些章**只有机器层**，不得写成「通过」 | 跳过 |
| L7 类闲笔（gender reveal 之问、porn 与 incognito 的玩笑、"Jolly Yeoman" 暗号、Ginger Pig 热狗、Caius 说工作压力大、Caius 最后只喝水） | 已逐条回原文确认存在，但属场景喜剧质地素材，不构成「关键事件/转折缺失」 | 跳过（不建议补） |

---

## 已核实为正确（防误修，固定一节）

以下写法**读着可疑但回原文核对后成立**，后续任何人不得以「读着不对」为由改动，除非能给出反证。

| # | md 写法 | 原文逐字（`text/ch06_6.txt`） | 结论 |
|---|---|---|---|
| S1 | block 2 译「不是婴儿洗礼的洗礼加乔迁聚会」 | 行 32 `Dotty was having a non-baby shower-cum-housewarming.` | ✅ 成立 |
| S2 | block 4 译「mock Tudor」为「都铎复兴式的仿古建筑」 | 行 86 `It looked like a vicarage. For a moment there Callie had worried it was going to be mock Tudor.` | ✅ 成立 |
| S3 | block 6 说 Dotty 因怀孕而唯一清醒 | 行 110 `They’ve been drinking since lunchtime and predictably everyone is plastered. Except for me, of course.’ She patted her growing bump.` | ✅ 成立 |
| S4 | 导航说卡莉在接下邀约时「有点出神」 | 行 296 `‘Yeah.’ Callie looked a little spaced out.` | ✅ 成立 |
| S5 | block 7 把 `private number` 译作「陌生号码」（词汇表另作「未登记在通讯录里的号码」） | 行 215 `It was a private number.` | ✅ 成立（两处口径不冲突） |
| S6 | block 3 说「想知道朋友家值多少钱又怕被看出来」 | 行 56 `‘How much was the house?’`（凯乌斯问）+ 行 59 `I’ll look it up on Rightmove when we get home.` | ✅ 成立 |
| S7 | block 1 说「开篇不解释她为什么紧张」 | 行 20 原文只给身体状态，无解释 | ✅ 成立（**但见 3-diff L6**：原文其实给了旁证——上次来 Richmond 是 Harriet 的订婚派对，持续五个星期） |
| S8 | 原文行 116 `‘Your boyfriend’s calling,’ Callie said to Caius…` 的**归属本身别扭**（像作者笔误或应指旁人喊话） | 行 116 逐字 | ⚠️ 这是**原文**的问题，不是 md 的问题——**不要**据此反过来把 md 的「丈夫」当正确；md 该改的是「丈夫→男友」 |
| S9 | block 5 逐项复述「头巾 / 紧身短裤 / 方檐帽 / 迷迭香猪排 / 泡泡糖电子乐」 | 行 113 `A gaggle of tipsy bemulletted men in tight short shorts and square-fronted baseball caps … rosemary-marinated pork chops … Bubblegum electro-pop …` | ✅ 物象清单逐项对上；**只有「东伦敦」的归属**有问题（见 W/提示 A7） |

---

## 最要紧的一条

**W3：block 8「为什么这样写」把卡莉自己的话当成多蒂的转述**（`text/ch06_6.txt:11054-11172` / `11175-11543`）。
引语里 `she has asked **yours truly** to help develop the whole concept` 的 `yours truly` 是说话人自称，而上一句是凯乌斯问 Callie `‘And what does Eulalia want from you?’` ⇒ 说话人是 **Callie**；Dotty 全章从未谈过头套（只有 `‘Eulalia as in the singer?’`、`‘Eulalia!’`、`‘Come on, spill, Cal.’` 三句）。
它躲得过全部四道机器探针（引语逐字 ✓、中文是中文 ✓、关键词成立 ✓、形态正常 ✓），且直接违反本章专属判据——**这一段正是「卡莉在这场聚会里的观察欲与不安」的出口**：她被一个「没人知道她长什么样」的谜题找上门，把职业焦虑转成创造欲。md 把它写成「多蒂转述、卡莉的回应是别处」，等于把这条人物线掰成了别人的八卦。
修法（只动一处）：`多蒂转述时` → `卡莉自己转述给凯乌斯时`（或「卡莉向凯乌斯转述时」）。
