# ch07 R4 逐块对应（每块一行）

> 唯一要回答的问题：**这段中文是不是在讲这句引语？**
> 判据（`docs/rules/审查表.md` R4）：
> ① 讲的是引语之外的上下文 → **引语选短**（退回创建卡 §2 ①）
> ② 讲的是全书主旨 / 作者生平 → **不对应**
> ③ 只复述字面、没有「为什么这样写」 → **密度不足**
> 固定追问：每个动词的主语是谁？受事是谁？与原文那一句一致吗？“谁的/谁欠谁/谁问的”回原文看 by/to/from/of。
> md 行号指 `ch07 cctv shows a willow lookalike.md`；原句行号指 `text/ch07_7.txt`。

| 块 | 引语（原句:区间） | 这段中文在讲什么 | 对应？ | 追问结论（施事 / 受事 / 归属） |
|---|---|---|---|---|
| 原句1 | `:19` ← `:20`（Matthew 的 jungle playlist + 门铃摄像头录像：画质不差但太远，放大后能看到大轮廓，身高/体格/穿戴/携带物可辨） | 中文理解讲“把录像调出来放大看、只能看到轮廓与穿戴携带物”；为什么这样写讲“先给证据划出上限”；读者视角提示讲“清单只有轮廓那几项”。**三段全部在讲引语本身的证据边界**，没有跑到全书主旨或作者生平 | **对应**（但读者视角提示超出引语：引语只说“轮廓/身高/体格/穿戴携带物可辨”，**没说走路姿势读不出来**——这句话原文零命中，属编1，见 `3-diff.md`） | 主语一致：Caius 放录像 + 放大（`pressed play`、`He’d zoomed in`）。受事一致：路过者的轮廓与穿戴携带物。**唯一错位＝“静止剪影 / 走路姿势”**，原文无据 |
| 原句2 | `:26` ← `:30`（看到 6.30，playlist 第三遍；一个穿宽大开衫+深色宽松牛仔裤、深色波波头的女人，极像实习生 Willow Bell） | 中文理解讲“看到一个女人：开衫、牛仔裤、波波头、像 Willow”；为什么这样写讲“playlist 循环三遍写实感 + 叙述者只肯说‘看上去像’”；读者视角提示讲“这一句只完成形似一步”。**全部在讲这句引语** | **对应** | 主语：Caius（他看录像看见的）。受事：那个穿得像 Willow 的女人。归属：“She looked remarkably like Willow Bell, the intern”→ 像的是 **Willow Bell**（实习生），md 写“整体看上去和实习生 Willow 极为相似”✓ |
| 原句3 | `:33` ← `:67`（“Do you always wear dark jeans and an oversized cardigan. You had a red one yesterday, but this one is orange. It’s the same one though, isn’t it?”） | 中文理解讲“先确认是否总这么穿 → 点出红/橙差别 → 反问是否同一件”；为什么这样写讲“颜色既显眼又可能辨错、不可靠”；读者视角提示讲“留意颜色差”。**全部在讲这句问话** | **对应**（内容对，但读者视角提示的落点与同块「为什么这样写」相反、且漏掉原文 `:70` 的当场答案 → 见 `3-diff.md` 错4，提示级） | 主语一致：**问话者是 Caius**（`:61` “Caius looked at her”），受事是 Willow。md `:35` 只写“这句问话”，未误指派说话人 ✓。**注意**：“this one”原文指代本身有歧义（Willow 当天那件 vs 录像里那件），原文 `:30` 从未说录像里那件的颜色——md 把它读成“两人之间的细节差”缺据 |
| 原句4 | `:40` ← `:73`（拿出截图，看着她，**She was diminutive.**，“Willow, how tall are you?”） | 中文理解讲“拿出截图、打量面前的人、说她娇小、问她多高”；为什么这样写讲“先目测再发问，把量身高变成当面核对”；读者视角提示讲“身高是少数能当场复核的量化项”。**全部在讲这句引语** | **对应**（但中文理解多走了一步：把叙述句当成 Caius 说出的话 → 见 `3-diff.md` 错2，阻断级） | **施事错位**：`She was diminutive.` 是**叙述句**（无引号），Caius 在此处唯一说出口的是 `‘Willow, how tall are you?’`；md `:42`“说了句‘她很娇小’”给叙述句加了台词引号，且与同块 `:44`“他先**目测**再发问”自相矛盾 |
| 原句5 | `:47` ← `:140`（“You’re a couple of inches taller than Willow and this person is a couple of inches taller than you,” Caius said, comparing **both figures** to the iron railings） | 中文理解讲“把三个身影一起对着铁栏杆比，说 Amy 比 Willow 高几英寸，那人又比 Amy 高几英寸”；为什么这样写讲“不报绝对数字、拿栏杆当尺子”；读者视角提示讲“这是一次相对测量”。**全部在讲这句引语** | **对应**（但中文理解把“both figures＝两个影像”写成“三个身影”，且 Willow 的身高并非量得 → 见 `3-diff.md` 错1，阻断级） | 说话人 ✓ Caius；受事 ✓；**对象错**：与栏杆比对的是**两个影像**（录像截图里的人 + Tiny Simm 在同一地点拍的 Amy 照，`:137`），Willow 的身高是她自己报的 `:76`“Five foot two.”，**没有参与栏杆比对**。md 后半句（Amy 高几英寸、那人又比 Amy 高几英寸）与原文一致 |
| 原句6 | `:54` ← `:146`（“Looks like it.” Caius picked up the image of Willow’s doppelgänger. “Is it a prank?”） | 中文理解讲“捡起那张酷似 Willow 的女人的照片，说看起来就是这样，随后问对方会不会只是一场恶作剧”；为什么这样写讲“‘分身’把画面升格成待解释实体”；读者视角提示讲“这个说法很快会被证据推翻，注意它是怎么没的”。**全部在讲这句引语** | **对应**（但读者视角提示承诺的“被证据推翻”在本章 md 内**从未兑现**——原文 `:152` 的 PO Box/寄信数周/送检那一段被整段漏掉 → 见 `3-diff.md` 漏C，提示级） | 说话人 ✓ Caius（原文紧接 Amy 的“‘So what? They’ve dressed up as her?’”）；受事 ✓ 那张 doppelgänger 图像；md 未误指派 ✓ |
| 原句7 | `:61` ← `:243`（“I don’t think so. It’s a grainy picture. Maybe she’s just one of the square’s residents.” … “Or maybe I do have a weirdo fan after all?”） | 中文理解讲“说不认识、只是画面粗糙、可能只是广场住户；抬眼看向 Caius 又转向 Amy，转口问是不是真有个怪粉丝”；为什么这样写讲“当事人的否认与自证一口气说完，两个解释并列，谁也没被排除”；读者视角提示讲“当事人同样依赖这张模糊画面，她也不能作证”。**全部在讲这句引语** | **对应** | 主语一致：**说话人是 Willow**（被问“Do you know who this woman is?”的一方）；受事一致（那张模糊截图）；md `:63`“抬眼看向 Caius，又转而看向 Amy”与原文 “Willow looked up at Caius, but then switched her gaze to Amy” 一致 ✓。原文自带一次“先笑后慌”的细节（`:242`“She almost laughed. Caius attributed this to the shock.”）md 未收，属可选补充，不构成对应问题 |
| 原句8 | `:68` ← `:265`（“Maybe? If they wanted to get into the house incognito then why mimic Digby’s intern? They’ve just drawn our attention to themselves. I’ve got screenshots of ten other people who walked past in the two hours before Digby’s death that aren’t a priority any more.”） | 中文理解讲“Caius 反问：为何非要模仿实习生，这不是把自己推到视线中央；而案发前两小时截下的另外十个人已不再优先”；为什么这样写讲“外貌模仿本该是伪装、在监控下反而成了招摇 + 取舍本身是一次判断”；读者视角提示讲“把十个被搁置的截图记下来”。**全部在讲这句引语** | **对应** | 说话人 ✓ Caius（在走廊/事故室对 Amy 说）；受事 ✓ “ten other people … that aren’t a priority any more”；md “另外十个人…案发前两小时…不再优先”三处数字与原文 `:265` 一致 ✓ |
| 原句9 | `:75` ← `:277`（“I’m not sure.” … “Maybe they thought they were in disguise and hadn’t thought that far ahead. If someone was watching the house, say a neighbour or one of the protestors outside, they would probably just see a dark bob and giant cardigan. There’s the height difference, but if you glanced across from the square you might reasonably dismiss them as Willow putting in a late shift. Isolde must have been watching the Institute for a while.”） | 中文理解讲“也许对方以为装扮过、没想那么远：外面盯着的人只会看到深色齐耳短发和宽大开衫；有身高差，但扫一眼可能合理地当成 Willow 在加晚班；Isolde 一定已经盯了这间研究所很久”；为什么这样写讲“这是对目击证据的正面拆解：录像能证明有人经过、看得出轮廓，却证明不了身份”；读者视角提示讲“形似排除不掉谁，身份也建立不起来，推论只停在假设这一级”。**全部在讲这句引语** | **对应**（本块最好的一块：中文、为什么这样写、读者视角提示三段逐句咬住引语，且“目击证据不可靠”这一层写到位） | 主语 ✓ Caius；受事 ✓ 那个冒充者/目击者；“Isolde must have been watching the Institute for a while” 是**Caius 的推测**（must have），md 中文写作“**Isolde 一定已经盯了这间研究所很久**”——把推测写成断言，但同块读者视角提示又明说“只被允许停在‘假设’这一级”，属表述不严（提示级，非阻断）。另一处：原文 `Isolde` 是**暂定身份**（`:295` “the figure who they had to assume was Isolde for now”），md 写作“已经盯了很久”读起来像实锤，建议加“按目前假设” |

---

## R4 结论

- **对应块数：9/9**（每块的中文都在讲它自己的引语；无“引语选短”、无“讲全书主旨/作者生平”、无“只复述字面而无为什么这样写”）。密度方面 9 块均有「为什么这样写」且都给出了原文之外的写法动因（限额式清单、循环播放的实感、颜色不可靠、目测再发问、拿栏杆当尺子、分身词的升格、两个解释并列、伪装反成招摇、承认证据链天花板）——**无密度不足块**。
- R4 之外发现的 4 处施事/对象问题（错1 三个身影、错2 叙述句变台词、错3 走路姿势、错4 颜色落点自相矛盾）与 2 处承接断裂（漏A 在场证明缺失、漏C 恶作剧伏笔未兑现）均记在 `3-diff.md`，不在此重复计数。
- 唯一“讲引语之外上下文”的痕迹：原句1 的读者视角提示越过了引语边界去断言“走路姿势读不出”（引语只列了轮廓/身高/体格/穿戴携带物）——本块因此记为「对应，但有越界断言」。
