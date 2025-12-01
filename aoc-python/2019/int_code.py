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
    args = []
    match opcode:
        case OpCode.ADD | OpCode.MUL | OpCode.LT | OpCode.EQ:
            inst = list(memory[i] for i in range(inst_ptr + 1, inst_ptr + 4))
            args = get_args(memory, inst, modes, rel_base)
            # Last argument is an lvalue
            mode = ParamMode(modes // 100)
            args[-1] = (
                inst[-1]
                if mode == ParamMode.POSITION_MODE
                else rel_base + inst[-1]
                if mode == ParamMode.RELATIVE_MODE
                else None
            )
        case OpCode.IN:
            inst = list(memory[i] for i in range(inst_ptr + 1, inst_ptr + 2))
            mode = modes % 10
            args = [
                inst[0]
                if mode == ParamMode.POSITION_MODE
                else rel_base + inst[0]
                if mode == ParamMode.RELATIVE_MODE
                else None
            ]
        case OpCode.OUT:
            inst = list(memory[i] for i in range(inst_ptr + 1, inst_ptr + 2))
            args = get_args(memory, inst, modes, rel_base)
        case OpCode.JT | OpCode.JF:
            inst = list(memory[i] for i in range(inst_ptr + 1, inst_ptr + 3))
            args = get_args(memory, inst, modes, rel_base)
        case OpCode.ADD_BASE:
            inst = list(memory[i] for i in range(inst_ptr + 1, inst_ptr + 2))
            args = get_args(memory, inst, modes, rel_base)
    return opcode, args


def get_args(memory, inst, modes, rel_base):
    return [
        get_arg(memory, arg, rel_base, ParamMode(mode))
        for arg, mode in zip(inst, digits(modes))
    ]


def get_arg(memory, arg, rel_base, mode):
    match mode:
        case ParamMode.POSITION_MODE:
            return memory[arg]
        case ParamMode.IMMEDIATE_MODE:
            return arg
        case ParamMode.RELATIVE_MODE:
            return memory[rel_base + arg]


def run_program(program):
    memory = defaultdict(lambda: 0, enumerate(program))
    inst_ptr = 0
    rel_base = 0
    opcode, args = parse_inst(memory, inst_ptr, rel_base)
    inp = None
    while opcode != OpCode.HALT:
        match opcode:
            case OpCode.ADD:
                memory[args[2]] = args[0] + args[1]
                jump = 4
            case OpCode.MUL:
                memory[args[2]] = args[0] * args[1]
                jump = 4
            case OpCode.IN:
                if inp is None:
                    inp = yield
                memory[args[0]] = inp
                inp = None
                jump = 2
            case OpCode.OUT:
                inp = yield args[0]
                jump = 2
            case OpCode.JT:
                if args[0] != 0:
                    inst_ptr = args[1]
                    jump = 0
                else:
                    jump = 3
            case OpCode.JF:
                if args[0] == 0:
                    inst_ptr = args[1]
                    jump = 0
                else:
                    jump = 3
            case OpCode.LT:
                memory[args[2]] = int(args[0] < args[1])
                jump = 4
            case OpCode.EQ:
                memory[args[2]] = int(args[0] == args[1])
                jump = 4
            case OpCode.ADD_BASE:
                rel_base += args[0]
                jump = 2
        inst_ptr += jump
        opcode, args = parse_inst(memory, inst_ptr, rel_base)
