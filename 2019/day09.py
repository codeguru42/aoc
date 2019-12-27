import unittest

from int_code import run_program


class Day09Test(unittest.TestCase):
    def test_part1_a(self):
        program = [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]
        result = list(run_program(program))
        self.assertEqual(program, result)

    def test_part1_b(self):
        program = [1102, 34915192, 34915192, 7, 4, 7, 99, 0]
        expected = 34915192 * 34915192
        result = list(run_program(program))
        self.assertEqual([expected], result)

    def test_part1_c(self):
        program = [104, 1125899906842624, 99]
        expected = program[1]
        result = list(run_program(program))
        self.assertEqual([expected], result)


def part1(program):
    itr = run_program(program)
    next(itr)
    return itr.send(1)


def part2(program):
    itr = run_program(program)
    next(itr)
    return itr.send(2)




def main():
    with open('day09.txt') as file:
        int_codes = [int(x) for x in file.readline().split(',')]
        print(part1(int_codes))
        print(part2(int_codes))


if __name__ == '__main__':
    main()
