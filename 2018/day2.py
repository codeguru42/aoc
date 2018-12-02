from collections import Counter


def part1():
    with open('day2.txt') as file:
        counts = [Counter(line) for line in file]

        twos = 0
        threes = 0

        for c in counts:
            if any(c[x] == 2 for x in c):
                twos += 1
            if any(c[x] == 3 for x in c):
                threes += 1

        return twos * threes


def part2():
    pass


def main():
    print(part1())
    print(part2())


if __name__ == "__main__":
    main()
