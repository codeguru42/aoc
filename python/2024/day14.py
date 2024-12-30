import collections
import math
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


def calculate_final_position(robots, width, height, seconds):
    for robot in robots:
        x = (robot.p.x + seconds * robot.v.x) % width
        y = (robot.p.y + seconds * robot.v.y) % height
        yield Point(x, y)


def get_quadrant(p, width, height):
    if p.x < width / 2 and p.y < height / 2:
        return 1
    if p.x < width / 2 and p.y > height / 2:
        return 2
    if p.x > width / 2 and p.y < height / 2:
        return 3
    if p.x > width / 2 and p.y > height / 2:
        return 4


def part1(robots, width, height):
    final_positions = calculate_final_position(robots, width, height, 100)
    quadrants = map(lambda p: get_quadrant(p, width, height), final_positions)
    return math.prod(collections.Counter(quadrants).values())


def part2(lines):
    pass


def main():
    data = get_data(year=2024, day=14)
    parsed = list(parse(data))
    width = 101
    height = 103
    print(
        "Part 1:", timeit.timeit(lambda: print(part1(parsed, width, height)), number=1)
    )
    print("Part 2:", timeit.timeit(lambda: print(part2(parsed)), number=1))


if __name__ == "__main__":
    main()
