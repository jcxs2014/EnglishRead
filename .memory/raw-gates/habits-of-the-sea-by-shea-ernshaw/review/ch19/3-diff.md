# ch19 素读 vs md 差异（人判）

素读清单：`1-suread.json`（6 条事实，锚点全部命中 `text/ch19_epilogue.txt`）。

## 查出的问题

### D1 · 导航两处计数与原文不符 🟡

- **位置**：md:15（叙事手法）
- **改前**：`全章七句` / `最后三个短句独立成行`
- **改后**：`全章八句` / `最后两个短句各自独立成行`
- **原文依据**（`text/ch19_epilogue.txt` 逐句点算）：
  1. `:13` `Saltwell Island would not be remembered.`
  2. `:13` `Most stories never are.`
  3. `:16` `But a fable doesn’t need to be remembered to be true.`
  4. `:19` `And endings are not what we think they are.`
  5. `:22` `The sea is deeper than we can measure; our minds are a place of make-believe.`
  6. `:22` `And if you find yourself standing at the edge of everything… this life, or the one waiting for you.`
  7. `:25` `Out there.`
  8. `:28` `Somewhere.`
  独立成行的短句只有 `:25` 与 `:28` 两处（`this life, or the one waiting for you` 仍在 `:22` 的同一段里）。

## 已核实为正确（不要改坏）

- 块 1/2/3 的引语边界与 `:13` `:19`–`:22` `:22`–`:28` 完全一致；块 3 把 `Out there. Somewhere.` 并入同一块**合规**（同段连续，非跨段缝合）。
- 块 3 中文理解「这一生，还是在等你的那一个」：`this life, or the one waiting for you` 的 `the one` 指「那一种生活」，译法**正确**。
- 导航「Ellie、Clay、Nana 都不再被点名」为**真陈述**（本章正文确实不含这三个人名）——`check_summary_names` 的三条提示是假阳，**不要改**。
- 三块引语合计 66 词、覆盖全章 81 词的 81%，⚠️「块数 3 偏离建议 2」不修（下限 3 为阻断型）。
