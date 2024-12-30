import re
import timeit
from dataclasses import dataclass

from aocd import get_data


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Robot:
    p: Point
    v: Point


def parse(data):
    lines = data.strip().splitlines()
    for line in lines:
        match = re.match(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line.strip())
        yield Robot(
            Point(int(match.group(1)), int(match.group(2))),
            Point(int(match.group(3)), int(match.group(4))),
        )


def part1(lines):
    pass


def part2(lines):
    pass


def main():
    data = get_data(year=2024, day=14)
    parsed = list(parse(data))
    print(parsed)
    print("Part 1:", timeit.timeit(lambda: print(part1(parsed)), number=1))
    print("Part 2:", timeit.timeit(lambda: print(part2(parsed)), number=1))


if __name__ == "__main__":
    main()
