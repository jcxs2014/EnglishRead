import sys

# (file, up_row, down_row)  -> move up_row from basic to intermediate, down_row from intermediate to basic
SWAPS = [
    (
        "notes/books/novels/kiss-slay-replay-by-rachel-harrison/ch11 part 2 the loop restarts.md",
        "| windshield | 挡风玻璃 | my view out the windshield transforms |",
        "| hornets | 大黄蜂，胡蜂（hornet 的复数） | There are hornets in my lungs. |",
    ),
    (
        "notes/books/novels/kiss-slay-replay-by-rachel-harrison/ch13 part 2 only way out is through.md",
        "| handshake | 握手（此处指两人约定好的暗号式握手） | He initiates our elaborate secret handshake that neither of us quite remembers. |",
        "| pity | 怜悯，同情 | “How are you?” Steph asks, with overt pity. |",
    ),
]

for path, up, down in SWAPS:
    s = open(path, encoding="utf-8").read()
    lines = s.split("\n")
    assert s.count(up) == 1, (path, "up row count", s.count(up))
    assert s.count(down) == 1, (path, "down row count", s.count(down))

    # 1. remove down row (from 进阶)
    i = lines.index(down)
    del lines[i]
    # 2. swap up row (in 基础) for down row
    j = lines.index(up)
    lines[j] = down
    # 3. re-fetch 基础 heading index (indices shifted by the deletion above)
    h = lines.index("### ⭐ 基础")
    lines.insert(h, up)

    open(path, "w", encoding="utf-8").write("\n".join(lines))
    print(path, "swapped:", up.split("|")[1].strip(), "<->", down.split("|")[1].strip())
