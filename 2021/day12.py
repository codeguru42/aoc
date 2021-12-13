import unittest
from collections import defaultdict


class TestDay12(unittest.TestCase):
    def test_parse(self):
        example = """start-A
            start-b
            A-c
            A-b
            b-d
            A-end
            b-end """
        expected = {
            'start': {'A', 'b'},
            'A': {'start', 'b', 'c', 'end'},
            'c': {'A'},
            'b': {'start', 'A', 'd', 'end'},
            'd': {'b'},
            'end': {'A', 'b'},
        }
        actual = parse(example.split('\n'))
        self.assertEqual(expected, actual)


def parse(file):
    g = defaultdict(lambda: set())
    for line in file:
        x, y = line.strip().split('-')
        g[x].add(y)
        g[y].add(x)
    return g


def part1():
    pass


def part2():
    pass


def main():
    with open('day12.txt') as file:
        g = parse(file)
        print(g)
    print(part1())
    print(part2())


if __name__ == '__main__':
    unittest.main(exit=False)
    main()
