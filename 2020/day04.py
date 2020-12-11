import unittest


class Part1Test(unittest.TestCase):
    def test_example1(self):
        example1 = 'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\nbyr:1937 iyr:2017 cid:147 hgt:183cm'
        self.assertTrue(is_valid(parse(example1.split())))

    def test_example2(self):
        example2 = 'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884\nhcl:#cfa07d byr:1929'
        self.assertFalse(is_valid(parse(example2.split())))

    def test_example3(self):
        example3 = 'hcl:#ae17e1 iyr:2013\neyr:2024\necl:brn pid:760753108 byr:1931\nhgt:179cm'
        self.assertTrue(is_valid(parse(example3.split())))

    def test_example4(self):
        example4 = 'hcl:#cfa07d eyr:2025 pid:166559648\niyr:2011 ecl:brn hgt:59in'
        self.assertFalse(is_valid(parse(example4.split())))


def parse(passport_strings):
    return dict(
        kv.split(':')
        for kv in passport_strings
    )


def is_valid(passport):
    keys = {
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
    }
    return keys <= set(passport.keys())


def part1(file):
    valid = 0
    passport_strings = []
    for line in file:
        if line.strip():
            passport_strings.extend(line.strip().split())
        else:
            passport = parse(passport_strings)
            if is_valid(passport):
                valid += 1
            passport_strings = []
    return valid


def part2():
    pass


def main():
    with open('day04.txt') as file:
        print(part1(file))
    print(part2())


if __name__ == '__main__':
    unittest.main(exit=False)
    main()
