# ch01 对账（R3）

素读：`1-suread.json`（6 条，全部带 `text/ch01_preface.txt:行` + 逐字 + 字符区间，子代理已脚本校验 6/6 命中本行）。
机器：`2-machine.json`（rc=0，9 块，引语 9 段全 ok，空引号 0，子项齐全，中文密度合格）。
md 216 行，9 块 + 词汇 32 条。原文 49 行 / 2,245 词 / 10,804 字符（去空白）。

## 一、漏（素读有、md 无）

### 1. 【提示】「为什么要写一本四千年跨度的书」的类比段整段未落

- 原文 `text/ch01_preface.txt:40`：
  「Covering four thousand years of history and a vast geographic area wasn't an obvious move for me. I tend to write books about periods of time ranging between about ten and fifty years; I had to learn some new moves to write a book that covers millennia rather than decades. … This is part of why Robert Caro's books do so well, or Naomi Klein's: They're looking at a "now," …」
- md 侧：概览第三段只写「她自陈惯常写十至五十年的题材，这本四千年跨度的书因此必须换一套方法」，**Caro／Klein 两个类比人物与「读者只想要一段『现在』」这一顾虑全无**；`/usr/bin/grep -n "Caro\|Klein" ch01*.md` → 0 命中（退出码 1）。
- 判断：数字部分已落且正确（见下「已核实为正确」第 3 条），缺的是类比与自我设问。属方法论介绍的可选细节，降档为提示。

## 二、编（md 有、原文无）

无。逐条核过 md 里所有具名断言（公民权/投票权/公立教育/契约/陪审/财产/遗嘱；不识字、不上学、不入政府与教会、死于分娩、接生婆与草药；八类制度；约七百年；四项恐惧；涌现属性与大写；1970 年代重编码），全部能在 `text/ch01_preface.txt` 内找到对应原句。

## 三、错（两边都有但不一致）

无。数字、专名、施受方向逐条比对一致（见「已核实为正确」）。

## 四、本文件读过的候选行

`assertion_scan.py` 对 ch01 报出的 ②类判断句 6 行、③类数字 19 行、④类亲属 2 行、⑤类方向 3 行，全部人读；另加 `1-suread.json` 6 条逐一回原文比对。
