# 4-verdict.md · ch10《Caius cooks korean pancakes》独立审查判定

- 审查对象：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch10 caius cooks korean pancakes.md`
- 权威源：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch10_10.txt`（4594 字符）
- 落盘目录：`.memory/raw-gates/a-fatal-legacy-by-charlotte-vassell/review/ch10/`
- 执行顺序：**R1 素读（只读 text）→ 落盘 `1-suread.json` → R2 机器层 → 开 md → R3/R4/R5**。素读全程未开 md、未看别章 md、未凭记忆。
- R2 命令：`bash scripts/chapter.sh "notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch10 caius cooks korean pancakes" --json > 2-machine.json` → **退出码 0**（无阻断；`quotes` 8 段全部 `ok:true`，`counts.segment_miss=0`；`issues` 四类全空）。
- 附带机器层（同一实现外复核，均退出码 0）：`scripts/check_vocab.py <书目录>` → FAIL 0、ch10 无 WARN；`scripts/corruption_scan.py <书目录>` → FAIL 0（U+FFFD/双句号）；`scripts/bookform.py <书目录>` → 形态众数；`scripts/check_chinese_layer.py <书目录>` → 全书 391 块合格密度 100%、阻断 0；`scripts/block_scope_check.py <书目录>` → ch10 无 PARTIAL。

---

## 一、四组数（只报这四组）

| 组 | 计数 | 结论 |
|---|---|---|
| **逐字** | 引语 **8/8** 片段逐字命中；词汇表 **28/28** 例句在本章原文逐字命中 | **0 处不符**（机器层 `segment_miss=0`；`check_vocab` FAIL 0 且 ch10 无 WARN） |
| **对应** | **6/6** 块成立 | 无引语选短／无不对应／无密度不足（逐块见 `4-correspondence.md`） |
| **形态** | H1 ✓ ／ 导航 5 项 ✓ ／ 子项集 4 项 ✓ ／ 块数 6（在众数区间内） | **0 处阻断级偏离**；1 条形态类提示（未标分部，见下） |
| **断言** | 实查 **10** 条（漏 3／编 5／错 2），另 4 条专项核对 | **阻断 1**、提示 9、假红 0、跳过 0 |

### 形态组明细

- **H1**：`# 10. Caius and Callie’s Flat`——形如 `N. 标题`，与原文小标题 `Caius and Callie’s Flat`（`text/ch10:17`）一致；本书 54 章 H1 全为 `N.` 式（`bookform.py` 输出 `H1 写法：{'N.': 54}`）→ **不偏离**。
- **导航项名与项数**：5 项＝`一句话概括 / 视角 / 线索结构 / 人物弧线 / 叙事手法`，与本书众数（5 项，项名完全相同）**一致**。
- **子项集**：`中文理解 / 关键词 / 为什么这样写 / 读者视角提示`（4 项）＝ genre profile `mystery-thriller` 的子项集 → **不偏离**。
- **块数**：本章 6 块；本书众数 7.0，范围 5–10，profile 允许 3–10 → **6 落在区间内，不偏离**，无需理由行。
- **形态类提示（1 条）**：本章导航未标注所属分部；本书分部按星期命名，本章属「**A SUNDAY IN MAY**」（前序 ch01–ch12 同属该分部，ch11 起才出现 `Caius appeared without his cast.`）。取证：`/usr/bin/grep -rn "分部" notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/*.md` → 命中 26 章（ch13、ch16、ch18、ch21、ch22、ch24–ch31、ch33、ch34、ch36、ch38、ch39、ch42、ch44、ch47、ch49、ch50、ch51、ch53、ch54），ch01–ch12 全组均未标注 → **书内惯例本身两派，ch10 不是个案偏离**，记为提示，不判阻断。

---

## 二、断言判定表

| # | 断言 | 证据（章:区间） | 结论 | 档位 |
|---|---|---|---|---|
| A1 | 导航「人物弧线」称 Caius 从「我不往下说」走到「被人当面读出『你脸上有那个表情』」 | `text/ch10:32`（区间 [522,543]）`'You have that look.'` ／ `text/ch10:65`（区间 [1674,1759]）`'It looks like a man was murdered by his date.' Caius was reluctant to go beyond that.` | **时序倒置**：原文先被读出（:32）、后闭口（:65），md 写成反序；且同句里 Callie 那一半是按原文时序写的，两半标准不一致 → 需改 | **阻断** |
| A2 | 原句 1 分析称「『看过视频就想试』顺手交代了他**不会做饭**」 | `text/ch10:20`（区间 [170,242]）`He'd seen a video of someone doing it the other day and wanted to try it.` ／ `text/ch10:59`（区间 [1361,1480]）`He should've waited to make this tomorrow when his cast would be off and he wouldn't have to hold the pan with one hand.` | 原文只支持「**没做过这道菜**」与「**单手不便也照做**」，未说他不会做饭（厨艺水平原文未交代）→ 措辞越界一格 | 提示 |
| A3 | 原句 2 分析称差别落在「这不是他的本行」 | `text/ch10:44`（区间 [791,920]）`'…it was just your job. It's grim but you got on with it because you're a professional.'` ／ `text/ch10:47`（区间 [924,1045]）`'In some ways gang stuff is easier to deal with, there's a brutal logic to them, but murder is murder and it's always grim.'` | 原文里帮派刺伤案**恰恰是「你的本行 / your job」**，差别在**案型**（毒品/帮派/家暴 ↔ 凶杀）而非「是不是本行」→ 落点写偏 | 提示 |
| A4 | 导航「想赶在 Callie 回来之前把饭做好」 | `text/ch10:20`（区间 [46,168]）`Callie came home to the most delicious smell. She walked into the kitchen area to find Caius frying Korean veggie pancakes.` | 原文无此意图，且事实上她进门时他**还在煎**；原文给的是相反方向（本可等明天却今天动手） | 提示 |
| A5 | 导航/原句 6「三整条**没拆封**的 Lindt 牛奶巧克力」 | `text/ch10:110`（区间 [3081,3136]）`Callie took out three full bars of Lindt milk chocolate.` | `full bars` = 整条；「没拆封」为推断，原文未写 | 提示 |
| A6 | 导航「最后用一个明天的**面试**把话题稳稳接住」 | `text/ch10:143`（区间 [4064,4111]）`'All set for your meeting with Eulalia tomorrow?'` ／ `text/ch10:146`（区间 [4115,4460]）`'Maybe? They didn't really give me much to plan for. I think I've read or listened to every interview she's ever given by now. I'm going to take my portfolio – I worked on a couple of editorial shoots back in the day – and just wing the rest.'` | 原文是 `meeting`＋她带 portfolio 做演示；原文里的 `interview` 指「她听过的采访」；且**话题由 Caius 发起**（Callie 是 `accepted the change of topic`）→ 「面试」误称＋发问/承接方对调 | 提示 |
| A7 | 全章未提及「孩子」这条线 | `text/ch10:68`（区间 [1762,1893]）`'I was worried it was going to be a kid.'` ／ `text/ch10:71`（区间 [1896,2042]）`'No. Not this time.' … 'Thank God. I'm mean, well, you know. Varying degrees.'` | 原文有（Callie 的担心＋Caius 的如释重负），md 导航/六块/词汇表均无 → 漏，但本章主线已被覆盖，不判阻断 | 提示 |
| A8 | 冷热游戏、`Six-year-olds do not get PMT`、`My dad put you up to this?`、`hollowed-out` 四处未被引语块承载 | `text/ch10:95`（区间 [2613,2637]）／ `text/ch10:101`（区间 [2790,2821]）／ `text/ch10:137`（区间 [3831,3879]）／ `text/ch10:140`（区间 [3911,3990]） | 导航与词汇表均已覆盖，不属「md 无」→ 仅记覆盖不均 | 提示 |
| A9 | Callie 的职业身份（milliner）只在词汇表出现，分析层未点明 | `text/ch10:77`（区间 [2202,2284]）`'You're a milliner who's moving on to exciting creative consulting opportunities.'` ／ `text/ch10:80`（区间 [2287,2337]）`'That makes me sound like a LinkedIn wannabe CEO.'` | 原文把「帽匠」与「LinkedIn 冒牌 CEO」两句连在一起构成自我吐槽；md 只收了后者入词汇表 | 提示 |
| A10 | 导航未标所属分部 | 见上文「形态组明细」取证 | 书内两派惯例，ch10 所在组一致 | 提示 |
| V1 | **专项核对①：谁下厨** | `text/ch10:20`（区间 [133,168]）`find Caius frying Korean veggie pancakes` | md 导航/原句 1/一句话总结均写 Caius 下厨 → **正确** | 已核实为正确 |
| V2 | **专项核对②：职业身份**（md 原句 2 称 Caius 为「警察」、Callie 为「警务系统之外的人」） | `text/ch12:191` `'He's a police officer.'` ／ `text/ch02:86` `He ducked under the police tape, nodding to the uniformed officer standing out front.` ／ `text/ch16:181` `Caius formally took a statement from Isolde Burrell at the station` | Caius 是**警察** ✓；`milliner`（帽匠）是 **Callie**（`text/ch10:77`，Caius 对她说话）✓；md **未**把任何人写成「自由撰稿人」✓ | 已核实为正确 |
| V3 | **专项核对③：「像是被约会对象杀的」是谁说的** | `text/ch10:65`（区间 [1674,1759]）`'It looks like a man was murdered by his date.' Caius was reluctant to go beyond that.` | 说话人＝**Caius**；md 原句 4 写「**他**说这案子……」，未误记为 Callie ✓ | 已核实为正确 |
| V4 | 「不会做饭却硬要做」这一专属判据的分量 | `text/ch10:20` + `text/ch10:59` | md 的**原句 3** 已把「明知单手不便仍现在动手」写成全章体贴的底色（对应正确 ✓）；越界只在**原句 1** 的「不会做饭」一词（见 A2） | 提示（已归入 A2） |

### 零命中类断言的自证（R5-补）

```
取证命令：/usr/bin/grep -rn -E "自由撰稿|freelance|自由职业|撰稿人" \
           notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/*.md
         → 命中 1 行（ch40 caius takes his family to frithsden.md:76，`their freelance cook`）；退出码 0
         （该行是 ch40 的钟点工，与 Callie 身份无关；全书 md 无「自由撰稿人」写法）
取证命令：/usr/bin/grep -c -E "You.re a milliner" \
           notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch10_10.txt
         → 命中 1（text/ch10:77）；退出码 0
```

---

## 三、已核实为正确（防误修护栏）

> 以下写法**读着可疑但回原文核对后成立**，后续任何人不得以「读着不对」为由改动，除非能给出反证。

1. **md 原句 2「让一个警务系统之外的人来读警察的状态」——Caius 确是警察。**
   `text/ch12:191`：`'Oh yeah, me included.' Callie remembered the look that Nell gave him on Saturday evening. 'He's a police officer.'`
   `text/ch02:86`：`He ducked under the police tape, nodding to the uniformed officer standing out front.`
   `text/ch16:181`：`Caius formally took a statement from Isolde Burrell at the station`
   ⇒ 不要因为本章只提石膏、绷带、翻锅就把他改成医生/法医。
2. **`milliner`＝Callie（帽匠），不是 Caius。** `text/ch10:77`：`'You're a milliner who's moving on to exciting creative consulting opportunities.'`（Caius 对 Callie 说）。md 词汇表释义「女帽匠」正确、归属未错；**不要**改成自由撰稿人，也不要改挂到 Caius 名下。
3. **「It looks like a man was murdered by his date.」＝Caius 说的。** `text/ch10:65` 紧接 `Caius was reluctant to go beyond that.`；md 原句 4 的「他说」正确，**不要**改成 Callie 说的。
4. **下厨者＝Caius**：`text/ch10:20` `find Caius frying Korean veggie pancakes.`；`text/ch11:20` `Caius appeared without his cast.`（与本章 “Cast off tomorrow” 呼应）。
5. **原句 3 对「明知不便仍上手」的解读成立**：`text/ch10:59` `He should've waited to make this tomorrow when his cast would be off and he wouldn't have to hold the pan with one hand.`——md「他明知单手翻锅不利索，仍旧现在动手」逐字对得上，**不要**因为 A2 就把这一层也削弱。

---

## 四、覆盖声明（抽样范围）

- 本次**人判**范围：**仅 ch10**（R1–R5 全跑）。
- 其余 **53 章只有机器层**（`bookform.py` 形态众数、`check_vocab.py` FAIL 0、`check_chinese_layer.py` 阻断 0、`corruption_scan.py` FAIL 0、`block_scope_check.py` 无 ch10 例外），**未做人判，不得记作「通过」**。
- 未跑：R5 的「第三方复核三步」（`run.sh` 与哈希比对）——本次是单章独立审查，未生成 `run.sh`。

---

## 五、结论

- **四组数**：逐字 **8/8 引语片段 + 28/28 词汇例句，0 不符**；对应 **6/6**；形态 **0 阻断级偏离**（1 条分部标注提示）；断言 **阻断 1、提示 9、假红 0、跳过 0**。
- **阻断型条数：1**（A1 导航「人物弧线」时序倒置）。
- **最要紧的一条**：**A1**——md 把 Caius 的弧线写成「从『我不往下说』走到『被当面读出「你脸上有那个表情」』」，而原文的顺序是先被读出（`text/ch10:32` `'You have that look.'`）、后闭口（`text/ch10:65` `'Caius was reluctant to go beyond that.'`）。同一句里 Callie 的半句（先读他 → 咽回自己的话 → 转回自己 → 用明天的会接住）是按原文时序写的，两半标准不一致，说明这不是刻意的非时序笔法。**改法只需调换 A1 括注里两项的前后次序**（先「你脸上有那个表情」被人读出，再「我不往下说」把话收住），不涉引语、不涉事实。
- 另须提醒修复方注意护栏（第三节 1–5）：**Caius 是警察、milliner 是 Callie、那句「像是被约会对象杀的」是 Caius 说的**——这三处 md 已经写对，**不要**在回改 A1/A2 时顺手「统一」成医生、帽匠或别的职业，也不要把句子归给 Callie。
