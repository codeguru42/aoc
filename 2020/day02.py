import collections


def part1(lines):
    valid_count = 0
    for line in lines:
        parts = line.split()
        min, max = parts[0].split('-')
        min = int(min)
        max = int(max)
        letter = parts[1][0]
        counts = collections.Counter(parts[2])
        if min <= counts[letter] <= max:
            valid_count += 1
    return valid_count


def part2():
    pass


def main():
    with open('day02.txt') as lines:
        print(part1(lines))
    print(part2())


if __name__ == '__main__':
    main()
