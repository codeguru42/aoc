def count_trees(lines, x_slope, y_slope):
    count = 0
    for i, line in enumerate(lines[::y_slope]):
        line = line.strip()
        if line[(i * x_slope) % len(line)] == '#':
            count += 1
    return count


def part1(lines):
    return count_trees(list(lines), 3, 1)


def part2():
    pass


def main():
    with open('day03.txt') as lines:
        print(part1(lines))
    print(part2())


if __name__ == '__main__':
    main()
