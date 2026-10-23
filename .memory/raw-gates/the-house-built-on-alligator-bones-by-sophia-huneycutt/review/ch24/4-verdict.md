# ch24 判定表（R5）

书：the-house-built-on-alligator-bones-by-sophia-huneycutt｜章：ch24（Chapter Twenty-Three）
档位：**深审（用户升级，全章 R1–R4 串行）**｜日期：2026-10-23
text：`text/ch24_chapter_twenty_three.txt`（351 行／2,932 词）｜md：`ch24 the culprit had to be a real person.md`

## 四组报数

| 组 | 结果 |
|---|---|
| 逐字 | 引语块 6／片段 6／查无 0（机器＋人工 6/6 复核）；词表 15 行例句逐字（flag 0）；ASCII 撇号 0；非块内嵌英文全书查无 0（模板例外 2） |
| 对应 | 阻断 2（C-24-1 凭空物种 ×3 处；C-24-2 条件句方向写反）；提示 4（P-1 称谓 ×2、P-3 漏 no count、P-4 漏记忆链、P-5 漏动机三联、P-6 漏 probably 推测——其中漏类 4 条） |
| 形态 | H1 `24. Chapter Twenty-Three` ✅｜导航 5 项 ✅｜块数 6（建议 5–9）✅｜词表三档 5+6+4=15 ✅ |
| 断言 | 阻断 1（C-24-3 跨章「第一次」）；提示 1（P-2 前瞻断言） |

## 阻断 3／提示 6／假红 11／不许裁决 8

- **C-24-1**（对应·凭空）：「野猪」×3（md:10／:11／:14）→ hog＝家猪，boar 全书 0 命中。改「猪」。
- **C-24-2**（对应·条件句→断言＋方向反转）：md:34「if I hadn’t seen the border 说明这条线是后来才出现的」→ 原文预设她先前见过边界；只能推出「边界被草吞掉、不靠记忆认不出」，不是「后来才出现」。
- **C-24-3**（断言·跨章第一次）：md:13「Aunt Virginia 第一次以恋爱中的姿态出现」→ ch04:234 已有脸红＋new-relationship happiness 判读、ch17:12 自报共餐。改「第一次当着叙述者的面」。
- 提示 6 条见 3-diff.md（P-1 称谓 ×2／P-2 前瞻／P-3~P-6 漏登记 4 条）。

## 假红（已核实为正确——防下一轮改坏）

1. 「Ginny 的女友 Henri」＝:39 逐字。
2. 「Cut it out」截断的方位与身份＝:339。
3. 「Dart, this is Henri」＝:84（本章原文确有 Dart，导航可用）。
4. backup plan／technically 仍雇员＝:219。
5. 弧线两端（abrasive competition :333 → hold a lot back :312）都在本章。
6. 「She doesn’t care for me」等关系交底确出自 Gazzie 台词（:39/:48）。
7. block2 引文本身逐字（错在推论句不在引文）。
8. 「the farm 从她手里起」＝:75。
9. block6 双层目光链（ch22:97 → ch24:135/:324）成立。
10. 章末「he looked stunned」＝:351。
11. 机器层四件（引语逐字／词表例句／内嵌英文／撇号）全绿复核属实。

## 不许裁决（8 条）

见 3-diff.md「不许裁决」节：嫌疑人名单不点名／Gazzie 是否进房／吻未坐实／争吵内容／愧疚猜想／要孩子 probably／手放腹部的含义／三种死法书级护栏。

## 覆盖声明

- 本章人判覆盖：R1 素读 226 facts／MISS 0 ＋ R3/R4 全 md 精读 ＋ R5 判定表（**深审全章**，非「仅机器层」）。
- 机器层：`bash scripts/chapter.sh` rc=0（输出存 `2-machine.json`）。
- 素读：`/tmp/s24.py` → `1-suread.json`（226 facts／8 relations／12 numbers，MISS 0）。
- 探针：v24（词表 15/0）、ap24（撇号 0）、in24（104 串／查无 2 模板例外）、span24（见下）。
- 分工：审查方**只出指令不改稿**；修复由执行方按 `2026-10-23-复核与修复指令.md` 执行后回执复核。

## 探针自检

`/tmp/span24.py`：反引号 span 61 条／MISS 5——`Chapter Twenty-Three`×2 与 `Tropes`（模板级）、`24. Chapter Twenty-Three`（H1 引用，模板级）；其余 2 条是省略号拼接，两段各自逐字（`/usr/bin/grep -c "Was she drowning her guilt"`＝1、`"For something more?"`＝1、`"She blushed"`＝1、`"That was new-relationship happiness"`＝1，均 ch04）；`/tmp/v24.py` 词表 15 行／flag 0；`/tmp/ap24.py` ASCII 撇号 0／反引号 span 0；`/tmp/in24.py` 内嵌英文 104 串／全书查无 2（两个模板例外）；`/tmp/s24.py` 素读 226 条／MISS 0。
