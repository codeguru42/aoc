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
    with open('day2.txt') as file:
        ids = [line.strip() for line in file]

        for id1 in ids:
            for id2 in ids:
                d = distance(id1, id2)
                if d == 1:
                    return ''.join(x for x, y in zip(id1, id2) if x == y)


def distance(s, t):
    return sum(0 if x == y else 1 for x, y in zip(s, t))


def main():
    print(part1())
    print(part2())


if __name__ == "__main__":
    main()
