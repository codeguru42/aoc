import ast

from aocd import get_data


def parse(data):
    for pair in data.strip().split('\n\n'):
        yield [ast.literal_eval(line) for line in pair.split('\n')]


def part1():
    pass


def part2():
    pass


def main():
    data = get_data(year=2022, day=13)
    packets = parse(data)
    print(list(packets))
    answer1 = part1()
    print(answer1)
    answer2 = part2()
    print(answer2)


if __name__ == '__main__':
    main()
