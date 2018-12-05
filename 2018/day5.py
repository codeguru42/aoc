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


def part2():
    pass


def main():
    assert part1('dabAcCaCBAcCcaDA') == 10
    polymer = read_input().strip()
    print(part1(polymer))
    print(part2())


if __name__ == "__main__":
    main()
