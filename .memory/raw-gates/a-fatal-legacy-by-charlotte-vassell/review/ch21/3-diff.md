# ch21 三张单子（漏 / 编 / 错）

- 章：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch21 benedict reports a break in.md`
- 唯一权威源：`text/ch21_21.txt`（全文 1872 字符，行号与字符区间一并给出）
- 跨章取证：`text/ch19_19.txt`（Tiny Simm 报「广场 7 号」入室盗窃）、`text/ch31_31.txt`（Benedict 家后门/地下室被撬开）、`text/ch37_37.txt`（案情板复盘：Benedict 是 7 号住户/证人）
- 审法：R1 素读先落盘（`1-suread.json`），再读 md；R2 机器层 `chapter.sh --json` exit=0 / verdict=ok

---

## 一、漏（素读有、md 无）

| # | 事项 | 原文逐字 | md 侧 | 档位 |
|---|---|---|---|---|
| L1 | **Tiny Simm 这个报信人整体消失** | `text/ch21_21.txt:44` — `‘I’m going to go check out a burglary on Priory Square. Tiny Simm flagged it.’`；`text/ch19_19.txt:116` — `‘I thought you might want to know that a break-in was reported on Priory Square this morning.’`；`:122` — `‘Seven.’`；`:128` — `‘No, the guy who reported it was apparently half-cut. … It’s rare for two things to happen in one small square like that so close together.’` | md 全文（含导航、5 个块、一句话总结）无 “Tiny Simm/西姆” 任何字样；块 5 中文理解直接写「他要去普里奥里广场」，未说这是同事报上来的 | **提示**（非阻断：案件事实——7 号、入室盗窃未遂、无人报案人不被信、无失窃——都在；但读者失去与 ch19 的接口，也失去 Simm 亲口说的「一个小广场上短期内难得发生两件事」这层对照，而那正是本章「相邻」效果的外化来源） |
| L2 | **“Did I beat Matt in?” 的赌注前提与 Coventry 玩笑** | `text/ch21_21.txt:23` — `‘Did I beat Matt in?’`；`:26` — `‘He’s been sent to Harrogate.’`；`:29` — `‘That’s better than being sent to Coventry. Why Harrogate?’` | md 只说「交代马特被派往哈罗盖特」，没有「赌」这件事，也没提 Coventry；块 2 中文理解「艾米问马特被派到哪里」把原话问答压成了 md 自造的问答 | 提示 |
| L3 | **Amy「要看三天的退网购录像」这记笑点** | `text/ch21_21.txt:35` — `‘Are you telling me that I have to watch three days’ worth of footage of people returning online orders?’` | 引语块 3 从 Caius 的句子起，md 5 条引语里没有这句；块 3 中文理解也不提「三天」 | 提示 |
| L4 | **数字「三」被弱化** | `text/ch21_21.txt:32` — `…the days that the last three letters were likely sent or received.` | 块 2 中文理解写「只覆盖末几封信可能寄出或收到的那些日子」，丢掉「三」；仅「关键词」行保留 `last three letters` | 提示 |

---

## 二、编（md 有、原文无）

| # | 事项 | 原文逐字 | md 侧 | 档位 |
|---|---|---|---|---|
| F1 | **「作案人是贝内迪克特·卡尔-里奇」** | 原文 `text/ch21_21.txt:20` 并未说他是作案人：`a report on an attempted burglary that had been made by a certain Benedict Carr-Ridge who lived at 7 Priory Square`；同一段紧接着写他不是作案见证而是**不可靠证人**：`Benedict wasn’t a reliable witness` / `The officer who had interviewed him wasn’t even convinced the incident had happened`；`text/ch31_31.txt:56` — `Benedict’s basement and back doors were wide open when he woke up.`；`text/ch37_37.txt:77` — `‘Caius interviewed Benedict Carr-Ridge, the novelist. He lives at number 7. It was a break-in, although—’` | 块 1 中文理解：`开篇，凯厄斯在办公桌前读一份入室盗窃未遂的报告：作案人是住在普里奥里广场七号的一位贝内迪克特·卡尔-里奇。` | **阻断**（详见错单 D1；md 断言了一个原文与后文都不支持的事实） |
| F2 | **「低声」这层语气是凭空加的** | `text/ch21_21.txt:50` — `‘It could be a coincidence but we are running out of leads fast with this one.’`（当面对话说出） | 导航·视角：`章末落到他对这桩小案的低声怀疑`；导航·人物弧线：`可出门前又低声承认线索快用完了` | 提示 |
| F3 | **「全章靠对话推进」** | `text/ch21_21.txt:20`（整段叙述，交代报告与酒瓶）、`:50` 后半（`Caius grabbed his suit jacket… It made him feel like an adult.`）都是叙述 | 导航·叙事手法：`全章靠对话推进，每轮问答只多出一小点信息` | 提示 |
| F4 | **「一纸空案卷」** | `text/ch21_21.txt:20` 是一份**关于一桩未被证实的报案的报告**（有卷宗、不为空），空的是案的事实 | 一句话总结：`被空酒瓶和一纸空案卷冲淡了可信度的入室盗窃未遂` | 提示 |
| F5 | **「出警的警员」** | `text/ch21_21.txt:20` — `The officer who had interviewed him wasn’t even convinced the incident had happened.`（是**问话/讯问**他的警员） | 一句话概括：`连出警的警员都不信这事真发生过`；块 1 中文理解：`出警的警员甚至不信事情发生过` | 提示 |

---

## 三、错（两边都有但不一致）

### D1（阻断）施事/归属反转：贝内迪克特被写成入室盗窃的**作案人**

- md 逐字（块 1 中文理解，第 21 行）：
  `开篇，凯厄斯在办公桌前读一份入室盗窃未遂的报告：作案人是住在普里奥里广场七号的一位贝内迪克特·卡尔-里奇。`
- 原文逐字（`text/ch21_21.txt:20`，字符区间 41–488）：
  `Caius was at his desk reading over a report on an attempted burglary that had been made by a certain Benedict Carr-Ridge who lived at 7 Priory Square. His name was familiar but Caius wasn’t sure why. It became apparent quite early on in the report that Benedict wasn’t a reliable witness. The officer who had interviewed him wasn’t even convinced the incident had happened. The empty bottles littered about the place hadn’t helped his credibility.`
- 判定依据（三条互相独立的原文）：
  1. 本章自己把贝内迪克特称作 **witness**（`wasn’t a reliable witness`），并说警员**连事发生过都不信**；若他本人作案，「不可靠的证人」与「未遂」两处都无从谈起。
  2. `text/ch19_19.txt:116–128`：Tiny Simm 报的是 `a break-in was reported on Priory Square this morning`，门牌 `‘Seven.’`，`‘Anything taken?’` — `‘No, the guy who reported it was apparently half-cut.’` ⇒ **7 号是报案地点，喝醉的是报案人**。
  3. `text/ch31_31.txt:56`：`Benedict’s basement and back doors were wide open when he woke up.`；`text/ch37_37.txt:77–89`：`‘Caius interviewed Benedict Carr-Ridge, the novelist. He lives at number 7. It was a break-in, although—’` / `‘—no,… and that Benedict was drunk at the time.’` ⇒ 他是 **7 号住户兼被害人**，警方问话对象。
- 内部自相矛盾（md 自证）：md **文件名**是 `ch21 benedict reports a break in`，**一句话概括**写「报案人喝了酒」，**线索结构**写「不可靠的报案人」——三处都说他是报案人，只有块 1 说他是作案人。
- 建议改法：块 1 中文理解改为「报案人是住在普里奥里广场七号的作家贝内迪克特·卡尔-里奇」，并保留「报告几乎一开头就显示他不是可靠证人」。
- 档位：**阻断**

### D2（提示）时序自相矛盾：「穿上这件外套让他觉得自己像个大人」

- md 逐字（块 5 中文理解，第 49 行）：`他从椅背上抓起西装外套，天气太潮，眼下穿不得，等到了普里奥里广场再穿；穿上这件外套让他觉得自己像个大人。`
- 原文逐字（`text/ch21_21.txt:50`）：`‘Apparently not.’ Caius grabbed his suit jacket off the back of his chair. It was too humid to wear it but he would once he got to Priory Square. It made him feel like an adult.`
- 同一句里先说「眼下穿不得」，后说「穿上让他觉得」——原文是**现在**就让他觉得像个大人（`It made him feel like an adult.` 紧接在前句之后），并未说等到穿上才觉得。
- 档位：提示（`It` 的所指（外套／打算穿上）原文本身有歧义，md 取了一种读法但与自己前半句冲突）

### D3（提示）摘要层物理细节：「还没干透的西装外套」

- md 逐字（一句话总结，第 99 行）：`警探穿着还没干透的西装外套出门前说了一句「这也许只是巧合」`
- 原文逐字（`text/ch21_21.txt:50`）：`It was too humid to wear it but he would once he got to Priory Square.`（是**天气太潮**，外套并非湿了未干；且他出门那一刻还没穿上）
- 档位：提示（同章块 5 已写对「天气太潮，眼下穿不得」，仅摘要层走样）

### D4（提示）块 2「为什么这样写」把两桩事说成在同一段对话里

- md 逐字（第 30 行）：`作者偏要让它和旁边那桩广场上的入室盗窃在同一段对话里来回答疑，让读者下意识把「信箱」和「广场」当成可以互换的两样东西。`
- 原文顺序：`text/ch21_21.txt:20` 叙述（入室盗窃，开篇）→ `:23–41` 对话（邮政信箱/监控/人脸程序）→ `:44` 才由 Caius 在对话里说出 `I’m going to go check out a burglary on Priory Square.`
- 即：入室盗窃**不在这段信箱对话里**；「巧合」在原文中指向的是**广场上的入室盗窃与本案**（后文 `text/ch31_31.txt:74` 明确区分 `‘The PO Box connection cannot be a coincidence.’` 与 `‘These two break-ins could be a coincidence.’`），md 换成「信箱 ↔ 广场」这一对。
- 档位：提示（解读方向可讨论，顺序事实不准）

### D5（提示）导航·视角「听汇报」

- md 逐字（第 12 行）：`叙述跟着他在「读报告—听汇报—从椅背上抓外套准备出门」之间移动`
- 原文：汇报 PO Box 进展的是 **Caius**（`:32` `Caius said, rapping his fingers on the desk.`），Amy 是听的一方； Amy 进屋先问的是赌注（`:23`）。
- 档位：提示
