import timeit

import networkx as nx
from aocd import get_data


def parse_rules_graph(rules):
    g = nx.DiGraph()
    for rule in rules.splitlines():
        a, b = rule.split("|")
        g.add_edge(a, b)
    return g


def parse_updates(updates):
    for line in updates.splitlines():
        yield line.split(",")


def parse(data):
    rules, updates = data.split("\n\n")
    return parse_rules_graph(rules), list(parse_updates(updates))


def part1(lines, updates):
    pass


def part2(lines, updates):
    pass


def main():
    data = get_data(year=2024, day=5)
    rules, updates = parse(data)
    print(rules)
    print(updates)
    print("Part 1:", timeit.timeit(lambda: print(part1(rules, updates)), number=1))
    print("Part 2:", timeit.timeit(lambda: print(part2(rules, updates)), number=1))


if __name__ == "__main__":
    main()
