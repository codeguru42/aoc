def parse(file):
    for line in file:
        signal, output = line.strip().split(' | ')
        yield signal.split(), output.split()


def part1(data):
    count = 0
    for _, output in data:
        count += sum(1 for x in output if len(x) in [2, 3, 4, 7])
    return count


def part2():
    pass


def main():
    with open('day08.txt') as file:
        data = list(parse(file))
    print(part1(data))
    print(part2())


if __name__ == '__main__':
    main()
