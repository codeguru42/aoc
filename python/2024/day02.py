import timeit

from aocd import get_data


def parse(data):
    lines = data.splitlines()
    for line in lines:
        yield [int(x) for x in line.strip().split()]


def part1(lines):
    pass


def part2(lines):
    pass


def main():
    data = get_data(year=2024, day=2)
    parsed = list(parse(data))
    print(parsed)
    print("Part 1:", timeit.timeit(lambda: print(part1(parsed)), number=1))
    print("Part 2:", timeit.timeit(lambda: print(part2(parsed)), number=1))


if __name__ == "__main__":
    main()
