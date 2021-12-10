def is_corrupt(line):
    opens = '{([<'
    closes = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>',
    }
    s = []

    for c in line:
        if c in opens:
            s.append(c)
        else:
            d = s.pop()
            if c != closes[d]:
                return c


def corrupt_lines(file):
    for line in file:
        yield is_corrupt(line.strip())


def part1(file):
    score = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }
    return sum(score[c] for c in corrupt_lines(file) if c)


def part2():
    pass


def main():
    with open('day10.txt') as file:
        print(part1(file))
        print(part2())


if __name__ == '__main__':
    main()
