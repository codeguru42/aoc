import unittest

from aocd import get_data


def parse(data: str):
    for line in data.strip().split('\n'):
        yield line.split()


example = '''noop
addx 3
addx -5
'''


class TestPart1(unittest.TestCase):
    def test_evaluate(self):
        inst = parse(example)
        result = evaluate(inst)
        expected = [1, 2, 3, 16, 20]
        self.assertEqual(expected, list(result))


def evaluate(instructions):
    clock = 1
    x = 1
    for inst in instructions:
        match inst:
            case 'noop', :
                yield clock * x
                clock += 1
            case 'addx', amt:
                yield clock * x
                clock += 1
                yield clock * x
                x += int(amt)
                clock += 1


def part1(instructions):
    return sum(list(evaluate(instructions))[19:220:40])


def part2():
    pass


def main():
    data = get_data(year=2022, day=10)
    inst = list(parse(data))
    answer1 = part1(inst)
    print(answer1)
    answer2 = part2()
    print(answer2)


if __name__ == '__main__':
    main()
