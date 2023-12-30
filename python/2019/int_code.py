from collections import defaultdict
from enum import IntEnum


class OpCode(IntEnum):
    ADD = 1
    MUL = 2
    IN = 3
    OUT = 4
    JT = 5
    JF = 6
    LT = 7
    EQ = 8
    ADD_BASE = 9
    HALT = 99


class ParamMode(IntEnum):
    POSITION_MODE = 0
    IMMEDIATE_MODE = 1
    RELATIVE_MODE = 2


def parse(data):
    return [int(x) for x in data.split(",")]


def digits(n):
    count = 0
    while n > 0 or count < 3:
        yield n % 10
        n //= 10
        count += 1


def parse_inst(memory, inst_ptr, rel_base):
    opcode = OpCode(memory[inst_ptr] % 100)
    modes = memory[inst_ptr] // 100
    if opcode in (OpCode.ADD, OpCode.MUL, OpCode.LT, OpCode.EQ):
        inst = list(memory[i] for i in range(inst_ptr + 1, inst_ptr + 4))
        args = get_args(memory, opcode, inst, inst_ptr, modes, rel_base)
        # Last argument is an lvalue
        mode = modes // 100
        args[-1] = inst[-1] if mode == 0 else rel_base + inst[-1] if mode == 2 else None
    elif opcode == OpCode.IN:
        inst = list(memory[i] for i in range(inst_ptr + 1, inst_ptr + 2))
        mode = modes % 10
        args = [inst[0] if mode == 0 else rel_base + inst[0] if mode == 2 else None]
    elif opcode == OpCode.OUT:
        inst = list(memory[i] for i in range(inst_ptr + 1, inst_ptr + 2))
        args = get_args(memory, opcode, inst, inst_ptr, modes, rel_base)
    elif opcode in (OpCode.JT, OpCode.JF):
        inst = list(memory[i] for i in range(inst_ptr + 1, inst_ptr + 3))
        args = get_args(memory, opcode, inst, inst_ptr, modes, rel_base)
    elif opcode == OpCode.ADD_BASE:
        inst = list(memory[i] for i in range(inst_ptr + 1, inst_ptr + 2))
        args = get_args(memory, opcode, inst, inst_ptr, modes, rel_base)
    else:
        args = []
    return opcode, args


def get_args(memory, opcode, inst, inst_ptr, modes, rel_base):
    return [
        get_arg(memory, opcode, arg, inst_ptr, rel_base, ParamMode(mode))
        for arg, mode in zip(inst, digits(modes))
    ]


def get_arg(memory, opcode, arg, inst_ptr, rel_base, mode):
    if mode == ParamMode.POSITION_MODE:
        return memory[arg]
    elif mode == ParamMode.IMMEDIATE_MODE:
        return arg
    elif mode == ParamMode.RELATIVE_MODE:
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
    inp = None
    while opcode != OpCode.HALT:
        if opcode == OpCode.ADD:
            memory[args[2]] = args[0] + args[1]
            jump = 4
        elif opcode == OpCode.MUL:
            memory[args[2]] = args[0] * args[1]
            jump = 4
        elif opcode == OpCode.IN:
            if inp is None:
                inp = yield
            memory[args[0]] = inp
            inp = None
            jump = 2
        elif opcode == OpCode.OUT:
            inp = yield args[0]
            jump = 2
        elif opcode == OpCode.JT:
            if args[0] != 0:
                inst_ptr = args[1]
                jump = 0
            else:
                jump = 3
        elif opcode == OpCode.JF:
            if args[0] == 0:
                inst_ptr = args[1]
                jump = 0
            else:
                jump = 3
        elif opcode == OpCode.LT:
            memory[args[2]] = int(args[0] < args[1])
            jump = 4
        elif opcode == OpCode.EQ:
            memory[args[2]] = int(args[0] == args[1])
            jump = 4
        elif opcode == OpCode.ADD_BASE:
            rel_base += args[0]
            jump = 2
        else:
            raise Exception(f"Invalid opcode {opcode} at address {inst_ptr}")
        inst_ptr += jump
        opcode, args = parse_inst(memory, inst_ptr, rel_base)
