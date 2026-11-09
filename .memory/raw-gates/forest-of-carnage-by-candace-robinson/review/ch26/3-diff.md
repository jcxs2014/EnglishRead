# ch26 · R3 对账（漏 / 编 / 错）

- 章：ch26；语料：`notes/books/novels/forest-of-carnage-by-candace-robinson/text/ch26_epilogue.txt`（279 行）
- R1 素读：`1-suread.json`（12 条事实）
- R2：`2-machine.json`（verdict ok）

| # | 类 | 断言 | 原文证据 | 改前 → 改后 | 档位 |
|---|---|---|---|---|---|
| 1 | 阻断 | 原句4 中文理解含引语外内容（缓步下小径、口袋里的礼物） | `text/ch26_epilogue.txt:52` 原文 `a hand in his pocket, toying with Sterling’s gift` | 于是他改为缓步走下小径——手插在口袋，捏着要给她的礼物。 → 删去引语外动作 | 阻断 |
| 2 | 阻断 | 原句7 中文理解含引语外内容（他把她拉进储藏室） | `text/ch26_epilogue.txt:79` 原文 `Inside the pantry` | 他把她拉进储藏室：“我们按狼的仪式结的契…” → 只留引语内台词 | 阻断 |
| 3 | 提示 | 原句6 跨章引用章号错（ch09 → ch04） | `text/ch26_epilogue.txt`（锚点未定位） | 对照 ch09 他在绞刑台上“仁慈”的反讽 → 对照 ch04 | 提示 |

## 结论

阻断 2 · 提示 1；均已当场整改（边审边改），整改后 `chapter.sh` rc=0。
