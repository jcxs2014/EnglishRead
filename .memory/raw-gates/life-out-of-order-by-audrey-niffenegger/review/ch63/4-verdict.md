# ch63 First Light — R5 判定

- md：`notes/books/novels/life-out-of-order-by-audrey-niffenegger/ch63 first light.md`
- text：`notes/books/novels/life-out-of-order-by-audrey-niffenegger/text/ch63_first_light.txt`
- R1：`review/ch63/1-suread.json`（先于 md 打开）｜R2：`review/ch63/2-machine.json`｜R3/R4：`review/ch63/3-diff.md`

## R2 机器层

`bash scripts/chapter.sh "…/ch63 first light.md" --json` → **rc=0**，`verdict=ok`，`issues=[]`，`blocks=8`，`cjk_ratio` 全部 >0.6。rc=0 不等于通过。

## R5 判定表

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 逐字：8 块引语 | `:23`「I dream that Alba has come home.」／`:28`「Someone stands at the kitchen sink with their back to me」／`:52`「I look at Alba more carefully and see that her hair is grayer and six inches longer」／`:108`「Remember to apply a lot of pressure to the wounds」／`:165`「He lies curled on his side」／`:172`「The future won’t magically take care of itself.」／`:205`「I imagine us as conjoined twins」／`:277`「I’ve been reading David Copperfield out loud to Oliver」 | 8/8 逐字成立 | 通过 |
| 逐字：词汇 13 条例句 | 逐条 `in flat(text)`：`silhouetted`／`consternation`／`tourniquet`／`nonjudgmental`／`distracted`／`unconscious`／`saturated`／`swigging`／`attendant`／`ambulance`／`blankets`／`wounds`／`brother` | 13/13 命中，miss=0 | 通过 |
| 对应：块 1 | 梦里的「倒回去／不知道反而安稳／不年轻了／平静」；md 未把它读成真的和解 | 在讲这句引语 | 通过 |
| 对应：块 2 | 背影→剪影→逼自己看清→转身→谨慎问候；md 未提前给她的脸 | 在讲这句引语 | 通过 |
| 对应：块 3 | 「更灰、六英寸长」→「从什么时候来」→「藏起惊愕」；md 保留了 when（时间）而非 where（地点） | 在讲这句引语 | 通过 |
| 对应：块 4 | 止血四步＋三个「因为」；说话人是阿尔芭，md 未误挂给扎克 | 归属正确 | 通过 |
| 对应：块 5 | 蜷、抱胸、屈膝、黑发散雪；md 未加「他死了」之类判断 | 在讲这句引语 | 通过 |
| 对应：块 6 | 「未来不会自己照顾自己」→「得动手」→跪雪攥腕→「没见过疤、没见过他老」 | 在讲这句引语 | 通过 |
| 对应：块 7 | 连体婴、两个「也许」、for her＝在她眼里 | 在讲这句引语 | 通过 |
| 对应：块 8 | 念《大卫·科波菲尔》、昏迷者也许听得见、她说「别停」 | 在讲这句引语 | 通过 |
| 形态：块数／子项／POV | 8 ∈ `block_target [4,8]`；四子项齐全；`:23` 单标签「Zach:」与全章第一人称一致 | 合格 | 通过 |
| 断言：`:11`「这一夜对她已是两年前的旧事」 | `:65`「It was only two years ago, for me.」 | 成立 | 已核 |
| 断言：`:11`「阿尔芭随即消失」 | `:217`「Alba smiles, and then she’s gone.」 | 成立 | 已核 |
| 断言：`:11`「第三天她回来听他念书」 | `:277`「On the third day after his surgery, Alba arrives.」 | 成立（原文是「手术后第三天」，比「第三天」更精确） | 已核 |
| 断言：`:11`「奥利弗在药物引导下昏迷」 | `:118`「Medically induced coma.」 | 成立 | 已核 |
| 断言：`:11`「雪中弃车」 | `:108`「we’re in the car」＋`:112`「The streets have been cleared overnight… I can’t drive as fast as I want to.」＋`:192`「I hope the ambulance doesn’t get blocked by our car.」＋`:267`「I maneuver my car」 | 路是通的、他后来自己开车去医院；「弃车」读起来像开不动而弃车步行 | 提示 |
| 断言：`:11` 未提 1978、未提「两个阿尔芭」 | `:136`「“Where’s your present self? In the house?”」／`:140`「“1978.”」／`:148`「Alba hesitates, then says, “Yes.”」 | 素读有、md 无 | 提示（漏，偏重） |
| 断言：`:11` 未提「这就像我爸死的时候」 | `:176`「“This is like when my dad died.”」 | 素读有、md 无 | 提示（漏） |

## 报数（四组）

- **逐字**：引语 8/8、词汇 13/13，0 条。
- **对应**：8/8 块在讲引语，0 条。
- **形态**：8 块顶格、POV 标签一致，0 条。
- **断言**：导航 5 条 + 抽查 3 条 = 8 条，其中 6 条成立、2 条提示（弃车、1978/父亲之死未进 md）。

| 章 | rc | 块数 | 漏 | 编 | 错 | 提示 |
|---|---|---|---|---|---|---|
| ch63 | 0 | 8 | 0 | 0 | 0 | 3 |

## 已核实为正确（防下一轮误修）

1. **「第三天」不是漏写成「两天后」**：原文 `:277`「On the third day **after his surgery**」，md 写「第三天」，与原文一致；若下一轮把它改成「手术两天后」反而错。
2. **「兄弟」是对警察现编的**：`:257` 先写「I want to give a fake name」，`:258` 才说「I’m his brother」，`:267` 还补「He’s my half brother. My mother remarried.」——md `:13` 说「这个称呼是他对警察现编的」正确，不要改成真兄弟。
3. **急救台词的主语是阿尔芭，不是扎克**：`:108` 那串祈使句出现在阿尔芭一边开车一边说话的场景里，扎克在「trail after her」；md `:15`「阿尔芭的急救说明」正确。
4. **奥利弗全章没有一句台词**：`:165`–`:221` 他只有身体动作（蜷、几乎闭眼、被抬上担架），md `:14`「始终没有开口」成立，不要因为后文「昏迷者听得见」就给他补台词。
5. **「她两年前经历过」与「她不知道之后会怎样」并不矛盾**：`:65`「It was only two years ago, for me」＋`:200`「I only know what you told me.」——她知道这一夜，但不知道结局；md `:13` 的「预知者」没有写成全知，正确。
6. **梦里的「平静」不是真的和解**：`:23` 引语自带括号「(in the dream I know something terrible has happened)」，md `:21`/`:25` 都保留了这层保留态度，不要读成夫妻和好。
