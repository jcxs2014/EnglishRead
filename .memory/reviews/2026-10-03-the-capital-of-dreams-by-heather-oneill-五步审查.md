# 《The Capital of Dreams》独立五步审查 — 缺陷清单与整改记录

- 书籍：`notes/books/novels/the-capital-of-dreams-by-heather-oneill/`（Heather O'Neill，2024，HarperCollins；37 章精读 + 3 篇总览）
- 触发：用户主动发起（m01600）「先完整读 AGENTS.md 第 10 条 + `docs/新书启动模板.md` 五步法节，回执三项后开始审查」
- 执行依据：`AGENTS.md:260` 触发条件 + `AGENTS.md:264-266` 同会话执行纪律；`docs/新书启动模板.md:706-710` a–e 五小标题
- 口径：**a–e 全部完整执行，不降级、不自我豁免**；同会话盲区只在「结论与局限」一节标注
- epub 位置（本书特殊）：`<书目录>/library/The Capital of Dreams (Heather ONeill) (Z-Library).epub` ⇒ **完整 lane**
- 体裁：小说（版权页 `LCGFT: Fantasy fiction. | LCGFT: Novels.`；标题页 `a novel`）

---

## a. 第 3 条提交门禁全量重跑（不信报告数字）

原始逐行输出（两跑，见下）：

- 首跑：`.memory/raw-gates/the-capital-of-dreams-by-heather-oneill/2026-10-03-审查-a-门禁全量重跑.txt`
- 整改后：`.memory/raw-gates/the-capital-of-dreams-by-heather-oneill/2026-10-03-审查-e-整改后门禁全量重跑.txt`

| 检查 | 首跑 | 整改后 |
| --- | --- | --- |
| `verify_quotes` | 807/807（100%）；干净 39/39 | **787/787（100%）；干净 39/39** |
| `verify_quotes --full` | 整串取证 0 | 整串取证 0 |
| `check_vocab` | 词条行 1189 ｜ FAIL 0 ｜ WARN 55 | 1189 ｜ FAIL 0 ｜ WARN 55 |
| `check_entities` | 0 个文件存在未知实体 | 0 |
| `corruption_scan` | FAIL 0 处 / 报告 0 处 | FAIL 0 / 报告 0 |
| `sweep_full` | ✅ 773 ｜ 跨章 0 ｜ 🔶 0 ｜ ❌ 0 | ✅ 753 ｜ 跨章 0 ｜ 🔶 0 ｜ ❌ 0 |
| `check_short_quotes` | ✅ 36 ｜ 别章 0 ｜ 🔶 0 ｜ 🔧 0 ｜ ❌ 0 | 同左 |
| `check_quote_blocks` | ✅ 720 行 / 37 文件 | ✅ 720 行 / 37 文件 |
| `check_chapter_quotes`（37 章） | 37/37 全 773/773（100%） | 37/37 全 773/773（100%） |
| `verify_overview_quotes` | 38/38（100%）；干净 2/2 | 38/38（100%）；干净 2/2 |
| `check_block_keywords`（⑱） | 117 处 | **78 处**（拼接红线仅 1 处假红，余 77 处模板不匹配） |

> **条数下降说明（非引语丢失）**：`verify_quotes` 807 → **787**、`sweep_full` 773 → **753**，差额 **20** 正是 d 步第二轮把 20 个 ` / ` 拼接块拆为规范多段块所致——**同一块内的 ` / ` 两侧原本被计为 2 条引语，拆分后仍是一条块内的两个自然段**，故独立「引语条目」计数减少而实际文本一字未少。修后 787/787 与 753/753 仍为**全绿**。

**★ a 步首跑即暴露一处工具盲区（真实教训）**：我第一次调用 `verify_quotes.py "$BOOK" "$BOOK/The Capital of Dreams - Heather O'Neill.epub"` 时**凭记忆拼 epub 路径**，脚本报「❓ 无法判定：epub 不存在」并**按降级 lane 处理**。真实路径在 `<书目录>/library/` 下且文件名不同。**教训：epub 路径必须 `ls` 实测，不得凭印象拼；「降级 lane」提示可能是路径错而非真的缺 epub。** 修正后为完整 lane。

**a 步结论：门禁全绿，无内容缺陷。** WARN 55 全为「基础档疑含超纲词」提示型（`check_vocab` 设计如此，不判红）。

---

## b. 逐章归属

原始输出：`.memory/raw-gates/the-capital-of-dreams-by-heather-oneill/2026-10-03-审查-b-逐章归属汇总.txt`

- **37 章逐一** `check_chapter_quotes.py <NN> "<md>" --book-dir "$BOOK"`：**每章均** `全章扫描: 解析引语块 773，命中本章 773（100%）` + `✅ 全部引语均归属正确章节`，零未过。
- 与写作时**不同路径**复核（模板 `:707` 要求）：写作期用的是 `sweep_full`（全书 flat 比对），本次改用 `check_chapter_quotes`（按章切分归属），两条实现独立。
- 总览层：`verify_overview_quotes` **38/38（100%）**，干净 2/2（`00_情感节点.md` 14/14、`00_金句精选.md` 24/24、`00_概述.md` ➖ 无引语行，属设计允许的散文体）。
- `check_overview_full`：A 整串命中 46 / 🔶0 / ⚪0 / ❌0；B 章节标签 对 36 / 不符 0 / 无标签未判 10；C 跨章多重命中 0；E H1 语义错配 0；F 0/0。

**b 步结论：无跨章错配。**

---

## c. 结构扫描

原始输出：`.memory/raw-gates/the-capital-of-dreams-by-heather-oneill/2026-10-03-审查-cd-结构扫描与第二实现.txt`

| 检查 | 结果 | 定档 |
| --- | --- | --- |
| `check_quote_blocks`（块结构权威） | ✅ 前缀完整 · 编号连续无撞车 · 无孤儿分析 · 无自查泄漏 | 干净 |
| `audit_structure` | 62 条「孤儿块」+ 多处「引语 N 个与众数 10 相差过大」 | **假红** |
| `check_block_keywords` | 117 条 | **假红 116 条**（拼接红线 1 真 + 模板不匹配 77，余 38 为早期残留，见「d 步第二轮」） |
| `check_struct_indep`（第二实现） | ❌ 37 条「引语块 N 个，超出 3–8 配额」 | **假红（模板不匹配）** |
| 空段扫描（内嵌 `gate.sh`） | **7 处** | **真缺陷，已修** |

### c 步真缺陷：`ch31`–`ch37` 导航项不足（7 处）

- 判据（`scripts/gate.sh:73-143` 内嵌 python，三条之一）：导航节须 ≥4 个 `**X**：正文` 粗体项且每项有正文。
- 实测：`ch01`–`ch30` 每章导航节均为 **4 项**（`- **一句话概括**：` / `- **情感弧线位置**：` / `- **人物弧线**：` / `- **叙事手法**：`），而 `ch31`–`ch37` 只有 `一句话概括` 一项，另外三项被**内联揉进了那一句话概括的长段落里**。
- 修法：在 `- **一句话概括**：` 行后各插入三条，内容按各章实际撰写（非模板套话）。
- 修后：逐章计数**全部为 4**；`gate.sh` 空段扫描报 `=== 空段扫描：0 处 ===`。

### c 步假红的技术根因（务必记入工具认知）

- **`audit_structure` / `check_block_keywords` 同一根因**：`scripts/audit_structure.py:57-59`
  `RE_QUOTE_BARE = re.compile(r'^\s*>\s*(?!\*\*)(?![一-鿿])(.+?)\s*$')`
  —— **每个 `>` 续行都被当成一个独立引语块**，于是任何用空行 `>` 分隔的多段引语的每一段都被算作「孤儿块」。脚本逐条自验：`多段引语的续行（假红）: 62 ｜ 真孤儿: 0`。
- 全书分布：ch13 1 / ch14 3 / ch15 3 / ch17 2 / ch18 4 / ch19 6 / ch20 1 / ch24 3 / ch27 3 / ch29 12 / ch30 15 / ch31 8 / ch37 1。
- `check_block_keywords` 的「引语跨自然段（拼接红线）」条——**我起初据「`> **原句 N:**` 是单行，写不进段落分隔符 `\n\n`」判定为防御性守卫、结构上不可触发，这是错判。第二轮实读实现（`scripts/check_block_keywords.py:21` docstring「引语只来自一个自然段（跨段拼接红线）」、`:260` 输出行）并构造反例后确认：多段引语用 ` / ` 或块内续行写成后，逐段落在不同自然段，**该判据完全可触发且实际抓出 20 块 ` / ` 拼接 + 6 块截断/伪引号**（详见「d 步第二轮」节）。**真防线另有 `sweep_full` 的 🔶 通道（本题 0）。**
- 「引语块 N 个，超出 3–8 配额」与「关键词行 0 ≠ 引语块 N」均为**模板不匹配**：本书按 ch01–ch30 确立的形态写（10 处/章，`ch21` 43 块、`ch27` 63 块），且本库格式里根本没有 `关键词` 行。
- **纪律**：AGENTS 8.4 已把 `audit_numbers`/`sweep_analysis_inline`/`check_anchor`/`audit_structure` 四个脚本降为**抽查**；**判定任何门禁报警前必须先读脚本实现的判据正则**，再决定真缺陷还是假红。

### c 步提示型（只记不改）

- `audit_structure` ⚠️：`ch29` 4/68、`ch30` 1/55「块子项少于同书主流」——**经独立复核不成立**：`ch29` 实为 **52 块**（非 68），三子项 52/52/52；`ch30` 实为 39 块，子项齐全。
- `ch10 babes in the woods.md:79` 出现 `A Naked Girl Is Always Priceless`（ch12 章标题）——**合法前瞻交叉引用**。

---

## d. 语义二审（全部引语↔分析逐对核对）

按模板 `:709` 要求，**不做抽样**。全书 **37 章 / 720 个引语块**分五批交由**五个独立子代理**逐块核对（每批约 120k–150k 字符，附真实失败案例 + 防幻觉条款）：

| 批 | 子代理 | 范围 | 块数 | 阻断型 |
| --- | --- | --- | --- | --- |
| 1 | `c2ca54c0-f1cf-47f6-85b0-0b59f4c4d0ba` | ch01–ch18 | 180（每章恰 10） | 2 |
| 2 | `b876cd28-858b-419b-81a2-1c1435085ea6` | ch19–ch25 | 195 | 0 |
| 3 | `064a32bb-098a-44ac-957d-19377fbdde5e` | ch26–ch29 | 158 | 2（+1 假红） |
| 4 | `996b0e99-1367-4985-a5cb-114196ba245a` | ch30–ch35 | 162 | 4 |
| 5 | `971b9ce3-a538-42e0-9145-2c124309b2ee` | ch36–ch37 + 总览三篇 | 42 + 三篇 | 3 |

合计 **737 块**逐块核对（720 章的块 + 总览层金句 24 / 节点 14 / 概述 106 行）。

### d 步阻断型缺陷与整改（共 11 条，全部已修并回源复核）

| # | 位置 | 缺陷 | 依据（原文逐字） | 修法 |
| --- | --- | --- | --- | --- |
| 1 | `ch02 the childrens train.md:12`（导航 `**人物弧线**`） | 改写冒充逐字 | `text/ch02_the_children_s_train.txt:145` `Instead she ran away from the world of adults.` | 改回 `Instead she ran away from the world of adults` |
| 2 | `ch02 the childrens train.md:77`（`**为什么这样写：**`） | 同上 | 同上 | 同上 |
| 3 | `ch06 a cat named napoleon.md:10`（导航） | 情节方向写反：写「**进城**探望祖母」 | `text/ch06_a_cat_named_napoleon.txt:13` `they were going to the country to visit her grandmother, who still resided in the large rural childhood estate.` | 改「**下乡去庄园探望祖母**」 |
| 4 | `ch06 a cat named napoleon.md:87` | 人物归属错：把 Clara 的反问安给祖母 | `:229` 祖母劝留下 → `:232` **Clara 反问** `If you are so convinced that the trees will protect us, then why in the world are you leaving the country?` → `:235` 祖母作答 → `:238` Clara 再说 | 改「**Clara 那句**…随后戳破了**祖母的**说辞」 |
| 5 | `ch23 handcuffs made of smoke.md:213` | 引号内改写 | `text/ch23_handcuffs_made_of_smoke.txt:121` `they knew they had to let this motherless child go.` | `had to let her go` → `had to let this motherless child go` |
| 6 | `ch24 the price of tears during wartime.md:217` | 自我否定病句（「会明确提到中国人…——没有」） | ch24 为虚构 Elysia 设定，`:34` 只有 `in any country` | 整句改纯中文：「请注意本章只说她"在她的国家"，未指明具体国族」 |
| 7 | `ch26 i heard the icicles singing.md:205` | 分析层引语非逐字 | `contentment` 在 ch26 源文 **0 次**（仅 ch21 有）；`:134` `She felt so content, it was troubling.` | `contentment 本身就是可疑的` → `content 本身就是可疑的` |
| 8 | `ch31 put a red rose in my buttonhole.md:458` | 时序错（把次日早晨的事写成夜里） | `text/ch31_...txt:292` `bathe the next morning` → `:391` `slide her valuable ring off it` | 改「**第二天早晨**从她手上取走」 |
| 9 | `ch35 the black market wore ribbons in her hair.md:144` | 把原文标注的谎言写成事实 | `text/ch31_...txt:193` `"It belonged to my grandmother," Sofia lied.` | 改「这枚戒指的来历**她谎称**是祖母所留（原文在第三十一章明标 `Sofia lied`）」 |
| 10 | `ch35 ...:232` / `:240` | 时序错：把闪回段写成「本章接下来/本章末」 | `text/ch35_...txt:319` `All those months ago, Sofia had left the train…`；L475–478 跑出军营；L481 章末上卡车去黑市 | 改「**闪回段结尾**」 |
| 11 | `ch37 what came first the mother or the egg.md:196` | 分析层引语多套一层外层直引号 | `text/ch37_...txt:97` 单行叙述句 + 台词 | 去外层 `> "…"`，改为 `> She said, "Sometimes a war can set a woman free."` |

### d 步总览层阻断型（批 5，2 条，已修）

| # | 位置 | 缺陷 | 依据 | 修法 |
| --- | --- | --- | --- | --- |
| 12 | `00_概述.md:45` | 引语章号/归属错标：实为 **Celeste** 的台词、逐字只在 **ch23** 命中，却被放在「## 三、白鹅」节下 | `text/ch23_handcuffs_made_of_smoke.txt` 命中 | 从白鹅节删除，移入「## 五」Celeste 条目，冠以「她替白鹅说出了这套书的诊断：」 |
| 13 | `00_概述.md:67` | 章节范围错标 `**Celeste**（ch20–ch23）` | `text/ch18_the_fog_wears_grey_stockings.txt:73` `My friend Celeste is there.` | 改 `（ch18–ch23）` |

### d 步第二轮：结构级缺陷（**五批子代理全部漏报，由我回源自查抓出**）

**★ 本轮是本审查最大的发现，务必记入方法论。** 起点是复核 `check_block_keywords`（⑱）的 117 条报警究竟是真是假——**先读实现再定档**，读到 `scripts/check_block_keywords.py:21` docstring「引语只来自**一个自然段**（跨段拼接红线）」与 `:260` 的输出行，确认**这条是真判据，不是防御性守卫**（与我此前压缩记录里的旧结论相反，旧结论是**错的**）。

规范源逐字：
- `docs/新书启动模板.md:135` 第 5 条「**引语只取一个说话轮次**」（每条引语只取自一个自然段）
- `docs/新书启动模板.md:926`「⭐ **跨段拼接的第二种形态：不是省略号，是段落边界**——…`…` 版本禁令只说「省略号两侧须原词」，**没说「不得跨越段落边界」**——而段落边界在 `text/` 里是 `\n\n\n`，**任何 flat 比对都不会报错**。⇒ 实操口径：**一条引语只能取自一个自然段**；要引下一段，另起一块。」
- `docs/新书启动模板.md:929`「**截取引语的首字符不得是原文没有的引号**；若原文的开引号在更前面的句子里，要么把整轮次引全，要么不引这一段。」

#### （1）` / ` 跨自然段拼接：20 块（全部已修）

- 扫描口径：全书 md 中形如 `> **原句 N:** "第一段" / "第二段"` 的块，把 ` / ` 两侧片段各自在**原始 text（不折叠空白）** 中定位，取相邻片段之间的原文子串，**若含 `\n\n` 即跨自然段**。
- 命中 **20 块**：`ch20 adrift in formaldehyde.md` 2（`:41`、`:113`）｜`ch23 handcuffs made of smoke.md` 1（`:137`）｜`ch31 put a red rose in my buttonhole.md` **9**（`:107`、`:123`、`:171`、`:179`、`:195`、`:211`、`:259`、`:299`、`:307`）｜`ch32 pink is a state of mind.md` 1（`:138`）｜`ch33 a suitcase the size of a country.md` 3（`:26`、`:42`、`:50`）｜`ch34 an army of little beasts.md` 3（`:50`、`:114`、`:138`）｜`ch35 the black market wore ribbons in her hair.md` 1（`:234`）。
- **两条独立取证**：① 上述每块的源文区间内各段之间实测隔着 `\n\n\n`；② `grep -rl '原句.*" / "' notes/books/*/*/ch*.md` 在**全库其它书命中 0** ⇒ ` / ` 是本书独创写法，非本库通行约定。
- **反证（证明我明知正确约定）**：本书自己在 `ch13`（`:49` 原句5）、`ch14`（`:57` 原句6、`:69` 原句7）、`ch15`（`:73` 原句8）、`ch17`（`:89` 原句10）、`ch18`（`:33` 原句3、`:83` 原句9、`:93` 原句10）、`ch19`（`:25` 原句2、`:83` 原句9、`:93` 原句10）、`ch20`（`:135` 原句15）、`ch24`（`:113` 原句13、`:259` 原句31、`:285` 原句34）、`ch27`（`:233` 原句28、`:429` 原句52、`:521` 原句63）、`ch29`（`:57` 原句6、`:133` 原句15、`:189` 原句21、`:209` 原句23、`:261` 原句29、`:305` 原句34、`:349` 原句39、`:409` 原句45、`:453` 原句50）、`ch30`（`:225` 原句27、`:269` 原句29、`:297` 原句31、`:365` 原句38、`:377` 原句39）、`ch31`（`:369` 原句42）、`ch37`（`:194` 原句23）共 **35 处**用了**规范写法**（块内 `>` 空行分隔多段，每段逐字）。
- 修法（脚本 `/tmp/fix_slash_blocks.py`）：拆为 `> **原句 N:** "第一段"` + 逐段 `>` 空行 + 段行（段间非空叙述句按原文保留）。
- **特例手工修 `ch31 …` 原句 36**：第一段实为源文 **536 字符长独白**（`text/ch31_put_a_red_rose_in_my_buttonhole.txt:463`，起点 `“You don't understand. You have much too high an opinion of me.…`）的**末句截取**，与第二段（`:466` `“Next you will be telling me…`）分属两个自然段 ⇒ 已改为**引全整段独白** + `>` 空行 + 白鹅回答，并同步扩写 `**中文理解：**`。
- 修后：残留 ` / ` **0 处**；规范多段块 **35 个**。

#### （2）截断型 + 伪加引号型：再 6 块（已修）

⑱ 复跑后又暴露 6 块，分两型：

| 型 | 位置 | 症状 | 修法 |
| --- | --- | --- | --- |
| 截断型（md 用闭引号收尾、源文该段仍在继续） | `ch25 every sentence is a magic spell.md` 原句10 | `…Never underestimate your worth.”` 但源文续 `You are going to need to be arrogant…` | 替换为完整自然段（532 字符） |
| 同上 | `ch31 put a red rose in my buttonhole.md` 原句38 | `…I knew you did not intend to eat me.”` 但源文续 `I was glad we were together.…` | 替换为完整自然段（497 字符） |
| 同上 | `ch35 the black market wore ribbons in her hair.md` 原句23 | `…That it made them lazy.` 但源文续 `“She sent me to the country to be with cousins.…` | 替换为完整自然段（363 字符） |
| 伪加引号型（引语起始于段中、开头引号系自加） | `ch25 …` 原句11 | 起点 `You are going to need…` 前有 `Never underestimate your worth.` | 替换为完整自然段（532 字符） |
| 同上 | `ch31 …` 原句24 | 起点前有 `…And I am worthy. I don't care whether he is pretending to love me.` | 替换为完整自然段（788 字符） |
| 同上 | `ch31 …` 原句39 | 起点前有 `…You have shown me the most incredible friendship.` | 替换为完整自然段（399 字符） |

**根因一句话：三类（` / ` 拼接、截断、伪加引号）都是同一个动作——「只想引最有意思的那半句」。** 故修法统一为「取源文完整自然段整段替换」。

#### （3）同批修掉的其它 4 处（⑱ 复跑后暴露）

| 位置 | 缺陷 | 依据 | 修法 |
| --- | --- | --- | --- |
| `ch24 the price of tears during wartime.md` 原句9 | 伪加引号（真实起点在段中） | 源段落 400 字符，起点为 `The Old Woman asked them questions…` | 替换为完整自然段 |
| `ch24 …` 原句24 | 同上 | 源段落 252 字符，起点为 `“There will be ink at the Black Market.…` | 替换为完整自然段 |
| `ch24 …` 原句37 | 同上 | 源段落 397 字符 | 替换为完整自然段 |
| `ch30 the saboteur wears patent leather shoes.md` 原句16 | **引语缺一个逗号** | 源文为 `which surprised Sofia, as she did not know accountants could be tone deaf`（md 漏 `Sofia` 后逗号） | 补逗号 |

> **定档修正**：`ch30` 原句16 此前被 d 步批 4 列为「提示型·标点级偏差」，**经回源实为可修的阻断型（引语非逐字）**，已改为阻断型并修。此条说明**子代理的「提示型」分类需要主会话回源复核**，不能直接采信。

#### （4）⑱ 残留判为假红：1 处

- `ch23 handcuffs made of smoke.md` 原句24 报「引语跨自然段」。回源核对：md 作 `seventeen-year-old`，源文与 **epub 原始 xhtml 均作 `seventeen- year-old`**（`OEBPS/text/9781443451628_Chapter22.xhtml`）。且 epub 内 `字母- 空格字母` 形态共 **8 处**（`lower- class` / `low- growing` / `good- looking` / `mid- afternoon` / `seventeen- year-old` 等）⇒ 属**提取件与 epub 的换行连字符伪影**，md 归一为正确词形是**正确处置**。⑱ 此处为**假红**，不改文。

#### （5）修后 ⑱ 状态

- **117 处 → 78 处**。其中「引语跨自然段（拼接红线）」仅剩 **1 处**（即上述 ch23 假红）。
- 其余 **77 处全部为已知模板不匹配类**：「引语块 N 个，超出言情精简格式的 3–8 配额」（ch26 24 / ch27 63 / ch28 19 / ch29 52 / ch30 39 / ch31 34 / ch32 15 / ch33 10 / ch34 21 / ch35 27 / ch36 19 / ch37 23）+「结构对账失败 —— 关键词行 0 ≠ 引语块 N」（同章）。**本库格式根本没有「关键词行」，故必报。**

### d 步假红排除（**关键，防止误报写入正式报告**）

- **`ch28:133` `Clara` 专名「错」——假红**：**Clara 就是母亲的本名**，全书源文出现 **116 次**（`Clara Bottom was the Simone de Beauvoir of Elysia.`），含 Clara 的章共 21 个。`ch12:37` / `ch20:103` / `ch23:10,61,69` / `ch31:279` 均为**合法跨章指称**。已回退为 `Clara 式母爱`；另 `ch28:12` 加括号写 `Clara（母亲）`。**教训：专名判定必须查全库词频与身份，不能只看本章。**
- **`ch21:253` `guilt` 「伪引语」——假红**：`grep -c -w guilt ch21` → **0**，但这是**论证性反事实对照**（「作者用 A 而不是 B」），B 词本就不该出现在原文里。**不改。**
- **`check_block_keywords`（⑱）的「引语跨自然段（拼接红线）」条——第一轮误判为假红，第二轮实为真判据**：该脚本 docstring（`scripts/check_block_keywords.py:21`）自述「引语只来自一个自然段（跨段拼接红线）」，`scripts/check_block_keywords.py:260` 输出该判据。**我最初据「`> **原句 N:**` 是单行，写不进 `\n\n`」把整条归为防御性守卫——这是错的**：多段引语写成 ` / ` 或块内续行后，逐段落在不同自然段，该判据完全可触发，且**实际抓出 20 块 ` / ` 拼接 + 6 块截断/伪引号**。**教训：判定任何门禁条目前必须读实现并构造反例，不能靠「格式上不可能」推理。**
- **`norm` 把 `\n` 折叠成空格会掩盖段落边界**：第一轮我用折叠空白做比对，得到「19 块全部紧邻、1 块查无」的结论，**完全错误**。必须用「保留换行 + 位置映射」或「在原始未折叠文本里逐段 `find`」才能看见 `\n\n\n`。**可靠算法**：在**原始 text**（不折叠空白）中逐段定位，取相邻段之间的原文子串，若含 `\n\n` 即跨段。
- **程序化引语比对报 `ch10 原句5 / ch13 原句8 / ch14 原句5 MISS` 及 ch13/14/15/17 编号 GAP——全为脚本误报**：根因是**块内空行 `>` 分隔多段原文**（模板案例三认定的**合法写法**）与弯/直引号差异，归引号后重跑 `miss=[]`。
- **`ch15:87` 引语照抄原文自身破损句**（`text/ch15:76` `They suddenly, from the ground, a glowing dome appeared.`）——属**忠实引用**，非缺陷。
- **`ch16:21` 「精灵树/会走路的树」交叉引用**——成立（`text/ch02:245` `The forest was filled with elf trees`；`text/ch13:64`）。

### d 步中段抽查型复核（我自己做的，非子代理报告）

抽出全书**中文括号内嵌英文片段 80 条**逐条比对本章 `text/`：**77 条逐字命中**，3 条报警**全部核实为假阳性**：

1. `ch14:29` `disguise` 是**章标题**（`# 14. Motherhood Is a Disguise`），作标题释义用；
2. `ch12:95` `the Capital of Dreams` 是**书名**；
3. `ch22:213` `monstrously, ferociously, madly` 是三词分列，源文同句内各有 1 次（`But Sofia loved her mother monstrously, ferociously. Sofia was madly in love with her mother.`），扫描器要求逗号连串故误报。

**结论：无真缺陷。**

### d 步提示型（只记不改）

1. `ch06:87` 引号内 `why` 原为句中首小写（仅句首大小写差异）。
2. `ch18 the fog wears grey stockings.md:31` 称「与第 8 章白鹅"信仰是一种不要求证据的信任"一脉相承」，但 `ch08` 源文 `faith|belief|proof` **0 次** ⇒ **交叉引用不可核**。
3. `ch08:47` 引 `"the commodification of evil"` 的 `the` 系 md 自加（原文 `:94-97` 为 `The aesthetics of evil. …The commodification of evil.`）。
4. `ch12:79` `"perversity is an acquired taste"` 句首应大写 `Perversity`。
5. `ch18:12` 称「白鹅全程只发出一个声音——拒绝喝牛奶」，但 ch18 白鹅对白计数为 **8**（`:22` 有整段台词，`:88/91/94/97` 另有 4 句，`:64` 才是递牛奶）。
6. `ch16:63` 对 ch02 引语的两种译法不一致。
7. `ch17 a wartime lullaby.md:135-136` 词表 `| peaches | … |` 行与上方表格之间有空行，表格被截断。
8. `ch28:107` 中文理解行末多一个双引号。
9. `ch30:438/445` `balcony` 在 ⭐⭐ 与 ⭐ 两档重复收录（例句相同）。
10. `ch30:455` 总结写「角落摇椅上」而原文 `text/ch30:10` 为 `wobbly chair`（同章导航 L10 作「摇摇晃晃的椅子」）——**同书两层自相矛盾**。
11. `ch32:10/138/140` 两句对话原文无说话人标签。
12. `ch37:194-196` 两段间原文隔一整段（`:94`→`:97`）。
13. `00_概述.md:8`「1 篇序曲 + 36 章（共 37 件）」与 `00_情感节点.md:8`「全书 37 章」**措辞不一致**（计数本身都对：`ch01` 是序曲 + `ch02`–`ch37` 共 36 章 = 37 件）。

---

## e. 总览层事实核对

### e 步自身发现（与 d 步批 5 互补）

- `00_概述.md:45` 的引语**兼有（a）归属错与（b）章号错两重问题**：该串逐字只在 **ch23** 命中（`text/ch23_handcuffs_made_of_smoke.txt`），且是 **Celeste 的台词**而非白鹅的；原先的标题「与白鹅"用最漂亮的语法说出最残忍的话"一脉相承」（`:44`）引的第二串同样只在 ch23 命中且亦为 Celeste 所说 ⇒ **两串均已移出白鹅节**。
- `00_概述.md:67` `**Celeste**（ch20–ch23）` → `（ch18–ch23）`（首次出现 `text/ch18_the_fog_wears_grey_stockings.txt:73`）。

### e 步事实核对结论

- `00_金句精选.md` 24 条：逐条引语逐字 + 章节号核对，**24/24 全对**，六组分组与引言口径一致。
- `00_情感节点.md` 14 条：逐条引语逐字 + 章节号核对，**14/14 全对**；编号「节点一」…「节点十四」连续不重置。
- `00_概述.md` 八节（全书结构 / Sofia 要做的事 / 白鹅 / 母亲 / 她遇到的人 / 主题四条 / 结局 / 一句话总述）：逐段核对人名、关系、时间线、情节走向。
- **说话人归属复核法（模板要求）**：凡 grep 命中后，**必须查看命中点前后约 200 字符窗口**确认说话人（原文常有 `X said` 在句前或句后），不得只看命中行。`00_概述.md:45` 的错标正是靠此法抓出。
- 修后 `verify_overview_quotes`：**38/38（100%）**、干净 2/2。

---

## 结论与局限

### 门禁最终状态（整改后，完整 lane）

| 项 | 结果 |
| --- | --- |
| `verify_quotes` | **787/787（100%）**，完全干净 39/39，`--full` 整串取证 0 |
| `check_vocab` | 词条行 1189 ｜ **FAIL 0** ｜ WARN 55（提示型） |
| `check_entities` | 0 个未知实体 |
| `corruption_scan` | FAIL 0 / 报告 0 |
| `sweep_full` | ✅ 753 ｜ 跨章 0 ｜ 🔶 0 ｜ ❌ 0 |
| `check_short_quotes` | ✅ 36 ｜ 别章 0 ｜ 🔶 0 ｜ 🔧 0 ｜ ❌ 0 |
| `check_chapter_quotes` | 37/37，每章 773/773（100%） |
| `verify_overview_quotes` | 38/38（100%），干净 2/2 |
| `check_quote_blocks` | ✅ 720 行 / 37 文件 |
| `check_block_keywords`（⑱） | 78 处报警：拼接红线 1（假红）｜模板不匹配 77（假红） |
| 空段扫描 | 0 处 |

**缺陷统计（两轮合计）：阻断型 31 条（全部已修并回源复核）｜提示型 13 条（只记不改）｜假红 6 类（不改文，根因已定位）。**

阻断型 31 条 = 第一轮 d 步 11 条（五批子代理报出）+ 第一轮总览层 2 条 + **第二轮 18 条**（20 块 ` / ` 拼接中的 19 块脚本修 + 1 块手工修，计 20 条，其中 2 条与第一轮重叠；另 6 块截断/伪引号 + 3 块 ch24 伪引号 + 1 处 ch30 缺逗号）。**第二轮 18–26 条全部由主会话回源自查抓出，五批子代理无一报出**——因为任务书把「块内空行 `>` 分隔多段原文」写成了**合法写法**，子代理据此把 ` / ` 也当容忍写法放行；**给子代理的判据本身有洞，则五批会一致漏掉**。

### 同会话审查的已知盲区（AGENTS.md:266 要求写明）

本次审查由**撰写本书的同一实例**在同一会话内执行。按 `AGENTS.md:264-266`，用户在同会话内主动要求时「局限」条款**不构成跳过任何步骤的理由**，故 a–e 已完整执行。但仍须如实标注以下盲区：

1. **撰写惯性盲区**：我自己的写作错误模式（引语改写冒充逐字、章号错标、时序倒置、` / ` 跨段拼接、截断后半句）可能还有本实例无法识别、且五批子代理判据相同因而同样漏掉的同类项。**同一套提示词不可能完全互相独立。**
2. **子代理同源盲区（已被本轮实证）**：五批子代理与主会话使用同一模型族，其「阻断型/提示型」判据由我拟定；判据本身若有系统性遗漏，五批会一致遗漏。**本轮实证：20 块 ` / ` 跨段拼接 + 6 块截断/伪引号 + 3 块 ch24 伪引号 + 1 处 ch30 缺逗号，五批子代理全部漏报**，根因是我给它们的任务书把「块内空行 `>` 分隔多段原文」写成了**合法写法**，它们据此把 ` / ` 也当容忍写法放行。**⇒ 教训：派子代理前必须先自己把规范源逐字读完并构造反例，否则「五批独立核对」只是同一盲区的五份拷贝。**
3. **`/tmp` 临时审计脚本未持久化**：本轮结构级审计用的 `/tmp/fix_slash_blocks.py`、`/tmp/fix_trunc.py`、`/tmp/fix_ch24.py` 均未入库，报告中只留了判据与算法描述。若后续需复查，须按报告内文的算法重建（见「d 步第二轮」节）。**这是我该改进的地方：审计脚本应写入 `<书目录>/audit/` 或 `scripts/` 以便复现。**
4. **提示型未整改**：13 条提示型按规范「只记不改」。其中第 2 条（`ch18:31` 交叉引用不可核）、第 5 条（`ch18:12` 白鹅台词计数夸大）、第 10 条（`ch30` 同书两层自相矛盾）**属实且值得后续修正**，本次因属提示档而未动文。
5. **块数两种口径须分清（易误判为遗漏）**：
   - `720` = `check_quote_blocks` 统计的**带 `> **原句 N:**` 前缀的行数**（37 文件）。
   - `773` = `check_chapter_quotes` **解析出的引语块数**上限口径（其每章输出 `X/X in chNN text` 逐章相加 = **773**）。
   - 差额 **53** 来自**同一块的续行**：多段原文用空行 `>` 分隔时，解析器把每个 `>` 段都算一块，而 md 里只有首个 `>` 行带 `**原句 N:**` 前缀。典型：`ch13` 前缀 10 / 解析 11、`ch14` 10/13、`ch15` 10/13、`ch17` 10/12、`ch18` 10/14、`ch19` 10/16、`ch20` 17/18、`ch24` 42/45、`ch26` 24/23、`ch27` 63/66、`ch29` 52/60、`ch30` 39/52、`ch31` 42/50、`ch37` 23/24。**非遗漏、非多余**，是同一事实的两种计量。
   - d 步五批的计数（737）＝ 按 md 块数逐块核对的 720 块 + 总览层金句 24 条与情感节点 14 条的独立逐条核对，**覆盖完整，无跳读**。
6. **`verify_quotes` 口径变化须按两次整改分段解释**：
   - 五步审查开始时 **807** 条 ⇒ d 步第一轮修掉 `ch37:196` 外层直引号后为 **806**（该串不再是独立引语行）。
   - d 步第二轮把 **20 个 ` / ` 拼接块**拆为规范多段块后为 **787**（同一块内 ` / ` 两侧原本计 2 条，拆分后仍是一块的多个自然段）。
   - **两次下降都不是引语丢失，而是「条目计量形态」随写法规范化而变化**；每次修后 `verify_quotes` 均为 **100% 全绿**，`sweep_full` 的 `❌ 全书查无` 始终为 0。**判「引语是否丢失」应看「❌ 查无」与「干净文件数」，不应看条目总数。**
7. **e 步由独立子代理执行**（`20d77e83-fbbe-4759-ab03-f40b0e4a8140`），其报告与 d 步批 5 结论一致；但该子代理同样由本实例调度，**不构成真正的外部独立**。
8. **第二轮自查之所以能抓到子代理的漏项，靠的是「先读门禁实现再定档」这一条纪律**（AGENTS 8.4 精神）。我此前把 ⑱ 整条判为「防御性守卫、结构上不可触发」，若不再读一遍实现并构造反例，这 30 处缺陷会**整批进入成品**。**⇒ 本次审查最有价值的产出不是那 31 条清单，而是「门禁报警在定档前必须读实现 + 构造反例」这条可复用的纪律。**

### 整改清单（已落盘）

**d 步第二轮 + 第三轮共修改 16 个 md 文件**（`git status --short` 实测）：

`00_概述.md`、`ch02 the childrens train.md`、`ch06 a cat named napoleon.md`、`ch20 adrift in formaldehyde.md`、`ch23 handcuffs made of smoke.md`、`ch24 the price of tears during wartime.md`、`ch25 every sentence is a magic spell.md`、`ch26 i heard the icicles singing.md`、`ch28 songs for city birds on clarinet.md`、`ch30 the saboteur wears patent leather shoes.md`、`ch31 put a red rose in my buttonhole.md`、`ch32 pink is a state of mind.md`、`ch33 a suitcase the size of a country.md`、`ch34 an army of little beasts.md`、`ch35 the black market wore ribbons in her hair.md`、`ch37 what came first the mother or the egg.md`

另新增审查原件 5 份：`.memory/raw-gates/the-capital-of-dreams-by-heather-oneill/` 下 `2026-10-03-审查-a-门禁全量重跑.txt`、`2026-10-03-审查-b-逐章归属汇总.txt`、`2026-10-03-审查-cd-结构扫描与第二实现.txt`、`2026-10-03-审查-d整改后门禁重跑.txt`、`2026-10-03-审查-e-整改后门禁全量重跑.txt`。

**提交方式**（遵 AGENTS.md git 红线）：逐路径 `git add`（**禁止 `git add -A` / `git add .`**）+ `git commit -q -m "<msg>" -- <明确路径>`（**`-m` 必须在 `--` 之前**）；**不推送**（需用户明确指令）。

### 可复用纪律（本次审查的最大产出）

1. **门禁报警定档前，先读实现并构造反例**。本轮 30 处缺陷全部藏在被我先判为「假红」的 ⑱ 里；判据读一遍、构造一个反例，即可推翻「格式上不可能」的推理。
2. **比对引语是否跨自然段，必须在原始文本（不折叠空白）里逐段 `find`**，取相邻段之间的原文子串看是否含 `\n\n`。折叠空白的一切比对都看不见段落边界。
3. **给子代理的判据本身若有洞，五批会一致漏掉**；派发前须自己先读完规范源并写出**反例清单**，而非只给「合法写法」示例。
4. **修法应当按根因归并**：` / ` 拼接、截断后半句、伪加引号三种症状同源于「只想引最有意思的那半句」，统一用「取源文完整自然段整段替换」即可一次覆盖。
5. **引语总数变化不能作为「引语丢失」的判据**，应看 `❌ 全书查无` 与「完全干净文件数」。
