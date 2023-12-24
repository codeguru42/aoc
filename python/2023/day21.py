import timeit

import networkx as nx
import pytest
from aocd import get_data

example = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
"""


def test_part1():
    start, g = parse(example)
    assert part1(start, g, 6) == 16


@pytest.mark.parametrize(
    "steps,expected",
    [
        (6, 16),
        (10, 50),
        (50, 1594),
        (100, 6536),
        (500, 167004),
        (1000, 668697),
        (5000, 16733044),
    ],
)
def test_part2(steps, expected):
    start, g = parse(example)
    make_infinite(g, example)
    assert part1(start, g, steps) == expected


def neighbors(i, j):
    deltas = (-1, 1)
    for dr in deltas:
        yield i + dr, j
    for dc in deltas:
        yield i, j + dc


def parse(data):
    lines = data.splitlines()
    height = len(lines)
    width = len(lines[0])
    g = nx.Graph()
    start = None
    for i, line in enumerate(lines):
        for j, cell in enumerate(line):
            if lines[i][j] == "#":
                continue
            if lines[i][j] == "S":
                start = i, j
            for n_i, n_j in neighbors(i, j):
                if (
                    0 <= n_i < height
                    and 0 <= n_j < width
                    and (lines[n_i][n_j] == "." or lines[n_i][n_j] == "S")
                ):
                    g.add_edge((i, j), (n_i, n_j))
    return start, g


def part1(start, g, steps):
    path = nx.single_source_shortest_path_length(g, start, cutoff=steps)
    return len(list(v for v, l in path.items() if l <= steps and l % 2 == 0))


def part2(start, g, steps):
    return part1(start, g, steps)


def make_infinite(g, data):
    lines = data.splitlines()
    height = len(lines)
    width = len(lines[0])
    for j, (top, bottom) in enumerate(zip(lines[1], lines[-1])):
        if top == "." and bottom == ".":
            g.add_edge((0, j), (height - 1, j))
    columns = list(zip(*lines))
    for i, (left, right) in enumerate(zip(columns[1], columns[-1])):
        if left == "." and right == ".":
            g.add_edge((i, 0), (i, width - 1))


def main():
    data = get_data(year=2023, day=21)
    start, g = parse(data)
    print(part1(start, g, 64))
    print("Part 1:", timeit.timeit(lambda: part1(start, g, 64), number=1))
    make_infinite(g, data)
    print(part2(start, g, 26501365))
    print("Part 2:", timeit.timeit(lambda: part2(start, g, 26501365), number=1))


if __name__ == "__main__":
    main()
