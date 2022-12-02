from aocd import get_data, submit

score_my_move = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

round_score = {
    'X': {
        'A': 3,
        'B': 0,
        'C': 6,
    },
    'Y': {
        'A': 6,
        'B': 3,
        'C': 0,
    },
    'Z': {
        'A': 0,
        'B': 6,
        'C': 3,
    },
}


def parse(data):
    return [line.split() for line in data.split('\n')]


def part1(moves):
    return sum(score_my_move[me] + round_score[me][you] for you, me in moves)


def part2():
    pass


def main():
    data = get_data(year=2022, day=2)
    moves = parse(data)
    answer1 = part1(moves)
    print(answer1)
    answer2 = part2()
    print(answer2)


if __name__ == '__main__':
    main()
