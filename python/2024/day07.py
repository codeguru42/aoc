import timeit

from aocd import get_data


def parse_equations(lines):
    for line in lines:
        result, terms = line.strip().split(":")
        yield int(result), tuple(int(term) for term in terms.strip().split())


def parse(data):
    lines = data.strip().splitlines()
    return list(parse_equations(lines))


def part1(lines):
    pass


def part2(lines):
    pass


def main():
    data = get_data(year=2024, day=7)
    parsed = parse(data)
    print(parsed)
    print("Part 1:", timeit.timeit(lambda: print(part1(parsed)), number=1))
    print("Part 2:", timeit.timeit(lambda: print(part2(parsed)), number=1))


if __name__ == "__main__":
    main()
