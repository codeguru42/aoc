import timeit

import networkx as nx
from aocd import get_data


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
    deltas = (-1, 0, 1)
    for dr in deltas:
        for dc in deltas:
            yield i + dr, j + dc


def add_edge(g, lines, i, j, n_i, n_j):
    height = len(lines)
    width = len(lines[0])
    if 0 <= n_i < height and 0 <= n_j < width and lines[n_i][n_j] != "#":
        g.add_edge((i, j), (n_i, n_j))


def part1(lines):
    pass


def part2(lines):
    pass


def main():
    data = get_data(year=2023, day=23)
    parsed = parse(data)
    print(parsed)
    print("Part 1:", timeit.timeit(lambda: print(part1(parsed)), number=1))
    print("Part 2:", timeit.timeit(lambda: print(part2(parsed)), number=1))


if __name__ == "__main__":
    main()
