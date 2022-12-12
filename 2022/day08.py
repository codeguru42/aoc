import unittest

from aocd import get_data

example = '''30373
25512
65332
33549
35390
'''


def parse(data):
    return data.strip().split('\n')


class TestPart1(unittest.TestCase):
    def test1(self):
        self.assertEqual(21, part1(parse(example)))

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

    def test_get_visible_rows(self):
        forest = parse(example)
        expected = [
            ((0, 0), '3'),
            ((0, 3), '7'),
            ((1, 0), '2'),
            ((1, 1), '5'),
            ((2, 0), '6'),
            ((3, 0), '3'),
            ((3, 2), '5'),
            ((3, 4), '9'),
            ((4, 0), '3'),
            ((4, 1), '5'),
            ((4, 3), '9'),
        ]
        self.assertEqual(expected, list(get_visible(forest)))

    def test_get_visible_rows_reversed(self):
        forest = [reversed(row) for row in parse(example)]
        expected = [
            ((0, 4), '3'),
            ((0, 3), '7'),
            ((1, 4), '2'),
            ((1, 2), '5'),
            ((2, 4), '2'),
            ((2, 3), '3'),
            ((2, 1), '5'),
            ((2, 0), '6'),
            ((3, 4), '9'),
            ((4, 4), '0'),
            ((4, 3), '9'),
        ]
        self.assertEqual(expected, list(get_visible(forest, reversed=True)))

    def test_get_visible_rows_transposed(self):
        forest = zip(*parse(example))
        expected = [
            ((0, 0), '3'),
            ((2, 0), '6'),
            ((0, 1), '0'),
            ((1, 1), '5'),
            ((0, 2), '3'),
            ((1, 2), '5'),
            ((0, 3), '7'),
            ((4, 3), '9'),
            ((0, 4), '3'),
            ((3, 4), '9'),
        ]
        self.assertEqual(expected, list(get_visible(forest, transposed=True)))


def increasing_subsequence(row):
    highest = 0
    for i, height in enumerate(row):
        if i == 0 or height > highest:
            highest = height
            yield i, height


def get_visible(forest, reversed=False, transposed=False):
    for i, row in enumerate(forest):
        row = list(row)
        n = len(row)
        sub = increasing_subsequence(row)
        for j, height in sub:
            if reversed:
                j = n - j - 1
            if transposed:
                yield (j, i), height
            else:
                yield (i, j), height


def transpose(array):
    return zip(*array)


def part1(forest):
    visible = set(get_visible(forest))
    visible |= set(get_visible((reversed(row) for row in forest), reversed=True))
    transposed = list(transpose(forest))
    visible |= set(get_visible(transposed, transposed=True))
    visible |= set(get_visible((reversed(row) for row in transposed), reversed=True, transposed=True))
    return len(visible)


class TestPart2(unittest.TestCase):
    def test_scenic_score1(self):
        forest = parse(example)
        self.assertEqual(4, scenic_score(forest, 1, 2))


def take_while(seq, f):
    for item in seq:
        if f(item):
            yield item


def less_than(y):
    return lambda x: x < y


def scenic_score(forest, i, j):
    left = list(take_while((-int(t) for t in forest[i][j::-1]), less_than(forest[i][j])))
    right = list(take_while((-int(t) for t in forest[i][j:]), less_than(forest[i][j])))
    transposed = list(transpose(forest))
    up = list(take_while((-int(t) for t in transposed[j][i::-1]), less_than(forest[i][j])))
    down = list(take_while((-int(t) for t in transposed[j][i:]), less_than(forest[i][j])))
    return len(left) * len(right) * len(up) * len(down)


def part2():
    pass


def main():
    data = get_data(year=2022, day=8)
    forest = parse(data)
    answer1 = part1(forest)
    print(answer1)
    answer2 = part2()
    print(answer2)


if __name__ == '__main__':
    main()
