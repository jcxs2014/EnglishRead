# R3 对账 · ch15

| 单子 | 项 | 两侧原文 | 结论 |
|---|---|---|---|
| 漏 | 无 | 素读 8 条（复活节/发令枪/扔椅子/金蛋值十/二吻/85/Kiara）在 md 均有 | 通过 |
| 编① | 虚构场景 | md「对照 ch07 她让 Oliver『别提 Gemma』的遮掩」；全书 `grep -i "don.t mention|not mention|别提"` 无此场景 | 阻断（编） |
| 编② | 预判 | md「Greg 在总览式收尾章回归」；Greg 只到 ch24，ch26 无 | 提示 |
| 编③ | 预判 | md「Kiara 支线必然引爆」；ch24 全家已接受（They love her） | 提示 |
| 错 | 错字 | 「把『赃』写成功勋」应为「脏」 | 提示 |

## 取证
```
/usr/bin/grep -rn -i "don.t mention|not mention|别提" text/*.txt → 仅 ch10/ch19/ch21/ch24 的「不谈某事」，无 Gemma 场景
/usr/bin/grep -rn "Greg" text/*.txt → ch15/22/24；ch26 无
/usr/bin/grep -n "They love her" text/ch24_chap24.txt → 146
```
