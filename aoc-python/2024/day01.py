import timeit
from typing import Counter

from aocd import get_data


def parse(data):
    lines = data.splitlines()
    for line in lines:
        x, y = line.strip().split()
        yield int(x), int(y)


def part1(lines):
    left, right = zip(*lines)
    s = zip(sorted(left), sorted(right))
    return sum(abs(l - r) for l, r in s)


def part2(lines):
    left, right = zip(*lines)
    counts = Counter[int](right)
    return sum(l * counts[l] for l in left)


def main():
    data = get_data(year=2024, day=1)
    parsed = list(parse(data))
    print("Part 1:", timeit.timeit(lambda: print(part1(parsed)), number=1))
    print("Part 2:", timeit.timeit(lambda: print(part2(parsed)), number=1))


if __name__ == "__main__":
    main()
