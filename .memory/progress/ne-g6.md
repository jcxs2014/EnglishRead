# ne-g6 交付报告（ch14 / ch15）

组前缀：ne-g6 ｜ 书：Null Entity (Seth Haddon) ｜ 体裁档：精简格式 · 完整 lane（epub 在 `library/`）
交付时间：2026-10-09

## 产出文件

| 章 | 文件（绝对路径） | 块数 | ne_strict 阻断 | WARN |
|---|---|---|---|---|
| ch14 | `/Users/jcxs2014/Documents/Works/EnglishRead/notes/books/novels/null-entity-by-seth-haddon/ch14 a wife turned extremist.md` | 8 | **0** | 0 |
| ch15 | `/Users/jcxs2014/Documents/Works/EnglishRead/notes/books/novels/null-entity-by-seth-haddon/ch15 i am lyrebird.md` | 8 | **0** | 0 |

两章 `text/` 实际体量：ch14 = 16,838 字符（121 段）、ch15 = 9,933 字符（68 段）——均按长章 8 块配。
自检命令（各跑一次，退出码 0）：

```
python3 scripts/attic/ne_strict.py "$BOOK/ch14 a wife turned extremist.md" --book "$BOOK"   # 块 8 | FAIL 0 | WARN 0
python3 scripts/attic/ne_strict.py "$BOOK/ch15 i am lyrebird.md" --book "$BOOK"             # 块 8 | FAIL 0 | WARN 0
```

写前另跑自写断言（`/tmp/ne_g6_assert.py`）：逐条 `assert q in src`（引语 13 / 12 段全部命中本章 `text/` 精确子串、
末字符均落 `.?!"""` 句读边界、零省略号）＋分析层英文片段逐条 `in src_flat`（ch14 57 条、ch15 47 条，问题 0）。
相邻性另用 `/tmp/ne_g6_adj.py` 取证：全部多段块均为**原文相邻段落**（ch14 块 1/2/6/7/8；ch15 块 1/5/7/8），
块起始偏移覆盖 0/9/40/55/59/73/82/99%（ch14）与 0/6/15/20/48/63/79/98%（ch15）⇒ 前中末段全覆盖。

词表：全部走 `python3 scripts/vocab_candidates.py "$BOOK" --ch 14|15 --tiers` 输出**粘贴选行 + 只做减法**，
未手打任何词条或例句；释义纯中文（WARN 0 佐证）；通行专名（VisorForge / LYREBIRD / Subsidiary / byronnicum /
Thorned Root / RABBIT）未收表。

## 跨章指涉（当场 grep 记行号）

| md 里的指涉 | 被指章 text/ 行号 | 原文（逐字） | 处置 |
|---|---|---|---|
| ch14「原句 5」读者视角提示：这份"赠予"在**上一章**链接空间里由 Aliers 反问"是谁把你弄出来的" | `ch13_chapter_13.txt:90` | `“Sable,” she laughed, tears rising. “Who do you think got you out of here?”` | **只写中文转述，md 内不出现该章英文**（ne_strict 只按本章 text/ 判） |
| ch14 本章内"机制补全"（为姓设提醒 ⇒ 撬开安保松掉束缚） | `ch14_chapter_14.txt:219` | `I had a ping set for the Alzian name …` | md 内引英文，命中本章 ✓ |
| ch15「原句 7」读者视角提示：null entity 此前一直被用来称呼 Wylla | `ch01_chapter_1.txt:259`（另 `ch02:325`／`ch03:267`／`ch04:125`） | `Erasing your GIRS record had made you a specter, a null entity.` | md 内只出现 **null entity**（该词本身在 ch15:192），其余中文转述 |
| ch14 末句「先把我弄回我的身体」→ ch15 开场把它列为第一优先 | `ch14:372` ↔ `ch15:18` | `“Get me back in my body,” you said, “and we’ll talk.”` / `Getting you back in your body was priority one.` | **md 内不跨章引英文**，只在 ch14 用中文说"下一章开场就把这件事列为第一优先" |

已核但**未写入 md** 的跨章证据（供总览层取用）：
- ch14:180 `And I recalled her saying: The Directory was mine.` 的原始出处 = `ch12_chapter_12.txt:48`（`“Because I designed it,” … the Directory was mine.”`）。
- ch14 开场的物理现场（Aliers 倒地、植物被压碎、身上有灼伤）的直接前因 = `ch13:117`（`Aliers had been hit by a plasma blaster.`）与 `ch13:126`（`You’d come like an angel … leveled it at her neck`）。
- ch14:93「the torture of the trials」／ch14:219「VisorForge trials」的前文 = `ch09:108`、`ch11:111`、`ch11:135`（LYREBIRD trials 的代价）。
- ch15 里 Rahn 的身份前文 = `ch10:75`（`the hacker Rahn`）、`ch11:45–96`（他抱走抽搐的 Sey）——**ch15 的 md 只按本章写他**（吊带的臂、树脂封的伤口、判断"从内部"），未把"hacker"当他的定语。

## 我不敢下判断的清单（总览层请勿据此落笔）

**ch14**
1. 「我」与 Sable Alzian 的**同一性**未被叙述者确认：本章只写 Aliers 那边的认定（`Sable—you—did the rest`、`who’d seen only my name and knew we were kin`），以及 `Sable Veonya and Sable Alzian, every version of that girl-turned-woman` 的并列——**"我就是 Sable Alzian"不是本章可下的结论**。
2. Wylla 是否真的打算"打完就走"、离开后去哪里：本章只给 `I’m seeing this through. And then I’m done.` 与 `You would go somewhere quiet, and I would … figure it out.`（后者是"我"的推测句）。
3. Aliers 身体的改造程度：`the sutures around her plants, the ratking cluster pressing into her veins` 只出现在"我"日后读取 LYREBIRD PRIME 的**记忆碎片段**里（`Later, when I split myself into LYREBIRD PRIME, I’d revisit its stores`）——时态是未来预演，不能当作本章已完成的动作。
4. RABBIT 被 daemon/biocode 改变的确切机制：Wylla 自己注了不确定 —— `The daemon affected it. The biocode, I think.`
5. 交易的实际履行（谁把 Wylla 的意识放回身体、用什么设备）本章未写；`neural pulse` 的原理陈述也只到"我临时编的"层级（`I made it up`）。
6. Fyster 之死的细节归属：本章只有 `You wrecked Fyster`（在 ch15:48，非本章）／ch14 内是 `her body’s death`、`as his mind burned`（Aliers 的幻想，非既成事实）。

**ch15**
1. **本章首句 "You're going to have to kill it." 的说话人原文无归属标签**——按行文紧邻（Rahn 随即出场并接手解释技术限制）指向 Rahn，md 里已按"随后接手解释的那个人"措辞，**不可升级为定论**。
2. 结尾 `you clutched something new` 的"新东西"是什么、来自哪一部分残骸：原文只给动词不给名词，本章不裁决。
3. RABBIT 被逐出系统后如何回来并吞掉信号：原文只写 `Without you asking, RABBIT had bounded after it … the signal absorbed in RABBIT’s furry flank`，机制未写。
4. Wylla 的人类身体能否成功苏醒（本章仍在呼吸器下、`chest hauled up and down by automated breath`），本章不下结论。
5. Four 之死对 VisorForge／Subsidiary 网络的连锁后果：本章止于"信号被吞"，`the fractional signal was racing` 是否已被别处读到未写。
6. 「我」自称 `I am LYREBIRD.` 与面具／载体的名分关系（她是不是 LYREBIRD 的"正主"）本章不解释——`I was human and beyond human` 是她的自我认领，不是设定判词。
7. `Subsidiaries were amalgamates … never more than their programming` 是叙述者在战斗中的立场性判断，**不可当作世界设定转述**。

## 过程备注

- **未做任何 git 写操作**（add/commit/stash 一律没跑）；临时脚本全部 `/tmp/ne_g6_*`（`/tmp/ne_g6_probe.py`、`_paras.txt`、`_xref.py`、`_xref.txt`、`_assert.py`、`_adj.py`）。
- 未读其他组的 md（在制品）；跨章取证只 grep `text/`。
- 本组只跑第 3 条门禁中的**章级自检**（ne_strict）；`verify_quotes` / `check_vocab` / `check_entities` / `corruption_scan` / `sweep_full` 的批次口径留给主会话提交前统一跑。
- 引语零省略号；含 `…` 的原段落（如 ch14 的 `[40]`／`[54]`／`[62]`／`[107]`）一律**未选作引语块**；分析层若要指涉其内容一律改中文转述。
- 追加自查（写完后）：`python3 scripts/corruption_scan.py "$BOOK"` 目录级跑一次 ⇒ **FAIL 0 处（U+FFFD / 双句号）**，本组两文件在内；
  中文散文行的直引号已统一为弯引号（两文件 `"` 与 `'` 均为 0，`>` 引语行未受影响，改后重跑 ne_strict 仍 FAIL 0）；
  文件名 keyphrase 与目录内既有 md（ch01/04/09/10/11/21/22）无重名。
