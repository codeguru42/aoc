import timeit

import networkx as nx
from aocd import get_data


def parse(data):
    lines = data.split("\n")
    height = len(lines)
    width = len(lines[0])

    start = None
    g = nx.Graph()
    for j, line in enumerate(lines):
        for i, pipe in enumerate(line):
            match pipe:
                case "|":
                    if i - 1 >= 0:
                        g.add_edge((i, j), (i - 1, j))
                    if i + 1 <= height:
                        g.add_edge((i, j), (i + 1, j))
                case "-":
                    if j - 1 >= 0:
                        g.add_edge((i, j), (i, j - 1))
                    if j + 1 < width:
                        g.add_edge((i, j), (i, j + 1))
                case "L":
                    if i - 1 >= 0:
                        g.add_edge((i, j), (i - 1, j))
                    if j + 1 < width:
                        g.add_edge((i, j), (i, j + 1))
                case "J":
                    if i - 1 >= 0:
                        g.add_edge((i, j), (i - 1, j))
                    if j - 1 >= 0:
                        g.add_edge((i, j), (i, j - 1))
                case "7":
                    if j - 1 >= 0:
                        g.add_edge((i, j), (i, j - 1))
                    if i + 1 <= height:
                        g.add_edge((i, j), (i + 1, j))
                case "F":
                    if j + 1 < width:
                        g.add_edge((i, j), (i, j + 1))
                    if i + 1 <= height:
                        g.add_edge((i, j), (i + 1, j))
                case ".":
                    pass
                case "S":
                    start = (i, j)
                    if i - 1 >= 0:
                        g.add_edge((i, j), (i - 1, j))
                    if i + 1 <= height:
                        g.add_edge((i, j), (i + 1, j))
                    if j - 1 >= 0:
                        g.add_edge((i, j), (i, j - 1))
                    if j + 1 < width:
                        g.add_edge((i, j), (i, j + 1))
    return start, g


def part1(start, g):
    pass


def part2(start, g):
    pass


def main():
    data = get_data(year=2023, day=10)
    start, g = parse(data)
    print(start)
    print(g)
    print(part1(start, g))
    print(part2(start, g))
    print("Part 1:", timeit.timeit(lambda: part1(start, g), number=1))
    print("Part 2:", timeit.timeit(lambda: part2(start, g), number=1))


if __name__ == "__main__":
    main()
