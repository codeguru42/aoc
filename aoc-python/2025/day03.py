import timeit

from aocd import get_data


def parse(data):
    for line in data.splitlines():
        yield [int(char) for char in line.strip()]


def part1(lines):
    pass


def part2(lines):
    pass


def main():
    data = get_data(year=2025, day=3)
    parsed = list(parse(data))
    print(parsed)
    print("Part 1:", timeit.timeit(lambda: print(part1(parsed)), number=1))
    print("Part 2:", timeit.timeit(lambda: print(part2(parsed)), number=1))


if __name__ == "__main__":
    main()
