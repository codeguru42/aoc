import unittest
from io import StringIO

from aoc import sliding_window

example_rules = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""


class TestDay14(unittest.TestCase):
    def setUp(self) -> None:
        _, self.rules = parse(StringIO(example_rules))

    def test_step1(self):
        self.assertEqual("NCNBCHB", "".join(step("NNCB", self.rules)))

    def test_step2(self):
        self.assertEqual("NBCCNBBBCBHCB", "".join(step("NCNBCHB", self.rules)))

    def test_step3(self):
        self.assertEqual("NBBBCNCCNBBNBNBBCHBHHBCHB", "".join(step("NBCCNBBBCBHCB", self.rules)))

    def test_step4(self):
        self.assertEqual("NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB", "".join(step("NBBBCNCCNBBNBNBBCHBHHBCHB", self.rules)))


def parse(file):
    d = {}
    p = file.readline().strip()
    file.readline()  # skip blank line
    for line in file:
        x, y = line.strip().split(' -> ')
        d[x] = y
    return p, d


def step(polymer, rules):
    for pair in sliding_window(polymer, 2):
        yield pair[0]
        key = "".join(pair)
        if key in rules:
            yield rules[key]
    yield pair[1]


def part1():
    pass


def part2():
    pass


def main():
    print(part1())
    print(part2())


if __name__ == '__main__':
    unittest.main()
    main()
