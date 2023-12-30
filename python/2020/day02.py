import collections
import unittest


class Part2Test(unittest.TestCase):
    def test_example1(self):
        self.assertTrue(validate2('1-3 a: abcde'))

    def test_example2(self):
        self.assertFalse(validate2('1-3 b: cdefg'))

    def test_example3(self):
        self.assertFalse(validate2('2-9 c: ccccccccc'))


def part1(lines):
    valid_count = 0
    for line in lines:
        parts = line.split()
        min_count, max_count = parts[0].split('-')
        min_count = int(min_count)
        max_count = int(max_count)
        letter = parts[1][0]
        counts = collections.Counter(parts[2])
        if min_count <= counts[letter] <= max_count:
            valid_count += 1
    return valid_count


def validate2(line):
    parts = line.split()
    index1, index2 = parts[0].split('-')
    index1 = int(index1) - 1
    index2 = int(index2) - 1
    letter = parts[1][0]
    password = parts[2]
    return (password[index1] == letter) != (password[index2] == letter)


def part2(lines):
    valid_count = 0
    for line in lines:
        if validate2(line):
            valid_count += 1
    return valid_count


def main():
    with open('day02.txt') as lines:
        print(part1(lines))
    with open('day02.txt') as lines:
        print(part2(lines))


if __name__ == '__main__':
    unittest.main(exit=False)
    main()
