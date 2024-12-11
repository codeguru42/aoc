import timeit

from aocd import get_data

test_input = """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""


def test_part1():
    lines = list(parse(test_input))
    assert part1(lines) == 36


def parse(data):
    lines = data.strip().splitlines()
    for line in lines:
        yield [int(x) for x in line]


def neighbors(r, c):
    deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for delta in deltas:
        yield r + delta[0], c + delta[1]


def is_in_bounds(r, c, row_count, col_count):
    return 0 <= r < row_count and 0 <= c < col_count


def get_score(r, c, lines):
    width = len(lines)
    height = len(lines[0])
    if not is_in_bounds(r, c, width, height):
        return 0
    if lines[r][c] == 9:
        return 1
    return sum(
        get_score(n_r, n_c, lines)
        for n_r, n_c in neighbors(r, c)
        if is_in_bounds(n_r, n_c, width, height) and lines[n_r][n_c] == lines[r][c] + 1
    )


def part1(lines):
    count = 0
    for r, line in enumerate(lines):
        for c, v in enumerate(line):
            if v == 0:
                count += get_score(r, c, lines)
    return count


def part2(lines):
    pass


def main():
    data = get_data(year=2024, day=10)
    parsed = list(parse(data))
    print(parsed)
    print("Part 1:", timeit.timeit(lambda: print(part1(parsed)), number=1))
    print("Part 2:", timeit.timeit(lambda: print(part2(parsed)), number=1))


if __name__ == "__main__":
    main()
