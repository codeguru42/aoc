import timeit
from dataclasses import dataclass
from itertools import repeat
from typing import Callable

import networkx as nx
from aocd import get_data

example = """1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9
"""


def test_part1():
    bricks = list(parse(example))
    assert part1(bricks) == 5


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


def get_x(p: Point) -> int:
    return p.x


def get_y(p: Point) -> int:
    return p.y


def max_coord(bricks: list[Point], get_coord: Callable[[Point], int]) -> int:
    return max(
        coord for coord in (max(get_coord(p1), get_coord(p2)) for p1, p2 in bricks)
    )


def supports(b1, b2):
    pass


def get_supported_bricks(support, bricks):
    return min(
        (b for b in bricks if supports(support, b)), key=lambda b: max(b[0].z, b[1].z)
    )


def make_support_network(bricks):
    max_x = max_coord(bricks, get_x)
    max_y = max_coord(bricks, get_y)
    g = nx.DiGraph()
    sorted_bricks = sorted(bricks, key=lambda b: min(b[0].z, b[1].z))
    for b in sorted_bricks:
        supported = get_supported_bricks(b, sorted_bricks)
        g.add_edges_from(zip(repeat(b), supported))
    return g


def part1(bricks):
    g = make_support_network(bricks)
    print(g)


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
