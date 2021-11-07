import itertools
import unittest


class Day11Tests(unittest.TestCase):
    def testHasStraight(self):
        self.assertTrue(has_straight('hijklmmn'))

    def testDoesNotContainIllegalLetters(self):
        self.assertFalse(contains_illegal_letters('hijklmmn'))


def has_straight(password):
    count = 1
    for prev, c in itertools.pairwise(password):
        if chr(ord(prev) + 1) == c:
            count += 1
            if count == 3:
                return True
        else:
            count = 0
    return False


def contains_illegal_letters(password):
    return 'i' not in password and 'o' not in password and 'l' not in password


def part1():
    pass


def part2():
    pass


def main():
    print(part1())
    print(part2())


if __name__ == '__main__':
    unittest.main(exit=False)
    main()
