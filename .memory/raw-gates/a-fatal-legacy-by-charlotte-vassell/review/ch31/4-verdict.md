# 4-verdict.md · ch31 《A Fatal Legacy》· 独立审查判定

- 审查对象：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch31 a second body is found at priory square.md`
- 唯一权威源：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch31_31.txt`（md5 `ad8aa838b3253c3214c5d5af6c74c5bc`，9053 字符）
- 执行顺序：**R1 素读（`1-suread.json`，先于开 md）→ R2 机器层（`2-machine.json`）→ R3 三张单子（`3-diff.md`）→ R4 逐块（`4-correspondence.md`）→ R5 本文件**
- 覆盖声明：**本次只审第 31 章**；本书其余 53 章**只有机器层**（`chapter.sh` / `check_vocab.py` / `verify_corpus.py`），**不写「通过」**。
- 机器层结果：`bash scripts/chapter.sh "<md>" --json` **退出码 0**（`verdict: ok`；`segment_miss 0`、`struct_bad 0`、`empty_quote 0`、`keyword_bad 0`、`cjk_low 0`）；`python3 scripts/check_vocab.py "<书目录>"` **退出码 0**（FAIL 0，本章 0 WARN）；`python3 scripts/verify_corpus.py "<书目录>"` **退出码 0**（FAIL 0 / WARN 3，WARN 均为全书级：件数未给 `--expect`、人物锚点未给 `--anchors`、页码 bleed 落在 ch23 非本章）。
- 覆盖代码：**只读不写**。未改书目录任何 md、未 `git add`、未 `git commit`。落盘仅在 `.memory/raw-gates/a-fatal-legacy-by-charlotte-vassell/review/ch31/`。

---

## 一、四组数

| 组 | 口径 | 结果 |
|---|---|---|
| **逐字** | 7 条引语 × 逐字比对原文 | **7/7 通过**（本人 Python 独立复核 `body in src` = True，pos = 36 / 1124 / 1988 / 2216 / 4142 / 4847 / 6943）；**无省略号拼接、无跨话轮拼接、无跨章搬句、无 U+FFFD** |
| **对应** | 7 个引语块逐块 R4 判定 | **成立 2（块 1、块 6）／部分对应 2（块 5、块 7）／不成立 3（块 2、块 3、块 4）**；密度不足 0；不对应 0 |
| **形态** | H1 / 导航 / 子项集 / 块数 vs 本书众数 & profile | **0 偏离**（见下表） |
| **断言** | 漏 2 + 编 4 + 错 7 = **13 条** | **阻断 5、提示 8、假红 0、跳过 0** |

**阻断型条数（去重后）＝ 6 条**：断言组 5 条（编 1、编 2、编 3、编 4、错 1）+ 对应组 1 条仅见于对应组（块 2 引语选短）。
（断言组 5 与对应组 3 有 3 条重叠：围观人群、Barry 角色、施事反转——同一缺陷的两个视角。）

### 形态组明细

| 项 | 本章 | 本书众数 / profile | 偏离 |
|---|---|---|---|
| H1 | `# 31. Priory Square` | 全书 54 章一律 `# NN. <epub 章名>`；本章 epub 章名即 `text/ch31_31.txt:17` 的「Priory Square」 | 无 |
| 导航项名与项数 | 本章导航：**一句话概括 / 视角 / 线索结构 / 人物弧线 / 叙事手法**，共 **5** 项 | 众数 **5**（`nav_counts: [5]`），`nav_missing: []` | 无 |
| 子项集 | 每块 4 项：**中文理解 / 关键词 / 为什么这样写 / 读者视角提示**（7 块齐全） | profile `mystery-thriller` 的 `profile_subitems` 同 4 项（可选 `句子结构` 未用） | 无 |
| 块数 | **7** | 本书众数 **7**（`block_median 7.0`，区间 5–10） | 无 |

⇒ **形态组 0 偏离，故无偏离理由行。**

---

## 二、判定表（断言 | 证据 | 结论 | 档位）

| # | 断言 | 证据（章:区间） | 结论 | 档位 |
|---|---|---|---|---|
| A1 | md：「围在场边的人对『又来一次』没有表现出任何意外」（块 3） | `text/ch31_31.txt:38-41`（到场者仅 Caius、Matt、Barry、技术员两人）；`text/ch32_32.txt:20,86`（围观/警灯在下一章） | 本章无围观人群、无邻居在场；该场面属**下一章**材料 | **阻断** |
| A2 | md：「法医技师巴里……」（块 3 中文理解）＋导航「法医巴里的判断」 | `text/ch31_31.txt:41`「A forensic technician was swabbing…」（另一人）；`text/ch02_2.txt:101`「Barry, the team’s favourite medical examiner」；`text/ch02_2.txt:128`「removed by two forensic technicians」 | Barry 是**验尸官**，与法医技术员分列；md 同句另列两名技师，自相矛盾 | **阻断** |
| A3 | md：「整个广场家家有摄像头」「每个人都确信自己是安全的」「每户人家的摄像头」（块 5＋导航两句） | `text/ch31_31.txt:68`「Quite a few of the houses have cameras but they’re all within the gardens and pointed at their gates」 | 原文是「**不少**房子有摄像头」，非家家；「人人放心」无据；md 论证建立在此放大之上 | **阻断** |
| A4 | md：「两起入室盗窃可以算巧合」被「PO Box 的关联不可能是巧合」**顶了回去**；「从这一刻起，同一个地点本身成了案件」（导航一句话概括＋一句话总结） | `text/ch31_31.txt:74`「…The PO Box connection cannot be a coincidence.’ … ‘These two break-ins could be a coincidence. The murder happens at the same time someone else is targeting the area.’」 | 两句**主语不同且并存**，都是 Caius 的最终立场；原文无「推翻」动作、无「不再是巧合」的时刻；md 块 6 自己的「一松一钉」写法是对的 ⇒ md 内部打架 | **阻断** |
| A5 | md：「他替的不是自己，是住户」「先想到的却是邻居的安危」（块 4 为什么这样写） | `text/ch31_31.txt:44`「But I wouldn’t want to live on this square. **I’d be worried I would be next.**」 | 主语是 **Caius 本人**；md 同块「中文理解」「读者视角提示」写的是「下一个就是我」⇒ 自相矛盾 | **阻断** |
| A6 | md：块 2 分析讲「以为那不过是节目效果」「围观」 | `text/ch31_31.txt:32`「And everyone watching thought what? That it was a bit?」（在引语外）＋ md 引语只到 `:35` | 分析对象在**引语之外** ⇒ 引语选短（修法：引语向上扩到 `:32`，两句相邻） | **阻断**（对应组） |
| A7 | md：漏——Jimmy 未出版的回忆录 | `text/ch31_31.txt:110`「It looks like Jimmy wrote a memoir」；`text/ch33_33.txt:23,51`（成为正式线索） | 本章内不构成转折，但属线索层遗漏；`ch33` 把它变成「文学线索」三联之一 | **提示** |
| A8 | md：漏——后门「关着但没锁、可伸手开锁」 | `text/ch31_31.txt:50`「the back gate which was undamaged and closed but unlocked… You could pop your arm over and open the lock」；`text/ch37_37.txt:95`（后文「有人在找地下室」） | 本章唯一解释「外人如何进出而不被看见」的具体机制，未收 | **提示** |
| A9 | md：「还让斯科特去寄，好避开邮局监控里的那张脸」（块 7） | `text/ch31_31.txt:101`「using Scott to avoid being seen on the CCTV at the Post Office」 | 被「避免被看见」的是冒名者一方，斯科特是被利用去露面的人；「那张脸」无所指，易读反 | **提示** |
| A10 | md：「尸体出现在自家门前的石阶上／倒在自家门前的石阶上」（导航两句） | `text/ch31_31.txt:41`「the latest body found in the square」；`:38-41`（作业在花园一侧）；`:119`（从正门抬走）；`:47`（石阶是 Barry 假说里的**致伤处**） | 原文未给尸体落点；「石阶」属越界 | **提示** |
| A11 | md：「发现入室者都从绕整圈的后巷进」（导航） | `text/ch31_31.txt:56`「In both incidents **it would seem they probably** entered in through the back」 | 双重限定被丢掉，且只限「两起事件」 | **提示** |
| A12 | md：「广场上一万户人家，没有一个人看见」（块 2） | `text/ch31_31.txt:68`「**No one has a visual of the alley.**」（说的是摄像头，且在块 5 引语内） | 语义漂移：摄像头看不见巷子 ≠ 居民没看见任何东西 | **提示** |
| A13 | md：「作者把这一章收在一句反差上」（块 7） | `text/ch31_31.txt:125-137`（引语 7 之后仍有怀旧闲话至「Mine are yet to come」）；md 导航「叙事手法」自己写「章末用两人关于『从前』的怀旧闲话把气压慢慢放掉」 | 引语 7 不是本章末句；md 内部不一致 | **提示** |
| A14 | md：「巴里一句问话就把这桩案子的『第二次』讲了出来」 | `text/ch31_31.txt:41` 用词是「**latest** body found in the square」；「第二次」由语料层成立（`text/ch01_1.txt:17` Digby 死于同一条 Priory Square 的 Institute；`text/ch33_33.txt:243`） | 结论对，但不是本句字面；写明「全书的第二具尸体在此」即可 | **提示** |
| A15 | md 导航：「在分部『A THURSDAY IN MAY』里」 | `text/` 提取件**不含**分部页（`/usr/bin/grep -ril "thursday in may" text/` → exit=1）；但兄弟章一致：ch28/29/30/33/34 同标「A THURSDAY IN MAY」（ch21/25/27 为 A WEDNESDAY IN MAY，ch36/38/39 为 A FRIDAY IN MAY） | 与全书约定一致，**未核**（语料层无分部页可证），不判缺陷 | **跳过** |

### 假红 0 条 / 机器报警复核
- `chapter.sh` 退出码 0、`check_vocab.py` 退出码 0、`verify_corpus.py` 退出码 0——**没有机器报警需要分类**，本组无假红。
- 本次**未新写检查器**，也未据机器绿结论放行任何一类（漏/对应/说话人/施事归属/事实断言五类均由人判完成，见 `3-diff.md` 与 `4-correspondence.md`）。

---

## 三、R5-补 · 「零命中」类断言的自证

凡本文件写「本章没有 X」的，一律附命令、输出、退出码（显式文件路径 + `/usr/bin/grep`；不用 `git grep`，不用 rg 系默认 ignore 规则；不接管道以免吞退出码）。

```
$ cd notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text
$ /usr/bin/grep -inE 'crowd|onlooker|bystander|neighbou?r|resident|passer-?by|pedestrian' ch31_31.txt
113:‘Another book. What a literary neighbourhood.’
exit=0
```
⇒ 唯一命中是 `neighbourhood`（街区，玩笑用法）；**本章无居民、无邻居、无围观人群在场**。

```
$ /usr/bin/grep -inE 'police car|siren|ambulance|flashing light|blue light|van' ch31_31.txt
exit=1
```
⇒ **本章语料里没有警车／警灯／救护车**；本章专属判据所列的「警车」元素在 `text/ch32_32.txt:86`（"The police are outside again. There were loads of flashing lights."）才出现。

```
$ /usr/bin/grep -ril "thursday in may" text/
exit=1
```
⇒ 分部名不在提取件里（提取时丢了分部页），故 A15 记「未核/跳过」，不据此判 md 有编造。

---

## 四、R5.5 · 已核实为正确（防误修护栏）

以下写法**看似可疑、回原文核对后成立**，后续任何人不得以「读着不对」为由改动，除非能给出反证：

1. **死因的谨慎表述（本章专属判据点名的项目）**：md「法医初判为滑倒撞上铁栏杆的意外」「法医说像是滑倒撞上铁栏杆的意外」**正确**。原文 `text/ch31_31.txt:47`：「This one looks like an accident. The poor guy simply hit his head on the iron railing after slipping on the crumbling stone steps. … ‘I’ll obviously be a little more thorough than that in my report, but there’s no evidence of foul play.’」——**原文本身就没确诊死因**，md 用「初判」是恰当的，**不得改成确定死因或改成他杀**。
2. **死者身份**：md「前电视主持人吉米·琼斯」**正确**：`text/ch31_31.txt:23`「Jimmy Jones, forty-eight years old. You may well remember him from mid-two-thousands late-night panel shows.」；`:125`（`Besides, Jimmy Jones would’ve been on big money at the BBC then. He did a travel show, right? … And that late-night game show.`）。md 未写年龄，**不算漏**。
3. **块 6 的「一松一钉」分析**：`text/ch31_31.txt:74` 确为「could（松动）/ cannot（钉子）」两句并存，块 6 写对了。**A4 要改的是导航「一句话概括」「一句话总结」，不是块 6**——勿反向把块 6 改成「互相推翻」。
4. **「同一个广场的第二具尸体」成立**：第一次是 Digby（`text/ch01_1.txt:17` The Horatio Combe Institute, Priory Square, Camden；`text/ch33_33.txt:243`「highlighted Digby’s and Jimmy’s houses in red」）。md 写「第二次」**不算编造**。
5. **H1 `# 31. Priory Square`**＝epub 原章名 `text/ch31_31.txt:17`「Priory Square」，且与全书 54 章的「`# NN. <epub 章名>`」一致——**不得改成文件名里的描述性标题**。
6. **译名**：「迪吉」（Digby，全书 22+ 处）、「吉米·琼斯」「假伊索尔德／真实的伊索尔德」——与全书一致，**不得改动**。
7. **块 7 的引语截取方式**：引语从原句中段起（`text/ch31_31.txt:101` 的「"Fake Isolde" is clever…」），**连续无 `…` 拼接**，逐字成立——不属「拼接未写省略号」那类缺陷，勿误修。
8. **词汇表 29 条例句**全部逐字命中本章（`check_vocab.py` FAIL 0、ch31 0 WARN）；例句与 md 分析正文**不必**重复出现。

---

## 五、最要紧的一条

**A4（阻断）**：md 把 `text/ch31_31.txt:74` 里**主语不同、并列共存**的两句（Caius 的 PO Box 关联「cannot be a coincidence」＋ 两起入室「could be a coincidence」）写成「后者被前者顶了回去」，并据此造出本章专属判据点名要写的那个时刻——「办案者意识到这不再是巧合的那一刻」「从这一刻起，同一个地点本身成了案件」。**该时刻在 ch31 原文里并不存在**：Caius 的最终立场恰恰是「这两起入室**可以**是巧合」，谋杀之所以不是巧合，是因为它与「有人正在针对这一带」同时发生。md 自己的块 6 已经写对了这一点，导航与「一句话总结」把它推翻。⇒ 全章主旨（以及导航「一句话概括」「一句话总结」）目前建立在一个原文不支持的转折上，**这是本章唯一必须改的**。


---

## 书级例句全串核验（2026-10-21，主会话收口补记）

- 本章词表有 **5 条**例句未通过「全串逐字」核验（`check_vocab` 只取前 60 字符指纹，故判绿）：
  - `mews`：原文该句是叙述，md 加了开引号（阻断）
  - `accident`：原文该对白仍在延续，md 补了原文没有的收尾引号（阻断）
  - `crumbling`/`body`/`square`/`intruder`/`memoir`：直引号 ≠ 原文弯引号（提示级，已归一）
- 处置：阻断 2 条已按原文改正；提示 5 条的引号形态已归一为原文的 `‘…’`
- 详见 `.memory/raw-gates/a-fatal-legacy-by-charlotte-vassell/vocab-full-string-audit.md`（书级审计记录与探针说明）。
