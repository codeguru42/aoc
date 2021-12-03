import unittest
from collections import Counter

example = '''
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
'''


class Day3Test(unittest.TestCase):
    def test_get_o2_rating(self):
        self.assertEqual(23, get_o2_rating(l.strip() for l in example.strip().split()))


def part1():
    with open('day03.txt') as file:
        bits = zip(*[line.strip() for line in file])
        counts = [Counter(b) for b in bits]
        gamma = ''.join(c.most_common(1)[0][0] for c in counts)
        epsilon = ''.join('0' if c == '1' else '1' for c in gamma)
        return int(gamma, 2) * int(epsilon, 2)


def get_o2_rating(bin_numbers):
    result = list(bin_numbers)

    for i in range(len(result[0])):
        if len(result) == 1:
            return int(result[0], 2)
        bits = zip(*result)
        counts = [Counter(b) for b in bits]
        c = counts[i]
        most = c.most_common(1)[0][0] if c['0'] != c['1'] else '1'
        result = [x for x in result if x[i] == most]
    return int(result[0], 2)


def part2():
    pass


def main():
    print(part1())
    print(part2())


if __name__ == '__main__':
    unittest.main(exit=False)
    main()
