import timeit

from aocd import get_data

from int_code import parse


def part1(program):
    pass


def part2(program):
    pass


def main():
    data = get_data(year=2019, day=19)
    parsed = parse(data)
    print(parsed)
    print("Part 1:", timeit.timeit(lambda: print(part1(parsed)), number=1))
    print("Part 2:", timeit.timeit(lambda: print(part2(parsed)), number=1))


if __name__ == "__main__":
    main()
