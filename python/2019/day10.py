import unittest
from collections import Counter

import numpy as np

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
        actual = part1(parse_asteroids(input_a.split()))
        self.assertEqual(expected, actual)

    def test_part1b(self):
        expected = ((1, 2), 35)
        actual = part1(parse_asteroids(input_b.split()))
        self.assertEqual(expected, actual)

    def test_part1c(self):
        expected = ((6, 3), 41)
        actual = part1(parse_asteroids(input_c.split()))
        self.assertEqual(expected, actual)

    def test_part1d(self):
        expected = ((11, 13), 210)
        actual = part1(parse_asteroids(input_d.split()))
        self.assertEqual(expected, actual)


def parse_asteroids(lines):
    return [
        (j, i)
        for i, line in enumerate(lines)
        for j, cell in enumerate(line)
        if cell == '#'
    ]


def part1(asteroids):
    counts = Counter()
    for a1 in asteroids:
        a1 = np.array(a1)
        for a2 in asteroids:
            a2 = np.array(a2)
            if not np.all(a1 == a2):
                delta = a2 - a1
                gcd = np.gcd(*delta)
                delta = delta / gcd
                x = a1 + delta
                blocked = False
                while not np.all(x == a2):
                    if tuple(x) in asteroids:
                        blocked = True
                        break
                    x += delta
                if not blocked:
                    counts[tuple(a1)] += 1
    m, = counts.most_common(1)
    return m


def part2(asteroids):
    pass


def main():
    with open('day10.txt') as file:
        asteroids = parse_asteroids(file.readlines())
        print(part1(asteroids))
        print(part2(asteroids))


if __name__ == '__main__':
    main()
