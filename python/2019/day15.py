import timeit
from enum import IntEnum

from aocd import get_data

from int_code import parse


class Movement(IntEnum):
    NORTH = 1
    SOUTH = 2
    WEST = 3
    EAST = 4


class Station(IntEnum):
    WALL = 0
    MOVED = 1
    OXYGEN = 2


def part1(lines):
    pass


def part2(lines):
    pass


def main():
    data = get_data(year=2019, day=15)
    parsed = parse(data)
    print(parsed)
    print("Part 1:", timeit.timeit(lambda: print(part1(parsed)), number=1))
    print("Part 2:", timeit.timeit(lambda: print(part2(parsed)), number=1))


if __name__ == "__main__":
    main()
