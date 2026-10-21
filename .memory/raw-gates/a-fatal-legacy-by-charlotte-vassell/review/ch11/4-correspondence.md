# ch11 逐块对应（R4）

> 判据（`docs/rules/审查表.md` R4）：不看子项标题，只回答「**这段中文是不是在讲这句引语**」。
> 不对应＝①讲的是引语之外的上下文（引语选短，退回 `docs/rules/创建卡.md` §2 ①）／②讲的是全书主旨或作者生平／③只复述字面、没有「为什么这样写」（密度不足）。
> 固定追问（对应 S3 第 ⑥ 类「施事/归属反转」）：每个动词的主语是谁？宾语/受事是谁？「谁的/谁欠谁/谁问的」回原文看 `by`/`to`/`from`/`of` 定方向。
> 引语区间＝`text/ch11_11.txt` 字符偏移 [start,end)（0 起算，Python 读全文）。

| 块 | 引语（md 行 / 原文区间） | 这段中文在讲这句引语吗？ | 施事/归属三问 | 结论 |
|---|---|---|---|---|
| 原句 1 | md:19 / [41,225) `Amy and Matt were busy arranging… institutional. Caius appeared without his cast.` | 是。中文理解拆成「分拣 personal or institutional」＋「凯厄斯没戴石膏绷带出现」，与引语两句一一对应；「为什么这样写」扣住「分类动作＝给纸定归属」，「读者视角提示」扣住「拿分类标准对后面每一份文件」——全在引语内 | ①主语=艾米和马特（分拣），凯厄斯（出现）②受事=迪吉办公室的文件③归属：personal/institutional 二分＝原文 `personal or institutional` | **对应** |
| 原句 2 | md:26 / [729,896) `Caius's phone rang… failed to get hold of her in Goa.` | 是。中文理解＝电话响起＋玩笑神色收住＋「迪吉的母亲芬内拉在楼下」＋外交部没联系上；「为什么这样写」扣住「全是短句的公文式通报」；「读者视角提示」扣住「在 Goa」这个地点 | ①主语=凯厄斯（接电话、说这句）②受事=电话/消息③归属：母亲＝芬内拉＝迪吉的母亲，原文 `Digby's mother Fenella`，md:28 写对了（与 md:35 冲突，见 W2） | **对应**（细节正确） |
| 原句 3 | md:33 / [2731,2891) `‘His mum wrote to him… the postcard sent from Goa on the fridge.` | 是（但**主语被改错**，见 W2）。中文理解讲「明信片与冰箱」，「为什么这样写」讲「私人信件的证据形态 vs 机构文件」——方向对；「冰箱贴」这一物名与同块中文理解「明信片」打架（C1） | ①主语＝写信人②受事＝收信人③**关键**：原文 `His mum` 的 `His` 指**迪吉**（上一句 `text:82` 谈 `Digby isn’t the only person who has a share of the property`；卡片实物见 `text/ch04_4.txt:56`，署名 `Mum x.`）。md:35 写「凯厄斯说，他母亲写信告诉迪吉」——中文「他」默认绑定最近的凯厄斯，等于凭空造出「凯厄斯的母亲给迪吉写信、两人要谈研究所未来」 | **对应（有归属错，见 W2）** |
| 原句 4 | md:40 / [3150,3437) `As you may be aware… et cetera, et cetera.` | 是。中文理解逐句对应（对方知道/本馆有七具/理事们的意愿/请部里指点渠道/两个 et cetera）；「为什么这样写」扣住公文套语与两次 et cetera 的含糊化 | ①主语=本信发信方（迪吉，以 Curator and Executive Chair 身份，落款块在 text:105-112，**在引语外**）②受事=七具 toi moko／mokomokai③归属：`the Institute is in possession of`＋`the wish of the trustees`＝机构口径；md:42「本馆」「理事们的意愿」方向对 | **对应**（引语可再扩到落款，见 4-verdict 提示） |
| 原句 5 | md:47 / [3579,3652) `‘It hasn’t been dated, or signed yet,’ Amy said, looking the letter over.` | 部分。中文理解扣住「没日期、没签名」（在引语内）；但「为什么这样写」后半段「**凯厄斯随即判断这封信是在等母亲回来后才发**」用的是 `text:123` `‘He was waiting to speak to his mum,’ Caius said.`——**落在引语之外**，属「引语选短」信号（R4 第一档）。另「和那些早已办妥的馆藏文件摞在一起」的「早已办妥」无原文支撑（W3） | ①主语=艾米（说这句）／引语外的判断主语＝凯厄斯②受事=那封信③归属：原文是「等母亲回来**谈**」，md 改写成「等母亲回来**才发**」——受事从「谈」漂移成「发信」 | **对应（密度足，但引语边界过窄＋W3）** |
| 原句 6 | md:54 / [3707,3895) `‘There was another letter kept in the same folder… Royal Geographical Society… ‘Also unsigned and undated.’` | 是（但**读者视角提示把结构讲反了**，见 W1）。「为什么这样写」扣住「同一个文件夹」＝原文 `the same folder` ✓；中文理解「同一个文件夹里还压着第二封信」✓ | ①主语=艾米②受事=「the rest of the collection」——原文是**其余**藏品，md:58 写成「藏品**整体**出手」（C2）③归属：`kept in the same folder`＝**同一个文件夹**，与 md:59「机构文件一摞／私人信件一摞」互相拆台（W1） | **对应（读者视角提示有结构性错，见 W1）** |
| 原句 7 | md:61 / [4451,4659) `‘Harm?’ she whispered… They murdered him!’` | 是。中文理解＝低声反问「伤害？」→ 想压住悲痛却冲凯厄斯喊出「他们杀了他…他们不是在胳膊上捏一把，他们是在谋杀他！」，与引语逐拍对上 | ①主语=芬内拉（whispered / shouting at Caius）②受事=警方对「harm」的用词③归属：`Harm?`＝对警方 `harm`（`text:151`，**在引语外**）的反驳；md:65「警方一开口用的是'harm'」方向对，但那句不在引语内 | **对应**（`text:151` 若并入引语更稳） |
| 原句 8 | md:68 / [6493,6960) `‘He called it “Our Apologia”… some man called Edward Said as a point of reference.’` | 是。中文理解逐点对应：书名→藏品不安→「藏品里有什么、怎么弄来的」→不光彩→谈出来比扫到虫蛀地毯下更健康→反思「直接继承了一份殖民恐怖」→Edward Said 作参照 | ①主语=芬内拉（说话人正确，`text:189` 提问、`:190` 回答）②受事=藏品/这本书③归属：`We both did`（`text:190`）＝芬内拉自己也厌恶——md:70「她也一样」译对了，未把 "we" 误派给他人 | **对应**（说话人/归属正确） |

## 逐块结论

- **8/8 块主题上对应**（每块的中文都确实在讲自己那句引语），无「讲全书主旨/作者生平」型不对应，无「只复述字面」型密度不足。
- 真正的缺口不在「对应」这一轴，而在 **归属轴与事实轴**：W2（原句 3 的「他母亲」）、W1（原句 6 读者视角提示把「同一个文件夹」拆成两摞）、C1（冰箱贴）、C2（整体 vs 其余）、W3（早已办妥）、W4（几十年）——其中 W2、W1 由本表直接暴露。
- 引语选短（R4 第一档）共 2 处，均为**提示级**（分析主体仍落在引语内，只是引用了紧邻的下一句作支撑）：
  - 原句 5 用到引语外的 `text:123`（`He was waiting to speak to his mum`）；
  - 原句 7 的「警方一开口用的是 harm」依赖引语外的 `text:151`。
  - 建议：把这两句并入引语，或在分析里标明「据下一段」。

## 三处词名级问题（不影响对应判定，随 3-diff 记）

- C1 `md:37` 「一张**冰箱贴**」——原文是明信片（`text:85` `the postcard sent from Goa on the fridge`；`text/ch04_4.txt:56` `a postcard of a Goan beach clinging to the front of it`）。同块 `md:35` 自己写的是「明信片」。
- C2 `md:58` 「把藏品**整体**出手」——原文 `offering the rest of the collection`（其余藏品）；同块 `md:56` 自己写的是「其余藏品」。
- C6 `md:82` 词汇条 `toi moko | 毛利人对待敌人遗骨的方式，此处指人头骨`——本章原文只说 `toi moko or mokomokai` 与 `human remains`（`text:99`），释义属书外补入（`text/ch02_2.txt:285` 给的是「纹饰人头」）。
