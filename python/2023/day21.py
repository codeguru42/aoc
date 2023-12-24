import timeit

import networkx as nx
from aocd import get_data


def neighbors(i, j):
    deltas = (-1, 0, 1)
    for dr in deltas:
        for dc in deltas:
            yield i + dr, j + dc


def parse(data):
    lines = data.splitlines()
    height = len(lines)
    width = len(lines[0])
    g = nx.Graph()
    for i, line in enumerate(lines):
        for j, cell in enumerate(line):
            for n_i, n_j in neighbors(i, j):
                if 0 <= n_i < height and 0 <= n_j < width and lines[n_i][n_j] == ".":
                    g.add_edge((i, j), (n_i, n_j))
    return g


def part1(lines):
    pass


def part2(lines):
    pass


def main():
    data = get_data(year=2023, day=21)
    parsed = parse(data)
    print(parsed)
    print(part1(parsed))
    print(part2(parsed))
    print("Part 1:", timeit.timeit(lambda: part1(parsed), number=1))
    print("Part 2:", timeit.timeit(lambda: part2(parsed), number=1))


if __name__ == "__main__":
    main()
