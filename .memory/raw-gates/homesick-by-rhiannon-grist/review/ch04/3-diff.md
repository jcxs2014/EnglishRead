# ch04 3-diff（素读事实 → md 对账）

| # | 素读事实 | md 位置 | 判定 |
|---|---|---|---|
| 1 | 呛着惊醒、卧室空荡、灰光从天窗；伸手摸到把石屋一分为二的墙；昨夜动静已停 | 导航·一句话概括；块1 读者提示 | 对应 |
| 2 | 1a 那半草坪被修得整整齐齐：交替条纹、直角、无杂草；她确信昨天不是这样 | 块1；导航 | 对应 |
| 3 | 内心自问自答："What's wrong, Tamsin?"…"Girl, you need to get out more" | 导航；人物弧线（引原句） | 对应 |
| 4 | 十点；替邻居找理由；决定去打招呼；吃最后薯片葡萄、编油头 | 导航·一句话概括 | 对应 |
| 5 | 门开黑缝；半张脸：圆而水润不眨的眼、微斜恳求的眉、扁塌长发；古怪的熟悉感；声音小、凭音高假定"她"、猜与自己同龄 | 块2；导航 | 对应 |
| 6 | 握手后幻想友谊→野餐/万圣节太妃苹果→成为恋人→结婚→拆墙让 Sgàthan Sìth 合一 | 块3；导航 | 对应（"两栋房子"译法偏移，见提示3） |
| 7 | 问是否听见墙声→邻居看墙、摇头；她提出带东西；邻居道谢"very generous"、邀她进屋；门开更大却更暗、人藏门后、嘴角在笑 | 块4；导航 | 对应 |
| 8 | 她拒绝进屋；邻居"哦，好吧。你好"后关上门；她忘了挡风玻璃与问电；回 1b 背包步行四十分钟去村；父亲的话；榆树叶像掌声 | 导航；一句话总结 | 对应 |

判定汇总：**阻断 1 / 提示 3**

证据：

```
$ /usr/bin/grep -n -i -E "scratched|pry|jimmy|crowbar|yale" text/ch02_chapter_2.txt
$ echo $?
1

$ /usr/bin/grep -n -i -E "scratched|pry|jimmy|crowbar|yale" text/ch01_chapter_1.txt
104:... Getting a standard, square-head Yale lock key had been a surprise ...
125:I ran my hand over the surface of the door. They’d been careless placing the lock. ... they’d failed to hide the deep scratches in the woodwork all around the edge. Maybe they’d had to pry it open after the last inhabitant. ...
128:... My anachronistic lock. My scratched door. ...
$ echo $?
0

$ /usr/bin/grep -n "closed the door" text/ch04_chapter_4.txt
161:Then she smoothly and quickly closed the door.
$ echo $?
0
```
