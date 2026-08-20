# BOOT.md — Hermes 会话启动记忆约定

## 命名约定
- 本目录按项目存放记忆，文件统一命名为 `<project>_MEMORY.md`。
- 当前：`<project>_MEMORY.md` 对应 EnglishRead 项目（英文精读 + 多IDE协作板）。

## 每个新会话开始时，按顺序做
1. 读取 `<project>_MEMORY.md` 全文，注入上下文作为长期约定。
2. 读取当日 `YYYY-MM-DD.md`（若不存在则跳过），获取最近动态。

## 写入纪律
- **长期约定** → 更新 `<project>_MEMORY.md`（按节归类，保持可读即可，无硬长度限制）。
- **当日事项** → 追加到 `YYYY-MM-DD.md`：若当日文件不存在，先创建（`touch`），再 append；已存在则 append 到末尾，不覆盖历史。
- 用文件工具（Write/Edit）维护，不要用内置 `memory` 工具写大量内容。

## 为何不用内置 `memory` 工具
内置工具：2200 字符硬上限、磁盘漂移守卫、单机不随 git 同步。本目录 git 跟踪、跨设备、无上限、无漂移锁。内置工具仅适合极轻量的跨会话小事实。
