# R3 对账 · ch13

| 单子 | 项 | 两侧原文 | 结论 |
|---|---|---|---|
| 漏 | 无 | 素读 8 条（72h/两千万/甩锅亡母/未婚/Taking her home/双胞胎作业/遗传/鸣不平）在 md 均有 | 通过 |
| 编 | 无 | — | 通过 |
| 错① | 计数 | md「六个词的邀请函」；`You’re coming home with me.` = 5 词 | 阻断（计数） |
| 错② | 施事 | md「是女方开的车（他开）」自相矛盾；原文 `I end up in the driver’s seat of my car, Eden on my left` | 阻断（方向） |
| 错③ | 计数 | md「四弟妹+爸妈=全家 six 口」；ch01 明写 `five kids`（五个孩子）⇒ 全家 7 口 | 阻断（计数） |
| 错④ | 记法 | 「B3/B4」英文字母块号 | 提示 |
| 错⑤ | 语言 | 「公路 become 灵修」中英混杂 | 提示 |

## 取证
```
python: len("You’re coming home with me.".split()) → 5
/usr/bin/grep -n "driver’s seat" text/ch13_chap13.txt → I end up in the driver’s seat of my car, Eden on my left
/usr/bin/grep -n "five kids" text/ch01_chap1.txt → Being the eldest of five kids
```
