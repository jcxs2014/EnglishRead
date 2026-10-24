# ch31 wild thing — 判定表（R5）

- 原文 412 行 / 精读 112 行；机器层 `2-machine.json` rc=0（verdict=ok，6 块 / 7 段全逐字，零 issue）
- 报数四组：**逐字 6/6 通 · 对应 6/6 通 · 形态 通（H1 `31. Wild Thing`／导航 5 条／子项四件齐）· 断言 漏 2 提示 · 编 0 · 错 0 阻断、1 提示**

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 块 1 引语逐字，且「从语气听出不对」这层未被写成「已经知道割胎」 | `text/ch31_wild_thing.txt:23` “Beck calls just as Alba’s violin lesson is ending. I’m gathering my things when my phone buzzes; I can tell by the way she says my name that Beck is upset.” | 成立 | 已核实 |
| 块 2 两句话分属原文相邻两行，未合并成一句假引语 | `:45` “When we finally arrive, I see Beck’s silver Jeep under the streetlight, alone in the parking lot, all the tires deflated.”；`:46` “Someone climbed the chain-link fence just to slash Beck’s tires.” | 成立 | 已核实 |
| 块 3「玻璃眼珠／剥皮尸体」两个意象都出自同一句，未拆分改写 | `:82` “Where there were camera lenses before, now there are eyelids, shutters with clumsily glued-on fake lashes… like a cadaver missing its skin.” | 成立 | 已核实 |
| 块 4 童谣的三段材料清单未被写错归属（男孩／女孩／Isadora） | `:158` “Little boys are made of snips and snails and puppy-dogs’ tails, little girls are made of sugar and spice and everything nice, and Isadora is made out of math.” | 成立 | 已核实 |
| 块 5「借房间回响把旋律叠在持续低音上」施事是 Alba | `:274` “I suddenly hear what she’s doing: the room is so resonant that she’s playing against the echoes, stacking melody on top of harmonic drones.” | 成立 | 已核实 |
| 块 6 以省略号跳句，未把跳掉的那句塞进引语 | `:412` “For now, I am happy, and the grief recedes. I try not to look back too much, or think too hard about the future. Sometimes I dream about Henry…”（跳过句在引号外） | 成立（省略号显式标注，机器层两段均 ok） | 已核实 |
| 导航与总结把 Alba 的演奏称作「即兴」 | `:283` “You improvised that? Wow.”；`:287` “That’s written music, but I couldn’t remember it very well so I kind of filled it in. It’s music from the notebooks at the Yellow House.” | Alba 当场更正为「有谱、记不全、自己补」，md 两处仍写「即兴」，且与同句「学来的」相抵 | 提示 |
| Alba 随行的缘由（Richard 有歌剧票）未进 md | `:44` “Richard has tickets to the opera tonight, so I take Alba with me.” | 未收，属交代性细节 | 提示 |
| 「Museum of Lost Souls」馆名与三座音乐库清单未进 md | `:339-342` “she has built a Museum of Lost Souls from real places, real libraries and museums… the British Museum, the Morgan, Stanford” | 未收；动机已由「馆藏／收藏者／策展人」传达 | 提示 |
| 词汇表 14 条例句逐字 | `:342` acquisitive／`:171` incorrigible／`:72` apprehensively／`:124` impassively／`:137` disinclined／`:45` deflated／`:82` clumsily／`:87` melodious／`:224` stricken／`:269` flat-eyed／`:364` umbrella／`:46` chain-link fence／`:68` artificial intelligence／`:60` violin case | 全部逐字命中 | 已核实 |
| 导航称「没有暴力场面」、威胁靠雨与空楼堆出 | `:55` “Tonight all I hear is the heating system.”；`:44` “It’s raining, the highway is slick, and traffic is backed up.” | 成立 | 已核实 |

## 已核实为正确（防下一轮误修）

1. 「伊莎多拉有了一对棕色玻璃眼珠」不是编的：`:82` “Isadora now has glass eyes, brown eyes that move randomly and then fix on us”。不得因「机器人不该有眼珠」删改。
2. 「我不是女孩，我是 wild thing」是 **Isadora 自称**，不是 Alba 说的；`:142` “Isadora says, “I’m not a girl. I’m a wild thing!””。块 4 上下文与导航均未错挂。
3. 「我的妈妈说我 incorrigible」是 **Alba 转述 Clare**，`:171`；“That’s a fine thing to be” 是 Isadora 的回应，未写成 Clare 自夸。
4. 索要黄房子的方向：**Isadora 要 Beck 弄来**（`:304` “You can get it for me?”），不是 Alba 提供、也不是 Clare 提供。
5. 「黄房子在 Alba 心里」是 **Beck 的话**（`:308` “The Yellow House is in Alba’s mind.”），导航未把它写成 Clare 的判断。
6. 「她将来会写的」是 **Clare 的预言**（`:369` “I think she will write it. Someday.”），不是 Beck 说的。
7. 机器层 rc=0 是真通过（`bash scripts/chapter.sh "…/ch31 wild thing.md" --json`，退出码 0，counts 全零），不必因「块 6 有省略号」重跑。
