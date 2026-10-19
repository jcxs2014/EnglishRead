# 派活简报：Maybe Next Time 词汇表重建（ch50–ch58）

> 背景：本书 ch46–ch59 的词汇表是某批子代理「凭印象手挑词条 + 手写例句」产出的，
> 结果 **145/249 行的词头在本章彻底不存在**（如 ch50 的 `TikTok`/`betrayal`，
> 而 ch50 原文通篇无 TikTok），例句 84 条在全书查无（凭空造句）。
> `check_vocab` 报 FAIL 147。
>
> **本批任务 = 用生产工具重建词表**：词头与例句**只能**来自本章 `text/` 的候选池
> （候选池由 `scripts/vocab_candidates.py` 从本章 text/ 逐字抽取），
> 你只负责**选词 + 写中文释义**。

---

## 你的产出物（唯一一个文件）

`.memory/raw-gates/maybe-next-time-by-cesca-major/vocab-fix/plan_ch50_58.json`

格式：

```json
{
  "ch50": {
    "⭐⭐⭐": [["词头", "中文释义"], ["词头", "中文释义"], ...共 6 条],
    "⭐⭐":  [[...], ...共 6 条],
    "⭐":    [[...], ...共 6 条]
  },
  "ch51": { ... },
  ...
  "ch58": { ... }
}
```

**共 9 章**（ch50, ch51, ch52, ch53, ch54, ch55, ch56, ch57, ch58）。

---

## 唯一数据源：候选池文件（已生成，逐章一个）

- `.memory/raw-gates/maybe-next-time-by-cesca-major/vocab-fix/ch50_cands.md`
- …（ch50–ch58 各一个）

每个文件的格式：

```
## ⭐⭐⭐ 高级
- churning :: It was overcast, the sea churning gray, ...
```

`- 词头 :: 例句` —— **词头与例句都是本章原文逐字**（由脚本抽取，不是人工写的）。

### 硬约束（违反 ⇒ 工具拒绝产出，你的这一章白做）

1. **词头必须逐字取自候选池**（大小写照抄，如 `INCREDIBLY`、`Seychelles`）。
   工具会校验「词头在本章语料命中」，自造词头一律被拒。
2. **例句不要写** —— 工具会自己从本章 text/ 抽取，你只写词头和释义。
3. **每章 6/6/6**（高级/进阶/基础各 6 条）。**高级档词头 ≥ 10 字符**，
   进阶档 5–9 字符，基础档短词或专名（地名/人名/品牌/机构）。
   候选池已按此分档（`## ⭐⭐⭐ 高级` 段的就是高级档），**在各段内选**即可。
4. **同一章内不得有重复词头**（跨档也不行）——ch53 旧表就在 `betrayal`/`routine`/`checklist`
   上高级与进阶各写了一遍，是本批要消灭的缺陷。
5. **释义用中文**，格式与本书既有风格一致：
   - 普通词：`「释义；释义」`（分号并列，不超过 8 字 × 2）
   - 专有名词：`「Brighton | 布莱顿（英国海滨城市）」`——带括号说明身份
   - 词组/短语：`「cast a shadow | 投下阴影；笼罩」`

---

## 反例（本批要避免的错误形态）

- ❌ **词头在别章**：`ring light`（旧 ch49 词表）—— ch49 全文无此物
- ❌ **例句是自造的**：`I felt lethargic`（旧 ch46）—— 本章无此句
- ❌ **例句是元叙述**：`the novel's thesis`、`Emma's detachment` —— 不是原文句子
- ❌ **专名当高级词**：`TikTok`/`Netflix`/`Zoom` 属基础档（工具/平台/地名/品牌）
- ❌ **同章重复词头**（见上）

---

## 自检命令（必须跑通再回报）

```bash
cd /Users/jcxs2014/Documents/Works/EnglishRead

# 1) 语法与结构自检
python3 -c "
import json
d=json.load(open('.memory/raw-gates/maybe-next-time-by-cesca-major/vocab-fix/plan_ch50_58.json',encoding='utf-8'))
for ch in ['ch50','ch51','ch52','ch53','ch54','ch55','ch56','ch57','ch58']:
    t=d[ch]; heads=[h for tier in ('⭐⭐⭐','⭐⭐','⭐') for h,_ in t[tier]]
    assert len(t['⭐⭐⭐'])==6 and len(t['⭐⭐'])==6 and len(t['⭐'])==6, (ch, {k:len(v) for k,v in t.items()})
    assert len(heads)==len(set(heads)), (ch, '重复词头')
print('结构 OK')
"

# 2) 工具硬校验（dry-run，**不写盘**）
python3 scripts/repair_vocab_from_text.py "notes/books/novels/maybe-next-time-by-cesca-major" \
  --from-ch 50 --to-ch 58 \
  --plan .memory/raw-gates/maybe-next-time-by-cesca-major/vocab-fix/plan_ch50_58.json \
  --dry-run
```

期望：**9 章全部「补入 54」，无「plan 校验失败」**。

若某章报「词头不在本章」或「本章无含该词的可用句子」，
**从候选池换一个词**（不要改工具、不要手写例句），改完重跑。

---

## 纪律

- **不写盘**：只产出 plan JSON，**不要**跑不带 `--dry-run` 的命令（主会话统一落盘）。
- **不改 md**、不改任何脚本、不执行 `git add` / `git commit`。
- 选词要**贴合本章内容**（本章是 Dan 的信 / 特定场景），不要每章都选同一批通用词。
- 回报格式：每章一行「chNN：高级 a 个 / 进阶 b 个 / 基础 c 个（自检通过）」，
  末尾附「遇到的问题」清单。
