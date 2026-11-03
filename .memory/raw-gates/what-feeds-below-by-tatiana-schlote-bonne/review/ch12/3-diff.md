# ch12 对账（R3）

> R1 素读：`review/ch12/1-suread.json`（facts 8，锚点 8/8 命中 text/，start-end 一致）
> R2 机器层：`review/ch12/2-machine.json`（chapter.sh --json，verdict=ok；块 10 / 引语 10 / segments 11 / segment_miss 0）
> R4 人判：`review/ch12/4-verdict.md`（10/10 块逐块核对）

## 漏（R1 有、md 无）
- 无（正文十块）。R1 8 条（第五层尸体便条、nylon 睡袋与腐尸、死者背包三把刀与滤芯与三张地图、Flint 否认偷窃、决定过夜八小时、Jade 断言那 fiend 是 Petra 父亲、Flint 自己拔耳塞、黄线被夺走）全部由导航或块覆盖。

## 编（md 有、原文无）
- 无。Gimm、nylon 睡袋、water breather 滤芯八小时、Unspoken Truth of the Void 等均可回原文命中。

## 错（两边都有但不一致）
- 错 1【阻断级】块 6 中文理解主语错位：md `ch12 the yellow line.md:80` 写「而且是他爸从他爸手里偷走了那件遗物，把他丢在那里等死。」——两个「他爸」都读成 Flint 的父亲。原文 `text/ch12_chapter_twelve.txt:199`「And his dad stole the relic from yours and left him for dead.」：his dad＝Flint 的爸，yours＝Petra 的爸 ⇒ 应改为「从他爸从**你爸**手里偷走了那件遗物」的完整表达（「是他爸从你爸手里偷走了那件遗物」）。
- 错 2【提示级】导航 `:10` 一句话概括的层级与时序写反：原文开头 Petra 仍在**第三层**的水下隧道（`:29`「There's an underwater passage that leads down to the Fourth Layer.」），Gimm 的尸体在第四层小岩岛（`:59-73`），`:305/:307` 才进入第四层 Blackout Sea（97% 在水下、最深两千英尺）——md 写成「进入第四层黑水海，在岩岛上安葬死者 Gimm」，把入黑水海写在安葬之前。
- 错 3【提示级】同一行「安葬」措辞：原文 `:165`「We'll have to send Gimm off to his grave」＋`:169`「Flint nudges Gimm off the rock. The bag slides into the water… then it sinks into the darkness.」——是**推下岩石沉入水中**，不是入土/安葬。
- 错 4【提示级】同一行「为那只 fiend 的手表争出结论」：原文是 Jade 的猜测（`:197`「I bet that was your dad, Pet.」）＋Petra 的默认点头（`:209`「Slowly, I nod.」），没有「争出结论」这一动作。
- 错 5【提示级】导航 `:13` 人物弧线「她对 Flint 的评价从『也许他真是有真心的人』转成『他会害死我们』」：前半有据（`:167`「maybe . . . Flint is a genuinely caring person」），后半**查无**——`/usr/bin/grep -n -i "kill us|kill you|get us killed" text/ch12_chapter_twelve.txt` 无输出（退出码 1）；原文 `:207` 的实际指控是「Flint's a selfish thief, just like his dad. That's why he stole from my donations.」
- 错 6【提示级】导航 `:14` 叙事手法「与本章安葬 Gimm 一节直接对话」：同错 3 的「安葬」措辞。
- 错 7【提示级】块 4 中文理解 `:56`「我们得送 Gimm 入土」：同错 3。
- 错 8【提示级】块 4「为什么这样写」`:60`「埋葬被处理成一件手续」：同错 3 的措辞。
- 错 9【提示级】一句话总结 `:167`「用一整套正确的规矩换掉 Petra 对 Jade 的沉默忠诚」：语意倒错。原文 `:193`「Why am I still wallowing over my dad when she's my family now?」＋`:199-209` 显示崩塌的是 Petra 对 **Flint** 的信任，不是对 Jade 的忠诚；同一句里的「安葬死者」亦属错 3 的措辞。

## 结论
R3 三单：漏 0、编 0、错 9。漏 0、编 0、错 9（阻断 1：块 6 主语错位；提示 8：安葬措辞×4、层级时序、争出结论、他会害死我们、总结语意倒错）。已列入修复指令。
