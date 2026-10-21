# ch37 · R4 逐块对应（这段中文是不是在讲这句引语？）

判据：**① 每个动词的主语是谁 ② 宾语/受事是谁 ③ 「谁的/谁欠谁/谁问的」的方向**（回原文读整句，不只读命中行）。
引语区间＝`text/ch37_37.txt` 的字符区间 `[起, 止)`；逐字核验＝md 引语是否为原文连续子串。

| 块 | 引语（原文区间） | 这段中文在讲这句引语吗？ | 施事/受事核对 | 判定 |
|---|---|---|---|---|
| 1 | 交接指令（[123, 432]，text:23） | 是。中文理解＝主语「总警监」宣布 Robbie 接任；受事/理由＝Caius 父亲持有租约的物业；Caius 休年假下周回案头。为什么这样写讲「把换人原因钉在产权上」，即本句本身；读者视角提示接的是同段 Chief 离开时盘算 NW1 租约（text:32） | 主语＝Chief Superintendent ✓；「his father」先行词＝Caius（md 中文「他」有歧义，见 3-diff 错-8）✓方向未反 | **对应**（1 处指代歧义，见错-8） |
| 2 | Robbie 复述案情（[1442, 2116]，text:44） | 是。中文理解逐句对上：毒沙拉→假 Isolde→交友广告→PO Box（盗刷约克郡女子信用卡）→面包店的 incel Scott→「假 Isolde」勾搭上、见女客就搭讪→两起闯入→Jimmy Jones 意外身亡。为什么这样写抓的是 supposedly / fake / accidental 三个偏差词 | 主语＝Robbie（复述者）✓；「collected by an incel」受事＝邮件、收取者＝Scott ✓；「that this 'fake Isolde' … had seduced」方向＝假 Isolde 勾搭 Scott（md 作「被…勾搭上」✓）；「where he hit on every other female customer」的 he＝Scott ✓ | **对应**（1 处译名失真：enfant terrible→「红星」，见错-3） |
| 3 | Matt 指 Robbie 打断 Amy（[2691, 2913]，text:71） | 是。中文理解＝Matt 把 Amy 的受挫翻译给 Robbie；为什么这样写论「用一句翻译把情绪讲出来」；读者视角提示落在「话没说完就被打断」 | 主语＝Matt（说话人）✓；受事＝Robbie（被告知）；「she is now feeling frustrated」＝Amy ✓ | **对应，但「为什么这样写」的断言与原文矛盾**（作者确实写了 Amy 的情绪，text:65）→ 计入断言组，见 3-diff 错-1 |
| 4 | Amy 讲降神会/霍雷肖/罗盘四方位点/160 年（[3429, 4280]，text:89） | 是。中文理解逐项对上：降神会→誊本→「博物馆要纪念的那个人」→四栋房子→修道院→异教神庙→罗盘四正方位点→nexus→160 年前的传闻 | 主语＝Amy（讲的人）✓；「Benedict told **Caius**」的受事是 Caius，md 写「Amy 转述本尼迪克的说法」✓未误标成 Benedict 在场；「these houses were rented, or purchased in Horatio's case」的方向＝霍雷肖那栋是买、其余是租 ✓ | **对应**（为什么这样写的「作案动机」说法与本块引语及同块读者视角提示不一致，见错-6） |
| 5 | Amy 讲动机/日记/指纹/直播（[4381, 5350]，text:95） | 是。中文理解逐项对上：动机由私生活转向日记→第二十二号日记是研究所唯一缺件→只有誊本→「安米知道那栋楼里每个抽屉她都翻过」→Willow 说因「古怪的性内容」被锁→封了几十年的地下室门上残缺指纹查不出→Benedict 不可靠→Jimmy Jones 直播里从楼梯区域出来的窃贼→「有人在搜地下室」 | 主语＝Amy ✓；「Caius thought that wasn't a coincidence」的主语＝Caius（md 写「Caius 认为」✓ 未安到 Amy 头上）；「someone is searching the basements」= 未知者（md 保留未指认 ✓） | **对应**（施事全部正确） |
| 6 | Matt 的「三件事」（[6734, 7553]，text:129） | 是。中文理解逐条对上：① 贬称说祖父／不知 Caius 出身；② 被停职、记笔记、整份卷宗、已举报两次无下文；③ 第一周见 Billy 从车钥匙吸古柯碱、被骂并被威胁；末了「别再叫 DI Fauntleroy、尊重 Amy、因为她是人」+ Matt 上车 | 主语＝Matt（第一人称叙述者）✓；受事＝Billy（被打、被举报的人）✓；「He’d already reported him twice」＝Caius 举报 Billy ✓（md 作「此前已经举报过两次」✓）；「He called me a 'chink'」＝Billy 对 Matt（不是对 Caius）✓ | **对应**（引语非逐字：漏右单引号，见错-2；另「骂了他一句」降级辱称，见错-4） |
| 7 | 深处传上来的问话（[8410, 8538]，text:142） | 是。中文理解＝水晶球／桌上塔罗牌／「那是一只手吗」；为什么这样写＝用一句从深处传上来的问话收尾、说话人自己也没认出那是什么 | 说话人＝法医中的一位（原文 `their voice`，性别未指认）✓ md 未误标性别；受事＝地下室里的物件 ✓ | **对应** |

**小结**：7/7 块「中文在讲这句引语」，无引语选短、无跑题、无密度不足；块 3/4/6 的问题落在**断言组**（原文矛盾 / 引语非逐字），不计入对应失分。
