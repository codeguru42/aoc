import unittest

example1 = '''123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i'''


class TestRun(unittest.TestCase):
    def test_example1(self):
        expected = {
            'd': 72,
            'e': 507,
            'f': 492,
            'g': 114,
            'h': 65412,
            'i': 65079,
            'x': 123,
            'y': 456,
        }
        wires = parse(example1.split('\n'))
        actual = {wire: run(wires, wire) for wire in expected}
        self.assertEqual(expected, actual)


def parse(lines):
    parsed = [line.strip().split('->') for line in lines]
    wires = {wire.strip(): op.strip().split() for op, wire in parsed}
    return wires


def run(wires, out_wire):
    values = evaluate({}, out_wire, wires[out_wire])
    return values[out_wire]


def evaluate(values, wire, expr):
    if len(expr) == 1:
        values[wire] = expr[0]
        return values


def part1():
    with open('day07.txt') as file:
        wires = parse(file)
        return run(wires, 'a')


def part2():
    pass


def main():
    print(part1())
    print(part2())


if __name__ == '__main__':
    unittest.main(exit=False)
    main()
