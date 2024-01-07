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


deltas = {
    Direction.LEFT: np.array((-1, 0)),
    Direction.RIGHT: np.array((1, 0)),
    Direction.UP: np.array((0, -1)),
    Direction.DOWN: np.array((0, 1)),
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


def paint_hull(instructions, initial_color):
    program = run_program(instructions)
    grid = defaultdict(lambda: Color.BLACK)
    painted = set()
    loc = np.array((0, 0))
    grid[tuple(loc)] = initial_color
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
        return len(painted), grid


def part1(instructions):
    count, _ = paint_hull(instructions, initial_color=Color.BLACK)
    return count


def draw(grid):
    coords = grid.keys()
    min_x = min(x for x, y in coords)
    max_x = max(x for x, y in coords)
    min_y = min(y for x, y in coords)
    max_y = max(y for x, y in coords)
    reg_id = [["." for _ in range(min_x, max_x + 1)] for __ in range(min_y, max_y + 1)]
    for (x, y), color in grid.items():
        if color == Color.WHITE:
            reg_id[y - min_y][x - min_x] = "#"
    for row in reg_id:
        print("".join(row))


def part2(instructions):
    _, grid = paint_hull(instructions, initial_color=Color.WHITE)
    draw(grid)


def main():
    data = get_data(year=2019, day=11)
    parsed = parse(data)
    print("Part 1:", timeit.timeit(lambda: print(part1(parsed)), number=1))
    print("Part 2:", timeit.timeit(lambda: part2(parsed), number=1))


if __name__ == "__main__":
    main()
