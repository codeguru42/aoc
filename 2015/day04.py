import unittest


class TestPart1(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(609043, part1('abcdef'))

    def test_example2(self):
        self.assertEqual(1048970, part1('pqrstuv'))


def part1(secret_key):
    pass


def part2(secret_key):
    pass


def main():
    secret_key = 'bgvyzdsv'
    print(part1(secret_key))
    print(part2(secret_key))


if __name__ == '__main__':
    unittest.main()
    main()
