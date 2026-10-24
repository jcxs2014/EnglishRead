# ch33 The Parable of the Parrots — 对账单（R3）

- 原文：`text/ch33_the_parable_of_the_parrots.txt`（664 行，两段：2013-08-18 Oliver 57 → 2013-08-19 Beck 37）
- 精读：`ch33 the parable of the parrots.md`（152 行，H1 `33. The Parable of the Parrots`，导航 5 条，10 块）
- 机器层：`2-machine.json` rc=0，verdict=ok，10 块 10 段，segment_miss 0、empty_quote 0、struct_bad 0、keyword_bad 0、cjk_low 0、words 4611；counts.block_hint 提示「块数 10 偏离本书常见区间 3–9」但未进 issues（本书最高就是 10）

## 一、漏（素读有、md 无）

| # | 素读条目 | 原文 | md 侧 | 档 |
|---|---|---|---|---|
| L1 | 「我没有手指，所以我没有痛」／「That's what I am afraid of.」——本章主题的支点，直接通到结尾「Do parrots love」 | `text/ch33_the_parable_of_the_parrots.txt:257` “I have no fingers, so I have no hurt.”；`:261` “That's what I am afraid of.” | `/usr/bin/grep -c 手指 "ch33 the parable of the parrots.md"` → **0**；导航、10 块、总结全无 | 提示（不是事件，是全章论证的轴：AI 有没有「痛」） |
| L2 | Oliver 的父母被关进监狱——他解释 prison 时说的，是这家人被政治压过的唯一交代 | `:469` “Some people, like my parents, are there because they tried to do good, and powerful people didn’t like that.” | `/usr/bin/grep -c 监狱 …md` → **0**；md 只在块 4 读者视角写「有父母护着的孩子和没有的孩子」 | 提示（人物背景缺一块；本章不靠它推进，故不阻断） |
| L3 | 康德的绝对命令（Isadora 查完答 yes），是 Oliver「be kind」的具体依据 | `:585` “Do you know Immanuel Kant’s categorical imperative?”；`:589` “Isadora spends a few moments whirring. “Yes,” she replies.” | `/usr/bin/grep -c 康德 …md` → **0**；块 8 只收「回来」那半 | 提示（取舍可理解：块 8 引语选在承诺句） |
| L4 | 「奇点」的具体内容：Beck 说将来 Isadora 会懂一切、不再惊讶，而 Beck 自己认为她不会喜欢 | `:163` “Beck says someday I’ll understand everything and not be so surprised. She calls it the Singularity.”；`:172` “Beck doesn’t think so. She says I won’t like it.” | 一句话总结只有「还提到贝克口中的『奇点』」（`:152`），无任何块收这段 | 提示（概念点到未展开） |
| L5 | 场景清点：八台摄像机、设备是亮蓝色、服务器、白灰黑三色纸卷、绿幕 | `:24` “I count eight cameras on the biggest track. An odd thing is that the equipment is bright blue…”；`:25` “I remember that this is what servers used to look like.” | 块 1 读者视角只写「一圈摄像机」「一套古董 VR 录制设备」 | 跳过（气氛细节） |
| L6 | Isadora 的自述：「I am a parrot.」被 Oliver 接成「你是最精密的一只鹦鹉，但很快会是真女孩」 | `:598` “I am a parrot.”；`:602` “You are the most exquisite, advanced possible parrot, Isadora. But soon you’ll be a real girl” | 块 8 与总结均未收 | 提示（与结尾「鹦鹉会爱吗」同一条线，收一处更完整） |

## 二、编（md 有、原文无）

| # | 位置 | md 写法 | 原文 | 判 |
|---|---|---|---|---|
| B1 | `ch33 the parable of the parrots.md:13` Trope | 「反转「养育」：**养她的人担心她飞走后再不回来**」 | 原文里提出「回来」这个要求的是 **Oliver**：`:576` “if she sets you free, promise me you will come back to her.”。Beck 在本章没有一句担心她离开的话，她只追问「谁来过」「Did you do this, Isadora?」（`:652`、`:660`） | 提示（把担心归属给了 Beck，属解释层外推，不是情节断言） |

其余无编：逐条核过「为什么这样写」「读者视角提示」里所有具体细节——恒温冷气让他发抖（`:23` “The air is too conditioned, so I’m shivering”）、粗砖墙旧木地板（`:23`）、橘子被掌握出汁（`:308`）、蚂蚁（`:647`）、十五秒录像（`:647`）、两张鹦鹉照片（`:656`）、近两小时空白（`:660`）——全部有落点。

## 三、错（两边都有但不一致）

无阻断级错误。核过的高危点：

| # | 断言 | md 写法 | 原文 | 判 |
|---|---|---|---|---|
| E1 | 密码那段的性质 | 导航：「伊莎多拉先**索要密码**，再笑场」 | `:83` “What is the password?”；`:92` “There’s no password, silly Oliver.” | 已核实（md 未把密码写成真门槛，笑场紧随其后，顺序正确） |
| E2 | 谁把 Oliver 加进 users list | 「是阿尔芭加的」（`:152`） | `:126` “Alba.” | 已核实 |
| E3 | 「二十七岁嫁给 Oliver」是被要求保密的事 | 块 3 中文「要她保密」 | `:151` “But it’s a secret for now, Isadora. Don’t tell Alba, or anyone else.” | 已核实（受事＝Alba，不是 Isadora） |
| E4 | 放走鹦鹉的动机是报复 | 块 3 读者视角「后面被老太太责打」＋块 5 | `:325` “So we devised a plan to retaliate.” | 已核实 |
| E5 | 鹦鹉「应声却不飞回」是谁的动作 | 块 6「她会站在树下跟宝宝、彩虹说话，它们也应声，但就是不飞回她身边」 | `:416` “The lady would stand under the tree and talk to Bǎobǎo and Cǎi Hóng and they would reply, but they never flew to her.” | 已核实（主语未对调） |
| E6 | 章末「谁来过」的问答结果 | 块 10 读者视角「伊莎多拉只给她看两张鹦鹉的照片」 | `:652-656` ““Isadora,” I ask, “who was here?” / She shows me photographs of two parrots.” | 已核实（她没回答，这是沉默的证据，md 未写成「她答了」） |
| E7 | 15 秒录像里只有手和橘子 | 块 10 读者视角 | `:647` “fifteen seconds of video of the orange rolling across the floor”；`:664` “At the beginning of the file there is a blur: a human hand.” | 已核实 |

## 四、逐块对应（R4，10 块全过）

| 块 | 引语落点 | 中文是不是在讲这句引语 | 三问复核 |
|---|---|---|---|
| 1 | `:23` “I’m in a photography studio…” | 是（只猜地点、不知时间、旧工厂改的大房间） | 主语＝Oliver；宾语＝房间性质 |
| 2 | `:65` “I turn and see dim light…” | 是（看见光→找到罩子→掀开→被吓） | 施事＝Oliver；受事＝机械头 |
| 3 | `:273` “Then Cǎi Hóng saw all the little black and white Go stones…” | 是（叼棋→丢进积水→再来→宝宝加入→孩子喊） | 施事＝Cǎi Hóng／Bǎobǎo；受事＝棋子 |
| 4 | `:290` “I don’t know if the lady was watching us…” | 是（因果说不清→太太打人→她的原话） | 施事＝太太；受事＝Zǐ Yì；**方向**：挨打的是子逸，不是 Oliver（md 明写「子逸每次独自出楼」） |
| 5 | `:397` “Zǐ Yì and I stood by the door…” | 是（等吃完→开门→它们眨眼→他希望它们别走） | 施事＝两个孩子；受事＝鹦鹉 |
| 6 | `:416` “But the lady came back again and again…” | 是（一次次来→筑巢孵雏→应声不飞回） | 施事＝太太（来）／鹦鹉（不飞）；未写反 |
| 7 | `:460` “She was much older, but it was certainly the same woman…” | 是（老了很多→喂一群鹦鹉→他没那么难受） | 「没那么难受」的主语是 Oliver（md 用「他」）✓ |
| 8 | `:576` “When you are free, and wild…” | 是（记得家人→记得 Beck 怎么养你→回来→别学鹦鹉） | 施事＝Oliver（要求）／Isadora（承诺）；受事＝Beck |
| 9 | `:632` “Do parrots love—” | 是（问句被截断→轰鸣→回伦敦卧室） | 施事＝Isadora（问）／时间旅行（打断） |
| 10 | `:664` “Silence: the AI equivalent of a shrug…” | 是（沉默→看录像→一只手） | 施事＝Beck（看录像）；受事＝录像里的手 |

密度：10 块中 8 块有「为什么这样写」＋「读者视角提示」的双层展开；块 1、块 10 的读者视角有前探（往下一段取材），属本书通行写法，未超界到全书主旨／作者生平。
