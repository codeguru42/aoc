import timeit
from dataclasses import dataclass

from aocd import get_data


@dataclass
class Node:
    name: str
    links: tuple


def parse_network(lines):
    for line in lines:
        name, rest = line.split(" = ")
        links = tuple(rest[1:-1].split(", "))
        yield Node(name=name, links=links)


def parse(data):
    lines = data.split("\n")
    return lines[0], list(parse_network(lines[2:]))


def part1(lines):
    pass


def part2(lines):
    pass


def main():
    data = get_data(year=2023, day=8)
    parsed = parse(data)
    print(parsed)
    print(part1(parsed))
    print(part2(parsed))
    print("Part 1:", timeit.timeit(lambda: part1(parsed), number=1))
    print("Part 2:", timeit.timeit(lambda: part2(parsed), number=1))


if __name__ == "__main__":
    main()
