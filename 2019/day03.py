import unittest


class Day03Test(unittest.TestCase):
    def test_part1_a(self):
        wires_input = 'R8,U5,L5,D3\nU7,R6,D4,L4'
        distance = part1(wires_input.split())
        self.assertEqual(6, distance)

    def test_part1_b(self):
        wires_input = 'R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83'
        distance = part1(wires_input.split())
        self.assertEqual(159, distance)

    def test_part1_c(self):
        wires_input = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7'
        distance = part1(wires_input.split())
        self.assertEqual(135, distance)


def part1(wires):
    pass


def part2(wires):
    pass


def main():
    with open('day03.txt') as file:
        wires = file.readlines()
        print(part1(wires))
        print(part2(wires))


if __name__ == '__main__':
    main()
