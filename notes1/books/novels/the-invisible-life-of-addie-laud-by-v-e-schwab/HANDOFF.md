# The Invisible Life of Addie LaRue 精读进度 Handoff

## 当前进度

已完成 **39/108 章** 精读，分 7 批提交：

| 批次 | 章节 | commit hash |
|------|------|-----------|
| 批1 | ch01-015 | 65f5a12 |
| 批2 | ch016-018 | 275e911 |
| 批3 | ch019-021 | 5fca5f6 |
| 批4 | ch022-024 | f01cbbf |
| 批5 | ch025-027 | ecaadcb |
| 批6 | ch028-030 | 92a6614 |
| 批7 | ch031-036 | 1005fa9 |
| 批8 | ch037-038 | c440d7c（部分，ch38 待提交） |

**注意**：ch39 文件尚未创建，需继续编写。

## 结构说明

- 书籍有 7 个 Part，章节编号在每个 Part 重新开始（Chapter I, II, III...）
- 全书共 108 个 text 文件（含 Part 分隔页），实际正文章节约 85 章
- 命名方案：`chNN_<keyplot>.md`（与 text/ 文件对应）

## 待办事项

### 立即任务
1. 创建 ch39（Chapter V, 2014 NYC, Addie 带 Henry 去 Fourth Rail 秘密俱乐部）
2. 提交 ch38-39 批次

### 剩余章节
- ch040-108（Part Three 到 Part Seven）
- 总览三篇：概述.md + 金句精选.md + 情感节点.md
- 最终验收：独立审查五步法 + verify_overview_quotes

## 格式规范

### 每章文件结构
```
---
状态: 未读
modified: "2026-09-04"
---

# NN. 章标题

## 本章导航
- 一句话概括
- 情感弧线位置：升温 / 高潮 / 转折 / 低谷 / 回落
- Tropes 兑现/反转
- 人物弧线
- 叙事手法

## 精读（3-8 处，每处 ≤4 行）
> **原句 N:** 英文原句

中文理解

**关键词**：2-3 个

**为什么这样写**

**读者视角提示**

## 本章词汇
### ⭐⭐⭐ 高级
### ⭐⭐ 进阶
### ⭐ 基础

## 一句话总结
```

### 引用块规则
- `>` 引用块只包含原句英文
- 中文理解/关键词/为什么这样写/读者视角提示在引用块外
- 引用块与解读之间留空行

### 词汇表规则
- 三档：⭐⭐⭐ 高级 / ⭐⭐ 进阶 / ⭐ 基础
- 表格格式：`| 词/短语 | 释义 | 例句 |`
- 例句直接从原文复制，不改写
- 每个词条写入前必须 `grep -i "word" text/chNN.txt` 验证真实存在

## 验证工具

每章写完立即跑三件套：

```bash
cd /Users/jcxs2014/Documents/Works/EnglishRead

# 引文逐字（必须 100%）
python3 scripts/verify_quotes.py "notes/books/novels/the-invisible-life-of-addie-laud-by-v-e-schwab" "notes/books/novels/the-invisible-life-of-addie-laud-by-v-e-schwab/library/V. E. Schwab - The Invisible Life of Addie LaRue (Tom Doherty Associates) - libgen.li.epub"

# 词汇表真实性（FAIL=0）
python3 scripts/check_vocab.py "notes/books/novels/the-invisible-life-of-addie-laud-by-v-e-schwab"

# 梗概实体一致性
python3 scripts/check_entities.py "notes/books/novels/the-invisible-life-of-addie-laud-by-v-e-schwab"
```

### 提交规则
- 每批 3 章（三章一批）
- commit 前三件套必须全绿
- commit message 格式：`books: add The Invisible Life of Addie LaRue chNN-NN 精读`
- 必须包含 co-author trailer：`Co-authored-by: CommandCodeBot <noreply@commandcode.ai>`

### 常见 FAIL 处理
1. **引文 FAIL**：检查原文是否一致（注意空格、标点、大小写）
2. **词汇 FAIL**：词条未命中本章 → 例句中找不到该词 → 改用 `grep` 验证后的真实词
3. **词汇 WARD**：工具建议分档调整 → 移动词条到合适档位

## 重要提醒

1. **原文先行**：精读任何章节前，必须先把该章原文放入上下文（text/chNN.txt）
2. **引文逐字**：所有英文引语必须逐字取自提取文本，需省略中间文字用 `…` 且省略号两侧都必须是原词
3. **禁止凭记忆引用原句**：这是历史教训（Nabokov's Dozen 与 100 Great 两次整批作废）
4. **内联 Gate**：每章写完立即跑 verify_quotes + check_vocab，FAIL=0 才推进下一章
5. **批次节奏**：一次会话处理 ≤5 篇，写完立即跑核验

## 总览三篇（最后写）

全书完成后创建：
- `概述.md`：全书梗概（6-8 段）+ 主题（3 个）+ 人物弧光（主角各一段）
- `金句精选.md`：25-30 句，每句 4 子项（中文 / 上下文 / 为什么重要 / 呼应关系）
- `情感节点.md`：8-10 个节点，每节点叙事概括 + 2-3 句关键引语

总览完成后单独跑：
```bash
python3 scripts/verify_overview_quotes.py "notes/books/novels/the-invisible-life-of-addie-laud-by-v-e-schwab" "notes/books/novels/the-invisible-life-of-addie-laud-by-v-e-schwab/library/V. E. Schwab - The Invisible Life of Addie LaRue (Tom Doherty Associates) - libgen.li.epub"
```

## 联系方式

如有问题，请在 COLLABORATION.md 留言。

---
生成时间：2026-09-04
