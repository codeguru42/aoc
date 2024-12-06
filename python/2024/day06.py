import collections
import itertools
import timeit

from aocd import get_data

test_map = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""


def test_part1():
    x, y, m = parse(test_map)
    assert part1(x, y, m) == 41


def find_start(lines):
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "^":
                return x, y


def parse(data):
    lines = data.splitlines()
    x, y = find_start(lines)
    return x, y, [list(line) for line in lines]


def print_map(m):
    print()
    for line in m:
        print("".join(line))


def predict_route(x, y, m):
    deltas = iter(itertools.cycle([(0, -1), (1, 0), (0, 1), (-1, 0)]))
    delta = next(deltas)
    next_x = x + delta[0]
    next_y = y + delta[1]
    while 0 <= next_x < len(m[0]) and 0 <= next_y < len(m):
        if m[next_y][next_x] != "#":
            m[y][x] = "X"
            x, y = next_x, next_y
        else:
            delta = next(deltas)
        next_x = x + delta[0]
        next_y = y + delta[1]
    m[y][x] = "X"


def count_visited(m):
    counts = [collections.Counter(line) for line in m]
    return sum(count["X"] for count in counts)


def part1(x, y, m):
    predict_route(x, y, m)
    return count_visited(m)


def part2(x, y, m):
    pass


def main():
    data = get_data(year=2024, day=6)
    x, y, m = parse(data)
    print("Part 1:", timeit.timeit(lambda: print(part1(x, y, m)), number=1))
    print("Part 2:", timeit.timeit(lambda: print(part2(x, y, m)), number=1))


if __name__ == "__main__":
    main()
