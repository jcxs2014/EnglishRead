# Null Entity 总览模板交付报告（代理产出，2026-10-10）

## 一、交付文件与统计

目录：`notes/books/novels/null-entity-by-seth-haddon/.overview_templates/`

| 文件 | 行数 | {Q:NN:seq} | {P:NN:seq} | 模板阶段多引语行 |
|---|---|---|---|---|
| ov_00_概述.md.tpl | 71 | 28 | 0 | 0 |
| ov_00_金句精选.md.tpl | 171 | 28 | 25 | 0 |
| ov_00_情感节点.md.tpl | 126 | 30 | 0 | 0 |

结构严格对齐 mazywood（`notes/books/mystery-thriller/mazywood-by-tananarive-due/.overview_templates/`，
任务书所写 `mazywood-by-eric-larsen` 路径不存在，已用实际路径）＋immortal 的 `{P:NN:seq}` 中文行形态：
YAML frontmatter（`状态: 未读`／`modified: "2026-10-10"`）、概述＝梗概九段＋三个主题＋人物弧光五组、
金句＝①…㉕ 十二条分组六节（每节「一、…」）、情感节点＝节点一～十（标题带章段）＋叙事概括＋关键引语三条。
未自创参考里不存在的节或行形态。

## 二、机器校验（内存模拟，未跑 gen_overview.py 产出 md）

- 全部 86 个占位符经 `gen_overview.build_pool`（活池，非 ne-pool.md 静态表）逐键命中，0 MISSING；
  展开＋`one_quote_per_line` 后三文件均为 0 条多 `（ch` 行。
- `check_overview_full` 口径：SPAN／SPAN_UNQUOTED 对账 0 错位、0 查无；H1 分别含 概述/金句精选/情感节点。
- `verify_overview_quotes` 口径：金句抽出 24/25（② `{Q:2:1}`「It's obviously a trap.」17 flat 字符，
  <20 被工具静默跳过，与 mazywood 先例一致，且该句本身来自已核实池）；情感节点 29/29 命中、0 标注错位。
- 池差异备忘：`ne-pool.md` 静态表列 ch05#1–8、ch07#1–8，活池实际为 ch05 六条、ch07 七条；
  模板一律以活池键为准（QA 已逐键验）。

## 三、主动回避的断言（书中未写判词，一律不裁决）

1. 叙述者「我」与 Wylla 的生死结局——ch22 原文只到「连贯性在此终止」，只复述文本状态，不作死亡宣告／复活证明。
2. `Hello, Sable`（epilogue 呼唤）的回应者是谁——只写「朝虚空喊出那声呼唤」，不写回应。
3. ch06 身体互换的机制——原文写明「我」并不知道，只把猜测系在 LYREBIRD 身上，照此措辞。
4. Sable 双姓 Alzian/Veonya 与 Fyster 的关系、Prime 口中 `Mrs. Alzian` 的指向——只并置，不裁决。
5. ch06 之后 I/you 指代随换体漂移——各段落按 facts 卡片逐章对应写「我／Wylla／Four」，不固化成单一「她/它」。
6. ch19 Wylla 打穿 Wood 头部一事书内明写，照写；其余悬置点（见下第四清单）全部不置判词。

## 四、「facts 无法证实所以没写」条目（12＋10 悬置点全量核对后弃写）

ch01 匿名邀约者身份；Aliers 何时知情（谁先认出 LYREBIRD）；Wylla 如何懂得覆写 Prime 的权限路径；
Specter 一词具体所指；epilogue 中呼唤得到何种本体论回应；Prime 的最终下场；RABBIT 变「明亮」的原因；
无名医护的姓名与来历；Ray 的尸首去向；「七个月」起算锚点（死亡日 or 弥散日）；Sey 与 Fulvia 的后续下场；
byronnicum 孢子效果的永久性；BASE 的坐标（原文即 no coordinates）；Δ 符号含义；
Aliers「wives」一语的归属；GIRS 之外联邦侧的伤亡统计；ch21「Watch us」朝向何人。

## 五、给编排方的接力提示

- 磁盘上 `00_概述.md`／`00_金句精选.md`／`00_情感节点.md`（00:35 生成）出自修正前的概述 tpl：
  梗概六原有两条 `（chNN）` 同行，被 `one_quote_per_line` 机械拆行。**模板已改为该段只留
  `{Q:12:7}（ch12）`**（ch09#5 内容改为中文转述「所有受试者都在几天内烧毁，唯一没有被烧掉的
  就是那个名叫 Sable Alzian 的受试者」，转述内容逐字对应已核实池句）。
  ⇒ 请重跑 `python3 scripts/gen_overview.py "$BOOK"` 再验门禁，否则 md 与 tpl 不同步。
- `.memory/progress/ne-ov-agent/` 里的快照是修正前版本，仅作恢复基线，勿用作验收参照。
- 金句 tpl `**中文**` 计数 25 ＝ len(CIRCLED)，未触 `gen_overview.py` 的超㉕熔断。

## 六、留痕

- 未运行 `gen_overview.py` 写任何 md；未做任何 git 写操作；临时脚本仅 `/tmp/ne_ov_qa*.py`。
