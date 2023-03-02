import ast
import unittest

from aocd import get_data

example = '''[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]'''


class TestPart1(unittest.TestCase):
    def test_is_in_order1(self):
        self.assertTrue(is_in_order([1, 1, 3, 1, 1], [1, 1, 5, 1, 1]))

    def test_is_in_order2(self):
        self.assertTrue(is_in_order([[1], [2, 3, 4]], [[1], 4]))

    def test_is_in_order3(self):
        result = is_in_order([9], [[8, 7, 6]])
        self.assertFalse(result)
        self.assertIsNotNone(result)

    def test_is_in_order4(self):
        self.assertTrue(is_in_order([[4, 4], 4, 4], [[4, 4], 4, 4, 4]))

    def test_is_in_order5(self):
        result = is_in_order([7, 7, 7, 7], [7, 7, 7])
        self.assertFalse(result)
        self.assertIsNotNone(result)

    def test_is_in_order6(self):
        self.assertTrue(is_in_order([], [3]))

    def test_is_in_order7(self):
        result = is_in_order([[[]]], [[]])
        self.assertFalse(result)
        self.assertIsNotNone(result)

    def test_is_in_order8(self):
        result = is_in_order([1, [2, [3, [4, [5, 6, 7]]]], 8, 9], [1, [2, [3, [4, [5, 6, 0]]]], 8, 9])
        self.assertFalse(result)
        self.assertIsNotNone(result)

    def test_is_in_order9(self):
        self.assertTrue(is_in_order([[1], 3], [[2], 2]))

    def test_is_in_order10(self):
        l1 = [[8, [[2, 6, 8, 4], 1]], [[], [], [[8, 3, 0, 8], 6], [3, [1, 3], 8]], [1, 10, [2, 2, [0, 5, 2, 9], [4, 10, 4, 8]]], [[8, 9, 6], [[], [4]]]]
        l2 = [[[[8]], 3, [1, 7, 5]], [[[3, 1, 2, 8], [4, 5], [1, 0, 4, 2, 9], 1, []], 8, 5, [5, [], [9, 4, 7, 3, 9], [0, 10, 10, 6, 0], [7, 5, 5, 3]], 6]]
        result = is_in_order(l1, l2)
        self.assertTrue(result)

    def test_part1(self):
        packets = parse(example)
        self.assertEqual(part1(packets), 13)


def parse(data):
    for pair in data.strip().split('\n\n'):
        yield [ast.literal_eval(line) for line in pair.split('\n')]


def is_in_order(p1, p2):
    match p1, p2:
        case [[], []]:
            return False
        case [[], _]:
            return True
        case [int(x1), *rest1], [int(x2), *rest2]:
            return x1 < x2 or x1 == x2 and is_in_order(rest1, rest2)
        case [list(x1), *rest1], [list(x2), *rest2]:
            return is_in_order(x1, x2) or x1 == x2 and is_in_order(rest1, rest2)
        case [int(x1), *rest1], _:
            return is_in_order([[x1], rest1], p2)
        case _, [int(x2), *rest2]:
            return is_in_order(p1, [[x2], rest2])
    return False


def get_indexes(packets):
    for i, p in enumerate(packets):
        if is_in_order(*p):
            yield i + 1


def part1(packets):
    return sum(get_indexes(packets))


class TestPart2(unittest.TestCase):
    def test_part2(self):
        packets = parse(example)
        self.assertEqual(140, part2(packets))


class PacketKey:
    def __init__(self, packet):
        self.packet = packet

    def __lt__(self, other):
        return is_in_order(self.packet, other.packet)


def part2(packet_pairs):
    packets = [i for sub in packet_pairs for i in sub] + [[[2]], [[6]]]
    packets.sort(key=PacketKey)
    return (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)


def main():
    data = get_data(year=2022, day=13)
    packets = list(parse(data))
    answer1 = part1(packets)
    print(answer1)
    answer2 = part2(packets)
    print(answer2)


if __name__ == '__main__':
    main()
