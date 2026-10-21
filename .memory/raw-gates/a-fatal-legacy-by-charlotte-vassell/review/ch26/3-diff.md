# 3-diff.md · ch26 对账（漏 / 编 / 错）

> 审查员：独立审查（先素读 `text/ch26_26.txt` → 落盘 `1-suread.json` → 再开 md）
> 唯一权威源：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch26_26.txt`（2331 字符 / 78 行 / 19 段）
> 副证源：`library/A Fatal Legacy (Charlotte Vassell) (z-library.sk, 1lib.sk, z-lib.sk).epub`（= text/ 的抽取母本，用于核对分部标题与段落结构）
> md：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch26 matt returns from harrogate.md`

## 0. 语料层先行核对（不算入三张单子）

| 项 | 命令 / 做法 | 结果 |
|---|---|---|
| epub 第 26 章段落 vs `text/ch26_26.txt` | 解包 epub → `OPS/s039-Chapter-026.xhtml` 取 19 个 `<p>`，与 text/ 逐段比对 | **19/19 段完全一致**（起句 "‘These are fat rascals,’…" 至 段19 "…It’s going to be a long night.’"）⇒ ch26 抽取边界完整，无并篇、无截断 |
| ch26 归属分部 | `OPS/toc.ncx` navPoint | 第 26 章（`s039-Chapter-026.xhtml`）落在 `s033-Part-006.xhtml` 之后、`s041-Part-007.xhtml` 之前 ⇒ 属 **Part-006** |
| Part-006 标题（逐字） | `OPS/s033-Part-006.xhtml` 正文去标签 | `WEDNESDAY 129 WEDNESDAY 130` ⇒ 分部名 = **"WEDNESDAY"**（页码 129/130） |
| 对照：Part-001 标题（逐字） | `OPS/s008-Part-001.xhtml` 正文去标签 | `A FRIDAY IN MAY 3 A FRIDAY IN MAY 4` ⇒ **"A FRIDAY IN MAY" 是 Part-001**（第 1–2 章），与第 26 章无关 |
| 全书分部序列（逐字） | `OPS/toc.ncx` | A FRIDAY IN MAY / SATURDAY / SUNDAY / MONDAY / TUESDAY / **WEDNESDAY** / THURSDAY / FRIDAY / SATURDAY / MONDAY / TUESDAY / SIX WEEKS LATER |

机器层（R2，退出码 0，verdict=ok）：引语 5 条全部 `ok:true`（pos 25 / 818 / 1297 / 1680 / 1799，全在 2331 字符内）��块 5、片段 5、`segment_miss 0`、`struct_bad 0`、`empty_quote 0`、`keyword_bad 0`、`cjk_low 0`。
独立实现补跑：`verify_fragments_indep.py`（全书 776 引语 / 844 受检片段，MISS 0、拼接未标省略号 0）、`check_vocab.py`（FAIL 0）、`corruption_scan.py`（FAIL 0）、`verify_corpus.py`（PASS，3 条 WARN 与本章无关）。

---

## 1. 漏（素读有、md 无）

### L1 · 漏 ·「被引答语所应答的两个提问」在分析层缺席 —— 提示
- **原文（逐字）**：`text/ch26_26.txt:66` `‘Do you think they’re a spree killer?’ Matt asked.`
  （chars 1336–1386）／`text/ch26_26.txt:72` `‘Why did he help? Do you think he knew he was an accomplice?’ Amy asked.`
  （chars 1709–1781）
- **md 侧**：
  - 块 3「中文理解」写「**Caius 先答「不」**」——所答的「连杀」提问（spree killer）只以例句形式出现在「本章词汇」表（`spree killer` 条），分析层与导航层均未出现；
  - 块 4「中文理解」写「**Matt 盯着白板说：「我怀疑他知道。」**」——所答的「accomplice」提问（chars 1709–1781）**全篇未出现**（不在 5 个引语块、导航 5 项、词汇表任何一处）。
- **判据**：块 3、块 4 的「中文理解」都以「答」字开头，但被答的问句缺席，读者在 md 内部无从还原「不」和「I doubt it」到底在答什么（块 4 的歧义见 W1）。
- **档位**：提示（只记不改）。理由：md 用「先答『不』」「我怀疑他知道」间接指涉了问句内容，且块 3 的「为什么这样写」完整覆盖了推理链；按「关键事件/转折未出现才阻断」的判据，不构成阻断。

### L2 · 漏 ·「Yumi（Matt 想带谁去）」与「Caius 在约克读过书」两条具体事实未进分析层 —— 提示
- **原文（逐字）**：`text/ch26_26.txt:29` `‘Delightful. Might take Yumi for a break in the summer. The climate was different, cooler, and yet I definitely saw a lot more men in shorts than down here.’`（chars 394–551）
  ／`text/ch26_26.txt:32` `‘I love Yorkshire. I went to uni up there.’ Caius took one of his fat rascal’s eyes and popped it in his mouth. ‘The tea’s shit though.’`（chars 554–690）
- **md 侧**：`/usr/bin/grep -n 'Yumi' "ch26 matt returns from harrogate.md"` → **命中 2 行（md:85、md:86），且两行都只是「本章词汇」表里 `definitely` / `different` 两条的例句**；导航 5 项与 5 个引语块中零出现（分析层从未点出「Yumi」是谁、Matt 要带谁去）。
  `/usr/bin/grep -c 'went to uni' "ch26 matt returns from harrogate.md"` → **命中 0**（Caius 在约克读过书这一具体出身，md 全文零出现）；导航只以「几句关于约克郡的玩笑」「互嘲地域的寒暄」概括。
- **判据**：两条都是有名有姓/有具体出身的事实（Yumi 是 Matt 的伴侣；Caius 读过约克的大学），构成读者的可查证锚点。
- **档位**：提示（寒暄段本身属可压缩区，且 md 的导航已声明本章「用一整段吃司康、喝茶、互嘲地域的寒暄垫底」）。

### L3 · 漏 ·「The tea’s shit though」在分析与词汇表两处均无 —— 提示
- **原文（逐字）**：`text/ch26_26.txt:32` 尾句 `‘The tea’s shit though.’`（chars 554–690 内）
- **md 侧**：块 1–5 的任何一段、词汇表 28 行均未出现该句（`treason against God’s own country` 只在词汇表 `tantamount` 例句里，`The tea’s shit` 完全缺席；`/usr/bin/grep -c "tea’s shit"` → 0）。
- **档位**：提示（骂茶这句与 `treason` 一句配对，构成「北方 vs 南方」的地域笑点主干；缺了它，导航「互嘲地域」就只剩蔡斯单方面的南方笑话）。

---

## 2. 编（md 有、原文无）

### C1 · 编 · 导航把本章归入「五月的星期三」分部 —— **阻断**
- **md 侧（逐字）**：`ch26 matt returns from harrogate.md:12`「……本章属「**五月的星期三**」这一分部。」
- **原文侧（逐字）**：epub 目录 `OPS/toc.ncx` → `<text>WEDNESDAY</text>` 对应 `src="s033-Part-006.xhtml"`；分部页 `OPS/s033-Part-006.xhtml` 正文去标签后逐字为 `WEDNESDAY 129 WEDNESDAY 130`。
  「A FRIDAY IN MAY」逐字出现在 `OPS/s008-Part-001.xhtml`（`A FRIDAY IN MAY 3 A FRIDAY IN MAY 4`），是 **Part-001**，覆盖第 1–2 章。
- **判据**：md 给出的分部名在书结构里并不存在；第 26 章所在的分部标题只有「WEDNESDAY」三个词，没有「IN MAY」。「IN MAY」来自 Part-001，被安到了第 26 章头上。
- **档位**：阻断（编造的书结构事实；本次审查任务书给定的「分部 A WEDNESDAY IN MAY」即源自 md 这句，不是书里的事实）。
- **取证命令**：
  ```
  unzip -q "notes/books/.../library/A Fatal Legacy (Charlotte Vassell) (...).epub" -d /tmp/afl_epub
  /usr/bin/grep -rn 'WEDNESDAY' /tmp/afl_epub/OPS/s033-Part-006.xhtml /tmp/afl_epub/OPS/toc.ncx
  ```
  → 命中 `s033-Part-006.xhtml` 与 `toc.ncx`（`WEDNESDAY`）；`s008-Part-001.xhtml` 命中 `A FRIDAY IN MAY`；退出码 0。

### C2 · 编（轻度）· 导航把「荤笑话」明确归给 Amy —— 提示
- **md 侧（逐字）**：`ch26 matt returns from harrogate.md:14`「……**Amy** 一边用 Tumblr、Etsy、meme 调侃，一边**用一句荤笑话把正经推测拽回地面**。」
- **原文侧（逐字）**：`text/ch26_26.txt:78`（chars 1909–2330）
  `‘Also known as her knickers.’ Caius’s desk phone rang. ‘All right. Thank you.’ He put the receiver down. ‘Uniform have collected his new starter forms from the bakery. …’`
  —— 原文**没有给这句话任何说话人标注**；块 5 的「中文理解」自己也只写「**有人**接上一句荤笑话」。
- **判据**：原文唯一可依的结构线索指向 Caius：整段是「Caius 的一句 → Caius 的座机响 → Caius 接电话（He put the receiver down）→ Caius 派活」，且全书有同型范式可对照 `text/ch38`（epub `s053-Chapter-038.xhtml`）`‘Yikes.’ Caius’s phone rang. He took the call, …`（同样是「无标注的一句 + 该角色本人的电话/动作」）。反向读法（Amy 插话）也讲得通，**原文不能一锤定音**。
- **档位**：提示（只记不改）。理由：md 在块级写「有人」是稳妥的、不构成错误；只有导航里那句平铺直叙的「Amy」缺原文支撑。建议改成不指名或按段落结构改指 Caius——但**原文没有排他证据，不判阻断**。

### C3 · 编（轻度）· 块 5 把「母亲联系方式」说成印在入职表上 —— 提示
- **md 侧（逐字）**：`ch26 matt returns from harrogate.md:44`「制服同事已经从那家面包店取走了斯科特的新员工入职表，**上面有他给的母亲联系方式**，这事他来处理」
- **原文侧（逐字）**：`text/ch26_26.txt:78`（chars 1909–2330）`Uniform have collected his new starter forms from the bakery. **We’ve got contact details for his mum that he gave to them.** I’ll deal with that.`
- **判据**：原文分两句说：① 表单已从面包房取回；② 我们有他给 uniform 的母亲的联系方式。原文**没说联系方式印在表单上**（虽高度可能）。md 用「上面有」把它合并成一条因果链。
- **档位**：提示。

### C4 · 编（轻度）· 块 2 把「白板是警局固定动作」写成通则 —— 提示
- **md 侧（逐字）**：`ch26 matt returns from harrogate.md:28`「白板是这间警局处理命案的**固定动作**：新案子来了，先开一块板，**再往板上写人物与关系**。」
- **原文侧（逐字）**：`text/ch26_26.txt:48`（chars 877–1000）`Matt looked up at the new whiteboard that had appeared for Scott Brown’s murder.`
- **判据**：本章原文只提供了「为 Scott Brown 的命案新出现了一块白板」这一件事；「固定动作」「写人物与关系」是本章之外的通则（本书 ch09 即 `money or sex on the whiteboard`），属推演而非本章证据。
- **档位**：提示（精读体裁允许此类推演，但应标明是通则推演，不宜与本章事实混写）。

---

## 3. 错（两边都有但不一致）

### W1 · 错 · **否定域反转**：块 4 把「I doubt it」译成「我怀疑他知道」 —— **阻断**
- **原文（逐字）**：`text/ch26_26.txt:75`（chars 1784–1906）
  `‘**I doubt it**,’ Matt said, staring at the board. ‘It was transactional. He was taking the letters to get in her good books.’`
  （it = Amy 上一问 `‘Why did he help? Do you think he knew he was an accomplice?’`，chars 1709–1781 ⇒ 原文语义是「**我不认为他知道（自己是同谋）**」）
- **md 侧（逐字）**：`ch26 matt returns from harrogate.md:38`「Matt 盯着白板说：「**我怀疑他知道**。」接着他把事情定性为一场交易——他替对方拿那些信，是为了在对方那里讨个好。」
- **判据**：「我怀疑他知道」在中文里的常规读法是「我怀疑（他）知道」＝ *I suspect he knows*，与原文 *I doubt it*（*I doubt that he knew*）**极性相反**。md 自己的同一块也不自洽：「为什么这样写」写「拿信**不是**因为知情或忠诚」＝ Scott **不知道**，与同一块给出的引语译文相反；「关键词」栏又照抄了 `transactional / the letters / her good books`，未把否定项带出来。
- **档位**：阻断（否定域反转；块级「中文理解」是对引语的直译，转述给读者的是相反的判断）。
- **修法建议**（不代改）：把该句译成「我不认为他知道」（或「我怀疑他知道——不是这样」），并补回 Amy 的提问（L1）。

### W2 · 错（轻度）· 块 3 把「Once we’d found him」的 him 换成了「影像」 —— 提示
- **原文（逐字）**：`text/ch26_26.txt:69`（chars 1389–1706）`… we would find the footage of Scott at the Post Office. **Once we’d found him**, Scott could easily identify them.`
- **md 侧（逐字）**：`ch26 matt returns from harrogate.md:32`「……任何有点脑子的人都会想到他们能在邮局找到拍到斯科特的影像——**影像一旦找到**，斯科特就能把他们指认出来。」
- **判据**：原文的 him 指 **斯科特本人**（警方顺藤找到他），触发条件是「找到斯科特」；md 写成「影像一旦找到」。两句主语不同（他 vs 影像）。链条结果不变，但触发点被换掉了。
- **档位**：提示（同块「为什么这样写」写的是「他被杀……是因为他会开口指认」，方向正确，故不判阻断）。

### W3 · 错（轻度）· 一句话总结把「警方会找到他」压成「他会被影像认出来」 —— 提示
- **原文（逐字）**：`text/ch26_26.txt:69`（chars 1389–1706）`Scott was killed because, well because anyone with half a brain would realise that we would find the footage of Scott at the Post Office. Once we’d found him, Scott could easily identify them.`
- **md 侧（逐字）**：`ch26 matt returns from harrogate.md:96`「……斯科特这起则是灭口——**他会被邮局拍到的影像认出来**，也能开口指认对方……」
- **判据**：原文的因果是「警方会找到那段拍到斯科特的影像 → 于是找到斯科特 → 斯科特能指认凶手 ⇒ 他必须死」；md 的总结把施事与被事压成「他被影像认出来」，漏掉了「警方顺藤找到他」这一环，也把「会开口指认」与「被认出来」并列为两条风险。
- **档位**：提示（同段其余部分（两桩命案两种逻辑、三路分工、「漫长的夜晚」）逐字对得上）。

---

### L4 · 漏 · 寒暄段与接话段共 4 句未进入 md（分析层与词汇表皆无）—— 提示
| 原文（逐字，text/ch26_26.txt） | chars | md 侧 |
|---|---|---|
| `‘They’re so cute,’ Amy said, picking one up and taking a bite out of its big, fat head.` | 157–244 | 未引未提（Amy 咬司康这一动作不在 md） |
| `‘I can see the Daily Mail headlines now,’ Caius said.` | 1003–1056 | 未引未提 |
| `‘Is that still going on?’` | 1256–1281 | 未引未提（meme 线程只有 P13 进了词表） |
| `‘Thank God.’` | 1321–1333 | 未引未提 |

- **判据**：四句都属对白接话/寒暄，不推进案情。md 的导航已声明「用一整段吃司康、喝茶、互嘲地域的寒暄垫底」，等于声明了取舍。
- **档位**：提示。

### L5 · 漏（与 W1 联动）· Amy 的「accomplice」提问全篇零出现 —— 提示（因 W1 而升级关注）
- **原文（逐字）**：`text/ch26_26.txt:72`（chars 1709–1781）`‘Why did he help? Do you think he knew he was an accomplice?’ Amy asked.`
- **md 侧**：`grep -c` 于 md 全文（导航 5 项 + 5 块 + 词表 28 行 + 总结）——`accomplice` 命中 0 次；「同谋」命中 0 次。
- **判据**：这是本章推理的枢轴（Amy 提出「Scott 知情参与」的假设 → Matt 否定 → 交易论）。块 4 的「中文理解」「我怀疑他知道」正是在回答它，却既没引问句、又译反了否定方向（见 W1）。
- **档位**：提示（与 W1 合并处理即可）。

---

## 4. 引语覆盖对照表（源 19 段 → md）

| # | 源段（epub `<p>` 序 = text/ 行序） | chars | 被引为 md 引语块？ |
|---|---|---|---|
| P1 | `‘These are fat rascals,’ Matt said, opening the box of scones he’d quickly purchased on his way out of Harrogate.` | 41–154 | **块 1** |
| P2 | `‘They’re so cute,’ Amy said, picking one up and taking a bite out of its big, fat head.` | 157–244 | —（L4） |
| P3 | `‘How was Harrogate?’ Caius asked. He placed a cup of tea in front of Matt and Amy each…` | 247–391 | —（词表 `tea` 例句引用） |
| P4 | `‘Delightful. Might take Yumi for a break in the summer…` | 394–551 | —（词表 `definitely`/`different` 例句；L2） |
| P5 | `‘I love Yorkshire. I went to uni up there.’ … ‘The tea’s shit though.’` | 554–690 | —（L2/L3） |
| P6 | `‘That’s tantamount to treason against God’s own country,’ Matt said.` | 693–761 | —（词表 `tantamount` 例句） |
| P7 | `‘They’ll never know I said it. Neither of you southern Jessies would dare rat me out,’ Caius said.` | 764–862 | —（词表 `southern`/`southern Jessies`/`rat me out` 例句） |
| P8 | `* * *` | 867–872 | 导航「用一个星号分隔线骤然切回案情」✓ |
| P9 | `Matt looked up at the new whiteboard that had appeared for Scott Brown’s murder. ‘So she’s what, some sort of black widow?’` | 877–1000 | **块 2** |
| P10 | `‘I can see the Daily Mail headlines now,’ Caius said.` | 1003–1056 | —（L4） |
| P11 | `‘And all the girly edgelords on Tumblr will lose it,’ Amy said…` | 1059–1253 | —（词表 `edgelords`/`merch` 例句；导航提到 Tumblr/Etsy/meme ✓） |
| P12 | `‘Is that still going on?’` | 1256–1281 | —（L4） |
| P13 | `‘No, you were a flash in the pan.’` | 1284–1318 | —（词表 `flash in the pan` 例句） |
| P14 | `‘Thank God.’` | 1321–1333 | —（L4） |
| P15 | `‘Do you think they’re a spree killer?’ Matt asked.` | 1336–1386 | —（词表 `spree killer` 例句；L1） |
| P16 | `‘No,’ Caius said, although he hesitated. ‘Digby’s murder…identify them.’` | 1389–1706 | **块 3** |
| P17 | `‘Why did he help? Do you think he knew he was an accomplice?’ Amy asked.` | 1709–1781 | —（L5） |
| P18 | `‘I doubt it,’ Matt said, staring at the board. ‘It was transactional…’` | 1784–1906 | **块 4** |
| P19 | `‘Also known as her knickers.’ Caius’s desk phone rang… ‘It’s going to be a long night.’` | 1909–2330 | **块 5** |

⇒ **被引为引语块 = P1 / P9 / P16 / P18 / P19（5 段）**；P3–P7、P11、P13、P15 由词汇表例句逐字引用；仅 P2、P10、P12、P14、P17 五句在 md 中零出现（L4/L5）。
**案情主干（白板→黑寡妇猜想→两案两逻辑→交易论→三路分工）五块全覆盖，无主线遗漏。**

---

## 5. 词汇层（S4）核对：28 条例句逐字命中

- 方法：把 md「本章词汇」28 行的例句单元格原文取出，对 `text/ch26_26.txt` 做子串计数（`str.count`），
  **要求恰好 1 次**（既验逐字、又验不是跨章/跨话轮误取）。
- 结果：**28/28 行命中次数 = 1**，非 1 的行数为 **0**（`rows with hits != 1: []`）。
- 三条例句是**截断引语**（`uniform` / `new starter` / `collected` 三行同用一段），截断点落在句号后，
  但**省掉了原文的收尾引号 `’`**（原文该处为 `…I’ll deal with that. Matt, get the staff…`）。逐字性不受影响，格式上属小瑕，记为提示。
- 档位注水：`check_vocab.py`（整书）FAIL 0；26 条 WARN 中属 ch26 的 4 条为
  `[基础] 基础档疑含超纲词「definitely」「different」「purchased」「collected」`——这四个都是日常高频词，列入 ⭐ 基础 档属**注水**（`different`/`definitely` 尤其接近无用条目）。全书 26 条同型 WARN（另 22 条分布在 ch13/ch18/ch19/ch21/ch33/ch34/ch39/ch41/ch46/ch50/ch52/ch54），属书级习惯，非本章独造。⇒ **提示**。

---
