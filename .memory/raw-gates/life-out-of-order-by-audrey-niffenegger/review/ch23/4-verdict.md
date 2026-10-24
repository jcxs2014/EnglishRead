# ch23 Red Galoshes — 判定表

机器层：`bash scripts/chapter.sh ".../ch23 red galoshes.md" --json` → **rc=0**，verdict=ok，
块数 4（本书 71 章中位 6、限 2–15；本章 1097 词，block_target 2–3 故未报警）、引语段 4（4/4 `ok:true`，查无 0）、空引号 0、子项缺 0、关键词坏 0、CJK 低 0。
**机器 rc=0，人判 1 处阻断。**

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 引语逐字 | `2-machine.json` quotes 4 段全 `ok:true`（pos 95 / 314 / 2592 / 5142） | 通过 | 假红（无问题） |
| 「噩梦是真的」这一问答被整段跳过 | `text/ch23_red_galoshes.txt:212` "“Was it real? I remember it, like it was real.”"；`:216` "“Yes,” she says. “I’m pretty sure it’s real. It’s a long time from now.”"；`:224` "“It wasn’t safe. You were right to stay inside the house.”"；`:232` "“Just the wind,” she says. “Nothing but the dark and the wind.”" | md 搜 `真的`=0、`很久以后`=0；无块覆盖；md:15"噩梦的意象在末尾被重新提起"在块里无着落 | **阻断（漏）** |
| 勋伯格《和声学》 | `text/ch23_red_galoshes.txt:165` "It’s the one Grandpa gave me for Christmas, Schoenberg’s Theory of Harmony."；`:173` "You’ll love it when you’re fifteen." | md 搜 `勋伯格`=0 / `和声`=0 / `十五岁`=0 | 提示 |
| 未来的 Alba 四十六岁 | `text/ch23_red_galoshes.txt:18` "Wednesday, April 7, 2010 (Alba is 8 and 46)" | md 只写"八岁"与"2047" | 提示 |
| 黑暗里说话的理由 | `text/ch23_red_galoshes.txt:198` "It’s like you’re talking inside my head, and I’m in your head."；`:202` "She was me, but I’m not her, yet." | 未进块 | 提示 |
| 秘密的坏处 | `text/ch23_red_galoshes.txt:140` "He might feel . . . left out."；`:106` "you might resent that" | md:90 只写"必须瞒着爸爸" | 提示 |
| 访客是"已经坐在那里" | `text/ch23_red_galoshes.txt:28` "Other Alba is sitting in my chair with the reading lamp on" | md:13"推门进来" | 提示（编） |
| 阅读灯的位置 | `text/ch23_red_galoshes.txt:28` "sitting in my chair with the reading lamp on" | md:31"床头那盏阅读灯" | 提示 |
| 形态：H1「23. Red Galoshes」、导航 5 项、四子项齐 | `2-machine.json` form 全绿（h1_shape_ok true、nav_count 5） | 通过 | 假红（无问题） |

## 报数（四组）

- **逐字**：4/4 通过，0 失败。
- **对应**：4 块全通过。
- **形态**：全绿（但 1097 词只 4 块，块均偏少——机器未报警，人工记为观察项，不判阻断）。
- **断言**：10 条断言，3 通过、**1 阻断**、6 提示。

**本章 rc=0；1 处阻断：本章的"预言落地"那一问答没有任何块承载，md:15 还替它宣称了"前后扣住"。**

**改法**：补第 5 块，引语取 `text/ch23_red_galoshes.txt:212-232`（"Was it real?"…"Nothing but the dark and the wind."），并在导航 md:11 末尾补一句"她确认那个梦是真的、发生在很久以后，屋外只有黑暗与风"；md:15"噩梦的意象在末尾被重新提起"随之成立。

## 已核实为正确（防下一轮误修）

1. `text/ch23_red_galoshes.txt:18` "(Alba is 8 and 46)" —— 不必改成"8 岁和 45 岁"：2047−2010=37，8+37=45，但原文抬头写 **46**，是作者给的数，md 未引用故不算错，补写时按原文写 46。
2. `text/ch23_red_galoshes.txt:46` "“2047. It’ll be Christmas in a couple weeks.”" —— 她来自 2047 年**圣诞节前约两周**；md:11"2047 年的圣诞节前"准确，勿改成"2047 年圣诞"。
3. `text/ch23_red_galoshes.txt:54` "I just got Mama some bright red galoshes." —— 雨靴是**买给 Mama 的圣诞礼物**，不是买给自己的；md:11"一双鲜红的雨靴"未错，若补写勿写成"她穿着红雨靴回来"。
4. `text/ch23_red_galoshes.txt:122` "“Daddy doesn’t know Beck. That is, he met her once, but he didn’t know who she was.”" —— 是"见过一次但不知道她是谁"；md:90 表述正确，勿改成"从没见过"。
5. `text/ch23_red_galoshes.txt:80` "“Beck will be good for her. And for you, too.”" —— 好的是**两个人**（Mama 与 Alba），md:90"会让妈妈不再常常哭"只取一半，但未写"只对妈妈好"，不算错。
6. `text/ch23_red_galoshes.txt:114` "“She’ll hardly ever cry.”" —— 是"几乎不再哭"，不是"再也不哭"；md:90"不再常常哭"**正确**，勿改强成"再也不会哭"。
7. `text/ch23_red_galoshes.txt:181` "Her hand is cold and kind of bony… It feels strong, like Daddy’s hands." —— 手"像爸爸的手"是**力量感**，不是"像爸爸本人"；md:90"像爸爸一样有力的手"正确。
8. `text/ch23_red_galoshes.txt:240` "You’ll walk through the valley of the shadow of death, and fear no evil." —— 是诗篇 23 的句子；md:51"走过死荫的幽谷也不怕"未误引成"不怕死"。
9. `text/ch23_red_galoshes.txt:245` "I don’t remember sleeping; I don’t dream anything; when I wake up, Other Alba is gone." —— "没做梦"指**这一觉**，不是"她从此不做梦"；md:90"天亮时，床上只剩她一个人"未把"不做梦"写进去，不算漏关键（它只是收尾的轻描）。
10. `text/ch23_red_galoshes.txt:37` "“What year is it?”" / `:41` "“2010.”" —— 是**小 Alba 反问**"你从哪一年来"之前的对答；md:11"从 2047 年的圣诞节前回来"方向正确（未来 Alba 问年份，小 Alba 答 2010）。
