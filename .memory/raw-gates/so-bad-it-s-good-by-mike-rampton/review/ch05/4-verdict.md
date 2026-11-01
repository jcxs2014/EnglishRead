# ch05 Animal Jokes So Bad They're Beastly 判定（R4 + R5）

机器层：`2-machine.json` verdict=ok，9 块。修后 `chapter.sh` rc=0。

## 逐块对应（9 块）

| 块 | 落位 | 中文是否讲这句 | 关键词 | 施事三问 | 档位 |
|---|---|---|---|---|---|
| 1 Annabel | :17 | 是：and a bell（本轮已修） | Annabel ✅ | 提议＝第二人 ✅ | 通过 |
| 2 翼龙 P | :49 | 是：p 不发音 | P / silent ✅ | 上厕所＝翼龙 ✅ | 通过 |
| 3 buffalo/bison | :54 | 是：bison≈basin | bison ✅ | 洗手＝听者（你）✅ | 通过 |
| 4 乌龟与蜗牛 | :59 | 是：happened so fast | so fast ✅ | 抢＝蜗牛 ✅ | 通过 |
| 5 两条鱼 | :74 | 是：tank 双义 | tank ✅ | 问＝鱼 ✅ | 通过 |
| 6 吃毛线的猫 | :80 | 是：mittens/kittens | mittens ✅ | 吃＝猫 ✅ | 通过 |
| 7 豹子 spotted | :117 | 是：斑点/被发现 | spotted ✅ | 藏＝豹子 ✅ | 通过 |
| 8 章鱼 ten tickles | :188 | 是：tentacles | ten tickles ✅ | 逗＝听者 ✅ | 通过 |
| 9 catscan | :173 | 是：CAT scan 拆词 | catscan ✅ | 操作 MRI＝狗 ✅ | 通过 |

## 断言核对

| 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|
| 39 条 | 41 非空段 − 2 标题（:1、:11）| 改后正确 | 阻断已修 |
| 字符数 3,518 | `len(text)`=3,518 | 正确 | 通过 |
| 一半条目依赖拼写/发音 | 39 条中拼音类 ≥15 条 | 成立（近似判断，非数字断言） | 通过 |

## 已核实为正确

- 原句 3 的 buffalo/bison 逻辑：`:54` 原文 `What’s the difference between a buffalo and a bison? You can’t wash your hands in a buffalo.` —— 靠 bison≈basin，md 未误写成"buffalo 是水牛所以能洗"。
- 原句 4 的 `happened so fast`：`:59` 乌龟被蜗牛抢，警察问经过，乌龟答"一切太快了"——md 引语与释义一致。
- 章末「说它是笑话靠惯例」的评述：`:173` catscan 与 `:188` ten tickles 均为单句谐音，无场景，评述有原文依据。

## 结论

阻断 1（计数 36→39，已修）/ 提示 1（Annabel 机制，已修）/ 假红 0。
