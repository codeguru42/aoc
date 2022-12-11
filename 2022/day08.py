import unittest

from aocd import get_data

example = '''30373
25512
65332
33549
35390
'''


class TestPart1(unittest.TestCase):
    def test_increasing_subsequence1(self):
        row = example.split('\n')[1]
        expected = [(0, '2'), (1, '5')]
        self.assertEqual(expected, list(increasing_subsequence(row)))

    def test_increasing_subsequence2(self):
        row = example.split('\n')[2]
        expected = [(0, '6')]
        self.assertEqual(expected, list(increasing_subsequence(row)))

    def test_increasing_subsequence3(self):
        row = example.split('\n')[3]
        expected = [(0, '3'), (2, '5'), (4, '9')]
        self.assertEqual(expected, list(increasing_subsequence(row)))


def increasing_subsequence(row):
    highest = 0
    for i, height in enumerate(row):
        if i == 0 or height > highest:
            highest = height
            yield i, height


def part1():
    pass


def part2():
    pass


def main():
    data = get_data(year=2022, day=8)
    answer1 = part1()
    print(answer1)
    answer2 = part2()
    print(answer2)


if __name__ == '__main__':
    main()
