# 4-verdict.md · ch36 独立审查判定

> 审查对象：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch36 callie pitches to the pcqv label.md`
> 唯一权威源：`text/ch36_36.txt`（15,504 字符 / 313 行；小标题 Priory Square；分部「FRIDAY」）
> **快照说明**：本次审查期间，另一实例在 commit `a363a8883`（2026-10-21 14:35）把 19 章的「A X IN MAY」自造措辞改回书内真实分部名，ch36 唯一改动＝导航「一句话概括」里的「A FRIDAY IN MAY」→「FRIDAY」。本审查的全部结论以 **HEAD `a363a8883` 的 ch36 md** 为准（`2-machine.json` 已按该版本重跑，退出码 0）；改动前后除该分部名外逐字一致。
> 审查顺序遵守铁律：**R1 素读（只读 text）→ 落盘 1-suread.json → 才开 md**（见 `1-suread.json`，偏移已逐条自校验）。
> 落盘目录：`.memory/raw-gates/a-fatal-legacy-by-charlotte-vassell/review/ch36/`（未改动书目录任何 md，未 git add/commit）

## 覆盖声明（本次只审第 36 章）

| 范围 | 覆盖度 |
|---|---|
| 第 36 章 | **R0–R5 全走**：R1 素读 → R2 机器层 → R3 三张单子 → R4 逐块对应 → R5 判定 |
| 本书其余 53 章 | **只有机器层**：`bash scripts/gate.sh "<书目录>"` → 退出码 0，正门 0 条阻断型（引语 391 块逐字 100%、中文层 391/391 合格、整书形态偏离 0 章）。**未做 R1–R4 人判，不得写成「通过」。** |
| 附带观察（不属本章判定） | 整书门禁 ⑮ `check_overview_full` 列出「未覆盖章号：ch18, ch21, ch24, ch28, ch34, **ch36**, ch43, ch44, ch49, ch50」——属总览层覆盖问题，本次不判，仅备案 |

---

## 四组数（只报这四组）

| 组 | 结果 | 明细 |
|---|---|---|
| **逐字** | **10/10 通过（阻断 0）** | 10 条引语全部逐字命中原文且在 `text/ch36_36.txt` 内**各只出现 1 次**；无省略号缝合（每条 1 段，片段间无 `…`）、无跨话轮拼接、无跨章搬句。**第二实现自算**（本审查员独立脚本，不复用门禁路径）结果与 `2-machine.json` 一致：10/10 `ok:true`、segment_miss=0。词表 27 条例句亦全部逐字命中且各命中 1 次（`check_vocab.py` FAIL=0、WARN 0 条落在 ch36）。 |
| **对应** | **8/10 成立；引语选短 2；不对应 0；密度不足 0（阻断 0、提示 2）** | 10 块的「为什么这样写」均给出写法层理由，无「只复述字面」的块。B2（分析写到引语外的「she shouldn’t have been this attractive」）与 B9（中文理解写到引语外的「take this one back… pass around the office」）属**引语选短**，详见 `4-correspondence.md`。 |
| **形态** | **0 偏离（阻断 0、提示 0）** | H1＝「36. Priory Square」，全书 54/54 章同形态（`bookform.py`：H1 写法 `{'N.': 54}`）✓；导航 5 项＝`一句话概括 / 视角 / 线索结构 / 人物弧线 / 叙事手法`，与本书众数逐字一致 ✓；子项集 4 项＝`中文理解 / 关键词 / 为什么这样写 / 读者视角提示`，与 profile `mystery-thriller` 一致 ✓（可选 `句子结构` 未用，profile 允许）；块数 10 ＝本书众数 6 / 中位 7 / 范围 5–10 / profile 3–10，**落在范围内**（本书 7/54 章同为 10 块：ch02、ch12、ch27、ch36、ch48、ch52、ch54），**无需写偏离理由**。 |
| **断言** | **11 条核查 → 阻断 2、提示 9** | 逐条见下表。阻断 2 条均为「与原文/全书不符」，附 `text/<文件>:<行>` 与原文逐字。 |

**阻断型条数合计：2**（均在「断言」组；逐字 0 / 对应 0 / 形态 0）

---

## 判定表（断言 | 证据 | 结论 | 档位）

| # | 断言（md 侧） | 证据（章:区间 · 原文逐字） | 结论 | 档位 |
|---|---|---|---|---|
| A1 | **五处**把 PCQV 叫作唱片公司：导航·一句话概括「为**唱片公司 PCQV** 演示她的香水概念」（行 11）、导航·叙事手法「让**唱片公司的人**先夸作品」（行 15）、原句 6·读者视角提示「这本册子后面会被**唱片公司的人**带走传阅」（行 59）、原句 9·中文理解「**唱片公司那位女士**说太有意思了」（行 77）、一句话总结（行 135） | md 行 11、15、59、77、135。`text/ch12:74`：「Mel was checking that **the name of the giant French luxury conglomerate** had landed with suitable weight.」／`text/ch12:170`：「…line up a series of commercial deals and pitch the aesthetic to them first **so that then the label will be forced to go along** with what I want…」／`text/ch18:23`：「‘**PCQV have sent over samples for you to try**…’（death-scented perfumes、lip oils、cream blushes…）」／`text/ch23:340`：「**The label and PCQV are both aware** and they’re fine with it.」／`text/ch17:59`：「**‘Plus Chic Que Vous … Zut alors.’**」 | **PCQV 不是唱片公司**：它是法国奢侈集团「Chic Que Vous」（美妆/香氛产品线方）；唱片公司是 **Eulalia 自己的 label**，是被 PCQV 的商业合同「逼着就范」的另一方（`text/ch12:47`「My deals with my label…」）。md 把两个并列实体并成一个，五处定性错误，且直接把本章的商业结构讲反。ch36 本身未写 PCQV 性质，故本条依据是**跨章原文的正面陈述**，非「查无」。 | **阻断** |
| A2 | 导航·一句话概括与一句话总结都只写「手册被交口称赞并要带回办公室传看」，**全篇无付款/合同/签约字样** | md 行 11、135。`text/ch36:158`：「The end was in sight – **as was the bank transfer.**」／`text/ch36:231`：「Callie’s phone had vibrated in her pocket as soon as she stopped giving her presentation. **Mel had made the payment as she was winding up.**」／`text/ch36:29`：「…**the quicker the commercial contracts got signed.**」 | **这次会面谈成了**：Mel 在收尾时已付款给 Callie（钱从梅尔一侧流出，不是 PCQV 付的）。md 的两处总结把会面落点全部放在作品评价上，读者会以为「只有口头认可」——**关键商业结果缺失（漏）**。补写时勿写成「PCQV 签了约」：原文 ch36 无签约场面，且 `text/ch23:340` 显示 PCQV 早在会前已原则同意（「they’ve already agreed」），本章演的是「让它看起来像一场胜利」。 | **阻断** |
| A3 | 导航·一句话概括「手册被**交口称赞**」；一句话总结同 | `text/ch36:234`（唯一好评，出自 Venetia）：「‘I’ve got to say, that was **bloody fascinating**. I love the booklet you made. **So much more original than the usual shit I see.**’」／`text/ch36:188`：「Mel had lost control of the room and Eulalia was neither the centre of attention nor holding Callie’s.」／`text/ch36:218`：「Venetia and Adam picked up the brocade-bound booklets, **unfazed by Eulalia’s nonchalance**.」／`text/ch36:155`：「…present your idea and then **we’re done**.」（Adam 全章无台词） | 给出手册正面评价的只有 Venetia 一人；梅尔想快点结束、欧拉莉亚全程冷落。「交口」夸大了评价方数量。 | 提示 |
| A4 | 导航·一句话概括「演示她的**香水概念**」；一句话总结同 | `text/ch12:299`：「…all the **creative assets we need to pitch**… mood boards, influences – **something to give to their product design team.**」／`text/ch18:23`：「the **forty-odd products**… death-scented perfumes… lip oils… cream blushes…」／`text/ch36:221`：Callie 讲的是 typography / textures / feelings / glamour 等**视觉体系** | 被 pitch 的是 PCQV 整条彩妆/香氛产品线的调性与视觉概念，香氛只是其中一支（ch36 的「五个」是香味）。写「香水概念」范围过窄，与 A1 相乘会加深误读。 | 提示 |
| A5 | 原句 4·为什么这样写「等于让**第三方**当场给凯莉的**作品**盖了一枚勋章」 | `text/ch36:83`：「‘**When’s Cal arriving?** Eulalia walked into the living room.」（主人之一）／`text/ch36:110`：「‘**Why are you being such a bitch?**’ **Eulalia hissed.**」／`text/ch36:29`：「the quicker **the commercial contracts got signed**.」（签约方是梅尔/欧拉莉亚一侧）／`text/ch36:122`：被夸奖的是凯莉的**衣着**（「Because she makes her own dresses」） | 欧拉莉亚不是「第三方」，她是这场会面的两个主人之一（且是委托方一侧），与 md 自己导航里「被审视的两位女主人」冲突；此处被「盖章」的是凯莉的衣着，与本章「作品＝概念与手册」的框架冲突。说话人本身在中文理解中标对了。 | 提示 |
| A6 | 原句 7·为什么这样写「而**凯莉对此一无所知**」 | `text/ch36:194`：「Eulalia shot her sister a dirty look. **Mel refused to look sheepish.**」（同段只写 Callie「**confused** by Eulalia’s tone and by Mel’s resulting undefinable smugness」） | 原文写的是凯莉**看出不对劲**（困惑、感到梅尔的 smug），没有写她一无所知；这句是合理推论但强度高于原文。 | 提示 |
| A7 | 原句 8·读者视角提示「把这串词与**香水的名字**对照着读」 | 取证三件套：`/usr/bin/grep -n -i -E "perfume (is \| was )?called\|fragrance (is \| was )?called\|scent (is \| was )?called\|the range\|our perfume" notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/*.txt > /tmp/z3.txt 2>&1; echo "exit=$?"` → **命中 0 行（/tmp/z3.txt 为空）；退出码 1**。另 `text/ch18:23` 只写「death-scented perfumes」这一品类，`text/ch36:191` 只写「the honeyed plum scent」，`text/ch12:170` 只写「a make-up line」 | 全书未给该香水/产品线起名 ⇒ 读者指针断头，读者无法执行「与名字对照着读」。 | 提示 |
| A8 | 原句 2·中文理解「她**还认识一个**把头发吹出造型感的发型师」 | `text/ch36:23`：「**she’d got a good hairdresser who’d given her a blow out**」 | 原文是凯莉**有个/请了**发型师给自己做吹风（雇用/光顾关系），md 写成「认识」，关系走样且施事方向变模糊。 | 提示 |
| A9 | 原句 2·为什么这样写引用了「**她本不该这么好看**」 | `text/ch36:23`：「Callie wasn’t thin. She wasn’t fat either, but still, **she shouldn’t have been this attractive.**」（在原句 2 引语**之前**一句） | 分析指向引语之外的上下文 ⇒ **引语选短**。处置：把引语往前扩一句覆盖该句，**不要删分析**（该句原文确实存在，见「已核实为正确」第 3 条）。 | 提示 |
| A10 | 原句 9·中文理解「紧接着她还说要把这一本带回办公室传看」 | `text/ch36:234`：「…**I’m going to take this one back with me to pass around the office**, Venetia said, staring at the magnolias overtaking the square.」（在原句 9 引语**之后**） | 中文理解覆盖的原文比引语长 ⇒ **引语选短**。处置：并入引语或从中文理解里撤出该句。 | 提示 |
| A11 | （无对应分析）Callie 对 Eulalia 的警惕线缺失 | `text/ch36:20`：「She was, in truth, **nervous about introducing Caius to Eulalia.**… **Callie suspected that Eulalia**… **was potentially a bit of a ‘Laura’.**」／呼应 `text/ch42:153`：「‘I think she’s a bit of a “Laura”.’」 | 素读有、md 无（**漏**）。属支线伏笔而非本章转折，故不判阻断。 | 提示 |
| A12 | 形态组整体 | 见上方「形态」行；`bookform.py` 退出码 0 | H1/导航/子项/块数四项均在本书众数与 profile 范围内，**无偏离、无需理由**。 | 跳过（无异常） |

### 口径备案（非缺陷，勿当假红修 md）

`2-machine.json` 的 `pos` 与 `1-suread.json`/`4-correspondence.md` 的绝对字符偏移不同源：门禁用的是 `scripts/lib/text.py::norm` 归一化后的语料（换行折成空格、去引号），偏移因此不可直接相减（B1：机器 20 / 本文 36；B10：机器 12721 / 本文 13124）。**内容无差异**，工具未报错，此处仅作口径备案。

---

## 已核实为正确（防误修·护栏）

> 看着像错、回原文核对后成立。后续任何人不得以「读着不对」为由改动，除非能给出反证。

1. **原句 5 把地上那件东西认作「昨天抽血后贴在手臂上的棉花球」——成立。**
   `text/ch36:44`：「the ball of cotton wool that had been taped to her arm **after the blood test yesterday** rolled out. She didn’t notice.」／`text/ch36:134`：「Eulalia stared at the ground **at the spot where Callie’s bag had been** and picked up a piece of rubbish. But it wasn’t rubbish. It was a bloody treasure.」
   排布与指称指向同一件物事。**注**：这次抽血与怀孕有关（`text/ch20:44`「‘Oh no, it’s OK. **I think they just do a blood test and weigh you or something.**’」，同段有孕检与助产士预约）——md 写「身体状况的物证」**不冲突**，**不得**据此改写，也**不得**把这一层加进 md（会剧透）。
2. **原句 10 未把「one is too present / the other not enough」分配给梅尔或欧拉莉亚——成立，不许改。** 原文本身未指名（`text/ch36:234`「Well, **those two.**」），md 也没指名（写「那两位啊：一个存在感太强，另一个又不够」）。
3. **原句 2 分析里那句「她本不该这么好看」原文确有——成立。** 见 A9：处置是扩引语，不是删分析。
4. **原句 9/10 的说话人是 Venetia（女的、uni friend、in charge of brand），不是 Adam——成立。** `text/ch36:164`：「A man, whose no-nonsense, well-tailored suit made Callie think he was the business side, **and a woman**…」／`text/ch36:212`：「**I’m in charge of brand** and my colleague Adam is from business planning.」（Adam 全章无台词）
5. **三个「五」都对**：五块展板（`text/ch36:44`「the **five easels**」）、五本样本册（`text/ch36:143`「the **five booklets**」）、五个香味样品（`text/ch36:191`「best out of **the five**」）。
6. **付款方向没写反（因为压根没写）。** `text/ch36:231`：「**Mel had made the payment**」——付款人是梅尔一侧；补 A2 时请写成「梅尔付了款」，**不要**写成「PCQV 付了钱」。

---

## 第三方复核（可重跑）

```bash
cd /Users/jcxs2014/Documents/Works/EnglishRead
D=notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell

# R2 机器层（本次：退出码 0）
bash scripts/chapter.sh "$D/ch36 callie pitches to the pcqv label" --json \
  > .memory/raw-gates/a-fatal-legacy-by-charlotte-vassell/review/ch36/2-machine.json; echo "exit=$?"

# 整书机器层（本次：退出码 0，正门 0 阻断）
bash scripts/gate.sh "$D"; echo "exit=$?"

# R3/R4 断言回原文（三条抽样）
sed -n '231p' $D/text/ch36_36.txt   # A2：Mel had made the payment as she was winding up.
sed -n '74p;170p' $D/text/ch12_12.txt  # A1：the giant French luxury conglomerate / the label will be forced to go along
sed -n '234p' $D/text/ch36_36.txt   # A3/A10：Venetia 的好评与 take this one back ... pass around the office
```

**抽 3 行回原文核**：A2（`text/ch36:231`）、A1（`text/ch12:74`）、A3（`text/ch36:234`）——三条均可逐字复现，结论不依赖任何未记录的中间状态。

---

## 最要紧的一条

**A1：把 PCQV 说成「唱片公司」——五处定性错误。** 它同时错在**对象**（PCQV 是法国奢侈集团 Chic Que Vous，做彩妆/香氛产品线；唱片公司是 Eulalia 自己的 label，是被 PCQV 的商业合同逼着就范的一方，`text/ch23:340` 明写「The label and PCQV are both aware」——两者是并列实体）与**结构**（本章的商业结构是「PCQV 出钱出渠道 → 唱片公司接受这套美学」，而 md 写成「向唱片公司推销香水概念」）。更重的是它与 md 自己搭的框架互相拆台：md 把全章收束成「作品被审视 vs 人被审视」两笔账，可 PCQV 恰是**让梅尔着急、让欧拉莉亚被挤到窗边**的那一方——梅尔要的是「the quicker the commercial contracts got signed」，而合同对手方正是 md 认错的那个公司。把「唱片公司 PCQV」改成「PCQV（法国奢侈集团）」，本章的商业骨架与「作品/人」对照才同时立住。

**次要紧**：**A2（漏：会面谈成了、Mel 已付款）**——这是本章专属判据「谈成了没有」的答案：谈成了，但 md 的两处总结只写了「手册被夸、被传看」，读者会以为会面止于口头认可。补一句「梅尔在收尾时付了款」即可（注意方向：梅尔付给凯莉，不是 PCQV 付的）。
