from aocd import get_data


def parse(data):
    return data.split()


def priority(item):
    p = ord(item.lower()) - ord('a') + 1
    if item.isupper():
        p += 26
    return p


def part1(sacks):
    total = 0
    for sack in sacks:
        n = len(sack)
        c1 = set(sack[:int(n/2)])
        c2 = set(sack[int(n/2):])
        both = c1 & c2
        for item in both:
            total += priority(item)
    return total


def part2():
    pass


def main():
    data = get_data(year=2022, day=3)
    supplies = parse(data)
    answer1 = part1(supplies)
    print(answer1)
    answer2 = part2()
    print(answer2)


if __name__ == '__main__':
    main()
