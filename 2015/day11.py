import itertools
import unittest


class Day11Tests(unittest.TestCase):
    def testHasStraight(self):
        self.assertTrue(has_straight('hijklmmn'))

    def testDoesNotHaveStraight(self):
        self.assertFalse(has_straight('abbceffg'))

    def testDoesNotContainIllegalLetters(self):
        self.assertFalse(contains_illegal_letters('hijklmmn'))

    def testContainsNonOverlappingPairs(self):
        self.assertTrue(contains_non_overlapping_pairs('abbceffg'))

    def testDoesNotContainNonOverlappingPairs(self):
        self.assertFalse(contains_non_overlapping_pairs('abbcegjk'))

    def testValidPassword1(self):
        self.assertFalse(valid_password('hijklmmn'))

    def testValidPassword2(self):
        self.assertFalse(valid_password('abbceffg'))

    def testValidPassword3(self):
        self.assertFalse(valid_password('abbcegjk'))

    def testIncrementBase26_1(self):
        self.assertEqual([1], list(increment_base26((0, ))))

    def testIncrementBase26_2(self):
        self.assertEqual([0, 1], list(increment_base26((25, ))))

    def testIncrementBase26_3(self):
        self.assertEqual([1, 1], list(increment_base26((0, 1))))


def valid_password(password):
    return has_straight(password) and not contains_illegal_letters(password) and contains_non_overlapping_pairs(password)


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


def contains_non_overlapping_pairs(password):
    pairs = set()
    for c, g in itertools.groupby(password):
        count = len(list(g))
        if count >= 2 and c not in pairs:
            count += 1
            pairs.add(c)
    return len(pairs) >= 2


def increment_base26(num):
    if len(num) == 0:
        yield 1
    else:
        n = num[0] + 1
        yield n % 26
        if n // 26 > 0:
            yield from increment_base26(num[1:])
        else:
            yield from reversed(num[1:])


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