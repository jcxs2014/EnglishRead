# 夹具：块数超上限

一章 16 个引语块（硬上限 15）。

```bash
bash scripts/chapter.sh "scripts/tests/bookform_blocks/ch01 test.md"
# 期望：❌ 块数：块数 16 超上限 15 …；rc=1
```

2026-10-21 用户拍板：块数不可随意决定，下限 2、上限 15（初始定 10，同日改 15）。
