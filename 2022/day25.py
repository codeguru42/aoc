import unittest

from aocd import get_data


class TestPart1(unittest.TestCase):
    def test_snafu_to_dec1(self):
        self.assertEqual(snafu_to_int('1'), 1)

    def test_snafu_to_dec2(self):
        self.assertEqual(snafu_to_int('1'), 1)

    def test_snafu_to_dec3(self):
        self.assertEqual(snafu_to_int('2'), 2)

    def test_snafu_to_dec4(self):
        self.assertEqual(snafu_to_int('1='), 3)

    def test_snafu_to_dec5(self):
        self.assertEqual(snafu_to_int('1-'), 4)

    def test_snafu_to_dec6(self):
        self.assertEqual(snafu_to_int('10'), 5)

    def test_snafu_to_dec7(self):
        self.assertEqual(snafu_to_int('11'), 6)

    def test_snafu_to_dec8(self):
        self.assertEqual(snafu_to_int('12'), 7)

    def test_snafu_to_dec9(self):
        self.assertEqual(snafu_to_int('2='), 8)

    def test_snafu_to_dec10(self):
        self.assertEqual(snafu_to_int('2-'), 9)

    def test_snafu_to_dec11(self):
        self.assertEqual(snafu_to_int('20'), 10)

    def test_snafu_to_dec12(self):
        self.assertEqual(snafu_to_int('1=0'), 15)

    def test_snafu_to_dec13(self):
        self.assertEqual(snafu_to_int('1-0'), 20)

    def test_snafu_to_dec14(self):
        self.assertEqual(snafu_to_int('1=11-2'), 2022)

    def test_snafu_to_dec15(self):
        self.assertEqual(snafu_to_int('1-0---0'), 12345)

    def test_snafu_to_dec16(self):
        self.assertEqual(snafu_to_int('1121-1110-1=0'), 314159265)

    def test_snafu_to_dec17(self):
        self.assertEqual(snafu_to_int('1=-0-2'), 1747)

    def test_snafu_to_dec18(self):
        self.assertEqual(snafu_to_int('12111'), 906)

    def test_snafu_to_dec19(self):
        self.assertEqual(snafu_to_int('2=0='), 198)

    def test_snafu_to_dec20(self):
        self.assertEqual(snafu_to_int('21'), 11)

    def test_snafu_to_dec21(self):
        self.assertEqual(snafu_to_int('2=01'), 201)

    def test_snafu_to_dec22(self):
        self.assertEqual(snafu_to_int('111'), 31)

    def test_snafu_to_dec23(self):
        self.assertEqual(snafu_to_int('20012'), 1257)

    def test_snafu_to_dec24(self):
        self.assertEqual(snafu_to_int('112'), 32)

    def test_snafu_to_dec25(self):
        self.assertEqual(snafu_to_int('1=-1='), 353)

    def test_snafu_to_dec26(self):
        self.assertEqual(snafu_to_int('1-12'), 107)

    def test_snafu_to_dec27(self):
        self.assertEqual(snafu_to_int('12'), 7)

    def test_snafu_to_dec28(self):
        self.assertEqual(snafu_to_int('1='), 3)

    def test_snafu_to_dec29(self):
        self.assertEqual(snafu_to_int('122'), 37)


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


def parse(data):
    return data.split('\n')


def part1(snafus):
    return sum(snafu_to_int(snafu) for snafu in snafus)


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
