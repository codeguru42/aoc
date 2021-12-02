def part1():
    with open('day02.txt') as file:
        x, y = 0, 0
        for line in file:
            ins = line.strip().split()
            if ins[0] == 'forward':
                x += int(ins[1])
            elif ins[0] == 'down':
                y += int(ins[1])
            elif ins[0] == 'up':
                y -= int(ins[1])
    return x * y


def part2():
    with open('day02.txt') as file:
        x, y, aim = 0, 0, 0
        for line in file:
            ins = line.strip().split()
            if ins[0] == 'forward':
                x += int(ins[1])
                y += aim * int(ins[1])
            elif ins[0] == 'down':
                aim += int(ins[1])
            elif ins[0] == 'up':
                aim -= int(ins[1])
    return x * y


def main():
    print(part1())
    print(part2())


if __name__ == '__main__':
    main()
