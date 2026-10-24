# ch15 Halloween · R5 判定

- 机器层：`chapter.sh` **rc=0**；块数 3 / 引语 3 / segment_miss 0 / 查无 0 / 空引号 0 / 结构缺项 0 / 关键词异常 0 / 字数 755
- 素读：`1-suread.json`（9 条 + 转折点补条；**全章 Oliver 第一人称**，声部标记 `Oliver:`）
- 对账：`3-diff.md`

| # | 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|---|
| 1 | 说话人未错置（Zach→Alba 的那句没被记成对 Oliver 说） | `text/ch15:38` `“Wait just a minute, we’re running low! Alba, honey, could you get me that bag of KitKats?”`；md:14 归给 Zach、md:12「他在这一章里没有开口，也没有人对他说话」 | 正确，无错置 | 跳过（核实无误） |
| 2 | 「真丈夫是 Zach、秘密是 Oliver」的归属 | `text/ch15:42` `This is Zach, her real husband… I’m just her other husband.`；`:43` `this is real, and I am the secret, not him.`；md:11/13/29/31/42 | 方向正确，`not him` 的 him 未被翻转 | 跳过（核实无误） |
| 3 | 门廊下「坏掉的塑料机器人…无害而悲伤」未进任何块 | `text/ch15:33` `these broken robots look quite harmless and sad, which are not feelings I usually have about bio-robots.`；`/usr/bin/grep -nE "机器人\|robot" "ch15 halloween.md"` → 无输出 **rc=1** | 2044/2031 两套世界的对照点缺席，属铺陈非事件 | 提示 |
| 4 | 「这里还有树」未进 md | `text/ch15:28` `There are still trees here, and they have yellow and red leaves.`；`/usr/bin/grep -nE "still trees\|还有树" "ch15 halloween.md"` → 无输出 **rc=1** | 全书缺树世界的暖色对照漏掉（素读补条） | 提示 |
| 5 | 街景清单未收全（粉色章鱼、僵尸长颈鹿） | `text/ch15:28` `a little girl dressed as a pink octopus. One boy is dressed as a zombie giraffe, covered in fake blood.`；`/usr/bin/grep -nE "章鱼\|长颈鹿\|octopus\|giraffe" "ch15 halloween.md"` → 无输出 **rc=1** | 清单节略 | 提示 |
| 6 | 本章只有 3 块覆盖 60 行，密度是否够 | `text/ch15` 全长 60 行、正文 5 段；md 3 块 755 字；`chapter.sh` 报 `block_hint ""`、`block_target [2,2]` | 门禁按书内主流判为达标；但 `:33`（机器人）与 `:28`（树木）无处安放，见上三条 | 提示（并入 3/4/5） |
| 7 | 抬头三家年龄 | `text/ch15:18` `Friday, October 31, 2031 (Oliver is 27, Alba is 30, Zach is 30)`；md:11 | 逐字对 | 跳过（核实无误） |
| 8 | 时态判读（现在时 + 末句后推） | `text/ch15:60` `When I wake up, it’s afternoon… for a long time afterward I don’t feel much of anything at all.`；md:15 | 判读正确 | 跳过（核实无误） |

报数（四组）：

- **逐字**：0（3 条引语全中；**10 条词汇例句逐字全中**，脚本核 13 行 0 miss）
- **对应**：0（3 块全部对得上，见 3-diff 第四节）
- **形态**：0（H1 `15. Halloween`；导航 5 项齐；子项原句1-3 齐；块序与原文一致；有「一句话总结」）
- **断言**：0 阻断 + 3 提示

## 已核实为正确（防下一轮误修）

| 看着像错 | 回原文核对 | 结论 |
|---|---|---|
| 「Oliver 27、Alba 30、Zach 30」——Zach 与 Alba 同龄、Oliver 小三岁 | `text/ch15:18` `(Oliver is 27, Alba is 30, Zach is 30)` | 原书抬头原文，勿改 |
| 同一章里 Oliver 27 而 ch14 他 16（差 80 年） | `text/ch14:18` `(Oliver is 16, Alba is 30)`；`text/ch15:18` 他 27 | 时间旅行者，年龄按各自时间线走，勿按年份换算 |
| 「他说自己是『另一个丈夫』」像是自嘲过头 | `text/ch15:42` `I’m just her other husband.` | 逐字有据 |
| 「白床单先被认成 KKK」 | `text/ch15:28` `(at first I thought it was a KKK but then I remembered that is how Westerners represent their ghosts)` | 逐字有据，且原文自己给了纠正 |
| md:13「他落在万圣节的街上」 | `text/ch15:33` `I crawled under here because the street was crowded` | 「落在」指时间落点、他随即钻进廊下，不构成与原文冲突（若求稳可改「落在这条街上」） |
| 「不敢睡」 | `text/ch15:54` `I hug myself to keep warm; I don’t dare to sleep.` | 逐字 |
| 词汇 10 条例句 | disconcertingly 49 / trick-or-treaters 48 / shrubbery 38 / Victorian 23 / vanishing 49 / pavements 28 / curtains 49 / hiding place 38 / real husband 42 / bedroom 60 | 全部逐字命中 |
