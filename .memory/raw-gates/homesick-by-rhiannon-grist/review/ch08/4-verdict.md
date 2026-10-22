# ch08 4-verdict

- 文件：`ch08 rowan in the hardware shop.md`
- 结论：**阻断 0 / 提示 4**

## 阻断

（无）

## 提示

1. **位置**：导航末句与一句话概括"他临走邀她明天去 The Cut Yard"。
   **问题**：这地方在原文里叫 **Curtyard**，`text/ch08_chapter_8.txt:266` "you should come to the Curtyard tomorrow."；"The Cut Yard" 只是她在 `:269` 没听清时的回问 "“The Cut Yard?”"，他也没有更正。md 把她的误听当成正式地名，读者会以为村子真有个"The Cut Yard"。
   **建议**：改成"他邀她明天去 Curtyard（她听成了 'The Cut Yard'）"。

2. **位置**：原句2 关键词 "alert（提示音）"。
   **问题**：alert 在这里是手机上的"提醒/通知"（`:59` "an alert on your phone"），不是"提示音"；本章的提示音是 `:26` 的 chime 与 `:53` 的 bleeping，两词已分别释义，混用会让学习者把三个词当成一回事。
   **建议**：改为 "alert（（手机）提醒、通知）"。

3. **位置**：Tropes 兑现/反转"热情来自一个趴在地上做平板支撑的中年男人"。
   **问题**：原文没有给 Rowan 任何年龄。`/usr/bin/grep -n -i -E "forty|forties|mid-thirties|middle-aged|older man" text/ch08_chapter_8.txt` → 无输出，`echo $?` = 1；只有 `:50` 的掺灰胡子、"lived in""been through the wars" 这类外貌推断。
   **建议**：改为"一个趴在地上做平板支撑、胡子掺灰的壮实男人"。

4. **位置**：导航（店内一段）。
   **问题**：素读事实 3 的店内质感整段没有落点——`:26` 汽油、木屑、冷天进屋的人身上带进来的户外气味，"cluttered, but clean and warm. All practicality and no style."。这不是可有可无的修辞：后文她"怕被当游客宰"的紧张，正是被这种"干净、暖和、全实用"的空间先卸掉一半的。
   **建议**：在导航"走进一家卖钢锯、防蠓网和引火袋的五金店"后补一句："店里一股汽油与木屑味，杂而不乱、干净暖和，全是实用、没有半点装点——她的紧张先被这股气味卸掉一半。"

## R4 三问

1. **谁做的**：趴到地上做平板支撑的是 **Rowan 自己**（`:53` "reached into his jeans pocket… got onto the floor in a plank position"），提醒是他伴侣设的（`:59` "my other half has a habit of putting reminders in my phone"）；先伸手报名字的是 **Rowan**（`:110` "He reached out a hand. "Rowan.""），她后握（`:119` "I took his hand and shook it."）——md 人物弧线写"到报名字时主动伸手"，方向正确；打断他推荐的是 **她**（`:92` ""Yes," I said, a little too loud."）。三处施事 md 均未错位。
2. **关系/谁欠谁**：`my other half` 后面跟的是 **he**（`:59` "He thinks everything can be solved with an alert on your phone."）——伴侣是男性；md 原句2 的读者视角提示专门点出这一句，**没有**写成"妻子/女友"，这是本章最容易出错的地方，保持原样。Rowan 是本地店主、她是刚搬来的顾客；她住 1b（`:245`），他说这房子"换过几任主人"（`:254` "It’s had a couple of owners"）——房主更替，不是她租自 Rowan，也不是亲属。
3. **数字与死因**："才一个小时"有据（`:5` "barely an hour"）；"1b"有据（`:245`）；房主数只有"a couple of owners"（`:254`），md 写"换过几个房主"未擅自给数字；本章**无金额**（斧头与晾衣绳只说付了钱，` :233` "I paid for the axe and the washing line."，无价目）、**无死亡**。Rowan 的年龄无逐字依据（见提示 3）。

## 已核实为正确（下一轮不要改坏）

- 原句 1–6 引语全部逐字：`:14`（清单 + 招牌）、`:59`（other half / Planks / alert）、`:128`（snort / disgust / put off）、`:227`（smile faded / flickered / customer service）、`:254`（Nothing / spooks / a couple of owners / seems to—）、`:272`（alley / locals hang out / as you’re a local now）。
- 三种声响分段的结构判断与原文一致：门铃 `:26`、手机提示音 `:53`、链锯落地 `:257`。
- `my other half` + `he` 未被误写成异性伴侣；Rowan 先伸手未被写成她先伸手；斧头是**他挑**、她付钱（`:227-233`），md 未写成她自选。
- 章际呼应正确：晾衣架砸挡风玻璃确在 ch02（`text/ch02_chapter_2.txt:182` "It slipped out of my hands and into the windscreen of my car"），"回两张五十镑只换来一声屁"确在 ch05（`text/ch05_chapter_5.txt:185` "Two fifty-pound notes." 之后的段落）。
- 词汇表例句均可逐字检得（fluff-less / hunkered / fleecing / plastered / mimicked / mock-smacked 等）。
