import timeit

import pytest
from aocd import get_data

example = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""


@pytest.fixture
def universe():
    parsed = parse(example)
    return expand(parsed)


def test_part1(universe):
    assert part1(universe) == 374


def parse(data):
    return data.split("\n")


def expand_rows(universe):
    for row in universe:
        yield row
        if all(c == "." for c in row):
            yield row


def expand_columns(universe):
    transposed = zip(*universe)
    yield from expand_rows(transposed)


def expand(universe):
    universe = list(expand_rows(universe))
    return expand_columns(universe)


def get_galaxy_coords(universe):
    for i, row in enumerate(universe):
        for j, col in enumerate(row):
            if col == "#":
                yield i, j


def dist(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])


def part1(universe):
    coords = list(get_galaxy_coords(universe))
    return sum(dist(x, y) for x in coords for y in coords) // 2


def part2(universe):
    pass


def main():
    data = get_data(year=2023, day=11)
    parsed = parse(data)
    universe = list(expand(parsed))
    print(part1(universe))
    print(part2(universe))
    print("Part 1:", timeit.timeit(lambda: part1(parsed), number=1))
    print("Part 2:", timeit.timeit(lambda: part2(parsed), number=1))


if __name__ == "__main__":
    main()
