import itertools
import math
import timeit
from dataclasses import dataclass

from aocd import get_data

example2 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
"""


def test_part2():
    instructions, nodes = parse(example2)
    assert part2(instructions, nodes) == 6


@dataclass
class Node:
    name: str
    links: tuple

    def right(self):
        return self.links[1]

    def left(self):
        return self.links[0]


def parse_network(lines):
    nodes = {}
    for line in lines:
        name, rest = line.split(" = ")
        links = tuple(rest[1:-1].split(", "))
        nodes[name] = Node(name=name, links=links)
    return nodes


def parse(data):
    lines = data.strip().split("\n")
    return lines[0], parse_network(lines[2:])


def count_steps(instructions, nodes, start, end):
    node = start
    steps = 0
    for i in itertools.cycle(instructions):
        node = nodes[next_node(i, node)]
        steps += 1
        if end(node):
            return steps


def part1(instructions, nodes):
    return count_steps(
        instructions, nodes, nodes["AAA"], lambda node: node.name == "ZZZ"
    )


def next_node(dir, node):
    match dir:
        case "L":
            node = node.left()
        case "R":
            node = node.right()
    return node


def part2(instructions, nodes):
    start_nodes = [node for name, node in nodes.items() if node.name.endswith("A")]
    end = lambda node: node.name.endswith("Z")
    counts = [count_steps(instructions, nodes, start, end) for start in start_nodes]
    return math.lcm(*counts)


def main():
    data = get_data(year=2023, day=8)
    parsed = parse(data)
    print(parsed)
    print(part1(*parsed))
    print(part2(*parsed))
    print("Part 1:", timeit.timeit(lambda: part1(*parsed), number=1))
    print("Part 2:", timeit.timeit(lambda: part2(*parsed), number=1))


if __name__ == "__main__":
    main()
