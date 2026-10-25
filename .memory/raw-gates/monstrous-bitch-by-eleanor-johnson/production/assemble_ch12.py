#!/usr/bin/env python3
"""Assemble the ch12 md: splice corrected 选择性精读 / 词汇分级 / 结构列表 into the file.

All quotes come from ch12-quotes.json (built by slicing the source text).
"""
from __future__ import annotations

import json
import re
from pathlib import Path

BASE = Path("/Users/jcxs2014/Documents/Works/EnglishRead")
PROD = BASE / ".memory/raw-gates/monstrous-bitch-by-eleanor-johnson/production"
MD = BASE / "notes/books/non-fiction/monstrous-bitch-by-eleanor-johnson/ch12 10 monstrous bitches bite back.md"
TXT = BASE / "notes/books/non-fiction/monstrous-bitch-by-eleanor-johnson/text/ch12_10_monstrous_bitches_bite_back.txt"

quotes = json.loads((PROD / "ch12-quotes.json").read_text(encoding="utf-8"))
text = TXT.read_text(encoding="utf-8")

# ── per-quote analysis, keyed 1..15 ──────────────────────────────────────────
ANALYSIS: dict[int, dict[str, str]] = {
1: dict(
 zh="作者先写两个哥特女孩在玩：玩吸血鬼、玩杀人、玩夜里的生物、玩女巫；然后点破她们真正在扮演的，是自己文化史里那些怪物母狗。转折落在最后一句——很快这就不再是游戏了。",
 st="首句是四个以「playing at」开头的分词短语并置，主语一个也没有换；第二句用「They are playing at being」重复同一个框架，把「扮演」的内容从具体身份换成文化史里的原型；末句用「But pretty soon, it won’t be a game anymore」把四个平铺的分词短语一下收成单句判断。",
 kw="`playing at vampirism`、`who populate their cultural history`、`being creatures of the night`、`be a game anymore`",
 way="同一句式连排四次，像小女孩数数一样把「玩」的内容一层层加码；作者不写她们后来怎样，只用一个转折句宣布游戏结束，把血淋淋的后文留在读者自己的想象里。",
 why="全章要论证的第一个前提是「怪物母狗是一种可传承的文化形象，而不只是银幕上的孤立类型」。把两个女孩的扮演行为直接接到「她们文化史里」那些原型上，血统与文化的连续性就先立住了。"),
2: dict(
 zh="回家路上，一个巨大的犬状生物开始追她们；她们差点脱身，金杰却被那东西咬了一口。作者说这事很糟，因为金杰恰好刚来初经，月经与疯狂的狗咬凑在一起，可是坏消息。",
 st="首句主谓宾加「starts pursuing」的动作推进；第二句用「They almost get away, but」把逃脱与被咬压进一个转折；末句以「This is a bummer, because」引出原因，再用「and」把两个本不相干的事实并置成因果。",
 kw="`a massive doglike creature`、`gets bitten by the thing`、`the combination of menstruation`、`her first period`",
 way="作者用「whatever it is」和「This is a bummer」这类轻佻的口语，把一次改变一生的咬伤写得像青春片里的麻烦事；「初经」与「狗咬」本是两套完全不同的语汇，被一只「and」拴在一起时，读者会自己感到那种生理与神话同时降临的荒诞。",
 why="作者要让读者明白，《姜饼人》里金杰的怪不是被谁造出来的，而是从「她成为女人」这一刻起自动发生的事；少女成人与怪物出生必须是同一个事件，月经和咬伤才有资格并排写。"),
3: dict(
 zh="作者说，就像《狼人女尸》一样：杀不死她体内的怪物母狗，哪怕你杀掉她的某一次化身。她会一次又一次地回来，在时间中反复出现，去勾引、去强奸、饮血、杀年轻人、说出那些既淫荡又贪婪的话，并在身后留下尸体。父权永远不会从她那里得到安全。",
 st="首句是「As in X, so here」的类比引子加一个「You can’t … even if …」的让步结构；次句用「She’ll come back again and again, throughout time」作主句，动词后面挂一串不定式，六个动作并排落下；末句是一个极短的独立判断句，把前面的清单收成一个结论。",
 kw="`kill the Monstrous Bitch within`、`one particular instantiation of her`、`come back again and again`、`Patriarchy will never be safe`",
 way="六个动词不定式没有主语、没有连接词，读起来像一份清单，也像一份供状；末句短到只有五个词，与前面绵长的威胁形成落差，把「不死」这件事压成一句冷静的断言。",
 why="本章的转折点在这两句之间——同样的断言，在上一部《狼人女尸》里是恐怖片式的绝望，在这里却是作者第一次说「这值得庆祝」的前提。先把「杀不死」钉死，后面那个令人意外的乐观才有立足处。"),
4: dict(
 zh="作者说，乐队男生这么干，是因为他们想让自己的乐队红遍国际，他们相信把詹妮弗献给恶魔附身就能如愿。那场附身仪式不过是轮奸的薄纱伪装；而这桩轮奸式的附身落到詹妮弗身上，把她变成一个恶魔般性感的、吃人的狼女吸血鬼。",
 st="首句用「because」和「they believe that」两重原因把动机拆开，第二个原因本身是一个宾语从句；次句用分号连接判断与结果，冒号后再用同位语「for Jennifer」限定承受者；末句是一个系表结构，主语是「the result of this rape-possession」，系动词之后接一连串形容词。",
 kw="`offering Jennifer up`、`the possession ritual`、`veiled allegory for gang rape`、`a demonically sexy vampiress`",
 way="「薄纱伪装」这个比喻把一桩暴行的包装纸直接点破；而结果句里三个身份（性感吸血鬼、食人者、狼女）连成一串，中间隔一个连字符，像在说同一具身体的三种叫法。",
 why="本节要论证的核心是「她不是生来就被造好的，而是被造的」；因此作者必须先把这群男生写得有明确动机、有可指认的行为，再把仪式翻译成它真正的样子，读者才会接受「怪物母狗可以被指认到具体的施暴者」这个判断。"),
5: dict(
 zh="作者用一句极短的感叹收束这一段的对照：现在这件事有意思了。詹妮弗作为怪物母狗的来历，是一场被写成恶魔附身的轮奸；妮迪的来历却既不是强奸也不是恶魔附体，而是女性之间的怪物传染。",
 st="首句是无主语系表结构加形容词，只有五个词；第二句的主语是「Jennifer’s origin story as a Monstrous Bitch」，表语是名词短语，末尾以过去分词短语「framed as demonic possession」作后置定语；第三句用「isn’t about … — it’s about …」的破折号对照，把「不是」与「而是」压进一句话。",
 kw="`Now this is interesting`、`framed as demonic possession`、`about rape or demonic possession`、`monstrous contagion between women`",
 way="作者在长对句之前先放一句五词的短感叹，像替读者换了一口气；而「附体」与「传染」被他当成两种不同的传承语法来分辨：一个是外来的、有仪式的中断，一个是内生的、在人与人之间流动的东西。",
 why="本节要证明的是：怪物母狗的来源不止一种，除了被仪式附体（那正是原书第 8 章处理过的机制），还有女性之间的直接传染；不把这两者分开，就无法说明为什么妮迪必须被写成与詹妮弗不同的一类。"),
6: dict(
 zh="作者说，于是这一对成了二十一世纪的劳拉与卡米拉，被血与禁忌之爱绑在一起。但《卡米拉》里的劳拉逃过了吸血鬼转化，被她生命里的男人们「救」了下来；而詹妮弗嘴里那一点点混进妮迪体内的唾液，就足以永远改变妮迪。",
 st="首句是系表结构加两个后置定语（由血与禁忌之爱捆绑）；次句用「But whereas …, …」的长对照结构，前半是旧故事里的例外结局，后半用「this little bit of saliva that gets into …」的关系从句收在「enough to change … forever」上。",
 kw="`the Laura and Carmilla`、`bound by blood and forbidden`、`escapes conversion to vampirism`、`this little bit of saliva`",
 way="作者用「这点口水」这样日常到近乎轻佻的说法，去对比旧传奇里改变命运的那一吻；两个时代的人文学名被并排放着，而「被男人们救下」与「被一点点唾液永远改变」之间的落差，就是两代恐怖故事的差别。",
 why="劳拉与卡米拉这条线正是原书第 6 章处理过的吸血鬼谱系，把它接过来，本章的「新传承」才有旧传承作对照；而用劳拉的结局做反例，说明这一次传染不再给男人留出拯救的位置，回咬的权力不再经过男性。"),
7: dict(
 zh="作者说，这是一部这样的电影：借用现代术语来说，食人是在女性儿童身上与性别连锁的常染色体显性遗传性状，只要一次轻微的环境伤害就能把它触发、唤醒那个病理过程。它既是遗传的，也是环境的。",
 st="首句是「This is a film in which」开头的主句，主语是「cannibalism」，后面两个破折号插入「借用现代术语来说」的口径说明；定语从句「which only has to be triggered by …」用不定式短语说明触发机制；末句是两个形容词并列的独立小句。",
 kw="`a sex-linked, autosomal-dominant trait`、`to use modern terminology`、`to awaken the pathological process`、`It is inherited and environmental`",
 way="作者把一部恐怖片直接套进遗传学的句式里，用「常染色体显性」「与性别连锁」这些术语给一个青春片式的暴食行为发了一张病历；而末句那六个词，把整部电影的病理学浓缩成两个词。",
 why="《生肉》是本章最需要被精细解读的一部——如果只说「怪物母狗是被父权造出来的」，就丢掉了遗传这一半；作者用医学口径把两半都保住，才好在下文推出「生与咬的双重性」这个关键概念。"),
8: dict(
 zh="作者先说一方面：在这部片子里，怪物母狗的怪性靠一条母系继承的路径取得，怪性被理解成先天的、烤进女人天性里的东西，是她从母亲那里传下来的本质性格。这与占支配地位的父权所主张的怪物母狗理论一脉相承，可以一直上溯到提亚马特、莉莉丝与拉米亚。这些母狗生下来就坏，因为她们的妈妈坏。",
 st="首句以「On the one hand」起头，介词短语后接主句与分号后的同位解释；次句是主语加系动词加三个并置的同位语（innate、baked into a woman’s nature、her essential character），其中后两个用逗号连缀；第三句是判断句加三个专名并列的状语；末句是「主系补」加一个 because 原因从句。",
 kw="`a matrilinear process of inheritance`、`baked into a woman’s nature`、`back to Tiamat and Lilith`、`born bad, because their mommies`",
 way="作者用「烤进天性」这个烹饪比喻把抽象的遗传写成一件已经发生的事；末句故意用最口语、最不学术的腔调写成，像一句母亲骂女儿的话，而这句民间说法恰恰就是父权用来解释女人的那套理论本身。",
 why="作者要先把父权那一侧的立场完整复述出来——生来就坏、有母系根源、能上溯到提亚马特——只有把这一侧摆足，下一段「另一方面」的反转才有分量：她要证明这套理论同时也是父权用来为暴行开路的说法。"),
9: dict(
 zh="作者接着说，但这位导演同时也在说：怪物母狗也是父权强制侵入女性身体造成的，那个父权秩序想把东西塞进她体内——阴茎、婴儿、食物——而她不想要。导演借着她那食人女主角贾丝汀，不再受这一套摆布了。贾丝汀要狠狠咬回去。",
 st="首句用「But she’s also saying」承接上文的「另一方面」，主干是「Monstrous Bitchery is caused by …」，主语与系动词之间插入一个较长的同位语；破折号内是三个并列名词，把「往身体里塞东西」具体化；次句是「And」引导的判断句，主语带一个后置介词短语；末句是极短的主谓结构加一个程度副词。",
 kw="`forcible violation of women’s bodies`、`put things in her`、`penises, babies, food`、`going to bite back hard`",
 way="作者把「阴茎、婴儿、食物」三个词并排放在破折号里，它们分属性、生育与饮食三个领域，却都是「被塞进她体内」；末句把「狠狠咬回去」写得短促而决绝，与前面长句的铺陈形成节奏落差，也正好让全片最响的那句话落在她自己的嘴里。",
 why="全章标题里的「回咬」在这一段第一次被明确说出，而作者要读者相信「回咬」是正当的回应；因此她必须先把被塞进女性身体的三样东西摆出来，让「强制」这个性质无法被否认，咬回去才不是失控而是回应。"),
10: dict(
 zh="作者写威廉的所作所为：他全然不顾妻子与四个孩子的安危与意愿，只喊了一声「凯瑟琳」，像唤狗一样把妻子叫到自己身边。他根本没有对孩子说话，也没有安抚他们说自己有什么计划、什么打算，甚至没有任何最基本的生存资源。",
 st="首句是前置状语「With no thought to …」加主句，主句里夹一个插入的直接引语，再接一个分词短语「beckoning … like a dog」作伴随状语；次句是并列否定结构「He doesn’t … nor does he …」，第二个分句用倒装，并以三个并列的名词短语收在「for their survival」上。",
 kw="`to the physical safety`、`his wife to his side`、`like a dog`、`nor does he reassure them`",
 way="作者把「像唤狗一样」这个比喻放在一个具体的动作细节上，而不是概括地说他态度恶劣；「连生存的基本资源都没有」这一句把一个宗教狂信者的傲慢落到柴米油盐上，反讽因此比形容词更有力。",
 why="《女巫》里的怪物母狗不是天生的，她是靠着一个暴君父亲一手造出来的；因此父亲的形象必须先被写成一家之主的绝对意志，「她被造出来」的机制才立得住。"),
11: dict(
 zh="作者说，但这部电影偏要绕道去说明一件事：林中的那个女巫——那个邪恶的森林女巫——她的权柄与力量，是直接由她身旁那位掠夺、虐待、控制一切的父亲威廉给她的。",
 st="主句是「this magnificent film is going to go out of its way to show how …」这一复杂宾语结构；how 引导的宾语从句里含一个插入语「the wicked witch of the woods」用破折号夹住；「is given power and authority directly by …」是被动语态，介词短语 by 引出施动者。",
 kw="`is given power and authority`、`by her adjacency to`、`predatory, abusive, controlling patriarch`、`wicked witch of the woods`",
 way="「going to go out of its way to」带着一股不甘心的强调，仿佛作者在说这部佳片偏偏要花力气去证明一件大家爱听的事；而「由她的靠近直接赋予」这个被动结构，把权力写成从旁边那个男人身上传导过来的。",
 why="作者全章的题目是「怪物母狗回咬」，但在《女巫》里她要先把「谁给了女巫权力」这件事说清楚；女巫的权柄来自父亲的暴行，她才不是一个天生邪恶的形象，回咬也就不是天性的发作而是被造成者的反抗。"),
12: dict(
 zh="作者说，在这部电影里，托马斯汀从父权的受害者变成了它的对手。甚至在她超拔地变成怪物母狗的那一刻，影片也仍然把她立为我们的英雄。事实上，正是她超拔地变成怪物母狗，才让她最终被立为我们的女英雄。",
 st="首句用「goes from being … to being …」这一平行结构，两个 being 后面各接一个名词性成分；次句是一个让步句，主句前有「Even in the moment of …」的时间状语，句末用「nevertheless」收束；末句用「Actually」起头作强调，并把两个分词短语（by her transcendent transformation / into a Monstrous Bitch）拆到介词前后。",
 kw="`goes from being a victim`、`her transcendent transformation`、`as our hero`、`as our heroine`",
 way="作者在同一条引文里先用「our hero」，再用一句「Actually」自我更正为「our heroine」；而那个 by 结构把「正是变成怪物母狗」写成她被立为女英雄的原因，转变因此不是代价而是资格。",
 why="这一段是全章论点的缩影：作者要论证的从来不是「怪物母狗变得更可怕了」，而是「观众站到了她那边」；把英雄与女英雄的措辞差别点出来，就说明她的转变在叙事结构上换来了什么。"),
13: dict(
 zh="作者说，瓜达尼诺看出原版《地狱变型》里「不死母亲」这个设定是一块纯粹由怪物母狗矿石铸成的金子，于是他顺着它跑；办法之一是造出一条与舞校巫群并行的叙事线。",
 st="首句是主句加两个并列的谓语（is a nugget of … and runs with it），主语是一个内嵌的直接引语「the undead mother」；次句以「He does this」作主句，用「in part by creating a parallel narrative」这一介词短语交代做法，末尾再以「alongside the dance school coven」点明并行的那一条线。",
 kw="`the undead mother`、`of pure Monstrous Bitch gold`、`creating a parallel narrative`",
 way="「一块纯粹的金子」把一个鬼故事设定说成矿脉，读者的注意力立刻从「拍得漂不漂亮」转到「这个设定值多少钱」；「顺着它跑」这个说法把导演的选择写成猎人的发现，敬意与功利同时在场。",
 why="作者在介绍《地狱变型》时要把新片与 1977 年原版区分开，而区分点不在拍摄风格上，在「哪一块设定被当真当成宝」；这一句先立住取舍，后面「敌人从父权换成母权」的整段判断才有依据。"),
14: dict(
 zh="作者说，影片结尾的情绪与其说是安慰，不如说是醒来、进入一种新的意识；但它也不是欢笑、不是轻松、不是任何一种浅表的安宁。瓜达尼诺没有退回安慰的领域。新的世界秩序可以女权得骇人，但这不代表它会舒适。",
 st="首句用「It’s more one of A, B, but it’s not one of C, D, or E」的正反对照；次句是单句否定加一个补语「in his film」；末句用 may … but … 的让步结构，主句是「may be feminist as all hell」，让步从句是「that doesn’t mean it’s going to be cozy」。",
 kw="`coming to a new consciousness`、`doesn’t retreat into the realm`、`be feminist as all hell`、`it’s going to be cozy`",
 way="作者用「as all hell」这种带刺的夸张去形容女权，又用「cozy」这样家常的词去否定它，两者一推一拉，把「未来是女性的」这句口号拆掉了温情的部分；「不安慰」这个判断干脆写成导演不肯退回去的立场。",
 why="全章最容易被读成单纯的乐观收尾，作者要在这里给读者一个刹车：她欢迎怪物母狗成为女英雄，却不认为新世界会因此变得舒适；这份保留才是她对当下这批影片既欣赏又不轻信的立场。"),
15: dict(
 zh="作者说，在不同程度的程度上，这在《姜饼人》《生肉》《地狱变型》《女巫》和《詹妮弗的身体》里都是真的。但确实有什么东西变了，因为在所有这些影片中，怪物母狗是主角，而且越来越是女英雄。",
 st="首句是一个主语带后置定语的判断句，五个片名以逗号并列；次句用「But something really has shifted, because」引出结论，because 后面接一个介词短语开头的从句，主句谓语是系动词加表语，表语本身又由「the protagonist and, increasingly, the heroine」并列而成。",
 kw="`To varying degrees, that’s true`、`something really has shifted`、`is the protagonist`、`increasingly, the heroine`",
 way="五个片名被排成一列，像交名单；「在不同程度上」先给读者留出余地，随后那句「但确实有什么变了」用一个副词和一个短促的完成时把话收住，结论的分量全压在「主角」与「女英雄」这两个词上。",
 why="本章要把五部影片的共同结论一次性交出来，而用「主角」与「女英雄」的递进说明这不是一步到位的翻转；把判断的重心放在叙事位置而不是角色善恶上，才与前面五节的分析接得上。"),
}

# ── structure list (12–22 items) ────────────────────────────────────────────
STRUCT = """### 结构列表

1. **二十一世纪开场的少女游戏**：《姜饼人》（2000）里两个女孩扮演吸血鬼、扮演女巫，作者说她们正在扮演自己文化史里的怪物母狗。
2. **咬与初经**：狗状生物咬了金杰一口，恰好撞上她的初经来潮，狼化、性欲爆涨、食人、暴戾四件事同时启动。
3. **狗的世系**：作者把金杰接回拉玛什图的狗头、菲洛斯特拉图斯的莫耳摩耳克、卡尼狄亚名字里的拉丁语「canis」，说她的「啮齿」正在朝四周的父权世界回咬。
4. **三重症状**：性欲、食人、暴戾三件套，加上血一样的感染路径，狼人病在片中是血源性、可传染的病原体。
5. **可治而不愿治**：布里吉特做出解药，金杰却像《吸血鬼舞女》里的弗兰与米里亚姆那样玩得正开心，故事在乱斗中以金杰之死收场。
6. **被驯服进地底**：《姜饼人：解除封印》（2004）里布里吉特被关进地下室当宠物，命运像复仇女神被驯服后打入地下。
7. **转世的前传**：《姜饼人：回到开端》（2004）把两人放到十九世纪初的加拿大，让她们血里注定成为狼人，世世代代结伴。
8. **杀不死的断言与第一次值得庆祝的永恒回归**：「你杀不死她体内的怪物母狗」，而这一回，怪物母狗的反复归来第一次开始像一件值得庆祝的事。
9. **轮奸的薄纱伪装**：《詹妮弗的身体》（2009）里乐队下药把詹妮弗献给撒旦仪式，作者说那场仪式不过是轮奸的伪装。
10. **被制造而非生来**：「詹妮弗是被一个想利用她身体牟利的父权秩序造出来的怪物母狗，她不是生来就是。」作者把影片接回 1970 年代与地中海。
11. **女性之间的怪物传染**：妮迪不是被附体而是被咬伤，她的来历落在酒神、吸血鬼、狼人传统而非附体传统，于是这一对成了二十一世纪的劳拉与卡米拉。
12. **食人作为遗传性状**：《生肉》（2016）里食人既是与性别连锁的常染色体显性遗传性状，又只需一次轻微环境外伤就能触发，遗传与环境两者兼具。
13. **生与咬的双重性**：作者点出母亲、莉莉丝、拉米亚的「生下来就坏」的谱系，同时坚持怪物母狗也是父权强制往女性身体里塞东西造成的。
14. **悲剧而非凯旋**：结局里贾丝汀咬掉男生嘴唇，姐姐阿莱克西亚谋杀并吃掉阿德里安，母亲在暴虐婚姻中吃掉父亲的肉，作者明说「她的命运更接近悲剧而不是胜利」。
15. **殖民地美洲的埃里克托**：《女巫》（2016）里森林老巫被作者判定为埃里克托式的厌女原型。
16. **像唤狗一样唤妻子**：威廉喊一声「凯瑟琳」就把妻子叫到身边，如同作者点出的卡尼狄亚、狗头拉玛什图与拉米亚的谱系。
17. **把女儿当牲口**：威廉与凯瑟琳商量把托马斯汀租出去换钱，把她当成可以出租的牲口。
18. **上升而不是堕落**：托马斯汀立约撒旦、随裸身女巫群升空，作者说这段「下降」根本不是下降，「而是一次上升——字面意义上的上升」。
19. **只招募年轻女性**：巫群明明可以收下全家七口，却只挑托马斯汀；巫群中没有一个男巫。
20. **当代寓言与新朋友**：托马斯汀从受害者变成对手，影片由此把她立为女英雄；她不再是孤例，她有一个叫苏西·班尼恩的朋友。
21. **敌人从父权换成母权**：《地狱变型》（2018）里不死不活的母亲们不肯死，影片的敌人变成一个要奴役年轻女性的母权。
22. **千面英雄的性别改写与不舒适的自由**：坎贝尔的原型是儿子必须弑父才能成人，本片改写成女儿必须让所有母亲死去；而新的世界秩序「可以女权得骇人，但不代表它会舒适」，怪物母狗最终成为主角与女英雄。"""

# ── vocab tiers (headword, meaning, example) ────────────────────────────────
VOCAB = {
 "高级": [
  ("mormolyke", "莫耳摩耳克，古代传说中的能化狼的巫妖", "And remember that Lamia is described by Philostratus as a mormolyke, or werewolf."),
  ("lycanthropy", "变狼妄想症；化狼状态", "Horrified by what her sister has become, Brigitte develops a cure for Ginger’s lycanthropy."),
  ("succubus", "女魅魔，诱惑男性并在梦中与之结合的恶魔", "Perplexed by Jennifer’s sudden monsterification, Needy does some research and finds out in the occult section of the library that Jennifer is, technically, a succubus."),
  ("matrilinear", "母系（的），经母亲一线传承的", "On the one hand, Monstrous Bitches in Raw come by their monstrosity through a matrilinear process of inheritance; monstrosity is understood to be innate, baked into a woman’s nature, her essential character as it descends to her from her mother."),
  ("autosomal-dominant", "常染色体显性的", "This is a film in which—to use modern terminology—cannibalism is a sex-linked, autosomal-dominant trait in female children, which only has to be triggered by a mild environmental injury in order to awaken the pathological process."),
  ("Erichtho", "埃里克托，希腊神话中驱使亡魂与恶犬的女巫", "Like Lamashtu, Erichtho, Canidia, lamiae, and vampiresses, she is now a Monstrous Bitch who eats human flesh."),
  ("Bacchanalian", "酒神节的；像酒神崇拜那样狂乱的", "So there’s something more than a little Bacchanalian at work in this dance."),
  ("indomitability", "不屈不挠；无法被驯服或消灭的品格", "That dynamic of celebrating the indomitability of the Monstrous Bitch will get turned way, way up as the 2000s wend their way forward."),
  ("Alecto", "阿勒克托，希腊神话中的复仇女神之一", "Her order heralds a return to the Bacchanal, to a world ruled by Alecto and Erichtho, rather than by patriarchs and matriarchs who want only to control young women."),
 ],
 "进阶": [
  ("patriarchal", "父权的；属于父系家长制的", "Patriarchal Katherine is murdered by her own daughter."),
  ("monstrosity", "怪性；异常凶恶的形态", "Her monstrosity includes all the usual elements: First, she is a sexual predator."),
  ("sapphic", "女同性恋的；与萨福式的爱相关的", "Of course, Justine and her sister and mother aren’t just riffing on Dorothy and Debbie; they are also like Lilith and the liliths, Lamia and the lamiae, or any number of the sexy sapphic vampires out there—though their “offspring” are born of a bite, rather than through childbirth."),
  ("forcible", "强制的；暴力的", "But it is similar in that it is a forcible introduction of flesh into an orifice of her body that she doesn’t want to receive that flesh."),
  ("allegory", "寓言；象征性的叙事", "The possession ritual is a barely veiled allegory for gang rape; the result of this rape-possession, for Jennifer, is that she is turned into a demonically sexy vampiress cannibal wolf-woman."),
  ("dehumanizing", "去人化的；剥夺人性的", "Mother Markos sees in Susie only a vessel for her own rebirth; in both cases, there is a poisonous, dehumanizing maternal controllingness at work."),
  ("seductive", "诱惑的；勾引人的", "Thomasin is, in her mother’s eyes, a lamia, a seductive, spellcasting witch who murders babies and children for their blood."),
  ("monstrous contagion", "怪物传染；在人与人之间传递的怪性", "Needy’s Monstrous Bitch origin isn’t about rape or demonic possession—it’s about monstrous contagion between women."),
  ("possession ritual", "附身仪式", "The possession ritual is a barely veiled allegory for gang rape; the result of this rape-possession, for Jennifer, is that she is turned into a demonically sexy vampiress cannibal wolf-woman."),
  ("bloodborne", "血源性（的）；经血液传播的", "He soon becomes a werewolf, too, because in this film lycanthropy is a bloodborne, transmissible pathogen, much like vampirism, or like an STD."),
 ],
 "基础": [
  ("vampire", "吸血鬼", "That means that Needy’s form of Monstrous Bitchery—unlike Jennifer’s—is in the Bacchae/vampire/werewolf tradition, rather than the possession tradition."),
  ("cannibal", "食人者", "The most concerning symptom, it turns out, is that she has become an obligate cannibal."),
  ("monster", "怪物", "So this film seems to participate in the punish-the-monsters trajectory we’ve seen in cinema since the 1930s."),
  ("sisters", "姐妹", "Ginger Snaps centers on two sisters—Ginger and Brigitte—who are “goth girls” obsessed with death, the macabre, and the occult."),
  ("girl", "女孩", "The twins are not made into witches—not even the little girl, Mercy."),
  ("bite", "咬；叮咬", "Justine is going to bite back hard."),
  ("witch", "女巫", "Maybe it’s not so bad to be a witch."),
  ("blood", "血", "So clad, they look like stylized dead people, streaked with blood and mortally wan underneath."),
 ],
}

# ── build sections ─────────────────────────────────────────────────────────
blocks = []
for q in quotes:
    n = q["n"]
    a = ANALYSIS[n]
    blocks.append(
        f'> **原句 {n}:** "{q["text"]}"\n\n'
        f'**中文理解**：{a["zh"]}\n\n'
        f'**句子结构**：{a["st"]}\n\n'
        f'**关键词**：{a["kw"]}\n\n'
        f'**表达方式**：{a["way"]}\n\n'
        f'**为什么这样写**：{a["why"]}'
    )
sel = "## 选择性精读\n\n" + "\n\n".join(blocks)

voc = ["## 词汇分级"]
for tier, rows in VOCAB.items():
    stars = {"高级": "⭐⭐⭐", "进阶": "⭐⭐", "基础": "⭐"}[tier]
    voc.append(f"### {stars} {tier}\n")
    voc.append("| 词/短语 | 释义 | 原文例句 |")
    voc.append("|---|---|---|")
    for head, mean, ex in rows:
        voc.append(f"| {head} | {mean} | {ex} |")
    voc.append("")
vocab_sec = "\n".join(voc).rstrip() + "\n"

md = MD.read_text(encoding="utf-8")
md = re.sub(r"### 结构列表\n\n.*?(?=\n## 论证结构)", STRUCT, md, flags=re.S)
md = re.sub(r"## 选择性精读\n\n.*?(?=\n## 词汇分级)", sel + "\n", md, flags=re.S)
md = re.sub(r"## 词汇分级\n\n.*?(?=\n## 一句话总结)", vocab_sec + "\n", md, flags=re.S)
MD.write_text(md, encoding="utf-8")

# ── self checks ────────────────────────────────────────────────────────────
errs = []
for q in quotes:
    a = ANALYSIS[q["n"]]
    for k in re.findall(r"`([^`]+)`", a["kw"]):
        n_words = len(k.split())
        if not (3 <= n_words <= 5):
            errs.append(f"Q{q['n']} 关键词词数 {n_words}: {k}")
        if k not in q["text"]:
            errs.append(f"Q{q['n']} 关键词不在引语中: {k}")
    for fld in ("zh", "st", "way", "why"):
        if not re.search(r"[一-鿿]", a[fld]):
            errs.append(f"Q{q['n']} 字段无中文: {fld}")
    if "…" in q["text"] or "..." in q["text"]:
        errs.append(f"Q{q['n']} 含省略号")
    if re.search(r"[.!?]\d", q["text"]):
        errs.append(f"Q{q['n']} 含脚注号")
    if not (30 <= q["nwords"] <= 70):
        errs.append(f"Q{q['n']} 词数 {q['nwords']}")
for tier, rows in VOCAB.items():
    for head, mean, ex in rows:
        if head.lower() not in text.lower():
            errs.append(f"词条不在本章: {head}")
        if head.lower() not in ex.lower():
            errs.append(f"例句不含词头: {head}")
        if not ex.strip(" ."):
            errs.append(f"例句空: {head}")
        if re.search(r"[一-鿿]", ex):
            errs.append(f"例句含中文: {head}")
        if ex not in text:
            errs.append(f"例句非逐字: {head}")
if errs:
    for e in errs:
        print("ERROR:", e)
    raise SystemExit(1)
print(f"OK: md assembled; {len(quotes)} blocks; 结构列表 {len(re.findall(r'^\d+\. \*\*', STRUCT, re.M))} items; "
      f"vocab {sum(len(v) for v in VOCAB.values())} rows")
print("bytes:", MD.stat().st_size, "lines:", len(md.splitlines()))
