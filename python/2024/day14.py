import collections
import math
import re
import timeit
from dataclasses import dataclass

import pytest
from aocd import get_data


@dataclass(frozen=True)
class Point:
    x: int
    y: int


@dataclass
class Robot:
    p: Point
    v: Point


test_input = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
"""


@pytest.fixture
def robots():
    return list(parse(test_input))


@pytest.fixture
def width():
    return 11


@pytest.fixture
def height():
    return 7


@pytest.fixture
def seconds():
    return 100


def test_part1(robots, width, height, seconds):
    assert part1(robots, width, height, seconds) == 12


def test_calculate_final_position(width, height):
    robot = Robot(Point(2, 4), Point(2, -3))
    assert calculate_final_position(robot, width, height, 5) == Point(1, 3)


def test_calculate_all_final_positions(robots, width, height, seconds):
    expected = {
        Point(6, 0): 2,
        Point(9, 0): 1,
        Point(0, 2): 1,
        Point(1, 3): 1,
        Point(2, 3): 1,
        Point(5, 4): 1,
        Point(3, 5): 1,
        Point(4, 5): 2,
        Point(1, 6): 1,
        Point(6, 6): 1,
    }
    result = collections.Counter(
        calculate_all_final_positions(robots, width, height, seconds)
    )
    assert result == expected


@pytest.mark.parametrize(
    "point,quadrant",
    [
        (Point(5, 4), None),
        (Point(0, 2), 1),
        (Point(1, 6), 2),
        (Point(6, 0), 3),
        (Point(6, 6), 4),
    ],
)
def test_get_quadrant(point, quadrant, width, height):
    assert get_quadrant(point, width, height) is quadrant


def parse(data):
    lines = data.strip().splitlines()
    for line in lines:
        match = re.match(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line.strip())
        yield Robot(
            Point(int(match.group(1)), int(match.group(2))),
            Point(int(match.group(3)), int(match.group(4))),
        )


def calculate_final_position(robot, width, height, seconds):
    x = (robot.p.x + seconds * robot.v.x) % width
    y = (robot.p.y + seconds * robot.v.y) % height
    return Point(x, y)


def calculate_all_final_positions(robots, width, height, seconds):
    return list(
        map(lambda r: calculate_final_position(r, width, height, seconds), robots)
    )


def get_quadrant(p, width, height):
    if p.x < width // 2 and p.y < height // 2:
        return 1
    if p.x < width // 2 and p.y > height // 2:
        return 2
    if p.x > width // 2 and p.y < height // 2:
        return 3
    if p.x > width // 2 and p.y > height // 2:
        return 4


def get_all_quadrants(final_positions, width, height):
    return list(map(lambda p: get_quadrant(p, width, height), final_positions))


def part1(robots, width, height, seconds):
    final_positions = calculate_all_final_positions(robots, width, height, seconds)
    quadrants = get_all_quadrants(final_positions, width, height)
    return math.prod(
        v for k, v in collections.Counter(quadrants).items() if k is not None
    )


def part2(lines):
    pass


def main():
    data = get_data(year=2024, day=14)
    parsed = list(parse(data))
    width = 101
    height = 103
    seconds = 100
    print(
        "Part 1:",
        timeit.timeit(lambda: print(part1(parsed, width, height, seconds)), number=1),
    )
    print("Part 2:", timeit.timeit(lambda: print(part2(parsed)), number=1))


if __name__ == "__main__":
    main()
