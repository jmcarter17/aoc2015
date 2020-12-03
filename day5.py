from utils import timer


def is_nice(string):
    num_vowels = 0
    for c in string:
        if c in 'aeiou':
            num_vowels += 1
        if num_vowels == 3:
            break

    if num_vowels < 3:
        return False

    bad = ['ab', 'cd', 'pq', 'xy']
    for comb in bad:
        if comb in string:
            return False

    if not any(x[0] == x[1] for x in zip(string, string[1:])):
        return False

    return True


def is_nice_2(string):
    ok = False
    pairs = list(zip(string, string[1:]))
    for i, pair in enumerate(pairs[:-2]):
        if pair in pairs[i+2:]:
            ok = True
            break

    if not ok:
        return False

    if not any(x[0] == x[1] for x in zip(string, string[2:])):
        return False

    return True


@timer
def solve_part1(data):
    return sum(is_nice(line) for line in data)


@timer
def solve_part2(data):
    return sum(is_nice_2(line) for line in data)


def solve_day5(data):
    part1 = solve_part1(data)
    part2 = solve_part2(data)

    return part1, part2


def main():
    with open("inputs/day5.txt") as f:
        data = [line.strip() for line in f]
    print(solve_day5(data))


if __name__ == "__main__":
    main()
