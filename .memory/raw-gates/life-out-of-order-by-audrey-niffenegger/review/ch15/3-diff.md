# ch15 Halloween · R3 对账

- 素读：`1-suread.json`（9 条 + 转折点补条，写定于打开 md 之前；**全章 Oliver 第一人称**，与 ch14 的 Alba 第一人称不同）
- 机器层：`2-machine.json`，rc=0，3 块 / 3 引语 / segment_miss=0 / 查无 0 / 空引号 0 / 字数 755
- md：`ch15 halloween.md`（78 行）

## 一、漏（素读有、md 无）

### L1（提示）门廊下那批「坏掉的塑料机器人」整条未进任何一块

```
text/ch15_halloween.txt:33  There is dirt under this porch as well as broken bricks, gravel and some plastic toys that look like robots—that is, they look like the humanoid robots that people once imagined would take over the world; these broken robots look quite harmless and sad, which are not feelings I usually have about bio-robots.
```

md 侧：第 11/12/14 行导航与第 19 行引语全都从「赤身、饥饿、寒冷」起，未提玩具机器人。
取证：`/usr/bin/grep -nE "机器人\|robot" "ch15 halloween.md"` → 无输出，**rc=1**。

判定：这是全章唯一一处写他「通常对生物机器人不会有的感觉」——反常感正是把 2044 与 2031 两套世界并置的着力点；但属铺陈非事件 ⇒ **提示**（可折进原句 1 的「读者视角提示」，一句话）。

### L2（提示）「这里还有树」这条暖色未进 md

```
text/ch15_halloween.txt:28  Halloween. There are still trees here, and they have yellow and red leaves.
```

md 侧：无。取证：`/usr/bin/grep -nE "still trees|还有树" "ch15 halloween.md"` → 无输出，**rc=1**。

判定：全书 2044 的世界几乎无树，这句是本章少见的暖色对照，且是素读「转折点自检」补进来的那条 ⇒ **提示**。

### L3（提示）街景清单未收全（粉色章鱼 / 僵尸长颈鹿）

```
text/ch15_halloween.txt:28  …holding the hand of a little girl dressed as a pink octopus. One boy is dressed as a zombie giraffe, covered in fake blood.
```

md 侧：只写「蜘蛛侠和裹白床单的鬼」（第 11 行、第 78 行）。取证：`/usr/bin/grep -nE "章鱼\|长颈鹿\|octopus\|giraffe" "ch15 halloween.md"` → 无输出，**rc=1**。

判定：属清单节略，不影响叙事 ⇒ **提示**。

## 二、编（md 有、原文无）

未发现。逐条核过 md 中所有可核查的实体与数值：

| md 写法 | 原文 | 结论 |
|---|---|---|
| 三家年龄（Oliver 27 / Alba 30 / Zach 30） | `text/ch15:18` `(Oliver is 27, Alba is 30, Zach is 30)` | 对 |
| 「蜘蛛侠」「神奇女侠」「白床单」「骷髅」「橙灯」「美国口音」 | `text/ch15:28` 逐项 | 对 |
| 「一袋 KitKats」 | `text/ch15:38` `that bag of KitKats` | 对 |
| 「剧院的包厢」「舞台上的演员」 | `text/ch15:38` `a box in a theater… like so many actors on a stage` | 对 |
| 「两层楼高的维多利亚式大房子」 | `text/ch15:23` `a large Victorian house`（原文无楼层数；md 第 78 行只写「一栋维多利亚式大房子」） | 对（未加楼层） |
| 「单层砖与玻璃的现代主义住宅」 | `text/ch15:38` `one level of brick and glass` | 对 |
| 「灌木剪成光滑的卵形」 | `text/ch15:38` `the shrubbery around it cut into smooth ovoid shapes` | 对 |

## 三、错（两边都有但不一致）

未发现。重点核过三处易错：

1. **说话人**：全章 Oliver 第一人称；md 第 12 行「他在这一章里没有开口，也没有人对他说话」与原文一致（`text/ch15:38` 那句 `Alba, honey…` 是 **Zach 对 Alba** 说的，md 第 14 行归给 Zach、第 11 行写「朝屋里喊了一声 Alba」，均未错置）。
2. **谁是真丈夫**：md 第 11/13/14 行与第 29/31 行引语均把 real husband 归 Zach、把「秘密」归 Oliver，与 `text/ch15:42-43` 一致。
3. **时间方向**：md 第 15 行「前面全是现在时，末句却用 for a long time afterward 往后看」——原文 `text/ch15:60` 确为现在时叙述 + 末句后推，判读正确。

## 四、R4 逐块对应（3 块）

| 块 | 引语 | 这段中文是不是在讲这句引语 | 三问（主语 / 受事 / 归属） |
|---|---|---|---|
| 1 | `It is impossible to be comfortable. I am naked, hungry and cold…` | 是。三句的分工（体感→身体清单→原因与判决）、破折号转向、`I would certainly be arrested` 的「档案式」落点都贴着引语讲，没有滑到全章主旨 | 主语：我（Oliver）；受事：藏身处、孩子；归属：`because the street was crowded` 是**他的**动机（md 第 21 行「于是爬了进来」正确），未错记成别人赶他进去 |
| 2 | `She says she loves me, but it’s obvious from the way she stands there with him…` | 是。四层 whatever 的递降、obvious/real 两个「最重的词」、secret 的身份义都从引语里来 | 主语：她（说爱、站着笑）、我（希望、假装、相信）；受事：她的幸福、我们在一起的「可能」；归属：`her real happiness is here` 的 here=街对面那栋房子（md 第 31 行明确），`not him` 的 him=Zach（md 未翻转） |
| 3 | `I climb into bed, into cold sheets, and pull the covers over my face and weep…` | 是。动作串不带情绪词、steadier→but 的假上扬、has departed 的无施动者被动都讲了，末句「站在那段日子之外」也扣住 for a long time afterward | 主语：我；受事：被单、被子、乐趣；归属：`some of the pleasure has departed **from my life**`——md 第 45 行「乐趣不是被谁拿走的」正确，未误写成 Alba 带走了它 |

R4 结论：3 块全部对应；无「引语选短了」或「讲主旨」的情形。唯一密度上的弱点是本章只有 3 块覆盖 60 行原文，`text/ch15:33` 那一段（机器人）与 `:28` 的树木对照无处安放 ⇒ 见 L1/L2。

## 附：一句话总结（md:78）核对

- 「赤身裸体、又饿又冷地缩在…门廊底下」✓ `text/ch15:33`
- 「透过木板交错出的几百个小菱形」✓ `:23`
- 「街对面那栋单层砖与玻璃的现代主义住宅门口，一个年轻男人在发糖，叫得出孩子的名字、夸他们的装扮，糖快没了就朝屋里喊 Alba 拿一袋 KitKats」✓ `:38`
- 「他在碎石里扒出一块平整的土面蜷着取暖，不敢睡」✓ `:54`
- 「回到自己的卧室…把被子拉过头顶哭」✓ `:60`
- 无一处超出原文。
