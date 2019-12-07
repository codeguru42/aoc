def part1(program):
    return run_program(list(program))


def part2(program):
    pass


def digits(n):
    count = 0
    while n > 0 or count < 3:
        yield n % 10
        n //= 10
        count += 1


def parse_inst(memory, inst_ptr):
    inst = memory[inst_ptr:inst_ptr+4]
    opcode = inst[0] % 100
    if opcode == 1 or opcode == 2:
        args = [arg if mode == 1 else memory[arg] for arg, mode in zip(inst[1:], digits(inst[0] // 100))]
        # Last argument is an lvalue
        args[-1] = inst[-1]
    elif opcode == 3:
        args = [inst[1]]
    elif opcode == 4:
        mode = inst[0] // 100 % 10
        args = [inst[1] if mode else memory[inst[1]]]
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
            memory[args[0]] = int(user_input)
            jump = 2
        elif opcode == 4:
            print(args[0])
            jump = 2
        inst_ptr += jump
        opcode, args = parse_inst(memory, inst_ptr)


def main():
    with open('day05.txt') as file:
        int_codes = [int(x) for x in file.readline().split(',')]
        print(part1(int_codes))
        print(part2(int_codes))


if __name__ == '__main__':
    main()
