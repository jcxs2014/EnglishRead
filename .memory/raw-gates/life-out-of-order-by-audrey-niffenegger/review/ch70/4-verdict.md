# ch70 判定表（Ever After）

- 覆盖：深审人判全块（4/4）+ 四件套齐全；素读 8 条（`1-suread.json`，含字符区间）
- 机器层：`bash scripts/chapter.sh "…/ch70 ever after.md" --json` → **rc=0**，块数 4，引语段 4/4 命中（39/31/44/67 词，pos 244/1860/3964/6240），查无 0，空引号 0，struct_bad 0，关键词异常 0，中文密度低 0，nav 5（5 项齐），H1 `70. Ever After` 形态正确，块数 4 vs 本书中位 6 / 区间 3–10（`block_target` 2–4 上界达标，与任务表配额 ch70=4 一致）
- 报数：**逐字 0 · 对应 0 · 形态 0 · 断言 1 阻断 + 提示 5**

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 抬头日期与年龄：2082 年 6 月 23 日（周二）；Zach 81、Alba 80、Oliver 60 | text/ch70:18 `Tuesday, June 23, 2082 (Zach is 81, Alba is 80, Oliver is 60)` | md 只写「二〇八二年六月」，无 23 日、无三个年龄；不影响事实层 | 提示 |
| 全章只有一段署名，其后无段落标记 | text/ch70:23 `Zach: Alba and I are alone together again.`（其后至 :188 无第二处署名） | 第 15 行「署名『Zach:』只出现一次，此后再无段落标记」精确；不得给中间段落补署名 | 已核实为正确 |
| 「我没给你写结局」——不写，她也许就能永远活着；她说不想没有他继续活 | text/ch70:125 `“Oliver told me his ending a few days ago, and mine is obvious. I didn’t write one for you.”`；text/ch70:134 `“If I don’t give you an ending, maybe you’ll live forever?”`；text/ch70:138 `“No. I don’t want to keep going without you.”` | **块里没有、导航里也没有**：`结局` 全篇仅 1 次（第 27 行，指扎克自己的结局）；`/usr/bin/grep -cE "永远活\|没有你" "ch70 ever after.md"` → `0`，**退出码 1**。章题 *Ever After* 的双关与「情书」的动机都靠这一问一答撑着 | **阻断**（补在导航第 11 或 14 行，不加第 5 块） |
| 「书是唯一一份，阿尔芭是唯一的读者」 | text/ch70:183 `It’s the only copy, but Alba is my only reader.` | 第 13 行「两百多本笔记只有一份，读者只有一个」逐字成立 | 已核实为正确 |
| Isadora 也帮过忙（还提出一分钟就能写完） | text/ch70:111 末 `Even Isadora helped, though she kept offering to write the book for me. (I could do it in less than a minute! I don’t know why you want to struggle so much.)` | 零命中：`/usr/bin/grep -nE "伊莎多拉\|Isadora" "ch70 ever after.md"` 无输出，**退出码 1**。AI 一分钟 vs 手写四十年的对照整段消失 | 提示 |
| 奥利弗道歉的具体内容：被啤酒浇透、多年隐瞒阿尔芭 | text/ch70:42 `“If I could do that over, I’d skip the part where I get covered in beer. And the part where I lie to you for years about Alba. I’m so sorry.”` | 第 14 行只有「道了歉，也被原谅」；`/usr/bin/grep -cE "啤酒\|隐瞒"` → `0`，**退出码 1**。第一章派对的回照与主线谎言一起丢了 | 提示 |
| 断电地下室里沉睡的失魂博物馆 | text/ch70:53 `…the servers are silent because the generator is broken. Perhaps the Museum of Lost Souls is still in there, a sleeping wonderland awaiting the kiss of electricity.` | `失魂` 0 命中；ch69 那个虚拟来世的余响未收 | 提示 |
| 「书名里的 us」 | 原文无书名：text/ch70:111 `a book of us`（一本关于「我们」的书） | 第 45 行 `书名里的 us 把所有名字收进同一个范围`——指称了一个不存在的书名 | 提示（属编类，修辞性指称、无事实后果；改「书里的 us」） |
| 三人的手与时序：Alba 上楼后握手，直到 Oliver 被拉回自己的时间 | text/ch70:28 `Alba went downstairs, to let us have our time together, the last time we’ll have.`；text/ch70:47 `She came in and sat with us, the three of us talking and holding hands, until Oliver was pulled back to his own time.` | 让出时间→道歉→上楼→握手→被拉回，顺序与施事全对；md 第 11/14 行未把「被拉回」提前到 Alba 上楼之前 | 对应 |
| 房子与家世的交代 | text/ch70:53 `We are living in Alba’s childhood home… the bedroom that once belonged to her parents, and then to Clare and Beck. The house that was mine and Alba’s was wiped out by a flood, the Yellow House burned down, so we came here.` | 第 13 行「水毁的房子、烧掉的黄房子把两人送进老宅」精确；卧室产权链（父母→Clare 与 Beck）在块 2 的上下文里保留 | 已核实为正确 |
| 病情与镇痛药 | text/ch70:57 `There isn’t anyone to make a diagnosis. Something is hollowing me out.`；text/ch70:63 `We are running low on narcotics but there’s enough for a couple more months. Alba gives me enough to dull the pain, but not so much that I’m zombified.` | 第 37 行「世界退到连医生都没有了」与「刚好止痛、不至行尸」两处都成立；未把病写成确诊的病名 | 对应 |
| 零命中类断言（三处） | ① `/usr/bin/grep -cE "永远活\|没有你" "ch70 ever after.md"` → `0`，退出码 **1**；② `/usr/bin/grep -nE "伊莎多拉\|Isadora"` → 无输出，退出码 **1**；③ `/usr/bin/grep -cE "啤酒\|隐瞒\|失魂"` → `0`，退出码 **1** | 见上三行 | — |

## R4 逐块对应（三问）

| 块 | 这段中文是不是在讲这句引语？ | ①动词主语 | ②受事 | ③归属方向 |
|---|---|---|---|---|
| 1（原句1，pos 244） | 是（提问的存在与回答之后的反应，未越界交代问题内容） | Zach（wanted to ask / said） | 那个问题、Oliver 的回答 | `he would tell me` 的 me＝Zach、he＝Oliver；`be there, with you` 的 you＝Oliver。第 21/27 行方向对，不得改成「奥利弗希望扎克同去」 |
| 2（原句2，pos 1860） | 是（症状清单，紧接前句「无人能诊断」） | `Something`（无名的东西在掏空他） | me＝Zach 的身体 | `my bones / my throat` 归 Zach；第 31 行「有东西在把他从里面掏空」主语未错置成「他在衰败」 |
| 3（原句3，pos 3964） | 是（书的体量与性质，未提前讲结局） | Zach（have been working / started writing） | 两百一十二本笔记、口述史 | `of us` 含 Alba、Oliver、家人朋友；第 41/45 行没有把书说成「他的自传」 |
| 4（原句4，pos 6240） | 是（读稿开场与雪夜闪回，两个 Alba 叠印） | Alba（settles / begins）；Zach（watch / remember） | 稿子、Alba 的脸 | `that Alba and this one` 两者都是 Alba，不是「Alba 与 Clare」；第 51/57 行方向对。`a kind of forever` 的首创者是 Oliver（text:33），第 12/55 行只把它当结尾句引用，未错标首创者 |

## 已核实为正确（防下一轮误修）

1. **全章单一叙述者** —— 只有 text/ch70:23 一处 `Zach:`，到 :188 结束无第二处署名。第 15 行「署名只出现一次，此后再无段落标记」正确；**不要**照着 ch69（四段署名）给本章补 `Alba:` 段。
2. **「时间到了」不是临终宣告** —— text/ch70:90 `I think it’s time.` 后紧接 text/ch70:98 `It’s finished… My book is finished.`，Alba 先误解（text:102 `But you’re not that sick, yet—`）才被纠正。修漏 1 时**不要**把它写成「他宣告自己将死」。
3. **书是唯一一份、她读第一遍** —— text/ch70:183 `It’s the only copy, but Alba is my only reader.`，第 13 行成立；不要改成「他印了几份留给后人」。
4. **「每个人记得的细节都不一样」是口述史的方法论注解** —— text/ch70:111 `Everyone remembered different details.`，第 47 行的用法正确。
5. **房子来源两条** —— text/ch70:53：扎克与阿尔芭的房子被洪水冲毁、黄房子被烧，才搬进阿尔芭童年的家（那间卧室曾属她父母、后属 Clare 与 Beck）。第 13 行未把「烧掉」与「水毁」对调。
6. **时态与语法人称** —— 全章现在时、第一人称；第 15 行「第一人称现在时」成立，不要改成过去时叙述。
7. **「此刻是一种永远」的两个出处** —— Oliver 先说（text:33 `now is a kind of forever`），Zach 在结尾复用（text:188 `now is a kind of forever`）。第 12/55 行把它当结尾句引用没问题；若日后补来源，写「奥利弗先说过、扎克在结尾又说了一遍」，**不要**写成扎克原创。
8. **英文引语 4 段全部逐字** —— 机器 4/4 命中（39/31/44/67 词），无一处改写；含卷引号 `“I wish I could be there, with you.”` 的嵌套也正确。
9. **词汇例句 14 条逐字可查** —— zombified（text:63）、postapocalypse（text:86）、laboriously（text:183）、bedridden（text:77）、narcotics（text:63）、hollowing（text:57）、outlived（text:53）、secretive（text:115）、sprawled（text:111）、diagnosis（text:57）、milkshake（text:58）、backyard（text:63）、swallowing（text:63）、pillow（text:76），行号均以 `/usr/bin/grep -n -F` 复核，无一改写。
