import timeit

from aocd import get_data


def parse(data):
    lines = data.strip().split("\n")
    for line in lines:
        cards, bid = line.strip().split()
        yield cards, int(bid)


def part1(lines):
    pass


def part2(lines):
    pass


def main():
    data = get_data(year=2023, day=7)
    parsed = list(parse(data))
    print(parsed)
    print(part1(parsed))
    print(part2(parsed))
    print("Part 1:", timeit.timeit(lambda: part1(parsed), number=1))
    print("Part 2:", timeit.timeit(lambda: part2(parsed), number=1))


if __name__ == "__main__":
    main()
