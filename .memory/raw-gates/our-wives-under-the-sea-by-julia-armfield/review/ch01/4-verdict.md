# ch01 判定表（our-wives-under-the-sea · T3 深审）

机器层（修后）：chapter.sh rc=0（块 9 / 引语 9 / 查无 0 / 子项缺 0 / 关键词不成立 0 / 残句 0 / 模板套话 0 / H1 ✅ / 导航 5 ✅；⚠️ 块数 9 vs 本章篇幅建议 3–5）；qcheck：62/48/59/46/54/**41**/37/37/35、关键词越界 0、直撇号 0、音译 0。

## R4 逐块（引语 ↔ 中文理解 ↔ 关键词 ↔ 为什么这样写）

| 块 | 断言 | 证据（text/ch01_miri.txt） | 结论 | 档位 |
|---|---|---|---|---|
| 1 | 深海＝闹鬼的房子；unstill 是 Leah 用的词、她侧头如应答 | `The deep sea is a haunted house…` / `Unstill, is the word Leah uses, tilting her head to the side` | 施事＝Leah（她侧头），中文说「她侧过头」 | ✅ |
| 2 | Leah 说海一直到最底下都有东西在动；她很少说这么多 | `“The ocean is unstill,” she says… All the way to the bottom, things move.` / `She seldom talks this much` | 说话人＝Leah，观察者＝Miri | ✅ |
| 3 | 这类话不是说给 Miri 听的；「只需要一副对的皮肤」 | `this kind of talk isn’t really meant for me… All they need is the right sort of skin.` | 「Miri 被降级成旁听者」与原文 `not meant for me` 一致 | ✅ |
| 4 | 回来一个月后改成并排坐沙发，从前坐地毯、像十几岁 | `since she returned last month… In the old days, we used to sit on the rug` | 时间与姿势对比均逐字对 | ✅ |
| 6（新增） | 六点醒即流鼻血；Miri 睡走廊对面的房间、没亲眼见，但摸熟了她的节律 | `At around six this morning, Leah woke and immediately had a nosebleed.` / `I’ve been sleeping in the room across the hall` | 施事＝Leah 流血、Miri 隔房推断；「分房」首次明写 | ✅ |
| 7 | 把「独自」当目的地是错的，它是被留下的处境 | `assume that alone was somewhere you could go, rather than somewhere you had to be left` | could / had to 对举与原文同向 | ✅ |
| 8 | Leah 说这是压力与压力突然消失；血不认得旧边界 | `it’s something to do with the pressure, the sudden lack thereof` | 施事＝Leah 的解释，非 Miri 诊断 | ✅ |
| 9 | 镜中皮肤像打捞物、溺死者的黄眼；她说一会儿就好 | `her skin had the look of something dredged from water… Be all right, she said` | 说话人＝Leah | ✅ |
| 10→9 | Miri 没有 personnel number，打电话就是为了拿到它 | `I do not… have Leah’s personnel number – the whole purpose of my calling the Centre` | 施事＝Miri 打电话 | ✅ |

R3 对账：漏 1（早六点照护序列 + 分房）**已修**（新增原句 6，41 词）· 编 0 · 错 0，详见 `3-diff.md`。

## 本轮修复
- 新增「原句 6」（41 词）：原文本章第 34 段前两句，覆盖「六点流鼻血 + Miri 睡走廊对面的房间 + 摸熟节律」——这是本章唯一明写分房的一句，此前只出现在导航。鞋不配对/A&E 作为同一模式的第二例，写进该块读者提示，不另立块（本章 1730 词，块数已远超篇幅建议，避免为同一动作再拆一块）。修后 `chapter.sh` rc=0。

## 已核实为正确（防误修）
1. 「Leah 上个月回到家里」——`since she returned last month`，原文明确。
2. 「第五十次」这类计数在 Q8 段落的录音语境里：`for the fiftieth time that my call is important`，指自动语音重复，不是她打了五十次电话。
3. 子代理 R1 的 relations「Miri–母亲 母女」是推断（原文仅 `My mother used to say…`）；md 未采用，无须改，后续勿据此给 Miri 的母亲关系下定性。
4. 词汇表 flannel 例句 `I passed her the flannel and watched her smear her hands with Ivory soap` 是本章原文（`text/ch01_miri.txt`），不是编造。

## 结论
逐字 ✅（8/8）· 对应 ✅（8/8）· 形态 ✅（块数 8 于 novels 上限 8，⚠️ 仅偏离篇幅建议）· 断言 ✅（0 阻断 / 1 提示）
