# 4-verdict.md · ch29《A Fatal Legacy》审查判定

- 审查员：独立审查实例（指派范围：**仅第 29 章**）
- 权威源：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch29_29.txt`（5464 字符）
- md：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch29 callie gets a blood test.md`
- 读取顺序：R1 素读 → 落盘 `1-suread.json` → R2 机器层 → **才**开 md（铁律遵守）
- 落盘目录：`.memory/raw-gates/a-fatal-legacy-by-charlotte-vassell/review/ch29/`
- **未改动书目录任何 md；未执行 git add / commit。**

---

## 四组数（只报这四组）

| 组 | 数 | 明细 |
|---|---|---|
| **逐字** | **6/6 引语逐字命中（100%）**；词汇例句 25/25 逐字且各命中 1 次 | `2-machine.json`：6 段全部 `ok: true`，`segment_miss: 0`；机器层 `verdict: ok`，`issues` 四类全空 |
| **对应** | **6/6 块对应，密度合格；不通过 0 块** | 引语选短需回退 **3 块**（块 2、3、6）＝提示；施事/归属方向不一致 **1 块**（块 4，仅分析层）＝提示 |
| **形态** | **0 偏离** | H1 / 导航 5 项 / 子项集 4 项 / 块数 6 —— 四项均在本书众数与 profile 内（详见下节） |
| **断言** | **核 24 条：阻断 2 · 提示 10 · 正确 12（假红 0 · 跳过 0）** | 见下表 |

**阻断型条数：2**（均为导航/线索结构层的因果断裂，不在引语逐字层——机器四道探针全绿也查不出）。

---

## R2 机器层（自跑，退出码 0）

```
bash scripts/chapter.sh "notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch29 callie gets a blood test" --json \
  > .memory/raw-gates/a-fatal-legacy-by-charlotte-vassell/review/ch29/2-machine.json
→ EXIT=0   （0 无阻断；2 才是"无法判定"，本次不是）
counts: blocks 6 · segments 6 · segment_miss 0 · struct_bad 0 · empty_quote 0 · keyword_bad 0 · cjk_low 0
issues: struct [] / empty_quote [] / keyword [] / cjk []
```

**注意**：`cjk.关键词 = 0` 不是缺失——md 的「关键词」子项内容是英文词条本身（如 `cotton wool / community midwife / vitamin D deficiency`），中文计数天然为 0，`keyword_bad = 0`、`cjk_low = 0`。**这是工具口径，不是内容缺陷。**

机器层的覆盖面只到"引语英文逐字 + 中文是中文 + 关键词成立 + 形态正常"；**本章两条阻断都不在它能读的层**。

---

## R5 判定表（断言 | 证据 | 结论 | 档位）

### 阻断型（2 条）

| # | 断言 | 证据（章:区间 · 原文逐字） | 结论 | 档位 |
|---|---|---|---|---|
| **B1** | md 导航「线索结构」把花束与卡片写成"**提前一天送到**"（既成事实），且全篇**没有一句**交代"这个给 Eulalia 的项目明天上午才结束"——本章收束的因果链整段缺失 | `text/ch29_29.txt:23`（1529–1695）："**This project for Eulalia had come from nowhere, wreaked havoc for an intense week and then after tomorrow morning would be gone again. She was glad of its transience.**"<br>`text/ch29_29.txt:98`（5044–5171）："**This is a bit weird right? I’d understand her sending this tomorrow afternoon once the project is finished but this is intense.**"<br>`text/ch29_29.txt:105`（5178–5212）："**Maybe it was sent a day too early?**"<br>md:11、md:13、md:28、md:67（词汇表收了 `transience` 却从未解释其含义） | 「提前一天」在原文里只是 Callie 的**猜测**（"Maybe…"），md 把它升格为事实；同时抽掉了它唯一的依据（项目明天上午才结束）。md 的凯莉没有说出"奇怪""项目还没结束"，读者也无从理解这束花为什么早到 | **阻断** |
| **B2** | md 导航两处把邻居的警告写在「**楼道**」，并把「血样」对应到「**咖啡店里的闲话**」 | `text/ch29_29.txt:44`（3054–3500）："…She smiled sororally at the woman (Caius’s parents’ tenant) who lived on the floor above them as she walked in the opposite direction. **She stopped Callie.**"<br>`text/ch29_29.txt:56`（3695–3743）："**They parted ways and Callie returned to the flat**, shutting the door firmly behind her…"<br>`text/ch29_29.txt:20`（227–313）："**She’d had blood taken, been weighed and had her height measured by a community midwife.**"<br>md:12"…转到回家路上的街、**楼道**，再到自己家的客厅与沙发"；md:13"它们分别由**咖啡店里的闲话**、楼道里的耳语和送货员递到门前" | 原文里警告发生在**街上**（二人分道后她才回家），**全程没有楼道场景**；血样的来路是**社区助产士**，与咖啡馆闲话（内裤插曲）无关。md 两处凭空添加了场景、并把三条线索与三条通道错配 | **阻断** |

### 提示型（10 条）

| # | 断言 | 证据（章:区间 · 原文逐字） | 结论 | 档位 |
|---|---|---|---|---|
| H1 | 导航「在分部「**A THURSDAY IN MAY**」里」 | epub `OPS/s041-Part-007.xhtml`："THURSDAY 173 THURSDAY 174"（该分部扉页仅写 "THURSDAY"，覆盖 s042-ch28…s048-ch34）；epub `OPS/s005-TableOfContents-01.xhtml` 只有第一部写作 "A FRIDAY IN MAY"；另 `text/ch20_20.txt:38`："Yeah, I’ve got an appointment with the community midwife on Thursday." | **归属正确**（ch29 确在 THURSDAY 分部，且抽血是周四的助产士预约，与本章互证）；但「A … IN MAY」是 md 自造措辞，非原文。**全书通例**（ch28/30/31/33/34 等同款），非本章独有问题 | 提示 |
| H2 | 送花场景的关键信息未进精读 | `text/ch29_29.txt:59–65`（4468–4874）："‘Calliope Foster,’ the delivery man asked." … "Callie took the flowers into the living room. They were a chaotic arrangement from a florist she recognised as being based near Sloane Square. **Callie thought they were perhaps from her father. Caius had already sent her a bunch that week.** She opened the card." | md:13 只写"一束花"，**"也许是父亲寄的""Caius 本周已送过一束"整章不出现**（md 全文检索无"父亲/Sloane/已经送过"）。父亲这条线在 ch35 落地，本章是它的伏笔 | 提示 |
| H3 | 凯莉发给凯厄斯的消息内容未进精读 | `text/ch29_29.txt:98`（5044–5171）、`:105`（5178–5212） | 两句消息只在词汇表以 "bit weird" 的例句形式露过一次脸；全章"等待"的最后一个动作（她把怀疑发出去）没有分析 | 提示 |
| H4 | 内裤对话在第一句后截短 | `text/ch29_29.txt:26–41`（2581–3051）："'Eaten by the tumble dryer or what?'" / "'Taken from my washing line.'" / "Callie turned to the woman. 'Sorry to interrupt, but I couldn’t help but overhear. **You should report that.**'" / "'Maybe,' Callie said, **feeling silly all of a sudden**. 'Sorry again, enjoy your coffee.'" | md 块 3 的「为什么这样写」用"真正**该报警**"作对照，依赖的正是被截掉的 "You should report that." ⇒ 引语选短（创建卡 §2 ①） | 提示 |
| H5 | 块 4「为什么这样写」："收尾那句独立的"She stopped Callie"**先给出身体的僵住**…先读到了**她的反应**" | `text/ch29_29.txt:44`（3481–3500）："**She stopped Callie.**"（"She"＝邻居，主动拦截；受事＝Callie） | 施事方向与原文相反（把邻居的动作读成凯莉身体的被动僵住）；**但同一块 md:42「中文理解」写"被对方叫住"是对的**，属块内表述打架。严格按《生产-审查对照》⑥可升为阻断，按"理解层已写对"记提示 | 提示 |
| H6 | 块 2「中文理解」："**恶心得**连再**犬儒的人**看了都要受不住"；同块「为什么这样写」却用"**骇人**" | `text/ch29_29.txt:23`（692–774）："…onto a page **to freak even the most cynical person out**." | "freak out"＝吓坏/惊到，不是"恶心"；块内两种定性不一致。"cynical" 硬译"犬儒"在中文里指犬儒学派，中文读者会读偏 | 提示 |
| H7 | 「Christine de Pizan 和她的**《女骑士团》**」 | `text/ch29_29.txt:110`（5371–5463）："She put on another Radio 4 programme on Christine de Pizan and her **City of Ladies** and tried to forget about it." | "City of Ladies"（*The Book of the City of Ladies*）字面为"女士之城/城市女士"，"骑士团"这层意思原文没有；md 自己的英文原句就贴在旁边可当场核对。**未核**：本机离线，无法核对是否存在出版社的正式中译名，故不判阻断 | 提示 |
| H8 | "只**签了一半**的卡片" | `text/ch29_29.txt:75–78`（4905–4945）："Dear Cal," … "I had such a great time. **E x**" | 原文只给落款 "E x"（首字母 + x），无"一半"的说法；读法可辩（仅落首字母），但字面无据 | 提示 |
| H9 | "我觉得我的内裤**少了几条**" | `text/ch29_29.txt:26`（2660–2730）："'I know this sounds crazy but I think I'm missing **some of my underwear**?'" | "some" 未指条数，"几条"是加数 | 提示 |
| H10 | "直到这一页还差一点**没对齐**" | `text/ch29_29.txt:56`（4321–4403）："Moving images around ever so slightly until the slide was only a little **imperfect**." | imperfect＝不完美，非"没对齐" | 提示 |

### 正确型（12 条，摘要）

| # | 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|---|
| C1 | 「血样（本章始终没有出现结果）」「没有人告诉她结果」「血检结果本身始终缺席」 | `text/ch29_29.txt` 全章仅第 20 行 "She’d had blood taken…"；**无任何结果通知、数值或结论** | 正确 ✔（**本章专属判据第 1 条通过：md 没有把「等待」写成「结果」**） | 正确 |
| C2 | 「没有等来任何答复」 | 同上 | 正确 ✔ | 正确 |
| C3 | 「社区助产士还替她称了体重、量了身高」 | `text:20`（227–313） | 正确 ✔ | 正确 |
| C4 | 「楼上那位（凯厄斯父母的房客）女士」 | `text:44`（3381–3404）"(Caius’s parents’ tenant)" | 正确 ✔ | 正确 |
| C5 | 「随后被对方叫住」（中文理解层归属） | `text:44`（3481–3500） | 正确 ✔（分析层另见 H5） | 正确 |
| C6 | 「露阴者」 | `text:56`（3624–3655）"She mouthed the word ‘flasher’." | 正确 ✔ | 正确 |
| C7 | 「自从认识凯厄斯，她开始到处都看见危险」 | `text:44`（3144–3202） | 正确 ✔ | 正确 |
| C8 | 「连名望都看淡成‘一个空洞的闪光’」 | `text:23`（2467–2494）"It was all an empty glimmer" | 正确 ✔ | 正确 |
| C9 | 「要养活一个小生命」 | `text:23`（2345–2392）"one preoccupied with keeping a tiny human alive" | 正确 ✔ | 正确 |
| C10 | 「可爱与骇人被同一个形容词并置」 | `text:23`（1059–1104）"equally adorable and macabre" | 正确 ✔ | 正确 |
| C11 | 「一条没被读到的消息」（未读方＝凯厄斯，方向正确） | `text:110`（5217–5249）"Her message was left on one tick." | 正确 ✔ | 正确 |
| C12 | 「最后打开 Radio 4 听 Christine de Pizan 的一档节目」「用广播把等待盖过去」 | `text:110`（5371–5463） | 正确 ✔ | 正确 |

---

## 形态组（对照本书众数 / profile）

| 项 | 本章 | 本书众数 / profile | 偏离 |
|---|---|---|---|
| H1 | `# 29. Running Latte Coffee Shop, Dartmouth Hill` | 众数＝「# N. <epub 场景标题>」（逐章核对 ch01–ch50 全部同形） | 无 |
| 导航项名与项数 | 5 项：一句话概括 / 视角 / 线索结构 / 人物弧线 / 叙事手法 | 众数 5（`2-machine.json: nav_count 5, nav_count_ok true`） | 无 |
| 子项集 | 中文理解 / 关键词 / 为什么这样写 / 读者视角提示 | profile `mystery-thriller` ＝ 同四项；`subitems_modal` 一致 | 无 |
| 块数 | 6 | 本书众数 7，区间 [5, 10] | 无（**6 落在区间内**，故无需写偏离理由） |

⇒ 形态组 **0 偏离**，不写理由行。

---

## 已核实为正确（防误修 · 后续任何人不得以「读着不对」为由改动）

1. **「血检结果本章始终缺席」**（md:13/24/104 三处）——原文 `text/ch29_29.txt:20` 只有 "She’d had blood taken…"，**全章无结果、无通知、无数值**。这是本章专属判据的核心，**不得**因为"md 没写结果"就判定为"漏写结果"。
2. **「被对方叫住」（md:42）**——原文 `text:44` "She stopped Callie."，施事是邻居、受事是 Callie，md 归属正确。（同块 md:44 的"身体的僵住"另见 H5。）
3. **「一个空洞的闪光」**——`text:23` "an empty glimmer"。
4. **「要养活一个小生命」**——`text:23` "one preoccupied with keeping a tiny human alive"。
5. **「露阴者」**——`text:56` "She mouthed the word ‘flasher’."
6. **「一条没被读到的消息」**——`text:110` "Her message was left on one tick."（**凯莉发出、凯厄斯未读**，方向不可反）。
7. **「可爱与骇人并置」**——`text:23` "equally adorable and macabre"。
8. **H1 用场景标题而非文件名**——本书 50 章全部如此（ch01–ch50 逐章核对），ch29 也不例外，**不是偏离**。
9. **分部归属「THURSDAY」**——epub `OPS/s041-Part-007.xhtml` 扉页即 "THURSDAY"，覆盖 ch28–34；**ch29 确在其中**。
10. **词汇例句 25 条全部逐字且各命中 1 次**（`3-diff.md` 文末取证命令，输出 `词条数 25 | 例句命中数≠1 的条数: 0`）。

---

## 覆盖声明（谁查了、谁没查）

- **本次人判：仅 ch29**（指派范围）。逐字 / 对应 / 形态 / 断言四组数**只覆盖 ch29**。
- 同书其余 53 章：**未人判**。ch29 的 `chapter.sh` 机器层退出码 0 只代表 ch29；**不能据此外推到其他章**。
- 本次未检查：`00_概述.md` / `00_金句精选.md` / `00_情感节点.md` 的**全局**断言；只核了它们引用的 ch29 一条 —— `00_情感节点.md:90` 引 ch29 的 "Her message was left on one tick…" 与本章原文一致 ✔。
- 语料层：已核 `text/ch29_29.txt` 与 epub `OPS/s043-Chapter-029.xhtml` **逐段一致**（34 段中仅 4 个页码 182–185 未入 `text/`），无并章、无截断 ✔。

## 「零命中」类断言的自证（按 R5-补）

**断言**：「A THURSDAY IN MAY」这一分部名在 `text/` 语料中**查无**（故不能以 `text/` 证明，只能以 epub 证明）。

```
/usr/bin/grep -rni "thursday" notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ > /tmp/o1 2>&1; echo "EXIT=$?"
→ EXIT=0
→ 唯一命中：notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch20_20.txt:38
   ‘Yeah, I’ve got an appointment with the community midwife on Thursday.’
```
（用 `/usr/bin/grep` + 显式路径，**未**用 `git grep`／rg 默认 ignore 规则——`text/` 被 `.gitignore` 排除，用错工具会得到不可区分的"零命中"。）

**改用 epub 验证分部归属**：
```
python3 - <<'PY'
import zipfile,re
z=zipfile.ZipFile("notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/library/A Fatal Legacy (Charlotte Vassell) (z-library.sk, 1lib.sk, z-lib.sk).epub")
for n in sorted(z.namelist()):
    if "Part-" in n or "Chapter-029" in n:
        d=z.read(n).decode("utf-8","ignore"); t=re.sub(r"<[^>]+>"," ",d); t=re.sub(r"\s+"," ",t).strip()
        print(n,"::",t[:80])
PY
→ OPS/s041-Part-007.xhtml :: THURSDAY 173 THURSDAY 174
→ OPS/s043-Chapter-029.xhtml :: 29 182 29 Running Latte Coffee Shop, Dartmouth Hill Callie quickly pulled the cotton wool …
退出码 0
```
⇒ **ch29 属 THURSDAY 分部成立**；"A THURSDAY IN MAY" 只是 md 的措辞（H1）。

**未核项声明**：H7（"City of Ladies" 是否另有出版社正式中译名）——本机离线无法联网核对，按 R5 硬约束记为**提示**而非阻断。

---

## 最要紧的一条

**B1：md 把"提前一天收到花束"写成了既成事实，却抽掉了它唯一的依据。**
原文里"早了一天"是**凯莉自己的猜测**（"Maybe it was sent a day too early?"），而它之所以可能成立的唯一理由是「这个给 Eulalia 的项目**明天上午**才结束」——这句话 md 全篇没有写；连收在词汇表里的 `transience`（例句 "She was glad of its transience."）指的正是这件事，md 也从未解释。
后果是本章从"抽血无结果"到"卡片提前到达"的因果链**在 md 内断成两截**，读者拿不到"等待"这个主题在结尾的落点——而这恰是本章专属判据盯的地方。（两条阻断中，这条伤的是**情节逻辑**；B2 伤的是**场景与线索对应**。）
