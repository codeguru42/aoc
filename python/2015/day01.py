import sys


def part1():
    file = sys.argv[1]
    floor = 0
    with open(file) as fp:
        for line in fp:
            for c in line:
                if c == '(':
                    floor += 1
                elif c == ')':
                    floor -= 1
    print(floor)


def part2():
    file = sys.argv[1]
    floor = 0
    pos = 1
    with open(file) as fp:
        for line in fp:
            for c in line:
                if c == '(':
                    floor += 1
                elif c == ')':
                    floor -= 1
                if floor < 0:
                    print(pos)
                    return
                pos += 1


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
