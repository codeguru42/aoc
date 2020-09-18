import re


def parse(line):
    inst_regex = r'(\D*)(\d*),(\d*) through (\d*),(\d*)'
    matches = re.fullmatch(inst_regex, line.strip())
    groups = matches.groups()
    return groups[0].strip(), (int(groups[1]), int(groups[2])), (int(groups[3]), int(groups[4]))


def turn_on(lights, start, end):
    startx, starty = start
    endx, endy = end
    for i in range(startx, endx+1):
        for j in range(starty, endy+1):
            lights[i][j] = True


def turn_off(lights, start, end):
    startx, starty = start
    endx, endy = end
    for i in range(startx, endx+1):
        for j in range(starty, endy+1):
            lights[i][j] = False


def toggle(lights, start, end):
    startx, starty = start
    endx, endy = end
    for i in range(startx, endx+1):
        for j in range(starty, endy+1):
            lights[i][j] = not lights[i][j]


def part1():
    lights = [[False] * 1000 for i in range(1000)]
    with open('day06.txt') as file:
        for line in file:
            inst, start, end = parse(line)
            if inst == 'turn on':
                turn_on(lights, start, end)
            elif inst == 'turn off':
                turn_off(lights, start, end)
            elif inst == 'toggle':
                toggle(lights, start, end)
    return sum(sum(row) for row in lights)


def turn_on2(lights, start, end):
    startx, starty = start
    endx, endy = end
    for i in range(startx, endx+1):
        for j in range(starty, endy+1):
            lights[i][j] += 1


def turn_off2(lights, start, end):
    startx, starty = start
    endx, endy = end
    for i in range(startx, endx+1):
        for j in range(starty, endy+1):
            lights[i][j] -= 1
            if lights[i][j] < 0:
                lights[i][j] = 0


def toggle2(lights, start, end):
    startx, starty = start
    endx, endy = end
    for i in range(startx, endx+1):
        for j in range(starty, endy+1):
            lights[i][j] += 2


def part2():
    lights = [[0] * 1000 for i in range(1000)]
    with open('day06.txt') as file:
        for line in file:
            inst, start, end = parse(line)
            if inst == 'turn on':
                turn_on2(lights, start, end)
            elif inst == 'turn off':
                turn_off2(lights, start, end)
            elif inst == 'toggle':
                toggle2(lights, start, end)
    return sum(sum(row) for row in lights)


def main():
    print(part1())
    print(part2())


if __name__ == '__main__':
    main()
