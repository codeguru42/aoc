import timeit

import networkx as nx
import pytest
from aocd import get_data

test_input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""


@pytest.fixture
def parsed_input():
    return parse(test_input)


@pytest.fixture
def rules(parsed_input):
    return parsed_input[0]


@pytest.fixture
def updates(parsed_input):
    return parsed_input[1]


@pytest.mark.parametrize("update_index", [0, 1, 2])
def test_is_in_order(rules, updates, update_index):
    assert is_in_order(rules, updates[update_index])


@pytest.mark.parametrize("update_index", [3, 4, 5])
def test_is_not_in_order(rules, updates, update_index):
    assert not is_in_order(rules, updates[update_index])


def test_part1(rules, updates):
    assert part1(rules, updates) == 143


def parse_rules_graph(rules):
    g = nx.DiGraph()
    for rule in rules.splitlines():
        a, b = rule.split("|")
        g.add_edge(int(a), int(b))
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
            if rules.has_edge(y, x):
                return False
    return True


def part1(rules, updates):
    return sum(
        update[len(update) // 2] for update in updates if is_in_order(rules, update)
    )


def part2(rules, updates):
    return sum(
        sorted(update, key=lambda x: x)[len(update) // 2]
        for update in updates
        if not is_in_order(rules, update)
    )


def main():
    data = get_data(year=2024, day=5)
    rules, updates = parse(data)
    print(rules)
    print(updates)
    print("Part 1:", timeit.timeit(lambda: print(part1(rules, updates)), number=1))
    print("Part 2:", timeit.timeit(lambda: print(part2(rules, updates)), number=1))


if __name__ == "__main__":
    main()
