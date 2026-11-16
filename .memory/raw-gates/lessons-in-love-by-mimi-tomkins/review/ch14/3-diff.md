# R3 对账 · ch14

| 单子 | 项 | 两侧原文 | 结论 |
|---|---|---|---|
| 漏 | 无 | 素读 8 条（1894/折叠床/鸡名/说漏 love/删志愿/护心宣言/忌日/双胞胎偷看）在 md 均有 | 通过 |
| 编 | 无 | — | 通过 |
| 错① | 代词/施事 | md 中译「你是她认识的最聪明的人之一」；原文 `You are one of the smartest people you know`（第二人称 you） | 阻断（人称错） |
| 错② | 预判 | md「Kyiv/Parma 后文大概率出来救场」；ch15–26 `grep Kyiv/Nugget/Schnitzel` 零命中 | 提示 |
| 错③ | 措辞 | 「四轮表白」「下本书（下章）」 | 提示 ×2 |
| 错④ | 总结 | 「半句 I love 双双卡壳」；他的 love 并未卡壳（是失言滑出） | 提示 |

## 取证
```
/usr/bin/grep -n "smartest people" text/ch14_chap14.txt → 518: You are one of the smartest people you know
/usr/bin/grep -rn "Kyiv|Schnitzel|Nugget" text/ch1[5-9]*.txt text/ch2*.txt → 无输出
```
