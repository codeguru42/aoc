import unittest

input_a = '''
......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####
'''

input_b = '''
#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##..
..##....##
......#...
.####.###.
'''

input_c = '''
.#..#..###
####.###.#
....###.#.
..###.##.#
##.##.#.#.
....###..#
..#.#..#.#
#..#.#.###
.##...##.#
.....#.#..
'''

input_d = '''
.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##
'''


class Day10Test(unittest.TestCase):
    def test_part1a(self):
        expected = ((5, 8), 33)
        actual = part1(input_a)
        self.assertEqual(expected, actual)

    def test_part1b(self):
        expected = ((1, 2), 35)
        actual = part1(input_b)
        self.assertEqual(expected, actual)

    def test_part1c(self):
        expected = ((6, 3), 41)
        actual = part1(input_c)
        self.assertEqual(expected, actual)

    def test_part1d(self):
        expected = ((11, 13), 210)
        actual = part1(input_d)
        self.assertEqual(expected, actual)


def part1(asteroids):
    pass


def part2(asteroids):
    pass


def main():
    with open('day10.txt') as file:
        asteroids = file.readlines()
        print(part1(asteroids))
        print(part2(asteroids))


if __name__ == '__main__':
    main()
