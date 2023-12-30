import math

def count_trees(lines, x_slope, y_slope):
    count = 0
    for i, line in enumerate(lines[::y_slope]):
        line = line.strip()
        if line[(i * x_slope) % len(line)] == '#':
            count += 1
    return count


def part1(lines):
    return count_trees(list(lines), 3, 1)


def part2(lines):
    slopes = [
        {'x_slope': 1, 'y_slope': 1},
        {'x_slope': 3, 'y_slope': 1},
        {'x_slope': 5, 'y_slope': 1},
        {'x_slope': 7, 'y_slope': 1},
        {'x_slope': 1, 'y_slope': 2},
    ]
    lines = list(lines)
    return math.prod(count_trees(lines, **slope) for slope in slopes)


def main():
    with open('day03.txt') as lines:
        print(part1(lines))
    with open('day03.txt') as lines:
        print(part2(lines))


if __name__ == '__main__':
    main()
