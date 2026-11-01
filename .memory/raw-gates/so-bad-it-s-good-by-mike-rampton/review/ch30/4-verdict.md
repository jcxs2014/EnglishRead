# ch30 Afterword 判定（R4 + R5）

机器层：`2-machine.json` verdict=ok，10 块；修后 `chapter.sh` rc=0。

## 逐块对应（10 块）

| 块 | 落位 | 中文是否讲这句 | 关键词 | 施事三问 | 档位 |
|---|---|---|---|---|---|
| 1 致读完的人 | :14 | 是：terrible/excellent | terrible / excellent ✅ | 读＝你 ✅ | 通过 |
| 2 语言失效 | :14 | 是：anchor/floorboard/wildebeest | anchor / floorboard ✅ | 说话＝作者 ✅ | 通过 |
| 3 致先读的人 | :17 | 是：jumping to conclusions | conclusions ✅ | 警告＝作者 ✅ | 通过 |
| 4 生菜与冰山 | :20 | 是：混合比喻 | lettuce / iceberg ✅ | 推＝你 ✅ | 通过 |
| 5 裸猫与冲浪者 | :20 | 是：错配比喻 | surfers ✅ | 挠＝猫 ✅ | 通过 |
| 6 修女 nun/none | :20 | 是：一则未收 | nun whatsoever ✅ | 说＝作者 ✅ | 通过 |
| 7 Hans/hands | :23 | 是：电工梗 | Hans ✅ | 电＝电工 ✅ | 通过 |
| 8 笑话联合人 | :23 | 是：unite | unite ✅ | 联合＝笑话 ✅ | 通过 |
| 9 immature/fully groan | :23 | 是：成熟度双关 | groan ✅ | 笑＝我们 ✅ | 通过 |
| 10 go forth | :26 | 是：排队梗 | go forth ✅ | 走＝你 ✅ | 通过 |

## 断言核对

| 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|
| 5 段正文（原写"四段"） | 7 段 − 2 标题 | 改后正确 | 提示已修 |
| 192 词 | `len(text.split())`=192 | 正确 | 通过 |
| 字符数 1,141（md 写"约 1,150"） | `len(text)` | 正确 | 通过 |
| 三个人 | `:26` 逐字 | 正确 | 通过 |

## 已核实为正确

- 原句 1 的 `terrible`/`excellent` 并列是原文的自嘲（"hundreds of the most terrible … and excellent jokes"），md 未只留一半。
- 原句 6 的 `nun whatsoever`（`:20`）——none whatsoever 的谐音，md 保留原拼写。
- 原句 10 是 T1 时因省略号与原文不符而整句替换的版本，本次复核该句与 `:26` 逐字一致。

## 结论

阻断 0 / 提示 1（已修）/ 假红 0。
