# ch00《Prologue》· R3 对账 + R4 逐块判定

- 书：`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez`
- 本轮：`ch00 prologue.md`（118 行） × `review/ch00/1-suread.json`（6 条 fact） × `text/ch00_prologue.txt`（24 行）
- 对账员：DSH-Mac ｜ 参照集：`text/`（不引 epub）
- 铁律自检：**所有「错位/错」条目都已确认引语行与分析行在同一 md 文件内相邻或同段**；未跨文件拼装 `text/` 句子。

## 0. 扫描集与未覆盖声明

**已判完**：
- R3：`1-suread.json` **6/6 条 fact 全部逐条判定**（见 §1）。
- R4：**5/5 个引语块全部判定完毕**（原句 1–5，见 §6），无未判块。
- 词汇表 19 条例句逐字核过（脚本 flat 比对，19/19 命中原文）。

**未进本轮扫描集（明确列出，不写「通过」）**：
1. **词汇表 19 条的中文释义准确性**未逐项判（只核例句逐字）；例：L86「sprawled = 趴伏、四肢摊开地躺着」属释义裁量，未判。
2. **`一句话总结` L116–118 未单独成条判定**（其中的「头部伤与不明耳环」并入 §4 E1/E3 两条）。
3. **本书他章（ch01–ch17）未作为本章 R3/R4 对象**；跨章取证只用于核实本章 md 的断言是否成立（取证结果记在条目里）。
4. **md 的英文小标题/关键词行**（L24/L36/L48/L60/L72 等）未判「关键词是否落在本块引语」——该判据属 `structure.py anchor`，本轮未跑（不在 R3/R4 职责内）。

---

## 1. R3 主表：素读 6 条 fact 逐条对账

| 素读事实 | md 落点 | 判定 |
|---|---|---|
| F1 黑暗中苏醒、摊在地板；灯分阶段亮起（像有人在有节奏地拨开关）；亮光「像一脚踢在脸上」；重新躺下闭眼躺了一会儿 | `ch00 prologue.md:20`（引语）/ `:22`（中文理解）/ `:26`（句子结构）/ `:28`（为什么这样写）/ `:30`（读者视角提示）/ 词表 `:86,:87,:111` | ✅ 一致（中文理解把「kick」译作「耳光」，见 §4 E2） |
| F2 浮现上次与 Brigitte 试戴塑料皇冠的画面；在这段记忆里躲了一分钟；女儿笑声（央求买下半个店）被一阵刺耳耳鸣取代 | `ch00 prologue.md:32`（引语）/ `:34`（中文理解）/ `:38`（句子结构）/ `:40`（为什么这样写）/ `:42`（读者视角提示）/ 词表 `:97` | ✅ 一致（「躲了一分钟」在中文理解里省略，但 `:38` 逐句结构原样引了 "For a minute, she took refuge in that memory."） |
| F3 撑起坐起、睁眼惊骇：成排芭蕾裙被红色泼溅、红染蝴蝶翅膀与毛绒耳罩、熊形背包、绒球触角全覆干硬血壳；在女儿最爱的店里、在 Brigitte 把廉价首饰当真品的地方；比任何事都伤、比命数更伤 | `ch00 prologue.md:44`（引语）/ `:46`（中文理解）/ `:50`（句子结构）/ `:52`（为什么这样写）/ `:54`（读者视角提示）/ 词表 `:98,:99,:100,:101` | ✅ 一致 |
| F4 头痛欲裂；几乎伸手去摸却停住，怕头不在或不完整；照「女孩们看芭蕾舞鞋」的镜子见倒影：头还在，头发结块、脸是大片深色污痕；把身体拖近；喘不上气；从未如此虚弱 | `ch00 prologue.md:56`（引语）/ `:58`（中文理解）/ `:62`（句子结构）/ `:64`（为什么这样写）/ 词表 `:88,:103` | ✅ 一致（中文理解把 matted hair 写成「结成血块」，见 §3 E3） |
| F5 脸也血糊；耳朵上新穿孔、塞满没见过的耳环；数出**九个**耳圈，大小不一，**一耳五、一耳四**；看似银质但因结痂褐黑不能确定；不记得的那次「预约」必定漫长、不卫生、残忍 | `ch00 prologue.md:56`（引语）/ `:58`（中文理解）/ `:62`（句子结构）/ `:64`（为什么这样写）/ `:66`（读者视角提示）/ 词表 `:89,:90,:104,:105` | ✅ 一致（数字 9/5/4 三项逐字对上，原文见 `text/ch00_prologue.txt:21`） |
| F6 听见有人哼唱 → 转头 → 看见那个女孩 | `ch00 prologue.md:68`（引语）/ `:70`（中文理解）/ `:74`（句子结构）/ `:76`（为什么这样写）/ `:78`（读者视角提示）/ 词表 `:114` | ✅ 一致 |

**小计**：✅ 一致 6 ｜ ❌ 漏 0 ｜ ❌ 错 0（本表口径）｜ ❌ 编 0（本表口径）—— 本表只判「素读 fact 有没有在 md 落地」。
md 反向多出来的主张、以及两边不一致之处，统一进 §3（编单）与 §4（错单）。

---

## 2. R3 单子一：漏（素读有、md 完全没写）

**空 —— 0 条。**

6 条 fact 的每一项实体（人/物/动作/数字/因果）都在 md 里有落点，逐条落点见 §1。

补充核查（易漏项，单独确认过）：
- 「九个耳圈、一耳五只一耳四只」这类**数字**：`ch00 prologue.md:58` 逐字给出「九个圈…一只耳五只、一只耳四只」✅
- 「干了结壳的血」：`ch00 prologue.md:46` 「一层如今已干硬的血痂覆盖」✅
- 「Brigitte 把廉价首饰当真品」：`ch00 prologue.md:46` ✅
- 「女孩们照芭蕾舞鞋的镜子」：`ch00 prologue.md:58` ✅

---

## 3. R3 单子二：编（md 有、素读没有 ⇒ 已回 `text/ch00_prologue.txt` 核实）

| # | md 落点 | md 的主张 | 原文核实 | 判定 / 档位 |
|---|---|---|---|---|
| E1 | `ch00 prologue.md:64` | 「把施暴者写成某种**有专业身份的人（像从业者）**而非普通凶手」 | 原文 `text/ch00_prologue.txt:21` 全文只写 "The appointment she couldn’t remember must have been long, **unhygienic**, and cruel." —— 无任何「专业/从业」措辞；`unhygienic` 指向的恰是非专业。全书 `text/` grep `practi*` 仅得 practically/practice/practical（ch02/ch03/ch04/ch05/ch10/ch12/ch17），**无 practitioner**；且 `text/ch11_chapter_11.txt:138` 揭穿施暴者是少女本人——「She didn’t use a piercing gun, or numb her up with an ice cube. She just channeled her rage into squeezing each earring post directly through Alba’s pale earlobe」，与「专业身份」直接相反 | ❌ 编 ｜**阻断**（建议删「把施暴者写成某种有专业身份的人（像从业者）而非普通凶手」一句；同段前半「appointment＝被预约的仪式／伪装成医疗美容行为」是正当解读，可保留） |
| E2 | `ch00 prologue.md:66` | 「"appointment she couldn’t remember" **暗示药物或催眠**」 | 全书 `text/` grep `anesthet*｜sedat*｜hypnos*｜drugged｜tranquiliz*｜narcotic*｜drugs` ⇒ **0 命中**（仅 `text/ch05_chapter_5.txt:177` Valium、`text/ch06_chapter_6.txt:87` sleeping pill，均与序章无关）。`text/ch11_chapter_11.txt:60` 的 "like when anesthesia starts to wear off" 是**比喻**（形容针刺感），不是给 Alba 用了药 | ❌ 编 ｜**提示**（书中无药物/催眠设定；「appointment」确有医疗联想，但「药物或催眠」是具体情节断言。建议改为「暗示这像一场被安排好的医疗/美容处置」，去掉药物与催眠） |
| E3 | `ch00 prologue.md:58` | 「头发**结成血块**」 | 原文 `text/ch00_prologue.txt:21`："Her head was there, but **her hair was matted**, and her face was a big, dark smudge." —— matted＝打结/结块，**未说血**；血在脸上（dark smudge）与现场的干血壳。本文件 `:62`（句子结构）自己也写作 "her hair was matted" | ❌ 编 ｜**提示**（细节加字；建议改「头发结成一团」） |
| E4 | `ch00 prologue.md:10` | 「自己**头部重创**」 | `text/ch00_prologue.txt:21` 只写 "Her head was pounding. She almost touched it but stopped herself, afraid it wouldn’t be there, or not entirely there." —— 序章**未描述头部创口**，是暗示。跨章取证：`text/ch11_chapter_11.txt:6` "She hit her head against the wall and fell right back to where she was before."、`text/ch12_chapter_12.txt:6` 重述序章同一段 ⇒ 全书层面「头部有伤」成立 | ❌ 编（弱）｜**需人判**（跨章有据，可保留；若按「本章逐字」口径则应改「头部伤」或「疑似头部受创」） |

---

## 4. R3 单子三：错（两边都有但不一致）

| # | 素读事实 | md 落点 | md 的说法 | 另一侧原文/素读 | 判定 / 档位 |
|---|---|---|---|---|---|
| E1' | F5：耳洞在**耳朵**上（ears were covered in new piercings）；脸是「大片暗色污痕」 | `ch00 prologue.md:10`（导航·一句话概括） | 「自己头部重创、**脸上布满不明穿孔**」 | `text/ch00_prologue.txt:21`："her face was a big, dark smudge, … and she saw that **her ears were covered in new piercings**" —— 穿孔在耳，不在脸；脸是血污。**同文件 `:58`（中文理解）写的是「耳朵上布满新的穿孔」，与 `:10` 自相矛盾** | ❌ 错（部位错）｜**阻断**（建议把 `:10` 改为「头部重创、耳朵上布满陌生的新穿孔」） |
| E2' | F1：亮光「像**一脚踢**在脸上」 | `ch00 prologue.md:22`（中文理解） | 「强光像**一记耳光**打在脸上」 | `text/ch00_prologue.txt:12`："The brightness was like **a kick** to the face." —— kick＝踢；耳光＝掌掴，动作与施事部位都不同。**同文件 `:26`（句子结构）自己写 "Kick to the face"、`:28` 也写 "like a kick to the face"**，与 `:22` 自相矛盾 | ❌ 错（译法不一致，轻）｜**提示**（建议「像挨了一脚」/「像一记重击」） |

---

## 5. 已核实为正确（防误修，勿动）

| md 落点 | 写法 | 核实依据 |
|---|---|---|
| `ch00 prologue.md:14` | 「主角（后文揭示为 **Alba**）」 | `text/ch12_chapter_12.txt:6` 逐字重述序章："**Alba** came to in the dark, sprawled across the floor."；`text/ch02_chapter_2.txt` 起首现 Alba；`text/ch11_chapter_11.txt:63,126,138` 为 Alba 本人 |
| `ch00 prologue.md:14` | 「发现头部伤与**陌生耳环**」 | `text/ch00_prologue.txt:21` "full of earrings she’d never seen before" |
| `ch00 prologue.md:42` | 「Brigitte 与 "the girl"（最后一句）尚未明确是否为同一人」 | `text/ch00_prologue.txt:24` 末句只写 "saw the girl"，全书 `text/` 中 "the girl" 从未与 Brigitte 或 Brisa 并置同指（ch13:6/L18、ch15:81、ch17:75 均无名指称） |
| `ch00 prologue.md:10` | 「在一家**儿童用品店**里苏醒」「店里布满干涸的血」 | `text/ch00_prologue.txt:18` 列举 tutus/butterfly wings/earmuffs/bear-shaped backpacks/pom-pom antennae + "cheap jewelry" ⇒ 儿童用品店成立；血＝"a now-stiff crust of dried blood"（同店即 `text/ch11_chapter_11.txt:126` Claire's，ch11:132 亦列 "tulle butterfly wings, pom-pom antennae, tutus in every color"） |
| `ch00 prologue.md:64` | 「"appointment" 一词把暴力伪装成医疗/美容行为」「must have been long, unhygienic, and cruel 三形容词递增」 | `text/ch00_prologue.txt:21` 三形容词逐字在序章内；医疗/美容联想属正当解读（**仅 E1 那半句「施暴者有专业身份」要删**） |
| `ch00 prologue.md:66` | 「九个耳环…是本章**唯一可数的细节**」 | 全章数字只有 nine / five / four（`text/ch00_prologue.txt:21`），可数断言成立 |
| `ch00 prologue.md:76` | 「全章最后一句只有 **10 个词**」 | `text/ch00_prologue.txt:24` "Then, hearing someone humming, she turned and saw the girl." ＝ 10 词 |
| `ch00 prologue.md:12` | 「为 Diana / Brisa / **Alba** 等人物的后续出场埋下伏笔」 | 三人名均在 `text/` 出现（Alba：ch02 起；Diana/Brisa：ch01 起）；Brisa 与 Brigitte 是**两个不同的孩子**（`text/ch05_chapter_5.txt:216` 同场出现 "Brisa even checked inside the yellow capsule from a Kinder egg" 与 "Brigitte lay flat on the floor"）——md 未混用，判为不矛盾 |

---

## 6. R4 逐块对应人判（本章 5 块，全部判定完毕）

| 块 | 引语首 20 字 | 判定 | 依据（哪一行分析） |
|---|---|---|---|
| 原句 1 | "She came to in the dark, spra…" | 对应 | 中文理解 `:22`（逐句对应该引语）；句子结构 `:26`（四句递进，句数与原文一致）；为什么这样写 `:28`（引 "as if someone were rhythmically flipping the switches" 与 "like a kick to the face"，两句皆在本块引语内）；读者视角提示 `:30`（引 "stayed that way awhile"，在本块末句） |
| 原句 2 | "An image arose in her mind: …" | 对应 | 中文理解 `:34`；句子结构 `:38`（三句全在本引语内）；为什么这样写 `:40`（主论点是本引语内 "begging to buy half the store" 与耳鸣的并置；其中 "rows of tutus splattered with red" 明写「**与后文**…形成对照」，属有标注的前瞻对照，不是把引语截短）；读者视角提示 `:42`（谈 Brigitte 与 "the girl" 的关系，属人物层，不构成引语选短） |
| 原句 3 | "She pushed herself up to a seat…" | 对应 | 中文理解 `:46`；句子结构 `:50`（五句拆分与原文一一对应）；为什么这样写 `:52`（"red-stained" / "now-stiff crust of dried blood" / "more than whatever fate this was" 全在本引语内）；读者视角提示 `:54`（引 "in her daughter’s favorite store"，在本引语内） |
| 原句 4 | "Her head was pounding. She al…" | 对应 | 中文理解 `:58`；句子结构 `:62`（「九句」逐句核对＝原文 9 句，**句数正确**）；为什么这样写 `:64`（"afraid it wouldn’t be there, or not entirely there" 与 "The appointment she couldn’t remember" 均在本引语内；**但其结论部分见 §3 E1 属编，不影响本块「对应」判定**）；读者视角提示 `:66`（引 "appointment she couldn’t remember"，在本引语内） |
| 原句 5 | "Then, hearing someone humming, s…" | 对应 | 中文理解 `:70`；句子结构 `:74`（现在分词状语 + 并列动词，逐字在本引语内）；为什么这样写 `:76`（论点是末句本身；"the girl" 的定冠词分析属语言层解读）；读者视角提示 `:78`（讲本引语的结尾效果） |

**R4 小计**：对应 5 ｜ 引语选短 0 ｜ 不对应 0 ｜ 密度不足 0。

**关于「引语选短」为何 0 条**：本章 5 条引语**均为原文整段**（`text/ch00_prologue.txt:12/15/18/21/24` 一段一引语，逐字核对无省略、无拼接、无截断）⇒ 分析不可能「讲引语之外的上下文而引语没截到」；若真要判引语选短，反而得先证明引语不完整。逐字核验：`verify_fragments_indep.py` 本书 109 条引语 / 346 片段 → MISS 0、拼接未标省略号 0；本轮另做 flat 比对，本章 5 条引语与 19 条例句 24/24 逐字命中。

**R4 附：逐块「施事/归属」核对（R4 固定追问）**
| 块 | 施事核对 | 结论 |
|---|---|---|
| 原句 1 | 施事＝环境（灯/强光），受事＝主角 | 一致 |
| 原句 2 | 施事＝女儿的笑声／耳鸣，受事＝主角的记忆 | 一致 |
| 原句 3 | 施事＝眼前景象（the sight of it），受事＝主角（hurt） | 一致（`:46` 译「这幅景象…刺痛了她」主客正确） |
| 原句 4 | 施事＝主角自己（She counted / She caught / She dragged），受事＝头部、耳环、镜子 | 一致 |
| 原句 5 | 施事＝外部声音（someone humming），受事＝主角（she turned and saw） | 一致 |

---

## 7. 提示（非阻断，不进三张单子）

| md 落点 | 现象 | 建议 |
|---|---|---|
| `ch00 prologue.md:26` | 「与前句的 **kicks** 形成强弱对比」——原文为单数 "a kick"；同句 "Kick to the face" 首字母大写 | 改 "kick"；大小写随句内格式 |
| `ch00 prologue.md:54`、`:66` | 「**全章唯一一次**」「本章**唯一可数**的细节」——属可数/最高级断言（`docs/rules/30-writing.md` 7c/7g 要求改成可核写法） | 本章成立，但建议写成「本段仅此一次」式就地可证写法 |
| `ch00 prologue.md:76` | 「暗示这个女孩对主角而言**并不陌生**」——原文只给 "the"，未给「主角认识她」的依据；`text/ch11_chapter_11.txt:63` 反而写 Alba 多年只记得一个模糊影像 | 已带「或至少，作者希望读者这样怀疑」的让步，判提示；如需收紧可改「定冠词让读者以为读者与主角共享指称」 |
| 工具盲区 | 早前 sweep 报告 `.memory/raw-gates/don-t-leave-her-alone-by-desiree-de-fez/2026-10-20-d-sweep-analysis-inline.txt:124` 标 `ch00 prologue.md:64 「 practitioner」→ 疑派生词`——**当前 md 全文已无 "practi" 字样**（现为中文「像从业者」）；该 sweep 条目疑似基于更早版本的 md，现已失效 | 修复方注意：真正要处理的是 §3 E1 的**论断**（施暴者有专业身份），不是那个英文词 |

---

**本章结论**：R3 漏 0 条；编 4 条（**阻断 1**：E1 施暴者专业身份；提示 2：E2 药物/催眠、E3 头发血块；需人判 1：E4 头部重创）；错 2 条（**阻断 1**：E1' `:10` 穿孔部位；提示 1：E2' `:22` 耳光/kick）。R4：5/5 块全部判定完毕，5 条对应、0 引语选短、0 不对应、0 密度不足。
