# R4 判定表 · ch02（修复后 11 块）

机器层（2-machine.json，修复后刷新）：verdict=ok，11 块引语逐字全过（R0 全书 161/161、250 片段 0 MISS）。

施事三问逐块：
- 块1 "we scared one another with water monster stories...no one went into the night lake alone"——主语=we（少年团体）✓；md「我们还在湖边用水怪故事互相吓唬」「没人敢独自走进夜里的湖」✓。
- 块2 "Lake Superior now became a graveyard to gilt-edged furniture"——施动=Lake Superior、受事=家具/收藏/面孔，md「变成了一座坟场——里面是镀金家具…」✓。
- 块3 "Mishibizhii walked slowly from the mythic caverns"——主语=Mishibizhii ✓；"One was foreshortened, perhaps broken in battle"——one=尖刺之一，md「其中一根短了一截，也许是在战斗中折断的」✓。
- 块4 省略号块："Two women of the tribe…danced. … Then suddenly the animal flicked his head and a single sharp horn pierced the soft flesh of Lu's belly."——两片段独立取证命中（verify_fragments_indep 0 MISS）✓；施动=animal/角、受事=Lu ✓。
- 块5 "The next few minutes are gone from my memory...in the hand that had held the pistol was a medicine bag"——置换方向 枪→药袋，md 同向 ✓；"It had the mark of a makwa manidoo"——mark 属于药袋 ✓。
- 块6 "Cloth strips that bound his leg at knee level bore the mark of dried blood"——受事=Ziib 的腿，md「绑在他膝盖处的布条上带着干涸的血迹」✓；"Me Tarzan. You see, Jane?" 说话人=Ziib ✓。
- 块7（新增）"Uncle Jon's screams of pain rose like dust in his wake. Then they stopped. He began singing his death song"——screams 的属主=Uncle Jon、singing 的主语=He（Uncle Jon）✓；md「惨叫声像扬尘一样升起来又戛然而止——他开始唱起死亡之歌」✓。
- 块8 说话人=Mikwam（"she said...she commanded"），md「母亲说…她命令道」✓；"I could bear a child"——主语=她（Mikwam）✓。
- 块9 "my mother asking the tribal leaders to let her become an adulteress"——请求者=母亲、被请求者=部落首领，md「我的母亲正在请求部落首领允许她成为一个通奸者」方向一致 ✓。
- 块10 "You who hear this story know a truth"——对读者喊话，md「听这个故事的人，你们知道…」✓；"Who should sacrifice for whom?" 双问保留 ✓。
- 块11 "Monsters roam the earth; sometimes they live inside us"——两个并列短句，md「怪物在大地上游荡；有时它们就活在我们心里」✓。

数字/唯一/第一次逐条回原文：
- 「每四十年」未入块（在 ch16）；本章数字类：$15,000 与 $50,000/day 未入块（R1#3 提示，见 3-diff）
- 块3「无数个纪元」← "Eons streamed by" ✓
- 分析层「唯一/第一次」扫描：块4 分析「全篇两次正面死亡（Lu 与 Uncle Jon）」——可数断言，回原文：Lu 死（text:76 段）与 Uncle Jon 死（text:187 段）确为仅有的两处 on-screen 死亡，另有过路船只发现溺死（叔叔式背景死）不计「正面」✓ 成立

覆盖声明：R1 全部 8 条中 7 条有块覆盖（1 条为陷阱熏鱼细节，提示不修）；md 11 块与 R1 无矛盾；阻断 1 条已当场修复并复验。

## 已核实为正确

- 块2 中文「苏必利尔湖曾经吞没埃德蒙·菲茨杰拉德号那样的船并守住秘密」——text:40 段 "Just as it had swallowed ships like the Edmund Fitzgerald and kept their secrets" ✓。
- 块5 中文「原本握着手枪的那只手里，是一只用皮革做的小药袋」——text:124 段 "in the hand that had held the pistol was a medicine bag" ✓（置换写法看似反常，实为原文原样）。
- 块8 中文「屋里响起一片哗然」——text:256 段 "A roar went up in the room when she stated this flatly." ✓。
- 块10 中文「巨兽会喷吐、会骚扰」——text:289 段 "a misaabe can spit and harass" ✓。
- 导航「罗马数字分节」——原文 I.–VI. 节标 ✓。

**结论：断言 1 阻断（漏，已当场修复）/ 提示 1 / 假红 0 / 跳过 0。已核实为正确 5 条。**
