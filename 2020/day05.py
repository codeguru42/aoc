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


class TestGetSeat(unittest.TestCase):
    def test_example1(self):
        self.assertEqual((44, 5), get_seat('FBFBBFFRLR'))

    def test_example2(self):
        self.assertEqual((70, 7), get_seat('BFFFBBFRRR'))

    def test_example3(self):
        self.assertEqual((14, 7), get_seat('FFFBBBFRRR'))

    def test_example4(self):
        self.assertEqual((102, 4), get_seat('BBFFBBFRLL'))


class TestGetID(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(357, get_id(44, 5))

    def test_example2(self):
        self.assertEqual(567, get_id(70, 7))

    def test_example3(self):
        self.assertEqual(119, get_id(14, 7))

    def test_example4(self):
        self.assertEqual(820, get_id(102, 4))


def binary_search(next, min, max):
    mid = (min + max) // 2
    if next in ('F', 'L'):
        return min, mid
    return mid + 1, max


def get_seat(boarding_pass):
    matches = re.fullmatch(r'([FB]*)([LR]*)', boarding_pass)
    min_row, max_row = 0, 127
    for c in matches.group(1):
        min_row, max_row = binary_search(c, min_row, max_row)
    min_col, max_col = 0, 7
    for c in matches.group(2):
        min_col, max_col = binary_search(c, min_col, max_col)
    return min_row, min_col


def get_id(row, col):
    return row * 8 + col


def part1(boarding_passes):
    return max(
        get_id(*get_seat(boarding_pass.strip()))
        for boarding_pass in boarding_passes
    )


def part2():
    pass


def main():
    with open('day05.txt') as file:
        print(part1(file))
    print(part2())


if __name__ == '__main__':
    main()
