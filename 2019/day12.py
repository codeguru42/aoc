import re
import unittest

example_moons = '''
<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>
'''


class TestDay12(unittest.TestCase):
    def test_parse_moons(self):
        moons = parse_moons(example_moons.strip().split('\n'))
        expected = [(-1, 0, 2), (2, -10, -7), (4, -8, 8), (3, 5, -1)]
        self.assertEqual(moons, expected)

    def test_step1(self):
        moon_coords = [(-1, 0, 2), (2, -10, -7), (4, -8, 8), (3, 5, -1)]
        moons = [Moon(mc) for mc in moon_coords]
        result = step(moons)
        expected = [] # TODO fill out expected values
        self.assertEqual(result, expected)


def parse_moons(file):
    moons = []
    for line in file:
        matches = re.search(r'<x=(-?[0-9]+), ?y=(-?[0-9]+), ?z=(-?[0-9]+)>', line)
        moon = tuple(int(n) for n in matches.group(1, 2, 3))
        moons.append(moon)
    return moons


def step(moons):
    pass


def part1(moons):
    pass


def part2(moons):
    pass


def main():
    with open('day12.txt') as file:
        moons = parse_moons(file)
        print(part1(moons))
        print(part2(moons))


if __name__ == '__main__':
    main()
