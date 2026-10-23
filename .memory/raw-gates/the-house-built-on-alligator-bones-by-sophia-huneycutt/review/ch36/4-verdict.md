# ch36（Chapter Thirty-Five）判定表

- 素读：`1-suread.json`（18 facts / MISS 0；R1 由子代理素读，回执经 /tmp/s36.py 全量回源核验）
- 机器层：`2-machine.json`（chapter.sh rc=0；4 引语块逐字 0 MISS）
- 探针：v36 词表 13 行 flagged 0；ap36 直撇号 0；in36 越 19/书 3（2 模板例外 + 1 关键词提示）
- 档位：深审（用户升级）；章号偏移：本 md＝Chapter Thirty-Five

## 报数（四组）

| 组 | 结果 |
|---|---|
| 逐字 | 4/4 引语块逐字 0 MISS；词表例句 13/13 |
| 对应 | 4/4 块「中文在讲这句引语」，施事/归属无反转 |
| 形态 | H1、导航 4 项、子项集、块数 4 落在本书建议区间 |
| 断言 | 13 条内嵌英文/事实断言回源命中；1 条关键词成形提示 |

## 判定

| 编号 | 断言 | 证据（text/ch36_chapter_thirty_five.txt） | 结论 | 档位 |
|---|---|---|---|---|
| P-36-1 | 原句 3 关键词行「cut off」 | L81 原文为 "She cut me off again."——"cut off" 跳过 "me"，非原文连续子串（两个词均出自该句） | 关键词锚定不严，建议改 "cut me off" | 提示 |

## 修复指令（不改稿，供汇总）

1. `ch36 the offering is a hunt.md` 原句 3 关键词行：`cut off / poachers / …` → `cut me off / poachers / …`。
2. 改完重跑 chapter.sh 确认 keyword 门仍绿。

## 已核实为正确

1. 「我不能去」是 L118 "I couldn't do it." 的忠实转写，其后 L120 嗡鸣与脸到，md 的「紧跟」成立。
2. 「快脑子表扬其实是在为狩猎铺路」：L54 "That's the kind of fast thinking I like to see." 紧接 L105 定狩猎日程——铺垫关系是解读，两处原文均实。
3. 「换原谅的条件是再犯一次同名的行为」：L28 "unless I revealed Harrison's betrayal"——揭发即对 Harrison 的背叛，这层双关为 md 的解读，原文用词支撑。
4. 「不喂幼鳄的『惩罚』其实是饲养知识差」：L27 "She doesn't need anything to eat this week."——原文本就是喂食周期而非惩罚，md 读法正确。
5. 「压下揭发选项」：L63 "Secure my inheritance by destroying any semblance of competition." 后接 "But I couldn't stop picturing his face…"——掂量并放弃，方向一致。

## 覆盖声明

深审 R1–R5 全流程（素读 18 facts / 机器层全量 / 三张单子 / 逐块对应 4/4）。

## 汇总

- 阻断 0 ／ 提示 1 ／ 假红 0
- 累计进度：深审人判 42/49 章（ch36 完）。
