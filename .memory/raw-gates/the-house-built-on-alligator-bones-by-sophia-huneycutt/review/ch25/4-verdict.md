# ch25 判定表（R5）

书：the-house-built-on-alligator-bones-by-sophia-huneycutt｜章：ch25（Chapter Twenty-Four）
档位：**深审（用户升级，全章 R1–R4 串行）**｜日期：2026-10-23
text：`text/ch25_chapter_twenty_four.txt`（147 行／1,608 词）｜md：`ch25 aunt virginia announces moving out.md`

## 四组报数

| 组 | 结果 |
|---|---|
| 逐字 | 引语块 5／片段 5／查无 0（机器＋人工 5/5）；词表 15 行例句逐字（flag 0）；ASCII 撇号 **5 处**（C-25-3，字形队列）；非块内嵌英文全书查无 0（模板例外 2） |
| 对应 | 阻断 2（C-25-1 Gertrude 漏登记；C-25-2 Leon 线三拍漏）；提示 5（P-1 细节增写 ×2、P-6 ugly thought 漏、P-7 画内容漏、P-3/P-4/P-5 措辞） |
| 形态 | H1 `25. Chapter Twenty-Four` ✅｜导航 5 项 ✅｜块数 5（建议 3–5）✅｜词表三档 5+6+4=15 ✅ |
| 断言 | 提示 2（P-2「第一次」范围、P-5「承认」过强）——无阻断级断言 |

## 阻断 3／提示 7／假红 11／不许裁决 8

- **C-25-1**（对应·漏承重）：Gazzie 本名 **Gertrude**（:18，`grep` 全书唯一一处）md 零登记。
- **C-25-2**（对应·漏承重）：graves（:63）→ breeding pond 之疑（:66）→ Leon 那行字复现（:69，首出 ch23:119）三拍全未登记。
- **C-25-3**（逐字·字形）：md:13 `That's`／`didn't`×2、md:14 `didn't`、md:98 `one's`——共 5 处，短语逐字正确、只改 U+2019；全书 15/49 章 51 处队列。
- 提示 7 条见 3-diff.md。

## 假红（已核实为正确——防下一轮改坏）

1. 「两姐妹」＝:42 逐字。
2. 夏至派对后搬去与 Henri 同住＝:51 逐字。
3. 步行五十分钟＝:114 逐字。
4. 「only one option: stay on Amelia Island and win her approval」＝:135 逐字。
5. 两句 didn’t 引文与 `That's what I told myself, anyway`＝:114/:123 逐字（仅字形）。
6. block2/3/5 引文与 `The details clicked into place`、`I can see that` 全部逐字。
7. 「I didn’t… 排比」＝:114 四连。
8. 机器层四件全绿复核属实（引语逐字／词表例句／内嵌英文／块数 5）。

## 不许裁决（8 条）

见 3-diff.md「不许裁决」节：Leon 死因与 breeding pond／grave 指谁／邀请动机两层／巴掌动机＝她的解读／one or two presences／Harrison 立场＝自我说服／coerce 旧账事例／Mother-Ida 裁定内容；三种死法书级护栏延续。

## 覆盖声明

- 本章人判覆盖：R1 素读 85 facts／MISS 0 ＋ R3/R4 全 md 精读 ＋ R5 判定表（**深审全章**）。
- 机器层：`bash scripts/chapter.sh` rc=0（输出存 `2-machine.json`）。
- 探针：v25（15/0）、ap25（撇号 5→C-25-3）、in25（117 串／查无 2 模板例外）、span25（见下）。
- 分工：审查方**只出指令不改稿**；修复由执行方按 `2026-10-23-复核与修复指令.md` 执行后回执复核。

## 探针自检

`/tmp/span25.py`：反引号 span 67 条／MISS 5——`Chapter Twenty-Four`×2 与 `Tropes`（模板级）、`25. Chapter Twenty-Four`（H1 引用，模板级）、`hold one's breath`（词表释义中的词目形态，`grep -c "hold one"`＝0 命中 ⇒ 非引语、预期 MISS）、`I imagined my hand connecting with her face… Another ugly thought.`（省略号拼接，两段各自逐字：`grep -c "I imagined my hand connecting with her face"`＝1、`"Another ugly thought."`＝1）；`/tmp/v25.py` 词表 15 行／flag 0；`/tmp/ap25.py` ASCII 撇号 5 处（md:13×3／:14／:98，C-25-3）／反引号 span 0；`/tmp/in25.py` 内嵌英文 117 串／全书查无 2（模板例外）；`/tmp/s25.py` 素读 85 条／MISS 0。
