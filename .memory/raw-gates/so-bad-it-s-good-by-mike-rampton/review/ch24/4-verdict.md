# ch24 Even More Classic Joke Formats Explained 判定（R4 + R5）

机器层：`2-machine.json` verdict=ok，10 块；修后 `chapter.sh` rc=0。

## 逐块对应（10 块）

| 块 | 落位 | 中文是否讲这句 | 关键词 | 施事三问 | 档位 |
|---|---|---|---|---|---|
| 1 cross 笑点受孩子喜爱 | :19 | 是：看似简单实则不简单 | straightforward ✅ | 喜爱＝孩子 ✅ | 通过 |
| 2 两路走向 | :19 | 是：双关/超现实 | woolly jumper ✅ | 造＝人 ✅ | 通过 |
| 3 椅子与仙人掌 | :19 | 是：自解构 | Nor do I ✅ | 说＝我 ✅ | 通过 |
| 4 paraprosdokian 定义 | :30 | 是：句尾反转 | paraprosdokian ✅ | 定义＝作者 ✅ | 通过 |
| 5 Groucho 与 King | :30 | 是：极难写、又傻又高雅 | highbrow ✅ | 说＝Groucho ✅ | 通过 |
| 6 stock characters 溯源 | :41 | 是：骑士/老妪/小丑 | stock characters ✅ | 溯源＝作者 ✅ | 通过 |
| 7 旅行推销员 | :41 | 是：作者自评"往往不好" | sticky situations ✅ | 过夜＝推销员 ✅ | 通过 |
| 8 Little Jimmy | :41 | 是：脏话/泄密 | lascivious ✅ | 说＝男孩 ✅ | 通过 |
| 9 non-sequitur 定义 | :52 | 是：拉丁语"不跟随" | non-sequitur ✅ | 定义＝作者 ✅ | 通过 |
| 10 九岁孩子 | :52 | 是：Hatstand! Spaceship! | Hatstand ✅ | 编＝孩子 ✅ | 通过 |

## 断言核对

| 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|
| 四节 95–160 词（原写 100–150） | 各段词数实测 | 改后正确 | 提示已修 |
| 538 词 | `len(text.split())`=538 | 正确 | 通过 |
| 字符数 3,243（md 写"约 3,240"） | `len(text)` | 正确 | 通过 |
| 九岁 | `:52` 逐字 | 正确 | 通过 |

## 已核实为正确

- 原句 3 的 `Nor do I`（`:19`）是椅子＋仙人掌笑话的包袱（"我不知道，我也不会把屁股放上去"），md 未把包袱改成别的句子。
- 原句 5 的 Stephen King 例句在 `:30` 段内（"罐子里的一颗小男孩的心"），md 与 Groucho 并列而未混淆两人。
- 原句 10 的 `Hatstand! Spaceship! Wibble wibble!`（`:52`）是九岁孩子自编 non-sequitur 的例证，md 保留其无意义性。

## 结论

阻断 0 / 提示 1（已修）/ 假红 0。
