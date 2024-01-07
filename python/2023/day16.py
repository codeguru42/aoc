import timeit
from enum import IntEnum

import networkx as nx
import numpy as np
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


def test_parse():
    g = parse(example)
    assert part1(g) == 46


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
                    g.add_edge((curr, Direction.LEFT), (curr, Direction.RIGHT))
                    g.add_edge((curr, Direction.RIGHT), (curr, Direction.DOWN))
                    g.add_edge((curr, Direction.RIGHT), (curr, Direction.RIGHT))
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
                    g.add_edge((curr, Direction.UP), (curr, Direction.DOWN))
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
    return g


def part1(g):
    start = ((0, 0), Direction.LEFT)
    nodes = nx.descendants(g, start)
    energized = set(coords for coords, _ in nodes)
    return len(energized)


def part2(lines):
    pass


def main():
    data = get_data(year=2023, day=16)
    parsed = parse(data)
    print(part1(parsed))
    print(part2(parsed))
    print("Part 1:", timeit.timeit(lambda: part1(parsed), number=1))
    print("Part 2:", timeit.timeit(lambda: part2(parsed), number=1))


if __name__ == "__main__":
    main()
