import timeit
from enum import IntEnum

import networkx as nx
import numpy as np
import pytest
from aocd import get_data

example = r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
"""


def test_part1():
    g, _, _ = parse(example)
    assert part1(g) == 46


def test_part2():
    g, width, height = parse(example)
    assert part2(g, width, height) == 51


class Direction(IntEnum):
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3


deltas = {
    Direction.LEFT: np.array((-1, 0)),
    Direction.RIGHT: np.array((1, 0)),
    Direction.UP: np.array((0, -1)),
    Direction.DOWN: np.array((0, 1)),
}

opposites = {
    Direction.LEFT: Direction.RIGHT,
    Direction.RIGHT: Direction.LEFT,
    Direction.UP: Direction.DOWN,
    Direction.DOWN: Direction.UP,
}


def is_in_bounds(x, y, width, height):
    return 0 <= x < width and 0 <= y < height


def neighbors(p, width, height):
    for d in Direction:
        n = np.array(p) + deltas[d]
        if is_in_bounds(*n, width, height):
            yield tuple(n), d


def parse(data):
    lines = data.strip().split("\n")
    g = nx.DiGraph()
    height = len(lines)
    width = len(lines[0])
    for j, line in enumerate(lines):
        for i, c in enumerate(line):
            curr = i, j
            match c:
                case "|":
                    g.add_edge((curr, Direction.LEFT), (curr, Direction.DOWN))
                    g.add_edge((curr, Direction.LEFT), (curr, Direction.UP))
                    g.add_edge((curr, Direction.RIGHT), (curr, Direction.DOWN))
                    g.add_edge((curr, Direction.RIGHT), (curr, Direction.UP))
                    g.add_edge((curr, Direction.UP), (curr, Direction.DOWN))
                    g.add_edge((curr, Direction.DOWN), (curr, Direction.UP))
                case "-":
                    g.add_edge((curr, Direction.UP), (curr, Direction.LEFT))
                    g.add_edge((curr, Direction.UP), (curr, Direction.RIGHT))
                    g.add_edge((curr, Direction.DOWN), (curr, Direction.LEFT))
                    g.add_edge((curr, Direction.DOWN), (curr, Direction.RIGHT))
                    g.add_edge((curr, Direction.LEFT), (curr, Direction.RIGHT))
                    g.add_edge((curr, Direction.RIGHT), (curr, Direction.LEFT))
                case "\\":
                    g.add_edge((curr, Direction.LEFT), (curr, Direction.DOWN))
                    g.add_edge((curr, Direction.DOWN), (curr, Direction.LEFT))
                    g.add_edge((curr, Direction.RIGHT), (curr, Direction.UP))
                    g.add_edge((curr, Direction.UP), (curr, Direction.RIGHT))
                case "/":
                    g.add_edge((curr, Direction.LEFT), (curr, Direction.UP))
                    g.add_edge((curr, Direction.UP), (curr, Direction.LEFT))
                    g.add_edge((curr, Direction.RIGHT), (curr, Direction.DOWN))
                    g.add_edge((curr, Direction.DOWN), (curr, Direction.RIGHT))
                case ".":
                    g.add_edge((curr, Direction.UP), (curr, Direction.DOWN))
                    g.add_edge((curr, Direction.DOWN), (curr, Direction.UP))
                    g.add_edge((curr, Direction.LEFT), (curr, Direction.RIGHT))
                    g.add_edge((curr, Direction.RIGHT), (curr, Direction.LEFT))
            for n, d in neighbors(curr, width, height):
                g.add_edge((curr, d), (n, opposites[d]))
    return g, width, height


def get_energized(g, start):
    nodes = nx.descendants(g, start)
    energized = set(coords for coords, _ in nodes)
    return len(energized)


def part1(g):
    start = ((0, 0), Direction.LEFT)
    return get_energized(g, start)


def get_top_row(width):
    for i in range(width):
        yield i, 0


def get_bottom_row(width, height):
    for i in range(width):
        yield i, height - 1


def get_left_column(height):
    for j in range(height):
        yield 0, j


def get_right_column(width, height):
    for j in range(height):
        yield width - 1, j


def part2(g, width, height):
    max_top = max(get_energized(g, (v, Direction.UP)) for v in get_top_row(width))
    max_bottom = max(
        get_energized(g, (v, Direction.DOWN)) for v in get_bottom_row(width, height)
    )
    max_left = max(
        get_energized(g, (v, Direction.LEFT)) for v in get_left_column(height)
    )
    max_right = max(
        get_energized(g, (v, Direction.RIGHT)) for v in get_right_column(width, height)
    )
    return max(max_top, max_bottom, max_left, max_right)


def main():
    data = get_data(year=2023, day=16)
    g, width, height = parse(data)
    print("Part 1:", timeit.timeit(lambda: print(part1(g)), number=1))
    print("Part 2:", timeit.timeit(lambda: print(part2(g, width, height)), number=1))


if __name__ == "__main__":
    main()
