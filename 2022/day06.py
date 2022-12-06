import collections
import unittest
from itertools import islice

from aocd import get_data


def sliding_window(iterable, n):
    # sliding_window('ABCDEFG', 4) --> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = collections.deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)


class TestPart1(unittest.TestCase):
    def test1(self):
        signal = 'bvwbjplbgvbhsrlpgdmjqwftvncz'
        self.assertEqual(5, part1(signal))

    def test2(self):
        signal = 'nppdvjthqldpwncqszvftbrmjlhg'
        self.assertEqual(6, part1(signal))

    def test3(self):
        signal = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'
        self.assertEqual(10, part1(signal))

    def test4(self):
        signal = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'
        self.assertEqual(11, part1(signal))


def part1(signal):
    for i, packet in enumerate(sliding_window(signal, 4)):
        if len(set(packet)) == len(packet):
            return i + len(packet)


class TestPart2(unittest.TestCase):
    def test1(self):
        signal = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
        self.assertEqual(19, part2(signal))

    def test2(self):
        signal = 'bvwbjplbgvbhsrlpgdmjqwftvncz'
        self.assertEqual(23, part2(signal))

    def test3(self):
        signal = 'nppdvjthqldpwncqszvftbrmjlhg'
        self.assertEqual(23, part2(signal))

    def test4(self):
        signal = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'
        self.assertEqual(29, part2(signal))

    def test5(self):
        signal = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'
        self.assertEqual(26, part2(signal))


def part2(signal):
    for i, packet in enumerate(sliding_window(signal, 14)):
        if len(set(packet)) == len(packet):
            return i + len(packet)


def main():
    data = get_data(year=2022, day=6)
    answer1 = part1(data)
    print(answer1)
    answer2 = part2(data)
    print(answer2)


if __name__ == '__main__':
    main()
