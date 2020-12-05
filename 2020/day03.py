def part1(lines):
    count = 0
    for i, line in enumerate(lines):
        line = line.strip()
        if line[(i * 3) % len(line)] == '#':
            count += 1
    return count


def part2():
    pass


def main():
    with open('day03.txt') as lines:
        print(part1(lines))
    print(part2())


if __name__ == '__main__':
    main()
