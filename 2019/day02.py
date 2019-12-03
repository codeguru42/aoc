def part1(int_codes):
    i = 0
    int_codes[1] = 12
    int_codes[2] = 2
    while int_codes[i] != 99:
        lhs = int_codes[i + 1]
        rhs = int_codes[i + 2]
        dest = int_codes[i + 3]
        if int_codes[i] == 1:
            int_codes[dest] = int_codes[lhs] + int_codes[rhs]
        elif int_codes[i] == 2:
            int_codes[dest] = int_codes[lhs] * int_codes[rhs]
        i += 4
    return int_codes[0]


def part2(int_codes):
    pass


def main():
    with open('day02.txt') as file:
        int_codes = [int(x) for x in file.readline().split(',')]
        print(part1(int_codes))
        print(part2(int_codes))


if __name__ == '__main__':
    main()
