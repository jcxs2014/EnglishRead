# R3 对账 · ch01

| 单子 | 项 | 两侧原文 | 结论 |
|---|---|---|---|
| 漏 | 无 | 素读 9 条（告别/Jake 身高/挂科链/Misty/名单/Oliver 档案/代发咨询）在 md 均有对应 | 通过 |
| 编 | 无 | md 全部情节均可在 text/ch01_chap1.txt 找到 | 通过 |
| 错① | 计数 | md（原句 2 正文与导航）称 `And if…` 为「三连排比」；引语块内逐字只有 **2** 次 `And if`（第三次 `And if it’s not easy` 在块外 `text/ch01_chap1.txt:107` 前段） | 阻断（计数） |
| 错② | 读者视角 | md「全书结尾大概率会回到农场呼应」；`text/ch26_chap26.txt` 尾声全在墨尔本书店/公寓，未回农场 | 提示（预言被后文推翻） |
| 错③ | 读者视角 | md「妈妈那边多半也有类似称呼」；`text/ch01_chap1.txt:80` 妈妈用的是 “sweetie”，非 possum | 提示（无据推测） |

## 取证

```
/usr/bin/grep -o "And if" text/ch01_chap1.txt | wc -l   → 3（全段）
引语块内（md:28 的引语）逐字：And if I lose my post-grad program… And if I lose my PhD offer… = 2 次
/usr/bin/grep -n "sweetie" text/ch01_chap1.txt → 80: “You’ll do so well, sweetie. We’re all here rooting for you.”
```
