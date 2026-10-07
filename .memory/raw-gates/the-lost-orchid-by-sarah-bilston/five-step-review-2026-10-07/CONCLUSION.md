# The Lost Orchid 五步审查结论
2026-10-07 | ZCode-Mac | 同会话五步审查

## 审查结果
- 阻断型：0
- 提示型：20条（WARN：17条词长≥9字符+3条B类语料缺失，均只记不改）
- 假红型：0
- 修复：无需修复

## 五步明细
a步（门禁全量）: verify_quotes 298/298 ✅ | check_vocab FAIL=0 ✅ | check_entities 0 ✅ | corruption_scan 0 ✅ | sweep_full 279/279 ✅
b步（逐章归属）: 279/279 本章命中 ✅
c步（结构扫描）: audit_structure 0缺陷 ✅ | check_overview_full 整串33/33 ✅ | 章节标签19/19对 ✅
d步（语义二审）: sweep_analysis_inline 1🔶假阳（已核实为原文真实用法）✅ | check_anchor 0 ✅ | audit_numbers 0不符 ✅ | check_xref_indep 0报警 ✅
e步（总览层）: verify_overview_quotes 19/19 ✅ | check_xref_zh 1引用（正确）✅

## 附注
- 本书为非虚构（Harvard UP 2025），目录误置于novels/，但不影响精读格式
- chNN编号=书内章号+1（ch01为序章占位，ch02=Chapter 1，ch28=尾声）
