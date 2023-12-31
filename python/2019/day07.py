from itertools import permutations

from int_code import run_program, parse


def part1(program, inp):
    max_outp = 0
    max_phase = None
    phases = range(5)
    for phase in permutations(phases):
        amps = [(run_program(list(program)), p) for p in phase]
        outp = inp
        for amp, p in amps:
            inp_list = [p, outp]
            outp = next(amp)
            for i in inp_list:
                outp = amp.send(i)
        if outp > max_outp:
            max_outp = outp
            max_phase = phase
    return max_outp, max_phase


def part2(program, inp):
    max_outp = 0
    max_phase = None
    phases = range(5, 10)
    for phase in permutations(phases):
        amps = []
        for i, p in enumerate(phase):
            amp = run_program(program)
            next(amp)
            amp.send(p)
            amps.append(amp)
        stop_count = 0
        inp = 0
        while True:
            for i, amp in enumerate(amps):
                try:
                    inp = amp.send(inp)
                except StopIteration:
                    stop_count += 1
            if stop_count == 5:
                break
        if inp > max_outp:
            max_outp = inp
            max_phase = phase
    return max_outp, max_phase


def main():
    with open("day07.txt") as file:
        int_codes = parse(file.readline())
        print(part1(int_codes, 0))
        print(part2(int_codes, 0))


if __name__ == "__main__":
    main()
