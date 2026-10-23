# ch33（Chapter Thirty-Two）判定表

- 素读：`1-suread.json`（22 facts / MISS 0；R1 由子代理素读，回执经 /tmp/s33.py 全量回源核验）
- 机器层：`2-machine.json`（chapter.sh rc=0；6 引语块逐字 0 MISS）
- 探针：v33 词表 22 行 flagged 0；ap33 直撇号 0；in33 越 19/书 3（2 模板例外 + 1 假红）
- 档位：深审（用户升级）；章号偏移：本 md＝Chapter Thirty-Two

## 报数（四组）

| 组 | 结果 |
|---|---|
| 逐字 | 6/6 引语块逐字 0 MISS；词表例句 22/22 |
| 对应 | 6/6 块「中文在讲这句引语」，施事/归属无反转 |
| 形态 | H1、导航 4 项、子项集、块数 6 落在本书建议区间 |
| 断言 | 17 条内嵌英文/事实断言全部回源命中（清单见 3-diff.md） |

## 判定

| 编号 | 断言 | 证据 | 结论 | 档位 |
|---|---|---|---|---|
| P-33-1 | 原句 2 读者视角提示「Instinctively, I stepped back.（本章原文同段）」 | carmine 句在 text L120；"Instinctively, I stepped back." 在 text L123，中间空行相隔，为**下一段** | 布局描述不准确（次段非同段），引文本身逐字无误 | 提示 |
| F-33-1 | in33 报 'outshine' 不在书内 | text L120/L9 用的是屈折形 "outshone"；md 分析层用的是引理 "outshine"（关键词 outshone 的词条讨论） | 探针不做词形归一，分析层引理提及非凭空引文 | 假红 |

## 提示型汇总

- P-33-1：改法（供修复指令）——「（本章原文同段）」→「（本章原文次段）」；其余一字不动。

## 已核实为正确

1. 「从未真正相信」是 L126 "I'd never fully believed" 的合理转写（fully→真正），与 L129 "I was convinced" 的转折配对成立。
2. 「唯独 Gazzie 锁着的办公室没事」逐字对应 L90 "Not your office; it's still locked. But it's everywhere else."；六处地点清单与 L90 列举一一对应。
3. 「排除法越严密、非人结论越顺理成章」的 Tropes 读法：排除素材（L156/L159/L144）与结论（L132 "A person couldn't cart in this much blood… No."）均在原文。
4. 「留宿既是危险任务也是被迫的亲密」：L189 "A whole night with Harrison… Was it a test?" 支撑。
5. 章末恐惧指向：L228 "toward me" 为全段末尾，md「第一次有了明确的指向坐标」成立。

## 覆盖声明

深审 R1–R5 全流程（素读 22 facts / 机器层全量 / 三张单子 / 逐块对应 6/6）。

## 汇总

- 阻断 0 ／ 提示 1 ／ 假红 1
- 累计进度：深审人判 39/49 章（ch33 完）。
