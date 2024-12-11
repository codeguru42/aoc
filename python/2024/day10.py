import timeit

from aocd import get_data


def parse(data):
    lines = data.splitlines()
    for line in lines:
        yield [int(x) for x in line]


def neighbors(r, c):
    deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for delta in deltas:
        yield r + delta[0], c + delta[1]


def is_in_bounds(r, c, row_count, col_count):
    return 0 <= r < row_count and 0 <= c < col_count


def is_trailhead(r, c, lines):
    row_count = len(lines)
    col_count = len(lines[0])
    for height in range(1, 10):
        if not any(
            is_in_bounds(n_r, n_c, row_count, col_count) and lines[n_r][n_c] == height
            for n_r, n_c in neighbors(r, c)
        ):
            return False
    return True


def part1(lines):
    count = 0
    for r, line in enumerate(lines):
        for c, v in enumerate(line):
            if v == 0:
                if is_trailhead(r, c, lines):
                    count += 1
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
