# ch67 判定表（Always Again）

- 覆盖：深审人判全块（4/4）+ 四件套齐全；素读 8 条（`1-suread.json`）
- 机器层：`bash scripts/chapter.sh "…/ch67 always again.md" --json` → **rc=0**，块数 4，引语段 4/4 命中（62/48/52/41 词，pos 671/1701/2214/2931），查无 0，空引号 0，子项缺 0（struct_bad 0），关键词异常 0，中文密度低 0，nav 5（5 项齐），H1 `67. Always Again` 形态正确，块数 4 vs 本书中位 6 / 区间 3–10（在范围内，且与任务表配额 ch67=4 一致）
- 报数：**逐字 0 · 对应 0 · 形态 0 · 断言 1（阻断，类级）+ 提示 2**

| 断言 | 证据（text/文件:行 + 原文逐字） | 结论 | 档位 |
|---|---|---|---|
| 抬头日期与年龄「2053 年 7 月 24 日，克莱尔 82、亨利 43、贝克 77」 | text/ch67:18 `Thursday, July 24, 2053 (Clare is 82, Henry is 43, Beck is 77)` | 三组数字全对；md 第 47 行只用「亨利四十三岁，克莱尔八十二岁」推 `died so young`，与抬头一致 | 已核实为正确 |
| 「这一章由贝克以第一人称讲述」 | text/ch67:23 `Beck: Clare and I are both early birds, in these long light summer days at our lake house in the Upper Peninsula of Michigan` | 叙述者归属正确（不是 Alba、不是 Clare），`our lake house` 与 `the Upper Peninsula of Michigan` 也逐字落地 | 已核实为正确 |
| 叙述者 Beck 的性别：全章用「他」（第 11/13/21/25/27/41/45/47/51/55/57/91 行），并把克莱尔两段婚姻说成「丈夫之间的敌意」（第 13 行） | 本章原文为第一人称、无性别信息；全书硬证据：text/ch04:65 `Beck is Alba’s stepmother; I don’t know who Jasper is.`；text/ch11:113 `I like Beck. I feel a certain kinship with her: We both arrived late and married into the DeTamble family`；text/ch69:118 `I turn to Beck and she is young again: Beck as I first knew her when I was a child. Her face is unlined`（2065 年，晚于本章）；text/ch01:2099 `Beck is there. She closes the door behind me` | **人物性别反了**：Beck 是克莱尔的**妻子**、Alba 的继母，全书一律 she/her；md 把她写成男性约 15 处，第 13 行「丈夫之间的敌意」随之落空（两段婚姻是前夫 Jasper 与妻子 Beck，不是两个丈夫） | **阻断** |
| 「克莱尔出来，握着他的手说亨利终于来了」 | text/ch67:55 `Eventually Clare appears, walking slowly until she is standing beside me. She takes my hand carefully, because we both have arthritis.`；text/ch67:60 `“He finally came, then?” I say.` | 动作方向对（`She takes my hand`＝Clare 握 Beck 的手），问句归属对（「He finally came, then?」是 Beck 问）；「关节炎」两人共有，md 未误挂一方 | 已核实为正确 |
| 「她什么也没问，只是让他走了」 | text/ch67:76-88 `“I’m sure he wished he could,” I say. “Did you ask him all your questions?”` / `“No.”` / `“Not one?”` / `“I just let him go,” Clare says.` | 问答双方正确（Beck 问、Clare 答），三层递进「No.」→「Not one?」→「I just let him go」md 未并成一句；「一个都没问」＝`Not one?` 的回应，非 md 编造 | 已核实为正确 |
| 「他等的不是自己的解脱，而是她的了结」 | text/ch67:49 `I’ve always imagined that when today finally arrived I’d feel relieved, glad, unburdened—but Clare has looked forward to this for half of her life.` | 「我一直以为我会解脱」→「可克莱尔盼了半辈子」的转折方向对；`half of her life` 译「半辈子」成立 | 对应 |
| 「整章里这个人始终没有转身，也没有开口」 | text/ch67:44 `There was a man with Clare, standing with his back to me, a white-haired man, but I could see that he was not an old man.`；全章亨利零台词（第 44–112 行仅 Beck 与 Clare 对话） | 零台词断言成立：亨利的全部呈现只有身体在场（背对、白发、赤身、相拥），无一句引语 | 已核实为正确 |
| 「灰皮诺」译 pinot grigio | text/ch67:33 `we’d been rowing the boat around the lake in the dark, drinking pinot grigio and singing old Beyoncé songs` | 译名正确（pinot grigio＝灰皮诺），且未把 Beyoncé 误作「老歌」的演唱者之外的改写 | 已核实为正确 |
| 心里话「if Alba ever told you who I really am」「Love is in short supply in this world」未进块也未进导航 | text/ch67:49 `I hope, if Alba ever told you who I really am, that you were generous enough to be happy for Clare. Love is in short supply in this world. You and Clare and I, we were lucky in love.` | 块 3 引语止于 `if you’d lived?`，此后两句（身世暗扣 + 爱的稀缺）全章无一字提及；虽非事件转折，但属本章唯一的身世钩子 | 提示 |
| 「蚊子几乎绝迹」的气候暗线未收 | text/ch67:33 `The lake is so warm these days and there are hardly any mosquitoes anymore, which is frightening but also convenient when you want to go for a swim in a lake surrounded by woods.` | md 第 27 行只取「泳衣／划船／灰皮诺／老歌」说明日子松快，`frightening but also convenient` 这层「舒适源自崩坏」的反讽未收 | 提示 |
| 零命中类断言 | 本章无「全书查无」型断言 | — | — |

## R4 逐块对应（三问）

| 块 | 这段中文是不是在讲这句引语？ | ①动词主语 | ②受事 | ③归属方向 |
|---|---|---|---|---|
| 1（原句1，pos 671） | 是（只解这 3 句，未越界到听见响动） | Beck（`I was dozing / I could feel / I was thinking`） | 「热」、卧室的凉、游泳 | `savor the cool of the bedroom`＝享受卧室的凉，未反成「享受热」；`put it off`＝把这一天推后，md「把热再往后推几分钟」成立 |
| 2（原句2，pos 1701） | 是（`standing with his back to me` 起，未把后文 Clare 出来握手混进来） | 那个男人（`There was a man… standing`）；辨认者是 Beck（`I could see… I knew`） | 背、白发、裸身、旧日一面之缘 | `with his back to me`＝背对 Beck，md「背对着贝克」方向对，**不得**改成「贝克背对他」；`I’d seen him once before, years ago`＝Beck 多年前见过他，非 Clare |
| 3（原句3，pos 2214） | 是（`Well, I say to Henry in my head` 到 `if you’d lived?`） | Beck（心里说）；听话对象 Henry | 「你陪她很久／我陪她更久」、`interesting life`、`died so young` | `you were with her` 的 you＝Henry、her＝Clare，md 未把「你」「我」对调；`between us she’s had an interesting life` 的 she＝Clare，成立 |
| 4（原句4，pos 2931） | 是（`I’ve always imagined` 到 `never knew`） | Beck（以为会解脱、难过、觉得奇怪） | 自己的期待、Henry 的永别、Clare 的半辈子 | `Clare has looked forward to this` 主语是 Clare，md「可克莱尔为这一刻盼了半辈子」方向对；`miss someone I never knew` 的 miss 主语是 Beck，md 第 57 行作「『miss』的主语是他自己」——归属对，仅代词性别错 |

## 已核实为正确（防下一轮误修）

1. **叙述者就是 Beck，不是 Alba** —— text/ch67:23 有说话人标记 `Beck:`，全章 `I / me / my` 均指 Beck。修代词性别时**不要**顺手把叙述者改成 Alba 或 Clare。
2. **「He finally came, then?」是贝克问的**，不是克莱尔自述 —— text/ch67:60；克莱尔的回答在 text/ch67:64 `“He did,” Clare says.`。修性别时只改人称，不要交换问答双方。
3. **「I just let him go」＝「一个都没问」** —— text/ch67:84-88 `“Not one?”` → `“I just let him go,” Clare says.`：是 Clare 主动放走，不是 Henry 自己走的，也不是 Beck 让 Henry 走的。
4. **亨利全章未转身、未开口** —— text/ch67:44 `standing with his back to me` + `He and Clare stood embracing silently.`，此后无他的台词。md 第 14/37 行成立，**不得**据电影版或别章补一句亨利的话。
5. **握手的施事是克莱尔** —— text/ch67:55 `She takes my hand carefully, because we both have arthritis.`：Clare 握 Beck 的手，且**两人都有**关节炎。别改成「贝克握住克莱尔的手」或「只有克莱尔有关节炎」。
6. **抬头三个年龄**（82/43/77）与 `died so young` 的推论 —— text/ch67:18 与 text/ch67:49 并置成立：Henry 停在 43 岁，所以「年轻」是事实，不是修辞。
7. **「灰皮诺」** —— text/ch67:33 `drinking pinot grigio`，译名正确，无需改「白皮诺／皮诺格利乔」。
8. **「我们的房子」不是笔误** —— text/ch67:111 `we walk into the lake house, our house`：原文就是 `our house` 同位语，md 第 88 行例句照录正确。
