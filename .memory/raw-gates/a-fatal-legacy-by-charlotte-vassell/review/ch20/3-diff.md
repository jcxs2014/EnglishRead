# 3-diff · ch20 对账三单（漏 / 编 / 错）

- 审查方：独立审查实例（只审 ch20）
- 权威源：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch20_20.txt`（149 行 / 4594 字节）
- 被审件：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch20 callie agrees to meet eulalia.md`（含同名 symlink）
- 语料核对：`text/ch20_20.txt` 与 epub `OPS/s032-Chapter-020.xhtml` 逐段一致，起止完整（首行 `20`/`125`，末行 `‘There you go,’ … ‘Meet up with her.’`）⇒ **无截断、无并章**
- 分部归属：epub `OPS/s027-Part-005.xhtml` = `TUESDAY`，覆盖 Chapter-016…020 ⇒ ch20 属「TUESDAY」分部（本章为该分部末章）
- 行号即 `text/ch20_20.txt` 行号；引语一律逐字抄（中文引号用 `‘’`，与原文一致）

---

## 一、「漏」单：素读有、md 无

**阻断级漏项：0 条。** 本章 6 个关键动作节点全部在 md 中有落点（十二周规矩 / 提画像 / 转介 Georgie / 降格速写 / 犹豫 / 替她决定）。

以下为**非阻断级取舍未说明**（记「提示」；本章块数 6 落在本书众数区间 5–10 内，属正常取舍，非缺陷）：

| # | 素读到的内容（原文逐字） | md 落点 | 档 |
|---|---|---|---|
| 漏-1 | `‘Mostly it’s a list of names to avoid. People I hated at school, people I’ve arrested, Chelsea players, you know. The worst people in the world.’`（L77）／`‘Yeah. Definitely not baby Max. I quite like the name Charles. It’s solid. You can shorten it to Charlie. No nonsense.’`（L83）／`‘Dated one. He was a nonsense person.’ Callie shook her head. That had been a terrible three weeks in 2011.`（L86） | 只在导航「线索结构」里概括为「给孩子的取名黑名单（讨厌的人、自己逮捕过的人、切尔西那边的人）」；**baby Max / Charles-Charlie / 2011 年那三周** 三个具体锚点未入正文 | 提示 |
| 漏-2 | `‘Want me to come?’`（L41）／`‘Oh no, it’s OK. I think they just do a blood test and weigh you or something.’`（L44） | 未入任何块；md 导航只提「十二周扫描的老话」，未写「他提出陪她去、她拒绝了」这一层 | 提示 |
| 漏-3 | `‘Why did you say ginger like it was the same as having six fingers? Red-headed babies are adorable.’`（L125） | 未入任何块（只在词汇表收了 `recessive`） | 提示 |
| 漏-4 | 白玫瑰的**来处**（Caius 否认是自己送的：`‘No,’ Caius said, slicing the vegetables.` L104；`‘Well, I did accidentally knock you up so it was the very least I could do.’` L110） | 导航「人物弧线」只写「走到客厅里对着白玫瑰评一句‘它们真漂亮’」，未写「他嘴硬否认 → 后来承认」 | 提示 |

---

## 二、「编」单：md 有、原文无

| # | md 逐字 | 原文逐字（不存在） | 判定 | 档 |
|---|---|---|---|---|
| 编-1 | L12 `末尾让丈夫替妻子说一句她本该自己说的话`；L24 `它同时规定了消息何时能公开、这段婚姻何时能被外人知道`；L72 `并不属于这段婚姻的理由`；L74 `才读得懂这段婚姻此刻的状态` | 本章无任何夫妻关系表述。**全书证据（跨章）**：`text/ch27_27.txt:98` `‘I take it that isn’t what it’s like with your boyfriend? He is your boyfriend, you’re not engaged, right?’`；`text/ch27_27.txt:100` `‘I refer to him as my “paramour” and he refers to me as his “missus”. It’s an equal partnership.’` ⇒ 二人**男友/女友关系，未订婚、未婚**，自称 paramour / missus。`/usr/bin/grep -nEi "husband|wife|marri|engage|boyfriend" text/ch20_20.txt` → 仅 1 命中（L38 `community midwife`，非婚姻词），退出码 0 | **关系凭空出现**（md 断言两人是夫妻） | **阻断** |
| 编-2 | L8 `卡莉在床上告诉凯厄斯自己怀孕了` | 本章无「她告知他怀孕」这一事件。原文：`text/ch20_20.txt:23` `‘Anything for you.’ Caius had got in under the covers with her after he’d come home. ‘When can we tell people?’`（他问的是**何时告诉别人**）；`text/ch20_20.txt:110` `‘Well, I did accidentally knock you up so it was the very least I could do.’`（他早知）。**跨章**：怀孕事实更早已成立——`text/ch15_15.txt:198` `‘Please may I have a pregnancy test?’`；`text/ch28_28.txt:41` `‘Callie’s pregnant, it’s too early to say anything but you’re chuffed and have chosen to tell me, Matt Cheung, beloved colleague, cherished friend. …’` | **事件凭空出现**（且与本章「什么时候才能说出口」的主题正好倒置） | **阻断** |
| 编-3 | L32 `提议不是"要不要去见她"，而是"给她画一张什么画"——见面这件事被包装成一件有交付物的作品，于是它看上去是卡莉的创作计划，而不是一次需要理由的社交。` | 本章**从未有人提出去见 Eulalia**：Eulalia 全章仅出现 1 次（`/usr/bin/grep -c "Eulalia" text/ch20_20.txt` → 1，退出码 0），在 L56 作为「要画的肖像对象」出现；紧接着 L59 `‘You should speak to Georgie.’`（转介）、L62 `‘Yes, I thought the same, but I doubt there’s time for a full-blown portrait. …’`（降格为速写）。`/usr/bin/grep -nE "meet|Meet" text/ch20_20.txt` → 仅 1 命中（L149 `‘Meet up with her.’`，**指 Tabitha**），退出码 0 | **前提凭空出现**：把「画像提议」重写成「一次被包装的会面提议」；md 自己的 L8 一句话概括与 L117 一句话总结都未作此说 ⇒ md 内部自相矛盾 | **阻断** |
| 编-4 | 文件名 `ch20 callie agrees to meet eulalia`（含同名 symlink） | 本章无「Callie 同意去见 Eulalia」；结尾的 `‘Meet up with her.’`（L149）指 **Tabitha**。**跨章**：`ch12 callie meets eulalia at tate.md`、`ch27 callie has dinner with eulalia.md` 才是与 Eulalia 相关的两章 | 文件名 slug 描述了本章没有的情节，且与本书 ch12/ch27 的 slug 撞题材 | **阻断** |
| 编-5 | L12 `用一道煎蛋把时间串起来（点菜、下锅、装盘）` | 原文只到下锅：`text/ch20_20.txt:149` `Caius said, whisking the eggs together and adding them to the pan.` ⇒ **无装盘描写** | 细节凭空 | 提示 |
| 编-6 | L12 `白玫瑰与速写本是仅有的两件道具` | 原文另有煎蛋卷、`unicorn` / `mythical animal meat`（L53）、手机与那条消息（L128–135，且是全章收束的载体）⇒ 「仅有的」过绝 | 绝对化 | 提示 |
| 编-7 | L8 `翻着速写本里给欧拉莉亚画像的打算` | 原文是速写本滑到地上、被捡起并问话：`text/ch20_20.txt:53` `Callie’s sketchbook had slid onto the floor. He picked it up. ‘What have you been drawing?’` ⇒ 无「翻」的动作 | 细节凭空 | 提示 |

---

## 三、「错」单：两边都有但不一致

| # | md 逐字 | 原文逐字 | 不一致处 | 档 |
|---|---|---|---|---|
| 错-1 | L42 `全章里凯厄斯处理卡莉的每一个念头都走这条路径——不表态，只换路径。` | 反例一 `text/ch20_20.txt:29` `‘I see.’`（对「什么时候告诉别人」既不表态也**不转介**）；反例二 `text/ch20_20.txt:83` `‘Yeah. Definitely not baby Max. I quite like the name Charles. It’s solid. You can shorten it to Charlie. No nonsense.’`（他**表态**推自己的名字，不是转介）；反例三 `text/ch20_20.txt:143` `‘Go, if you want to,’ Caius said as he cracked an egg into a bowl. ‘You like her, right?’`（**明确表态**）；反例四 `text/ch20_20.txt:149` `‘There you go,’ … ‘Meet up with her.’`（**替她拍板**） | **过宽概括**：「每一个念头…都…只换路径」被本章 4 处反例推翻；且与本 md 自己的原句 6 分析（「决定由他作出」）自相矛盾 | **阻断**（一句话可修：把「每一个念头都」改为「至少在欧拉莉亚这件事上」） |
| 错-2 | L58 `她只给出三个字——"我不确定"。` | `text/ch20_20.txt:140` 末句 `‘I’m not sure.’` | 中文「我不确定」是**四个字**（英文 `I’m not sure` 才是三个词） | 提示 |
| 错-3 | L9 `**视角**：第三人称限知，全程贴着卡莉` | `text/ch20_20.txt:149` `It might not be the worst thing if Callie heard the odd account of Arthur Hampton’s goings-on.` —— 这是 **Caius 的内心**，Callie 并不知道；本 md L72 自己写「叙述在此处插进来点明」 | 「全程贴着卡莉」与章末视角切换冲突 | 提示 |
| 错-4 | 词汇表 `Mercenary \| 唯利是图的；势利的（这里带自嘲）` | `text/ch20_20.txt:146` `‘Yeah, she’s nice. Plus she works in fashion so she may be useful at some point. Mercenary, I know.’` | 例句逐字正确；但释义「势利的」对应的是 snobbish，与 mercenary（唯利是图的／雇佣的）不同义 | 提示 |
| 错-5 | md 全文无「分部」标注 | 本章属 epub `OPS/s027-Part-005.xhtml` = `TUESDAY`（覆盖 ch16–20）；本书 **26/54 章**在导航里写明「分部「A WEDNESDAY IN MAY」」等 | 章内星期/分部信息缺失（书内惯例，未过半，属弱偏离） | 提示（形态组） |

---

## 四、已核对为**正确**（勿误改，防修坏）

| md 逐字 | 原文逐字 | 结论 |
|---|---|---|
| L18 `凯厄斯钻进被窝后问"我们什么时候能告诉别人"` | `text/ch20_20.txt:23` `Caius had got in under the covers with her after he’d come home. ‘When can we tell people?’` | 说话人与动作顺序均对 |
| L28 `凯厄斯从地上捡起掉落的速写本，问她在画什么` | `text/ch20_20.txt:53` `Callie’s sketchbook had slid onto the floor. He picked it up. ‘What have you been drawing?’` | 对 |
| L28 `她是这一章里第一个把欧拉莉亚抬上桌的人` | Eulalia 全章仅 1 次出现（L56），说话人是 Callie | 对 |
| L48 `卡莉说她也想到一块儿去了` | `text/ch20_20.txt:62` `‘Yes, I thought the same, …’` | 对 |
| L72 `它把她上一句「Mercenary, I know」那句自嘲，当成了她已经想通的证据` | L146 → L149 的相邻关系成立 | 对（「上一句」指 L146，正确） |
| L8 `凯厄斯替她拍板：去见她` | L149 `‘Meet up with her.’` | 「她」指**塔比莎**（上一分句主语是「塔比莎的咖啡邀约」）⇒ **正确，勿误改为 Eulalia** |
| L117 `卡莉先说出给欧拉莉亚画像的想法，凯厄斯把它转手给乔治，卡莉又自己把它降成几张速写` | L56 → L59 → L62 | 对 |
| 词汇表 22 条例句（表格 25 行 − 3 行表头） | 全部逐字命中 `text/ch20_20.txt`（自建脚本逐条 `in` 判定，22/22） | 对 |

---

## 五、机器层（自跑，非采信前次）

```
bash scripts/chapter.sh "notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch20 callie agrees to meet eulalia" --json > 2-machine.json
→ 退出码 0；quotes 6/6 ok；segment_miss 0；empty_quote 0；struct_bad 0；keyword_bad 0；cjk_low 0
python3 scripts/check_vocab.py "<书目录>" → FAIL 0，ch20 无 WARN（全书 WARN 26 条均属他章）
python3 scripts/verify_corpus.py "<书目录>" → PASS（FAIL 0 / WARN 3，WARN 与 ch20 无关）
python3 scripts/bookform.py "<书目录>" → H1 众数 {'N.': 54}；导航众数 5 项；子项众数 4 项；块数中位 7、范围 5–10
```

自建脚本另验（词汇条数：本书中位 27.5、范围 21–30，ch20＝22，在范围内）：6 个引语块**全部为原文连续子串**（无 `…` 缝合、无跨话轮拼接），区间 `[274,383) L26` / `[1137,1285) L56` / `[1288,1318) L59` / `[1321,1488) L62` / `[3711,3938) L140` / `[4136,4333) L149`。
