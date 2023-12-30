from collections import defaultdict


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
        inst = list(memory[i] for i in range(inst_ptr + 1, inst_ptr + 4))
        args = get_args(memory, opcode, inst, inst_ptr, modes, rel_base)
        # Last argument is an lvalue
        mode = modes // 100
        args[-1] = inst[-1] if mode == 0 else rel_base + inst[-1] if mode == 2 else None
    elif opcode == 3:
        inst = list(memory[i] for i in range(inst_ptr + 1, inst_ptr + 2))
        mode = modes % 10
        args = [inst[0] if mode == 0 else rel_base + inst[0] if mode == 2 else None]
    elif opcode == 4:
        inst = list(memory[i] for i in range(inst_ptr + 1, inst_ptr + 2))
        args = get_args(memory, opcode, inst, inst_ptr, modes, rel_base)
    elif opcode in (5, 6):
        inst = list(memory[i] for i in range(inst_ptr + 1, inst_ptr + 3))
        args = get_args(memory, opcode, inst, inst_ptr, modes, rel_base)
    elif opcode == 9:
        inst = list(memory[i] for i in range(inst_ptr + 1, inst_ptr + 2))
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
            f"Invalid mode {mode} in instruction {opcode} at address {inst_ptr}"
        )


def run_program(program):
    memory = defaultdict(lambda: 0, enumerate(program))
    inst_ptr = 0
    rel_base = 0
    opcode, args = parse_inst(memory, inst_ptr, rel_base)
    inp = yield
    while opcode != 99:
        if opcode == 1:
            memory[args[2]] = args[0] + args[1]
            jump = 4
        elif opcode == 2:
            memory[args[2]] = args[0] * args[1]
            jump = 4
        elif opcode == 3:
            memory[args[0]] = inp
            print(f"Input: {memory[args[0]]}")
            jump = 2
        elif opcode == 4:
            print(f"Output: {args[0]}")
            inp = yield args[0]
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
            raise Exception(f"Invalid opcode {opcode} at address {inst_ptr}")
        inst_ptr += jump
        opcode, args = parse_inst(memory, inst_ptr, rel_base)
