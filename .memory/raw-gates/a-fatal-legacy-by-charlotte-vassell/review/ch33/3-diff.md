# 3-diff.md · ch33 漏／编／错 三张单子

> 执行者：ZCode-Mac（主会话接手）。原派审查代理完成 R1/R2 后在 R3 阶段停摆（14:29 落盘后再无文件），
> 其 R1 素读底稿（`1-suread.json`，10 条事件带字符区间）与 R2 机器层（`2-machine.json`）在盘上、可复用；
> R3/R4/R5 由派工人按同一判据完成。

## 一、逐条核过的事实断言（核过 21 条）

| # | md 的断言 | 原文依据 | 结论 |
|---|---|---|---|
| 1 | 直播迟迟不结束，粉丝 David Glossop 报的警 | `text/ch33_33.txt` 开头：Amy 转述 | 属实 |
| 2 | 闯入者穿深色衣服、光线昏暗、说不出是谁、判不出身高 | 同上 `They couldn’t say who they were … couldn’t judge their height` | 属实 |
| 3 | 族裔判断：白人或中东人 | `either white or Middle Eastern` | 属实 |
| 4 | 凯厄斯下令读全部日记并说「二十一卷」 | `All twenty-one of them.` | 属实 |
| 5 | 「文学弯」的三例：迪吉在写书、吉米写了未出版回忆录、本尼迪克写了争议之作后被一条刻薄评论击到自我怀疑 | `Digby was planning on writing a book, Jimmy had penned an unpublished memoir and Benedict had written one controversial banger and then exploded into self-doubt after one scathing review` | 属实 |
| 6 | 艾米抱怨像读 Flashman 小说、连「它是虚构」这点安慰都没有 | `Flashman novel without the comfort of knowing it’s fiction` | 属实 |
| 7 | Willow 誊的是二十二本 | `All twenty-two of the bloody things.` | 属实 |
| 8 | 楼上图书馆只有二十一卷 | `There were only twenty-one in the library upstairs.` | 属实 |
| 9 | 先人因「淫秽」把那卷抽出收藏、锁在迪吉书桌里；祖父叮嘱别读第二十二卷，但 Willow 读了且从这卷开始誊 | `One of Digby’s forebears removed this one specific volume from the collection for being lewd. It was kept under lock and key in Digby’s desk. … He had me start there` | 属实 |
| 10 | 那一卷是疟疾那一年，通灵与群交的胡话，配图她没誊、只拍了两张发给女孩们 | `The malaria year?`；`gibberish about communing with the dead and orgies. There were diagrams. I didn’t transcribe those.` | 属实 |
| 11 | 艾米与 Tiny Simm 把楼翻了个遍、抽屉里任何文件都已列为证物 | `Me and Tiny Simm went through every inch of that building. Any paperwork in Digby’s drawers was taken into evidence.` | 属实 |
| 12 | 班尼迪克家地下室厨房那层的墙上有一处像五芒星的记号、油漆剥落才露出 | `a marking on the wall in his basement kitchen level that looked like a pentagram. A layer of paint had peeled away.` | 属实（md 写「五芒星」，原文是「看起来像五芒星」，属措辞，提示级） |
| 13 | 原文 `He stores books in his.` 是残句、语意不完整 | 原文即如此 | 属实（md 如实标注 ✓） |
| 14 | 两个被害人的工作地点相距步行五分钟内 | `Two victims whose workplaces were within five minutes’ walk of each other.` | 属实 |
| 15 | 入室盗窃正好落在那两户人家；另怀疑迪吉家也被搜过 | `Then the break-ins happening in those two specific houses. We suspect that Digby’s house had also been searched.` | 属实 |
| 16 | 收尾一句让整座广场姓 Beauchamp | `‘Priory Square. It’s Beauchamp land.’` | 属实 |
| 17 | 凯厄斯被调离本案、理由是利益冲突 | `I’ve got to tell the Chief Superintendent. I’ll be taken off the case. It’s a conflict.` | 属实 |
| 18 | 家族持有的是 leasehold 与三分之一的房子 | `The leasehold yes, and a third of the houses still.` | 属实 |
| 19 | 凯厄斯写申请要进研究所地下室、并追了一段让他在意的监控申请 | `quickly put in writing a request to Fenella Combe-Watson to gain access to the basement … chased up a CCTV request` | 属实 |
| 20 | 艾米把凯厄斯的策略记在笔记本上 | `Amy then took out a pen and wrote Caius’s strategy down in a notebook` | 属实 |
| 21 | 导航称誊录者「没把二十二卷全部敲完」、没誊图 | R1 E5 + 原句 5 逐字 | 属实 |

**漏 0 · 编 0 · 错 0**

## 二、提示级（只记不改）

1. **漏（提示）**：Willow 那句「会不会就有个住在广场上的人盯着我的一举一动」（`What if there was someone who lived on the square who was watching my every move?`）未进 md——本章专属判据的「同住广场的跟踪者」这条线，md 只在原句 8 的读者视角提示里以「此人必须住在广场上」旁敲侧击，没有引她的原话。
2. 原句 4「正因为它被藏起来，它才可能被人盯上」——原文未言明这层因果，属评析推断。
3. 导航「被油漆盖住的五芒星」——原文是「看起来像五芒星」的记号（a marking … that looked like a pentagram），措辞更硬了一点。
4. 原句 8 读者视角提示的「半径五分钟的圈子」——原文是「步行五分钟之内」，非半径。
5. 导航「两个被害人相距五分钟步行的工作地点」——原文 `workplaces` 未说明是工作地点以外的意思 ✓ 属实。

## 三、机器层

`bash scripts/chapter.sh "…ch33 the missing journal volume.md" --json` → 退出码 0 / verdict ok；引语 9/9 段逐字命中；`structure.py order` 0 缺陷；严格逐字子串比对 9/9 命中、0 跨段。
