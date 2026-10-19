# 2026-10-19 gate.sh ② lane 修复后的全库 check_vocab 存量状态

> **背景**：gate.sh ② lane 原为 `| grep -E "词条行合计|FAIL \(|WARN \("`——**只打印**
> `FAIL (N)` 文字，**不计入退出码** ⇒ gate 报「0 条阻断型 · 退出码 0」而 check_vocab 实际 FAIL。
> 2026-10-19 修复：改为与 ③ lane 同口径（取退出码 + 结论行判红）。

> **本表是「这些书在当前工具下是什么状态」的可查记录，不是整改清单。**
> 按 AGENTS「🚦 新规则的适用范围」节第 1 条：**判据变更只对新增书籍生效**，
> 已完工的书**不自动回溯整改**。check_vocab 的 FAIL 判据本身**没有变**——
> 变的是 gate **是否把它计入阻断**。⇒ 这 39 本书在修复前的 gate 结论是**假绿**。

## 统计

- 扫描书目录：**249**（notes/books/ 四个根，含 library/ 或 text/ 的）
- `check_vocab` FAIL > 0 的书：**39**
- FAIL 条数合计：**1392**

## 逐书（FAIL 条数降序）

| 书目录 | FAIL |
|---|---|
| `notes/books/novels/the-room-in-the-ground-by-john-ajvide-lindqvist` | 193 |
| `notes/books/mystery-thriller/the-lost-village-by-camilla-sten` | 126 |
| `notes/books/novels/maybe-once-maybe-twice-by-alison-rose-greenberg` | 124 |
| `notes/books/short-story-anthologies/barron-collected-short-fiction` | 124 |
| `notes/books/novels/the-rules-of-fortune-by-danielle-prescod` | 104 |
| `notes/books/mystery-thriller/devil-inside-by-clay-mcleod-chapman` | 90 |
| `notes/books/novels/golden-boy-by-a-j-symon` | 80 |
| `notes/books/short-story-anthologies/unearthed-new-horror-of-ancient-ruins-by-dan-coxon` | 70 |
| `notes/books/novels/wings-of-starlight-by-allison-saft` | 66 |
| `notes/books/novels/wolftamer-by-maggie-rapier` | 52 |
| `notes/books/novels/as-you-wake-break-the-shell-by-becky-chambers` | 49 |
| `notes/books/novels/a-cozy-holiday-by-denise-stone-and-kels-stone` | 45 |
| `notes/books/non-fiction/the-art-of-thinking-clearly-by-rolf-dobelli` | 37 |
| `notes/books/novels/armor-for-liars-by-s-e-grove` | 36 |
| `notes/books/novels/their-shadows-deep-by-peter-golden` | 29 |
| `notes/books/novels/meet-cute-magic-by-morgan-elizabeth` | 27 |
| `notes/books/mystery-thriller/beware-the-abbott-boys-by-chelsea-ichaso` | 26 |
| `notes/books/mystery-thriller/lies-and-dolls-by-nev-fountain` | 20 |
| `notes/books/novels/traitors-nest-by-frances-hardinge` | 18 |
| `notes/books/novels/theft-by-abdulrazak-gurnah` | 17 |
| `notes/books/novels/the-lost-spectacular-by-zoe-duhaime` | 15 |
| `notes/books/novels/in-a-heartbeat-by-ali-novak` | 10 |
| `notes/books/mystery-thriller/the-man-by-laura-sims` | 9 |
| `notes/books/novels/flesh-by-david-szalay` | 3 |
| `notes/books/short-story-anthologies/aickman-collected-short-fiction` | 3 |
| `notes/books/short-story-anthologies/seven-stories-for-a-summer-afternoon-by-loes-jossy` | 3 |
| `notes/books/novels/a-sea-of-unspoken-things-by-adrienne-young` | 2 |
| `notes/books/novels/i-hope-this-email-finds-you-in-hell-by-mackenzie-reed` | 2 |
| `notes/books/novels/local-gods-by-melinda-salisbury` | 2 |
| `notes/books/novels/everything-was-beautiful-and-nothing-hurt-by-ben-reeves` | 1 |
| `notes/books/novels/rooted-by-leopoldo-gout` | 1 |
| `notes/books/novels/strange-lights-by-mira-gonzalez` | 1 |
| `notes/books/novels/the-last-thing-by-bethany-monaco-smith` | 1 |
| `notes/books/novels/the-runaway-duchess-by-alda-kazmierczak` | 1 |
| `notes/books/novels/the-shadow-king-by-maaza-mengiste` | 1 |
| `notes/books/novels/things-we-never-got-over-by-lucy-score` | 1 |
| `notes/books/non-fiction/why-we-read-shannon-reed-2024` | 1 |
| `notes/books/short-story-anthologies/best-british-short-stories-2023-by-nicholas-royle` | 1 |
| `notes/books/short-story-anthologies/land-of-oz-by-marie-oregan` | 1 |

## 处置口径

- ❌ **不自动回溯整改**：这些书在 2026-10-19 之前已完成并入库，
  按 AGENTS「🚦 新规则的适用范围」第 1 条，判据变更只对新增书籍生效。
- ✅ **新增书籍必须过**：任何新书进 gate 时，② lane 现在会真判红。
- ⏸ **逐本由用户决定**：某本书若被再次打开返修（touched-on-write），
  其词表部分按**新规则**核（AGENTS 第 3 条第 3 行）。
- ⚠️ **报告措辞**：这 39 本书的「gate 退出码 0」若出现在旧报告里，
  应读作「**② lane 未计入该判据**」而非「词表干净」。

## 复算命令

```bash
cd ~/Documents/Works/EnglishRead
for d in notes/books/*/*/; do
  [ -d "$d/library" ] || continue
  n=$(python3 scripts/check_vocab.py "$d" 2>&1 | grep -oE '^--- FAIL \([0-9]+\)' | grep -oE '[0-9]+')
  [ "${n:-0}" -gt 0 ] && echo "$n  $d"
done | sort -rn
```

_生成时间：2026-10-19（Opencode-Mac）_