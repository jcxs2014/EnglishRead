# ch04 4-verdict

- 文件：`ch04 the mown lawn and half a face.md`
- 结论：**阻断 1 / 提示 3**

## 阻断

**阻断 1（章号错标：把 ch01 的撬门痕记成 ch02）**
- 位置：块4 读者视角——"ch02 是她自己那扇被撬过的门"。
- 原文证据：撬痕与新锁写在 ch01：`text/ch01_chapter_1.txt:104` "Getting a standard, square-head Yale lock key had been a surprise…"；`:125` "…they’d failed to hide the deep scratches in the woodwork all around the edge. Maybe they’d had to pry it open after the last inhabitant."；`:128` "My anachronistic lock. My scratched door."
- 查证命令：`/usr/bin/grep -n -i -E "scratched|pry|jimmy|crowbar|yale" text/ch02_chapter_2.txt` → 无输出，`echo $?` = 1。
- 建议改为：「ch01 是她自己那扇带新 Yale 锁、门框四周有深撬痕的门」。

## 提示

1. **位置**：导航·一句话概括"对方轻轻关上门"。
   **问题**：原文 `text/ch04_chapter_4.txt:161` 是 "Then she smoothly and quickly closed the door."——"流畅而迅速"，不是"轻轻"；这一差别正是本章的诡异点（不是温柔，是利落得没有余地）。
   **建议**：改为"对方流畅而迅速地关上了门"。

2. **位置**：导航·人物弧线"事中只会说 Sorry"。
   **问题**：她实际说了不止 Sorry：`text/ch04_chapter_4.txt` 中有 "Hi, I'm Tamsin. I'm your new neighbour."、"I'm driving into the village. Do you need anything?"、"That's okay. Just wanted to say hello."——"只会说 Sorry"把她的失语夸大成只剩一个词。
   **建议**：改为"开口就道歉、话头一再被自己掐断（Sorry / Hi, I'm Tamsin… / Just wanted to say hello）"。

3. **位置**：块3 中文理解"把两栋房子之间的墙拆掉"。
   **问题**：原文是 "the walls between our two homes"——1a 与 1b 是同一栋石屋被一分为二，"两栋房子"读起来像两座独立建筑，与本章"把房子合回一个整体"的分析自相拉扯。
   **建议**：改为"把我们两个家之间的墙拆掉"。

## R4 三问

1. **谁做的**：伸手的是邻居——`text/ch04_chapter_4.txt:86` "She reached out a limp hand."，Tamsin 是去握的一方（`:91` "Feeling rude, I took it"），md 未反置。关门（`:161`）、摇头、邀她进屋（`:140` 附近）、在门后微笑（`:152`）都是邻居做的，md 归属正确。"编头发""吃薯片葡萄"是 Tamsin 做的，正确。
2. **关系/谁欠谁**：1a 与 1b 是同一栋半独立石屋的两半（`text/ch04_chapter_4.txt:101` "the walls between our two homes"），不是两栋独立房子；两人是共墙邻居，不是房东与租客、也不是亲属。md 的"两栋房子"是唯一的偏移（见提示3）；未把邻居写成房东或旧识，正确。
3. **数字与死因**："十点"有据（`text/ch04_chapter_4.txt:47` "Ten o’clock in the morning."）；"四十分钟"有据（`:179` "It would be a forty-minute walk to the nearest village."）；"九十度"有据（`:23` "Each corner was a tight ninety degrees."）。年龄无断言——原文只有 Tamsin 的猜测 "I guessed she must be about my age"，md 只写"猜她与自己年纪相仿"，正确。本章无死亡、无金额。

## 已核实为正确（下一轮不要改坏）

- 8 条素读事实在 md 均有落点，无遗漏：呛醒与隔墙（导航）、草坪条纹（块1）、内心自问自答（导航+人物弧线）、十点/编发（导航）、半张脸细节（块2）、友谊—恋人—拆墙幻想（块3）、问墙声—摇头—邀入（块4）、拒入—关门—四十钟步行—父亲的话—榆树叶（导航+一句话总结）。
- 引语逐字无误：`text/ch04_chapter_4.txt:26` "What’s wrong, Tamsin?"；`:20` "1a’s side of the front lawn was now neatly mown."；`:77` "half a face"；`:101` "opposites attract"；`:188` 榆树叶一句（"The leaves on the elm tree hushed in the wind, like a small audience clapping me off stage."）。
- "粉红指甲"未在本章误植；"Girl, you need to get out more." 属 Tamsin 内心自语（`:44`），md 未误给邻居。
