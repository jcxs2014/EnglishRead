# ch07 The Oldest Jokes in the World 判定（R4 + R5）

机器层：`2-machine.json` verdict=ok，8 块。修后 `chapter.sh` rc=0。

## 逐块对应（8 块）

| 块 | 落位 | 中文是否讲这句 | 关键词 | 施事三问 | 档位 |
|---|---|---|---|---|---|
| 1 口传与保存 | :15 | 是：ad hoc 记录，"mere 4,000 years" | orally / preserving ✅ | 传＝人们 ✅ | 通过 |
| 2 苏美尔放屁笑话 | :18 | 是：含 Poo-ey 的现代改写 | sexist / observational ✅ | 讲＝作者 ✅ | 通过 |
| 3 埃及法老渔网 | :25 | 是：词多、可能原本更利落 | wordy / snappier ✅ | 逗＝读者（你）✅ | 通过 |
| 4 1200 BCE 残本 | :28 | 是：译者成笑柄 | punchline / contrived ✅ | 受害＝译者 ✅ | 通过 |
| 5 Philogelos | :31 | 是：264 条、库迈人 | compiled / stereotyped ✅ | 编＝古人 ✅ | 通过 |
| 6 生菜＝春药 | :34 | 是：Caesar 沙拉与 dressing 双关 | aphrodisiac / dressing ✅ | 瞥＝公鸡 ✅ | 通过 |
| 7 Facetiae 273 条 | :37 | 是：印刷术之后才出版 | printing press / one-liners ✅ | 出版＝Poggio ✅ | 通过 |
| 8 主题收束 | :37 | 是：建构成讽刺反驳、三主题 | retorts / themes ✅ | 作者自评本章 ✅ | 通过 |

## 断言核对

| 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|
| 三则独立古笑话（原写四条） | :18 / :25 / :28 | 改后正确 | 提示已修 |
| Philogelos 264 条、250–400 CE | :31 | 正确 | 通过 |
| Facetiae 273 条、1470s | :37 | 正确 | 通过 |
| 字符数 3,331 | `len(text)`=3,331 | 正确 | 通过 |
| 苏美尔残本到 Philogelos 隔"another millennium or so" | :31 | 正确（可质疑处 2 引语有据） | 通过 |

## 已核实为正确

- 原句 6 的"a chicken sees a salad"：`:34` 原文括注 `(or, as it’s also known, ‘A chicken sees a salad’)`，md 点明是 Caesar salad 的谐音，与原文并置的 dressing 双关一致。
- "Poo-ey!" 是原文所有：`:18` 结尾 `‘Hey, have you ever noticed how women are always farting? Poo-ey!’`。
- 可质疑处 1（样本偏差）并非 md 臆断：`:15` 原文确实只解释"口传→偶然被写下"，未讨论书写者的阶层。

## 结论

阻断 0 / 提示 1（四条→三则，已修）/ 假红 0。
