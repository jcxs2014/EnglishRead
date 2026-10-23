# ch35（Chapter Thirty-Four）判定表

- 素读：`1-suread.json`（19 facts / MISS 0；R1 由子代理素读，回执经 /tmp/s35.py 全量回源核验）
- 机器层：`2-machine.json`（chapter.sh rc=0；6 引语块逐字 0 MISS）
- 探针：v35 词表 13 行 flagged 0；ap35 直撇号 1；in35 越 19/书 仅 2 模板例外
- 档位：深审（用户升级）；章号偏移：本 md＝Chapter Thirty-Four

## 报数（四组）

| 组 | 结果 |
|---|---|
| 逐字 | 6/6 引语块逐字 0 MISS；词表例句 13/13 |
| 对应 | 6/6 块「中文在讲这句引语」，施事/归属无反转 |
| 形态 | H1、导航 4 项、子项集、块数 6 落在本书建议区间 |
| 断言 | 13 条内嵌英文/事实断言回源命中；1 条撇号（C-35-1）、1 条译法提示（P-35-1） |

## 判定

| 编号 | 断言 | 证据（text/ch35_chapter_thirty_four.txt） | 结论 | 档位 |
|---|---|---|---|---|
| C-35-1 | md L44 引原文 "I'd been out cold" 用 ASCII 直撇号 | L69 逐字："While I'd been out cold in the tower…"（弯撇号） | 引语字形失真，沿先例 | 阻断 |
| P-35-1 | 导航「他用"是它们开的门"回应她」 | L75 "They opened the pond gates."；L81 "I didn't see who did it."——"They" 无人称实指，"它们"属过度确定 | 措辞正当性存疑，改法见修复指令 | 提示 |

## 修复指令（不改稿，供汇总）

1. `ch35 herder in the fog.md` L44：`I'd`→`I’d`。
2. 同 md 导航：「他用"是它们开的门"回应她」→「他用"是'他们'开的门"回应她（原文 They，无人称实指）」或等义保留原文。
3. 改完重跑 chapter.sh 与 ap 探针。

## 已核实为正确

1. 「与 Nova 约定'谁被抓谁顶罪'」：L168 "we'd already agreed what would happen if one of us got caught" ＋ L165 "you let Nova take the blame"（他未否认）——压缩合理，约定内容（顶罪）有 L165 侧写支撑。
2. 「通电赶牛棒」：cattle prod 为通电驱畜棒的定义性事实，原文 L90/L203 用具名，无需原文再证。
3. 「先让她拼出结论（he did it）」：L69 "Of course he was behind the problems at the farm."——"he did it" 为叙事手法层的转写简称，非原文明句，未作引用宣称。
4. 「留下的背包」与「追到车窗的呼喊」两面：L18 "His backpack still leaned against the wall" ＋ L213 "pounding on the window"。
5. 农场名 "Greer Fine Alligators" 逐字：L228。

## 覆盖声明

深审 R1–R5 全流程（素读 19 facts / 机器层全量 / 三张单子 / 逐块对应 6/6）。

## 汇总

- 阻断 1 ／ 提示 1 ／ 假红 0
- 累计进度：深审人判 37/49 章（ch35 完；余 ch37、ch38、ch40–ch48）。
