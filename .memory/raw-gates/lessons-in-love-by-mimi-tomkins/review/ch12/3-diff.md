# R3 对账 · ch12

| 单子 | 项 | 两侧原文 | 结论 |
|---|---|---|---|
| 漏 | 无 | 素读 8 条（三家店/剁腿/职业口径/破载片/吓跑他/邀他来农场/慢慢提/取消短信）在 md 均有 | 通过 |
| 编 | 无 | — | 通过 |
| 错① | 计数 | md「professional working relationship 全书第三次出场（ch03、ch05、本章）」；全书 grep 仅 ch12:92 一次 | 阻断（计数） |
| 错② | 言语方向 | md「Eden 嘴上答应，心里全是 Absolutely not」；原文她先说 `“Absolutely not.”`（text:209），后说 `“Okay,” I say, mostly to placate Mum`（text:215） | 阻断（说/想颠倒） |
| 错③ | 计数 | md「Not now 两次独立成拍」；原文 `Not now. Not when…`（text:224）各一次 | 提示 |
| 错④ | 跨章 | md「too much 从 ch05 起有伏笔」；ch05 无该词（`grep too much` ch05 未命中） | 提示 |

## 取证
```
/usr/bin/grep -rn "professional working relationship" text/*.txt → 仅 ch12_chap12.txt:92
/usr/bin/grep -n "Absolutely not" text/ch12_chap12.txt → 209（她说）
/usr/bin/grep -n "Not now\|Not when" text/ch12_chap12.txt → 224（各 1 次）
/usr/bin/grep -l "too much" text/ch05*.txt → 无输出
```
