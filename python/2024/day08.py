import collections
import itertools
import timeit

from aocd import get_data

test_input = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""


def test_part2():
    antennas, width, height = parse(test_input)
    assert part2(antennas, width, height) == 34


def parse(data):
    lines = data.strip().splitlines()
    antennas = collections.defaultdict(list)
    for r, line in enumerate(lines):
        for c, antenna in enumerate(line):
            if antenna != ".":
                antennas[antenna].append((r, c))
    return antennas, len(lines), len(lines[0])


def get_antinodes(antennas, height, width):
    for coords in antennas.values():
        for p1, p2 in itertools.combinations(coords, 2):
            dr, dc = (p1[0] - p2[0], p1[1] - p2[1])
            a1 = p1[0] + dr, p1[1] + dc
            a2 = p2[0] - dr, p2[1] - dc
            if 0 <= a1[0] < height and 0 <= a1[1] < width:
                yield a1
            if 0 <= a2[0] < height and 0 <= a2[1] < width:
                yield a2


def part1(antennas, height, width):
    return len(set(get_antinodes(antennas, height, width)))


def get_antinodes2(antennas, height, width):
    for coords in antennas.values():
        for p1, p2 in itertools.combinations(coords, 2):
            dr, dc = (p1[0] - p2[0], p1[1] - p2[1])
            a1 = p1
            while 0 <= a1[0] < height and 0 <= a1[1] < width:
                a1 = a1[0] + dr, a1[1] + dc
                yield a1
            a2 = p2
            while 0 <= a2[0] < height and 0 <= a2[1] < width:
                a2 = a2[0] - dr, a2[1] - dc
                yield a2


def part2(antennas, height, width):
    return len(set(get_antinodes2(antennas, height, width)))


def main():
    data = get_data(year=2024, day=8)
    antennas, height, width = parse(data)
    print(
        "Part 1:",
        timeit.timeit(lambda: print(part1(antennas, height, width)), number=1),
    )
    print(
        "Part 2:",
        timeit.timeit(lambda: print(part2(antennas, height, width)), number=1),
    )


if __name__ == "__main__":
    main()
