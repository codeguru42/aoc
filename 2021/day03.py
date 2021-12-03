from collections import Counter


def part1():
    with open('day03.txt') as file:
        bits = zip(*[line.strip() for line in file])
        counts = [Counter(b) for b in bits]
        gamma = ''.join(c.most_common(1)[0][0] for c in counts)
        epsilon = ''.join('0' if c == '1' else '1' for c in gamma)
        return int(gamma, 2) * int(epsilon, 2)


def part2():
    pass


def main():
    print(part1())
    print(part2())


if __name__ == '__main__':
    main()
