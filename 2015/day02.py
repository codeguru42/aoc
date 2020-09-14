import sys


def area(l, w):
    return l * w


def min_area(l, w, h):
    return min(area(x, y) for x, y in ((l, w), (l, h), (w, h)))


def perimeter(l, w):
    return 2*l + 2 * w


def min_perimeter(l, w, h):
    return min(perimeter(x, y) for x, y in ((l, w), (l, h), (w, h)))


def surface_area(l, w, h):
    return 2*l*w + 2*l*h + 2*w*h


def volume(l, w, h):
    return l*w*h


def total_wrapping_paper(lines):
    for line in lines:
        dims = [int(d) for d in line.split('x')]
        yield surface_area(*dims) + min_area(*dims)


def total_ribbon(lines):
    for line in lines:
        dims = [int(d) for d in line.split('x')]
        yield min_perimeter(*dims) + volume(*dims)


def part1():
    filename = sys.argv[1]
    with open(filename) as file:
        print(sum(total_wrapping_paper(file)))


def part2():
    filename = sys.argv[1]
    with open(filename) as file:
        print(sum(total_ribbon(file)))


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
