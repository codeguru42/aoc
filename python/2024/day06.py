import collections
import itertools
import timeit

from aocd import get_data


def find_start(lines):
    for x, line in enumerate(lines):
        for y, c in enumerate(line):
            if c == "^":
                return x, y


def parse(data):
    lines = data.splitlines()
    x, y = find_start(lines)
    return x, y, [list(line) for line in lines]


def predict_route(x, y, m):
    deltas = iter(itertools.cycle([(0, -1), (1, 0), (0, 1), (-1, 0)]))
    delta = next(deltas)
    while 0 <= x < len(m[0]) and 0 <= y < len(m):
        next_x = x + delta[0]
        next_y = y + delta[1]
        if m[next_x][next_y] != "#":
            m[x][y] = "X"
            x, y = next_x, next_y
        else:
            delta = next(deltas)


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
