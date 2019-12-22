import asyncio
import unittest
from itertools import permutations


class Day07Test(unittest.TestCase):
    def test_part1_a(self):
        expected_outp = 43210
        expected_phase = (4, 3, 2, 1, 0)
        expected = (expected_outp, expected_phase)
        program = [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0]
        result = part1(program, 0)
        self.assertEqual(expected, result)

    def test_part1_b(self):
        expected_outp = 54321
        expected_phase = (0, 1, 2, 3, 4)
        expected = (expected_outp, expected_phase)
        program = [3, 23, 3, 24, 1002, 24, 10, 24, 1002, 23, -1, 23, 101, 5, 23, 23, 1, 24, 23, 23, 4, 23, 99, 0, 0]
        result = part1(program, 0)
        self.assertEqual(expected, result)

    def test_part1_c(self):
        expected_outp = 65210
        expected_phase = (1, 0, 4, 3, 2)
        expected = (expected_outp, expected_phase)
        program = [3, 31, 3, 32, 1002, 32, 10, 32, 1001, 31, -2, 31, 1007, 31, 0, 33, 1002, 33, 7, 33, 1, 33, 31, 31, 1, 32, 31, 31, 4, 31, 99, 0, 0, 0]
        result = part1(program, 0)
        self.assertEqual(expected, result)


def part1(program, inp):
    loop = asyncio.get_event_loop()
    max_outp = 0
    max_phase = None
    phases = range(5)
    for phase in permutations(phases):
        amps = []
        inp_queue = asyncio.Queue()
        amps.append(loop.create_task(amp_input(inp, inp_queue)))
        outp_queue = asyncio.Queue()
        for p in phase:
            amps.append(run_program(list(program), p, inp_queue, outp_queue))
            outp_queue = inp_queue
            inp_queue = asyncio.Queue()
        amps.append(amp_output(outp_queue))

        task = asyncio.gather(*amps)
        thrust = loop.run_until_complete(task)
        print(thrust)
        if thrust > max_outp:
            max_outp = thrust
            max_phase = phase
    return max_outp, max_phase


def part2(program):
    # run_program(list(program))
    pass


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
    else:
        args = []
    return opcode, args


async def amp_input(inp, out_queue):
    await out_queue.put(inp)


async def amp_output(inp_queue):
    return await inp_queue.get()


async def run_program(memory, phase, inp, outp):
    await inp.put(phase)
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
            memory[args[0]] = await inp.get()
            jump = 2
        elif opcode == 4:
            await outp.put(args[0])
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
            memory[args[2]] = int(args[0] == args[1])
            jump = 4
        else:
            raise Exception(f'Invalid opcode {opcode} at address {inst_ptr}')
        inst_ptr += jump
        opcode, args = parse_inst(memory, inst_ptr)


def main():
    with open('day07.txt') as file:
        int_codes = [int(x) for x in file.readline().split(',')]
        print(part1(int_codes, 0))
        print(part2(int_codes))


if __name__ == '__main__':
    main()
