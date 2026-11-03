# 4-verdict · ch01（Prélude）

覆盖声明：R1 子代理素读（text-only，8 事实）→ R2 机器层（chapter.sh --json rc=0）→ R3 对账 → R4 逐块 7/7。

## 判定表

| 断言 | 证据（章:区间） | 结论 | 档位 |
|---|---|---|---|
| 块 3 分析含引语外内容（Rheal 去北林） | text/ch01_prelude.txt [3093:3180]（1-suread.json 事实③区间；引语原起点在 "Or at least"） | 引语选短，扩至同段完整段（96 词） | 阻断→已修 |
| 块 5 分析含引语外内容（「远谈不上」对话） | text/ch01 [8xxx]（"Am I hallucinating?…Hardly." 段） | 删分析外延句 | 阻断→已修 |
| 块 6 分析含引语外内容（「邻里需要你领导」句） | text/ch01 [9800 附近]（"your neighbors are going to need you to lead"）——与引语不相邻 | 删分析外延句（保留于导航/总结） | 阻断→已修 |
| 块 7 分析含引语外内容（「自己那杯洗了」「母亲消失后」） | text/ch01 [12200 附近]（"Then she was gone…rinsed the mug"） | 删改至引语范围 | 阻断→已修 |
| 块 1/2/4 关键词、施事、对应 | 逐块人判：主语/受事与原文一致；关键词均在引语内 | 正确 | 通过 |
| 导航「29 岁 / 死去十年 / Huntington's」 | text/ch01 [1063:1207]/[3367:3435]（1-suread） | 正确 | 通过 |
| 「1984-08-27」日期 | text/ch01 首段 "August 27, 1984" | 正确 | 通过 |
| 素读⑥咖啡/香烟成形未设块 | md 块 7 分析已引用该规则 | 取舍成立 | 跳过（不必修） |

## 修复后复验

chapter.sh rc=0（7 块/7 片段查无 0）；引语长度全部 ≤100 词；修复未触发新报警。

## 已核实为正确

- 块 2 读者视角提示「1900 年、240 吨、大萧条零失业」：三数均在 text/ch01 [1459:1603]（素读②区间 "Since 1900 it had rolled out…240 tons of paper a day…not one person in Waterville had lost their job"），虽引语只取后半段，数字为本章事实且提示明写「记牢这组数字」——**正确，不得删改**。
- 块 3「做头发」比喻、块 5「刺穿其肺」：与原文 "having her hair set" / "stabbed him in the lung" 逐字对应。
- 块 4 「比春节攻势的新闻早了几小时，比…敲门早了三天」：与原文 "hours before…the Tet Offensive…three days before" 一致。
- 块 7 「显灵头一回留下了物证」：素读⑧（倒扣空杯）为原文事实，解读合理。
