import unittest
from collections import Counter


class TestDay06(unittest.TestCase):
    def test_next_day1(self):
        ages = [3, 4, 3, 1, 2]
        expected = [2, 3, 2, 0, 1]
        self.assertEqual(Counter(expected), next_day(Counter(ages)))

    def test_next_day2(self):
        ages = [2, 3, 2, 0, 1]
        expected = [1, 2, 1, 6, 0, 8]
        self.assertEqual(Counter(expected), next_day(Counter(ages)))

    def test_part1(self):
        with open('day06.txt') as file:
            ages = [int(a) for a in file.readline().strip().split(',')]
            self.assertEqual(365862, part1(ages))


def next_day(ages):
    new_ages = Counter()
    for age in ages:
        new_age = age - 1
        if new_age == -1:
            new_ages[6] += ages[age]
            new_ages[8] += ages[age]
        else:
            new_ages[new_age] += ages[age]
    return new_ages


def spawn_fish(ages, days):
    counts = Counter(ages)
    for _ in range(days):
        counts = next_day(counts)
    return sum(counts.values())


def part1(ages):
    return spawn_fish(ages, 80)


def part2(ages):
    return spawn_fish(ages, 256)


def main():
    with open('day06.txt') as file:
        ages = [int(a) for a in file.readline().strip().split(',')]
    print(part1(ages))
    print(part2(ages))


if __name__ == '__main__':
    unittest.main(exit=False)
    main()
