import timeit

from aocd import get_data


def parse(data):
    for line in data.splitlines():
        for range in line.split(','):
            yield tuple(map(int, range.split('-')))


def is_invalid(ident):
    s = str(ident)
    return s[:len(s) // 2] == s[len(s) // 2:]


def gen_ranges(ranges):
    for a, b in ranges:
        for i in range(a, b + 1):
            yield i


def part1(ranges):
    return sum(i for i in gen_ranges(ranges) if is_invalid(i))

def part2(lines):
    pass


def main():
    data = get_data(year=2025, day=2)
    parsed = list(parse(data))
    print("Part 1:", timeit.timeit(lambda: print(part1(parsed)), number=1))
    print("Part 2:", timeit.timeit(lambda: print(part2(parsed)), number=1))


if __name__ == "__main__":
    main()
