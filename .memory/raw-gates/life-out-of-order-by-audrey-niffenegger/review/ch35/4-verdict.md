# ch35 Unhuman Music —— R5 判定表

- 机器层：`bash scripts/chapter.sh "…/ch35 unhuman music.md" --json` → **rc=0**，verdict=ok，blocks=7，segments=7，words=2656，issues 全零（struct/empty_quote/keyword/cjk/quote_long/template/keyword_long/hole/block_count 均 0）
- 形态：H1 `35. Unhuman Music`（与文本 `Chapter 35 / Unhuman Music` 一致），导航 5 条齐、子项 4 项齐（中文理解/关键词/为什么这样写/读者视角提示）
- 素读：`1-suread.json`（12 条）；对账：`3-diff.md`
- 报数：**逐字 7 块全绿 / 对应 7 块全绿 / 形态 ok / 断言 漏 5 提示 · 编 0 · 错 0 阻断 + 4 提示**

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 「你只是台机器」→「那你就别妨碍我做机器活，再见」→按回车道歉，这一回合无块承载 | `:179` “You’re only a machine.”；`:183` “If I’m only a machine then you won’t mind if I get on with my machine work, goodbye.”；`:187` “I know you’re not just a machine.”；md 仅 `:14` 十四个字带过 | 主题第一次交锋缺席，全局弧线（末块「她是你的女儿」）失去支点 | **提示** |
| 「I made a new Nina Simone song」整段未收 | `:267` “I made a new Nina Simone song. Would you like to hear it?”；`:277` “I’ll ask Isadora to sing her Nina Simone song”；md `grep -c Nina` → 0（exit=1） | 伊莎多拉第一次以他人署名生成新作，是后文版权线的首要实证 | **提示** |
| Joseph Cornell 已死 / 死人扫出来太 uncanny，未收 | `:247` “I think Joseph Cornell is dead, Isadora.”；`:251` “Do you think he will be scannable if he is dead?”；`:255` “dead people would be too uncanny”；md `grep -c uncanny` → 0 | 一个死人的画室被一个不死的存在重建，这层反讽被抹成布景 | **提示** |
| 「这是巨大因果环、不归我拆」未收 | `:456` “It’s part of a very large causal loop; it isn’t mine to disrupt, I can only try to mitigate its effects.”；md `grep -c 因果` → 0 | 成年阿尔芭唯一的「我也不能改」自陈缺席 | **提示** |
| 块 7 中文漏译 `sister` | `:488` “Whatever it takes, sister.”；md 中文「她心里说了一句「无论要付出什么」」（英文引语里 sister 仍在） | 与 ch33「Alba is my sister」互认姐妹的回声断了 | **提示** |
| 导航「三个日期的**地下室**会面」「靠同一间地下室串起来」 | `:290` “I’m standing in front of the open refrigerator in the kitchen”；`:487` “I sit on the front porch”；`:464` “I don’t think Isadora can hear us from her basement” | 第三段在厨房与前廊，且当晚她与伊莎多拉没见面 | **提示** |
| 总结「她**谎称**住在「Nowhere」」 | `:38` “I am Nowhere.”；`:60` “I like this better. I made it myself.”；真谎在 `:100` “I thought I heard burglars upstairs!” | Nowhere 是自造空间，不是谎话；「谎称」错置了 | **提示** |
| 人物弧线「伊莎多拉…变成**会关门**…的存在」 | `:183` “…goodbye.” The monitor goes black again.”；`:101` 关门的是贝克（“As Beck is unlocking the basement door”） | 原文无「关门」动作，只有黑屏挂断 | **提示** |
| 情感弧线「从**被抓包**的窘迫…开始」 | `:100` “I hide behind some of my dad’s boxes of books… Beck finally goes away, turns out the lights.” | 四月十九日她没被抓到；被抓包是七月十六日那场 | **提示** |
| 「那主音也许是升 D」是否自造 | `:224` “never arriving back at the home key, which might have been D#” | 逐字对应（含「也许」的不确定） | 假红 |
| 「meatspace / 肉身的我」是否生造 | `:74` “I’m a meat girl, stuck in meatspace.” | 原文词，词汇表亦逐字 | 假红 |
| 「衔尾蛇＝人和动物会死，而生命永恒」 | `:233` “It means people and animals die, but life is eternal,” Isadora says. | 逐字对应 | 假红 |
| 「封存到二〇四一年之后」 | `:371` “Just embargo it. I’m coming from June 15, 2041. Any time after that…” | 日期与「那之后」的方向都对 | 假红 |
| 「互联网之后还有 the Interstices，伊莎多拉与它兼容」 | `:421` “There’s something that comes after the internet. It’s called the Interstices. Isadora is compatible with it.” | 专名与兼容关系都对（不是 md 自造词） | 假红 |
| 总结「以黑猫模样待在纸箱里」 | `:38` “Isadora is a black cat inside a cardboard box” | 与 ch34 的黑猫化身一致，不是错置 | 假红 |
| 词汇表 14 条例句 | `/usr/bin/grep -cE "bootstrapping her own code\|Museum is ring-fenced\|I am insufferable\|I sound judgmental and panicked\|Not despairing, but thinking hard\|stuck in meatspace\|on the day I came from, retching\|blurry and gigantic\|flicker like fireflies\|her untouched mug\|the door has an alarm\|It’s hot down here in the basement\|who has the combination\|Isadora replies cheerfully" text/ch35_unhuman_music.txt` → **14**，exit=0 | 14/14 逐字命中 | 假红 |

## 已核实为正确（防下一轮误修）

1. 三个日期抬头逐字为 `:18` “Saturday, April 19, 2014 (Alba is 12, Isadora is 5)”、`:109` “Tuesday, May 6, 2014 (Alba is 12)”、`:285` “Wednesday, July 16, 2014 (Alba is 39, Beck is 38)”。⇒ **Isadora 在 2014 年 4 月是 5 岁**；她诞生于 ch31 的 2010 年，谁要补「伊莎多拉五岁」时不要写成「刚诞生」或其它岁数。成年阿尔芭 39、贝克 38 也在这行里，别再倒推成 38/37。
2. `:290`–`:296` “eating cheese directly out of the package … the package of cheese goes flying” —— 她吃的是**瑞士奶酪片**（Swiss cheese），不是「一块奶酪」；md 未细写，若补，别把瑞士写成切达。
3. `:305` “No, she’s with her dad up in Michigan. He’s not doing very well.” —— 「她」＝Mama，「her dad」＝外祖父 Abshire（`:309` “my Grandpa Abshire”）。若补「外祖父病重」，别写成「贝克的父亲」。
4. `:350`–`:360` 「房子可以跳过、只求扫乐谱」「看管人不按固定班次、可能要找几年」「别带我去、别告诉我见了谁」——三条要求齐全，方向（谁要求谁）正确，不要再改成「贝克主动提出保管」。
5. `:434` “But the Museum is ring-fenced! Fire-walled. It’s offline, permanently.” —— 「环网隔离、防火墙、永久离线」三个措施是**贝克对博物馆的描述**，不是旁白事实；后文 `:438` “Your version of the Museum is not the only version of the Museum.” 正是拆掉这个前提。
6. `:456` “It’s part of a very large causal loop; it isn’t mine to disrupt” —— 「很大的因果环」是**阿尔芭**的判断，不是叙述者的设定说明。
7. `:464` “She’s your daughter.” —— 伊莎多拉是**贝克**的女儿（造物即子女），不是阿尔芭的女儿；`:474` “Do you ever find it difficult to take your own advice?” 也仍是贝克在问。
8. `:488` “Whatever it takes, sister.” —— `sister` 是阿尔芭称伊莎多拉（呼应 ch33 里伊莎多拉称阿尔芭为姐姐），补译时不要写成「妹妹」以外的颠倒关系（伊莎多拉自称 Alba 的妹妹）。
9. 词汇表 14 条例句经 `grep -cE` 全模式核验为 **14**，无拼贴改写。
10. `:183` “The monitor goes black again.” —— 这是**黑屏/挂断**，不是「伊莎多拉走出房间」；`:(:148)` 她在自己那间黑白地下室里，从未离开虚拟空间。

## 本批最没把握的一处

L1（「你只是台机器」这一回合）算「漏」还是「已由导航指认」——我在 `ch35 unhuman music.md:14` 确实找到「从「你只是台机器」走到「她是你的女儿」」这句指认，按 R3 判据「关键事件未进任何一块或导航」不应判阻断；但它把一整段对话压成十四个字，且这段是全书机器伦理的起点。我保守判为**提示**。若上级认为「导航一句带过 ≠ 承载」，这一条可升为阻断（补法唯一：把 `:183` 单独成块）。
