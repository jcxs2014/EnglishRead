# 4-verdict · ch19 it was hope（T3 深审 2026-11-18）

R1：子代理盲读 8/8（区间验证 0 失败）。R2：rc=0。R3：漏 1（轻微，提示不修）/ 编 0 / 错 0。

## 逐块判定（15 块）

| 块 | 断言 | 证据（text/ch19_chapter_19.txt） | 结论 | 档位 |
|---|---|---|---|---|
| 原句1 Eugénie | 施事：抢门报家底＝Eugénie | "“She doesn’t have a housekeeper or anyone,” and raced from the room." | 对应 | ✅ |
| 原句2 teacup | 施事：倒茶杯＝Merry；接杯豪饮＝Berthe | "he poured it into a teacup and thrust it at Berthe... with exaggerated care, and drank." | 对应 | ✅ |
| 原句3 toast | 说话人＝Berthe；举杯三人＝女人们 | "we must salute those we have lost and never forget that we once were loved." | 对应 | ✅ |
| 原句4 fire/snake | 施事：亮袜=Berthe；受审=Beauclerc；「affront to the name Huré」=转述 de L'Estrange | "Huré needs someone with fire" | 对应 | ✅ |
| 原句5 shattered | 施事：认输离席=Beauclerc | "“No, madame, I’m not sure I have,” he said and all but ran from the room." | 对应 | ✅ |
| 原句6 line | 说话人=Berthe；「line=命」=其设计论 | "It’s dependent upon the line." | 对应 | ✅ |
| 原句7 Gagnon | 说话人=Berthe；勒索逻辑=黑心人 | "he might come to you for more." | 对应 | ✅ |
| 原句8 poor girl | 施事：抚脸=Berthe；融化=她 | "She reached out and touched Odette’s face, tracing the line of it" | 对应 | ✅ |
| 原句9 unheroic | 说话人=Berthe；命令对象=Odette | "He is unheroic. Find help." | 对应 | ✅ |
| 原句10 herons card | 施事：画鹭=沈 Arielle；赞叹=她 | "They were perfect." | 对应 | ✅ |
| 原句11 dolt | 自判=她；翻案=Beauclerc 是好人 | "Beauclerc was a good man, honest and hardworking, whose anger was often fueled by principle." | 对应 | ✅ |
| 原句12 likable | 施事：镜像更换=朋友们；改变=她 | "reflected in their eyes she saw parts of herself that were likable" | 对应 | ✅ |
| 原句13 leaving | 说话人=Arielle；一周死线 | "We will quit our house within the week. We have to go." | 对应 | ✅ |
| 原句14 defiance | 说话人=Odette；bullies=房东等 | "Surely the greatest act of defiance would be to be happy?" | 对应 | ✅ |
| 原句15 hope | 独词段=叙述层顿点 | "It was hope." | 对应 | ✅ |

## 修复

无阻断。

## 已核实为正确

- 原句4 「Auguste de L'Estrange at Printemps」＝原文逐字（买家姓名/商场名核对无误）。
- 原句6 「they speak to no one」＝原文逐字；md 分析「line=命」公式建立在原文三段推论上。
- 原句11 「sanctimonious dolt」＝原文逐字（她原先的判词）。
- 原句13 「It matters not what you say」＝原文逐字；md 转述「你说什么都没有用」一致。
- 原句15 七词终段与门禁的短引语兜底命中记录一致（check_short_quotes 命中 2 之一）。

已核实为正确（R5.5 固定节）：以上各条后续不得以「读着不对」为由改动，除非给出反证。
