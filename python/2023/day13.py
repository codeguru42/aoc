import timeit

from aocd import get_data

example = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""


def test_find_horizontal_mirror():
    (_, mountain) = parse(example)
    assert list(find_horizontal_mirror(mountain)) == [4]


def test_find_vertical_mirror():
    (mountain, _) = parse(example)
    assert list(find_vertical_mirror(mountain)) == [5]


def parse(data):
    valley = data.strip().split("\n\n")
    return [v.strip().split("\n") for v in valley]


def find_horizontal_mirror(mountain):
    height = len(mountain)
    for i in range(height - 1):
        top = mountain[i::-1]
        bottom = mountain[i + 1 :]
        if all(x == y for x, y in zip(top, bottom)):
            yield i + 1


def find_vertical_mirror(mountain):
    yield from find_horizontal_mirror(list(zip(*mountain)))


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
