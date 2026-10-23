# ch34（Chapter Thirty-Three）判定表

- 素读：`1-suread.json`（19 facts / MISS 0；R1 由子代理素读，回执经 /tmp/s34.py 全量回源核验）
- 机器层：`2-machine.json`（chapter.sh rc=0；9 引语块逐字 0 MISS）
- 探针：v34 词表 13 行 flagged 0；ap34 直撇号 6；in34 越 19/书 仅 2 模板例外
- 档位：深审（用户升级）；章号偏移：本 md＝Chapter Thirty-Three

## 报数（四组）

| 组 | 结果 |
|---|---|
| 逐字 | 9/9 引语块逐字 0 MISS；词表例句 13/13 |
| 对应 | 9/9 块「中文在讲这句引语」，施事/归属无反转 |
| 形态 | H1、导航 4 项、子项集、块数 9 落在本书建议区间 |
| 断言 | 11 条内嵌英文/事实断言回源命中；时间断言 1 条错（C-34-1） |

## 判定

| 编号 | 断言 | 证据（text/ch34_chapter_thirty_three.txt） | 结论 | 档位 |
|---|---|---|---|---|
| C-34-1 | 导航与原句 1 中文理解作「八点整」 | L9 逐字："Harrison knocked on the front door at eight thirty on the dot." — "on the dot"＝准时，eight thirty＝八点半 | 时间错译，两处同改 | 阻断 |
| C-34-2 | 分析层引原文片段 5 处用 ASCII 直撇号（L54 couldn't；L74 he'd、we'd；L84 You're；L94 I'd） | 原文全部为弯撇号：L18 / L280 / L297 / L327 | 引语字形失真，沿 C-25-3 / C-28-2 先例 | 阻断 |
| P-34-1 | L135 释义 "under one's breath" 用直撇号 | 词典引理形态（原文 L72 "under his breath"），非引原文 | 随批统一改弯撇号 | 提示 |

## 修复指令（不改稿，供汇总）

1. `ch34 surveillance night and first move.md` 导航首句：「Harrison 八点整敲门」→「Harrison 八点半准时敲门」。
2. 同 md 原句 1 中文理解：「Harrison 八点整准时敲了前门」→「Harrison 八点半准时敲了前门」。
3. 同 md 5 处直撇号改弯撇号：L54 `couldn't`→`couldn’t`；L74 `he'd`→`he’d`、`we'd`→`we’d`；L84 `You're`→`You’re`；L94 `I'd`→`I’d`；L135 `one's`→`one’s`。
4. 改完重跑 `bash scripts/chapter.sh "<该 md>"` 与 ap 探针，确认 ASCII 0。

## 已核实为正确

1. 「撤回与盛赞在同一独白序列先后出现」：L276（撤回）与 L297（盛赞段）之间仅有她的短反应与他的 "I'm not finished"，属同一场坦白。
2. 「本章没有任何一次异常被实际证实」：L177 "I didn't feel any kind of presence—not a supernatural one, at least."＋L204 后无异常发生，监视落空（L408 睡着）。
3. 「愿 Ironheart 把 Harrison 从塔上甩下去」：L288 "I wouldn't have minded if Ironheart used his malevolent will to hurl Harrison off the tower."——md 概括与原文方向一致（她不介意，非主动诅咒）。
4. 「他打算离开农场」有双重支撑：L312 "I won't stay here. I can't." 与 L329 "I don't want to start anything with someone who may make it difficult to leave."
5. 「平生第一次主动」：L327 "Something I'd never done before, had never even dreamed of doing."（引语逐字在块内，语义概括无放大）。

## 覆盖声明

深审 R1–R5 全流程（素读 19 facts / 机器层全量 / 三张单子 / 逐块对应 9/9）。

## 汇总

- 阻断 2 ／ 提示 1 ／ 假红 0
- 累计进度：深审人判 40/49 章（ch34 完）。
