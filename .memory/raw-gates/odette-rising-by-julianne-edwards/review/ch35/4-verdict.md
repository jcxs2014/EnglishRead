# 4-verdict · ch35 the castle on rue des binelles（T3 深审 2026-11-18）

R1：子代理盲读 8/8（区间验证 0 失败）。R2：rc=0。R3：漏 1（轻微，提示不修）/ 编 0 / 错 0。
（T3 人判阶段已修：nav「丧子之痛的儿子」→「丧母之痛的儿子」——亲属关系硬伤，死亡者为其妻/其母。）

## 逐块判定（7 块）

| 块 | 断言 | 证据（text/ch35_chapter_35.txt） | 结论 | 档位 |
|---|---|---|---|---|
| 原句1 unmoored | 施事：不接 offer＝他；不快乐＝他 | "He was unhappy. Unmoored." | 对应 | ✅ |
| 原句2 fripperies | 忏悔＝他；逼走全家＝他 | "He had let them all down." | 对应 | ✅ |
| 原句3 beast | 反应差：aghast＝父；giggle＝子 | "His son, however, started to giggle." | 对应（含 T3 亲属修复） | 阻断→已修 |
| 原句4 halo | 施事：开门立于光＝她；仰望＝父子 | "She was an otherworldly being, an angel with a bright halo." | 对应 | ✅ |
| 原句5 nightmares | 说话人＝Odette（出示自己的狼梦）；听众＝男孩 | "Wolves. I was sometimes too scared to get out of bed." | 对应 | ✅ |
| 原句6 invitation | 说话人＝Odette；名单含 mice | "To the mothers, fathers, friends, and mice who are so loved" | 对应 | ✅ |
| 原句7 To return | 施事：起意回家＝他 | "If she would have him, he would come home." | 对应 | ✅ |

## 修复

1. nav「丧子之痛的儿子」→「丧母之痛的儿子」（阻断：亲属关系写反——亡者是 Beauclerc 之妻、男孩之母；text/ch35 "“She got consumption. It made her spit blood,” said the boy." 为证）。已跑 chapter.sh rc=0。

## 已核实为正确

- 原句2 「fripperies」＝原文逐字；md 分析「判词作废」建立在原文的忏悔句上。
- 原句3 「the antithesis of the symmetrical, classically proportioned house」＝原文逐字；md 分析「正负片」有据。
- 原句5 「They stop eventually.」＝原文逐字；md 分析「全书最轻的许诺」一致。
- 原句6 名单「mothers, fathers, friends, and mice」＝原文逐字；md 分析「哀悼清单民主化」有据。
- 词汇表 wrong-footed 例句 "She had wrong-footed him again."＝叙述逐字（施事＝她）。

已核实为正确（R5.5 固定节）：以上各条后续不得以「读着不对」为由改动，除非给出反证。
