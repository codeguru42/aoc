import timeit
from enum import IntEnum

import numpy as np
from aocd import get_data

from int_code import parse, run_program


class Direction(IntEnum):
    NORTH = 1
    SOUTH = 2
    WEST = 3
    EAST = 4


class Status(IntEnum):
    WALL = 0
    MOVED = 1
    OXYGEN = 2


deltas = {
    Direction.WEST: np.array((-1, 0)),
    Direction.EAST: np.array((1, 0)),
    Direction.NORTH: np.array((0, 1)),
    Direction.SOUTH: np.array((0, -1)),
}

opposites = {
    Direction.WEST: Direction.EAST,
    Direction.EAST: Direction.WEST,
    Direction.NORTH: Direction.SOUTH,
    Direction.SOUTH: Direction.NORTH,
}


def part1(instructions):
    maze = [[" " for _ in range(100)] for _ in range(100)]
    path = []
    visited = set()
    curr = Status.MOVED
    loc = np.array((0, 0))
    stack = []
    program = run_program(instructions)
    next(program)
    while curr != Status.OXYGEN:
        if tuple(loc) not in visited:
            visited.add(tuple(loc))
            path.append(loc)
            for d in Direction:
                stack.append((d, tuple(loc)))
        else:
            back = opposites[d]
            path.pop()
            program.send(back)
        while True:
            d, loc = stack.pop()
            loc = np.array(loc) + deltas[d]
            if tuple(loc) not in visited:
                curr = program.send(d)
                if curr != Status.WALL:
                    break
    return len(path)


def part2(instructions):
    pass


def main():
    data = get_data(year=2019, day=15)
    parsed = parse(data)
    print(parsed)
    print("Part 1:", timeit.timeit(lambda: print(part1(parsed)), number=1))
    print("Part 2:", timeit.timeit(lambda: print(part2(parsed)), number=1))


if __name__ == "__main__":
    main()
