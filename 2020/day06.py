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


def part2():
    pass


def main():
    with open('day06.txt') as file:
        print(part1(file))
    print(part2())


if __name__ == '__main__':
    unittest.main(exit=False)
    main()
