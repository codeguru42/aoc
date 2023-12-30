import re
import numpy as np


def parse(line):
    inst_regex = r'(\D*)(\d*),(\d*) through (\d*),(\d*)'
    matches = re.fullmatch(inst_regex, line.strip())
    groups = matches.groups()
    return groups[0].strip(), (int(groups[1]), int(groups[2])), (int(groups[3]), int(groups[4]))


def part1():
    lights = np.array([[False] * 1000 for i in range(1000)])
    with open('day06.txt') as file:
        for line in file:
            inst, start, end = parse(line)
            startx, starty = start
            endx, endy = end
            if inst == 'turn on':
                lights[startx:endx+1, starty:endy+1] = True
            elif inst == 'turn off':
                lights[startx:endx+1, starty:endy+1] = False
            elif inst == 'toggle':
                lights[startx:endx+1, starty:endy+1] = np.logical_not(lights[startx:endx+1, starty:endy+1])
    return np.sum(np.sum(lights))


def part2():
    lights = np.array([[0] * 1000 for i in range(1000)])
    with open('day06.txt') as file:
        for line in file:
            inst, start, end = parse(line)
            startx, starty = start
            endx, endy = end
            if inst == 'turn on':
                lights[startx:endx+1, starty:endy+1] += 1
            elif inst == 'turn off':
                lights[startx:endx+1, starty:endy+1] -= 1
                lights[lights < 0] = 0
            elif inst == 'toggle':
                lights[startx:endx+1, starty:endy+1] += 2
    return np.sum(np.sum(lights))


def main():
    print(part1())
    print(part2())


if __name__ == '__main__':
    main()
