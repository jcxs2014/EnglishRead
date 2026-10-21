# 4-verdict.md · 《A Fatal Legacy》第 50 章独立审查判定

- 审查员：独立审查（读取顺序：先 `text/ch50_50.txt` 素读并落盘 `1-suread.json`，再开 md）
- 权威源：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch50_50.txt`（172 行 / 6280 字节）
- 审查对象：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch50 isolde is questioned about the stories.md`
- 机器层：`bash scripts/chapter.sh "<书目录>/ch50 isolde is questioned about the stories.md" --json` → **退出码 0**，`verdict: ok`（输出见 `2-machine.json`）
- 本次未改动书目录任何 md，未 `git add`／`git commit`；只写 `.memory/raw-gates/a-fatal-legacy-by-charlotte-vassell/review/ch50/`

---

## 一、四组数（只报这四组）

| 组 | 分母 | 通过 | 缺陷 | 说明 |
|---|---|---|---|---|
| **逐字** | 6 个引语块 | 6 | **0** | 6/6 逐片段独立取证命中、原文各出现 1 次、无 `…` 缝合、无跨话轮拼接；词汇例句 27/27 在原文各命中 1 次；md 内引用的英文片段全部命中 |
| **对应** | 11 个分析单元（6 块 + 5 导航项） | 8 | **3（阻断）** | 3 条缺陷全是「施事/归属/否认对象」类：引语选短 0、密度不足 0、不对应 0 |
| **形态** | 4 项（H1 / 导航项 / 子项集 / 块数） | 4 | **0 偏离** | 详见下节 |
| **断言** | 22 条可核查陈述 | 13 成立 | **8 提示 + 1 假红** | 断言组内 0 阻断（3 条阻断已在「对应」组计，避免重复计数） |

**阻断型条数：3（D1、D2、D3）**

---

## 二、形态组（H1 / 导航项 / 子项集 / 块数 与本书众数、profile 的偏离）

| 形态项 | 本章 md | 本书众数（`2-machine.json` → `form`） | profile（mystery-thriller） | 偏离 |
|---|---|---|---|---|
| H1 | `# 50. The Police Station`（原文 `:17` 标题 `The Police Station`） | `h1_shape_ok: true`（`# NN. 章标题` 形） | 同 | 无 |
| 导航项 | 5 项（一句话概括 / 视角 / 线索结构 / 人物弧线 / 叙事手法） | `nav_count: 5`，众数 `nav_counts: [5]`，`nav_missing: []` | 同 | 无 |
| 子项集 | 中文理解 / 关键词 / 为什么这样写 / 读者视角提示（每块 4 项） | `subitems_modal` = 同样 4 项 | `profile_subitems` = 同样 4 项（可选 `句子结构` 本章未用，可选项不作偏离） | 无 |
| 块数 | 6 | `block_median: 7`，`block_range: [5, 10]` | — | 无（6 落在 [5,10] 内） |

**形态组结论：4 项全部与本书众数/profile 一致，偏离 0，无需理由行。**（另：`分部 MONDAY` 属 epub 的 Part 标题层，见第四节 F1，已核实为真。）

---

## 三、判定表（断言 | 证据 | 结论 | 档位）

证据写法：`text/ch50_50.txt:<行>`（字符区间 `[start,end)`，原始文件偏移）+ 原文逐字。

### 3.1 阻断型（3 条，必须改；均在 md 侧）

| # | 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|---|
| D1 | 导航「视角」：`Isolde 的内心全部靠台词与动作传达（瞪眼、**涨红的脸**、跛着走、掉泪）` | `text/ch50_50.txt:57` `[1364,1624]`：`‘About that …’ **Matt started to blush.** He thought she was far too hot to be sat at home writing things like salad sex. Surely, girls like her were just out there getting laid rather than just imagining it.` | 涨红的是**提问者 Matt**，不是 Isolde。施事反转；且原文同一句把 Matt 对她的物化式判断写得很直白，md 抹掉这一层后，导航对「谁在想什么」的交代失真。 | **阻断** |
| D2 | 原句 2「为什么这样写」：`而“给陌生人写”这个结构……**等于承认那个账号存在、只是不归她管**` | `text/ch50_50.txt:66` `[1689,1731]`：`‘What? I don’t have an account like that.’`；`:72` `[1789,1827]`：`‘Absolutely not.’ Isolde was offended.`；`:78` `[1869,1930]`（引语本身）：`‘I do not write dirty stories for strangers on the internet.’`；`:87` `[2138,2419]`：`‘You’re still logged in.’ He spun the laptop around.` | 原句 2 发生时她**刚否认过账号存在**；账号存在是被 Matt 用仍登录的笔记本（`:87`）推翻的，发生在引语**之后**。md 把一次否认读成了「默认账号存在」的让步，且与 md 自己的原句 1 分析（`她第一次否认落点……在“这个账号存不存在”……这层否认在几分钟后被笔记本电脑上的登录状态顶了回来`）自相矛盾。**违反本章专属判据 ①（她否认的具体对象）。** | **阻断** |
| D3 | 原句 6「读者视角提示」：`更像是**在试对方知道多少——被问到自己家族与地下的关系时**，他笑着把话头从房子转到了广场` | `text/ch50_50.txt:142` `[4248,4391]`：`‘No, it was a conflict of interest. He just discovered that **his family** own the leaseholds in the area where the crimes have been concentrated.’`；`:145` `[4394,4655]`：`‘I see. … ‘**Their house** in Hertfordshire has lots of priest holes. … Did you know that?’`；`:151` `[4733,4788]`：`‘**Your colleague’s ancestors …**’ Andy sagely drifted off.` | 两处方向都错：**那家族是 Matt 同僚 Beauchamp 家的，不是 Andy 的「自己家族」**（原文明写 `Your colleague's ancestors`）；**Andy 是主动抛出，Matt 从未就「家族与地下」向他发问**（Matt 只回 `‘No, I didn’t’`/`:148`、`‘Yes?’`/`:154`、`‘Oh.’`/`:160`）。归属方向反转。 | **阻断** |

### 3.2 提示型（8 条，只记不改或仅措辞建议）

| # | 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|---|
| D4 | 三处「Andy **在警局门口**」 | `text/ch50_50.txt:115` `[3281,3411]`：`He walked her back to **reception**. Andy, her ex, was waiting for her.`；`:166` `[5650,5792]`：`He returned to his desk in the incident room …` | 对话发生在**警局内的接待处**，不是门口。地点失准（三处重复），不影响情节。 | 提示 |
| D5 | 原句 6：`Matt 的**全部回应**只有一句“No, I didn’t”` | `text/ch50_50.txt:148` `[4658,4730]`：`‘No, I didn’t,’ Matt replied. …`；`:154` `[4791,4797]`：`‘Yes?’`；`:160` `[5511,5516]`：`‘Oh.’` | Matt 实际有三次回应；且 `‘Yes?’` 正是引出 Andy 那整段十六世纪「科普」的触发点。「全部」过硬。 | 提示 |
| D6 | 原句 5：`violated 是这一章里她对自己的**唯一定位词**——她描述的不是“身份被冒用”，而是“被侵犯”` | `text/ch50_50.txt:54` `[1052,1361]`：`‘Thank God. I’ve been petrified all week. It’s so grim. **Stealing parts of my life** to seduce and murder a man. …’` | 她自己用过「人生被窃取」即身份被冒用的说法；md 自家原句 2 也承认这一点 ⇒ 绝对化措辞 + 自相矛盾。 | 提示 |
| D7 | 导航「叙事手法」：`“我没回答那个问题”与“**我没听懂那番话**”这两处空白，都被留到**下一次再看录像时**才结算` | `text/ch50_50.txt:163` `[5519,5647]`：`Andy’s mouth quivered. **He wanted to ask Matt something else but backed off it.** ‘Anyway, I best drive Princess Isolde back home.’`；跨章：`/usr/bin/grep -c -i -E "where were you|alibi|Stratford|those dates" text/ch51_51.txt` → `0`，**退出码 1** | 原文的空白是 **Andy 有话没问出口**，不是「某人没听懂」；Matt 听懂了（叙述把 Andy 的话整段转述）。跨章断言在下一章未兑现（ch51 只到 Marcus 说次日 10 点带机器人摄像去 site）。 | 提示 |
| D8 | 原句 3：`正是在上课中间` | `text/ch50_50.txt:96` `[2536,2940]`：`‘… That’s right in the middle of **a school day**. I was substituting in a school in Stratford. …’` | `a school day` = 一个上学日的中段，「上课中间」易读成「一节课上到一半」。 | 提示 |
| D9 | 导航「人物弧线」：`一路滑到“**有人在用我的名字写**色情故事”` | `text/ch50_50.txt:121` `[3473,3630]`：`‘I need a strong drink,’ Isolde said, shaking her head as if to hold back the tears that had been forming. ‘**Someone’s writing dirty stories about me online.**’` | 原话是 `about me`（关于我）；「用我的名字」比原文多走一步（原文只到「有人用她的账号发布、她说『这些我没写过』」）。**但 md 未据此断言冒名者是谁 ⇒ 判据 ④ 未越权。** | 提示 |
| D10 | 词汇档位：`psychopath` 列 ⭐⭐⭐ 高级（`crypt` 同级） | `text/ch50_50.txt:157` `[4800,5508]`：`He was a Boy’s Own psychopath, after all.` | `psychopath` 为日常高频词，与 metaphorical/leaseholds/priest holes 同列偏注水（S4 第 ③ 类）。 | 提示 |
| D11 | 覆盖缺口：导航/六块均未提 **Forensics 在 Institute 找到真隧道、Robbie 赶往 Institute** | `text/ch50_50.txt:23` `[128,372]`：`‘I’ve got to go to the Institute, Matt. That nutter wasn’t talking about metaphorical tunnels. **Forensics have bloody found one.**’`；`:26` `[375,447]`：`‘I’d give Caius’s dad a call in that case. It’s his land.’`；`:32` `[525,568]`：`Matt shrugged. ‘I’ll speak to Isolde then.’` | 本章唯一的「案件推进实锤」，md 全文 `Institute` 命中 0、`forens` 命中 0（`Robbie` 仅出现在词汇表例句）。属覆盖缺口而非错写。 | 提示 |
| D12 | 覆盖缺口：Andy 后半段（维多利亚时代拆修道院、十六世纪二次封地道、老 Horatio、`a change in precedence`）无引语块、无分析 | `text/ch50_50.txt:157` `[4800,5508]`：`‘Well.’ Andy moved closer to Matt. ‘When the current houses were built in the Victorian era and the priory was exposed for the first time in three hundred years, the Beauchamps already knew what was down there. They chose to seal it up again, like their ancestors had in the sixteenth century. They knocked the priory down, you know. Left the crypt and basement levels only. … I wouldn’t be surprised if old Horatio knocked through. He was a Boy’s Own psychopath, after all. …’` | md 全文 `Horatio` 命中 0、`十六` 命中 0；原句 6 止于 `:145`。本章对 Beauchamp 家族最重的一击未被任何一层覆盖。 | 提示 |

### 3.3 假红（1 条：工具/语料口径错，md 没错）

| # | 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|---|
| F1 | md 导航「叙事手法」称本章属 `分部 MONDAY` | 按唯一权威源：`/usr/bin/grep -c -w "MONDAY" text/*.txt` → **55 个文件全部为 0，退出码 1**；`/usr/bin/grep -c -w "MONDAY" text/ch50_50.txt` → `0`，退出码 1 | **报警复核（先假定语料口径错）**：解包 epub `library/A Fatal Legacy (…).epub` → `OPS/s064-Part-010.xhtml` 标题即 `MONDAY`；`OPS/TOC.xhtml` 目录为 `… SATURDAY 41…47 / MONDAY 48 / 49 / 50 / 51 / TUESDAY 52 / 53 / SIX WEEKS LATER 54`；`OPS/s067-Chapter-050.xhtml` 即第 50 章，位于 Part-010 之下。⇒ **md 的「分部 MONDAY」正确**，查无的原因是 `text/` 提取件丢弃了 epub 的 Part 标题层（语料口径），非 md 编造。 | **假红** |

### 3.4 跳过（0 条）

无。6 块引语、5 项导航、27 条词汇例句、以及两处跨章断言全部实查。

---

## 四、R5-补 ·「零命中」类断言的自证（命令 / 输出 / 退出码）

```
cd notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell

$ /usr/bin/grep -c -w "MONDAY" text/*.txt
（55 个文件全部输出 file:0，无非零行）
exit=1

$ /usr/bin/grep -c -w "MONDAY" text/ch50_50.txt
0
exit=1

$ /usr/bin/grep -o -i -E '\b(monday|tuesday|wednesday|thursday|friday|saturday|sunday)\b' text/*.txt | sort | uniq -c
2 text/ch02_2.txt:Saturday … 1 text/ch05_5.txt:Monday … （全部为散文中的星期词，ch50 无命中）
exit=0

$ /usr/bin/grep -o -i -- "Institute" "ch50 isolde is questioned about the stories.md" | wc -l   → 0
$ /usr/bin/grep -o -i -- "forens"  "ch50 isolde is questioned about the stories.md" | wc -l   → 0
$ /usr/bin/grep -o -i -- "Horatio" "ch50 isolde is questioned about the stories.md" | wc -l   → 0
$ /usr/bin/grep -o -i -- "十六"    "ch50 isolde is questioned about the stories.md" | wc -l   → 0
$ /usr/bin/grep -o -i -- "门口"    "ch50 isolde is questioned about the stories.md" | wc -l   → 3

$ /usr/bin/grep -c -i -E "where were you|alibi|Stratford|those dates" text/ch51_51.txt
0
exit=1
```

**语料边界核验（跨步骤·语料）**：解包 epub 后 `OPS/s067-Chapter-050.xhtml` 去标签、去页码，与 `text/ch50_50.txt` 逐行比对 ⇒ **除 epub 排版换行外完全一致**（`IDENTICAL: False` 的唯一差异是两处 epub 硬回车被 corpus 合并），**无「两篇并进一个文件」问题**。

---

## 五、R5.5 · 已核实为正确（防误修，护栏）

以下写法**看起来像错，回原文核对后成立**——后续任何人不得以「读着不对」为由改动，除非能给出反证。

| # | md 写法 | 证据（原文逐字） |
|---|---|---|
| 1 | `分部 MONDAY` | `OPS/s064-Part-010.xhtml` 标题 `MONDAY`；`OPS/TOC.xhtml`：`MONDAY` 段含 48/49/50/51；ch50 在其中。（见 F1） |
| 2 | 原句 3：`她是一名英语语言教学 lead` | `text/ch50_50.txt:96`：`firstly, I’m an English lead – the grammar is appalling.`；另 `:84`：`I was going to go to a cafe after and apply for English language teaching jobs in Italy.` ⇒ 「英语 lead / 英语教学」解读与原文一致，未把 `lead` 误读为「铅」。 |
| 3 | 原句 6：`priest holes（藏人的地洞）`、`Priory Square 有段有意思的历史`「把范围指向警方正在查的那片区域」 | `text/ch01_1.txt:17`：`The Horatio Combe Institute, Priory Square, Camden`；`text/ch33_33.txt:274`：`Priory Square had been the site of St Agnes’s Priory founded by Eleanor of Aquitaine … in 1188.`；`:286`：`In the 1860s, when the houses that now form Priory Square were constructed …`；`:331`：`Priory Square. It’s Beauchamp land.` ⇒ 指向成立。 |
| 4 | 原句 3 对 Isolde 两条反驳理由的转述（English lead + 语法糟 / 在 Stratford 代课、笔记本在家、关机、师德） | `text/ch50_50.txt:96` 逐项对应（见 `4-correspondence.md` 对应表）。 |
| 5 | 原句 4：`可这一问之后紧跟一个分节符，本章没有给出她的回答，她人已经走出大楼了` | `text/ch50_50.txt:99` → `:104` `* * *` → `:109` `Matt escorted her out of the building.` |
| 6 | 一句话总结：`Matt 真正没得到答案的那个问题（那几天她人在哪里），本章始终悬着` | `text/ch50_50.txt:99` 提问后本章无回答（`text/ch51_51.txt` 亦未答）。 |
| 7 | 全章问答的说话人归属（Matt 提问、Isolde 否认、Andy 闲话；Robbie 不在场） | `text/ch50_50.txt:45`：`Matt introduced himself for the recording.`；`:23`/`:32` Robbie 离场去 Institute，`:45` 起只有 Matt 与 Isolde。 |
| 8 | 未把「冒名者是谁」写成事实（判据 ④） | 原文全章无人指认作者；md 亦未点名任何人（`text/ch52_52.txt:377` 才是结局揭晓处，属下一章）。 |
| 9 | 词汇表 27 条例句 | 全部在 `text/ch50_50.txt` 原文各命中 1 次（脚本核验，0 例外）。 |
| 10 | 原句 1：`这层否认在几分钟后被笔记本电脑上的登录状态顶了回来` | `text/ch50_50.txt:87`：`‘You’re still logged in.’ He spun the laptop around.`（方向正确：Matt 用她的笔记本推翻，不是她自认） |

---

## 六、覆盖声明

- 本次**只审第 50 章**；R1 素读、R2 机器层、R3–R5 全部只针对 ch50。
- 其余 52 章：**未跑机器层、未查**——按 `审查表.md` §0.5 记作「未查」，**不得写成「通过」**。
- 为核验 md 的跨章断言，读取了 `text/ch49_49.txt`（尾部）、`text/ch51_51.txt`、`text/ch52_52.txt`、`text/ch33_33.txt`、`text/ch01_1.txt`、`text/ch21_21.txt` 的**原文**（未开任何其他章节的 md）。
- epub 仅用于核验 epub 结构（Part 标题 `MONDAY`）与语料边界，比对对象是 `OPS/s067-Chapter-050.xhtml`（本章），其余 Part/TOC 文件只读标题行。

---

## 七、一句话结论

机器层全绿（6/6 引语逐字、形态 4/4 一致、27/27 词汇例句命中），人判在**施事/归属/否认对象**三类上查出 **3 条阻断**（涨红的脸属于 Matt 不属于 Isolde；原句 2 把「我否认账号存在」读成「她承认账号存在」；原句 6 把 Beauchamp 家写成 Andy 的「自己家族」且把他写成被问方），另有 8 条提示（地点、绝对化措辞、两处覆盖缺口、跨章断言未兑现、词汇档位注水、译法）与 1 条假红（「分部 MONDAY」查无系语料口径，实为真）。**md 自身没有把嫌疑写成事实，也没有越权点名冒名者。**
