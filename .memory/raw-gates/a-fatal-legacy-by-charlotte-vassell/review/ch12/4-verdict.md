# 4-verdict.md · ch12《A Fatal Legacy》独立审查判定

- **审查员**：独立审查实例（只负责第 12 章）
- **被审对象**：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch12 callie meets eulalia at tate.md`
- **权威源**：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch12_12.txt`（18,050 字符）
- **落盘**：`.memory/raw-gates/a-fatal-legacy-by-charlotte-vassell/review/ch12/`
- **纪律**：先素读（`1-suread.json` 已落盘）后开 md；机器能判的先跑（`2-machine.json`）；人只判漏/对应/说话人/施事归属/事实断言；未改书目录任何文件，未 `git add`／`git commit`。

## 0. 覆盖声明

- 本次**只审第 12 章**（受命范围）。本书其余 53 章**只有机器层的形态统计被引用**（作为众数基线），**没有人判**，不得读作"通过"。
- 未跑全量 `bash scripts/gate.sh "<书目录>"`（范围外）；`scripts/chapter.sh` 只跑了 ch12（退出码 0）。
- R2 命令：
  ```
  bash scripts/chapter.sh "notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch12 callie meets eulalia at tate" --json > .memory/raw-gates/a-fatal-legacy-by-charlotte-vassell/review/ch12/2-machine.json
  → exit 0；verdict "ok"；quotes 10/10 ok；segment_miss 0；struct_bad 0；empty_quote 0；keyword_bad 0；cjk_low 0；issues 全空
  ```
- 章型判定：**对话密集型初见章**（人物第一次见面的对话章）→ 按 `docs/rules/生产-审查对照.md` 加权 S2（跨话轮拼接）/ S3（说话人、施事归属）。本章**不是**首末章、**不是**cliffhanger 章、**不是**重述章，故未加 S1/S5 权重。

## 1. 四组数

| 组 | 数 | 结论 |
|---|---|---|
| **逐字** | **10/10** 引语逐字命中；**27/27** 词汇例句逐字命中；省略号拼接 0；跨话轮拼接 0；U+FFFD 0；双句号 0 | ✅ 全绿（独立取证，非采信 `2-machine.json`） |
| **对应** | **10/10** 块对应；讲引语之外为主 0；讲全书主旨/作者生平 0；密度不足 0；外溢（引语外上下文）7 块＝提示级 | ✅ 全绿 |
| **形态** | H1 ✓ ／导航 5 项＝众数 5 ✓ ／子项 4 项＝众数＝profile ✓ ／块数 10（众数 6、中位 7、范围 5–10）＝**偏离众数，已给理由** | ✅ 合格 |
| **断言** | 共判 **12** 条：阻断 **1**、提示 **11**、假红 **0**、跳过 **0** | ⚠️ 1 条阻断待修 |

> 不给单一"阻断 0"式结论；四组数如上，机器层与人工层分别标注。

## 2. 形态组明细

| 项 | 本章 | 本书众数/profile | 偏离 |
|---|---|---|---|
| H1 | `# 12. Tate Britain` | 形如 `# N. <地点/标题>`，全书 54 章同形（ch01 `# 1. The Horatio Combe Institute, Priory Square, Camden` … ch54 `# 54. The Whittington Hospital`） | 无 |
| 导航项名与项数 | 5 项：**一句话概括 / 视角 / 线索结构 / 人物弧线 / 叙事手法** | 众数 5（`chapter.sh` 形态段 `nav_count_ok: true`、`nav_counts: [5]`） | 无 |
| 子项集 | 中文理解 / 关键词 / 为什么这样写 / 读者视角提示 | 众数 ＝ `mystery-thriller` profile（`profile_optional` 另有"句子结构"，本章未用，不判偏离） | 无 |
| 块数 | **10** | 众数 **6**（19/54）、中位 **7**、范围 5–10 | **偏离众数（向上）** |
| 中文密度 | 中文理解 53–126 CJK／为什么这样写 83–102／读者视角提示 27–50，`cjk_low 0` | profile 门槛内 | 无 |

**块数偏离理由（按 R5 要求）**：本章为**对话密集型初见章**，10 个引语块对应 10 个话轮转折点（改地点→握手与甩手→宣言→梅尔登场→北方来历→奥菲利娅/神圣女性→业务交底→认领与恭维→门票钱→收尾条款）；本书**另有 6 章同为 10 块**（ch02、ch27、ch36、ch48、ch52、ch54），落在既有形态内 ⇒ **不判缺陷**（提示级记录）。
（块数众数取证：Python 统计全书 54 个 `ch*.md` 的 `^> \*\*原句 \d+:\*\*` 行数 ⇒ Counter({6:19, 7:10, 9:8, 10:7, 8:5, 5:5})。）

## 3. 断言判定表

| # | 断言 | 证据（章:区间） | 结论 | 档位 |
|---|---|---|---|---|
| A1 | 导航「线索结构」：「真正管事的姐姐梅尔**几乎全程在场**却基本不接话」 | `text/ch12_12.txt:56` [4613,5025] "Callie wasn’t sure where she’d appeared from. **She wondered if** Mel had been summoned by her sister’s criticisms. **It was quite likely** she had been there the whole time but Callie had been so engrossed in Eulalia that she hadn’t noticed." ／ `:68` [6075,6281] "'I’m going to go meet the people at PCQV." ／ `:80` [6643,6768] 递水后离场 | 原文是**卡莉的猜想**（"quite likely"），md 导航把它写成事实并省去限定；md 自身 `原句 5` 中文理解写对了（"更可能的是她从头到尾都在场"）⇒ 块内不一致，但"几乎全程"可解为**美术馆那场对话**（与原文猜想范围一致），**不构成事实冲突** | **提示** |
| A2 | 导航「人物弧线」：「一路走到**挽着卡莉的胳膊**、**把门票钱记到梅尔账上**」 | `:230` [13816,14023] "'Thank you so much. **Invoice Mel for the tickets.**" ／ `:293` [16191,16581] "Eulalia **linked her arm through hers** and practically marched Callie back towards Westminster station." | 两项各自为真，但**列举次序与原文相反**（原文先记梅尔账、后挽臂出教堂）。该句可读作"两项并列的状态收束"，故**不判事实错误**；建议调换次序以免读者读出倒序 | **提示** |
| A3 | `原句 8`·为什么这样写：「掏钱的人**连自己身上没钱都不解释**，只让对方'记梅尔'」 | `text/ch12_12.txt:230` [13816,14023]（**即该块引语自身的后半**）："'I don’t have any money on me. Only my Oyster card.'" | md 的转述与**同一块引语的原文直接冲突**：欧拉莉亚明说身上没带钱（并补"只有交通卡"）；md 同块"中文理解"也写对了（"她说：我身上没带钱，只有交通卡"）⇒ 块内自相矛盾，且属本章专属判据点名范围（"凡涉及欧拉莉亚说过的话……是否逐字、是否被正确归属"） | **阻断** |
| A4 | 漏：`原句 3` 读者视角提示自指"后面整场关于奥菲利娅、圣女与'神圣女性'的判断，都从这里长出来"，但**无任何块**覆盖 | `:116` [7689,7804] "stopped in front of Millais’s Ophelia" ／ `:122` [7839,8046] "she’s fucking weak. I hate that she goes mad and that makes her fuckable" ／ `:125` [8049,8071] "'Viragos not damsels.'" ／ `:128` [8074,8157] "I’m all about the divine feminine." ／ `:134` [8187,8710] "God’s a woman. God’s a mother. … That’s why I bought my house." | md 未就此作出任何**错误**陈述，只是未展开（且 `原句 4` 已覆盖宣言主干）⇒ 非"关键事件被写错/被虚构"，属**未兑现的自指承诺** | **提示**（优先补） |
| A5 | 漏：业务交底段的关键数字与"legacy works"母题全缺 | `:152` [9335,9902] "**We estimate that I have five years**… I’m going to get fabulously rich and then I’ll make my **legacy works**." ／ `:164` [10612,10797] "**They’ve given me two weeks**" ／ `:170` [10867,11725] "**We need to pitch the brand feel to them next week**… sold in high-end department stores and in **Sephora**" | md 中 `legacy`／`five years`／`two weeks`／`Sephora`／`PCQV` **全部零命中**（取证命令见 §5）；但 `原句 10` 已覆盖交付物机制（资产清单 / mood boards / 产品设计团队 / 本周演示前再见 / turnaround），且真正的 pitch 在本书另章（ch36 `callie pitches to the pcqv label`）⇒ **不判"关键事件缺失"**，属重要补充 | **提示** |
| A6 | 漏：教堂内实质对话（Pepys / Catherine of Valois / Elizabeth I / ruffs / Brontës）未成块 | `:245` [15020,15076] "'Samuel Pepys was a creepy little fucker'" ／ `:251` [15168,15386] "kissed her on the lips" ／ `:257` [15411,15504] "'Such a baddie.'" ／ `:275` [15656,15682] "'I want to take up space.'" ／ `:284` [15878,15954] "'The Brontës.'" | md 未写错，只是未展开（`:8`、`:9` 两块已覆盖前后）⇒ **提示** | **提示** |
| A7 | `原句 9`·读者视角提示：「**对烈士画像满不在乎的人**面前，这个细节是作者落下的硬判断」 | `:293` [16191,16581] "something about Eulalia’s flippant tone rankled **her** while **she** stared up at Martin Luther King" | 原文里**抬头看 MLK 的是卡莉**（her/she 皆指 Callie），文本只记录"欧拉莉亚的轻佻语气刺到了卡莉"，**没有记录欧拉莉亚对烈士纪念物的态度**；md 把"硬判断"改派给欧拉莉亚的"满不在乎"＝**分析层施事/归属偏移**（R4 三问）。md 同块中文理解写对了主语 ⇒ 块内不一致 | **提示** |
| A8 | `原句 9`·中文理解：「墙上**马丁·路德·金的画像**」；读者视角提示「**烈士画像**」 | `:293` "while she stared up at Martin Luther King" ／ `:287` [15957,16158] "silently taking in the **twentieth-century martyrs above the door**" | 原文只写 "stared up at Martin Luther King"，**未指明载体**；md 把未指明具体化成"画像"（原文写的是门上的殉道者铭牌/碑）⇒ 细节性添加 | **提示** |
| A9 | `原句 6`·中文理解：「她甚至为两个人一起报了朗读发声课」 | `:89` [6945,7201] "Mel had advised **her** to so she’d be taken more seriously. **She’d** gone as far as to get elocution lessons **for the pair** but Eulalia knew she couldn’t keep it up as well as Mel could." | "She'd" 的先行词原文两可（Mel 或 Eulalia）；md 取 Eulalia，而同块读者视角提示又说"姐姐一手安排" ⇒ **原文未钉死，不判与原文冲突**，建议显式标注为推断 | **提示** |
| A10 | `原句 4`·为什么这样写：「作者让卡莉**几乎无从插话**」 | `:41` [3405,3639]（宣言本体）／`:44` [3642,3979] "'**In my experience that depends on the man.**' Callie took out her notebook…" | 宣言之后卡莉**确有回话**（`:44`），同块读者视角提示也写"卡莉回应这句话……把球踢了回去" ⇒ 块内自相矛盾；"宣言本身未被打断"成立，"无从插话"过头 | **提示** |
| A11 | `原句 1`·为什么这样写：「'awe-inspiring'……**也是给自己壮胆的**」 | `:20` [35,789] "Eulalia had decided that she wanted to meet 'somewhere awe-inspiring', and had changed the venue at the last minute." | 原文只给动机（想见一个 awe-inspiring 的地方），**无任何自我畏缩/需要壮胆的线索** ⇒ 作者动机凭空补写（解读越界） | **提示** |
| A12 | 导航「一句话概括」：「两人在名画前互相打量、**用客气话互相试探**」 | `:35` [2933,3202] "Eulalia’s handshake was limp. **She didn’t care for such formalities.** … **Eulalia ignored Callie**" ／ `:41` [3405,3639] "… Cholera in trousers." | 欧拉莉亚一侧**不客气**；"客气"是卡莉一侧（"We all have our strengths"）。md 自己在 `原句 9` 写"整章的**客气**到这一句第一次出现裂纹"指的是卡莉 ⇒ 导航"互相"读法与自家分析不一致 | **提示** |

**档位小计**：阻断 1（A3）· 提示 11（A1、A2、A4、A5、A6、A7、A8、A9、A10、A11、A12）· 假红 0 · 跳过 0。

## 4. 已核实为正确（防误修，固定一节）

以下写法**看着像错、回原文核对后成立**，后续任何人不得以"读着不对"为由改动，除非能给出反证：

1. `原句 4` 的"女人与男人宣言"**归属欧拉莉亚**——`text/ch12_12.txt:41` [3405,3639] "Women should be unpredictable…" ＋ `:44` [3642,3979] "'In my experience that depends on the man.' Callie took out her notebook…" ⇒ 宣言必为 Eulalia 所说。
2. `原句 6` 的问答方向——`:86` [6908,6942] "'Where in the North are you from?'" → `:89` [6945,7201] Eulalia "'How could you tell?'" → `:92` [7204,7282] "'The humour in your work feels northern. I expected you to be from Yorkshire.'"（**卡莉**）→ `:95` [7285,7330] Eulalia "'God’s own country.'" → `:98` [7333,7376] 卡莉 "'See, only people from Yorkshire say that.'" → `:101` [7379,7442] Eulalia "'All right, you’ve got me. I’m a Yorkshire lass born and bred.'" ⇒ **问者卡莉、被问者欧拉莉亚**，md 一致。
3. `原句 7` 把 "Performance art meets Renaissance fayre?" 归**卡莉**、"Exactly." 归**欧拉莉亚**——`:173` [11728,11770]（未标说话人，接 `:170` 卡莉插话后）+ `:176` [11773,12072] "Eulalia: 'Exactly. I knew you’d get it.'" ⇒ 正确。
4. `原句 5` 把画旁翻白眼的女人认定为**梅尔**——`:56` [4613,5025] + `:59` [5028,5065] "'Mel, this is Cal; Cal, this is Mel.'" ⇒ 正确。
5. `原句 9`·中文理解把"抬头看马丁·路德·金"的主体给**卡莉**——`:293` "rankled **her** while **she** stared up at Martin Luther King"（her/she 皆为 Callie）⇒ 正确（只 A7 的读者视角提示有问题）。
6. `原句 8` 的 £70／两张票／由卡莉垫付——`:227` [13450,13813] "Callie paid the £70 with a smile on her face." ⇒ 正确（仅 £70 实含两本厚重导览册，属 A 级轻提示）。
7. 十个引语块**全部逐字连续命中原文**，无省略号缝合、无跨话轮拼接（见 §5 取证）。

## 5. 取证命令（R5-补：零命中类断言必须自证）

```
# (1) 10 条引语逐字命中（独立于 chapter.sh 的第二实现）
python3 - <<'PY'   # md 引语 → text/ch12_12.txt 做 str.find
  Q1..Q10 → ok=YES, pos = 35 / 2306 / 2933 / 3405 / 4613 / 6945 / 11773 / 13816 / 16191 / 16738
  ellipsis in quotes: False
PY
→ 退出码 0；10/10 连续命中，无省略号、无跨话轮拼接。

# (2) A5 的零命中断言（md 侧）
cd notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell
for pat in legacy 'five years' 'two weeks' Sephora PCQV; do /usr/bin/grep -cE "$pat" "ch12 callie meets eulalia at tate.md"; echo " exit=$?"; done
→ legacy 0 exit=1 ／ five years 0 exit=1 ／ two weeks 0 exit=1 ／ Sephora 0 exit=1 ／ PCQV 0 exit=1

# (3) A4 的零命中断言（md 侧）
for pat in Ophelia Viragos 'divine feminine'; do /usr/bin/grep -cE "$pat" "ch12 callie meets eulalia at tate.md"; echo " exit=$?"; done
→ Ophelia 0 exit=1 ／ Viragos 0 exit=1 ／ divine feminine 0 exit=1
（对照组：unpredictable 3 exit=0 ／ female anger 1 exit=0 ／ wild-eyed 1 exit=0 ⇒ 工具本身可命中，零命中为真零）
```

## 6. 结论

- **四组数**：逐字 **10/10**（＋词汇 27/27）／对应 **10/10**／形态 **合格**（块数 10 高于众数 6，已给理由）／断言 **12 条 → 阻断 1、提示 11、假红 0、跳过 0**。
- **阻断型条数：1**（A3）。
- **最要紧的一条**：**A3** —— `原句 8` 的"为什么这样写"说"掏钱的人连自己身上没钱都不解释"，而**同一块引语原文**就写着"'I don't have any money on me. Only my Oyster card.'"；md 在同块"中文理解"里也已写对。这条同时踩中本章专属判据（凡涉及欧拉莉亚说过的话，逐字与归属）与机器探针的死角（引语逐字 ✅、中文是中文 ✅、关键词 ✅、形态 ✅ 四道全绿，只有 R4 三问能抓）。最小改法：把该分句改成"……而掏钱的人一句'我身上没带钱'就把责任转给梅尔"。
- 其余 11 条提示均**不要求先改**：A1/A2（导航压缩口径）、A7/A8（施事与载体）、A9（指代两可）、A10/A11/A12（措辞越界或块内不一致）、A4/A5/A6（建议补的内容）——**按章型加权（对话密集章 → S3 说话人与施事）优先修 A7，其次 A1**；A4/A5 若要提升本章密度，优先补 A5（"legacy works" 母题 + 五年/两周两个数字）。
