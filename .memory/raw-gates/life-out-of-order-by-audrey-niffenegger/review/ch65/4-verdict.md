# ch65 Lemon Cake and Coffee — R5 判定

- md：`notes/books/novels/life-out-of-order-by-audrey-niffenegger/ch65 lemon cake and coffee.md`
- text：`notes/books/novels/life-out-of-order-by-audrey-niffenegger/text/ch65_lemon_cake_and_coffee.txt`
- R1：`review/ch65/1-suread.json`｜R2：`review/ch65/2-machine.json`｜R3/R4：`review/ch65/3-diff.md`

## R2 机器层

`bash scripts/chapter.sh "…/ch65 lemon cake and coffee.md" --json` → **rc=0**，`verdict=ok`，`issues=[]`，`blocks=4`，`cjk_ratio` 全部 >0.6。rc=0 不等于通过。

## R5 判定表

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 逐字：4 块引语 | `:23`「When I returned to bed Zach reached over and clasped my hand. “It’ll be fine,” I told him, but now I’m not so sure. Zach looks as though he’s about to have dental surgery.」／`:29`「He’s wearing a white button-down shirt and linen trousers…“They are healing very nicely,” Oliver says.」／`:80`「…the only thing my two marvelous husbands are willing to have in common is me.」／`:133`「In the morning, Oliver is gone. Zach and I have some of the lemon cake for breakfast…he belongs.」 | 4/4 逐字成立 | 通过 |
| 逐字：词汇 14 条例句 | 逐条 `in flat(text)`：`clattering`（`:28`）／`foil-covered`（`:38`）／`determination`（`:80`）／`repertoire`（`:85`）／`virtuosity`（`:114`）／`alluring`（`:71`）／`worrisome`（`:71`）／`measured`（`:71`）／`intimacy`（`:85`）／`marvelous`（`:80`）／`eyes`（`:76`）／`bed`（`:114`）／`breath`（`:119`）／`double`（`:67`） | **14/14 命中，miss=0** | 通过 |
| 对应：块 1 | 抓手→「会好的」→自己不确定→牙科手术；md 指出两种声音同出一人 | 在讲这句引语 | 通过 |
| 对应：块 2 | 白衬衫、亚麻裤、卷袖、六英寸粉疤、翻腕、愈合得好；「He」＝奥利弗 | 在讲这句引语 | 通过 |
| 对应：块 3 | 本非她想、三个未来的自己鼓励、维恩图重叠处、唯一共有的是她（by 方向未译反） | 在讲这句引语 | 通过 |
| 对应：块 4 | 清晨奥利弗不在、分吃蛋糕、煮咖啡、抬头笑、belongs 无对象只有地点 | 在讲这句引语 | 通过 |
| 形态：块数 | 4 块，`block_target [2,3]` → 超建议值 1 块（`block_limit` 内） | 提示 | 提示 |
| 断言：`:11`「三人靠金汤力熬过最长的半小时」 | `:51`「“Would anyone like a gin and tonic?”」＋`:71`「It’s the longest half hour of my life.」——但同句前半是 `:71`「When we all have drinks it feels more like a party and less like a dentist’s waiting room.」 | 成立，唯「熬」压掉了「像派对」那一面 | 提示（措辞） |
| 断言：`:11`「客气得用力」 | `:80`「What follows is the most polite sex I’ve ever had…it takes some determination to not touch.」 | 成立 | 已核 |
| 断言：`:13`「十点喝金汤力」 | `:59`「“Alba, it’s ten a.m.,” Zach says.」 | 成立 | 已核 |
| 断言：`:92`「一磅咖啡」 | `:38`「“We brought lemon cake and a pound of coffee,”」 | 成立 | 已核 |
| 断言：`:92`「奥利弗提议即兴来一段华彩、用斜向进行」 | `:106`「“Let’s improvise,” Oliver says. “A cadenza, with oblique motion.”」 | 成立 | 已核 |
| 断言：`:92`「她解释成一个声部动、另一个不动」 | `:114`「‘Oblique motion’ means one part moves and the other remains stationary.」 | 成立 | 已核 |
| 断言：`:92`「扎克承认原不知道想要这个，并吻了他」 | `:127`「“I didn’t know I wanted that, but I do.” He leans forward and kisses Oliver on the lips」 | 成立 | 已核 |
| 断言：`:92`「她说回家…永远受欢迎」 | `:142`「“We go home. But in the future, when I’m gone, and you’re lonely, you can come here…you’ll always be welcome.”」 | 成立 | 已核 |
| 断言：`:92` 结尾「她说，我们值得」 | `:151`「“Why not?” I say. “I think we deserve it.”」 | 成立（但漏掉 `:147`「“‘And they all lived happily ever after.’”」） | 提示（漏，偏重） |
| 断言：`:12` 未提前一晚「我不知道该怎么面对这件事」 | `:23`「Last night as we got into bed he said, “I don’t know how to feel about this.”… “You can change your mind once we’re there.”」 | 素读有、md 无 | 提示（漏） |
| 断言：`:14` 未提「我知道我们可以重新幸福了」 | `:127`「…and I know that we can be happy again.」 | 素读有、md 无 | 提示（漏） |
| 断言：全文未提「我两个丈夫都很美」 | `:123`「Both of my husbands are very beautiful and I love them both very much.」 | 素读有、md 无 | 提示（漏） |
| 断言：正文未写「性的套路」一段 | `:85`「It’s funny how a sexual repertoire develops…I share different habits, moves and caresses with each of my husbands and I see that they are noticing and wondering.」 | 素读有、md 无（仅词汇表收词） | 提示（漏） |

## 报数（四组）

- **逐字**：引语 4/4、词汇 14/14，0 条。
- **对应**：4/4 块在讲引语，0 条。
- **形态**：块数超建议值 1 块，1 条（提示）。
- **断言**：导航/总结/抽查 14 条，10 条成立、4 条提示（「熬」的措辞＋三处漏＋结尾童话句）。

| 章 | rc | 块数 | 漏 | 编 | 错 | 提示 |
|---|---|---|---|---|---|---|
| ch65 | 0 | 4 | 0 | 0 | 0 | 5 |

## 已核实为正确（防下一轮误修）

1. **「两个丈夫愿意共享的只有她一个人」没有译反**：`:80`「the only thing my two marvelous husbands are willing to have in common is me」——主语是两个丈夫，共有的宾语是她；不要改成「她愿意与两个丈夫共有的一切」。
2. **「三个未来的自己鼓励了她」方向正确**：`:80`「had I not been encouraged by all three of our future selves」是被动（她被人鼓励），md `:41`「是三个未来的自己鼓励了她」正确。
3. **破冰的第一句是「我喜欢即兴」，不是阿尔芭先解释**：`:106` 奥利弗提议，`:110` 扎克说听不懂，`:114` 她才解释；md `:92` 的顺序与此一致，别把解释挪到奥利弗嘴里。
4. **「奥利弗穿白衬衫下楼」**：`:28`「he comes clattering down the stairs」＋`:29`「He’s wearing a white button-down shirt and linen trousers」——是先下楼、后写衣着，md 说法成立。
5. **「十点喝金汤力」是扎克的反对而非叙述**：`:59`「“Alba, it’s ten a.m.,” Zach says.」，`:67` 他自己「Make mine a double」；md `:13` 把它当作「钟点不算数」的兑现，成立。
6. **「一磅咖啡」**：`:38`「a pound of coffee」，md 未写成「一罐」或「一袋」，正确。
7. **`belongs` 后面确实没有对象**：`:133`「Here he is, in the Yellow House; he belongs.」句号收尾，md `:57`「他属于的不是某个人，而是这座房子」是对原文句法的准确读法。
8. **`repertoire` 收进词汇表是合规的**：`:85`「a sexual repertoire develops」原文有据，虽然正文段未进块，词条本身不是编造。
