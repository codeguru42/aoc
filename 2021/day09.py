import unittest


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


def part2():
    pass


def main():
    with open('day09.txt') as file:
        bump_map = list(parse(file))
    print(part1(bump_map))
    print(part2())


if __name__ == '__main__':
    unittest.main(exit=False)
    main()
