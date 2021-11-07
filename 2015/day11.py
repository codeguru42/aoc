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
