# ne-g4 交付报告（Null Entity 精读写章 · 组前缀 ne-g4）

书目录 `$BOOK = /Users/jcxs2014/Documents/Works/EnglishRead/notes/books/novels/null-entity-by-seth-haddon`
本组原始派单：ch09–ch10；会话中被逐步扩到 ch09–ch23。报告分两部分：**本组落盘的章**（ch09/ch10）与**扩范围部分的处置说明**（ch11–ch23，见第五节）。

## 一、交付与自检（阻断数）

| 章 | 文件 | 块数 | 章长（`text/` strip 后字符／去空白字符） | ne_strict（带 `--book`） |
|---|---|---|---|---|
| ch09 | `$BOOK/ch09 ten thousand masks.md` | 8 | 13,596／11,134（长章→8 块合规） | FAIL 0｜WARN 0 |
| ch10 | `$BOOK/ch10 the cargo wing.md` | 8 | 11,568／9,522（长/中边界，8 块在两种判读下都合规） | FAIL 0｜WARN 0 |
| ch11 | `.memory/progress/ne-orphans/ch11 your own directory.md` | 6 | 6,575／5,355（中章→5–8 合规） | FAIL 0｜WARN 0（现为孤儿件，见第五节） |
| ch12 | `.memory/progress/ne-orphans/ch12 the directory was mine.md` | 8 | 7,518／6,092（中章→5–8 合规） | FAIL 0｜WARN 0（现为孤儿件，见第五节） |

另加两道自检之外的自证：
- **写前断言**：每条引语/作证据的英文片段先跑 `/tmp/ne_g4_assert.py`（`q in src` + `q[-1] in '.?!"’”'`）才落盘。
- **落盘后复扫**：`/tmp/ne_g4_fragcheck.py` 把四份 md 的**分析层**（非 `>` 行、非表格行）里的全部 ≥2 词英文片段逐条测 `frag in src`（精确子串，不用扁平近似）——四章均 **misses 0**。

## 二、本轮审计后自纠的缺陷（全部为真实违例，已改）

ch09（7 处）
1. 导航「月面基地」→「据点」：`moon` 全章仅 1 次命中（ch09:57，且是“我”的问句），其回答是 ch09:60 `Not quite.`，语意指向模糊；`base/station/hangar/dome` 均 0 命中。
2. 导航「在 “Why do you need me?” 之后答出 “Yes.”」→ 按实际顺序改写：`Yes.`（ch09:258）在切通讯（261）**之前**，`Why do you need me?` 在 267，第二个 `Yes.` 在 288。
3. 块1 读者提示「本章后半注视越来越失焦」（无据）→ 换成本章自证句 `my focus kept slipping to Aliers`（ch09:24）。
4. 块1「修道院与民兵的合体」→ 补本章判词 `part monastery, part militia`（ch09:27）。
5. 叙事手法行的独立短段清单：原写 `Fuck.` / `Well—losing you.` —— 二者都**不是**独立段（分别在 ch09:36、300 的长段内）；改为真正独立成段三行 `Not yet.`（69）/ `Of course she does.`（177）/ `“Yes.”`（288）。
6. 块7 违例引语 `Break a mind into…`（省略号）→ `Break a mind into skills`；「第 8 章前后『面具即商品』」→ 改指第 1 章（见第三节）；「本章后文还会出现 suppress the prefrontal cortex…」→ 改「同一段落紧接着」（三者同在 ch09:171 一段内）。
7. 块8 「“Deal”这个字在上一章是两人的暗号」→ **删**：ch07 `deal` 0 命中，ch08 仅 `idealist` 含该子串，无暗号用例。
8. 块6 姿态清单里的裸词 `She shrugged`（与本章句首大小写不配套、易被当转写）→ 换成 `eyes narrowed`（ch09:201），并把「每次投喂都配一次姿态」软化为「反复配姿态动作」。

ch10（4 处）
1. 导航 `All thought drained away…`（省略号）→ 完整两句 `All thought drained away, all purpose collapsed` / `And the barrels of six blasters.`。
2. 块1 读者提示「五名士兵」→ 补本章自证 `Aliers had brought five`（ch10:57，含 2+1+2 分工）。
3. 块5 读者提示「本章内 Aliers 立刻接上『I thought you said no one had been here in three days?』」→ **双重错**：该句在 ch10:120，位于终端段（171/183）**之前**，且说话者是“我”（117 撞见灯亮 → 120 质问 → 123 Aliers 才拔枪前压）。改为「终端之前“我”就撞见同一类矛盾」。
4. 块3 「第三次强调」计数断言不可复现 → 改为非计数表述。

ch11（5 处，现存孤儿件内已修）
1. 导航「只有第 9 章的警告被验证：Thorned Root was burning itself out」→ **误归章**：该句在 ch11:126（本章），且 ch01–ch10 无对应原话（`burning itself` 全库仅 ch11:126 命中）。改为直引本章原句、不指认出处章。
2. 导航「为后文两人的牺牲埋线」→ 后文赴死的是 Rahn 与 **Sira**（ch20:78、ch21:36），Sey 在 ch16:27、ch17:93 仍在场；且 `Sira` 未出现在 ch11 原文（禁名规则），故改「为后文他自己的牺牲埋线」。
3. 块3「花瓣从何人身上掉落，本章没写」→ 本章其实给了相邻证据（ch11:45 `monstera leaves at his neck` → 48 `Petals scattered`），改成「相邻两行说完，不给解释」。
4. 块4 读者提示「本段紧接一段记忆闪回」→ **方向反了**：闪回 ch11:81 在结论 84、质问 87 **之前**。改为「画面→结论→质问」并给出三处原文。
5. 块5 读者提示「她曾把 Aliers 说的“it required living tissue”当成在谈理想」→ 该话的**原始场景不在任何一章正文**（`living tissue` 仅 ch11:99 回忆式、ch12:165 再述），改为直引 ch11:99 两句；并补 `voice cracked`（ch11:69）作 Rahn 愤怒的实证。
6. 块6「fever 呼应她的士兵 burning itself out 的体质」→ 原句主语是整个 Thorned Root（ch11:126），不是士兵体质；改为直引该句。

ch12（2 处，现存孤儿件内已修）
1. 块5 的中文理解被我写成两行、第二行以 `> ` 开头 → ne_strict 把它当**引语**判 2 条 FAIL（`太多了。` 非原文子串＋末字不在句读集）。改为段内中文。**自检机制提示**：`^> ` 在精读块内一律按引语解析，中文换行绝不能带 `> `。
2. 块1 读者提示「后文她冲过去戴它」无据（本章只有 ch12:153 `You probably need to put it on your head` 的提议与 156 的前提）；块7 读者提示「Aliers 在第 10 章就借 Veonya 试探」保留（已核 ch10:96/99/102 的说话人链）；「It’s called…」省略号 → 补全为 `It’s called LYREBIRD MARK II PRIME`；「为何知道 Facility」的裸词 Facility 不在 ch12 原文（0 命中）→ 改中文「那座设施」；块5 读者提示「早于第 1 章…很多年」→ 书内无年数，删「很多年」。

## 三、跨章指涉：当场 grep 的行号（只列写进 md 的）

指涉 ch09 的（本组 ch09/ch10/ch12 用到）
- ch09:51 `“Informants.” She shrugged` ← ch10 块1 用 `wrung` 承接。
- ch09:78 `Rhizomes were stems growing horizontally, putting out lateral roots` ← ch10 块5 用「横着生长」+ `lifted`（ch10:183）。
- ch09:114 `They burned out in days. Except Sable Alzian.` / ch09:120 `her mind survived intact` ← ch09 块5、ch12 块3「幸存例外」。
- ch09:126 `the mind can be seized, preserved, redeployed`（在 ch09:93 `fused` 之后）← ch09 块4 读者提示的「后滑向工业术语」。
- ch09:171 同段：`skills, reflexes, obedience` / `ten thousand masks bound for the Syndicate` / `suppress the prefrontal cortex` / `trick the amygdala and hippocampus` ← ch09 块7 两子项、ch10 块7「模块化」。
- ch09:219 `Early volunteers gave neural patterns` ← ch11 块5「志愿者」回收。
- ch09:249 `Don’t go down there.` / ch09:261 `severed the comm` ← ch09 块8、ch10 全章单向通讯、ch12 块6 读者提示。

指涉 ch01 的
- ch01:18 `replies bloomed across the message board`；ch01:226 `Green crept in from the edges`；ch01:235 `Those words grew from moss over the screen` ← ch09 块1 的植物链。
- ch01:57 `The small-time mask manufacturer Auntie Donnelly had been absorbed…`；ch01:63 `Cheaper masks, now with the VisorForge guarantee.` ← ch09 块7「面具即商品」（md 内只用中文转述，不越章搬英文）。
- ch01:72 `the contract we’d salvaged from my dead husband’s ship` ← ch12 块4 读者提示的「Fyster 与 tester 是两人」前提。

指涉 ch10 的（ch12 用）
- ch10:96 `“It’s this way,” I said` → ch10:99 `“Veonya says that?”` → ch10:102 `I didn’t answer, but she took me at my word`（说话人链证明是 Aliers 在试探名字归属）。

指涉 ch11 的（ch12 用）／指涉 ch12 的（ch11 用）
- ch11:108 `But it’s brittle. Skills degrade… rejects the graft` ← ch12 块3「排异清单」。
- ch12:15 `“It’s called LYREBIRD MARK II PRIME.”`（本章第一段）← ch11 块6「下一章开头给名字」。

指涉 ch13 的（ch12 用）
- ch13:15 `Renata Aliers’s mind was full of thorns.`（正文第一句）/ ch13:18 `I could sense the garden in her` / ch13:33 `We were strapped to the rig` ← ch12 块8 读者提示的「荆棘园扫描」与衔接点。

指涉 ch20/ch21 的（审计 ch11 时核，未写进 md 名）
- ch20:78 `“Do it now.”` / ch21:36 `Rahn and Sira’s sacrifice had stripped the field down to Prime alone.`

计数类（可复现，已写进 md 或供总览层用）
- `upload`/`download`：ch01–ch08 逐章 grep 命中 **0**，ch09 起于 114 → ch09 块5「本书此前从未露面」成立。
- `burning itself`：ch01–ch23 仅 ch11:126 一处。
- `living tissue`：仅 ch11:99、ch12:165 两处，均为回忆/转述，原始场景不在正文。
- `Three major records appeared:`（ch10:171）→ ch10:174 / 177（`CY 339.260`）/ 180 三条全大写记录，ch10 导航「三条全大写记录」由此而来。
- ch10:57 自数 `Aliers had brought five`（2 grunts + 1 sweep + 2 grafters）+ Aliers + “I” = ch10:18 `Seven of us`。

## 四、不敢下判断清单（总览层请照此收口）

1. **I／you 的名分**：ch09:252 Aliers 直呼 `Sotain`、ch12:79 `I would never hurt you, Wylla`、ch12:177 `I can kill Wylla Sotain’s body` 可证「you＝Wylla 的身体/本人」在本章层；但 Veonya／Alzian／Sotain 三个名字在“I”身上的**归属次序**书内没定论（ch09:117 只是“I”的口头纠正）——总览层不要写成已决。
2. **ch09 据点的地理**：是否 moon 上（ch09:57→60 的 `Not quite.` 语义两可），本组已回避，只写「据点/观测舱」。
3. **ch10 七人的构成**：`Seven of us` 与 `brought five` 可加合，但 Rahn/Sey 是否在那五人之内无文本直陈（分工名单 Maris/Ivara/Joril 在 ch10:78，Rahn/Sey 在 ch10:219 才与“我们四人”同框）。
4. **ch11 花瓣**：与 Rahn 的 `monstera leaves` 只相邻、无因果句，任何「花瓣即从他身上磕下来」的断言都超出原文。
5. **ch11:126 `You’d been right, Wylla`** 回指的是哪一次警告：前八至十章无对应原话——不可写成「第 9 章的警告兑现」。
6. **ch12 闪回的年代**：距 ch01 多久、Fyster 之死与谋杀 tester 的先后年数，书内无数字。
7. **Rahn 的后续牺牲对象**：是 Rahn+Sira（ch20/21），不是 Rahn+Sey；Sey 在 ch16 仍活着、ch17:93 留下 `Sey’s parting gift`（其下场本章未写明）。
8. **「Wylla 在场/缺席」的表述**：身体在场、意识被切走（ch09:261 切通讯、ch12:159 之后 Aliers 以那具身体要挟）——写「缺席」须限定为「没有台词/无法回应」。
9. **ch09 “Deal” 是否为旧暗号**：无据（已删），别在总览里恢复。

## 五、扩范围部分（ch11–ch23）的处置

- 本组按扩后的范围落了 ch11、ch12 两份 md；随后编排方并行派单 g5（ch11–13）、g6（ch14–15）、g7（ch16–18）、g8（ch19–20）、g9（ch21–23）也在同一时段落盘。00:03–00:09 的外部整理把本组 ch11/ch12 移入 `.memory/progress/ne-orphans/`，`$BOOK` 内保留 ne-g5 的 `ch11 cheap echoes of me.md`／`ch12 like knows like.md`。
- 本组**没有**再往 ch11–ch23 落任何文件（避免三份同名章并存的第三次撞车），也**没有**改动他人章节文件。现 `$BOOK` 为 ch01–ch23 各 1 份。
- 全量复跑（只读）：`ne_strict.py <md> --book "$BOOK"` → ch01–ch23 **23/23 均 FAIL 0｜WARN 0**（块数依章序 8/8/8/8/6/8/7/8/8/8/8/8/6/8/8/8/8/8/8/5/7/8/4）。
- 顺带核到一条**报告层面的事实更正**：`ne-g5.md` §3.7 称孤儿件 `ch12 the directory was mine.md`「导航项 8 条（违恰好 4 条）」。实测该文件 `^- \*\*` 命中 **4**（合规）；8 应是把精读块内四子项抬头一起计入。留此以免总览层误判孤儿件格式。
- 已抽查 ne-g5 现行 ch11/ch12 的跨章句：其「上一章最后写四人从对接闸门进入…」经核为真（ch10:219 `…join us at the docking airlock. The four of us…`），其 ch12 末尾「下一章」句亦与 ch13:33 相符。本组未发现需要在现行件上追加的阻断项。

## 六、合规声明

- 无 git 写操作（未 add/commit/stash），只跑过只读 `git status`／`git log`。
- 写入范围：`$BOOK/ch09 ten thousand masks.md`、`$BOOK/ch10 the cargo wing.md`、`.memory/progress/ne-g4.md`（本报告）；ch11/ch12 两份为扩范围期间的产物，现由整理方安置于 `ne-orphans/`，本组未再触碰。
- 临时件均在 `/tmp/ne_g4_*`（`ne_g4_assert.py` 写前断言器、`ne_g4_fragcheck.py` 落盘后英文片段复扫器、`ne_g4_vocab_ch09…ch23.txt` 词表候选原始输出）。
- 词表生产：全部 `python3 scripts/vocab_candidates.py "$BOOK" --ch N --tiers` 输出粘贴后**只做减法**，释义纯中文、无词性前缀；表头三档齐全（某档不足则该档留空或 2–3 行）。
