from utils import timer
from itertools import groupby


def look_and_say(n):
    # return "".join(
    #     ("".join((f"{sum(1 for _ in group)}", label)) for label, group in groupby(n))
    # )
    # result = ""
    # for label, group in groupby(n):
    #     result += f"{len(list(group))}{label}"
    # return result

    c = n[0]
    current = 0
    result = ''
    for char in n:
        if char == c:
            current += 1
        else:
            result += f'{current}{c}'
            c = char
            current = 1
    result += f'{current}{c}'
    return result


@timer
def solve_part1(initial):
    n = initial
    for _ in range(40):
        n = look_and_say(n)

    return n


@timer
def solve_part2(initial):
    n = initial
    for _ in range(10):
        n = look_and_say(n)

    return n


def solve_day10(initial):
    part1 = solve_part1(initial)
    part2 = solve_part2(part1)

    return len(part1), len(part2)


def main():
    initial = "1113222113"

    print(solve_day10(initial))
    # result = look_and_say(initial)
    # print(result)


if __name__ == "__main__":
    main()
