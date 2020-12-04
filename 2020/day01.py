import itertools
import math


def part1():
    for expenses in itertools.combinations(read_expenses(), 2):
        if sum(expenses) == 2020:
            return math.prod(expenses)


def part2():
    for expenses in itertools.combinations(read_expenses(), 3):
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
