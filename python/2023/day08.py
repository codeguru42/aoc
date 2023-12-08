import itertools
import timeit
from dataclasses import dataclass

from aocd import get_data


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
    lines = data.split("\n")
    return lines[0], parse_network(lines[2:])


def part1(instructions, nodes):
    node = nodes["AAA"]
    steps = 0
    for i in itertools.cycle(instructions):
        node = nodes[next_node(i, node)]
        steps += 1
        if node.name == "ZZZ":
            return steps


def next_node(dir, node):
    match dir:
        case "L":
            node = node.left()
        case "R":
            node = node.right()
    return node


def part2(lines):
    pass


def main():
    data = get_data(year=2023, day=8)
    parsed = parse(data)
    print(parsed)
    print(part1(*parsed))
    print(part2(parsed))
    print("Part 1:", timeit.timeit(lambda: part1(*parsed), number=1))
    print("Part 2:", timeit.timeit(lambda: part2(parsed), number=1))


if __name__ == "__main__":
    main()
