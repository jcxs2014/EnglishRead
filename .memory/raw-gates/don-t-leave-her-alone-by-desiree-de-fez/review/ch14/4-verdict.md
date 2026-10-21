# 第 14 章 R5 判定（人工审查）

**覆盖声明**：本次人工审查只覆盖**第 14 章**（全书 18 章里人判覆盖的收口章——此前 ch00/ch03/ch05/ch06/ch09/ch12/ch13/ch17 已由我本人人判，ch01/ch02/ch04/ch07/ch08/ch10/ch11/ch15/ch16 由审查子代理并行补齐）。R0–R5 全流程已跑完（`1-suread.json` → `2-machine.json` → `3-diff.md` → 本文件）。**其余各章的人判结论见各自目录下的 `4-verdict.md`；只有机器层、尚未补人判的章，不写成「通过」**（`docs/rules/审查表.md:31`）。机器层唯一真值＝`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/text/ch14_chapter_14.txt`（292 行，10,446 字符）；成品＝`notes/books/novels/don-t-leave-her-alone-by-desiree-de-fez/ch14 chapter 14.md`（113 行，7 个引语块）。审查人：DSH-Mac。

---

## 一、四组数（只报这四组）

| 组 | 数 | 依据 |
|---|---|---|
| 逐字 | **7 / 7** | `2-machine.json`：`segments 7`、`segment_miss 0`、`quote_long 0`、`empty_quote 0`；7 个引语块逐字命中原文，起始字符位 666 / 1416 / 3860 / 4716 / 5136 / 7155 / 9747；引语词数 43 / 45 / 35 / 44 / 32 / 37 / 30，全部落在创建卡第 3 条硬线（1–3 句、30–70 词）内。另：`## 本章词汇` 26 条例句全部是原文子串（自写脚本 `/tmp/vocab_all2.py`：`ch14: rows=26 bad=0`）。 |
| 对应 | **7 / 7 块（21 问）** | R4 逐块对应走完 7 个块，每块固定三问（①每个动词的主语是谁 ②受事／宾语是谁 ③归属方向回原文看 by/to/from/of）＝21 问，全部有原文出处；导航 5 条、词汇 26 条、一句话总结 1 条另行逐句对账。 |
| 形态 | **0 偏离 ／ 1 提示** | `2-machine.json` `counts`：`struct_bad 0`、`keyword_bad 0`、`cjk_low 0`、`empty_quote 0`、`quote_long 0`、`template 0`、`hole 0`；`form`：`h1_shape_ok true`（`14. Chapter 14`）、`nav_count 5 ok`、`blocks 7`、`subitems_modal`＝中文理解／关键词／为什么这样写／读者视角提示（与 `profile: novels` 一致）、`baseline: book`、`issues` 四组全空。唯一「异常」＝① 块数 7 偏离本章篇幅建议 3–6（本书中位 7.5、范围 5–8，**在本书范围内**）② 7 处「关键词整句」——关键词子项取的是引语里的整段短语而非精选词，属提示级。 |
| 断言 | **24** | 判定表 24 行：通过 10 ／ **阻断 6** ／ 提示 8 ／ 假红 0 ／ 跳过 1。 |

---

## 二、判定表

| # | 断言 | 证据（章:区间） | 结论 | 档位 |
|---|---|---|---|---|
| 1 | 7 个引语块与原文逐字一致 | `2-machine.json` `quotes[].segments[].ok=true`（7/7）；字符位 666/1416/3860/4716/5136/7155/9747 | 通过 | — |
| 2 | `本章词汇` 26 条例句均为原文子串 | 自写脚本 `/tmp/vocab_all2.py`（正文 text 全文）`ch14: rows=26 bad=0` | 通过 | — |
| 3 | 块 1（`md:19-27`）对应「阿尔芭浑身是血、卡洛斯吻她脸颊后一句话也没说走向车」 | `text/ch14:9`「She was covered head to toe in blood… Carlos walked toward his sister-in-law. With tears in his eyes, he kissed her cheek, and without a word, he rushed to the car.」 | 通过 | — |
| 4 | 块 2（`md:26-31`）对应「胡安一头雾水、手柄才是大事」 | `text/ch14:27`「Juan was baffled. Was that really the most important question right now—whether she’d found the Switch controllers?」；`:27` 末「the nonsensical logic of her mother and sister, who swept everything under the rug.」 | 通过 | — |
| 5 | 块 3（`md:33-38`）对应「卡门躺回草地上、把包挪成枕头」 | `text/ch14:114`「"Are you bringing the blanket or what?" Carmen asked. She shook the bag she’d been resting her head on, readjusting it to make it feel more like a pillow, before she slowly lay back down.」 | 通过 | — |
| 6 | 块 4（`md:40-45`）对应「三人腹部同样的银色疤痕」 | `text/ch14:138`「Carmen and Diana opened their coats and lifted their sweaters. Where there had been a sash of flesh and blood…a delicate scar had now formed. The three had identical scars on their abdomens: closed, silvery scars…」 | 通过 | — |
| 7 | 块 5（`md:47-52`）对应「胡安靠车里孩子的脸撑住自己」 | `text/ch14:141`「Juan walked back toward the car. As he got closer, he felt comforted seeing the children’s faces inside. He held on to that bit of light, trying hard not to break down.」 | 通过 | — |
| 8 | 块 6（`md:54-59`）对应「胡安哭诉那个洞」 | `text/ch14:213`「"She was completely naked from the waist up, covered in blood, with a hole in her belly. A hole. Round and dark inside. I wish I were making it up, but I’m not, I promise I’m not."」 | 通过 | — |
| 9 | 块 7（`md:61-66`）对应「胡安放下两份比萨、一句话也没说」 | `text/ch14:285`「Then, before he returned to the car, he made his way over to the three women and placed two pizzas where they were sitting. He did it without a word.」 | 通过 | — |
| 10 | 块 4 里「两个女儿一左一右把头靠在母亲肩上、好多年没挤在一起」 | `text/ch14:111`「The sisters sat down in the grass, each on one side of their mother.」；`:138`「Both Diana and Alba leaned back into their mother, each daughter resting her head on one of Carmen’s shoulders… It had been years since all three had been so physically glued together.」 | 通过 | — |
| 11 | `md:13`「卡洛斯为了不让孩子看到阿尔芭而默默跑去车里」与原文动机不符 | `text/ch14:9`「He didn’t run, not wanting to scare anyone. He wanted to know how Alba was doing, wanted to ask, but he couldn’t let the children see her like that.」 | 与原文不符 | **阻断** |
| 12 | `md:21`／`:23`／`:24` 把 `rushed to the car` 译成「跑」「奔跑」「沉默的奔跑」 | `text/ch14:9`：引语写 `rushed to the car`，紧接 `He didn’t run, not wanting to scare anyone.`（作者先写 rushed 随即否认 run） | 与原文冲突 | **阻断** |
| 13 | `md:11`「卡门和两个女儿并排躺在草地上」 | `text/ch14:111`「The sisters sat down in the grass」；`:114`「…before she slowly lay back down」（**躺下的只有卡门一人**） | 与原文冲突 | **阻断** |
| 14 | `md:31`「三个女人都在用同一招：不谈伤，只谈毯子和比萨」 | 比萨是 Juan 提的（`text/ch14:240`「Should we order some pizza? Juan asked after a moment.」），三个女人全程没谈比萨 | 施事归属错 | **阻断** |
| 15 | `md:52`「副驾是胡安的位置，他不会开车」 | `text/ch14:141`「Carlos was in the driver's seat… He had never sat in the driver's seat. Juan got in through the passenger door.」（原文只说 Juan 从副驾车门上车）；不会开车的是 **Carlos**（`text/ch10:888`「Since he had no idea how a car worked…」） | 与原文不符 | **阻断** |
| 16 | `md:110`「异口同声地说自己不疼、坚决不去医院」 | `:120`「"We're fine," the three said in unison.」（三人齐声，只这一句）；`:84` 拒绝医院的只有 Carmen；`:126` 说自己完全不疼的只有 Alba | 施事合并 | **阻断** |
| 17 | `md:58`「他在同一段话里先说『穿过肚子』」 | `text/ch14:213` 段首「Alba had a hole right through her stomach.」与段末「a hole in her belly.」**分属不同段落**，是跨段缝合 | 提示 |
| 18 | `md:11`「卡洛斯坐在驾驶座上看孩子」 | `text/ch14:141` Carlos 是 `looking tense`；「看孩子的脸」是 Juan（`:141`「he felt comforted seeing the children’s faces inside」） | 提示 |
| 19 | `md:110`「伤口奇迹般愈合了」 | `text/ch14:219`「well, look, it’s gone now… They healed right away.」（平的陈述，无惊叹、无奇迹） | 措辞过头 | 提示 |
| 20 | `md:65` 把结尾两句并成一句引号式表述 | `text/ch14:288-291`「That Christmas Eve, everyone ate Domino’s.」与「It was a relief.」是分开的两段 | 提示 |
| 21 | `md:14`「从远远看着阿尔芭走来」漏 `torn apart` | `text/ch14:6`「Carlos and Diana saw them coming from a distance. They saw her from afar, torn apart.」 | 漏（措辞） | 提示 |
| 22 | 漏：Juan 九岁在婚宴上抽第一支烟 | `text/ch14:162`「I think I was nine when I had my first cigarette.」；`:168`「I was at a wedding. They let us kids smoke at weddings.」 | 漏（覆盖缺口） | 提示 |
| 23 | 漏：卡门躺着数落「卡洛斯连暖气都调不明白」 | `text/ch14:69`「"And turn the heat on! It’s freezing, and I’m sure Carlos couldn’t figure it out. You know he’s useless with cars."」 | 漏（覆盖缺口） | 提示 |
| 24 | 漏：Juan 发现地点在商场另一个出口、超市招牌底下；孩子当时就在那边玩；时间黑洞 | `text/ch14:213`「I found her passed out on the ground at the other entrance, over by the Mercadona sign. … We didn’t see her, neither did the kids, and they were playing right over there. … I don’t know how long she was there or how we missed her before.」 | 漏（覆盖缺口） | 提示 |

---

## 三、收口复核（修完后的独立结论）

1. **11 条阻断级已全部落到 md**（本轮实际改动行）：`md:11`／`:12`／`:13`／`:14`／`:21`／`:23`／`:24`／`:31`／`:52`／`:58`／`:59`／`:64`／`:65`／`:110`／`:113`。
   复核命令与结果：
   - `/usr/bin/grep -n "跑去\|奔跑\|跑开" "ch14 chapter 14.md"` → exit=1（无输出）✔
   - `/usr/bin/grep -n "并排躺" "ch14 chapter 14.md"` → exit=1 ✔
   - `/usr/bin/grep -n "只谈毯子和比萨" "ch14 chapter 14.md"` → exit=1 ✔
   - `/usr/bin/grep -n "副驾是胡安的位置" "ch14 chapter 14.md"` → exit=1 ✔
   - `/usr/bin/grep -n "奇迹般愈合" "ch14 chapter 14.md"` → exit=1 ✔
   - `python3 /tmp/vocab_all2.py` → `ch14: rows=26 bad=0`，全书 18 章 `TOTAL rows 394 bad 0` ✔
   - `bash scripts/chapter.sh "ch14 chapter 14.md"` → **EXIT=0**，`verdict: ok`，`segment_miss 0` ✔
2. **修完后本章无「原文没有的定性」残留**：全章对伤口只有「愈合／一道精致的疤」这类中性描写，不再出现「奇迹」；对「两份比萨 vs 三个女人」的份数缺口写的是「原文没交代」，**不**写成「作者故意留白」。
3. **本章不含任何超自然解释**：`tentacle` 在本章仅出现一次（`:138` 伤口清单里的 `a gaping hole that housed tentacles`）。md 不暗示成因，符合原文。
4. **称呼链核对**：Carmen 母亲；Alba 小女儿（`:12`「her younger daughter」）；Diana 长女（ch05:549「six years older than Alba」）。md 全用「卡门／阿尔芭／戴安娜」「两个女儿」「妹妹」，方向正确。

---

## 四、已核实为正确（防误修清单——本轮复核后**不得**再改）

1. `md:19` 引语本身逐字，**不要**为了迁就中文理解去改引语；`rushed` 保留原样，中文侧写「快步走去」即可。
2. `md:11`「胡安被她们支去车里拿毯子」——原文 `:90`「Come on, bring us a blanket from the car.」（Carmen 说的）与 `:99` Alba 说后备箱格纹袋里有毯子，成立。
3. `md:13`「三个人腹部同样的银色疤痕、像被描了亮粉」——`:138`「as if someone had waited until they healed properly then traced over them with glitter」逐字对应，成立。
4. `md:52` 括注「他不会开车的证据在第十章：卡洛斯怕误发动引擎，一直没敢开暖气」——`text/ch10:888` 成立，且**保留了原始出处**，是本轮新增的合格写法，不要删。
5. `md:44`「身体重新贴在一起，身体上就长出同一种东西」——`:138`「It had been years since all three had been so physically glued together.」与紧随其后的 identical scars 构成对照，属解读而非事实，措辞已明确标为作者意图层，成立。
6. `md:64`「草地上是三个人，送到的是两份比萨，剩下那一份的去向原文没交代」——`:285` 成立，**写法正确**，不要改成「作者故意只给两份」。
7. `md:113` 一句话总结里「坚决不去医院的只有母亲，说自己完全不疼的只有阿尔芭」——`:84`（Carmen）与 `:126`（Alba）分列，成立。
8. `## 本章词汇` 基础档的 `cigarette` / `wedding` 两条——例句逐字取自 `text/ch14:162`、`:168`，成立。
9. 块数 7（本章 1,845 词）——落在本书实测范围 5–8 内，只是偏离本章篇幅建议 3–6，属提示，**不要**为凑块数拆并引语块。
