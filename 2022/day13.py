import ast
import unittest

from aocd import get_data


class TestPart1(unittest.TestCase):
    def test_is_in_order1(self):
        self.assertTrue(is_in_order([1, 1, 3, 1, 1], [1, 1, 5, 1, 1]))

    def test_is_in_order2(self):
        self.assertTrue(is_in_order([[1], [2, 3, 4]], [[1], 4]))

    def test_is_in_order3(self):
        self.assertFalse(is_in_order([9], [[8, 7, 6]]))

    def test_is_in_order4(self):
        self.assertTrue(is_in_order([[4, 4], 4, 4], [[4, 4], 4, 4, 4]))

    def test_is_in_order5(self):
        self.assertFalse(is_in_order([7, 7, 7, 7], [7, 7, 7]))

    def test_is_in_order6(self):
        self.assertTrue(is_in_order([], [3]))

    def test_is_in_order7(self):
        self.assertFalse(is_in_order([[[]]], [[]]))

    def test_is_in_order8(self):
        self.assertFalse(is_in_order([1, [2, [3, [4, [5, 6, 7]]]], 8, 9], [1, [2, [3, [4, [5, 6, 0]]]], 8, 9]))


def parse(data):
    for pair in data.strip().split('\n\n'):
        yield [ast.literal_eval(line) for line in pair.split('\n')]


def is_in_order(p1, p2):
    match p1, p2:
        case [x1, *rest1], [x2, *rest2]:
            match x1, x2:
                case [int(), int()]:
                    return x1 < x2 and is_in_order(rest1, rest2)
                case [list(), list()]:
                    return is_in_order(x1, x2) and is_in_order(rest1, rest2)
                case [int(), list()]:
                    return is_in_order([x1], x2) and is_in_order(rest1, rest2)
                case [list(), int()]:
                    return is_in_order(x1, [x2]) and is_in_order(rest1, rest2)


def get_indexes(packets):
    for i, p in enumerate(packets):
        if is_in_order(*p):
            yield i


def part1(packets):
    return sum(get_indexes(packets))


def part2():
    pass


def main():
    data = get_data(year=2022, day=13)
    packets = parse(data)
    answer1 = part1(packets)
    print(answer1)
    answer2 = part2()
    print(answer2)


if __name__ == '__main__':
    main()
