# ch26 判定表（R5）

书：the-house-built-on-alligator-bones-by-sophia-huneycutt｜章：ch26（Chapter Twenty-Five）
档位：**深审（用户升级，全章 R1–R4 串行）**｜日期：2026-10-23
text：`text/ch26_chapter_twenty_five.txt`（243 行／1,939 词）｜md：`ch26 dart confronts nova.md`

## 四组报数

| 组 | 结果 |
|---|---|
| 逐字 | 引语块 6／片段 6／查无 0（机器＋人工 6/6）；词表 15 行例句逐字（flag 0）；ASCII 撇号 0；非块内嵌英文全书查无 0（模板例外 2） |
| 对应 | 阻断 2（C-26-1「烧」凭空改动作；C-26-2 开篇梦整段漏登记）；提示 4（P-1 时距、P-2 满身血、P-4 电话内容漏、P-5 giggle 归属） |
| 形态 | H1 `26. Chapter Twenty-Five` ✅｜导航 5 项 ✅｜块数 6（建议 4–6）✅｜词表三档 5+6+4=15 ✅ |
| 断言 | 提示 3（P-3「确实涉案」、P-6「无出处」、P-7「第一次」）——无阻断级断言 |

## 阻断 2／提示 8／假红 11／不许裁决 8

- **C-26-1**（对应·凭空）：md:11「只**烧**一个棚」→ 原文是 kudzu 缠死（:54/:60），非纵火。改「只缠一个棚」。
- **C-26-2**（对应·漏承重）：开篇的梦（:12 沼泽＋步枪＋gentle hand＋无形存在摆姿势＋背上目光）md 零登记——本章超自然线第一拍、ch20 冷手线的直系延续。
- 提示 8 条见 3-diff.md（含 P-8「外婆/祖母」全书称谓统一问题：Gazzie＝Caroline 之母，「外婆」就亲缘而言更准，但须整书统一，不由单章擅改）。

## 假红（已核实为正确——防下一轮改坏）

1. 「Nova 头一回打断 Gazzie」＝:24（restraint she'd shown before）支持。
2. 「眼放光追出去」＝:237 逐字。
3. 「keeping my head straight」＝:51；「Good，不用马上见他」＝:27。
4. pause 链四条引文＝:99 逐字。
5. 两句短判断（This was not normal.／This was Ironheart.）＝:63/:66。
6. 内心两分引文＝:111 逐字。
7. block2/3/4/6 分析层引文全部逐字。
8. 机器层四件全绿复核属实（引语逐字／词表例句／内嵌英文／块数 6）。

## 不许裁决（8 条）

见 3-diff.md「不许裁决」节：电话 she 的指代两读／Nova 是否实施者／killer 的两读／Gazzie 是否伤 Nova／梦之手与冷手同指？／Joe 是否同伙／屋内怪事是否人为／三种死法书级护栏。

## 覆盖声明

- 本章人判覆盖：R1 素读 84 facts／MISS 0 ＋ R3/R4 全 md 精读 ＋ R5 判定表（**深审全章**）。
- 机器层：`bash scripts/chapter.sh` rc=0（输出存 `2-machine.json`）。
- 探针：v26（15/0）、ap26（撇号 0）、in26（114 串／查无 2 模板例外）、span26（见下）。
- 分工：审查方**只出指令不改稿**；修复由执行方按 `2026-10-23-复核与修复指令.md` 执行后回执复核。

## 探针自检

`/tmp/span26.py`：反引号 span 41 条／MISS 4——`Chapter Twenty-Five`×2 与 `Tropes`（模板级）、`26. Chapter Twenty-Five`（H1 引用，模板级）、`maybe…were, too`（省略号拼接，整段逐字：`grep -c "maybe Greer House’s oddities were, too"`＝1）；`/tmp/v26.py` 词表 15 行／flag 0；`/tmp/ap26.py` ASCII 撇号 0／反引号 span 0；`/tmp/in26.py` 内嵌英文 114 串／全书查无 2（模板例外）；`/tmp/s26.py` 素读 84 条／MISS 0。
