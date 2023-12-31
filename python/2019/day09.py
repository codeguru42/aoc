from int_code import run_program, parse


def part1(program):
    itr = run_program(program)
    next(itr)
    return itr.send(1)


def part2(program):
    itr = run_program(program)
    next(itr)
    return itr.send(2)


def main():
    with open("day09.txt") as file:
        int_codes = parse(file.readline())
        print(part1(int_codes))
        print(part2(int_codes))


if __name__ == "__main__":
    main()
