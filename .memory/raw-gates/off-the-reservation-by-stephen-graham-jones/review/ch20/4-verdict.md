# ch20 4-verdict（R4 逐块 + R5 判定）

R2 机器层：2-machine.json rc=0，12 块 12 引语，issues 全空。
R4 人判：12/12 块逐对核 + 施事三问。

| 断言 | 证据（章:行） | 结论 | 档位 |
|---|---|---|---|
| 素读#7「子弹揭示」在块10 悬置 | 素读 anchor「it was a bullet」命中 True；一句话总结层已覆盖 | T1 拆短牺牲；块10 悬置措辞使精读块不完整 | 提示（建议修：补回揭示句） |
| 素读#4「博物馆正门前」未入块 | 素读 anchor 命中 True | ch07 幻境版本的回收，与「回家」结局对照 | 提示（不修，与 ch07 同链） |
| 素读#3「Great Falls 砍半」未入块 | 素读 anchor 命中 True | 动机细节 | 提示（不修） |
| 块11「You're not broken…You're just stupid」 | 引语自证；素读#8 | 全书最治愈句逐字保留 | 已核实为正确 |

取证命令记录：
- 素读 anchor 偏移验证 True ×8（ch20 子代理自证）
- `/usr/bin/grep -n "it was a bullet" text/ch20_19_serious_indian_stuff.txt` → 命中（素读#7）；退出码 0

## 已核实为正确

- 块8「serious Indian stuff」的章名出处标注正确（D 的台词），恐龙≠灵兽的规则吐槽保留了 D 的青春期语气（"That's, just, like, the rules, I don't know"）。
- 块9「白尾鹿拦路→D 绕到这条路」的守护机制解读与素读一致；「母鹿眼睛周围的眼线」呼应 ch01 的性别辨认细节，非过度解读。
- 块12「the little boy, safe at last」的双重身份解读（玩偶头骨＋Nate 内心少年）——T1 已把「九岁」改为「少年」，本轮复核确认无年龄错置残留。

**结论：阻断 0、提示 3（1 建议修子弹揭示悬置、2 不修）。本章干净。**
