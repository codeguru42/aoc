import unittest


class LookAndSayTest(unittest.TestCase):
    def test1(self):
        self.assertEqual('11', look_and_say('1'))

    def test2(self):
        self.assertEqual('21', look_and_say('11'))

    def test3(self):
        self.assertEqual('1211', look_and_say('21'))

    def test4(self):
        self.assertEqual('111221', look_and_say('1211'))

    def test5(self):
        self.assertEqual('312211', look_and_say('111221'))


def look_and_say(digits):
    previous = digits[0]
    count = 1
    result = ''
    for digit in digits[1:]:
        if digit == previous:
            count += 1
        else:
            result += str(count) + previous
            count = 1
        previous = digit
    result += str(count) + previous
    return result


def part1(start):
    result = start
    for i in range(40):
        result = look_and_say(result)
    return len(result)


def part2(start):
    result = start
    for i in range(50):
        result = look_and_say(result)
    return len(result)


def main():
    print(part1('3113322113'))
    print(part2('3113322113'))


if __name__ == '__main__':
    unittest.main(exit=False)
    main()
