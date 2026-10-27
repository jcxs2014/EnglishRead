# T1 自检结论 — off-the-reservation-by-stephen-graham-jones

抽样章：ch01、ch06、ch11、ch16、ch20（20 章按 1/4=5，首末必含、等距取；**先定后读**）。
另有：总览三篇全篇人判 + assertion_scan 六类候选行全量人读（①②③⑥全量，④⑤抽样 20 后因触发 T2 补至全量）。

## 整改清单（改前 → 改后｜依据）

| # | 位置 | 改前 | 改后 | 原文依据 |
|---|---|---|---|---|
| 1 | ch03 读者视角 | 「On his knees 在第一章也出现过（Nate 在雪地里）」 | 删虚假跨章指认 | ch01/ch02 text 均查无 knees/雪地跪 |
| 2 | ch03 中文理解 | Nessa「同母异父的妹妹」 | 「Nate 的妹妹」 | ch03 text 仅「Nate's little sister」；全书查无 half-sister |
| 3 | ch01 读者视角 | D 是前作 Denorah（「Nate 的女儿」） | 「同名同姓……本书中是与 Nate 同龄的恋人」 | ch15「Romeo and Juliet of the reservation」、ch20「Love you too」 |
| 4 | ch08 中文理解 | 「Mooch Pease」 | 「Mooch」 | 全书 text 查无 Pease；她姓 Lomas |
| 5 | ch09/概述/金句/情感节点 ×4 | 「卡莱尔老园丁之子」 | 「父亲曾在卡莱尔做工」 | ch09 text 行404「It was my dad who worked there」——职业未言明 |
| 6 | ch15 读者视角 | 「Sebby 在 ch11 被月亮人带走」 | 「仍昏迷在 Browning 的医院里」 | ch02「昏迷的 Sebby」、ch19「Dr. Rodge pronounced him」 |
| 7 | ch17 读者视角 | 「杀了她的儿子们（包括 Trace）」 | 「害死了她的家人（把丈夫 Trace 拉回毒品…）」 | ch06/ch07：Trace 是丈夫（植物人被她终结）；儿子=Shelby/Brady/Conrad |
| 8 | ch17 为什么这样写 | 「让 Nate 第一次看清」 | 「再次直面」 | ch07 已发现断舌（「Christian's tongue was blunt」） |
| 9 | ch19 为什么这样写 | 皮夹克「原本是 Nate 从 Sebby 那里拿的」 | 「本来就是他的（ch16 Mooch 拿它裹 Nate）」 | ch16 text「dragged Benjamin's leather jacket over」 |
| 10 | ch20 为什么这样写 | 「他等了 150 年」 | 「一百三十六年」 | ch02 text 行618「one hundred and thirty-six years」 |
| 11 | ch20 读者视角 | 「Nate 内心那个九岁的自己」 | 「还没长大的少年」 | 九岁是 Heavy Runner 男孩的年龄（ch02），非 Nate |
| 12 | 00_情感节点 节点三 | 「Night 三十点」 | 「那天夜里」 | 错字 |
| 13 | 00_情感节点 节点十二 | 「等了一百五十年」 | 「一百三十六年」 | 同 #10 |
| 提示 | ch05 读者视角 | 「曾祖母为迷路儿子点起的火」 | 「曾祖母让年幼的儿子点起、为迷路猎人引路」 | ch02 原句6：点火者=年幼的父亲，发起者=曾祖母（身份有据） |

## 数字/事实回灌总览（T1 第 4 步）

grep 00_*.md「九岁/同母异父/Pease/一百五十/150/Nate 的女儿/从 Sebby 拿夹克」→ 0 残留；概述「死于 1879 年」与 ch18「卡莱尔第一年」自洽。

## 覆盖与读行记录

- assertion_scan 命中 353 行：①10 + ②67 + ③141 + ⑥25 全量；④85、⑤25 先抽 20 后（触发 T2）补至全量——**共 353 行全读**。
- 抽样章素读复用：5 章 suread.json 均为写作期 8/8–10/10 全命中，T1 复跑无新增查无；抽 2–3 条事实回源（ch01 的钟、ch16 的 Pratt 化名、ch20 的 Impala）均命中。
- 总览：金句 25 条 + 情感节点 12 节点引语 58/58 可核实（gate ⑭）。
- 整改后 9 个受影响章节 chapter.sh 复跑全部 EXIT=0。

## 结论

阻断 12 条 + 提示 1 条，**全部当场整改完毕**；阻断密度 12/20≈0.6/章（候选行口径），触发并完成了 T2 全量覆盖。同一成因类（亲属/身份错置）跨 ch01/ch03/ch08/ch09/ch17 共 5 章——已在上方逐条修复。本 verdict 为同会话自检，非独立验收。
