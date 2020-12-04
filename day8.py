from utils import timer


def process_line(ln):
    length = len(ln)
    chars = list(ln)
    i = 1
    count = 0
    while i < length-1:
        count += 1
        if chars[i] == "\\":
            if chars[i + 1] == "x":
                i += 4
            else:
                i += 2
        else:
            i += 1
    return length, count


@timer
def solve_part1(data):
    return sum(x[0] - x[1] for x in data)


@timer
def solve_part2(data):
    pass


def solve_day8(data):
    part1 = solve_part1(data)
    part2 = solve_part2(data)

    return part1, part2


def main():
    with open("inputs/day8.txt") as f:
        data = [process_line(line.strip()) for line in f]

    print(solve_day8(data))


if __name__ == "__main__":
    main()
