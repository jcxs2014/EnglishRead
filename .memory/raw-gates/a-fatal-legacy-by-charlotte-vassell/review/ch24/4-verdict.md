# ch24 判定表（R5）

> 审查员：独立审查（第 24 章）
> 落盘：`.memory/raw-gates/a-fatal-legacy-by-charlotte-vassell/review/ch24/`
> 顺序：R1 素读（`1-suread.json`）→ R2 机器层（`2-machine.json`）→ R3（`3-diff.md`）→ R4（`4-correspondence.md`）→ R5（本文件）
> 唯一权威源：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch24_24.txt`（7942 字符）

## 0. 覆盖声明

- **本章**：第 24 章《Priory Square》，`ch24 benedict opens his basement.md`。
- R1 素读：全章（22 条事件 + 12 条关系 + 15 条数字，全部带原文字符区间）。
- R2 机器层：全章（`bash scripts/chapter.sh … --json`，**退出码 0**，`verdict: ok`）。
- R3：全章三张单子。R4：7/7 块逐块人判。R5：逐条断言。
- **他章未做独立审查**——`ch21 / ch25 / ch27 / ch33 / ch48` 等仅作为**跨章取证来源**被引用（Alice 身份、五芒星唯一性），其本身**只有机器层或零核查**，不写「通过」。
- 覆盖门禁：`chapter.sh` 退出码 0（**0 ≠ 全绿无缺陷**，见下「机器绿≠无缺陷」）。

---

## 1. 四组数（只报这四组）

| 组 | 数 | 明细 |
|---|---|---|
| **逐字** | **7/7 引语逐字 + 27/27 词汇例句逐字** | 机器 `2-machine.json`：`quotes` 7 块全部 `ok:true`、`segment_miss:0`；人工独立复核：7 段引语在原文中**连续存在**、**无 `…` 拼接**（无省略号缝合风险）；词汇表 27 条例句逐条 `in text` 命中（0 miss） |
| **对应** | **7/7 块对应** | 引语选短 0 · 不对应 0 · 密度不足 0 · 施事/归属反转 0（详见 `4-correspondence.md`） |
| **形态** | **无偏离** | H1 `24. Priory Square`（`h1_shape_ok:true`）· 导航项 **5** 项（一句话概括／视角／线索结构／人物弧线／叙事手法）＝ 本书众数 `nav_counts:[5]`（每章均 5）· 子项集 **4** 项（中文理解／关键词／为什么这样写／读者视角提示）＝ profile `mystery-thriller` 的 4 项（可选「句子结构」未用）· 块数 **7** ＝ 本书众数 `block_median:7.0`（`block_range:[5,10]`）——**无偏离，故无理由行** |
| **断言** | **阻断 1 · 提示 11 · 假红 0 · 跳过 1** | 逐条见第 3 节 |

> **机器绿 ≠ 无缺陷**：唯一那条**阻断**（A-01）出现在导航/总结层的中文转述上——引语逐字、中文是中文、关键词成立、形态正常，四道机器探针全照不到；只有人判能抓。

---

## 2. 断言判定表

| # | 断言 | 证据（章:区间） | 结论 | 档位 |
|---|---|---|---|---|
| A-01 | `md:11` 导航「**第四次才被放进屋**」；`md:13` 线索结构「**按到第四次才进屋**」；`md:107` 一句话总结「**第四次才进得去**」（共 3 处） | `text/ch24_24.txt:20` "For the third time Caius rang the doorbell of Benedict Carr-Ridge’s town house. … **He rang for a fourth time.**" → `:23` "‘What the fuck do you want?’" → `:29` "**He slammed the door shut.**" → `:32` "**Caius rang the doorbell again.**" → `:35` "He looked **through the letterbox** at Caius" → `:41` "**He swung the door open** to reveal himself … beckoning him in." | **错（数字/时序）**：第四次按铃后他被骂、门被摔上；Caius **又按了一次**（第五次），经信箱口对话才被放进去。「第四次＝进门」与原文动作序列不符，且与 md 自己的块1 中文理解（`md:20`「他按响了第四遍」，正确）自相矛盾 | **阻断** |
| A-02 | `md:11,47,59`「**房东**」称 Benedict（3 处） | `text/ch24_24.txt:131` "I was told by the old lady **I bought the house off** in 1973"；`:113` "The land was then parcelled off to a loyal courtier. **His descendants still own my fucking leasehold.**"（取证：§4 命令 E，`landlord` 0 命中） | 关系称谓不符：Benedict 是**自住房的租赁产权持有人**，出租方（地主）是那位朝臣的后代。同一 md 的 `md:15` 又用「主人」，他章用「屋主／房主」 | 提示 |
| A-03 | `md:107`「**家具**、书堆、抽屉里的手稿**一样没动**」；`md:40`「进来的人**没有翻动任何东西**」 | 支持面：`text/ch24_24.txt:143` "**They didn’t steal that from me.**"、`:137` "‘**No, not that I’ve noticed.**’"、`:152` "all those manuscripts **in the drawer**"、`:44` 书堆仍在；反面：`:44` "a **pile of twelve hardbacks fell** in front of Caius"（书堆并非原样）；取证：§4 命令 D（`furniture` 0 命中，`drawer` 仅 `:152` 一处） | 「**没人偷东西**」这一层**成立**（本章专属判据达成，导航/块4/块6/总结四处口径一致）；但「**家具**一样没动」「**抽屉**没翻」是原文没有的具体化——原文只给出「没被偷」，家具二字全章无着落 | 提示 |
| A-04 | `md:40`「**墙边的书堆还堆着**」；`md:15`「**书堆原样**」 | `text/ch24_24.txt:44` "One wobbled as Benedict walked past and a **pile of twelve hardbacks fell in front of Caius**." | 与原文的「塌落」动作有张力；原文并未交代书堆在入侵前后是否被动过 | 提示 |
| A-05 | `md:59`「碑上所献的 Alice **正是**…那位被当作女巫烧死、据说能看见异象的修女」 | `text/ch24_24.txt:171` "For Alice and all the other women philosophers that we lost to the flames"（同章 `:119` "the madwoman they executed"、`:125` "some nun who had visions"；跨章 `text/ch33_33.txt:283` "**Alice de Burge**. … a young nun … **prophetic visions** … **burnt at the stake for heresy in 1532**"、`text/ch48_48.txt:262` "‘It could be **Alice de Burge**? … **The one with the blob statue in the middle of the square.**’"） | 断言**与全书一致**（跨章可证），但**本章内未建立**（本章从未把 Alice 与修女相连，也未称其为 philosopher）→ 宜改「也许就是」；**已列入「已核实为正确」，不得以「读着不对」为由改掉** | 提示 |
| A-06 | `md:46` 块5「**全案头一个画出来的符号**」 | 取证：§4 命令 A（`pentagram|pentacle` 全书仅命中 `text/ch24_24.txt:104,128` 与 `text/ch33_33.txt:237` 的回指） | 跨章断言成立 | 提示（已核实为正确） |
| A-07 | `md:32` 块3「这回**杜松子酒大概不合身了**」 | `text/ch24_24.txt:77` "I fell asleep again thinking that **unusually the gin hadn’t agreed with me**." | 语义误译：应为「这酒（这回）不对劲／不服身」；"不合身"（尺寸）属直译走样 | 提示 |
| A-08 | `md:26` 块2「「哦，**一位警司**。」」 | `text/ch24_24.txt:38` "‘**DI** Caius Beauchamp. I’m here about the break-in.’" | 职级渲染与本书不一致：全书他章一律「警探」（`ch21:11,51,52,99`；`ch34:11`；`ch37:12`；`ch41:14`；`ch46:24`；`ch52:85`；`00_概述.md:60`），中文语境「警司」通常指 Superintendent | 提示 |
| A-09 | `md:12` 导航·视角「随后在地下室**抬头**看见剥落的漆下露出的五芒星」 | `text/ch24_24.txt:104` "Caius asked, **looking at a mark on the wall** revealed by a layer of paint peeling away." | 「抬头」是原文没有的动作 | 提示 |
| A-10 | `md:11` 导航「后门大开…可屋里没有一样东西被拿走，**被打开的只是通往地下室的那道门**」 | `text/ch24_24.txt:83` "I woke up in the morning and **my back door was wide open** … but **it was flapping about and so was the door to my basement**." | 自相矛盾：同句已说后门大开，又说「只是」地下室那扇门被打开；原文是**两扇门都开着**（后门可由「我总忘锁」解释，地下室门才是反常）。同 md 的 `md:107`「后门与地下室的门都敞着」是对的 | 提示 |
| A-11 | `md:28` 块2「于是警察在他眼里**先是同道**，不是麻烦」 | `text/ch24_24.txt:41` "‘**I am important.** Oh **and** a detective who reads quality literature. Well, I never. I suppose you may enter.’" | 原文顺序＝先摆自己的重要地位、再提对方读不读得出好东西；md「先是同道」把次序倒置（不影响施事归属） | 提示 |
| A-12 | `md:12` 导航·视角「本章属「**五月的星期三**」这一分部」 | 分部证据：本书同分部他章均作「在分部「**A WEDNESDAY IN MAY**」里」（`ch21:11`、`ch25:11`、`ch27:11`）；`text/` 内无分部标题行（`/usr/bin/grep -rniE "wednesday in may" text/` → 0 命中），故分部名以本书既有 md 用法为准 | 分部归属**正确**（A WEDNESDAY IN MAY），但标签写法与本书多数章（英文大写原名）不一致；`ch18:11` 有中文先例「五月的星期二」 | 提示 |
| A-13 | `md:107`「一个自认「重要人物」的**落魄作家**」 | `text/ch24_24.txt:41` "‘I am important.’"；`:62` "The literary spat that **ended Benedict’s career** came back to him."；`:143` "Only thirty years’ worth of manuscripts." | 「自认重要人物」逐字有据 ✓；「落魄」为概括性修辞，未与原文冲突 | 通过（措辞可接受） |
| A-14 | 漏：`text/ch24_24.txt:98` "**That much paper was highly flammable.**"、`:44` "a **pile of twelve hardbacks fell** in front of Caius"、`:131` "**performed seances down here**"、`:98` "‘You think the **wannabe burglar** came down here?’" | 见 `3-diff.md` L1–L5 | 伏笔/细节漏引（**非情节转折，不判阻断**）：其中「纸太多极易燃」与末段献辞 "we lost to the flames" 构成现成呼应，md 两处都提到 flames 却未把「易燃」接上 | 提示 |
| A-15 | 假红候选：`chapter.sh` 全绿 → 本章无缺陷 | `2-machine.json`：`verdict:"ok"`、`counts:{segment_miss:0,struct_bad:0,empty_quote:0,keyword_bad:0,cjk_low:0}` | **不成立**：机器绿只覆盖它读的那一层（引语英文逐字 / 中文是中文 / 关键词成立 / 形态正常），A-01 恰在其覆盖范围之外 | 假红（对「机器全绿=无缺陷」这一推论） |

---

## 3. 四组数的计数口径

- **逐字**：分母＝7 个引语块 + 27 条词汇例句，合计 34/34。
- **对应**：分母＝7 块；「对应」= 7；其余三类各 0。
- **形态**：分母＝4 项（H1 / 导航项 / 子项集 / 块数）；偏离 0。
- **断言**：分母＝15 条已判定断言（A-01…A-15）；**阻断 1 · 提示 11 · 假红 1 · 通过 1 · 跳过 0**（A-14 含 4 条漏引细节，合并计 1 条）。

---

## 4. 取证三件套（凡「零命中／查无」类断言必须自证）

```
取证命令：/usr/bin/grep -rniE "pentagram|pentacle" text/ > /tmp/o1 2>&1; echo "exit=$?"
         → exit=0；命中 3 行：text/ch24_24.txt:104、text/ch24_24.txt:128、text/ch33_33.txt:237
         （即：五芒星只在 ch24 出现，ch33 为回指 ⇒ A-06「全案头一个画出来的符号」成立）

取证命令：/usr/bin/grep -rnwi "Alice" text/ > /tmp/o2 2>&1; echo "exit=$?"
         → exit=0；命中 5 处：text/ch24_24.txt:171、text/ch33_33.txt:283、text/ch46_46.txt:219、
                             text/ch48_48.txt:262、text/ch52_52.txt:239

取证命令：/usr/bin/grep -rn "Alice de Burge" text/ > /tmp/o3 2>&1; echo "exit=$?"
         → exit=0；命中 4 行（含 ch33:283 的 "Alice de Burge … burnt at the stake for heresy in 1532"
                             与 ch48:262 的 "The one with the blob statue in the middle of the square"）

取证命令：/usr/bin/grep -n "furniture\|drawer\|furnitur" text/ch24_24.txt > /tmp/o4 2>&1; echo "exit=$?"
         → exit=0；仅 1 行：:152 "… Send your editor all those manuscripts in the drawer. …"
         （furniture 0 命中 ⇒ md 的「家具」二字在原文无着落；抽屉只此一处，且只说手稿在抽屉里，
           全文没有任何一句写「抽屉没翻」⇒ A-03 的依据范围到此为止）

取证命令：/usr/bin/grep -nE "landlord|leasehold|courtier" text/ch24_24.txt > /tmp/o5 2>&1; echo "exit=$?"
         → exit=0；仅 1 行：:113 "… His descendants still own my fucking leasehold."
         （landlord 0 命中 ⇒ 原文没有把 Benedict 写成出租方，A-02 成立）
```
（工具口径：显式文件路径 + `/usr/bin/grep`（BSD grep 2.6.0-FreeBSD, GNU compatible），交替匹配用 `-E`、查单词用 `-w`；**未用 `git grep`/rg**——`text/` 被 `.gitignore` 排除（`notes*/books/**/text/`），在那两个工具上恒为零命中。）

---

## 5. 已核实为正确（防误修 · 固定节）

> 下面各条**看起来像错**，回原文核对后**成立**；后续任何人不得以「读着不对」为由改动，除非能给出反证。

1. **「Alice 正是那位修女」（`md:59`）** — 成立。`text/ch33_33.txt:283` "One of the priory’s most infamous inhabitants was **Alice de Burge**. She was a young nun … supposedly blessed with **prophetic visions** … **burnt at the stake for heresy in 1532**"；`text/ch48_48.txt:262` "‘It could be **Alice de Burge**? The nun who was burnt for heresy during the Reformation. **The one with the blob statue in the middle of the square.**’" ⇒ 碑上 Alice ＝ 广场雕像那位疯修女。**章内未建立**只是叙述时点问题，不是错误。
2. **「全案头一个画出来的符号」（`md:46`）** — 成立（取证命令 A）。
3. **块6「他们没能从我这里拿走这些」（`md:50`）** — 成立。`text/ch24_24.txt:143` "**They** didn’t steal that from me. **Martin fucking Amis did.**" ⇒ 被偷者＝Benedict，未被偷者＝手稿/生涯；Amis 拿走的是生涯不是稿子。**md 的施事方向正确，勿改成「Amis 没偷走手稿」之类**。
4. **块3「正是你现在坐的那把」（`md:32`）** — 成立。`text/ch24_24.txt:77` "I fell asleep in my chair. **The very one you’re sat in now.**" ⇒ 第二人称指向 Caius（当时正坐在这把椅子上），md 用「你」指 Caius 正确。
5. **块5「也许 Matt 说得对」（`md:44`）** — 成立。`text/ch24_24.txt:104` "**Maybe** Matt was right and the goths of Camden were really involved…" ⇒ md 保留了原文的「也许」，**勿删「也许」改成肯定**。
6. **块7「Callie 指给他看过」（`md:56`）** — 成立。`text/ch24_24.txt:183` "He only knew they were fritillaria because **Callie had pointed them out** at some point during a Sunday morning stroll around Regent’s Park." ⇒ 归属方向是 Callie → 指给 → Caius，**勿倒过来**。
7. **块4「后门则是他历来不上锁的那一扇」（`md:40`）** — 成立。`text/ch24_24.txt:83` "**I forget to lock the damn thing all the time** but I wouldn’t leave it like that."。
8. **献辞逐字（`md:13,58`）** — 成立。`text/ch24_24.txt:168-173` "In memoriam / For Alice and all the other women / philosophers that we lost to the flames" ⇒ md 的引号内文字与铭牌逐字一致（含分行导致的 "women / philosophers" 断行）。

---

## 6. 修复建议（不改 md，只给写法；本会话**未改书目录任何文件、未 git add/commit**）

1. **必改（A-01 阻断）**：`md:11`、`md:13`、`md:107` 三处「第四次才被放进屋 / 按到第四次才进屋 / 第四次才进得去」
   → 改为「**第四次按铃仍被拒，Caius 又按了一次，第五次才被放进屋**」一类表述。
2. 宜改（A-02/A-03/A-04/A-10）：「房东」→「房主」；「家具、书堆、抽屉里的手稿一样没动」→「一样东西也没被拿走」；删「书堆原样／还堆着」或改「墙边的书还在」；导航「被打开的只是通往地下室的那道门」→「唯一反常的是通往地下室的那道门」。
3. 宜改（A-05/A-07/A-08/A-09/A-11/A-12）：Alice 那句加「也许」；「不合身」→「不对劲」；「警司」→「警探」；删「抬头」；「先是同道」调序；分部标签统一为「A WEDNESDAY IN MAY」。
4. 宜补（A-14）：块4/块5 补引「That much paper was highly flammable」与「a pile of twelve hardbacks fell」，把「易燃」与献辞的 flames 接上。
