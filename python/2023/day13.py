import timeit

from aocd import get_data

import aoc


def parse(data):
    valley = data.split("\n\n")
    return [v.split("\n") for v in valley]


def find_horizontal_mirror(mountain):
    for i, (line, next_line) in enumerate(aoc.sliding_window(mountain, n=2)):
        if line == next_line:
            yield i


def part1(mountains):
    for mountain in mountains:
        print(list(find_horizontal_mirror(mountain)))


def part2(lines):
    pass


def main():
    data = get_data(year=2023, day=13)
    parsed = parse(data)
    print(part1(parsed))
    print(part2(parsed))
    print("Part 1:", timeit.timeit(lambda: part1(parsed), number=1))
    print("Part 2:", timeit.timeit(lambda: part2(parsed), number=1))


if __name__ == "__main__":
    main()
