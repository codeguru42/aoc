import timeit

import matplotlib.pyplot as plt
import networkx as nx
from aocd import get_data


def parse(data):
    lines = data.splitlines()
    g = nx.DiGraph()
    for line in lines:
        reactants, product = line.split("=>")
        prod_amt, prod_name = product.strip().split()
        for reactant in reactants.strip().split(","):
            react_amt, react_name = reactant.strip().split()
            g.add_edge(prod_name, react_name)
    return g


def part1(lines):
    pass


def part2(lines):
    pass


def main():
    data = get_data(year=2019, day=14)
    g = parse(data)
    nx.draw(g)
    plt.show()
    print("Part 1:", timeit.timeit(lambda: print(part1(g)), number=1))
    print("Part 2:", timeit.timeit(lambda: print(part2(g)), number=1))


if __name__ == "__main__":
    main()
