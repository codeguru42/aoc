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
        yield [int(x) for x in line.split(",")]


def parse(data):
    rules, updates = data.split("\n\n")
    return parse_rules_graph(rules), list(parse_updates(updates))


def is_in_order(rules, update):
    print(f"{update=}")
    for i, x in enumerate(update):
        for y in update[i + 1 :]:
            if not rules.has_edge(x, y):
                return False
    return True


def part1(rules, updates):
    return sum(
        update[len(update) // 2 + 1] for update in updates if is_in_order(rules, update)
    )


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
