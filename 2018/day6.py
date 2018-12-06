from collections import Counter


def parse():
    with open('day6.txt') as file:
        return [(int(x), int(y)) for x, y in [line.split(',') for line in file]]


def ccw(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])


def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def min_distance(p, points):
    distances = [
        {
            'p': q,
            'd': manhattan_distance(q, p),
        }
        for q in points
    ]
    min_dist = min(distances, key=lambda a: a['d'])
    return [x for x in distances if x['d'] == min_dist['d']]


def part1(points):
    coords = list(zip(*points))
    min_x = min(coords[0])
    max_x = max(coords[0])
    min_y = min(coords[1])
    max_y = max(coords[1])

    infinite = set()
    for x in range(min_x, max_x + 1):
        for y in [min_y, max_y]:
            min_dist_points = min_distance((x, y), points)
            if len(min_dist_points) == 1:
                infinite.add(min_dist_points[0]['p'])
    for x in [min_x, max_x + 1]:
        for y in range(min_y, max_y):
            min_dist_points = min_distance((x, y), points)
            if len(min_dist_points) == 1:
                infinite.add(min_dist_points[0]['p'])

    areas = Counter()
    for x in range(min_x + 1, max_x):
        for y in range(min_y + 1, max_y):
            points_at_d = min_distance((x, y), points)
            if len(points_at_d) == 1:
                areas[points_at_d[0]['p']] += 1
    interior_areas = [areas[p] for p in points if p not in infinite]
    return max(interior_areas)


def part2(points):
    return points


def main():
    example = [(1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9), ]
    assert part1(example) == 17
    points = parse()
    print(part1(points))
    print(part2(points))


if __name__ == "__main__":
    main()
