---
name: englishread-memory-index
description: EnglishRead 工作区跨会话记忆索引
metadata:
  type: user
---

# EnglishRead 记忆索引

> 本文件 = **记忆索引**（不包含规则内容，规则见根 AGENTS.md 和 docs/新书启动模板.md）。
> 新会话读取顺序：system-reminder → docs/新书启动模板.md → 根 AGENTS.md。

## 核心规则文档

| 文档 | 位置 | 用途 |
|------|------|------|
| 精读执行规则 | `AGENTS.md`（根目录） | 完整执行规则（格式/门禁/工具链/git 策略） |
| **新书启动模板** | `docs/新书启动模板.md` | **每本新书开工前必读**，含执行规则速查 + 历史坑表 |
| 协作消息板 | `COLLABORATION.md` | 跨 IDE 实时消息（newest first） |

## 重要记忆（按时间倒序）

### 2026-08-30 新增
- **Barron's 批次 928 条 A 类虚构**：`check_vocab` 工具盲区——"（未出现在原文）"标注绕过工具检测，52篇全部存在。修复后 FAIL=0 ✅，WARN=72（B类）。详见 `docs/新书启动模板.md` 第5条。
- **check_vocab 标注盲区**：工具只检词频/例句前20字符/分档，不识别中文单元格。独立审查时必须 grep "（未出现在原文）"全文，有输出即 A 类虚构。

### 2026-08-29 新增
- **Room in the Ground 审查整改**：19 文件名偏移 + 5 跨章错植 + 7 cross-ref 联动修复 + 总览 8 处说话人反转。verify 235/235 ✅，FAIL=0。
- **AGENTS.md 第 10 条固化**：独立审查 SOP 五步法 + 完成报告硬要求 + 七类高发坑位。

### 历史教训
- Book Lovers 言情用逐句格式写到 35 篇崩坏重做
- 100 Great 两次大量生成后期衰减实证
- ~20 处"引语换新句、分析停旧句"在 verify_quotes 全绿下漏网
- NS 报告"101/101 ✅"重跑实为 108/109 含 1 FAIL
- 多 IDE 并行：git add -A 裹挟 / COLLABORATION.md 覆写 / amend 改写他实例 commit

## 工具链

| 工具 | 用途 |
|------|------|
| `extract_chapters.py` | epub → 逐章 text/ |
| `verify_quotes.py` | 引语逐字门禁 |
| `check_vocab.py` | 词汇表真实性（FAIL=0 才推进）|
| `check_entities.py` | 梗概实体一致性 |
| `check_chapter_quotes.py` | 逐章归属校验（凡有 text/ 必跑）|
| `audit_book.py` | 一键总账（commit 前必跑）|

## 推送策略
- commit 自由；push 仅限批次定稿/重大交付/明确指令
- 多 IDE 并行时禁止 `git add -A` / `git add .`
