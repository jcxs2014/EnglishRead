# ch20 Tiny Violin Lessons — 判定表

机器层：`bash scripts/chapter.sh ".../ch20 tiny violin lessons.md" --json` → **rc=0**，verdict=ok，
块数 9、引语段 10（0 查无）、空引号 0、关键词坏 0、子项缺 0、CJK 低 0、3298 词。
**机器 rc=0，人判 2 处阻断。**

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 引语逐字 | `2-machine.json` quotes 10 段全 `ok:true`（pos 113/327/1093/1338/3157/7785/8144/9076/11387/17253） | 通过 | 假红（无问题） |
| 回到过去的是 15 岁，不是"成年" | `text/ch20_tiny_violin_lessons.txt:18` "Tuesday, May 20, 2008 (Alba is 6 and 15, Clare is 36)" | md:11/14/15/27/47/77/141 六处写"成年的 Alba" | **阻断** |
| 2009 年 6 月 16 日是 Henry 46 岁生日 | `text/ch20_tiny_violin_lessons.txt:333` "Tuesday, June 16, 2009 (Clare is 38, Alba is 7, Richard is 72)"；`:348` "Today would have been Henry’s forty-sixth birthday." | md 全文 0 次（`grep -c 生日` → 0） | **阻断（漏）** |
| Henry 死后仍现身一次 | `text/ch20_tiny_violin_lessons.txt:343` "Even after he died? I asked. Only once, said Richard, but that was enough to make me hope." | md 全文 0 次（`grep -c 死后` → 0） | 阻断（同上条） |
| 四个纸杯蛋糕、紫色糖霜花 | `text/ch20_tiny_violin_lessons.txt:348` "a box of four chocolate cupcakes … flowers made out of purple frosting, Alba’s favorite." | 仅词汇表 md:137 收 cupcakes 例句，导航/块未提 | 阻断（同上条） |
| 那个点头的含义 | `text/ch20_tiny_violin_lessons.txt:362` "the small nod that means Now: together they begin again." | md:14 说成"为一个音准点头"；md:101 译文正确 | 提示 |
| ½ 号琴是她参与挑的 | `text/ch20_tiny_violin_lessons.txt:28` "helped me choose a ½ size Ming Jiang Zhu" | md:13"琴不是她自己选的"概括过宽 | 提示 |
| 这一天为何重要 | `text/ch20_tiny_violin_lessons.txt:143-144` "Mama recently told me this day was the first time she’d heard me really play … it gave her the will to keep driving me" | 未进任何块与导航 | 提示 |
| 祖父在叙述者的现在已死 | `text/ch20_tiny_violin_lessons.txt:196` "In my present my grandfather is dead." | 未进块 | 提示 |
| 引语省略号处省去什么 | `text/ch20_tiny_violin_lessons.txt:28` "“No!” I kept telling my parents. “Just try a little longer,” they always replied." | md:21 明说"省去的是她跟父母来回推托的几句对白"，**准确** | 已核实为正确 |
| 形态：H1、导航 5、四子项、9 块（限 2–15） | `2-machine.json` form 全绿 | 通过 | 假红（无问题） |

## 报数（四组）

- **逐字**：10/10 通过，0 失败。
- **对应**：9 块全通过（无"讲引语之外的上下文"）。
- **形态**：全绿（9 块，3298 词，block_target 6–10）。
- **断言**：12 条断言，5 通过、**2 阻断**、5 提示。

**本章 rc=0，但 2 处阻断：①"成年的 Alba"（应为 15 岁）；②整个 2009 年段的时间坐标与"Henry 死后仍来过一次"缺失。**

**改法（两句话）**：
1. 六处"成年的 Alba"→"十五岁的 Alba"（md:11/14/15/27/47/77/141）。
2. 在导航 md:11 与 `## 一句话总结` md:141 的 2009 年段补一句："那天本是 Henry 四十六岁生日，Richard 买了四个巧克力纸杯蛋糕；他说 Henry 死后还来过一次——她问『Even after he died?』，他答『Only once … but that was enough to make me hope』"，并考虑把 `text/ch20_tiny_violin_lessons.txt:343` 或 `:348` 提升为第 10 块。

## 已核实为正确（防下一轮误修）

1. `text/ch20_tiny_violin_lessons.txt:18` "Alba is 6 and 15" —— 两个 Alba 一个 6 岁一个 15 岁，**不要**把 15 岁写成"成年"以外的其他年龄（如 17/18）；也不要改成"两个都是 Alba 本人以外的角色"。
2. `text/ch20_tiny_violin_lessons.txt:28` "a ½ size Ming Jiang Zhu and a bright red carbon-fiber bow" —— 是 ½ 号（不是 1/2 以外尺寸）、红色碳纤维弓；md:11"黄纸"对应 `:267` "a yellow pad"，正确。
3. `text/ch20_tiny_violin_lessons.txt:188` "G. Why aren’t there any bars?" —— 小 Alba 自己说出 G 调、问"为什么没有小节线"；md:101 的对话归属正确，勿改成成年 Alba 告诉她调性。
4. `text/ch20_tiny_violin_lessons.txt:262` "Don’t stop sending me to Grandpa, and don’t tell him" —— 条件是"别停外公的课 + 别告诉外公"，md:11"条件是不要让祖父知道"未丢"别停课"（见 md:141 亦未提），补写时两句都要留。
5. `text/ch20_tiny_violin_lessons.txt:277` "He was playing Biber’s Passacaglia in G Minor." —— 比贝尔《G 小调帕萨卡利亚》；md 未误写成巴赫。
6. `text/ch20_tiny_violin_lessons.txt:353` "one reading it upside down, the other right side up" —— 一人倒读谱；md:11"用同一页谱玩镜像二重奏"正确。
7. `text/ch20_tiny_violin_lessons.txt:343` "Richard says he left the room intact because Henry used to show up at odd times, naked and disheveled" —— 房间原样保留的原因；md 未误写成"Clare 保留"。
