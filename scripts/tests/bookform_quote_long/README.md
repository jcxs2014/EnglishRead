# 夹具：引语偏长（提示型）

`ch01 test.md` 的引语约 240 词，超过 `bookform.LONG_QUOTE_WORDS = 100`。

**期望**：`bash scripts/chapter.sh "scripts/tests/bookform_quote_long/ch01 test.md"`
- 输出 `⚠️ 引语偏长 1 块 >100 词`
- **退出码 0**（长度是提示型，不判红）

## 为什么要有这个夹具

2026-10-21 `don-t-leave-her-alone` 整本返工：引语中位 168 词、72% 超 100 词，
而当时 19 个 lane 全绿——长度这一层没有任何探针。夹具保证这条提示不会在某次重构里被静默删掉。
