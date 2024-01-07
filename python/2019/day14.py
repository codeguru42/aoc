import timeit

import networkx as nx
from aocd import get_data


def parse(data):
    lines = data.splitlines()
    g = nx.DiGraph
    for line in lines:
        reactants, product = line.split("=>")
        for reactant in reactants.strip().split(","):
            pass
    return g


def part1(lines):
    pass


def part2(lines):
    pass


def main():
    data = get_data(year=2019, day=14)
    print(data)
    parsed = parse(data)
    print("Part 1:", timeit.timeit(lambda: print(part1(parsed)), number=1))
    print("Part 2:", timeit.timeit(lambda: print(part2(parsed)), number=1))


if __name__ == "__main__":
    main()
