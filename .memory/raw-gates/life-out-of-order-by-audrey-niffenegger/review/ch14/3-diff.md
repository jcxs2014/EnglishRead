# ch14 Oliver Arrives · R3 对账

- 素读：`1-suread.json`（12 条，写定于打开 md 之前；全章 Alba 第一人称）
- 机器层：`2-machine.json`，rc=0，10 块 / 10 引语 / segment_miss=0 / 查无 0 / 空引号 0 / 字数 3054
- md：`ch14 oliver arrives.md`（154 行）

## 一、漏（素读有、md 无）

### L1（提示）那封信的内容整段未进块

```
text/ch14_oliver_arrives.txt:142  “Something like, ‘Dear Yang Qing, You are in a safe house in Chicago. The lady’s name is Alba DeTamble, she is a composer and a violinist. She will not lie to you, so be careful what you ask her. She is a time traveler. You may tell her anything you like.’
text/ch14_oliver_arrives.txt:151  “I’ll be terrified of you. Just feed me breakfast and look benevolent. My English was quite poor then.”
text/ch14_oliver_arrives.txt:126  “I don’t remember it very well,” he said. “I burned it after I’d read it.”
```

md 侧：第 15 行只说「括号里的她却和他讨论一封将要留在他桌上的信」，未给信的任何内容；正文 10 块无一块取这段。`/usr/bin/grep -nE "安全屋|不会对你说谎|间谍" md` → 仅第 13 行「兑现「安全屋」：衣服、钱…」（指房子，不是信），**rc=0 但无信内容**。

判定：信是本章的机制说明（谁安全、她能问什么、他该怕什么），且「She will not lie to you」与全书「隐瞒」母题直接咬合；但 md 已点出括号段的存在与功能，未构成整场戏被抹掉 ⇒ **提示**（建议折进第 15 行叙事手法，一句话即可）。

### L2（提示）「找不到他的婚戒」这一空位未进块

```
text/ch14_oliver_arrives.txt:83  I look around for his wedding ring. It’s nowhere to be seen.
```

md 侧：无。`/usr/bin/grep -nE "婚戒|wedding ring" "ch14 oliver arrives.md"` → 无输出 **rc=1**。

判定：与 ch13 他已戴婚戒正成对照，是伏笔级细节；但非事件 ⇒ **提示**。

### L3（提示）「没有电脑/电话/电视」只留在词汇例句里

```
text/ch14_oliver_arrives.txt:83  It’s conspicuously devoid of computers. No Apple product has ever entered this room. No telephone, no television, nothing digital.
```

md 侧：仅第 128 行 `conspicuously` 的例句；第 15 行清单（书架、唱片、八轨录音机、米妮娃娃、地图）未收这条否定式清单。

判定：这条否定清单是 2044 年世界观的侧写，漏了不影响叙事 ⇒ **提示**。

## 二、编（md 有、原文无）

### N1（提示）md 第 13 行：「坏掉的门廊灯」

```
md:13  …湿透、赤裸、坏掉的门廊灯、只开一条缝的门、三点钟。
text/ch14_oliver_arrives.txt:38  The porch light isn’t on, of course, so I carefully part the blinds and peer into the darkness.
```

原文只说灯没开（且「of course」暗示一向如此），没说坏。

判定：细节性添加，不涉情节 ⇒ **提示**。

### N2（提示）md 第 14 行：「Adam 在柜台后读**体育版**连环画」

```
md:14  Adam 在柜台后读体育版连环画，父亲得了肺炎…
text/ch14_oliver_arrives.txt:428  Adam smiles and settles back on his high stool with the Trib’s comics section.
```

原文是《论坛报》的连环画版（comics section），未提体育版。

判定：属性添加，一字之差 ⇒ **提示**。

## 三、错（两边都有但不一致）

### E1（阻断）谁把这间房攒满——md 三处把施动者从 Oliver 换成了 Alba

原文（正文明写施动者是 Oliver，Alba 只是第一次「用他的眼睛看」）：

```
text/ch14_oliver_arrives.txt:73  Oliver has been stuffing this room with possessions since the 1950s. For the first time I see it as he must have, as an egg, a small contained space full of everything his young self will need or want, all the nutrients this starved boy requires to inhabit his future.
text/ch14_oliver_arrives.txt:68  I open the closet door. “This is yours,” I say. “The clothes. The room. All for you.”
```

md 侧三处：

```
md:11（导航）  …把他带上走廊尽头那间卧室——从 1950 年代起她就往里面攒东西，像一个蛋。
md:13（Tropes）  反转补给的方向——房间从 1950 年代起就由她替他攒，蛋里的养分是他自己。
md:51（原句 4 中文理解）  她从 1950 年代起就往这间房里塞东西。她头一回用他的眼睛看它：像一个蛋…
md:57（原句 4 读者视角）  这句话解释了她凭什么能提前几十年备一间房：她知道他会在什么年纪、以什么状态出现。
```

判定：主语与归属方向反了。原句的主语是 Oliver（成年后的他一次次回到过去、把自己的房间攒起来），Alba 的动作只有「第一次像他那样看这间房」。md 把「攒」记在她账上，直接改变人物关系（她成了供养者），并使第 13 行「反转补给的方向」自相矛盾（既说由她攒，又说养分是他自己）。⇒ **错，阻断**（一处根因、四处外显，一并修）。

### E2（提示）md 第 15 行：「她习惯性瞄的那眼报纸日期」

```
md:15  …以及她习惯性瞄的那眼报纸日期「May 12, 1999」。
text/ch14_oliver_arrives.txt:428  I peek at the date out of habit: May 12, 1999.
```

原文只说「习惯性看一眼日期」，未说是报纸（同段 Adam 在读《论坛报》连环画，读者可推，但原文未写）。

判定：**提示**（可保留，属合理推断；若求稳可改为「她顺手瞄的那眼日期」）。

## 四、R4 逐块对应（10 块）

| 块 | 引语（首句） | 这段中文是不是在讲这句引语 | 三问（主语 / 受事 / 归属） |
|---|---|---|---|
| 1 | `It is raining, a lashing spring rain…` | 是。洗车房比喻、`leaf-choked`、冒号后只留 doorbell 都对着引语讲 | 主语：雨/房子/她（听）；受事：屋顶、檐沟；归属：`in all the years I’ve been coming here` 的「我」= Alba，md 第 27 行「她是常客」正确 |
| 2 | `There’s someone there, an indistinct shape slouched against the doorframe…` | 是。三次判断（看见/推理/承认直觉）解析准确 | 主语：Alba（看、排除）；受事：门外的人；归属：`he’d just come in the back door` 的 he=Oliver，md 未错置 |
| 3 | `“Yang Qing,” he says back in a scared whisper…` | 是。三个动作连成向下的曲线，落到 avert my eyes | 主语：他（报名字、护住下体）、她（开门、移开目光）；受事：他自己；归属：中文名由他说、Oliver 由她叫，md 第 47 行「谁用哪个名字是刻度」正确 |
| 4 | `Oliver has been stuffing this room with possessions since the 1950s…` | **否**——中文理解把主语写成「她」，与引语 `Oliver has been stuffing` 相反 | 主语应为 Oliver；受事：这间房；归属：`his young self` = Oliver 年少时的自己，md 第 55 行「这个饿坏了的男孩」对，但第 51/57 行把施动者换成她 ⇒ E1 |
| 5 | `At this age, Oliver drinks tea, not coffee…` | 是。三个细节各管一头（口味/两副餐具/擦亮的鞋） | 主语：她（泡茶、摆桌）、他（穿）；受事：茶、餐具；归属：`At this age` 指他的年纪，md 第 67 行读对 |
| 6 | `The “Metamorphosis” variations by Philip Glass…` | 是。rippling 接雨、冒号后的否定串、a kind of audition 都落在引语上 | 主语：琴声/他（弹）/她（听）；受事：整栋房子；归属：`he’s playing for me` 的「我」= Alba，md 第 77 行引 `I decided years ago` 正确 |
| 7 | `Oliver has never seen a twentieth-century American supermarket…` | 是。supersaturated 的化学义、三种感官依次失守 | 主语：他（走、念）；受事：货架、商标；归属：`He sounds out` 的 he=Oliver，未错 |
| 8 | `“Please do not worry about money.”…` | 是。两个理由分列、`not only mine` 的否定收尾都讲了 | 主语：她（说）；受事：他、这个地方；归属：`this place is ours` 的 ours=两人，md 第 95 行「不只我的」准确 |
| 9 | `The entry is from last week…` | 是。「示范比解释有用」「为鸟停下割草机」贴着引语 | 主语：她（念）、Oliver（写）；受事：巢、草坪；归属：条目署名 Oliver（`Much love, Oliver.`），md 未错置 |
| 10 | `For the rest of his life, Oliver will remember today…` | 是。will remember 的时态翻面、两个量词并排都讲了 | 主语：Oliver（记得）；受事：今天；归属：`the day he met me` 的 me=Alba，md 未错 |

R4 结论：9 块对应；**第 4 块不对应（主语错）**，见 E1。
