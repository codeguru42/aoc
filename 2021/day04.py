class Bingo:
    def __init__(self, board):
        self.board = board

    def __repr__(self):
        return str(self.board)


def parse_bingo(file):
    for i in range(5):
        yield file.readline().split()


def parse_bingos(file):
    while file.readline():
        yield Bingo(list(parse_bingo(file)))


def parse(file):
    numbers = file.readline().split(',')
    bingo = list(parse_bingos(file))
    return numbers, bingo


def part1():
    pass


def part2():
    pass


def main():
    with open('day04.txt') as file:
        numbers, bingo = parse(file)

    print(numbers)
    print(bingo)
    print(part1())
    print(part2())


if __name__ == '__main__':
    main()
