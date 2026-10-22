# ch03 3-diff（素读事实 → md 对账）

| # | 素读事实 | md 位置 | 判定 |
|---|---|---|---|
| 1 | 电灶同样用电、不通电就没法做饭；她把意面酱料塞进空橱柜，坐客厅地板吃薯片葡萄当第一餐；原想外卖披萨＋马克杯香槟，实际掬水喝 | 导航·一句话概括；块1 | 对应（但"电磁炉"是译词偏移，见 4-verdict 提示1） |
| 2 | 天黑时恐慌、自问"我做了什么"；三十多岁独自搬到陌生地方是疯狂之举 | 导航·一句话概括；人物弧线 | 对应 |
| 3 | 想念爱丁堡：灰窗景、街声、咖啡馆、啤酒厂麦芽香、Leith 海盐风 | 导航·一句话概括 | 对应（"利斯"＝Leith，正确） |
| 4 | 毛巾铺床垫、只穿内衣、连帽衫当枕头；房子要家具/保温/新锅炉/新电线；搬家是前三压力事（与离婚、死亡并列） | 导航·一句话概括；块3 | 对应（"前三压力事"未落，不判） |
| 5 | 很久没跟活人说话、想不出可打电话的人；抱自己肩膀假装是别人的拥抱 | 块2；导航 | 对应 |
| 6 | 墙后吱呀→隔壁脚步、耳边砰响、尖叫刮擦，"像在搬重家具"；十一点；1a 整夜不停 | 块3；导航；一句话总结 | **错**（提示级：把"听起来像搬家具"写成"有人在搬动看不见的家具"，推断升为事实，另加"看不见的"） |
| 7 | 梦里后视镜中的黑暗吞没一切；抵达只有一扇门的房子；她一向有压力梦（手变铅、大学被冲走、父亲拆包裹） | 导航·一句话概括；叙事手法 | 对应 |
| 8 | 屋内变旧办公室（玻璃隔断、橙色百合、手提箱→背包→手袋）；粉红指甲的女总监三问；她**背诵了弱点**、说"Something's wrong"；最后总监掰断自己小指 | 块4；导航；叙事手法 | **错（阻断）**：叙事手法称"对话只有提问，没有她的回答"，原文她答了 |

判定汇总：**阻断 1 / 提示 2**

证据：

```
$ /usr/bin/grep -n "recited my weaknesses" text/ch03_chapter_3.txt
158:Her eyes scanned me up and down as I recited my weaknesses.
$ echo $?
0

$ /usr/bin/grep -n "Something’s wrong" text/ch03_chapter_3.txt
173:“Something’s wrong.”
$ echo $?
0

$ /usr/bin/grep -n "hob was also electric" text/ch03_chapter_3.txt
5:Unfortunately, the hob was also electric. With no clue how to turn the electricity on, there was no way to cook anything. ...
$ echo $?
0

$ /usr/bin/grep -n "moving heavy furniture" text/ch03_chapter_3.txt
92:... It sounded like they were moving heavy furniture around. ...
$ echo $?
0
```
