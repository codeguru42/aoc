import unittest

example_moons = '''
<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>
'''


class TestDay12(unittest.TestCase):
    def test_parse_moons(self):
        moons = parse_moons(example_moons.split())
        expected = [(1, 0, 2), (2, -10, -7), (4, -8, 8), (3, 5, -1)]
        self.assertEqual(moons, expected)


def parse_moons(file):
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
