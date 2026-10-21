# ch13 逐块对应（R4）

问法固定：**不看子项标题，只回答「这段中文是不是在讲这句引语？」**
三问（施事/受事/归属）逐块过一遍。

引语位置为 `text/ch13_13.txt` 的 0-based 字符区间（程序核对：每块为源文**单段连续串**，无 `…` 缝合、无跨话轮拼接）。

---

## 原句 1 ｜源文 515-919（`text/ch13_13.txt:44`）
> "Matt narrowed his eyes. He’d bet with Amy that it was going to be weird today. … so far, no one had endeavoured to cheat."

- **是不是在讲这句引语？** 是。中文理解（md:21）逐项对应引语内容：赌局、计分规则、月底请客、两人轮换裁定、英国标准、无人作弊。
- **密度够不够？** 够。「为什么这样写」把「公司规章化的玩笑」与案情并置，给出了「为什么这样写」而非复述字面；「读者视角提示」有具体抓手。
- **三问**：① 主语＝Matt ✓（narrowed / bet / scored）；② 受事＝「今天会不会很怪」这个赌题 ✓；③ 归属＝「赌给 Amy、对手是 Caius」——原文 "If he was correct, he scored a point but if he was wrong then Caius gained it"，md:21 写「赌对了自己得一分，赌错了分就归 Caius」✓ 方向正确。
- **但**：本块分析层含两条与原文不符的断言 → 见 3-diff 的 **J2**（比赛「没有结算结果」）、**J3**（「笑话落在改写成他杀之后」的时序）、**C4**（「对方不在时的裁判」）。
- **结论**：对应成立；带错 3 处（计断言组）。

## 原句 2 ｜源文 923-1149（`text/ch13_13.txt:47`）
> "‘OK fine, Callie baked the rolls using live Greek yoghurt. It was a recipe she saw online from a gastroenterologist-cum-chef. But it was just from M&S. In fact, it was their basic range. We’re trying to improve our gut health.’"

- **是不是在讲这句引语？** 是。md:28 覆盖活酸奶、配方来源、M&S 基础款、肠道健康四点，一一对应。
- **密度够不够？** 够。「为什么这样写」把「肠道友好」与毒芹投毒并置，解释了本章的母题在两处同时运转，不是字面复述。
- **三问**：① 主语＝Callie（baked the rolls）、Caius（说出这段话）✓；② 受事＝the rolls ✓；③ 归属＝「配方来自网上某位兼做厨师的胃肠科医生」——md 写「配方来自她在网上看到的一位兼做厨师的胃肠科医生」，「她」指 Callie ✓（原文 she saw online，she＝Callie）。
- **结论**：对应成立，无错。

## 原句 3 ｜源文 2206-2452（`text/ch13_13.txt:95`）
> "‘Nope,’ Caius said, picking up his sandwich. ‘Just had an email from the Food Standards Agency. … no trace of hemlock in their polytunnels whatsoever. It was murder.’"

- **是不是在讲这句引语？** 是。md:35「不会。Caius 拿起三明治说，刚收到食品标准局的邮件……那边的温室里压根没有毒芹的痕迹——是谋杀」——逐字级对应。
- **密度够不够？** 够。「为什么这样写」给出支点论证：查过来源农场、查过温室、没有毒芹 ⇒ 排除供应链 ⇒ 只剩故意；再补「偏偏这句结论被放在一只三明治旁边说出来」的落差。
- **三问**：① 主语＝Caius（said / had an email）✓；② 受事＝那袋沙拉的来源农场与温室 ✓；③ 归属＝结论来自**食品标准局**（不是 Caius 自创）✓，md 写「他们已经查过……来源农场」✓ 方向正确。
- **本章专属判据②**：毒芹与「是谋杀」的结论逐字 ✓。
- **结论**：对应成立，无错。

## 原句 4 ｜源文 2810-3107（`text/ch13_13.txt:114`）
> "‘As expected.’ Caius scrolled through the document. ‘This is interesting. They eliminated Willow’s and Digby’s fingerprints from the ones they’ve found and there were two partial prints that match each other. One on the library door and one on the door to the basement that has been painted over.’"

- **是不是在讲这句引语？** 是。md:42 覆盖「排除 Willow 与 Digby 指纹」「两枚残缺指纹彼此吻合」「图书馆门」「被漆盖住的地下室门」。
- **密度够不够？** 够。「为什么这样写」把物证功能从「谁在场」改写成「谁在别的时候来过」，并把解释权留给读者。
- **三问**：① 主语＝Caius（scrolled / said）；报告的发出方＝Barry 的报告（「They eliminated」＝法医）✓；② 受事＝残缺指纹 ✓；③ 归属＝「一枚在图书馆门、一枚在被漆盖住的地下室门」——md 写「一枚在图书馆门上，另一枚在那扇已经被漆盖住的地下室门上」✓ 方向与位置均正确。
- **注意**：md:44 的「漆是后来刷上去的，说明有人不想让那扇门再被打开」是**解释层推断**，原文只说 painted over；因指纹在门上、门又被漆盖住，推断「漆晚于指纹」在文本内自洽（漆盖住指纹），故不作缺陷，但「有人不想让门再被打开」一句超出原文，属解读范围。
- **结论**：对应成立，无错。

## 原句 5 ｜源文 3500-3874（`text/ch13_13.txt:132`）
> "‘I doubt Digby dusted that place. … Caius remembered how immaculate his own home had been though. ‘He was neglecting it. He’d had enough. Those two partial fingerprints could’ve stuck around for quite a while.’ … ‘Nothing was missing from the library, was he?’"

- **是不是在讲这句引语？** 是。md:49 逐项对应：Digby 没擦得那么干净 / 天知道留了多久 / Caius 想起自己家一尘不染 / 他在敷衍 / 他受够了 / 指纹可能早留下 / 图书馆没少东西吧。
- **密度够不够？** 够（正文层面）。「为什么这样写」正是本章专属判据要的那一层——办案人员说不出口的猜测。
- **三问**：① 主语：引语内「He was neglecting it / He’d had enough」的主语是 **Digby**（受话人对象），md:49 写「但他是在敷衍那地方，他受够了」✓ 指 Digby；「Caius 想起自己家」主语是 Caius ✓；② 受事＝那两枚残缺指纹 ✓；③ 归属＝「他可能会对警察说、却没说的那句心里话」✗ ——原文这句是**已说出口的台词**（在引号内，Caius 当着 Amy 说的）；叙述句只有 "Caius remembered how immaculate his own home had been though." 一句。
- **但**：本块分析层把「叙述 vs 台词」说反 → 3-diff **C1（阻断）**、**C2（提示）**。
- **结论**：对应成立；带错 2 处（计断言组）。

## 原句 6 ｜源文 8358-8926（`text/ch13_13.txt:235`）
> "Caius understood, he was in a similar situation himself, but … handsome payout for ridding himself of the guilt rankled him. … This windswept little rock clinging to the edge of Europe has the sixth largest economy. … ‘So Digby was moving back to York then?’"

- **是不是在讲这句引语？** 是。md:56 覆盖处境相似 / payout 不痛快 / Knaresborough 小屋 / 退到乡间能否洗脱 / 英国宽容 / 风雨小岛经济体量第六 / 遗产能否送人 / 拉回约克。
- **密度够不够？** 够。给出了「整段全是问而不答的内心追问」这一形式判断，并把它接回本章的不安主题。
- **三问**：① 主语＝Caius（understood / rankled / knew）✓；② 受事＝Digby 那笔卖房收益与自身处境 ✓；③ 归属：「迪吉能靠甩掉愧疚换上一笔漂亮的钱」——原文 "Digby would've had a handsome payout for ridding himself of the guilt"（受益者是 Digby）✓；「卖给国家的是家里那幅 Turner」出自原句 7，本块未越界。
- **但**：导航「人物弧线」把 rankled 写成「羡慕」→ 3-diff **C5（提示）**。
- **结论**：对应成立，无错。

## 原句 7 ｜源文 10326-10860（`text/ch13_13.txt:262`）
> "‘I really don’t know. We gave a Turner painting to the nation, but knowing my dad that was just a tax thing. Write an Apologia? You can’t inherit blame, but you do inherit responsibility.’ … ‘Isolde isn’t real. She responded to an ad. Maybe a scammer. “Fake Isolde” wore a “Willow costume” because she’d been watching the place and calculated that she wouldn’t look suspicious entering the building dressed as the intern.’"

- **是不是在讲这句引语？** 是。md:63 覆盖 Turner 捐画/税务/Apologia/罪责与责任/三点钟/假 Isolde/广告/骗子/Willow 扮相/盯梢与算计。
- **密度够不够？** 够。「为什么这样写」指出这是本章唯一被说出口的作案还原，却被写成随口一说，并把「继承责任」与「假 Isolde」并置。
- **三问**：① 主语＝Caius（said / gave）✓；「We gave a Turner painting to the nation」的主体是**Caius 一家**（原文 knew my dad 亦证）✓ md 写「他们曾把一幅 Turner 的画捐给国家」✓；② 受事＝那幅 Turner 画 ✓；③ 归属：「她早盯上了这个地方」——原文 "because she'd been watching the place"（施事＝假 Isolde）✓；「穿实习生打扮不会惹人怀疑」✓；方向全对。
- **结论**：对应成立，无错。

## 原句 8 ｜源文 10890-11112（`text/ch13_13.txt:268`）
> "‘It’s a long shot if it’ll throw up anything useful, but we really do need to check that every woman called Isolde within a hundred miles of London isn’t murdering their dates. One for us tomorrow, Matt, while Amy is off.’"

- **是不是在讲这句引语？** 是。md:70 覆盖「多半没指望」「未必查出有用东西」「查一查伦敦一百英里内每一个叫 Isolde 的女人」「是不是在谋杀自己的约会对象」「明天 Amy 休息，一个人来」。
- **密度够不够？** 够。「为什么这样写」解释了「全城 Isolde 被摊成名单」这个效果，并点出「办案人自己清楚这条线索有多薄」。
- **三问**：① 主语＝Caius（提出任务）✓；② 受事＝每一个叫 Isolde 的女人 ✓；③ 归属：「谁去查」——原文 "One for us tomorrow, **Matt**, while Amy is off"（派给 Matt，Amy 休假）✓ md:70 写「明天 Amy 休息，这活儿一个人来」✓；但 md:72 追加「**还在吃三明治的 Matt**」——原文里吃三明治的是 **Caius**（`:95`），且此刻早已过午饭、章末才去酒吧 ⇒ **施事/属性错配**（3-diff **J1，阻断**）。
- **但**：本块「为什么这样写」含 J1（阻断）。
- **结论**：对应成立；带错 1 处（计断言组）。

---

## 导航层（不在引语块内，一并核）

- md:11 一句话概括 / md:121 一句话总结：所述两条线（午饭比赛、毒芹与 Isolde 排查）确实是本章内容；但「周一上午」「一场毒芹排查同时占满」「摊成一张名单」三处措辞在原文里没有落点（本章只**派**任务、不做排查；名单实物在 ch16）→ 3-diff **C3（提示）**。
- md:12 视角：电话方向写反 → **C6（提示）**。
- md:13 线索结构四项逐条对得上原文：FSA 结论（`:95`）、两枚残缺指纹（`:114`）、失踪的 Willow 笔记与 Apologia 草稿（`:247`）、只写「深色头发」的纸面人物 Isolde（`:220`）✓。
- md:14 人物弧线：「罪责不能继承、责任却要继承」＝`:262` 逐字 ✓；「羡慕」一词 → **C5（提示）**。

## R4 汇总

| 块 | 对应（是不是在讲这句引语） | 密度 | 三问（施事/受事/归属） | 带错 |
|---|---|---|---|---|
| 原句 1 | 是 | 够 | 过 | J2、J3、C4 |
| 原句 2 | 是 | 够 | 过 | — |
| 原句 3 | 是 | 够 | 过 | — |
| 原句 4 | 是 | 够 | 过 | —（漆的解释层属解读，不判） |
| 原句 5 | 是 | 够 | **不过**（台词/叙述说反） | C1、C2 |
| 原句 6 | 是 | 够 | 过 | —（C5 在导航层） |
| 原句 7 | 是 | 够 | 过 | — |
| 原句 8 | 是 | 够 | **不过**（吃三明治者错配） | J1 |

- **对应 8/8**：没有一块在讲引语之外的上下文、没有一块滑向全书主旨或作者生平、没有一块只复述字面（每块均有「为什么这样写」层）。
- **无「引语选短」**：八块引语长度 222–568 字符，均为源文单段连续串，且各自的分析所指内容都在引语覆盖范围内。
- **三问失手 2 块**（原句 5、原句 8）→ 转入断言组计数。
