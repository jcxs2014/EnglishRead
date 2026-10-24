# ch22 Russian Tea — 判定表

机器层：`bash scripts/chapter.sh ".../ch22 russian tea.md" --json` → **rc=0**，verdict=ok，
块数 9（限 2–15）、引语段 9（9/9 `ok:true`，查无 0）、空引号 0、子项缺 0、关键词坏 0、CJK 低 0、3581 词。
**机器 rc=0，人判 2 处阻断。**

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 引语逐字 | `2-machine.json` quotes 9 段全 `ok:true`（pos 90 / 448 / 2561 / 3761 / 4021 / 7074 / 8934 / 11909 / 18538） | 通过 | 假红（无问题） |
| 碰杯那句是本章题眼 | `text/ch22_russian_tea.txt:395` "“To life, out of order,” she says."；`:399` "“‘To world enough, and time,’” I reply. It was Henry’s favorite toast" | md 全文 0 次（`grep -nE "杯\|敬\|world enough\|toast\|干杯"` 退出码 1）；无块、无导航 | **阻断（漏）** |
| Beck 的丈夫活着 | `text/ch22_russian_tea.txt:127` "Jasper and I met in grad school, at MIT."；`:149` "He seems so lost."；`:150` "Beck sighs."（她仍在说这个人现在怎样） | md:11"刚失去丈夫"、md:13"各自带着亡夫" | **阻断** |
| Beck 的女儿出生即死 | `text/ch22_russian_tea.txt:141` "We had a daughter. She died at birth." | md 未收（`婴儿`=0） | 提示 |
| 大选段被写成"不能改"的实例 | `text/ch22_russian_tea.txt:364` "I lower my voice and start to tell her about the 2016 presidential election."；`:369` "“We don’t,” I say gently. “We can’t.”" | 仅 md:13 Tropes 一笔带过，无块 | 提示 |
| 这顿饭是晚饭 | `text/ch22_russian_tea.txt:25` "rush-hour crowds"；`:395` "The waiter places glasses of wine in front of us." | md:21"一顿午饭"（md:12 却写"晚饭"） | 提示 |
| 裸体 Alba 的年龄 | `text/ch22_russian_tea.txt:18` "(Clare is 38, Beck is 34, Alba is 36)"；`:187` "she might be in her late thirties" | md 只写"成年的女儿""三十几岁"，未给"她此时 36 岁、来自更晚的年份" | 提示 |
| 宗教对照 | `text/ch22_russian_tea.txt:299` "both sides of my family have been various sorts of Quakers going back to Underground Railroad times"；`:312` "it was like a power failure, pfft, dead." | md 无（`贵格`=0） | 提示 |
| 结尾那句好消息 | `text/ch22_russian_tea.txt:387` "“Gene therapy works. They announce it next year.”" | md 无（`基因`=0） | 提示 |
| 形态：H1「22. Russian Tea」、导航 5 项、四子项齐、9 块 | `2-machine.json` form 全绿（h1_shape_ok true、nav_count 5、block_range 3–10、block_median 6） | 通过 | 假红（无问题） |

## 报数（四组）

- **逐字**：9/9 通过，0 失败。
- **对应**：9 块全通过（无一块越出引语）。
- **形态**：全绿。
- **断言**：13 条断言，4 通过、**2 阻断**、7 提示。

**本章 rc=0，但 2 处阻断都出在"块与块之间"：题眼碰杯被整段跳过、Beck 的丈夫被写成亡夫。**

**改法**：
1. 新增第 10 块，引语取 `text/ch22_russian_tea.txt:395-399`（"To life, out of order," … "It was Henry's favorite toast"），并在导航 md:11 与 `## 一句话总结` md:142 末尾各补一句"碰杯：她敬'失序的人生'，Clare 用 Henry 最爱的那句'To world enough, and time'回应"。
2. md:11「两个刚失去丈夫的女人」→「一个死了丈夫、一个丈夫『lost』的女人」；md:13「两人各自带着亡夫」→「两人各自带着一个回不来的男人」。

## 已核实为正确（防下一轮误修）

1. `text/ch22_russian_tea.txt:18` "(Clare is 38, Beck is 34, Alba is 36)" —— 裸体 Alba 是 **36 岁**的版本；md:69"三十几岁"没有写错，勿改成"四十岁"。
2. `text/ch22_russian_tea.txt:85` "“Alba is eight.”" —— 饭桌上那个 Alba 是 8 岁；md 未写不算错，若补写勿写成"六岁"。
3. `text/ch22_russian_tea.txt:93` "“. . . Henry died? She was five.”" —— Henry 死时 Alba 五岁；与前章"Henry 死于 2007"一致。
4. `text/ch22_russian_tea.txt:187` —— 是 Alba **先**说 "Sorry! Sorry!" 再走向桌；md:11"闯进来"未歪曲，勿改成"Clare 把她拉进来"。
5. `text/ch22_russian_tea.txt:214` "Um, can I borrow your shoes?" —— 她借的是**鞋**（外套是 Clare 披上的、围巾是给的、面包与二十元钞票也是给的）；md:11"用外套裹住她、塞给她面包和钱"**没有把外套写成"借"**，正确。
6. `text/ch22_russian_tea.txt:224` "Charisse told me." —— 是 **Charisse** 把时间旅行的事告诉了 Beck，不是 Clare 当场说的；md:11"Clare 却说不出口时间旅行的实话"与 md:14"破了多年的保密习惯"需并读才不矛盾（她后来讲的是**规则**，不是"我丈夫会穿越"这件事本身）。
7. `text/ch22_russian_tea.txt:245` "If my grown-up Alba is unsurprised to see you, it bodes well." —— "好兆头"指**两人会成为朋友**，不是指 Alba 平安；md 未误植。
8. `text/ch22_russian_tea.txt:426` "“The lady took care of it,”" —— 车费与账单都是 **Beck** 付的；md:11 未写"谁付账"，勿补成 Clare。
9. `text/ch22_russian_tea.txt:336` "there was a doctor at University of Chicago who published a paper—" / `:341` "“David Kendrick,” I tell her." —— 医生说 **David Kendrick**，是 Henry 的医生、Alba 仍在他那里看；md 未提不算错，补写时勿写成"Kendrick 医生是 Beck 的医生"。
