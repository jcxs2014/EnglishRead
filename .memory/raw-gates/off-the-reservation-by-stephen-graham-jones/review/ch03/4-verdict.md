# ch03 4-verdict（R4 逐块 + R5 判定）

R2 机器层：2-machine.json rc=0，12 块 12 引语，issues 全空。
R4 人判：12/12 块逐对核 + 施事三问。

| 断言 | 证据（章:行） | 结论 | 档位 |
|---|---|---|---|
| 导航概括「坐在医院门口的台阶上」地点错误 | text/ch03_2_the_reverse_massacre.txt:638「sitting on the curb of that little statue-island in the parking lot」；md 行9 | 应为「停车场雕像岛的路缘」 | **阻断** |
| 块7 未提「五岁那年/父母打架」 | text「I was five, I think」（素读#5 anchor 命中验证 True） | 数字细节未入 md，非关键转折 | 提示（不修） |
| 块12 读者视角「the smallest bleat」少 little | text:158「the smallest little bleat」 | 转述层措辞 | 提示（不修） |
| 块12 中文「仪表盘打火机」 | 引语「cigarette lighter from a dashboard」 | 一致 | 已核实为正确 |

取证命令记录：
- `/usr/bin/grep -n "statue\|curb\|steps\|stairs" text/ch03_2_the_reverse_massacre.txt` → 行245/386/515/638；退出码 0
- `/usr/bin/grep -n "bleat" text/ch03_2_the_reverse_massacre.txt` → 行158/164/167；退出码 0
- 素读#5 anchor 偏移命中验证（python text[start:end]==anchor）→ True

## 已核实为正确

- 块7 亲属信息「Nessa 是 Nate 的妹妹，住在 Great Falls」——text 行353「Nessa, Nate's little sister down in Great Falls with his mom」（T1 已修「同母异父」，本轮复核确认原文无 half-sister）。
- 块8 马墓献烟草的因果（「horses didn't ask for any of this…shot so the soldiers could hide from bullets behind them」）与中文理解方向一致：马被射杀是为让士兵躲子弹。
- 块9 施事：割臂立誓者=父亲（unfolded his knife 主语承前为 dad），Nate 的镜像动作是块9 分析的合法引申。

**结论：阻断 1（导航地点）、提示 2（不修）。**
