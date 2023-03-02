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
