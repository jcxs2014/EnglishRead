# R3 对账 · ch06

| 单子 | 项 | 两侧原文 | 结论 |
|---|---|---|---|
| 漏 | 无 | 素读 8 条（四百页/三百页/要读好几年/文学无限性/沉默家宴/妈妈在时/通信岗/actually matters）在 md 均有 | 通过 |
| 编 | block7 分析超出引语 | md 中文理解写「公司通信岗在招人，我报了你的名字」，该句在 text:125，**不在** block7 引语（text:134 起）内 | 阻断（分析超出引语） |
| 错 | 跨章指认 | md「ch05 里 Eden 家的农场告别（抱腿、哭、veranda）」；`grep veranda/possum` ch05=0、ch01=1，告别戏在 ch01 | 阻断（跨章错指） |

## 取证
```
/usr/bin/grep -c "veranda" text/ch05_chap5.txt → 0
/usr/bin/grep -c "veranda" text/ch01_chap1.txt → 1
/usr/bin/grep -c -i "possum" text/ch05_chap5.txt → 0
/usr/bin/grep -n "put your name up" text/ch06_chap6.txt → 125（block7 引语自 134 起）
```
