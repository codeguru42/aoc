import unittest
from hashlib import md5
from itertools import count


class TestPart1(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(609043, part1(b'abcdef'))

    def test_example2(self):
        self.assertEqual(1048970, part1(b'pqrstuv'))


def hashes(secret_key):
    for x in count():
        yield x, md5(secret_key + str(x).encode('utf8'))


def part1(secret_key):
    for x, hash in hashes(secret_key):
        if hash.hexdigest().startswith('0'*5):
            return x


def part2(secret_key):
    pass


def main():
    secret_key = b'bgvyzdsv'
    print(part1(secret_key))
    print(part2(secret_key))


if __name__ == '__main__':
    unittest.main(exit=False)
    main()
