import unittest

example1 = """11111
19991
19191
19991
11111
"""

expected_step1 = """34543
40004
50005
40004
34543
"""

expected_step2 = """45654
51115
61116
51115
45654
"""


class TestDay11(unittest.TestCase):
    def test_do_step1(self):
        starting_energy = list(parse(example1.split()))
        expected = list(parse(expected_step1.split()))
        do_step(starting_energy)
        self.assertEqual(expected, starting_energy)


def parse(file):
    for line in file:
        yield [int(c) for c in line.strip()]


def increase_enery(energy_levels):
    for row in energy_levels:
        for j in range(len(row)):
            row[j] += 1


def flash(energy_levels, i, j, flashed):
    if energy_levels[i][j] > 9 and (i, j) not in flashed:
        flashed.add((i, j))
        for di in (-1, 0, 1):
            for dj in (-1, 0, 1):
                if not(di == 0 and dj == 0):
                    if 0 <= i + di < len(energy_levels):
                        if 0 <= j + dj < len(energy_levels[i]):
                            energy_levels[i + di][j + dj] += 1
                            flash(energy_levels, i + di, j + dj, flashed)


def do_step(energy_levels):
    flashed = set()
    increase_enery(energy_levels)
    for i, row in enumerate(energy_levels):
        for j in range(len(row)):
            flash(energy_levels, i, j, flashed)
    for i, j in flashed:
        energy_levels[i][j] = 0
    return len(flashed)


def part1(energy_levels):
    total = 0
    for steps in range(100):
        total += do_step(energy_levels)
    return total


def part2():
    pass


def main():
    with open('day11.txt') as file:
        starting_energy = list(parse(file))
    print(part1(starting_energy))
    print(part2())


if __name__ == '__main__':
    unittest.main(exit=False)
    main()
