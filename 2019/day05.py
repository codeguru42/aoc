def part1(program):
    pass


def part2(program):
    pass


def run_program(memory):
    inst_ptr = 0
    opcode = memory[inst_ptr]
    while opcode != 99:
        lhs = memory[inst_ptr + 1]
        rhs = memory[inst_ptr + 2]
        dest = memory[inst_ptr + 3]
        if opcode == 1:
            memory[dest] = memory[lhs] + memory[rhs]
            jump = 4
        elif opcode == 2:
            memory[dest] = memory[lhs] * memory[rhs]
            jump = 4
        inst_ptr += jump


def main():
    with open('day05.txt') as file:
        int_codes = [int(x) for x in file.readline().split(',')]
        print(part1(int_codes))
        print(part2(int_codes))


if __name__ == '__main__':
    main()
