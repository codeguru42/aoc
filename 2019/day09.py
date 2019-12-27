import unittest


class Day09Test(unittest.TestCase):
    def test_part1_a(self):
        program = [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]
        result = list(run_program(program))
        self.assertEqual(program, result)

    def test_part1_b(self):
        program = [1102, 34915192, 34915192, 7, 4, 7, 99, 0]
        expected = 34915192 * 34915192
        result = list(run_program(program))
        self.assertEqual([expected], result)

    def test_part1_c(self):
        program = [104, 1125899906842624, 99]
        expected = program[1]
        result = list(run_program(program))
        self.assertEqual([expected], result)


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


def parse_inst(memory, inst_ptr, rel_base):
    opcode = memory[inst_ptr] % 100
    modes = memory[inst_ptr] // 100
    if opcode in (1, 2, 7, 8):
        inst = memory[inst_ptr+1:inst_ptr+4]
        args = get_args(memory, opcode, inst, inst_ptr, modes, rel_base)
        # Last argument is an lvalue
        mode = modes // 100
        args[-1] = inst[-1] if mode == 0 else rel_base + inst[-1] if mode == 2 else None
    elif opcode == 3:
        inst = memory[inst_ptr+1:inst_ptr+2]
        mode = modes % 10
        args = [inst[0] if mode == 0 else rel_base + inst[0] if mode == 2 else None]
    elif opcode == 4:
        inst = memory[inst_ptr+1:inst_ptr+2]
        args = get_args(memory, opcode, inst, inst_ptr, modes, rel_base)
    elif opcode in (5, 6):
        inst = memory[inst_ptr+1:inst_ptr+3]
        args = get_args(memory, opcode, inst, inst_ptr, modes, rel_base)
    elif opcode == 9:
        inst = memory[inst_ptr+1:inst_ptr+2]
        args = get_args(memory, opcode, inst, inst_ptr, modes, rel_base)
    else:
        args = []
    return opcode, args


def get_args(memory, opcode, inst, inst_ptr, modes, rel_base):
    return [
        get_arg(memory, opcode, arg, inst_ptr, rel_base, mode)
        for arg, mode in zip(inst, digits(modes))
    ]


def get_arg(memory, opcode, arg, inst_ptr, rel_base, mode):
    if mode == 0:
        return memory[arg]
    elif mode == 1:
        return arg
    elif mode == 2:
        return memory[rel_base + arg]
    else:
        raise Exception(
            f'Invalid mode {mode} in instruction {opcode} at address {inst_ptr}')


def run_program(memory):
    inst_ptr = 0
    rel_base = 0
    opcode, args = parse_inst(memory, inst_ptr, rel_base)
    while opcode != 99:
        if opcode == 1:
            memory[args[2]] = args[0] + args[1]
            jump = 4
        elif opcode == 2:
            memory[args[2]] = args[0] * args[1]
            jump = 4
        elif opcode == 3:
            memory[args[0]] = yield
            jump = 2
        elif opcode == 4:
            yield args[0]
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
            memory[args[2]] = int(args[0] == args[1])
            jump = 4
        elif opcode == 9:
            rel_base += args[0]
            jump = 2
        else:
            raise Exception(f'Invalid opcode {opcode} at address {inst_ptr}')
        inst_ptr += jump
        opcode, args = parse_inst(memory, inst_ptr, rel_base)


def main():
    with open('day09.txt') as file:
        int_codes = [int(x) for x in file.readline().split(',')]
        part1(int_codes)
        part2(int_codes)


if __name__ == '__main__':
    main()
