from aocd import get_data


def parse(data: str):
    for line in data.strip().split('\n'):
        yield line.split()


def part1():
    pass


def part2():
    pass


def main():
    data = get_data(year=2022, day=10)
    inst = list(parse(data))
    answer1 = part1()
    print(answer1)
    answer2 = part2()
    print(answer2)


if __name__ == '__main__':
    main()
