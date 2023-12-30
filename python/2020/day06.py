import string

import unittest

example = """abc

a
b
c

ab
ac

a
a
a
a

b"""


class TestParse(unittest.TestCase):
    def test_example(self):
        expected = [
            set('abc'),
            set('abc'),
            set('abc'),
            set('a'),
            set('b'),
        ]
        actual = parse_yeses(example.splitlines())
        self.assertEqual(expected, list(actual))


def parse_yeses(file):
    group = set()
    for line in file:
        if line.strip():
            group |= set(line.strip())
        else:
            yield group
            group = set()
    yield group


def part1(file):
    return sum(len(s) for s in parse_yeses(file))


def parse_yeses2(file):
    group = set(string.ascii_letters)
    for line in file:
        if line.strip():
            group &= set(line.strip())
        else:
            yield group
            group = set(string.ascii_letters)
    yield group


def part2(file):
    return sum(len(s) for s in parse_yeses2(file))


def main():
    with open('day06.txt') as file:
        print(part1(file))
    with open('day06.txt') as file:
        print(part2(file))


if __name__ == '__main__':
    unittest.main(exit=False)
    main()
