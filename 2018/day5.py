def read_input():
    with open('day5.txt') as file:
        return file.read()


def react(polymer):
    start = ''
    end = polymer

    while end != '':
        if start == '':
            start = end[0]
            end = end[1:]
        else:
            a = start[-1]
            b = end[0]
            if ((a.islower() and b.isupper())
                or (a.isupper() and b.islower())) \
                    and a.lower() == b.lower():
                start = start[:-1]
                end = end[1:]
            else:
                start = start + end[0]
                end = end[1:]
    return start


def part1(polymer):
    return len(react(polymer))


def part2(polymer):
    units = set(polymer.lower())
    m = len(polymer)
    for unit in units:
        replaced = polymer.replace(unit, '')
        replaced = replaced.replace(unit.upper(), '')
        reduced = react(replaced)
        if len(reduced) < m:
            m = len(reduced)
    return m


def main():
    assert part1('dabAcCaCBAcCcaDA') == 10
    polymer = read_input().strip()
    print(part1(polymer))
    assert part2('dabAcCaCBAcCcaDA') == 4
    print(part2(polymer))


if __name__ == "__main__":
    main()
