# 4-verdict.md · 《A Fatal Legacy》第 22 章独立审查判定

| 项 | 值 |
|---|---|
| 章 | 22 · `ch22 matt questions beverley parkin.md` |
| 权威源 | `notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch22_22.txt`（6119 字符 / 149 行） |
| 落盘 | `.memory/raw-gates/a-fatal-legacy-by-charlotte-vassell/review/ch22/`（1-suread.json / 2-machine.json / 3-diff.md / 4-correspondence.md / 4-verdict.md） |
| 覆盖声明 | **本次只审第 22 章**（人判 R1–R5 全跑）。**其余 53 章只有机器层**（`verify_corpus.py` 全书 PASS、`check_vocab.py` 全书 FAIL 0、`bookform.py` 全书形态基线），**未做人判，不写成「通过」**。本章未做跨章人判（ch19/ch26 与本章的线索相接未核）。 |
| 机器层 | `bash scripts/chapter.sh "<md>" --json` → **EXIT 0**，`verdict: ok`；输出存 `2-machine.json` |

---

## 一、四组数（只报这四组）

### 1. 逐字：**6/6 引语段逐字命中；词汇例句 29/29 逐字命中本章**

- 引语：6 个块各 1 段，**每段 `ok=true`，无 `…` 缝合、无跨话轮拼接**（`2-machine.json` 的 `counts.segment_miss = 0`）。
- 词汇表：29 行（⭐⭐⭐ 9 / ⭐⭐ 10 / ⭐ 基础 10）例句**逐字命中本章**——工具口径 `check_vocab.py` 全书 FAIL 0 且 ch22 无 WARN；**另用独立实现**（Python 逐行 `in text` 比对）复核：**0 行不命中**；29 个词头也全部在本章出现。
- 例句排版：2 条例句缺收尾引号（见提示 #17）——**内容逐字成立，只是引号未闭合**。

### 2. 对应：**6 块中 3 块三层全中引语；2 块中文覆盖越出引语边界；1 块部分越界；阻断级 1 条（块 1 归属反转）**

| 块 | 引语位置 | 中文理解 | 为什么这样写 | 读者视角提示 | 该块结论 |
|---|---|---|---|---|---|
| 1 | `:32` | 对应 | **引语选短** | **归属反转（阻断）** | 阻断 1 + 提示 2 |
| 2 | `:95` 后半 | **引语选短** | 对应（解读过强） | 对应 | 提示 2 |
| 3 | `:119` 前段 | **引语选短** | 对应 | **编**（地毯、书架） | 提示 2 |
| 4 | `:125` | 对应 | 对应 | 与引语相抵 | 提示 1 |
| 5 | `:137` 后半 | 对应 | 对应（判断正确） | 对应 | **完全对应** |
| 6 | `:149` 末段 | 对应 | 对应（＋梳妆台） | 对应 | 提示 1 |

- **密度不足：0 块**（6 块都写了「为什么这样写」＋「读者视角提示」，且都指向本章对照轴，不是字面复述）。
- **不对应（讲全书主旨/作者生平）：0 块。**

### 3. 形态：**无偏离**（H1 / 导航项名与项数 / 子项集 / 块数 四项全合本书众数与 profile）

| 项 | 本章 | 本书众数 / profile | 偏离 |
|---|---|---|---|
| H1 | `# 22. Harrogate` | 「N.」写法 **54/54** | 无 |
| 导航项名与项数 | 5 项：一句话概括 / 视角 / 线索结构 / 人物弧线 / 叙事手法 | 众数 **5 项，名单逐字相同** | 无 |
| 子项集 | 中文理解 / 关键词 / 为什么这样写 / 读者视角提示（4） | 众数 **4 项，名单逐字相同** | 无 |
| 块数 | **6** | 中位 7，范围 5–10；profile 3–10 | 无（在范围内，**不需写偏离理由**） |
| 前置元信息 | `状态: 未读` / `modified` / `source_text: ch22` | 全书 54 章一致 | 无 |

### 4. 断言：**核 25 条（导航 5 + 6 块×3 层 + 一句话总结 1）+ 漏 2 条 + 词表 29 行；不成立 17 条＝阻断 2 + 提示 15；词表 29 行断言全部成立（例句逐字 29/29、词头 29/29 在本章）**

- 不成立明细：**阻断 2 条**（#1 称谓归属反转、#2 「亲口说出」）、**提示 15 条**（#3–#4 引语选短 ×2、#5–#7 编 ×3、#8–#9 漏 ×2、#10–#17 措辞/断言相抵 ×8）。
- 机器层（`2-machine.json`）：`struct_bad 0` / `empty_quote 0` / `keyword_bad 0` / `cjk_low 0`；中文理解 CJK 36–89 字（占比 0.78–0.93）、为什么这样写 57–75 字（0.79–0.91）、读者视角提示 30–52 字（0.43–0.88）。

---

## 二、判定表（断言 | 证据 | 结论 | 档位）

| # | 断言（md 侧） | 证据（章:区间） | 结论 | 档位 |
|---|---|---|---|---|
| 1 | md:23 原句 1 读者视角提示：「妻子叫「Bev」、丈夫叫「Beverley」；门外那个「Mrs Beverley Parkin」在这套叫法之外，是另一重身份。」 | `text/ch22_22.txt:38`「‘What is it, Beverley?’ … ‘I told you, Bev, just shut the door.’」／`:41`「‘No, Nigel, he’s police.’」／`:110`「‘Bev, did you leave a little piece of paper with the PIN number on it with the card?’」／`:23`「‘Hello, are you Mrs Beverley Parkin?’」 | 原文里 **「Bev」「Beverley」都是丈夫 Nigel 对妻子 Beverley 的称呼**；丈夫叫 Nigel；「Mrs Beverley Parkin」就是她本人的正式称谓，不是「另一重身份」。md 把丈夫改名成 Beverley 并多造一个身份 | **阻断** |
| 2 | md:14 导航·人物弧线：「走到后来**亲口说出**女儿的「another turn with her nerves」、伦敦有「better doctors」，以及那笔瞒着丈夫的钱」 | `text/ch22_22.txt:137`「‘I know.’ Beverley nodded. **She thought** it was for the best too for Jenny … It also meant that if Jenny had another turn with her nerves the neighbours didn’t have to see or hear of it like last time. Besides, they had better doctors down there.」／`:149`「…**She really didn’t want to upset** the little bit of ‘housekeeping’ she was sent on the sly every month without her tight husband’s knowledge…」 | 三项**全在内心叙述里，不是说出口的话**；`:149` 更明写 `without her tight husband’s knowledge`（说出口就不叫瞒着）。且与本 md 原句 5「这些话全被压在贝弗利的心想里，夫妇俩谁也没有说出口」**自相矛盾**；本章轴心是「她说的 vs 她没说的」 | **阻断** |
| 3 | md:26 原句 2 中文理解首句：「贝弗利先说自己只有一个账户、只用来收账单和 Next 的促销邮件」 | `text/ch22_22.txt:95` 前半：「‘Oh no. I’ve got an account but I only really use it to get my bills and emails about the Next sale,’ Beverley said. She turned to look at Nigel and furrowed her brow. **‘Hang on, Nigel. …’**」 | 该句在**引语之外**（引语从 “Hang on, Nigel.” 起）⇒ 引语选短 | 提示 |
| 4 | md:32 原句 3 中文理解末句：「母亲年轻时应当是秀气的，这姑娘大概随了她那位面团似的父亲」 | `text/ch22_22.txt:119` 引语止于 “…colour of her neck.”，其后才是「**Beverley looked like she would’ve been pretty when she was younger. Her daughter must have taken after her doughy father.**」 | 分析盖过引语边界 ⇒ 引语选短 | 提示 |
| 5 | md:35 原句 3 读者视角提示：「先看房间（**吊灯、地毯、书架**）」 | `text/ch22_22.txt:20/35/50/56/95/119` 全部陈设；**无地毯、无书架**（见下方取证 #5） | 陈设虚增（原文只有吊灯） | 提示 |
| 6 | md:52 原句 6 为什么这样写：「秘密都藏在**衣柜与梳妆台**之间」 | `text/ch22_22.txt:149`：「…all the other little treats that her husband had been convinced had come from **the back of the wardrobe**.」；本章无 vanity/dresser/comb | 梳妆台为原文没有的物件 | 提示 |
| 7 | md:13 导航·线索结构：「毕业照与**那双刻意藏拙的眼睛**」 | `text/ch22_22.txt:119`：「…hide under **a chunky fringe and a layer of caked-on make-up that didn’t match the colour of her neck**.」；本章唯一的 eye 是 `:134`「her sister kept an eye on her」 | 眼睛为虚增；且与原句 3 自己的中文理解（刘海＋浓妆）口径不一 | 提示 |
| 8 | md 全章 6 块 + 导航线索：未覆盖 `:77`–`:83` 皇家婚礼/Lady Di 一段 | `text/ch22_22.txt:77`「‘I’ve not been to London since the Royal Wedding. … I was stood right in front of Westminster Abbey. Me and my cousin camped out the night before. What a fairytale.’」／`:80`「‘Kate Middleton?’」／`:83`「‘Oh no, Lady Di,’ Beverley said, gesturing to a commemorative plate in a cabinet. ‘Taken too young.’」 | 有信息量的对话漏出；这是全章唯一直接回应「伦敦 PO Box」的材料（词汇表仅收了 commemorative 一词） | 提示 |
| 9 | md 全章：未覆盖 `:110`–`:116` PIN 纸条一段 | `text/ch22_22.txt:110`「‘Bev, did you leave a little piece of paper with the PIN number on it with the card?’」／`:113`「‘I might have done, Nigel.’」／`:116`「‘You’ve got to be more careful.’」 | 本章最实的一个漏洞未成块 | 提示 |
| 10 | md:41 原句 4 读者视角提示：「三件事一口气说完，**中间没有一句「为什么」**」 | `text/ch22_22.txt:125`：「…She said she just wanted to buy a cardigan. **And why are the police interested?’**」 | 引语第三件事本身就是 why 句，措辞与引语相抵 | 提示 |
| 11 | md:28 原句 2 为什么这样写：「这一段等于由她自己**认下了「受害者」这个位置**」 | `text/ch22_22.txt:95`：「It can’t have been an expensive charge or I would’ve noticed and challenged it with the bank. **I hadn’t noticed anything, actually.**」；`:71`「‘No, definitely not,’ Beverley said, mystified.」 | 她明说没察觉、否认受害；「主动翻出丢卡」是给替代解释，非认下受害 | 提示 |
| 12 | md:11 导航·一句话概括：「转头却**跟丈夫念叨**女儿要「买件开衫」，**以及每月瞒着丈夫办的那趟差事**」 | `text/ch22_22.txt:149`：「…she was sent on the sly every month **without her tight husband’s knowledge**…」 | 瞒着丈夫的事不可能念叨给丈夫；句子自相矛盾 | 提示 |
| 13 | md:103 一句话总结：「她嘴里没说的那部分……**全落在她转身跟丈夫说话的那些话里**」 | `text/ch22_22.txt:137`（`She thought …`）／`:149`（`She really didn’t want to upset …`） | 这三样只在**叙述层（她心里）**；她说出口的只有 “I know.” / “It’s no big deal.” / “I’ll call later, love.” | 提示 |
| 14 | md:22 原句 1 为什么这样写：「作者先用**一个笑声**把这次登门定成家庭喜剧……**丈夫的慌手慌脚**并置」 | `text/ch22_22.txt:32`（引语全文）无笑声；丈夫的慌张在 `:35`「A bald man appeared behind his wife at the door. **He was flustered, his cheeks red;**…」 | ①全章无 laugh/chuckle/giggle；②所分析的「丈夫的慌手慌脚」不在引语内 ⇒ 措辞＋引语选短 | 提示 |
| 15 | md:20 原句 1 中文理解：「像**歌剧里的号角**一样喊了出去」 | `text/ch22_22.txt:32`：`and then again with **operatic gusto**`（本章无 bugle/horn/trumpet） | 「歌剧般的劲头」被换成「号角」；方向对（夸张带表演感），非阻断 | 提示 |
| 16 | md:11 导航·一句话概括：「Matt 开着**四个小时**的车到哈罗盖特」 | `text/ch22_22.txt:119`：「Matt handed Beverley his card and **left for the four-hour drive back to London**.」 | 四小时是**回程**；去程时长原文未言（往返同路，可接受） | 提示 |
| 17 | md:82 / md:83 词表例句缺收尾引号 | `text/ch22_22.txt:146` 原文「…one little dodgy payment like **that.’**」／`:95` 原文「…in M&S Food the other month. **I had to get a new card…**」 | 例句只有开引号无收引号；**全书同类 37 行 / 17 章**，非本章独有 ⇒ 排版口径问题，不判本章阻断 | 提示 |

### 假红（工具判错，不改 md）

| # | 报警 | 证据 | 结论 | 档位 |
|---|---|---|---|---|
| F1 | `grep -cinE 'carpet|rug|bookshelf|dressing table' text/ch22_22.txt` → **1**（读起来像「原文里有地毯」） | 命中行是 `:131`「Beverley **Shrugged**.」——**子串 `rug`**；改用 `-w` 口径 → 无输出，EXIT=1 | **工具口径错**（纯子串误命中），md 无地毯；R5-补 明示此类坑 | **假红** |
| F2 | `2-machine.json` 报 `关键词` 子项 CJK 计数全为 0 | 关键词层是西文词条行（`demurely / operatic gusto / …`），工具按中文字符计 | 非缺项，非密度问题；`keyword_bad = 0` | **假红** |

### 跳过

无（本章 R1–R5 全部跑完）。**跨章人判未做**：ch19（PO Box 线索来源）、ch26（Matt 回伦敦）只经全书机器层覆盖。

---

## 三、已核实为正确（防误修 · 本节内容后续不得以「读着不对」为由改动）

| 看起来像错 | 回原文核对 | 原文逐字 | 结论 |
|---|---|---|---|
| 导航写「本章属『五月的星期三』这一分部」，而 `text/ch22_22.txt` 里只有 “Harrogate”、没有星期字样 ⇒ 像编造 | **epub 目录结构为准**：`OPS/s005-TableOfContents-01.xhtml` 分部表为 Part1=`A FRIDAY IN MAY`、Part2=`SATURDAY`…**Part6=`WEDNESDAY`**（ch21–ch27 在 Part6 内）；全书首分部即 “A FRIDAY IN MAY”，其后连日顺排 ⇒ ch22 属五月的星期三 | TOC 链接逐条：`s033-Part-006.xhtml#Part6 | 'WEDNESDAY'` | **成立**，非编造 |
| 「五个星期三」这分部名看起来像 md 内部自造，与其他章写法不一致 | ch21/ch24/ch25/ch26/ch27 的 md 同样写「分部「A WEDNESDAY IN MAY」」 | — | **全书口径一致**；ch22 写成「五月的星期三」只是措辞不同，不判缺陷 |
| H1「22. Harrogate」像是把两处标题并成一处 | epub：`s035-Chapter-022.xhtml` = `<h1>22</h1>` + `<h2>Harrogate</h2>`；本书 54 章 H1 众数即「N. + 副标题」 | — | **成立**，与全书形态一致 |
| 原文只有 “22” 与 “Harrogate” 两行，语料像是缺内容 | epub 逐段对账：`s035-Chapter-022.xhtml` 44 段**全部逐字命中 `text/ch22_22.txt`**，0 段丢失、0 段多出 | — | **语料完整**，`verify_corpus.py` 全书 PASS |
| 原句 3 说「母亲的女儿」是照片里的姑娘，但原文只写 “a young woman” | `text/ch22_22.txt:119`：「There was a graduation photo of a young woman… **Her daughter must have taken after her doughy father.**」 | — | **成立**：女儿身份是 Matt 的推断，md 照此写，未把它说成事实 |
| 原句 4 写「Matt 问的是信箱，贝弗利转述给丈夫的却是『买开衫』」，像在说两句是同一件事 | `text/ch22_22.txt:56`「Did you rent a PO Box in London recently?」／`:125`「She said she just wanted to buy a cardigan.」 | — | **成立**（本章的对照轴即此） |
| 原句 5 说「这层没说出口的话全在贝弗利心里」，像与本章「她嘴里没说的」主题矛盾 | `text/ch22_22.txt:137`「**She thought** it was for the best too…」 | — | **成立**，原句 5 判断正确；错的是导航「人物弧线」（阻断 #2） |
| 词汇表把 `commemorative` 放 ⭐⭐⭐、`mystified` 放 ⭐⭐，像档位注水 | `check_vocab.py` 全书 FAIL 0 且 **ch22 无 WARN**（分档合理性检查覆盖本章） | — | **工具口径内不成立**；仅作「档位高低可再斟酌」的提示，不计缺陷 |

---

## 四、取证命令（全部贴命令 + 输出 + 退出码）

```
# 1) 机器门禁（第二章专属）
CMD: bash scripts/chapter.sh "notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch22 matt questions beverley parkin" --json > .memory/raw-gates/a-fatal-legacy-by-charlotte-vassell/review/ch22/2-machine.json
→ verdict: ok；quotes 6/6 ok=true；counts: segment_miss 0 / struct_bad 0 / empty_quote 0 / keyword_bad 0 / cjk_low 0；form.h1 "22. Harrogate"、nav_count 5、blocks 6（book 众数中位 7，范围 5–10）
EXIT=0

# 2) 语料验收（全书）
CMD: python3 scripts/verify_corpus.py "notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell"
→ "=== P0-0 语料验收: PASS（FAIL 0 / WARN 3）==="（3 条 WARN 与本章无关：未给 --expect / ch23 页码 bleed / 未给 --anchors）
EXIT=0

# 3) 词汇表（全书 + ch22）
CMD: python3 scripts/check_vocab.py "notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell"
→ "--- FAIL (0) ---"；"--- WARN (26) ---" 中 **无 ch22**（ch13×2 / ch18 / ch19 / ch21×2 / ch26×5 / ch33×2 / ch34 / ch39 / ch41×2 / ch46×2 / ch50×2 / ch52×2 / ch54×2）
EXIT=0

# 4) 本书形态基线
CMD: python3 scripts/bookform.py "notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell"
→ 已有章 md: 54；H1 写法 {'N.': 54}；导航项（众数，5 项）一句话概括/视角/线索结构/人物弧线/叙事手法；子项集（众数，4 项）中文理解/关键词/为什么这样写/读者视角提示；每章块数中位 7.0，范围 5–10；profile mystery-thriller（子项 4 项｜块数 3–10｜总览 3 篇）
EXIT=0

# 5) 地毯/书架/梳妆台（否证 #5 #6）——显式路径 + 词边界
CMD: /usr/bin/grep -inwE 'carpet|rug|bookshelf|bookcase|vanity|dresser|comb' text/ch22_22.txt
→ 无输出
EXIT=1
（对照 CMD: /usr/bin/grep -cinE 'carpet|rug|bookshelf|dressing table' text/ch22_22.txt → 1，命中 :131 "Beverley Shrugged." 的子串 rug ⇒ **假红 F1**，词边界为准）

# 6) 笑声（否证 #14）
CMD: /usr/bin/grep -inE 'laugh|chuckle|giggle' text/ch22_22.txt
→ 无输出
EXIT=1

# 7) 号角/小号（否证 #15）
CMD: /usr/bin/grep -inE 'bugle|horn|trumpet' text/ch22_22.txt
→ 无输出
EXIT=1

# 8) 眼睛（否证 #7 的「藏拙的眼睛」，并给出本章唯一的 eye）
CMD: /usr/bin/grep -inwE 'eye|eyes' text/ch22_22.txt
→ 134:…her sister kept an eye on her. Made sure she was OK.
EXIT=0

# 9) 称谓归属（正证 #1）
CMD: /usr/bin/grep -inwE 'Bev|Beverley|Nigel' text/ch22_22.txt
→ 命中 20+ 行，逐行核对：「Beverley」每次都指妻子（Nigel 叫/Matt 叫/她自称），「Nigel」每次都指丈夫，「Bev」只出现在 Nigel 的台词（:38/:110/:146）
EXIT=0

# 10) 皇家婚礼段（正证 #8 的存在）
CMD: /usr/bin/grep -inE 'Royal Wedding|Lady Di|Kate Middleton|Westminster' text/ch22_22.txt
→ 77:…I’ve not been to London since the Royal Wedding… Westminster Abbey…；80:‘Kate Middleton?’；83:‘Oh no, Lady Di,’ … ‘Taken too young.’
EXIT=0

# 11) epub 分部与章结构（正证「五月的星期三」）
CMD: unzip -p "library/A Fatal Legacy (…).epub" OPS/s005-TableOfContents-01.xhtml | python3 -c '…'
→ s008-Part-001.xhtml#Part1 | 'A FRIDAY IN MAY'；… s033-Part-006.xhtml#Part6 | 'WEDNESDAY'（ch21–ch27 在其内）；s035-Chapter-022.xhtml#Chapter22 | '22'
EXIT=0

# 12) epub ↔ text 逐段对账（本语料自证）
CMD: python3 - <<'PY'  # 抽出 s035-Chapter-022.xhtml 的 44 段，逐段在 text/ch22_22.txt 中查逐字命中
→ "epub paras: 46 src lines: 47"；"epub paras NOT found verbatim in src: 0"；"src lines NOT found in epub: 0"
EXIT=0

# 13) 词表例句逐字（第二实现，独立于 check_vocab）
CMD: python3 - <<'PY'  # 29 行例句逐行 in text/ch22_22.txt
→ "rows: 29"；"examples NOT verbatim in ch22 text: 0"；"headword not literally in chapter text: []"
EXIT=0
```

---

## 五、结论

- **阻断型 2 条**（均属机器查不出的两类）：① md:23 把「Bev／Beverley」的称呼方向写反、把丈夫说成叫 Beverley；② md:14 把贝弗利的**心里话**说成「亲口说出」，与原文、与本 md 原句 5 均相抵，且正好推翻了本章的对照轴（她说的 vs 她没说的）。
- **提示 15 条**：引语选短 ×2（块 2、块 3）、原文没有的陈设/身体细节 ×3（地毯书架、梳妆台、眼睛）、未成块的对话 ×2（皇家婚礼/Lady Di 段、PIN 纸条段）、措辞或解读与引语相抵 ×8（没有一句为什么／认下受害者／念叨那趟差事／位置错／笑声／号角／四小时去程／例句缺收尾引号）。
- **形态无偏离**；**逐字 6/6 + 例句 29/29**；**对应 3/6 完全成立**，密度不足 0、不对应 0。
- **假红 2 条**（`grep` 子串 `rug` 命中 `Shrugged`；关键词层 CJK 计数为 0）——均为工具口径，**不要求改 md**。
- **已核实为正确 8 条**（含「五月的星期三」这一分部、语料完整、H1 形态、原句 3 的女儿推断、原句 5 的「没说出口」判断、词表例句与档位），后续不得以「读着不对」为由改动。
