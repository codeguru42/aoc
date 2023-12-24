import timeit

import networkx as nx
from aocd import get_data


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


def part1(start, g):
    pass


def part2(start, g):
    pass


def main():
    data = get_data(year=2023, day=21)
    start, g = parse(data)
    print(part1(start, g))
    print(part2(start, g))
    print("Part 1:", timeit.timeit(lambda: part1(start, g), number=1))
    print("Part 2:", timeit.timeit(lambda: part2(start, g), number=1))


if __name__ == "__main__":
    main()
