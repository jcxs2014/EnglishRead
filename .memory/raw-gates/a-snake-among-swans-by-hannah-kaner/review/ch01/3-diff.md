# ch01 R3 对账（素读 8 条 ↔ md 9 块）

R1 素读：`1-suread.json`（8 条，interval 实算，intervals_ok 8/8）

## 漏（素读有、md 无）

- **fact 4「Rivani 反问九岁 Maela of Hallion」**：md 正文块里没有出现 Maela，但 `## 一句话总结` 写明「Rivani 用一位九岁的新娘人选和一部经文顶回去」——已覆盖，只是未落进任一块的引语/分析。
  ⇒ 结论：**不算漏**（md 有交代）。提示级：若要让读者在正文看到这场反击的原文，可在原句 3 后补一句分析。证据：text/ch01_chapter_one_tilde.txt:「'Maela of Hallion, perhaps? She is nine years of age, and cannot bear children till she has her bloods.'」

## 编（md 有、原文无）

- 逐块引语：机器层 `quotes.py verbatim --full` 550/550、`verify_fragments_indep` MISS 0 ⇒ 引语 0 编造。
- 分析句抽查（含数字/身份/归属）：
  - 「Isabella the Wise, Isabella the Weak, was from Galen」→ 原文 `Isabella the Wise, Isabella the Weak, was from Galen` ✅
  - 「一个子宫 / 一大片庄稼里的一个」→ 原文 `'She is but one womb,' … 'in a crop of many.'` ✅
  - 「milk-faced palati（不是王子、不是公爵）」→ 原文 `insultingly not a prince, or a ducal, but a mere milk-faced palati` ✅
  - 「我差点就在那一刻把自己毁了」→ 原文 `I had almost undone myself there and then.` ✅
  - 「Rivani 自残（把自己的手指抠到流血结疤）」→ 原文 `Rivani waged war on her own fingers, picking at the skin around her nails till they bled and scarred` ✅
  ⇒ 编：0

## 错（主语/因果/数字/时序不一致）

- 「被围困在 Ardwen 城堡里」→ 原文是边地被反复侵入、付贡以免民饥（`our walls bruised of body`、`so our people would not starve next winter`），无「围城」字样。属**概括加码**（提示级，不改）。
- 「Tilde 藏在楼上走廊里」→ 原文 `I watched in secret from the gallery above our great and empty hall`：是**大厅上方的楼座/回廊**，不是走廊。提示级。
- nav「kingsmoot 六年」→ 原文 `Six years after the kingsmoot` ✅
- 「Rivani 用一位九岁的新娘人选」→ 原文 `She is nine years of age` ✅
- 时序：块 2（Isabella 死→使节来）在原句顺序上先于块 3（谈判）✅

## 小结

阻断 0 ｜ 提示 3（正文未落 Maela 原文 / 「围困」加码 / gallery 译作「走廊」）
