# R3 对账 · ch03

| 单子 | 项 | 两侧原文 | 结论 |
|---|---|---|---|
| 漏 | 无 | 素读 8 条（起哄/职业划界/眨眼短信/试水/无情节吐槽/雇佣反问/雀斑距离/不回头的离开）在 md 均有 | 通过 |
| 编① | 读者层虚构台词 | md「Oliver 反问『你为什么要自我惩罚』类对话」；`/usr/bin/grep -c -i punish text/*.txt` → 0 命中（退出码 1） | 提示（虚构预期） |
| 编② | 读者层虚构情节 | md「近距离婚礼兑现」；全书无婚礼（`grep -i "wedding\|married"` 仅 ch13 父母未合法结婚、ch14 前任「married with three kids」假设） | 提示（虚构预期） |
| 错 | 无 | 计数/施事/章号均核 | 通过 |

## 取证
```
/usr/bin/grep -c -i "punish" notes/books/novels/lessons-in-love-by-mimi-tomkins/text/ch*.txt | grep -v ":0"
→ 无输出；退出码 1（零命中）
/usr/bin/grep -c -i "wedding\|married" .../text/ch*.txt | grep -v ":0"
→ ch13_chap13.txt:1  ch14_chap14.txt:1
```
