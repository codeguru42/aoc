import timeit

from aocd import get_data


def parse(data):
    lines = data.splitlines()
    for line in lines:
        d, n, c = line.split()
        yield d, int(n), c[1:-1]


def sum_dir(instructions, direction):
    return sum(n for d, n, _ in instructions if d == direction)


def calc_width(instructions):
    return sum_dir(instructions, "L") + sum_dir(instructions, "R")


def calc_height(instructions):
    return sum_dir(instructions, "U") + sum_dir(instructions, "D")


def calc_dimensions(instructions):
    return calc_width(instructions), calc_height(instructions)


def part1(instructions):
    trenches = make_trench(instructions)
    with open("out.txt", "w") as file:
        for line in trenches:
            file.write("".join(line))
            file.write("\n")


def make_trench(instructions):
    w, h = calc_dimensions(instructions)
    x, y = w // 2, h // 2
    x_min = x_max = x
    y_min = y_max = y
    trenches = [["."] * w for _ in range(h)]
    trenches[y][x] = "#"
    for d, n, c in instructions:
        for i in range(n):
            match d:
                case "U":
                    y -= 1
                case "D":
                    y += 1
                case "L":
                    x -= 1
                case "R":
                    x += 1
            trenches[y][x] = "#"
        x_min = min(x_min, x)
        x_max = max(x_max, x)
        y_min = min(y_min, y)
        y_max = max(y_max, y)
    return [t[x_min : x_max + 1] for t in trenches[y_min : y_max + 1]]


def part2(lines):
    pass


def main():
    data = get_data(year=2023, day=18)
    parsed = list(parse(data))
    print(part1(parsed))
    print(part2(parsed))
    print("Part 1:", timeit.timeit(lambda: part1(parsed), number=1))
    print("Part 2:", timeit.timeit(lambda: part2(parsed), number=1))


if __name__ == "__main__":
    main()
