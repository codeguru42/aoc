import itertools
import math


def part1():
    return solve(2)


def part2():
    return solve(3)


def solve(count):
    for expenses in itertools.combinations(read_expenses(), count):
        if sum(expenses) == 2020:
            return math.prod(expenses)


def read_expenses():
    with open('day01.txt') as file:
        for line in file:
            yield int(line.strip())


def main():
    print(part1())
    print(part2())


if __name__ == '__main__':
    main()
