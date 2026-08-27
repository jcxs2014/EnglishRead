import os,re
BASE="notes/books/short-story-anthologies/Best British Short Stories 2023 by Nicholas Royle"
# (file, old_line_substring, new_line)
REPS=[
 # 01 Islands
 ("01 Islands.md","**one time**（Caribbean） | 从前","**one time** | 从前"),
 # 05 Somewhere Out There West of Thetford
 ("05 Somewhere Out There West of Thetford.md","**breach** | 违背；突破 | — |","**barbed-wire** | 带刺铁丝网 | Mrs Grote lived ... beneath the overhang of the elm trees. |"),
 ("05 Somewhere Out There West of Thetford.md","**debateable lands** | 争议之地","**Breckland** | 英格兰东部沼泽/荒野地带（诺福克-萨福克交界的荒凉区） | The wind chimes rattled constantly in the Breckland gales |"),
 # 08 Chimera
 ("08 Chimera.md","**lingerie** | 内衣（法语词，英语发音） | — |","**barman** | 调酒师 | The barman stood polishing a pint glass with a white tea-towel |"),
 # 10 The Thinker
 ("10 The Thinker.md","**grunt** | 咕哝声；发牢骚","**thinker** | 深思的人（本篇题眼，反讽）"),
 # 11 Middle Ground
 ("11 Middle Ground.md","flora/fauna | 植物群/动物群 | （本篇未出现）","**foreground** | 前景（艺术构图术语） | From here, the primrose was the whole foreground |"),
 ("11 Middle Ground.md","| **barefoot** | 光脚的 | （未出现在本篇） |","| **exposed** | 显露；揭开 | The light touched the girls' cheeks and exposed the down on them |"),
 # 12 Still Life
 ("12 Still Life.md","| method of loci | 记忆宫殿法","| **paramedics** | 急救医护人员 | The paramedics asked him what was wrong |"),
 ("12 Still Life.md","| unreliable narrator | 不可靠叙述者","| **laboured** | 吃力的；费劲的 | He explained in a laboured way that he was a taxi driver |"),
 ("12 Still Life.md","| receptionist | 接待员","| **pyjamas** | 睡衣（英式拼写） | I could see through the window a man in his pyjamas |"),
 # 13 When We Went Gallivanting
 ("13 When We Went Gallivanting.md","| surreality / surrealism | 超现实","| **hangovered** | 宿醉的 | Richie was scooping his hangovered behind out of an acquaintance's yard |"),
 ("13 When We Went Gallivanting.md","| carnivalesque | 嘉年华式的，颠覆性的 | （未出现） |","| **hysterically** | 歇斯底里地；夸张地 | Last night it had seemed hysterically funny getting up to Floor 29 |"),
 ("13 When We Went Gallivanting.md","| bathos | 突降法（高潮后的突然平淡）","| **concertina** | 手风琴（此处用作比喻：挤成一团） | like climbing a concertina |"),
 # 14 QX
 ("14 QX.md","| bibliomystery | 书痴文学（关于书籍的悬疑小说）","| **second-hand** | 二手的 | They had emerged from a large second-hand bookshop |"),
 ("14 QX.md","| invocation | 召唤，祈求","| **earnest** | 认真的；诚挚的 | An earnest couple were playing at chess at the next table |"),
 ("14 QX.md","| palimpsest | 羊皮纸手稿（刮去旧字重写新字） | （未出现） |","| **foraging** | 搜寻；觅食 | resting from the foraging that had occupied them for the last hour |"),
 ("14 QX.md","| bookplate | 藏书票 | （未出现） |","| **coffees** | 咖啡（此处作可数复数） | sipping at coffees in a corner of a nearby café |"),
 # 15 The Beard
 ("15 The Beard.md","| totalitarian aesthetic | 极权美学","| **shuffles** | 拖沓着走；蹒跚 | he shuffles in his cluster of thick, black, woollen robes |"),
 ("15 The Beard.md","| \"Down like dominoes\" — the totalitarian aesthetic of control. |","| thick, black, woollen **robes** | 厚重黑色羊毛长袍 | |"),
 # 16 The Slime Factory
 ("16 The Slime Factory.md","| eco-dystopia | 生态反乌托邦","| **promotional** | 宣传的；推广的 | The promotional video came out of the blue |"),
 ("16 The Slime Factory.md","| pastoral | 田园牧歌的 | Pastoral ideal of England. |","| **eccentric** | 古怪的；怪异的 | The eccentric billionaire had shut himself away inside his research complex |"),
 ("16 The Slime Factory.md","| technocratic | 技术官僚的 | Technocratic utopia. |","| **tubby** | 圆胖的（口语） | looking extraordinarily tubby |"),
 # 17 Bonsoir
 ("17 Bonsoir (after Ithell Colquhoun).md","| collage | 拼贴艺术 | Scissors and paste — the raw materials of collage. |","| **velvet** | 天鹅绒的 | on my door hangs a dark red velvet dress |"),
 ("17 Bonsoir (after Ithell Colquhoun).md","| cut-up technique | 截断拼贴技术 | Burroughs/Brion Gysin random cutting method. |","| **spell** | 咒语；魔咒（双关：既是念咒，也是写作本身） | until it becomes like a spell |"),
 ("17 Bonsoir (after Ithell Colquhoun).md","| occult | 神秘学 | Moon's only mansion — occult/astrological term. |","| **moon's only mansion** | 月亮唯一的宅邸（原文隐喻性短语，指月亮/夜晚本身） | powdered face, perfumed wrists, moon's only mansion, o sweet Andromeda |"),
 # 18 Common Ground
 ("18 Common Ground.md","| voyeurism | 窥视 | \"I've seen you in your garden.\" |","| **well-trimmed** | 修剪整齐的 | his neat silver hair and his well-trimmed moustache |"),
 ("18 Common Ground.md","| power dynamics | 权力动态 | The kettle and the coffee — hospitality as control. |","| **cardigan** | 开襟毛衣 | his buttoned-up cardigan and his hand, which, when she took it, was cool and dry |"),
 # 19 The Bull
 ("19 The Bull.md","| anamnesis | 记忆，追忆 | Memory as anamnesis — the past surfaces unbidden. |","| **bridleway** | 徒步与骑马两用道（英式道路分类） | I pulled in before the bridleway and walked to the lookout |"),
 ("19 The Bull.md","| palimpsest | 羊皮纸手稿 | The landscape as palimpsest — old and new overlaid. |","| **embankment** | 堤坝；河岸 | just an old man crossing the embankment |"),
 ("19 The Bull.md","| epitaph | 墓志铭 | （未出现） |","| **bracken-clad** | 蕨草覆盖的 | the wind plait myriad reflections of the bracken-clad hills |"),
]
for fn,old,new in REPS:
    p=os.path.join(BASE,fn)
    md=open(p).read()
    if old not in md:
        print('NOT FOUND',fn,'::',old[:60])
        continue
    md=md.replace(old,new,1)
    open(p,'w').write(md)
    print('OK',fn)
