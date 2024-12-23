import re
import timeit
from dataclasses import dataclass

import numpy as np
import pytest
from aocd import get_data

test_input = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""


@pytest.fixture
def machines():
    return list(parse(test_input))


def test_solve(machines):
    print()
    for machine in machines:
        actual = solve(machine)
        print(actual)


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


def solve(machine):
    a = np.array(
        [
            [machine.button_a.x, machine.button_b.x],
            [machine.button_a.y, machine.button_b.y],
        ]
    )
    b = np.array([machine.prize.x, machine.prize.y])
    return np.linalg.solve(a, b)


def is_int(x):
    y = x.round()
    return np.all(np.abs(x - y) < [0.0001, 0.0001])


def part1(machines):
    presses = [solve(machine) for machine in machines]
    filtered = [x for x in presses if is_int(x)]
    return np.sum(np.sum(np.array([3, 1]) * x for x in filtered))


def part2(lines):
    pass


def main():
    with open("../day13.txt") as f:
        data = f.read()
    parsed = list(parse(data))
    print(parsed)
    print("Part 1:", timeit.timeit(lambda: print(part1(parsed)), number=1))
    print("Part 2:", timeit.timeit(lambda: print(part2(parsed)), number=1))


if __name__ == "__main__":
    main()
