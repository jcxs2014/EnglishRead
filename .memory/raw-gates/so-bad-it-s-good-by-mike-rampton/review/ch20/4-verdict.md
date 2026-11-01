# ch20 Literally Terrible Book Jokes 判定（R4 + R5）

机器层：`2-machine.json` verdict=ok，10 块；修后 `chapter.sh` rc=0。

## 逐块对应（10 块）

| 块 | 落位 | 中文是否讲这句 | 关键词 | 施事三问 | 档位 |
|---|---|---|---|---|---|
| 1 裸体营与马克思 | :15 | 是：read Marx/red marks | read Marx ✅ | 问＝一人 ✅ | 通过 |
| 2 图书馆耳语 | :25 | 是：三层楼、喊完改低声 | pint of lager ✅ | 喊＝读者 ✅ | 通过 |
| 3 Forster | :30 | 是：forced her | Forster ✅ | 说＝我 ✅ | 通过 |
| 4 Lo, a case | :40 | 是：大写/小写 | Lo, a case ✅ | 说＝福尔摩斯 ✅ | 通过 |
| 5 同义词词典 | :45 | 是：自我演示 | thesaurus / rubbish ✅ | 买＝我 ✅ | 通过 |
| 6 saliva | :50 | 是：rolls off the tongue | saliva ✅ | 说＝我 ✅ | 通过 |
| 7 riveting | :57 | 是：铆接/引人入胜 | riveting ✅ | 读＝我 ✅ | 通过 |
| 8 mammoth | :67 | 是：百万词写猛犸 | mammoth ✅ | 写＝我 ✅ | 通过 |
| 9 Narnia business | :148 | 是：none of your business | Narnia ✅ | 拿＝白女巫 ✅ | 通过 |
| 10 Brontësaurus | :153 | 是：Brontë + dinosaur | Brontësaurus ✅ | 写＝恐龙 ✅ | 通过 |

## 断言核对

| 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|
| 37 条（原写"约 35"） | 39 段 − 2 标题 | 改后正确 | 提示已修 |
| 660 词 | `len(text.split())`=660 | 正确 | 通过 |
| 字符数 3,820（md 写"约 3,800"） | `len(text)` | 正确 | 通过 |
| 图书馆三层 | `:25` 原文 three floors | 正确 | 通过 |

## 已核实为正确

- 原句 4 的 `Lo, a case`：`:40` 原文即全小写写法（T1 时把关键词 `lowercase` 删掉，只留 `Lo, a case`），本次复核该修正仍在。
- 原句 2 的耳语台词：`:25` `‘Ah,’ he says, then whispers, ‘A pint of lager please.’`，md 与 suread 锚点一致（T3 修正过凭印象写错的锚点）。
- 原句 9 的 `White Witch carrying a briefcase` 与 `Narnia business`：`:148` 逐字，施事是白女巫，md 未写成"我"。

## 结论

阻断 0 / 提示 1（已修）/ 假红 0。
