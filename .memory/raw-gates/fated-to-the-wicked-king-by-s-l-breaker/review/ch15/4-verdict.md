# ch15 判定表（R4）

| # | 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|---|
| 1 | 原句1 Sophie 的友善不设防 | text/ch15:16 | 一致 | — |
| 2 | 原句2 Gregory 护住 Sophie | text/ch15:25 | 一致 | — |
| 3 | 原句3 国王说「这是我的女巫」 | text/ch15:28 | 一致 | — |
| 4 | 原句4 她纠正「我是科学家」 | text/ch15:31 | 一致 | — |
| 5 | 原句5「谁在谈判，你还是我」 | text/ch15:64 | 一致 | — |
| 6 | 原句6 Sophie 说破 mystical heart | text/ch15:215 | 一致（说话人是 Sophie） | — |
| 7 | 原句7 编造的红心女王藏心故事 | text/ch15:275 | 一致（叙述者编造） | — |
| 8 | 原句8 Sophie 复述「戴它／护它／借此毁掉红心女王」 | text/ch15:284 | 一致 | — |
| 9 | 原句9 父亲的旧事 | text/ch15:362 | 一致（转述口径） | — |
| 10 | 原句10 红皇后操纵记忆、统治数百年 | text/ch15:365 | 一致 | — |
| 11 | 原句11「I hope so too.」收尾 | text/ch15:374 | 一致 | — |
| 12 | Sophie 自行推断未被 md 记录 | text/ch15:220–226 | 缺一手信息 | **提示（已修）** |
| 13 | 块序 11 块偏移递增 | 2-machine.json | 递增 | — |

## 已核实为正确（防误修）

1. **「You wear a mystical heart.」的说话人是 Sophie**（`text/ch15:215`，紧接 `Her mouth dropped open`）；**不是**叙述者自陈。
2. **「This is my witch, Allie.」是国王说的**（`text/ch15:28`），她随即否认（`:31`）——两句必须成对。
3. **红心女王藏心的故事是编的**：`text/ch15:275` 是叙述者"adopting a somewhat eerie tone"讲的故事，`text/ch15:284` Sophie 只是顺着复述；本章没有任何旁白把它证成事实。
4. **Sophie 的推断独立于故事**：`text/ch15:226` "It wasn't hard to guess. I've only observed your interactions this morning"——顺序是「她先说破→叙述者再讲故事」。
