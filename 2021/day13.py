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
    new_points = set()
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


def part2():
    pass


def main():
    with open('day13.txt') as file:
        points, instructions = parse(file)
    print(part1(points, instructions[0]))
    print(part2())


if __name__ == '__main__':
    main()
