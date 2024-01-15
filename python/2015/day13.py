import re
import timeit
from dataclasses import dataclass

from aocd import get_data


@dataclass
class Happiness:
    name: str
    next_to: str
    change: int


def parse(data):
    lines = data.splitlines()
    for line in lines:
        match = re.match(
            r"(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+)\.",
            line,
        )
        name, direction, change, next_to = match.groups()
        change = int(change)
        if direction == "lose":
            change = -change
        yield Happiness(name=name, next_to=next_to, change=change)


def part1(lines):
    pass


def part2(lines):
    pass


def main():
    data = get_data(year=2015, day=13)
    parsed = list(parse(data))
    print(parsed)
    print("Part 1:", timeit.timeit(lambda: print(part1(parsed)), number=1))
    print("Part 2:", timeit.timeit(lambda: print(part2(parsed)), number=1))


if __name__ == "__main__":
    main()
