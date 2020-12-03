from utils import timer


def partial_sums(iterable):
    total = 0
    for i in iterable:
        total += i
        yield total


def iterable_with_index(iterable):
    for i, val in enumerate(iterable):
        yield i, val


def convert(c):
    return 1 if c == '(' else -1


@timer
def solve_part1(values):
    return sum(values)


@timer
def solve_part2(values):
    ps = iterable_with_index(partial_sums(values))
    for i, val in ps:
        if val == -1:
            return i+1


def solve_day1(data):
    values = [convert(c) for c in data]
    part1 = solve_part1(values)
    part2 = solve_part2(values)

    return part1, part2


def main():
    with open("inputs/day1.txt") as f:
        data = f.readline().strip()

    print(solve_day1(data))


if __name__ == "__main__":
    main()
