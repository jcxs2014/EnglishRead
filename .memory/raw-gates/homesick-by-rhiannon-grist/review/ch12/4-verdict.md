# ch12 4-verdict

- 文件：`ch12 a rug for the fragile softness of myself.md`
- 结论：**1 阻断 / 2 提示**

## 说明

**阻断 1（章号错标 + 原句归属）**：块 2「为什么这样写」写“这也把 ch01 的房产宣传语（“we hope you love your new home”）反过来了”。该句不在 ch01，而在 ch06：

```
$ /usr/bin/grep -rn -i "new home" text/
text/ch06_chapter_6.txt:155:We hope you love your new home!
$ echo $?
0
```
（ch01 全文无此句；ch06 上下文是中介把她的乔迁照发在 Facebook 并 tag 了她，见 text/ch06_chapter_6.txt:150-155。）

**提示 2 条**：① 块 5 把 `I’m sure you’ll find what you’re looking for there` 译作“我保证你能在那儿找到想要的”（“I'm sure”＝我确信，非“保证”）；② 块 4 把原文的 `a stuffed fox on a high shelf`（text/ch12_chapter_12.txt:101）写成“货架旁蹲着一只龇牙的标本狐狸”（位置与姿态均偏移）。

## 已核实为正确

① 门是“一定是我睡前没关严”的自我判词；② 螳螂/坟墓两句逐字无误；③ 店主原话“You should check one of the bigger supermarkets just outside Glasgow.”；④ 她挑的是“最近、也最小”的那块；⑤ 拒绝收据（“No-thank-you-don’t-need-one.”）与“抱地毯走回家”均在原文。
