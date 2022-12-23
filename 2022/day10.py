import unittest
from itertools import islice, zip_longest

from aocd import get_data


def parse(data: str):
    for line in data.strip().split('\n'):
        yield line.split()


def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


example = '''noop
addx 3
addx -5
'''


class TestPart1(unittest.TestCase):
    def test_evaluate(self):
        inst = parse(example)
        result = evaluate(inst)
        expected = [(1, 1), (2, 1), (3, 1), (4, 4), (5, 4)]
        self.assertEqual(expected, list(result))

    def test_part1(self):
        inst = parse(example2)
        result = part1(inst)
        self.assertEqual(13140, result)


def evaluate(instructions):
    clock = 1
    x = 1
    for inst in instructions:
        match inst:
            case 'noop', :
                yield clock, x
                clock += 1
            case 'addx', amt:
                yield clock, x
                clock += 1
                yield clock, x
                x += int(amt)
                clock += 1


def part1(instructions):
    return sum(islice((clock * x for clock, x in evaluate(instructions)), 19, 220, 40))


def scan_line(seq):
    for clock, x in seq:
        if (clock - 1) % 40 <= x <= (clock + 1) % 40:
            yield '#'
        else:
            yield '.'


example2 = '''addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
'''

expected_scanline = '''##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....
'''


class TestPart2(unittest.TestCase):
    def test_part2(self):
        inst = parse(example2)
        result = part2(inst)
        self.assertEqual(expected_scanline, result)


def part2(instructions):
    lines = scan_line(evaluate(instructions))
    return '\n'.join(''.join(line) for line in grouper(lines, 40))


def main():
    data = get_data(year=2022, day=10)
    inst = list(parse(data))
    answer1 = part1(inst)
    print(answer1)
    answer2 = part2(inst)
    print(answer2)


if __name__ == '__main__':
    main()
