# 4-verdict.md · ch09 独立审查判定表

- 书：《A Fatal Legacy》（Charlotte Vassell）　章：09「Money or sex on the whiteboard」
- 审查对象：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch09 money or sex on the whiteboard.md`
- 权威源：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch09_9.txt`（7,269 字符 / 208 行）
- 落盘目录：`.memory/raw-gates/a-fatal-legacy-by-charlotte-vassell/review/ch09/`（本次**只**写此处；未改书目录任何 md，未 git add/commit）
- 覆盖声明：**本次受派只审第 9 章**。第 1–8、10–54 章未做人判，**只有机器层**（`chapter.sh` 已在全书跑过），不得读作「通过」。
- 执行顺序：R1 素读（只读 `text/ch09_9.txt`）→ 落盘 `1-suread.json` → R2 机器层 → 开 md → R3/R4/R5。

---

## 0. 四组数（只报这四组，不给单一「阻断 0」）

| 组 | 口径 | 结果 |
|---|---|---|
| **逐字** | 引语全串逐字命中 `text/ch09_9.txt`（自建全串比对，**不只前 90 字**）+ 词汇例句逐字 | 引语 **7/7**；词汇例句 **23/26**（3 条不逐字）。合计 **30/33** |
| **对应** | 逐块回答「这段中文是不是在讲这句引语」＋施事三问 | 块数 7；**对应 6 / 不对应 1**（原句 7）；引语选短 0；密度不足 0 |
| **形态** | H1 / 导航项名与项数 / 子项集 / 块数 vs 本书众数 + profile | **0 偏离**（详见 §3） |
| **断言** | 可核对的事实断言逐条回原文 | 共核 **47** 条（判定表 18 + 已核实为正确 29）：**阻断 6 / 提示 11 / 跳过 1 / 假红 0**；即不成立 **17** 条、成立 29 条、跳过 1 条 |

**阻断型条数：6**（A1–A6）。最要紧的一条见 §4。

---

## 1. 断言 | 证据（章:区间） | 结论 | 档位

| # | 断言 | 证据（text/ch09_9.txt:行 + 逐字） | 结论 | 档位 |
|---|---|---|---|---|
| **A1** | 原句 7「中文理解」`艾米说：她是在暗示，但让迪吉以为这是他自己想出来的。`；同块「为什么这样写」`艾米读信时抓到的是一个手法而不是一个事实` —— 说话人是艾米 | `text:177` [6044,6104] `‘She’s suggesting it but letting him think it was his idea.’`；前一轮 `text:174` [5808,6041] `‘It’s funny.’ Amy picked up a letter to show Caius one specific passage. ‘She doesn’t ask specifically to meet him there but she bookends the proposed date with a comment about the Institute and how interesting he is for running it.’`；后一轮 `text:180` [6107,6146] `‘Yeah. Why there and not a restaurant?’`；再后 `text:183` `‘A public place is safer, but that’s a female way of necessary, precautionary thinking.’` / `text:186` `‘Exactly. I wouldn’t arrange a date with a guy – at all but, you know, hypothetically – in a secluded place.’` | **说话人反**：该句是**凯厄斯**的推断（174 艾米举证 → 177 凯厄斯解读 → 180 艾米以「Yeah」附议 → 183 凯厄斯 → 186 艾米以「Exactly」附议凯厄斯）。若 177 归艾米，则 180 的「Yeah」成艾米附议自己；且 186 的「Exactly」附议对象只能是 183 的凯厄斯。md 两处均误安给艾米 | **阻断** |
| **A2** | 原句 7「为什么这样写」`伊索尔德从不直接要求见面` | `text:168` [5731,5783] `‘No. Although she’s very keen to meet face to face.’`；`text:174` `‘She doesn’t ask specifically to meet him there but she bookends the proposed date…’` | 原文只说她**不指定在 Institute 见**，并明说很想见面；md 写成「从不直接要求见面」＝把「不定地点」说成「不见面」 | **阻断** |
| **A3** | 导航·线索结构 `伊索尔德的来信：日期、**笔迹**、口吻与那三行自我介绍` | 本章无笔迹分析：`text:116` [4086,4301] `‘Forensics are done with the letters from Isolde. No fingerprints. The envelopes weren’t licked. No trace of the person who sent them.’`；`text:138` `‘I’ve gone through all the letters and I’ve made a key of their dates and contents…’`；`text:201` [6609,7135] 自述清单（`‘Five seven; brown hair; a primary school teacher (English lead); …’`）<br>取证：`/usr/bin/grep -icE 'handwriting\|hand-written\|hand written' notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch09_9.txt` → 输出 `0`，**退出码 1**；全书 `text/*.txt` 同模式 → 仅 `text/ch33_33.txt:1`（Isolde 讲自己写日记，与本章信件笔迹无关） | 线索类型凭空：「笔迹」在本章与全书（除 ch33 无关处）都没有 | **阻断** |
| **A4** | 导航·线索结构 `那**三行**自我介绍` | `text:201` [6609,7135] 清单在源文里是**一段**（行 201，单行 526 字符，12 项分号分隔）：`‘Five seven; brown hair; a primary school teacher (English lead); wants to move to a small village for the peace and quiet; grew up in Dorset; Dad is big Wagner aficionado; used to do ballet until she fractured three metatarsals; has a brother called Richard; took up watercolours last year; allergic to strawberries but adores raspberries; big fan of Dickens novels; went to Exeter university.’` | 计数无据：既不是三行也不是三项；建议改 `那串自我介绍` / `那份自述清单` | **阻断** |
| **A5** | 本章词汇（⭐ 基础）`plastic bag` 例句 `‘I’ll send you a link,’ Amy said, before handing Caius a plastic bag with the first letter in.` | `text:138` [4732,5080] `‘I’ve gone through all the letters and I’ve made a key of their dates and contents. I’ll send you a link,’ Amy said, before handing Caius a plastic bag with the first letter in.` | 例句被**截短**且**伪造开头引号**：原文的 `‘` 开在 `I’ve gone through…`，md 把开头两句砍掉后另起一个 `‘`，使它在原文里根本不是一句完整引语（Amy 说的不止这一句）。自检 `ex.strip() in src` → **False** | **阻断** |
| **A6** | 本章词汇（⭐ 基础）`day-to-day life` 例句 `…his friends, what he’re reading. Giving that ego a good, firm rubbing.’` | `text:144` [5150,5355] `‘Isolde takes a huge amount of interest in his day-to-day life. She’s asking him questions about the Institute, the book he’s writing, his friends, what he’s reading. Giving that ego a good, firm rubbing.’` | 逐字不符：`he’re` 应为 `he’s`（源码点 `0x73`='s'，md `0x72`='r'）；例句非本章原句形态 | **阻断** |
| B1 | 原句 2「中文理解」`银行里恐怕连两百万都没有` | `text:65` [1971,2367] `‘We need to look into Digby’s personal finances, but I doubt he had a couple of million in the bank.` | 措辞：原文 `a couple of million` 约「两三百万」，md 收窄为「两百万」；判断方向不变 | 提示 |
| B2 | 原句 2「读者视角提示」`他把迪吉的住处写进白板时` | `text:65` `He drew arrows coming off the word and started writing keywords as they spoke.` | 原文只说「边说边写关键词」，未明写把「studio in Dollis Hill」写上板；推断当事实 | 提示 |
| B3 | 原句 4「读者视角提示」`此时白板上大致有三行（钱、性、继承）` | `text:71` [2404,2729] `‘The contents or the building?’ Caius wrote both down.`；`text:89` [3152,3215] `‘Bogus name,’ Caius said, adding it to the board. ‘The PO Box.’` | 计数偏少：写下继承那格时板上另有 Money/箭头/关键词、contents、building；md 自带「大致」二字，属约数 | 提示 |
| B4 | 原句 1「读者视角提示」`留意这面白板此后只增不减：写上去的每一行，接下来都要拿证据去填满或者去划掉。` | 全章白板动作只有新增：`text:59` `wrote two words on a whiteboard`／`text:71` `Caius wrote both down`／`text:77` `writing it down`／`text:89` `adding it to the board` | 同一句自相矛盾（「只增不减」vs「去划掉」），且「划掉」本章未兑现 | 提示 |
| B5 | 原句 5「中文理解」`拒绝使用过去五十年里任何一项技术发明的家伙` | `text:83` [2928,3123] `‘Yes. Solitary Digby, who refuses to deal with any technology developed in the last fifty years, puts a lonely-hearts ad in a magazine.` | 措辞：原文是「过去五十年里**发展出来**的技术」，md 作「技术发明」 | 提示 |
| B6 | 本章词汇（⭐ 基础）`pavement` 例句 `‘The police cars had strewn past and blocked the pavement.’` | `text:129` [4367,4644] `…The police cars had strewn past and blocked the pavement.`（叙述句，**原文无引号**） | 给叙述句加了原文没有的一对引号，使其像一句对白；词句本身逐字 | 提示 |
| B7 | 导航·线索结构未承接「三分法」 | `text:26`/`text:29`/`text:32` `‘There are three options here, aren’t there? Firstly… Secondly, Digby is murdered.’ … ‘And thirdly, he was killed for access to the Institute.’` | 漏（提示级）：md 只承接了第三项被排除（`"为拿藏品"被排除`），三分框架本身未出现；非关键转折故不判阻断 | 提示 |
| B8 | 章末定调句未承接 | `text:207` [7177,7268] `‘Indeed.’ Caius gave Amy back her notebook. ‘She’s perfect for Digby. Too perfect perhaps.’` | 漏（提示级）：未成块、一句话总结亦未收；原句 6 分析已部分呼应「过度完美的可疑」，故不判阻断 | 提示 |
| B9 | 「性」这一栏的读信过程未成块 | `text:138` `…I’ve made a key of their dates and contents…`；`text:144` `Giving that ego a good, firm rubbing.`；`text:162` `‘Love bombing?’`；`text:165` `‘Yeah, I’m wondering.’`；`text:168` `‘No. Although she’s very keen to meet face to face.’`；`text:201` `‘Well, her height and hair colour match up with the footage at least.’` | 漏（提示级）：隔日回信模式／抚慰 ego／love bombing 疑点／未交换照片／自述与监控比对均未成块 | 提示 |
| B10 | 导航·视角 `紧贴**顾问警员**凯厄斯` | `text/xx_characters.txt:20` `An Irish-Jamaican detective in the Met, CAIUS is a foodie…`；`text/ch39_39.txt:54` `…your colleague DI Caius Beauchamp previously.` | 本章源文未给职级；全书另有 8 章用「顾问」（书级约定）。**书级口径问题，非本章独有**，故记提示、不判阻断 | 提示 |
| B11 | 全章 7 处用「博物馆」指 the Institute | `text/ch03_3.txt:98` `‘I was supposed to do tours of the museum. Sorry, Institute. I’m not supposed to call it a museum, it’s an institute for the further study of something or another.` | 书级译法：原文专门开了这个玩笑；全书「研究所」约 27 处、「博物馆」约 37 处，两种混用。建议全书统一口径，非本章缺陷 | 提示 |
| C1 | 支线 Barry / 门铃摄像头未提 | `text:107` `‘The neighbouring houses don’t, and no one else has a view either…’`；`text:110` `‘When will you hear from Barry?’`；`text:113` `…‘Not until tomorrow now.’` | 跳过：死线支线，非关键事件 | 跳过 |

## 2. 机器层（第二实现，不读 md 的结构）

```
$ bash scripts/chapter.sh "notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch09 money or sex on the whiteboard" --json > 2-machine.json
EXIT=0
```

`2-machine.json` 摘要：`verdict: ok`；`quotes` 7 条全部 `ok: true`；`blocks` 7 块，`segment_miss 0 / struct_bad 0 / empty_quote 0 / keyword_bad 0 / cjk_low 0`；四子项 CJK 占比 0.81–0.93。

**机器层口径两处限制（须人补，本章已补）**：
1. `chapter.sh` 的引语比对显示的是**前 90 字**（JSON 里 `text` 被截到 90 字符）。本章另做**全串**比对：7/7 全串命中（`pos` 分别为 1831 / 1971 / 2732 / 2840 / 2928 / 4166 / 6044）。
2. `check_vocab.py` 的例句比对口径是 `flat = re.sub(r'[^a-z0-9]','',…)` 后的**前 60 字符指纹**（`scripts/check_vocab.py:506` `example_ok`）。**该口径把引号全部抹掉、且只看前 60 字**，因此下面三类例句缺陷它一条都抓不到（本书 `check_vocab` FAIL=0、WARN 不含 ch09）：
   - A5 开头引号错位（flat 后正好命中）
   - A6 `he’re` vs `he’s`（差异位置在第 156 个字符，落在 60 字指纹之外）
   - B6 叙述句被加引号（flat 后命中）
   ⇒ 结论：**A5/A6/B6 是真缺陷，不是工具误报**；建议把 `example_ok` 的指纹从 60 扩到全长并保留引号比对（本条是工具口径建议，不改 md 之外的任何东西）。

## 3. 形态组

| 维度 | 本章实测 | 本书众数 / profile | 偏离 |
|---|---|---|---|
| H1 | `# 9. The Police Station`（源 `text:17` 标题行 `The Police Station`） | `# NN. <标题>`（ch01–ch12 实测同形） | 无 |
| 导航项名与项数 | 5 项：`一句话概括` / `视角` / `线索结构` / `人物弧线` / `叙事手法` | 本书 54/54 章同集（ch05、ch20 少 2 项）；profile `mystery-thriller` 记为「情感弧线位置」——本书统一用「视角」变体；`chapter.sh` `nav_missing: []` | 无（profile↔本书差异属本书既定变体，非本章偏离） |
| 子项集 | `中文理解` / `关键词` / `为什么这样写` / `读者视角提示`（7 块全覆盖，无缺项、无加项） | profile `subitems` 4 项（`optional: 句子结构` 未用） | 无 |
| 块数 | **7** | 本书中位 **7**，profile 区间 3–10；全书分布 5×5 / 6×19 / **7×10** / 8×5 / 9×8 / 10×7 | 无 |
| section | 4 个：`本章导航` / `精读` / `本章词汇` / `一句话总结` | profile `sections` 4 项 | 无 |
| 分部「A SUNDAY IN MAY」 | md 未设分部小节 | 权威源中该分部只剩分节符 `* * *`（`text:124` [4357,4362] `* * *`）；本书 26 章带分节符，**54 章 md 无一设分部小节** ⇒ 本章不设与本书约定一致 | 无 |
| frontmatter | `状态: 未读` / `modified: "2026-10-20"` / `source_text: ch09` | 与 ch08 等同书各章同形 | 无 |

**形态偏离：0 条。**

## 4. 最要紧的一条

**A1 —— 原句 7 的说话人被写反了：md 写成「艾米说」，原文这句是凯厄斯的推断。**
它同时污染同块「为什么这样写」（`艾米读信时抓到的是一个手法`），且正好打在本章的专属判据上——本章要写清「谁提出、谁反驳、谁沉默」：原文里是**艾米举证（text:174）→ 凯厄斯解读（text:177）→ 艾米以「Yeah」附议（text:180）→ 凯厄斯（text:183）→ 艾米以「Exactly」附议（text:186）**；md 把「举证者」当成了「解读者」，等于把推理链条的方向写反了。
四道机器探针全绿（引语逐字、7/7 命中；中文是中文；关键词成立；形态正常），只有 R4 的施事三问能抓到。
修法：原句 7「中文理解」与「为什么这样写」两处「艾米」改「凯厄斯」（艾米在此处是**读出信件原文**的人，凯厄斯是**做出推断**的人）。

## 5. 已核实为正确（防误修，固定一节）

> 凡写进这一节的，后续任何人不得以「读着不对」为由改动，除非能给出反证。

| # | 看着可能不对、实际成立 | 证据（text/ch09_9.txt:行 逐字） |
|---|---|---|
| V1 | **白板上那两个词是凯厄斯亲笔写的**（本章专属判据①） | `text:59` [1751,1953] `Amy poured herself a glass of water and the pair returned to the incident room. Caius put his tea on his desk and then, picking up a marker pen, wrote two words on a whiteboard. ‘Money or sex,’ he said.` — md 原句 1「中文理解」`凯厄斯把茶杯放到自己桌上，拿起一支马克笔，在白板上写下两个词：钱，或者性。` **相符** |
| V2 | **「钱」这一栏由凯厄斯圈定**（不是艾米） | `text:62` [1956,1968] `‘Which one?’`（艾米）→ `text:65` `‘Money.’ He drew arrows coming off the word and started writing keywords as they spoke.` — md 原句 2 `他先圈定"钱"这一栏` **相符** |
| V3 | **继承问题由艾米提出**（本章专属判据②） | `text:74` [2732,2837] `‘It’s worth a bomb.’ Amy stared at the whiteboard. ‘I wonder who inherits the Institute with Digby gone?’` — md 原句 3 `艾米盯着白板说……接着她抛出另一个问题——迪吉一死，博物馆归谁继承？` **相符** |
| V4 | **继承那一格由凯厄斯写上板、填的是「问题本身」而非答案**（本章专属判据③） | `text:77` [2840,2913] `‘That’s a good question,’ Caius said, writing it down. ‘Sex as a motive.’` — md 原句 4 `凯厄斯说这个问题问得好，一边把它记在白板上…` 且 `他既没有回答继承归谁，也没有否定这个问题，只是把它写下来当作待查项` **相符**；`Sex as a motive.` 是另起一栏，不是填格 |
| V5 | 本章只写到「提出问题」，未引后章答案 | 取证：`/usr/bin/grep -inc "inherit" …/text/ch09_9.txt` → `1`，退出码 0；命中行仅 `text:74`（提问句）。md 全文无继承者姓名 ✅ |
| V6 | 「谁反驳」：艾米反驳第三项、凯厄斯自驳「钱」 | `text:35` `‘I think three has been ruled out. What would they want access to? The boss-eyed kangaroo?’`；`text:65` `A scam to lure him out so he could be burgled isn’t impossible. Just no evidence to support it.` — md 导航人物弧线 + 原句 2「为什么这样写」`提出者自己先动手拆自己刚提出的假设` **相符** |
| V7 | 「谁沉默」：凯厄斯把继承问题记下而不答 | `text:77` `…writing it down. ‘Sex as a motive.’` — md 原句 4「为什么这样写」`被记下却不作答的沉默` **相符** |
| V8 | 导航「博物馆目录与展品逐一核对、并无一件失窃（"为拿藏品"被排除）」 | `text:23` [322,508] `‘We’ve finished cross-referencing the catalogue with the exhibits in the Institute,’ Amy said, sniffing her shirt. She could smell the damn place on her. ‘Not a single thing is missing.’`；`text:35` `I think three has been ruled out.` **相符** |
| V9 | 导航「迪吉的银行状况与多利斯山的小公寓（"图财"这一支缺少分量）」 | `text:65` `…but I doubt he had a couple of million in the bank. He was living in a studio in Dollis Hill. He wasn’t loaded.` **相符** |
| V10 | 导航「博物馆房产本身的价值与继承归属」 | `text:71` `‘I think the building is worth far more than its contents.’`；`text:74` `‘It’s worth a bomb.’` **相符** |
| V11 | 导航叙事手法「把街区写成被"凯特·摩丝化"再被金融从业者磨平」 | `text:71` `…then it was Kate Mossified with Cool Britannia, and now it’s been dullified by international finance bros in navy gilets.` **相符** |
| V12 | 导航叙事手法「用泡茶、煮水、拿马克笔、翻信件这类实物动作串起推理」 | `text:20` `He got up from his desk and went to the break room. He did squats as he waited for the kettle to boil.`；`text:59` `picking up a marker pen`；`text:138` `before handing Caius a plastic bag with the first letter in` **相符** |
| V13 | 导航视角「场景在警局休息室与事件室之间来回」 | `text:20` `went to the break room`；`text:59` `the pair returned to the incident room` **相符** |
| V14 | 导航视角「章末落到事件室的桌前，两人对着成叠信件读」 | `text:198` `Amy handed Caius her notebook.`；`text:201` `Caius began reading it out loud.` **相符** |
| V15 | 导航人物弧线「凯厄斯从一句"我卡住了"走到把猜想一条条画成箭头与词组」 | `text:50` [1419,1464] `‘Exactly. That’s where I keep getting stuck.’`；`text:65` `He drew arrows coming off the word and started writing keywords as they spoke.` **相符** |
| V16 | 导航人物弧线「正是她（艾米）问出"迪吉一死博物馆归谁继承"」 | `text:74`（同 V3）**相符** |
| V17 | 导航「艾米则从跑腿的人变成提出关键反问的人」 | `text:53` `‘I’ve had all of Digby’s paperwork from his office brought here. Everything is being fingerprinted.’` → `text:74` 提出继承问题 **相符** |
| V18 | 一句话总结「财产那一支因为死者自己并不有钱而显得分量不足」 | `text:65` `He wasn’t loaded. … It’s a lot of effort for a seemingly small bounty.` **相符** |
| V19 | 一句话总结「转而牵出"迪吉一死后博物馆归谁继承"这个没人答得上来的问题」 | `text:74` + `text:77`（全章无答案，见 V5）**相符** |
| V20 | 一句话总结「当法证在求爱信上查不出指纹与痕迹时，另一支"性"上的可疑便显得越来越浓」 | `text:116` `No fingerprints. The envelopes weren’t licked. No trace of the person who sent them.`；`text:119` [4304,4352] `‘Isolde is looking more and more like a killer.’` **相符** |
| V21 | 原句 5「他说：是」——答的是艾米 `‘Isolde?’` | `text:80` [2916,2925] `‘Isolde?’` → `text:83` `‘Yes. Solitary Digby…’` **相符** |
| V22 | 原句 6 的结论未被误安给任何人 | `text:116` `Amy’s desk phone rang… She hung up. ‘Forensics are done with the letters from Isolde…’` — md 用被动「法证那边把来信查完了」，未指错人 **相符** |
| V23 | 关键词子项 7 块全部命中所引原文 | whiteboard / Money or sex / marker pen；personal finances / loaded / bounty；worth a bomb / whiteboard / inherits；writing it down / Sex / motive；lonely-hearts / tailor-made / Solitary Digby；Forensics / No fingerprints / No trace；suggesting / his idea **全部命中** |
| V24 | 词汇档位无注水 | ⭐⭐⭐ 七条（Mossified / dullified / cross-referencing / tailor-made / metatarsals / instinctively / bookends）均为实词或习语，无常见词高星；⭐⭐ / ⭐ 分档合理 |
| V25 | 词汇例句 26 条中 23 条逐字命中本章 | 逐条 `ex.strip() in src` 命中；不命中的 3 条即 A5 / A6 / B6 |
| V26 | 原句 1「白板把散乱的猜想压成两个互相排斥的选项」 | `text:59` `‘Money or sex,’ he said.` 二选一结构 **相符** |
| V27 | 原句 3「把焦点从迪吉本人挪到房产上」 | `text:71` `The contents or the building?` → `text:74` `‘It’s worth a bomb.’` **相符** |
| V28 | 原句 6「三句短促的否定排成一列」 | `text:116` `No fingerprints.` / `The envelopes weren’t licked.` / `No trace of the person who sent them.` 三项否定 **相符** |
| V29 | 原句 5 读者提示「留意"杂志征友"这个入口」 | `text:83` `puts a lonely-hearts ad in a magazine` **相符** |

## 6. 本次审查自身的限制（诚实标注）

1. **只审第 9 章**：第 1–8、10–54 章只有机器层，**未做人判**，不得读作「通过」。
2. **R4 逐块对应只做「这句引语是不是这段中文在讲的东西」＋施事三问**，未逐句做语义等价复核；A2（`从不直接要求见面`）即由此抓出，仍可能存在同类未被逐句挑出的措辞级偏差。
3. **「笔迹」类零命中取证**已按 R5-补 附命令/输出/退出码；其余「本章没有」类判断（如白板无划掉动作、无人名继承者）均已回原文逐行确认，未依赖单一工具。
4. **未做**：本书 epub 缺失（`library/` 下无 epub），故无法核「A SUNDAY IN MAY」这个分部标题在 epub 原文里的字面形态；本次以 `text/ch09_9.txt` 的 `* * *` 分节符与本书 54 章 md 的统一约定为判据。
