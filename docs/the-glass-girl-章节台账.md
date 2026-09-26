---
状态: 未读
---

# The Glass Girl 章节台账（2026-09-26 建）

> **本文件是写作期的取名与归属依据**，不是精读内容。
> `text/` 与 epub 的 spine **一一对应**（54 件），故本台账也按 1:1 编号；
> 重跑 `extract_chapters` 应得同样 54 件与同样顺序。

## 语料层验收状态（P0-0）

```
verify_corpus --expect 54   --expect-source "版权页目录 48 正文章 + Prologue + Author's Note
                  + nav 未列但含正文的 4 页" \
  --anchors "ch15=Sarah; ch31=Hayley; ch38=Lisa" \
  --shared "Laurel,Gideon,Bella,Tracy,Holly,Ricci"
→ PASS（FAIL 0 / WARN 0）
```

`--min-len 200`（本书专用，**不是全局默认**）：`Day Twenty-Two` 只有 427 字符
真实正文，默认 600 会把它当噪声丢掉。

## 三条已定规则

1. **Prologue 占两件**（ch01 题词诗 + ch02 正文）——md 层各写一件，
   `ch02 prologue.md` 承接 `ch01 prologue.md`。**text/ 不合并**，保持与 spine 一一对应。
2. **nav 未列的 6 件用简单命名**（下表 ★），不追求还原原书标题。
3. **`ch12_day_one` 与 `ch40_day_one` 同名不处理**——md 文件名以 ch 号开头即唯一。

## 章节台账（54 件）

| # | text 件 | 标题 | 类型 | 字符 | md 文件名 |
|---|---|---|---|---|---|
| 01 | `ch01_prologue` | Prologue 题词诗 ★ | 题词 | 750 | `ch01 prologue.md` |
| 02 | `ch02_chap2` | Prologue 正文 ★ | 序章 | 2,627 | `ch02 prologue.md` |
| 03 | `ch03_friday` | Friday | 正文 | 39,012 | `ch03 friday.md` |
| 04 | `ch04_saturday` | Saturday | 正文 | 50,328 | `ch04 saturday.md` |
| 05 | `ch05_chap5` | 题词：everyone is gone ★ | 题词 | 1,108 | `ch05 everyone_is_gone.md` |
| 06 | `ch06_sunday` | Sunday | 正文 | 24,332 | `ch06 sunday.md` |
| 07 | `ch07_monday` | Monday | 正文 | 9,048 | `ch07 monday.md` |
| 08 | `ch08_tuesday` | Tuesday | 正文 | 16,653 | `ch08 tuesday.md` |
| 09 | `ch09_wednesday` | Wednesday | 正文 | 9,545 | `ch09 wednesday.md` |
| 10 | `ch10_thursday` | Thursday | 正文 | 29,302 | `ch10 thursday.md` |
| 11 | `ch11_chap11` | 无标题章（Part Two 起始） ★ | 正文 | 42,975 | `ch11 part_two.md` |
| 12 | `ch12_day_one` | Day One | 正文 | 29,722 | `ch12 day_one.md` |
| 13 | `ch13_day_two` | Day Two | 正文 | 10,857 | `ch13 day_two.md` |
| 14 | `ch14_day_three` | Day Three | 正文 | 30,967 | `ch14 day_three.md` |
| 15 | `ch15_day_four` | Day Four | 正文 | 33,262 | `ch15 day_four.md` |
| 16 | `ch16_day_five` | Day Five | 正文 | 10,305 | `ch16 day_five.md` |
| 17 | `ch17_day_six` | Day Six | 正文 | 4,788 | `ch17 day_six.md` |
| 18 | `ch18_day_seven` | Day Seven | 正文 | 3,308 | `ch18 day_seven.md` |
| 19 | `ch19_day_eight` | Day Eight | 正文 | 14,509 | `ch19 day_eight.md` |
| 20 | `ch20_day_nine` | Day Nine | 正文 | 6,013 | `ch20 day_nine.md` |
| 21 | `ch21_day_ten` | Day Ten | 正文 | 9,633 | `ch21 day_ten.md` |
| 22 | `ch22_day_eleven` | Day Eleven | 正文 | 4,491 | `ch22 day_eleven.md` |
| 23 | `ch23_day_twelve` | Day Twelve | 正文 | 4,573 | `ch23 day_twelve.md` |
| 24 | `ch24_day_thirteen` | Day Thirteen | 正文 | 2,368 | `ch24 day_thirteen.md` |
| 25 | `ch25_day_fourteen` | Day Fourteen | 正文 | 5,521 | `ch25 day_fourteen.md` |
| 26 | `ch26_day_fifteen` | Day Fifteen | 正文 | 8,040 | `ch26 day_fifteen.md` |
| 27 | `ch27_day_sixteen` | Day Sixteen | 正文 | 2,051 | `ch27 day_sixteen.md` |
| 28 | `ch28_day_seventeen` | Day Seventeen | 正文 | 4,025 | `ch28 day_seventeen.md` |
| 29 | `ch29_day_eighteen` | Day Eighteen | 正文 | 12,671 | `ch29 day_eighteen.md` |
| 30 | `ch30_day_nineteen` | Day Nineteen | 正文 | 1,931 | `ch30 day_nineteen.md` |
| 31 | `ch31_day_twenty` | Day Twenty | 正文 | 16,979 | `ch31 day_twenty.md` |
| 32 | `ch32_day_twenty_one` | Day Twenty One | 正文 | 5,058 | `ch32 day_twenty_one.md` |
| 33 | `ch33_day_twenty_two` | Day Twenty Two | 正文 | 396 | `ch33 day_twenty_two.md` |
| 34 | `ch34_day_twenty_four` | Day Twenty Four | 正文 | 4,747 | `ch34 day_twenty_four.md` |
| 35 | `ch35_day_twenty_five` | Day Twenty Five | 正文 | 8,682 | `ch35 day_twenty_five.md` |
| 36 | `ch36_day_twenty_six` | Day Twenty Six | 正文 | 3,684 | `ch36 day_twenty_six.md` |
| 37 | `ch37_day_twenty_seven` | Day Twenty Seven | 正文 | 1,996 | `ch37 day_twenty_seven.md` |
| 38 | `ch38_day_twenty_eight` | Day Twenty Eight | 正文 | 10,021 | `ch38 day_twenty_eight.md` |
| 39 | `ch39_day_twenty_nine` | Day Twenty Nine | 正文 | 5,191 | `ch39 day_twenty_nine.md` |
| 40 | `ch40_day_one` | Day One | 正文 | 975 | `ch40 day_one.md` |
| 41 | `ch41_chap41` | 无标题章（Part Four 起始） ★ | 正文 | 27,376 | `ch41 part_four.md` |
| 42 | `ch42_have_you_gone_to_your_first_group_meetin` | Have You Gone To Your First Group Meetin | 正文 | 6,498 | `ch42 have_you_gone_to_your_first_group_meetin.md` |
| 43 | `ch43_school_may_be_stressful_expect_the_unexp` | School May Be Stressful Expect The Unexp | 正文 | 13,730 | `ch43 school_may_be_stressful_expect_the_unexp.md` |
| 44 | `ch44_family_can_be_a_challenge` | Family Can Be A Challenge | 正文 | 16,932 | `ch44 family_can_be_a_challenge.md` |
| 45 | `ch45_chap45` | 信（Dear Dad） ★ | 书信 | 939 | `ch45 dear_dad.md` |
| 46 | `ch46_was_there_a_routine_you_liked_at_sonoran` | Was There A Routine You Liked At Sonoran | 正文 | 1,518 | `ch46 was_there_a_routine_you_liked_at_sonoran.md` |
| 47 | `ch47_people_will_drift_back_to_you` | People Will Drift Back To You | 正文 | 1,639 | `ch47 people_will_drift_back_to_you.md` |
| 48 | `ch48_everybody_is_trying_in_their_own_way` | Everybody Is Trying In Their Own Way | 正文 | 3,553 | `ch48 everybody_is_trying_in_their_own_way.md` |
| 49 | `ch49_do_you_feel_safe_today` | Do You Feel Safe Today | 正文 | 9,220 | `ch49 do_you_feel_safe_today.md` |
| 50 | `ch50_one_friend_is_all_you_need` | One Friend Is All You Need | 正文 | 6,341 | `ch50 one_friend_is_all_you_need.md` |
| 51 | `ch51_today_you_will_rediscover_something_you_` | Today You Will Rediscover Something You  | 正文 | 3,278 | `ch51 today_you_will_rediscover_something_you_.md` |
| 52 | `ch52_if_it_isn_t_working_fix_it` | If It Isn T Working Fix It | 正文 | 1,219 | `ch52 if_it_isn_t_working_fix_it.md` |
| 53 | `ch53_you_can_start_over_as_many_times_as_it_t` | You Can Start Over As Many Times As It T | 正文 | 4,678 | `ch53 you_can_start_over_as_many_times_as_it_t.md` |
| 54 | `ch54_author_s_note` | Author S Note | 作者注 | 4,978 | `ch54 author_s_note.md` |

## 写 ch01–ch10 时的实验分配（AGENTS 第 8 条 8.5）

| 章 | 臂 | 写法 |
|---|---|---|
| ch01 prologue（题词诗） | **预防** | 8.1 证据先行 + 8.2 五条禁令 + 8.3 抄模板 |
| ch02 prologue（正文） | 旧法 | 照常写，不刻意守禁令 |
| ch03 friday | **预防** | 同 ch01 |
| ch04 saturday | 旧法 | |
| ch05 everyone is gone（题词） | **预防** | 同 ch01 |
| ch06 sunday | 旧法 | |
| ch07 monday | **预防** | 同 ch01 |
| ch08 tuesday | 旧法 | |
| ch09 wednesday | **预防** | 同 ch01 |
| ch10 thursday | 旧法 | |

**每章写完记录三项**（缺一不可，防"少写"冒充"防住了"）：

| 章 | 臂 | 报警数（越少越好） | 精读块数（不能少） | 子项完整度（不能降） |
|---|---|---|---|---|
| ch01 | 预防 | | | |
| ch02 | 旧法 | | | |

报警数取 `audit_numbers` / `sweep_analysis_inline` / `check_anchor` /
`audit_structure` 四脚本之和，**分档报告不看总数**（四类基线差两个数量级：
计数断言 4.2/章、分析层英文 3.2/章、关键词 0.1/章、结构 0.0/章）。

**基线**：11 本 323 章旧法 = **7.5 条/章**。若预防侧 ≈ 0 而旧法侧复现基线，
则预防成立。
