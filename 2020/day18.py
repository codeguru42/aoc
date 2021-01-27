import unittest

import pyparsing


class TestParse(unittest.TestCase):
    def test1(self):
        result = parse('1 + 2 * 3 + 4 * 5 + 6')
        self.assertEqual(71, result)

    def test2(self):
        result = parse('1 + (2 * 3) + (4 * (5 + 6))')
        self.assertEqual(51, result)

    def test3(self):
        result = parse('2 * 3 + (4 * 5)')
        self.assertEqual(26, result)

    def test4(self):
        result = parse('5 + (8 * 3 + 9 + 3 * 4 * 3)')
        self.assertEqual(437, result)

    def test5(self):
        result = parse('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))')
        self.assertEqual(12240, result)

    def test6(self):
        result = parse('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2')
        self.assertEqual(13632, result)


def parse(line):
    integer = pyparsing.pyparsing_common.integer
    op = pyparsing.oneOf('+ *')
    expr = pyparsing.infixNotation(integer, [(op, 2, pyparsing.opAssoc.LEFT, evaluate)])
    return expr.parseString(line)[0]


class InvalidOperator(Exception):
    pass


def evaluate(s, i, r):
    expr = r[0]
    while len(expr) > 1:
        expr = evalulate_prime(*expr)
    return expr[0]


def evalulate_prime(lhs, op, rhs, *rest):
    if op == '+':
        return [lhs + rhs, *rest]
    elif op == '*':
        return [lhs * rhs, *rest]
    else:
        raise InvalidOperator()


def part1():
    with open('day18.txt') as file:
        return sum(parse(line) for line in file)


def part2():
    pass


def main():
    print(part1())
    print(part2())


if __name__ == '__main__':
    unittest.main(exit=False)
    main()
