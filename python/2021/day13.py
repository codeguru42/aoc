def parse_points(file):
    for line in file:
        if line == '\n':
            break
        x, y = line.strip().split(',')
        yield int(x), int(y)


def parse_instructions(file):
    for line in file:
        axis, value = line.strip().split()[2].split('=')
        yield axis, int(value)


def parse(file):
    return set(parse_points(file)), list(parse_instructions(file))


def fold(points, instruction):
    axis, value = instruction
    for x, y in points:
        if axis == 'x':
            if x < value:
                yield x, y
            else:
                yield 2*value - x, y
        elif axis == 'y':
            if y < value:
                yield x, y
            else:
                yield x, 2*value - y
        else:
            print('WHAT THE FUCK HAPPENED?')


def part1(points, instruction):
    new_points = set(fold(points, instruction))
    return len(new_points)


def part2(points, instructions):
    for instruction in instructions:
        points = set(fold(points, instruction))
    max_x = max(x for x, _ in points)
    max_y = max(y for _, y in points)
    grid = [[' '] * (max_x + 1) for _ in range(max_y + 1)]
    for x, y in points:
        grid[y][x] = '*'
    return '\n'.join(''.join(row) for row in grid)


def main():
    with open('day13.txt') as file:
        points, instructions = parse(file)
    print(part1(points, instructions[0]))
    print(part2(points, instructions))


if __name__ == '__main__':
    main()
