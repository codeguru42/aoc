def part1(program):
    memory = list(program)
    memory[1] = 12
    memory[2] = 2
    run_program(memory)
    return memory[0]


def part2(program, target):
    for noun in range(100):
        for verb in range(100):
            memory = list(program)
            memory[1] = noun
            memory[2] = verb
            run_program(memory)
            if memory[0] == target:
                return 100 * noun + verb


def run_program(memory):
    i = 0
    while memory[i] != 99:
        lhs = memory[i + 1]
        rhs = memory[i + 2]
        dest = memory[i + 3]
        if memory[i] == 1:
            memory[dest] = memory[lhs] + memory[rhs]
        elif memory[i] == 2:
            memory[dest] = memory[lhs] * memory[rhs]
        i += 4


def main():
    with open('day02.txt') as file:
        int_codes = [int(x) for x in file.readline().split(',')]
        print(part1(int_codes))
        print(part2(int_codes, 19690720))


if __name__ == '__main__':
    main()
