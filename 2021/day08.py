def part1():
    with open('day08.txt') as file:
        count = 0
        for line in file:
            signal, output = line.strip().split(' | ')
            count += sum(1 for x in output.split() if len(x) in [2, 3, 4, 7])
        return count


def part2():
    pass


def main():
    print(part1())
    print(part2())


if __name__ == '__main__':
    main()
