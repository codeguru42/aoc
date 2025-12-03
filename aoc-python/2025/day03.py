import operator
import timeit

import pytest
from aocd import get_data


@pytest.mark.parametrize(
    "line, expected",
    (
        ("987654321111111", 98),
        ("811111111111119", 89),
        ("234234234234278", 78),
        ("818181911112111", 92),
    ),
)
def test_max_joltage(line, expected):
    parsed = parse_line(line)
    assert max_joltage(parsed, 2) == expected


def parse(data):
    for line in data.splitlines():
        yield parse_line(line)


def parse_line(line) -> list[int]:
    return [int(char) for char in line.strip()]


def max_digit(line, n, k):
    if len(line) == 1:
        return line[0], []
    i, m = max(enumerate(line[: len(line)-(n - k)]), key=operator.itemgetter(1))
    return m, line[i + 1 :]


def max_second_digit(line):
    i, m = max(enumerate(line), key=operator.itemgetter(1))
    return m, line[i + 1 :]


def joltages(lines):
    for line in lines:
        yield max_joltage(line, 2)


def max_joltage(line, n):
    result = 0
    rest = line
    for k in range(n):
        m, rest = max_digit(rest, n, k + 1)
        result = 10 * result + m
    return result


def part1(lines):
    return sum(joltages(lines))


def part2(lines):
    pass


def main():
    data = get_data(year=2025, day=3)
    parsed = list(parse(data))
    print("Part 1:", timeit.timeit(lambda: print(part1(parsed)), number=1))
    print("Part 2:", timeit.timeit(lambda: print(part2(parsed)), number=1))


if __name__ == "__main__":
    main()
