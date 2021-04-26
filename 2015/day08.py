def part1():
    text_sum = 0
    memory_sum = 0
    with open('day08.txt') as file:
        for line in file:
            text_sum += len(line.strip())
            memory_sum += len(eval(line.strip()))
    return text_sum - memory_sum


def part2():
    replace = {
        ord('"'): '\\"',
        ord('\\'): '\\\\'
    }
    text_sum = 0
    repr_sum = 0
    with open('day08.txt') as file:
        for line in file:
            text_sum += len(line.strip())
            repr_line = line.strip().translate(replace)
            repr_sum += len(repr_line) + 2
    return repr_sum - text_sum


def main():
    print(part1())
    print(part2())


if __name__ == '__main__':
    main()
