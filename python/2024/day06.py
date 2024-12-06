import timeit

from aocd import get_data


def find_start(lines):
    for x, line in enumerate(lines):
        for y, c in enumerate(line):
            if c == "^":
                return x, y


def parse(data):
    lines = data.splitlines()
    x, y = find_start(lines)
    return x, y, lines


def part1(x, y, m):
    pass


def part2(x, y, m):
    pass


def main():
    data = get_data(year=2024, day=6)
    x, y, m = parse(data)
    print("Part 1:", timeit.timeit(lambda: print(part1(x, y, m)), number=1))
    print("Part 2:", timeit.timeit(lambda: print(part2(x, y, m)), number=1))


if __name__ == "__main__":
    main()
