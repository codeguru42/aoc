import sys


def part1():
    filename = sys.argv[1]
    with open(filename) as file:
        for line in file:
            for c in line:
                print(c)


def part2():
    pass


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
