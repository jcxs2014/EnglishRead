# ne-g5 交付报告 — ch11 / ch12 / ch13（2026-10-10 00:12 重建版）

⚠️ 本文件在 00:07 前是空壳：我收到的压缩摘要称「23:50 已有一份 11,949 B 的报告」，但我在本方转录
（sidechain `agent-ageneral-purpose-a1b211cc56a9328e`）与全部 sidechain 转录里都找不到那次写入。
**请勿把「那份报告曾存在」当作事实引用**；下面是据实重建，所有数字为 00:05–00:12 现算。

## 一、逐章清单

| 章 | 文件（keyphrase 取自本章 text/） | 源字符 | 块数（分档） | 首块/末块所在真实行 | ne_strict --book | 词表 高/进/基 | 汉字 |
|---|---|---|---|---|---|---|---|
| ch11 | `ch11 cheap echoes of me.md` | 6,576 | 8（中章 5–8） | L15 → L159–L162 | **FAIL 0｜WARN 0** | 11/12/5=28 | 3,406 |
| ch12 | `ch12 like knows like.md` | 7,519 | 8（中章 5–8） | L15 → L183–L201 | **FAIL 0｜WARN 0** | 12/16/5=33 | 4,212 |
| ch13 | `ch13 hostile fusion.md` | 4,996 | 6（短章 3–6） | L15 → L108–L129 | **FAIL 0｜WARN 0** | 13/14/5=32 | 3,578 |

覆盖：三章首块都起于正文第一行 L15（L1 是 `Chapter NN` 标题行，L2–L14 空），中段有块，且末块都收到**本章文件的最后一行**——ch11 块 8＝text/:159＋:162（`And this, I knew, was what she had wanted us to see.`）、ch12 块 8＝:183…:201（`“Hello, Sable.”`）、ch13 块 6＝:108…:129（`“Get your head out of my girlfriend, bitch.”`）。（`text/` 文件首行 L1 是 `Chapter NN` 标题行，正文自 L15 起，段间夹空行——以下所有行号都是文件真实行号。）
一句话总结 77／71／97 字。

## 二、跨章指涉（00:12 用脚本重扫全书 `text/` 得的确切行号；md 内一律只用中文表述，不放他章英文）

- ch11 开场 ↔ **ch10:219** `The four of us entered the cargo wing together.`；ch10 的**最后一行 ch10:234** `And the barrels of six blasters.` 与本章首块 `six of my cousins` 咬合。
- ch11:159 `When I’d asked Aliers your question—What do you need us for?—she’d said: That’s easier to show you.` ⇒ `need us for` **全书仅这一处**（ch09 里没有同一句），所以它是章内转述，不是对第 9 章的回指（压缩前的旧笔记记的「ch09:270」经重扫**证伪**，勿用）。
- ch11:108 `daemon removal`；`daemon` 一词的概念层在 **ch04:101 一带**建立（ch04 内 10 处）。ch11:114 `Veonya`、:120 `mutiny`、:126 `Thorned Root was burning itself out.` 各自本章只 1 次；`Thorned Root` 首现 **ch03:444**（此后 ch07/ch08/ch10… 多处）。
- ch12:15 `LYREBIRD MARK II PRIME`（全书唯一）；ch12:57 `Four’s amalgamate mind`（全书唯一）；ch12:141 同一行内 `BSMC-07` 与 `invaluable`（`BSMC-07` 另见 ch01:24/79/175、ch08:258）；ch12:183 `mnemonic parasite`（全书唯一）。
- ch12→ch13 相接：ch12 末行 `“Hello, Sable.”`（:201）→ ch13 正文首行 `Renata Aliers’s mind was full of thorns.`（:15）。**Renata 在 ch11/ch12 出现 0 次**，首次落地就是 ch13:15（其后 ch14:48/51/66/312、ch22:96）。
- ch13:54 `General Aliers` 是本章唯一一处 `General`；`General Aliers` 这一称呼早于本章即有（**ch07:156、:201**）。ch13:60 `Sable-wearing-LYREBIRD` 全书三处：ch13:60、ch14:243、ch15:60。ch13:75 `killed the bastard`（全书唯一）。
- ch13:90 `Who do you think got you out of here?` ⇒ `got you out` **全书只这一处**，救人者在本章没有交代（md 内未断言是谁救的）。
- 引文行号一律按文件真实行号：ch11 共 162 行、ch12 共 201 行、ch13 共 129 行。

## 三、我不敢下判断的清单（总览层需用）

1. ch11 首段显形的「Sable」是本人、幻象还是别物——本章无判据，md 写成「读者此刻无法分辨」。
2. ch13:60 `appearing as Sable-wearing-LYREBIRD`：显出的到底是 Sable 还是穿着 Sable 战衣的 LYREBIRD，原文歧义，不作定论。
3. ch12:201 `“Hello, Sable.”` 的说话者、以及「一副新的感官」是谁的——本章不交代，md 明说「不做说明」。
4. Wylla 是否知道 Renata 在场/知情；ch12:141 Aliers 那句 `“That directory is invaluable. … What do you think?”`（把 Wylla 当 `an expert hacker, Sotain` 来劝）之后 Wylla 的立场如何——本章不给反应，无文本证据。
5. 「Renata Aliers」＝「Aliers 将军」＝本章被夺舍的那个人：这是**我的推断**，原文没有一句明写等同（我只核到 ch13:15 `Renata Aliers’s mind…` 与 ch13:54 `General Aliers` 都在写眼前这位 Aliers）。他章是否另有明写未逐一 grep。
6. 「谁把我们弄出去的」：ch13:90 只是反问，答案我未核到具体行（全书 `got you out` 仅此一处），md 因此不写。
7. ch13:123–:126（`You had happened.` / `You’d come like an angel. A savior. …`）两行**无引号、无说话人标签**：我在 md 里按「叙述者在 Aliers 颅内替她感受」处理，但这是解读，原文没有明写是谁在想。
8. `Directory` 的机制说法我只在本章内逐句核过引语（ch12:48 `Because I designed it` / :60 `The Rhizome Directory.` / :72 `her link to the Directory died` / :117 `Sable can see the Directory, can’t she?` / :141 `That directory is invaluable` / :165 `the Directory needs living tissue`），与 ch09/ch10/ch14/ch19 的设定描述是否一致**未核**；总览层若要写设定说明需另查。
9. 章节号映射 ch01–ch22＝正文 1–22 章、ch23＝Epilogue，系据 `text/` 文件名（`ch23_epilogue.txt`）推得。
10. 词表短语行（如 `invaluable` 行）已按指令书第 6 节末条把英文短语列改写为中文释义。
11. **压缩前旧笔记里有一批行号经重扫证伪，已全部剔除，请勿引用**：ch12:213 `Her name was Renata Aliers.`、ch12:159 `The station was my design.`、ch12:201 `We both did.`（实为 ch01:308）、ch13:138–141 `And then we screamed together.`（实为 ch13:117 `We screamed together, pain snapping us back to reality.`）、ch08:312 `We are going to take you to our camp.`（全书无此句）、ch10 尾句 `Ten thousand faces and none of them mine.`（全书无此句，`Ten thousand` 只在 ch09:153）、ch13 首行是破折号（实际首行是 `Chapter 13` 标题行）。我三章的 **md 文件里没有引用上述任何一句**（脚本反查：命中 0）。

## 四、并发事故（请总览层裁决）

- **同一 prompt 启动了两个 ne-g5 实例**：本方 `a1b211cc…`（21:37:13.540Z）与 `c4dbaed2…`（21:37:13.798Z），两者都领 ch11–ch13 ⇒ 同章双文件。
- 00:00–00:07 书目录内出现 `ch11 your own directory.md`（6 块）与 `ch12 the directory was mine.md`（8 块、导航 8 条，违「恰好 4 条」）；这两份**本方转录中从无写入记录**（Write/Edit 零命中，他实例转录 80／47 处提及）⇒ 归他实例。00:09 编排方已将其移入 `.memory/progress/ne-orphans/`。
- 本方三份 md 的 mtime 于 00:03 被外部改写一次，内容抽查无损（ch12 `| shrugged |` 行头词、`那座设施`、`her link to the Directory died`；ch13 `I was being told what to do.` 已恢复、`栽培`、`pain snapping us back to reality`；ch11 `记忆 flared`、`磕出淤伤`），复跑 `ne_strict.py --book` 仍 **FAIL 0｜WARN 0**。
- 若他实例再次向 `ne-g5.md` 落笔，本文件会再被覆盖：请把它并入本报告，或在 intake 里把 ch11–ch13 属主钉死。

## 五、合规自查

- 引语 0 处省略号、块尾均落句读边界；含多段的块其各段在原文相邻（`ne_strict` 检查项 2／3／4 三章全绿，故不再手列块号）。
- 分析层英文全部经本章 `text/` 逐字断言（`/tmp/ne_g5_pre.py`＋`/tmp/ne_g5_kw.py`＋`/tmp/ne_g5_tokens.py`）；跨章内容一律中文表述，不带引号。
- 词表由 `vocab_candidates.py --ch N --tiers` 粘贴后只做减法，释义纯中文；头词与例证列逐字复算（ch13 曾因 `snapped` 不在本章而换作 `snapping` 行）。
- 专名越界自查：三章分析层出现的专名（Aliers/Sable/LYREBIRD/Wylla/Sotain/Veonya/Fyster/Rahn/Sey/VisorForge/Order/Directory/Thorned Root/Subsidiary/BSMC…）逐一回查本章 `text/`，**零命中违例**。
- 计数断言全部 `str.count` 复算：ch11 `Veonya`=1、`mutiny`=1、`daemon removal`=1、`cheap echoes`=1；ch12 `Sable Veonya`=1、`Sable Alzian`=2（另含小写 `sable alzian`）、`Wylla`=4、`Sotain`=5、`invaluable`=1、`firewall`=1、`mnemonic parasite`=1；ch13 `Renata`=1、`General`=1、`girlfriend`=1、`bluff`=1、`Please,`=1、`Please!`=1、`Sable-wearing-LYREBIRD`=1、`hostile fusion`=1。
- 未执行任何 git 写操作；临时文件仅 `/tmp/ne_g5_*`（本报告尾部备份 `/tmp/ne_g5_report_tail.md`）。
