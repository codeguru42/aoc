import re
import timeit
from dataclasses import dataclass

from aocd import get_data


@dataclass
class Button:
    x: int
    y: int


@dataclass
class Prize:
    x: int
    y: int


@dataclass
class Machine:
    button_a: Button
    button_b: Button
    prize: Prize


def parse(data):
    machines = data.split("\n\n")
    for machine in machines:
        lines = machine.splitlines()
        line1 = re.match(r"Button A: X\+(\d+), Y\+(\d+)", lines[0])
        line2 = re.match(r"Button B: X\+(\d+), Y\+(\d+)", lines[1])
        line3 = re.match(r"Prize: X=(\d+), Y=(\d+)", lines[2])
        yield Machine(
            button_a=Button(x=int(line1.group(1)), y=int(line1.group(2))),
            button_b=Button(x=int(line2.group(1)), y=int(line2.group(2))),
            prize=Prize(int(line3.group(1)), int(line3.group(2))),
        )


def part1(lines):
    pass


def part2(lines):
    pass


def main():
    data = get_data(year=2024, day=13)
    parsed = list(parse(data))
    print(parsed)
    print("Part 1:", timeit.timeit(lambda: print(part1(parsed)), number=1))
    print("Part 2:", timeit.timeit(lambda: print(part2(parsed)), number=1))


if __name__ == "__main__":
    main()
