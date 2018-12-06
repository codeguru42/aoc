from collections import Counter
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


def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def part1(points):
    hull = convex_hull(points)
    interior = set(points) - set(hull)
    hull_coords = list(zip(*hull))
    min_x = min(hull_coords[0])
    max_x = max(hull_coords[0])
    min_y = min(hull_coords[1])
    max_y = max(hull_coords[1])
    print(min_x, min_y, max_x, max_y)

    areas = Counter()
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            distances = [
                {
                    'p': p,
                    'd': manhattan_distance(p, (x, y)),
                }
                for p in points
            ]
            min_dist = min(distances, key=lambda a: a['d'])
            points_at_d = [x['p'] for x in distances if x['d'] == min_dist['d']]
            if len(points_at_d) == 1:
                areas[min_dist['p']] += 1
    print('areas', areas)
    interior_areas = [areas[p] for p in interior]
    print('interior_areas', interior_areas)
    return max(interior_areas)


def part2(points):
    return points


def main():
    example = [(1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9), ]
    print(part1(example))
    # assert part1(example) == 17
    points = parse()
    print(part1(points))
    print(part2(points))


if __name__ == "__main__":
    main()
