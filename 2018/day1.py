def part1():
    with open('day1.txt') as file:
        return sum(int(line) for line in file)


def main():
    print(part1())


if __name__ == "__main__":
    main()
