import itertools
import typing
import unittest


class TestDay8(unittest.TestCase):
    def test_build_map(self):
        signal = 'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab'.split()
        expected = {
            ''.join(sorted('acedgfb')): 8,
            ''.join(sorted('cdfbe')): 5,
            ''.join(sorted('gcdfa')): 2,
            ''.join(sorted('fbcad')): 3,
            ''.join(sorted('dab')): 7,
            ''.join(sorted('cefabd')): 9,
            ''.join(sorted('cdfgeb')): 6,
            ''.join(sorted('eafb')): 4,
            ''.join(sorted('cagedb')): 0,
            ''.join(sorted('ab')): 1,
        }
        self.assertEqual(expected, build_map(signal))


default_seven_segment_map = {
    'abcefg': 0,
    'cf': 1,
    'acdeg': 2,
    'acedfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9,
}


def build_map(signal: typing.Iterable[str]):
    length_map = dict((key, list(group)) for key, group in itertools.groupby(sorted(signal, key=len), key=len))
    seven_segment_map = {
        1: set(length_map[2][0]),
        4: set(length_map[4][0]),
        7: set(length_map[3][0]),
        8: set(length_map[7][0]),
    }

    # 3 has five segments and contains the same segments as in a 1
    seven_segment_map[3] = [set(x) for x in length_map[5] if seven_segment_map[1] < set(x)][0]
    # 5 has five segments and contains segments that are in 4 but not in 1
    seven_segment_map[5] = [set(x) for x in length_map[5] if (seven_segment_map[4] - seven_segment_map[1]) < set(x)][0]
    # 6 has six segments and does not contain all segments in 1
    seven_segment_map[6] = [set(x) for x in length_map[6] if not seven_segment_map[1] < set(x)][0]
    # 9 has six segments and contains all segments in 4
    seven_segment_map[9] = [set(x) for x in length_map[6] if seven_segment_map[4] < set(x)][0]

    # 0 has 6 segments and isn't 6 or 9
    seven_segment_map[0] = [set(x) for x in length_map[6] if set(x) not in [seven_segment_map[i] for i in (6, 9)]][0]
    # 2 has 5 segments and isn't 3 or 5
    seven_segment_map[2] = [set(x) for x in length_map[5] if set(x) not in [seven_segment_map[i] for i in (3, 5)]][0]

    # invert mapping but key is a string with characters in alphabetical order
    return {''.join(sorted(value)): key for key, value in seven_segment_map.items()}


def parse(file):
    for line in file:
        signal, output = line.strip().split(' | ')
        yield signal.split(), output.split()


def part1(data):
    count = 0
    for _, output in data:
        count += sum(1 for x in output if len(x) in [2, 3, 4, 7])
    return count


def decode(signal, output):
    seven_segment_map = build_map(signal)
    for segs in output:
        yield seven_segment_map[''.join(sorted(segs))]


def part2(data):
    decoded = [decode(signal, output) for signal, output in data]
    return sum(int(''.join(str(digit) for digit in digits)) for digits in decoded)


def main():
    with open('day08.txt') as file:
        data = list(parse(file))
    print(part1(data))
    print(part2(data))


if __name__ == '__main__':
    unittest.main(exit=False)
    main()
