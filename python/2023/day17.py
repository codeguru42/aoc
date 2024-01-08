import timeit

import networkx as nx
from aocd import get_data


def parse(data):
    g = nx.DiGraph()
    lines = data.splitlines()
    for j, line in enumerate(lines):
        for i, c in enumerate(line):
            for n in neighbors(i, j):
                g.add_edge((i, j), n, weight=int(c))

    return g


def part1(lines):
    pass


def part2(lines):
    pass


def main():
    data = get_data(year=2023, day=17)
    g = parse(data)
    print(g)
    print("Part 1:", timeit.timeit(lambda: print(part1(g)), number=1))
    print("Part 2:", timeit.timeit(lambda: print(part2(g)), number=1))


if __name__ == "__main__":
    main()
