from utils import timer


def update_coords(c, i, j):
    if c == ">":
        i += 1
    elif c == "<":
        i -= 1
    elif c == '^':
        j += 1
    elif c == 'v':
        j -= 1
    return i, j


@timer
def solve_part1(data):
    houses = set()
    i, j = 0, 0
    houses.add((i, j))
    for c in data:
        i, j = update_coords(c, i, j)
        houses.add((i, j))
    return len(houses)


@timer
def solve_part2(data):
    houses = set()
    si, sj = 0, 0
    ri, rj = 0, 0
    houses.add((si, sj))
    houses.add((ri, rj))
    for i, c in enumerate(data):
        if i % 2 == 0:
            si, sj = update_coords(c, si, sj)
            houses.add((si, sj))
        else:
            ri, rj = update_coords(c, ri, rj)
            houses.add((ri, rj))
    return len(houses)


def solve_day3(data):
    part1 = solve_part1(data)
    part2 = solve_part2(data)

    return part1, part2


def main():
    with open("inputs/day3.txt") as f:
        data = f.read().strip()

    print(solve_day3(data))


if __name__ == "__main__":
    main()
