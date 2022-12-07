from aocd import get_data


def parse(data):
    lines = iter(data.split('\n'))
    fs = {}
    build_fs(lines, fs, fs)
    return fs


def populate_dir(current_dir, commands):
    file_spec = next(commands, None)
    while file_spec is not None and not file_spec.startswith('$'):
        size, name = file_spec.split()
        if size == 'dir':
            current_dir[name] = {'..': current_dir}
        else:
            current_dir[name] = int(size)
        file_spec = next(commands, None)
    return file_spec


def build_fs(commands, root_dir, current_dir):
    command = next(commands, None)
    while command is not None:
        parts = command.split()
        if parts[1] == 'ls':
            command = populate_dir(current_dir, commands)
        elif parts[1] == 'cd':
            if parts[2] == '/':
                build_fs(commands, root_dir, root_dir)
            else:
                build_fs(commands, root_dir, current_dir[parts[2]])
            command = next(commands, None)
        else:
            print("Invalid command:", parts[1])
            command = next(commands, None)


def sum_dirs(fs):
    sizes = {}
    sum = 0
    for name, value in fs.items():
        if name == '..':
            pass
        elif type(value) == dict:
            sizes[name] = sum_dirs(value)
            sum += sizes[name][0]
        else:
            sum += value
    return sum, sizes


def sum_smalls(sizes):
    sum = 0
    for name, value in sizes.items():
        if name == '..':
            pass
        else:
            size, sub_dir = value
            sum += sum_smalls(sub_dir)
            if size < 100000:
                sum += size
    return sum


def part1(fs):
    total, sizes = sum_dirs(fs)
    return sum_smalls(sizes)


def part2():
    pass

def main():
    data = get_data(year=2022, day=7)
    fs = parse(data)
    answer1 = part1(fs)
    print(answer1)
    answer2 = part2()
    print(answer2)


if __name__ == '__main__':
    main()
