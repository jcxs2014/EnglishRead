# T2-断言全扫 · chunk1（① 相对章号 33 行 + ② 前半 00_三篇 / ch01–ch33）

核对口径：每条都先用 awk/sed 取 md 当前整行（chunk1 候选行截断到约 200 字符），再在 `text/` 对应章 grep 支撑原文。共 11 条缺陷（阻断 2 · 提示 9）。

**00_情感节点.md:52**｜原断言：节点五（ch15-17）里「听见 Mender 说「当一个人是可以的」。然后她把这段话拿去说给 Four 听」｜应改为：这句属 ch22 盛宴（不在 ch15-17 节点内）；且 ch17 没有任何「把这段话讲给 Four 听」的段落，应删去该转述关系｜原文依据："“It’s okay to be a person, to want things, to think whatever you like in your private thoughts.” … “It’s okay to be free.”"（text/ch22_chap22.txt:555）；text/ch17_chap17.txt 全章 grep person/free/allowed 仅 473/478 行两处，与此句无关｜类型：阻断

**00_情感节点.md:52**｜原断言：「十三岁的 Mae」｜应改为：「Mae（Mender 的妹妹）」——原文只以 little girl / little sister 指称，未给年龄｜原文依据："Across from him is a little girl with a book propped up in front of her."（text/ch15_chap15.txt:353）；"“I’m Mae. I’m his little sister.”"（text/ch15_chap15.txt:378）；`thirteen` 在全书 62 个 text 文件中 0 命中｜类型：提示

**00_金句精选.md:19**｜原断言：「她因此被罚沉默一整天」｜应改为：「被罚沉默到第二天早上」（Penalty of Silence until morning）｜原文依据："“Penalty of Silence until morning.”"（text/ch02_chap2.txt:270；同章 357 行复述同句）｜类型：提示

**ch01 the mirror and the scissors.md:57**｜原断言：「作者偏不写结果——剪成什么样，要等下一章」｜应改为：原文整章止于落剪，下一章也不写发型结果（第 2 章开头是做饭、Marcus 赴宴），「要等下一章」不成立｜原文依据："I close the scissors over the first lock of hair, and cut."（text/ch01_chap1.txt:65）；text/ch02_chap2.txt 全章 hair/haircut/trim/mirror 仅 97、331、361 三处 hair，均与剪发结果无关｜类型：提示

**ch04 divergent.md:65**｜原断言：「讲完定义，Tori 没有接着解释「所以会怎么样」，这个空白是有意的」｜应改为：她刚说到 "And it's—" 就被 Tris 抢断，随后仍继续解释了三种倾向与登记口径；「没有接着解释」不成立｜原文依据："“It’s what we call it when someone’s mind is especially resistant to the faction computers. And it’s—”"（text/ch04_chap4.txt:206）→ 210 行 "“So what am I supposed to do?” The question bursts out of me." → 216 行 Tori 继续 "Solving the maze that quickly was very Erudite…" → 220 行 "I logged your result as ‘Abnegation’"｜类型：提示

**ch08 the memory vault and the shared meal.md:37**｜原断言：「「for some of you」给「最后一次」留了例外……这句例外没有解释缘由，只说明有人会被再叫进来一次」｜应改为：缘由就在同段——除被召来做 offering 的人以外一律禁止再进，各界都有人被召、有人不止一次、有人一次也没有；「没有解释缘由」不成立｜原文依据："Accessing the Memory Vault after this point is forbidden to all except those summoned to make an offering. People of all factions are called upon to make offerings, some more than once, some not at all."（text/ch08_chap8.txt:96）｜类型：提示

**ch20 the tunnel and the name prior.md:11**｜原断言：「接上一章末尾那句「告诉她我会考虑」」｜应改为：「接 ch17 末尾那句 "Tell her I'll think about it"」——该句在 ch17 末段，ch19 末尾是 Tris 提出去叫 Evelyn、Four 说那会有帮助｜原文依据："“Tell her I’ll think about it,” he says to me, without looking back."（text/ch17_chap17.txt 末段）；"“Do you want me to go get Evelyn?” she asks … “Yeah,” I reply. “That would be helpful.”"（text/ch19_chap19.txt:394-398）｜类型：提示

**ch20 the tunnel and the name prior.md:12**｜原断言：「反转「说客」——上一章他嫌她是说客」｜应改为：「反转「说客」——ch17 他嫌她是说客，这一章他把这层嫌弃升级成「安排」」｜原文依据：ch19 全文无说客/mouthpiece 相关句（grep sent/mouthpiece/spokes 仅命中 233 行 "Stop."）；对峙在 "“You really don’t know why she sent you?” Four asks"（text/ch17_chap17.txt:478）｜类型：提示

**ch20 the tunnel and the name prior.md:37**｜原断言：「这句话和上一章 Weaver 说的「犯罪天才组成的第六派系」是同一件事的两面」｜应改为：「这句话和 ch16 Jove 说的「犯罪天才组成的第六派系」是同一件事的两面」——说话人是 Jove，不是 Weaver；且不在 ch19｜原文依据："Jove sneers at her. “Well, which is it? Are we defectives who can’t function in a society, or are we a sixth faction of criminal masterminds?”"（text/ch16_chap16.txt:640）；同章 Weaver 说的是 "radical friends"（text/ch16_chap16.txt:661）；ch19 全文无 "sixth faction"｜类型：阻断

**ch25 the hearing errand and the train panel.md:30**｜原断言：「上一章 Weaver 限他们两天搬空，这一章一天就搬完了」｜应改为：「ch23 Weaver 限他们两天搬空」——ch24 是 Caleb 的无派系者迷宫章（POV=Caleb），全章无 Weaver｜原文依据："I’ll be sending someone back here in two days to make sure you’re gone."（text/ch23_chap23.txt:230）；同章 298 行 Jove 说 "We’re moving tomorrow"｜类型：提示

**ch25 the hearing errand and the train panel.md:44**｜原断言：「上一章这双手还伸向过哨兵腿上的枪」｜应改为：「ch23 这双手还伸向过哨兵腿上的枪」——该动作在 ch23，不在 ch24｜原文依据："the gun in its holster on a Dauntless guard’s thigh. The Mender spots it at the same time I do … The Mender reaches for the gun with his spare hand"（text/ch23_chap23.txt:130）｜类型：提示
