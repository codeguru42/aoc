import re


def parse(line):
    inst_regex = r'(\D*)(\d*),(\d*) through (\d*),(\d*)'
    matches = re.fullmatch(inst_regex, line.strip())
    groups = matches.groups()
    return groups[0], (int(groups[1]), int(groups[2])), (int(groups[3]), int(groups[4]))


def part1():
    lights = [[False] * 1000 for i in range(1000)]
    with open('day06.txt') as file:
        for line in file:
            inst, start, end = parse(line)
            print(inst, start, end)


def part2():
    pass


def main():
    print(part1())
    print(part2())


if __name__ == '__main__':
    main()
