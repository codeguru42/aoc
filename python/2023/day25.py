import math
import timeit

import networkx as nx
from aocd import get_data
from matplotlib import pyplot as plt

example = """jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr
"""


def test_part1():
    g = parse(example)
    nx.draw(g, with_labels=True)
    plt.show()


def parse(data):
    g = nx.Graph()
    lines = data.strip().splitlines()
    for line in lines:
        source, destinations = line.split(":")
        for dest in destinations.strip().split():
            g.add_edge(source, dest)
    return g


def part1(g):
    cut = nx.minimum_edge_cut(g)
    for edge in cut:
        g.remove_edge(*edge)
    return math.prod(len(component) for component in nx.connected_components(g))


def main():
    data = get_data(year=2023, day=25)
    parsed = parse(data)
    print("Part 1:", timeit.timeit(lambda: print(part1(parsed)), number=1))


if __name__ == "__main__":
    main()
