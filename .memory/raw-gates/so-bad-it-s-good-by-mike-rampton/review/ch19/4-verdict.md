# ch19 Music Jokes That Are Hideously Out of Tune 判定（R4 + R5）

机器层：`2-machine.json` verdict=ok，10 块；`chapter.sh` rc=0。

## 逐块对应（10 块）

| 块 | 落位 | 中文是否讲这句 | 关键词 | 施事三问 | 档位 |
|---|---|---|---|---|---|
| 1 George Michael | :16 | 是：Highlights reel | Highlights reel ✅ | 看＝人 ✅ | 通过 |
| 2 four-tune cookies | :21 | 是：fortune/four-tune | four-tune ✅ | 有＝我 ✅ | 通过 |
| 3 Seedy | :29 | 是：低俗/有籽 | Seedy ✅ | 问＝人 ✅ | 通过 |
| 4 贝多芬的鸡 | :34 | 是：Bach/back | Bach ✅ | 处理＝贝多芬 ✅ | 通过 |
| 5 A flat miner | :44 | 是：降 A／矿工 | A flat ✅ | 掉＝钢琴 ✅ | 通过 |
| 6 古典作曲家带什么 | :54 | 是：谱／指挥 | baton ✅ | 带＝作曲家 ✅ | 通过 |
| 7 No chants | :59 | 是：chant/chant | chants ✅ | 说＝修士 ✅ | 通过 |
| 8 三音进酒吧 | :133 | 是：minors/minors | Middle C / minors ✅ | 说＝酒保 ✅ | 通过 |
| 9 Ba-dum-tssh | :98 | 是：鼓点拟声 | Ba-dum-tssh ✅ | 落地＝乐器 ✅ | 通过 |
| 10 bandstand | :118 | 是：撤椅子 | bandstand ✅ | 拆＝人 ✅ | 通过 |

## 断言核对

| 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|
| 约 30 条（实测 31 条） | 33 段 − 2 标题 | 正确（"约"） | 通过 |
| 575 词 | `len(text.split())`=575 | 正确 | 通过 |
| 字符数 3,310 | `len(text)` | 正确 | 通过 |
| 凌晨三点敲门 | `:16` 前段 | 正确 | 通过 |

## 已核实为正确

- 原句 7 的引号缺口：`:59` 原文 `Will you tell me which type you prefer?’‘No chants.’` 确实没有 Will 前的开引号，md 引语照抄（T3 前已记此条），机器校验通过。
- 原句 10 的 "Take away their chairs" 是原文末句（文末），md"以 bandstand 收尾"成立。
- T1 时把词汇表 `repertoire` 换成 `cassette` 的改动仍在（本条目例句含该词），已复核。

## 结论

阻断 0 / 提示 0 / 假红 0。
