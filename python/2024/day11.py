import timeit

from aocd import get_data


def parse(data):
    return [int(x) for x in data.strip().split()]


def part1(lines):
    pass


def part2(lines):
    pass


def main():
    with open("day11.txt") as f:
        data = f.read()
    parsed = parse(data)
    print(parsed)
    print("Part 1:", timeit.timeit(lambda: print(part1(parsed)), number=1))
    print("Part 2:", timeit.timeit(lambda: print(part2(parsed)), number=1))


if __name__ == "__main__":
    main()
