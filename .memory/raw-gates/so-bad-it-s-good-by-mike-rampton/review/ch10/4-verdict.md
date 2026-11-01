# ch10 Classic Joke Formats Explained 判定（R4 + R5）

机器层：`2-machine.json` verdict=ok，10 块；`chapter.sh` rc=0。

## 逐块对应（10 块）

| 块 | 落位 | 中文是否讲这句 | 关键词 | 施事三问 | 档位 |
|---|---|---|---|---|---|
| 1 敲门笑话总论 | :19 | 是：最持久却最烂＋no-bell 自嘲 | enduring / no-bell ✅ | 讲＝作者 ✅ | 通过 |
| 2 Shaun 一条 | :19 | 是：忘了带钥匙 | knock / Shaun ✅ | 说＝Shaun ✅ | 通过 |
| 3 悬念与颠覆 | :19 | 是：名字如何变成进门的话 | suspense / subversion ✅ | 判断＝作者 ✅ | 通过 |
| 4 打断的牛 | :19 | 是：抢在提问前 | Interrupting / MOOOO ✅ | 哞＝牛 ✅ | 通过 |
| 5 长毛狗定义 | :33 | 是：长、极虎头蛇尾 | anticlimactic / audacity ✅ | 讲＝讲者 ✅ | 通过 |
| 6 松散框架 | :33 | 是：不逐字背 | loose frames / granular ✅ | 处置＝讲者 ✅ | 通过 |
| 7 酒吧两个陌生人 | :44 | 是：被迫对话 | efficient / bound ✅ | 走进＝顾客 ✅ | 通过 |
| 8 酒吧只是偶然 | :44 | 是：马那条例证 | incidental / licensed premises ✅ | 问＝马 ✅ | 通过 |
| 9 鸡过马路 | :52 | 是：讲不通却最有名 | anticlimactic / allegory ✅ | 讲＝所有人 ✅ | 通过 |
| 10 变体生成 | :52 | 是：替换元素 | variants / evolved ✅ | 造＝讲者 ✅ | 通过 |

## 断言核对

| 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|
| 四个 H2 小节 | 文件内四个格式节 | 正确 | 通过 |
| 字符数 3,400 | `len(text)`=3,400 | 正确 | 通过 |
| "shaggy dog" 名字出现于 1930 年代 | `:33` 原文 | 正确 | 通过 |
| 吐温只是"据说"是粉丝 | `:33` “Mark Twain was said to be a fan” | 正确 | 通过 |

## 已核实为正确

- 原句 1 的 no-bell 双关是原文自带的作者自嘲（`:19`），md「中文理解」保留"无铃奖"这一层，未当成真事。
- 原句 7 的"两个互不相识的角色"：`:44` 原文 "two characters who don’t know one another"，md 未夸大成"两个陌生人讲笑话"。
- 可质疑处 1（无时间证据）有据：全文除 1930 年代外无其他年代。

## 结论

阻断 0 / 提示 0 / 假红 0。
