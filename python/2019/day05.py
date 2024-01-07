from int_code import parse, run_program


def part1(program, inp):
    machine = run_program(list(program))
    next(machine)
    outp = machine.send(inp)
    try:
        while True:
            outp = next(machine)
    finally:
        return outp


def part2(program, inp):
    machine = run_program(list(program))
    next(machine)
    outp = machine.send(inp)
    try:
        while True:
            outp = next(machine)
    finally:
        return outp


def main():
    with open("day05.txt") as file:
        int_codes = parse(file.readline())
        print(part1(int_codes, 1))
        print(part2(int_codes, 5))


if __name__ == "__main__":
    main()
