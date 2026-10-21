# 3-diff.md · 《A Fatal Legacy》第 1 章 审查对账

- 审查方：独立审查员（只查 ch01）
- 唯一权威源：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch01_1.txt`（2404 字符；下称「原文」）
- 受审 md：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch01 digby dies on the institute rug.md`
- 底稿：`1-suread.json`（R1 素读，先于读 md）、`2-machine.json`（R2 机器层，`chapter.sh --json`，退出码 0 / verdict ok）
- 字符区间一律为**原文原始文件**的 0 基字符偏移（非归一化文本）。

---

## 一、漏（原文有、md 没有）

### L1 · 濒死递进的最后一级台阶：「喉咙闭合 + 挣扎呼吸」
- **原文**（区间 **2256–2339**）：`Digby’s throat is beginning to close. He turns his head as he struggles to breathe.`
- **md**：全文检索「喉」「throat」均 **0 命中**；无引语块引用，分析层未提及，词汇表亦无。
- **md 自设的对照物**：原句 2 的读者视角提示写「留意身体失控自下而上推进的顺序」——而链条的第三级（喉）恰恰没被引用。
- **取捨理由**：md 未写任何取捨说明。
- **档**：提示（死亡本身由原句 6「as his heart stops」覆盖，本项非转折缺失；属引语覆盖缺口，一行可补）

### L2 · 递进第二级台阶：「Digby can’t feel his legs.」
- **原文**（区间 **1519–1545**）：`Digby can’t feel his legs.`
- **md**：只在**词汇表例句**里出现一次（`| legs | 腿 | Digby can’t feel his legs. |`），**无任何引语块**引用、无分析；原句 4 的引语直接从 `The coldness,` 起，把同一段的第一句丢在引语外。
- **取捨理由**：无。
- **档**：提示

### L3 · 六块未译楔形文字泥板 + 博物馆二楼
- **原文**（区间 **722–803**）：`Besides, the rug made a great jumping-off point for Digby to talk about the six as-yet-untranslated cuneiform tablets the museum had on the second floor.`
- **md**：仅作词汇例句（cuneiform / jumping-off 两行）出现；分析层与导航均未收录（「二楼」0 命中）。这是 md 断言迪吉是「博物馆学者」的唯一具体证据。
- **档**：提示

### L4 · NW1 的破旧联排住宅（迪吉的边缘处境）
- **原文**（区间 **2219–2253**）：`whereas he has spent his short life paying homage to those seedy adventures from a decrepit town house in NW1.`
- **md**：「NW1」只出现在 galivanting / seedy 两行**词汇例句**里；导航「人物弧线」「视角」均未交代迪吉住在 NW1 的破旧房子里。
- **档**：提示

---

## 二、编（md 有、原文没有）

### C1 ·【阻断】把凶手的活眼睛说成「这间屋子里的收藏」
- **md**（原句 5 · 为什么这样写）：`那双冷硬如钢的眼睛来自这间屋子里的收藏，与开篇铺陈的柜中标本彼此呼应；`
- **原文**（区间 **1810–1865**）：`He catches a cold steely eye lazily gazing back at him, and he knows that help isn’t coming and he is about to die surrounded here by the morbidity of his odious ancestor.`
- **为什么不符**：原文里这只眼睛是**一个正在回望他的人**（凶手在场，「help isn’t coming」正由此而来）；「藏品」在原文中是**另一组东西**——`Horatio Combe’s shrine to his obsessions.`（1982–2023）与 `The shrunken heads watch from their cabinet as his heart stops.`（2340–2403）。md 把「凶手」改写成「藏品」，与原文相反，且与同句「不会有人来救」的现场逻辑冲突（若凶手是标本，就不会「lazily gazing back」）。
- **档**：阻断（编造情节关系）

### C2 ·【提示】「中毒」作为既成事实（2 处）
- **md**：导航「一句话概括」与文末「一句话总结」两处均写 `中毒濒死`。
- **原文**：全文无「毒/poison」字样，只有症状描写（`Digby can’t feel his toes.` / `The coldness, the frozen hand of death, is moving up his body inch by mortal inch.`）。
- **为什么不符**：属合理推断而非文本事实（本书 ch05「the poisoned salad is investigated」事后才坐实），但 ch01 精读层面应写成「疑为中毒／原因不明」而非断言。
- **档**：提示

### C3 ·【提示】「自家博物馆」（2 处）
- **md**：导航「一句话概括」`在自家博物馆的古董地毯上`；文末「一句话总结」`在自己博物馆的古董地毯上`。
- **原文**：只说 `the museum had on the second floor`（722–803）与 `Horatio Combe’s shrine to his obsessions.`（1982–2023）——博物馆是**以祖先命名的研究所**，原文未说迪吉拥有它。
- **档**：提示

---

## 三、错（两边都有但不一致：主语 / 因果 / 数字 / 时序）

### X1 ·【提示】块 1 的从句归属错位（谁在劫掠、谁在作乐）
- **md**（原句 1 · 中文理解）：`1849 年由当时那位"感激他的"伊朗统治者纳赛尔·丁"赠予"他的曾曾曾祖父，随之而来的是亚历山大大帝式的劫掠足迹与波斯波利斯废墟上的作乐。`
- **原文**（区间 **71–378**）：`…apocryphally gifted to his great-great-great-grandfather in 1849 by an appreciative Naser al-Din, the then Shah of Iran, while he followed in the marauding footsteps of Alexander the Great across Central Asia and made merry with the ruins of Persepolis.`
- **不一致**：原文里「追随亚历山大的劫掠足迹、在波斯波利斯废墟上作乐」是**赠礼者 Shah 本人**的行状（`while he followed…` 的主语是 Shah）；md 用「随之而来的是」把这两件事挂到**地毯**身上，且把 Shah 的「作乐」与亚历山大的「劫掠足迹」并列成同一主体的两项。
- **为什么只判提示**：1849、Naser al-Din（时任 Shah）、亚历山大大帝、波斯波利斯四项事实全部在位，原文从句本身有歧义，中文压缩尚可辩；只判错在归属松动，未与原文事实相反。
- **档**：提示

### X2 ·【提示】块 3 的因果方向与原文相反
- **md**（原句 3 · 为什么这样写）：`他用自己的性别给一条自我约束的规矩开了后门，于是毫无防备地私下赴了约。`
- **原文**（区间 **874–1516**）：`Digby was taken by surprise. He’d thought better of himself. He’d thought too much, frankly, and Digby hadn’t ever stopped to consider that this little tête-à-tête wasn’t the best idea. He was a man, after all, and cardinal rules like meet in a public place applied to only women.`
- **不一致**：原文是**先赴约、后自辩**（`hadn’t ever stopped to consider that this little tête-à-tête wasn’t the best idea` → 才是 `He was a man, after all…`），且自辩的前提是「他想得太多、他自认更聪明」。md 写成「因为规矩有例外→所以他去赴约」，因果反了，讽刺点（男人自认无风险）也换掉了。
- **档**：提示

### X3 ·【提示】章末总结停在「濒死」，与本章结局（已死亡）不一致
- **md**（文末 一句话总结）：`…在自己博物馆的古董地毯上中毒濒死，身体一寸寸失温的这段时间里…`（无死亡）
- **原文**（区间 **2340–2403**）：`The shrunken heads watch from his cabinet as his heart stops.`——心脏停止＝死亡完成。
- **内部自相矛盾**：md 自己的导航「叙事手法」写 `结尾把死者的结局交给柜中标本的凝视`，已承认死者结局；文末总结却只写「濒死」。
- **档**：提示

### X4 ·【提示】块 1「掠夺来的东西」指代不明（按地毯读则与原文相反）
- **md**（原句 1 · 为什么这样写）：`这间屋子把掠夺来的东西包装成馈赠、把遗物供奉成圣物。`
- **原文**：地毯**不是**掠来的——`It had in fact been purchased down Portobello Road to hide an ugly port stain on the floorboard in 1927, but this fact was now lost to the vagaries of time.`（**493–543** 起，md 自己的导航「线索结构」写的正是「其实是 1927 年的旧物」，与此处相反）。若把「掠夺来的东西」泛指 Horatio Combe 的藏品，则与原文 `The relics of an exhilarating life led galivanting all over the empire collecting whatever and whoever took his fancy` 相容——一句两读。
- **档**：提示（建议明确指代）

### X5 ·【提示】内部引述与本章末句/本块译文不一致
- **md**（原句 1 · 为什么这样写）：`读者读到最后一句"僵硬的标本正在看着他"时，会意识到…`
- **md 本章末句**（原句 6 · 中文理解）：`柜子里那些风干的缩头就这样看着，直到他的心脏停下。`
- **原文**（区间 **2340–2403**）：`The shrunken heads watch from his cabinet as his heart stops.`
- **不一致**：md 用引号引述的「僵硬的标本正在看着他」既非原文，也与本 md 自己的译文（**风干**的缩头，词汇表亦注「风干的缩头标本」）不一致。
- **档**：提示

---

## 四、机器层与形态实情（R2，非本次缺陷）

- `bash scripts/chapter.sh "<ch01 md>" --json` → **退出码 0**，verdict `ok`，`issues` 四类全空。
- 引语 **6/6** `ok`；本审查另用**原始文件**（未归一化）独立取证复核：6 条引语在 `text/ch01_1.txt` 中**原样命中**，原始偏移 71 / 806 / 1061 / 1546 / 1810 / 2340；**无 `…`、无跨段拼接、无省略号缝合**。
- 词汇：`python3 scripts/check_vocab.py <书目录>` → **FAIL 0**；ch01 的 21 条例句（⭐⭐⭐6 / ⭐⭐7 / ⭐8）经查全部为**本章原句**，无跨章搬句、无自标「未出现」。
- 形态（对照 profile `mystery-thriller`，另有本书众数可用）：H1 = `# 1. The Horatio Combe Institute, Priory Square, Camden` → `# NN. 标题` **符合**（标题取自原文首行英文地名，本书各章同形）；导航 **5 项** = profile 5 项 **符合**；子项 = 中文理解 / 关键词 / 为什么这样写 / 读者视角提示 **四项全齐且 6 块一致** **符合**；块数 **6**，落在 profile 的 3–10 内，也在本书众数区间 [5,10] 内（众数中位 7）。**形态组无偏离，无需理由。**
- 中文密度：6 块中文理解 CJK 占比 0.85–0.92、「为什么这样写」0.81–0.92，无整段英文（关键词项 CJK 计数为 0 属该子项性质，非英文夹杂）。
- **机器层未报任何红项** ⇒ 本章所有问题都是机器查不了的三类：**漏 / 编 / 对应**。

---

## 五、附注（非本章精读缺陷，需派工人处理）

书目录 `notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/` 内，**ch02–ch54 各存在一个无扩展名的重复文件**，内容与同名 `.md` **完全相同**（`diff -q` → IDENTICAL），共 **53 个**：

- **已被 git 跟踪的 15 个**：`ch08 callie opens the neon pink box` / `ch12 callie meets eulalia at tate` / `ch24 benedict opens his basement` / `ch25 scott brown goes missing` / `ch26 matt returns from harrogate` / `ch28 leigh cannot place scott` / `ch31 a second body is found at priory square` / `ch32 eulalia watches from her window` / `ch37 robbie takes over the case` / `ch39 the institute is to be sold` / `ch41 margot bourne is questioned` / `ch43 the forum stories are read` / `ch48 the case is rebuilt on the board` / `ch51 caius runs in the park` / `ch54 there is no heartbeat`
- **未跟踪（在磁盘上）的 38 个**（`git status` 显示 `??`）
- ch01 恰好**没有**这个重复件——形态上像是某次重命名的残留（ch02–ch54 有、ch01 无）。

风险：Quartz 构建会把这些无扩展名文件当页面渲染，造成同名重复页；且若有人违反 AGENTS「禁止 `git add -A`」误提交，会一次卷入几十个重复文件。请派工人核实来源后清理（**只删无扩展名的重复件，保留 `.md`**）。本审查员按纪律 4 **未改书目录任何文件**。
