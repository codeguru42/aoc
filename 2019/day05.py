def part1(program):
    run_program(list(program))


def part2(program):
    run_program(list(program))


def digits(n):
    count = 0
    while n > 0 or count < 3:
        yield n % 10
        n //= 10
        count += 1


def parse_inst(memory, inst_ptr):
    opcode = memory[inst_ptr] % 100
    modes = memory[inst_ptr] // 100
    if opcode in (1, 2, 7, 8):
        inst = memory[inst_ptr+1:inst_ptr+4]
        args = [arg if mode == 1 else memory[arg] for arg, mode in zip(inst, digits(modes))]
        # Last argument is an lvalue
        args[-1] = inst[-1]
    elif opcode == 3:
        inst = memory[inst_ptr+1:inst_ptr+2]
        args = [inst[0]]
    elif opcode == 4:
        mode = modes % 10
        inst = memory[inst_ptr+1:inst_ptr+2]
        args = [inst[0] if mode else memory[inst[0]]]
    elif opcode in (5, 6):
        inst = memory[inst_ptr+1:inst_ptr+3]
        args = [arg if mode == 1 else memory[arg] for arg, mode in zip(inst, digits(modes))]
        # Last argument is an lvalue
        args[-1] = inst[-1]
    else:
        args = []
    return opcode, args


def run_program(memory):
    inst_ptr = 0
    opcode, args = parse_inst(memory, inst_ptr)
    while opcode != 99:
        if opcode == 1:
            memory[args[2]] = args[0] + args[1]
            jump = 4
        elif opcode == 2:
            memory[args[2]] = args[0] * args[1]
            jump = 4
        elif opcode == 3:
            user_input = input('Enter a value: ')
            memory[args[0]] = int(user_input)
            jump = 2
        elif opcode == 4:
            print(args[0])
            jump = 2
        elif opcode == 5:
            if args[0] != 0:
                inst_ptr = args[1]
                jump = 0
            else:
                jump = 3
        elif opcode == 6:
            if args[0] == 0:
                inst_ptr = args[1]
                jump = 0
            else:
                jump = 3
        elif opcode == 7:
            memory[args[2]] = int(args[0] < args[1])
            jump = 4
        elif opcode == 8:
            memory[args[2]] = int(args[0] > args[1])
            jump = 4
        inst_ptr += jump
        opcode, args = parse_inst(memory, inst_ptr)


def main():
    with open('day05.txt') as file:
        int_codes = [int(x) for x in file.readline().split(',')]
        part1(int_codes)
        part2(int_codes)


if __name__ == '__main__':
    main()
