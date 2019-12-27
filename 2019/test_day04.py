import unittest

from day04 import is_password1, is_password2


class Day04Test(unittest.TestCase):
    def test_part1_a(self):
        self.assertTrue(is_password1(111111))

    def test_part1_b(self):
        self.assertFalse(is_password1(223450))

    def test_part1_c(self):
        self.assertFalse(is_password1(123789))

    def test_part2_a(self):
        self.assertTrue(is_password2(112233))

    def test_part2_b(self):
        self.assertFalse(is_password2(123444))

    def test_part2_c(self):
        self.assertTrue(is_password2(111122))
