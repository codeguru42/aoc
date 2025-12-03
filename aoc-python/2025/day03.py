import operator
import timeit

from aocd import get_data


def parse(data):
    for line in data.splitlines():
        yield [int(char) for char in line.strip()]


def max_digit(line):
    if len(line) == 1:
        return line[0], []
    i, m = max(enumerate(line[:-1]), key=operator.itemgetter(1))
    return m, line[i + 1 :]


def joltages(lines):
    for line in lines:
        m1, rest = max_digit(line)
        m2, _ = max_digit(rest)
        yield 10 * m1 + m2


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
