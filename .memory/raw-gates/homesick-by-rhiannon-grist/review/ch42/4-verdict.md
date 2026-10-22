# ch42 4-verdict

- 文件：`ch42 neither of you are rowan.md`
- 结论：**1 阻断 / 2 提示**

## 阻断

### 阻断 1｜原句4 读者视角提示（第 62 行）："第一章那扇'打碎的车窗'"章号错标
- 位置：`ch42 neither of you are rowan.md:62`「回头想第一章那扇'打碎的车窗'。玻璃在这个故事里从来不是意外。」
- 原文证据：打碎车挡风玻璃的是**第 2 章**——`text/ch02_chapter_2.txt:182`「It slipped out of my hands and into the windscreen of my car, instantly spiderwebbing the whole thing with cracks and shards.」+ `:188`「I stared at the broken windscreen with dismay.」（晾衣架砸穿挡风玻璃）；第 1 章通查无此事：`/usr/bin/grep -n -i "windscreen" text/ch01_chapter_1.txt` → 无输出、`rc=1`。
- 为什么是阻断：这是跨章指认，读者会照着回查第 1 章而查不到；章号错标属判级里的"错"。（另注：ch40 的回忆串 `text/ch40_chapter_40.txt:323`「The clotheshorse bouncing off the windscreen.」也指同一件事，可交叉印证发生在 ch02。）
- 建议改后中文：「回头想第二章那扇被晾衣架砸碎的挡风玻璃。玻璃在这个故事里从来不是意外。」

## 提示

1. **第 2 条事实无落点｜漏掉"全是我的错"（提示）**
   证据：`text/ch42_chapter_42.txt:14`「This was all my fault. I had to get him out. How in the hell was I going to get him out?」——她的第一反应是自责，而不是自保；这与她拒绝伸手并不矛盾（她仍在试图"把他弄出去"）。建议在人物弧线补半句：「她一边认定'全是我的错'，一边把手放回斧柄——她要救他，但不能用交出武器的办法。」

2. **一句话总结（第 112 行）｜"把她撞下楼梯"施事偏移（提示）**
   证据：`text/ch42_chapter_42.txt:77`「I forgot the use of the axe in terror and threw myself away from the imposter. I slipped on the top step, fumbled on my own feet and tumbled down the stairs」——它只是**扑过来**，没有碰到她；她是自己扭身躲、在最高一级踩滑、绊到自己的脚才滚下去。md 写成"把她撞下楼梯"，把"她自己失足"改成了"被它撞落"。
   建议改为：「在尖叫中扑过来，她吓得忘了斧头、扭身就躲，在最高一级台阶上踩滑，一路滚下楼梯。」

（附一条分析越界，可与上条一并处理：导航·情感弧线（第 14 行）说"这个选择救了她"，但本章结尾她正滚进"那个声音"等候的黑暗，救援并未发生；建议改为"这个选择没让她被那张脸牵走"。）

## R4 三问

1. **谁做的**：① 解释来意、伸手、被拒后愤怒、最后从眼眶里倒出碎玻璃并扑上来的，是**浴室里那个假 Rowan**（`:11,29,59,74-77`）；② 在楼下用 Rowan 的声音喊她"你没事吧""我知道你在里面"的，是**另一个假 Rowan**（`:17,125`，承 ch41）；③ 拒绝伸手、把两只手放回斧柄、说出"你们两个都不是 Rowan"的是 Tamsin 自己（`:41,71`）；④ 她滚下楼梯是**自己失足**，不是被推（`:77`）；⑤ 真正的 Rowan 全章**没有出场**（`:71`「Rowan’s not here.」）。
2. **什么关系 / 谁欠谁**：两个"Rowan"都不是 Rowan——本章只确认"两个都是假的"，**没有说它们是不是同一批、谁先来**（那是 ch43–44 的事，本章不要提前判定）；Tamsin 对 Rowan 欠的是愧疚（"我把他拖进来了"），但这份愧疚被本章用来做诱饵：正因为它像 Rowan，她才差点伸手；Fergus 的换子故事是她的判据（`:38`）。
3. **数字与死因**：① 数字只有"两个"（楼下一个、浴室一个；换子故事里的"一个妈妈/一个妈妈"）；② 无年龄、无金额、无日期；③ **本章无人死亡**，也没有人受伤见血——碎玻璃是从"它"眼眶里出来的，不是谁被玻璃割伤；④ 她滚下楼梯后是否受伤，本章未写（留给 ch43）。

## 已核实为正确（下一轮不要改坏）

① 原句 1–5 逐字，且都能在本章同一/相邻自然段内对上；② "她知道那声音像自己"是假 Rowan 自己说的（`:11`「Why does it sound like me?」），不是 Tamsin 的判断，md 未写反；③ 拒绝伸手的**直接触发**是"她会猎你"＋Fergus 的换子故事（`:35-38`），md 归因正确；④ "你不是 Rowan"之后还有一句更狠的"两个都不是"（`:71`），md 的一句話总结保留了这一层；⑤ 眼睛的"抽搐"实为"填充"（`:74`「it wasn’t twitching but filling, like a coin purse」），md 第 52 行的"先给错误解释再拆掉"判断正确；⑥ 结尾她是**滚下**楼梯、落进有声音等候的黑暗（`:77`），不是"跑下楼"、不是"被拖下去"。
