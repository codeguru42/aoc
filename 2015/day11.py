import itertools
import unittest


class Day11Tests(unittest.TestCase):
    def test_has_straight(self):
        self.assertTrue(has_straight('hijklmmn'))

    def test_does_not_have_straight(self):
        self.assertFalse(has_straight('abbceffg'))

    def test_does_not_contain_illegal_letters(self):
        self.assertFalse(contains_illegal_letters('hijklmmn'))

    def test_contains_non_overlapping_pairs(self):
        self.assertTrue(contains_non_overlapping_pairs('abbceffg'))

    def test_does_not_contain_non_overlapping_pairs(self):
        self.assertFalse(contains_non_overlapping_pairs('abbcegjk'))

    def test_valid_password1(self):
        self.assertFalse(valid_password('hijklmmn'))

    def test_valid_password2(self):
        self.assertFalse(valid_password('abbceffg'))

    def test_valid_password3(self):
        self.assertFalse(valid_password('abbcegjk'))

    def test_increment_base26_1(self):
        self.assertEqual([1], list(increment_base26((0, ))))

    def test_increment_base26_2(self):
        self.assertEqual([0, 1], list(increment_base26((25, ))))

    def test_increment_base26_3(self):
        self.assertEqual([1, 1], list(increment_base26((0, 1))))

    def test_string_to_base26_1(self):
        self.assertEqual([1, ], list(string_to_base26('a')))

    def test_string_to_base26_2(self):
        self.assertEqual([0, ], list(string_to_base26('z')))

    def test_string_to_base26_3(self):
        self.assertEqual([0] + list(range(25, 0, -1)), list(string_to_base26('abcdefghijklmnopqrstuvwxyz')))


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


def string_to_base26(s):
    return reversed([(ord(c) - ord('a') + 1) % 26 for c in s])


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
