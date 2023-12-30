import timeit
from dataclasses import dataclass

from aocd import get_data


@dataclass
class Broadcaster:
    children: list[str]


@dataclass
class FlipFlop:
    children: list[str]


@dataclass
class Conjunction:
    children: list[str]


def parse(data):
    lines = data.strip().splitlines()
    components = {}
    for line in lines:
        first, second = line.strip().split("->")
        children = [d.strip() for d in second.split(",")]
        match first:
            case ["%", name]:
                components[name] = FlipFlop(children=children)
            case ["&", name]:
                components[name] = Conjunction(children=children)
            case name:
                components[name] = Broadcaster(children=children)
    return lines


def part1(lines):
    pass


def part2(lines):
    pass


def main():
    data = get_data(year=2023, day=20)
    parsed = parse(data)
    print(parsed)
    print("Part 1:", timeit.timeit(lambda: print(part1(parsed)), number=1))
    print("Part 2:", timeit.timeit(lambda: print(part2(parsed)), number=1))


if __name__ == "__main__":
    main()
