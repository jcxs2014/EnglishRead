# ch40（Chapter Thirty-Nine）深审 R5 判定

> 机器层：`2-machine.json` rc=0，6 块精读，segment_miss 0。
> R1 素读：`1-suread.json` 13 facts，全部回源命中（MISS 0）。

## R3 三张单子

- **词表**：v40 探针 20 行，例句逐字命中 20／20。
- **撇号**：ap40 直撇号 token 0，backtick span 0。
- **块内嵌英文**：in40 未命中 2，均为模板（Chapter Thirty-Nine／Tropes）。

## R4 逐块对应（6 块）

| 块 | 取证（text/ch40_chapter_thirty_nine.txt） | 结论 |
|---|---|---|
| 原1 纵火报告／两本同日不同额的账 | L21 逐字 | ✓ |
| 原2 gathering evidence／must not have known／sentiment | L24 逐字 | ✓ |
| 原3 hit at once／double time／stopping himself | L57 附近（引语逐字，机器层+suread 核） | ✓ |
| 原4 hurled／exploded／flinched／eyes locked | 引语逐字 | ✓ |
| 原5 confronted／money to stay quiet／summer job／spy | L123 逐字 | ✓ |
| 原6 directly under／rippling／billowing／swear | L216 逐字 | ✓ |

## 导航层断言

| 断言 | 取证 | 结论 |
|---|---|---|
| 撬棒别开锁箱（梳妆台上） | L9／L12 crowbar | ✓ |
| 纵火报告／两本账／市长贺信／George R. 便条（Publix、蛋数） | L21 逐字（Brian Yelton 拼写一致） | ✓ |
| 父＝Leon 最好的朋友 | L42 "Best friends." | ✓ |
| 目击、收钱沉默、病重、派子监视 | L123 逐字 | ✓ |
| 砸酒杯、凉风奖励、reined in my fury | L84／L87 | ✓ |
| Tell me everything.／That's over. | L90／L180 | ✓ |
| "Ask Ginny"／"Gazzie's dangerous" | L201 | ✓ |
| 抱文件走进八点暴雨；Gazzie 那句话 | L222／L228 | ✓ |
| He wasn't even my boyfriend…／You should hear it from family | L195／L192 | ✓ |
| Ida 撮合争吵（wanted me to argue with Harrison） | L84 | ✓ |
| honest by nature／spin lie after lie／refused to let my anger die | L174／L177 | ✓ |
| 毁财产、用刀传话、怕她和她一样 | L159／L165 | ✓ |
| 清单手法 The first…Next…Then…Finally | L21 | ✓ |
| "Spy." This was getting more and more ridiculous. | L126 | ✓ |
| Why would I listen to you? Or her? | L204 | ✓ |
| beach ball／six summers ago | L138 | ✓ |
| 判断力自陈（alligator farming law） | L21 句尾 | ✓ |

## 判定汇总

- **阻断：0**
- **提示：0**
- **假红：0**

## 已核实为正确

- 引语 6 块逐字（s40 13 facts MISS 0；机器层 segment_miss 0）。
- 词表 20 行例句逐字；人名拼写（Brian Yelton、George R.、Ginny）与原文一致。
- 撇号全弯；导航/弧线/手法层 17 项断言全部回源命中；时序（撬箱→清单→家世→发作→听真相→出门）与原文一致。
