import timeit

from aocd import get_data


def parse(data):
    return data.split("\n")


def expand_rows(universe):
    for row in universe:
        yield row
        if all(c == "." for c in row):
            yield row


def expand_columns(universe):
    transposed = zip(*universe)
    yield from expand_rows(transposed)


def expand(universe):
    universe = list(expand_rows(universe))
    return expand_columns(universe)


def part1(universe):
    pass


def part2(universe):
    pass


def main():
    data = get_data(year=2023, day=11)
    parsed = parse(data)
    universe = list(expand(parsed))
    for row in universe:
        print(row)
    print(part1(universe))
    print(part2(universe))
    print("Part 1:", timeit.timeit(lambda: part1(parsed), number=1))
    print("Part 2:", timeit.timeit(lambda: part2(parsed), number=1))


if __name__ == "__main__":
    main()
