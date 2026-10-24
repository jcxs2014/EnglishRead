# ch32 richard — 判定表（R5）

- 原文 367 行 / 精读 131 行；机器层 `2-machine.json` rc=0（verdict=ok，8 块 8 段全逐字，零 issue）
- 报数四组：**逐字 8/8 通 · 对应 8/8 通 · 形态 通（H1 `32. Richard`／导航 5 条／子项四件齐）· 断言 漏 3 提示 · 编 0 · 错 0 阻断、3 提示**

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 亲属链：Richard 是 Henry 之父、Alba 的祖父（非外公） | `text/ch32_richard.txt:23` “I’m staying over at Grandpa’s apartment… I am lying in my dad’s bed in his old room.”；`:367` “I think about my father, climbing that tree” | 成立 | 已核实 |
| 亲属链：Annette 是 Richard 的亡妻、Henry 之母、Alba 的祖母，且**同一人** | `:52` “He could never bear to give away any of my grandmother’s clothing.”；`:79` ““Darling. Annette.” He’s mistaken me for my grandmother.”；`:268` “Annette is buried in Graceland Cemetery under a double-wide granite stone with Richard’s name already carved next to hers.” | 成立（「祖母＝亡妻」未拆成两人，「亡妻」也未误挂到 Clare 身上） | 已核实 |
| 亲属链：Kimy 是房东兼老友，不是亲属 | `:128` “Kimy lives downstairs; she is Grandpa’s landlady.”；`:218` “I’m eighteen years older than Richard” | 成立（md 用「房东金米」，未写成亲戚） | 已核实 |
| 乐器：同一夜的音乐是**提琴**，不是钢琴 | `:42` “Music; a violin; Brahms; my grandfather is playing.”；`:57` “holding his violin and bow”；`:110` “His violin is next to him, with the bow beside it.”；`/usr/bin/grep -nE "piano\|violin\|bow" text/ch32_richard.txt` → 5 条命中全为 violin/bow，**无 piano**，exit=0 | md 四处写「弹（琴）」，应为「拉／奏」 | 提示 |
| 块 5「祖父端坐在沙发上」与「头歪成不自然角度」相抵 | `:110` “Grandpa is sitting on the sofa. His head is at a weird angle and his hands are in his lap, palms up.” | 「端坐」加戏，应是「坐着」 | 提示 |
| 块 4 读者视角同一句意重复两次（「她还没说出那个词」×2） | 原文该段仅一处「未说破」：`:70-75`，`:75` 才说 “You’re having a stroke” | 编辑残留，建议删后一处 | 提示 |
| 克莱尔在密歇根看父亲这一前因未进 md | `:23` “Mama has gone to Michigan to see my other grandpa.” | 未收，导致「天亮后赶到」无来处 | 提示 |
| Kimy 大十八岁、Richard 住了五十年未进 md | `:218` “I’m eighteen years older than Richard, no way he would go first.”；`:242` “He was here fifty years.” | 未收，属取舍 | 提示 |
| 「你相信天堂吗」这一问未进 md | `:362` ““Do you believe in Heaven?” Alba asks me.”；`:367` “But I’m spared having to answer…” | 未收；消失一拍已在总结保留 | 提示 |
| 块 1「门被推开一点、有人站在那儿」未被写成「父亲/时间旅行者现身」 | `:29` “just as I might be asleep I think the door opens a little and someone is standing there, then they’re gone.” | 成立（md 明确留白：「谁站在门口，她没有说」） | 已核实 |
| 块 8「long before his death」的时间折叠未写反（不是死后追悼） | `:367` “I grieve him more, here on this random El platform on a random morning long before his death, than I ever knew I could.” | 成立 | 已核实 |
| 词汇表 13 条例句逐字 | `:323` acrophobic／`:153` perishable／`:52` olfactory／`:242` grotesquely／`:29` improvises／`:110` lopsided／`:133` paramedics／`:128` landlady／`:259` belongings／`:75` stroke·ambulance／`:105` bare feet／`:269` blank dates | 全部逐字命中 | 已核实 |

## 已核实为正确（防下一轮误修）

1. **「祖母」与「亡妻」是同一人，不是两个人**：`:52` 说「我祖母的衣服」，`:79` 他被认成的人叫 Annette、旁白点明 “mistaken me for my grandmother”，`:268` 墓碑上 Annette 与 Richard 同穴。⇒ 下一轮若见「祖母／亡妻并用」不得判矛盾。
2. **Kimy 不是继祖母**：她的身份逐字是 “Grandpa’s landlady”（`:128`，词汇表也收了这条），且 `:218` 自陈比 Richard 大十八岁。md 写「房东」正确。
3. **Richard 是父系祖父（Grandpa），不是外公**：`:23` 明写「睡在我爸的旧房间」，`:367` Henry 称「我父亲」。md 用「祖父」正确；密歇根那位才是「另一个祖父」（母系）。
4. **死的不是 Henry**：1982 段 Henry 活着并在站台上哀悼父亲（`:367` “long before his death”）；md 未把「哀悼」写成 Henry 已死。
5. 「琴就放在旁边，像刚放下」是 **Kimy 转述医生/现场的话**（`:167` “his violin was next to him like he had just put it down”），不是 Alba 说的。
6. 原文未交代 Annette 的死因与年份（只有 `:52` “forty-some years after she died”），md 亦未编造死因——**下一轮不得据外部设定补写**。
7. 机器层 rc=0 是真通过（`bash scripts/chapter.sh "…/ch32 richard.md" --json`，退出码 0，counts 全零）。
