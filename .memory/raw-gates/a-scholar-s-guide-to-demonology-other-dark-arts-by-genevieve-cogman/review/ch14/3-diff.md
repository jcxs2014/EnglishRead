# ch14 对账（R1 素读 ↔ `ch14 chapter thirteen.md`）

素读：`review/ch14/1-suread.json`（20 条，20/20）。md：14 块。

## 漏（素读有、md 无）

| 素读事实 | 原文 | 处置 |
|---|---|---|
| 猫第一件事是**点早餐**（「把自助餐端上来」） | `text/ch14_chapter_thirteen.txt:1003` 字符位 `Kindly present the buffet` | 块 1–2 未单独成块；导航以「会点餐要早餐」带过 |
| 校长已起床穿戴好：**米色两件套＋珍珠**，茶与吐司、桌子摆了两份 | `:11393` | 未写；导航只写「早餐、吐司和茶维持体面外壳」 |
| Faust（柯基）见猫进门**竖起全身毛跳起来** | `:11804` | 未成块 |
| 校长说亲自教的只是「 handful of sixth-formers. Nobody below that level」 | `:33235` | 块 7 中文概括为「等到六、七年级」——与原文一致，但「她亲自教」这层未译出 |
| 她给菲丝「改天再来、全部取消、记忆抹掉」这个选项 | `:35164` | 块 14 有 |
| Anne Bredon 是**作为拉丁文教师**进来的，学校不知道她私下那套的全部细节 | `:12116` 前后 | 块 11 中文只写「企图占用学校资源」 |

## 编（md 有、原文无）

| 位置 | md 写法 | 原文 | 档位 | 处置 |
|---|---|---|---|---|
| 导航 Tropes 3 | 「一所有**校董会**、有教研、有年级制度的学校」 | 全书 `grep -i "governors\|board of"` **0 命中**（exit=1） | 提示 | 删「有校董会、」 |
| 块 10 为什么 | 「三个否定加一个肯定」 | `:295` 一带原文是 `not necessarily evil` + `not necessarily good` + `necessarily extremely dangerous`＝**两否定一肯定** | 提示 | 改「两个否定加一个肯定」 |
| 块 13 为什么 | 「**括号里**那句『契约是我留下的』」 | 原文 `which I admit I left there` 是定语从句，不在括号里 | 提示 | 改「那句『我承认是我留在那儿的』」 |

## 错（两边都有、不一致）

无。

## 已核实为正确

- 「Alastor, Duke of Hell, Executioner of Lucifer, Hell's Commissioner of Public Works」：块 3 引语逐字。
- 「契约是她念出声就算数」：`:4162` `You have bound me to you with your skilful contract`。
- 「猫的形态是她强加的」：同上，`bound` 之后她说「我要一只猫」，md 未写反方向。
- 「最初的形态是女修院、现形态追溯到十七世纪」：块 8 逐字。
- 「指挥链直接通到王座」：块 9 逐字。
- 「恶魔未必邪恶、也未必善良、但一定极其危险」：块 10 逐字。
- 「Bredon 被当场除名」：块 11 逐字 `we removed her on the spot`。
- 「三个品质：有伦理、够好奇、够鲁莽」：块 13 逐字。
- 「退路：可以不做，连记忆也能处理」：块 14 逐字。
- 「饼干证据」：块 6 逐字（`chocolate digestives, or ginger snaps, or Hobnobs`）。
