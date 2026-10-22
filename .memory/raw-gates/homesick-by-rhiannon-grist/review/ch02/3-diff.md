# ch02 3-diff（素读事实 → md 对账）

| # | 素读事实 | md 位置 | 判定 |
|---|---|---|---|
| 1 | 前门直通主起居区，只有厚霉帘与下沉瓷砖门廊；她评这是农工做法，入冬前得改 | 块3 中文理解（"摔进下沉的门厅"） | 对应（仅取"下沉门厅"，帘与"入冬前处理"未展开） |
| 2 | 一楼打通大单间、无家具：左壁炉／远端发黄橱柜厨房／右楼梯／楼梯下斜切门（储物） | 导航·一句话概括；块1 | 对应 |
| 3 | 踏上地板被尖物扎伤、跌进箱子；血透过为搬家新买的灰羊毛袜；伤口小而整齐（"not as deep as I feared"），她记着查破伤风 | 导航·一句话概括；一句话总结；原句3 | **编**（写成"一枚钉子扎穿脚底"：原文明确"no nail"，且伤口"not as deep as I feared"） |
| 4 | 吱呀声像有人藏近处调姿势；声音从壁炉那面墙传来；她认定是邻居、站起盯墙；声音随即停止 | 块4 | 对应 |
| 5 | 冷冻柜/冰箱又黑又室温；开关发黏无效；清单有电无煤气；她估计要先通知水电公司 | 导航·一句话概括（"没通电、没有热水"） | 对应（未展开"有电但未接通"，不判） |
| 6 | 浴室在檐下、PVC 天窗、斜顶不能站洗；无电热水器，龙头只出冷水；清单只写"shower bath"，供暖写"Biomass heating system"，她想到煤桶烧水 | 导航·一句话概括；词汇 scuttle/euphemistic | 对应（导航已覆盖核心；浴室细目不展开，不判） |
| 7 | 卧室与 1a 不同——**她这侧**窗上无窗帘，长夏夜难熬；前任留下床垫无床架；晾衣架在檐下柜里摊开着（要放进去得先折再展） | 导航·Tropes（"声音穿墙、无窗帘的卧室"） | **错**（提示级：把"我这侧无窗帘"挂在"隔壁有人"线索下，方向易读反——原文是 1a **有**窗帘） |
| 8 | 折叠晾衣架触发荧光灯/笑声/亮粉指甲油→抽气、沉默、尖叫；她把晾衣架扔向树林失准，砸碎自己车挡风玻璃，警报响，1a 毫无反应 | 块5；块6；导航 | 对应 |

判定汇总：**阻断 1 / 提示 2**

证据：

```
$ /usr/bin/grep -n "no nail" text/ch02_chapter_2.txt
47:I searched the floorboards for the nail or splinter that had stabbed me. I found a small blotch of blood, but no nail. The blood seeped into a small hole in the wood. I carefully ran my fingertip round its edges. I must have pushed whatever it was under the floor—
$ echo $?
0

$ /usr/bin/grep -n "deep as I feared" text/ch02_chapter_2.txt
44:I pulled off my sock and took a look at the sole of my foot. It was a small, neat wound. Not as deep as I feared, but it would still need cleaning. Blood wept out of the small pink puncture mark. I made a mental note to google tetanus.
$ echo $?
0

$ /usr/bin/grep -n "no curtains" text/ch02_chapter_2.txt
116:... Unlike in 1a, my upstairs window had no curtains. No blinds, no shutters, nothing. ...
$ echo $?
0
```
