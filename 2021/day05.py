def parse(file):
    for line in file:
        points = line.split(' -> ')
        yield [[int(x) for x in point.split(',')] for point in points]


def part1(lines):
    grid = [[0] * 1000 for _ in range(1000)]
    for p1, p2 in lines:
        x1, y1 = p1
        x2, y2 = p2
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                grid[x1][y] += 1
        if y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                grid[x][y1] += 1
    return sum(sum(c > 1 for c in row) for row in grid)


def part2():
    pass


def main():
    with open('day05.txt') as file:
        lines = list(parse(file))
    print(part1(lines))
    print(part2())


if __name__ == '__main__':
    main()
