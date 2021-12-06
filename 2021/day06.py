import unittest


class TestDay06(unittest.TestCase):
    def test_next_day1(self):
        ages = [3, 4, 3, 1, 2]
        expected = [2, 3, 2, 0, 1]
        self.assertEqual(expected, list(next_day(ages)))

    def test_next_day2(self):
        ages = [2, 3, 2, 0, 1]
        expected = [1, 2, 1, 6, 0, 8]
        self.assertEqual(expected, list(next_day(ages)))


def next_day(ages):
    new_fish = 0
    for age in ages:
        new_age = age - 1
        if new_age == -1:
            new_fish += 1
            yield 6
        else:
            yield new_age

    yield from [8] * new_fish


def spawn_fish(ages, days):
    for _ in range(days):
        ages = next_day(ages)
    return len(list(ages))


def part1(ages):
    return spawn_fish(ages, 80)


def part2():
    pass


def main():
    with open('day06.txt') as file:
        ages = [int(a) for a in file.readline().strip().split(',')]
    print(part1(ages))
    print(part2())


if __name__ == '__main__':
    unittest.main(exit=False)
    main()
