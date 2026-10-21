# 3-diff.md · 00_情感节点 漏／编／错 三张单子

> 执行者：ZCode-Mac（主会话）。R1/R2 由独立审查子代理完成（`1-suread.json`、`2-machine.txt` 已在盘上，
> 机器层 30/30 全绿）；**R3–R5 由派工人接手**（该代理在 R1/R2 后卡死 3h15m、harness 层失联）。
> 复核判据：① 标题里的章号区间是否与该节点讲的事件真实范围一致；② 叙事概括里的人名、数字、死因、
> 时序是否与原文一致；③ 节点之间是否实质重复；④ 节点里的引语是否逐字、是否真在它标注的章。

| # | 类型 | 断言 | 原文证据 | 处置 |
|---|---|---|---|---|
| 1 | 编 | 节点一「博物馆学者迪吉·康姆-沃森在**自家研究所**的古董地毯上**中毒**」 | ch01 无毒物字样（毒芹结论在 ch13）；ch01 只说这是以祖先命名的研究所（`Horatio Combe’s shrine to his obsessions.`） | 改为「死在**以祖先命名的研究所**的古董地毯上」（毒芹结论属 ch13） |
| 2 | 错 | 节点四「『谁继承博物馆』这一格从头到尾没人填得出名字」 | ch11 `Two million pounds.`；ch11 `It’s just the two of us now.` | 改为「这一格却很快填上了：上周刚估过两百万英镑，可受托人一减再减，最后『就剩我们俩了』」 |
| 3 | 错 | 节点八「**死者的母亲**交出他生前寄出的最后一封信」 | ch39 交信的是**迪吉的母亲**芬内拉：`I opened this yesterday. He sent it while I was away… It was the last thing he wrote to me` | 改为「而**迪吉的母亲**交出儿子生前寄给她的最后一封信」 |
| 4 | 编 | 节点八「**前电视主持人**吉米·琼斯」 | ch31 `Jimmy Jones, forty-eight years old. You may well remember him from mid-two-thousands late-night panel shows.` | 改为「深夜谈话秀主持人吉米·琼斯」 |
| 5 | 越界 | 节点八「**凯厄斯第三次走进这些格局完全相同的房子**，发现每一户的摄像头都只对着自己的院门」 | 「第三次走进房子」是 ch24 的情节；摄像头对院门是 ch34 的（`There’s one at the basement level and the back door as well`） | 改为「而广场上每户的摄像头都只对着自己的院门，后巷是全广场的盲区」（去掉 ch24 的越界叙述） |
| 6 | 编 | 节点九「早餐室里，**一张毕业照**把整件事翻了过来」 | 毕业照是 ch22 贝弗利家客厅那张（`There was a graduation photo of a young woman on the mantlepiece`）；ch42 的揭晓是对话本身 | 改为「早餐桌上，一句『那是梅尔，是她妹妹』把整件事翻了过来」 |
| 7 | 错 | 节点十「**进门第一句是道歉**」 | ch54 第一句是 `‘Yes, please.’`，第二句才是 `‘I’m sorry.’` | 改为「进门的第一句是『好的，谢谢』，紧接着才是那句道歉」 |

**汇总：漏 0 · 编 4 · 错 3 ＝ 阻断型 7 条，已全部改（commit aa5ea4156）。**

**假红（不改 md，附依据）**：
- 节点十「这个故事真正的句号，要等到**六周之后**」——审查范围只有 54 份章节提取件（**分部页不在其中**）；
  回 epub 核：Part-012 = `SIX WEEKS LATER`，其下唯一一章即 Chapter-054（`s072-Part-012.xhtml` → `s073-Chapter-054.xhtml`）
  ⇒ 断言成立，与 ch54 的同根因同裁定。
- 节点三「按对方邮件里给好的时间地点动身」——ch08 `Callie reread the email from Eulalia’s people… just giving her a where and when` ⇒ 属实。
- 节点七「桌上只有两个人，第三个人从未露面」——ch27 `Table for two, please.`、`That was probably why her sister dealt with the business side` ⇒ 属实。

**提示级保留**：节点三「凯厄斯拿她的身体开玩笑（钟表/满月）」——ch06 `Your body runs like clockwork and there’s a full moon tonight` ⇒ 属实，保留；
节点八「死者的母亲交出最后一封信」已在阻断表里改；节点六「避孕药三个月前吃完」按 ch15 原文保留。
