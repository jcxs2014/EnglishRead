# ch20 an experiment with seeds —— R3 差异单

对照物：`review/ch20/1-suread.json`（R1 独立素读，8 条）＋ `review/ch20/2-machine.json`（R2）。

## 单子一：漏（素读有、md 未体现）
**3 条，均已补**：
1. R1 第 2 条（`text/ch20_chapter_20.txt:7` `Again, she woke up standing over a sleeping Lucy with a knife in her hand. Of all the moments she can recall, the fact that she keeps playacting this one, recapitulating the worst day of her life while dreaming?`）——md 只在导航说「开头像一场罪案复盘」，`醒来`/`握刀` 的复发句本身没有任何落点；而这是本书第三次同一动作（ch09、ch13），也是本章第一句。处置：补写为**原句 2**（47 词 2 句），旧 2–4 顺延为 3–5。
2. R1 第 4 条（`:31` `Her first boyfriend used to wrap his fingers around her wrist to show how far they overlapped. “I could snap your arm so easily,” he liked to say as he held it in two hands like an old baguette.`）——md 里 `手腕`/`掰断` 零命中，而一句话总结只把它压成「捏着她手腕展示指节重叠的男友」，那句威胁原话无处可查。处置：补写为**原句 4**（39 词 2 句），旧 4 顺延为 5。
3. R1 第 7 条后半（`:70` `Maybe she will get her own Audrey II like Seymour in Little Shop of Horrors.`）——md 里 `Audrey` 零命中；种子实验的收尾比喻整章缺席。处置：补写为**原句 7**（15 词 1 句；单句成段的短段例外）。
- 有落点的 5 条：刀顶门挡＋钥匙→原句 1；门挡是她的主意／「她危险而 Lucy 不懂」→导航人物弧线＋一句话总结；芭蕾舞女孩（丝带与肉色紧身衣）→一句话总结（『那个总想让她扮成芭蕾舞者的女孩』）；三粒／六粒／四粒→原句 6；章末缩脚与尖叫→导航＋一句话总结。
- 块数 4→7（⑱ 3–8 内）。

## 单子二：编（md 有、素读无）
- 0 条。

## 单子三：错（md 与素读不一致）
- 0 条。两处回源核实：
  1. 导航「对着她像一面镜子」→ `:4` `a mirror in the darkness` 逐字命中。
  2. 一句话总结「那个总想让她扮成芭蕾舞者的女孩」→ `:49` `In college she dated a girl who was always begging her to dress up like a ballerina` 属实。

## 派工人处置（3 条）
- 新增**原句 2**（又一次醒在 Lucy 身旁握刀）、**原句 4**（第一任男友的威胁原话）、**原句 7**（Audrey II），块数 4→7；改后 `chapter.sh` rc=0、`structure.py order` 29 md / 187 块 · 0 缺陷。
