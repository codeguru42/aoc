import timeit
from collections import defaultdict
from enum import IntEnum, Enum

import numpy as np
from aocd import get_data

from int_code import parse, run_program


class Color(IntEnum):
    BLACK = 0
    WHITE = 1


class Direction(IntEnum):
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3


def part1(instructions):
    deltas = {
        Direction.LEFT: np.array((-1, 0)),
        Direction.RIGHT: np.array((1, 0)),
        Direction.UP: np.array((0, 1)),
        Direction.DOWN: np.array((0, -1)),
    }
    turns = {
        Direction.LEFT: {
            Direction.LEFT: Direction.DOWN,
            Direction.RIGHT: Direction.UP,
        },
        Direction.RIGHT: {
            Direction.LEFT: Direction.UP,
            Direction.RIGHT: Direction.DOWN,
        },
        Direction.UP: {
            Direction.LEFT: Direction.LEFT,
            Direction.RIGHT: Direction.RIGHT,
        },
        Direction.DOWN: {
            Direction.LEFT: Direction.RIGHT,
            Direction.RIGHT: Direction.LEFT,
        },
    }
    program = run_program(instructions)
    grid = defaultdict(lambda: Color.BLACK)
    painted = set()
    loc = np.array((0, 0))
    facing = Direction.UP

    try:
        next(program)
        while True:
            color = program.send(grid[tuple(loc)])
            painted.add(tuple(loc))
            grid[tuple(loc)] = Color(color)
            direction = next(program)
            facing = turns[facing][Direction(direction)]
            loc += deltas[facing]
    except StopIteration:
        pass
    finally:
        return len(painted)


def part2(instructions):
    pass


def main():
    data = get_data(year=2019, day=11)
    parsed = parse(data)
    print(parsed)
    print("Part 1:", timeit.timeit(lambda: print(part1(parsed)), number=1))
    print("Part 2:", timeit.timeit(lambda: print(part2(parsed)), number=1))


if __name__ == "__main__":
    main()
