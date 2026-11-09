# ch25 · R3 对账（漏 / 编 / 错）

- 章：ch25；语料：`notes/books/novels/forest-of-carnage-by-candace-robinson/text/ch25_chapter_twenty_five.txt`（175 行）
- R1 素读：`1-suread.json`（13 条事实）
- R2：`2-machine.json`（verdict ok）

| # | 类 | 断言 | 原文证据 | 改前 → 改后 | 档位 |
|---|---|---|---|---|---|
| 1 | 阻断 | 原句1 中文理解含引语外内容（狼群不会像他那样宽容） | `text/ch25_chapter_twenty_five.txt:16` 原文 `His wolves wouldn’t have been as lenient` | …惨得多，他的狼群不会像他那样宽容。 → 删去该句 | 阻断 |
| 2 | 阻断 | 原句5 中文理解含引语外内容（“那他不就没有继承人了？”） | `text/ch25_chapter_twenty_five.txt:49` 原文 `But then he would have no heir` | 她问：那他不就没有继承人了？ → 删去该问句 | 阻断 |
| 3 | 阻断 | 原句6 中文理解含引语外整段对白（Rawling 撞门、我杀了他、浴室剧本） | `text/ch25_chapter_twenty_five.txt:61` 原文 `I killed him` | General Rawling 撞门而入…再补一句：“我现在是你们的王…” → 只留引语内的王权宣告 | 阻断 |
| 4 | 阻断 | 原句10 中文理解含引语外内容（wear this、署名） | `text/ch25_chapter_twenty_five.txt:151` 原文 `You can be free of me to do whatever you wish` | 若你来，戴上这个。署名 Winter。 → 引语补全至 But, if you do come, wear this.（含中间句，保持连续） | 阻断 |

## 结论

阻断 4 · 提示 0；均已当场整改（边审边改），整改后 `chapter.sh` rc=0。
