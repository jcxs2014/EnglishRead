# ch18 · R3 对账（漏 / 编 / 错）

- 章：ch18；语料：`notes/books/novels/forest-of-carnage-by-candace-robinson/text/ch18_chapter_eighteen.txt`（261 行）
- R1 素读：`1-suread.json`（12 条事实）
- R2：`2-machine.json`（verdict ok）

| # | 类 | 断言 | 原文证据 | 改前 → 改后 | 档位 |
|---|---|---|---|---|---|
| 1 | 阻断 | 原句4 中文理解含引语外内容（父亲讽刺他不给新娘拉椅） | `text/ch18_chapter_eighteen.txt:94` 原文 `Aren’t you going to hold a chair out for your bride-to-be` | 宴会定调：父亲讽刺他不给新娘拉椅——他反手把她按跪在脚边 → 删去引语外动作，只留“他反手把她按跪在脚边” | 阻断 |
| 2 | 阻断 | 原句5 中文理解含引语外内容（脚踩餐具位）＋英文误引（spoil food） | `text/ch18_chapter_eighteen.txt:115` 原文 `put his feet up on the table` | 他脚踩上她的餐具位、眼神像看馊掉的食物 → 删去脚踩动作；“spoil food”改为“spoiled food” | 阻断 |
| 3 | 阻断 | 原句6 中文理解含引语外内容（倒完酒想坐下、靴子勾椅） | `text/ch18_chapter_eighteen.txt:139` 原文 `grasped the leg with his boot` | 她倒完酒想坐下，他用靴子勾走椅子、笑眯眯毁约 → 只留引语内的毁约台词 | 阻断 |
| 4 | 阻断 | 原句8 中文理解含引语外内容（血溅上脸、大脑空白） | `text/ch18_chapter_eighteen.txt:243` 原文 `Blood sprayed across Winter’s face` | 血溅上脸的瞬间他大脑空白：父亲的爪子… → 只留引语内的动作 | 阻断 |
| 5 | 提示 | 原句2 错字（着辱戏） | `text/ch18_chapter_eighteen.txt:70` 原文 `don’t defy anything` | 宴会着辱戏 → 宴会的羞辱戏 | 提示 |
| 6 | 提示 | 原句9 计数断言（bored 模式第四次）不可核 | `text/ch18_chapter_eighteen.txt:252` 原文 `That was dramatic` | 第四次登场 → 又一次登场 | 提示 |

## 结论

阻断 4 · 提示 2；均已当场整改（边审边改），整改后 `chapter.sh` rc=0。
