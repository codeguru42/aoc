import timeit

import networkx as nx
from aocd import get_data


def parse(data):
    g = nx.Graph()
    lines = data.splitlines()
    for line in lines:
        source, destinations = line.split(":")
        for dest in destinations.strip().split():
            g.add_edge(source, dest)
    return g


def part1(lines):
    pass


def part2(lines):
    pass


def main():
    data = get_data(year=2023, day=25)
    parsed = parse(data)
    print(parsed)
    print("Part 1:", timeit.timeit(lambda: print(part1(parsed)), number=1))
    print("Part 2:", timeit.timeit(lambda: print(part2(parsed)), number=1))


if __name__ == "__main__":
    main()
