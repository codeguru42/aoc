def main():
    with open('day1.txt') as file:
        print(sum(int(line) for line in file))


if __name__ == "__main__":
    main()
