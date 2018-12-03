def parse():
    claims = []
    with open('day3.txt') as file:
        for line in file:
            tokens = line.split()
            claims.append({
                'id': tokens[0][1:],
                'loc': [int(x) for x in tokens[2][:-1].split(',')],
                'size': [int(x) for x in tokens[3].split('x')],
            })
    return claims


def part1():
    claims = parse()
    overlap = set()
    used = set()
    for claim in claims:
        left, top = claim['loc']
        width, height = claim['size']
        for x in range(left, left + width):
            for y in range(top, top + height):
                if (x, y) in used:
                    overlap.add((x, y))
                else:
                    used.add((x, y))
    return len(overlap)


def part2():
    claims = parse()
    overlap = {}
    for claim in claims:
        left, top = claim['loc']
        width, height = claim['size']
        for x in range(left, left + width):
            for y in range(top, top + height):
                o = overlap.get((x, y), set())
                o.add(claim['id'])
                overlap[(x, y)] = o
    all_ids = set(claim['id'] for claim in claims)
    overlap_ids = set()
    for loc in overlap:
        if len(overlap[loc]) > 1:
            overlap_ids |= overlap[loc]
    return all_ids - overlap_ids


def main():
    print(part1())
    print(part2())


if __name__ == "__main__":
    main()
