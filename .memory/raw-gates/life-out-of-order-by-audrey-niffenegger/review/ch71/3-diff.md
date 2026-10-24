# ch71 素读 vs 精读 差异（The Vanished World）

素读：`1-suread.json`（10 条，只读 `text/ch71_the_vanished_world.txt`，540 行 / 131 非空行 / 4694 词）
精读：`ch71 the vanished world.md`（152 行，10 块，导航 11–15，词汇 65–152 区间，总结 152）
机器：`chapter.sh --json` rc=0，10 块，引语段 10/10 命中（33/38/59/32/31/48/31/49/36/37 词，pos 640/2871/12160/14652/18912/20934/21998/22403/23925/24437），nav 5，H1 `71. The Vanished World` shape_ok，`block_target [9,15]`，`block_hint` 提示 10 块高于本书常见区间 3–9（本书最高即 10）

## 一、漏（素读有、md 无）

| # | 素读条目 | 原文证据 | md 侧 | 档 |
|---|---|---|---|---|
| 漏1 | 开篇：梦见自己回到上海童年卧室、母亲在隔壁唱《两只老虎》；醒来枕上有小而圆的湿点，不知是记忆还是梦 | text/ch71:23 `Oliver: I wake from a particularly vivid dream. I was small again, I was back in my old bedroom in Shanghai, in my narrow bed. In the next room my mother was singing:`；歌词 :30–58（`两只老虎 Two little tigers` / `跑得快 Running very fast` / `一只没有眼睛 One has no eyes` / `一只没有尾巴 One has no tail` / `真奇怪 How strange`）；:64 `I find small, round wet spots on my pillow. I am not sure if this was a memory, or merely a dream.` | **整段不在场**：`/usr/bin/grep -cE "两只老虎\|上海\|母亲" "ch71 the vanished world.md"` → `0`，退出码 **1**；`-nE "焗豆\|湿点\|枕"` → 无输出，退出码 **1**。全书唯一一次出现的奥利弗的母亲、《两只老虎》的缺眼缺尾意象、以及「记忆还是梦」的存疑，全部落空 | **阻断** |
| 漏2 | 三瓶啤酒的用处：老自己说「我们顺路去接阿尔芭」 | text/ch71:241 `“Why three beers?”`，:245 `“We’re going to collect Alba on our way.”` | 第 152 行只写「带上啤酒、毯子与药膏」；`三瓶` 零命中（同上 grep B，rc=1）。数字与动机的呼应丢失 | 提示 |
| 漏3 | 伊莎多拉说鹦鹉多了、还有叫不出名字的新动物，「也许我让它们自己命名」 | text/ch71:435 `“Oliver, there are so many parrots now. There are new animals, too, I don’t have names for them.”`；:444 `“Or maybe I will let them name themselves.”` | `鹦鹉` 零命中（grep B，rc=1）。「世界在愈合」的最具体证据（新物种）与命名权的交接都缺 | 提示 |
| 漏4 | 管风琴管子被偷光，她特意为奥利弗留了一架 Steinway Model B | text/ch71:457 `“the organ is ruined. People stole all the metal pipes. There is a piano for you. I keep it specially.” The piano turns out to be a Steinway Model B` | `Steinway\|斯坦威` 无输出（grep C，rc=1）；第 13 行只有「废墟里有一架音色出乎意料好的钢琴」 | 提示 |
| 漏5 | 「你还会再来一次吗」「当然。会。嗯，大部分吧」 | text/ch71:523 `“Would you do it again?”`，:527 `“Of course. Yes, I would. Well, most of it, anyway.”` | `再来一次` 无输出（grep C，rc=1）。终章里他对自己一生的唯一一次总评缺失 | 提示 |
| 漏6 | 他口袋里留着一包巧克力消化饼干，「一直等着这一天」 | text/ch71:513 `I’ve got plenty of water and a packet of chocolate digestive biscuits I’ve been saving. I’ve been looking forward to this` | `饼干` 零命中（grep B，rc=1） | 提示 |
| 漏7 | 他不出门，「除了黄房子」；越老越少待在现在，想阿尔芭就越常与她（和扎克）在一起 | text/ch71:299 `“I don’t go out, except to the Yellow House, of course. … the more I yearned for Alba the more I found myself with her—and Zach, too. … witness to the vanished world.”` | `黄房子` 零命中（grep B，rc=1）；第 152 行「他躲进过去，成了这个消失世界的见证者」抓住了后半句，前半句的「黄房子」例外没有 | 提示 |

## 二、编（md 有、原文无）

| # | md 句 | 原文 | 判定 |
|---|---|---|---|
| — | 本块未发现无原文支撑的实质断言 | — | 0 |

（第 14 行「阿尔芭从水里来、又从岸上消失」略松：原文她是在**船边**帮忙安顿老人时消失的，text/ch71:501 `We are helping my older self get settled in the boat when Alba says, “Oliver!” and vanishes.`，非「岸上」；属地理解层面的轻微偏差，未单列编，见 4-verdict 提示栏。）

## 三、错（两边都有、不一致）

| # | 项目 | md 侧 | 原文 | 判定 |
|---|---|---|---|---|
| — | 主语 / 施事 / 数字 / 时序 | — | — | 0 |

逐项核过：①「你来了，我准备好了」是老自己说的（text:88），第 11 行归属对；②水线位置「五十米上坡」（text:277 `fifty meters uphill`），第 14 行沿用；③安魂曲「为从未谋面的玛德琳写的」（text:471 `Alba wrote it for Madeline, whom she never met`），块 6 中文理解对；④「露辛达准备好了，我让她走的」是伊莎多拉说的（text:422），第 11/14 行归属对；⑤「他们从不告别」的「他们」＝叙述者（57 岁奥利弗）与阿尔芭（text:501 `We never say goodbye to each other`），块 8 中文理解对；⑥结尾回到 2086 年厨房「几乎没过去时间」（text:535 `Almost no time has passed since I left.`），第 152 行对。

## 四、形态

| 项 | 值 | 说明 |
|---|---|---|
| 块数 | 10 | 与任务表配额 ch71=10 一致；机器 `block_hint` 仅提示高于常见区间 3–9，`block_target [9,15]` 内 |
| 引语 | 10/10 命中 | 无空引号、无改写 |
| 导航 | 5 项齐 | 第 11–15 行 |
| H1 | `71. The Vanished World` | 与 ch66–ch70 同形 |
| 词汇 | 14 条 | filtration 158、unwrinkled 93、vegetation 205、miraculously 400、extracting 331、wardrobe 93、eyebrows 83、guarantee 144、pavement 200、hospital 93、stage 400、adventure 513、beloved 471、anxiety 144，均 `/usr/bin/grep -n -F` 逐字命中 |
| 末章标记 | text:540 `*****` | md 未收，属排版符号，不影响 |
