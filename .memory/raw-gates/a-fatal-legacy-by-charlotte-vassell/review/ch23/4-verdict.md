# 4-verdict.md · ch23《Eulalia's House》独立审查判定

> 审查方：独立审查员（本会话，非写作方）
> 语料（唯一权威源）：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch23_23.txt`（14267 字符 / 465 行）
> 被审 md：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch23 eulalia watches the footage again.md`
> 落盘目录：`.memory/raw-gates/a-fatal-legacy-by-charlotte-vassell/review/ch23/`（本文件、`1-suread.json`、`2-machine.json`、`3-diff.md`、`4-correspondence.md`）
> **纪律声明**：先素读（只读 `text/ch23_23.txt`，落盘 `1-suread.json`）→ 后开 md；R2 机器层自跑；**未改书目录任何 md，未 git add/commit**。

---

## 一、四组数（只报这四组）

| 组 | 口径 | 结果 |
|---|---|---|
| **逐字** | 9 块 / 10 段引语按 `…` 拆段独立取证 + 词汇表 28 条例句逐条比对原文 | 引语 **10/10 逐字命中**（`2-machine.json` → `counts.segment_miss=0`；block 3 的两段同在 `text/ch23_23.txt:151`，其中的 `…` 是作者自留省略号，非拼接）；词汇例句 **27/28 严格逐字**，1 条为截断引文（E6，提示）⇒ **逐字组 1 条（提示）** |
| **对应** | 9 块逐块回答「这段中文是不是在讲这句引语」 | **8 块对应成立**（含 2 块因别的问题落缺陷，非对应问题）；**1 块引语选短**（block 8，分析覆盖 `:404`、`:431-434`，超出引语 `:398`）⇒ **对应组 1 条（提示）**；「不对应（全书主旨/作者生平）」0 块；「密度不足」0 块 |
| **形态** | H1 / 导航项名与项数 / 子项集 / 块数 vs 本书众数与 profile | **0 条偏离**（详见下表） |
| **断言** | 漏 / 编 / 错三类事实断言 | **共 10 条**：漏 3、编 0、错 7 ⇒ **阻断 2 条、提示 8 条** |

### 形态组细目

| 维度 | 本章 | 本书众数 / profile | 偏离 |
|---|---|---|---|
| H1 | `# 23. Eulalia’s House` | 全书 `# NN. 标题`（如 `# 54. The Whittington Hospital`），`h1_shape_ok=true` | 无 |
| 导航项名与项数 | `## 本章导航`，5 项（一句话概括／视角／线索结构／人物弧线／叙事手法） | 全书一致 5 项（`2-machine.json` → `form.nav_counts=[5]`、`nav_count_ok=true`） | 无 |
| 子项集 | 中文理解／关键词／为什么这样写／读者视角提示 | profile `mystery-thriller` 同 4 项（可选「句子结构」未用） | 无 |
| 块数 | **9 块** | 本书众数 **7**（`form.block_median=7.0`），区间 5–10；本次 grep 实测全书 54 章块数落在 6–10，其中 9 块者 7 章、10 块者 8 章 | **无偏离**（在区间内、高于中位数 2） |

> **块数高于众数的一行理由**：本章是长章，三条线并行（录像线／地下室谈判线／午餐线），需要 9 个引语块才能同时承载录像里的花语与「外头挺难」、公司的安排、以及妹妹与姐姐之间的钱与饭；若压回 7 块，必弃其中一条线。

---

## 二、判定表（断言 | 证据 | 结论 | 档位）

| # | 断言 | 证据（章:区间） | 结论 | 档位 |
|---|---|---|---|---|
| E1 | 「全章结束时她仍然在看同一段录像」／「她此刻全部心思还留在屏幕上那段录像里」 | md block 1「读者视角提示」、block 9「为什么这样写」／原文 `text/ch23_23.txt:410` `‘I’m not obsessed, see.’ Eulalia closed the tab. ‘I’m going to read instead.’`；`text/ch23_23.txt:443` `‘Let’s just have quality us time.’ Mel looked at her sister picking over her lunch, reading some brain rot story on her laptop.` | **与原文相反**。录像在午餐前已被她主动关掉，午餐时她在看别的；本章专属判据「刻意隐瞒」被写反（原文＝隐瞒，md＝不隐瞒） | **阻断** |
| E2 | block 5「梅尔应了一声『好』」「梅尔……只回了一个『好』」 | md block 5「中文理解」「为什么这样写」／原文 `text/ch23_23.txt:298`（梅尔自己说 NDA 与合同）→ `text/ch23_23.txt:301` `‘Good.’ Eulalia looked up at her sister and started pacing.`→ `text/ch23_23.txt:304` `‘Are you OK? You seem a bit manic.’`；同型行文体例 `:289` `:295` `:410` | **`‘Good.’` 是欧拉莉亚说的**：紧邻前句属梅尔（不能回应自己），行文体例「引语在前、随后的动作属同一说话人」三处一致，话轮上 `:304` 才是梅尔的回应。md 的说话人判错，且 why 段结论建立其上 | **阻断** |
| L1 | 漏：欧拉莉亚「关掉标签页」这个动作（隐瞒的物证）md 全篇没有 | 原文 `text/ch23_23.txt:410` 同上 | 漏，且与 E1 同源；**并入 E1 一并修**（补写「关掉标签页」这一动作即可同时消掉漏与错） | **阻断**（并入 E1） |
| E3 | 导航「人物弧线」把「让卡莉到家里吃饭」写成既成事实 | md 导航／原文 `text/ch23_23.txt:446`（提议）、`:449`（`‘Here?’ Mel wasn’t keen on having her in the house.`）、`:452` `‘I thought we could go out?’`、`:455` `‘Sure.’` | 提议属实，落点不同：**最终改为外出吃**；且梅尔本不愿她进家，与「依赖挪到地盘上」的方向相反 | 提示 |
| E4 | block 4「为什么这样写」的「一个同行者平平常常的一句实话」 | md block 4「为什么这样写」vs 同块「读者视角提示」（「这句是对同行者说的」＝受话者 Monty Don）／原文 `text/ch23_23.txt:279` `Callie:`、`:281` `I don’t know, Monty. It’s rough out there.` | 同块两处对「同行者」指代不一致，why 段可被读成「主持人说的实话」；说话人应是卡莉（本块「中文理解」已写对） | 提示 |
| E5 | block 8 把 `:404` 的身世（金雀花／非婚生继承）并入本块引语；并以「眼前这位卡莉的男朋友」指认身份 | md block 8「为什么这样写」／原文 `text/ch23_23.txt:398`（引语所在行）、`:404`（身世所在行）、`:151`（`my stupid ex`）、`:68`（`The new man!`） | ① 分析覆盖原文长于引语 ⇒ **引语选短**（与 R4 判定一致）；② 原文从未点名 boyfriend 是谁，md 的「眼前这位」暗示无据 | 提示 |
| E6 | 词汇表 `lasagne` 例句 `‘Can’t I have lasagne? Or cottage pie?’` | md 本章词汇·⭐ 基础／原文 `text/ch23_23.txt:416` `… Can’t I have lasagne? Or cottage pie? A cheeseburger? What about a roast? Let’s have a roast on Sunday! …` | 例句为更长台词的中段截断，却以起止引号写成完整句；应加省略号或改取完整句 | 提示 |
| E7 | 导航「叙事手法」的「妹妹的病」 | md 导航／原文 `text/ch23_23.txt:331` `… not a sweet girl who possibly had a personality disorder …`（Sonikk 的**揣测**）、`:346`（梅尔盯药与精神科复核剂量） | 原文无人下诊断；「妹妹的病」写成既成事实超出原文 | 提示 |
| L2 | 漏：录像里 Callie 自己那句 `You know, right now I rather wish it was.` | 原文 `text/ch23_23.txt:125`（紧接 `:112` `Chivalry isn’t dead.`） | md 只留 `Chivalry isn’t dead`，抹掉了录像自身的反讽底色；提示级 | 提示 |
| L3 | 漏：地下室「梅尔开口唱」这一落点 | 原文 `text/ch23_23.txt:373` `Sonikk played the track and Mel began to sing.`、`:376` `…listening back to Mel nailing the vocals in one perfectly haunting take.`、`'We’re all going to be so rich'`；`:316`「PR 女友」一段 | md 仅在导航以「谁在唱歌」一点，未落为事实。本书 ch42（`mel is the voice and eulalia is the face`）正式展开该秘密，故本章不判阻断 | 提示 |
| — | 编（凭空情节/关系/数字） | 引语 10/10 逐字命中；例句 27/28 逐字；md 中全部数字/日期（an hour and a half / two / 100 per cent / five years / a thousand ships / M42 two junctions / ten minutes ago / Sunday / for a week / one perfectly haunting take）均见原文 `:322 :331 :355 :358 :358 :386 :416 :340 :376` | **本栏 0 条** | — |

### 「零命中」类断言的自证（R5-补）

E5 中「原文从未点名 boyfriend 是谁」一条属「查无」型断言，取证如下：

```
$ cd notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell
$ /usr/bin/grep -n "boyfriend" text/ch23_23.txt > /tmp/o1 2>&1; echo "EXIT=$?"
EXIT=0
398:‘I’m not obsessed. I just think she’s terribly romantic. Her boyfriend will be a knight one day. An actual knight. His family have a big house in the country.’

$ /usr/bin/grep -nE "\bMax\b|\bCaius\b|lover" text/ch23_23.txt > /tmp/o2 2>&1; echo "EXIT=$?"
EXIT=0
37:…signal to her lover that she never wants to see him again by wearing a Michaelmas daisy…
40:[Monty Don spots Max jumping over the rope around the show garden…]
71:[Max wobbles as he raises his fists as he marches across the shot to Caius…]
106:[Max swings at Caius who easily dodges it and in turn catches him…]
```

⇒ `boyfriend` 全章仅 `:398` 一次且不带名字；录像里出现过的男性只有 Max（被 Callie 于 `:151` 称作 `my stupid ex`）与 Caius（`:68` 被 Max 喊 `The new man!`）。故「眼前这位卡莉的男朋友」的身份在原文无据。

---

## 三、已核实为正确（防误修，固定一节）

以下写法**看着像错、回原文核对后成立**，后续任何人不得以「读着不对」为由改动：

1. **md block 5 把 `:295` `‘I like her vibe.’` 归给欧拉莉亚** —— 正确（`text/ch23_23.txt:295` `‘I like her vibe.’ Eulalia jumped up in defence of Callie’s honour.`）；错的只是 `:301` 那句 `‘Good.’`（见 E2）。
2. **md block 6 把 `a slim volume` 译作「薄薄的诗集」** —— 正确，原文另有 `text/ch23_23.txt:322` `she left with a volume of poetry` 印证。
3. **词汇表 `isolated` 例句 `She seemed so isolated when he saw her.`** —— 与 `text/ch23_23.txt:349` 逐字一致（不是 `him`），不必改。
4. **md block 3 的 `…` 不是拼接** —— 两段同在 `text/ch23_23.txt:151` 一段之内，`…` 是作者自己的省略号，逐片段独立取证各自成立（`2-machine.json` → `segments[2].ok/segments[3].ok=true`）。
5. **md block 2 tip「『永不想再见到他』既是花语的意思，也是那位被求婚者的原话」** —— 正确：花语在 `text/ch23_23.txt:37`，Callie 的原话在 `:55` `I don’t ever want to see you again.`。
6. **md 词汇表 `Melusine` 例句保留原文的 `…`** —— 与 `text/ch23_23.txt:404` 一致（原文 `… I think she’s half snake or something …`），不必改成实心省略号。
7. **md 导航「父母只关心账户里的钱」** —— 正确（`text/ch23_23.txt:370` `They don’t care as long as they get cash in their bank account every month.`）。

---

## 四、覆盖声明与本次未查的部分

- **本次只审第 23 章**：R1 素读、R2 机器层、R3 三张单子、R4 逐块对应、R5 判定全部针对 `ch23`。
- **其余 53 章未做 R1–R4 人判**，本次仅为形态组做了一次全书的块数/H1 机械统计（`grep` 块数）。**不得据此写成「其余各章通过」**——它们连机器层本次都未逐章跑，只在本章的 `chapter.sh` 内部与本书众数做过比对。
- 导航「一句话概括」「一句话总结」两处汇总层与本章引语的一致性已随块级检查一并核对；**全书总览三篇（`00_*.md`）本次未查**（不在本章委托范围）。

## 五、第三方复核（可重跑）

```bash
cd /Users/jcxs2014/Documents/Works/EnglishRead
# 0) 本次 2-machine.json 的 sha256（第三方比对用）
#    0216962cbdf733996a1286ae4abda533b4cfb282d5e4cc663359f1dd55414082
# 1) 机器层（应复现 2-machine.json 的结论：segment_miss=0 / struct_bad=0 / blocks=9 / h1="23. Eulalia’s House"）
bash scripts/chapter.sh "notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch23 eulalia watches the footage again" --json \
  > /tmp/ch23-machine.json 2>&1; echo "EXIT=$?"
# 2) 逐字与例句（本次已跑：引语 10/10；例句 27/28，lasagne 一条为截断）
# 3) 抽 3 行回原文核（建议抽：E1 / E2 / E5）
/usr/bin/grep -n "closed the tab\|brain rot" notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch23_23.txt
/usr/bin/grep -n "^‘Good.’" notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch23_23.txt
/usr/bin/grep -n "boyfriend" notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch23_23.txt
```


---

## 书级例句全串核验（2026-10-21，主会话收口补记）

- 本章词表有 **1 条**例句未通过「全串逐字」核验（`check_vocab` 只取前 60 字符指纹，故判绿）：
  - `lasagne`：原文该对白仍在延续，md 补了凭空的开引号与收尾引号
- 处置：去掉凭空的开引号与收尾引号
- 详见 `.memory/raw-gates/a-fatal-legacy-by-charlotte-vassell/vocab-full-string-audit.md`（书级审计记录与探针说明）。
