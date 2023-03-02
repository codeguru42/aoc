import unittest

from day02 import run_program, part1, part2


class Day02Test(unittest.TestCase):
    def test_run_program_a(self):
        program = [1, 0, 0, 0, 99]
        expected = [2, 0, 0, 0, 99]
        run_program(program)
        self.assertEqual(expected, program)

    def test_run_program_b(self):
        program = [2, 3, 0, 3, 99]
        expected = [2, 3, 0, 6, 99]
        run_program(program)
        self.assertEqual(expected, program)

    def test_run_program_c(self):
        program = [2, 4, 4, 5, 99, 0]
        expected = [2, 4, 4, 5, 99, 9801]
        run_program(program)
        self.assertEqual(expected, program)

    def test_run_program_d(self):
        program = [1, 1, 1, 4, 99, 5, 6, 0, 99]
        expected = [30, 1, 1, 4, 2, 5, 6, 0, 99]
        run_program(program)
        self.assertEqual(expected, program)

    def test_part1(self):
        with open('day02.txt') as file:
            int_codes = [int(x) for x in file.readline().split(',')]
            result = part1(int_codes)
            expected = 3085697
            self.assertEqual(expected, result)

    def test_part2(self):
        with open('day02.txt') as file:
            int_codes = [int(x) for x in file.readline().split(',')]
            target = 19690720
            result = part2(int_codes, 19690720)
            expected = 9425
            self.assertEqual(expected, result)
