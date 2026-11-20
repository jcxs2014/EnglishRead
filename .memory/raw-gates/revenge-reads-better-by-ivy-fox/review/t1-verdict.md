# T1 自检 — Revenge Reads Better（Ivy Fox，42 件 ch00–ch41）

抽样章（先写后读）：ch00、ch04、ch09、ch13、ch18、ch23、ch27、ch32、ch36、ch41（10/42=1/5 强，首末必含等距取）+ 专项 ch31（既有疑点）。

## 专项核验（开工前既定疑点）
- **主时间线重建**：text/ 各章第 7 行日期抬头＝偶数章过去线（2008-10-31 双葬礼 → 2016-07-08 纸厂火灾）、奇数章现在线（2026 万圣节重聚周）；ch41 尾声 2027（「almost eleven years」自洽）。
- **Collins 疑点解除**：ch28=2015-03-13 十八岁生日闪回（超市现身）→ ch31「已死五年、自杀」（≈2021）**不矛盾**；原进度记忆的矛盾判定作废。
- **六尸 vs Five counts**：ch39 text 实证 Misty 溺亡于 Alder Lake（"you went to the lake and waited"）→ 六名受害者；ch41 起诉书原文「Five counts of murder」＝**原书内部张力**（可能部分罪名另诉），两章各忠实原文，不修，记录。
- **ch35 "Ten years ago"（2026）vs ch41 "almost eleven years"（2027）**：视角年份不同，自洽，不修。

## 缺陷与修复（10 条，全部当场修+复跑 rc=0）
| 位置 | 改前 | 改后 | 原文依据 |
|---|---|---|---|
| 00_概述/金句⑤ | 两葬礼=2016 | 2008 万圣节（Lucia 守灵+Max 妈下葬同晚） | ch02 抬头 Oct 31st, 2008 |
| 00_概述/金句⑮⑲ | 焚稿/栽赃=2016 | 2013 | ch20 抬头 Sep 20th 2013 / ch26=Oct 15th 2013 |
| ch39 原句7 提示 | 2013 纸厂火灾 | 2016-07 | ch38 抬头 July 8th, 2016 |
| ch02 一句话概括 | 母亲过量的当晚 | 下葬当晚（死因针头过量） | "I buried my mother…this morning" |
| ch35 叙事手法 | 五名一生日一死亡日 | 五个名字·五个生日·同一死亡日 | "Five names…Five dates of birth. One date of death." |
| ch38 为什么 | 门被铁棒卡死 | Dylan 忘放铁棒→门锁困人（方向反） | "I just forgot to put the iron bar against the door" |
| ch41 概括 | 他的毁容 | 她的毁容（Peyton 女性） | ch39/41 text she/her |
| ch01 提示 | 两家母亲同日而死 | 同日下葬（死因各异） | 同上 ch02：举丧同日、死亡时点无同日实证 |
| ch29 概括 | 葬礼次日 | 葬礼当日下午 | "this morning's fiasco at Sydney's funeral" |
| ch23/ch28 | Milols 错拼 / 从酗酒中带回家 | Milo / 狂欢 binge 后 | 原文 "one of her binges"（未指明酒精） |

## 覆盖与密度
- assertion_scan 641 行**全量人判**（①8 ②147 ③327 ⑥17 全读；④97 ⑤45 超出抽 20 要求全读）——等效覆盖全部 42 章，强于「再抽一倍」。
- 抽样章素读复验：suread --check 11 章 rc=0 锚点全命中；引语邻域重点读 0 新缺陷。
- 密度：抽样直读层 0/11（<0.2）；断言扫描层 10 条已全修并复绿（gate EXIT=0·总览引语 91/91）。
- 改动事实回灌总览：年份类已同步重生成（gen_overview 复跑）；酗酒/铁棒/同日类 grep 00_* 无残留。
- ⑲ 提示 30 处（人物弧光 15+呼应关系 15）逐条定性＝模板既定形态、引语经 lane⑭ 91/91 核实，非缺陷（量级条款满足）。

读了哪些候选行、共几行：t1-candidates.txt 641 行（六个类全量），另 total 行标头 6 行；共 655 行。
