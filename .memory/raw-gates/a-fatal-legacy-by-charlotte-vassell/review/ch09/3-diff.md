# 3-diff.md · 《A Fatal Legacy》ch09「Money or sex on the whiteboard」对账三单

- 审查对象：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/ch09 money or sex on the whiteboard.md`
- 唯一权威源：`notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch09_9.txt`（7,269 字符 / 208 行）
- 区间记法：`text/ch09_9.txt:<行号>` + 字符区间 `[起,止)`
- 素读底稿：`1-suread.json`（先素读后开 md，R1 已落盘）
- 本次不修改书目录任何 md、不 git add/commit；只写本目录

---

## 单子一 · 漏（素读有、md 无）

| 编号 | 档 | 素读事实（源文逐字） | md 现状 | 判定 |
|---|---|---|---|---|
| L1 | 提示 | `text:26` `‘Good job,’ Caius said, pouring water into the cup. He turned to look at Amy. ‘There are three options here, aren’t there? Firstly, Digby accidentally ate the salad with poisoned leaves in, he dies, Isolde panics and flees.’`；`text:29` `‘Secondly, Digby is murdered.’`；`text:32` `‘Specifically, because of something he’s done or will do. Something personal. And thirdly, he was killed for access to the Institute.’`；`text:35` `‘I think three has been ruled out. What would they want access to? The boss-eyed kangaroo?’` | md 全文无「三分法（意外／谋杀／为取物）」这一框架本身；导航「线索结构」只承接了第三项的排除（`"为拿藏品"被排除`），前两项与「Amy's rule-out」只作为背景隐含 | 提示级漏：三分法是本章开篇的结构性框架（也是后文「钱/性」两栏的前身），但导航已部分承接，不判阻断 |
| L2 | 提示 | `text:207` `‘Indeed.’ Caius gave Amy back her notebook. ‘She’s perfect for Digby. Too perfect perhaps.’` | 无块引用；「一句话总结」亦未收；仅原句 6 的「为什么这样写」顺带提到 `"量身定做"那种过度完美的可疑` | 提示级漏：章末定调句未被独立承接（md 已有部分呼应，故不判阻断） |
| L3 | 提示 | `text:138` `‘I’ve gone through all the letters and I’ve made a key of their dates and contents…’`；`text:144` `…Giving that ego a good, firm rubbing.’`；`text:162` `‘Love bombing?’`；`text:165` `‘Yeah, I’m wondering.’…`；`text:168` `‘No. Although she’s very keen to meet face to face.’`；`text:201` `‘Five seven; brown hair; … went to Exeter university.’… ‘Well, her height and hair colour match up with the footage at least.’` | 「性」这一栏的实质读信过程（隔日回信模式／抚慰ego／love bombing 疑点／未交换照片／自述清单与监控比对）未成块，只在导航以 `那三行自我介绍` 一笔带过 | 提示级漏（非关键转折；原句 6、7 已承接部分） |
| L4 | 跳过 | `text:107` `‘The neighbouring houses don’t, and no one else has a view either…’`；`text:110` `‘When will you hear from Barry?’`；`text:113` `…‘Not until tomorrow now.’` | 未提 | 跳过：死线支线，非关键事件，不计入漏 |

---

## 单子二 · 编（md 有、原文无）

| 编号 | 档 | md 逐字 | 源文事实 | 判定 |
|---|---|---|---|---|
| F1 | **阻断** | 导航·线索结构：`伊索尔德的来信：日期、笔迹、口吻与那三行自我介绍（"性"这一支填出内容）` 中的「笔迹」 | 本章**无任何笔迹/字迹分析**；法证只查了指纹与唾液（`text:116` `‘Forensics are done with the letters from Isolde. No fingerprints. The envelopes weren’t licked. No trace of the person who sent them.’`），Amy 做的是「日期与内容对照表」（`text:138`），Caius 读的是 Amy 的自述清单（`text:201`） | **编**：线索类型凭空。取证：`/usr/bin/grep -icE 'handwriting\|hand-written\|hand written' notes/books/mystery-thriller/a-fatal-legacy-by-charlotte-vassell/text/ch09_9.txt` → 输出 `0`，退出码 1；全书 `text/*.txt` 同模式 → 仅 `text/ch33_33.txt:1`（Isolde 讲自己写日记的往事，与本章信件笔迹无关） |
| F2 | **阻断** | 导航·线索结构：`那三行自我介绍` | `text:201` 自述清单在 `text/` 里是**一段**（一个段落、行号 201，单行 526 字符），由 12 个分号隔开的项目组成：`‘Five seven; brown hair; a primary school teacher (English lead); wants to move to a small village for the peace and quiet; grew up in Dorset; Dad is big Wagner aficionado; used to do ballet until she fractured three metatarsals; has a brother called Richard; took up watercolours last year; allergic to strawberries but adores raspberries; big fan of Dickens novels; went to Exeter university.’` | **编（计数无据）**：「三行」在权威源里没有对应物；源文该清单既不是三行，也不是三项。改法：改 `那串自我介绍` 或 `那份自述清单` |
| F3 | **阻断** | 本章词汇（⭐ 基础）`plastic bag` 例句：`‘I’ll send you a link,’ Amy said, before handing Caius a plastic bag with the first letter in.` | `text:138` 原文为：`‘I’ve gone through all the letters and I’ve made a key of their dates and contents. I’ll send you a link,’ Amy said, before handing Caius a plastic bag with the first letter in.` | **编**：例句把一句长引语的**开头截掉**并在 `I’ll` 前**伪造一个原文没有的引号**；该例句在原文里根本不是一句完整的引语（Amy 说的不止这一句）。自检：`ex.strip() in src` → **False**（逐字命中失败） |
| F4 | **阻断** | 本章词汇（⭐ 基础）`day-to-day life` 例句：`…his friends, what he’re reading. Giving that ego a good, firm rubbing.’` | `text:144` 原文为：`…his friends, what he’s reading. Giving that ego a good, firm rubbing.’` | **编（逐字不符）**：`he’re` 应为 `he’s`（原文是 `he’s reading`，逐码点核对：源 `0x73`='s'，md `0x72`='r'）。例句非本章原句形态 |
| F5 | **阻断** | 原句 7「为什么这样写」：`伊索尔德从不直接要求见面，只把博物馆的评论夹在约定日期的前后` | `text:168` `‘No. Although she’s very keen to meet face to face.’`；`text:174` `‘She doesn’t ask specifically to meet him there but she bookends the proposed date with a comment about the Institute and how interesting he is for running it.’` | **编（过度断言）**：原文只说她**不指定在 Institute 见**，且明说「very keen to meet face to face」；md 写成「从不直接要求见面」＝把「不定地点」说成「不见面」 |
| F6 | 提示 | 本章词汇（⭐ 基础）`pavement` 例句：`‘The police cars had strewn past and blocked the pavement.’` | `text:129` 原文是叙述句、无引号：`The police cars had strewn past and blocked the pavement.` | 提示（措辞/标点形态）：词句逐字有，但给叙述句加了原文没有的一对引号，使其看起来像一句对白 |

---

## 单子三 · 错（两边都有但不一致）

| 编号 | 档 | md 逐字 | 源文逐字（说话人判定依据） | 判定 |
|---|---|---|---|---|
| E1 | **阻断** | 原句 7「中文理解」：`艾米说：她是在暗示，但让迪吉以为这是他自己想出来的。`；同块「为什么这样写」：`艾米读信时抓到的是一个手法而不是一个事实` | 该句是**凯厄斯**说的。轮次证据：`text:174` `‘It’s funny.’ Amy picked up a letter to show Caius one specific passage. ‘She doesn’t ask specifically to meet him there but she bookends the proposed date…’`（Amy 举出信件原文）→ `text:177` `‘She’s suggesting it but letting him think it was his idea.’`（推断落在此）→ `text:180` `‘Yeah. Why there and not a restaurant?’`（**Amy** 用「Yeah」附议上一句并反问）→ `text:183` `‘A public place is safer, but that’s a female way of necessary, precautionary thinking.’`（Caius）→ `text:186` `‘Exactly. I wouldn’t arrange a date with a guy – at all but, you know, hypothetically – in a secluded place.’`（Amy 用「Exactly」附议 Caius） | **错（说话人/施事归属反）**：md 把推断归给 Amy。原文的推断者是凯厄斯——174 是 Amy 举证，177 是凯厄斯的解读，180 是 Amy 以「Yeah」附议凯厄斯；若 177 是 Amy 说的，180 的「Yeah」就成了 Amy 附议自己。全章问-答轮次（138–207）一致交替：Amy 174 → Caius 177 → Amy 180 → Caius 183 → Amy 186 |
| E2 | 提示 | 原句 2「中文理解」：`银行里恐怕连两百万都没有` | `text:65` `‘We need to look into Digby’s personal finances, but I doubt he had a couple of million in the bank.` | 提示（措辞）：`a couple of million` 约「两三百万」，md 收窄成「两百万」，方向不改变判断 |
| E3 | 提示 | 原句 4「读者视角提示」：`此时白板上大致有三行（钱、性、继承）` | `text:71` `‘The contents or the building?’ Caius wrote both down.`（另有两个词已写上板）；`text:89` `‘Bogus name,’ Caius said, adding it to the board. ‘The PO Box.’` | 提示（计数）：写下「继承」那一格时白板上还有 Money/箭头/关键词与 contents、building；「三行」偏少（md 自带「大致」二字，属约数） |
| E4 | 提示 | 原句 2「读者视角提示」：`他把迪吉的住处写进白板时，等于承认这个受害者没有旁人以为的那种资产` | `text:65` `He drew arrows coming off the word and started writing keywords as they spoke.` | 提示（推断当事实）：原文只说他「边说边写关键词」，未明写把「studio in Dollis Hill」写上板 |
| E5 | 提示 | 原句 1「读者视角提示」：`留意这面白板此后只增不减：写上去的每一行，接下来都要拿证据去填满或者去划掉。` | 全章白板动作只有新增：`text:59` wrote two words、`text:71` wrote both down、`text:77` writing it down、`text:89` adding it to the board；本章**无任何划掉/擦除动作** | 提示：同一句内自相矛盾（「只增不减」vs「去划掉」），且「划掉」本章未兑现 |
| E6 | 提示 | 原句 5「中文理解」：`拒绝使用过去五十年里任何一项技术发明的家伙` | `text:83` `‘Yes. Solitary Digby, who refuses to deal with any technology developed in the last fifty years, puts a lonely-hearts ad in a magazine.` | 提示（措辞）：原文是「过去五十年里**发展出来**的技术」，md 写成「技术发明」 |
| E7 | 提示 | 导航·视角：`紧贴顾问警员凯厄斯` | 本章源文未给职级；`text/xx_characters.txt:20` `An Irish-Jamaican detective in the Met, CAIUS is a foodie…`；`text/ch39_39.txt:54` `…your colleague DI Caius Beauchamp previously.` | 提示（书级约定，非本章独有）：全书另有 8 章用「顾问」；本章源文无据可判，不判阻断 |
| E8 | 提示 | 全章 7 处用「博物馆」指 the Institute | `text/ch03_3.txt:98` `‘I was supposed to do tours of the museum. Sorry, Institute. I’m not supposed to call it a museum, it’s an institute for the further study of something or another.` | 提示（书级译法约定，非本章缺陷）：原文专门开了这个玩笑；全书「研究所」约 27 处 / 「博物馆」约 37 处，两种混用，建议全书统一口径 |

---

## 三单小计

- 漏：4 条（阻断 0 · 提示 3 · 跳过 1）
- 编：6 条（**阻断 5** · 提示 1）
- 错：8 条（**阻断 1** · 提示 7）
- 合计 **18 条**（阻断 **6** · 提示 11 · 跳过 1 · 假红 0）——与 `4-verdict.md` §1 判定表 18 行一一对应

## 本章专属判据核对（只核对到「提出问题」为止，不引后章答案）

| 判据 | 源文 | md | 结论 |
|---|---|---|---|
| 白板上那两个词是谁写的 | `text:59` `Caius put his tea on his desk and then, picking up a marker pen, wrote two words on a whiteboard. ‘Money or sex,’ he said.` | 原句 1「中文理解」：`凯厄斯把茶杯放到自己桌上，拿起一支马克笔，在白板上写下两个词：钱，或者性。` | ✅ **相符**（凯厄斯亲笔；md 未含糊成「两人合写」） |
| 钱这一栏由谁定 | `text:62` `‘Which one?’` → `text:65` `‘Money.’` | 原句 2「中文理解」：`他先圈定"钱"这一栏` | ✅ 相符（Amy 问、凯厄斯答并从 Money 拉箭头） |
| 谁提出继承问题 | `text:74` `‘It’s worth a bomb.’ Amy stared at the whiteboard. ‘I wonder who inherits the Institute with Digby gone?’` | 原句 3「中文理解」：`艾米盯着白板说：那栋楼值一大笔钱；接着她抛出另一个问题——迪吉一死，博物馆归谁继承？` | ✅ 相符（**艾米提出**） |
| 继承那一格最后填上的是谁、填了什么 | `text:77` `‘That’s a good question,’ Caius said, writing it down. ‘Sex as a motive.’` | 原句 4「中文理解」：`凯厄斯说这个问题问得好，一边把它记在白板上，一边接上另一条：把"性"作为动机。`；「为什么这样写」：`他既没有回答继承归谁，也没有否定这个问题，只是把它写下来当作待查项` | ✅ 相符（**凯厄斯把「谁继承」这个问题写上板**；填上去的内容就是这个问题本身，不是答案；`Sex as a motive.` 是另起一栏，非填格） |
| 谁反驳、谁沉默 | 反驳：`text:65` 凯厄斯自驳自己的「钱」（`A scam… isn’t impossible. Just no evidence to support it.`）；`text:35` 艾米反驳第三项（`I think three has been ruled out`）；沉默：`text:77` 凯厄斯把继承问题记下而不答 | 原句 2「为什么这样写」：`提出者自己先动手拆自己刚提出的假设`；原句 4「为什么这样写」：`被记下却不作答的沉默…这一章里"谁提出、谁反驳、谁沉默"的形状就摆在这里` | ✅ 相符（md 三个位置均已写明） |
| 不得引入后章答案 | 本章止于「提出问题」；`text:4352` 之后无继承答案 | 全文无继承者姓名、无后章信息 | ✅ 相符 |
