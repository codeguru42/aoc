import re
import unittest


class TestBinarySearch(unittest.TestCase):
    def test_example1(self):
        self.assertEqual((0, 63), binary_search('F', 0, 127))

    def test_example2(self):
        self.assertEqual((32, 63), binary_search('B', 0, 63))

    def test_example3(self):
        self.assertEqual((32, 47), binary_search('F', 32, 63))

    def test_example4(self):
        self.assertEqual((40, 47), binary_search('B', 32, 47))

    def test_example5(self):
        self.assertEqual((44, 47), binary_search('B', 40, 47))

    def test_example6(self):
        self.assertEqual((44, 45), binary_search('F', 44, 47))

    def test_example7(self):
        self.assertEqual((44, 44), binary_search('F', 44, 45))

    def test_example8(self):
        self.assertEqual((4, 7), binary_search('R', 0, 7))

    def test_example9(self):
        self.assertEqual((4, 5), binary_search('L', 4, 7))

    def test_example10(self):
        self.assertEqual((5, 5), binary_search('R', 4, 5))


def binary_search(next, min, max):
    mid = (min + max) // 2
    if next in ('F', 'L'):
        return min, mid
    return mid + 1, max


def part1():
    pass


def part2():
    pass


def main():
    print(part1())
    print(part2())


if __name__ == '__main__':
    main()
