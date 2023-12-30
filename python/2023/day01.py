import re

from aocd import get_data

part2_input = '''two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
'''


def test_part2_digits():
    parsed = parse(part2_input)
    numbers = list(digits2(parsed))
    expected = [29, 83, 13, 24, 42, 14, 76]
    assert numbers == expected


def test_part2():
    parsed = parse(part2_input)
    assert part2(parsed) == 281


def parse(data):
    return data.split()


def part1(lines):
    return sum(digits1(lines))


def digits1(lines):
    for line in lines:
        digits = [c for c in line if c.isdigit()]
        yield int(digits[0] + digits[-1])


def part2(lines):
    return sum(digits2(lines))


def digits2(lines):
    numbers = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
    }
    regex = re.compile(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))")
    for line in lines:
        match = regex.findall(line)
        yield 10 * numbers[match[0]] + numbers[match[-1]]


def main():
    data = get_data(year=2023, day=1)
    parsed = parse(data)
    print(part1(parsed))
    print(part2(parsed))


if __name__ == '__main__':
    main()
