# ch15 Historically Bad Jokes Laden With Eras 判定（R4 + R5）

机器层：`2-machine.json` verdict=ok，10 块；修后 `chapter.sh` rc=0。

## 逐块对应（10 块）

| 块 | 落位 | 中文是否讲这句 | 关键词 | 施事三问 | 档位 |
|---|---|---|---|---|---|
| 1 Incan paper | :15 | 是：ink and paper | parchment / Incan paper ✅ | 签＝我 ✅ | 通过 |
| 2 罗马五杯啤酒 | :25 | 是：两指＝五（罗马数字） | two fingers / five ✅ | 要＝罗马人 ✅ | 通过 |
| 3 Vlad 与维尼 | :35 | 是：middle name 双关 | Impaler / middle name ✅ | 有＝两者 ✅ | 通过 |
| 4 Alexander 的军队 | :40 | 是：sleevies/armies | sleevies ✅ | 放＝亚历山大大帝 ✅ | 通过 |
| 5 克利奥帕特拉 | :45 | 是：Mummy's home | mummy ✅ | 说＝她 ✅ | 通过 |
| 6 路易十四 | :50 | 是：Baroque/broke | Baroque ✅ | 付钱＝路易十四 ✅ | 通过 |
| 7 马克思 | :60 | 是：proper tea/property | proper tea ✅ | 喝＝马克思 ✅ | 通过 |
| 8 李将军 | :70 | 是：General Lee/generally | General Lee ✅ | 站错边＝南方军 ✅ | 通过 |
| 9 海盗耳环 | :164 | 是：buck an ear | buck an ear ✅ | 收费＝海盗 ✅ | 通过 |
| 10 海盗字母 | :174 | 是：P/pea、C/sea | ‘P’ ✅ | 说＝海盗 ✅ | 通过 |

## 断言核对

| 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|
| 27 条历史条目（原写"约 24 条"） | 37 段 − 2 标题 − 2 抬头 − 6 海盗 | 改后正确 | 提示已修 |
| 顺序非严格年代递进（原写"按时间顺序"） | :25 罗马先于 :35 Vlad；:60 马克思先于 :70 内战 | 改后正确 | 提示已修 |
| 71,000,004 年零六个月 | `:174` 前段 | 正确 | 通过 |
| 3,000 年油渍 | `:20` 段 | 正确 | 通过 |
| 字符串 3,122（md 写"约 3,000"） | `len(text)` | 正确（"约"） | 通过 |

## 已核实为正确

- 原句 1 的 `Incan paper` = ink and paper：`:15` 原文逐字，md 已把错写的 "in Cain paper" 改成 ink and paper。
- 原句 8 的 `generally`：`:70` 原文 `…they were on the wrong side of history, generally`，md 解释有据。
- 海盗 6 条确为章末并入的二级小节（`:29` 与 `:30` 两个 "Pirates!" 抬头），md「概览」已注明。

## 结论

阻断 0 / 提示 2（已修）/ 假红 1（原文自带的地理错，不修）。
