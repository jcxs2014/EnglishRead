# R4 逐块对应 · ch35《A Fatal Legacy》

判据（`docs/rules/审查表.md` R4）：不看子项标题，只回答「**这段中文是不是在讲这句引语**？」
四种结论：**对应** / **引语选短**（讲的是引语之外的上下文）/ **不对应**（讲全书主旨或作者生平）/ **密度不足**（只复述字面、没有「为什么这样写」）。
固定三问（R4 §固定追问）：① 每个动词的主语是谁 ② 受事/宾语是谁 ③ 「谁的 / 谁欠谁 / 谁问的」按原文 `by`/`to`/`from`/`of` 定方向。

引语区间＝本次审查从 `text/ch35_35.txt` 独立算出的字符偏移 [start, end)（原文 14455 字符）。

| 块 | 引语区间（字符） | 引语落点 | 这段中文是不是在讲这句引语 | 结论 | 三问核对（主语 / 受事 / 归属方向） |
|---|---|---|---|---|---|
| 原句 1 | 92–236（`text/ch35_35.txt:23`） | 「Hello, uh.」+「call him Peter but he got funny」+「97 per cent of her life」 | 是。中文理解逐项对应称呼、反应、百分比三件事；「为什么这样写」给出「称谓写成事故、97% 把天经地义写成可疑多数」——有「为什么」，非复述 | **对应**（密度合格） | ① 主语=卡莉（开门、开口、看出他神色不对）② 受事=那个称呼 ③ 「she'd called him for 97 per cent of her life」归属=卡莉（原文主语 she）✓ |
| 原句 2 | 239–349（`:26`） | 「I hope you don't mind me stopping by」+「peering over her shoulder to make sure she was home alone」 | 是。「作者不先写寒暄，先写视线」= 探头的动作当场拆穿「顺路」；并把凯厄斯后来进门提前压在读者心上 | **对应**（密度合格） | ① 主语=Peter（探头）② 受事=无 ③ 「home alone」=他要确认的是屋里只有她一人，方向由 `make sure` 决定 ✓ |
| 原句 3 | 1109–1358（`:41` 段后半） | 「She found it rather amusing; she was certain Peter had had elocution lessons in the eighties…」 | 基本是。中文对应「八十年代 / 谈吐训练课 / 响亮元音 / 喉塞音 / 从男爵爵位」；「为什么这样写」谈语音/政治词汇把父女分到两个世界，并兼带解释彼得忌惮凯厄斯——但这句解释的另一半成因（`partially due to how they had first met`）在引语**之前**且被丢掉（见 3-diff L2） | **对应 + 提示**（分析越出引语半步，漏一半成因） | ① 主语=卡莉（觉得滑稽、确信彼得上过课）② 受事=彼得/Caius 一家 ③ 「his elocution lessons」归彼得、「here was Caius's family」归凯厄斯一家 ✓ 未反转 |
| 原句 4 | 2560–2717（`:101`） | 「Not this again.」+ 上月改姓企图 + tabloid headline | 是。中文理解与「为什么这样写」（姓=要她认下名分）都在讲这一句；但「读者视角提示」把「他前面那句『你不是辛普森吧』」（`:98`）抬为本块起因，并把关系方向讲成「他在确认她认哪一半的血缘」——原文实为**父亲认领（Biologically speaking）/ 卡莉反问（Am I?）**（`:104-110`），方向被讲反了一层（见 3-diff L1/W5） | **对应 + 提示**（前后文取用有误，未构成「引语选短」） | ① 主语=卡莉（Not this again）+Peter（改姓企图）② 受事=姓 ③ 「change her surname to **his**」=Peter 要她改姓 ✓；「their relationship」原文未指明是何关系，md 未擅自指定 ✓ |
| 原句 5 | 4321–4649（`:137` 段内） | 「You're going to have to face up to it… the vultures would just be gleefully picking over your corpse」 | 是。「逼他面对 / 洗两次就烂的聚酯衬衫 / 临终与死后 / 秃鹫啄尸」逐项对应；「为什么这样写」给出道德→生死的升级路径与落点具体的反效果 | **对应**（密度合格） | ① 主语=卡莉 ② 受事=彼得（被逼面对的是他）③ 「your deathbed / your corpse / You'd have no right of reply」全归彼得 ✓ 未反转 |
| 原句 6 | 7888–8072（`:212`） | 「Bye, Dad」+ shutting the door + ginger tea too hot | 是。中文理解对应「挥手道别 / 门后喊爸 / 姜茶太烫」；「为什么这样写」把两个称呼与两杯茶对照——但三处说法与原文时序/在场事实不合（「生分的名字」「关上门、人走远之后」「等没有人的时候」，见 3-diff W1–W3） | **对应 + 提示**（时序与在场事实错，非对应问题） | ① 主语=Callie（喊、关门、坐回椅子、喝茶）② 受事=Peter（喊话对象）③ 「her ginger tea」归卡莉、「He didn't touch his tea」归彼得那杯 ✓ |
| 原句 7 | 8075–8113（`:215`） | 「He didn't touch his tea,' Caius said」 | 是。全章最短引语，中文只有一句「凯厄斯只说了一句：他的茶一口都没动」，但「为什么这样写」给出「不抿一口＝不肯客套」与「唯一实物当场被收拾掉」的判断 | **对应**（密度合格；但分析延伸到引语之后的 `:245`，属紧邻延展） | ① 主语=凯厄斯（说话者）② 受事=彼得那杯茶 ③ 「He」=彼得 ✓（`picked up Peter's cup of tea` 同一归属） |
| 原句 8 | 8283–8414（`:233`） | 「The series of crimes happened on a square that my dad partially owns… It's ours anyway」 | 是，但**主语被改**：中文理解写「凯厄斯说」✓，为什么这样写却写「**卡莉**那句『反正都是我们的』」✗；读者视角提示把产权人写成「**彼得**」✗（原文是凯厄斯的父亲） | **对应（主题在讲这句引语）+ 阻断（说话人错、施事反转）** | ① 主语=凯厄斯（`:227` 他报被撤案 → `:233` 他答）② 受事=凯厄斯的父亲部分持有的广场 ③ 「**my dad** partially owns」= 凯厄斯的父亲；「It's ours anyway」= 凯厄斯的「我们」。md 两处都归错 ⇒ 见 3-diff F1/F2 |
| 原句 9 | 11695–11865（`:320`） | 「Quite an unusual group of flowers. Asphodel, carnations and bay leaves aren't normally put together」 | 是。中文理解对应「搭配不寻常、三种花通常不搭」；但「为什么这样写」与「读者视角提示」继续讲**引语之后**的三条花语与祖母那本花语书（`:326`）——分析覆盖的原文长于引语（引语选短），主题仍属同一场景 | **引语选短（提示级）** | ① 主语=卡莉（走过去看、指出搭配）② 受事=那束花 ③ 三种花归卡莉口中的清单 ✓；md 把 asphodel 译作「水仙」、把三条花语都判为「绕不开死」，为原文所无/过强（W6） |

## 统计

- 对应：**9 / 9**（无「不对应」，无「密度不足」）
- 引语选短：**1**（原句 9，提示级；分析引语之外的紧邻花语段）
- 三问核对出的人物/施事错：**2**（均在原句 8：说话人 1 处、产权人 1 处）→ 见 `3-diff.md` F1 / F2，均判阻断
- 另：原句 4 的「读者视角提示」方向讲反（原句本身的对应不受影响）→ `3-diff.md` L1 / W5
