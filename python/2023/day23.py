import timeit

import networkx as nx
from aocd import get_data

example = """#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#
"""


def test_part1():
    start, end, g = parse(example)
    assert part1(g, start, end) == 90


def parse(data: str):
    g = nx.DiGraph()
    lines = data.splitlines()
    for i, line in enumerate(lines):
        for j, cell in enumerate(line):
            match cell:
                case ".":
                    for n_i, n_j in neighbors(i, j):
                        add_edge(g, lines, i, j, n_i, n_j)
                case ">":
                    n_i = i
                    n_j = j + 1
                    add_edge(g, lines, i, j, n_i, n_j)
                case "<":
                    n_i = i
                    n_j = j - 1
                    g.add_edge((i, j), (n_i, n_j))
                case "^":
                    n_i = i - 1
                    n_j = j
                    g.add_edge((i, j), (n_i, n_j))
                case "v":
                    n_i = i + 1
                    n_j = j
                    g.add_edge((i, j), (n_i, n_j))
    start = 0, lines[0].find(".")
    end = len(lines) - 1, lines[-1].find(".")
    return start, end, g


def neighbors(i, j):
    deltas = (-1, 1)
    for dr in deltas:
        yield i + dr, j
    for dc in deltas:
        yield i, j + dc


def add_edge(g, lines, i, j, n_i, n_j):
    height = len(lines)
    width = len(lines[0])
    if 0 <= n_i < height and 0 <= n_j < width and lines[n_i][n_j] != "#":
        g.add_edge((i, j), (n_i, n_j))


def part1(g, start, end):
    paths = nx.all_simple_paths(g, start, end)
    for path in paths:
        print(path)
    return max(len(path) for path in paths)


def part2(g, start, end):
    pass


def main():
    data = get_data(year=2023, day=23)
    start, end, g = parse(data)
    print("Part 1:", timeit.timeit(lambda: print(part1(g, start, end)), number=1))
    print("Part 2:", timeit.timeit(lambda: print(part2(g, start, end)), number=1))


if __name__ == "__main__":
    main()
