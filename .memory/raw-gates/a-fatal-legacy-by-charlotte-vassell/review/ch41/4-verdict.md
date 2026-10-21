# 4-verdict.md · ch41 判定表（阻断 / 提示 / 假红 / 跳过）

> 审查范围：**仅 ch41**（作业方指定）。md＝`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch41 margot bourne is questioned.md`；
> 原文＝`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch41_41.txt`（唯一权威源，6221 字符）。
> **未审的其他章**（ch01–ch40、ch42–ch54）＝「只有机器层」（全书机械探针已跑，见 §三），**不写「通过」**。
> 本轮**未改动书目录任何 md，未 git add/commit**；只写 `.memory/raw-gates/a-fatal-legacy-by-charlotte-vassell/review/ch41/`。

---

## 一、四组数（逐字 / 对应 / 形态 / 断言）

### 1）逐字组
| 项 | 数 | 说明 |
|---|---|---|
| 引语块逐字 | **6 / 6** | `chapter.sh --json`（从 `text/` 重建再与 md 对账）：6 段全部 `ok: true`；`segment_miss: 0` |
| 引语逐字（第二实现） | **848 片段 / 0 MISS** | `python3 scripts/verify_fragments_indep.py "<书目录>"` → 「引语条数 780 ｜受检片段 848 ｜❌ MISS 0 ｜❌ 拼接未标省略号 0」；退出码 0（逐片段独立取证，防 `…` 缝合） |
| 词汇例句逐字 | **26 / 26** | 自写脚本读 `text/ch41_41.txt` 做子串计数：每条例句**恰好命中 1 次**，非 1 计数 = 0 |
| **逐字组结论** | **32 / 32 全对，缺陷 0** | 无「省略号只验首段」「跨章搬句」类问题 |

### 2）对应组（R4 逐块人判）
| 项 | 数 | 说明 |
|---|---|---|
| 块数 | 6 | md `:19/:26/:33/:40/:47/:54` |
| 对应（讲的就是这句引语） | **6 / 6** | 逐块见 `4-correspondence.md` |
| 不对应（讲全书主旨/作者生平） | **0** | — |
| 密度不足（只复述字面） | **0** | 6 块「为什么这样写」均给出「为什么」；机器 `cjk_low: 0`，中文占比 0.80–0.92 |
| 说话人错配 | **0** | 逐块核过：马特（块 1、2）／罗比（块 3）／玛戈特（块 4）／艾米（块 5、6）——**全部与原文一致**（艾米的话见 `text/ch41_41.txt:127`、`:145`、`:151`，md `:49`、`:56` 归属正确） |
| 施事／受事／归属写反 | **0** | 逐动词核主语与宾语；最易错的 `hid the fact **from** DC Noakes`（块 3）、`the deceased`/`his property`（块 3）、`she`＝玛戈特（块 2）**方向全对** |
| 引语外越界（引语选短） | **1** | 块 2：引语只取 `:44` 第一句，分析对象却主要是紧接的下一句（估价单）⇒ 提示级 |
| 断言越权（含阻断） | **1** | 块 5：「只可能是」＋章末句缺失 ⇒ 阻断（见 V1、V2） |
| **对应组结论** | **6/6 对应，0 错配，0 反转** | 缺陷 2 条（1 提示 + 1 阻断），均属边界/断言层，非对应层 |

### 3）形态组
| 项 | 本章 | 本书众数 / profile | 偏离 |
|---|---|---|---|
| H1 | `# 41. The Police Station` | H1 写法 `N.` ×54；本章小标题与原文 `text/ch41_41.txt:17`「The Police Station」逐字相符 | 无 |
| 导航项名 | 一句话概括 / 视角 / 线索结构 / 人物弧线 / 叙事手法 | 众数 5 项，**名与序全同** | 无 |
| 导航项数 | 5 | 众数 5（`bookform.py`：导航项（众数，5 项）） | 无 |
| 子项集 | 中文理解 / 关键词 / 为什么这样写 / 读者视角提示 | 众数 4 项＝profile（mystery-thriller）4 项；可选「句子结构」未用（可选，不算偏离） | 无 |
| 块数 | 6 | 众数中位 7.0，范围 5–10；profile 3–10 | 无（6 落在众数区间内） |
| 词汇表 | 26 条（7 / 10 / 9 三档） | 无众数可比 | 无（档位问题见 V10、V11、V12） |
| **形态组结论** | **偏离 0** | — | **无须写偏离理由** |

> 分部名红线：md **未出现任何分部名**（取证：E1，0 命中）⇒ 未违反「分部名只能用书里真名」；本章所属分部为 **SATURDAY**（书内真名，全书仅第一部叫 A FRIDAY IN MAY）。若要按全书惯例补标，只能写「分部「SATURDAY」」（见 V13，提示级）。

### 4）断言组
| 项 | 数 | 说明 |
|---|---|---|
| 本章共核断言 | **22** | 漏/编/错三单（3-diff.md）＋ 作业方四个待核点 ＋ 形态/逐字/对应各组结论 |
| **阻断** | **2** | V1（漏：章末句）、V2（错：单向化＋必要性过强） |
| 提示 | 11 | V3–V11、V13、V21 |
| 假红 | 1 | V12（工具口径，非本章缺陷） |
| 通过（md 写对） | 7 | V14–V20 |
| 跳过（未核） | 1 | V22 |
| **断言组结论** | **阻断 2 / 提示 11 / 假红 1 / 通过 7 / 跳过 1** | — |

---

## 二、判定表

| # | 断言 | 证据（章:区间） | 结论 | 档位 |
|---|---|---|---|---|
| V1 | 全章末句「凶手可能是她的读者之一」未进 md | 原文 `text/ch41_41.txt:154`（字符 6176–6220）＝ `‘So the killer could be one of her readers.’`；md 全章无对应（E3：0 命中，退出码 1）；md 最近处 `:11`「…只有源头者才可能写出的细节」、`:14`「…变成"伊索尔德自己就是源头"」、`:107` 一句话总结 | 关键转折缺失；md 以相反方向的单向结论收束 | **阻断** |
| V2 | md 把「艾米材料所示方向」写成必然结论 | 原文 `:145`（字符 5663–5894）只写「她写故事时用到了生活片段，包括所有被告诉过迪吉的剩余细节」，**未下**「源头＝伊索尔德」的结论；紧接着 `:154` 给的是「凶手可能是她的读者之一」。md `:11`「只有…才可能」、`:14`「伊索尔德自己就是源头」、`:51`「只可能是写出这些细节的人」 | 必要性（只可能/只有…才）强于原文，且方向单向化 | **阻断** |
| V3 | 导航「人物弧线」引号内「我记得这位警探」原文无 | md `:14`；原文 `:60`＝`‘Margot, please,’ she interrupted. She liked this policeman too. Less than the other one, he was a dish, but still.`（字符 1580–1614） | 引号内语句原文不存在；另「改口要律师」不准——她从未否认报过低价（`:66` ‘Yes, why?’／`:81`） | 提示 |
| V4 | 「用邮政信箱（PO Box）注册的公司」／「以邮政信箱注册」 | 原文 `:38`＝`‘Yes, on Companies House. Interestingly, the contact address is a PO Box.’`（字符 664–688）——邮政信箱是**联络地址**；md `:11`、`:107` 写成「注册」，而同一文件 `:13`「联络地址为邮政信箱的公司」是对的 | 属性挂错对象，文件内自相矛盾 | 提示 |
| V5 | 「又让现成的估价单把它坐实」 | 原文 `:44`（字符 1059–1234）——估价单＝房产中介**建议价**这个基准，报价数额始终是马特的**猜测**（`I'm guessing`） | 物证功能被放大成「证实猜测」 | 提示 |
| V6 | 块 2 分析对象越出引语 | 引语＝`:44` 第一句（字符 1122–1234）；md `:30`、`:31` 主要讲紧接的下一句（估价单） | 引语选短（轻度） | 提示 |
| V7 | 「顺手把警察称作『坏男人』」 | 原文 `:93`（字符 2824–3043）`the nasty men` 未指明对象 | 归属越权断言 | 提示 |
| V8 | 块 6「作者自己先打了个折扣」 | 原文 `:151`（字符 6085–6172）——`probably` 出自**艾米**之口；md `:56` 用「作者」（本书惯例＝小说作者），同块内又用「说话人」＝艾米 | 表述含混 | 提示 |
| V9 | 导航「视角」称「三段切换」但只枚举两组地点 | md `:12` vs md `:15`「两处星号分隔线…切成三场」（原文 `:52`、`:113` 两处 `* * *`，已核）；`:12` 只列「警局办公室里的问询」＋「案发室」 | 计数不齐 | 提示 |
| V10 | 词汇「anachronistic」释义含「反潮流的」 | 原文 `:32`（字符 414–486）`He was a character. He was purposefully anachronistic.`——指刻意用旧式做派 | 第二义非 anachronistic 义项 | 提示 |
| V11 | 词汇「deceased」收 ⭐⭐⭐ | 原文 `:90`；犯罪小说语境属常用正式词 | 档位略高 | 提示 |
| V12 | `check_vocab.py` 报本章 4 条「基础档疑含超纲词」（character / interview / attacking / online community） | 输出见 §三；同型在 ch26/33/34/39/46/50 命中；脚本 `--- FAIL (0) ---`，退出码 0 | **工具口径问题（全书同型）**，非本章缺陷 | **假红** |
| V13 | 本章未标注所属分部 | md 全文无「分部/SATURDAY/…」（E1：0 命中，退出码 1）；书内真名为 **SATURDAY**（唯一叫 A FRIDAY IN MAY 的是第一部） | 未违规，但与全书 26/54 章的标注惯例不齐；若补写只能用 SATURDAY | 提示 |
| V14 | 问询对象与身份说法 | 原文 `:38`（两名登记董事＝杰拉德与玛戈特·伯恩，住在隔壁）、`:44`（艾米已与 Mrs Bourne 接触过）、`:47`（罗比：把玛戈特叫来问话）、`:57`–`:66`（受询人自称「Margot, please」）；md `:11`、`:13`、`:21`、`:24` | **md 写对** | 通过 |
| V15 | 关于 Isolde 的资料的来源 | 原文 `:127`（Google 旧闻／Twitter／领英／东哈姆小学／Instagram 私密＋带数字用户名）、`:133`（用该用户名搜到粉丝小说站）、`:145`（上月自我介绍帖）；md `:13`、`:49`、`:52` 来源归属逐项对得上 | **md 写对**（且这些资料在原文属艾米查证线，不在玛戈特问询里，md 未混淆） | 通过 |
| V16 | 笔录里的公司/机构名与数字 | 原文本章**无任何公司名**（E4：museum/PCQV/collector 0 命中）；机构名仅 Companies House、DC Noakes、the Institute；数字「不到三分之一」(`:44`)、2011 (`:127`)、22nd volume (`:124`) 逐字相符；md 未编造公司名，**未把 PCQV 与唱片公司混为一谈**（本章 0 命中） | **md 写对** | 通过 |
| V17 | 「登记董事」这条线索的表述 | 原文 `:38` 登记董事修饰**公司**；md `:21`「这家公司的两名登记董事是杰拉德·伯恩先生和玛戈特·伯恩夫人」；md 全文 0 次「博物馆/Institute/研究所」（E2：0 命中，退出码 1） | **md 未把「博物馆的两位登记董事」这层改写带进来** | 通过 |
| V18 | 形态（H1/导航/子项/块数） | `bookform.py`：H1 写法 `N.`×54；导航众数 5 项同名同序；子项众数 4＝profile 4；块数众数中位 7、范围 5–10、profile 3–10 | **合规，偏离 0** | 通过 |
| V19 | 逐字（6 引语 + 26 词汇例句） | `2-machine.json`（6/6 `ok:true`）、`verify_fragments_indep`（848 片段 0 MISS）、自写例句计数（26/26 各命中 1 次） | **全对** | 通过 |
| V20 | 跨章断言「前面已经把迪吉写给『假伊索尔德』的信与邮政信箱挂上钩」（md `:23`） | `text/ch04_4.txt:83`「It's a PO Box.」、`text/ch07_7.txt:152`「Setting up a PO Box and corresponding with Digby by letter for weeks.」、`text/ch16_16.txt:259`「chase the Post Office. We need to find out about that PO Box.」、`text/ch25_25.txt:224`「delivering the letters to the PO Box」 | 断言**属实**（跨章已建立该线） | 通过 |
| V21 | 略去的次要素材 | 原文 `:127` 东哈姆小学／Instagram 私密／带数字用户名（凯厄斯受审时告知）、`:139` Waterplaygate（尼克松成人向系列）／Dramione＝Draco and Hermione／Fi 的评价 | 非关键转折，md 在「线索结构」`:13` 与「读者视角提示」`:52` 已概括到主线 | 提示（取舍，无须改） |
| V22 | md 中涉及**其他章节**的事实断言是否逐条核过 | 本轮只审 ch41，未逐条核 md 中所有跨章断言（除 V20 一条外） | 未核 | **跳过** |

---

## 三、机器层原始输出（供第三方复跑比对）

```
$ bash scripts/chapter.sh "notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch41 margot bourne is questioned" --json > 2-machine.json
  → 退出码 0；verdict "ok"；quotes 6/6 ok:true；blocks 6；cjk_low 0；keyword_bad 0；struct_bad 0；
    form.h1 "41. The Police Station"（h1_shape_ok true）；form.nav_count 5（nav_count_ok true）；
    form.subitems_modal [中文理解, 关键词, 为什么这样写, 读者视角提示]；form.blocks 6；
    form.block_median 7.0；form.block_range [5,10]；form.profile "mystery-thriller"；baseline "book"

$ python3 scripts/verify_fragments_indep.py "<书目录>"
  → 引语条数 780 ｜ 受检片段 848 ｜ ❌ MISS 0 ｜ ❌ 拼接未标省略号 0 ｜ 缺参照章 0；退出码 0

$ python3 scripts/check_vocab.py "<书目录>"
  → --- FAIL (0) ---（退出码 0）
    [WARN] ch41 [基础] 基础档疑含超纲词「character」「interview」「attacking」「online community」
           （同型另见 ch26/ch33/ch34/ch39/ch46/ch50 ⇒ 全书基线，非本章缺陷）

$ python3 scripts/bookform.py "<书目录>"
  → 已有章 md 54；H1 写法 {'N.': 54}；导航项（众数 5 项）一句话概括/视角/线索结构/人物弧线/叙事手法；
    子项集（众数 4 项）中文理解/关键词/为什么这样写/读者视角提示；每章块数中位 7.0，范围 5–10；
    profile mystery-thriller；退出码 0

$ python3 scripts/corruption_scan.py ".memory/raw-gates/a-fatal-legacy-by-charlotte-vassell/review/ch41"
  → FAIL 0 处（U+FFFD / 双句号）；退出码 0
    报告 2 处「占位崩坏 —— 词表行例句列为空或占位」：4-verdict.md:25 / :55，
    实为本报告自己的统计表末格写成「—」被启发式误判，与被审 md 无关 ⇒ 假红，不改。
```

---

## 四、已核实为正确（防误修，护栏条目）

> 以下写法**读着像错、回原文核对后成立**，后续任何人不得以「读着不对」为由改动，除非能给出反证。

1. **块 1 的主语/受事/归属全对**：「迪吉写信 → 假伊索尔德（收信人）」「the killer」是 fake Isolde 的同位语、「两名登记董事是杰拉德与玛戈特」——`text/ch41_41.txt:38` 逐字。
2. **块 3 的 `from` 方向**：原文 `hid the fact **from** DC Noakes` ⇒ 是**玛戈特瞒着 DC Noakes**（不是 Noakes 瞒着谁）；md `:35` 方向正确，**不要**改成「对 DC Noakes 隐瞒」以外的任何方向。
3. **块 3 的 `the deceased`/`his property`**：受事是**死者（迪吉）的产业**，md `:35` 写「死者去世前不久…要买他的产业」正确。
4. **块 2 的 `she` ＝ 玛戈特**：`I'm guessing she didn't tell Amy that she'd offered Digby…` —— `she` 指 Margot Bourne，md `:28` 正确；**不要**改成 Amy 或艾米。
5. **块 4 的「Mummy」＝她自己（对狗说话的自称）**，狗名 Halloumi、狗在她怀里（`text/ch41_41.txt:72`「barely moved in her arms」）——md `:42` 正确。
6. **块 5 的说话人是艾米**，被转述的施事是**真伊索尔德**（`text/ch41_41.txt:145`）；md `:49` 正确。**注意**：`:154`「So the killer could be one of her readers.」是**马特**说的，补这句时说话人不可写成艾米。
7. **md `:13` 的「Companies House 上联络地址为邮政信箱的公司与两名登记董事」是准确的**（对照 `:11`、`:107` 两处不准的写法，以本行为准）。
8. **词汇表 26 条例句全部是本章原句**（各命中 1 次），例句被截断（如 `proposition`、`forums` 两行）是本书体例，不是残缺。
9. **md `:23`「前面已经把迪吉写给『假伊索尔德』的信与邮政信箱挂上钩」跨章属实**（`ch04_4.txt:83`、`ch07_7.txt:152`、`ch16_16.txt:259`、`ch25_25.txt:224`）。
10. **`anachronistic` 的语境是「迪吉写信刻意不合时宜/用旧式做派」**（`text/ch41_41.txt:32`）——**只有第二义「反潮流的」要删**，「刻意不合时代的」保留。

---

## 五、结论（给修复方的一行指引）

- **必须改（阻断 2 条，同轴可一次改完）**：补上章末 `‘So the killer could be one of her readers.’`（`text/ch41_41.txt:154`）这条转折，并把 `:11`、`:14`、`:51` 三处「只有…才 / 只可能是 / 伊索尔德自己就是源头」的单向必然结论降为**与马特末句并置的开放假设**。
- **建议改（提示 11 条）**：`:11`/`:107`「以邮政信箱注册」→「联络地址是邮政信箱」；`:14`「我记得这位警探」去引号并改回原文义（她喜欢这个警探，只是不如喜欢另一个）；`:30`「坐实」→「提供比较基准」；`:44`「把警察称作坏男人」加限定；`:56`「作者自己先打了个折扣」改成说话人归属清楚的说法；`:67` 删「反潮流的」；块 2 可把估价单那句并入引语。
- **不要改**：块 1/2/3/4/5/6 的主语、受事与归属方向全部正确（见 §四 护栏 1–6）。
- 本轮**未改书目录任何 md，未 git add/commit**，只落盘 `.memory/raw-gates/a-fatal-legacy-by-charlotte-vassell/review/ch41/`（`1-suread.json`、`2-machine.json`、`3-diff.md`、`4-correspondence.md`、`4-verdict.md`）。
