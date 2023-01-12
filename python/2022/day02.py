from aocd import get_data

opponent_map = {
    'A': 'R',
    'B': 'P',
    'C': 'S',
}

player_map = {
    'X': 'R',
    'Y': 'P',
    'Z': 'S',
}

score_my_move = {
    'R': 1,
    'P': 2,
    'S': 3,
}

round_score = {
    'R': {
        'R': 3,
        'P': 0,
        'S': 6,
    },
    'P': {
        'R': 6,
        'P': 3,
        'S': 0,
    },
    'S': {
        'R': 0,
        'P': 6,
        'S': 3,
    },
}

move_map = {
    'X': {
        'R': 'S',
        'P': 'R',
        'S': 'P',
    },
    'Y': {
        'R': 'R',
        'P': 'P',
        'S': 'S',
    },
    'Z': {
        'R': 'P',
        'P': 'S',
        'S': 'R',
    },
}


def parse(data):
    return [line.split() for line in data.split('\n')]


def part1(moves):
    moves = [(opponent_map[you], player_map[me]) for you, me in moves]
    return sum(score_my_move[me] + round_score[me][you] for you, me in moves)


def part2(moves):
    moves = [(opponent_map[you], move_map[me][opponent_map[you]]) for you, me in moves]
    return sum(score_my_move[me] + round_score[me][you] for you, me in moves)


def main():
    data = get_data(year=2022, day=2)
    moves = parse(data)
    answer1 = part1(moves)
    print(answer1)
    answer2 = part2(moves)
    print(answer2)


if __name__ == '__main__':
    main()
