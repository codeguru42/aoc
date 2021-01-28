def parse():
    with open('day08.txt') as file:
        return [line.strip().split() for line in file]


def execute(instructions):
    prog_counter = 0
    acc = 0
    executed = [False] * len(instructions)
    while not executed[prog_counter] or prog_counter >= len(instructions):
        executed[prog_counter] = True
        inst = instructions[prog_counter]
        if inst[0] == 'acc':
            acc += int(inst[1])
            prog_counter += 1
        elif inst[0] == 'jmp':
            prog_counter += int(inst[1])
        elif inst[0] == 'nop':
            prog_counter += 1
    return acc, prog_counter


def part1(instructions):
    return execute(instructions)


def part2():
    pass


def main():
    instructions = parse()
    print(part1(instructions))
    print(part2())


if __name__ == '__main__':
    main()
