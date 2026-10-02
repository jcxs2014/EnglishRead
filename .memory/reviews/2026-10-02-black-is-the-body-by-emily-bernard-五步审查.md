# 《Black Is the Body》独立五步审查 — 缺陷清单与整改记录

- 书籍：`notes/books/non-fiction/black-is-the-body-by-emily-bernard/`（Emily Bernard 随笔集，13 章精读 + 3 篇总览；非虚构论述格式）
- 触发：用户主动发起（m01005）「先读 AGENTS.md 第 10 条 + 模板五步法节，回执三项后开始审查」
- 执行依据：`AGENTS.md` 第 10 条（`AGENTS.md:260` 触发条件）+ `docs/新书启动模板.md:706-710` a–e 五小标题、`:707-710` 审查自身四条纪律
- 口径：a–e 全部完整执行，不降级；同会话盲区只在结论部分标注
- epub 位置（本书特殊）：`<书目录>/library/` 内，`verify_quotes.py "<书目录>" "<epub>" [--full]` ⇒ 完整 lane

---

## a. 第 3 条提交门禁全量重跑（不信报告数字）

原始逐行输出：`.memory/raw-gates/black-is-the-body-by-emily-bernard/2026-10-02-review-a-gates.txt`

| 检查 | 首跑结果 |
| --- | --- |
| `verify_quotes --full` | 166/166（100%）；完全干净文件 15/15 |
| `check_vocab` | 词条行 839 ｜ FAIL 0 ｜ WARN 0 |
| `check_entities` | 0 个文件存在未知实体 |
| `corruption_scan` | FAIL 0 处（U+FFFD / 双句号） |
| `sweep_full` | ✅ 128 ｜ 跨章 0 |

**a 步结论：门禁全绿，无内容缺陷**——但门禁本身在本书暴露了 1 个结构性盲区（见「工具盲区」#1）。

---

## b. 逐章归属

原始输出：`2026-10-02-review-b-gates.txt`

- 13 章逐章归属：**全部 10/10 in 本章 text**，无跨章错配。
- `check_short_quotes`：10 条短引语命中（全书固定项，`verify_quotes` 不校，由该脚本兜底）。
- `check_anchor`：130 个引语块，凭空造词 0、松散关键词 0。

**b 步结论：无跨章错配，无遗漏块。**

---

## c. 结构扫描

原始输出：`2026-10-02-review-c-gates.txt`

| 检查 | 首跑结果 |
| --- | --- |
| `audit_structure` | 16 个 md、176 个引语块；❌ 结构缺陷 0 ｜ ⚠️ 0 ｜ 🔀 0 |
| `check_struct_indep.py`（第二实现） | **缺陷 39 处** |

### c 步唯一真缺陷：词汇表缺三档 H3（39 条）

- 判据：`scripts/check_struct_indep.py:32` `TIER = ["### ⭐⭐⭐ 高级", "### ⭐⭐ 进阶", "### ⭐ 基础"]`，`:226-228` 整串子串匹配；本书 16 个 md 中 `⭐` 出现 **0 次**。
- 规范源：`docs/新书启动模板.md:1146` 非虚构档第 6 条「6. `## 词汇分级`：⭐⭐⭐ / ⭐⭐ / ⭐ **三档表格**」；全库 32 本非虚构有 30 本带该 H3 ⇒ 本书属漏做，不是格式变通。
- **两把尺子互相看不见**（盲区 #1）：`scripts/check_vocab.py:90` `TIER_PAT = re.compile(r'^#+\s*[⭐★]*\s*(高级|进阶|基础)')` —— 无 H3 时 `tier=None`，分档检测**直接跳过**，所以 check_vocab 报 WARN 0；check_struct_indep 报 39。两个脚本口径不一致，且都不报「口径冲突」。

### 整改过程（两次失败，都靠 `git checkout` 回滚）

1. 第一次脚本 bucket 键名被 mangled ⇒ 839 行词条全丢，回滚。
2. 第二次扫描边界算错 ⇒ `rows=0`，回滚。
3. 成功方案：以 `## 词汇分级` 行号 `i` 为锚扫到下一个 `## `，取 `|` 开头且非表头/非分隔线的行，按规则分档后重写 `lines[:i+1] + [""] + 三段(H3+空行+表头+行+空行) + lines[k:]`。
   - 分档规则：最长实词 ≥12 **或** 存在 ≥10 且不在 `check_vocab` 的 `COMMON` → 高级；≤5 **或** 全部实词 ∈ `COMMON` → 基础；其余 → 进阶。
   - 结果：高级 205 / 进阶 525 / 基础 109（24% / 63% / 13%）。

顺带修：总览三篇「伊莎贝拉四岁要求拉直头发」无出处（ch09 源文只写 `a few days before her birthday`），改为不写年龄。

**c 步结论：39 条真缺陷（实为 13 章 + 3 篇总览的同一类漏做），一次整改完成。**

---

## d. 语义二审

机械子项：`check_struct_indep.py` 缺陷 39（已在 c 步修完）、`check_anchor` 0/0、`sweep_analysis_inline` 逐字 1249 / 跨章 0。

语义层交给**两个后台子代理分章审**（`82b53c37` ch01–ch07、`431f5d08` ch08–ch13），**每条我都回查原文后才动手**。共报 30 条，复核后**全部属实、全部修完**（脚本 `notes/books/non-fiction/fix_d1.py` / `fix_d2.py`，用后已 `rm`；保护式 `s.count(old) != 1` 即报 MISS）。

### d1. ch01–ch07（子代理 `82b53c37`）

| # | md | 缺陷 | 原文证据 |
| --- | --- | --- | --- |
| 1 | `ch01 Beginnings.md:97` | 说引语"无主谓"，实为自带 `I turned` | `text/ch01_beginnings.txt` 引语本身含主谓 |
| 2 | `ch01 Beginnings.md:100` | 「三个词」实为九词 | 同上 |
| 3 | `ch02 Scar Tissue.md:26` | 「白人男子抱着白人女子」 | `ch02:144` 抱的是**棕肤**男子与白人女子 |
| 4 | `ch02 Scar Tissue.md:85` | 被钉在原地的写成持刀人 | `ch02:92` `Like the narrator, I was fixed to the spot.` ⇒ 是作者本人 |
| 5 | `ch02 Scar Tissue.md:74` | 「倒装」 | 实为正常语序 |
| 6 | `ch03 Teaching the N-Word.md:24` | 全班「被勒住脖子」 | `ch03:234` 说的是 Colin 一人，其余学生是 cringing |
| 7 | `ch03 Teaching the N-Word.md:37` | 街头喊叫在 1994 年 | `ch03:338`；`ch03:177/:332` SEPTEMBER **2004** |
| 8 | `ch04 Interstates.md:26` / `:80` | 写成"黑人球星""黑白混贴" | `ch04:105` 两张海报都是白人（Leif Garrett + Björn Borg）；黑人偶像 El DeBarge / Jim Rice 不在墙上 |
| 9 | `ch04 Interstates.md:53` | 主谓语拆反 | `ch04:56` 主语是 `the difference`、`lies` 是谓语 |
| 10 | `ch04 Interstates.md:120` | 「圣诞夜」 | 原文 `Christmas Eve morning` ⇒ 圣诞夜**早晨** |
| 11 | `ch05 Mother on Earth.md:26` | 「朋友说」 | `ch05:41` 说话人是访谈里的知名女演员 |
| 12 | `ch05 Mother on Earth.md:64` | `interest` 重复三次 | 实为两次 |
| 13 | `ch05 Mother on Earth.md:72` | 「第一章/第四章」 | `grep -c selfish` ch01–ch04 = 0 ⇒ 应为第 1 节/第 4 节 |
| 14 | `ch05 Mother on Earth.md:96` | `even` 取"偶数" | 此处取"平稳的" |
| 15 | `ch05 Mother on Earth.md:105` | 「十一个词」 | 本句不到十个词（Q1 才是 11 词） |
| 16 | `ch06 Black Is the Body.md:27` | 「十二岁的女儿」 | `ch06:57` 是三年级同学；`ch06:43` 的 twelve 是 months |
| 17 | `ch06 Black Is the Body.md:54` / `:86` | `explained` 判为现在时，且凭空引入 `said` | 实为一般过去时，原文无 `said` |
| 18 | `ch07 Skin.md:112` | 「只有一个动词 say」 | 实有 encounter / is / say / see 四动词，被否定的是 `afraid` |

### d2. ch08–ch13（子代理 `431f5d08`）

| # | md | 缺陷 | 原文证据 |
| --- | --- | --- | --- |
| 19 | `ch09 Her Glory.md:11` | 段组 13 | `grep -c "^—\+$" text/ch09_her_glory.txt` = **9**；epub `<hr>` 同 9 |
| 20 | `ch10 Motherland.md:27` | 「同时向两边撒谎」 | `ch10:86` `I tell the agency the truth… and I lie to Helen` ⇒ 只对海伦撒谎（连带改 `:34` 论证脉络、`:38` 可质疑处） |
| 21 | `ch10 Motherland.md:28` | 日期区间安给机构 | `ch10:181` `She gave us a range` ⇒ 是海伦给的，机构只是 `agreed` |
| 22 | `ch10 Motherland.md:118` / `:120` | 「三个并列现在分词 rushing、assuaging、circulating」 | `ch10:384` `rush` 是**限定动词**，只有 assuaging / circulating 两个现在分词 |
| 23 | `ch11 Going Home.md:12` | 外婆「1994 年去世」 | `grep -c 1994 text/ch11_going_home.txt` = **0**；且与 `ch11:241`「1919 年生」+「九十四岁」不相容 ⇒ 删年份 |
| 24 | `ch11 Going Home.md:40` | 「一共五个孩子」 | `ch11:394` 朱莉娅之后又两个女儿 + `ch11:241` 母亲是长女 + `ch11:94` 母亲的三个姐妹 ⇒ **4 个** |
| 25 | `ch11 Going Home.md:80` | 「第二句的主句又成为第三句的条件」 | 引语只有两句，无第三句（同章 `:82` 的说法正确，属行间笔误） |
| 26 | `ch11 Going Home.md:114` | 「两个 here」 | 引语内只有 1 个 here |
| 27 | `ch12 People Like Me.md:11` | 段组 11 | `grep -c "^—\+$" text/ch12_people_like_me.txt` = **8**；epub `<hr>` 同 8 |
| 28 | `ch12 People Like Me.md:83` | 「她的眼睛像审讯灯」 | `ch12:80` `his eyes behind his glasses beaming like interrogation lamps` ⇒ 是**咖啡店老板**的眼睛 |
| 29 | `ch13 Epilogue My Turn.md:11` | 段组 5 | `grep -c "^—\+$" text/ch13_epilogue_my_turn.txt` = **2**；epub `<hr>` 同 2 |
| 30 | `ch13 Epilogue My Turn.md:91` | 「找到『药膏』之前先引鲍德温」 | `ch13:22` salve 先出、`:25` 鲍德温引文后出 ⇒ 顺序相反 |

**段组数两条口径说明**：ch10=14/14、ch11=16/16 与笔记同口径吻合，故 ch09/ch12/ch13 的 9/8/2 判定为笔记错，不是口径分歧。

**子代理判为不确定、我复核后仍改的 3 条**：ch10:28（海伦 vs 机构，低置信但原文明确）、ch11:80（第三句，属描述瑕疵但与 `:82` 自相矛盾）、段组数三条（双口径确认）。

**子代理核过未报、我复核后确认无缺陷的 2 条**：
- ch09 证据链「编发带来的成就感与背痛」——`ch09:47` `I complained proudly about the way my back ached after hours of bending over Isabella's head.` ⇒ **有出处，不报正确**。
- ch10:105「紧跟着的『我站直了身子』」——`ch10:201` 顺序为烈日句 → `I stand up straight.` → 不躲烈日；「紧跟着」方向其实对（站直在决定之后），但为免歧义改为「随即写下的」。

---

## e. 总览层事实核对

子代理 `2a92f772`（首次失败无输出，`send_message` 续跑后返回 16 条）。脚本逐字核对结果：**章节归属 28/28 全对、呼应关系 0 错** ⇒ 总览里 `(chNN)` 标注本来就全对，无需补标。16 条全部复核属实并修完（脚本 `notes/books/non-fiction/fix_e.py` / `fix_e2.py` / `fix_e3.py`，已 `rm`）。

| # | 位置 | 缺陷 | 证据 |
| --- | --- | --- | --- |
| 1 | `00_概述.md:10`、`00_情感节点.md:10`、`00_金句精选.md:13` | **遇刺段六错**：1995 年／感恩节前／陌生女人／刺伤背部／离脊梁两英寸／无目击无逮捕／第 19 版 | `ch02:52` `On the night of August 7, 1994… Koffee? on Audubon Street`；`ch01:29` `The man who stabbed me was white`；`ch02:202` `stabbed in the gut`；`ch02:219` Daniel Silva 认罪纵火；`ch02:223` 收治于 Connecticut Valley Hospital；`ch02:41` 约 10 人在场；`ch02:20/:45` 《New Haven Register》1994-08-08。全书 `two inches` 仅 `ch10:243`（推婴儿车）；`spine` 仅 `ch03:647`（书脊）与 `ch10:127`（脊柱伤）；`Thanksgiving`/`November` 在 ch01–ch02 **0 命中** |
| 2 | `00_金句精选.md:85`、`00_情感节点.md:30` | ch04「两只手」写成"八小时车程开回纳什维尔" | `ch04:337` 母亲圣诞夜早晨去世 → `ch04:343` `John's right hand in mine, and his left one… on the wheel`（去机场）；八小时车程是 `ch04:67` Nashville→Hazlehurst，方向相反、非此幕 |
| 3 | `00_金句精选.md:157`、`00_情感节点.md:40` | 卡伦的教子写成"她丈夫" | `ch08:22` `We are talking about Len, her godson… Karen is white; Len is black.` |
| 4 | `00_金句精选.md:166` | "就叫它爱吧"对象写成埃丝黛尔 | `ch08:87` Estelle 是黑人；`ch08:51` `“You're my only black friend,” Loree told me.` ⇒ white friend 指 **Loree** |
| 5 | `00_金句精选.md:184`、`00_概述.md:26` | 美容院对象写成伊莎贝拉 | `ch09:87` `Giulia was five years old… her appointment at a beauty shop`；`ch09:90` `I bowed my head. Giulia and I left the store.` |
| 6 | `00_金句精选.md:197` / `:202` | 机场问话人写成"服装店店主" | `ch10:352-368`：店主 `smiles in greeting and then continues her conversation`；问 `"Your daughter?"` 的是 **the friend**；`ch10:376` `"You're very good," the shopkeeper concludes.` |
| 7 | `00_金句精选.md:211` | "他肯定是黑人"写成读到马里兰枪击案新闻 | `ch11:47`：凶手母亲说 `He was sweet and gentle`；`"He had to be black," my mother would say` 是作者母亲的**多年口头禅**；本案 `there is none`（未提种族） |
| 8 | `00_概述.md:12` | 「打磨了三十年」 | `ch02:9` 只说 `telling this story for years`；全书 `thirty` 在 ch01–ch02 **0 命中** ⇒ 改"讲了多年" |
| 9 | `00_概述.md:22` | ch07「课堂上没有一个人敢说出自己看见了什么」 | `ch07:257` `a generation afraid to say what they see` ⇒ 改"这一代学生不敢说出自己看见的东西" |
| 10 | `00_金句精选.md:132` | 呼应 ch03「没有一个人敢说出自己看见了什么」（**我自查追加**） | `ch03:208` `no one in the class will say "nigger"` ⇒ 改"没有一个人愿意说出那个词" |
| 11 | `00_概述.md:58` | "上帝的旨意"标在 ch12 | 实际 `ch11:381` `It was God's will, my father says…`（冰暴、航班取消）⇒ 改 ch11 |
| 12 | `00_概述.md:50` | 母亲克拉拉·琼「把衣服扔掉、把诗烧掉」 | `ch11:248` 是**曾外婆坦皮妈妈**扔掉**外婆多西**的衣物与诗 ⇒ 母亲弧光只留「"好头发"从不让女儿碰」（`ch09:115`） |

**已核验通过（无缺陷）**：Mama Tempie＝母亲的祖母（`ch13:12`）、Dotsie＝祖母（`ch11:284`）、Giulia/Isabella 埃塞俄比亚双胞胎（`ch10:9`）、生母已故（`ch05:172`）、Larry＝Dr. H. Lawrence McCrorey 1966 北上（`ch12:179`）、Curtiss Reid Jr.（`ch12:148`）、Ellie「家是长久」（`ch12:9`）、"七年才明白"（`ch01:12` `It took seven more years`）、"拿掉了血、疼痛、愤怒"（`ch02:209`）。

---

## 工具盲区（本轮审查最有价值的产出）

| # | 盲区 | 表现 | 建议 |
| --- | --- | --- | --- |
| 1 | **`check_vocab` 与 `check_struct_indep` 对词汇三档 H3 的口径打架，且都不报冲突** | `check_vocab.py:90` `TIER_PAT` 无 H3 时 `tier=None` ⇒ 分档检测跳过、WARN 0；`check_struct_indep.py:32/226-228` 却报 39 条缺陷 | 两个脚本取同一份「必备结构」判据；或至少让 check_vocab 在「无 H3 但有 ` |
| 2 | **概览里的计数断言（段组数、年份、子女数）不在任何门禁内** | ch09/ch12/ch13 段组数、ch11「1994 年去世」「五个孩子」全部靠 d 步语义二审抓出 | 无解（散文断言结构上无法机械验），只能保留 d 步人审；但可考虑 `audit_numbers` 扩到年份类断言 |
| 3 | **说话人/动作主体错配不在任何门禁内** | ch12:83「她的眼睛」实为老板的眼睛、ch02:85 被钉住的是作者本人，均只有语义二审能抓 | 同上 |
| 4 | **`audit_numbers` 对中文计数短语的误判噪声** | 写"第一个/第二个""一个词"会被判「非英文，不判」或「分句口径不统一」 | 降噪改法：把"第一个/第二个"改成"前者/后者"、删掉"一个词" |
| 5 | **`gate.sh` 必须用 `bash scripts/gate.sh`** | 用 `python3 scripts/gate.sh` 报 `SyntaxError: unmatched ')'` | 已固化到流程笔记 |
| 6 | **md 正文用半角双引号 `"…"`**，写 python 替换脚本用弯引号会整批 MISS | 本轮 e 步第一批 6 条因此全 MISS | 已固化：写替换脚本前先 `grep` 实测引号形态 |

---

## 复验

整改后全家复跑（原件 `.memory/raw-gates/black-is-the-body-by-emily-bernard/2026-10-02-review-final-gates.txt`，2026-10-02 21:04 UTC）：

```
① verify_quotes --full    166/166（100%）；完全干净文件 15/15；--full 整串取证 0
② check_vocab             词条行 839 ｜ FAIL 0 ｜ WARN 0
③ check_entities          0 个文件存在未知实体
④ corruption_scan         FAIL 0 处 ｜ 报告 0 处
⑤ sweep_full              ✅ 128 ｜ 跨章 0 ｜ 拼接 0 ｜ 查无 0
⑥ audit_structure         16 md / 176 块 ｜ ❌ 0 ｜ ⚠️ 0 ｜ 🔀 0
⑦ check_struct_indep      13 个 md，缺陷 0 处
⑧ check_overview_full     A 命中 38 ｜ 🔶 0 ｜ ❌ 查无 0 ｜ 短引语列出 9
⑨ verify_overview_quotes  38/38 可核实（100%）；干净文件 2/2
⑩ check_anchor            凭空造词 0 ｜ 松散关键词 0
⑪ check_crossref          0 对，报警 0
⑫ sweep_analysis_inline   ✅ 逐字 1249 ｜ 跨章 0 ｜ 🔶 拼接 1 ｜ 🟠 0 ｜ ❌ 0
⑬ audit_numbers           6 条 ⚪ 年龄待人核（ch09 八十九岁×3 / 五岁、ch11 九十四岁 / 十四岁）
⑭ bash scripts/gate.sh    EXIT=0 ｜ ⑰ 引语块结构 130 行全绿 ｜ ⑱ 覆盖度问题 1 处（ch01 假红）
```

**两条非阻断项的处置**：
- `sweep_analysis_inline` 与 ⑱ 的同一条 🔶：`ch01 Beginnings.md:50` `not only... but also...` —— 是**语法术语**（中文句子结构说明里举的关联词），非引语，按 `docs/新书启动模板.md:133` 禁令 3「语法术语豁免」判**假红不改**。
- `audit_numbers` 6 条 ⚪：全部为年龄类断言，已逐条比对源文（ch09 八十九岁外婆 ×3、五岁朱莉娅；ch11 九十四岁外婆、十四岁）⇒ **与原文一致，放行**。

---

## 缺陷总计

| 类别 | 阻断型 | 提示型 | 假红（不计入） |
| --- | --- | --- | --- |
| c 步结构（词汇三档 H3 漏做） | 39 | — | 0 |
| d1 ch01–ch07 | 18 | — | 0 |
| d2 ch08–ch13 | 12 | — | 2（子代理核过未报，复核确认无缺陷） |
| e 步总览层 | 16 | — | 0 |
| **合计** | **85** | **0** | **2** |

85 条阻断型全部改完并回查原文；2 条假红保持原样并记录理由。

---

## 同会话审查的已知局限（`AGENTS.md:242` 要求仅在结论部分标注）

1. **作者即审查者**：精读 md 与原文由同一会话写出（本会话完成 ch01–ch13 全部精读 + 总览三篇）。d 步能证明「这句与原文不符」，不能证明「我当初为什么会这么写」——意图无法与错误分离。
2. **d 步用了两个子代理，但它们与我在同一会话上下文里**（`subagent_fork` 继承本会话已完成的轮次），不是完全冷启动的第三方。对冲手段是「子代理结论必须逐条回查原文」（本轮 30 条 + e 步 16 条全部回查），但无法排除同源偏差。
3. **e 步不是穷举**：子代理按「高风险模式定向扫」（时间词、计数词、亲属称谓、极值断言、专名、章号区间），总览三篇里可能仍有未被定向模式命中的失实。已穷举覆盖的是全部 `（chNN）` 标注引语（28/28）。
4. **audit_numbers 的 6 条年龄断言是人工核的**，不是脚本核的——脚本只负责「列出待人核」。
5. **本轮未做投毒自证**（`docs/新书启动模板.md:710` 建议）：d/e 步未注入已知缺陷验证子代理能抓到，因此「子代理零报警的章节」（ch08 报 0 条）只能说「它没找到」，不能说「确实没有」。
