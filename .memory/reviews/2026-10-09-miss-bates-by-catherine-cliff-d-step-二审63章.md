# Miss Bates: Emma Revisited — 五步审查 d 步语义二审 逐章 staging（63 章）

- **日期**：2026-10-09
- **身份**：Raccoon-Mac
- **方法**：d 步「语义二审」逐章逐引语块核对（说话人 + 逐字 + 分析对应 + 关键词回查）
- **章数**：63 章（ch02 Prologue – ch64 Epilogue），每章一节，按章号升序
- **来源**：`review_miss-bates/staging/verify_ch{02..64}.md`（原件，归档时合并为单文件）
- **说明**：每件均经落盘校验（`wc -c` 非空，最小 1414 B / 最大 7477 B）；超时批次按修正记录采用已落盘件、缺失章单章补发
- **门禁复跑**：verify_quotes 256/256（100%）、check_chapter_quotes 63/63（零跨章）、corruption_scan 0 FAIL

---


---

# d 步二审 · ch02

## 结论：共 4 块，通过 4，缺陷 0，待复核 0

本章仅 4 个引语块（原句 1–4），每块「引语行 + 中文理解 + 关键词 + 为什么这样写 + 读者视角提示」五要素齐全，无孤儿块、无重复块。逐块核对如下：

### 原句 1
- **引语逐字**：`As if she were bending a large iron rod with sheer force of will, Henrie curved her lips upward into a pleasant smile. She had used all her powers to refuse Mrs. Elton's hospitality.` 命中 text 第 16 行，逐字一致（原文弯引号 `’`，md 直引号，属允许差异）。✓
- **说话人**：命中所指为围绕 Henrie 的第三人称叙述（Henrie 是动作主语，Mrs. Elton 是宾语），与「中文理解」归因（Henrie 用意志力微笑并拒绝 Mrs. Elton 款待）一致。✓
- **引语↔分析对应**：中文理解/关键词/为什么这样写/读者视角提示均在讲"微笑之难=拒绝之难"这一句；"used all her powers" 与"iron rod"比喻均被分析覆盖，未截短。✓
- **关键词回查**：refuse ✓ / hospitality ✓ / sheer force of will ✓ 均在本块引语内。✓

### 原句 2
- **引语逐字**：`But to go as a guest to this of all places, in her current state, the state of having been flayed alive in public, placed, skin aflap, bleeding beneath the microscope of derision, she did not, on this particular afternoon, think she could bear it.` 命中 text 第 25 行，逐字一致。✓
- **说话人**：第三人称叙述、心理主体为 Henrie，与「中文理解」归因一致。✓
- **引语↔分析对应**：中文理解对"那个地方（如今属于别人的牧师住宅）"的补充说明来自同段落前文（第 22 行 "her own home, of course, more than twenty years ago"），属语境解释而非引语自身文字，不构成截短。分析覆盖 flayed alive / microscope of derision / "on this particular afternoon" 三处关键，均对应。✓
- **关键词回查**：flayed alive in public ✓ / microscope of derision ✓ / bear ✓ 均在本块引语内。✓

### 原句 3
- **引语逐字**：`At this point in her discourse, Henrie was tumbled from the carriage like a bale of hay by Mr. Elton, who did not pause his conversation nor break eye contact with his wife as he handed her out, merely raising a hand in absent salute over his shoulder as he climbed back in. No microscope here, then.` 命中 text 第 31 行，逐字一致。✓
- **说话人**：句末"Mrs. Elton, thank you so much for a wonderful—"是 Henrie 被打断的话，其后"At this point in her discourse…"回到叙述层；动作主体 Mr. Elton、受事 Henrie，与「中文理解」归因（Mr. Elton 像丢干草一样放下 Henrie、无礼送客）一致。✓
- **引语↔分析对应**：中文理解讲推让被打断、丢下车、不停谈话不看、爬回抬手，均对应；为什么这样写引用章末短句 "No microscope here, then." 承接原句 2 比喻，该句确在引语末尾。✓
- **关键词回查**：tumbled ✓ / like a bale of hay ✓ / in absent salute ✓ 均在本块引语内。✓

### 原句 4
- **引语逐字**：`Her throat was so tight with holding back her sobs that it felt like there were ribbons wound all around it, like she was choking.` 命中 text 第 34 行（末段末句），逐字一致。✓
- **说话人**：第三人称叙述、主体 Henrie，与「中文理解」归因一致。✓
- **引语↔分析对应**：中文理解"全章最后一句落在缠着丝带的喉咙上"确为正文末句；关键词/为什么这样写/读者视角提示均围绕同一句。✓
- **关键词回查**：holding back her sobs ✓ / ribbons wound ✓ / choking ✓ 均在本块引语内。✓

### 附：本章词汇例句抽查（非引语块，供参考）
本章词汇表 11 条例句逐条命中 text（hospitality→L16；indispensable/toadeaters/refitted/dowdy→L22；derision→L25；effusions/vicarage/detour→L28；discourse→L31；self-possession→L34），说话人归属均正确（Mrs. Elton 台词归 Mrs. Elton，叙述句归 Henrie 主体），未见错标。此部分不计入引语块统计。

## 缺陷清单（无则写"无"）
无

## 待人工复核
无

说明：本次未发现说话人反转、跨章章号错标、引语截短或拼装幻觉。原句 2 中文理解中的"那个地方/牧师住宅"为同段落语境解释，已判为合理而非截短，特此留痕以备人工再判。

ch02 完成：4 块，缺陷 0，待复核 0
---

# d 步二审 · ch03

## 结论：共 4 块，通过 4，缺陷 0，待复核 0

## 缺陷清单
无

## 待人工复核
无

---

## 逐块核对记录

### 块 1（原句 1）
- **引语逐字**：md 第 21 行 vs text 第 17 行 —— 逐字一致（破折号、撇号、大小写均吻合）。✓
- **说话人**：旁白叙述（第三人称贴身叙事），与「中文理解」把这段话当作叙事背景描述 Henrie 的动作一致。✓
- **引语↔分析**：中文理解逐句对应；为什么这样写紧扣「in secret」偷糖细节与实验精神；读者视角提示指向 George 猫与后文名字被夺的伏笔，均在引语/章内可支撑。✓
- **关键词回查**：in secret ✓、Demerara sugar ✓、thimble ✓ —— 均在引语中。✓
- **结构**：引语行 + 中文理解 + 关键词 + 为什么这样写 + 读者视角提示，齐全。✓

### 块 2（原句 2）
- **引语逐字**：md 第 33 行 vs text 第 32 行 —— 逐字一致（含弯引号 "Henrie"、破折号）。✓
- **说话人**：旁白叙述，介绍父亲形象，与「中文理解」描述父亲的行为一致。✓
- **引语↔分析**：中文理解逐句对应；为什么这样写提及「火鸡图在后一章复现、'liked her' 是对照伏笔」（属章外线索，引语内火鸡图已确证）；读者视角提示指向「希腊神有一半是女神」句，均在引语中。✓
- **关键词回查**：mystery ✓、nickname ✓、fond ✓ —— 均在引语中。✓
- **结构**：齐全。✓

### 块 3（原句 3）
- **引语逐字**：md 第 45 行 vs text 第 55 行 —— 逐字一致（含括号内容 "and that, actually, had been her"）。✓
- **说话人**：旁白叙述，与「中文理解」一致。✓
- **引语↔分析**：中文理解逐句对应；为什么这样写紧扣 spell、reallocating、括号自白；读者视角提示指向括号那句，均在引语中。✓
- **关键词回查**：a spell ✓、reallocating ✓、loaf of squalls ✓ —— 均在引语中。✓
- **结构**：齐全。✓

### 块 4（原句 4）
- **引语逐字**：md 第 57 行 vs text 第 58 行 —— 逐字一致。✓
- **说话人**：旁白叙述，与「中文理解」一致。✓
- **引语↔分析**：中文理解逐句对应；为什么这样写紧扣名册字迹对比与 "the real Henrie"；读者视角提示指向拼写执念，均在引语中。✓
- **关键词回查**：no longer Henrie ✓、parish register ✓、minuscule ✓ —— 均在引语中。✓
- **结构**：齐全。✓

---

**附注（非缺陷）**：md frontmatter 标题写「精读 02 · Chapter 1（Part One）」，正文标题写「Chapter 1（Part One: 1769–1795）」，均指向 Chapter 1，与 text 文件标题 "Chapter 1" 一致，无跨章章号错标。

ch03 完成：4 块，缺陷 0，待复核 0
---

# d 步二审 · ch04

## 结论：共 4 块，通过 4，缺陷 0，待复核 0

审查文件：
- 精读 md：`notes/books/novels/miss-bates-by-catherine-cliff/ch04 what is a witch.md`
- 原文提取件：`notes/books/novels/miss-bates-by-catherine-cliff/text/ch04_chapter_2.txt`

核对方法：对每一引语块，①在 text/ch04 中逐字定位引语；②读取命中点前后 ~200 字符确认说话人/叙述主体；③核对中文理解、关键词、为什么这样写、读者视角提示是否指向同一句；④关键词英文回查引语原文；⑤结构完整性检查。

---

### 原句 1 ✅ 通过

- **引语行**：`"“But the marks on the wall, the wheels carved in the stone? I heard you say they are witches’ marks? And mother and Mrs. Wren touch them when they are worried. Are they… magic?” She whispered this last word, ... Now he shook his head with disgust."`
- **定位**：text 第 16 行，从 `“But the marks on the wall` 到 `Now he shook his head with disgust.`，逐字完全一致（含省略号、弯引号、破折号）。
- **说话人**：Henrie 追问父亲（牧师/教区牧师），引语后的叙述句描述「Now he shook his head with disgust」——叙述主体为牧师；上一行「her father said」明确 Henrie 在问父亲。✅ 说话人正确（Henrie → 父亲）。
- **中文理解 ↔ 引语**：中文译文完整对应引语全部内容（含耳语、画火鸡、多年前为他画过、厌恶摇头），无截短、无拼接。✅
- **关键词回查**：`witches’ marks`（原文 "witches’ marks"）✅、`whispered`（"She whispered this last word"）✅、`disgust`（"Now he shook his head with disgust"）✅。
- **为什么这样写 / 读者视角**：都在讲这一句（好奇→耳语→画火鸡→摇头），"years ago when he liked her"、"'whispered this last word'" 均取自本块引语。✅
- **结构**：引语行 + 中文理解 + 关键词 + 为什么这样写 + 读者视角提示，五件齐全。✅

---

### 原句 2 ✅ 通过

- **引语行**：`"“One what has powers, I suppose. Can do things she oughtn’t but without moving a muscle. She looks all small, like a sparrow, but it turns out she can make turrible things pass. My granny told me about one as blighted her neighbor’s well just by saying some powerful dark words in her cottage at night. Killed every last one of his sheep. And his wife.”"`
- **定位**：text 第 105 行，逐字完全一致（"oughtn’t"、"turrible" 方言拼写保留）。
- **说话人**：Jenkins。text 第 105 行是 Jenkins 回答 Henrie 的 "What kind of a lady?"，其上方对话链（第 102–104 行）确认 Jenkins 在说话。中文理解行明确「Jenkins 的回答」。✅ 说话人正确。
- **中文理解 ↔ 引语**：完整对应（有法力、不挪肌肉、像麻雀、弄坏井、杀死羊和妻子），无截短。✅
- **关键词回查**：`powers`（"One what has powers"）✅、`without moving a muscle` ✅、`blighted`（"as blighted her neighbor's well"）✅。
- **为什么这样写 / 读者视角**：均在讲这一句的"不挪肌肉"/"词句让事情发生"隐喻；引用的 "she looks all small, like a sparrow" 与 "词句能让事情发生" 定义均出自本块。✅
- **结构**：五件齐全。✅

---

### 原句 3 ✅ 通过

- **引语行**：`"“Agnes Twythorpe? Nah. I knowed her when I was a nipper. ... No one sees it happen. Here, done with this little man.” The goat cantered off ... the circles where the horn buds were looked like a second set of spectral eyes glaring out from the top of his head."`
- **定位**：text 第 147 行，从 `“Agnes Twythorpe? Nah.` 到 `glaring out from the top of his head.`，逐字完全一致。
- **说话人**：Jenkins（叙述句描述山羊被去除角芽后回头瞪视）。text 第 147 行是 Jenkins 回答 Henrie 的 "Is Miss Twythorpe one?"；其上方（第 144–146 行）确认 Henrie 发问、Jenkins 作答。✅ 说话人正确。
- **中文理解 ↔ 引语**：完整对应（醋/不是毒药、隐形融入、祖母说、没人看得见、山羊回头幽灵眼睛），无截短。✅
- **关键词回查**：`invisible`（"they’re invisible"）✅、`blend right in`（"Just blend right in"）✅、`spectral eyes`（"a second set of spectral eyes"）✅。
- **为什么这样写 / 读者视角**：均在讲本句的"隐形/融入人群"与山羊幽灵眼睛；引用 "醋、不是毒药"、"invisible / blend right in" 均出自本块。✅
- **结构**：五件齐全。✅

---

### 原句 4 ✅ 通过

- **引语行**：`"Sometimes, when Henrie couldn’t sleep, she imagined herself inside one of Mrs. Wren’s plum trifles. She was her normal size and the pudding was immense. She had to eat her way out of it, working through the layers of jam and biscuits and cream until finally her head emerged smiling into the world, triumphant."`
- **定位**：text 第 151 行，逐字完全一致。
- **说话人**：无引号对白，为叙述段（Henrie 的白日梦）。中文理解行亦按叙述处理（"有时候，Henrie 睡不着，就想象…"）。✅ 无说话人归因问题。
- **中文理解 ↔ 引语**：完整对应（李子双皮糕、平常个头、吃出路、笑着进入世界、得胜），无截短。✅
- **关键词回查**：`imagined`（"she imagined herself"）✅、`eat her way out`（"eat her way out of it"）✅、`triumphant`（"into the world, triumphant"）✅。
- **为什么这样写 / 读者视角**：均在讲本段（甜食白日梦、自己吃出路、笑着钻出世界、与全章残酷问答的落差），引用的 "自己吃出一条路来"、"笑着钻进世界"、"triumphant" 均出自本块。✅
- **结构**：五件齐全。✅

---

## 附：本章词汇例句抽查（辅助核对，全部通过）

对「本章词汇」表中例句逐条回查 text/ch04，均逐字命中：
- apotropaic：text L19 ✅；curtsy：text L77 ✅；vinegar：text L147 ✅；spectral：text L147 ✅；triumphant：text L151 ✅
- slaughter：text L50 ✅；blighted：text L105 ✅；cagey：text L111 ✅；wiggler：text L99 ✅
- quill：text L59 ✅；menus：text L41 ✅

## 缺陷清单（无则写"无"）

无

## 待人工复核

无

---

ch04 完成：4 块，缺陷 0，待复核 0
---

# d 步二审 · ch05

## 结论：共 4 块，通过 4，缺陷 0，待复核 0

## 各块逐对核对

### 原句 1
- **引语逐字**：与 text/ch05_chapter_3.txt 第 13 行逐字一致 ✓
- **说话人**：第三人称贴着 Henrie 的叙事，主语为 Mother；「中文理解」归因母亲忙碌，正确 ✓
- **关键词**：bustling / bounty baskets / parishioners 均在引语内 ✓
- **对应**：中文理解、为什么这样写（家务清单铺开日常 + bounty baskets 重命名施舍 + 孩子视角「更多时候被留下」）与「读者视角提示」（段尾埋不情愿伏笔）均指向本句 ✓
- **结构**：引语行 + 中文理解/关键词/为什么这样写/读者视角提示 四子项齐全 ✓

### 原句 2
- **引语逐字**：与 text 第 19 行逐字一致 ✓
- **说话人**：句中 "She held up…" 的 She 紧接 "Mrs. Bates let out a sharp yelp"，即 Henrie 的母亲；「中文理解」归因母亲，正确 ✓（非他人，无说话人反转）
- **关键词**：semicircle / dental impression / reproach 均在引语内 ✓
- **对应**：中文理解、为什么这样写（黄油呈堂证物、法庭式庄重措辞的喜剧落差）、读者视角提示（解释降级原因 + 全书笔调）均讲同一句引语，无截短 ✓
- **结构**：齐全 ✓

### 原句 3
- **引语逐字**：与 text 第 34 行逐字一致 ✓
- **说话人**：Henrie 的自由间接/内心叙述（"Oh, to be Mrs. Wren"），「中文理解」归为 Henrie 的羡慕，正确 ✓
- **关键词**：routine of plenty / mistress / pouch of coins 均在引语内 ✓
- **对应**：中文理解、为什么这样写（routine of plenty 丰足节奏 vs mother never handed coins 匮乏对照、羡慕「能决定」的权力）、读者视角提示（食物痴迷是家境拮据症候）均围绕本句 ✓
- **结构**：齐全 ✓
- 备注（非缺陷）：「读者视角提示」提到黄油/腌洋葱/耐放奶酪这些更经吃的东西，属本章其他段落（黄油 line 19、腌洋葱 line 31、奶酪 line 64）的内容，作为读者视角的跨段落归纳；与引语主题一致，非拼装无关分析，不判定为缺陷。

### 原句 4
- **引语逐字**：与 text 第 88 行一致（md 用直引号，text 用弯引号，允许差异），实词逐字 ✓
- **说话人**："said Mother"，Henrie noticed 的观察；「中文理解」归因母亲说 + Henrie 注意到，正确 ✓
- **关键词**：nonsense / carved wheels / chimney 均在引语内 ✓
- **对应**：中文理解、为什么这样写（对白 + 小动作戳穿理性、指尖碰到石头的收束）、读者视角提示（嘴否认 vs 手求平安的距离）均讲本句，无截短 ✓
- **结构**：齐全 ✓

## 缺陷清单（无则写"无"）：无

## 待人工复核
（无）

ch05 完成：4 块，缺陷 0，待复核 0
---

# d 步二审 · ch06

## 结论：共 4 块，通过 4，缺陷 0，待复核 0

## 缺陷清单：无

逐块核对结果：

- **原句 1**：引语逐字命中 text/ch06 第 13 行（逐字一致，含标点）。说话人归因为叙述/场景句，正确。中文理解、为什么这样写、关键词（nobody knew / Harry / where 均在句中）一致，无截短。✔
- **原句 2**：引语逐字命中 text/ch06 第 34 行（整段完整，未截短）。说话人归因为八岁 Henrie 目击视角的叙述，正确（该句为叙事段，非对话，归属合理）。关键词 ominously devoid of ducks / murk / dragged the small body 均在句中出现。✔
- **原句 3**：引语逐字命中 text/ch06 第 74 行（含弯引号 "Oh, pardon me," 与直引号原文一致）。说话人为 Henrie（"said Henrie"），正确。中文理解正确对应"在饭桌上说蠕虫被母亲喝止"（前文第 71 行）。关键词 power / appear different on the outside from the inside / alone in her mind 均在句中。✔
- **原句 4**：引语逐字命中 text/ch06 第 78 行（整段完整，未截短）。说话人归因为 Henrie 叙述/内心，正确。关键词 reconstructed in excruciating detail / stopped breathing / necessary 均在句中。✔

未发现说话人反转、章号错标、引语截短、跨块拼装或孤儿/重复块问题。

## 待人工复核

无。

ch06 完成：4 块，缺陷 0，待复核 0
---

# d 步二审 · ch07

## 结论：共 4 块，通过 4，缺陷 0，待复核 0

审查对象：
- 精读 md：`notes/books/novels/miss-bates-by-catherine-cliff/ch07 attract the least attention.md`
- 原文提取件：`notes/books/novels/miss-bates-by-catherine-cliff/text/ch07_chapter_5.txt`

核对方法：逐块到 text/ch07_chapter_5.txt 中 grep 引语行，命中后在前后 ~200 字符窗口内确认说话人与叙述语境一致；再核对中文理解/为什么这样写/关键词/读者视角提示是否都在讲同一句引语、引语是否截短、关键词英文词是否在本块引语内。

## 逐块核对明细

### 原句 1（md 第 19–29 行）
- **引语逐字**：完整命中 text 第 13 行（同一段逐字一致，弯/直引号与"do you do?"逗号位置一致）。✓
- **说话人**：前段为第三人称叙述描写"母亲的期望一减再减 + 被裁剪到尺寸"，末段为母亲对 Henrie 的当面操练直接引语（"Do you hear me, Henrietta? Do not stare."）。中文理解把"期望一减再减"归为母亲对 Henrie 的目标、"这一周母亲在操练她"归为母亲，说话人归属正确。✓
- **引语↔分析对应**：中文理解"期望一减再减""裁剪到合身的尺寸""屈膝礼、问好、微笑、匆匆看一眼——但不要盯着看""不要盯着看"逐句对应；为什么这样写谈 halved 递减动词、被裁剪到尺寸、"do not stare"反复出现，均为本块引语内容，未越界。引语未截短（整段完整到母亲斥责句）。✓
- **关键词回查**：halved ✓、cut to size ✓、do not stare ✓（均原词出现在引语内）。✓
- **结构**：原句行 + 中文理解 + 关键词 + 为什么这样写 + 读者视角提示，五件齐全。✓

### 原句 2（md 第 31–41 行）
- **引语逐字**：完整命中 text 第 25 行，逐字一致。✓
- **说话人**：前句为叙述"母亲给过的另一条指令"，主体为 Mrs. Bates（母亲）对 Henrie 的排练台词（"Do you understand, Hetty? ... I am Mrs. Mott, and I have just bestowed upon you a blue-veined cheese."）。中文理解明确归为"母亲给过的另一条指令……母亲让亲口说出"，归属正确。✓
- **引语↔分析对应**：中文理解"小礼物要微笑着说多高兴""你不必真的高兴""我是 Mrs. Mott，我刚赏给你一块蓝纹奶酪"逐句对应；为什么这样写讲"你不必真的高兴""bestowed 配蓝纹奶酪"的庄重与可笑并置，均为本块内容。引语完整未截短。✓
- **关键词回查**：Gratitude ✓、actually pleased ✓、bestowed ✓（原词均在引语内）。✓
- **结构**：五件齐全。✓

### 原句 3（md 第 43–53 行）
- **引语逐字**：完整命中 text 第 59 行，逐字一致。✓
- **说话人**：第三人称贴身叙述描写 Henrie 的失眠幻想（imagined a trade / 砍头 / Harry 归来）。中文理解"睡不着的时候，Henrie 会想象一场交易"归为 Henrie 的幻想，归属正确。✓
- **引语↔分析对应**：中文理解逐句覆盖"切鸡小斧""酗酒牧师父亲上砧板""砍下父亲的头""三岁 Harry 笑着走出来""无头身体跑动片刻""只顾为 Harry 回来欣喜若狂"；为什么这样写谈"把失去的父亲与失去的婴儿弟弟放同一架天平、用砍头换 Harry 归来"、"Trade 说明不是单纯暴力幻想"，均为本块引语内容。引语完整未截短。✓
- **关键词回查**：imagined a trade ✓、chopped off ✓、overjoyed ✓（原词均在引语内）。✓
- **结构**：五件齐全。✓

### 原句 4（md 第 55–65 行）
- **引语逐字**：完整命中 text 第 81 行，逐字一致（含内嵌 "You are terrible, Amelia" 与 "they shared a cozy chuckle"）。✓
- **说话人**：主段为 Mrs. Mott 的当面议论（"The other child I cannot speak so favorably of..."），末句"其他女人也许说 'You are terrible, Amelia'"为旁观者。上下文（text 第 69、72 行）确认议论者即 Mrs. Mott（拜访过、与 Henrie 相处不愉快、对教堂女眷服饰品头论足的那位）；Henrie 躺在墓碑后偷听。中文理解把主要非议归为 Mrs. Mott、把"你真坏，Amelia"归为另一位女士，归属正确。✓
- **引语↔分析对应**：中文理解逐句覆盖"低能儿/五官乱扭/Lavvy 以为她在试着笑""发育迟缓、面包箱身形、没脖子、鼻子、剪影师会剪成牲口""冬马蓬发""你真坏，Amelia 与舒适低笑"；为什么这样写谈"最恶毒攻击全部放进 Mrs. Mott 长篇议论""Lavvy thought she was trying to smile 最刺""末尾轻飘飘的真坏 + 舒适低笑"，均为本块内容。引语完整未截短。✓
- **关键词回查**：moron of sorts ✓、trying to smile ✓、barnyard creature ✓（原词均在引语内）。✓
- **结构**：五件齐全。✓

## 缺陷清单
无

## 待人工复核
无

---

ch07 完成：4 块，缺陷 0，待复核 0
---

# d 步二审 · ch08

## 结论：共 4 块，通过 4，缺陷 0，待复核 0

## 缺陷清单（无则写"无"）

无

## 待人工复核

无

## 逐块核对明细

### 原句 1（第 19–29 行）
- **逐字核对**：`text/ch08_chapter_6.txt` 第 13 行整段逐字一致，实词无改写，仅省略号两侧原词保留。
- **说话人**：第三人称叙述（叙述者），非角色口白；中文理解与"为什么这样写"均按叙述内容解读，归因正确。
- **引语↔分析对应**：supposedly（缝衣为幌子）、ravening beasts（厌恶）、unspoken agreement（看与被看主题）三点分析均落在该段之内，无截短。
- **关键词回查**：supposedly / ravening beasts / unspoken agreement 均在引语中找到，逐字存在。
- **结构**：引语行 + 中文理解 + 关键词 + 为什么这样写 + 读者视角提示，五项齐全。通过。

### 原句 2（第 31–41 行）
- **逐字核对**：`text/ch08_chapter_6.txt` 第 46 行整段逐字一致。
- **说话人**：此处为叙述者描写（Henrie 视角所见 Miss Twythorpe 的肖像），非母亲台词；中文理解与"为什么这样写"均按叙述描写解读，归因正确。
- **引语↔分析对应**：stalking / scarecrow / 灰鹭 / 空钱包 / "第三只瘪掉的乳房"均在引语中；"一年七十五镑"来自同章母亲台词（第 40 行），作为分析呼应，不是本块引语内容，但属于本章事实、非幻觉。
- **关键词回查**：hobbling / stalking / scarecrow 均在引语中找到。
- **结构**：五项齐全。通过。

### 原句 3（第 43–53 行）
- **逐字核对**：`text/ch08_chapter_6.txt` 第 73 行整段逐字一致。
- **说话人**："It will be nice to say a prayer now, Hetty. Please join me in thanks to our Lord."为 Mrs. Bates 的台词；其后"Henrie had little truck with God..."为叙述（Henrie 内心）。中文理解将前者归为母亲说话、后者归为 Henrie 内心独白，归因正确。
- **引语↔分析对应**：grateful enough... to feed me 在引语中；分析称其"直接引用并倒转了母亲那句'必须先感恩才配得上（得到）'"，对应同章第 67 行母亲台词"You must appreciate in order to deserve."，属同章真实文本呼应，无幻觉。
- **关键词回查**：thanks / grateful enough / feed me 均在引语中找到。
- **结构**：五项齐全。通过。

### 原句 4（第 55–65 行）
- **逐字核对**：`text/ch08_chapter_6.txt` 第 162 行整段逐字一致。
- **说话人**：叙述者（Henrie 视角叙事）+ 其中一句母亲台词"Hetty, you are babbling, and I am busy."；中文理解将"Hetty，你啰啰嗦嗦，我忙着呢。"归为母亲说话、其余为 Henrie 的困境叙述，归因正确。母亲末句裁定"分不清坏笑和微笑"在引语末尾（Mrs. Bates's pronouncement...），属叙述转述母亲的话，归因正确。
- **引语↔分析对应**：clotted（凝结）/ clump（结块）/ the acceptable part / the unacceptable part / as revelation / 死结手帕（tied in tight knots... unbinding）均在引语中；无截短。读者视角提示中"被丝带勒住的喉咙""锤子睡进枕头底下"为跨章/本章其他处呼应（第 159 行 the hammer thumped... / slept with the hammer under her pillow），属分析引证、非引语缺失。
- **关键词回查**：clotted up in her throat / the unacceptable part / as revelation 均在引语中找到。
- **结构**：五项齐全。通过。

## 备注
- 本章共 4 个引语块，均逐字命中、说话人归属正确、关键词回查通过、引语未被截短。
- 分析中引用的"七十五镑/每年""必须先感恩才配得上""从不道谢"等属同章其他段落真实文本（第 40、52、67 行），作为分析呼应而非引语块内容，属正常做法，非幻觉。
- 未发现跨章章号错标、说话人反转、引语截短等问题。

ch08 完成：4 块，缺陷 0，待复核 0
---

# d 步二审 · ch09

## 结论：共 4 块，通过 4，缺陷 0，待复核 0

## 缺陷清单（无则写"无"）：无

## 待人工复核

无。

## 逐块核对记录

### 原句 1（md 行 21）
- 引语逐字：与 text 行 13 完全一致（含 "When I am a married lady,” said Jeannette, “I shall have a curricle..." 全段）✓
- 说话人：首句为 Jeannette 所说（text 行 13 明确 "said Jeannette"）；Henrie was impressed ✓。中文理解归给"九岁的 Jeannette"正确。
- 引语↔分析：关键词 a married lady / curricle / impressed 均在引语内命中 ✓；"为什么这样写"谈 Jeannette 幻想对照 Henrie 想象力天花板，对应引语后半段 Henrie "never thought" ✓。无截短。
- 年龄：Jeannette 九岁——text 行 31 "You are nine." ✓，与 text 行 16 "At sixteen and nine" 一致。

### 原句 2（md 行 33）
- 引语逐字：与 text 行 37 一致 ✓
- 说话人：此段为 Henrie 所说。text 行 34 "Jeannette let out a loud peel of laughter... Henrie elaborated." 后接行 37 整段（含 "They considered in silence as Jeannette pulled the metal comb..." 夹层后仍接 Henrie 的 Jenkins 话）✓。中文理解归给 Henrie 正确。
- 引语↔分析：关键词 to have been married / the being / devils 均在引语内命中 ✓；"为什么这样写"讲完成时 vs 进行时的语法缝，对应 the being ✓。引语含两个引号段，中文理解两段均覆盖，无截短 ✓。
- 年龄：读者视角提示"早在十六岁"→ Henrie 十六岁，text 行 16 "At sixteen and nine" ✓ 有支撑。

### 原句 3（md 行 45）
- 引语逐字：与 text 行 52 一致 ✓
- 说话人：叙述者/聚焦 Henrie 所见（"Henrie saw her face darken with shame"），Mrs. Bates 是对象 ✓。中文理解归给 Mrs. Bates（脸因羞耻沉下）+ Henrie（看见）正确。
- 引语↔分析：关键词 darken with shame / covered it up 均命中 ✓；"为什么这样写"讲父亲失控公开、母亲体面防御工事，对应钢琴/赌债背景（text 行 49-52）✓。无截短。

### 原句 4（md 行 57）
- 引语逐字：与 text 行 71 一致 ✓
- 说话人：叙述者，Henrie 伸向 Jeannette ✓。中文理解归给 Henrie 正确。
- 引语↔分析：关键词 couldn't sleep / reach across / hold her hand 均命中 ✓；"为什么这样写"讲全章热闹收束到无声动作，与"和 Jeannette 这样过下去"（text 行 67）呼应 ✓。无截短。

## 数字断言专项核查
- "Henrie 十六岁、Jeannette 九岁"（md 行 12/41/83）：text 行 16 "At sixteen and nine, they were allowed to take the gig out..." ✓；Jeannette 九岁另见 text 行 31 "You are nine." ✓。年龄断言均有原文支撑，无"数字断言无支撑"问题。

## 结构
- 4 块，每块引语行 + 中文理解 / 关键词 / 为什么这样写 / 读者视角提示 四子项齐全 ✓
- 无孤儿块、无重复块、无跨章章号错标（本章为 Chapter 7，导航与 frontmatter 一致）。

ch09 完成：4 块，缺陷 0，待复核 0
---

# d 步二审 · ch10

## 结论：共 3 块，通过 3，缺陷 0，待复核 1

核对基准：精读 md `notes/books/novels/miss-bates-by-catherine-cliff/ch10 the cap.md`（正文标 **Chapter 8**，frontmatter 标题 `Chapter 8（Part One: 1769–1795）`）↔ 原文 `text/ch10_chapter_8.txt`（页首 "Chapter 8"）。章号一致，无跨章错标。

逐块核对：

### 块 1 · 原句 1（引语行在第 21 行，中文理解在第 23 行，相邻）
- **逐字核对**：text 第 13 行 "The cap, she had discovered, was a magical cloak of total invisibility; once affixed, hardly any young man was presented for a dance of pity." — 逐字命中，实词无改写。✓
- **说话人**：命中窗口为描述 Henrie 的第三人称叙述（紧接 "Henrie had already been wearing a cap…"），确为 Henrie 的发现。中文理解归因"她发现"正确。✓
- **引语↔分析对应**：中文理解/关键词（magical cloak, invisibility, dance of pity 均在引语内）/为什么这样写（隐身衣→成人社交规则、dance of pity 冷搭配）/读者视角提示（自嘲反写、frog-marched 呼应同句语境）都围绕同一句引语；引语完整未截短。✓
- **关键词回查**：magical cloak / total invisibility / dance of pity 逐字在引语内。✓
- **结构**：引语行 + 中文理解 + 关键词 + 为什么这样写 + 读者视角提示 齐全。✓

### 块 2 · 原句 2（引语行第 33 行，中文理解第 35 行，相邻）
- **逐字核对**：text 第 19 行 "The cap was a victory, not a surrender, an end to the battle of trying to look like a potential partner for any young man. With it, she lay down the burden of being a young woman who did not satisfy." — 逐字命中。✓
- **说话人**：命中窗口紧接 "And when she first donned her cap, a few older women said… But this was not what she wanted. The cap was a victory…"，归 Henrie。中文理解归因"她/她放下了"正确（注意窗口内的 older women 引言已被引号包裹、不属本句，未被误归）。✓
- **引语↔分析对应**：为什么这样写拆解 a victory, not a surrender 对折句式 + battle/burden 战争意象 + did not satisfy，全部落在本句引语内；引语完整未截短。✓
- **关键词回查**：a victory, not a surrender / the burden 逐字在引语内。✓
- **结构**：五要素齐全。✓

### 块 3 · 原句 3（引语行第 45 行，中文理解第 47 行，相邻）
- **逐字核对**：text 第 28 行（章末）"For while she had Jeannette, she was not a spinster. She was a sister." — 逐字命中。✓
- **说话人**：命中窗口位于章末 Henrie 视角段落结尾（"while Henrie tried to detangle her work basket…"），归 Henrie。中文理解归因"她/她是姐姐"正确。✓
- **引语↔分析对应**：为什么这样写（spinster/sister 只差两字母、while 埋脆弱、有条件的身份）与读者视角提示（对照《爱玛》Miss Bates）都扣住本句；引语完整未截短。✓
- **关键词回查**：spinster / sister / while 逐字在引语内。✓
- **结构**：五要素齐全。✓

## 缺陷清单（无）

## 待人工复核

1. **原句 1 中文理解的 `presented` 译法（翻译取舍，非缺陷）**：原句 "hardly any young man was presented for a dance of pity" 中 `presented` 偏"被呈献/被推到"，中文理解译作"被'介绍'过来"，属轻度意译（用引号提示非字面），意思方向不偏，但严格字面为"被献上/被拉来跳一支舞"。建议如需更贴字面可改"几乎再没有哪个年轻男子会被'献'到她面前，和她跳一支出于怜悯的舞"；不必改也可。

---

ch10 完成：3 块，缺陷 0，待复核 1
---

# d 步二审 · ch11

## 结论：共 4 块，通过 4，缺陷 0，待复核 0

逐块核对结果（引语逐字 / 说话人 / 引语↔分析对应 / 关键词回查 / 结构）：

### 原句 1
- **引语逐字**：与 `text/ch11_chapter_9.txt` 第 13 段逐字一致（"But when she was eighteen, Jeannette met someone worth dancing with twice. … All of Highbury was interested and happy to see such beautiful young people so becomingly in love."）。引语完整，未截短。
- **说话人**：叙述性段落（贴近 Henrie 视角的第三人称叙述），与「中文理解」的叙述口吻归因一致。
- **引语↔分析对应**：中文理解、关键词、为什么这样写、读者视角提示均围绕同一句引语（舞会相遇），对应正确；无截短。
- **关键词回查**：worth dancing with twice / switched his attention / twirled 均在引语中找到。
- **结构**：引语行 + 中文理解 + 关键词 + 为什么这样写 + 读者视角提示，五要素齐全。

### 原句 2
- **引语逐字**：与 text 第 25 段逐字一致（弯引号差异、省略号两侧原词均合规）。
- **说话人**：Mrs. Otway 所说（"Yes," Mrs. Otway said, pulling Henrie back onto her track, "but Miss Jane Bates was so dazzling with her green ribbons…"）。text 前后窗口确认说话人正确，**未出现说话人反转**。
- **引语↔分析对应**：中文理解正确归因为 Mrs. Otway 的闲话；"刀子般的眼神"对应引语 "a look that felt pointed and dangerous, like a knife"；章末心愿 "Don't let me lose Jeannette so soon" 与读者视角提示一致。引语完整未截短。
- **关键词回查**：dazzling / a strong shine / like a knife 均在引语中找到。
- **结构**：五要素齐全。

### 原句 3
- **引语逐字**：与 text 第 73 段逐字一致（"Could there be anything more shameful than finding that the life you treasure … with her entreaties."）。
- **说话人**：Henrie 的内心独白/叙述段，与「中文理解」的 Henrie 自我审判归因一致。
- **引语↔分析对应**：中文理解逐句对应引语；"她是多么彻头彻尾的傻瓜"对应 "What an absolute fool she was"；"把妹妹越推越远"对应 "repelling her sister … with her entreaties"。引语完整未截短。
- **关键词回查**：desperate to escape / her lot / entreaties 均在引语中找到。
- **结构**：五要素齐全。

### 原句 4
- **引语逐字**：与 text 第 79 段逐字一致（""I'm so silly. … but now the spiky weeds were creeping back in."），起于 Jeannette 台词，含 Henrie 内心叙述，完整未截短。
- **说话人**：前半为 Jeannette 台词（"I'm so silly…"），后半为 Henrie 的叙述与内心暗愿（"May Lieutenant Fairfax, George, spend his last breath fighting for England…"）。中文理解与读者视角提示均正确归因，未混搭无关分析行。
- **引语↔分析对应**：中文理解逐句对应；"心灵的花园/带刺的杂草"对应 "the garden of her mind … the spiky weeds were creeping back in"；"拍下去、踩上去"对应 "She batted the thought down, stomped on it"。对应正确。
- **关键词回查**：irrepressibly / batted the thought down / spiky weeds 均在引语中找到。
- **结构**：五要素齐全。

### 年龄数字核实（十八岁）
- 「十八岁的 Jeannette（Jane）」在 text 有原文支撑：第 13 段 "But when she was eighteen, Jeannette met someone worth dancing with twice."；另有第 98 段 "She and Jeannette had, for these eighteen years, been the joint sun of their solar system."。年龄断言**有支撑，非数字断言无支撑**。

### 结构总检
- 全章 4 个引语块，每块「引语行 + 中文理解 + 关键词 + 为什么这样写 + 读者视角提示」五要素齐全；无孤儿块、无重复块。
- 引语行与对应中文理解行均在同一 md 且相邻（同块内），未见跨块拼装。

## 缺陷清单（无则写"无"）

无

## 待人工复核

无

ch11 完成：4 块，缺陷 0，待复核 0
---

# d 步二审 · ch12

## 结论：共 4 块，通过 2，缺陷 1，待复核 1

- 通过：原句 2、原句 3（引语逐字、说话人、关键词、引语↔分析对应均无问题）
- 缺陷：原句 1（中文理解漏覆盖引语末句意象）
- 待人工复核：原句 4（中文理解末句为分析延伸）

## 各块逐对核对明细

### 原句 1
- **引语逐字**：与 text/ch12_chapter_10.txt 第 16 行逐字一致（仅弯/直引号与破折号差异），允许。
- **说话人**：命中处为第三人称叙述（描述 Henrie 看清自己），窗口前后为同一叙述段；中文理解归因于"Henrie 第一次看清自己的脸"，正确。
- **关键词**：spectacles ✓、Devastating ✓、pockmarks ✓，均在引语中找到。
- **引语↔分析对应 / 截短**：中文理解覆盖"麻点、小胡子、乱发"及"奇迹→毁灭"翻转，但**未覆盖引语末句 "A nose like a Gloucestershire Old Spot."**（鼻子＋老花斑猪）。"为什么这样写"提到"乡村世界的粗粝意象（熊、猪）"，其中"猪"在意象层面间接呼应 Old Spot（格洛斯特郡老花斑猪），但"鼻子"这一实词在中文理解中确未翻译。→ **缺陷**。

### 原句 2
- **引语逐字**：与 text 第 19 行逐字一致。
- **说话人**：叙述/Henrie 的感知段，中文理解归"别人根本不看她"，正确。
- **关键词**：resolved themselves into faces ✓、skidded away ✓、make her disappear ✓。
- **引语↔分析**：中文理解、为什么这样写、读者视角均围绕同一段引语（看清别人目光→被无视→不停说话维持存在），对应完整，未截短。**通过**。

### 原句 3
- **引语逐字**：与 text 第 39 行逐字一致（内部 "As you know," 等直/弯引号差异允许）。
- **说话人**：律师 Mr. Cole 带来的消息＋叙述描述，中文理解归 Mr. Cole / 母女处境，正确。
- **关键词**：dire position ✓、assumed a level of knowledge ✓、the panic rising ✓。
- **引语↔分析**：中文理解覆盖全段并作综合（"父亲之死不是最痛的一击…破产宣判"），属合理分析，未截短。**通过**。

### 原句 4
- **引语逐字**：与 text 第 60 行逐字一致（"Then he said, 'That money has been spent…'"，直/弯引号差异允许）。
- **说话人**：命中处为 Mr. Cole（律师）的说话＋其后叙述 "Again, Mr. Cole busied himself…"，中文理解归 Mr. Cole，正确。
- **关键词**：considerable ✓、undertaken ✓、busied himself ✓（"busied himself with reshuffling"）。
- **引语↔分析 / 截短**：中文理解末句「而债主们用另一种方式把她计算在家之外」在引语中**无直接对应**；引语仅有 "A further loan was undertaken for Mrs. Fairfax's portion."。该句为对"Mrs. Fairfax's portion"（Jeannette 在账本中仅余"嫁妆"一栏）的主题延伸，非实词错译，但表述较抽象。读者视角提示亦重复此表述。→ **待人工复核**。

## 缺陷清单

**缺陷 1 · 引语↔分析覆盖不对应（中文理解漏译末句实词意象）**
- 类型：引语截短/分析漏覆盖
- 引语行原文：`> **原句 1:** "The spectacles were miraculous; … And her hair grew just like a shaggy bear's—the young scholars had been right; Mrs. Mott had not exaggerated. A nose like a Gloucestershire Old Spot."`
- 中文理解原文：`妹妹寄来的眼镜本是善意，却让 Henrie 第一次"看清"自己的脸——麻点、小胡子、乱发，全是她靠看不清而没受过的伤害。作者用"奇迹→毁灭"的一词翻转，把"获得视力"写成一场灾难。`
- 问题说明：中文理解列举"麻点、小胡子、乱发"，未覆盖引语末尾 "A nose like a Gloucestershire Old Spot"（鼻子＋格洛斯特郡老花斑猪）。"为什么这样写"的"熊、猪"在意象层面对"猪"有间接呼应，但"鼻子"这一实词未被中文理解翻译，末句引语实际被落下。
- 建议修法：在中文理解补一句，例如「……乱发、还有一只像格洛斯特郡老花斑猪那样的鼻子，全是她靠看不清而没受过的伤害」，使引语末句意象得到覆盖。

## 待人工复核

**待复核 1 · 原句 4 中文理解末句为分析延伸**
- 引语行原文：`> **原句 4:** "Then he said, "That money has been spent every year, and more besides. The debts are considerable. A further loan was undertaken for Mrs. Fairfax's portion. I often said to your husband that he should be careful. But here we are." Again, Mr. Cole busied himself with reshuffling his papers, his bushy eyebrows raised high."`
- 中文理解原文：`……而债主们用另一种方式把她计算在家之外。`
- 问题说明：引语本身无"债主们用另一种方式把她计算在家之外"的表述；此为对 "A further loan was undertaken for Mrs. Fairfax's portion" 的主题延伸（Jeannette 出嫁后在账本中仅余"嫁妆"一笔）。非实词错译，分析方向合理，但表述抽象、与引语字面无直接对应，请人工确认是否需加"（此为推论）"或改为更贴合引语的表述（如「她在账本中只剩'Mrs. Fairfax 的嫁妆'这一笔」）。

## 备注
- "为什么这样写"引用的 "sad silence that told the story before Mr. Cole did" 出自 text 第 57 行，属上下文引用而非本块引语，未计入缺陷。
- 无跨章章号错标、无说话人反转、无孤儿/重复块；结构上 4 块引语行＋中文理解/关键词/为什么这样写/读者视角提示齐全。

ch12 完成：4 块，缺陷 1，待复核 1
---

# d 步二审 · ch13

## 结论：共 4 块，通过 4，缺陷 0，待复核 1

## 缺陷清单

无

## 待人工复核

**块 4 · 原句 4 · 「为什么这样写」引用前文诅咒长句，本块引语不含咒文**

- **引语行原文**：
  > **原句 4:** "Henrie had taken the time to picture each possible outcome. A thrill went through her as she willed that choked gurgle into being."

- **中文理解原文**：
  > 她花时间把每一种可能的下场都想了一遍；当她"意念驱动"着那声被呛住的喉音成真时，一阵战栗般的兴奋贯穿了她。

- **问题说明**：
  「为什么这样写」称「前文她的诅咒是一整段华丽的长句咒文，这里收束到两个短句」，但本块引语只含两短句，未含咒文。经核对 **text/ch13_chapter_11.txt 第 55 行**，咒文确实存在，且在同一章、位于本块引语（第 64 行）之前——「前文」指代准确，非跨章或错位引用。因此该分析指向正确出处。
  存疑点：咒文段落（text 第 55 行，自 "After he left…" 至 "…gurgling out and never in."）内容重要且篇幅不小，精读 md 未将其列为独立引语块，导致块 4 读者仅凭本块无法看到被分析所引用的咒文原文。这是体例问题（是否应补一引语块），非事实性缺陷。
- **建议修法**：可不改（分析事实正确）；若要提升可读性，可在原句 3 与原句 4 之间补一引语块收录完整咒文，或在块 4 的「为什么这样写」后加括注「见前文咒文（text 第 55 行）」。建议人工复核后再决定。

---

### 逐块核对明细

**块 1 · 原句 1**
- 引语逐字：text 第 13 行首三句，逐字一致 ✓
- 说话人：第三人称贴身叙事 Henrie，中文理解归因正确 ✓
- 引语↔分析：中文理解/关键词/为什么这样写/读者视角提示均围绕同一段（眼镜、鼻伤、疲态）✓
- 关键词回查：spectacles / tender / blow 均在引语 ✓
- 结构：引语行+四子项齐全 ✓

**块 2 · 原句 2**
- 引语逐字：text 第 16 行末句，逐字一致（含破折号、逗号）✓
- 说话人：第三人称叙事，描述邻居行为，归因正确 ✓
- 引语↔分析：中文理解与四子项均围绕"邻居翻检+地位翻转"同一句 ✓
- 关键词回查：paw through / preceded into dinner / envy 均在引语 ✓
- 结构：齐全 ✓
- 截短检查：引语为该段末句，自成完整语义单元，未截去支撑分析的成分 ✓

**块 3 · 原句 3**
- 引语逐字：text 第 52 行整段，逐字一致 ✓
- 说话人：Henrie 事后卧房内心独白（第三人称贴身），归因正确 ✓
- 引语↔分析：中文理解与四子项均围绕同一段（排除医生/律师、指向拍卖师）✓
- 关键词回查：resentment / contained / watching the door 均在引语 ✓
- 结构：齐全 ✓

**块 4 · 原句 4**
- 引语逐字：text 第 64 行整段，逐字一致 ✓
- 说话人：Henrie 事后回想（第三人称贴身），归因正确 ✓
- 引语↔分析：中文理解与四子项均围绕同一段（意念/喉音/战栗）；「为什么这样写」引用的前文咒文经核实位于同章第 55 行，指代正确，详见"待人工复核" ✓
- 关键词回查：thrill / willed / gurgle 均在引语 ✓
- 结构：齐全 ✓

---

ch13 完成：4 块，缺陷 0，待复核 1
---

# d 步二审 · ch14

## 结论：共 4 块，通过 4，缺陷 0，待复核 0

审查范围：Chapter 12（Part One: 1769–1795）· 精读「原句 1–4」四个引语块，逐对核对引语逐字 / 说话人 / 引语↔分析对应 / 关键词回查 / 结构。

对照来源：`notes/books/novels/miss-bates-by-catherine-cliff/text/ch14_chapter_12.txt`（Chapter 12）

## 逐块核对明细

### 原句 1（md 第 21 行 ↔ text 第 13 行）
- **引语逐字**：一致（逐字全同，无实词改写）。
- **说话人**：叙述者陈述句，非对话；中文理解「母女俩很少收到她的音信」归因叙述正确，未见说话人反转。
- **引语↔分析**：中文理解/为什么这样写/读者视角提示均围绕同一句；引语未被截短。
- **关键词**：infrequently ✓、expensively ✓、three years of life she had left ✓，均在本块引语内命中。
- **结论**：通过。

### 原句 2（md 第 33 行 ↔ text 第 20 行）
- **引语逐字**：一致（逐字全同）。
- **说话人**：Henrie 写给 Jeannette 的信件段落（"I suppose I must now say, Mrs. Woodhouse"、"you know that giant creaky barouche he has"）；中文理解已标注「（Henrie 写给 Jeannette 的信）」，归因正确。
- **引语↔分析**：分析中「该改口叫太太」对应引语 "I suppose I must now say, Mrs. Woodhouse"；「袋中猪」对应 "a pig being taken to market in a poke"；无截短。
- **关键词**：barouche ✓、a pig being taken to market in a poke ✓、new position ✓，均命中。
- **结论**：通过。

### 原句 3（md 第 45 行 ↔ text 第 77 行）
- **引语逐字**：一致（逐字全同）。
- **说话人**：叙述者陈述句；中文理解「费尔法克斯中尉的战友坎贝尔上尉……写来了信」归因正确。
- **引语↔分析**：分析中「炮弹/弹道/慢镜头」对应 "cannon-shot"/"excruciatingly slowly"；「七周」呼应同段 text 中 "It was dated seven weeks previous to their receipt"（引语截在炮弹比喻句，未覆盖七周细节，但分析并未声称该细节出自引语本身，故不构成截短）；无实质问题。
- **关键词**：cannon-shot ✓、excruciatingly slowly ✓、devastating ✓，均命中。
- **结论**：通过。

### 原句 4（md 第 57 行 ↔ text 第 98 行）
- **引语逐字**：一致（逐字全同）。
- **说话人**：叙述者陈述句，系 Part One 终句；中文理解「那颗炮弹骤然加速……击倒在地」归因正确。
- **引语↔分析**：分析中「sped up/先穿过母亲再击倒 Henrie/木刺扎面颊」均对应引语原文，无截短。
- **关键词**：cannonball ✓、tore through ✓、splinters ✓，均命中。
- **结论**：通过。

## 结构检查
- 每块「引语行 + 中文理解/关键词/为什么这样写/读者视角提示」四子项齐全。
- 无孤儿块、无重复块、无跨块错配；引语行与中文理解行均在同一 md 相邻，未与无关分析拼装。
- 章号标注：md 为 Chapter 12（Part One），与 text 文件头 "Chapter 12" 一致，无跨章章号错标。

## 缺陷清单
无

## 待人工复核
无

ch14 完成：4 块，缺陷 0，待复核 0
---

# d 步二审 · ch15

## 结论：共 4 块，通过 4，缺陷 0，待复核 2

**核对基准说明**：任务给定路径 `text/ch15_chapter_13.txt` 在 text/ 下不存在；该目录中实际文件为 `text/ch15_chapter_1.txt`，且精读 md 自述提取件为 `text/ch15_chapter_1.txt`（见 md 第 8 行）。本次以 `text/ch15_chapter_1.txt` 为原文基准核对（内容与 md 完全对应）。此路径差异见「待人工复核」第 3 条。

| 块 | 引语逐字 | 说话人 | 引语↔分析 | 关键词回查 | 结构 | 判定 |
|---|---|---|---|---|---|---|
| 原句 1 | ✅ 命中 text 第 14 行 | ✅ 母亲（叙事描写） | ✅ | ✅ shears / stricken / sash 均在引语 | ✅ | 通过 |
| 原句 2 | ✅ 命中 text 第 26 行 | ✅ 母女摊牌（叙事+前文对白对照） | ✅ | ✅ a rare, true thing / take back / trunks 均在引语 | ✅ | 通过 |
| 原句 3 | ✅ 命中 text 第 42 行 | ✅ Henrie 做娃娃（叙事） | ✅ | ✅ simulacrum / tidbits / burial 均在引语 | ✅ | 通过 |
| 原句 4 | ✅ 命中 text 第 105 行 | ✅ Henrie 深夜幻想（叙事） | ✅ | ✅ mallet / unblemished / beads 均在引语 | ✅ | 通过 |

## 缺陷清单

无。

（逐项已核对：四条引语行均在 text/ch15_chapter_1.txt 中逐字命中，仅标点（弯/直引号、省略号两侧）差异；无实词改写；无引语截短——每条引语均为完整句，足以支撑其「中文理解」「为什么这样写」的分析。）

## 待人工复核

1. **原句 1 · 读者视角提示越出引语块**
   - 引语行原文：`> **原句 1:** "Her mother stood beside the deal table, ... but she wouldn't give it up."`（止于第 14 行）
   - 读者视角提示原文：「注意 Henrie 伸手去碰裙子却被母亲挥剪喝止的细节……」
   - 问题说明：该细节出自 text 第 17 行（She put out a hand to touch the dress, but her mother snatched it away, brandishing the shears at her…），位于引语块**之外**（紧邻其后）。这是指向下一句的前瞻提示，非引语截短，属常见手法；但因不在引语块内，请人工确认是否属意如此。
   - 建议修法：无需改；如求严格可注明「下句」。

2. **原句 4 · 读者视角提示「前一句」指代**
   - 引语行原文：`> **原句 4:** "Sometimes, when Henrie couldn't sleep, ... remove any risk."`（text 第 105 行）
   - 读者视角提示原文：「结合前一句能读出更冷的一层……她把自己能给的都列完了，却发现不够；这个'不够'正是章末转向命运的起点。」
   - 问题说明：「不够」实指**引语之后**的 text 第 108 行（But she knew it was not enough…），属章末后续句，而非「前一句」。指代方向用词与原文位置略有出入。
   - 建议修法：将「前一句」改为「本章末尾一句」或「下文一句」。

3. **原文提取件路径**
   - 问题说明：任务指定的 `text/ch15_chapter_13.txt` 不存在；实际提取件为 `text/ch15_chapter_1.txt`，精读 md 第 8 行也正确引用后者。内容与 md 完全对应，无章号错标（md 标题「Chapter 1（Part Two: 1795–1811）」与 text 首行「Chapter 1」一致）。仅为路径记录差异，非内容缺陷。
   - 建议修法：核对任务参数路径是否笔误。

---

ch15 完成：4 块，缺陷 0，待复核 2
---

# d 步二审 · ch16

## 结论：共 4 块，通过 4，缺陷 0，待复核 0

## 缺陷清单
无

## 待人工复核
无

---

### 核对说明

- **绝对路径使用的提取件**：md 内 frontmatter 声明 `提取件：text/ch16_chapter_2.txt`，实际文件为
  `/Users/jcxs2014/Documents/Works/EnglishRead/notes/books/novels/miss-bates-by-catherine-cliff/text/ch16_chapter_2.txt`
  （任务描述中给的 `ch16_chapter_14.txt` 不存在，已按 md 声明的正确文件名核对）。

**原句 1**
- 引语逐字：text 第 16 段逐字命中（含 Jeannette 直接引语嵌套双引号）。✓
- 说话人：叙述者/Jeannette 回忆段落，归因正确。✓
- 关键词：unravel / knitting / pick up the pattern 全部在本块引语内命中。✓
- 分析对应：中文理解逐句对应「退回去拆毛线→重织感恩与温顺」；为什么这样写把「gratitude and meekness」处理成必须维持的花纹，与引语吻合。✓
- 结构：引语行+中文理解+关键词+为什么这样写+读者视角提示 齐全，无截短。✓

**原句 2**
- 引语逐字：text 第 28 段逐字命中。✓
- 说话人：Henrie 视角的叙述段（Jane 在 cottage 的照料动作），归因正确。✓
- 关键词：caretaking / ailing / shied away 全部在本块引语内命中。✓
- 分析对应：中文理解与引语一致；为什么这样写对「strong, competent Jeannette」破折号反复的解读贴合原文；读者视角提示「Jane 几乎从不提起」的伏笔合理。✓

**原句 3**
- 引语逐字：text 第 40 段逐字命中。✓
- 说话人：Henrie 视角叙述，归因正确。✓
- 关键词：tugging / struggling / feet 全部命中。✓
- 分析对应：为什么这样写引用的「If only Jane's feet didn't grow quite so vigorously」确在 text 第 13 段；读者视角提示与引语/上文呼应。✓

**原句 4**
- 引语逐字：text 第 68 段逐字命中。✓
- 说话人：Henrie 想象段（第三人称贴身跟随），归因正确。✓
- 关键词：pantomime of complaisance / unconstrained / just be 全部命中。✓
- 分析对应：中文理解逐项对应；为什么这样写对「hopefully, dead」「smile-free women」「just be」的解读均有原文支撑；读者视角提示引用的「despite her frequent and voluble protestations」在 text 第 74 段命中。✓

### 年龄数字断言核查
- md 导航写「五岁的 Jane」，text 第 19 段「So, wasn't it lucky that Jane, five now, was growing so well?」明确支撑「Jane, five now」。→ **数字断言有原文支撑，非幻觉。** ✓

ch16 完成：4 块，缺陷 0，待复核 0
---

# d 步二审 · ch17

**审查对象**：`notes/books/novels/miss-bates-by-catherine-cliff/ch17 in the churchyard.md`（精读）
**对照原文提取件**：`notes/books/novels/miss-bates-by-catherine-cliff/text/ch17_chapter_3.txt`

> 说明：任务给定路径 `text/ch17_chapter_15.txt` 不存在，实际提取件为 `text/ch17_chapter_3.txt`，且精读 md 头部自引即为 `text/ch17_chapter_3.txt`，二者一致；原文件头为 "Chapter 3"，内容起于 "3"，与 md 标注 "Chapter 3（Part Two: 1795–1811）" 相符，章号无错标。

## 结论：共 4 块，通过 4，缺陷 0，待复核 0

## 缺陷清单（无则写"无"）

无

## 逐块核对明细

### 块 1 · 原句 1（教堂墓地 + Hartfield 改名）

- **引语逐字**：逐字命中原文 line 13，一致（含弯引号"Hartfield"）。✓
- **说话人正确**：原文为叙述性段落，讲述 Mrs. Woodhouse 在教堂墓地谈论"Hartfield"宴客，以及 Lavinia Mott 自称考据出真名 Hatfield 六年未流行、只有当面才叫、Mr. Knightley 不理会。中文理解将其归因为 Lavinia/镇上人的态度，与原文一致。✓
- **引语↔分析对应**：中文理解与为什么这样写都在讲"改名虚荣"与镇上人敷衍态度，指向同一句引语，无截短。✓
- **关键词回查**：`claimed`（line 13 "Lavinia Mott had claimed"）、`entertaining`（line 13）、`Mr. Knightley`（line 13）均在引语中。✓
- **结构**：引语行 + 中文理解 + 关键词 + 为什么这样写 + 读者视角提示，齐全。✓

### 块 2 · 原句 2（Lavinia 给 Emma 找朋友）

- **引语逐字**：逐字命中原文 line 34（含括号内对比句、`visitors’ calls` 弯撇号）。✓
- **说话人正确**：原文为叙述段，讲 Lavinia 脱身来找 Bates 家、想给 Emma 找朋友、据说并不享受带孩子、Henrie 见小 Emma 拧母亲、Jane 会是好影响（唱赞美诗好、安静、常读书）。中文理解正确归因为 Lavinia 的算计与 Henrie 观察，无说话人反转。✓
- **引语↔分析对应**：为什么这样写讲"友谊开端是算用""a pinch"细节"括号对比"，均在讲同一句引语，无截短。✓
- **关键词回查**：`a friend`（"to have a friend"）、`a good influence`（"would be a good influence"）、`a pinch`（"giving her mother a pinch"）均在引语中。✓
- **结构**：齐全。✓

### 块 3 · 原句 3（猜数字游戏）

- **引语逐字**：逐字命中原文 line 43（数字序列、引号内 honor system）。✓
- **说话人正确**：原文为 Jane 回家转述的猜数字游戏叙述段，讲 Emma 让 Jane 猜数、拒写下来讲"荣誉规则"、Jane 一股劲猜几乎不中、规则十五次、Emma 猜时范围缩到 1–20 常第十次就中并自称先知。中文理解归因正确。✓
- **引语↔分析对应**：为什么这样写讲"规则不对等""荣誉是奢侈品""mysteriously changed"，均指向同一句引语，无截短。✓
- **关键词回查**：`the honor system`、`doggedly`、`a seer` 均在引语中；`mysteriously changed` 亦在引语（分析中呼应）。✓
- **结构**：齐全。✓

### 块 4 · 原句 4（押韵谜语与 Henrie 的羞愧）

- **引语逐字**：逐字命中原文 line 78（含引号"Right you are, my love."）。✓
- **说话人正确**：原文该句为 Henrie 对 Jane 的回应，随后"Henrie was thinking about the riddle and felt a prickling of shame…spinster with a rhyme"为紧跟 Henrie 的叙述。中文理解归因为 Henrie 因谜语（"我说话说个不停、永远不停止"）而起羞愧，正确。✓
- **引语↔分析对应**：为什么这样写讲镇上人把 Henrie=话痨老姑娘编成韵语、谜语诗行，指向同一句引语；引语未截短。分析引用的谜语诗行 "My nose is that of a pig / I talk and I talk / And never will stop" 可在原文 line 59–68 找到（原文为"My nose is that of a pig / In a copse so shady. / I talk and I talk / And never will stop."），分析在诗行中省略了"In a copse so shady"，属分析性引用省略，不构成引语逐字改写，且未歪曲原意。✓
- **关键词回查**：`the riddle`、`a prickling of shame`、`a spinster with a rhyme` 均在引语中。✓
- **结构**：齐全。✓

## 附：词汇表例句抽查（非任务核对范围，附注）

本章词汇表的 11 条例句均能在原文找到并逐字一致（vivacity/line 37、overbearing/line 40、doggedly/line 43、stoicism/line 85、exhibitionist/line 37、homebody/line 37、tippet/line 46、vestibule/line 22、riddles/line 49、embarrassing/line 40、shrieking/line 88），无拼装或改字。

## 待人工复核

无

---

ch17 完成：4 块，缺陷 0，待复核 0
---

# d 步二审 · ch18

## 结论：共 4 块，通过 4，缺陷 0，待复核 1

核对基准文本：`notes/books/novels/miss-bates-by-catherine-cliff/text/ch18_chapter_4.txt`（Chapter 4）
（说明：本任务下发的 text 路径写作 `ch18_chapter_16.txt`，实际该目录下存在的是 `ch18_chapter_4.txt`；md 前言的 `提取件：text/ch18_chapter_4.txt` 与文本文件一致，故按实际存在的 `ch18_chapter_4.txt` 核对。）

---

## 逐块核对

### 原句 1（md 第 21 行）
- **引语逐字**：与 text 第 13 行完全一致（逗号、破折号、词序均同）。✔
- **说话人**：第三人称贴身叙述（Henrie 内心），非角色对白；"中文理解"按叙述视角归因，正确。✔
- **引语↔分析对应**："开篇把还礼写成难过的事 / 借要不要改名接上假名梗 / 比作卡珊德拉预示威胁"均在讲同一句引语内容，无截短。✔
- **关键词回查**：hospitality（引语第 2 词）、anxiety（引语中段）、Cassandra（引语中段）——三词均在引语逐字命中。✔
- **结构**：引语行 + 中文理解 + 关键词 + 为什么这样写 + 读者视角提示 齐全。✔

### 原句 2（md 第 33 行）
- **引语逐字**：与 text 第 41 行完全一致。✔
- **说话人**：叙述句（Henrie 视角描述 Emma 到场），非角色对白；"中文理解"按叙述归因，正确。✔
- **引语↔分析对应**：短促节奏、天气落空、"No walk in the mizzle"反讽客套——均对应引语内容。无截短。✔
- **关键词回查**：coach、mizzle、governess 均在引语中逐字出现。✔
- **结构**：五子项齐全。✔
- 附：读者视角提示称"接在 Henrie 剪玫瑰、刺破手指的段落之后"，text 中剪玫瑰/刺破手指在第 34、37 行，coach 段在第 41 行，顺序正确。✔

### 原句 3（md 第 45 行）
- **引语逐字**：与 text 第 80 行开头部分一致，直到"…doing a slight motion with her hands."（text 第 80 行同位置）。✔
- **说话人**：引语以 Emma 的童言对白起头，其后为叙述；"中文理解"归 Emma，正确；Mrs. Bates 那句"这孩子到底在暗示什么？"确为 text 第 80 行 Mrs. Bates 所说。✔
- **引语↔分析对应**：晾衣绳对比、Henrie 感激、三重羞耻分工、Mrs. Bates 端架子——均对应引语内容。⚠ 见待复核项（"学搓床单"手势暗示未含在引语内）。
- **关键词回查**：lines and lines、ashamed、hauteur 均在引语中。✔
- **结构**：五子项齐全。✔

### 原句 4（md 第 57 行）
- **引语逐字**：与 text 第 111 行 Jane 的整段复述一致。✔
- **说话人**：Jane 对 Henrie（Aunt Henny）说话。⚠ 说话人归属需重点确认——"中文理解"明确写"Jane 哭着复述 Emma 在 Hartfield 对她的威胁"，归 Jane，正确。不是 Emma 本人说的。✔
- **引语↔分析对应**：钉子当匕首、脸僵成怪笑、"因为我从来不好好笑"报应理由——均对应引语内容。无截短。✔
- **关键词回查**：a dagger、gush、a monstrous smile 均在引语中。✔
- **结构**：五子项齐全。✔

---

## 缺陷清单（无则写"无"）

无。四块引语逐字、说话人、分析对应、关键词回查、结构均通过。

（说明：本任务下发的文本路径 `text/ch18_chapter_16.txt` 不存在，实际文件为 `text/ch18_chapter_4.txt`，与 md 前言一致；此为路径信息差，非本章内容缺陷。）

---

## 待人工复核

**待复核 1 · 原句 3 · 引语截短与"学搓床单"分析点的对应**
- 类型：引语边界（引语截短）
- 引语行原文：`> **原句 3:** "“They have lines and lines in their back garden to hang the washing to dry. I run in between them like a maze. The sheets smell so lovely. Do you have lines and lines in your back garden?” She leapt up and ran to the window. …Emma turned back to the room and walked very close by Henrie, paused in front of her, and cast a sly glance up, doing a slight motion with her hands."`
- 中文理解原文：`"…Emma 转回屋，紧挨着 Henrie 走过来，在她面前停下，偷偷往上瞄了一眼，手上做了个小动作。"`
- 问题说明：引语在 "doing a slight motion with her hands" 处截断，未包含 text 紧随其后的解释——"…again made a back-and-forth gesture with her hands like she was scrubbing a bedsheet along a washboard. She mouthed 'scrub, scrub'…"。而"为什么这样写"明确写道"Emma 随后的手势暗示（**学搓床单**）把'无意的童言'推进到有意刻薄的边界"，这一分析要点依赖引语之外、位于 text 第 80 行后段的内容；单看引语读者只能看到"slight motion"，看不出"学搓床单"的具体含义。引语截断处本身落在完整句子末尾，不是句中腰斩，因此不构成硬缺陷，但存在"引语短于其支撑的分析"的轻微迹象。
- 建议修法（供人工判断）：若确认引语应覆盖该分析点，可将引语下沿延伸至 text 第 80 行 "…She mouthed 'scrub, scrub' with a small smile and her eyebrows raised."；或将"为什么这样写"中"学搓床单"改为对引语内"slight motion with her hands"的保守表述，并把"学搓床单"作为引语外的补充说明处理。是否修改可由主编裁量，暂不定为缺陷。

---

ch18 完成：4 块，缺陷 0，待复核 1
---

# d 步二审 · ch19

## 结论：共 4 块，通过 4，缺陷 0，待复核 1

## 逐块核对结果

### 原句 1（md 第 21 行）
- **引语逐字**：`"Henrie would always do what was best for Jane—that was her guiding principle in life, was it not? She would be grateful and Jane would have choices."`
  - text/ch19_chapter_5.txt 第 40 行逐字命中（破折号、词序、标点一致）。✓
- **说话人正确**：本块为叙述者贴身第三人称描写 Henrie 的内心律法（独立成段），非对话。中文理解将其归为 Henrie 的指导原则，正确。✓
- **引语↔分析对应**：中文理解讲"自己吞下感激，替对方保留选择权"，正是该句内容；设问"was it not?"的自我盘问分析点（为什么这样写/读者视角提示）均针对同一句。无截短（引语完整）。✓
- **关键词回查**：guiding principle ✓、grateful ✓、choices ✓ 均在本块引语原词命中。✓

### 原句 2（md 第 33 行）
- **引语逐字**：`"Henrie tried to control her face and speak patiently. She squeezed the pleats of her dress hard but kept her voice level. "Mother, we cannot afford this cottage another year. We will have to move. Do you want Jane to live like that, her rooms closing smaller and ruder about her? At the Campbells', she will learn things, she will be properly educated. She will be prepared for her life, whatever that may be." Henrie did not say the word governess to her mother, but it skulked in the back of her mind like the unwelcome guest that lady so often was."`
  - text/ch19_chapter_5.txt 第 61 行起逐字命中（含内嵌 Henrie 的对话与叙述收尾）。✓
- **说话人正确**：内嵌引号"Mother, we cannot afford..."确为 Henrie 对母亲所说；前后叙述为 Henrie 内心动作。中文理解归为 Henrie 控制表情、劝说母亲，正确。✓
- **引语↔分析对应**：为什么这样写讲"攥紧裙褶""governess 用 skulk"——均在引语内。中文理解逐条对应（控制表情/裙褶/付不起/受正当教育/家庭女教师潜行）。引语在原句"unwelcome guest that lady so often was."处收束，后续"More optimistically..."未被纳入，但分析未依赖后续内容，非实质截短。✓
- **关键词回查**：governess ✓、skulked ✓、pleats ✓ 均在引语中（skulked 为原词、非词形变化）。✓

### 原句 3（md 第 45 行）
- **引语逐字**：`"Doesn't your hair look beautiful this evening—...—just like Emma Woodhouse!" Why, why, why had she said that? Always her words tumbled out of her mouth in the wrong direction by one hundred and eighty degrees, an inevitable tide."`
  - text/ch19_chapter_5.txt 第 88 行逐字命中（含连续破折号切分、内嵌对话与结尾叙述）。✓
- **说话人正确**：整段为 Henrie 对 Jane 的劝诱絮叨 + 叙述者接 Henrie 内心的懊悔；中文理解归为 Henrie 的话滚落一百八十度，正确。✓
- **引语↔分析对应**：中文理解"糖天天有、衣服同一家、学琴、像 Emma Woodhouse"逐项对应；为什么这样写讲"破折号切断半空""Emma Woodhouse 是地雷"均针对同一句。无截短。✓
- **关键词回查**：tumbled ✓、Emma Woodhouse ✓、tide ✓ 均在引语中。✓

### 原句 4（md 第 57 行）
- **引语逐字**：`"We shall miss you so much," Henrie whispered into the pink doll's saucer of her ear. ... her outline getting smaller and smaller through the coach's back window until she disappeared up the lane."`
  - text/ch19_chapter_5.txt 第 121 行逐字命中。✓
- **说话人正确**：内嵌对话为 Henrie 对 Jane 的耳语；叙述为送别场景。中文理解归为 Henrie 耳语、Jane 沉默上车，正确。✓
- **引语↔分析对应**：中文理解与为什么这样写（无眼神接触、closed in on itself、越缩越小）均出自同一句引语。无截短。✓
- **关键词回查**：outline ✓、saucer ✓、whispered ✓ 均在引语中。✓

## 结构检查
- 每块「引语行 + 中文理解 + 关键词 + 为什么这样写 + 读者视角提示」五要素齐全，无孤儿块、无重复块。✓

## 缺陷清单（无则写"无"）

无

## 待人工复核

- **"So simple and elegant, everything that is necessary"（呼应来源）**：该句确实存在于 text/ch19_chapter_5.txt 第 128 行，为 Henrie 向母亲描述搬进杂货店楼上新居时所说（"We are like snails; we carry our home upon our back! So simple and elegant, everything that is necessary, aren't we fortunate!"）。但本章 md（ch19 best for jane.md）的精读部分**未将其列为独立引语块**（仅设 原句 1–4，其中不含此句）。ch20「读者视角提示」称"上一章 Henrie 说的每一句 'so simple and elegant'"——本章 md 无对应引语块可核对逐字与说话人。按任务规则标为**待人工复核（呼应来源）**，不断定为缺陷；如确认 ch20 引用的即 text 第 128 行这句 Henrie 台词，则来源成立，但建议在 ch19 md 中补一条含该句的引语块，或确认 ch20 的引用指向 text 原文而非 ch19 md。

---

ch19 完成：4 块，缺陷 0，待复核 1
---

# d 步二审 · ch20

核对对象：
- 精读 md：`notes/books/novels/miss-bates-by-catherine-cliff/ch20 village living overstated.md`
- 原文提取件：`notes/books/novels/miss-bates-by-catherine-cliff/text/ch20_chapter_6.txt`

核对方法：对每一个引语块，逐字比对 text/ch20，grep 命中后在 text 前后 ~200 字符窗口确认说话人归属，再核对中文理解/为什么这样写/关键词/读者视角提示是否对应同一句引语，并检查截短。

## 结论：共 3 块，通过 3，缺陷 0，待复核 0

## 各块核对明细

### 块 1 · 原句 1
- **引语行**：`> **原句 1:** "Perhaps she had overstated the charm of village living to her mother."`
- **逐字核对**：text/ch20 第 13 行，逐字一致。✓
- **说话人**：该句为本章开篇的第三人称贴身叙事（Henrie 内心），中文理解归因「她之前对母亲把乡村生活的迷人之处说得太满了」正确。✓
- **引语↔分析对应**：中文理解、为什么这样写（"Perhaps"起头、最短句收拢上一章热情、骤然降温）均围绕同一句。关键词 overstated / charm 均在本句找到。✓
- **读者视角提示**：提示写明「上一章 Henrie 说的每一句 'so simple and elegant'」，明确指向上一章（跨章呼应，非本章引语）。经核对，本章 3 个引语块中均未把 "so simple and elegant" 列为本章引语，text/ch20 也查无此句——按任务规则，这是有意的跨章指向，非缺陷。✓
- **结构**：引语行 + 四子项齐全。✓

### 块 2 · 原句 2
- **引语行**：`> **原句 2:** "It had been no small feat getting Mother up the staircase from the street. ... yanked her up."`（完整长引语，含括号、对话、"滚桶上山"比喻、Mrs. Cole 设想、yanked）
- **逐字核对**：text/ch20 第 16 行，逐字一致（弯引号差异允许）。✓
- **说话人**：第三人称贴身叙事 + Henrie 对母亲说的话（"Well, won't we stay fit…" 等），中文理解归因「Henrie 从后面托扶、一边说话分散注意」正确。✓
- **引语↔分析对应**：中文理解覆盖窄梯、托扶、掩饰亲昵、鸟瞰设想、yanked；为什么这样写引用「滚桶上山」「必须掩饰的亲昵」（camouflage 括号）「yanked」——均在引语内。✓
- **关键词**：camouflage（引语括号内）、bird's-eye view、yanked 均在本块引语找到。✓
- **截短检查**：引语截至 "yanked her up."，text 第 16 行其后还有 "Keep going, Mother… behold!" 未纳入。分析未引用被截去部分，故不构成引语短于其所支撑的分析。✓
- **结构**：引语行 + 四子项齐全。✓

### 块 3 · 原句 3
- **引语行**：`> **原句 3:** "Behold was a bit grand for what they were looking at, she admitted. The room had two grimy windows, neither large. One faced the street and the other looked onto an alley where carriages and horses were kept. To the back of the room were two doors, each one leading to a small cupboard, which would be the ladies' bedrooms."`
- **逐字核对**：text/ch20 第 19 行，逐字一致。✓
- **说话人**：叙事 + "she admitted"，中文理解「她自己也承认」正确。✓
- **引语↔分析对应**：中文理解覆盖两窗、巷子、两橱柜卧室；为什么这样写引用 "Behold"（舞台腔，确出自上一段 text 第 16 行末尾 "…behold!"，作者用本段第一句自我拆台）、"cupboard"（储物空间）、"which would be the ladies' bedrooms"（平静将来时）——均在本块引语内。✓
- **关键词**：grimy、cupboard、behold 均在本块引语找到。✓
- **结构**：引语行 + 四子项齐全。✓

## 缺陷清单（无则写"无"）

无。

## 待人工复核

无。块 1 读者视角提示中 "so simple and elegant" 属明确标注「上一章」的跨章呼应，本章未将其列为引语，不构成缺陷；如需最终确认可核对 text/ch19 第 128 行，但不在本章二审范围。

ch20 完成：3 块，缺陷 0，待复核 0
---

# d 步二审 · ch21

## 结论：共 4 块，通过 4，缺陷 0，待复核 0

## 缺陷清单
无

### 逐块核对记录

**原句 1**
- 引语行：`> **原句 1:** "When Jane first sent letters from the Campbells’, they were a laundry list of privilege without any pleasure."`
- text/ch21 命中（第 13 行首句）：`When Jane first sent letters from the Campbells’, they were a laundry list of privilege without any pleasure.` ——逐字一致 ✓
- 说话人：为叙述句（非人物对话），描述 Jane 初到 Campbell 家所寄信件内容；「中文理解」归因于「Jane 刚从 Campbell 家寄信回来时，信里列的是一串特权清单」，与 text 一致 ✓
- 引语↔分析：中文理解列举的跳舞课/兜风/冰激凌/真丝纸娃娃来自 text 同一段落后续句，属对信内容的合理展开，引语本身为段落总起句，支撑关键词与分析，无截短 ✓
- 关键词回查：laundry list / privilege / pleasure 均在引语内 ✓
- 结构：引语行 + 中文理解 + 关键词 + 为什么这样写 + 读者视角提示，四子项齐全 ✓
- 读者视角提示「这句话是 Henrie（或叙述者）对信的读后感，不是信的原文」判断正确 ✓

**原句 2**
- 引语行：`> **原句 2:** "Henrie had begun to put spin on her readings of these to her mother in an effort to stave off the older woman’s infrequent-but-dire remarks. Today it did not work."`
- text/ch21 命中（第 19 行）：`Henrie had begun to put spin on her readings of these to her mother in an effort to stave off the older woman’s infrequent-but-dire remarks. Today it did not work.` ——逐字一致 ✓
- **特别关注确认：`dire` 确实在引语内**——位于 `infrequent-but-dire remarks`，非缺陷 ✓
- 说话人：叙述句，归因于 Henrie 读信时的润色行为；中文理解与 text 一致 ✓
- 引语↔分析：为什么这样写提到「Today it did not work」与后续 Mrs. Bates 台词冲击力，与引语一致；无截短 ✓
- 关键词回查：put spin / stave off / dire 均在引语内 ✓
- 结构：四子项齐全 ✓

**原句 3**
- 引语行：`> **原句 3:** "But there were many days when the callers didn’t come, and Henrie and her mother spent their hours in their room with nothing to do and nothing left to talk about. Which did not stop Henrie. She talked on and on, trying to scribble something, some existence, onto these blank days."`
- text/ch21 命中（第 47 行首部）：`But there were many days when the callers didn’t come, and Henrie and her mother spent their hours in their room with nothing to do and nothing left to talk about. Which did not stop Henrie. She talked on and on, trying to scribble something, some existence, onto these blank days.` ——逐字一致 ✓
- 说话人：叙述句，描述 Henrie 与母亲在无人来访日的状态；中文理解与 text 一致 ✓
- 引语↔分析：为什么这样写逐句剖析引语（空/执拗/诗眼），完全对应，无截短 ✓
- 关键词回查：nothing to do / scribble / blank days 均在引语内 ✓
- 结构：四子项齐全 ✓

**原句 4**
- 引语行：`> **原句 4:** "The rest of her visit was awash in the silence of her practicing with dedication and single-mindedness. They put the instrument away when callers were announced, but otherwise it was out and Jane was playing her voiceless piano. Henrie was mostly very happy, but also sometimes found her eyes filled with tears as she listened to the silent measure of her own meagerness."`
- text/ch21 命中（第 77 行）：`The rest of her visit was awash in the silence of her practicing with dedication and single-mindedness. They put the instrument away when callers were announced, but otherwise it was out and Jane was playing her voiceless piano. Henrie was mostly very happy, but also sometimes found her eyes filled with tears as she listened to the silent measure of her own meagerness.` ——逐字一致 ✓
- 说话人：叙述句，描述 Jane 探亲余下日子的练琴与 Henrie 心境；中文理解与 text 一致 ✓
- 引语↔分析：为什么这样写围绕 voiceless piano / silent measure / meagerness 双关展开，完全对应；「短了一个半八度」出自 text 前段（第 68 行），是背景呼应而非本引语主张，非截短 ✓
- 关键词回查：awash in the silence / voiceless piano / meagerness 均在引语内 ✓
- 结构：四子项齐全 ✓

## 待人工复核
无
---

# d 步二审 · ch22

## 结论：共 3 块，通过 3，缺陷 0，待复核 0

逐对核对说明（含说话人窗口查验、引语↔分析对应、关键词回查、结构）：

### 原句 1
- **引语行**：`> **原句 1:** "And so the years passed in gray worsted with the scarlet stitches of Jane's weekly letters and the occasional bright button of her visits."`
- **text 核对**：text/ch22_chapter_8.txt 第 13 行逐字命中（弯引号差异不计）。
- **说话人**：属第三人称叙事（编年概述），非某人话语；中文理解未错归说话人，一致。
- **关键词回查**：gray worsted ✓、scarlet stitches ✓、bright button ✓ 均在引语中。
- **引语↔分析**：为什么这样写讲"把年月织成布料"比喻，读者视角提示讲"编年章开场/快进"，与引语吻合；无截短。
- **结构**：引语行 + 中文理解 + 关键词 + 为什么这样写 + 读者视角提示 齐全。✅

### 原句 2
- **引语行**：`> **原句 2:** "But she was a professional in this if in nothing else; her mask of contentment and appreciation remained perfectly fixed, if her eyes were a bit wild."`
- **text 核对**：第 22 行逐字命中。
- **说话人（前后 ~200 字窗口）**：窗口含 "who was now twenty, twenty!"、"Henrie felt dizzy with longing…"、以及 Henrie 说 "How lovely. We shall certainly enjoy this."——确认是讲 Henrie 强颜欢笑的叙述，归因 Henrie 正确。
- **年龄断言**：中文理解"女儿两年未见、如今二十岁了"→ 窗口内 "It had been two years since they had seen their girl, who was now twenty, twenty!" **有原文支撑** ✅。
- **关键词回查**：professional ✓、mask of contentment ✓、wild（a bit wild）✓。
- **引语↔分析**：中文理解的"滴水不漏""眼神有点野"均对应引语；引语为完整句，无截短（后续 "She lifted the excrement…" 属相邻另句，非本引语支撑）。
- **结构**：齐全。✅

### 原句 3
- **引语行**：`> **原句 3:** "Sometimes, when Henrie couldn't sleep, she thought about what it would be like to cease existing. An immense thumb and forefinger coming up along either side of her life force and pinching it out. Just a serene blackness. Heaven."`
- **text 核对**：第 26 行逐字命中，为章末句。
- **说话人**：Henrie 的失眠想象，归因正确。
- **关键词回查**：cease existing ✓、pinching it out ✓、serene blackness ✓ 均在引语。
- **引语↔分析**：为什么这样写讲"掐灭烛火/安宁的黑即天堂"，与引语吻合；读者视角提示讲"最黑暗的一句/Part Two 压底"，为分析引申，非引语改写，可接受。无截短。
- **结构**：齐全。✅

### 年龄数字断言专项
- 「十三岁」：text 第 13 行 "Jane was thirteen, fourteen, fifteen." **有支撑** ✅
- 「二十岁」：text 第 22 行 "who was now twenty, twenty!" **有支撑** ✅

## 缺陷清单（无则写"无"）

无。

## 待人工复核

无。

ch22 完成：3 块，缺陷 0，待复核 0
---

# d 步二审 · ch23

## 结论：共 4 块，通过 4，缺陷 0，待复核 0

## 缺陷清单
无

## 逐块核对记录

### 块 1 · 原句 1
- **引语逐字**：与 text/ch23_chapter_9.txt 第 13 行逐字一致（含开篇 "Mother, listen to what Jane writes. She is in Weymouth, you remember?" 及后接叙述句）。✓
- **说话人**：Henrie 对母亲说话 + 叙述者；grep 窗口确认无误。✓
- **引语↔分析**：中文理解"妈妈，听简写的信…可要抓住母亲的注意力越来越难了"与引语后半叙述句完全对应，无截短。✓
- **关键词**：engage her mother's attention、muffler、handiwork 均在引语中逐字找到。✓
- **结构**：引语行 + 四子项（中文理解/关键词/为什么这样写/读者视角提示）齐全。✓

### 块 2 · 原句 2
- **引语逐字**：与 text 第 16 行逐字一致（织毛线/拆毛线 + 括号补充 + 窗外冷风 + 简信中关于韦茅斯距离、父亲地图册、"可是拍卖师——"、姑妈长寿 + 贝茨太太默默点头 + "It was all they had."）。✓
- **说话人**：叙述者交代亨莉的行动，中段为简信内容（亨莉念出）；说话人归因正确。✓
- **引语↔分析**：中文理解覆盖织毛线、拆毛线、窗外风、简信中多塞特晴天、奈特利先生、"拍卖师——"破折号、姑妈长寿、贝茨太太点头、"她们仅有的一切"，与引语一一对应。✓
- **关键词**：unraveling、too dear、auctioneer 均在引语中逐字找到。✓
- **结构**：齐全，无重复块。✓

### 块 3 · 原句 3
- **引语逐字**：与 text 第 25 行逐字一致（午睡安顿 + vivacious + air of duty + Jane Dixon / Preserve the x / A kiss / union of true love / the good ever find the good / beam / white frills / the immense heavy log / The wind had changed）。✓
- **说话人**：叙述者贴身跟随亨莉的自由间接独白，归因正确。✓
- **引语↔分析**：中文理解逐句覆盖"风浪/大梁"与"浪漫想象"的拉扯，末句"风变了"呼应谶语解读，无截短。✓
- **关键词**：vivacious、air of duty、beam 均在引语中逐字找到。✓
- **结构**：齐全。✓

### 块 4 · 原句 4
- **引语逐字**：与 text 第 37 行逐字一致（In the next letter, though, Jane announced that Mr. Dixon was to marry Elizabeth Campbell. Henrie did not detect any disappointment but her own.）。✓
- **说话人**：叙述者；归因正确。✓
- **引语↔分析**：中文理解"下一封信里…狄克逊先生将迎娶伊丽莎白·坎贝尔。亨莉没有觉察到任何失望——除了她自己的"完全对应；分析中对 "detect" 的解读与引语一致。✓
- **关键词**：announced、detect、disappointment 均在引语中逐字找到。✓
- **结构**：齐全，为全章收束块。✓

## 待人工复核
无。

## 备注
- 章号一致性：md 标题为 "Chapter 9（Part Two: 1795–1811）"，text 文件头为 "Chapter 9"，与文件名 ch23_chapter_9.txt 一致，无跨章章号错标。
- 本章词汇表内部分例句（stature、discreet、packet、nodded 等）来自本章其他行，属词汇示例而非引语块，不在本次引语↔分析逐对核对范围内。

ch23 完成：4 块，缺陷 0，待复核 0
---

# d 步二审 · ch24

## 结论：共 4 块，通过 4，缺陷 0，待复核 0

## 缺陷清单

无

## 待人工复核

无

## 核对明细

### 原句 1
- **逐字核对**：与 text/ch24_chapter_10.txt 第 25 段完全一致（含弯引号、破折号、斜体/词形一致）。✓
- **说话人**：`"Miss Bates. We have a letter for you."` 为 Mr. Norrish 所说；中文理解归因「诺里斯先生」正确。后续补史段落在 text 中同属该段落，归入亨莉内心视角（she suspected），中文理解表述一致。✓
- **关键词回查**：`forgiven`、`tumble`、`satisfaction` 均在引语内找到。✓
- **引语↔分析**：中文理解覆盖钢琴赌局、投靠叔叔、回海比当局长、阶层下坠、眼神冰冷——与引语逐项对应；「为什么这样写」提到的拟声 `bumpity bump`、`she suspected` 均在引语中，无截短。✓

### 原句 2
- **逐字核对**：与 text 第 46 段完全一致。✓
- **说话人**：`"No, Miss Bates. I am sorry, but absolutely not…"` 为 Mr. Norrish 所说，中文理解归因「诺里斯先生」正确。✓
- **关键词回查**：`whisked`、`absolutely not`、`short-term loans` 均在引语内找到。✓
- **引语↔分析**：中文理解逐句对应收回动作、双重否定、「国王陛下」抬伞；「为什么这样写」所指的三层权力刻度（收回、否定、官方权威）全部由引语支撑，无截短。「一便士半邮资」为前文已知信息，非本块引语硬伤。✓

### 原句 3
- **逐字核对**：与 text 第 55 段完全一致。✓
- **说话人**：本段为亨莉（Henrie）的第三人称贴身叙事；中文理解主语「亨莉」正确。✓
- **关键词回查**：`fury`、`clarified`、`spigot` 均在引语内找到。✓
- **引语↔分析**：中文理解逐句对应怒气、店里有人、掐腕、门铃、开水龙头；「为什么这样写」指出的三处意象（掐腕=刹车、门铃=外物接通内里、水龙头=滔滔客套阀门）全部由引语支撑，无截短。`spigot` 为象征解读，作者未明写，属合理诠释而非断言。✓

### 原句 4
- **逐字核对**：与 text 第 61 段完全一致（长引语逐句比对通过）。✓
- **说话人**：`"Absolutely, Miss Bates. Mr. Woodhouse says the very same thing about sweets."` 为 Mr. Ford 所说；中文理解归因「福特先生」正确。✓
- **关键词回查**：`hoisted`、`effusions`、`bountiful` 均在引语内找到。✓
- **引语↔分析**：中文理解逐句对应纸锥未封好、唾液糖卷、福特先生看破不说破、塞柜台下、两便士、真实感激、「后槽牙旧日位置」——全部由引语支撑，无截短；引语完整覆盖至 back teeth 收尾句，分析中的关键意象（「后槽牙」=贫穷写进身体）有引语末句作为直接依据。✓

### 结构检查
- 4 个引语块均含「引语行 + 中文理解 + 关键词 + 为什么这样写 + 读者视角提示」，无孤儿块、无重复块。✓

ch24 完成：4 块，缺陷 0，待复核 0
---

# d 步二审 · ch25

审查文件：《miss-bates-by-catherine-cliff/ch25 moved the furniture.md》（Chapter 1, Part Three: February–May 1812）
对照原文：`text/ch25_chapter_1.txt`（Chapter 1 正文）

## 结论：共 4 块，通过 4，缺陷 0，待复核 1

## 逐块核对

### 原句 1
- 引语：`"She and Patty had moved the furniture to the center of the room, and she had thrown the window open (though it was quite chillsome) so that they could beat their sole rug."`
- 逐字核对：✅ 原文 text 第 17 行完整逐字命中（含括号 chillsome）。
- 说话人：✅ 叙述性段落（第三人称贴身跟随 Henrie），非对话；中文理解把句子归为对 Bates 家打抄场景的描写，与上下文一致（前文为 Henrie 擦洗 tallow、拉回地毯）。
- 引语↔分析对应：✅ 中文理解"家具挪到房间中央/敞开窗/拍打仅有的一张地毯"逐点对应引语；关键词 sole rug / chillsome / beat 全在本块引语命中；"为什么这样写"围绕 sole rug 与 chillsome 的贫穷隐喻展开，呼应成立；读者视角提示讲"仅有一张地毯"的家底对照，同一引语。
- 关键词回查：sole rug ✓、chillsome ✓、beat ✓。
- 结构：引语行 + 中文理解 / 关键词 / 为什么这样写 / 读者视角提示 四子项齐全。

### 原句 2
- 引语：`"You have never visited the Bates women? Consider yourself blessed. I never walk by here without fearing that I will be snatched up as if by a witch's claw and dragged into their deadly eyrie to be force-fed tidbits torn from Jane Fairfax's letters. If you are not careful, you will find yourself fallen into a hundred years sleep."`
- 逐字核对：✅ 原文 text 第 20 行完整逐字命中（弯引号差异，允许）。
- 说话人：✅ 该段为 Emma Woodhouse 的对话。原文第 17 行明确"one of them, unmistakably Emma Woodhouse, was describing her, Henrie, to her companion"；第 26 行确认同伴即 Mrs. Goddard 的寄宿生、后文点名 Harriet Smith。中文理解"Emma 对 Harriet 说"归因正确。（**说话人反转类缺陷在此未出现。**）
- 引语↔分析对应：✅ 中文理解逐点对应（谢天谢地/女巫之爪/致命巢穴/硬灌 Jane 信屑/沉睡百年/妖怪洞窟），无截短；"为什么这样写"的三个童话意象（女巫之爪、强行喂食、百年沉睡）均来自本块引语。
- 关键词回查：snatched up ✓、witch's claw ✓、force-fed ✓。
- 结构：齐全。

### 原句 3
- 引语：`"And then she forces one to admire a mangled piece of leather she calls a purse—there is something repulsive and slippery about her. She is an example of how poverty can render celibacy contemptible."`
- 逐字核对：✅ 原文 text 第 35 行完整逐字命中（破折号一致）。
- 说话人：✅ 该句为 Emma 对话中紧接"Mother's shoe was worn quite through… it is my new purse…"之后的部分，仍是 Emma 之口；中文理解"Emma 抱怨说"归因正确。
- 引语↔分析对应：✅ 中文理解逐点对应（破烂皮革钱包/令人厌恶又滑腻/贫穷使独身可鄙）；"为什么这样写"引述的 Henrie 原话"这是我的新钱包，简直像圣诞节早晨！"确在 text 第 35 行同一对话块内（"It is my new purse, why, it feels like Christmas morning!"），属同块支撑，非拼装、非截短。
- 关键词回查：mangled ✓、repulsive and slippery ✓、contemptible ✓。
- 结构：齐全。

### 原句 4
- 引语：`"She talked on and on, sewing Emma and Miss Smith to their seats with her relentless chatter, all the while imagining taking the porridge pot from behind her mother's chair and swinging it in an awful arc toward Emma Woodhouse's high cheekbone and feeling the bone splinter at the impact."`
- 逐字核对：✅ 原文 text 第 62 行完整逐字命中（全书最后一段）。
- 说话人：✅ 叙述性段落（第三人称贴身跟随 Henrie），描述 Henrie 的絮叨与幻想；中文理解"她滔滔不绝地说下去……"归因为 Henrie，正确。
- 引语↔分析对应：✅ 中文理解逐点对应（缝在座位上/从母亲椅后拿粥锅/砸向颧骨/骨头碎裂）；"为什么这样写"把 sewing…relentless chatter 与 Emma 的"女巫之爪"对照，并把粥锅（前文第 47 行藏于母亲椅后）点明为幻想凶器，呼应成立；读者视角提示也落在粥锅与絮叨上，同一引语。
- 关键词回查：sewing ✓、relentless chatter ✓、bone splinter ✓。
- 结构：齐全。

## 缺陷清单

无。

## 待人工复核

1. **任务给出的 text 路径与 md 实际引用不符（非章节缺陷）**：本次委托要求核对 `text/ch25_chapter_11.txt`，该文件不存在；目录中实际文件为 `text/ch25_chapter_1.txt`。md 自身 frontmatter 与"提取件"一行均正确指向 `text/ch25_chapter_1.txt`，且正文首行为 "Chapter 1"，与精读标题"Chapter 1（Part Three）"一致。故这是委托路径笔误，不是跨章章号错标，md 本身无误。建议后续委托使用 md 内声明的 `text/ch25_chapter_1.txt`。**判定：待人工复核（委托侧）**。

ch25 完成：4 块，缺陷 0，待复核 1
---

# d 步二审 · ch26

审查文件：
- 精读 md：`notes/books/novels/miss-bates-by-catherine-cliff/ch26 the notebook.md`
- 原文提取件：`notes/books/novels/miss-bates-by-catherine-cliff/text/ch26_chapter_2.txt`

## 结论：共 4 块，通过 4，缺陷 0，待复核 0

## 逐块核对明细

### 原句 1（引语行在 md 第 21 行）
- **引语逐字**：与 text 第 13 行逐字一致（省略号/引号差异无，破折号 "to—what?" 一致）。✓
- **说话人正确**：text 上下文为 Henrie 视角第三人称叙述（"Henrie's heart accelerated…"），"Henrie and her mother…", "the cord that connected them" 属 Henrie 反思。中文理解归因 Henrie 清醒知道亲情磨损，正确。✓
- **引语↔分析对应**：四子项均在讲同一段——"cord 磨损""daughter→niece→cousin 降格"；无截短，引语完整到 "not intimacy"。✓
- **关键词回查**：frayed / cord / convention 均在引语原文出现。✓
- **结构**：引语行 + 中文理解 + 关键词 + 为什么这样写 + 读者视角提示，齐全。✓

### 原句 2（引语行在 md 第 33 行）
- **引语逐字**：与 text 第 16 行逐字一致，包括括号内 "this one had a star next to the name as she was, extraordinarily, female!"。✓
- **说话人正确**：text 第 16 行上文 "she had made an effort to keep up with the information that she had gleaned about music…copied out in her own irregular handwriting. Looking at the notebook now, she was embarrassed…" — "she"=Henrie。中文理解归因 Henrie，正确。✓
- **引语↔分析对应**：四子项均围绕 Henrie 自我贬低 + 名单；无截短（止于 "and so on."）。✓
- **关键词回查**：embarrassed / earnest / childish 均在引语原文。✓
- **结构**：齐全。✓
- 注：分析中引用的 "'Just a list, it meant nothing to her' 与 'maybe she would be able to say one of the names in conversation'" 为引语块之后、同段（text 第 16 行末尾）的原文补充说明，非拼接无关句，可用。

### 原句 3（引语行在 md 第 45 行）
- **引语逐字**：与 text 第 28 行逐字一致。✓
- **说话人正确**：text 第 28 行描述的对象是 Jane（"She looked like life had used up some of her vitality…"），承接第 25 行"a less familiar face"与"the most beautiful thing Henrie could imagine"。中文理解归因为"Jane 依旧是 Henrie 想象中最美的模样"，正确；"She"=Jane 而非 Henrie，未反转。✓
- **引语↔分析对应**：四子项均讲 Jane 面庞/气质的变与 "like a grown woman"；无截短。✓
- **关键词回查**：minus / vitality / drained 均在引语原文。✓
- **结构**：齐全。✓

### 原句 4（引语行在 md 第 57 行）
- **引语逐字**：与 text 第 76 行逐字一致（弯引号 vs 直引号差异忽略）。✓
- **说话人正确**：text 第 76 行承接第 73 行"she dutifully nibbled at the pork"，描述 Henrie 观察 Jane 吃土豆，Henrie 是动作主体。中文理解"Henrie 试着让自己的演奏去配合外甥女的心情""她看着 Jane 出于礼貌把那个土豆吃了下去"，正确。✓
- **引语↔分析对应**：四子项均围绕"uneven tempo + match her playing + to be polite"；无截短（止于 "to be polite."）。✓
- **关键词回查**：uneven tempo / match her playing / to be polite 均在引语原文。✓
- **结构**：齐全。✓

## 特别关注：年龄数字「五六岁」核实
- md 原句 3「读者视角提示」写："Henrie 在窗口认出的还是'五六岁起就有的那种姿态'。"
- text 第 25 行有原文支撑："Henrie immediately recognized the perfect posture and elegant bearing of little Jane, which she had from when she was very small, five or six."（即该姿态自五六岁起即有）。
- **结论：数字断言有原文支撑，无需报警。**

## 缺陷清单（无则写"无"）
无

## 待人工复核
无

---

ch26 完成：4 块，缺陷 0，待复核 0
---

# d 步二审 · ch27

## 结论：共 3 块，通过 3，缺陷 0，待复核 0

## 缺陷清单

无。

## 逐块核对记录

### 块 1 · 原句 1
- **引语逐字**：md 引语行与 `text/ch27_chapter_3.txt` 第 13 行逐字一致（含省略语流、标点），无实词改写。✓
- **说话人正确**：该段为第三人称贴身跟随 Henrie 的自由间接/内心叙述，无对话引号；中文理解归因为 Henrie 心里所想（"Henrie 在心里称她"），与 text 窗口内叙事视角一致。✓
- **引语↔分析对应**：四子项（中文理解/关键词/为什么这样写/读者视角提示）均围绕"Emma 七天才来、带 Harriet、Jane 气色好"同一句；未发现引语截短——引语已完整覆盖分析所依据的内容（Beast of Hartfield、protégée、glowing like a lamp）。✓
- **关键词回查**：Beast of Hartfield ✓、protégée ✓、fluctuate ✓、glowing like a lamp ✓，均在引语内找到。✓
- **结构**：引语行 + 中文理解 + 关键词 + 为什么这样写 + 读者视角提示，齐全，无孤儿/重复块。✓

### 块 2 · 原句 2
- **引语逐字**：md 引语行与 text 第 16 行逐字一致。✓
- **说话人正确**：段内"Henrie was happy to say (to herself)"、"Henrie knew"明确标记为 Henrie 内心；中文理解归因为 Henrie 暗自高兴，正确。✓
- **引语↔分析对应**：四子项围绕同一段"内心比美+见识盘点+could not resist"；引语覆盖"could not resist"（分析用以引出下一句八卦），无截短。✓
- **关键词回查**：provincial ✓、measured voice ✓、talented ✓、could not resist ✓，均在引语内。✓
- **结构**：齐全。✓

### 块 3 · 原句 3
- **引语逐字**：md 引语行与 text 第 43 行逐字一致。✓
- **说话人正确**：段首"Henrie had been hoping"、"Led the conversation"为 Henrie 内心自责；中文理解归因为 Henrie（"Henrie 本想…"），正确。✓
- **引语↔分析对应**：四子项围绕"本想来场八卦却引向家庭教师话题、Jane 披斗篷走"同一句；引语已含分析强调的"Governessing."与"Shortly after this, Jane put on her cape."，无截短。✓
- **关键词回查**：cozy gossip ✓、Governessing ✓、avoid ✓、cape ✓，均在引语内。✓
- **结构**：齐全。✓

## 待人工复核

无。

ch27 完成：3 块，缺陷 0，待复核 0
---

# d 步二审 · ch28

## 结论：共 4 块，通过 4，缺陷 0，待复核 0

## 缺陷清单
无

## 逐块核验明细

### 原句 1
- **引语逐字**：text/ch28 第 13 行整段逐字一致。md 块首加了一对直引号把首句包起来，text 中该句为上文对话的延续、无前引号，属引号标记差异，允许。
- **说话人**：该段为 Henrie 的第三人称贴身叙事＋她对母亲（Mrs. Bates）说的缝纫夸奖独白。text 第 13 行上下文（13–25 行）确认：thinking 的是 Henrie，Jane 望窗外、Mrs. Bates 低头缝补，"You are sewing up the tear..." 是 Henrie 对母亲说的。与中文理解归因一致。
- **引语↔分析对应**：中文理解的"盘算晚饭储备/收到请柬如释重负/Jane 望窗/母亲愁容缝补/缝纫大师夸奖链/对 Mrs. Goddard 的敬畏/treasure sack/Butter on tea tray"全部落在引语行内，无截短、无无中生有。
- **关键词**：fretfully ✓、deft ✓、Mistress of Stitches ✓、treasure sack ✓、unimaginable ✓，均在引语行找到。
- **结构**：引语行＋中文理解＋关键词＋为什么这样写＋读者视角提示齐全。

### 原句 2
- **引语逐字**：text 第 86 行逐字一致（含全部标点与引号）。
- **说话人**：text 第 80 行 Jane 说 "I am directly behind Grandmama..."，第 83 行 Henrie 回应，第 86 行 "Yes, yes, I know, Aunt Henny..." 是 Jane 答 Henrie。与中文理解"Jane 不耐烦地接过话头"一致。
- **引语↔分析对应**：感恩三连、铅针刺肤箴言、两段反话致谢（Miss Woodhouse 富到请客不伤家计、Mr. Woodhouse 马车送半英里反正自己不用）均逐字在引语行，分析无截短。
- **关键词**：dictum ✓、carved into my skin ✓、hosanna ✓、household economy ✓。
- **结构**：五要素齐全。

### 原句 3
- **引语逐字**：text 第 101 行逐字一致。
- **说话人**：text 第 98 行 Jane 说 "I have a lavender handkerchief in my sleeve which always serves perfectly."，第 101 行叙事 "Always." 回指该词。中文理解解释为"Jane 说'总是'、Henrie 注意到"——归因正确。注意：引语行本身是叙事段，中文理解已准确说明"总是"源自 Jane 之口。
- **引语↔分析对应**：satchel of worries / puzzle / solution / scared 均在引语行内，无截短。
- **关键词**：Always ✓、satchel of worries ✓、puzzle ✓、solution ✓。
- **结构**：五要素齐全。

### 原句 4
- **引语逐字**：text 第 233 行逐字一致。
- **说话人**：第三人称叙事（Jane 弹琴、Henrie 的感受），中文理解归因一致。
- **引语↔分析对应**：glorious sound、与 Emma 民谣对比、穿过不同情绪总回同一主题、悲伤而美丽、Henrie"变高一倍"全部逐字在引语行内，无截短。
- **关键词**：glorious sound ✓、moods ✓、returning to the same theme ✓、exalted ✓、pride ✓。
- **结构**：五要素齐全。

## 待人工复核
无

## 说明
- 未发现说话人反转、章号错标、引语截短三类已知失败模式。
- 唯一可注意的格式差异：原句 1 块首多了一对直引号包裹首句（text 中原为该段承接上文对话、无前引号），按规则属引号标记差异，不计为缺陷。
- 本章 4 个引语块全部为整段完整引用，无跨段拼装。

ch28 完成：4 块，缺陷 0，待复核 0
---

# d 步二审 · ch29

审查对象：`notes/books/novels/miss-bates-by-catherine-cliff/ch29 tops of heads.md`（Chapter 5, Part Three: February–May 1812）
原文提取件：`notes/books/novels/miss-bates-by-catherine-cliff/text/ch29_chapter_5.txt`

## 结论：共 4 块，通过 4，缺陷 0，待复核 2

## 各块核对明细

### 原句 1
- **逐字命中**：是。text 第 13 行逐字一致（引号差异忽略）。✓
- **说话人**：Henrie。窗口内容：开头即 Henrie 的街景独白，后接她对 Woodhouse/Harriet 友谊的品评（"I do wonder at that friendship…"）。归因正确。✓
- **引语↔分析对应**：四子项（中文理解 / 关键词 / 为什么这样写 / 读者视角提示）均围绕同一句。引语未截短，首尾完整。✓
- **关键词**：patroness、particular friend、no family 均在引语内。✓

### 原句 2
- **逐字命中**：是。text 第 16 行逐字一致。✓
- **说话人**：非对话，为叙述者对 Mrs. Bates 的描写。中文理解正确按叙述处理，未误归为某人说话。✓
- **引语↔分析对应**：四子项齐全且同指一句。引语未截短。✓
- **关键词**：accustomed chair、tortoise、reptile eyelids 均在引语内。✓

### 原句 3
- **逐字命中**：是。text 第 19 行逐字一致。✓
- **说话人**：Henrie。窗口（第 19 行整段为 Henrie 独白，"continued Henrie" 前一行有归属）确认归因正确。✓
- **引语↔分析对应**：四子项齐全同指一句。引语未截短。✓
- **关键词**：audience、players、personal theater 均在引语内。✓

### 原句 4
- **逐字命中**：是。text 第 127 行逐字一致。✓
- **说话人**：Jane。窗口（第 124 行 Frank 皱眉："But it is short an octave and a half?"；第 127 行 "now Jane spoke up" 后接引语）确认归因正确。✓
- **引语↔分析对应**：四子项齐全同指一句。引语未截短。✓
- **关键词**：no difference、grateful、well-limbered 均在引语内。✓

## 结构检查
- 四块均为「引语行 + 中文理解 + 关键词 + 为什么这样写 + 读者视角提示」，齐全无缺。✓
- 无孤儿块、无重复块、无跨章章号错标。✓
- 各块引语行与中文理解行在同一 md 且相邻。✓

## 缺陷清单（无）

无逐字失配、说话人反转、引语截短或跨章错标等硬缺陷。

## 待人工复核

1. **类型**：分析引用了引语块外的词
   - **引语行原文**：`"There go Mrs. Goddard's students in their double row, what nice-looking, neat girls they are. Blooming! Mrs. Goddard at the front, such a success she has made of that school. Oh, and Miss Woodhouse's particular friend, Miss Smith. No family, of course, but she is a beauty in quite a different way from her patroness."`
   - **中文理解原文**：Henrie 隔窗看着 Mrs. Goddard 的学生们排成双列走过，一一品评……
   - **问题说明**：「为什么这样写」中提到 "Round rather than slim" 这类脱口而出的等级评语——该短语**不在本块引语内**（存在于 text 第 13 行引语结束之后的同一段落，"Blue eyes rather than hazel, round rather than slim"）。分析本身仍由引语内 "No family, of course… from her patroness" 支撑，故非幻觉；但读者按引语块核对时找不到 "Round rather than slim"。
   - **建议修法**：在「为什么这样写」中把该短语标注为引语外的同段补充，或改为直接引用引语内的等级评语（如 "No family, of course"）。

2. **类型**：分析对 Jane 说话时点的表述略夸张
   - **引语行原文**：`"That made no difference to me. There are many, indeed most, pieces that do not make use of the very bottom of the keyboard. I was very grateful to my aunt for allowing me to keep my fingers well-limbered."`
   - **中文理解原文**：面对 Frank Churchill 对"缺了一个半八度"的皱眉，Jane 平静地接住……
   - **问题说明**：「为什么这样写」称本句是 "Jane 在全章的昏沉沉默里重新开口的时刻"。但 Jane 在本章此前已多次开口：text 第 73 行（"Not so many"）、第 88 行（"Aunt Henny, I beg you, please stop"）、第 100 行、第 106 行、第 118 行。因此"重新开口"并不准确；本句真正特殊之处是 Jane 主动替姨妈的寒酸发明辩护，而非她"首次"开口。引语本身与中文理解无误。
   - **建议修法**：将「为什么这样写」改为强调这是 Jane 在键盘话题上**主动为姨妈辩护**的时刻，去掉"昏沉沉默里重新开口"的绝对化表述。

## 附注
- 引语均为原文逐字、说话人正确、关键词齐备，四子项对应清晰。
- 「本章词汇」表格中的例句来自本章其他段落，非本次逐块核对范围；抽查未见硬错（如 "wrong side of the blanket" 对应"私生"概念在 text 第 16 行存在，用于支持原句 1 读者视角提示中"用'私生'的说法把它点破"的说法）。

ch29 完成：4 块，缺陷 0，待复核 2
---

# d 步二审 · ch30

## 结论：共 4 块，通过 4，缺陷 0，待复核 1

审查对象：
- 精读 md：`notes/books/novels/miss-bates-by-catherine-cliff/ch30 the impertinence.md`
- 原文提取件：`notes/books/novels/miss-bates-by-catherine-cliff/text/ch30_chapter_6.txt`

核对方法：对每一引语块，先在 text/ch30 全文逐字比对英文引语；逐字命中后回读 text/ 前后约 200 字符窗口确认说话人/归属；再核对四子项是否同指一句、是否截短；最后回查关键词。

---

## 逐块核对

### 块 1 · 原句 1（原句 1）

> **引语行**：`> **原句 1:** "The three women of the Bates household stood in awe, arrayed around it. Silent and stunned as if an immense tree had fallen through their roof and landed in their sitting room. And really the delivery was no more commodious."`

- **逐字**：text 第 13 段开头三句逐字全中，无省略、无改写。✅
- **说话人**：本章开篇第三人称叙述（非对白），描述 Bates 家三位女眷围绕钢琴的反应。窗口上下文（Broadwood's 搬运工进出）佐证为叙述者对"她们"的描述，非任何角色台词。中文理解归因"Bates 家的三个女人敬畏地站在钢琴四周"正确。✅
- **引语↔分析对应**：四子项（中文理解／关键词／为什么这样写／读者视角提示）均在讲这一句。末句"末句反讽地把比喻坐实"针对"no more commodious"原文已在引语内。✅
- **截短检查**：引语在句末自然收束（下一句"The men from Broadwood's had moved in..."未引，非截短）。✅
- **关键词**：`immense tree`✅、`stunned`✅、`no more commodious`✅ 均在引语内。
- **结构**：引语行 + 中文理解 + 关键词 + 为什么这样写 + 读者视角提示，齐全。✅

### 块 2 · 原句 2

> **引语行**：`> **原句 2:** "Jane and Henrie read it and then frowned at each other in confusion and a rare moment of communion. There could be no arguing with the direction, the delivery was certainly for Jane."`

- **逐字**：text 第 16 段中逐字全中。✅
- **说话人**：句中主语为 Jane 与 Henrie，动词 read 指向"它"——前文 Patty 送上楼的送货单（MISS JANE FAIRFAX…）。窗口上下文（"Well, Patty, I suppose whatever they are bringing, it is indeed for Miss Fairfax"）佐证确实是两位读单、而非旁人。中文理解"Jane 和 Henrie 读完送货运单"正确。✅
- **引语↔分析对应**：四子项均在讲同一句；"两人同时意识到：没有人订购这架钢琴"由"in confusion""no arguing with the direction"支撑。✅
- **截短检查**：引语以"Jane and Henrie read it"起句，为完整句子开头（非词中截断）；"it"的指代需前文（送货单），属引语省略，非截短。✅
- **关键词**：`confusion`✅、`communion`✅、`certainly for Jane`✅。
- **结构**：齐全。✅

### 块 3 · 原句 3

> **引语行**：`> **原句 3:** "Henrie knew he would not have felt at liberty to speak so directly to her, nor to complain so volubly on the stairs, had she still been living at the vicarage, or if she had a husband. She, and her mother, and her niece, could be addressed as if they were children before these burly laborers. Children to be scolded. As if the essence of the men's employment, carrying heavy things, was in some way Henrie's fault."`

- **逐字**：text 第 22 段后半逐字全中。✅
- **说话人**：句中 "Henrie knew" 明确为主角内心独白/叙述；"he"指上文那位"man in charge"（搬运头领），"her"指 Henrie。窗口上下文（"Nowt seen a pianoforte like this brought into such a room afore," said the man in charge…）佐证。中文理解归因"Henrie 明白，如果她还住在牧师住宅……"正确。✅
- **引语↔分析对应**：四子项均在讲同一句；"为什么这样写"评述"如果……就不会"的社会性刺点，紧扣原文。✅
- **截短检查**：引语以"Henrie knew"起句，前一句是搬运头领的对白，属引语起点自然，非截短。✅
- **关键词**：`vicarage`✅、`burly laborers`✅、`children to be scolded`✅。
- **结构**：齐全。✅

### 块 4 · 原句 4

> **引语行**：`> **原句 4:** "The impertinence. This is part of what had stunned the Bates women into silence. With what could they fight back? What did they want with a pianoforte that took up all their living room? Nothing! But how could they admit to this man that they had not ordered it themselves and knew nothing about its provenance."`

- **逐字**：text 第 28 段开头逐字全中。✅
- **说话人**：Henrie 的内心独白（"The impertinence"是对上文搬运头领那句" What are you wanting with an instrument this size in a room like this, then?"的愤慨反应）。窗口上下文（"Small place for such a grand instrument…"→搬运头领的话）佐证。中文理解归因"真是放肆。这也正是 Bates 家女眷被惊得说不出话的部分原因"正确。✅
- **引语↔分析对应**：中文理解／关键词／为什么这样写 三项均在讲引语内内容。⚠️ 但**读者视角提示**描述"她急着等工人走好听 Jane 交代，又害怕工人走了她就会知道答案——这架钢琴是下一章所有悬念的起点"，此双重心思出自引语之后紧接的一句原文：`Henrie could not wait for them to leave so she could question Jane, but she also feared them leaving, for what would she find out?`（text 第 28 段末尾），**不在引语内**。属轻微截短——子项分析依赖了引语之外的句子。
- **截短检查**：引语在第 28 段第 6 句结束，其后" What would such an extravagant gift say about Jane? Given as a surprise?…"及"Henrie could not wait…"未引。分析的四子项中"读者视角提示"实质引用的是引语外的句子。非逐字错，属"引语短于其支撑分析"的轻度情况，建议补全或标注来源。
- **关键词**：`impertinence`✅、`stunned into silence`✅、`provenance`✅。
- **结构**：齐全。✅

---

## 缺陷清单（无则写"无"）

无（硬性逐字/说话人/关键词/结构缺陷 0 处）。块 4 的引语截短问题归入下方"待人工复核"。

---

## 待人工复核

1. **块 4 · 引语截短（轻度）**：读者视角提示"她急着等工人走好听 Jane 交代，又害怕工人走了她就会知道答案"所对应的原文 `Henrie could not wait for them to leave so she could question Jane, but she also feared them leaving, for what would she find out?` 位于引语之后（text 第 28 段末），未被本块引语覆盖。建议二选一：
   - 把该句补入块 4 引语（或把读者视角提示明确标注为"续下文"）；
   - 或维持现状但将"读者视角提示"改为只依赖引语内内容（如引语内"With what could they fight back?"的沉默困局）。
   逐字与说话人均无问题，此条仅为分析↔引语边界一致性提示。

---

## 词汇例句核查（附）

词汇表 11 条例句全部逐字命中 text：
- excoriate（第 19 段）✅；volubly（第 22 段）✅；impertinence（第 28 段）✅；provenance（第 28 段）✅；acerbic（第 37 段）✅；commodious（第 13 段）✅；burly（第 22 段）✅；communion（第 16 段）✅；parquet（第 25 段）✅；grunting（第 22 段）✅；stomped（第 16 段）✅。

ch30 完成：4 块，缺陷 0，待复核 1
---

# d 步二审 · ch31

## 结论：共 4 块，通过 4，缺陷 0，待复核 0

## 缺陷清单：无

## 待人工复核：无

### 逐块核对记录

**原句 1**（md L21 ↔ text L16）：
- 引语逐字：全文命中，实词一致（Coles's / perch / balanced / stretched thin and tight from worry）。
- 说话人：旁白叙述（Henrie 视角第三人称），无归因错误。
- 引语↔分析：四子项（中文理解 / 关键词 / 为什么这样写 / 读者视角提示）均围绕同一句；引语未截短（完整三句+末句比喻句都在）。
- 关键词：perched ✓ balanced ✓ stretched thin and tight ✓ 均在该块引语内。
- 结构：完整。

**原句 2**（md L33 ↔ text L80）：
- 引语逐字：全文命中（weather in the room changed / stagnant stench / impasse / withstand / cheery confidence）。
- 说话人：旁白叙述，无归因问题。
- 引语↔分析：四子项围绕同一句；"not withstand"双刃解读与原文用词一致，未截短。
- 关键词：weather in the room changed ✓ stagnant stench ✓ impasse ✓。
- 结构：完整。

**原句 3**（md L45 ↔ text L55）：
- 引语逐字：全文命中（Holding the tea in his left hand / trace a line / wandering fingers / A tickle? A scratch? / It took only a moment, but, oh, the intimacy）。
- 说话人：旁白叙述（偷窥视角），无归因错误。
- 引语↔分析：四子项围绕同一句；引语完整（含末尾惊叹句）。读者视角提示提到的拍卖师/涂写表面在 text L55 有原文支撑（"She thought of the auctioneer. What a thing to be a surface on which men scrawl as they wish."）。
- 关键词：trace a line ✓ wandering fingers ✓ intimacy ✓。
- 结构：完整。

**原句 4**（md L57 ↔ text L104）：
- 引语逐字：全文命中（And with that, Henrie was swept out of her own home / Mr. Churchill's will determining her actions / He put her in mind of Emma; those two were a pair）。
- 说话人：旁白叙述，无归因问题。
- 引语↔分析：四子项围绕同一句；末句判词解读与原文一致，未截短。
- 关键词：swept out of her own home ✓ will determining her actions ✓ a pair ✓。
- 结构：完整。

---

ch31 完成：4 块，缺陷 0，待复核 0
---

# d 步二审 · ch32

**审查文件**：`notes/books/novels/miss-bates-by-catherine-cliff/ch32 jane running uphill.md`
**原文对照**：`notes/books/novels/miss-bates-by-catherine-cliff/text/ch32_chapter_8.txt`

## 结论：共 3 块，通过 3，缺陷 0，待复核 0

逐块核对结果：

### 块 1 · 原句 1
- 引语逐字：✓ `"After this, the good weather held both inside and out, and Jane went for long walks. One Sunday evening she even asked her aunt to join her, what joy!"` 与 text 第 13 行完全一致。
- 说话人：✓ 为叙述语（Henrie 视角）；中文理解归因「Henrie 的立场/语气」正确，且「even」「what joy」正是 Henrie 的兴奋语气。
- 引语↔分析对应：✓ 中文理解 / 关键词 / 为什么这样写 / 读者视角提示 四子项齐全，均在讲同一句；无截短问题（引语止于 "what joy!"，分析未引用句外内容）。
- 关键词回查：held ✓、asked her aunt to join her ✓、what joy ✓，均在本块引语内。
- 结构：✓ 引语行 + 四子项齐全，无孤儿/重复。

### 块 2 · 原句 2
- 引语逐字：✓ `"The next Tuesday morning, Jane came running up the stairs with an immense bouquet of lilacs and lupine so that it seemed as if a part of the landscape was bursting into the room. Allegro!"` 与 text 第 16 行完全一致。
- 说话人：✓ 叙述语；中文理解「下一个星期二早晨，Jane 抱着一大捧丁香和羽扇豆跑上楼来」归因正确。
- 引语↔分析对应：✓ 四子项齐全，同一句；无截短。
- 关键词回查：immense bouquet ✓、bursting into the room ✓、Allegro ✓，均在本块引语内。
- 结构：✓ 齐全。读者视角提示中「稍后 Henrie 追问『是不是超过了快板』」为对 text 第 34 行 "Maybe beyond allegro—she must consult the notebook. Presto?" 的跨句呼应（Henrie 内心记分），非引语级错误，属合理的叙述互文。

### 块 3 · 原句 3
- 引语逐字：✓ `"When Henrie arrived home, she said, “Jane, these flowers are so lovely, I think we should keep them in our bedroom where the smell will garnish our sleep.” She did not need anyone else making the same connections that occurred as possibilities to her."` 与 text 第 52 行完全一致（弯引号一致）。
- 说话人：✓ 说话人是 Henrie（姨妈），对 Jane（外甥女）说；中文理解「Henrie 回到家便说：『Jane，这些花太可爱了……』」归因正确。
- 引语↔分析对应：✓ 四子项齐全，同一句；无截短。
- 关键词回查：garnish ✓、connections ✓、possibilities ✓，均在本块引语内。
- 结构：✓ 齐全。

**附：本章词汇例句抽查**（超出引语块范围，一并核对）
- immense / bouquet 例句（第 34 行 Jane）✓
- abundance 例句（第 34 行 Jane）✓
- entrancing 例句（第 40 行 Henrie 对 Mrs. Weston）✓
- suspicion 例句（第 55 行叙述）✓
- frivolous 例句（第 49 行 Mrs. Weston）✓
- afield 例句（第 25 行 Henrie 对 Jane）✓
- animated 例句（第 34 行叙述）✓
- garnish 例句（第 52 行 Henrie）✓
- condition 例句（第 37 行叙述）✓
- vase 例句（第 37 行叙述）✓

全部例句与 text 逐字一致，说话人归因正确。

## 缺陷清单（无则写"无"）

无。

## 待人工复核

无。

ch32 完成：3 块，缺陷 0，待复核 0
---

# d 步二审 · ch33

## 结论：共 4 块，通过 4，缺陷 0，待复核 0

## 缺陷清单

无

## 逐块核对记录

### 原句 1（通过）
- **引语逐字**：md 第 21 行引语 ↔ text/ch33 第 13 行逐字一致（直引号 vs 直引号，实词无改写）。✓
- **说话人**：引语为叙述段，无引语内直接引语；中文理解归 Henrie（她听出脚步声渐慢），与 text 上下文（随后 "Any post..." Henrie 开口）一致。✓
- **引语↔分析**：四子项均围绕"听脚步识心情/雨珠小仙子/音乐术语"，与引语一致；引语未截短，末句 "a sad fairy" 完整。✓
- **关键词**：Ritardando、aglitter、a sad fairy 均在引语命中。✓

### 原句 2（通过）
- **引语逐字**：md 第 33 行引语 ↔ text/ch33 第 25 行逐字一致（含 "No. Not a single letter. No letters. Enough."）。✓
- **说话人**：引语前导 "she rounded on her aunt and said bitterly" 为叙述，实际说话人是 Jane（"No, Aunt Henny."），中文理解归 Jane 顶回 Henrie，与 text 第 22 行 "Any post at Mr. Norrish's?" asked Henrie 呼应，归因正确。✓
- **引语↔分析**："为什么这样写"引用 "No. Not a single letter. No letters. Enough." 均在引语内；引语未截短。✓
- **关键词**：capricious、bitterly、Enough 均在引语命中。✓

### 原句 3（通过）
- **引语逐字**：md 第 45 行引语 ↔ text/ch33 第 46 行逐字一致。✓
- **说话人**：引语为 Henrie 的答话；text 第 43 行 Jane 问 "Was she a witch?"，第 46 行 Henrie 答 "That depends on what a witch is..."。中文理解归 Henrie 答，正确。✓
- **引语↔分析**：四子项围绕"女巫定义/无魔法/老处女无财产"，与引语一致；引语未截短。✓
- **关键词**：witch、spinster、no resources 均在引语命中。✓

### 原句 4（通过，含重点核实）
- **引语逐字**：md 第 57 行引语 ↔ text/ch33 第 88 行**逐字一致**，含反常词序 "looked at **each again other** for a long moment"。
- **重点核实（each again other）**：text/ch33 第 88 行原文即为 "Jane and Henrie looked at each again other for a long moment" —— 与 md 完全一致。**属原文如此（作者/出版排版如此），非转录错位，不算缺陷。**（注意：正常英语应为 "each other again"，此词序反常为 source 本身所有。）
- **说话人**：引语为叙述段，无引语内直接引语；中文理解描述两人对视、Jane 俯身亲吻，与 text 上下文（第 85 行 Mrs. Bates "Thought she was too good to be grateful!" 之后）一致。✓
- **引语↔分析**："为什么这样写"引用 "For a brief minute" 在引语内；引语未截短，末句 "Jane was her daughter again." 完整。✓
- **关键词**：a kiss on the top of her head、her daughter 均在引语命中。✓

## 结构核查
- 每块「引语行 + 中文理解 + 关键词 + 为什么这样写 + 读者视角提示」四子项齐全，共 4 块，无孤儿块、无重复块。✓
- 引语行与中文理解行在同 md 且相邻（同块内），无跨块拼装。✓

## 待人工复核

无

---

# d 步二审 · ch34

## 结论：共 4 块，通过 4，缺陷 0，待复核 0

**引语逐字核对**：4 个引语块均在 `text/ch34_chapter_10.txt` 中逐字命中（允许弯/直引号与撇号差异，如 `lifetime's` / `lifetime’s`），实词无改写。

**说话人核对**：逐字命中后均查看 text 前后 ~200 字符窗口确认归因。4 句均为 Henrie 贴身第三人称叙述（内含 Henrie 的内心判断），与中文理解的归因一致，无说话人反转。

**引语↔分析对应**：四个子项（中文理解 / 关键词 / 为什么这样写 / 读者视角提示）在每块内都指向同一句，无跨句拼装。无引语截短——4 块引语均完整覆盖其分析所支撑的语义。

**关键词回查**：关键词英文词均能在本块引语中找到（含词形一致）。

**结构**：每块「引语行 + 四子项」齐全，无孤儿块、无重复块。

### 逐块记录

| 块 | 引语行（text 行号） | 逐字 | 说话人 | 关键词命中 | 结论 |
|---|---|---|---|---|---|
| 原句 1 | L13 | ✓ | Henrie 叙述眼光（"thought Henrie as she settled into her pew"） | sulkily / like a man goes to an auction / paddle ✓ | 通过 |
| 原句 2 | L16 | ✓ | Henrie 贴身叙述（对照 Mr. Elton "was not observant"） | paying attention to small details / fidgeting / of all people ✓ | 通过 |
| 原句 3 | L25 | ✓ | Henrie 内心判断（叙述层） | allied / claw at Jane / make sure ✓ | 通过 |
| 原句 4 | L62 | ✓ | Henrie 贴身叙述 | sewed the conversation closed / neat stitches / a bit of a bounce ✓ | 通过 |

## 缺陷清单

无

## 待人工复核

无

ch34 完成：4 块，缺陷 0，待复核 0
---

# d 步二审 · ch35

## 结论：共 4 块，通过 2，缺陷 1，待复核 1

逐块核对结果（引语逐字比对 text/ch35_chapter_11.txt 第 13/28/43/49 行；说话人按 text 前后 ~200 字符窗口确认）：

- **原句 1**（text 第 13 行）：逐字一致 ✅。说话人按行文逻辑应为 Henrie（向 Mrs. Elton 说"you are kind"，并转向 Jane 确认），但本提取件从该行起章、无前置语境窗口可核，归为待人工复核。四子项齐全。关键词 invisibility / keep talking / from experience 均在引语内 ✅。
- **原句 2**（text 第 28 行）：逐字一致 ✅，说话人 Mrs. Elton 正确 ✅。四子项齐全。关键词 rematerialized / roaring whisper / double humiliation 均在引语内 ✅。引语完整未截短 ✅。
- **原句 3**（text 第 43 行）：逐字一致 ✅，但说话人归因错误 ❌（见缺陷 1）。四子项齐全。关键词 dematerialized / domestic strife / chatterboxes 均在引语内 ✅。
- **原句 4**（text 第 49 行）：逐字一致 ✅，说话人 Jane 正确 ✅。四子项齐全。关键词 each in her place 在引语内 ✅。

另核查「本章词汇」表 11 条例句（invisibility / humiliation / picturesque / self-effacing / jabber / luncheon / dematerialized / strife / saucy / laden / cross）：全部与 text 逐字一致，未列入本块计数。

## 缺陷清单

**缺陷 1（说话人反转 / 引语↔分析错位）**

- 类型：说话人归因错误（对应失败案例①说话人反转）
- 引语行原文：`> **原句 3:** ""Wonderful." Henrie had dematerialized again. Mrs. Elton was picking up her bags. "Perhaps I should have come in the coach, ... we chatterboxes!""`
- 中文理解原文：`**中文理解**：Henrie 说了句"太好了"，随即又"隐形"了——Mrs. Elton 只顾收拾包裹，开始滔滔自述……`
- 问题说明：text 第 40 行 Henrie 正在自述（"You are absolutely right, Mrs. Elton. ... And Jane, you must bring us back all the news from the vicarage—worms to the nest, I always say! You know, I am sure, that I grew up—"，话被打断），第 43 行紧接着的 `"Wonderful."` 是 Mrs. Elton 对"Jane 将欣然赴宴"这一安排的回应/打断，随后才是 `Henrie had dematerialized again`（Henrie 重新隐形）。逐字引语命中，但中文理解把"Wonderful." 归给 Henrie，与 text 语境相反。这正是"逐字命中≠说话人正确"的门禁缺口。
- 建议修法：把中文理解首句改为「Mrs. Elton 说了句"太好了"，随即 Henrie 又"隐形"了」，或将"太好了"明确标注为 Mrs. Elton 之语；若需保留"Henrie 的同意与否不在 Mrs. Elton 听觉范围内"这一分析点，应改为针对"dematerialized again"一句展开，而非针对"Wonderful."。

## 待人工复核

**原句 1 说话人**：text 提取件从第 13 行起章（`Mrs. Elton, you are kind! ...`），无前置语境窗口可直接确认说话人。按行文逻辑（向 Mrs. Elton 说"you are kind"、转向 Jane 追问）应属 Henrie，与中文理解一致；但缺乏文本内证据，建议人工翻阅全书该章起点确认，确认前不视为通过。

ch35 完成：4 块，缺陷 1，待复核 1
---

# d 步二审 · ch36

## 结论：共 4 块，通过 4，缺陷 0，待复核 0

核对对象：`notes/books/novels/miss-bates-by-catherine-cliff/ch36 unrelenting.md` ↔ `text/ch36_chapter_12.txt`

### 逐块核对记录

**原句 1**
- 逐字：md 引语行与 text L13 逐字一致（仅弯/直引号、撇号差异）。
- 说话人：叙述层第三人称贴身跟随 Henrie（POV），md 中文理解归因正确；"her niece"称谓符合 Henrie 视角（Jane 口中叫"Aunt Henny"，见 text L28/L37），与 md 读者视角提示自洽。
- 四子项齐全（中文理解/关键词/为什么这样写/读者视角提示）。
- 关键词：listening✅ profligate✅ expert✅，均在本块引语内。
- 无截短：引语止于"casual pose of comfort and leisure."完整句末。

**原句 2**
- 逐字：md 引语行与 text L25 逐字一致。
- 说话人：仍是 Henrie POV 叙述层，md 归因正确（隐含"她"即 Henrie）。
- 四子项齐全。
- 关键词：the cap of invisibility✅ eardrums✅ stretched taut✅，均在引语内。
- 无截短：止于"hoped Jane wouldn't notice."完整句末。

**原句 3**
- 逐字：md 引语行（对话段 + 紧接叙述段）与 text L91 逐字一致；引语止于"stroking her forehead in the dark."，恰为完整句末，未截短。引语含对话+叙述两部分，md 中文理解也分别覆盖（Jane 台词 + 叙述补句），对应关系正确。
- 说话人：对话为 Jane 说（"Yes, she was unrelenting..."针对 Mrs. Elton），md 中文理解"Jane 说"归因正确；叙述段为第三人称补叙，md 一并翻译并标注"叙述补一句"，无误。
- 四子项齐全。
- 关键词：up on the block✅ slaver✅ stroking her forehead✅，均在引语内。
- 无截短（见上）。

**原句 4**
- 逐字：md 引语行与 text L133 逐字一致。
- 说话人：Jane 说，md 中文理解归因正确。
- 四子项齐全。
- 关键词：friendliness and finality✅ slamming✅ sash✅，均在引语内。
- 无截短：整句完整。

### 其他检查
- 章号：md 前端标注"Chapter 12（Part Three）"，text 首行"Chapter 12"，一致，无跨章错标。
- 结构：4 块均「引语行 + 中文理解 + 关键词 + 为什么这样写 + 读者视角提示」齐全，无孤儿块、无重复块。
- 词汇表例句抽查：profligate/fêted/insufferable/trifler/unrelenting/fisticuffs/aghast/missives/governess/quilt/taut 共 11 条例句，均逐字命中 text 对应句，无幻觉。

## 缺陷清单（无则写"无"）

无

## 待人工复核

无

ch36 完成：4 块，缺陷 0，待复核 0
---

# d 步二审 · ch37

## 结论：共 4 块，通过 4，缺陷 0，待复核 0

逐块核对明细：

### 原句 1（md 行 21）
- **引语逐字**：`text/ch37` 第 13 行逐字一致 ✓（Frank Churchill / village on fire / at his instigation）
- **说话人**：引语为第三人称叙事（贴身跟随 Henrie 的视角陈述），`text` 前后窗口（行 13、行 16、行 19）均为叙事段，无任何直接引语归属，`中文理解` 亦按叙事描述处理——无归错说话人 ✓
- **对应**：关键词（instigation / on fire / assured）均在引语内命中 ✓；四子项（中文理解 / 关键词 / 为什么这样写 / 读者视角提示）齐全，均围绕此句 ✓；未见截短
- 词汇表例句（anticipatory，行 13）亦与 text 一致。

### 原句 2（md 行 33）
- **引语逐字**：`text` 第 56 行逐字一致 ✓
- **说话人**：紧邻前后窗口（行 56 同一段，行 53 起 `Jane seemed to be easily upset lately`）为 Henrie 视角的内心叙事，`中文理解` 表述为 Henrie 的感受——正确 ✓
- **对应**：关键词（petted / mother cat / paw）均在引语内 ✓；四子项齐全 ✓；未见截短

### 原句 3（md 行 45）
- **引语逐字**：`text` 第 62 行逐字一致 ✓
- **说话人**：`text` 行 62 为 `Jane's throat` 的直接描写，紧邻行 59 Henrie 的长段鼓动与行 65 Henrie 的 `"No?"` 反应；`中文理解` 明确归为 Jane 说出的"不"——正确 ✓（此处易与 Henrie 混淆，经窗口核对无误）
- **对应**：关键词（ripped / scab / suffering）均在引语内 ✓；四子项齐全 ✓；未见截短

### 原句 4（md 行 57）—— 含"controlled voice"句
- **引语逐字**：`text` 第 74 行逐字一致 ✓（含 `in a controlled voice`、`plaits`、`old maid`、`We wear curls!`、`it must be admitted, a slam`）
- **说话人**：`text` 行 74 明确为 `Jane said in a controlled voice`，属 Jane 对 Henrie（Henny 姨妈）说的整段话；`中文理解` 逐句归为 Jane，且"Henny 姨妈"称呼一致——正确 ✓
- **对应**：关键词（controlled voice / plaits / old maid）均在引语内 ✓；四子项齐全 ✓；未见截短
- **特别关注（controlled voice 呼应）**：ch37 已将该句列为 原句 4 引语块，且归属 Jane 正确。ch38「读者视角提示」所称"上一章 Jane 的 'controlled voice'"确为指向本章（ch37）该句的有意呼应，来源与归属均成立——**非缺陷**。

## 缺陷清单
无

## 待人工复核
无

ch37 完成：4 块，缺陷 0，待复核 0
---

# d 步二审 · ch38

**章节**：Chapter 14（Part Three: February–May 1812）· 精读分析
**提取件**：`text/ch38_chapter_14.txt`
**审查范围**：精读 md「引语块」逐对核对（引语逐字 / 说话人 / 引语↔分析对应 / 关键词回查 / 结构）

## 结论：共 4 块，通过 4，缺陷 0，待复核 0

## 缺陷清单（无则写"无"）

无。

## 逐块核对记录

### 块 1 · 原句 1
- **引语行**（md 第 21 行）：`> **原句 1:** "My love, I know you want to do your own hair, but I have set out these blossoms and my little box of pins—I have twenty-one, can you imagine?” Jane said nothing, glancing at the pins and the rosebuds as she removed her pelisse and hung it by the door."`
- **逐字核对**：text/ch38 第 13 行 `My love, I know you want to do your own hair, but I have set out these blossoms and my little box of pins—I have twenty-one, can you imagine?" Jane said nothing, glancing at the pins and the rosebuds as she removed her pelisse and hung it by the door.` —— **逐字命中**（实词无改写；仅弯引号/直引号差异）。
- **说话人核对**：前段话（"亲爱的……你敢想象吗"）出自 Henrie（她摆好花苞与别针盒、等 Jane 回应）；"Jane said nothing, glancing…"为叙述者描述 Jane 的动作。中文理解行（第 23 行）正确将对话归 Henrie、将动作归 Jane。text 前 ~200 字符窗口（第 13 行整段）：Jane 刚从牧师住宅回来，Henrie 摆花苞与别针替她梳头 → 归因正确。✅
- **关键词**：blossoms ✅、glancing ✅、pelisse ✅ —— 均在本块引语内。
- **引语↔分析对应**：中文理解、关键词、为什么这样写、读者视角提示四子项均围绕同一句；引语完整，无截短。（"上一章 Jane 刚说完'我这辈子都要自己梳头'"为正文跨章指代，非引语块，不纳入逐字核对。）

### 块 2 · 原句 2
- **引语行**（md 第 33 行）：`> **原句 2:** "Jane drew in the deep breath of someone calling on deep wells of patience. “Thank you, Aunt. You are very kind.”"`
- **逐字核对**：text/ch38 第 16 行 `Jane drew in the deep breath of someone calling on deep wells of patience. "Thank you, Aunt. You are very kind."` —— **逐字命中**。
- **说话人核对**：句为 Jane 的动作与台词（"谢谢你，姨妈。你真好"）。中文理解行（第 35 行）归 Jane。text 前 ~200 字符窗口（第 13–16 行）：Henrie 絮叨后"flinched a bit as she waited for Jane's response"，随后紧接本句 → 归因正确。✅
- **关键词**：deep wells of patience ✅、kind ✅ —— 均在本块引语内。
- **引语↔分析对应**：四子项均围绕同一句；引语完整，无截短。
- **特别核查（controlled voice）**：md 第 41 行读者视角提示写"把这一句与上一章 Jane 的'controlled voice'放在一起读"。经全文检索，"controlled voice" 仅出现于该读者视角提示行，**未作为本章引语块**；提示明确写"上一章"，属有意指向上一章的呼应。按任务规则，本章未把 "controlled voice" 列为引语块 → **非缺陷**。

### 块 3 · 原句 3
- **引语行**（md 第 45 行）：`> **原句 3:** "And she had given up that taste of power. … But wasn’t this precisely the idea? To never be frightening (as somehow, for no reason Henrie could understand, women like her were to the rest of the world)."`
- **逐字核对**：text/ch38 第 37 行 `And she had given up that taste of power. She never let herself think about it, it was too tantalizing. That brief period where she had stood up for what she wanted and taken what she needed. For Jane, she had vowed to live as a vessel of anodyne appreciation, a cat who had not only lost her claws but her teeth as well. She was aware she was rendered ridiculous, someone to be pitied. But wasn't this precisely the idea? To never be frightening (as somehow, for no reason Henrie could understand, women like her were to the rest of the world).` —— **逐字命中**（仅弯/直引号差异）。
- **说话人核对**：此为 Henrie 的内心独白/自由间接引语（用"她"自称、谈"为了 Jane"）。中文理解行（第 47 行）归 Henrie。text 第 37 行处于 Henrie 长段自辩流中 → 归因正确。✅
- **关键词**：taste of power ✅、anodyne ✅、claws ✅ —— 均在本块引语内。
- **引语↔分析对应**：四子项均围绕同一段自辩；引语完整，无截短。

### 块 4 · 原句 4
- **引语行**（md 第 57 行）：`> **原句 4:** "And this decision, to allow Jane to be prepared for this life, as she herself was certainly not, this is what the girl resented now? Henrie’s heart, which had tried to hold onto Jane as life took the girl further and further away, now seemed to tumble off the back of that thundering carriage, like lost luggage, the clasp broken and the contents splayed in the dirt."`
- **逐字核对**：text/ch38 第 61 行 `And this decision, to allow Jane to be prepared for this life, as she herself was certainly not, this is what the girl resented now? Henrie's heart, which had tried to hold onto Jane as life took the girl further and further away, now seemed to tumble off the back of that thundering carriage, like lost luggage, the clasp broken and the contents splayed in the dirt.` —— **逐字命中**。
- **说话人核对**：Henrie 的内心独白（"她本人""Henrie 的心"）。中文理解行（第 59 行）归 Henrie。text 第 61 行为章末 Henrie 内心流 → 归因正确。✅
- **关键词**：resented ✅、tumble off ✅、lost luggage ✅ —— 均在本块引语内。
- **引语↔分析对应**：四子项均围绕同一句；引语完整，无截短。（"呼应此前 Jane 被送往 Campbell 家的'隆隆马车'"为正文跨章指代，非引语块。）

## 结构检查
- 4 个引语块均齐全「引语行 + 中文理解 + 关键词 + 为什么这样写 + 读者视角提示」四子项。
- 无孤儿块（引语存在而无分析）、无重复块。
- 本章另含"本章词汇"表与"一句话总结"，非引语块，不纳入逐字核对；其中词汇例句均可回溯至 text/ch38 对应行（如 anodyne→第 37 行、superabundance/gewgaws/bartering→第 55/13/46 行、pelisse→第 13 行、governess→第 49 行、rendered→第 37 行、self-sufficiency→第 22 行、slipper→第 28 行、thorns→第 13 行），抽查无误。

## 待人工复核

无。

ch38 完成：4 块，缺陷 0，待复核 0
---

# d 步二审 · ch39

## 结论：共 4 块，通过 4，缺陷 0，待复核 0

### 逐块核对明细

**原句 1** ✅
- 引语逐字：与 `text/ch39_chapter_15.txt` line 13 完全一致（`Henrie held the wooden overshoes up in each hand... where Henrie could be of some real worth.`）。
- 说话人：第三人称旁白（跟随 Henrie），紧跟 Henrie 的对话开场之后；归因为「Henrie 的处境旁白」正确。
- 引语↔分析：四子项（中文理解/关键词/为什么这样写/读者视角提示）均在讲"刮干净木套鞋换被需要感"这同一句；读者视角提示中"下一句 Jane 说'Mrs. Elton 派马车来'"与原文 line 16 "Mrs. Elton is sending her carriage, Aunt Henny." 相符，属于准确的跨句指引，非拼接错误。
- 关键词：smug ✓、of some real worth ✓、overshoes ✓（均在引语内，无词形变化问题）。

**原句 2** ✅
- 引语逐字：与 line 35 完全一致（含破折号 `three months—no, six months`）。
- 说话人：旁白叙述 Henrie 的内心讨价还价，归因正确（"she said to herself"）。
- 引语↔分析：四子项均围绕"被遗忘焦虑→跟冥冥主宰折寿交易"，与引语一致；引语截停在"the Eltons' kind attention."，后文"The matter felt of deepest importance..."未被引用，但四子项未涉及该后续内容，无截短导致的证据缺口。
- 关键词：misplacing ✓、barter ✓、the Eltons' kind attention ✓。

**原句 3** ✅
- 引语逐字：与 line 53 完全一致（含 `we, we` 与 `What is it to forget someone imaginary?—there can be no consequence.`）。
- 说话人：出自 **Jane** 的整段控诉（引号内），归因为「Jane 发言」正确；本段是 Jane 言语正面，非 Henrie。说话人无反转。
- 引语↔分析：四子项围绕"隐形女性=虚构之物，生与死之别"，与 Jane 控诉主题吻合。
- 关键词：undistinguished and unmarried women ✓、imaginary beings ✓、the difference between living and dying ✓。

**原句 4** ✅
- 引语逐字：与 line 72 完全一致。
- 说话人：第三人称旁白（Henrie 独自下到底层），归因正确。
- 引语↔分析：四子项围绕"楼上喧闹/楼下空寂的上下隔离、熟人数量与归属感无关"，与引语一致。
- 关键词：not a soul ✓、extra lonely ✓、This world was not hers ✓。

### 结构检查
- 4 块齐全，每块均含「引语行 + 中文理解 + 关键词 + 为什么这样写 + 读者视角提示」五要素（四子项齐备）。
- 无孤儿块、无重复块、无缺行。
- 跨块引用（原句1 读者提示→Jane 马车句）准确，未与无关分析行拼装。

## 缺陷清单

无

## 待人工复核

无

ch39 完成：4 块，缺陷 0，待复核 0
---

# d 步二审 · ch40

## 结论：共 4 块，通过 4，缺陷 0，待复核 1

## 缺陷清单：无

## 待人工复核

- **章号/标题内部不一致（元数据）**：本 md 文件名与原文提取件均为 `ch40`（`ch40 official loss of hope.md` / `text/ch40_chapter_1.txt`），但 md 顶部 title 与正文标题写的是「Miss Bates 精读 39 · Chapter 1（Part Four）」。引语与原文核对无误，但「精读 39」与文件名「ch40」存在编号错位，建议人工确认本章在精读序列中的正确章号后统一修改 title 或文件名。此项属元数据，不属本次引语↔分析五项核对范围，故仅标记待复核。

## 逐块核对明细

### 原句 1 — 通过
- **引语逐字**：text L14 逐字命中，含"Lost in every sense."独立句。
- **说话人**：叙述者关于 Henrie 的陈述（"Henrie dated her complete and official loss…"），与中文理解"Henrie 把自己'彻底地、正式地失去简'的日期定在……"一致。
- **引语↔分析**：四子项均围绕"草莓会=母女关系分水岭"这一句，无截短（引语含全句）。
- **关键词**：loss、strawberry party、in every sense 均在本块引语中。
- **结构**：引语行 + 中文理解/关键词/为什么这样写/读者视角提示 四子项齐全。

### 原句 2 — 通过
- **引语逐字**：text L20 逐字命中，含"’72?"（弯引号）与"Was that—no."破折号。
- **说话人**：Henrie 记忆的叙述流（"Her eyes strained into the past."），与中文理解"她的目光费力地伸进过去"一致。
- **引语↔分析**：四子项均围绕"摘草莓→回忆童年→撞上弟弟哈利之死"同一句，引语完整未截短。
- **关键词**：strained into the past、cramming、the berries of the buried 均在本块引语中。
- **结构**：四子项齐全。

### 原句 3 — 通过
- **引语逐字**：text L23 逐字命中。
- **说话人**：叙述者关于埃尔顿夫妇接 Henrie 与 Jane 的陈述（"The Eltons…had fetched her and Jane…"），与中文理解"埃尔顿夫妇……接了她和简来参加聚会"一致。
- **引语↔分析**：四子项均围绕"埃尔顿夫妇殷勤补过+聚会仍出岔子"同一句，引语完整未截短。
- **关键词**：ball fiasco、equipage、ill-behaved asses 均在本块引语中。
- **结构**：四子项齐全。

### 原句 4 — 通过
- **引语逐字**：text L50 逐字命中，含"she, Henrie, could not gain access"等。
- **说话人**：叙述者关于 Henrie 上楼发现 Jane 病卧的陈述，与中文理解"Henrie 心跳如鼓地小跑上狭窄的楼梯，发现简躺在床上"一致。
- **引语↔分析**：四子项均围绕"Henrie 无法进入 Jane 的世界"同一句，引语完整未截短。
- **关键词**：howled like an animal、distress、could not gain access 均在本块引语中。
- **结构**：四子项齐全。

ch40 完成：4 块，缺陷 0，待复核 1
---

# d 步二审 · ch41

## 结论：共 4 块，通过 4，缺陷 0，待复核 0

审查对象：`notes/books/novels/miss-bates-by-catherine-cliff/ch41 there lies the difficulty.md`
对照原文：`notes/books/novels/miss-bates-by-catherine-cliff/text/ch41_chapter_2.txt`

| 块 | 引语逐字核对 | 说话人核对（窗口 ~200 字符） | 引语↔分析对应 | 关键词回查 | 结构 | 结论 |
|---|---|---|---|---|---|---|
| 原句 1 | text L16 逐字一致 | 叙述者（Henrie 视角），正确 | 四子项同一句，未截短 | enthusiasm / patchwork / slanted meadow 均在 | 完整 | ✅ 通过 |
| 原句 2 | text L31 逐字一致 | 叙述者（Henrie 视角），正确 | 四子项同一句，未截短 | the lens / maliciously / magnifying glass 均在 | 完整 | ✅ 通过 |
| 原句 3 | text L40 逐字一致 | 引语为 Emma Woodhouse 所说；中文理解归因「爱玛」，正确 | 四子项同一句，未截短 | three dull utterances / reverberated / not invisible 均在 | 完整 | ✅ 通过 |
| 原句 4 | text L49 逐字一致 | 叙述者（Henrie 视角），正确 | 四子项同一句，未截短 | mortification / wriggling / laid bare 均在 | 完整 | ✅ 通过 |

### 逐块核对明细

- **原句 1**：md 引语行与 text L16 完全一致。中文理解忠实原文（"简对求婚者们毫无兴趣…像她母亲的拼布被面"）。关键词三词均在引语中。子项"为什么这样写""读者视角提示"均紧扣 mother's patchwork 比喻与 "the next day" 时间焊点，无张冠李戴。✅
- **原句 2**：md 引语行与 text L31 完全一致。说话人为叙述者/Henrie 视角，"爱玛正隔着它恶意地窥视"归因正确。关键词三词均在。分析（屠宰流程：放大镜/锤子/牲口）与引语逐项对应。✅
- **原句 3**：md 引语行与 text L40 完全一致（含弯引号）。引语为 Emma 对 Henrie 说的羞辱话，中文理解归因「爱玛」正确。关键词三词均在。分析正确指出引语后紧跟记忆质疑（"Was that actually what she said?"），对应到位。✅
- **原句 4**：md 引语行与 text L49 完全一致。"爱玛和弗兰克继续说笑"归因正确（text L49 "Emma Woodhouse and Frank Churchill carried on"）。关键词三词均在。分析紧扣 mortification / wriggling / laid bare，未超引语支撑范围。✅

## 缺陷清单（无）

无

## 待人工复核

无

ch41 完成：4 块，缺陷 0，待复核 0
---

# d 步二审 · ch42

## 结论：共 4 块，通过 4，缺陷 0，待复核 0

## 逐块核对明细

### 块 1（原句 1）
- **引语逐字**：md 引语行 = text 第 13 段（本章开篇首段），逐字一致，段落完整未截短（止于 "She hardly ever let herself cry."）。
- **说话人**：窗口 ~200 字符为章首叙述，第三人称贴身叙述 Henrie（含 "(Jeannette!)" 旁白），与中文理解归因一致。
- **引语↔分析对应**：四子项（中文理解/关键词/为什么这样写/读者视角提示）均围绕 Henrie 放 Patty 假、独自面对羞辱、几乎不哭展开，对应同一句。
- **关键词回查**：`a second self` ✓、`the choking knot of humiliation` ✓、`let herself cry` ✓（均逐字命中，无词形变化问题）。
- **结构**：引语行 + 四子项齐全。

### 块 2（原句 2）
- **引语逐字**：md 引语行 = text 第 25 段，逐字一致，单段完整未截短。
- **说话人**：此句为 Henrie 所读信匣中一封信（Frank 写给 Jane 的私信）末尾的落款语；上下文为 Henrie 偷读，"There was no signature..." 是 Henrie 的视角对信的描述。中文理解"信的末尾没有署名，只有一句话"归因正确（Henrie 读信，而非说话人）。窗口第 22 段确认 Henrie 抽出信、"She would just read who it was from"。
- **引语↔分析对应**：四子项均讲这一无署名私语令 Henrie 当场瓦解"只看一眼"的自我约束，对应同一句。
- **关键词回查**：`no signature` ✓、`I dream, as ever` ✓。
- **结构**：齐全。

### 块 3（原句 3）
- **引语逐字**：md 引语行 = text 第 43 段，逐字一致，整段完整未截短（止于 "She kept looking."）。
- **说话人**：上下文为紧接"两个讨人嫌的姑妈"（"Of our two objectionable aunts..."，text 第 40 段）之后 Henrie 的心理反应；窗口第 43 段本身即叙述 Henrie，归因正确。中文理解中"又是那记敲门声"呼应前段引文中的信，归属 Henrie 视角，正确。
- **引语↔分析对应**：四子项围绕 Henrie 的恶心、错位的脸、继续读下去，对应同一句。"为什么这样写"中提到的"两个讨人嫌的姑妈"指前一段引文（text 第 40 段），属跨句指代而非截短，符合上下文，无幻觉风险。
- **关键词回查**：`the knocker again` ✓、`outburst` ✓、`the wrong geometry of her face` ✓。
- **结构**：齐全。

### 块 4（原句 4）
- **引语逐字**：md 引语行 = text 第 85 段（本章末段），逐字一致，整段完整未截短。
- **说话人**：窗口第 85 段为 Jane 深夜归来宣布，"As she snuffed out the candle... she announced"——说话人确为 Jane，与中文理解归因一致。Henrie 装睡（"Henrie pretended to be asleep, but Jane knew she was not"）亦属叙述。
- **引语↔分析对应**：四子项围绕 Jane 一句话覆盖母亲一晚挣扎、堵死回应，对应同一句。
- **关键词回查**：`an awful silence` ✓、`left Highbury for good` ✓、`Please do not say a word` ✓。
- **结构**：齐全。

## 缺陷清单
无

## 待人工复核
无

---

ch42 完成：4 块，缺陷 0，待复核 0
---

# d 步二审 · ch43

审查对象：《Miss Bates: Emma Revisited》精读库 ch43「the beast arrives」，提取件 `text/ch43_chapter_4.txt`。
方法：每个引语块逐字比对 text 原文，命中后在前后 ~200 字符窗口确认说话人归属，再核对四子项与关键词。

## 结论：共 3 块，通过 3，缺陷 0，待复核 1

## 逐块核对

### 原句 1 —— ✅ 通过
- **引语逐字**：命中 text 第 13 行，逐字一致（仅 `Henrie's` 弯/直撇号差异，允许）。
- **说话人**：本块为叙述段，非对话；无说话人归属问题。
- **引语↔分析**：中文理解逐句对应（次日到访、望窗外、Jane 写信、笔尖沙沙配愤怒念头、无解）。无截短，原文整句完整引用。
- **关键词回查**：`The Beast`、`with plenty of fanfare`、`None yet read like a solution` 均在引语中命中。
- **结构**：引语行 + 中文理解 / 关键词 / 为什么这样写 / 读者视角提示 四子项齐全。

### 原句 2 —— ✅ 通过
- **引语逐字**：命中 text 第 37 行，逐字一致。
- **说话人**：上下文链——第 28 行 Henrie 应答 Emma、第 31 行 Emma 问 soirée、第 34 行 Henrie 内心独白、第 37 行接续回答，归 Henrie 正确（md 中文理解归 Henrie 也一致）。
- **引语↔分析**：中文理解逐句对应（愉快小聚会、Box Hill 众人、唯独 Emma 与 Knightley 缺席、Coles/Goddard/Otway、快活收尾）；"Coles" 指 Cole 家（中文表述"Cole 家两口子"略窄于"the Coles"，非实质错误）。无截短。
- **关键词回查**：`bar you`、`could not attend`、`a jolly little crush` 均在引语中命中。
- **结构**：四子项齐全。
- 备注：md 导航"独自在前厅接待"与 text 第 22 行"Henrie followed Jane into her room"在接待空间上有细微出入，属叙事概括，非引语块缺陷。

### 原句 3 —— ✅ 通过
- **引语逐字**：命中 text 第 52 行，逐字一致。
- **说话人**：上下文链——第 46 行 Henrie 抛消息、第 49 行"Emma had not known"、第 52 行 Henrie 解释确认，归 Henrie 正确（md 中文理解同样归 Henrie）。
- **引语↔分析**：中文理解逐句对应（是的走了、Hatfield/Hartfield 口误纠正、奇怪、附著之情、精力与自由涌动、更敷衍的道谢）。无截短。
- **关键词回查**：`I beg pardon`、`That is odd`、`more cursorily than usual` 均在引语中命中。
- **结构**：四子项齐全。

## 缺陷清单（无则写"无"）

无

## 待人工复核

1. **frontmatter 编号不一致**：文件头 `title: Miss Bates 精读 42 · Chapter 4（Part Four）`，而文件名与正文标题为 `ch43`。精读序号 42 与文件 ch43 不一致，请人工确认该序号应为 42 还是 43（属内部编号问题，非引语/说话人缺陷）。

ch43 完成：3 块，缺陷 0，待复核 1
---

# d 步二审 · ch44

## 结论：共 4 块，通过 4，缺陷 0，待复核 0

## 缺陷清单（无则写"无"）

无

## 核查明细

### 原句 1
- **引语行**：`> **原句 1:** "When they received the news of Mrs. Churchill’s death from Mrs. Weston, Jane had been in bed for several days with a splitting headache and a sore throat. Henrie knew that her worry for the girl was making her intolerable, but also that she could no more control it than Jane could control her migraine."`
- **text/ch44 命中**：text/ch44_chapter_5.txt 第 13 段，逐字一致（弯引号、撇号一致；无改写）。
- **说话人**：第三人称叙事（紧贴 Henrie 视角）。中文理解归因为"Henrie 明白"——命中，说话人正确。
- **引语↔分析对应**：中文理解/关键词/为什么这样写/读者视角提示 四子项齐全，均讲同一句；无截短。
- **关键词**：intolerable ✓、no more control it than ✓、migraine ✓（均在本句出现）。

### 原句 2
- **引语行**：`> **原句 2:** "“Good God, Aunt. Just leave me be!” Jane’s voice was hoarse; she held her mittened hands to her muffled ears and closed her eyes. “There is nothing anyone can do for me. Emma Woodhouse has ruined my life, and now I will have to go to Bristol to be abused by a mistress more uncouth than Augusta Elton, if such a thing might exist! Let me be. Oh, I wish I were dead.”"`
- **text/ch44 命中**：text/ch44_chapter_5.txt 第 25 段，逐字一致。
- **说话人**：Jane（对 Henrie 说话）。中文理解归因为 Jane 的爆发——命中，说话人正确。
- **引语↔分析对应**：四子项齐全，均围绕 Jane 的绝望爆发；无截短。
- **关键词**：ruined my life ✓、uncouth ✓、I wish I were dead ✓。

### 原句 3
- **引语行**：`> **原句 3:** "Henrie retreated and placed a hand on the pianoforte, the other across her mouth, sucking in huge breaths of air through her nose. She moved to the front of the pianoforte and sat down to the stool, and then simply banged on every note she could reach. She ignored her mother’s shouted queries; she ignored Jane’s silence."`
- **text/ch44 命中**：text/ch44_chapter_5.txt 第 28 段，逐字一致。
- **说话人**：第三人称叙事（描述 Henrie 动作）。中文理解归因为"Henrie 退了出来..."——命中，说话人正确。
- **引语↔分析对应**：四子项齐全；中文理解行末尾"跟原句 2 里 Jane 的嘶喊正好互补"为合理互文引用，非拼装，正确。
- **关键词**：retreated ✓、banged on every note ✓、ignored ✓。

### 原句 4
- **引语行**：`> **原句 4:** "But, when Henrie had finished, a plan came to her, fully articulated. She called Patty and asked her to go get Mr. Perry, whatever Jane might protest, while she sat down to write a letter."`
- **text/ch44 命中**：text/ch44_chapter_5.txt 第 31 段，逐字一致。
- **说话人**：第三人称叙事（描述 Henrie 的计划）。中文理解归因为"Henrie 砸完琴，一个计划..."——命中，说话人正确。
- **引语↔分析对应**：四子项齐全，均讲"计划成形→写信"；无截短。
- **关键词**：a plan came to her ✓、fully articulated ✓、whatever Jane might protest ✓。

## 结构
- 4 个引语块结构完整（引语行 + 中文理解 + 关键词 + 为什么这样写 + 读者视角提示）。
- 无孤儿引语、无重复块、无跨章串错。
- 附注：本章词汇表例句（intolerable / migraine / wretched / pianoforte / articulated / hoarse / nostrils / bracing / muffled / pillow / stool）经逐句比对 text/ch44，均与原文逐字一致，未发现错配。

## 待人工复核

无

ch44 完成：4 块，缺陷 0，待复核 0
---

# d 步二审 · ch45

## 结论：共 4 块，通过 4，缺陷 0，待复核 0

## 缺陷清单（无则写"无"）

无

## 各块核对明细

### 原句 1
- 引语逐字：text/ch45 第 16 行完全一致（含弯引号 aunt’s），✓
- 说话人：Henrie（写信人）自述，窗口上下文为信首吊唁语，归因正确 ✓
- 引语↔分析：引语完整（至句号 "dear uncle."），四子项均在讲同一句 ✓
- 关键词：sadness ✓、passing ✓、terrible loss ✓
- 结构：引语行 + 中文理解/关键词/为什么这样写/读者视角提示 齐全 ✓

### 原句 2
- 引语逐字：text/ch45 第 22 行逐字一致（peerless、’Twas 直引号、unheeded 等全部原样）✓
- 说话人：Henrie 转述自己对 Mrs. Weston 说的失言，为 Henrie 的声音，归因正确 ✓
- 引语↔分析：引语止于自然句末 "said too much."；text 其后尚有 "I just obscured my remark…your secret is safe with me!" 数句未引，但四子项（失言、括号感叹号、"slipped out unheeded"/"said too much"、敬重程度暗指 Jane）均落在引语范围内，未越界支撑，**不构成截短缺陷** ✓
- 关键词：without thinking ✓、slipped out unheeded ✓、said too much ✓
- 结构：齐全 ✓

### 原句 3
- 引语逐字：text/ch45 第 25 行完全一致（含 "grow wan"、"baked peaches and cream"）✓
- 说话人：Henrie，归因正确 ✓
- 引语↔分析：引语完整至句号；"some here"/"baked peaches" 加密解读均基于本句 ✓
- 关键词：the heart of the matter ✓、grow wan ✓、lost their appetite ✓
- 结构：齐全 ✓

### 原句 4
- 引语逐字：text/ch45 第 28 行一致（含双括号、Jane’s 弯引号、Frank!）✓
- 说话人：Henrie，归因正确 ✓
- 引语↔分析：引语止于自然句末 "whose name it is!"；text 其后 "Well, I am certain…appellation!" 未引，但四子项（discretion/clandestine/named her/frank 双关）均在引语内，无越界 ✓
- 关键词：discretion itself ✓、clandestine ✓、I have named her ✓
- 结构：齐全 ✓

## 附加检查（词汇例句，非引语块但一并核对）
- appellation（text L28）、racket（L34）、negligible（L37）、instrument（L31）、keyboard（L34）例句逐字命中原文 ✓
- 章号：md 与 text 均为 "Chapter 6"，无跨章错标 ✓

## 待人工复核

无

ch45 完成：4 块，缺陷 0，待复核 0
---

# d 步二审 · ch46

> 审查对象：《Miss Bates: Emma Revisited》Chapter 7（精读 md：`notes/books/novels/miss-bates-by-catherine-cliff/ch46 eleven days after.md`）
> 原文提取件：`notes/books/novels/miss-bates-by-catherine-cliff/text/ch46_chapter_7.txt`

## 结论：共 4 块，通过 4，缺陷 0，待复核 0

## 逐块核对明细

### 原句 1
- **逐字核对**：引语行与 text 第 13 段逐字一致（含弯引号与破折号差异为直/弯与省略号允许范围内，实词无改写）。**命中**。
- **说话人**：本段为全知叙述（narration），无对话归属问题；中文理解归因于「Frank 回来/邀请 Jane/带回订婚消息」与原文一致。
- **引语↔分析对应**：中文理解、关键词、为什么这样写、读者视角提示均围绕「两个精确天数并置＋he 不看 Henrie＋打了折扣的 cheerful confidence」展开，与引语同一段。**无截短**（引语完整至"They returned nearly two hours later with the happy surprise news of their engagement."）。
- **关键词回查**：`a certain letter` ✓、`enforced soberness` ✓、`cheerful confidence` ✓。
- **结构**：引语行＋中文理解＋关键词＋为什么这样写＋读者视角提示，齐全。

### 原句 2
- **逐字核对**：引语行与 text 第 16 段（Jane 对话句＋其后叙述句）逐字一致。**命中**。
- **说话人**：对话引号内为 **Jane** 对「Aunt Henny」所说（原文"Aunt Henny"）；引号外叙述为作者视角。中文理解归因「Jane 天真地转述未婚夫的判断」正确。**说话人无反转**。
- **引语↔分析对应**：四子项均讲同一句（"he was right" 的讽刺、chilly smile、So it goes 收束）；`So it goes.` 为 text 第 16 段段末，分析称其为「结尾」收束（非声称全章末句），**不构成跨段/跨句拼装**。
- **关键词回查**：`chilly smile` ✓、`Cupid's bow mouth` ✓、`forgive` ✓。
- **结构**：齐全。

### 原句 3
- **逐字核对**：引语行与 text 第 46 段逐字一致（含"Frank cut her off."引导句）。**命中**。
- **说话人**：引号内为 **Frank**（"we will not even be able to announce..."），引号外叙述归 Frank。中文理解归因「Frank 打断 Henrie 的话」正确。**说话人无反转**。
- **引语↔分析对应**：四子项围绕「礼貌用语＋as if he would like to bite her＋cut her off」展开，与引语同段；**无截短**。
- **关键词回查**：`cut her off` ✓、`suitable time` ✓、`bite her` ✓。
- **结构**：齐全。

### 原句 4
- **逐字核对**：引语行与 text 第 55 段（text 末段）逐字一致。**命中**。
- **说话人**：引号内为 **Jane**（"Aunt Henny... you know and approve"），引号外叙述为作者视角。中文理解归因「Jane 说这不算真正的秘密」正确。**说话人无反转**。
- **引语↔分析对应**：四子项均讲同一句；分析称 "It was all worth it." 为「全章最后一句」，经核对 **text 第 55 段确为全文末段末句**，判断正确。**无截短**。
- **关键词回查**：`real secret` ✓、`ravishing` ✓、`worth it` ✓。
- **结构**：齐全。

## 防幻觉排查
- 引语行与中文理解行均在 md 同一「### 原句 N」块内且相邻，未跨块拼装。
- 无跨章章号错标：md 标注 Chapter 7（Part Four），text 页眉/正文均为 Chapter 7 / "7"，一致。
- 无说话人反转、无引语截短、无孤儿/重复块。

## 缺陷清单
无

## 待人工复核
无

---

ch46 完成：4 块，缺陷 0，待复核 0
---

# d 步二审 · ch47

## 结论：共 4 块，通过 4，缺陷 0，待复核 0

## 缺陷清单（无则写"无"）：无

逐块核对记录：

**原句 1**：引语逐字与 text/ch47 第 13 段完全一致（至"a month ago."段末收尾，无截短）。说话人为第三人称叙事者（Henrie 贴身视角），中文理解归因正确。关键词 reconciled / wriggle away / suspicions 均在引语内命中。四子项（中文理解、关键词、为什么这样写、读者视角提示）齐备，且都在讨论同一句——"riding back and forth"奔波、"wriggle away"回勾、"seemed entirely reconciled"中"seemed"的秤砣作用，与"without arousing the suspicions of the populace"的读者提示均对应本块引语。✅

**原句 2**：引语逐字与 text/ch47 第 16 段一致（含内嵌引号弯/直差异，属允许范围）。说话人为 Frank Churchill（"he"= Frank，对到访的 Mrs. Cole 说话），中文理解归因正确。关键词 casually / ajar / inventing a task 均在引语内命中。四子项齐备且同句——挪座位、老太太张着嘴打瞌睡、编道具戏的喜剧程式。✅

**原句 3**：引语逐字与 text/ch47 第 19 段一致，结尾"beautiful girl?"疑问句完整包含在引语内，未截短。说话人为第三人称叙事者（Henrie 视角），中文理解归因正确。关键词 the girl Henrie had sent away / pet mouse / beautiful girl 均命中。四子项齐备且同句——"as she had ever been since"的愧疚、"他怎么可能想离开"的留白。✅

**原句 4**：引语逐字与 text/ch47 第 28 段一致。说话人为第三人称叙事者（Henrie 视角），中文理解归因正确。关键词 borrowing trouble / invisible stitches / little ones 均命中。四子项齐备且同句——"borrowing trouble"转折阀、幸福清单、"invisible stitches"接续序章丝带意象。✅

结构检查：共 4 块引语块，每块「引语行 + 中文理解 + 关键词 + 为什么这样写 + 读者视角提示」五要素齐全，无孤儿块、无重复块、无跨章章号错标、无说话人反转、无引语截短。

## 待人工复核

无。

ch47 完成：4 块，缺陷 0，待复核 0
---

# d 步二审 · ch48

## 结论：共 4 块，通过 4，缺陷 0，待复核 0

## 缺陷清单（无则写"无"）

无

## 逐块核对明细

### 原句 1
- **引语逐字**：`One month passed, then two. Frank Churchill had been in Yorkshire for eleven weeks, and Jane's cough, which had never disappeared entirely, gained in force that autumn, quickly becoming a barking spasm she could not control and that pained her abdomen with its violence. As a result, she had not been present at Mrs. Perry's one morning. Had she believed in Him, Henrie might have thought the cough had been sent by God precisely for this reason.`
  - text/ch48_chapter_9.txt 第 13 行逐字一致 ✓（弯引号/撇号差异属允许范围）
- **说话人**：叙述者对 Henrie 的有限视角叙述，与「中文理解」中 Henrie 作为视角主人的归因一致 ✓
- **引语↔分析对应**：四子项（中文理解/关键词/为什么这样写/读者视角提示）均围绕"咳嗽使 Jane 缺席 Mrs. Perry 家"这一句，无截短 ✓
- **关键词**：barking spasm、precisely、sent by God 均在引语内 ✓

### 原句 2
- **引语逐字**：`"Oh yes," she said, "Indeed I know the new master of Enscombe! Although he'd probably be hard-pressed to pick me out of a crowd. Just another plump matron, isn't that the way, Cassie?" The two ladies chortled, but Henrie was alert and focused.`
  - text 第 19 行逐字一致 ✓
- **说话人**：text 第 16 行明确 Mrs. Holyday 是 Mrs. Perry 的 cousin，来自 Enscombe 附近村庄，第 19 行 "she said" 即 Mrs. Holyday；md「中文理解」归因 Mrs. Holyday ✓
- **引语↔分析对应**：四子项均围绕"Mrs. Holyday 自嘲认识 Enscombe 新主人 + Henrie 警觉"同一句，无截短 ✓
- **关键词**：the new master of Enscombe、alert and focused 均在引语内 ✓

### 原句 3
- **引语逐字**：`"Dear me, I think people in the North are not so nice in their ideas of obsequies! When it gets dark shortly after luncheon, one must take cheer where one can. But I think you are right, now that you mention it. I saw him just two weeks ago at the assembly, and he seemed to be limiting himself to flirting along the sidelines rather than in the quadrille. Yes, when I come to think of it, he sat with the belle of the county and her mother for two glasses of ratafia, which really counts for more than a waltz, I would say! Several of my acquaintance were making predictions for January when he may change his black band for gold! The girl, in addition to being a happy little plump beauty, mind you, is the only daughter of the man who owns every mill north of Sheffield, so the advantage would go both ways."`
  - text 第 31 行逐字一致 ✓
- **说话人**：text 上下文为 Mrs. Holyday 的连续发言（承接第 28 行 Henrie 插话之后 Mrs. Holyday 的回应）；md「中文理解」归因 Mrs. Holyday ✓
- **引语↔分析对应**：四子项均围绕"北边守丧规矩不讲究 + 舞会调情 + 一月订婚预测"同一整段，未截短 ✓
- **关键词**：flirting、predictions for January、the only daughter 均在引语内 ✓

### 原句 4
- **引语逐字**：`Henrie could think of nothing else than this report, and lived in fear of the anecdote being repeated in Jane's presence. As a preventative measure, she made sure to be at her most voluble when any likely source visited Jane, who spent the days indoors by their small fire or in bed. Mr. Perry had come to prescribe mustard poultices, but they seemed to have little effect other than making their bed smell like a ham breakfast.`
  - text 第 40 行逐字一致 ✓
- **说话人**：叙述者对 Henrie 的叙述，与「中文理解」中 Henrie 的防范举措一致 ✓
- **引语↔分析对应**：四子项均围绕"Henrie 用话多作防线 + 芥子泥黑色幽默"同一段，无截短 ✓
- **关键词**：lived in fear、preventative measure、her most voluble 均在引语内 ✓

## 待人工复核

无

---

ch48 完成：4 块，缺陷 0，待复核 0
---

# d 步二审 · ch49

## 结论：共 4 块，通过 4，缺陷 0，待复核 0

核对对象：`notes/books/novels/miss-bates-by-catherine-cliff/ch49 decant her longevity.md` ↔ 原文提取件 `text/ch49_chapter_10.txt`。

逐块结果：

**原句 1**（flying visit / no longer seemed anxious / dwindling frequency）
- 引语逐字：与 text 第 13 行全段一致（逐字命中）。✓
- 说话人：叙述层（关于 Frank 来访、Jane 的冷淡、Henrie 的洞察），非角色对话；中文理解归因为叙述描写，正确。✓
- 引语↔分析：中文理解、关键词、为什么这样写、读者视角提示均在讲 Frank 拖延 / Jane 不再焦虑 / 信件递减；引语未被截短，四子项全部落在引语范围内。✓
- 关键词：flying visit ✓、no longer seemed anxious ✓、dwindling frequency ✓ 均在本块引语命中。

**原句 2**（useful information / every fiber / a man of her own choosing）
- 引语逐字：与 text 第 19 行全段一致（含弯引号内的 Mrs. Campbell 台词）。✓
- 说话人：末句为 Mrs. Campbell 低声对 Duncan 说的台词；中文理解正确归因为 Campbell 太太对 Jane 气色的担忧。✓
- 引语↔分析：四子项围绕"没人认为 Henrie 有 useful information"和"自选之人"两个重点，均在引语内；无截短。✓
- 关键词：useful information ✓、every fiber ✓、a man of her own choosing ✓ 均命中。

**原句 3**（momentarily cheered / pulled back in surprise / solicitously）
- 引语逐字：与 text 第 28 行全段一致。✓
- 说话人：叙述层（Henrie 视角看 Frank 一行），非对话；中文理解正确。✓
- 引语↔分析：四子项聚焦"靴子穿反的闹剧 vs Frank 惊惶一缩"、"Henrie saw it, and so must Jane have"，均在引语内；无截短。✓
- 关键词：momentarily cheered ✓、pulled back in surprise ✓、solicitously ✓ 均命中。

**原句 4**（did not sleep much / a flat white lozenge / decant）
- 引语逐字：与 text 第 50 行全段一致。✓
- 说话人：叙述层（Henrie 夜间巡屋的内心），非对话；中文理解正确。✓
- 引语↔分析：四子项围绕"菱形含片""倒寿命"两个意象，均在引语内；无截短。✓
- 关键词：did not sleep much ✓、a flat white lozenge ✓、decant ✓ 均命中。

结构检查：4 块「引语行 + 中文理解 + 关键词 + 为什么这样写 + 读者视角提示」齐全，无孤儿块、无重复块。✓

## 缺陷清单（无则写"无"）

无。

## 待人工复核

- 无实质性问题。仅一处非引语级小瑕疵（不影响引语↔分析对应）：原句 4 的"为什么这样写"中把 decant 写作"decan（滗、倒）"（缺尾字母 t），属于拼写小误，引语行本身写的是正确的 "decant"；如后续校对可顺手更正，非二审缺陷。

ch49 完成：4 块，缺陷 0，待复核 0
---

# d 步二审 · ch50

## 结论：共 4 块，通过 4，缺陷 0，待复核 0

## 缺陷清单

无

## 待人工复核

无

## 核对明细

- **原句 1**（text 第 13 行）：逐字完全一致（含破折号 "—"），说话人/叙事视角无归错（第三人称叙事，非对话）。关键词 beef broth / storage / pretense 均在引语内。四子项齐备，无截短。
- **原句 2**（text 第 61 行）：逐字一致（md 用直引号 "，text 用弯引号 ""，属允许差异）。关键词 sank down in the gravel / curse / prophesy 均在引语内。无截短，四子项齐备。
- **原句 3**（text 第 74 行）：逐字一致。关键词 smiled with zeal / cheeks collapsed / mad expression 均在引语内。无截短，四子项齐备。
- **原句 4**（text 第 77 行）：逐字一致（含 "silhouettist's" 撇号，md 直 '，text 弯 '）。关键词 silhouettist's scissors / snipping away / blackest hatred 均在引语内。无截短，四子项齐备。

说明：本章 4 个引语块全部为第三人称叙事（Henrie 贴身视角），不涉及对话说话人，故不存在"说话人反转"类风险；无跨章章号标注（本章标题/场景一致，提取件为 ch50_chapter_11.txt）。引语截短检查通过——每段引语均为 text 中的完整连续句段，未在中途省略实词或断句拼接。

ch50 完成：4 块，缺陷 0，待复核 0
---

# d 步二审 · ch51

## 结论：共 4 块，通过 4，缺陷 0，待复核 0

## 缺陷清单（无则写"无"）

无。

## 逐块核验记录

### 原句 1（引语行：md 第 21 行；text 第 14 行）
- **引语逐字**：与 text 第 14 段逐字一致（`Henrie sat next to Jane's bed, holding her cold hand, and thinking of her baby brother, Harry. ... while everyone who loved him went about their business unknowingly in the house, not listening.`）。✓
- **说话人正确**：text 明确以 Henrie 为主语（`Henrie sat next to Jane's bed`），前后窗口均为 Henrie 的回忆叙事。md 中文理解归因为 Henrie 回忆幼弟哈利，正确。✓
- **引语↔分析对应**：四子项（中文理解 / 关键词 / 为什么这样写 / 读者视角提示）均围绕"哈利溺亡的强迫性回忆 + 自我惩罚 + 无人在听"，与引语一致，无截短（引语覆盖 text 该段完整句组）。✓
- **关键词回查**：`penance`（text 14 "as penance for letting it happen"）、`headfirst`（"he ran headfirst"）、`not listening`（"in the house, not listening"）均在引语内命中。✓
- **结构**：引语行 + 四子项齐全。✓

### 原句 2（引语行：md 第 33 行；text 第 17 行）
- **引语逐字**：与 text 第 17 段逐字一致。✓
- **说话人正确**：该段承接原句 1 的 Henrie 内心叙述（`Now it seemed like a blessing if the alternative were this.`），speaker 为 Henrie。md 归因一致。✓
- **引语↔分析对应**：中文理解、关键词、为什么这样写、读者视角提示四子项均围绕"Jane 的死亡是数周溺水、众人看见却无助、Jeannette 死于列日"，与引语一致。✓
- **关键词回查**：`weeks-long drowning`、`consumption`、`aware and unable to help` 均在引语内。✓
- **结构**：齐全。✓

### 原句 3（引语行：md 第 45 行；text 第 26 行）
- **引语逐字**：与 text 第 26 段逐字一致。✓
- **说话人正确**：text 第 23 行明示 `Emma Woodhouse's voice claiming I am never ill echoed in her ears`，第 26 段正是这段在 Henrie 脑中回响的 Emma 内心独白。md 归因"Henrie 耳中 Emma 的内心独白"，正确（不是 Henrie 自己说的）。✓
- **引语↔分析对应**：四子项围绕 Emma 的第一人称傲慢独白、Box Hill 羞辱、`I am never ill` 回环，与引语一致。✓
- **关键词回查**：`ridicule`（"I can ridicule my old neighbor"）、`risible`（"that she is risible"）、`glow`（"I will glow in the attention"）均在引语内。✓
- **结构**：齐全。✓

### 原句 4（引语行：md 第 57 行；text 第 38 行）
- **引语逐字**：与 text 第 38 段逐字一致（含 `"Jane, my darling girl, come back to us. ..."` 到 `"Goodbye, my lovely baby."` 及结尾 `She roared into Jane's cold neck.`）。✓
- **说话人正确**：text 上下文主语为 Henrie（`Henrie squeezed her eyes shut`），所有引号内话语均为 Henrie 对将死女儿说的话。md 归因正确。✓
- **引语↔分析对应**：四子项围绕按分钟计数的告别、`There were no more words` 的失语收束、面具落下，与引语一致。✓
- **关键词回查**：`stopped breathing`（"stopped breathing for one minute"）、`subtract away`（"subtract away what your being in it added"）、`letting her mask fall`（"letting her mask fall for the first time in three months"）均在引语内。✓
- **结构**：齐全。✓

## 备注
- 章号：md frontmatter 写 `Chapter 1（Part Five）`，text 文件首行标题同为 `Chapter 1`，且正文叙事（Epiphany 婚礼次日、Jane 停息、Mr. Elton 到访）与"Part Five 开篇"一致，章号无跨章错标。✓
- 引语均未被截短：每块引语都完整覆盖其支撑分析所需的句子。✓
- 词汇表例句（penance / consumption / ridicule / Epiphany / defleshed / ticking / shallower / handkerchiefs / squeezed / suffocating）经抽查均能在 text 中逐字找到对应原句（text 14、17、20、23、26、29、35、38），无幻觉。✓

## 待人工复核

无。

ch51 完成：4 块，缺陷 0，待复核 0
---

# d 步二审 · ch52

## 结论：共 4 块，通过 4，缺陷 0，待复核 0

### 核对明细

- **原句 1**：引语逐字命中 text/ch52 第 13 段（`Mr. E. has been run off his feet...fresh dirt near Harry and her father.`）。说话人正确——原文为 `Henrie heard his wife say`，即 Mrs. Elton（Mr. E. 之妻），与中文理解归因一致。关键词 `run off his feet` / `chaotic haze` / `fresh dirt` 均在本块引语中原形命中。四子项（中文理解/关键词/为什么这样写/读者视角提示）均围绕同一引语块，无截短，引语完整含 `All dead but her` 等关键句。✅
- **原句 2**：引语逐字命中第 16 段（`There had been one funeral service...my obligations here.`）。说话人正确——`Mrs. Elton could be heard saying`。关键词 `practical` / `dreary` / `obligations` 原形命中。四子项一致。✅
- **原句 3**：引语逐字命中第 34 段（`Now standing in the bare winter churchyard...safe and true.`）。说话人正确——Henrie 内心独白/第三人称贴身叙述。关键词 `arthritic` / `the Beast` / `hatred` 命中（`hatred` 出现在句中 `hatred for her was the only emotion...`）。四子项一致。✅
- **原句 4**：引语逐字命中第 37 段（`If she had her old under-her-apron hammer...like strawberries.`）。说话人正确——Henrie 的暴力幻想。关键词 `rainbow of force` / `splintering` / `like strawberries` 命中。四子项一致。✅

## 缺陷清单

无

## 待人工复核

无

## 备注

- 本章引语块均为单段连续原文引用，起止与原段落对齐，未发现引语截短、说话人反转或跨章章号错标。
- 引语行与中文理解行在同一 md 中相邻配对，四子项齐全，无孤儿/重复块。
- 词汇表中例句（counterpane/commended/huswife/sward/burbling/sexton/shovelfuls/arthritic/economizing/gurgle/clunk）经抽查均能在 text/ch52 对应句中找到出处（如 `counterpane` 见第 19 段，`sexton`/`shovelfuls` 见第 28/31 段，`gurgle`/`clunk` 见第 40 段），未发现幻觉例句。

ch52 完成：4 块，缺陷 0，待复核 0
---

# d 步二审 · ch53

## 结论：共 4 块，通过 4，缺陷 0，待复核 0

## 缺陷清单（无则写"无"）

无。

## 逐块核验明细

### 原句 1
- **引语逐字**：命中（text/ch53 line 13）。"She was sitting in her mother's old chair, well away from the window. She had been crying recently, but it seemed like right now she wasn't. Her hand, alien, slowly lifted to her cheeks and patted around like an animal sniffing through the leaves for water. Damp, not wet." 完全一致。
- **说话人**：第三人称贴身跟随 Henrie 的叙述，主语 Henrie，与中文理解"Henrie 坐在亡母的旧椅子里"一致。正确。
- **引语↔分析对应**：四子项（中文理解/关键词/为什么这样写/读者视角）均围绕该开篇解离段，无截短。
- **关键词**：alien ✓、patted ✓、damp ✓（均在引语内）。
- **结构**：引语行 + 四子项齐全。

### 原句 2
- **引语逐字**：命中（text/ch53 line 32）。"It was, without a doubt, Dorothea Goddard who saved Henrie from a lonely Twythorpian death in those cramped rooms that she could no longer afford. The first thing she did was insist that the school was in dire need of just such a piano and, if Henrie could bear to part with it, she would pay a handsome price. Henrie broke her usual silence to say that if she could, she would throw the instrument out the window." 完全一致。引语截到 "out the window." 为完整句，未截掉支撑分析的必要内容。
- **说话人**：作者插叙，主语 Dorothea Goddard（Mrs. Goddard 本名），与中文理解"是 Dorothea Goddard 把 Henrie 救了出来"一致。正确。
- **引语↔分析对应**：四子项均围绕"买钢琴救援/体面慈善"同一主题，无错配。
- **关键词**：saved ✓、piano ✓、silence ✓。
- **结构**：齐全。

### 原句 3
- **引语逐字**：命中（text/ch53 line 35）。"Henrie, after a career of keeping herself to the fore in people's thoughts with the relentless engine of appreciation, had removed herself from the public eye. If she were to be seen, she would be in danger of revealing herself as that most frightening of things—an ungrateful, unruly, angry woman." 完全一致（含破折号）。
- **说话人**：叙述者写 Henrie，与中文理解"Henrie 半辈子靠着那台感激发动机…如今她把自己从公众视野里彻底移除了"一致。正确。
- **引语↔分析对应**：四子项均讲"感激发动机/退出公共视野/愤怒无处安放"，一致。
- **关键词**：relentless engine of appreciation ✓、removed herself ✓、ungrateful ✓。
- **结构**：齐全。

### 原句 4
- **引语逐字**：命中（text/ch53 line 38）。"There were rumors that people saw her after dark, gathering things in the lanes around Highbury. And there had been a spate of henhouses being raided, but nobody spoke of it, and when they did, quietly, in pairs, everyone agreed that no single person could have use of so many chickens. It must be the Travellers, people said, and chased them out of their spot in the woods before their season ended." 完全一致。
- **说话人**：叙述者写 Highbury 关于 Henrie 的夜间传闻与集体指控，与中文理解"有传闻说人们天黑后看见她在 Highbury 附近…众口一词一定是'游民'干的"一致。正确。
- **引语↔分析对应**：四子项均围绕"夜间捡食/鸡舍被撬/游民被赶"同一段，无截短。
- **关键词**：rumors ✓、henhouses being raided ✓、Travellers ✓。
- **结构**：齐全。

## 备注（非引语缺陷）
- md 第 2 行 frontmatter 的 title 写为"Miss Bates 精读 52 · Chapter 3"，但本文件为 ch53 章节；此为元数据编号，不影响引语核验，如需可另处统一。
- 本块关键词 "silence" 引文（md 第 93 行）与"原句 2"引语一致，未发现孤儿或重复块。

## 待人工复核

无。

ch53 完成：4 块，缺陷 0，待复核 0
---

# d 步二审 · ch54

## 结论：共 3 块，通过 3，缺陷 0，待复核 0

逐块核对结果（逐字比对 text/ch54_chapter_4.txt）：

### 块 1（原句 1）
- **引语逐字**：与 text 第 13 段逐字一致 ✓（"Mrs. Wren's" 弯引号差异，允许）
- **说话人**：叙述者（旁白），text 上下文为章节开篇叙事，非人物对话；中文理解归因为叙述，正确 ✓
- **引语↔分析对应**：中文理解讲"意外催化剂是一道菜"，与本句含义吻合；四子项（中文理解/关键词/为什么这样写/读者视角提示）齐备，均在讲同一句，无截短 ✓
- **关键词**：hankering、catalyst、re-entry 均在本句中找到 ✓

### 块 2（原句 2）
- **引语逐字**：与 text 第 16 段逐字一致 ✓
- **说话人**：叙述者（旁白），中文理解归因为叙述，正确 ✓
- **引语↔分析对应**：中文理解讲"味道凭空回到舌尖、黄油酥皮抵上颚"，与本句吻合；四子项齐备，无截短 ✓
- **关键词**：out of the blue、taste、buttery crust 均在本句中找到 ✓

### 块 3（原句 3）
- **引语逐字**：与 text 第 28 段逐字一致 ✓
- **说话人**：叙述者（旁白，紧接 Mrs. Goddard 长段对话之后的叙述），中文理解正确归因为 Henrie 的心理反应，非误归给 Mrs. Goddard ✓
- **引语↔分析对应**：中文理解讲"Emma 的不舒服更让 Henrie 乐意、想到 Emma 受苦就流口水"，与本句吻合；四子项齐备，无截短 ✓
- **关键词**：reluctantly、concomitant、mouth watered 均在本句中找到 ✓

结构检查：3 个引语块均为「引语行 + 中文理解/关键词/为什么这样写/读者视角提示」四子项齐全，无孤儿块、无重复块。

## 缺陷清单
无

## 待人工复核
无

ch54 完成：3 块，缺陷 0，待复核 0
---

# d 步二审 · ch55

## 结论：共 3 块，通过 3，缺陷 0，待复核 0

核对文件：
- 精读 md：`notes/books/novels/miss-bates-by-catherine-cliff/ch55 emmas discontent.md`
- 原文提取件：`notes/books/novels/miss-bates-by-catherine-cliff/text/ch55_chapter_5.txt`

---

### 逐块核对明细

#### 原句 1
- **引语行**：`> **原句 1:** "The smell of Emma’s discontent was like a fox trail to a beagle, and Henrie could not resist baying down the road after it."`
- **text 命中**：第 13 行，逐字一致（弯引号差异不计）。
- **说话人核对**：该句为无归属的叙述句（全书视角叙述者），中文理解未将其归给任何角色，只作为动机交代——归因正确。
- **中文理解↔引语**：气味/狐狸踪迹/猎犬/吠叫循味——四子项与引语句意完全对应，未超范围，无截短。
- **关键词回查**：discontent ✓ / fox trail ✓ / baying ✓（均在引语原文中出现，无改写）。
- **结构**：引语行 + 中文理解 + 关键词 + 为什么这样写 + 读者视角提示，四子项齐全，无孤儿/重复块。

#### 原句 2
- **引语行**：`> **原句 2:** "Emma Knightley was, just as Mrs. Goddard had said, physiognomically altered for the worse. For the worst, Henrie might even say. Henrie had observed mothers who grew more beautiful with their expectation, glossy as hazelnuts, as well as those who lost their looks, scaly and gray. Mrs. Wren used to say that loss of looks meant a baby girl because the infant was stealing her mother’s beauty. If so, Emma was due for girl triplets."`
- **text 命中**：第 31 行，逐字一致（含 `mother’s` 弯撇号与原文一致）。
- **说话人核对**：叙述句（亨莉视角观察），未归给具体角色。中文理解提到「戈达德太太说的」与「雷恩太太过去常说」均为引语内人物转述，text 第 31 行确认 `just as Mrs. Goddard had said` 与 `Mrs. Wren used to say` 存在，归因正确。
- **中文理解↔引语**：面相变差 / 榛子油亮 vs 灰败掉相两极对照 / 三胞胎女儿——四子项均对应引语内容，无截短。
- **关键词回查**：physiognomically altered ✓ / glossy as hazelnuts ✓ / girl triplets ✓。
- **结构**：四子项齐全。

#### 原句 3
- **引语行**：`> **原句 3:** "But, after fifteen minutes alone with Emma, she realized that Mrs. Weston was right. Emma was not just uncomfortable and anxious. She was furious with regret, simmering with grievance—so unlike her lifelong complacence. She could not accept that this was real, she wanted people to blame. Many of the same emotions Henrie herself had over the last year. Emma Knightley was in mourning for Emma Woodhouse."`
- **text 命中**：第 34 行，逐字一致。
- **说话人核对**：叙述句（亨莉视角），未归给角色，归因正确。
- **中文理解↔引语**：十五分钟 / 韦斯顿太太说得对 / 悔恨发狂 / 怨气咕嘟 / 与自满判若两人 / 不能接受 / 找人怪罪 / 这些情绪自己也有 / 为伍德豪斯小姐服丧——全部对应，无截短。
- **关键词回查**：furious with regret ✓ / simmering with grievance ✓ / mourning for Emma Woodhouse ✓。
- **结构**：四子项齐全。

**附带核查**：原句 3 的「读者视角提示」引述「韦斯顿太太那句『仿佛真正的爱玛已经死了』」——text 第 25 行确认存在 `"She is just utterly transformed, it's as if the real Emma has died."`，且该句在上下文中由亨莉归给 Emma 的家庭教师即韦斯顿太太（第 22 行 `Emma's old governess... continue`）所说，归因正确。

---

## 缺陷清单（无）

本章 3 个引语块逐字命中、说话人归因正确、引语与分析完全对应、关键词齐全、结构完整，无截短、无跨章错标、无说话人反转问题。

## 待人工复核

无。
---

# d 步二审 · ch56

## 结论：共 4 块，通过 4，缺陷 0，待复核 0

## 缺陷清单

无

## 逐块核对记录

### 原句 1
- **引语逐字**：与 `text/ch56_chapter_6.txt` 第 34 行完全一致 ✓（`"Memories of who Emma had always been flitted through Henrie's mind as she walked the long road to Highbury that August. Now that the Beast was leading a life she had never wanted, or had wanted for only a jealous and capricious moment, Henrie had made a point of visiting her often to see what she could see."`）
- **说话人**：叙述（第三人称贴身跟随亨莉），亨莉走在长路上的回忆与动机。中文理解归因为「亨莉的观察与盘算」，正确 ✓
- **引语↔分析对应**：四子项均围绕"野兽"标签、"to see what she could see"的观察动机展开，对应一致；引语完整未截短 ✓
- **关键词回查**：the Beast ✓ / jealous and capricious moment ✓ / to see what she could see ✓

### 原句 2
- **引语逐字**：与第 73 行完全一致 ✓（`"These moments of alliance didn't last long. Emma was like a cat, suddenly deciding it did not actually like the strokes that had formerly brought a purr."`）
- **说话人**：叙述（亨莉视角），描述爱玛。中文理解归因为对爱玛的描写，正确 ✓
- **引语↔分析对应**：猫的善变比喻、翻脸节律、purr 均对应；引语完整未截短 ✓
- **关键词回查**：moments of alliance ✓ / like a cat ✓ / purr ✓

### 原句 3
- **引语逐字**：与第 76 行完全一致 ✓（`"Henrie almost pitied her. Here was a woman who had been doing that unimaginable thing, living her happiest life with all the choices she could ever want, but because of a moment of envy, a flicker in the courage of her convictions, she had given it all up to be responsible for people (a husband, a child) she would never love as much as she loved herself."`）
- **说话人**：叙述（亨莉视角），"Henrie almost pitied her" 明确指出。中文理解归因为亨莉对爱玛的心理分析，正确 ✓
- **引语↔分析对应**："嫉妒的一瞬"=moment of envy，"爱自己胜过一切"=never love as much as she loved herself，"几乎"、"（丈夫、孩子）"均在引语内；引语完整未截短 ✓
- **关键词回查**：moment of envy ✓ / flicker in the courage of her convictions ✓ / as much as she loved herself ✓

### 原句 4
- **引语逐字**：与第 88 行完全一致 ✓（`"And Emma dared to bring up the subject of his child to Henrie—Henrie knew it was the scrub, scrub writ large. She would use the shears on both of them. A shiver of rage ran through her. She smiled up at the servant as he held the door for her."`）
- **说话人**：叙述（亨莉视角），Emma 提起孩子 / Henrie 要用剪刀 / Henrie 对仆人微笑。中文理解归因正确 ✓
- **引语↔分析对应**：scrub writ large、大剪刀（shears）、杀意的战栗（a shiver of rage）、对仆人的微笑，四者均在引语内；引语完整未截短 ✓
- **关键词回查**：the scrub ✓ / scrub writ large ✓ / the shears ✓ / a shiver of rage ✓
- **备注**：读者视角提示中引用的"九月的天气真够冷的，是不是？"出自原文第 91 行（`"Thank you, Thomas. It is a chilly day for September, is it not?"`），属分析层面对章末的补充引用，未混入引语块本身，不构成缺陷。

## 防幻觉检查

- 4 个引语行均在 md 中与对应中文理解行相邻，且均在 `text/ch56_chapter_6.txt` 中逐字命中。
- 无跨章错标（引语块未引用章号，内部"原句 N"编号连续 1-4）。
- 无说话人反转：全章引语均为亨莉视角叙述，中文理解归因一致。
- 无引语截短：每条引语完整覆盖其分析所需内容。
- 词汇表例句亦全部核对通过（elephantine/writ large/protégée/myriad/gazette/purr/incredulity/simpleton/shiver/cape 共 11 条，全部与原文逐字一致）。

## 待人工复核

无

ch56 完成：4 块，缺陷 0，待复核 0
---

# d 步二审 · ch57

**章节**：Chapter 7（Part Five: 1813–1819）· "tricky albert"
**精读 md**：`notes/books/novels/miss-bates-by-catherine-cliff/ch57 tricky albert.md`
**原文提取件**：`notes/books/novels/miss-bates-by-catherine-cliff/text/ch57_chapter_7.txt`

## 结论：共 4 块，通过 4，缺陷 0，待复核 1

逐块核对结果（引语逐字 / 说话人 / 引语↔分析对应 / 关键词回查 / 结构）如下。

---

### 原句 1 ✅
- **逐字**：`But there was still enough of Emma's traditional good fortune remaining: both she and the baby made it through alive. A little boy, Albert. He was small and he had a little lift at the center of his upper lip, nothing too terrible, the palate beyond was fine. But he had trouble eating, and Henrie knew that Emma found the irregularity embarrassing. She was not accustomed to imperfection.` 与 text 第 16 行完全一致。✅
- **说话人**：原文为叙事段（非直接引语）。中文理解把 "Henrie knew that Emma found the irregularity embarrassing" 归给 Henrie 的所知，与原文一致。✅
- **引语↔分析**：四子项齐全；"为什么这样写"收尾引用的 "She was not accustomed to imperfection." 确在引语末尾，未截短。✅
- **关键词**：good fortune / irregularity / imperfection 均在本块引语中出现。✅

### 原句 2 ✅
- **逐字**：`But it was true that Albert had been a tricky infant, even for Dame Webb, who had so much experience—his cleft lip did make it difficult for him to catch hold of the breast, and on top of that he was colicky. His mighty squawks of displeasure were known in the neighborhood. Henrie had a way with him, though, and her arrival in the late afternoon, his most querulous time, became very welcome.` 与 text 第 29 行完全一致（破折号形式一致）。✅
- **说话人**：叙事段。中文理解未把叙述归为某角色直接说话，符合原文。✅
- **引语↔分析**：四子项齐全；分析提到的转折词 "though" 与 "became very welcome" 均在引语内，未截短。✅
- **关键词**：tricky / squawks / querulous 均在本块引语中出现。✅

### 原句 3 ✅
- **逐字**：`Week after week, month after month, she made her way down the lane, often arriving wet from the rain, and even, eventually, snow. "The wet doesn't bother me, I have my pattens and my nice warm shawl," she said, and she meant it.` 与 text 第 35 行完全一致。✅
- **说话人**（重点核查，防说话人反转）：整段主语为 Henrie（"she made her way down the lane…"），前一段 line 32 "It was her only hot meal, although she would have gone anyway" 及后一段 line 38 为 Dame Webb 开口，故 line 35 的 "she said" 指 Henrie。中文理解「"她说这话的时候，是真心这么想的"」归因 Henrie，正确。✅
- **引语↔分析**：四子项齐全；"为什么这样写"引用的 "and she meant it" 与"木套鞋、一条披巾"均在引语内，未截短。✅
- **关键词**：week after week / pattens / meant it 均在本块引语中出现。✅

### 原句 4 ✅
- **逐字**：`"So soon," said Henrie softly and gave a sad "bawk, bawk" to Albert, who understood the game and matched her tone with an answering mournful cluck.` 与 text 第 54 行完全一致。✅
- **说话人**：原文明确 "said Henrie softly"，"So soon" 为 Henrie 所言，中文理解归因 Henrie，正确。✅
- **引语↔分析**：四子项齐全；分析提到的 "matched her tone" 确在引语内，未截短。✅
- **关键词**：so soon / mournful / answering 均在本块引语中出现。✅

---

### 结构检查
- 4 个引语块，每块均含「引语行 + 中文理解 + 关键词 + 为什么这样写 + 读者视角提示」四子项齐全；无孤儿块、无重复块。✅
- 引语行与中文理解在 md 中相邻（同块），未与无关分析行拼装。✅

---

## 缺陷清单

无。

## 待人工复核

1. **章号/编号一致性（疑似，超出引语核对范围）**：文件名 `ch57 tricky albert.md` 与 frontmatter `title: Miss Bates 精读 56 · Chapter 7` 存在编号差异（ch57 vs 精读 56）。原文件首为 `Chapter 7`，精读正文标题亦为 `Chapter 7（Part Five）`，三者对"本书第 7 章"一致；差异只在精读库内部编号（56/57）。疑为命名口径不同（"ch57" 可能指精读第 57 篇，而非 Chapter 57），建议人工确认该文件在精读库中的正式编号，以排除跨章章号错标类风险。**非引语缺陷**。

---

ch57 完成：4 块，缺陷 0，待复核 1
---

# d 步二审 · ch58

## 结论：共 4 块，通过 4，缺陷 0，待复核 0

## 缺陷清单
无

## 待人工复核
无

## 逐块核对记录

### 原句 1
- **引语逐字**：md 引语行与 text/ch58 第 13 行逐字一致（实词无改写；开引号为补回的弯引号，属允许差异）。
- **说话人**：text 窗口内紧接 `said Mr. Woodhouse`，中文理解归因「Woodhouse 先生」正确。
- **引语↔分析**：四子项（中文理解/关键词/为什么这样写/读者视角）均围绕同一段话：反差句「不高兴」+ 三个衰老细节 + 引语内「老友最好」与「想念家里人都在的舒服」。无截短——引语覆盖到句尾 `as if on the verge of tears.`。
- **关键词回查**：grasshopper ✓、wavered ✓、the comfort of family ✓（原文 "I do miss the comfort of family."）。
- **结构**：引语行 + 四子项齐全，无孤儿/重复。

### 原句 2
- **引语逐字**：与 text/ch58 第 28 行逐字一致（叙述段，非对话）。
- **说话人**：本段为 Henrie 视角的叙述，无对话归因问题；中文理解亦作叙述描述，归因正确。
- **引语↔分析**：四子项均针对同一段（Emma 的 relief/cabbage、Knightley 反复摩挲手套）。无截短——引语覆盖整段至 `hatless.`。
- **关键词回查**：relief ✓、cabbage ✓、gloves ✓。
- **结构**：齐全。

### 原句 3
- **引语逐字**：与 text/ch58 第 75 行逐字一致（叙述句）。
- **说话人**：叙述，无对话归因；中文理解为 Emma 的判词，正确。
- **引语↔分析**：四子项均围绕「Emma 不亲孩子但方法粘不上」这一句；引语未截短（完整格言句）。
- **关键词回查**：attach herself ✓、inadhesive methods ✓。
- **结构**：齐全。

### 原句 4
- **引语逐字**：与 text/ch58 第 143 行逐字一致（叙述段）。
- **说话人**：叙述（Henrie 夜里回忆），无对话归因；中文理解归 Henrie 的回忆，正确。
- **引语↔分析**：四子项均针对「看魔术」比喻 + confusion and misery。无截短——引语覆盖整段至 `confusion and misery.`。
- **关键词回查**：magic trick ✓、sleight of hand ✓、misery ✓。
- **结构**：齐全。

## 说明
- 全章仅 4 个引语块，均无「逐字命中但归错说话人」、无跨章章号错标、无引语截短问题。
- 逐字比对中未发现实词改写；仅 Block 1 开引号由 text 的分页起点补回弯引号，属允许的标点差异。
- 关键词均在本块引语内命中（含词形变化）。

ch58 完成：4 块，缺陷 0，待复核 0
---

# d 步二审 · ch59

## 结论：共 4 块，通过 4，缺陷 0，待复核 0

核对依据：精读 md `ch59 not to be burnt like rubbish.md` × 原文 `text/ch59_chapter_9.txt`（逐字比对 + 上下文 ~200 字符窗口判说话人）。

## 各块核对明细

### 原句 1（Mrs. Elton）
- 引语逐字：md 引语行 vs text 第 16 段，英文逐字一致（含 `unenthusiastically`、`breezed through a door opened by Thomas`、`quart of cream that had gone off`）。✓
- 说话人：text 第 13–16 段窗口显示马车到 Hartfield、Mrs. Elton 下车、`“Miss Bates,” she said unenthusiastically over her shoulder…`，说话人确为 Mrs. Elton；中文理解归因 Mrs. Elton ✓。
- 引语↔分析：四子项（中文理解/关键词/为什么这样写/读者视角提示）都在讲 Mrs. Elton 冷淡招呼 + 变质奶油；引语未截短（含后续叙述句，与 md 引语行一致）。✓
- 关键词：unenthusiastically / condolence / gone off 均在引语内命中。✓
- 结构：完整。✓

### 原句 2（Emma 被娇养 / Mrs. Withers 护理）
- 引语逐字：text 第 41 段完整一致（coddling、health potions、peeled pig、括号内蜂蜜威士忌茶与"不许读书"均在）。✓
- 说话人：本段为叙述者转述/叙述，中文理解未归具体人物，归"Emma 被众星捧月"语境正确。✓
- 引语↔分析：四子项一致讲"护理仪式 + 括号拆穿 + peeled pig 戳破"；引语未截短。✓
- 关键词：coddling / health potions / peeled pig 均在引语内命中。✓
- 结构：完整。✓

### 原句 3（Mr. Woodhouse）
- 引语逐字：text 第 63 段完整一致（`You are kindness itself, Miss Bates…`、`he has the…" he wafted an old speckled hand toward his mouth`、`Won't you sit down with me for a moment?`）。✓
- 说话人：text 第 60–63 段窗口为 "Her routine always ended with this fireside chat between the two of them"，随后 Henrie 说"Mr. Woodhouse, you must be so proud of Albert"，Mr. Woodhouse 回应；本引语确为 Mr. Woodhouse 所说；中文理解归因正确 ✓。
- 引语↔分析：四子项一致讲"半句吞回的'那个…' + 挥手 + Henrie willed herself 维持表情 + 好安静"；引语未截短。✓
- 关键词：willed herself / wafted / speckled hand 均在引语内命中。✓
- 结构：完整。✓

### 原句 4（Henrie 埋葬女婴）
- 引语逐字：text 第 215 段完整一致（`She was not to be burnt like rubbish`、`selected a spade`、`her own shawl—her only shawl, actually`、`another underground body`、`little bundle of almost-baby`）。✓
- 说话人：叙述句，中文理解归 Henrie 主体行为正确；上下文（第 212 段女婴、第 218 段 tall enough to go into the barn）吻合。✓
- 引语↔分析：四子项一致讲"短促动作句 + 断言式开头 + 唯一披肩 + 床单丢上柴堆"；引语未截短。✓
- 关键词：rubbish / spade / her only shawl 均在引语内命中。✓
- 结构：完整。✓

## 「三岁」年龄数字核查
- md 导航（第 12 行）称"Henrie 带着三岁的 Albert"。
- text 第 13 段原文支撑：`Henrie and Albert (whose third birthday had been the week before; they had had a marzipan cake, which both had loved)` —— 刚过三岁生日，年龄 3 岁有原文支撑。**数字断言成立**。

## 缺陷清单
无

## 待人工复核
无

ch59 完成：4 块，缺陷 0，待复核 0
---

# d 步二审 · ch60

## 结论：共 4 块，通过 3，缺陷 1，待复核 0

## 引语↔分析逐对核对记录

### 原句 1（md L21 ↔ text L13）
- 引语逐字：逐句与 text 第 13 行比对，全部命中（含 "not coming out" 弯引号、结尾 "She was good at things!"）。
- 说话人：该段为叙述/自由间接引语，中文理解归因「Henrie 知道」正确（text 中 "Henrie knew"）。无说话人反转。
- 引语↔分析：四子项（中文理解/关键词/为什么这样写/读者视角）均指向同一段引语，无截短。
- 关键词：listless、galvanized、somebody was not her 均在引语内命中。
- 结构：引语行 + 四子项齐全。

### 原句 2（md L33 ↔ text L61）
- 引语逐字：与 text 第 61 行逐句命中，结尾 "Brush with death. Changeling." 完整。
- 说话人：Emma 的话语与 Albert 的动作/反应分属正确，中文理解归因无误。
- 引语↔分析：四子项一致，无截短。
- 关键词：shrunk、brush with death、changeling 均在引语内命中。
- 结构：齐全。

### 原句 3（md L45 ↔ text L70）
- 引语逐字：与 text 第 70 行逐句命中，含 Henrie 引语 "That is my fault alone."。
- 说话人：叙述段归 Henrie 本人，引语归 Henrie，中文理解正确。
- 引语↔分析：四子项一致，无截短。
- 关键词：incandescent、schooled her features、my fault alone 均在引语内命中。
- 结构：齐全。

### 原句 4（md L57 ↔ text L73）
- 引语逐字：与 text 第 73 行逐句命中，结尾 "Really, Emma Knightley was a cruel woman." 完整。
- 说话人：叙述者（Henrie 视角）判断句，中文理解归因正确。
- 引语↔分析：四子项一致，无截短。
- 关键词：dropped the flowers、ruined something beautiful、cruel 均在引语内命中。
- 结构：齐全。

## 缺陷清单

- 类型：数字断言无支撑（年龄）
- 引语行原文：原句 2 引语（md L33）——引语本身不涉年龄
- 中文理解/分析原文：「一个三岁孩子捧着花怯生生靠近病床，换来的却是尖叫与"换生灵"这种民俗诅咒式的定性」（md L39，原句 2 的"为什么这样写"）
- 问题说明：全章 text/ch60_chapter_10.txt 通篇未出现 Albert 的年龄信息（未出现 three years old / three-year-old / 年龄数字），Albert 仅被描述为捧着花的男孩、被抱起/牵着下楼。因此"三岁"这一年龄断言在原文本中无任何支撑，属数字断言无支撑。
- 建议修法：删去"三岁"或改为不涉具体年龄的表述（如"一个孩子"、"捧着花的男孩"），避免虚构原文未提供的年龄信息。

## 待人工复核

无。

ch60 完成：4 块，缺陷 1，待复核 0
---

# d 步二审 · ch61

## 结论：共 4 块，通过 4，缺陷 0，待复核 0

## 逐块核对记录

### 原句 1
- **引语行**：`"Curious. In both her acts of justice, a chestnut had proved her weapon of choice. That was funny."`
- **源文核对**：text/ch61_chapter_11.txt 第 13 行逐字命中（含引号位置），实词无改写，仅两侧引号由弯/直差异（源文无引号，为叙述句）。
- **说话人窗口**（~200 字符）：紧邻上下文为叙述句，无对话归属，是 Henrie 视角的旁白开头。中文理解归因为"开篇短短三句收束上一章事件"，即叙事者/Henrie 内心，正确。
- **引语↔分析对应**：四子项（中文理解／关键词／为什么这样写／读者视角提示）均围绕"两次 acts of justice 里栗子作武器、That was funny"这一句；引语完整，无截短。
- **关键词回查**：acts of justice / chestnut / weapon of choice 均在引语中原样出现。✓

### 原句 2
- **引语行**：`"He sat on the cold corridor floor … she wasn’t at all sure if Emma was even aware of his presence."`（原文：He sat on the cold corridor floor with all his feathers laid out in order of size. … But standing in the threshold of the room, she wasn’t at all sure if Emma was even aware of his presence.）
- **源文核对**：text/ch61_chapter_11.txt 第 16 行逐字命中，实词一致，仅结尾双引号（源文无引号，为叙述句）。
- **说话人窗口**：该段为叙述段落，主语 He（Albert）／Henrie，叙述者视角。中文理解归因"Albert 坐在…Henrie 知道他是在盼母亲…她根本不敢肯定 Emma 是否知道儿子在那里"，正确。
- **引语↔分析对应**：四子项均对应同一句；"cold corridor floor""threshold"被分析引用；引语完整未截短。
- **关键词回查**：feathers / hoping / threshold 均在引语中（hoping 出现于 hoping his mother would look out；threshold 出现于 standing in the threshold）。✓

### 原句 3
- **引语行**：`"“No one is sending me, I am not a parcel! Don’t you worry.” She told him one of her rare lies: “And your mother loves you, of course she does, exactly as you are. Mamas always love their babies, and you are her baby! And you look so much like your grandpapa.”"`
- **源文核对**：text/ch61_chapter_11.txt 第 124 行逐字命中（含内层弯引号），实词一致。
- **说话人窗口**：紧邻前文第 121 行 Albert 说"please don’t box her ears because then they might send you"；本句开头"No one is sending me, I am not a parcel!"正是 Henrie 回应 Albert；"She told him one of her rare lies"明确归 Henrie。中文理解归因 Henrie 对 Albert 撒的谎，正确。
- **引语↔分析对应**：四子项均围绕"parcel 比喻＋exactly as you are＋少见谎"；引语完整（含前后两段直接引语与中间叙述），未截短。
- **关键词回查**：rare lies（She told him one of her rare lies）/ exactly as you are / parcel 均在引语中。✓

### 原句 4
- **引语行**：`"Sometimes, when Henrie couldn’t sleep, she imagined Albert-of-the-future, … Butterflyicas batesiensis. And maybe he would point her out … Henrie would curtsy, very low. Emma Knightley was not at this ceremony."`（原文：…accepting a knighthood… telling the king, You know, actually, it was a woman who made my life as a man of science possible, the wonderful woman who raised me. Henrie Bates. … Butterflyicas batesiensis. And maybe he would point her out … Henrie would curtsy, very low. Emma Knightley was not at this ceremony.）
- **源文核对**：text/ch61_chapter_11.txt 第 179 行逐字命中，实词一致，仅末双引号（源文无引号，为叙述句）。
- **说话人窗口**：该段为 Henrie 睡不着的想象（叙述段），主语 Henrie；中文理解归因"Henrie 想象未来的 Albert"，正确。
- **引语↔分析对应**：四子项均围绕这场未来典礼想象与末句"Emma Knightley was not at this ceremony."；引语完整未截短（含拉丁文笑话处）。
- **关键词回查**：imagined / the wonderful woman who raised me / was not at this ceremony 均在引语中。✓

## 缺陷清单（无）

无。

## 待人工复核

无。四块引语逐字核对均命中源文、说话人归因与中文理解一致、引语未截短、四子项齐全、关键词均在引语中。

## 备注（供参考，非缺陷）

- 引语行统一采用弯引号包裹整段；源文均为无引号的叙述句，故"原句 N"行的外层双引号为精读稿统一格式，非文本改写，实词逐字一致。
- 原句 3 内层含弯引号与源文第 124 行完全一致。

ch61 完成：4 块，缺陷 0，待复核 0
---

# d 步二审 · ch62

## 结论：共 4 块，通过 4，缺陷 0，待复核 0

## 缺陷清单
无

## 待人工复核
无

---

## 逐块核对明细

### 原句 1
- **引语逐字**：text/ch62_chapter_12.txt 第 13 行逐字命中（"Henrie peeked her head around the door to Emma's bedchamber. All her life she had hovered by doorways. A chicken hoping to come into the kitchen. "Yoo-hoo!" she bawked softly."）。弯/直引号差异不计，实词一致。✓
- **说话人**：叙事者描写 Henrie 探门。中文理解归因 Henrie，正确。✓
- **引语↔分析对应**：四子项（中文理解/关键词/为什么这样写/读者视角提示）均围绕"Hovering/鸡探头/bawekd"这一出场意象，讲同一句，无截短。✓
- **关键词回查**：peeked ✓、hovered ✓、bawked ✓ 均在引语内。✓
- **结构**：引语行+四子项齐全。✓

### 原句 2
- **引语逐字**：text 第 43 行逐字命中（"Albert's only problem was his mother. … Based on the bitter bile in her throat, Henrie was fairly sure that that was not funny."）。✓
- **说话人**：叙事者内心，对象为 Henrie 被逼到墙角的反应。中文理解归因 Henrie，正确。✓
- **引语↔分析对应**：四子项均讲 Henrie 言行分裂与"baited/Bates"双关，讲同一句，无截短。✓
- **关键词回查**：baited ✓、discordant ✓、badger ✓ 均在引语内。✓
- **结构**：齐全。✓

### 原句 3
- **引语逐字**：text 第 85 行逐字命中（"What if she had looked at Henrie with imploring eyes, … ashamed of himself."）。✓
- **说话人**：叙事者内心，Emma 呛住、Henrie 冷观。中文理解归因 Henrie 的盘问与裁决，正确。✓
- **引语↔分析对应**：四子项均讲"不施救/冷评估/pink woman"，讲同一句，无截短。✓
- **关键词回查**：imploring ✓、frozen ✓、evaluative ✓ 均在引语内。✓
- **结构**：齐全。✓

### 原句 4
- **引语逐字**：text 第 128 行逐字命中（"Henrie wondered, as she watched Albert's head bent to his cup, … choke on a grape."）。✓
- **说话人**：叙事者内心（Henrie 视角）。中文理解归因 Henrie，正确。✓
- **引语↔分析对应**：四子项均讲"登记簿/庆幸"的社交反讽，讲同一句，无截短。✓
- **关键词回查**：register ✓、congratulate ✓、imagined ✓ 均在引语内。✓
- **结构**：齐全。✓

---

## 核对方法说明
- 引语行与中文理解行取自同一 md 且相邻（同一 `### 原句 N` 块内），未跨块拼装。
- 每条引语均在 text/ch62_chapter_12.txt 中 grep 命中，并回看该处前后 ~200 字符窗口确认说话人与归属语境。
- 本章正文段落与引语均落在 text 第 13–128 行之间，章号（Chapter 12）标注正确。
- 本章共 4 个引语块，无孤儿块、无重复块。

ch62 完成：4 块，缺陷 0，待复核 0
---

# d 步二审 · ch63

- 精读 md：`notes/books/novels/miss-bates-by-catherine-cliff/ch63 backgammon with mr woodhouse.md`
- 原文提取件：`notes/books/novels/miss-bates-by-catherine-cliff/text/ch63_chapter_13.txt`（首行 `Chapter 13`，与 md 标题一致，章号无错标）
- 章内共 **4 个引语块**，均为「引语行 + 中文理解 + 关键词 + 为什么这样写 + 读者视角提示」齐全，无孤儿/重复块。

## 结论：共 4 块，通过 3，缺陷 0，待复核 1

逐块核对结果：

| 块 | 引语逐字 | 说话人 | 引语↔分析对应 | 关键词回查 |
|---|---|---|---|---|
| 原句 1 | ✅ text L25 逐字一致 | ✅ 叙事/贴身 Henrie 内心 | ✅ 四子项同讲一句 | ✅ iniquitous / muslin / crabapple 均在引语 |
| 原句 2 | ✅ text L31 逐字一致（含弯引号） | ✅ Woodhouse 先生对话 + 叙事 | ✅ 四子项同讲一句 | ✅ backgammon / comfort / acquaintance 均在引语 |
| 原句 3 | ✅ text L34 逐字一致 | ✅ 叙事/Henrie 视角 | ✅ 四子项同讲一句 | ✅ muffler / bouquet 均在引语 |
| 原句 4 | ✅ text L43 逐字一致 | ✅ 叙事/Henrie 视角 + Perry 先生括号语 | ✅ 四子项同讲一句 | ✅ cordial / condolence / mistress 均在引语 |

## 缺陷清单（无则写"无"）

无。

无引语截短：4 条引语均为 text 中完整整段或完整整句，未被剪断到不足以支撑其后的分析。
无跨章章号错标：md 与 text 均为 Chapter 13。
无说话人反转：4 块的说话人归因均经 text 前后 ~200 字符窗口核对确认。

## 待人工复核

1. **原句 1 · 中文理解末句越界**（轻微，非引语截短）：
   - 引语行原文结尾：`...buried in a prime spot under the old crabapple tree in the churchyard."`
   - 中文理解原文末句：`可 Emma 下葬时大概还是一个有皮肤、有眼睛、有头发的年轻女人，还占着教堂墓地里老海棠树下的一块好位置。她真不该得意忘形。`
   - 说明：「她真不该得意忘形」对应 text 下一段独立的一句 `She really must not gloat.`（text L28，与引语块不在同一段），不在本块引语之内。中文理解把它当作本块内容收尾，与"引语逐字"范围不完全对应。
   - 但本块「读者视角提示」已正确指出「段末紧跟着一行独立的话——'她真不该得意'」，说明作者清楚这是相邻的另一句，并非误认引语内容。故判为轻微内部不一致，不构成引语截短或说话人错标。
   - 建议修法：在中文理解末句前加"（紧随其后一句）"，或将其移入读者视角提示处，避免读者误以为「得意忘形」在本块引语内。

## ch63 完成：4 块，缺陷 0，待复核 1
---

# d 步二审 · ch64

## 结论：共 4 块，通过 4，缺陷 0，待复核 0

## 缺陷清单（无则写"无"）

无

## 待人工复核

无

---

### 逐块核对明细

**原句 1**
- 引语行：`"One member of Highbury society was not pleased by all these recent changes in the social order. Augusta Elton was looking out of the window in her front room, munching on a stale piece of cake like a horse with a carrot—crunch, crunch, crunch—the hard triangle disappeared bit by bit into her mouth."`
- text 命中：段落 1（第 13 行）开篇叙述句，逐字一致 ✓
- 说话人：叙述（非对话）。中文理解归因为"Highbury 社交圈一位成员 / Augusta Elton"的第三人称叙述，正确 ✓
- 关键词 stale piece of cake / like a horse with a carrot / munching 均在引语内 ✓
- 四子项齐全、同一句，无截短 ✓

**原句 2**
- 引语行：`"She used her moistened fingertip to collect some stray crumbs on the windowsill and reunite them with their brethren in her mouth. Henrie was nearing the old chestnut tree, looking up into its flowering branches—much like an idiot, Mrs. Elton observed."`
- text 命中：第 13 行同一段，逐字一致 ✓
- 说话人：叙述，其中 "much like an idiot, Mrs. Elton observed" 明确挂到 Mrs. Elton。中文理解归因"用 Mrs. Elton 的观察来说，傻乎乎地出神"正确 ✓
- 关键词 moistened fingertip / crumbs / much like an idiot 均在引语内 ✓
- 四子项齐全、同一句，无截短 ✓

**原句 3**
- 引语行：`"She stopped speaking because Henrie had now paused and turned, looking up at the window, unerringly, to the spot where Mrs. Elton stood. The erstwhile Miss Bates looked not like a simpleton at all, but more like something awesome and austere. Mrs. Elton swallowed a dry crumb which had caught at the back of her tongue."`
- text 命中：第 13 行同一段，逐字一致 ✓
- 说话人：叙述。中文理解归因正确 ✓
- 关键词 unerringly / awesome and austere / swallowed 均在引语内 ✓
- 四子项齐全、同一句，无截短 ✓

**原句 4**
- 引语行：`"A shiver ran over Augusta Elton as she watched a slow, private smile, so different from Miss Bates’s energetic smiles of old, spread across Henrie’s face as their eyes met."`
- text 命中：第 13 行同一段末尾，逐字一致（md 用弯引号 ’，text 亦为弯引号，无差异）✓
- 说话人：叙述。中文理解归因正确 ✓
- 关键词 a shiver / a slow, private smile 均在引语内 ✓
- 四子项齐全、同一句，无截短 ✓

---

### 附：本章词汇例句抽查（非门禁项，均逐字命中）
- high-handed：`"I can tell you that that unsmiling, high-handed spinster had very few friends indeed."` ✓
- effusions：`"And one would think that the new Mrs. Woodhouse would have plenty more reason for happiness and effusions than the old Miss Bates, but no, these days there is nary a smile, hardly a word."` ✓
- complaisant：`"And she used to have such a complaisant, grateful, voluble way about her."` ✓
- ninny：`"Selina positively stared when I told her that Miss Bates, the village ninny, had married Mr. Woodhouse."` ✓
- morsel：`"Mrs. Elton’s hand fished around on her plate for any morsel she may have missed, her eyes still fixed on Henrie."` ✓
- patronage：`"This required a moment of silent respect for all which the benefit of that patronage would have meant to the girl, robbed of so many favors and connections by cruel death."` ✓
- stale：`"You, this cake is terribly stale, please take this plate away and tell Cook it was inedible."` ✓
- mourning：`"People say that’s the mourning, but it is my opinion, and I am rarely wrong, that the woman has given up pleasing!"` ✓

ch64 完成：4 块，缺陷 0，待复核 0