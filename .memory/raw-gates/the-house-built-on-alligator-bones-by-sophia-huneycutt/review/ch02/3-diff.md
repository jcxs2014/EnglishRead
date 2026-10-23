# ch02 对账（R3/R4：素读事实 ↔ md）

text = `text/ch02_chapter_one.txt`（151 行）｜md = `ch02 the letter in the trash.md`｜块数 5｜素读事实 30 条

## 阻断

- **[C-02-1] 对应／凭空**｜md:11「章末情绪落到主动——她按下 Send，把「One of the Greers」念出声。」
  原文 `text/ch02_chapter_one.txt:147` `One of the family, I thought to myself, liking the sound of it.` → :150 `One of the Greers.`
  「念出声」是**出声**，原文写明 `I thought to myself`＝心里想；且「liking the sound of it」指**说法的听起来的效果**，不是朗读动作。
- **[C-02-2] 凭空**｜md:34「支票不是「一张」而是「two halves」——撕开又被人捡回来收着的残片」
  原文 :24 只给 `two halves of a ripped check`（与信一起掉出来），:27 `The letter itself was intact but crumpled, like Mama had handled it often` 的主语是**信**不是支票；全章**没有任何一句**写支票被捡起收存，也没写是谁撕的。
- **[C-02-3] 凭空量词**｜md:60「枪托没入一人深的荒草里」
  原文 :129 `its stock disappearing into overgrown grass`——只有 overgrown，**没有高度量度**。「一人深」是补进来的画面尺寸。
- **[C-02-4] 章内时序写反**｜md:64「画像比信早一步有了归属，又立刻被 whoever that was 取消归属」
  顺序相反：:49 信的 PPS 先给出名字 `I’m including a small print of Ida’s portrait.`，:129 她才据画自证 `I decided she must be Ida, whoever that was.`
  ⇒ 归属流向是**信→画像**；md 写成画像先于信。（另：`whoever that was` 悬置的是 **Ida 是谁**，不是「画像归属」。）
- **[C-02-5] 章内时序＋因果凭空**｜md:66「藏的位置也是信息——本章最后一封「回信」将由这个位置差异发起。」
  回信只有**一封**，且已在 :120 `I clicked Send` 发出；藏匿差异的复盘在 :141 `At the time, I didn’t consider the fact that…`——**在其后**。不存在「由这个位置差异发起」的回信。
- **[C-02-6] 归属／出处错**｜md:14「信的正文整段照录，不经叙述者改写；……同一封里也承认「I had no other guesses」」
  `I had no other guesses` 出自 :18 的**叙述层**（`Maybe this Gazzie person was an acquaintance from Mama’s years in the foster system; I had no other guesses.`），**不在信的正文**（:31–:49，抬头 Caroline／落款 Gazzie）之内。「同一封里」把叙述者的猜测算进 Gazzie 的信。
- **[C-02-7] 漏（主要信息单元全篇未提）**｜:85 `We’d had a circle of trust, Mama and I; whatever false fronts we put on for outsiders, we told the truth to family.`＋同段 `here Mama had spun a fake history about being born into the foster system, about having no real last name other than the one she’d married into`
  本章背叛感的支点＝**母女的家规被 Mama 自己破了**，且 Mama 的假出身具体是「福利系统＋没有真姓」两件事。md 导航五项目、五个块、词汇层**均未出现**这条家规与这条假出身的内容（Tropes 只有泛称「被隐瞒的家族」）。
  同段还漏 :91 `Or maybe, whispered a familiar voice, that bitch wanted to keep you all to herself.`——「一个熟悉的声音」是叙述者内在敌意的第一次到场（本章四个「也许」之后的第五个），md 未提。

## 提示

- **[C-02-P1]**｜md:10「信中称她「my girl」」——句中主语一路是叙述者，读者会把她当成 my girl 的对象；原文 :31 抬头 `Caroline,`＋:37 明确是写给 Caroline 的。md:44 自己写对了（「写信人管 Caroline 叫 my girl」），此处改为「称 Caroline「my girl」」。
- **[C-02-P2]**｜md:64「读者由此知道这不是摄影棚摆拍，是真实水边的草」——推断语气偏硬：原文只在同一句里给了 `behind her stretched the black waters of a marsh`，画的仍是画；「水边」可，「不是摄影棚摆拍」超出本章证据。
- **[C-02-P3]**｜:129 `a messy medium I hadn’t worked in yet`（油画＝她尚未用过的媒介，人物作为创作者的第一条线索）md 未提；与 ch23  ruined sketchbook、ch49 五年前速写本同一条线。
- **[C-02-P4]**｜:132 `Mama would have skinned me sideways for looking at someone like that.` md 未提（本章唯一一处用「剥皮」作家教比喻的句子，与 ch18 skinning 101 的动词层同源）。
- **[C-02-P5]**｜md:20「发黑的橙皮」——原文 `browning`＝氧化发褐，不是发黑。

## 已核实为正确

- 五个引语块逐字（`chapter.sh` ①＋`verify_fragments_indep` 分片均命中，见 2-machine.json）。
- md:44 对信的读法：抬头 Caroline／落款 Gazzie／my girl 指 Caroline ✓（:31、:37、:43）。
- md:46「thirty-two years 没有被明说是她的年龄」✓——全章只有 :56 这一处 `thirty-two years`，无第二处支撑她的年龄。
- md:36「信纸皱得像被反复摸过、信封邮戳却只有两周 ⇒ 推出 Mama 手术前就收到信」✓（:27，且原文自带 `She must have received it several days before her surgery`，md 把推断归给叙述者，方向正确）。
- 关于回信内容「撒谎说「我母亲一定想让我们见面」」✓——:110 `as I’m sure my mother intended`＋:120 `Mama had not intended we meet`，md:13 写法与原文的自认一致。
- 产业信息：总部 Jacksonville／1892 创立／125 年以上 ✓（:75）；Fernandina Beach ✓（:9）；邮箱 `virginia@greerfinealligators.com` 与 "Ginny" ✓（:40）。
- 「Mama 刚下葬／本周去世」✓（:9、:21、:107）。
