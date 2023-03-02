import math
import queue
import unittest
from functools import reduce
from operator import mul


class TestDay09(unittest.TestCase):
    def setUp(self):
        self.bump_map = [
            [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
            [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
            [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
            [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
            [9, 8, 9, 9, 9, 6, 5, 6, 7, 8],
        ]

    def test_is_low_point_false1(self):
        self.assertFalse(is_low_point(self.bump_map, 0, 0))

    def test_is_low_point_false2(self):
        self.assertFalse(is_low_point(self.bump_map, 0, 2))

    def test_is_low_point_true1(self):
        self.assertTrue(is_low_point(self.bump_map, 0, 1))

    def test_is_low_point_true2(self):
        self.assertTrue(is_low_point(self.bump_map, 0, 9))

    def test_flood_fill1(self):
        expected = {(0, 0), (0, 1), (1, 0)}
        actual = flood_fill(self.bump_map, 0, 0)
        self.assertEqual(expected, actual)

    def test_flood_fill2(self):
        expected = {
            (0, 5), (0, 6), (0, 7), (0, 8), (0, 9),
            (1, 6), (1, 8), (1, 9),
            (2, 9),
        }
        actual = flood_fill(self.bump_map, 1, 8)
        self.assertEqual(expected, actual)

    def test_flood_fill3(self):
        with open('day09.txt') as file:
            bump_map = list(parse(file))
        expected = {
            (0, 1), (0, 2), (0, 3), (0, 4),
            (1, 2), (1, 3),
            (2, 3), (2, 4),
            (3, 4),
        }
        actual = flood_fill(bump_map, 0, 1)
        self.assertEqual(expected, actual)


def parse(file):
    for line in file:
        yield [int(x) for x in line.strip()]


def is_low_point(bump_map, i, j):
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if not (dx == 0 and dy == 0):
                if 0 <= i + dx < len(bump_map):
                    if 0 <= j + dy < len(bump_map[i]):
                        if bump_map[i][j] >= bump_map[i + dx][j + dy]:
                            return False
    return True


def part1(bump_map):
    risk = 0
    for i in range(len(bump_map)):
        row = bump_map[i]
        for j in range(len(row)):
            if is_low_point(bump_map, i, j):
                risk += 1 + bump_map[i][j]
    return risk


def flood_fill(bump_map, i, j):
    basin = set()
    visited = set()
    q = queue.Queue()
    q.put((i, j))

    while not q.empty():
        x, y = q.get()
        visited.add((x, y))
        if bump_map[x][y] != 9:
            basin.add((x, y))
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                if not (dx == 0 and dy == 0):
                    if 0 <= x + dx < len(bump_map):
                        if 0 <= y + dy < len(bump_map[x]):
                            if (x + dx, y + dy) not in visited:
                                q.put((x + dx, y + dy))
    return basin


def part2(bump_map):
    basins = []
    visited = set()
    for i in range(len(bump_map)):
        for j in range(len(bump_map[i])):
            if (i, j) not in visited:
                basin = flood_fill(bump_map, i, j)
                if basin:
                    basins.append(basin)
                    visited |= basin
    basins.sort(key=lambda b: len(b))
    return math.prod(len(b) for b in basins[-3:])


def main():
    with open('day09.txt') as file:
        bump_map = list(parse(file))
    print(part1(bump_map))
    print(part2(bump_map))


if __name__ == '__main__':
    unittest.main(exit=False)
    main()
