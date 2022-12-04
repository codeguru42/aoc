import unittest

from aocd import get_data


example = '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
'''


class TestDay04(unittest.TestCase):
    def test_part1(self):
        ranges = parse(example)
        result = part1(ranges)
        self.assertEqual(2, result)


def parse(data):
    for line in data.strip().split('\n'):
        ranges = line.split(',')
        yield [[int(x) for x in r.split('-')] for r in ranges]


def part1(ranges):
    count = 0
    for r1, r2 in ranges:
        x1, x2 = r1
        y1, y2 = r2
        if (x1 <= y1 and y2 <= x2) or (y1 <= x1 and x2 <= y2):
            count += 1
    return count


def part2():
    pass


def main():
    data = get_data(year=2022, day=4)
    ranges = list(parse(data))
    answer1 = part1(ranges)
    print(answer1)
    answer2 = part2()
    print(answer2)


if __name__ == '__main__':
    main()
