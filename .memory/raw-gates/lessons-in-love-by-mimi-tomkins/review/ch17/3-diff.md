# R3 对账 · ch17

| 单子 | 项 | 两侧原文 | 结论 |
|---|---|---|---|
| 漏 | 无 | 素读 8 条（girlfriend/更开朗/live for/书房黑史/sees something/五十万/cancer/章末答案）在 md 均有 | 通过 |
| 编 | 无 | — | 通过 |
| 错① | 语言 | md「以关心 form 出场」 | 提示 |
| 错② | 指认 | md「下一块她自嘲的 Girls love a man they can fix」；该句在本块引语之前 | 提示 |
| 错③ | 归属 | md「她在 ch07 的 suspenders 名场面」；吊裤带是 Oliver 穿的 | 提示（归属错） |
| 错④ | 跨章 | md「ch01 埋下的 something to live for」；ch01 只有 `a reason to live`（另一句） | 提示 |

## 取证
```
/usr/bin/grep -n "suspenders" text/ch07_chap7.txt → He’s got suspenders on（指 Oliver）
/usr/bin/grep -n "Girls love a man" text/ch17_chap17.txt → 101（在 actual person 段之前）
/usr/bin/grep -n "reason to live" text/ch01_chap1.txt → 107
```
