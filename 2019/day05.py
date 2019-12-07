def part1(program):
    pass


def part2(program):
    pass


def digits(n):
    while n > 0:
        yield n % 10
        n //= 10


def parse_inst(memory, inst_ptr):
    inst = memory[inst_ptr:inst_ptr+4]
    opcode = inst[0] % 100
    args = [arg if mode == 1 else memory[arg] for arg, mode in zip(inst[1:], digits(opcode // 100))]
    return opcode, args


def run_program(memory):
    inst_ptr = 0
    opcode, args = parse_inst(memory, inst_ptr)
    while opcode != 99:
        if opcode == 1:
            memory[args[2]] = args[0] + args[1]
            jump = 4
        elif opcode == 2:
            memory[args[2]] = args[0] + args[1]
            jump = 4
        elif opcode == 3:
            user_input = input()
            memory[args[0]] = user_input
            jump = 2
        elif opcode == 4:
            print(memory[args[0]])
            jump = 2
        inst_ptr += jump


def main():
    with open('day05.txt') as file:
        int_codes = [int(x) for x in file.readline().split(',')]
        print(part1(int_codes))
        print(part2(int_codes))


if __name__ == '__main__':
    main()
