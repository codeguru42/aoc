import json
import timeit

from aocd import get_data


def parse(data):
    return json.loads(data)


def part1(data):
    pass


def part2(data):
    pass


def main():
    data = get_data(year=2015, day=12)
    parsed = parse(data)
    print(parsed)
    print("Part 1:", timeit.timeit(lambda: print(part1(parsed)), number=1))
    print("Part 2:", timeit.timeit(lambda: print(part2(parsed)), number=1))


if __name__ == "__main__":
    main()
