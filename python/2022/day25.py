import unittest

from aocd import get_data


class TestPart1(unittest.TestCase):
    def test_snafu_to_int1(self):
        self.assertEqual(snafu_to_int('1'), 1)

    def test_snafu_to_int2(self):
        self.assertEqual(snafu_to_int('2'), 2)

    def test_snafu_to_int3(self):
        self.assertEqual(snafu_to_int('1='), 3)

    def test_snafu_to_int4(self):
        self.assertEqual(snafu_to_int('1-'), 4)

    def test_snafu_to_int5(self):
        self.assertEqual(snafu_to_int('10'), 5)

    def test_snafu_to_int6(self):
        self.assertEqual(snafu_to_int('11'), 6)

    def test_snafu_to_int7(self):
        self.assertEqual(snafu_to_int('12'), 7)

    def test_snafu_to_int8(self):
        self.assertEqual(snafu_to_int('2='), 8)

    def test_snafu_to_int9(self):
        self.assertEqual(snafu_to_int('2-'), 9)

    def test_snafu_to_int10(self):
        self.assertEqual(snafu_to_int('20'), 10)

    def test_snafu_to_int11(self):
        self.assertEqual(snafu_to_int('1=0'), 15)

    def test_snafu_to_int12(self):
        self.assertEqual(snafu_to_int('1-0'), 20)

    def test_snafu_to_int13(self):
        self.assertEqual(snafu_to_int('1=11-2'), 2022)

    def test_snafu_to_int14(self):
        self.assertEqual(snafu_to_int('1-0---0'), 12345)

    def test_snafu_to_int15(self):
        self.assertEqual(snafu_to_int('1121-1110-1=0'), 314159265)

    def test_snafu_to_int16(self):
        self.assertEqual(snafu_to_int('1=-0-2'), 1747)

    def test_snafu_to_int17(self):
        self.assertEqual(snafu_to_int('12111'), 906)

    def test_snafu_to_int18(self):
        self.assertEqual(snafu_to_int('2=0='), 198)

    def test_snafu_to_int19(self):
        self.assertEqual(snafu_to_int('21'), 11)

    def test_snafu_to_int20(self):
        self.assertEqual(snafu_to_int('2=01'), 201)

    def test_snafu_to_int21(self):
        self.assertEqual(snafu_to_int('111'), 31)

    def test_snafu_to_int22(self):
        self.assertEqual(snafu_to_int('20012'), 1257)

    def test_snafu_to_int23(self):
        self.assertEqual(snafu_to_int('112'), 32)

    def test_snafu_to_int24(self):
        self.assertEqual(snafu_to_int('1=-1='), 353)

    def test_snafu_to_int25(self):
        self.assertEqual(snafu_to_int('1-12'), 107)

    def test_snafu_to_int26(self):
        self.assertEqual(snafu_to_int('12'), 7)

    def test_snafu_to_int27(self):
        self.assertEqual(snafu_to_int('1='), 3)

    def test_snafu_to_int28(self):
        self.assertEqual(snafu_to_int('122'), 37)

    def test_int_to_snafu1(self):
        self.assertEqual(int_to_snafu(1), '1')

    def test_int_to_snafu2(self):
        self.assertEqual(int_to_snafu(2), '2')

    def test_int_to_snafu3(self):
        self.assertEqual(int_to_snafu(3), '1=')

    def test_int_to_snafu4(self):
        self.assertEqual(int_to_snafu(4), '1-')

    def test_int_to_snafu5(self):
        self.assertEqual(int_to_snafu(5), '10')

    def test_int_to_snafu6(self):
        self.assertEqual(int_to_snafu(6), '11')

    def test_int_to_snafu7(self):
        self.assertEqual(int_to_snafu(7), '12')

    def test_int_to_snafu8(self):
        self.assertEqual(int_to_snafu(8), '2=')

    def test_int_to_snafu9(self):
        self.assertEqual(int_to_snafu(9), '2-')

    def test_int_to_snafu10(self):
        self.assertEqual(int_to_snafu(10), '20')

    def test_int_to_snafu11(self):
        self.assertEqual(int_to_snafu(15), '1=0')

    def test_int_to_snafu12(self):
        self.assertEqual(int_to_snafu(20), '1-0')

    def test_int_to_snafu13(self):
        self.assertEqual(int_to_snafu(2022), '1=11-2')

    def test_int_to_snafu14(self):
        self.assertEqual(int_to_snafu(12345), '1-0---0')

    def test_int_to_snafu15(self):
        self.assertEqual(int_to_snafu(314159265), '1121-1110-1=0')

    def test_int_to_snafu16(self):
        self.assertEqual(int_to_snafu(1747), '1=-0-2')

    def test_int_to_snafu17(self):
        self.assertEqual(int_to_snafu(906), '12111')

    def test_int_to_snafu18(self):
        self.assertEqual(int_to_snafu(198), '2=0=')

    def test_int_to_snafu19(self):
        self.assertEqual(int_to_snafu(11), '21')

    def test_int_to_snafu20(self):
        self.assertEqual(int_to_snafu(201), '2=01')

    def test_int_to_snafu21(self):
        self.assertEqual(int_to_snafu(31), '111')

    def test_int_to_snafu22(self):
        self.assertEqual(int_to_snafu(1257), '20012')

    def test_int_to_snafu23(self):
        self.assertEqual(int_to_snafu(32), '112')

    def test_int_to_snafu24(self):
        self.assertEqual(int_to_snafu(353), '1=-1=')

    def test_int_to_snafu25(self):
        self.assertEqual(int_to_snafu(107), '1-12')

    def test_int_to_snafu26(self):
        self.assertEqual(int_to_snafu(7), '12')

    def test_int_to_snafu27(self):
        self.assertEqual(int_to_snafu(3), '1=')

    def test_int_to_snafu28(self):
        self.assertEqual(int_to_snafu(37), '122')


def snafu_to_int(snafu):
    def digits():
        for i, c in enumerate(reversed(snafu)):
            match c:
                case '2':
                    yield i, 2
                case '1':
                    yield i, 1
                case '0':
                    yield i, 0
                case '-':
                    yield i, -1
                case '=':
                    yield i, -2
    return sum(d*5**i for i, d in digits())


def int_to_snafu(val):
    def snafus(val):
        while val > 1:
            if val % 5 <= 2:
                yield str(val % 5)
            else:
                if val % 5 == 3:
                    yield '='
                elif val % 5 == 4:
                    yield '-'
                else:
                    raise Exception(f'invalid val: {val}')
                val += 5
            val //= 5
        if val != 0:
            yield str(val)
    return ''.join(reversed(list(snafus(val))))


def parse(data):
    return data.split('\n')


def part1(snafus):
    s = sum(snafu_to_int(snafu) for snafu in snafus)
    return int_to_snafu(s)


def part2():
    pass


def main():
    data = get_data(year=2022, day=25)
    snafus = parse(data)
    answer1 = part1(snafus)
    print(answer1)
    answer2 = part2()
    print(answer2)


if __name__ == '__main__':
    main()
