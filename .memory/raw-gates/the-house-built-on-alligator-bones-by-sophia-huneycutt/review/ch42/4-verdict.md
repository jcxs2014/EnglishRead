# ch42（Chapter Forty-One）深审 R5 判定

> 机器层：`2-machine.json` rc=0，10 块精读，segment_miss 0。
> R1 素读：`1-suread.json` 20 facts，全部回源命中（MISS 0）。

## R3 三张单子

- **词表**：v42 探针 25 行，flagged 1（batshit 例句截断补引号）→ 假红 F-42-1，其余 24 行逐字命中。
- **撇号**：ap42 直撇号 token 0，backtick span 0。
- **块内嵌英文**：in42 未命中 3，模板 2，其余 1 项为跨章回指（F-42-2）。

## 判定汇总

- **阻断：0**
- **提示：0**
- **假红：2**
  - **F-42-1**：词表 batshit 例句在原文 L99 于 "And passionate." 处截断并补收尾引号，flat 串因此不命中；例句内容逐字有据（截断型，与词头式假红先例同族）。
  - **F-42-2**：原句6 分析层引 "rotten to the core"——本章查无，ch41 L144 有原文（Caroline："Said we were rotten to the core, herself included."）；跨章回指成立，非凭空。

## R4 逐块对应（10 块）

| 块 | 取证（text/ch42_chapter_forty_one.txt） | 结论 |
|---|---|---|
| 原1 Honda／foot-long crack／installed／last guest | L9 逐字 | ✓ |
| 原2 party／sacrificing／million | L21 逐字 | ✓ |
| 原3 imagined rifle／coal-black／worth keeping alive | L27 逐字 | ✓ |
| 原4 sorrowful／rampage／storm shutters／get out | L51＋L57 逐字 | ✓ |
| 原5 started to like her／batshit／passionate | L99 逐字 | ✓ |
| 原6 police／manslaughter／fifteen or twenty | L108 逐字 | ✓ |
| 原7 grimly／empire／dominate nature | L135 逐字 | ✓ |
| 原8 pushed her—hard／bed frame／glazed over | L195 逐字（suread）＋L162 heart attack 前文 | ✓ |
| 原9 old part of me／dangerous／safer alone | 引语逐字 | ✓ |
| 原10 pang of guilt／worn socks／slipped out | L351 逐字（suread） | ✓ |

## 导航层断言

20 项断言（Haints didn't sit on couches L30、stone-cold bitch of a haint L102、psychopath L144、vase/sunning alligator halved L132、technically died of a heart attack L162、"Then maybe you shouldn't," coldly L183、evil person wouldn't regret/He didn't return to the couch L213、"This family is all I have" L240/270、"You have me" L273、to keep me out of the storm L276、That, or they trusted me. They shouldn't have. L348、skeleton key L9、take me for a fool L315、so tired of being angry L66、"Why are you telling me this?" L204、empire/dominate nature L135、watery red paint/break the façade L45）——全部回源命中。

## 已核实为正确

- 引语 10 块逐字；词表 25 行词头全在本章、例句 24 逐字＋1 截断型假红。
- 撇号全弯；时序（雨夜进门→火边对谈→供述→瓷瓶投票→偷钥匙）与原文一致；无数量断言异常。
