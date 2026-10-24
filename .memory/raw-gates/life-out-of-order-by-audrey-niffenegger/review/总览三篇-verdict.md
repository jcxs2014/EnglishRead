# 总览三篇 · T3 判定（写作方同会话深审）

机器层：`overview.py quotes` 46/46；`overview.py full` A 整串 18 / ❌ 查无 0 / 拼接 0；`gate.sh` EXIT=0。
人判：三篇逐段逐句回 `text/` 找支撑行（`00_概述.md` 66 行、`00_金句精选.md` 30 句 × 4 子项、`00_情感节点.md` 10 节点 × 2–3 引语）。

| # | 位置 | 改前 | 改后 / 依据 |
|---|---|---|---|
| 1 | 概述·出处 | 故事在 1975 至 2098 年之间来回 | 1964 至 2098 年（`text/ch13_coming_attractions.txt:18` "Thursday, November 19, 1964"） |
| 2 | 概述·梗概 2 | 为被撞死的骑行少年立一辆白漆的 ghost bike | 十八岁女孩莉莉·汉科（`text/ch05_ghost_bikes.txt:37` "A girl named Lily Hanko… She was only eighteen."） |
| 3 | 概述·梗概 4 | 十三岁的杨青从 2044 年被扔进 1999 年的门廊 | 十六岁（`text/ch14_oliver_arrives.txt:18` 抬头 "Oliver is 16"） |
| 4 | 概述·梗概 4 | 一九七五年，阿尔芭看着这个少年一天练十四小时琴 | 看着三十八岁的奥利弗一天练十到十四小时琴（`text/ch45_oliver_practices_piano.txt:18` 抬头 "1975 (Alba is 24, Oliver is 38)"、同文件 "ten hours a day, twelve, fourteen"） |
| 5 | 概述·梗概 4 | 到了 ch69，贝克自己走进那座记忆宫殿 | 贝克把「来世」当成可以送人的礼物：她安排好一切，让阿尔芭在记忆宫殿里待了一小时，出来时她已经没有脉搏（`text/ch69_a_murmuration.txt` 末段 "Beck’s body is crumpled on the floor… she is dead, as she told me she would be."） |
| 6 | 情感节点·节点二 | 这句是扎克转述的小说里的句子 | 阿尔芭先念出布尔加科夫，扎克接「那是我最喜欢的书」（`text/ch01_the_last_party.txt:481-483`） |
| 7 | 情感节点·节点二 | 年长的阿尔芭对扎克说的全部内容 | 不是全部：扎克追问「什么时候」，她答「现在。今晚。」（`text/ch01:1407-1413`） |
| 8 | 情感节点·节点四 | 十八岁骑行少年 | 十八岁女孩莉莉·汉科（同上 #2） |
| 9 | 金句 ⑤ | 两人约定一年后再给答案，最后提前结了婚 | 她定下期限「明年七月十五日再给答案」，两人在 2025 年 8 月结婚（`text/ch05:574`、`text/ch09:52`） |
| 10 | 金句 ㉔ | 阿尔芭承认她和扎克之间有说不清的关系 | 说的是奥利弗：她克制着不问私人问题，「He’s my friend. I want that to be enough.」（`text/ch51_random_acts_of_randomness.txt:332-333`） |
| 11 | 金句 ⑮ 呼应 | ch44 她谎称那是贝克的设备 | ch03（`text/ch03_fallout.txt` 地下室多锁钢门与「Beck 的电脑设备」那段；ch44 无此情节） |

修后复跑：`overview.py quotes` 仍 46/46、`full` 查无 0 / 拼接 0；`gate.sh` EXIT=0。
⚠️ 记一行（不修）：`overview full` 报「引语标签覆盖 44/72 章，28 章未被任何总览引语提到」（体裁允许，非阻断）。

## 已核实为正确（防误修）

- 「戈麦斯在车里对扎克引雷蒙德·威廉斯」——`text/ch07_mayday.txt:377` "Someone taps on the passenger side window… he gets in"，两人确实在车内。
- 「克莱尔说 You can choose. In the present, you can always choose.」——`text/ch05_ghost_bikes.txt:307` 那段是 Mama（克莱尔）对扎克说的。
- 「店主在吧台后替她父亲存衣服」——`text/ch09_no_place_like_home.txt:52` "the owners kept a stash of clothes for him behind the bar, and now they do the same for me."
- 「露辛达失踪三十四天后回到长椅」——`text/ch60_the_return_of_the_darling.txt:58` "“Thirty-four days,” I tell her."；同章 36 行她在图书馆前的长椅上等。
- 「亨利在时间旅行中落进医院储藏间、双脚已失」——`text/ch38_an_horizon…:28` "a supply closet in a hospital"、:58 "Since I lost my feet"。
- 「1927 年纪念警察的巨像被脱轨电车撞毁」等干草市场细节——`text/ch17_haymarket.txt` 现场段落。
