import timeit

import networkx as nx
from aocd import get_data


def parse(data):
    lines = data.strip().split("\n")
    g = nx.DiGraph()
    height = len(lines)
    width = len(lines[0])
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            curr = i, j
            up = i - 1, j
            down = i + 1, j
            left = i, j - 1
            right = i, j + 1
            match c:
                case "|":
                    if i - 1 >= 0:
                        g.add_edge(curr, up)
                    if i + 1 < height:
                        g.add_edge(curr, down)
                case "-":
                    if j - 1 >= 0:
                        g.add_edge(curr, left)
                    if j + 1 < width:
                        g.add_edge(curr, right)
                case "\\":
                    if j - 1 >= 0:
                        g.add_edge(curr, left)
                    if i + 1 < height:
                        g.add_edge(curr, down)
                case "/":
                    if j + 1 < width:
                        g.add_edge(curr, right)
                    if i + 1 < height:
                        g.add_edge(curr, down)
                case ".":
                    pass
    return lines


def part1(lines):
    pass


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
