# ch21 R5 判定表

- 审查对象：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch21 benedict reports a break in.md`
- 权威源：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch21_21.txt`（1872 字符）
- 受审 md 的 md5：`99ca78ca2d5c0e835a4fb71086aa5bd4`（size 12176）
- ⚠️ **审查期间的并发改动**：我在 14:2x 读到的是 `在分部「A WEDNESDAY IN MAY」里`；另一实例于 **14:33:53** 把该行改成 `在分部「WEDNESDAY」里`（size 12185→12176）。已**全文重读**确认**其余 99 行逐字未变**，机器层已对当前版本重跑（exit 0 / verdict ok，数字与前一次完全一致）。⇒ 本判定表对 md5 `99ca78c…` 成立。
- 落盘目录：`.memory/raw-gates/a-fatal-legacy-by-charlotte-vassell/review/ch21/`（未改动书目录任何 md；未 git add / commit）

---

## 一、四组数

| 组 | 结果 | 说明 |
|---|---|---|
| **逐字** | **5 / 5 通过** | `chapter.sh --json`：`quotes` 5 条、`segments` 5、`segment_miss 0`、`empty_quote 0`；5 条引语均为**连续单段**，无 `…` 缝合、无跨话轮拼接（故无需逐片段独立取证）。逐字组无扣分项。 |
| **对应** | **5 / 5 成立**（块 1 附带 1 条施事/归属错，计入断言组） | 逐块回答「这段中文是不是在讲这句引语」：**没有**「讲引语之外的上下文」（引语选短）、**没有**「讲全书主旨/作者生平」（不对应）、**没有**「只复述字面没有为什么这样写」（密度不足）。见 `4-correspondence.md`。 |
| **形态** | **4 / 4 无偏离** | H1 `21. The Police Station`（本书众数写法 `N.`，54/54 章一致）；导航 **5** 项（一句话概括 / 视角 / 线索结构 / 人物弧线 / 叙事手法，本书众数 5）；子项集 **4** 项（中文理解 / 关键词 / 为什么这样写 / 读者视角提示，本书众数 4，与 genre profile `mystery-thriller` 一致）；块数 **5**（本书中位 7.0、范围 5–10、profile 3–10）⇒ **块数落在众数区间内，不构成偏离，无需写理由**。 |
| **断言** | 核 **28** 条 → **阻断 1 / 提示 14 / 通过 12 / 假红 1** | 明细见下表。阻断 1 条＝块 1 的施事/归属反转。 |

**阻断型条数：1**

---

## 二、断言表

| # | 断言 | 证据（章:区间 / 行） | 结论 | 档位 |
|---|---|---|---|---|
| A1 | **块 1「作案人是住在普里奥里广场七号的一位贝内迪克特·卡尔-里奇」** | `text/ch21_21.txt:20`（字符 41–488）：`a report on an attempted burglary that had been made by a certain Benedict Carr-Ridge who lived at 7 Priory Square. His name was familiar but Caius wasn’t sure why. It became apparent quite early on in the report that Benedict wasn’t a reliable witness. The officer who had interviewed him wasn’t even convinced the incident had happened.`；`text/ch19_19.txt:116` `‘I thought you might want to know that a break-in was reported on Priory Square this morning.’`、`:122` `‘Seven.’`、`:128` `‘No, the guy who reported it was apparently half-cut.’`；`text/ch31_31.txt:56` `Benedict’s basement and back doors were wide open when he woke up.`；`text/ch37_37.txt:77` `‘Caius interviewed Benedict Carr-Ridge, the novelist. He lives at number 7. It was a break-in, although—’`、`:83` `‘…and that Benedict was drunk at the time.’` | 原文及后文都把贝内迪克特置于**报案人／证人／7 号住户（被害人）**位置，从未说他是作案人；md 自己的**文件名**（`benedict reports a break in`）、**一句话概括**（报案人喝了酒）、**线索结构**（不可靠的报案人）也都写他是报案人 ⇒ 块 1 与原文、与 md 其余部分**双双不符** | **阻断** |
| A2 | 「**出警的**警员甚至不信事情发生过」 | `text/ch21_21.txt:20`：`The officer who had interviewed him wasn’t even convinced the incident had happened.` | 原文是**问话（interview）**他的警员，不是出警警员 | 提示 |
| A3 | 「报案人喝了酒 / 不可靠的报案人 / 满地空酒瓶」 | `text/ch21_21.txt:20`：`The empty bottles littered about the place hadn’t helped his credibility.`；`text/ch19_19.txt:128`：`the guy who reported it was apparently half-cut`；`text/ch37_37.txt:83`：`Benedict was drunk at the time` | 成立 | 通过 |
| A4 | 「普里奥里广场**七号**」（= 这桩入室盗窃的地点） | `text/ch21_21.txt:20`：`who lived at 7 Priory Square`；`text/ch19_19.txt:119–122`：`‘A break-in? What number?’` `‘Seven.’` | 成立（ch19 的「Seven」与 ch21 的 7 号是同一处） | 通过 |
| A5 | 「和命案共用同一个广场」「一片出过命案的广场」 | `text/ch01_1.txt:17` `The Horatio Combe Institute, Priory Square, Camden`；`:20` `Digby Combe-Watson is sprawled out on the antique rug…`；`text/ch02_2.txt:17` 同址 | 成立：命案现场（研究所）就在 Priory Square ⇒ 本章的「相邻」机关成立 | 通过 |
| A6 | 「交代马特被派往哈罗盖特去查那个邮政信箱」 | `text/ch21_21.txt:578–608`：`‘He’s been sent to Harrogate.’`；`:673–992`：`The PO Box was paid for by a woman called Beverley Parkin who lives there.`（ch22 即 ch19 线索的下一步：问讯 Beverley Parkin） | 成立 | 通过 |
| A7 | 「信箱由住在哈罗盖特的帕金太太付钱，警方认为算某种欺诈」 | `text/ch21_21.txt:673–992` | 成立 | 通过 |
| A8 | 「巴内特邮局的监控只覆盖那几天」 | `text/ch21_21.txt:673–992`：`security footage but only covering the days that the last three letters were likely sent or received` | 成立 | 通过 |
| A9 | 「Met 试用跨多段录像追踪人脸的程序；申请加入；转发资料；等程序到了再处理」 | `text/ch21_21.txt:1103–1361` | 成立 | 通过 |
| A10 | 「艾米以『讨厌看 CCTV』把这份安排推开」 | `text/ch21_21.txt:1364–1509` | 成立 | 通过 |
| A11 | 「现场什么也没被偷走」 | `text/ch21_21.txt:1593–1611` `‘Anything stolen?’` + `:1614–1626` `‘Apparently not.’` | 成立 | 通过 |
| A12 | 「天气太潮，眼下穿不得，等到了普里奥里广场再穿」 | `text/ch21_21.txt:1614–1871`：`It was too humid to wear it but he would once he got to Priory Square.` | 成立 | 通过 |
| A13 | 「**穿上**这件外套让他觉得自己像个大人」 | `text/ch21_21.txt:1614–1871`：`It was too humid to wear it but he would once he got to Priory Square. It made him feel like an adult.` | 时序错位：原文此刻（还没穿）已让他觉得；md 却归到「穿上」，且与自己前半句「眼下穿不得」冲突 | 提示 |
| A14 | 「这个案子他们能追的线索已经不多了」 | `text/ch21_21.txt:1614–1871`：`we are running out of leads fast with this one` | 成立 | 通过 |
| A15 | 「出门前又**低声**承认线索快用完了」「章末落到他对这桩小案的**低声**怀疑」 | `text/ch21_21.txt:1614–1871`（该句是对话，当面说出） | 「低声」这一层语气是原文没有的 | 提示 |
| A16 | 「警探穿着**还没干透**的西装外套出门」 | `text/ch21_21.txt:1614–1871`：`It was too humid to wear it but he would once he got to Priory Square.` | 原文是**天气太潮**，不是外套湿了未干；且他出门那一刻尚未穿上 | 提示 |
| A17 | 「全章靠对话推进」 | `text/ch21_21.txt:41–488`（整段叙述）与 `:1614–1871` 后半（`Caius grabbed his suit jacket…`） | 开篇与收尾均为叙述，非全靠对话 | 提示 |
| A18 | 「被空酒瓶和**一纸空案卷**冲淡了可信度」 | `text/ch21_21.txt:41–488` | 原文是**一份关于未被证实的报案的报告**（有卷宗），空的是案不是卷 | 提示 |
| A19 | 「作者偏要让它和旁边那桩广场上的入室盗窃**在同一段对话里**来回答疑」，「让读者下意识把『信箱』和『广场』当成可以互换的两样东西」 | `text/ch21_21.txt:673–992`（信箱对话）与 `:1512–1590`（`I’m going to go check out a burglary on Priory Square.`） | 入室盗窃**不在**这段信箱对话里（`:44` 才出现）；且原文的「巧合」指向**广场上的盗窃与本案**（`text/ch31_31.txt:74`：`‘The PO Box connection cannot be a coincidence.’` / `‘These two break-ins could be a coincidence.’`），md 换成「信箱↔广场」 | 提示 |
| A20 | 「这名字他有印象，却想不起为什么」 | `text/ch21_21.txt:41–488`：`His name was familiar but Caius wasn’t sure why.` | 成立 | 通过 |
| A21 | 导航·视角「读报告—**听汇报**—从椅背上抓外套准备出门」 | `text/ch21_21.txt:673–992`：`Caius said, rapping his fingers on the desk.`；`:491–575`：Amy 进屋先问的是赌注 | 汇报 PO Box 进展的是**凯厄斯**，不是他在听汇报 | 提示 |
| A22 | 块 2 中文理解「**艾米问马特被派到哪里**」 | `text/ch21_21.txt:491–670`：`‘Did I beat Matt in?’` / `‘He’s been sent to Harrogate.’` / `‘That’s better than being sent to Coventry. Why Harrogate?’` | 原文 Amy 问的是赌注与「为什么是哈罗盖特」，没有「问马特被派到哪里」这一问（为 md 自造的问答） | 提示 |
| A23 | 块 2 中文理解「只覆盖**末几封**信可能寄出或收到的那些日子」 | `text/ch21_21.txt:673–992`：`the last three letters` | 数字「三」在中文理解里丢失（仅关键词行保留 `last three letters`） | 提示 |
| A24 | 原文「Tiny Simm flagged it」——**md 全文无此人** | `text/ch21_21.txt:1512–1590`：`‘I’m going to go check out a burglary on Priory Square. Tiny Simm flagged it.’`；`text/ch19_19.txt:110–134`（Simm 报「广场 7 号」入室盗窃 + `‘It’s rare for two things to happen in one small square like that so close together.’`） | **漏**：读者失去与 ch19 的接口，也失去 Simm 亲口那句「一个小广场上短期内难得发生两件事」——这正是本章「相邻」效果的外化 | 提示 |
| A25 | 原文 `‘Did I beat Matt in?’` 与 `‘That’s better than being sent to Coventry.’`——**md 无** | `text/ch21_21.txt:491–670` | **漏**：「Matt 被派往哈罗盖特」少一个动因（赌注），Coventry 的对照笑点也丢了 | 提示 |
| A26 | 原文 `‘Are you telling me that I have to watch three days’ worth of footage of people returning online orders?’`——**md 无** | `text/ch21_21.txt:995–1100` | **漏**：Amy 的这记笑点与「三天」这个数都没进 5 条引语 | 提示 |
| A27 | 导航「在分部『**WEDNESDAY**』里」 | 本章原文**无任何日期字样**（取证见下）；兄弟章：`ch22`/`ch24`/`ch26` 写「本章属『五月的星期三』这一分部」，`ch25`/`ch27` 写「在分部『A WEDNESDAY IN MAY』里」，`ch28`–`ch31` 为 THURSDAY、`ch36`–`ch39` 为 FRIDAY、`ch42` 为 SATURDAY | 分部归属**成立**（ch21 落在星期三分部内）；但写法「WEDNESDAY」与兄弟章「A WEDNESDAY IN MAY／五月的星期三」不同形（且该行正在被另一实例改动中） | 提示 |
| A28 | 词汇档位：基础档含 `apparently` / `coincidence` | `python3 scripts/check_vocab.py <书目录>` → `--- FAIL (0) ---`，`--- WARN (26) ---`，**退出码 0**；同类 WARN 遍布全书（ch13/18/19/26/33/34/39/41/46/50/52/54…） | 工具口径问题：词表黑名单不含语境，全书同判、从未进 FAIL；且这两个词在本章句中均为常见词 | **假红** |

**合计：阻断 1 · 提示 14 · 通过 12 · 假红 1（共 28 条）**

---

## 三、已核实为正确（防误修，固定一节）

以下写法**看着像错**，回原文核对后**成立**；后续任何人不得以「读着不对」为由改动，除非能给出反证。

1. **「报案人喝了酒」「不可靠的报案人」「满地空酒瓶」**——成立。`text/ch21_21.txt:20`：`The empty bottles littered about the place hadn’t helped his credibility.`；`text/ch19_19.txt:128`：`‘No, the guy who reported it was apparently half-cut.’`；`text/ch37_37.txt:83`：`‘…and that Benedict was drunk at the time.’`
2. **「普里奥里广场七号」作为这桩入室盗窃的地点**——成立。`text/ch19_19.txt:119–122`：`‘A break-in? What number?’` `‘Seven.’`
3. **「和命案共用同一个广场」「这片出过命案的广场」**——成立。`text/ch01_1.txt:17` `The Horatio Combe Institute, Priory Square, Camden`；`:20` `Digby Combe-Watson is sprawled out on the antique rug…`
4. **「马特被派往哈罗盖特去查那个邮政信箱」**——成立（Harrogate 由 PO Box 付款人所在地说出）。`text/ch21_21.txt:578–608`：`‘He’s been sent to Harrogate.’`；`:673–992`：`The PO Box was paid for by a woman called Beverley Parkin who lives there.`
5. **「Met ＝ 伦敦警察厅」**——成立。`text/ch21_21.txt:1103–1361`：`the Met is trialling a computer program…`（ch22:29 `‘DS Matthew Cheung, from the Metropolitan Police’` 亦证）。
6. **块 3/块 4 的「申请加入试用 / 转发资料 / 等程序到了再处理」「放它一马」**——成立，逐字对得上 `text/ch21_21.txt:1103–1361` 与 `:1364–1509`。
7. **「什么也没被偷走」**——成立。`text/ch21_21.txt:1593–1611` `‘Anything stolen?’` → `:1614–1626` `‘Apparently not.’`

---

## 四、零命中类断言的自证（R5-补）

本节两条断言形如「查无」，按规则附**原命令 + 输出 + 退出码**。
（`text/` 被 `.gitignore` 排除 ⇒ `git grep` 与尊重 ignore 的 rg 系在该目录恒为空且退出码 1 不可区分，故**只用 `/usr/bin/grep` + 显式文件路径**。）

```
/usr/bin/grep -inE "simm|西姆" "notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch21 benedict reports a break in.md" > /tmp/o1 2>&1; echo $?
→ 无输出；退出码 1（无匹配）   # 用于 A24：md 全文没有 Tiny Simm
```

```
/usr/bin/grep -inE "wednesday|may|june|april" notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch21_21.txt > /tmp/o2 2>&1; echo $?
→ 无输出；退出码 1（无匹配）   # 用于 A27：本章原文没有任何日期/星期/月名字样
```

```
/usr/bin/grep -rn "Carr-Ridge" notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ | cut -c1-300
→ text/ch21_21.txt:20 / text/ch31_31.txt:38,62 / text/ch37_37.txt:77,95 / text/ch24_24.txt:20,26；退出码 0
   # 用于 A1：贝内迪克特在全书的每一次出现都作「7 号住户／小说家／证人／醉酒的报案人」，从未作作案人
```

```
/usr/bin/grep -rn "Tiny Simm" notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ | cut -c1-300
→ text/ch21_21.txt:44 / ch19_19.txt:110,116 / ch33_33.txt:148 / ch07_7.txt:82,94,137 / ch05_5.txt:135,138 / ch45_45.txt:20,26,32 / ch41_41.txt:121；退出码 0
```

---

## 五、覆盖声明

- **ch21：全量人工审查（R1 素读 → R2 机器层 → R3 三张单子 → R4 逐块 → R5 判定）**，已完成。
- **机器层（可复现）**：`bash scripts/chapter.sh "<书目录>/ch21 benedict reports a break in" --json` → 退出码 **0**、`verdict: ok`；`python3 scripts/check_vocab.py <书目录>` 退出码 **0**（FAIL 0 / WARN 26）；`python3 scripts/verify_corpus.py <书目录>` **PASS**（FAIL 0 / WARN 3，WARN 均与 ch21 无关：未给 `--expect`／未给 `--anchors`／ch23 页码 bleed）；`python3 scripts/bookform.py <书目录>` 退出码 0；`python3 scripts/corruption_scan.py <书目录>` FAIL 0；`python3 scripts/check_speaker_consistency.py <书目录>` 归因不一致 **0**（**注意：该工具报 0 不等于说话人都对**，本章的施事错误正是它查不出的一类）。
- **本书其余 53 章：只有机器层**，本次**未做人判**——不得读作「通过」。
- 本次审查**未改动**书目录任何 md，**未** `git add` / `git commit`；产物只写在 `.memory/raw-gates/a-fatal-legacy-by-charlotte-vassell/review/ch21/`。

---

## 六、修复优先级建议（仅建议，未执行）

1. **阻断**：块 1 中文理解（md 第 21 行）——把「**作案人**是住在普里奥里广场七号的一位贝内迪克特·卡尔-里奇」改成「**报案人／7 号住户**是……」（原文只把他写成 unreliable witness；ch19/ch31/ch37 三处证明他是被害方）。改后重跑 `chapter.sh`。
2. 提示级（可选一并处理）：块 5 中文理解「穿上这件外套让他觉得自己像个大人」→「这件外套让他觉得自己像个大人」（对齐 `It made him feel like an adult.`）；一句话总结「穿着还没干透的西装外套出门」→「提着他嫌潮、准备到广场再穿的外套出门」；导航两处「低声」删去；导航·叙事手法「全章靠对话推进」→「除开篇一段叙述外主要靠对话推进」；块 2 中文理解「艾米问马特被派到哪里」→「艾米问『为什么是哈罗盖特』」并补回「三封信」；块 2「为什么这样写」删去「在同一段对话里」；补写 Tiny Simm（他才是广场这桩案子的报信人，也是 ch19 与本章的接口）。
