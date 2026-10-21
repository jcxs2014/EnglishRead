# 4-verdict.md · ch04 判定表

- 书：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell`｜章：`ch04 digbys studio is searched.md`
- 唯一权威源：`text/ch04_4.txt`（4178 字符 / 98 行）
- 审查员：独立审查员（只负责第 4 章）｜**未改书目录任何 md，未 git add/commit，落盘仅本目录**
- 配套：`1-suread.json`（R1，先于读 md 完成）· `2-machine.json`（R2，`chapter.sh --json` 退出码 0）· `3-diff.md`（R3）· `4-correspondence.md`（R4）

---

## 0. 覆盖声明

- **本次实际人判范围：仅 ch04。** 本书其余 53 章**未跑**机器层，也**未人判**——按 `docs/rules/审查表.md` §0.5「没跑的章要写『只有机器层』，不许写成『通过』」：**其他章＝未查（跳过）**，不在本报告的通过/不通过统计内。
- ch04 内部：R1 素读（全文 98 行）· R2 机器层（退出码 0）· R3 三张单子（全文对账）· R4 六块逐块 · R5 判定 32 条断言——**全部做完，无未核项**。
- 本章专属判据（搜查死者住所与书房／房间本身如何讲述这个人／旧沙发／登在报纸上的交友广告／人物弧线抓孤独怎么被写出来）——见 `3-diff.md` §四，逐项核过。

---

## 1. 四组数（逐字 / 对应 / 形态 / 断言）

### 组一 · 逐字（verbatim）
| 项 | 数 | 说明 |
|---|---|---|
| 引语块 | 6 | md 有 6 块，`2-machine.json` 块清单同 |
| 引语段（segments） | 6 | **无 `…` 拼接、无跨话轮缝接**：6 块各 1 段，全部连续逐字 |
| 逐字命中 | **6/6**，各命中原文 **1 次** | 机器 `segment_miss=0`；人工 Python 计数复核同为 6/6（每段 count=1） |
| 词条例句 | 32 行（29 词条 + 3 表头行） | 人工 Python 逐条 `txt.count(ex)`：**29/29 真实词条例句均为原文精确子串且命中 1 次** |
| `check_vocab.py`（全书口径） | **FAIL(0)**，ch04 无 WARN | 与人工逐条复核互为独立两路 |
| **逐字组缺陷** | **0** | — |

### 组二 · 对应（correspondence，6 块逐块人判）
| 判定 | 块数 | 明细 |
|---|---|---|
| ✅ 对应成立 | 4 | 块 1、块 3、块 4、块 5 |
| ⚠️ 对应成立但夹带缺陷 | 1 | 块 2（含 1 条阻断级位置编造 B1） |
| ⚠️ 引语选短（分析主要落在引语外） | 1 | 块 6（收尾句 `A memento mori now.` 在引语外，见 `text/ch04_4.txt:98`） |
| ❌ 不对应（讲全书主旨/作者生平） | **0** | — |
| ❌ 纯密度不足（只复述字面无「为什么」） | **0** | 6 块「为什么这样写」均密度达标（机器 `cjk_low=0`；最低块 6「为什么这样写」CJK 72 字） |
| 施事/归属反转（R4 固定追问，核 12 处） | **0** | 见 `4-correspondence.md` 逐块「主语/受事核对」 |
| **对应组缺陷** | **2 块带问题**（块 2、块 6），**0 块不对应** | — |

### 组三 · 形态（form）
| 项 | 本章实测 | 本书众数 / profile | 结论 |
|---|---|---|---|
| H1 | `4. Digby Combe-Watson’s Studio, Dollis Hill` | `h1_shape_ok=true`；且与 `text/ch04_4.txt:17` 的章内标题逐字一致 | ✅ 一致 |
| 导航项名与项数 | 5 项：**一句话概括 / 视角 / 线索结构 / 人物弧线 / 叙事手法** | 全书 `nav_counts=[5]`（每章均 5），`nav_missing=[]` | ✅ 无偏离 |
| 子项集 | `{中文理解, 关键词, 为什么这样写, 读者视角提示}` | profile `mystery-thriller` 的 `profile_subitems` **完全相同**；`profile_optional` 的「句子结构」为可选、未用 | ✅ 无偏离（可选项未用不计偏离） |
| 块数 | 6 | 本书众数中位 **7.0**，范围 **5–10** | ✅ 落在众数区间内，**无偏离，故不需写理由** |
| 引语块数 vs profile | 6 | 在 [5,10] 内 | ✅ |
| **形态组缺陷** | **0** | — |

### 组四 · 断言（assertions）
| 档位 | 条数 |
|---|---|
| **阻断** | **2** |
| 提示 | 11 |
| 假红 | 0 |
| 跳过（未查） | 0（ch04 内部） |
| 已判断言总数 | **32** |

**四组数汇总：逐字 0 缺陷（6/6 命中）· 对应 2 块带问题、0 块不对应 · 形态 0 偏离 · 断言 32 条中阻断 2 / 提示 11 / 假红 0。**

---

## 2. 判定表（断言 | 证据 | 结论 | 档位）

> 证据一律带 `text/<文件>:<行>` 与该处**原文逐字**；md 侧带 `ch04 digbys studio is searched.md:<行>`。

| # | 断言 | 证据（章:区间） | 结论 | 档位 |
|---|---|---|---|---|
| 1 | 「信在抽屉里」（md:11「抽屉里那一叠通信」、md:13「抽屉里的信件」、md:109「抽屉里的旧信」） | `text/ch04_4.txt:56`：「Caius turned to a half-height bookcase near the bed. **A wooden box with a rose carved into the side** had caught his eye. He opened it. It contained a month’s worth of frequent correspondence.」另 `text/ch04_4.txt:89`：「Caius took the other letters out of **the box**.」 | 容器错置：原文是刻玫瑰的**木盒**，全章唯一抽屉是 `Digby’s sock drawer`（`:26`） | **阻断** |
| 2 | 「那只标本被安置在这间极简小屋的抽屉里 / 抽屉一拉开就撞见一只标本」（md:30） | `text/ch04_4.txt:26`：「‘Makes sense,’ Caius said, **opening Digby’s sock drawer**. ‘If I had to see that cross-eyed taxidermy kangaroo every day I’d want to live in an immaculate little minimalist box too. …’」——原文未交代标本位置（`grep -nE 'kangaroo\|taxidermy' text/ch04_4.txt` → 仅 `:26`，exit=0） | 位置凭空：md 有、原文无 | **阻断** |
| 3 | 「把公共收藏品与私人洁癖混着过日子」「私人生活里仍然装着博物馆的碎片」（md:30、md:31） | `text/ch04_4.txt:26` 原文只写 `cross-eyed taxidermy kangaroo`；`grep -nE 'museum\|museums' text/ch04_4.txt` → 仅 `:65`「does it at the museum」（约会地点），exit=0 | 标本来源（馆藏）无据 | 提示 |
| 4 | 「抽屉上摆着一台**不能联网**的老电视」（md:14） | `text/ch04_4.txt:38`：「There’s an old TV that wouldn’t be able to **stream** on top of the drawers and a radio in the kitchenette but no laptop.」 | 「不能串流」被改写成「不能联网」，另一事实断言 | 提示 |
| 5 | 「交友广告**剪报**」「需要**登报**找人」（md:11、md:13、md:14、md:49） | `text/ch04_4.txt:89`：「**A cut-out from a magazine was at the back.** … He posted a lonely-hearts ad.」；md 自己词表 `magazine | 杂志`（md:100） | 媒介是**杂志**，「剪报/登报」与原文及本章词表不一致；**md 未出现「报纸」二字**（`grep -nE '报纸\|newspaper' md` → 命中 0，exit=1） | 提示 |
| 6 | 「搜查队…翻找线索」（md:11）与「两名警探…」（md:109）并存 | `text/ch04_4.txt:23`–`:98` 全章对话仅 Matt、Caius 二人 | 人数夸大 + 文件内不一致 | 提示 |
| 7 | 「独居**老**学者」（md:11、md:109） | `text/ch04_4.txt:89`：「…37, good-ish looking…」 | 与章内自引的 37 岁相冲；「学者」仅为推衍 | 提示 |
| 8 | 「连交友广告都**自己剪下来**收着」（md:14） | `text/ch04_4.txt:89`：「A cut-out from a magazine was at the back.」＋`:95`「‘The poor guy had kept the ad. …’」 | 原文未写由谁剪下 | 提示 |
| 9 | 「作者让嫌疑沿着一条采购链去**找凶手**，把搜查从房间推回到**社会关系**上」（md:44） | `text/ch04_4.txt:68`：「‘**Accidental contamination?**’ Matt asked … ‘What if the hemlock leaves made it into the bagged salad he bought from the greengrocer’s by mistake …’」 | 假说性质被改写：Matt 提的是**意外**（无凶手），收据指向供应链非社会关系 | 提示 |
| 10 | 「紧接着那句把「A memento of their romance」翻成「A memento mori now」」（md:58） | `text/ch04_4.txt:95`：「‘The poor guy had kept the ad. **A memento of their romance.**’」；`text/ch04_4.txt:98`：「‘**A memento mori now.**’」（两句相邻，第三句在引语外） | 并列两句被写成替换关系；并牵出「引语选短」 | 提示 |
| 11 | 「他**只看得见其中一半**」（md:21） | `text/ch04_4.txt:20`：「It now had a view of a **halved garden**.」 | 原文说花园被一分为二，未说他只能看见一半 | 提示 |
| 12 | 明信片线索（「the Institute」「27th」「Mum x.」）缺失 | `text/ch04_4.txt:56`：「Inspecting a postcard of a Goan beach … ‘Darling, meant to write when in Blighty but had mad rush for visa. **Let’s talk about the Institute when I get back on 27th. Mum x.**’」 | 全章唯一含机构名与日期的物件缺席于分析层（md:11/13 的物证清单未列） | 提示 |
| 13 | Isolde 动机三选项（已婚/宵禁）与 Willow 一线缺失 | `text/ch04_4.txt:74`：「‘Isolde could be married? …’」；`:77`：「‘Or maybe she’s broken her curfew? **He hit on Willow the intern; she’s twenty, twenty-one. Maybe nineteen when she started.**’」；`:71`：「…this letter feels quite lovey-dovey. … You’d think they’d have enough sense to at least call an ambulance.」 | md:13 只压成「毒芹误入沙拉，还是约会对象事后逃走」二选一，Caius 的反驳逻辑丢失 | 提示 |
| 14 | 块 6 分析的力道落在引语外的收尾句 | `text/ch04_4.txt:98`：「‘A memento mori now.’」不在 md:54 的引语范围内 | 引语选短（R4 判据：讲的是引语之外的上下文） | 提示 |
| 15 | 宅邸被分隔、书房原是餐厅、花园一分为二（md:21/23） | `text/ch04_4.txt:20`：「Digby’s place had once been a substantial Edwardian family home but had since been partitioned off into separate dwellings. His studio would likely have been the dining room. It now had a view of a halved garden.」 | 逐字对得上 | 通过（非缺陷） |
| 16 | 蜂蜡味、每周牙刷擦（md:28） | `text/ch04_4.txt:26`：「It smells like beeswax. I bet he polished the place with a toothbrush every week.」 | 逐字对得上 | 通过 |
| 17 | Willow 转述「无 email / 都用邮寄」（md:35） | `text/ch04_4.txt:32`：「‘Willow said he doesn’t have an email. Did everything by post.’」 | 说话人与内容都对 | 通过 |
| 18 | 墙画评语「现代·抽象·1960 年代？」（md:35） | `text/ch04_4.txt:32`：「‘Modern. Abstract. 1960s? Antibiotics but no mobile phone.’」 | 逐字对得上（`1960s?` 的疑问语气也保留了） | 通过 |
| 19 | 毒芹叶混进袋装沙拉 / 收据写 organic / 店家加了野地植物（md:42） | `text/ch04_4.txt:68`：「What if the hemlock leaves made it into the bagged salad he bought from the greengrocer’s by mistake. It says organic on the receipt. Maybe they added a bit of the hedgerow not realising.」 | 施事/受事方向全对 | 通过 |
| 20 | 广告四要素「37 岁 / 还算过得去 / 有时挺好笑 / 文化爱好者」（md:49） | `text/ch04_4.txt:89`：「“North London romantic seeks connection with fellow old soul. 37, good-ish looking, sometimes amusing, culture vulture.”」 | `37` 的归属（Digby 的年龄）与 `He posted` 的施事都正确 | 通过 |
| 21 | 收据来自车站旁蔬果店（md:13、md:44） | `text/ch04_4.txt:35`：「He found a receipt for the greengrocer’s by the station dated the day before he died.」 | 逐字对得上 | 通过 |
| 22 | 「打字机」列为物证（md:13） | `text/ch04_4.txt:29`：「Matt said, taking the case off the typewriter perched on the edge of the table.」 | 打字机确在房中 | 通过 |
| 23 | 「小厨房里一台收音机」（md:14） | `text/ch04_4.txt:38`：「…and a radio in the kitchenette but no laptop.」 | 逐字对得上 | 通过 |
| 24 | Isolde 是通信对象 / 约会对象（md:13、md:51） | `text/ch04_4.txt:59`：「‘“Dearest Darling Digby,” … “Yours eternally, Isolde.”’」；`:71`：「‘Isolde, his date, …’」 | 逐字对得上 | 通过 |
| 25 | 「只有一个邮政信箱的地址」（md:13） | `text/ch04_4.txt:83`：「‘It’s a PO Box,’ Caius said.」 | 逐字对得上 | 通过 |
| 26 | 结尾把「纪念品」改口成「死亡纪念物」（md:15、md:109） | `text/ch04_4.txt:95`、`:98`（见 #10） | 逐字对得上 | 通过 |
| 27 | 6 条引语全部逐字（md 引语块 1–6） | `2-machine.json`：`segment_miss=0`；人工复核每段 count=1 | 机器 + 人工两路一致 | 通过 |
| 28 | 29 条词条例句均为本章原句 | 人工 Python `txt.count(ex)`：29/29 = 1；`check_vocab.py` FAIL(0) | 两路一致 | 通过 |
| 29 | H1 / 导航项 / 子项集 / 块数（md:7、md:9–15、md:17–59） | `2-machine.json` form 段：`h1_shape_ok=true`、`nav_counts=[5]`、`nav_missing=[]`、`subitems_modal` = profile 子项集、`blocks=6` ∈ 众数区间 [5,10]（中位 7.0） | 无偏离 | 通过 |
| 30 | 本章专属判据：「一件旧沙发」 | `/usr/bin/grep -nE '沙发\|sofa\|couch' text/ch04_4.txt` → 命中 0，exit=1；同命令对 md → 命中 0，exit=1 | 原文与 md **双方均无沙发** ⇒ 无缺陷（记录以防后续误加） | 通过（已核实） |
| 31 | 本章专属判据：「登在**报纸**上的交友广告」 | `/usr/bin/grep -nE '报纸\|newspaper' md` → 命中 0，exit=1；`/usr/bin/grep -nE 'magazine\|newspaper\|journal' text/ch04_4.txt` → 命中 1（`:89`，magazine），exit=0 | 原文媒介是**杂志**（非报纸）；md 也未写「报纸」 ⇒ 无编造，仅措辞提示（见 #5） | 通过（已核实） |
| 32 | 本章专属判据：「人物弧线抓孤独怎么被写出来」（md:14） | 孤独的物证在原文俱在：`text/ch04_4.txt:32`（无 email 只邮寄）、`:38`（老电视/收音机/无 laptop）、`:83`（PO Box）、`:86`（not like he’s on the apps）、`:95`（kept the ad） | 主题抓得准，弧线成立；措辞问题另记 #4/#5/#8 | 通过（已核实） |

---

## 3. R5-补 · 零命中类断言的自证（全部附命令 / 输出 / 退出码）

```
$ cd notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell
$ /usr/bin/grep -nE '沙发|sofa|couch' "ch04 digbys studio is searched.md"  → 命中 0；exit=1
$ /usr/bin/grep -nE '沙发|sofa|couch' text/ch04_4.txt                   → 命中 0；exit=1
$ /usr/bin/grep -nE '报纸|newspaper' "ch04 digbys studio is searched.md" → 命中 0；exit=1
$ /usr/bin/grep -nE '报纸|newspaper' text/ch04_4.txt                    → 命中 0；exit=1
$ /usr/bin/grep -nE 'kangaroo|taxidermy' text/ch04_4.txt                → 命中 1（:26）；exit=0
$ /usr/bin/grep -nE 'museum|museums' text/ch04_4.txt                    → 命中 1（:65）；exit=0
$ /usr/bin/grep -nE 'drawer|box|bookcase' text/ch04_4.txt               → 命中 5（:26 :29 :38 :56 :89）；exit=0
$ /usr/bin/grep -noE '[0-9]+ ?[a-z]*|[a-z]+ ?[0-9]+' text/ch04_4.txt    → :32 1960s / :56 on 27 / :89 37；exit=0
$ /usr/bin/grep -nE '全书|查无|零命中|从没|从未|没有出现' md           → 命中 0；exit=1（md 无此类断言）
```
工具口径：显式文件路径 + `/usr/bin/grep`（非 `git grep`、非 rg 默认 ignore 规则）；交替匹配用 `-E`。**「旧沙发」「报纸」两处零命中均为原文侧实无，非工具口径问题。**

---

## 4. 已核实为正确（防误修，固定一节）

> 以下条目**读着像错**，回原文核对后成立；后续任何人不得以「读着不对」为由改动，除非给出反证。

1. **「37 岁」**（md:49）——原文 `text/ch04_4.txt:89`：「…37, good-ish looking, sometimes amusing, culture vulture.」广告是 Digby 的第一人称自述，`37` 指他本人年龄，成立。
2. **「他登了个交友广告」／「一则自登的交友广告」**（md:49、md:109）——原文同句：「He posted a lonely-hearts ad.」施事是 Digby，成立。
3. **「实习生 Willow 说他没有电子邮箱」**（md:35）——原文 `text/ch04_4.txt:32`：「Willow said he doesn’t have an email. Did everything by post.」说话人是 Willow、受事是 Digby；`text/ch04_4.txt:77` 的「Willow the intern」佐证「实习生」标签，非编造。
4. **「毒芹叶混进了他从果蔬店买回的袋装沙拉」**（md:42）——原文 `text/ch04_4.txt:68`：「What if the hemlock leaves made it into the bagged salad he bought from the greengrocer’s by mistake.」施事=hemlock leaves、受事=bagged salad、方向正确，**勿改为「收据混进毒芹」之类**。
5. **「马特把收据递给 Caius 看」**（md:42）——原文 `:68`：「Matt asked, showing Caius the receipt he’d found.」给出者/受领者方向正确。
6. **「收据上写着有机」**（md:42）——原文 `:68`：「It says organic on the receipt.」成立。
7. **「这家收据来自车站旁蔬果店」**（md:13、md:44）——原文 `:35`：「a receipt for the greengrocer’s by the station dated the day before he died.」成立。
8. **「小厨房里一台收音机」**（md:14）——原文 `:38`：「a radio in the kitchenette but no laptop.」成立。
9. **「只有一个邮政信箱的地址」**（md:13）——原文 `:83`：「‘It’s a PO Box,’ Caius said.」成立。
10. **「最终把纪念品改口成死亡纪念物」**（md:15、md:109、md:58）——原文 `:95`「A memento of their romance.」＋`:98`「A memento mori now.」成立（但**引语选短**另记于 #14、#10）。
11. **「斜着眼的动物标本」/「cross-eyed｜斜视的」**（md:28、md:82）——原文 `:26`「cross-eyed taxidermy kangaroo」，成立。
12. **「他把收藏的癖好带回了住处」**（md:30 前半）——原文 `:26`「If I had to see that cross-eyed taxidermy kangaroo every day」蕴含它每天可见、在他住处，成立；**仅后半「公共收藏品/博物馆碎片」不成立**（见 #3）。
13. **「墙面挂画『现代·抽象·1960 年代？』」**（md:35）——原文 `:32`「Modern. Abstract. 1960s?」，原文自带问号，md 保留问号，成立。
14. **「收尾的黑色玩笑把死者的私情压成一句冷笑话」**（md:15）——原文 `:95`→`:98` 的三句结构成立；**发言人不明**（`:98` 未署说话人），md 也未虚构说话人，成立。

---

## 5. 落盘状态说明（并发实例提示，第三方复核请先读这一节）

- 本目录**同时被两个实例写入**：我在 13:33–13:40 写入本套 5 个文件后，另一实例于 13:40 把当时已存在的 4 个文件移入 `prior-run/`，并于 13:41 写入它自己的 `1-suread.json` 与 `2-machine.json`（`2-machine.json` 两边**逐字节相同**，`diff -q` 已确认）。
- 现目录顶层是**我的完整一套**（1-suread / 2-machine / 3-diff / 4-correspondence / 4-verdict），我的原件同时保留在 `prior-run/`；对方实例的 `1-suread.json` 已另存为 `prior-run/peer-1-suread.json`（**未删除、未改写对方任何内容**）。
- 若本目录随后被另一实例覆盖，**本套完整原文在 `prior-run/`**（`1-suread.json`、`3-diff.md`、`4-correspondence.md` 均为原件；`4-verdict.md` 以本文档为准）。
- 本审查员**未改书目录任何 md、未 `git add`、未 `git commit`、未 push**；落盘范围严格限于 `.memory/raw-gates/a-fatal-legacy-by-charlotte-vassell/review/ch04/`。

---

## 6. 结论（可交付的一句话）

**ch04 机器层全绿（`chapter.sh` 退出码 0，6/6 引语逐字、形态零偏离），人判抓出 2 条阻断型（同源：把「抽屉」当通用容器——木盒里的通信被改写成抽屉里的通信、位置无凭的标本被写成在抽屉里），11 条提示型；四组数：逐字 0 缺陷 · 对应 2 块带问题（0 块不对应）· 形态 0 偏离 · 断言 32 条中阻断 2 / 提示 11 / 假红 0。**最要紧的一条是 #1（信件位置：原文木盒 → md 三处写抽屉，且两处落在导航层与一句话总结层）**，它直接动摇本章专属判据「房间本身如何讲述这个人」的读法。修复建议仅两处：把 md:11/13/109 的「抽屉里」改回「木盒/盒中」，把 md:30 的标本位置句删去或改为不指定位置的写法。
