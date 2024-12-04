import itertools
import re
import timeit

from aocd import get_data

test_lines = """MMMSXXMASM
MSAMXMSMSA
"""

test_lines2 = """
MMMSX
MSAMX
AMXSX
MSAMA
XMASA
"""


def test_reversed_lines():
    assert reversed_lines(parse(test_lines)) == ["MSAMXXSMMM", "ASMSMXMASM"]


def test_columns():
    expected = [
        "MM",
        "MS",
        "MA",
        "SM",
        "XX",
        "XM",
        "MS",
        "AM",
        "SS",
        "MA",
    ]
    assert columns(parse(test_lines)) == expected


def test_reversed_columns():
    expected = [
        "MM",
        "SM",
        "AM",
        "MS",
        "XX",
        "MX",
        "SM",
        "MA",
        "SS",
        "AM",
    ]
    assert reversed_columns(parse(test_lines)) == expected


def test_down_diagonals():
    expected = [
        "....X",
        "...MM",
        "..ASA",
        ".MMAS",
        "MSXMA",
        "MASA.",
        "MMX..",
        "SX...",
        "X....",
    ]
    assert down_diagonals(parse(test_lines2)) == expected


def test_up_diagonals():
    expected = [
        "M....",
        "MM...",
        "MSA..",
        "SAMM.",
        "XMXSX",
        ".XSAM",
        "..XMA",
        "...AS",
        "....A",
    ]
    assert up_diagonals(parse(test_lines2)) == expected


def parse(data):
    return data.strip().splitlines()


def count_xmas(lines):
    return sum(len(re.findall(r"XMAS", line)) for line in lines)


def part1(lines):
    return (
        count_xmas(lines)
        + count_xmas(reversed_lines(lines))
        + count_xmas(columns(lines))
        + count_xmas(reversed_columns(lines))
        + count_xmas(down_diagonals(lines))
        + count_xmas(reversed_down_diagonals(lines))
        + count_xmas(up_diagonals(lines))
        + count_xmas(reversed_up_diagonals(lines))
    )


def reversed_lines(lines):
    return ["".join(reversed(line)) for line in lines]


def columns(lines):
    return ["".join(line) for line in itertools.zip_longest(*lines, fillvalue=".")]


def reversed_columns(lines):
    return reversed_lines(columns(lines))


def down_diagonals(lines):
    n = len(lines)
    return columns(["." * (n - r) + line[: r + 1] for r, line in enumerate(lines)])[
        1:-1
    ] + columns(line[r:] for r, line in enumerate(lines))


def reversed_down_diagonals(lines):
    return reversed_lines(down_diagonals(lines))


def up_diagonals(lines):
    n = len(lines)
    return columns("." * r + line[: n - r] for r, line in enumerate(lines)) + columns(
        line[n - r :] for r, line in enumerate(lines)
    )


def reversed_up_diagonals(lines):
    return reversed_lines(up_diagonals(lines))


def part2(lines):
    count = 0
    n = len(lines)
    for r, line in enumerate(lines):
        for c, val in enumerate(line):
            if val == "A":
                if 1 <= r < n - 1 and 1 <= c < n - 1:
                    if (lines[r - 1][c - 1] == "M" and lines[r + 1][c + 1] == "S") or (
                        lines[r - 1][c - 1] == "S" and lines[r + 1][c + 1] == "M"
                    ):
                        if (
                            lines[r - 1][c + 1] == "M" and lines[r + 1][c - 1] == "S"
                        ) or (
                            lines[r - 1][c + 1] == "S" and lines[r + 1][c - 1] == "M"
                        ):
                            count += 1
    return count


def main():
    data = get_data(year=2024, day=4)
    parsed = parse(data)
    print("Part 1:", timeit.timeit(lambda: print(part1(parsed)), number=1))
    print("Part 2:", timeit.timeit(lambda: print(part2(parsed)), number=1))


if __name__ == "__main__":
    main()
