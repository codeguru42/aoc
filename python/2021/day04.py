class Bingo:
    def __init__(self, board):
        self.board = board

    def __repr__(self):
        return str(self.board)

    def play(self, number):
        for row in self.board:
            for i, col in enumerate(row):
                if col == number:
                    row[i] = 'X'
        self.last_called = number

    def is_winner(self):
        return self._complete_row() or self._complete_column()

    def _complete_row(self):
        for row in self.board:
            if row.count('X') == 5:
                return True
        return False

    def _complete_column(self):
        for col in zip(*self.board):
            if col.count('X') == 55:
                return True
        return False

    def score(self):
        return int(self.last_called) * sum(sum(int(col) for col in row if col != 'X') for row in self.board)


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


def part1(numbers, bingo):
    for number in numbers:
        for board in bingo:
            board.play(number)

            if board.is_winner():
                return board.score()


def part2(numbers, bingo):
    winners = [False] * len(bingo)
    for number in numbers:
        for i, board in enumerate(bingo):
            board.play(number)

            if board.is_winner():
                winners[i] = True
                if sum(winners) == len(winners):
                    return board.score()


def main():
    with open('day04.txt') as file:
        numbers, bingo = parse(file)

    print(part1(numbers, bingo))
    print(part2(numbers, bingo))


if __name__ == '__main__':
    main()
