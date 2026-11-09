# ch21 · R3 对账（漏 / 编 / 错）

- 章：ch21；语料：`notes/books/novels/forest-of-carnage-by-candace-robinson/text/ch21_chapter_twenty_one.txt`（219 行）
- R1 素读：`1-suread.json`（12 条事实）
- R2：`2-machine.json`（verdict ok）

| # | 类 | 断言 | 原文证据 | 改前 → 改后 | 档位 |
|---|---|---|---|---|---|
| 1 | 阻断 | 原句1 中文理解含引语外内容（“他盼着我们放了你”） | `text/ch21_chapter_twenty_one.txt:16` 原文 `in hopes that we would set you free` | 引语止于 What a wonderful sister you are. → 引语扩至 I can promise you that. | 阻断 |
| 2 | 阻断 | 原句2 中文理解含引语外内容（背对折纸、纸森林垂挂） | `text/ch21_chapter_twenty_one.txt:22` 原文 `Paper decorations that Cyan had made dangled` | 她推门而见：弟弟背对她坐在毛毯上折纸，纸做的森林垂挂满屋 → 只留引语内的纸雕内容 | 阻断 |
| 3 | 阻断 | 原句4 中文理解整段是上一段她的话（引语是他的一句） | `text/ch21_chapter_twenty_one.txt:40` 原文 `He withdrew his arms from around her` | “我理解你恨我，”她哽咽…——他抽身退开 → 只留他抽身与问话 | 阻断 |
| 4 | 阻断 | 原句7 中文理解含引语外内容（“为了救你”“表情会很难看”） | `text/ch21_chapter_twenty_one.txt:76` 原文 `But that’s not the whole reason you married him` | 她又说为了救你，他补刀… → 只留引语内的拆穿句 | 阻断 |
| 5 | 提示 | 原句2 计数断言（纸艺第五次出场）不可核 | `text/ch21_chapter_twenty_one.txt:28` 原文 `A smile radiated in Cyan’s voice` | 纸艺第五次出场 → 纸艺又一次出场 | 提示 |

## 结论

阻断 4 · 提示 1；均已当场整改（边审边改），整改后 `chapter.sh` rc=0。
