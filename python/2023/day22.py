import timeit
from dataclasses import dataclass

from aocd import get_data


@dataclass
class Point:
    x: int
    y: int
    z: int


def parse(data):
    lines = data.splitlines()
    for line in lines:
        top, bottom = line.split("~")
        x1, y1, z1 = top.split(",")
        x2, y2, z2 = bottom.split(",")
        yield Point(x=x1, y=y1, z=z1), Point(x=x2, y=y2, z=z2)


def part1(lines):
    pass


def part2(lines):
    pass


def main():
    data = get_data(year=2023, day=22)
    bricks = list(parse(data))
    print(bricks)
    print("Part 1:", timeit.timeit(lambda: print(part1(bricks)), number=1))
    print("Part 2:", timeit.timeit(lambda: print(part2(bricks)), number=1))


if __name__ == "__main__":
    main()
