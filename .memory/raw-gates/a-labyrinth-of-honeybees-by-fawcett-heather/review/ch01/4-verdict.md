# ch01 The Royal Inquisitor — R5 判定表

审查路径：R1 素读（子代理，仅读 text/ch01，未给审查表）→ `/tmp/t3_validate.py` 锚点负对照 → R2 `chapter.sh --json` → R3 对账（`3-diff.md`）→ R4 逐块语义核对 → 本表。
md：`notes/books/short-story-anthologies/a-labyrinth-of-honeybees-by-fawcett-heather/ch01 the royal inquisitor.md`

## 一、四组报数

| 组 | 数 | 结果 |
|---|---|---|
| 逐字 | 引语块 4 / 分段 4 / 查无 0 | ✅ 4 块引语全部回 `text/ch01_the_royal_inquisitor.txt` 逐字成立 |
| 对应 | 5 处断言（导航 4 项 + 总结 1）＋ 4 块 ×5 子项 = 25 项逐块核对 | 24 项成立；1 项措辞不准（见 错-1） |
| 形态 | H1 `01. The Royal Inquisitor` ✅ / 导航 4 项 ✅ / 块数 4（契约 3–10）✅ / 引语 >100 词 0 ✅ | ✅ |
| 断言 | R3 三单：编 1、漏 2、错 2（共 5 条） | 阻断 1 / 提示 4 |

R2 机器层（`review/ch01/2-machine.json`，rc=0）：`verdict: ok`，`quotes 4 / blocks 4`，`segment_miss 0`，`struct_bad 0`，`empty_quote 0`，`keyword_bad 0`，`cjk_low 0`，`template 0`，`hole 0`，`quote_long 0`，`words 1409`，`block_limit {lo:2, hi:15}`。

## 二、R4 逐块核对（只问：这段中文是不是在讲这句引语）

| 块 | 引语出处 | 追问①主语 | 追问②受事 | 追问③谁的/谁欠谁 | 结论 |
|---|---|---|---|---|---|
| 原句 1 | ch01:3 | 那死人 glaring（主语＝死者） | 「我」被他瞪着 | 洞在他喉咙上（his throat） | ✅ 对应 |
| 原句 2 | ch01:12 | 幻象 overtook「我」；脸 flitted across **审问官**的脸 | 叙述者被幻象攫住 | 那些脸属于审问官（the royal inquisitor’s） | ✅ 对应；md:37 段落先后说反（错-1） |
| 原句 3 | ch01:24 | 「我」假装整理围巾 | 动作指向**自己的**围巾 | 围巾是「我」的（my scarf / It’s embroidered） | ✅ 对应 |
| 原句 4 | ch01:27 | 他 swept gaze over me | 受事＝叙述者 | 特征全属「我」（my elbows / my face / my hair） | ✅ 对应 |

未发现施事归属反转、说话人错配或引语与中文脱节。

## 三、判定

| 断言 | 证据（章:区间） | 结论 | 档位 |
|---|---|---|---|
| md:10 导航「两名税吏**溺死**蓝河」 | ch01:40–42（尸体在蓝河被发现；她自己说 `If they fell`）；`/usr/bin/grep -rn -iE "drown" text/` 仅 ch05:203 比喻用法，rc=0 但无关 | 原文无溺死机制，属 md 增写死因 | **阻断**（已修，见下） |
| md:10/12 未记「鬼魂先到 ＋ 喝止／圣地」 | ch01:1–3 | 覆盖取舍，非失实 | 提示 |
| md 全篇未记「女鬼进了圣迷宫」 | 素读第 2 条；ch04:37＋:55 为该线的兑现 | 伏笔线未记 | 提示 |
| md:37「前一段刚写他身后跟着一大群鬼」 | 原句＝ch01:12，而「horde」句在 ch01:14（原句之后） | 段落先后倒置 | 提示 |
| md:10「并答应带他去看现场」 | ch01:44–46 他只要「find a murderer」；带路在 ch02:1 | 跨章预叙 | 提示（随修复一并删除） |

**本章阻断 1 条**（编-1：溺死），当场修复；其余 4 条为提示，均不改事实主干。

### 修复记录（修前 → 修后）

- **修前** `ch01 the royal inquisitor.md:10`：`调查两名税吏溺死蓝河一案；守园的女祭司藏起身份，自称 "the groundskeeper"，并答应带他去看现场。`
- **修后** `ch01 the royal inquisitor.md:10`：`调查两名税吏死在蓝河一案——尸体在蓝河被发现，死因其实是"跌下去了"；守园的女祭司藏起身份，自称 "the groundskeeper"。`
- 依据：ch01:40 `Their bodies were found in the Blue River.`；ch01:42 `If they fell, I had no part in it`。
- 同时删除跨章预叙的「并答应带他去看现场」（带路在 ch02:1）。
- 复验：`bash scripts/chapter.sh "…/ch01 the royal inquisitor.md"` **rc=0**（块数 4，机器层无阻断）；`python3 scripts/corruption_scan.py "<书目录>"` FAIL 0。

## 四、已核实为正确

| 断言 | 证据 | 结论 |
|---|---|---|
| 人脸「十二张」（md:33） | ch01:12 `The faces of a dozen people` | ✅（T1 已由「十几张」修正） |
| 叙事手法引 `This was both true and untrue`（md:13） | ch01:34 逐字 | ✅ |
| 块 3「审问官刚问『那你是……』」（md:51） | ch01:23 `Then you are . . . ?` 说话人＝审问官 | ✅ |
| 总结「审问官带着他杀过的人」（md:101） | ch01:12 幻象 ＋ ch02:29 `those he had killed` | ✅ |
| 块 4「I was sun freckled … congruous with …」三处语法说明（md:67） | ch01:27 原句（独立主格、形容词短语后置） | ✅ |
| 导航「守园的女祭司藏起身份，自称 the groundskeeper」 | ch01:21–25 | ✅ |

## 五、同会话自检已知盲区

- 本表由**生产同一会话**出具（非异会话独立复核），R4 语义二审由我本人执行，无法提供第三方盲读背书。
- 词表例句的「本章逐字」由 `chapter.sh` 机器层保证；词义释义的中文准确性不在机器判据内，本章 12 条释义经我逐条比对原句语境，未发现与句意冲突。
- ch05:203 的 `drown` 比喻用法是本次「溺死」取证的唯一 dump，已核对与税吏无关。
