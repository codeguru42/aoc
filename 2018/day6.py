from math import atan2


def parse():
    with open('day6.txt') as file:
        return [(int(x), int(y)) for x, y in [line.split(',') for line in file]]


def ccw(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])


def angle_between(u, v):
    x = (v[0] - u[0], v[1] - u[1])
    return atan2(x[1], x[0])


def convex_hull(points):
    min_y = min(points, key=lambda p: p[1])
    points.sort(key=lambda p: angle_between(min_y, p))
    s = [points[0], points[1]]
    for p in points[2:]:
        while len(s) >= 2 and ccw(s[-2], s[-1], p) <= 0:
            s.pop()
        s.append(p)
    return s


def part1(points):
    hull = convex_hull(points)
    return hull


def part2(points):
    return points


def main():
    points = parse()
    print(part1(points))
    print(part2(points))


if __name__ == "__main__":
    main()
